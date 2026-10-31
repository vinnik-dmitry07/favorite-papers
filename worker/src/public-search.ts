import vocabText from '../tokenizer/vocab.txt'
import { AsyncLocalStorage } from 'node:async_hooks'
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
const FRESH_BUDGET_KEY = 'public-fresh-ai-day-v1'
const FRESH_DAILY_LIMIT = 200
export const CLIENT_LIMITS = Object.freeze({ daily: 200, minute: 20 })
export const FRESH_SAMPLES = 32
const BUDGET_KEY = 'public-ai-day-v1'
const LEGACY_STATE_KEY = 'public-release-v1'
export const PUBLIC_RELEASE_KEY = 'public-release-v2:' + PUBLIC_MANIFEST_SHA
const STATE_KEY = PUBLIC_RELEASE_KEY
const BASELINE_KEY = 'public-compatibility-v1:' + PUBLIC_MANIFEST_SHA
const CLIENT_KEY = 'public-client-day-v1'
const clientContext = new AsyncLocalStorage<string>()
export function publicationStateKey(publication: string) { return 'public-release-v3:' + PUBLIC_MANIFEST_SHA + ':' + publication }
function publicationPauseKey(publication: string) { return 'public-pause-v2:' + publication }
const THRESHOLD = 0.999
const BATCH = 16
type Corpus = Awaited<ReturnType<ReturnType<typeof createFullCorpusStoreLoader>>>
interface Result { index: number, cosine: number, remote_norm: number }
interface Compatibility {
  status: 'not_started' | 'running' | 'passed' | 'failed'
  checked: number, expected: number, threshold: number, min_cosine: number | null
  results: Result[], pending: number[] | null, error?: string
}
interface FreshCheck extends Compatibility { publication_id: string, checked_at: number | null }
interface Release { manifest_sha256: string, activation: string | null, compatibility: Compatibility, fresh?: FreshCheck }
interface Budget { day: string, query_texts: number, query_tokens_reserved: number,
  compatibility_texts: number, compatibility_tokens_reserved: number, ai_calls: number }
export interface PublicSearchEnv {
  ASSETS: { fetch(request: Request): Promise<Response> }
  AI: { run(model: string, input: { text: string[], pooling: string }): Promise<{ data?: number[] | number[][] }> }
  PUBLIC_SEARCH: Pick<DurableObjectNamespace, 'idFromName' | 'get'>
  PUBLIC_MANIFEST_SHA: string, PUBLICATION_ID: string, PUBLICATION_TOKEN: string
  PUBLIC_PREVIEW?: string
  PUBLIC_PREVIEW_EXPIRES_AT?: string
  PQ_WASM?: WebAssembly.Module
}

