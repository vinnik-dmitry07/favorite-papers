import type { ActivePointer, ConfirmedDoc, CorpusStore, GraphDoc, PaperDoc } from './corpus'
import { FullSearchIndex, type FullIndexManifest, type IndexMemorySample } from './full-search-index'
import { DomainError, fail } from './schemas'
import { canonicalJson, sha256Hex, signatures, vectorIdOf } from './signatures'
import { embed } from './tokenize'

export interface FullCorpusManifest extends FullIndexManifest {
  schema_version: 1
  reader_schema: number
  kind: 'full-corpus-int8' | 'full-corpus-int8-geometry-fixture'
  synthetic: boolean
  publication_ready: false
  scope: 'isolated-full-corpus-evaluation-not-production'
  slot: 'full-probe'
  release_id: string
  embedding_signature: string
  build_signature: string
  paper_ids: string[]
  text_paper_ids: string[]
  graph_path: string
  files: Record<string, { bytes: number, sha256: string }>
  source_manifest_sha256: string
  source_rows_sha256: string
  fixture_vectors?: { generator: string, seed: number, count: number, dimensions: number,
    dtype: string, byte_order: string, normalization: string, sha256: string, purpose: string }
  source_embeddings?: { model_id: string, model_revision: string, pooling: string,
    normalization: string, dtype: string, byte_order: string, count: number,
    dimensions: number, sha256: string }
  metadata: { path: string, row_bytes: 128, order: 'vector-id-lexicographic' }
  compatibility: { path: string, indices: number[], source_indices: number[] }
}

export interface FullCorpusRow {
  id: string
  paper_id: string
  chunk_index: number
  start: number
  end: number
  token_count: number
  sourceIndex: number
  content_hash: string
  input_hash: string
}

const HASH = /^[0-9a-f]{64}$/
const MAX_ASSET = 24 * 1024 * 1024
function check(value: unknown, message: string): asserts value {
  if (!value) fail('config_mismatch', 503, 'Full corpus: ' + message)
}
function object(value: unknown): value is Record<string, unknown> {
  return !!value && typeof value === 'object' && !Array.isArray(value)
}
function integer(value: unknown, min: number, max: number): value is number {
  return Number.isSafeInteger(value) && Number(value) >= min && Number(value) <= max
}
function hash(value: unknown): value is string { return typeof value === 'string' && HASH.test(value) }
function hex(bytes: Uint8Array): string {
  let result = ''
  for (const byte of bytes) result += byte.toString(16).padStart(2, '0')
  return result
}
async function digest(bytes: ArrayBuffer): Promise<string> {
  return hex(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes)))
}
function parse(bytes: ArrayBuffer): unknown {
  try { return JSON.parse(new TextDecoder('utf-8', { fatal: true, ignoreBOM: false }).decode(bytes)) }
  catch { fail('config_mismatch', 503, 'Full corpus: invalid JSON') }
}
function sortedIds(raw: unknown): raw is string[] {
  return Array.isArray(raw) && raw.length > 0 && raw.length <= 10000
    && raw.every((id, index) => typeof id === 'string' && id.length > 0
      && (!index || raw[index - 1] < id))
}
function freeze<T>(value: T): T {
  if (value && typeof value === 'object' && !Object.isFrozen(value)) {
    for (const item of Object.values(value)) freeze(item)
    Object.freeze(value)
  }
  return value
}

export interface FullCorpusOptions {
  module?: WebAssembly.Module
  memorySample?: (sample: IndexMemorySample) => void
}
type Assets = { fetch(request: Request): Promise<Response> }
type Embedder = (text: string) => Promise<number[]>
type Limiter = (key: string) => Promise<boolean>
const allow: Limiter = async () => true
export const PAPER_LOAD_LIMITS = Object.freeze({ active: 1, queued: 16 })
export const ASSET_RETRY_MS = 5000

/** Transport failures can recover; authenticated content mismatches cannot. */
export class TransientAssetError extends DomainError {
  constructor(message: string) { super('asset_temporarily_unavailable', 503, message) }
}

/** Real encoder envelope only. Synthetic input must use the explicit fixture API. */
export function createFullCorpusStore(assets: Assets, expectedManifestHash: string,
  embedder: Embedder, limiter: Limiter = allow, options: FullCorpusOptions = {}) {
  return loadFullCorpusStore(assets, expectedManifestHash, embedder, limiter, options, false)
}

