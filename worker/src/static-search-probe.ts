import { rankedCatalog } from './catalog-search'
import { validProbeToken } from './probe-auth'
import { WasmPqScorer } from './static-search-wasm'
import { Int8Index } from './static-search-int8'
import vocabText from '../tokenizer/vocab.txt'

import { handleRest, json, requestOrigin } from './http'
import { handleMcp } from './mcp'
import { DomainError, errorBody, fail, parseBoundedInt, parseId, parseOffset } from './schemas'
import type { ContentArgs, Service } from './service'
import { PqIndex, type PqConfig, type PqEngine } from './static-search'
import { embed, pointLength, slicePoints, WordPieceTokenizer } from './tokenize'

export interface ProbeEnv {
  ASSETS: { fetch(request: Request): Promise<Response> }
  PQ_WASM?: WebAssembly.Module
  PROBE_TOKEN?: string
  PROBE_EXPIRES_AT?: string
}

interface AssetReference { path: string, bytes?: number }
interface Manifest extends PqConfig {
  synthetic: true
  corpus_version: string
  seed: number
  record_shard_size: number
  text_part_size: number
  codes: AssetReference
  codebooks: AssetReference
  papers: { path: string, count: number }
  records: { path: string, shards: number }
  records_small?: { path: string, shards: number }
  int8?: AssetReference[]
  int8_norms?: AssetReference
  binary?: AssetReference
}
interface Paper {
  section?: string | null
  topic?: string | null
  id: string
  title: string
  url: string | null
  path: string
  available: boolean
  total_length: number
  part_count: number
  corpus_version: string
  synthetic: true
}
interface PaperInfo extends Paper {
  sections: { title: string, level: number, offset: number }[]
}
interface TextPart {
  paper_id: string
  corpus_version: string
  synthetic: true
  offset: number
  total_length: number
  text: string
}
interface RecordRow {
  index: number
  paper_id: string
  title: string
  url: string | null
  chunk_index: number
  start: number
  end: number
  snippet: string
  corpus_version: string
  synthetic: true
}
interface Identity { paper: string, version: string, start: number | null }

const TEXT_PART_SIZE = 16000
const SITE = 'https://vinnik-dmitry07.github.io/favorite-papers'
const SYNTHETIC_TITLE = '[SYNTHETIC RANKING — NOT SEMANTIC] '

class Lru<T> {
  private readonly entries = new Map<string, Promise<T>>()
  constructor(private readonly capacity: number) {}

  get(key: string, load: () => Promise<T>): Promise<T> {
    let value = this.entries.get(key)
    if (value) this.entries.delete(key)
    else {
      value = load().catch((error) => {
        if (this.entries.get(key) === value) this.entries.delete(key)
        throw error
      })
    }
    this.entries.set(key, value)
    while (this.entries.size > this.capacity) {
      this.entries.delete(this.entries.keys().next().value!)
    }
    return value
  }
}