function freshCompatibility(): Compatibility {
  return { status: 'not_started', checked: 0, expected: 200, threshold: THRESHOLD,
    min_cosine: null, results: [], pending: null }
}
function freshCheck(publication: string): FreshCheck {
  return { ...freshCompatibility(), expected: FRESH_SAMPLES, publication_id: publication, checked_at: null }
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
      description: 'Client minute/day or shared daily semantic-search allowance exhausted. Follow Retry-After; daily allowances reset at 00:00 UTC.' }
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
  private freshInFlight: Promise<unknown> | undefined
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
      let raw = await tx.get<Release>(publicationStateKey(this.env.PUBLICATION_ID))
      if (!raw) {
        const legacy = await tx.get<Release>(STATE_KEY) ?? await tx.get<Release>(LEGACY_STATE_KEY)
        // Copy only this corpus's legacy state; never migrate activation or
        // compatibility from a different corpus. The daily ledger stays global.
        if (legacy?.manifest_sha256 === PUBLIC_MANIFEST_SHA) raw = { ...legacy,
          activation: legacy.activation === this.env.PUBLICATION_ID ? legacy.activation : null,
          fresh: legacy.fresh?.publication_id === this.env.PUBLICATION_ID ? legacy.fresh : undefined }
        const baseline = await tx.get<Compatibility>(BASELINE_KEY)
        if (baseline?.status === 'passed' && !raw) raw = { manifest_sha256: PUBLIC_MANIFEST_SHA,
          activation: null, compatibility: baseline }
      }
      const release = checkedRelease(raw, corpus.manifest.compatibility.indices)
      release.fresh ??= freshCheck(this.env.PUBLICATION_ID)
      this.checkedFresh(release.fresh, corpus.manifest.compatibility.indices)
      if (release.compatibility.pending !== null) {
        release.compatibility.pending = null
        release.compatibility.status = 'failed'
        release.compatibility.error = 'interrupted_compatibility_batch'
        release.activation = null
      }
      if (release.fresh.pending !== null) {
        release.fresh.pending = null; release.fresh.status = 'failed'
        release.fresh.error = 'interrupted_fresh_batch'; release.activation = null
      }
      await tx.put(publicationStateKey(this.env.PUBLICATION_ID), release)
    }).catch((error) => { this.releaseInitialized = undefined; throw error })
    await this.releaseInitialized
    const release = checkedRelease(await this.state.storage.get<Release>(publicationStateKey(this.env.PUBLICATION_ID)), corpus.manifest.compatibility.indices)
    this.checkedFresh(release.fresh, corpus.manifest.compatibility.indices)
    return await this.state.storage.get<boolean>(publicationPauseKey(this.env.PUBLICATION_ID)) === true ? { ...release, activation: null } : release
  }
  private checkedFresh(c: FreshCheck | undefined, indices: number[]): asserts c is FreshCheck {
    if (!c || c.publication_id !== this.env.PUBLICATION_ID || c.expected !== FRESH_SAMPLES
        || c.threshold !== THRESHOLD || !Array.isArray(c.results) || c.checked !== c.results.length
        || c.checked > FRESH_SAMPLES || !['not_started', 'running', 'passed', 'failed'].includes(c.status)
        || c.results.some((r, i) => r.index !== indices[Math.floor(i * 200 / FRESH_SAMPLES)]
          || !Number.isFinite(r.cosine) || r.cosine < -1 || r.cosine > 1
          || !Number.isFinite(r.remote_norm) || r.remote_norm <= 0)
        || !(c.pending === null || (Array.isArray(c.pending) && c.pending.length <= BATCH
          && c.pending.length > 0 && c.pending.every((v, i) => v === indices[Math.floor((c.checked + i) * 200 / FRESH_SAMPLES)])))
        || (c.status === 'passed' && (c.checked !== FRESH_SAMPLES || c.pending !== null
          || !Number.isFinite(c.checked_at) || c.results.some((r) => r.cosine < THRESHOLD)))
        || (c.status === 'not_started' && (c.checked !== 0 || c.pending !== null))) {
      fail('public_state_invalid', 503, 'Fresh compatibility state is invalid')
    }
  }
  private active(release: Release) {
    return release.activation === this.env.PUBLICATION_ID && release.compatibility.status === 'passed'
      && release.fresh?.status === 'passed' && release.fresh.publication_id === this.env.PUBLICATION_ID
  }
  private async requireActive() {
    if (!this.active(await this.release())) fail('search_disabled', 503, 'Semantic search has not been activated for this publication')
  }
  private async reserve(kind: 'query' | 'compatibility' | 'fresh', count: number, indices?: number[]) {
    const corpus = await this.ready()
    await this.release()
    await this.state.storage.transaction(async (tx) => {
      const release = checkedRelease(await tx.get<Release>(publicationStateKey(this.env.PUBLICATION_ID)), corpus.manifest.compatibility.indices)
      const budget = checkedBudget(await tx.get<Budget>(BUDGET_KEY))
      if (kind === 'query' && (!this.active(release) || await tx.get<boolean>(publicationPauseKey(this.env.PUBLICATION_ID)) === true)) {
        fail('search_disabled', 503, 'Semantic search is disabled')
      }
      if (kind === 'compatibility' && (release.compatibility.pending !== null
          || !['not_started', 'running'].includes(release.compatibility.status))) {
        fail('compatibility_conflict', 409, 'Compatibility cannot advance')
      }
      const check = kind === 'fresh' ? release.fresh : release.compatibility
      if (kind === 'fresh') {
        this.checkedFresh(check as FreshCheck, corpus.manifest.compatibility.indices)
        if (check?.pending !== null || !['not_started', 'running'].includes(check!.status)) fail('compatibility_conflict', 409, 'Fresh check cannot advance')
      }
      const textKey = kind === 'query' ? 'query_texts' : 'compatibility_texts'
      const tokenKey = kind === 'query' ? 'query_tokens_reserved' : 'compatibility_tokens_reserved'
      if (kind !== 'fresh' && (budget[textKey] + count > PUBLIC_LIMITS[textKey]
          || budget[tokenKey] + count * 512 > PUBLIC_LIMITS[tokenKey])) fail('daily_ai_budget_exhausted', 429,
        'Daily public AI allowance exhausted; catalog and reading remain available', { retry_after: retrySeconds() })
      if (kind === 'fresh') {
        const fresh = await tx.get<{ day: string, texts: number, tokens_reserved: number }>(FRESH_BUDGET_KEY)
        const daily = !fresh || fresh.day < budget.day ? { day: budget.day, texts: 0, tokens_reserved: 0 } : fresh
        if (daily.day !== budget.day || !Number.isSafeInteger(daily.texts) || daily.texts < 0
            || daily.tokens_reserved !== daily.texts * 512) fail('public_state_invalid', 503, 'Fresh-check budget is invalid')
        if (daily.texts + count > FRESH_DAILY_LIMIT) fail('daily_ai_budget_exhausted', 429, 'Daily fresh-check allowance exhausted', { retry_after: retrySeconds() })
        await tx.put(FRESH_BUDGET_KEY, { ...daily, texts: daily.texts + count, tokens_reserved: (daily.texts + count) * 512 })
      } else {
        budget[textKey] += count
        budget[tokenKey] += count * 512
        budget.ai_calls++
      }
      if (kind === 'query') await this.reserveClient(tx, budget.day)
      if (kind !== 'query') {
        check!.pending = indices!
        check!.status = 'running'
        await tx.put(publicationStateKey(this.env.PUBLICATION_ID), release)
      }
      if (kind !== 'fresh') await tx.put(BUDGET_KEY, budget)
    })
  }
  private async reserveClient(tx: Pick<DurableObjectStorage, 'get' | 'put'>, day: string) {
    let salt = await tx.get<string>('public-client-salt-v1')
    if (!salt) { salt = crypto.randomUUID(); await tx.put('public-client-salt-v1', salt) }
    const bytes = new TextEncoder().encode(salt + '\0' + (clientContext.getStore() ?? 'unknown'))
    const hash = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes)), (v) => v.toString(16).padStart(2, '0')).join('')
    type Clients = { day: string, rows: Record<string, { day: number, minute: number, count: number }> }
    let clients = await tx.get<Clients>(CLIENT_KEY)
    if (!clients || clients.day < day) clients = { day, rows: {} }
    if (clients.day !== day || !clients.rows || Object.keys(clients.rows).length > 1000) fail('public_state_invalid', 503, 'Client allowance state is invalid')
    const minute = Math.floor(Date.now() / 60000)
    const row = clients.rows[hash] ?? { day: 0, minute, count: 0 }
    if (![row.day, row.minute, row.count].every((v) => Number.isSafeInteger(v) && v >= 0)) fail('public_state_invalid', 503, 'Client allowance is invalid')
    if (row.day >= CLIENT_LIMITS.daily) fail('client_daily_budget_exhausted', 429, 'This client address has used its daily search allowance', { retry_after: retrySeconds() })
    if (row.minute === minute && row.count >= CLIENT_LIMITS.minute) fail('client_rate_limited', 429, 'This client address has used its minute search allowance', { retry_after: 60 - Math.floor(Date.now() / 1000) % 60 })
    clients.rows[hash] = { day: row.day + 1, minute, count: row.minute === minute ? row.count + 1 : 1 }
    await tx.put(CLIENT_KEY, clients)
  }
  private async callAi(texts: string[], reserve: () => Promise<void>): Promise<number[][]> {
    let timer: ReturnType<typeof setTimeout> | undefined
    let expired = false
    try {
      const result = await Promise.race([this.aiAdmission.run(async () => {
        await reserve()
        if (expired) fail('embedding_timeout', 503, 'Embedding deadline expired before provider submission; reservation retained')
        return this.env.AI.run(embed.model, { text: texts, pooling: embed.pooling })
      }),
        new Promise<never>((_resolve, reject) => { timer = setTimeout(() => {
          expired = true
          reject(new DomainError('embedding_timeout', 503, 'Embedding deadline exceeded; reservation retained'))
        }, PUBLIC_LIMITS.ai_timeout_ms) })])
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
            recovery_protocol: 'publication-v1',
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
      fresh_compatibility: release.fresh, recovery_protocol: 'publication-v1', client_limits: CLIENT_LIMITS,
      fresh_budget: { ...await this.state.storage.get(FRESH_BUDGET_KEY) as object, daily_text_limit: FRESH_DAILY_LIMIT },
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
      const release = checkedRelease(await tx.get<Release>(publicationStateKey(this.env.PUBLICATION_ID)), corpus.manifest.compatibility.indices)
      if (JSON.stringify(release.compatibility.pending) !== JSON.stringify(indices)) fail('compatibility_conflict', 409, 'Canary reservation changed')
      const current = release.compatibility
      current.pending = null
      current.results.push(...results)
      current.checked = current.results.length
      current.min_cosine = current.checked ? Math.min(...current.results.map((r) => r.cosine)) : null
      if (error || results.some((r) => r.cosine < THRESHOLD)) {
        current.status = 'failed'; current.error = error ?? 'embedding_cosine_below_threshold'; release.activation = null
      } else if (current.checked === 200) current.status = 'passed'
      await tx.put(publicationStateKey(this.env.PUBLICATION_ID), release)
      if (current.status === 'passed') await tx.put(BASELINE_KEY, current)
    })
    return this.compatibilityResponse()
  }
  private async compatibilityResponse() {
    const status = await this.status()
    return { ...status.compatibility, manifest_sha256: status.manifest_sha256,
      release_id: status.release_id, budget: status.budget }
  }
  private async freshCompatibility() {
    const corpus = await this.ready(), release = await this.release(), c = release.fresh!
    if (release.compatibility.status !== 'passed') fail('embedding_compatibility_unverified', 409, 'Baseline compatibility must pass first')
    if (c.status === 'passed' || c.status === 'failed') return c
    const positions = Array.from({ length: Math.min(BATCH, FRESH_SAMPLES - c.checked) },
      (_, i) => Math.floor((c.checked + i) * 200 / FRESH_SAMPLES))
    const refs = await Promise.all(positions.map((i) => corpus.referencePassage(i)))
    if (refs.some((r) => this.getTokenizer().tokenIds('', r.input).length > 512)) fail('config_mismatch', 503, 'Fresh input exceeds token limit')
    const indices = positions.map((i) => corpus.manifest.compatibility.indices[i])
    let reserved = false, error: string | undefined
    let results: Result[] = []
    try {
      const vectors = await this.callAi(refs.map((r) => r.input), async () => {
        await this.reserve('fresh', refs.length, indices); reserved = true
      })
      results = vectors.map((v, i) => {
        const norm = Math.sqrt(v.reduce((s, x) => s + x * x, 0)), ref = refs[i].vector
        const cosine = v.reduce((s, x, j) => s + x * ref[j], 0) / (norm * Math.sqrt(ref.reduce((s, x) => s + x * x, 0)))
        if (!Number.isFinite(cosine)) fail('embedding_response_invalid', 503, 'Invalid fresh cosine')
        return { index: indices[i], cosine: Math.max(-1, Math.min(1, cosine)), remote_norm: norm }
      })
    } catch (cause) {
      if (!reserved) throw cause
      error = cause instanceof DomainError ? cause.code : 'embedding_request_failed'
    }
    return this.state.storage.transaction(async (tx) => {
      const stored = checkedRelease(await tx.get<Release>(publicationStateKey(this.env.PUBLICATION_ID)), corpus.manifest.compatibility.indices)
      this.checkedFresh(stored.fresh, corpus.manifest.compatibility.indices)
      const current = stored.fresh
      if (JSON.stringify(current.pending) !== JSON.stringify(indices)) fail('compatibility_conflict', 409, 'Fresh reservation changed')
      current.pending = null; current.results.push(...results); current.checked = current.results.length
      current.min_cosine = current.checked ? Math.min(...current.results.map((r) => r.cosine)) : null
      if (error || results.some((r) => r.cosine < THRESHOLD)) {
        current.status = 'failed'; current.error = error ?? 'embedding_cosine_below_threshold'; stored.activation = null
      } else if (current.checked === FRESH_SAMPLES) { current.status = 'passed'; current.checked_at = Date.now() }
      await tx.put(publicationStateKey(this.env.PUBLICATION_ID), stored)
      return current
    })
  }
  private async admin(request: Request) {
    authorize(request, this.env)
    const path = new URL(request.url).pathname
    if (path === '/admin/state' && request.method === 'GET') return json(await this.status())
    if (request.method !== 'POST') fail('invalid_argument', 405, 'Admin mutation requires POST')
    if (path === '/admin/deactivate') {
      // Emergency pause must work with unavailable assets or corrupt AI state.
      // A separate durable latch also survives an in-flight compatibility batch.
      await this.state.storage.put(publicationPauseKey(this.env.PUBLICATION_ID), true)
      return json({ kind: 'public-static-search', manifest_sha256: PUBLIC_MANIFEST_SHA,
        publication_id: this.env.PUBLICATION_ID, active: false })
    }
    if (path === '/admin/compatibility') {
      this.compatibilityInFlight ??= this.compatibility().finally(() => { this.compatibilityInFlight = undefined })
      return json(await this.compatibilityInFlight)
    }
    if (path === '/admin/fresh-compatibility') {
      this.freshInFlight ??= this.freshCompatibility().finally(() => { this.freshInFlight = undefined })
      return json(await this.freshInFlight)
    }
    if (!['/admin/activate', '/admin/reset-compatibility'].includes(path)) fail('invalid_argument', 404, 'Unknown admin operation')
    const corpus = await this.ready()
    await this.release()
    await this.state.storage.transaction(async (tx) => {
      const release = checkedRelease(await tx.get<Release>(publicationStateKey(this.env.PUBLICATION_ID)), corpus.manifest.compatibility.indices)
      if (path === '/admin/activate') {
        if (release.compatibility.status !== 'passed') fail('embedding_compatibility_unverified', 409, 'Canary must pass before activation')
        this.checkedFresh(release.fresh, corpus.manifest.compatibility.indices)
        if (release.fresh.status !== 'passed' || Date.now() - release.fresh.checked_at! > 3600000
            || release.fresh.checked_at! > Date.now()) fail('embedding_compatibility_unverified', 409, 'A fresh 32-input check of this publication must pass within one hour of activation')
        release.activation = this.env.PUBLICATION_ID
        await tx.put(publicationPauseKey(this.env.PUBLICATION_ID), false)
      } else {
        if (this.active(release) || this.compatibilityInFlight || release.compatibility.status !== 'failed') {
          fail('compatibility_conflict', 409, 'Only inactive failed compatibility may be reset')
        }
        release.compatibility = freshCompatibility()
      }
      await tx.put(publicationStateKey(this.env.PUBLICATION_ID), release)
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
      const response = await clientContext.run(request.headers.get('cf-connecting-ip') ?? 'unknown', () => this.handler.fetch(request))
      if (response.status === 429) {
        const body = await response.clone().json() as { error?: { details?: { retry_after?: number } } }
        response.headers.set('retry-after', String(body.error?.details?.retry_after ?? retrySeconds()))
      }
      return response
    } catch (error) { return failed(error) }
  }
}