/** Test-only entry point; shares all packing/index/paper mechanics with real data. */
export function createGeometryFixtureStore(assets: Assets, expectedManifestHash: string,
  embedder: Embedder, limiter: Limiter = allow, options: FullCorpusOptions = {}) {
  return loadFullCorpusStore(assets, expectedManifestHash, embedder, limiter, options, true)
}

function singleton<T>(initialize: () => Promise<T>): () => Promise<T> {
  let pending: Promise<T> | undefined
  let retryAt = 0
  return () => {
    if (retryAt && Date.now() >= retryAt) { pending = undefined; retryAt = 0 }
    // Share retries too. Integrity/configuration errors remain latched for this
    // immutable release; only transport failures become eligible after backoff.
    return pending ??= initialize().catch((error) => {
      if (error instanceof TransientAssetError) retryAt = Date.now() + ASSET_RETRY_MS
      throw error
    })
  }
}

/** Own one getter per runtime instance; concurrent cold callers share every allocation. */
export function createFullCorpusStoreLoader(...args: Parameters<typeof createFullCorpusStore>) {
  return singleton(() => createFullCorpusStore(...args))
}
export function createGeometryFixtureStoreLoader(...args: Parameters<typeof createGeometryFixtureStore>) {
  return singleton(() => createGeometryFixtureStore(...args))
}

