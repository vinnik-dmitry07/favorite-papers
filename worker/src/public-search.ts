import vocabText from '../tokenizer/vocab.txt'
import { createFullCorpusStoreLoader } from './full-corpus-store'
import { BoundedAdmission, createBoundedProbeHandler, PROBE_REQUEST_LIMITS } from './probe-admission'
import { validProbeToken } from './probe-auth'
import { json, requestOrigin } from './http'
import { manual } from './manual'
import { openApiDocument } from './openapi'
import { DomainError, errorBody, fail } from './schemas'
import { createService, type Service } from './service'
import { embed, WordPieceTokenizer } from './tokenize'

export const PUBLIC_MANIFEST_SHA = '6b9c87883f525a128eb9a48aead5914d9524ba2f7433ff3b14c62b3c0d970b47'
export const PUBLIC_OBJECT_NAME = 'public-search'
export const PUBLIC_LIMITS = Object.freeze({ query_texts: 1000, query_tokens_reserved: 512000,
  compatibility_texts: 200, compatibility_tokens_reserved: 102400, ai_timeout_ms: 20000 })
const BUDGET_KEY = 'public-ai-day-v1'
const LEGACY_STATE_KEY = 'public-release-v1'
export const PUBLIC_RELEASE_KEY = 'public-release-v2:' + PUBLIC_MANIFEST_SHA
const STATE_KEY = PUBLIC_RELEASE_KEY
const PAUSE_KEY = 'public-search-paused-v1'
const THRESHOLD = 0.999
const BATCH = 16
type Corpus = Awaited<ReturnType<ReturnType<typeof createFullCorpusStoreLoader>>>
interface Result { index: number, cosine: number, remote_norm: number }
interface Compatibility {
  status: 'not_started' | 'running' | 'passed' | 'failed'
  checked: number, expected: number, threshold: number, min_cosine: number | null
  results: Result[], pending: number[] | null, error?: string
}
interface Release { manifest_sha256: string, activation: string | null, compatibility: Compatibility }
interface Budget { day: string, query_texts: number, query_tokens_reserved: number,
  compatibility_texts: number, compatibility_tokens_reserved: number, ai_calls: number }
export interface PublicSearchEnv {
  ASSETS: { fetch(request: Request): Promise<Response> }
  AI: { run(model: string, input: { text: string[], pooling: string }): Promise<{ data?: number[] | number[][] }> }
  PUBLIC_SEARCH: Pick<DurableObjectNamespace, 'idFromName' | 'get'>
  PUBLIC_MANIFEST_SHA: string, PUBLICATION_ID: string, PUBLICATION_TOKEN: string
  PQ_WASM?: WebAssembly.Module
}

