import type { ActivePointer, ConfirmedDoc, CorpusStore, GraphDoc, PaperDoc } from './corpus'
import { fail } from './schemas'
import { canonicalJson, sha256Hex, signatures, vectorIdOf } from './signatures'
import { embed } from './tokenize'

export interface RealProbeRow {
  id: string
  paper_id: string
  chunk_index: number
  start: number
  end: number
  token_count: number
  content_hash: string
  input_hash: string
}

export interface RealProbeManifest {
  schema_version: number
  reader_schema: number
  kind: 'real-subset'
  synthetic: false
  publication_ready: false
  scope: 'isolated-integration-subset-not-full-corpus'
  dimensions: number
  slot: string
  release_id: string
  embedding_signature: string
  build_signature: string
  passage_count: number
  paper_ids: string[]
  sample_paper_id: string
  rows: RealProbeRow[]
  files: Record<string, string>
  compatibility_indices: number[]
  queries: { id: string, query: string, expected_paper_id: string }[]
  embeddings: {
    path: string
    sha256: string
    model_id: string
    model_revision: string
    pooling: string
    normalization: string
    dtype: string
    byte_order: string
    dimensions: number
    count: number
  }
  [key: string]: unknown
}

export interface StaticCorpusAssets {
  fetch(request: Request): Promise<Response>
}

export interface StaticCorpusBundle {
  store: CorpusStore
  manifest: RealProbeManifest
  referencePassage(index: number): { input: string, vector: number[], row: RealProbeRow }
}

const HASH = /^[a-f0-9]{64}$/
const MAX_FILE_BYTES = 4 * 1024 * 1024
const MAX_TOTAL_BYTES = 12 * 1024 * 1024

function requireValue(condition: unknown, message: string): asserts condition {
  if (!condition) fail('config_mismatch', 503, 'Real subset: ' + message)
}

function isObject(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === 'object' && !Array.isArray(value)
}

function integer(value: unknown, min: number, max: number): value is number {
  return Number.isSafeInteger(value) && Number(value) >= min && Number(value) <= max
}

function hash(value: unknown): value is string {
  return typeof value === 'string' && HASH.test(value)
}

function freeze<T>(value: T): T {
  if (value && typeof value === 'object' && !Object.isFrozen(value)) {
    for (const child of Object.values(value)) freeze(child)
    Object.freeze(value)
  }
  return value
}

async function bytesHash(bytes: ArrayBuffer): Promise<string> {
  const digest = await crypto.subtle.digest('SHA-256', bytes)
  return Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, '0')).join('')
}

function parseJson(bytes: ArrayBuffer): unknown {
  try {
    return JSON.parse(new TextDecoder('utf-8', { fatal: true, ignoreBOM: false }).decode(bytes))
  } catch {
    fail('config_mismatch', 503, 'Real subset: invalid JSON asset')
  }
}

function validateManifest(raw: unknown): RealProbeManifest {
  requireValue(isObject(raw), 'manifest must be an object')
  requireValue(raw.schema_version === 1 && raw.reader_schema === embed.reader_schema
    && raw.kind === 'real-subset' && raw.publication_ready === false
    && raw.scope === 'isolated-integration-subset-not-full-corpus'
    && raw.synthetic === false && raw.dimensions === embed.dimensions
    && raw.slot === 'real-probe', 'unsupported manifest or subset scope')
  requireValue(hash(raw.release_id) && hash(raw.embedding_signature)
    && hash(raw.build_signature), 'invalid release signatures')
  requireValue(integer(raw.passage_count, 200, 500), 'expected 200–500 canonical passages')
  requireValue(Array.isArray(raw.paper_ids) && raw.paper_ids.length > 0
    && raw.paper_ids.length <= raw.passage_count
    && raw.paper_ids.every((id) => typeof id === 'string' && id.length > 0)
    && new Set(raw.paper_ids).size === raw.paper_ids.length, 'invalid paper IDs')
  requireValue(raw.paper_ids.includes(raw.sample_paper_id), 'sample paper is outside subset')
  requireValue(Array.isArray(raw.rows) && raw.rows.length === raw.passage_count,
    'passage row count disagrees with manifest')
  requireValue(isObject(raw.files) && Object.entries(raw.files).every(([path, digest]) =>
    /^[a-zA-Z0-9_./-]+$/.test(path) && !path.startsWith('/')
    && !path.split('/').some((part) => part === '.' || part === '..' || !part)
    && hash(digest)), 'invalid asset map')
  const vectors = raw.embeddings
  requireValue(isObject(vectors) && vectors.path === 'vectors.f32'
    && hash(vectors.sha256) && raw.files[vectors.path] === vectors.sha256
    && vectors.model_id === embed.tokenizer.id
    && vectors.model_revision === embed.tokenizer.revision
    && vectors.pooling === 'cls' && vectors.normalization === 'l2'
    && vectors.dtype === 'float32' && vectors.byte_order === 'little'
    && vectors.dimensions === embed.dimensions && vectors.count === raw.passage_count,
  'missing or incompatible FP32 embeddings')
  requireValue(Array.isArray(raw.compatibility_indices)
    && raw.compatibility_indices.length === 200
    && raw.compatibility_indices.every((index) => integer(index, 0, Number(raw.passage_count) - 1))
    && new Set(raw.compatibility_indices).size === 200, 'invalid compatibility sample')
  requireValue(Array.isArray(raw.queries) && raw.queries.length > 0
    && raw.queries.every((query) => isObject(query) && typeof query.id === 'string'
      && typeof query.query === 'string' && query.query.trim().length > 0
      && (raw.paper_ids as unknown[]).includes(query.expected_paper_id)), 'invalid query fixtures')
  return raw as unknown as RealProbeManifest
}

