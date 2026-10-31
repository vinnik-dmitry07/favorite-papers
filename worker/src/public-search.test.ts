import { afterEach, describe, expect, it, vi } from 'vitest'
import type { createFullCorpusStoreLoader } from './full-corpus-store'
import { createPublicGateway, PublicSearch, PUBLIC_LIMITS, PUBLIC_MANIFEST_SHA,
  PUBLIC_OBJECT_NAME, publicationStateKey, CLIENT_LIMITS, type PublicSearchEnv } from './public-search'
import { signatures, sha256Hex } from './signatures'

const PUBLIC_RELEASE_KEY = publicationStateKey('publication-one')
const TOKEN = 'publication-test-token-at-least-thirty-two-characters'
const VECTOR = [1, ...Array(767).fill(0)]
const INDICES = Array.from({ length: 200 }, (_, i) => 40574 - i * 173)
const ID = 'arxiv:2402.03300'
const TEXT = 'DeepSeekMath evidence: group size 64 and KL 0.04. 😀'
const RELEASE = 'b'.repeat(64)

async function setup() {
  const data = new Map<string, any>()
  const get = async <T>(key: string) => structuredClone(data.get(key)) as T | undefined
  const put = async (key: string, value: unknown) => { data.set(key, structuredClone(value)) }
  let tail: Promise<unknown> = Promise.resolve()
  const storage = { get, put, transaction: <T>(work: (tx: { get: typeof get, put: typeof put }) => Promise<T>) => {
    const result = tail.then(() => work({ get, put })); tail = result.catch(() => {}); return result
  } }
  const state = { storage } as unknown as DurableObjectState
  const sig = await signatures()
  const documents = new Map<string, unknown>()
  documents.set('active.json', { release_id: RELEASE, slot: 'full-probe', activated_at: 0,
    reader_schema: 1, embedding_signature: sig.embedding, build_signature: sig.build,
    verified_passage_count: 40575, global_index_count: 40575,
    publication_check: { ok: true, checked_at: 0, by: 'test' } })
  documents.set(`releases/${RELEASE}/graph.json`, { nodes: { [ID]: { id: ID, title: 'DeepSeekMath',
    url: 'https://arxiv.org/abs/2402.03300', text: { available: true, reason: null,
      code_points: [...TEXT].length, chunks: 1 } } }, out: { [ID]: [] }, in: { [ID]: [] } })
  documents.set(`releases/${RELEASE}/papers/${await sha256Hex(ID)}.json`, { paper_id: ID, text: TEXT,
    chunks: [{ index: 0, start: 0, end: [...TEXT].length, token_count: 20, content_hash: 'h', input_hash: 'i' }] })
  documents.set('slots/full-probe/confirmed.json', { release_id: RELEASE, embedding_signature: sig.embedding,
    build_signature: sig.build, passage_count: 1, vectors: { v: { paper_id: ID, chunk_index: 0,
      content_hash: 'h', input_hash: 'i' } } })
  let embedQuery!: (text: string) => Promise<number[]>
  const loader = vi.fn((_assets, _hash, embedder) => {
    embedQuery = embedder
    const corpus = { manifest: { kind: 'full-corpus-int8', synthetic: false, passage_count: 40575,
      release_id: RELEASE, compatibility: { indices: INDICES } },
    store: { now: () => Date.now(), getJson: async (key: string) => documents.get(key) ?? null,
      embed: embedder, query: async () => [{ id: 'v', score: 0.9 }], rateLimit: async () => true },
    referencePassage: async (ordinal: number) => ({ input: 'Canonical sample ' + ordinal, vector: [...VECTOR] }) }
    return async () => corpus
  }) as unknown as typeof createFullCorpusStoreLoader
  const forwarded = vi.fn(async () => new Response('forwarded'))
  const env = { PUBLICATION_ID: 'publication-one', PUBLICATION_TOKEN: TOKEN, PUBLIC_MANIFEST_SHA,
    ASSETS: { fetch: vi.fn() }, AI: { run: vi.fn(async (_model: string, input: { text: string[] }) =>
      ({ data: input.text.map(() => [...VECTOR]) })) },
    PUBLIC_SEARCH: { idFromName: vi.fn(() => 'fixed-object'), get: vi.fn(() => ({ fetch: forwarded })) },
  } as unknown as PublicSearchEnv
  let object = new PublicSearch(state, env, { loader })
  const request = (path: string, method = 'GET', body?: unknown, token: string | null = TOKEN) =>
    new Request('https://public-test.workers.dev' + path, { method,
      headers: { ...(token ? { 'x-publication-token': token } : {}), 'content-type': 'application/json',
        accept: 'application/json, text/event-stream' }, ...(body === undefined ? {} : { body: JSON.stringify(body) }) })
  const call = async (path = '/admin/state', method = 'GET', body?: unknown, token: string | null = TOKEN) => {
    const response = await object.fetch(request(path, method, body, token))
    const text = await response.text()
    return { response, body: JSON.parse(text.includes('data:')
      ? text.split('\n').filter((line) => line.startsWith('data:')).at(-1)!.slice(5) : text) }
  }
  const rpc = (name: string, args: unknown) => call('/mcp', 'POST', {
    jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name, arguments: args } }, null)
  const compatible = async () => { for (let i = 0; i < 13; i++) expect((await call('/admin/compatibility', 'POST')).response.status).toBe(200) }
  const fresh = async () => { for (let i = 0; i < 2; i++) expect((await call('/admin/fresh-compatibility', 'POST')).response.status).toBe(200) }
  const activate = async () => { await compatible(); await fresh(); expect((await call('/admin/activate', 'POST')).body.active).toBe(true) }
  return { data, env, call, rpc, request, loader, forwarded, compatible, fresh, activate,
    fetch: (request: Request) => object.fetch(request),
    restart: () => { object = new PublicSearch(state, env, { loader }) },
    embedQuery: (text: string) => embedQuery(text) }
}
afterEach(() => { vi.useRealTimers(); vi.restoreAllMocks() })

