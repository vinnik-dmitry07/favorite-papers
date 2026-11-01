/** Run the actual probe kernels on externally supplied real embedding fixtures. */
import { readFileSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { cpus } from 'node:os'
import { performance } from 'node:perf_hooks'
import { PqIndex } from '../src/static-search'
import { WasmPqScorer } from '../src/static-search-wasm'
import { Int8Index } from '../src/static-search-int8'

const directory = process.argv[2]
const wasmPath = process.argv[3]
const config = JSON.parse(readFileSync(join(directory, 'config.json'), 'utf8'))
function buffer(name: string): ArrayBuffer {
  const data = readFileSync(join(directory, name))
  return data.buffer.slice(data.byteOffset, data.byteOffset + data.byteLength) as ArrayBuffer
}
const module = new WebAssembly.Module(readFileSync(wasmPath))
const pq = new PqIndex(config, buffer('codes.bin'), buffer('codebooks.bin'), new WasmPqScorer(module))
const sq = new Int8Index(module, config.count, config.dimensions,
  [buffer('int8.bin')], buffer('norms.bin'), buffer('bits.bin'))
const queries = new Float32Array(buffer('queries.bin'))
const rankings: Record<string, number[][]> = {}
const wall: Record<string, number[]> = {}
const names = ['probe_pq_js', 'probe_pq_js4', 'probe_pq_wasm',
  'probe_int8', 'probe_pq100_int8', 'probe_raw_binary200_int8']
for (const name of names) { rankings[name] = []; wall[name] = [] }
function measure(name: string, fn: () => { index: number }[]) {
  const start = performance.now()
  const hits = fn()
  wall[name].push(performance.now() - start)
  const ids = hits.map((hit) => hit.index)
  rankings[name].push(ids)
  return ids
}
for (let offset = 0; offset < queries.length; offset += config.dimensions) {
  const query = queries.subarray(offset, offset + config.dimensions)
  measure('probe_pq_js', () => pq.search(query, 200, 'js'))
  measure('probe_pq_js4', () => pq.search(query, 200, 'js4'))
  measure('probe_pq_wasm', () => pq.search(query, 200, 'wasm'))
  measure('probe_int8', () => sq.search(query, 200))
  measure('probe_pq100_int8', () => sq.search(query, 100,
    pq.search(query, 100, 'wasm').map((hit) => hit.index)))
  measure('probe_raw_binary200_int8', () => sq.search(query, 200, undefined, true))
  if ((offset / config.dimensions + 1) % 250 === 0) {
    process.stderr.write('Kernel queries: ' + (offset / config.dimensions + 1) + '\n')
  }
}
const times = Object.fromEntries(Object.entries(wall).map(([name, values]) => {
  const ordered = values.slice(1).sort((a, b) => a - b)
  return [name, { first_ms: values[0], subsequent_p50_ms: ordered[Math.ceil(ordered.length / 2) - 1],
    subsequent_p99_ms: ordered[Math.ceil(ordered.length * 0.99) - 1] }]
}))
writeFileSync(join(directory, 'kernel-rankings.json'), JSON.stringify({ rankings, times,
  node: process.version, cpu: cpus()[0]?.model,
  timing_scope: 'Local Node kernel wall time, shared process, no hydration, embedding or Cloudflare CPU.' }))
