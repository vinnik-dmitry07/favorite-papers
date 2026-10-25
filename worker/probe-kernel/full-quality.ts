/** Offline rankings from the exact full-corpus runtime, not a Python surrogate. */
import { createHash } from 'node:crypto'
import { execFileSync } from 'node:child_process'
import { readFileSync, renameSync, writeFileSync } from 'node:fs'
import { dirname, isAbsolute, resolve, sep } from 'node:path'
import { performance } from 'node:perf_hooks'
import { FullSearchIndex } from '../src/full-search-index'

const [assetsArgument, sourceArgument, queriesArgument, outputArgument, wasmArgument,
  frozenArgument, certificateArgument, confirmation] = process.argv.slice(2)
if (![assetsArgument, sourceArgument, queriesArgument, outputArgument, wasmArgument,
  frozenArgument, certificateArgument].every(Boolean) || confirmation !== '--full-run-confirmed') {
  throw new Error('Usage: full-quality.mjs PACKED_DIR SOURCE_DIR QUERY_VECTORS OUTPUT SCAN_WASM FROZEN_QUERIES CERTIFICATE --full-run-confirmed')
}
// The same fresh intended-path certificate protects all expensive entrypoints.
// Verification runs before loading the index or executing even one query.
execFileSync(process.env.FULL_PROBE_PYTHON || 'python', ['-c',
  'import sys; sys.path.insert(0, sys.argv[1]); from preflight_full_search_probe import verify_certificate; '
    + 'verify_certificate(sys.argv[2], corpus=sys.argv[3], queries=sys.argv[4])',
  resolve(process.cwd(), 'src'), resolve(certificateArgument), resolve(sourceArgument), resolve(frozenArgument),
], { stdio: 'inherit' })
const assets = resolve(assetsArgument)
const source = resolve(sourceArgument)
const output = resolve(outputArgument)
const sha = (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex')
const manifestBytes = readFileSync(resolve(assets, 'probe.json'))
const manifest = JSON.parse(manifestBytes.toString('utf8'))
const sourceBytes = readFileSync(resolve(source, 'probe.json'))
const original = JSON.parse(sourceBytes.toString('utf8'))
if (manifest.source_manifest_sha256 !== sha(sourceBytes)
  || manifest.source_rows_sha256 !== original.rows_sha256
  || manifest.passage_count !== original.rows.length) throw new Error('Packed/source manifest mismatch')
async function loadAsset(path: string): Promise<ArrayBuffer> {
  const target = resolve(assets, path)
  if (isAbsolute(path) || !target.startsWith(assets + sep)) throw new Error('Unsafe packed asset path')
  const bytes = readFileSync(target)
  const identity = manifest.files[path]
  if (!identity || bytes.length !== identity.bytes || sha(bytes) !== identity.sha256) {
    throw new Error('Packed asset checksum mismatch: ' + path)
  }
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) as ArrayBuffer
}
const metadata = new DataView(await loadAsset(manifest.metadata.path))
if (manifest.metadata.row_bytes !== 128 || metadata.byteLength !== manifest.passage_count * 128) {
  throw new Error('Unsupported row metadata')
}
const sourceIndices: number[] = []
let previousId = ''
for (let index = 0; index < manifest.passage_count; index++) {
  const offset = index * 128
  const sourceIndex = metadata.getUint32(offset + 52, true)
  const id = Buffer.from(metadata.buffer, offset, 32).toString('hex')
  const row = original.rows[sourceIndex]
  if (!row || row.id !== id || (index && id <= previousId)
    || row.paper_id !== manifest.paper_ids[metadata.getUint32(offset + 32, true)]
    || row.chunk_index !== metadata.getUint32(offset + 36, true)
    || row.start !== metadata.getUint32(offset + 40, true)
    || row.end !== metadata.getUint32(offset + 44, true)) throw new Error('Packed row mapping mismatch')
  previousId = id
  sourceIndices.push(sourceIndex)
}
if (new Set(sourceIndices).size !== manifest.passage_count) throw new Error('Source row mapping is not bijective')
const queryBytes = readFileSync(resolve(queriesArgument))
const queryMetadata = JSON.parse(readFileSync(resolve(queriesArgument) + '.json', 'utf8'))
if (queryMetadata.vectors_sha256 !== sha(queryBytes)
  || queryMetadata.query_manifest_sha256 !== sha(readFileSync(resolve(frozenArgument)))
  || queryMetadata.encoder_signature !== original.embeddings.encoder_signature
  || queryBytes.length !== queryMetadata.count * 768 * 4) throw new Error('Query vector provenance mismatch')
