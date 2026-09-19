import { mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises'
import { spawn } from 'node:child_process'
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

function runSlidev(arguments_) {
	return new Promise((resolve, reject) => {
		const process_ = spawn(process.execPath, [slidevCli, ...arguments_], { stdio: 'inherit' })

		process_.on('error', reject)
		process_.on('exit', (code) => {
			if (code === 0)
				resolve()
			else
				reject(new Error(`Slidev export failed with exit code ${code}`))
		})
	})
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

const workspace = await createNoSolutionsWorkspace()

try {
	const variants = [
		{ source: path.resolve('src/slides'), output: path.resolve('slides_solutions') },
		{ source: workspace.slidesDirectory, output: path.resolve('slides_no_solutions') },
	]

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
			const deckName = deck.replace(/\.md$/, '')
			const pdfOutputPath = path.join(variant.output, `${deckName}.pdf`)
			const htmlOutputPath = path.join(variant.output, `${deckName}.html`)
			const htmlBuildPath = path.join(variant.output, `.html-build-${deckName}`)

			console.log(`Exporting ${inputPath} to ${pdfOutputPath}`)
			await runSlidev([
				'export',
				inputPath,
				'--output',
				pdfOutputPath,
				'--format',
				'pdf',
				'--wait-until',
				'networkidle',
			])

			console.log(`Building ${inputPath} to ${htmlOutputPath}`)

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
				])
				await createStandaloneHtml(htmlBuildPath, htmlOutputPath)
			}
			finally {
				await rm(htmlBuildPath, { recursive: true, force: true })
			}
		}
	}
}
finally {
	await removeNoSolutionsWorkspace(workspace.rootDirectory)
}
