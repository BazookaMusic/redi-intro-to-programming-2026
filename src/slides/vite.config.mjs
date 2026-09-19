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
		},
	}
}

export default defineConfig(({ command }) => ({
	plugins: command === 'build' ? [viteSingleFile(), removeManualChunks()] : [],
}))