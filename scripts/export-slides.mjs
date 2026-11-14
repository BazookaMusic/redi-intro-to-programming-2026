import { cp, mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises'
import { spawn } from 'node:child_process'
import { availableParallelism } from 'node:os'
import path from 'node:path'
import { pathToFileURL } from 'node:url'
import { load } from '@slidev/parser/fs'
import { PDFDocument } from 'pdf-lib'
import { chromium } from 'playwright-chromium'
import { createNoSolutionsWorkspace, removeNoSolutionsWorkspace } from './generate-no-solutions.mjs'

const slidevCli = path.resolve('node_modules/@slidev/cli/bin/slidev.mjs')
const imageMimeTypes = new Map([
	['.gif', 'image/gif'],
	['.jpeg', 'image/jpeg'],
	['.jpg', 'image/jpeg'],
	['.png', 'image/png'],
	['.svg', 'image/svg+xml'],
	['.webp', 'image/webp'],
])

const concurrency = Number(process.env.SLIDES_EXPORT_CONCURRENCY)
	|| Math.max(1, Math.min(8, Math.floor(availableParallelism() / 2)))

// Output is buffered so logs from parallel jobs do not interleave.
function runSlidev(arguments_, log) {
	return new Promise((resolve, reject) => {
		const process_ = spawn(process.execPath, [slidevCli, ...arguments_], { stdio: ['ignore', 'pipe', 'pipe'] })

		process_.stdout.on('data', chunk => log.push(chunk.toString()))
		process_.stderr.on('data', chunk => log.push(chunk.toString()))
		process_.on('error', reject)
		process_.on('exit', (code) => {
			if (code === 0)
				resolve()
			else
				reject(new Error(`Slidev ${arguments_[0]} failed with exit code ${code}`))
		})
	})
}

async function runPool(jobs, limit) {
	const failures = []
	let next = 0

	async function worker() {
		while (next < jobs.length) {
			const job = jobs[next++]

			try {
				await job()
			}
			catch (error) {
				failures.push(error)
			}
		}
	}

	await Promise.all(Array.from({ length: Math.min(limit, jobs.length) }, worker))

	if (failures.length > 0)
		throw new AggregateError(failures, `${failures.length} slide export job(s) failed`)
}

async function listFiles(directory) {
	const files = []

	for (const entry of await readdir(directory, { withFileTypes: true })) {
		const entryPath = path.join(directory, entry.name)

		if (entry.isDirectory())
			files.push(...await listFiles(entryPath))
		else
			files.push(entryPath)
	}

	return files
}

async function createStandaloneHtml(buildDirectory, outputPath) {
	let html = await readFile(path.join(buildDirectory, 'index.html'), 'utf8')

	html = html
		.replace(/<link rel="preload" as="image" href="\.\/images\/[^"]+">\n?/g, '')
		.replace(/<link rel="icon" href="https?:\/\/[^">]+">\n?/g, '')

	for (const imagePath of await listFiles(path.join(buildDirectory, 'images'))) {
		const extension = path.extname(imagePath).toLowerCase()
		const mimeType = imageMimeTypes.get(extension)

		if (!mimeType)
			throw new Error(`Unsupported image type in HTML build: ${imagePath}`)

		const relativePath = path.relative(buildDirectory, imagePath).split(path.sep).join('/')
		const dataUrl = `data:${mimeType};base64,${(await readFile(imagePath)).toString('base64')}`

		for (const reference of [`./${relativePath}`, `/${relativePath}`, relativePath])
			html = html.replaceAll(reference, dataUrl)

		if (html.includes(relativePath))
			throw new Error(`Standalone HTML still references ${relativePath}: ${outputPath}`)
	}

	html = html.replace(/[ \t]+$/gm, '')
	await writeFile(outputPath, html)
}

function parseAspectRatio(value) {
	if (typeof value === 'number')
		return value

	const [width, height] = String(value).split(/[/:x]/).map(Number)

	return width / height
}

// Matches the page size and metadata that `slidev export` produces.
async function readPdfSettings(inputPath) {
	const { headmatter, slides } = await load(path.dirname(inputPath), inputPath)
	const width = Number(headmatter.canvasWidth ?? 980)
	const height = Math.round(width / parseAspectRatio(headmatter.aspectRatio ?? 16 / 9))

	return { width, height, title: slides[0]?.title, subject: slides[0]?.frontmatter?.info }
}

// Prints the built deck's /print route, which src/slides/vite.config.mjs keeps in the build.
// This avoids starting a Slidev dev server per PDF.
async function printPdf(browser, buildDirectory, inputPath, outputPath) {
	const { width, height, title, subject } = await readPdfSettings(inputPath)
	const context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: 2 })

	try {
		const page = await context.newPage()
		const url = `${pathToFileURL(path.join(buildDirectory, 'index.html'))}?print=true#/print`

		await page.emulateMedia({ colorScheme: 'light', media: 'screen' })
		await page.goto(url, { waitUntil: 'networkidle', timeout: 60_000 })

		const slides = page.locator('.print-slide-container')

		await slides.first().waitFor({ timeout: 60_000 })
		await page.setViewportSize({ width, height: height * await slides.count() })

		// Mermaid renders asynchronously into a shadow root; a failed diagram renders a <pre> instead.
		await page.waitForFunction(() =>
			document.querySelector('.slidev-slide-loading') === null
			&& [...document.querySelectorAll('.mermaid')].every(element => element.shadowRoot?.querySelector('svg'))
			&& [...document.images].every(image => image.complete), null, { timeout: 60_000 })
		await page.evaluate(async () => {
			await document.fonts.ready
			document.getElementById('mermaid-rendering-container')?.style.setProperty('display', 'none')
			await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))
		})

		const pdf = await PDFDocument.load(await page.pdf({
			width,
			height,
			margin: { top: 0, right: 0, bottom: 0, left: 0 },
			printBackground: true,
			preferCSSPageSize: true,
		}))

		if (title)
			pdf.setTitle(title)
		if (subject)
			pdf.setSubject(subject)

		await writeFile(outputPath, await pdf.save())
	}
	finally {
		await context.close()
	}
}

