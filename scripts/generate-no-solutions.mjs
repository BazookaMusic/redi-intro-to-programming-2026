import { cp, mkdir, readdir, readFile, rm, writeFile } from 'node:fs/promises'
import path from 'node:path'

const sourceDirectory = path.resolve('src/slides')
const outputDirectory = path.resolve('src/slides_no_solutions')
const solutionStart = '<!-- solution:start -->'
const solutionEnd = '<!-- solution:end -->'

function removeSolutions(markdown, filePath) {
	let output = ''
	let cursor = 0
	let removedSlides = 0

	while (true) {
		const start = markdown.indexOf(solutionStart, cursor)
		const unmatchedEnd = markdown.indexOf(solutionEnd, cursor)

		if (unmatchedEnd !== -1 && (start === -1 || unmatchedEnd < start))
			throw new Error(`Found ${solutionEnd} without a matching start in ${filePath}`)

		if (start === -1) {
			output += markdown.slice(cursor)
			break
		}

		const end = markdown.indexOf(solutionEnd, start + solutionStart.length)
		if (end === -1)
			throw new Error(`Found ${solutionStart} without a matching end in ${filePath}`)

		output += markdown.slice(cursor, start)
		cursor = end + solutionEnd.length
		removedSlides += 1
	}

	return { markdown: output, removedSlides }
}

async function generateDirectory(source, output) {
	await mkdir(output, { recursive: true })

	let removedSlides = 0
	const entries = await readdir(source, { withFileTypes: true })

	for (const entry of entries) {
		if (entry.name === 'node_modules')
			continue

		const sourcePath = path.join(source, entry.name)
		const outputPath = path.join(output, entry.name)

		if (entry.isDirectory()) {
			removedSlides += await generateDirectory(sourcePath, outputPath)
		}
		else if (entry.name.endsWith('.md')) {
			const sourceMarkdown = await readFile(sourcePath, 'utf8')
			const result = removeSolutions(sourceMarkdown, sourcePath)
			await writeFile(outputPath, result.markdown)
			removedSlides += result.removedSlides
		}
		else {
			await cp(sourcePath, outputPath)
		}
	}

	return removedSlides
}

await rm(outputDirectory, { recursive: true, force: true })
const removedSlides = await generateDirectory(sourceDirectory, outputDirectory)

console.log(`Generated src/slides_no_solutions and removed ${removedSlides} solution slide(s).`)
