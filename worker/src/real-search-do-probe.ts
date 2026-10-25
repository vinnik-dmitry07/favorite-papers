import vocabText from '../tokenizer/vocab.txt'

import { handleRest, json, requestOrigin } from './http'
import { handleMcp } from './mcp'
import { DomainError, errorBody, fail } from './schemas'
import { createService, type Service } from './service'
import { createStaticCorpusStore } from './static-corpus-store'
import { embed, WordPieceTokenizer } from './tokenize'

export const REAL_PROBE_OBJECT_NAME = 'real-corpus'
export const COMPATIBILITY_THRESHOLD = 0.999
export const COMPATIBILITY_BATCH_SIZE = 16
export const AI_TIMEOUT_MS = 20_000
export const AI_LIMITS = { total_texts: 300, query_texts: 24, input_tokens: 300 * 512 } as const
const LEDGER_KEY = 'real-probe-ledger-v1'
const SAFE_LABEL = /^[a-zA-Z0-9_.:-]{1,128}$/
const SHA256 = /^[a-f0-9]{64}$/

export interface RealProbeEnv {
  ASSETS: { fetch(request: Request): Promise<Response> }
  AI: {
    run(model: string, input: { text: string[], pooling: string }): Promise<{ data?: number[] | number[][] }>
  }
  SEARCH_PROBE: Pick<DurableObjectNamespace, 'idFromName' | 'get'>
  PROBE_TOKEN: string
  PROBE_EXPIRES_AT: string
  PROBE_MANIFEST_SHA: string
}

interface CompatibilityResult {
  index: number
  cosine: number
  remote_norm: number
}

interface Compatibility {
  status: 'not_started' | 'running' | 'passed' | 'failed'
  checked: number
  expected: number
  threshold: number
  min_cosine: number | null
  results: CompatibilityResult[]
  error?: string
}

interface Ledger {
  version: 1
  manifest_sha256: string
  compatibility_texts: number
  query_texts: number
  total_texts: number
  input_tokens: number
  ai_calls: number
  compatibility: Compatibility
  pending: number[] | null
}

type Corpus = Awaited<ReturnType<typeof createStaticCorpusStore>>
interface Dependencies { loadCorpus?: typeof createStaticCorpusStore }

function ensureLive(env: RealProbeEnv): void {
  const expiresAt = Date.parse(env.PROBE_EXPIRES_AT)
  if (!Number.isFinite(expiresAt) || Date.now() >= expiresAt) {
    fail('probe_expired', 503, 'this isolated probe has expired')
  }
}

function budgetOf(ledger: Ledger) {
  return {
    compatibility_texts: ledger.compatibility_texts,
    query_texts: ledger.query_texts,
    total_texts: ledger.total_texts,
    input_tokens: ledger.input_tokens,
    ai_calls: ledger.ai_calls,
    limits: AI_LIMITS,
  }
}

function validLedger(ledger: Ledger, manifestHash: string, indices: number[]): void {
  const expected = indices.length
  const counts = [ledger.compatibility_texts, ledger.query_texts, ledger.total_texts,
    ledger.input_tokens, ledger.ai_calls, ledger.compatibility?.checked]
  if (ledger.version !== 1 || ledger.manifest_sha256 !== manifestHash
      || counts.some((value) => !Number.isSafeInteger(value) || value < 0)
      || ledger.total_texts !== ledger.compatibility_texts + ledger.query_texts
      || ledger.total_texts > AI_LIMITS.total_texts || ledger.query_texts > AI_LIMITS.query_texts
      || ledger.input_tokens > AI_LIMITS.input_tokens
      || ledger.compatibility?.expected !== expected
      || ledger.compatibility.threshold !== COMPATIBILITY_THRESHOLD
      || !Array.isArray(ledger.compatibility.results)
      || ledger.compatibility.checked !== ledger.compatibility.results.length
      || ledger.compatibility.checked > expected
      || !['not_started', 'running', 'passed', 'failed'].includes(ledger.compatibility.status)
      || !(ledger.pending === null || (Array.isArray(ledger.pending)
        && ledger.pending.length > 0 && ledger.pending.length <= COMPATIBILITY_BATCH_SIZE
        && ledger.pending.every((index, position) => index === indices[ledger.compatibility.checked + position])))
      || ledger.compatibility.results.some((row, position) => !row
        || row.index !== indices[position] || !Number.isFinite(row.cosine)
        || row.cosine < -1 || row.cosine > 1 || !Number.isFinite(row.remote_norm) || row.remote_norm <= 0)
      || (ledger.compatibility.status === 'not_started'
        && (ledger.compatibility.checked !== 0 || ledger.pending !== null))
      || (ledger.compatibility.status === 'passed'
        && (ledger.compatibility.checked !== expected || ledger.pending !== null
          || ledger.compatibility.results.some((row) => row.cosine < COMPATIBILITY_THRESHOLD)))) {
    fail('probe_state_mismatch', 503, 'persistent probe state is invalid or belongs to another bundle')
  }
}