// Slidev rewrites shared files under <deck folder>/node_modules/.slidev during a build, so parallel
// builds from one folder can read each other's half-written files. Each build gets its own copy.
// The copy sits two levels below the workspace so `theme: ../../themes/...` still resolves.
async function createBuildRoot(inputPath, buildRoot) {
	const sourceDirectory = path.dirname(inputPath)

	await mkdir(buildRoot, { recursive: true })

	for (const entry of await readdir(sourceDirectory, { withFileTypes: true })) {
		if (entry.name !== 'node_modules' && !entry.name.endsWith('.md'))
			await cp(path.join(sourceDirectory, entry.name), path.join(buildRoot, entry.name), { recursive: true })
	}

	const deckPath = path.join(buildRoot, path.basename(inputPath))

	await cp(inputPath, deckPath)
	return deckPath
}

async function exportDeck(browser, inputPath, outputDirectory, buildRoot) {
	const deckName = path.basename(inputPath, '.md')
	const label = `${path.basename(outputDirectory)}/${deckName}`
	const pdfOutputPath = path.join(outputDirectory, `${deckName}.pdf`)
	const htmlOutputPath = path.join(outputDirectory, `${deckName}.html`)
	const htmlBuildPath = path.join(buildRoot, 'dist')
	const log = []
	const startTime = Date.now()

	console.log(`Started ${label}`)

	try {
		const deckPath = await createBuildRoot(inputPath, buildRoot)

		await runSlidev([
			'build',
			deckPath,
			'--out',
			htmlBuildPath,
			'--base',
			'./',
			'--router-mode',
			'hash',
		], log)
		await createStandaloneHtml(htmlBuildPath, htmlOutputPath)
		await printPdf(browser, htmlBuildPath, deckPath, pdfOutputPath)
	}
	catch (error) {
		console.error(`Failed ${label}:\n${log.join('')}`)
		throw new Error(`${label}: ${error.message}`)
	}
	finally {
		await rm(buildRoot, { recursive: true, force: true })
	}

	console.log(`Finished ${label} in ${((Date.now() - startTime) / 1000).toFixed(1)}s`)
}

const workspace = await createNoSolutionsWorkspace()
const browser = await chromium.launch()

try {
	const variants = [
		{ source: path.resolve('src/slides'), output: path.resolve('slides_solutions') },
		{ source: workspace.slidesDirectory, output: path.resolve('slides_no_solutions') },
	]
	const jobs = []

	for (const variant of variants) {
		const entries = await readdir(variant.source, { withFileTypes: true })
		const decks = entries
			.filter(entry => entry.isFile() && entry.name.endsWith('.md'))
			.map(entry => entry.name)
			.sort()

		if (decks.length === 0)
			throw new Error(`No Slidev decks found in ${variant.source}`)

		await rm(variant.output, { recursive: true, force: true })
		await mkdir(variant.output, { recursive: true })

		for (const deck of decks) {
			const inputPath = path.join(variant.source, deck)
			const buildRoot = path.join(workspace.rootDirectory, 'builds', `${path.basename(variant.output)}-${path.basename(deck, '.md')}`)
			// Mermaid makes a deck's build several times slower, so start those decks first.
			const usesMermaid = (await readFile(inputPath, 'utf8')).includes('```mermaid')

			jobs.push({ usesMermaid, run: () => exportDeck(browser, inputPath, variant.output, buildRoot) })
		}
	}

	jobs.sort((first, second) => second.usesMermaid - first.usesMermaid)
	console.log(`Exporting ${jobs.length} deck(s) with ${concurrency} parallel job(s)`)
	await runPool(jobs.map(job => job.run), concurrency)
}
finally {
	await browser.close()
	await removeNoSolutionsWorkspace(workspace.rootDirectory)
}
