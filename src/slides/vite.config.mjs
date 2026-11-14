import { defineConfig } from 'vite'
import { viteSingleFile } from 'vite-plugin-singlefile'

function removeManualChunks() {
	return {
		name: 'slidev-single-file',
		enforce: 'post',
		config(config) {
			const output = config.build?.rollupOptions?.output

			for (const options of Array.isArray(output) ? output : [output]) {
				if (options)
					delete options.manualChunks
			}

			// Keep the /print route in builds so scripts/export-slides.mjs can print PDFs from the static HTML
			// without enabling Slidev's download button.
			config.define = { ...config.define, __SLIDEV_FEATURE_PRINT__: 'true' }
		},
	}
}

export default defineConfig(({ command }) => ({
	plugins: command === 'build' ? [viteSingleFile(), removeManualChunks()] : [],
}))