/** Only packed binaries and graph remain resident; CorpusCache owns paper LRU. */
async function loadFullCorpusStore(assets: Assets, expectedManifestHash: string,
  embedder: Embedder, limiter: Limiter, options: FullCorpusOptions, fixture: boolean) {
  check(hash(expectedManifestHash), 'manifest SHA-256 must be pinned')
  let residentIndexBytes = 0
  const sample = (phase: string, currentAssetBytes = 0) => options.memorySample?.({
    phase, resident_index_bytes: residentIndexBytes, current_asset_bytes: currentAssetBytes,
  })
  const fetchBytes = async (path: string, expected: string, size?: number) => {
    let response: Response
    try { response = await assets.fetch(new Request('https://full-probe-assets.invalid/' + path)) }
    catch { throw new TransientAssetError('Asset request failed: ' + path) }
    if (response.status !== 200) {
      void response.body?.cancel().catch(() => {})
      throw new TransientAssetError('Asset request returned HTTP ' + response.status + ': ' + path)
    }
    const declared = response.headers.get('content-length')
    check(declared === null || (Number.isSafeInteger(Number(declared))
      && Number(declared) >= 0 && Number(declared) <= (size ?? 1024 * 1024)), 'asset length header exceeds bound')
    // Assets are pinned, but still bound the stream before allocating its full
    // buffer. A malicious/misconfigured origin must not make arrayBuffer OOM.
    const limit = size ?? 1024 * 1024
    const reader = response.body?.getReader()
    check(reader, 'missing asset body')
    const storage = new Uint8Array(limit)
    let length = 0
    while (true) {
      let part: ReadableStreamReadResult<Uint8Array>
      try { part = await reader.read() }
      catch { throw new TransientAssetError('Asset stream interrupted: ' + path) }
      if (part.done) break
      length += part.value.byteLength
      if (length > limit) {
        await reader.cancel()
        check(false, 'asset exceeds declared byte length')
      }
      storage.set(part.value, length - part.value.byteLength)
    }
    check(size === undefined || length === size, 'asset length mismatch: ' + path)
    const bytes = length === limit ? storage : storage.slice(0, length)
    check(await digest(bytes.buffer) === expected, 'asset checksum mismatch: ' + path)
    sample('verified-asset:' + path, bytes.byteLength)
    return bytes.buffer
  }
  const raw = parse(await fetchBytes('probe.json', expectedManifestHash))
  check(object(raw) && raw.schema_version === 1 && raw.reader_schema === embed.reader_schema
    && raw.kind === (fixture ? 'full-corpus-int8-geometry-fixture' : 'full-corpus-int8')
    && raw.synthetic === fixture && raw.publication_ready === false
    && raw.scope === 'isolated-full-corpus-evaluation-not-production' && raw.slot === 'full-probe'
    && raw.dimensions === 768 && integer(raw.passage_count, 1, 60000)
    && sortedIds(raw.paper_ids) && sortedIds(raw.text_paper_ids)
    && hash(raw.release_id) && hash(raw.embedding_signature) && hash(raw.build_signature)
    && hash(raw.source_manifest_sha256) && hash(raw.source_rows_sha256), 'unsupported manifest')
  check(object(raw.files) && Object.entries(raw.files).every(([path, entry]) =>
    /^[A-Za-z0-9_./-]+$/.test(path) && !path.startsWith('/')
      && path.split('/').every((part) => part && part !== '.' && part !== '..')
      && object(entry) && hash(entry.sha256) && integer(entry.bytes, 1, MAX_ASSET)), 'invalid asset map')
  const manifest = raw as unknown as FullCorpusManifest
  sample('manifest-parsed')
  const local = await signatures()
  check(manifest.embedding_signature === local.embedding && manifest.build_signature === local.build,
    'reader signature mismatch')
  if (fixture) {
    const vectors = manifest.fixture_vectors
    check(manifest.source_embeddings === undefined && object(vectors)
      && typeof vectors.generator === 'string' && /^[a-z0-9-]{1,80}$/.test(vectors.generator)
      && integer(vectors.seed, 0, 0xffffffff) && vectors.count === manifest.passage_count
      && vectors.dimensions === 768 && vectors.dtype === 'float32'
      && vectors.byte_order === 'little' && vectors.normalization === 'l2'
      && hash(vectors.sha256)
      && vectors.purpose === 'allocation-and-contract-testing-not-semantic-quality',
    'invalid synthetic geometry provenance')
  } else {
    check(manifest.fixture_vectors === undefined, 'fixture provenance in real corpus')
    const encoding = manifest.source_embeddings
    check(object(encoding) && encoding.model_id === embed.tokenizer.id
      && encoding.model_revision === embed.tokenizer.revision && encoding.pooling === 'cls'
      && encoding.normalization === 'l2' && encoding.dtype === 'float32'
      && encoding.byte_order === 'little' && encoding.dimensions === 768
      && encoding.count === manifest.passage_count && hash(encoding.sha256), 'source encoder mismatch')
  }
  check(object(manifest.metadata) && manifest.metadata.path === 'metadata.bin'
    && manifest.metadata.row_bytes === 128 && manifest.metadata.order === 'vector-id-lexicographic'
    && object(manifest.index) && manifest.index.kind === 'exact-int8'
    && manifest.index.quantization === 'per-row-maxabs-rint-127'
    && manifest.index.norms_path === 'norms.f64' && Array.isArray(manifest.index.shards)
    && manifest.index.shards.length > 0 && manifest.index.shards.length <= 60,
  'invalid packed index layout')
  check(object(manifest.compatibility) && manifest.compatibility.path === 'references.f32'
    && Array.isArray(manifest.compatibility.indices) && Array.isArray(manifest.compatibility.source_indices)
    && manifest.compatibility.indices.length === Math.min(200, manifest.passage_count)
    && manifest.compatibility.source_indices.length === manifest.compatibility.indices.length
    && manifest.compatibility.indices.every((i) => integer(i, 0, manifest.passage_count - 1))
    && manifest.compatibility.source_indices.every((i) => integer(i, 0, manifest.passage_count - 1))
    && new Set(manifest.compatibility.indices).size === manifest.compatibility.indices.length,
  'invalid reference sample')
  const loadAsset = (path: string) => {
    const entry = manifest.files[path]
    check(entry, 'unlisted asset: ' + path)
    return fetchBytes(path, entry.sha256, entry.bytes)
  }
  check(manifest.graph_path === `releases/${manifest.release_id}/graph.json`, 'invalid graph path')
  const paperPaths = new Map<string, string>()
  for (const id of manifest.text_paper_ids) {
    check(manifest.paper_ids.includes(id), 'text paper outside graph')
    paperPaths.set(`releases/${manifest.release_id}/papers/${await sha256Hex(id)}.json`, id)
  }
  const paths = [manifest.graph_path, manifest.metadata.path, manifest.index.norms_path,
    manifest.compatibility.path, ...manifest.index.shards.map((s) => s.path), ...paperPaths.keys()]
  check(new Set(paths).size === paths.length
    && JSON.stringify(paths.sort()) === JSON.stringify(Object.keys(manifest.files).sort()),
  'asset set does not match manifest')
  check(manifest.files[manifest.metadata.path].bytes === manifest.passage_count * 128
    && manifest.files[manifest.index.norms_path].bytes === manifest.passage_count * 8
    && manifest.files[manifest.compatibility.path].bytes === manifest.compatibility.indices.length * 768 * 4,
  'binary layout byte length mismatch')
  const graphRaw = parse(await loadAsset(manifest.graph_path))
  check(object(graphRaw) && object(graphRaw.nodes) && object(graphRaw.out) && object(graphRaw.in), 'invalid graph')
  const graph = graphRaw as unknown as GraphDoc
  sample('graph-parsed')
  for (const map of [graph.nodes, graph.out, graph.in]) {
    check(JSON.stringify(Object.keys(map).sort()) === JSON.stringify(manifest.paper_ids), 'graph node set mismatch')
  }
  const out: string[] = [], incoming: string[] = []
  for (const id of manifest.paper_ids) {
    const card = graph.nodes[id]
    const available = manifest.text_paper_ids.includes(id)
    check(object(card) && card.id === id && typeof card.title === 'string'
      && object(card.text) && card.text.available === available
      && integer(card.text.code_points, 0, 10000000) && integer(card.text.chunks, 0, manifest.passage_count)
      && (available ? card.text.reason === null && card.text.chunks > 0
        : typeof card.text.reason === 'string' && card.text.chunks === 0 && card.text.code_points === 0),
    'invalid graph card')
    for (const [dir, adjacency] of [['out', graph.out[id]], ['in', graph.in[id]]] as const) {
      check(Array.isArray(adjacency), 'invalid adjacency')
      for (const edge of adjacency) {
        check(object(edge), 'invalid graph edge')
        const neighbor = dir === 'out' ? (edge as { target: string }).target : (edge as { source: string }).source
        check(typeof neighbor === 'string' && Object.hasOwn(graph.nodes, neighbor)
          && ['id', 'title', 'url'].includes(edge.evidence), 'dangling graph edge')
        ;(dir === 'out' ? out : incoming).push(JSON.stringify(dir === 'out'
          ? [id, neighbor, edge.evidence] : [neighbor, id, edge.evidence]))
      }
    }
  }
  check(JSON.stringify(out.sort()) === JSON.stringify(incoming.sort()), 'reverse edges mismatch')
  freeze(graph)
  const metadata = await loadAsset(manifest.metadata.path)
  const bytes = new Uint8Array(metadata), view = new DataView(metadata)
  sample('metadata-loaded', metadata.byteLength)
  const readRow = (index: number): FullCorpusRow => {
    check(integer(index, 0, manifest.passage_count - 1), 'row outside index')
    const at = index * 128
    return { id: hex(bytes.subarray(at, at + 32)),
      paper_id: manifest.paper_ids[view.getUint32(at + 32, true)],
      chunk_index: view.getUint32(at + 36, true), start: view.getUint32(at + 40, true),
      end: view.getUint32(at + 44, true), token_count: view.getUint32(at + 48, true),
      sourceIndex: view.getUint32(at + 52, true), content_hash: hex(bytes.subarray(at + 56, at + 88)),
      input_hash: hex(bytes.subarray(at + 88, at + 120)) }
  }
  const rowIndex = (id: string): number => {
    if (!HASH.test(id)) return -1
    // Lowercase hexadecimal order equals unsigned big-endian word order.
    // Decode the requested key once instead of allocating a 64-character
    // candidate string at every binary-search comparison.
    const key = new Uint32Array(8)
    for (let word = 0; word < key.length; word++) {
      key[word] = Number.parseInt(id.slice(word * 8, word * 8 + 8), 16)
    }
    let low = 0, high = manifest.passage_count - 1
    while (low <= high) {
      const mid = (low + high) >>> 1
      let order = 0
      for (let word = 0; word < key.length; word++) {
        const candidate = view.getUint32(mid * 128 + word * 4, false)
        if (candidate !== key[word]) { order = candidate < key[word] ? -1 : 1; break }
      }
      if (order === 0) return mid
      if (order < 0) low = mid + 1
      else high = mid - 1
    }
    return -1
  }
  // Only small temporary bitsets: no 40K JS row objects or ID->row map.
  const sourceStarts = new Map<string, number>()
  let sourceCount = 0
  for (const id of manifest.text_paper_ids) {
    sourceStarts.set(id, sourceCount)
    sourceCount += graph.nodes[id].text.chunks
  }
  check(sourceCount === manifest.passage_count, 'canonical chunk count mismatch')
  const sourceSeen = new Uint8Array(manifest.passage_count)
  const chunksSeen = new Map(manifest.text_paper_ids.map((id) => [id, new Uint8Array(graph.nodes[id].text.chunks)]))
  let previousId = ''
  for (let i = 0; i < manifest.passage_count; i++) {
    const row = readRow(i), seen = chunksSeen.get(row.paper_id)
    check(row.id > previousId && seen && row.chunk_index < seen.length && !seen[row.chunk_index]
      && row.sourceIndex < manifest.passage_count && !sourceSeen[row.sourceIndex]
      && row.sourceIndex === sourceStarts.get(row.paper_id)! + row.chunk_index
      && row.start < row.end && row.end <= graph.nodes[row.paper_id].text.code_points
      && row.end - row.start <= embed.max_code_points
      && integer(row.token_count, 2, embed.max_input_tokens)
      && bytes.subarray(i * 128 + 120, i * 128 + 128).every((value) => value === 0), 'invalid packed row')
    seen[row.chunk_index] = 1
    sourceSeen[row.sourceIndex] = 1
    previousId = row.id
  }
  check([...chunksSeen.values()].every((seen) => seen.every(Boolean)), 'missing canonical chunk row')
  for (let i = 0; i < manifest.compatibility.indices.length; i++) {
    check(readRow(manifest.compatibility.indices[i]).sourceIndex === manifest.compatibility.source_indices[i],
      'reference sample mapping mismatch')
  }
  const index = await FullSearchIndex.load(manifest, loadAsset, options.module, (value) => {
    residentIndexBytes = value.resident_index_bytes
    options.memorySample?.(value)
  })
  // A property lookup view preserves CorpusStore's confirmed map contract
  // without materializing 40K string-keyed JS objects. It is immutable; only
  // bracket reads are used by the production service. No request-local cache.
  const mappings = new Proxy(Object.create(null) as ConfirmedDoc['vectors'], {
    get(_target, key) {
      if (typeof key !== 'string') return undefined
      const i = rowIndex(key)
      if (i < 0) return undefined
      const row = readRow(i)
      return Object.freeze({ paper_id: row.paper_id, chunk_index: row.chunk_index,
        content_hash: row.content_hash, input_hash: row.input_hash })
    },
    set: () => false, defineProperty: () => false, deleteProperty: () => false,
  })
  const confirmed: ConfirmedDoc = Object.freeze({ release_id: manifest.release_id,
    embedding_signature: manifest.embedding_signature, build_signature: manifest.build_signature,
    passage_count: manifest.passage_count, vectors: mappings })
  const now = Date.now()
  const pointer: ActivePointer = Object.freeze({ release_id: manifest.release_id, slot: manifest.slot,
    activated_at: now, reader_schema: embed.reader_schema, embedding_signature: manifest.embedding_signature,
    build_signature: manifest.build_signature, verified_passage_count: manifest.passage_count,
    global_index_count: manifest.passage_count,
    publication_check: { ok: true, checked_at: now, by: 'isolated-full-probe' } })
  const pending = new Map<string, Promise<PaperDoc>>()
  // CorpusCache bounds retained papers after loading, not concurrent fetches.
  // Serialize distinct paper validation to bound transient decoded text and
  // hash buffers as well; queued jobs retain only their path/ID strings.
  let paperQueue: Promise<void> = Promise.resolve()
  let activePapers = 0, peakActivePapers = 0, rejectedPapers = 0
  const paper = async (path: string, id: string): Promise<PaperDoc> => {
    const doc = parse(await loadAsset(path))
    sample('paper-parsed:' + id)
    check(object(doc) && doc.paper_id === id && typeof doc.text === 'string'
      && Array.isArray(doc.chunks), 'invalid paper document')
    const card = graph.nodes[id].text
    check(doc.chunks.length === card.chunks && card.object === await sha256Hex(id), 'paper card mismatch')
    // Only record chunk-boundary UTF16 positions; no Array.from(whole paper)
    // and no per-code-point lookup table survives validation.
    const boundaries = new Map<number, number>()
    for (const chunk of doc.chunks) {
      check(object(chunk) && integer(chunk.start, 0, card.code_points - 1)
        && integer(chunk.end, chunk.start + 1, card.code_points), 'invalid chunk boundaries')
      boundaries.set(chunk.start, -1); boundaries.set(chunk.end, -1)
    }
    let points = 0, units = 0
    // Scan numeric positions without allocating one string/iterator result
    // per code point on every cache miss, including large papers.
    while (units < doc.text.length) {
      if (boundaries.has(points)) boundaries.set(points, units)
      units += doc.text.codePointAt(units)! > 0xffff ? 2 : 1
      points++
    }
    boundaries.set(points, units)
    check(points === card.code_points, 'paper code-point count mismatch')
    let covered = 0, previousStart = -1
    for (let i = 0; i < doc.chunks.length; i++) {
      const chunk = doc.chunks[i] as PaperDoc['chunks'][number]
      const rowAt = rowIndex(await vectorIdOf(manifest.slot, id, i))
      check(rowAt >= 0, 'canonical chunk missing from packed rows')
      const row = readRow(rowAt)
      check(chunk.index === i && chunk.start > previousStart && chunk.start <= covered
        && covered - chunk.start <= embed.overlap_code_points
        && row.paper_id === id && row.chunk_index === i && row.start === chunk.start && row.end === chunk.end
        && row.token_count === chunk.token_count && row.content_hash === chunk.content_hash
        && row.input_hash === chunk.input_hash, 'canonical chunk does not match packed row')
      const passage = doc.text.slice(boundaries.get(chunk.start)!, boundaries.get(chunk.end)!)
      check(await sha256Hex(passage) === chunk.content_hash
        && await sha256Hex(canonicalJson({ embedding_signature: manifest.embedding_signature,
          input: embed.passage_template + passage })) === chunk.input_hash, 'canonical passage hash mismatch')
      covered = Math.max(covered, chunk.end); previousStart = chunk.start
    }
    check(covered === points, 'incomplete canonical paper')
    return freeze(doc as unknown as PaperDoc)
  }
  const getPaper = (path: string, id: string) => {
    const existing = pending.get(path)
    if (existing) return existing
    if (pending.size >= PAPER_LOAD_LIMITS.active + PAPER_LOAD_LIMITS.queued) {
      rejectedPapers++
      return Promise.reject(new DomainError('overloaded', 503, 'Full corpus paper validation queue is full'))
    }
    const promise = paperQueue.then(async () => {
      activePapers++
      peakActivePapers = Math.max(peakActivePapers, activePapers)
      try { return await paper(path, id) }
      finally { activePapers-- }
    }).finally(() => pending.delete(path))
    paperQueue = promise.then(() => undefined, () => undefined)
    pending.set(path, promise)
    return promise
  }
  freeze(manifest)
  const store: CorpusStore = {
    now: () => Date.now(), embed: embedder, rateLimit: limiter,
    async getJson(path) {
      if (path === 'active.json') return pointer
      if (path === `slots/${manifest.slot}/confirmed.json`) return confirmed
      if (path === manifest.graph_path) return graph
      const id = paperPaths.get(path)
      return id ? getPaper(path, id) : null
    },
    async query(namespace, vector, k) {
      check(namespace === manifest.slot, 'wrong vector namespace')
      return index.search(vector, k).map((hit) => ({ id: readRow(hit.index).id, score: hit.score }))
    },
  }
  let references: Promise<ArrayBuffer> | undefined
  return { store, manifest, index, readRow,
    paperLoadStats: () => ({ active: activePapers, queued: Math.max(0, pending.size - 1),
      pending: pending.size, peak_active: peakActivePapers, rejected: rejectedPapers,
      max_active: PAPER_LOAD_LIMITS.active, max_queued: PAPER_LOAD_LIMITS.queued }),
    residentBinaryBytes: metadata.byteLength + index.residentBytes,
    async referencePassage(sampleIndex: number) {
      check(integer(sampleIndex, 0, manifest.compatibility.indices.length - 1), 'reference sample outside index')
      references ??= loadAsset(manifest.compatibility.path)
      const buffer = await references
      const reference = new DataView(buffer, sampleIndex * 768 * 4, 768 * 4)
      const vector = Array.from({ length: 768 }, (_, dim) => reference.getFloat32(dim * 4, true))
      check(vector.every(Number.isFinite)
        && Math.abs(Math.sqrt(vector.reduce((sum, v) => sum + v * v, 0)) - 1) <= 1e-4,
      'invalid FP32 reference vector')
      const row = readRow(manifest.compatibility.indices[sampleIndex])
      const doc = await getPaper(`releases/${manifest.release_id}/papers/${await sha256Hex(row.paper_id)}.json`, row.paper_id)
      let position = 0, input = ''
      for (const point of doc.text) {
        if (position >= row.end) break
        if (position++ >= row.start) input += point
      }
      return { row, vector, input: embed.passage_template + input }
    },
  }
}