function freshCompatibility(): Compatibility {
  return { status: 'not_started', checked: 0, expected: 200, threshold: THRESHOLD,
    min_cosine: null, results: [], pending: null }
}
function freshBudget(): Budget {
  return { day: new Date().toISOString().slice(0, 10), query_texts: 0,
    query_tokens_reserved: 0, compatibility_texts: 0, compatibility_tokens_reserved: 0, ai_calls: 0 }
}
function checkedBudget(raw: Budget | undefined): Budget {
  const today = freshBudget()
  if (!raw) return today
  if (typeof raw.day !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(raw.day) || raw.day > today.day) {
    fail('public_state_invalid', 503, 'Daily AI reservation date is invalid')
  }
  if (raw.day < today.day) return today
  if (!Number.isSafeInteger(raw.ai_calls) || raw.ai_calls < 0
      || Object.entries(PUBLIC_LIMITS).filter(([key]) => key !== 'ai_timeout_ms').some(([key]) =>
        !Number.isSafeInteger(raw[key as keyof Budget]) || Number(raw[key as keyof Budget]) < 0)
      || raw.query_tokens_reserved !== raw.query_texts * 512
      || raw.compatibility_tokens_reserved !== raw.compatibility_texts * 512
      || raw.ai_calls > raw.query_texts + raw.compatibility_texts) {
    fail('public_state_invalid', 503, 'Daily AI reservations are invalid')
  }
  return raw
}
function checkedRelease(raw: Release | undefined, indices: number[]): Release {
  if (!raw) return { manifest_sha256: PUBLIC_MANIFEST_SHA, activation: null, compatibility: freshCompatibility() }
  const c = raw.compatibility
  if (raw.manifest_sha256 !== PUBLIC_MANIFEST_SHA || !(raw.activation === null || typeof raw.activation === 'string')
      || !c || c.expected !== 200 || c.threshold !== THRESHOLD || !Array.isArray(c.results)
      || c.checked !== c.results.length || c.checked > 200
      || !['not_started', 'running', 'passed', 'failed'].includes(c.status)
      || c.results.some((row, i) => row.index !== indices[i] || !Number.isFinite(row.cosine)
        || row.cosine < -1 || row.cosine > 1 || !Number.isFinite(row.remote_norm) || row.remote_norm <= 0)
      || !(c.pending === null || (Array.isArray(c.pending) && c.pending.length > 0 && c.pending.length <= BATCH
        && c.pending.every((index, i) => index === indices[c.checked + i])))
      || (c.status === 'passed' && (c.checked !== 200 || c.pending !== null
        || c.results.some((row) => row.cosine < THRESHOLD)))
      || (c.status === 'not_started' && (c.checked !== 0 || c.pending !== null))) {
    fail('public_state_invalid', 503, 'Compatibility state is invalid')
  }
  return raw
}
function retrySeconds() { return Math.max(1, Math.ceil((Date.parse(new Date().toISOString().slice(0, 10)) + 86400000 - Date.now()) / 1000)) }
function failed(error: unknown): Response {
  const known = error instanceof DomainError ? error : new DomainError('corpus_unavailable', 503, 'Public search is unavailable')
  const response = json(errorBody(known), known.status)
  if (known.status === 429) response.headers.set('retry-after', String(retrySeconds()))
  return response
}
function authorize(request: Request, env: PublicSearchEnv) {
  if (!validProbeToken(env.PUBLICATION_TOKEN, request.headers.get('x-publication-token'))) {
    fail('forbidden', 403, 'Publication authorization required')
  }
  const expectedPublication = request.headers.get('x-publication-id')
  if (expectedPublication !== null && expectedPublication !== env.PUBLICATION_ID) {
    fail('version_conflict', 409, 'Administrative request targets another publication')
  }
}
function publicOpenApi(origin: string) {
  const spec = openApiDocument(origin)
  for (const path of Object.values(spec.paths)) {
    const responses = path.get.responses as Record<string, { description: string }>
    if (responses['429']) responses['429'] = { ...responses['429'],
      description: 'Shared daily semantic-search allowance exhausted. Follow the Retry-After header; reset is at 00:00 UTC.' }
  }
  return spec
}

/** Stable public object: immutable assets, daily durable reservations, explicit activation. */
export class PublicSearch {
  private initialized: Promise<Corpus> | undefined
  private loader: ReturnType<typeof createFullCorpusStoreLoader> | undefined
  private tokenizer: WordPieceTokenizer | undefined
  private service: Service | undefined
  private compatibilityInFlight: Promise<unknown> | undefined
  private releaseInitialized: Promise<void> | undefined
  private readonly admission = new BoundedAdmission(PROBE_REQUEST_LIMITS.active,
    PROBE_REQUEST_LIMITS.queued, PROBE_REQUEST_LIMITS.queue_wait_ms)
  // Unlike the HTTP deadline, this permit follows the actual provider promise.
  private readonly aiAdmission = new BoundedAdmission(4, 0)
  private readonly handler = createBoundedProbeHandler(() => this.getService(), this.admission)

  constructor(private readonly state: DurableObjectState, private readonly env: PublicSearchEnv,
    private readonly dependencies: { loader?: typeof createFullCorpusStoreLoader } = {}) {}

