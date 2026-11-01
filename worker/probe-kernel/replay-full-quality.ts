/** Read-only historical vector analysis; never issues a live admission certificate. */
import { createHash } from 'node:crypto'
import { readFileSync, renameSync, writeFileSync } from 'node:fs'
import { isAbsolute, resolve, sep } from 'node:path'
import { performance } from 'node:perf_hooks'
import { FullSearchIndex } from '../src/full-search-index'

const [assetsArgument, sourceArgument, queriesArgument, outputArgument, wasmArgument,
  frozenArgument, restorationArgument, ...extra] = process.argv.slice(2)
if (![assetsArgument, sourceArgument, queriesArgument, outputArgument, wasmArgument,
  frozenArgument, restorationArgument].every(Boolean) || extra.length) {
  throw new Error('Usage: replay-full-quality.mjs PACKED_DIR SOURCE_DIR QUERY_VECTORS OUTPUT SCAN_WASM FROZEN_QUERIES RESTORATION_JSON')
}
const started = performance.now()
const sha = (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex')
const archiveSha = '8f3fd29b369ae41f1474e052e0eef931a23ca7437c99640adbc6bc13d519c65c'
const sourceCommit = 'fa3f4ec3724949a98b2b510949cf8efe405baf8a'
const restorationBytes = readFileSync(resolve(restorationArgument))
const restoration = JSON.parse(restorationBytes.toString('utf8'))
if (restoration.kind !== 'historical-full-search-artifact-restoration'
  || restoration.artifact_sha256 !== archiveSha || restoration.run_id !== 40448979121
  || restoration.source_commit !== sourceCommit) throw new Error('Historical restoration pin mismatch')
const sourceFiles = [
  'worker/src/full-search-index.ts', 'worker/src/static-search-int8.ts',
  'worker/probe-kernel/scan.wat', 'worker/probe-kernel/scan.wasm',
  'worker/probe-kernel/build.mjs',
]
const sourceHashes = Object.fromEntries(sourceFiles.map((path) => {
  const checksum = sha(readFileSync(resolve(process.cwd(), path)))
  if (restoration.source_sha256?.[path] !== checksum) {
    throw new Error('Historical runtime source mismatch: ' + path)
  }
  return [path, checksum]
}))
const wasmBytes = readFileSync(resolve(wasmArgument))
if (sha(wasmBytes) !== sourceHashes['worker/probe-kernel/scan.wasm']) {
  throw new Error('Supplied WASM differs from the restored runtime')
}
const assets = resolve(assetsArgument)
const source = resolve(sourceArgument)
const output = resolve(outputArgument)
const manifestBytes = readFileSync(resolve(assets, 'probe.json'))
const manifest = JSON.parse(manifestBytes.toString('utf8'))
const sourceBytes = readFileSync(resolve(source, 'probe.json'))
const original = JSON.parse(sourceBytes.toString('utf8'))
if (restoration.canonical_manifest_sha256 !== sha(sourceBytes)
  || restoration.packed_manifest_sha256 !== sha(manifestBytes)
  || manifest.synthetic !== false || original.synthetic !== false
  || manifest.passage_count !== 40575 || original.rows.length !== 40575
  || manifest.source_manifest_sha256 !== sha(sourceBytes)
  || manifest.source_rows_sha256 !== original.rows_sha256) {
  throw new Error('Historical packed/source manifest mismatch')
}
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
for (let position = 0; position < manifest.passage_count; position++) {
  const offset = position * 128
  const sourceIndex = metadata.getUint32(offset + 52, true)
  const id = Buffer.from(metadata.buffer, offset, 32).toString('hex')
  const row = original.rows[sourceIndex]
  if (!row || row.id !== id || (position && id <= previousId)
    || row.paper_id !== manifest.paper_ids[metadata.getUint32(offset + 32, true)]
    || row.chunk_index !== metadata.getUint32(offset + 36, true)
    || row.start !== metadata.getUint32(offset + 40, true)
    || row.end !== metadata.getUint32(offset + 44, true)) throw new Error('Packed row mapping mismatch')
  previousId = id
  sourceIndices.push(sourceIndex)
}
if (new Set(sourceIndices).size !== manifest.passage_count) throw new Error('Source row mapping is not bijective')
const queryBytes = readFileSync(resolve(queriesArgument))
const frozenBytes = readFileSync(resolve(frozenArgument))
const queryMetadata = JSON.parse(readFileSync(resolve(queriesArgument) + '.json', 'utf8'))
if (queryMetadata.count !== 2064 || queryMetadata.dimensions !== 768
  || queryMetadata.vectors_sha256 !== sha(queryBytes)
  || queryMetadata.query_manifest_sha256 !== sha(frozenBytes)
  || restoration.query_vectors_sha256 !== sha(queryBytes)
  || restoration.query_manifest_sha256 !== sha(frozenBytes)
  || queryMetadata.encoder_signature !== original.embeddings.encoder_signature
  || queryBytes.length !== queryMetadata.count * 768 * 4) throw new Error('Query vector provenance mismatch')
const queries = new Float32Array(queryBytes.buffer.slice(queryBytes.byteOffset,
  queryBytes.byteOffset + queryBytes.byteLength))
const module = new WebAssembly.Module(wasmBytes)
const index = await FullSearchIndex.load(manifest, loadAsset, module)
const jsIndex = await FullSearchIndex.load(manifest, loadAsset)
const crosschecks = new Set(Array.from({ length: 64 }, (_, position) =>
  Math.floor(position * (queryMetadata.count - 1) / 63)))
const rankings: number[][] = []
const wall: number[] = []
let maxScoreDifference = 0
for (let q = 0; q < queryMetadata.count; q++) {
  if (performance.now() - started > 600_000) throw new Error('Historical analysis exceeded 600 seconds')
  const query = queries.subarray(q * 768, (q + 1) * 768)
  const before = performance.now()
  const hits = index.search(query, 50)
  wall.push(performance.now() - before)
  if (hits.length !== 50) throw new Error('Incomplete runtime ranking')
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
  if ((q + 1) % 250 === 0) process.stderr.write('Historical full int8 runtime queries: ' + (q + 1) + '\n')
}
const ordered = wall.slice().sort((a, b) => a - b)
sourceHashes['worker/probe-kernel/replay-full-quality.ts'] = sha(readFileSync(
  resolve(process.cwd(), 'worker/probe-kernel/replay-full-quality.ts')))
const result = {
  schema_version: 1, kind: 'historical-artifact-offline-rankings', engine: 'full-int8-runtime',
  run_id: 40448979121, source_commit: sourceCommit, artifact_sha256: archiveSha,
  restoration_sha256: sha(restorationBytes),
  scope: 'Read-only analysis of retained vectors; no new inference or admission certificate.',
  implementation: { primary: 'FullSearchIndex WASM exact int8',
    crosscheck: 'FullSearchIndex JS exact int8', source_sha256: sourceHashes,
    wasm_sha256: sha(wasmBytes) },
  manifest_sha256: sha(sourceBytes), packed_manifest_sha256: sha(manifestBytes),
  source_rows_sha256: original.rows_sha256,
  query_vectors_sha256: sha(queryBytes), query_manifest_sha256: sha(frozenBytes),
  query_count: queryMetadata.count, passage_count: manifest.passage_count,
  rankings, js_wasm_checked_queries: [...crosschecks], js_wasm_max_score_difference: maxScoreDifference,
  node: process.version, admission_certificate: 'NOT_ISSUED', production_ready: false,
  timing_scope: 'Local kernel wall time only; not Cloudflare CPU or an API journey.',
  wall_ms: { p50: ordered[Math.ceil(ordered.length * .5) - 1],
    p99: ordered[Math.ceil(ordered.length * .99) - 1], first: wall[0] },
  elapsed_seconds: (performance.now() - started) / 1000,
}
writeFileSync(output + '.tmp', JSON.stringify(result))
renameSync(output + '.tmp', output)
process.stdout.write(JSON.stringify({ output, query_count: rankings.length,
  js_wasm_checked: crosschecks.size, elapsed_seconds: result.elapsed_seconds }) + '\n')
