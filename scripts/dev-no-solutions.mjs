import { spawn } from 'node:child_process'
import path from 'node:path'
import { createNoSolutionsWorkspace, removeNoSolutionsWorkspace } from './generate-no-solutions.mjs'

const slidevCli = path.resolve('node_modules/@slidev/cli/bin/slidev.mjs')
const [deck = '01-github-desktop.md', ...slidevArguments] = process.argv.slice(2)
const workspace = await createNoSolutionsWorkspace()
let previewProcess

const stopPreview = (signal) => {
	previewProcess?.kill(signal)
}

for (const signal of ['SIGINT', 'SIGTERM', 'SIGHUP'])
	process.on(signal, stopPreview)

try {
	const deckPath = path.join(workspace.slidesDirectory, deck)
	const exitCode = await new Promise((resolve, reject) => {
		previewProcess = spawn(
			process.execPath,
			[slidevCli, deckPath, '--open', ...slidevArguments],
			{ stdio: 'inherit' },
		)

		previewProcess.on('error', reject)
		previewProcess.on('exit', code => resolve(code ?? 0))
	})

	process.exitCode = exitCode
}
finally {
	for (const signal of ['SIGINT', 'SIGTERM', 'SIGHUP'])
		process.off(signal, stopPreview)

	await removeNoSolutionsWorkspace(workspace.rootDirectory)
}