  private ready(): Promise<Corpus> {
    this.initialized ??= (async () => {
      if (this.env.PUBLIC_MANIFEST_SHA !== PUBLIC_MANIFEST_SHA
          || !/^[a-zA-Z0-9_.-]{1,160}$/.test(this.env.PUBLICATION_ID ?? '')
          || this.env.PUBLICATION_ID === 'UNPUBLISHED') fail('config_mismatch', 503, 'Publication identity missing')
      this.loader ??= (this.dependencies.loader ?? createFullCorpusStoreLoader)(this.env.ASSETS,
        PUBLIC_MANIFEST_SHA, (text) => this.embedQuery(text), async () => true, { module: this.env.PQ_WASM })
      const corpus = await this.loader()
      if (corpus.manifest.kind !== 'full-corpus-int8' || corpus.manifest.synthetic !== false
          || corpus.manifest.passage_count !== 40575 || corpus.manifest.compatibility.indices.length !== 200) {
        fail('config_mismatch', 503, 'Expected the retained genuine full corpus')
      }
      return corpus
    })().catch((error) => { this.initialized = undefined; throw error })
    return this.initialized
  }
  private async release() {
    const corpus = await this.ready()
    this.releaseInitialized ??= this.state.storage.transaction(async (tx) => {
      let raw = await tx.get<Release>(STATE_KEY)
      if (!raw) {
        const legacy = await tx.get<Release>(LEGACY_STATE_KEY)
        // Copy only this corpus's legacy state; never migrate activation or
        // compatibility from a different corpus. The daily ledger stays global.
        if (legacy?.manifest_sha256 === PUBLIC_MANIFEST_SHA) raw = legacy
      }
      const release = checkedRelease(raw, corpus.manifest.compatibility.indices)
      if (release.compatibility.pending !== null) {
        release.compatibility.pending = null
        release.compatibility.status = 'failed'
        release.compatibility.error = 'interrupted_compatibility_batch'
        release.activation = null
      }
      await tx.put(STATE_KEY, release)
    }).catch((error) => { this.releaseInitialized = undefined; throw error })
    await this.releaseInitialized
    const release = checkedRelease(await this.state.storage.get<Release>(STATE_KEY), corpus.manifest.compatibility.indices)
    return await this.state.storage.get<boolean>(PAUSE_KEY) === true ? { ...release, activation: null } : release
  }
  private active(release: Release) {
    return release.activation === this.env.PUBLICATION_ID && release.compatibility.status === 'passed'
  }
  private async requireActive() {
    if (!this.active(await this.release())) fail('search_disabled', 503, 'Semantic search has not been activated for this publication')
  }
  private async reserve(kind: 'query' | 'compatibility', count: number, indices?: number[]) {
    const corpus = await this.ready()
    await this.release()
    await this.state.storage.transaction(async (tx) => {
      const release = checkedRelease(await tx.get<Release>(STATE_KEY), corpus.manifest.compatibility.indices)
      const budget = checkedBudget(await tx.get<Budget>(BUDGET_KEY))
      if (kind === 'query' && (!this.active(release) || await tx.get<boolean>(PAUSE_KEY) === true)) {
        fail('search_disabled', 503, 'Semantic search is disabled')
      }
      if (kind === 'compatibility' && (release.compatibility.pending !== null
          || !['not_started', 'running'].includes(release.compatibility.status))) {
        fail('compatibility_conflict', 409, 'Compatibility cannot advance')
      }
      const textKey = kind === 'query' ? 'query_texts' : 'compatibility_texts'
      const tokenKey = kind === 'query' ? 'query_tokens_reserved' : 'compatibility_tokens_reserved'
      if (budget[textKey] + count > PUBLIC_LIMITS[textKey]
          || budget[tokenKey] + count * 512 > PUBLIC_LIMITS[tokenKey]) fail('daily_ai_budget_exhausted', 429,
        'Daily public AI allowance exhausted; catalog and reading remain available', { retry_after: retrySeconds() })
      budget[textKey] += count
      budget[tokenKey] += count * 512
      budget.ai_calls++
      if (kind === 'compatibility') {
        release.compatibility.pending = indices!
        release.compatibility.status = 'running'
        await tx.put(STATE_KEY, release)
      }
      await tx.put(BUDGET_KEY, budget)
    })
  }
  private async callAi(texts: string[], reserve: () => Promise<void>): Promise<number[][]> {
    let timer: ReturnType<typeof setTimeout> | undefined
    try {
      const result = await Promise.race([this.aiAdmission.run(async () => {
        await reserve()
        return this.env.AI.run(embed.model, { text: texts, pooling: embed.pooling })
      }),
        new Promise<never>((_resolve, reject) => { timer = setTimeout(() => reject(
          new DomainError('embedding_timeout', 503, 'Embedding deadline exceeded; reservation retained')), PUBLIC_LIMITS.ai_timeout_ms) })])
      const data = result?.data
      const vectors = Array.isArray(data) && typeof data[0] === 'number' ? [data as number[]] : data as number[][]
      if (!Array.isArray(vectors) || vectors.length !== texts.length || vectors.some((v) => !Array.isArray(v)
          || v.length !== 768 || v.some((x) => typeof x !== 'number' || !Number.isFinite(x))
          || v.reduce((sum, x) => sum + x * x, 0) <= 0)) fail('embedding_response_invalid', 503, 'Invalid query embedding')
      return vectors
    } catch (error) {
      if (error instanceof DomainError) throw error
      throw new DomainError('embedding_request_failed', 503, 'Embedding failed; reservation retained')
    } finally { if (timer !== undefined) clearTimeout(timer) }
  }
  private getTokenizer() { return this.tokenizer ??= new WordPieceTokenizer(vocabText) }
  private async embedQuery(text: string) {
    if (this.getTokenizer().tokenIds('', text).length > 512) fail('query_too_long', 400, 'Embedding input exceeds 512 tokens')
    return (await this.callAi([text], () => this.reserve('query', 1)))[0]
  }
  private async getService(): Promise<Service> {
    if (!this.service) {
      const corpus = await this.ready()
      const service = createService(corpus.store, this.getTokenizer())
      this.service = { ...service,
        search: async (args) => { await this.requireActive(); return service.search(args) },
        researchSearch: async (query, ip) => { await this.requireActive(); return service.researchSearch(query, ip) },
        health: async () => {
          const health = await service.health()
          let active = false, searchError: string | undefined
          try {
            active = this.active(await this.release())
            checkedBudget(await this.state.storage.get<Budget>(BUDGET_KEY))
          } catch (error) {
            active = false
            searchError = error instanceof DomainError ? error.code : 'public_state_unavailable'
          }
          return { ...health, status: active && health.status === 'ready' ? 'ready' : 'degraded',
            search_enabled: active, manifest_sha256: PUBLIC_MANIFEST_SHA, passage_count: 40575,
            publication_id: this.env.PUBLICATION_ID, ...(searchError ? { search_error: searchError } : {}) }
        },
      }
    }
    return this.service
  }
  private async status() {
    const corpus = await this.ready(), release = await this.release()
    return { kind: 'public-static-search', manifest_sha256: PUBLIC_MANIFEST_SHA,
      publication_id: this.env.PUBLICATION_ID, release_id: corpus.manifest.release_id,
      passage_count: 40575, active: this.active(release), compatibility: release.compatibility,
      budget: { ...checkedBudget(await this.state.storage.get<Budget>(BUDGET_KEY)), limits: PUBLIC_LIMITS } }
  }
  private async compatibility() {
    const corpus = await this.ready(), release = await this.release(), c = release.compatibility
    if (c.status === 'passed' || c.status === 'failed') return this.compatibilityResponse()
    const positions = Array.from({ length: Math.min(BATCH, 200 - c.checked) }, (_, i) => c.checked + i)
    const refs = await Promise.all(positions.map((i) => corpus.referencePassage(i)))
    if (refs.some((ref) => this.getTokenizer().tokenIds('', ref.input).length > 512)) fail('config_mismatch', 503, 'Canary input exceeds token limit')
    const indices = positions.map((i) => corpus.manifest.compatibility.indices[i])
    let reserved = false
    let results: Result[] = [], error: string | undefined
    try {
      const vectors = await this.callAi(refs.map((ref) => ref.input), async () => {
        await this.reserve('compatibility', refs.length, indices)
        reserved = true
      })
      results = vectors.map((v, i) => {
        const ref = refs[i].vector, norm = Math.sqrt(v.reduce((s, x) => s + x * x, 0))
        const cosine = v.reduce((s, x, j) => s + x * ref[j], 0) / (norm * Math.sqrt(ref.reduce((s, x) => s + x * x, 0)))
        if (!Number.isFinite(cosine)) fail('embedding_response_invalid', 503, 'Invalid cosine')
        return { index: indices[i], cosine: Math.max(-1, Math.min(1, cosine)), remote_norm: norm }
      })
    } catch (cause) {
      if (!reserved) throw cause
      error = cause instanceof DomainError ? cause.code : 'embedding_request_failed'
    }
    await this.state.storage.transaction(async (tx) => {
      const release = checkedRelease(await tx.get<Release>(STATE_KEY), corpus.manifest.compatibility.indices)
      if (JSON.stringify(release.compatibility.pending) !== JSON.stringify(indices)) fail('compatibility_conflict', 409, 'Canary reservation changed')
      const current = release.compatibility
      current.pending = null
      current.results.push(...results)
      current.checked = current.results.length
      current.min_cosine = current.checked ? Math.min(...current.results.map((r) => r.cosine)) : null
      if (error || results.some((r) => r.cosine < THRESHOLD)) {
        current.status = 'failed'; current.error = error ?? 'embedding_cosine_below_threshold'; release.activation = null
      } else if (current.checked === 200) current.status = 'passed'
      await tx.put(STATE_KEY, release)
    })
    return this.compatibilityResponse()
  }
  private async compatibilityResponse() {
    const status = await this.status()
    return { ...status.compatibility, manifest_sha256: status.manifest_sha256,
      release_id: status.release_id, budget: status.budget }
  }
  private async admin(request: Request) {
    authorize(request, this.env)
    const path = new URL(request.url).pathname
    if (path === '/admin/state' && request.method === 'GET') return json(await this.status())
    if (request.method !== 'POST') fail('invalid_argument', 405, 'Admin mutation requires POST')
    if (path === '/admin/deactivate') {
      // Emergency pause must work with unavailable assets or corrupt AI state.
      // A separate durable latch also survives an in-flight compatibility batch.
      await this.state.storage.put(PAUSE_KEY, true)
      return json({ kind: 'public-static-search', manifest_sha256: PUBLIC_MANIFEST_SHA,
        publication_id: this.env.PUBLICATION_ID, active: false })
    }
    if (path === '/admin/compatibility') {
      this.compatibilityInFlight ??= this.compatibility().finally(() => { this.compatibilityInFlight = undefined })
      return json(await this.compatibilityInFlight)
    }
    if (!['/admin/activate', '/admin/reset-compatibility'].includes(path)) fail('invalid_argument', 404, 'Unknown admin operation')
    const corpus = await this.ready()
    await this.release()
    await this.state.storage.transaction(async (tx) => {
      const release = checkedRelease(await tx.get<Release>(STATE_KEY), corpus.manifest.compatibility.indices)
      if (path === '/admin/activate') {
        if (release.compatibility.status !== 'passed') fail('embedding_compatibility_unverified', 409, 'Canary must pass before activation')
        release.activation = this.env.PUBLICATION_ID
        await tx.put(PAUSE_KEY, false)
      } else {
        if (this.active(release) || this.compatibilityInFlight || release.compatibility.status !== 'failed') {
          fail('compatibility_conflict', 409, 'Only inactive failed compatibility may be reset')
        }
        release.compatibility = freshCompatibility()
      }
      await tx.put(STATE_KEY, release)
    })
    return json(await this.status())
  }
  async fetch(request: Request): Promise<Response> {
    try {
      requestOrigin(request)
      const url = new URL(request.url)
      if (url.pathname === '/openapi.json' && request.method === 'GET') {
        return await this.admission.run(async () => json(publicOpenApi(url.origin)), request.signal)
      }
      if (new URL(request.url).pathname.startsWith('/admin/')) {
        authorize(request, this.env)
        // The authenticated one-write pause cannot wait behind hung searches.
        if (url.pathname === '/admin/deactivate' && request.method === 'POST') return await this.admin(request)
        return await this.admission.run(() => this.admin(request), request.signal)
      }
      const response = await this.handler.fetch(request)
      if (response.status === 429) response.headers.set('retry-after', String(retrySeconds()))
      return response
    } catch (error) { return failed(error) }
  }
}