function vectorsFromResponse(result: { data?: number[] | number[][] }, count: number): number[][] {
  const data = result?.data
  const vectors = Array.isArray(data) && typeof data[0] === 'number' ? [data as number[]] : data
  if (!Array.isArray(vectors) || vectors.length !== count || vectors.some((vector) =>
    !Array.isArray(vector) || vector.length !== embed.dimensions
    || vector.some((value) => typeof value !== 'number' || !Number.isFinite(value))
    || vector.reduce((sum, value) => sum + value * value, 0) <= 0)) {
    fail('embedding_response_invalid', 503, 'Workers AI returned invalid embedding dimensions or values')
  }
  return vectors as number[][]
}

function compareVectors(index: number, reference: number[], remote: number[]): CompatibilityResult {
  let dot = 0
  let referenceSquared = 0
  let remoteSquared = 0
  for (let i = 0; i < reference.length; i++) {
    dot += reference[i] * remote[i]
    referenceSquared += reference[i] * reference[i]
    remoteSquared += remote[i] * remote[i]
  }
  const cosine = dot / Math.sqrt(referenceSquared * remoteSquared)
  if (!Number.isFinite(cosine)) fail('embedding_response_invalid', 503, 'embedding comparison is not finite')
  return { index, cosine: Math.max(-1, Math.min(1, cosine)), remote_norm: Math.sqrt(remoteSquared) }
}

/** One isolated object owns all initialization, semantic work, and durable AI limits. */
export class StaticSearchProbe {
  private readonly bootId = crypto.randomUUID()
  private firstRequest = true
  private corpusPromise: Promise<Corpus> | undefined
  private readyPromise: Promise<Corpus> | undefined
  private tokenizer: WordPieceTokenizer | undefined
  private service: Service | undefined
  private compatibilityInFlight: Promise<Ledger> | undefined

  constructor(private readonly state: DurableObjectState, private readonly env: RealProbeEnv,
    private readonly dependencies: Dependencies = {}) {}

  private getTokenizer() {
    this.tokenizer ??= new WordPieceTokenizer(vocabText)
    return this.tokenizer
  }

  private corpus(): Promise<Corpus> {
    if (!SHA256.test(this.env.PROBE_MANIFEST_SHA ?? '')) {
      fail('probe_config_invalid', 503, 'a pinned manifest SHA-256 is required')
    }
    this.corpusPromise ??= (this.dependencies.loadCorpus ?? createStaticCorpusStore)(
      this.env.ASSETS, this.env.PROBE_MANIFEST_SHA, (text) => this.embedQuery(text), async () => {
        const ledger = await this.readLedger()
        return ledger.query_texts < AI_LIMITS.query_texts
      },
    )
    return this.corpusPromise
  }

  private ready(): Promise<Corpus> {
    this.readyPromise ??= (async () => {
      const corpus = await this.corpus()
      const expected = corpus.manifest.compatibility_indices.length
      if (expected !== 200) fail('probe_config_invalid', 503, 'the real pilot requires exactly 200 compatibility passages')
      await this.state.storage.transaction(async (transaction) => {
        let ledger = await transaction.get<Ledger>(LEDGER_KEY)
        if (!ledger) {
          ledger = {
            version: 1, manifest_sha256: this.env.PROBE_MANIFEST_SHA,
            compatibility_texts: 0, query_texts: 0, total_texts: 0, input_tokens: 0, ai_calls: 0,
            compatibility: { status: 'not_started', checked: 0, expected,
              threshold: COMPATIBILITY_THRESHOLD, min_cosine: null, results: [] }, pending: null,
          }
        } else {
          validLedger(ledger, this.env.PROBE_MANIFEST_SHA, corpus.manifest.compatibility_indices)
          if (ledger.pending !== null) {
            // Reservation survived a restart but its outcome did not. Repeating it
            // could spend twice; keep the experiment incomplete and its charge counted.
            ledger.compatibility.status = 'failed'
            ledger.compatibility.error = 'interrupted_compatibility_batch'
            ledger.pending = null
          }
        }
        await transaction.put(LEDGER_KEY, ledger)
      })
      return corpus
    })()
    return this.readyPromise
  }