describe('permanent public full-corpus API', () => {
  it('rejects unauthenticated admin before DO access and serves truthful discovery without loading the index', async () => {
    const f = await setup(), gateway = createPublicGateway()
    for (const token of [null, 'incorrect']) {
      expect((await gateway.fetch(f.request('/admin/state', 'GET', undefined, token), f.env)).status).toBe(403)
      expect((await f.call('/admin/state', 'GET', undefined, token)).response.status).toBe(403)
    }
    expect(f.env.PUBLIC_SEARCH.get).not.toHaveBeenCalled(); expect(f.loader).not.toHaveBeenCalled()
    expect((await gateway.fetch(f.request('/probe/info'), f.env)).status).toBe(404)
    const unsupported = await gateway.fetch(f.request('/mcp'), f.env)
    expect(unsupported.status).toBe(405); expect(unsupported.headers.get('allow')).toBe('POST')
    const manual = await (await gateway.fetch(f.request('/llms.txt'), f.env)).text()
    expect(manual).toContain('1000 query embeddings per UTC day'); expect(manual).not.toContain('30/minute')
    const spec = (await f.call('/openapi.json')).body
    expect(spec.paths['/v1/search'].get.responses['429'].description).toContain('00:00 UTC')
    expect(f.loader).not.toHaveBeenCalled()
    expect((await gateway.fetch(f.request('/v1/catalog', 'GET', undefined, null), f.env)).status).toBe(200)
    expect(f.env.PUBLIC_SEARCH.idFromName).toHaveBeenCalledWith(PUBLIC_OBJECT_NAME)
  })

  it('starts inactive while catalog and Unicode content reads remain public and AI-free', async () => {
    const f = await setup()
    expect((await f.call('/admin/state')).body).toMatchObject({ active: false, passage_count: 40575,
      compatibility: { status: 'not_started' }, budget: { query_texts: 0 } })
    expect((await f.call('/health')).body).toMatchObject({ status: 'degraded', search_enabled: false })
    expect((await f.call('/v1/catalog?q=DeepSeekMath')).body.papers[0].id).toBe(ID)
    expect((await f.call('/v1/content?id=' + ID)).body.text).toBe(TEXT)
    expect((await f.call('/v1/search?q=reasoning')).response.status).toBe(503)
    expect((await f.rpc('search', { query: 'DeepSeekMath' })).body.result.isError).toBe(true)
    expect((await f.call('/admin/activate', 'POST')).response.status).toBe(409)
    expect(f.env.AI.run).not.toHaveBeenCalled()
  })

  it('checks all200 samples once, activates REST/MCP, and retains results and query budget over restart', async () => {
    const f = await setup(); await f.activate()
    const state = (await f.call()).body
    expect(state.compatibility.results.map((row: any) => row.index)).toEqual(INDICES)
    expect(state.budget).toMatchObject({ compatibility_texts: 200, compatibility_tokens_reserved: 102400, ai_calls: 13 })
    expect((await f.call('/health')).body).toMatchObject({ status: 'ready', search_enabled: true, publication_id: 'publication-one' })
    const search = await f.call('/v1/search?q=reasoning')
    expect(search.body.hits[0].paper_id).toBe(ID)
    await f.call('/v1/search?q=reasoning') // Same cached query has no new reservation.
    expect((await f.call()).body.budget.query_texts).toBe(1)
    const found = await f.rpc('search', { query: 'DeepSeekMath' })
    const fetched = await f.rpc('fetch', { id: found.body.result.structuredContent.results[0].id })
    expect(fetched.body.result.structuredContent.text).toBe(TEXT)
    f.restart(); expect((await f.call()).body.active).toBe(true)
    await f.call('/admin/compatibility', 'POST')
    expect(f.env.AI.run).toHaveBeenCalledTimes(16)
    await f.call('/admin/deactivate', 'POST')
    expect((await f.call('/v1/search?q=reasoning')).response.status).toBe(503)
    expect((await f.call('/v1/content?id=' + ID)).body.text).toBe(TEXT)
  })

  it('does not inherit activation when PUBLICATION_ID changes, but preserves canary and global quota', async () => {
    const f = await setup(); await f.activate(); await f.embedQuery('A query')
    f.env.PUBLICATION_ID = 'publication-two'; f.restart()
    const state = (await f.call()).body
    expect(state.active).toBe(false); expect(state.compatibility.status).toBe('passed')
    expect(state.budget.query_texts).toBe(1)
    expect((await f.call('/admin/activate', 'POST')).response.status).toBe(409)
    await f.fresh(); await f.call('/admin/activate', 'POST'); expect((await f.call()).body.active).toBe(true)
    expect(f.env.AI.run).toHaveBeenCalledTimes(18)
  })

  it('atomically admits only one concurrent request at the remaining daily allowance and resets only the UTC-day budget', async () => {
    vi.useFakeTimers(); vi.setSystemTime(new Date('2026-10-29T12:00:00Z'))
    const f = await setup(); await f.activate()
    const budget = f.data.get('public-ai-day-v1')
    budget.query_texts = 999; budget.query_tokens_reserved = 999 * 512; budget.ai_calls += 999
    const results = await Promise.allSettled(Array.from({ length: 8 }, () => f.embedQuery('new query')))
    expect(results.filter((r) => r.status === 'fulfilled')).toHaveLength(1)
    expect(f.data.get('public-ai-day-v1').query_texts).toBe(1000)
    const denied = await f.call('/v1/search?q=uncached')
    expect(denied.response.status).toBe(429); expect(denied.response.headers.get('retry-after')).toBe('43200')
    f.restart(); expect((await f.call()).body.budget.query_texts).toBe(1000)
    vi.setSystemTime(new Date('2026-10-30T00:00:00Z')); await f.embedQuery('next day')
    const next = (await f.call()).body
    expect(next.budget).toMatchObject({ day: '2026-10-30', query_texts: 1, compatibility_texts: 0 })
    expect(next.active).toBe(true); expect(next.compatibility.checked).toBe(200)
  })

  it('counts failures without retry and bounds actual pending providers after HTTP timeouts', async () => {
    vi.useFakeTimers(); const f = await setup(); await f.activate()
    const before = vi.mocked(f.env.AI.run).mock.calls.length
    vi.mocked(f.env.AI.run).mockImplementation(() => new Promise(() => {}))
    const waiting = Promise.allSettled(Array.from({ length: 4 }, () => f.embedQuery('a query')))
    await vi.waitFor(() => expect(f.env.AI.run).toHaveBeenCalledTimes(before + 4))
    await vi.advanceTimersByTimeAsync(PUBLIC_LIMITS.ai_timeout_ms)
    expect((await waiting).every((row) => row.status === 'rejected')).toBe(true)
    await expect(f.embedQuery('another query')).rejects.toMatchObject({ code: 'probe_overloaded' })
    expect(f.env.AI.run).toHaveBeenCalledTimes(before + 4)
    expect((await f.call()).body.budget.query_texts).toBe(4)
  })

  it('fails an incompatible canary and allows only authenticated inactive reset without refund', async () => {
    const f = await setup()
    vi.mocked(f.env.AI.run).mockImplementationOnce(async (_model, input) => ({ data: input.text.map(() => VECTOR.map((x) => -x)) }))
    expect((await f.call('/admin/compatibility', 'POST')).body.status).toBe('failed')
    expect((await f.call('/admin/activate', 'POST')).response.status).toBe(409)
    expect((await f.call('/admin/reset-compatibility', 'POST')).body.compatibility.status).toBe('not_started')
    expect((await f.call()).body.budget.compatibility_texts).toBe(16)
    expect((await f.call('/admin/reset-compatibility', 'POST')).response.status).toBe(409)
  })

  it('never dispatches AI if quota preparation finishes after the HTTP deadline', async () => {
    vi.useFakeTimers(); const f = await setup(); await f.activate()
    const before = vi.mocked(f.env.AI.run).mock.calls.length
    let finish: (() => void) | undefined
    vi.spyOn(crypto.subtle, 'digest').mockImplementationOnce(() => new Promise<ArrayBuffer>((resolve) => {
      finish = () => resolve(new ArrayBuffer(32))
    }))
    const pending = f.embedQuery('delayed preparation').catch((error) => error)
    await vi.waitFor(() => expect(finish).toBeDefined())
    await vi.advanceTimersByTimeAsync(PUBLIC_LIMITS.ai_timeout_ms)
    expect(await pending).toMatchObject({ code: 'embedding_timeout' })
    finish!()
    await vi.waitFor(() => expect(f.data.get('public-ai-day-v1').query_texts).toBe(1))
    expect(f.env.AI.run).toHaveBeenCalledTimes(before)
  })

  it('fails closed on interrupted canary reservation and invalid durable counters', async () => {
    const f = await setup(); await f.call()
    const release = f.data.get(PUBLIC_RELEASE_KEY)
    release.compatibility.status = 'running'; release.compatibility.pending = INDICES.slice(0, 16)
    f.restart()
    expect((await f.call()).body.compatibility).toMatchObject({ status: 'failed', error: 'interrupted_compatibility_batch' })
    f.data.set('public-ai-day-v1', { day: new Date().toISOString().slice(0, 10),
      query_texts: 0, query_tokens_reserved: -1, compatibility_texts: 0,
      compatibility_tokens_reserved: 0, ai_calls: 0 })
    f.restart(); expect((await f.call()).response.status).toBe(503)
    expect(f.env.AI.run).not.toHaveBeenCalled()
  })

  it('keeps catalog, text and degraded health available when current AI state is corrupt', async () => {
    const f = await setup(); await f.activate()
    f.data.get('public-ai-day-v1').query_tokens_reserved = -1
    f.restart()
    expect((await f.call('/v1/catalog')).response.status).toBe(200)
    expect((await f.call('/v1/content?id=' + ID)).body.text).toBe(TEXT)
    expect((await f.call('/health')).body).toMatchObject({ status: 'degraded', search_enabled: false,
      search_error: 'public_state_invalid' })
    expect((await f.call('/v1/search?q=new')).response.status).toBe(503)
    f.data.set(PUBLIC_RELEASE_KEY, { manifest_sha256: PUBLIC_MANIFEST_SHA, compatibility: null })
    f.restart()
    expect((await f.call('/v1/catalog')).response.status).toBe(200)
    expect((await f.call('/health')).body.search_enabled).toBe(false)
    expect((await f.call('/admin/deactivate', 'POST')).body.active).toBe(false)
  })

  it('discards expired counters before validating them and treats a reduced cap as exhaustion', async () => {
    vi.useFakeTimers(); vi.setSystemTime(new Date('2026-10-29T12:00:00Z'))
    const f = await setup(); await f.activate()
    const budget = f.data.get('public-ai-day-v1')
    budget.query_texts = 1001; budget.query_tokens_reserved = 1001 * 512; budget.ai_calls += 1001
    expect((await f.call()).response.status).toBe(200)
    expect((await f.call('/v1/search?q=uncached')).response.status).toBe(429)
    expect((await f.call('/v1/catalog')).response.status).toBe(200)
    // Even obsolete/corrupt counters from yesterday cannot poison today's ledger.
    budget.query_tokens_reserved = -1
    vi.setSystemTime(new Date('2026-10-30T00:00:00Z')); f.restart()
    expect((await f.call()).body.budget).toMatchObject({ query_texts: 0, compatibility_texts: 0 })
    await f.embedQuery('next day')
    expect((await f.call()).body.budget.query_texts).toBe(1)
  })

  it('migrates only matching legacy compatibility and never resets the global daily ledger', async () => {
    const f = await setup(); await f.activate(); await f.embedQuery('already used')
    const old = structuredClone(f.data.get(PUBLIC_RELEASE_KEY))
    f.data.set('public-release-v1', old); f.data.delete(PUBLIC_RELEASE_KEY); f.restart()
    expect((await f.call()).body.active).toBe(true)
    expect((await f.call()).body.budget.query_texts).toBe(1)
    f.data.delete('public-compatibility-v1:' + PUBLIC_MANIFEST_SHA)
    old.manifest_sha256 = 'f'.repeat(64)
    f.data.set('public-release-v1', old); f.data.delete(PUBLIC_RELEASE_KEY); f.restart()
    const next = (await f.call()).body
    expect(next.compatibility.status).toBe('not_started'); expect(next.active).toBe(false)
    expect(next.budget.query_texts).toBe(1)
    expect(f.data.get('public-release-v1').manifest_sha256).toBe('f'.repeat(64))
  })

  it('can pause before loading any assets and keeps the pause over restart', async () => {
    const f = await setup()
    vi.mocked(f.loader).mockImplementationOnce(() => async () => { throw new Error('assets unavailable') })
    const paused = await f.call('/admin/deactivate', 'POST')
    expect(paused.response.status).toBe(200)
    expect(paused.body).toMatchObject({ kind: 'public-static-search', publication_id: 'publication-one', active: false })
    expect(f.loader).not.toHaveBeenCalled()
    expect((await f.call('/v1/catalog')).response.status).toBe(503)
    f.restart(); await f.activate()
    await f.call('/admin/deactivate', 'POST'); f.restart()
    expect((await f.call()).body.active).toBe(false)
    await expect(f.embedQuery('paused')).rejects.toMatchObject({ code: 'search_disabled' })
    expect((await f.call('/v1/content?id=' + ID)).body.text).toBe(TEXT)
  })

  it('pauses immediately while every request permit is occupied by a hung provider', async () => {
    vi.useFakeTimers()
    const f = await setup(); await f.activate()
    vi.mocked(f.env.AI.run).mockImplementation(() => new Promise(() => {}))
    const pending = Promise.all(Array.from({ length: 4 }, (_, i) => f.call('/v1/search?q=hanging' + i)))
    await vi.advanceTimersByTimeAsync(0)
    expect((await f.call('/admin/deactivate', 'POST')).body.active).toBe(false)
    await vi.advanceTimersByTimeAsync(PUBLIC_LIMITS.ai_timeout_ms)
    expect((await pending).every((r) => r.response.status === 503)).toBe(true)
    expect((await f.call()).body.active).toBe(false)
  })

  it('rejects a pause targeting another publication before changing durable state', async () => {
    const f = await setup(); await f.activate()
    const request = f.request('/admin/deactivate', 'POST', {})
    request.headers.set('x-publication-id', 'another-publication')
    expect((await new PublicSearch({ storage: {} } as DurableObjectState, f.env).fetch(request)).status).toBe(409)
    expect((await f.call()).body.active).toBe(true)
  })

  it('requires a fresh model sample for every publication and preserves the rollback state', async () => {
    const f = await setup(); await f.activate(); await f.embedQuery('before release')
    const original = structuredClone(f.data.get(PUBLIC_RELEASE_KEY))
    const baselineBudget = structuredClone(f.data.get('public-ai-day-v1'))
    f.env.PUBLICATION_ID = 'publication-two'; f.restart()
    expect((await f.call('/admin/activate', 'POST')).response.status).toBe(409)
    expect((await f.call()).body.fresh_compatibility.checked).toBe(0)
    vi.mocked(f.env.AI.run).mockImplementationOnce(async (_model, input) => ({ data: input.text.map(() => VECTOR.map((x) => -x)) }))
    expect((await f.call('/admin/fresh-compatibility', 'POST')).body.status).toBe('failed')
    expect((await f.call('/admin/activate', 'POST')).response.status).toBe(409)
    await f.call('/admin/deactivate', 'POST')
    expect(f.data.get(PUBLIC_RELEASE_KEY)).toEqual(original)
    expect(f.data.get('public-ai-day-v1')).toEqual(baselineBudget)
    expect(f.data.get('public-fresh-ai-day-v1').texts).toBe(48)
    // Returning to the previous code/environment identity restores its state,
    // without importing a snapshot or refunding either global ledger.
    f.env.PUBLICATION_ID = 'publication-one'; f.restart()
    expect((await f.call()).body.active).toBe(true)
    await f.embedQuery('after recovery')
    expect(f.data.get('public-ai-day-v1').query_texts).toBe(2)
    expect(f.data.get('public-fresh-ai-day-v1').texts).toBe(48)
  })

  it('joins concurrent fresh checks, persists completion and rejects stale activation', async () => {
    vi.useFakeTimers(); const f = await setup(); await f.compatible()
    const before = vi.mocked(f.env.AI.run).mock.calls.length
    const responses = await Promise.all(Array.from({ length: 4 }, () => f.call('/admin/fresh-compatibility', 'POST')))
    expect(responses.every((r) => r.body.checked === 16)).toBe(true)
    expect(f.env.AI.run).toHaveBeenCalledTimes(before + 1)
    await f.call('/admin/fresh-compatibility', 'POST')
    f.restart(); await f.call('/admin/fresh-compatibility', 'POST')
    expect(f.env.AI.run).toHaveBeenCalledTimes(before + 2)
    vi.setSystemTime(Date.now() + 3600001)
    expect((await f.call('/admin/activate', 'POST')).response.status).toBe(409)
  })

  it('retains a charged interrupted fresh batch and keeps reading available', async () => {
    const f = await setup(); await f.compatible()
    const release = f.data.get(PUBLIC_RELEASE_KEY)
    release.fresh.pending = Array.from({ length: 16 }, (_, i) => INDICES[Math.floor(i * 200 / 32)])
    release.fresh.status = 'running'
    f.data.set('public-fresh-ai-day-v1', { day: new Date().toISOString().slice(0, 10), texts: 16, tokens_reserved: 8192 })
    f.restart()
    expect((await f.call()).body.fresh_compatibility).toMatchObject({ status: 'failed', error: 'interrupted_fresh_batch' })
    expect((await f.call('/admin/activate', 'POST')).response.status).toBe(409)
    expect((await f.call('/v1/content?id=' + ID)).body.text).toBe(TEXT)
    expect(f.data.get('public-fresh-ai-day-v1').texts).toBe(16)
  })

  it('atomically limits uncached calls by address across protocols, retaining budgets over restart', async () => {
    vi.useFakeTimers(); vi.setSystemTime(new Date('2026-10-31T12:00:00Z'))
    const f = await setup(); await f.activate()
    for (let i = 0; i < CLIENT_LIMITS.minute; i++) {
      expect((await f.call('/v1/search?q=uncached' + i)).response.status).toBe(200)
    }
    const denied = await f.call('/v1/search?q=one-too-many')
    expect(denied.response.status).toBe(429); expect(denied.response.headers.get('retry-after')).toBe('60')
    expect((await f.call('/v1/search?q=uncached0')).response.status).toBe(200)
    expect((await f.rpc('search_passages', { q: 'new mcp query' })).body.result.isError).toBe(true)
    expect(f.data.get('public-ai-day-v1').query_texts).toBe(20)
    f.restart()
    expect((await f.call('/v1/search?q=still-limited')).response.status).toBe(429)
    const request = f.request('/v1/search?q=another-address')
    request.headers.set('cf-connecting-ip', '192.0.2.7')
    expect((await f.fetch(request)).status).toBe(200)
    expect(JSON.stringify(f.data.get('public-client-day-v1'))).not.toContain('192.0.2.7')
    vi.advanceTimersByTime(60000)
    expect((await f.call('/v1/search?q=next-minute')).response.status).toBe(200)
    expect((await f.call('/v1/catalog')).response.status).toBe(200)
  })

  it('reserves the per-client daily ceiling before AI and resets it only at UTC midnight', async () => {
    vi.useFakeTimers(); vi.setSystemTime(new Date('2026-10-31T12:00:00Z'))
    const f = await setup(); await f.activate()
    for (let i = 0; i < CLIENT_LIMITS.daily; i++) {
      if (i % CLIENT_LIMITS.minute === 0) vi.advanceTimersByTime(60000)
      await f.embedQuery('unique ' + i)
    }
    await expect(f.embedQuery('denied')).rejects.toMatchObject({ code: 'client_daily_budget_exhausted' })
    expect(f.data.get('public-ai-day-v1').query_texts).toBe(200)
    vi.setSystemTime(new Date('2026-11-01T00:00:00Z'))
    await f.embedQuery('new day')
    expect(f.data.get('public-ai-day-v1').query_texts).toBe(1)
  })

  it('requires the private Preview token and rejects expired candidates before DO access', async () => {
    const f = await setup(), gateway = createPublicGateway()
    f.env.PUBLIC_PREVIEW = 'true'; f.env.PUBLIC_PREVIEW_EXPIRES_AT = new Date(Date.now() + 60000).toISOString()
    expect((await gateway.fetch(f.request('/v1/catalog'), f.env)).status).toBe(403)
    const request = f.request('/v1/catalog'); request.headers.set('x-preview-token', TOKEN)
    expect((await gateway.fetch(request, f.env)).status).toBe(200)
    vi.mocked(f.forwarded).mockClear()
    f.env.PUBLIC_PREVIEW_EXPIRES_AT = '2000-01-01T00:00:00Z'
    expect((await gateway.fetch(request, f.env)).status).toBe(503)
    expect(f.forwarded).not.toHaveBeenCalled()
  })
})
