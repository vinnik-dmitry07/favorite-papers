import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'
import { FullSearchIndex, type FullIndexManifest } from './full-search-index'

const module = new WebAssembly.Module(readFileSync(new URL('../probe-kernel/scan.wasm', import.meta.url)))

function fixture() {
  const count = 9, dimensions = 768
  const vectors = new Int8Array(count * dimensions)
  const norms = new Float64Array(count)
  for (let row = 0; row < count; row++) {
    for (let dim = 0; dim < dimensions; dim++) vectors[row * dimensions + dim] = (row * 19 + dim * 7) % 255 - 127
    if (row === 8) vectors.set(vectors.subarray(0, dimensions), row * dimensions)
    let squared = 0
    for (let dim = 0; dim < dimensions; dim++) squared += vectors[row * dimensions + dim] ** 2
    norms[row] = 1 / Math.sqrt(squared)
  }
  const files = new Map<string, ArrayBuffer>([
    ['vectors-0.i8', vectors.buffer.slice(0, 4 * dimensions)],
    ['vectors-1.i8', vectors.buffer.slice(4 * dimensions)], ['norms.f64', norms.buffer],
  ])
  const manifest: FullIndexManifest = { passage_count: count, dimensions,
    index: { kind: 'exact-int8', quantization: 'per-row-maxabs-rint-127', norms_path: 'norms.f64',
      shards: [{ path: 'vectors-0.i8', start: 0, count: 4 }, { path: 'vectors-1.i8', start: 4, count: 5 }] } }
  return { manifest, vectors, norms, files, load: async (path: string) => files.get(path)!.slice(0) }
}

describe('full exact int8 index', () => {
  it.each([undefined, module])('matches independent quantized cosine with deterministic ID-order ties', async (kernel) => {
    const data = fixture()
    const query = new Float32Array(Array.from({ length: 768 }, (_, dim) => Math.sin(dim * 0.3)))
    const norm = Math.sqrt(Array.from(query).reduce((sum, value) => sum + value * value, 0))
    const expected = Array.from({ length: 9 }, (_, row) => {
      let dot = 0
      for (let dim = 0; dim < 768; dim++) dot += data.vectors[row * 768 + dim] * (query[dim] / norm)
      return { index: row, score: dot * data.norms[row] }
    }).sort((a, b) => b.score - a.score || a.index - b.index)
    const actual = await FullSearchIndex.load(data.manifest, data.load, kernel)
    expect(actual.search(query, 9)).toEqual(expected)
    expect(actual.search(query, 3)).toEqual(expected.slice(0, 3))
    expect(actual.residentBytes).toBeLessThan(100000)
    expect(() => actual.search(new Float32Array(768), 8)).toThrow('norm')
    query[7] = NaN
    expect(() => actual.search(query, 8)).toThrow('Non-finite')
  })

  it('loads shards sequentially and rejects corrupt geometry or quantization', async () => {
    const data = fixture()
    let pending = 0, maximum = 0
    const events: string[] = []
    await FullSearchIndex.load(data.manifest, async (path) => {
      pending++; maximum = Math.max(maximum, pending)
      await Promise.resolve()
      const result = await data.load(path)
      pending--
      return result
    }, module, (sample) => events.push(sample.phase))
    expect(maximum).toBe(1)
    expect(events.at(-1)).toBe('ready')
    data.manifest.index.shards[1].start = 3
    await expect(FullSearchIndex.load(data.manifest, data.load)).rejects.toThrow('Noncontiguous')
    data.manifest.index.shards[1].start = 4
    new DataView(data.files.get('norms.f64')!).setFloat64(0, 1, true)
    await expect(FullSearchIndex.load(data.manifest, data.load)).rejects.toThrow('normalization')
  })
})