  private async readLedger(): Promise<Ledger> {
    const corpus = await this.ready()
    const ledger = await this.state.storage.get<Ledger>(LEDGER_KEY)
    if (!ledger) fail('probe_state_mismatch', 503, 'persistent probe state is missing')
    validLedger(ledger, this.env.PROBE_MANIFEST_SHA, corpus.manifest.compatibility_indices)
    return ledger
  }

  private countInputs(texts: string[]): number {
    let total = 0
    for (const text of texts) {
      const count = this.getTokenizer().tokenIds('', text).length
      if (count > embed.max_input_tokens) fail('probe_input_invalid', 400, 'an AI input exceeds the canonical token limit')
      total += count
    }
    return total
  }

  private async reserve(kind: 'compatibility' | 'query', texts: string[], indices?: number[]): Promise<Ledger> {
    ensureLive(this.env)
    const corpus = await this.ready()
    const tokens = this.countInputs(texts)
    return this.state.storage.transaction(async (transaction) => {
      const ledger = await transaction.get<Ledger>(LEDGER_KEY)
      if (!ledger) fail('probe_state_mismatch', 503, 'persistent probe state is missing')
      validLedger(ledger, this.env.PROBE_MANIFEST_SHA, corpus.manifest.compatibility_indices)
      if (kind === 'query' && ledger.compatibility.status !== 'passed') {
        fail('embedding_compatibility_unverified', 503, 'local and Workers AI embeddings have not passed compatibility')
      }
      if (kind === 'compatibility' && (ledger.pending !== null
          || !['not_started', 'running'].includes(ledger.compatibility.status))) {
        fail('compatibility_state_conflict', 409, 'compatibility is already complete or a batch is in flight')
      }
      if (ledger.total_texts + texts.length > AI_LIMITS.total_texts
          || ledger.input_tokens + tokens > AI_LIMITS.input_tokens
          || (kind === 'query' && ledger.query_texts + texts.length > AI_LIMITS.query_texts)) {
        fail('probe_ai_budget_exhausted', 429, 'the isolated probe AI budget is exhausted')
      }
      ledger.total_texts += texts.length
      ledger.input_tokens += tokens
      ledger.ai_calls += 1
      if (kind === 'query') ledger.query_texts += texts.length
      else {
        ledger.compatibility_texts += texts.length
        ledger.compatibility.status = 'running'
        ledger.pending = [...indices!]
      }
      // Reserve before calling AI. Errors, timeouts, and object restarts do not
      // refund the counters, since the provider may already have done the work.
      await transaction.put(LEDGER_KEY, ledger)
      return ledger
    })
  }

  private async callAi(texts: string[]): Promise<number[][]> {
    let timeout: ReturnType<typeof setTimeout> | undefined
    try {
      const result = await Promise.race([
        this.env.AI.run(embed.model, { text: texts, pooling: embed.pooling }),
        new Promise<never>((_resolve, reject) => {
          timeout = setTimeout(() => reject(new DomainError(
            'embedding_timeout', 503, 'Workers AI did not answer within the probe deadline',
          )), AI_TIMEOUT_MS)
        }),
      ])
      return vectorsFromResponse(result, texts.length)
    } catch (error) {
      if (error instanceof DomainError) throw error
      throw new DomainError('embedding_request_failed', 503, 'Workers AI request failed; its reservation remains counted')
    } finally {
      if (timeout !== undefined) clearTimeout(timeout)
    }
  }

  private async embedQuery(text: string): Promise<number[]> {
    await this.reserve('query', [text])
    return (await this.callAi([text]))[0]
  }