const queries = new Float32Array(queryBytes.buffer.slice(queryBytes.byteOffset,
  queryBytes.byteOffset + queryBytes.byteLength))
const module = new WebAssembly.Module(readFileSync(resolve(wasmArgument)))
const index = await FullSearchIndex.load(manifest, loadAsset, module)
const jsIndex = await FullSearchIndex.load(manifest, loadAsset)
// Fixed spread includes both ends and never selects queries by observed results.
const crosschecks = new Set(Array.from({ length: Math.min(64, queryMetadata.count) }, (_, position) =>
  Math.floor(position * (queryMetadata.count - 1) / (Math.min(64, queryMetadata.count) - 1 || 1))))
const rankings: number[][] = []
const wall: number[] = []
let maxScoreDifference = 0
const started = performance.now()
for (let q = 0; q < queryMetadata.count; q++) {
  const query = queries.subarray(q * 768, (q + 1) * 768)
  const before = performance.now()
  const hits = index.search(query, 50)
  wall.push(performance.now() - before)
  if (crosschecks.has(q)) {
    const reference = jsIndex.search(query, 50)
    if (reference.length !== hits.length || reference.some((hit, at) => hit.index !== hits[at].index)) {
      throw new Error('Actual JS/WASM ranking disagreement at frozen query ' + q)
    }
    for (let at = 0; at < hits.length; at++) {
      maxScoreDifference = Math.max(maxScoreDifference, Math.abs(hits[at].score - reference[at].score))
    }
    if (maxScoreDifference > 1e-12) throw new Error('Actual JS/WASM score disagreement')
  }
  rankings.push(hits.map((hit) => sourceIndices[hit.index]))
  if ((q + 1) % 250 === 0) process.stderr.write('Actual full int8 runtime queries: ' + (q + 1) + '\n')
}
const ordered = wall.slice().sort((a, b) => a - b)
const root = resolve(dirname(new URL(import.meta.url).pathname), '..', '..')
const sourceFiles = [
  'worker/src/full-search-index.ts', 'worker/src/static-search-int8.ts',
  'worker/probe-kernel/scan.wat', 'worker/probe-kernel/full-quality.ts',
]
const sourceHashes = Object.fromEntries(sourceFiles.map((path) => {
  // A bundled harness can live elsewhere; explicit repo cwd owns source paths.
  const bytes = readFileSync(resolve(process.cwd(), path))
  return [path, sha(bytes)]
}))
void root
const result = {
  schema_version: 1, engine: 'full-int8-runtime',
  implementation: { primary: 'FullSearchIndex WASM exact int8',
    crosscheck: 'FullSearchIndex JS exact int8', source_sha256: sourceHashes,
    wasm_sha256: sha(readFileSync(resolve(wasmArgument))) },
  manifest_sha256: sha(sourceBytes), packed_manifest_sha256: sha(manifestBytes),
  source_rows_sha256: original.rows_sha256,
  query_vectors_sha256: sha(queryBytes),
  query_manifest_sha256: queryMetadata.query_manifest_sha256,
  preflight_certificate_sha256: sha(readFileSync(resolve(certificateArgument))),
  query_count: queryMetadata.count, passage_count: manifest.passage_count,
  rankings, js_wasm_checked_queries: [...crosschecks],
  js_wasm_max_score_difference: maxScoreDifference,
  node: process.version,
  timing_scope: 'Local kernel wall time only; not Cloudflare CPU or an API journey.',
  wall_ms: { p50: ordered[Math.ceil(ordered.length * .5) - 1],
    p99: ordered[Math.ceil(ordered.length * .99) - 1], first: wall[0] },
  elapsed_seconds: (performance.now() - started) / 1000,
}
writeFileSync(output + '.tmp', JSON.stringify(result))
renameSync(output + '.tmp', output)
process.stdout.write(JSON.stringify({ output, query_count: rankings.length,
  js_wasm_checked: crosschecks.size, elapsed_seconds: result.elapsed_seconds }) + '\n')