function validateGraph(raw: unknown, paperIds: string[]): GraphDoc {
  requireValue(isObject(raw) && isObject(raw.nodes) && isObject(raw.out)
    && isObject(raw.in), 'invalid graph')
  const expected = JSON.stringify([...paperIds].sort())
  for (const map of [raw.nodes, raw.out, raw.in]) {
    requireValue(JSON.stringify(Object.keys(map).sort()) === expected, 'graph node set disagrees with subset')
  }
  const edges: string[] = []
  const reverse: string[] = []
  for (const id of paperIds) {
    const node = raw.nodes[id]
    requireValue(isObject(node) && node.id === id && typeof node.title === 'string'
      && Array.isArray(node.authors) && node.authors.every((author) => typeof author === 'string')
      && isObject(node.text) && node.text.available === true && node.text.reason === null,
    'invalid complete-paper card')
    for (const [direction, map] of [['out', raw.out], ['in', raw.in]] as const) {
      const adjacency = map[id]
      requireValue(Array.isArray(adjacency), 'invalid graph adjacency')
      for (const edge of adjacency) {
        requireValue(isObject(edge), 'invalid graph edge')
        const neighbor = edge[direction === 'out' ? 'target' : 'source']
        requireValue(typeof neighbor === 'string' && paperIds.includes(neighbor)
          && ['id', 'title', 'url'].includes(String(edge.evidence)), 'dangling graph edge')
        const tuple = direction === 'out' ? [id, neighbor, edge.evidence] : [neighbor, id, edge.evidence]
        ;(direction === 'out' ? edges : reverse).push(JSON.stringify(tuple))
      }
    }
  }
  requireValue(JSON.stringify(edges.sort()) === JSON.stringify(reverse.sort()),
    'incoming and outgoing graph edges disagree')
  return raw as unknown as GraphDoc
}

