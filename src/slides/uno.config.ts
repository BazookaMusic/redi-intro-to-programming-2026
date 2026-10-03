import { createRequire } from 'node:module'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig } from 'unocss'

const slidevClient = dirname(createRequire(import.meta.url).resolve('@slidev/client/package.json'))

// `slidev export` renders PDFs from a print page whose CSS is generated before
// the slides and Slidev's built-in components are scanned. Scanning them up front
// keeps utility classes in PDFs and hides the code copy buttons.
export default defineConfig({
	content: {
		filesystem: [
			fileURLToPath(new URL('./*.md', import.meta.url)),
			join(slidevClient, 'builtin/CodeBlockWrapper.vue'),
		],
	},
})
