import { readFileSync } from 'node:fs'
import { defineConfig } from 'vitest/config'

export default defineConfig({
  plugins: [
    {
      name: 'vocab-text',
      transform(_code, id) {
        const path = id.split('?')[0]
        if (!path.endsWith('.txt') || path.includes('node_modules')) {
          return null
        }
        const text = readFileSync(path, 'utf8')
        return `export default ${JSON.stringify(text)}`
      },
    },
  ],
  test: {
    environment: 'node',
    include: ['src/**/*.test.ts'],
  },
})