  private async requireCompatible(): Promise<void> {
    if ((await this.readLedger()).compatibility.status !== 'passed') {
      fail('embedding_compatibility_unverified', 503, 'local and Workers AI embeddings have not passed compatibility')
    }
  }

  private serviceFor(corpus: Corpus): Service {
    if (!this.service) {
      const underlying = createService(corpus.store, this.getTokenizer())
      this.service = {
        ...underlying,
        search: async (args) => {
          await this.requireCompatible()
          return underlying.search(args)
        },
        researchSearch: async (query, ip) => {
          await this.requireCompatible()
          return underlying.researchSearch(query, ip)
        },
      }
    }
    return this.service
  }

  private async nextCompatibilityBatch(): Promise<Ledger> {
    const corpus = await this.ready()
    const ledger = await this.readLedger()
    if (ledger.compatibility.status === 'passed' || ledger.compatibility.status === 'failed') return ledger
    const indices = corpus.manifest.compatibility_indices.slice(
      ledger.compatibility.checked, ledger.compatibility.checked + COMPATIBILITY_BATCH_SIZE,
    )
    const references = indices.map((index) => corpus.referencePassage(index))
    await this.reserve('compatibility', references.map((reference) => reference.input), indices)
    let results: CompatibilityResult[] = []
    let error: string | undefined
    try {
      const vectors = await this.callAi(references.map((reference) => reference.input))
      results = vectors.map((vector, index) => compareVectors(indices[index], references[index].vector, vector))
    } catch (cause) {
      error = cause instanceof DomainError ? cause.code : 'embedding_request_failed'
    }
    return this.state.storage.transaction(async (transaction) => {
      const current = await transaction.get<Ledger>(LEDGER_KEY)
      if (!current) fail('probe_state_mismatch', 503, 'persistent probe state is missing')
      validLedger(current, this.env.PROBE_MANIFEST_SHA, corpus.manifest.compatibility_indices)
      if (JSON.stringify(current.pending) !== JSON.stringify(indices)) {
        fail('compatibility_state_conflict', 409, 'the reserved compatibility batch changed')
      }
      current.pending = null
      current.compatibility.results.push(...results)
      current.compatibility.checked += results.length
      current.compatibility.min_cosine = current.compatibility.results.length
        ? Math.min(...current.compatibility.results.map((row) => row.cosine)) : null
      if (error || results.some((row) => row.cosine < COMPATIBILITY_THRESHOLD)) {
        current.compatibility.status = 'failed'
        current.compatibility.error = error ?? 'embedding_cosine_below_threshold'
      } else if (current.compatibility.checked === current.compatibility.expected) {
        current.compatibility.status = 'passed'
      }
      await transaction.put(LEDGER_KEY, current)
      return current
    })
  }

  private advanceCompatibility(): Promise<Ledger> {
    if (!this.compatibilityInFlight) {
      const work = this.nextCompatibilityBatch()
      this.compatibilityInFlight = work
      void work.finally(() => {
        if (this.compatibilityInFlight === work) this.compatibilityInFlight = undefined
      }).catch(() => {})
    }
    return this.compatibilityInFlight
  }