const publicManual = manual.replace('Uncached semantic queries share a 30/minute budget per client IP. On 429 wait\nRetry-After seconds. Read-only catalog/text/citation operations do not use it.',
  'Uncached semantic requests share 1000 query embeddings per UTC day across all\nclients. Each reserves 512 input tokens before submission; failed calls remain\ncounted. On 429 wait Retry-After seconds. Catalog/text/citation reads use no AI.\nThe account also has shared platform limits; availability is not guaranteed.')
export function createPublicGateway() {
  return { async fetch(request: Request, env: PublicSearchEnv): Promise<Response> {
    try {
      const url = new URL(request.url)
      requestOrigin(request)
      if (url.pathname.startsWith('/admin/')) authorize(request, env)
      if (url.pathname.startsWith('/probe/')) return json({ error: { code: 'not_found' } }, 404)
      if (url.pathname === '/mcp' && request.method !== 'POST') return new Response(null, { status: 405, headers: { allow: 'POST' } })
      if (request.url.length > PROBE_REQUEST_LIMITS.url_characters) fail('invalid_argument', 414, 'URL too long')
      if ((url.pathname === '/' || url.pathname === '/llms.txt') && ['GET', 'HEAD'].includes(request.method)) {
        return new Response(request.method === 'HEAD' ? null : publicManual, { headers: { 'content-type': 'text/plain; charset=utf-8' } })
      }
      return await env.PUBLIC_SEARCH.get(env.PUBLIC_SEARCH.idFromName(PUBLIC_OBJECT_NAME)).fetch(request)
    } catch (error) { return failed(error) }
  } }
}
export default createPublicGateway()