/** Load one pinned, isolated subset. Callers share this promise within their DO. */
export async function createStaticCorpusStore(
  assets: StaticCorpusAssets,
  expectedManifestHash: string,
  embedder: (text: string) => Promise<number[]>,
  limiter: (key: string) => Promise<boolean> = async () => true,
): Promise<StaticCorpusBundle> {
  requireValue(hash(expectedManifestHash), 'manifest hash must be pinned')
  let loadedBytes = 0
  // The pinned asset set is read once during the shared initialization. Do not
  // keep resolved byte-buffer promises alongside the parsed resident corpus.
  const load = async (path: string, digest: string): Promise<ArrayBuffer> => {
    const response = await assets.fetch(new Request('https://real-probe-assets.invalid/' + path))
    requireValue(response.status === 200, 'asset is missing: ' + path)
    const declared = response.headers.get('content-length')
    const limit = Math.min(MAX_FILE_BYTES, MAX_TOTAL_BYTES - loadedBytes)
    const validLength = declared === null || (/^\d+$/.test(declared)
      && Number.isSafeInteger(Number(declared)) && Number(declared) <= limit)
    if (!validLength) {
      if (response.body) void response.body.cancel().catch(() => {})
      requireValue(false, 'asset exceeds size bound')
    }
    const reader = response.body?.getReader()
    requireValue(reader, 'asset body is missing')
    const parts: Uint8Array[] = []
    let length = 0, complete = false
    try {
      while (true) {
        const part = await reader.read()
        if (part.done) { complete = true; break }
        requireValue(length + part.value.byteLength <= limit && parts.length < 1024,
          'assets exceed subset size bound')
        parts.push(part.value)
        length += part.value.byteLength
      }
    } finally {
      if (!complete) void reader.cancel().catch(() => {})
      reader.releaseLock()
    }
    const output = new Uint8Array(length)
    let offset = 0
    for (const part of parts) { output.set(part, offset); offset += part.byteLength }
    const bytes = output.buffer
    loadedBytes += length
    requireValue(await bytesHash(bytes) === digest, 'asset checksum mismatch: ' + path)
    return bytes
  }
  const manifest = validateManifest(parseJson(await load('probe.json', expectedManifestHash)))
  const local = await signatures()
  requireValue(manifest.embedding_signature === local.embedding
    && manifest.build_signature === local.build, 'reader signatures disagree with subset')
  const graphPath = `releases/${manifest.release_id}/graph.json`
  const paperPaths = new Map<string, string>()
  for (const id of manifest.paper_ids) {
    paperPaths.set(id, `releases/${manifest.release_id}/papers/${await sha256Hex(id)}.json`)
  }
  const expectedPaths = [graphPath, 'vectors.f32', ...paperPaths.values()].sort()
  requireValue(JSON.stringify(Object.keys(manifest.files).sort()) === JSON.stringify(expectedPaths),
    'asset map must contain exactly the subset graph, papers and vectors')
  const graph = validateGraph(parseJson(await load(graphPath, manifest.files[graphPath])), manifest.paper_ids)
  const objects = new Map<string, unknown>([[graphPath, graph]])
  const texts = new Map<string, string[]>()
  const chunkByKey = new Map<string, PaperDoc['chunks'][number]>()
  for (const id of manifest.paper_ids) {
    const path = paperPaths.get(id)!
    const raw = parseJson(await load(path, manifest.files[path]))
    requireValue(isObject(raw) && raw.paper_id === id && typeof raw.text === 'string'
      && Array.isArray(raw.chunks) && raw.chunks.length > 0, 'invalid paper asset')
    const points = Array.from(raw.text)
    const card = graph.nodes[id].text
    requireValue(card.code_points === points.length && card.chunks === raw.chunks.length
      && card.object === await sha256Hex(id), 'paper card does not match canonical text')
    let covered = 0
    let previousStart = -1
    for (let index = 0; index < raw.chunks.length; index++) {
      const chunk = raw.chunks[index]
      requireValue(isObject(chunk) && chunk.index === index
        && integer(chunk.start, 0, points.length - 1)
        && integer(chunk.end, chunk.start + 1, points.length)
        && chunk.start > previousStart && chunk.start <= covered
        && covered - chunk.start <= embed.overlap_code_points
        && chunk.end - chunk.start <= embed.max_code_points
        && integer(chunk.token_count, 2, embed.max_input_tokens)
        && hash(chunk.content_hash) && hash(chunk.input_hash), 'invalid canonical chunk range')
      const text = points.slice(chunk.start, chunk.end).join('')
      const input = embed.passage_template + text
      requireValue(chunk.content_hash === await sha256Hex(text)
        && chunk.input_hash === await sha256Hex(canonicalJson({
          embedding_signature: manifest.embedding_signature, input,
        })), 'canonical passage hash mismatch')
      chunkByKey.set(JSON.stringify([id, index]), chunk as unknown as PaperDoc['chunks'][number])
      covered = Math.max(covered, chunk.end)
      previousStart = chunk.start
    }
    requireValue(covered === points.length, 'canonical chunks do not cover complete paper')
    objects.set(path, raw)
    texts.set(id, points)
  }
  requireValue(chunkByKey.size === manifest.passage_count, 'canonical passage count mismatch')
  const paperBlob = Object.fromEntries([...paperPaths].map(([id, path]) => [id, objects.get(path)]))
  requireValue(manifest.release_id === await sha256Hex(canonicalJson({
    graph: manifest.files[graphPath], papers: await sha256Hex(canonicalJson(paperBlob)),
    build_signature: manifest.build_signature, embedding_signature: manifest.embedding_signature,
  })), 'release identity does not match canonical corpus')
  const ids = new Set<string>()
  const mappings = new Set<string>()
  const vectorsById: ConfirmedDoc['vectors'] = {}
  for (const row of manifest.rows) {
    requireValue(isObject(row) && typeof row.paper_id === 'string'
      && integer(row.chunk_index, 0, manifest.passage_count - 1), 'invalid vector row')
    const key = JSON.stringify([row.paper_id, row.chunk_index])
    const chunk = chunkByKey.get(key)
    requireValue(chunk && !mappings.has(key) && !ids.has(row.id)
      && row.id === await vectorIdOf(manifest.slot, row.paper_id, row.chunk_index)
      && row.start === chunk.start && row.end === chunk.end
      && row.token_count === chunk.token_count && row.content_hash === chunk.content_hash
      && row.input_hash === chunk.input_hash, 'dangling or inconsistent vector row')
    ids.add(row.id)
    mappings.add(key)
    vectorsById[row.id] = { paper_id: row.paper_id, chunk_index: row.chunk_index,
      content_hash: row.content_hash, input_hash: row.input_hash }
  }
  const binary = await load('vectors.f32', manifest.embeddings.sha256)
  requireValue(binary.byteLength === manifest.passage_count * embed.dimensions * 4,
    'FP32 byte length disagrees with rows')
  const view = new DataView(binary)
  const vectors = new Float32Array(manifest.passage_count * embed.dimensions)
  for (let row = 0; row < manifest.passage_count; row++) {
    let norm = 0
    for (let dim = 0; dim < embed.dimensions; dim++) {
      const index = row * embed.dimensions + dim
      const value = view.getFloat32(index * 4, true)
      requireValue(Number.isFinite(value), 'non-finite FP32 embedding')
      vectors[index] = value
      norm += value * value
    }
    requireValue(Math.abs(Math.sqrt(norm) - 1) <= 1e-4, 'FP32 embedding is not unit normalized')
  }
  const now = Date.now()
  const pointer: ActivePointer = {
    release_id: manifest.release_id, slot: manifest.slot, activated_at: now,
    reader_schema: embed.reader_schema, embedding_signature: manifest.embedding_signature,
    build_signature: manifest.build_signature, verified_passage_count: manifest.passage_count,
    global_index_count: manifest.passage_count,
    // This asserts verified subset integrity only. The authenticated probe is
    // not a production publication, and the runtime separately gates AI compatibility.
    publication_check: { ok: true, checked_at: now, by: 'isolated-real-probe' },
  }
  const confirmed: ConfirmedDoc = {
    release_id: manifest.release_id, embedding_signature: manifest.embedding_signature,
    build_signature: manifest.build_signature, passage_count: manifest.passage_count,
    vectors: vectorsById,
  }
  objects.set('active.json', pointer)
  objects.set(`slots/${manifest.slot}/confirmed.json`, confirmed)
  for (const value of objects.values()) freeze(value)
  freeze(manifest)
  const store: CorpusStore = {
    now: () => Date.now(),
    getJson: async (key) => objects.get(key) ?? null,
    embed: embedder,
    rateLimit: limiter,
    async query(namespace, vector, topK) {
      requireValue(namespace === manifest.slot, 'unknown vector namespace')
      requireValue(Array.isArray(vector) && vector.length === embed.dimensions
        && vector.every((value) => typeof value === 'number' && Number.isFinite(value)),
      'invalid query vector')
      requireValue(integer(topK, 1, 500), 'invalid candidate limit')
      const norm = Math.sqrt(vector.reduce((sum, value) => sum + value * value, 0))
      requireValue(Number.isFinite(norm) && norm > 0, 'query vector has no finite norm')
      const hits = manifest.rows.map((row, index) => {
        let dot = 0
        const offset = index * embed.dimensions
        for (let dim = 0; dim < embed.dimensions; dim++) dot += vectors[offset + dim] * (vector[dim] / norm)
        return { id: row.id, score: dot }
      })
      hits.sort((a, b) => b.score - a.score || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0))
      return hits.slice(0, topK)
    },
  }
  return { store, manifest, referencePassage(index) {
    requireValue(integer(index, 0, manifest.passage_count - 1), 'unknown reference passage')
    const row = manifest.rows[index]
    return {
      input: embed.passage_template + texts.get(row.paper_id)!.slice(row.start, row.end).join(''),
      vector: Array.from(vectors.subarray(index * embed.dimensions, (index + 1) * embed.dimensions)),
      row,
    }
  } }
}
