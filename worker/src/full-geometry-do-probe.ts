import vocabText from '../tokenizer/vocab.txt'
import { createGeometryFixtureStoreLoader } from './full-corpus-store'
import { BoundedAdmission, createBoundedProbeHandler, PROBE_REQUEST_LIMITS } from './probe-admission'
import { validProbeToken } from './probe-auth'
import { DomainError, errorBody } from './schemas'
import { createService, type Service } from './service'
import { WordPieceTokenizer } from './tokenize'

export interface GeometryProbeEnv {
  ASSETS: { fetch(request: Request): Promise<Response> }
  SEARCH_PROBE: Pick<DurableObjectNamespace, 'idFromName' | 'get'>
  PROBE_TOKEN: string
  PROBE_EXPIRES_AT: string
  PROBE_MANIFEST_SHA: string
  PQ_WASM?: WebAssembly.Module
}

export const GEOMETRY_OBJECT_NAME = 'full-synthetic-corpus'
export const GEOMETRY_REQUEST_CAP = 350
const SAFE_LABEL = /^[a-zA-Z0-9_.:-]{1,128}$/
const json = (value: unknown, status = 200) => new Response(JSON.stringify(value), {
  status, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' },
})
const expired = (env: GeometryProbeEnv) => !Number.isFinite(Date.parse(env.PROBE_EXPIRES_AT))
  || Date.now() >= Date.parse(env.PROBE_EXPIRES_AT)

/** Full-size storage/search mechanics only: no inference binding or semantic claim. */
export class StaticSearchProbe {
  private readonly bootId = crypto.randomUUID()
  private requests = 0
  private embeddedQueries = 0
  private readonly queryVectors: number[][] = []
  private preparing: Promise<void> | undefined
  private service: Promise<Service> | undefined
  private readonly load: ReturnType<typeof createGeometryFixtureStoreLoader>
  private readonly admission = new BoundedAdmission(PROBE_REQUEST_LIMITS.active,
    PROBE_REQUEST_LIMITS.queued, PROBE_REQUEST_LIMITS.queue_wait_ms)
  private readonly handler: ReturnType<typeof createBoundedProbeHandler>

  constructor(private readonly state: DurableObjectState, private readonly env: GeometryProbeEnv) {
    this.load = createGeometryFixtureStoreLoader(env.ASSETS, env.PROBE_MANIFEST_SHA, async (text) => {
      const match = /^memory workload query (\d{1,3})$/.exec(text)
      if (!match || Number(match[1]) >= 160 || this.queryVectors.length !== 16) {
        throw new DomainError('invalid_argument', 400, 'only prepared synthetic workload queries are allowed')
      }
      this.embeddedQueries++
      return this.queryVectors[Number(match[1]) % 16]
    }, undefined, { module: env.PQ_WASM })
    this.handler = createBoundedProbeHandler(() => this.service ??= this.load().then(
      ({ store }) => createService(store, new WordPieceTokenizer(vocabText))), this.admission)
  }

  private async control(path: string, request: Request) {
    if (request.method !== 'GET' || request.body) return json({ error: 'method_not_allowed' }, 405)
    if (path !== '/_probe/status' && path !== '/_probe/prepare') return json({ error: 'not_found' }, 404)
    return this.admission.run(async () => {
      const corpus = await this.load()
      if (path === '/_probe/prepare') {
        this.preparing ??= (async () => {
          const vectors: number[][] = []
          for (let i = 0; i < 16; i++) {
            const index = Math.floor(i * (corpus.manifest.compatibility.indices.length - 1) / 15)
            vectors.push((await corpus.referencePassage(index)).vector)
          }
          this.queryVectors.push(...vectors)
        })()
        await this.preparing
      }
      return json({ kind: 'full-geometry-probe', synthetic: true,
        manifest_sha256: this.env.PROBE_MANIFEST_SHA, release_id: corpus.manifest.release_id,
        passages: corpus.manifest.passage_count, papers: corpus.manifest.paper_ids.length,
        text_papers: corpus.manifest.text_paper_ids.length, prepared_queries: this.queryVectors.length,
        embedded_queries: this.embeddedQueries, requests: this.requests,
        admission: this.admission.stats(), paper_loads: corpus.paperLoadStats(),
        memory: { status: 'unverified', reason: 'no platform memory counter' },
        quality: { status: 'not_measured', reason: 'synthetic vectors' } })
    }, request.signal)
  }

  async fetch(request: Request): Promise<Response> {
    const first = this.requests === 0
    this.requests++
    const marker = request.headers.get('x-probe-marker')
    const runId = request.headers.get('x-probe-run-id')
    console.log({ kind: 'full_geometry_probe', runtime_role: 'durable_object',
      run_id: runId, probe_marker: marker, boot_id: this.bootId, object_id: this.state.id.toString() })
    let response: Response
    try {
      if (expired(this.env)) response = json({ error: 'probe_expired' }, 503)
      else if (this.requests > GEOMETRY_REQUEST_CAP) response = json({ error: 'probe_request_budget' }, 429)
      else if (request.url.length > PROBE_REQUEST_LIMITS.url_characters) response = json({ error: 'invalid_argument' }, 414)
      else {
        const path = new URL(request.url).pathname
        response = path.startsWith('/_probe/') ? await this.control(path, request)
          : await this.handler.fetch(request)
      }
    } catch (error) {
      const known = error instanceof DomainError ? error
        : new DomainError('corpus_unavailable', 503, 'geometry probe request failed')
      console.error({ kind: 'full_geometry_probe_error', code: known.code, probe_marker: marker })
      response = json(errorBody(known), known.status)
    }
    response.headers.set('x-probe-boot-id', this.bootId)
    response.headers.set('x-probe-first-request', String(first))
    response.headers.set('x-probe-runtime-role', 'durable_object')
    response.headers.set('x-probe-object-id', this.state.id.toString())
    response.headers.set('x-probe-marker', marker ?? '')
    response.headers.set('x-probe-synthetic', 'true')
    response.headers.set('x-probe-manifest-sha256', this.env.PROBE_MANIFEST_SHA)
    return response
  }
}

export function createGeometryGateway() {
  let bootId: string | undefined
  return {
    async fetch(request: Request, env: GeometryProbeEnv): Promise<Response> {
      if (expired(env)) return json({ error: 'probe_expired' }, 503)
      if (!validProbeToken(env.PROBE_TOKEN, request.headers.get('x-probe-token'))) return json({ error: 'probe_forbidden' }, 403)
      if (!/^[0-9a-f]{64}$/.test(env.PROBE_MANIFEST_SHA)) return json({ error: 'config_mismatch' }, 503)
      const marker = request.headers.get('x-probe-marker') ?? crypto.randomUUID()
      const runId = request.headers.get('x-probe-run-id')
      if (!SAFE_LABEL.test(marker) || (runId !== null && !SAFE_LABEL.test(runId))) return json({ error: 'invalid_probe_marker' }, 400)
      bootId ??= crypto.randomUUID()
      console.log({ kind: 'full_geometry_probe', runtime_role: 'gateway', run_id: runId,
        probe_marker: marker, boot_id: bootId })
      const headers = new Headers(request.headers)
      headers.delete('x-probe-token')
      headers.set('x-probe-marker', marker)
      const id = env.SEARCH_PROBE.idFromName(GEOMETRY_OBJECT_NAME)
      return env.SEARCH_PROBE.get(id).fetch(new Request(request, { headers }))
    },
  }
}

export default createGeometryGateway()
