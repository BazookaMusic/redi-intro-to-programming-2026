import { mkdir, readdir, rm } from 'node:fs/promises'
import { spawn } from 'node:child_process'
import path from 'node:path'

const slidevCli = path.resolve('node_modules/@slidev/cli/bin/slidev.mjs')

const variants = [
	{ source: 'src/slides', output: 'slides_solutions' },
	{ source: 'src/slides_no_solutions', output: 'slides_no_solutions' },
]

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

for (const variant of variants) {
	const sourceDirectory = path.resolve(variant.source)
	const outputDirectory = path.resolve(variant.output)
	const entries = await readdir(sourceDirectory, { withFileTypes: true })
	const decks = entries
		.filter(entry => entry.isFile() && entry.name.endsWith('.md'))
		.map(entry => entry.name)
		.sort()

	if (decks.length === 0)
		throw new Error(`No Slidev decks found in ${variant.source}`)

	await rm(outputDirectory, { recursive: true, force: true })
	await mkdir(outputDirectory, { recursive: true })

	for (const deck of decks) {
		const inputPath = path.join(sourceDirectory, deck)
		const outputPath = path.join(outputDirectory, deck.replace(/\.md$/, '.pdf'))

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