function assetPath(path: string): string {
  if (typeof path !== 'string' || !path.startsWith('/probe/') || /[?#\\]/.test(path)
      || path.split('/').includes('..')) fail('corpus_unavailable', 503, 'invalid probe asset path')
  return path
}

function integer(value: unknown, min = 0, max = Number.MAX_SAFE_INTEGER): value is number {
  return typeof value === 'number' && Number.isSafeInteger(value) && value >= min && value <= max
}

function assetVersion(value: { corpus_version?: unknown, synthetic?: unknown }, manifest: Manifest): void {
  if (!value || value.synthetic !== true || value.corpus_version !== manifest.corpus_version) {
    fail('corpus_unavailable', 503, 'probe assets have inconsistent versions')
  }
}

function checkVersion(version: string | null | undefined, manifest: Manifest): void {
  if (version && version !== manifest.corpus_version) {
    fail('version_conflict', 409, 'probe corpus version changed; restart the query', {
      corpus_version: manifest.corpus_version,
    })
  }
}

function documentId(identity: Identity): string {
  const bytes = new TextEncoder().encode(JSON.stringify(identity))
  return 'probe-doc:' + btoa(Array.from(bytes, (byte) => String.fromCharCode(byte)).join(''))
    .replaceAll('+', '-').replaceAll('/', '_').replaceAll('=', '')
}

function documentIdentity(id: string): Identity {
  try {
    if (typeof id !== 'string' || !id.startsWith('probe-doc:') || id.length > 4096) throw new Error('id')
    const binary = atob(id.slice(10).replaceAll('-', '+').replaceAll('_', '/'))
    const value = JSON.parse(new TextDecoder('utf-8', { fatal: true, ignoreBOM: false }).decode(
      Uint8Array.from(binary, (char) => char.charCodeAt(0)),
    )) as Identity
    if (!value || typeof value.paper !== 'string' || typeof value.version !== 'string' || !value.version
        || !(value.start === null || integer(value.start))) throw new Error('shape')
    return value
  } catch {
    fail('invalid_argument', 400, 'copy the complete probe document id from search or fetch')
  }
}

/** No model call: hashes token IDs into a deterministic synthetic query vector. */
function queryTokens(query: string, tokenizer: WordPieceTokenizer): number[] {
  if (typeof query !== 'string' || !query.trim()) fail('invalid_query', 400, 'query is empty')
  if (pointLength(query) > 2000) fail('query_too_long', 400, 'query exceeds 2000 code points')
  const tokens = tokenizer.tokenIds(embed.query_template, query)
  if (tokens.length > embed.max_input_tokens) fail('query_too_long', 400, 'query exceeds the token budget')
  return tokens
}

function syntheticQuery(tokens: number[], manifest: Manifest): Float32Array {
  let state = (2166136261 ^ manifest.seed) >>> 0
  for (const token of tokens) state = Math.imul(state ^ token, 16777619) >>> 0
  if (!state) state = 1
  const vector = new Float32Array(manifest.dimensions)
  for (let dimension = 0; dimension < vector.length; dimension++) {
    state ^= state << 13
    state ^= state >>> 17
    state ^= state << 5
    vector[dimension] = (state >>> 0) / 2147483648 - 1
  }
  return vector
}

export const VARIANTS = {
  'js-json128': { engine: 'js', small: false, algorithm: 'pq' },
  'js-json16': { engine: 'js', small: true, algorithm: 'pq' },
  'js4-json128': { engine: 'js4', small: false, algorithm: 'pq' },
  'js4-json16': { engine: 'js4', small: true, algorithm: 'pq' },
  'wasm-json128': { engine: 'wasm', small: false, algorithm: 'pq' },
  'wasm-json16': { engine: 'wasm', small: true, algorithm: 'pq' },
  'wasm-rerank100': { engine: 'wasm', small: true, algorithm: 'rerank' },
  'wasm-int8': { engine: 'wasm', small: true, algorithm: 'int8' },
  'wasm-binary200': { engine: 'wasm', small: true, algorithm: 'binary' },
} as const
export type Variant = keyof typeof VARIANTS

export function createProbeService(
  env: ProbeEnv,
  variant: Variant = 'js-json128',
  tokenizerProvider?: () => WordPieceTokenizer,
) {
  const options = VARIANTS[variant]
  // Construct only in the request's owning service, never during gateway module startup.
  let tokenizer: WordPieceTokenizer | undefined
  const getTokenizer = tokenizerProvider ?? (() => tokenizer ??= new WordPieceTokenizer(vocabText))
  let int8Promise: Promise<Int8Index> | undefined
  let manifestPromise: Promise<Manifest> | undefined
  let indexPromise: Promise<PqIndex> | undefined
  let papersPromise: Promise<Map<string, Paper>> | undefined
  const records = new Lru<RecordRow[]>(8)
  const parts = new Lru<TextPart>(16)

  async function asset(path: string): Promise<Response> {
    const response = await env.ASSETS.fetch(new Request('https://assets.local' + assetPath(path)))
    if (!response.ok) fail('corpus_unavailable', 503, 'probe asset is unavailable', { path })
    return response
  }

  async function getJson<T>(path: string): Promise<T> {
    return (await asset(path)).json() as Promise<T>
  }

  function manifest(): Promise<Manifest> {
    if (!manifestPromise) {
      manifestPromise = getJson<Manifest>('/probe/index.json').then((value) => {
        if (!value || value.synthetic !== true || value.format !== 'pq-ip-v1'
            || typeof value.corpus_version !== 'string' || !value.corpus_version
            || !integer(value.count, 1, 1_000_000) || !integer(value.dimensions, 1, 1536)
            || !integer(value.subquantizers, 1, value.dimensions)
            || value.dimensions % value.subquantizers !== 0 || !integer(value.centroids, 1, 256)
            || !integer(value.seed) || value.text_part_size !== TEXT_PART_SIZE
            || !integer(value.record_shard_size, 1, 1024)
            || !integer(value.papers?.count, 1, 10000) || !integer(value.records?.shards, 1)
            || value.records.shards !== Math.ceil(value.count / value.record_shard_size)) {
          fail('corpus_unavailable', 503, 'probe manifest is malformed')
        }
        assetPath(value.codes?.path)
        assetPath(value.codebooks?.path)
        assetPath(value.papers.path)
        assetPath(value.records.path.replace('{shard}', '0'))
        return value
      }).catch((error) => { manifestPromise = undefined; throw error })
    }
    return manifestPromise
  }

  function index(): Promise<PqIndex> {
    if (!indexPromise) {
      indexPromise = manifest().then(async (value) => {
        const [codes, books] = await Promise.all([
          asset(value.codes.path).then((response) => response.arrayBuffer()),
          asset(value.codebooks.path).then((response) => response.arrayBuffer()),
        ])
        return new PqIndex(value, codes, books, options.engine === 'wasm' && env.PQ_WASM ? new WasmPqScorer(env.PQ_WASM) : undefined)
      }).catch((error) => { indexPromise = undefined; throw error })
    }
    return indexPromise
  }

  async function int8(): Promise<Int8Index> {
    if (!int8Promise) int8Promise = manifest().then(async (value) => {
      if (!env.PQ_WASM || !value.int8?.length || !value.int8_norms || !value.binary) {
        fail('corpus_unavailable', 503, 'int8 fixture or WASM module missing')
      }
      const load = (ref: AssetReference) => asset(ref.path).then((response) => response.arrayBuffer())
      const [vectors, norms, bits] = await Promise.all([
        Promise.all(value.int8.map(load)), load(value.int8_norms), load(value.binary),
      ])
      return new Int8Index(env.PQ_WASM, value.count, value.dimensions, vectors, norms, bits)
    }).catch((error) => { int8Promise = undefined; throw error })
    return int8Promise
  }

  async function rank(query: Float32Array, topK = 200) {
    if (options.algorithm === 'int8' || options.algorithm === 'binary') {
      return (await int8()).search(query, topK, undefined, options.algorithm === 'binary')
    }
    const hits = (await index()).search(query, options.algorithm === 'rerank' ? 100 : topK, options.engine as PqEngine)
    return options.algorithm === 'rerank'
      ? (await int8()).search(query, topK, hits.map((hit) => hit.index)) : hits
  }

  async function catalog(query: string) {
    return rankedCatalog(Object.fromEntries(await papers()), query)
  }

  function papers(): Promise<Map<string, Paper>> {
    if (!papersPromise) {
      papersPromise = manifest().then(async (value) => {
        const rows = await getJson<Paper[]>(value.papers.path)
        if (!Array.isArray(rows) || rows.length !== value.papers.count) {
          fail('corpus_unavailable', 503, 'probe paper catalog is malformed')
        }
        const result = new Map<string, Paper>()
        for (const row of rows) {
          assetVersion(row, value)
          if (typeof row.id !== 'string' || !row.id || typeof row.title !== 'string'
              || !(row.url === null || typeof row.url === 'string') || typeof row.available !== 'boolean'
              || !integer(row.total_length) || !integer(row.part_count)
              || row.part_count !== (row.available ? Math.ceil(row.total_length / TEXT_PART_SIZE) : 0)
              || result.has(row.id)) fail('corpus_unavailable', 503, 'invalid probe paper metadata')
          assetPath(row.path)
          result.set(row.id, row)
        }
        return result
      }).catch((error) => { papersPromise = undefined; throw error })
    }
    return papersPromise
  }

  async function paper(id: string): Promise<Paper> {
    const row = (await papers()).get(parseId(id))
    if (!row) fail('unknown_id', 404, 'catalog id was not found', { id })
    return row
  }

  function paperUrl(row: Paper): string {
    return `${SITE}/agents/papers/${row.path.split('/')[3]}/`
  }

  async function record(rowIndex: number, value: Manifest): Promise<RecordRow> {
    const size = options.small ? 16 : value.record_shard_size
    const source = options.small ? value.records_small : value.records
    if (!source || source.shards !== Math.ceil(value.count / size)) fail('corpus_unavailable', 503, 'missing metadata layout')
    const shard = Math.floor(rowIndex / size)
    const path = source.path.replace('{shard}', String(shard))
    const rows = await records.get(path, async () => {
      const result = await getJson<RecordRow[]>(path)
      const expected = Math.min(size, value.count - shard * size)
      if (!Array.isArray(result) || result.length !== expected) {
        fail('corpus_unavailable', 503, 'probe record shard is malformed')
      }
      return result
    })
    const row = rows[rowIndex % size]
    assetVersion(row, value)
    if (row.index !== rowIndex || typeof row.paper_id !== 'string' || typeof row.title !== 'string'
        || !integer(row.start) || !integer(row.end, row.start) || !integer(row.chunk_index)
        || typeof row.snippet !== 'string' || row.snippet.length > 3200
        || !(row.url === null || typeof row.url === 'string')) {
      fail('corpus_unavailable', 503, 'probe record is malformed')
    }
    return row
  }

  async function textPart(row: Paper, part: number, value: Manifest): Promise<TextPart> {
    const path = row.path.replace(/paperinfo\.json$/, `parts/${part}.json`)
    return parts.get(path, async () => {
      const result = await getJson<TextPart>(path)
      assetVersion(result, value)
      const start = (part - 1) * TEXT_PART_SIZE
      if (result.paper_id !== row.id || result.offset !== start || result.total_length !== row.total_length
          || typeof result.text !== 'string'
          || pointLength(result.text) !== Math.min(TEXT_PART_SIZE, row.total_length - start)) {
        fail('corpus_unavailable', 503, 'probe text part is malformed')
      }
      return result
    })
  }

  async function span(row: Paper, start: number, end: number, value: Manifest): Promise<string> {
    if (start === end) return ''
    const first = Math.floor(start / TEXT_PART_SIZE) + 1
    const last = Math.floor((end - 1) / TEXT_PART_SIZE) + 1
    if (last - first >= 3) fail('invalid_argument', 400, 'probe text reads are limited to three parts')
    const selected: Promise<TextPart>[] = []
    for (let part = first; part <= last; part++) selected.push(textPart(row, part, value))
    const text = (await Promise.all(selected)).map((part) => part.text).join('')
    return slicePoints(text, start - (first - 1) * TEXT_PART_SIZE, end - (first - 1) * TEXT_PART_SIZE)
  }

  async function content(args: ContentArgs): Promise<Awaited<ReturnType<Service['content']>>> {
    const value = await manifest()
    checkVersion(args.version, value)
    const row = await paper(args.id)
    const offset = parseOffset(args.offset)
    const length = parseBoundedInt(args.length, 6000, 1, 32000, 'length')
    if (!row.available) {
      return { corpus_version: value.corpus_version, paper_id: row.id, available: false,
        reason: 'no_markdown', offset: 0, next_offset: null, total_length: 0, text: '' }
    }
    if (offset > row.total_length) fail('invalid_offset', 400, 'offset is past the text')
    const end = Math.min(row.total_length, offset + length)
    return { corpus_version: value.corpus_version, paper_id: row.id, available: true,
      reason: null, offset,
      next_offset: end < row.total_length ? end : null, total_length: row.total_length,
      text: await span(row, offset, end, value) }
  }

  async function unsupported(): Promise<never> {
    fail('probe_unsupported', 501, 'this operation is outside the isolated synthetic runtime probe')
  }

  // MCP search validates/tokenizes and ranks catalog candidates before it
  // calls passage search. Reuse those values rather than repeating both tasks.
  const performSearch = async (
    args: Parameters<Service['search']>[0],
    validatedTokens?: number[],
    precomputedCatalog?: Awaited<ReturnType<typeof catalog>>,
  ): ReturnType<Service['search']> => {
    const k = parseBoundedInt(args.k, 5, 1, 8, 'k')
    const value = await manifest()
    const query = syntheticQuery(validatedTokens ?? queryTokens(args.q, getTokenizer()), value)
    const ranked = await rank(query)
    const metadata = precomputedCatalog ?? await catalog(args.q)
    const hits: Awaited<ReturnType<Service['search']>>['hits'] = []
    const seen = new Set<string>()
    for (const match of ranked) {
      const row = await record(match.index, value)
      if (seen.has(row.paper_id)) continue
      seen.add(row.paper_id)
      const params = new URLSearchParams({ id: row.paper_id, offset: String(row.start),
        version: value.corpus_version })
      hits.push({ paper_id: row.paper_id, title: SYNTHETIC_TITLE + row.title, url: row.url,
        chunk_index: row.chunk_index, score: match.score, snippet: slicePoints(row.snippet, 0, 480),
        start: row.start, end: row.end, corpus_version: value.corpus_version,
        content: `/v1/content?${params}` })
      if (hits.length >= k) break
    }
    return { corpus_version: value.corpus_version, k, hits, metadata_hits: metadata.slice(0, k).map(({ node }) => ({
      id: node.id, title: node.title, url: node.url, date: null,
      section: node.section ?? null, quality: null, text_available: node.available,
    })) }
  }

  const service: Service = {
    health: unsupported, paper: unsupported, catalog: unsupported,
    citations: unsupported, traverse: unsupported,
    content,
    async contents(id, version) {
      const value = await manifest()
      checkVersion(version, value)
      const row = await paper(id)
      const info = await getJson<PaperInfo>(row.path)
      assetVersion(info, value)
      if (info.id !== row.id || info.total_length !== row.total_length || !Array.isArray(info.sections)
          || info.sections.length > 10000 || info.sections.some((section) => (
            typeof section.title !== 'string' || !integer(section.level, 1, 6)
            || !integer(section.offset, 0, row.total_length)
          ))) fail('corpus_unavailable', 503, 'probe contents are malformed')
      return { corpus_version: value.corpus_version, paper_id: row.id, available: row.available,
        reason: row.available ? null : 'no_markdown', total_length: row.total_length, sections: info.sections }
    },
    async find(args) {
      const value = await manifest()
      checkVersion(args.version, value)
      if (typeof args.q !== 'string' || !args.q.trim() || pointLength(args.q) > 200) {
        fail('invalid_query', 400, 'find query must be 1..200 code points')
      }
      const row = await paper(args.id)
      const offset = parseOffset(args.offset)
      if (offset > row.total_length) fail('invalid_offset', 400, 'offset is past the text')
      const scanEnd = Math.min(row.total_length, offset + TEXT_PART_SIZE)
      const end = Math.min(row.total_length, scanEnd + pointLength(args.q) - 1)
      const text = row.available ? await span(row, offset, end, value) : ''
      const pattern = new RegExp(args.q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'giu')
      const matches: { start: number, end: number, snippet: string }[] = []
      let previousUnit = 0
      let previousPoint = 0
      let next: number | null = scanEnd < row.total_length ? scanEnd : null
      for (let match = pattern.exec(text); match; match = pattern.exec(text)) {
        const localStart = previousPoint + pointLength(text.slice(previousUnit, match.index))
        const start = offset + localStart
        if (start >= scanEnd) break
        if (matches.length === 12) { next = start; break }
        const matchEnd = start + pointLength(match[0])
        matches.push({ start, end: matchEnd,
          snippet: slicePoints(text, Math.max(0, localStart - 120), Math.max(0, localStart - 120) + 480) })
        previousUnit = match.index + match[0].length
        previousPoint = matchEnd - offset
        if (next !== null) next = Math.max(next, matchEnd)
      }
      if (next !== null && next >= row.total_length) next = null
      return { corpus_version: value.corpus_version, paper_id: row.id, available: row.available,
        matches, next_offset: next }
    },
    search: performSearch,
    async researchSearch(query, ip) {
      const validatedTokens = queryTokens(query, getTokenizer())
      // Include the same catalog prepass as the production MCP path.
      const candidates = await catalog(query)
      const exact = candidates.filter(({ score }) => score === 100)
      if (exact.length) {
        const value = await manifest()
        return { results: exact.slice(0, 8).map(({ node }) => ({
          id: documentId({ paper: node.id, version: value.corpus_version, start: node.available ? 0 : null }),
          title: SYNTHETIC_TITLE + node.title, url: node.url || paperUrl(node),
        })) }
      }
      const result = await performSearch({ q: query, k: 5, ip }, validatedTokens, candidates)
      const metadataResults = candidates.slice(0, 3).map(({ node }) => ({
        id: documentId({ paper: node.id, version: result.corpus_version, start: null }),
        title: SYNTHETIC_TITLE + node.title + ' (catalog record)', url: paperUrl(node),
      }))
      const passageResults = await Promise.all(result.hits.map(async (hit) => {
        const row = await paper(hit.paper_id)
        const start = Math.floor(hit.start / TEXT_PART_SIZE) * TEXT_PART_SIZE
        return { id: documentId({ paper: row.id, version: result.corpus_version, start }),
          title: `${hit.title} (text part ${start / TEXT_PART_SIZE + 1})`, url: row.url || paperUrl(row) }
      }))
      return { results: [...metadataResults, ...passageResults] }
    },
    async fetchDocument(id) {
      const identity = documentIdentity(id)
      const value = await manifest()
      checkVersion(identity.version, value)
      const row = await paper(identity.paper)
      const url = paperUrl(row)
      if (identity.start === null) {
        return { id, title: SYNTHETIC_TITLE + row.title, text: `${row.title}\nFull text available: ${row.available}`,
          url, metadata: { paper_id: row.id, corpus_version: value.corpus_version,
            item_type: 'catalog', text_available: row.available,
            first_text_id: row.available ? documentId({ ...identity, start: 0 }) : null } }
      }
      if (!row.available || identity.start >= row.total_length || identity.start % TEXT_PART_SIZE !== 0) {
        fail('invalid_offset', 400, 'fetch part is outside the document')
      }
      const end = Math.min(row.total_length, identity.start + TEXT_PART_SIZE)
      return { id, title: `${SYNTHETIC_TITLE}${row.title} (text part ${identity.start / TEXT_PART_SIZE + 1})`,
        text: await span(row, identity.start, end, value), url: row.url || url,
        metadata: { paper_id: row.id, corpus_version: value.corpus_version, item_type: 'text_part',
          start: identity.start, end, total_length: row.total_length, paper_url: url,
          next_id: end < row.total_length ? documentId({ ...identity, start: end }) : null,
          previous_id: identity.start > 0 ? documentId({ ...identity, start: identity.start - TEXT_PART_SIZE }) : null } }
    },
  }

  // Log before the shared REST/MCP adapters sanitize unexpected exceptions.
  const observed = new Proxy(service, {
    get(target, key, receiver) {
      const value = Reflect.get(target, key, receiver)
      if (typeof value !== 'function') return value
      return async (...args: unknown[]) => {
        try { return await Reflect.apply(value, target, args) }
        catch (error) {
          if (!(error instanceof DomainError)) console.error({ operation: String(key), probe_error: String(error) })
          throw error
        }
      }
    },
  })
  return Object.assign(observed, {
    async stage(stage: string, q: string) {
      if (stage === 'noop') return { synthetic: true, stage }
      const value = await manifest()
      if (stage === 'tokenize') {
        const ids = getTokenizer().tokenIds(embed.query_template, q)
        return { synthetic: true, stage, tokens: ids.length }
      }
      if (stage === 'scan') {
        // Fixed query isolates scanning from tokenization and result assembly.
        const hits = await rank(Float32Array.from({ length: value.dimensions }, (_, i) => Math.sin(i + 1)))
        return { synthetic: true, stage, checksum: hits.reduce((sum, hit) => sum + hit.score, 0), hits: hits.length }
      }
      fail('invalid_argument', 400, 'unknown diagnostic stage')
    },
    async probeInfo() {
      const value = await manifest()
      const rows = [...(await papers()).values()].filter((row) => row.available)
      const sample = rows.find((row) => row.id === 'arxiv:2402.03300') ?? rows[0]
      if (!sample) fail('corpus_unavailable', 503, 'probe has no readable papers')
      const longest = rows.reduce((best, row) => row.total_length > best.total_length ? row : best)
      return { synthetic: true, corpus_version: value.corpus_version, count: value.count,
        sample_paper_id: sample.id, longest_paper_id: longest.id,
        sample_query: 'How is group relative policy optimization used?', sample_find_query: 'the',
        sample_query_max: 'a '.repeat(500).trim(),
        sample_query_adversarial: ('q'.repeat(99) + '🧪 ').repeat(19).trim(),
        sample_fetch_id: documentId({ paper: longest.id, version: value.corpus_version, start: 0 }),
        variants: Object.keys(VARIANTS),
        semantic_quality_measured: false, embedding_provider_called: false }
    },
  })
}

export interface ProbeAppOptions {
  fixedVariant?: Variant
  runtimeRole?: 'durable_object'
  objectId?: string
}

/** Each owner gets independent mutable caches and a stable instance identity. */
export function createProbeApp(options: ProbeAppOptions = {}) {
  let bootId: string | undefined
  // Vocab belongs to the owning app/DO and survives application-cache resets,
  // matching the original probe workload without work in gateway module startup.
  let tokenizer: WordPieceTokenizer | undefined
  const getTokenizer = () => tokenizer ??= new WordPieceTokenizer(vocabText)
  let app: { cacheId: string, assets: ProbeEnv['ASSETS'], variant: Variant, service: ReturnType<typeof createProbeService> } | undefined

  return {
    async fetch(request: Request, env: ProbeEnv): Promise<Response> {
      const url = new URL(request.url)
      const selected = url.searchParams.get('variant') ?? options.fixedVariant ?? 'js-json128'
      if (options.fixedVariant && selected !== options.fixedVariant) return json({ error: 'unknown_variant' }, 400)
      if (!Object.hasOwn(VARIANTS, selected)) return json({ error: 'unknown_variant' }, 400)
      const variant = selected as Variant
      const firstRequest = !bootId
      bootId ??= crypto.randomUUID()
      const cacheReset = url.searchParams.get('cold') === '1'
      if (cacheReset || app?.assets !== env.ASSETS || app?.variant !== variant) app = undefined
      const cacheState = app ? 'warm' : 'cold'
      if (!app) app = { cacheId: crypto.randomUUID(), assets: env.ASSETS, variant,
        service: createProbeService(env, variant, getTokenizer) }
      // Retain this generation across awaits even if another request resets the cache.
      const current = app
      const coldKind = firstRequest ? (options.runtimeRole ? 'object-constructor' : 'app-instance')
        : cacheReset ? 'application-cache-reset' : cacheState === 'warm' ? 'warm' : 'application-cache-load'
      const marker = request.headers.get('x-probe-marker') ?? crypto.randomUUID()
      console.log({ probe_marker: marker, probe_run: url.searchParams.get('probe_run'),
        probe_case: url.searchParams.get('probe_case'), probe_seq: url.searchParams.get('probe_seq'), boot_id: bootId, variant, first_request: firstRequest,
        ...(options.runtimeRole ? { kind: 'static_do_probe', runtime_role: options.runtimeRole,
          run_id: request.headers.get('x-probe-run-id'), cache_id: current.cacheId, cache_reset: cacheReset,
          cold_kind: coldKind, object_id: options.objectId, object_first_request: firstRequest } : {}) })
      let response: Response
      try {
        if (url.pathname === '/probe/stage') {
          if (request.method !== 'GET') fail('invalid_argument', 405, 'method not allowed')
          const q = url.searchParams.get('q') ?? 'query'
          if (pointLength(q) > 2000) fail('query_too_long', 400, 'query too long')
          response = json(await current.service.stage(url.searchParams.get('stage') ?? 'noop', q))
        } else if (url.pathname === '/mcp') {
          response = request.method === 'POST' ? await handleMcp(request, current.service)
            : new Response(null, { status: 405, headers: { allow: 'POST' } })
        } else if (url.pathname === '/' || url.pathname === '/probe/info') {
          requestOrigin(request)
          if (request.method !== 'GET') fail('invalid_argument', 405, 'method not allowed')
          response = url.pathname === '/probe/info' ? json({ ...await current.service.probeInfo(), ...(options.runtimeRole ? {
            runtime: 'durable-object', variants: [options.fixedVariant], object_id: options.objectId,
            cold_isolation: 'application-cache-only', true_isolate_cold_measured: false,
          } : {}) }) : json({
            synthetic: true, warning: 'Runtime probe only. Rankings are synthetic and have no semantic meaning.',
            info: '/probe/info', search: '/v1/search?q=example', mcp: '/mcp',
            cold: 'cold=1 resets application caches; it does not create a new isolate.',
          })
        } else response = await handleRest(request, current.service)
      } catch (error) {
        if (!(error instanceof DomainError)) console.error({ probe_marker: marker, error: String(error) })
        const domain = error instanceof DomainError ? error
          : new DomainError('corpus_unavailable', 503, 'probe request failed')
        response = json(errorBody(domain), domain.status)
      }
      const headers = new Headers(response.headers)
      headers.set('x-probe-boot-id', bootId)
      if (options.runtimeRole) {
        headers.set('x-probe-runtime', 'durable-object')
        headers.set('x-probe-cache-id', current.cacheId)
        headers.set('x-probe-object-id', options.objectId!)
        headers.set('x-probe-cold-kind', coldKind)
        headers.set('x-probe-object-first-request', String(firstRequest))
      }
      headers.set('x-probe-marker', marker)
      headers.set('x-probe-first-request', String(firstRequest))
      headers.set('x-probe-variant', variant)
      headers.set('x-probe-cache', cacheState)
      headers.set('x-probe-synthetic', 'true')
      return new Response(response.body, { status: response.status, statusText: response.statusText, headers })
    },
  }
}

/** The public Worker entrypoint rejects requests before mutable app state. */
export function createWorkerProbeGateway() {
  const app = createProbeApp()
  return {
    async fetch(request: Request, env: ProbeEnv): Promise<Response> {
      const expiresAt = Date.parse(env.PROBE_EXPIRES_AT ?? '')
      if (!Number.isFinite(expiresAt) || Date.now() >= expiresAt) return json({ error: 'probe_expired' }, 503)
      if (!validProbeToken(env.PROBE_TOKEN, request.headers.get('x-probe-token'))) {
        return json({ error: 'probe_forbidden' }, 403)
      }
      const headers = new Headers(request.headers)
      headers.delete('x-probe-token')
      return app.fetch(new Request(request, { headers }), env)
    },
  }
}

export default createWorkerProbeGateway()
