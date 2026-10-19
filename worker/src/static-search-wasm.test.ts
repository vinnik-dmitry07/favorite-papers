import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'
import { PqIndex } from './static-search'
import { WasmPqScorer } from './static-search-wasm'
import { Int8Index, selectTop } from './static-search-int8'

const kernel = new WebAssembly.Module(readFileSync(new URL('../probe-kernel/scan.wasm', import.meta.url)))

describe('alternative scoring kernels', () => {
  it('matches PQ reference including non-multiple-of-four layouts and top-k ties', () => {
    for (const m of [1, 2, 5, 96]) {
      const config = { format: 'pq-ip-v1' as const, dimensions: m * 8, subquantizers: m, centroids: 7, count: 83 }
      const codes = Uint8Array.from({ length: m * config.count }, (_, i) => (i * 31 + (i >>> 2)) % 7).buffer
      const books = Float32Array.from({ length: config.dimensions * 7 }, (_, i) => Math.sin(i * 3)).buffer
      const index = new PqIndex(config, codes, books, new WasmPqScorer(kernel))
      const query = Float32Array.from({ length: config.dimensions }, (_, i) => Math.cos(i))
      for (const k of [1, 8, 50, 100]) {
        const expected = index.search(query, k)
        for (const engine of ['js4', 'wasm'] as const) {
          const actual = index.search(query, k, engine)
          expect(actual.map((r) => r.index)).toEqual(expected.map((r) => r.index))
          actual.forEach((r, i) => expect(r.score).toBeCloseTo(expected[i].score, 12))
        }
      }
    }
  })

  it('int8 full scan, selected rerank, and sign-bit shortlist match an independent oracle', () => {
    const count = 257, dimensions = 32
    const vectors = Int8Array.from({ length: count * dimensions }, (_, i) => (i * 31 + (i >>> 5)) % 255 - 127)
    const norms = Float64Array.from({ length: count }, (_, row) => 1 / Math.hypot(...vectors.slice(row * dimensions, (row + 1) * dimensions)))
    const bits = new Uint8Array(count * dimensions / 8)
    for (let i = 0; i < vectors.length; i++) if (vectors[i] >= 0) bits[i >>> 3] |= 1 << (i % 8)
    const index = new Int8Index(kernel, count, dimensions, [vectors.buffer], norms.buffer, bits.buffer)
    const query = Float32Array.from({ length: dimensions }, (_, i) => Math.sin(i + 0.5))
    const norm = Math.hypot(...query)
    const expected = Array.from({ length: count }, (_, row) => ({ index: row,
      score: Array.from(query).reduce((sum, q, i) => sum + q / norm * vectors[row * dimensions + i], 0) * norms[row] }))
      .sort((a, b) => b.score - a.score || a.index - b.index)
    const actual = index.search(query, 8)
    expect(actual.map((r) => r.index)).toEqual(expected.slice(0, 8).map((r) => r.index))
    actual.forEach((r, i) => expect(r.score).toBeCloseTo(expected[i].score, 12))
    const candidates = expected.slice(10, 110).map((r) => r.index).reverse()
    expect(index.search(query, 8, candidates).map((r) => r.index)).toEqual(expected.slice(10, 18).map((r) => r.index))
    const binary = Array.from({ length: count }, (_, row) => ({ index: row,
      score: -Array.from(query).reduce((n, q, i) => n + Number((q >= 0) !== (vectors[row * dimensions + i] >= 0)), 0) }))
      .sort((a, b) => b.score - a.score || a.index - b.index).slice(0, 200).map((r) => r.index)
    expect(index.search(query, 8, undefined, true)).toEqual(index.search(query, 8, binary))
    expect(() => index.search(query, 8, [count])).toThrow()
  })

  it('selection resolves ties by original row id regardless of rerank order', () => {
    expect(selectTop(Float64Array.from([1, 1, 2, 1]), 2, [9, 1, 7, 0])).toEqual([
      { index: 7, score: 2 }, { index: 0, score: 1 },
    ])
  })
})