  async fetch(request: Request): Promise<Response> {
    const marker = request.headers.get('x-probe-marker') ?? crypto.randomUUID()
    const objectId = this.state.id.toString()
    const first = this.firstRequest
    this.firstRequest = false
    console.log({ kind: 'real_do_probe', runtime_role: 'durable_object', probe_marker: marker,
      run_id: request.headers.get('x-probe-run-id'), object_id: objectId, boot_id: this.bootId })
    let response: Response
    try {
      ensureLive(this.env)
      requestOrigin(request)
      const corpus = await this.ready()
      const url = new URL(request.url)
      if (url.pathname === '/probe/info' && request.method === 'GET') {
        const ledger = await this.readLedger()
        response = json({
          probe_type: 'real-subset', synthetic: false, runtime: 'durable-object', scope: 'subset',
          release_id: corpus.manifest.release_id, source_sha: corpus.manifest.source_sha,
          manifest_sha256: this.env.PROBE_MANIFEST_SHA, passage_count: corpus.manifest.passage_count,
          paper_ids: corpus.manifest.paper_ids, sample_paper_id: corpus.manifest.sample_paper_id,
          queries: corpus.manifest.queries, compatibility_indices: corpus.manifest.compatibility_indices,
          compatibility: ledger.compatibility, budget: budgetOf(ledger),
        })
      } else if (url.pathname === '/probe/compatibility') {
        if (request.method !== 'GET' && request.method !== 'POST') {
          response = new Response(null, { status: 405, headers: { allow: 'GET, POST' } })
        } else {
          // Request bodies cannot choose a model, passage, vector or batch size.
          const ledger = request.method === 'POST' ? await this.advanceCompatibility() : await this.readLedger()
          response = json({ ...ledger.compatibility, budget: budgetOf(ledger),
            manifest_sha256: this.env.PROBE_MANIFEST_SHA, release_id: corpus.manifest.release_id })
        }
      } else {
        const service = this.serviceFor(corpus)
        if (url.pathname === '/health' && (request.method === 'GET' || request.method === 'HEAD')) {
          const ledger = await this.readLedger()
          const compatible = ledger.compatibility.status === 'passed'
          const health = await service.health()
          response = json({ ...health,
            status: compatible ? health.status : 'degraded',
            search_enabled: compatible && health.search_enabled,
            scope: 'subset', compatibility_gate: ledger.compatibility.status,
            production_readiness: 'unverified',
          }, compatible ? 200 : 503)
        } else if (url.pathname === '/mcp') {
          response = request.method === 'POST' ? await handleMcp(request, service)
            : new Response(null, { status: 405, headers: { allow: 'POST' } })
        } else response = await handleRest(request, service)
      }
    } catch (error) {
      const domain = error instanceof DomainError ? error : new DomainError('probe_unavailable', 503, 'real probe initialization failed')
      console.error({ kind: 'real_do_probe_error', code: domain.code, probe_marker: marker })
      response = json(errorBody(domain), domain.status)
    }
    const headers = new Headers(response.headers)
    headers.set('x-probe-runtime', 'durable-object')
    headers.set('x-probe-kind', 'real-subset')
    headers.set('x-probe-synthetic', 'false')
    headers.set('x-probe-marker', marker)
    headers.set('x-probe-object-id', objectId)
    headers.set('x-probe-boot-id', this.bootId)
    headers.set('x-probe-manifest-sha256', this.env.PROBE_MANIFEST_SHA)
    headers.set('x-probe-cold-kind', first ? 'object-constructor' : 'warm')
    return new Response(response.body, { status: response.status, statusText: response.statusText, headers })
  }
}

export function createRealProbeGateway() {
  let bootId: string | undefined
  return {
    async fetch(request: Request, env: RealProbeEnv): Promise<Response> {
      try {
        ensureLive(env)
        if (typeof env.PROBE_TOKEN !== 'string' || env.PROBE_TOKEN.length < 32
            || request.headers.get('x-probe-token') !== env.PROBE_TOKEN) {
          fail('probe_forbidden', 403, 'a valid isolated-probe token is required')
        }
        const suppliedMarker = request.headers.get('x-probe-marker')
        const runId = request.headers.get('x-probe-run-id')
        if ((suppliedMarker !== null && !SAFE_LABEL.test(suppliedMarker))
            || (runId !== null && !SAFE_LABEL.test(runId))) {
          fail('invalid_probe_marker', 400, 'probe markers must be bounded identifiers')
        }
        const marker = suppliedMarker ?? crypto.randomUUID()
        bootId ??= crypto.randomUUID()
        console.log({ kind: 'real_do_probe', runtime_role: 'gateway', probe_marker: marker,
          run_id: runId, boot_id: bootId })
        const headers = new Headers(request.headers)
        headers.delete('x-probe-token')
        headers.set('x-probe-marker', marker)
        const id = env.SEARCH_PROBE.idFromName(REAL_PROBE_OBJECT_NAME)
        return await env.SEARCH_PROBE.get(id).fetch(new Request(request, { headers }))
      } catch (error) {
        const domain = error instanceof DomainError ? error : new DomainError('probe_unavailable', 503, 'isolated probe routing failed')
        return json(errorBody(domain), domain.status)
      }
    },
  }
}

export default createRealProbeGateway()
