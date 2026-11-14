import { mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises'
import { spawn } from 'node:child_process'
import { availableParallelism } from 'node:os'
import path from 'node:path'
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
	|| Math.max(1, Math.min(4, Math.floor(availableParallelism() / 2)))

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

async function exportDeck(inputPath, outputDirectory) {
	const deckName = path.basename(inputPath, '.md')
	const label = `${path.basename(outputDirectory)}/${deckName}`
	const pdfOutputPath = path.join(outputDirectory, `${deckName}.pdf`)
	const htmlOutputPath = path.join(outputDirectory, `${deckName}.html`)
	const htmlBuildPath = path.join(outputDirectory, `.html-build-${deckName}`)
	const log = []
	const startTime = Date.now()

	console.log(`Started ${label}`)

	try {
		// networkidle waits for lazily loaded code; the extra wait covers rendering that starts afterwards
		// (slide paint, Mermaid diagrams), otherwise PDFs can be blank or miss diagrams under parallel load.
		await runSlidev([
			'export',
			inputPath,
			'--output',
			pdfOutputPath,
			'--format',
			'pdf',
			'--wait-until',
			'networkidle',
			'--wait',
			'3000',
		], log)

		try {
			await runSlidev([
				'build',
				inputPath,
				'--out',
				htmlBuildPath,
				'--base',
				'./',
				'--router-mode',
				'hash',
			], log)
			await createStandaloneHtml(htmlBuildPath, htmlOutputPath)
		}
		finally {
			await rm(htmlBuildPath, { recursive: true, force: true })
		}
	}
	catch (error) {
		console.error(`Failed ${label}:\n${log.join('')}`)
		throw new Error(`${label}: ${error.message}`)
	}

	console.log(`Finished ${label} in ${((Date.now() - startTime) / 1000).toFixed(1)}s`)
}

const workspace = await createNoSolutionsWorkspace()

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

		for (const deck of decks)
			jobs.push(() => exportDeck(path.join(variant.source, deck), variant.output))
	}

	console.log(`Exporting ${jobs.length} deck(s) with ${concurrency} parallel job(s)`)
	await runPool(jobs, concurrency)
}
finally {
	await removeNoSolutionsWorkspace(workspace.rootDirectory)
}