const publicManual = manual.replace('Uncached semantic queries share a 30/minute budget per client IP. On 429 wait\nRetry-After seconds. Read-only catalog/text/citation operations do not use it.',
  'Uncached semantic requests share 1000 query embeddings per UTC day across all\nclients, with 200/day and 20/minute per client IP (shared proxies share this).\nEach reserves 512 input tokens before submission; failed calls remain counted.\nOn 429 wait Retry-After seconds. Catalog/text/citation reads use no AI.\nThe account also has shared platform limits; availability is not guaranteed.')
export function createPublicGateway() {
  return { async fetch(request: Request, env: PublicSearchEnv): Promise<Response> {
    try {
      const url = new URL(request.url)
      requestOrigin(request)
      if (env.PUBLIC_PREVIEW === 'true' && !validProbeToken(env.PUBLICATION_TOKEN, request.headers.get('x-preview-token'))) {
        fail('forbidden', 403, 'Private release candidate')
      }
      if (env.PUBLIC_PREVIEW === 'true' && (!Number.isFinite(Date.parse(env.PUBLIC_PREVIEW_EXPIRES_AT ?? ''))
          || Date.parse(env.PUBLIC_PREVIEW_EXPIRES_AT!) <= Date.now())) fail('preview_expired', 503, 'Release candidate expired')
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
