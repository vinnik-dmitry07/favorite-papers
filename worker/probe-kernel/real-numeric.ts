/** Bounded genuine-vector JS/WASM comparison with an independent scalar int8 oracle. */
import assert from 'node:assert/strict'
import { createHash } from 'node:crypto'
import { readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { FullSearchIndex } from '../src/full-search-index'

const [directory, wasmPath, output] = process.argv.slice(2)
assert(directory && wasmPath && output)
const descriptor = JSON.parse(readFileSync(resolve(directory, 'numeric.json'), 'utf8'))
const count = descriptor.passage_count
assert(Number.isSafeInteger(count) && count >= 50 && count <= 500)
assert.equal(descriptor.query_count, 32)
const loaded = new Map<string, ArrayBuffer>()
const load = async (path: string) => {
  assert(['vectors.i8', 'norms.f64', 'queries.f32'].includes(path))
  const bytes = readFileSync(resolve(directory, path))
  assert.equal(createHash('sha256').update(bytes).digest('hex'), descriptor.files[path])
  const buffer = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) as ArrayBuffer
  loaded.set(path, buffer)
  return buffer
}
const module = new WebAssembly.Module(readFileSync(wasmPath))
const wasm = await FullSearchIndex.load(descriptor, load, module)
const js = await FullSearchIndex.load(descriptor, load)
const integers = new Int8Array(loaded.get('vectors.i8')!)
const queries = new Float32Array(await load('queries.f32'))
assert.equal(queries.length, 32 * 768)
assert.equal(new Set(descriptor.source_indices).size, count)
assert.equal(descriptor.source_indices.length, count)
assert.equal(descriptor.packed_ids.length, count)
for (let index = 0; index < count; index++) {
  const source = descriptor.source_indices[index]
  assert(Number.isInteger(source) && source >= 0 && source < count)
  assert.equal(descriptor.packed_ids[index], descriptor.source_rows[source].id)
  if (index) assert(descriptor.packed_ids[index - 1] < descriptor.packed_ids[index])
}
let maxDifference = 0
for (let q = 0; q < 32; q++) {
  const query = queries.subarray(q * 768, (q + 1) * 768)
  let qSquared = 0
  for (const value of query) qSquared += value * value
  const qNorm = Math.sqrt(qSquared)
  const expected = []
  for (let row = 0; row < count; row++) {
    let dot = 0, normSquared = 0
    for (let dim = 0; dim < 768; dim++) {
      const value = integers[row * 768 + dim]
      dot += value * (query[dim] / qNorm)
      normSquared += value * value
    }
    expected.push({ index: row, score: dot / Math.sqrt(normSquared) })
  }
  expected.sort((a, b) => b.score - a.score || (descriptor.packed_ids[a.index] < descriptor.packed_ids[b.index] ? -1 : 1))
  for (const k of [25, 40, 50]) {
    const actual = wasm.search(query, k), reference = js.search(query, k)
    assert.deepEqual(actual.map((hit) => hit.index), expected.slice(0, k).map((hit) => hit.index))
    assert.deepEqual(reference.map((hit) => hit.index), actual.map((hit) => hit.index))
    for (let index = 0; index < k; index++) {
      maxDifference = Math.max(maxDifference, Math.abs(actual[index].score - expected[index].score),
        Math.abs(actual[index].score - reference[index].score))
    }
  }
}
assert(maxDifference <= 1e-12)
writeFileSync(output, JSON.stringify({ status: 'PASS', count, query_count: 32,
  candidate_limits: [25, 40, 50], checks: { quantized_oracle: true, js_wasm: true, row_mapping: true },
  max_score_difference: maxDifference, score_tolerance: 1e-12, node: process.version }))
