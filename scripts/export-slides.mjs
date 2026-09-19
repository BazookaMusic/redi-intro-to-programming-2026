import { mkdir, readdir, rm } from 'node:fs/promises'
import { spawn } from 'node:child_process'
import path from 'node:path'
import { createNoSolutionsWorkspace, removeNoSolutionsWorkspace } from './generate-no-solutions.mjs'

const slidevCli = path.resolve('node_modules/@slidev/cli/bin/slidev.mjs')

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
			const outputPath = path.join(variant.output, deck.replace(/\.md$/, '.pdf'))

			console.log(`Exporting ${inputPath} to ${outputPath}`)
			await runSlidev([
				'export',
				inputPath,
				'--output',
				outputPath,
				'--format',
				'pdf',
				'--wait-until',
				'networkidle',
			])
		}
	}
}
finally {
	await removeNoSolutionsWorkspace(workspace.rootDirectory)
}
