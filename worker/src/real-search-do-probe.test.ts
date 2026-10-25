import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import { AI_LIMITS, AI_TIMEOUT_MS, createRealProbeGateway, REAL_PROBE_OBJECT_NAME,
  StaticSearchProbe, type RealProbeEnv } from './real-search-do-probe'
import type { createStaticCorpusStore } from './static-corpus-store'

const TOKEN = 'only-for-tests-not-a-real-secret-with-32-characters'
const HASH = 'a'.repeat(64)
const VECTOR = [1, ...Array(767).fill(0)]
const clone = <T>(value: T): T => structuredClone(value)

function setup() {
  const data = new Map<string, unknown>()
  const get = async <T>(key: string) => clone(data.get(key)) as T | undefined
  const put = async (key: string, value: unknown) => { data.set(key, clone(value)) }
  let previous: Promise<unknown> = Promise.resolve()
  const storage = {
    get, put,
    transaction: <T>(work: (transaction: { get: typeof get, put: typeof put }) => Promise<T>) => {
      const result = previous.then(() => work({ get, put }))
      previous = result.catch(() => {})
      return result
    },
  }
  const state = { storage, id: { toString: () => 'object-real' } } as unknown as DurableObjectState
  const forwarded: Request[] = []
  const fetch = vi.fn(async (request: Request) => { forwarded.push(request); return new Response('forwarded') })
  const env = {
    PROBE_TOKEN: TOKEN,
    PROBE_EXPIRES_AT: new Date(Date.now() + 60000).toISOString(),
    PROBE_MANIFEST_SHA: HASH,
    ASSETS: { fetch: vi.fn(async () => new Response(null, { status: 404 })) },
    AI: { run: vi.fn(async (_model: string, input: { text: string[] }) => ({ data: input.text.map(() => [...VECTOR]) })) },
    SEARCH_PROBE: {
      idFromName: vi.fn(() => ({ toString: () => 'object-real' })),
      get: vi.fn(() => ({ fetch })),
    },
  } as unknown as RealProbeEnv
  let queryEmbedder: ((text: string) => Promise<number[]>) | undefined
  const loadCorpus = vi.fn(async (_assets, hash, embedder) => {
    expect(hash).toBe(HASH)
    queryEmbedder = embedder
    return {
      manifest: {
        release_id: 'b'.repeat(64), source_sha: 'c'.repeat(40), passage_count: 300,
        paper_ids: ['arxiv:2402.03300'], sample_paper_id: 'arxiv:2402.03300',
        compatibility_indices: Array.from({ length: 200 }, (_, i) => i),
        queries: [{ id: 'grpo', query: 'How does GRPO work?', expected_paper_id: 'arxiv:2402.03300' }],
      },
      store: { now: () => Date.now(), getJson: async () => null,
        embed: embedder, query: async () => [], rateLimit: async () => true },
      referencePassage: (index: number) => ({ input: `Canonical passage ${index}`, vector: [...VECTOR], row: { index } }),
    }
  }) as unknown as typeof createStaticCorpusStore
  const object = new StaticSearchProbe(state, env, { loadCorpus })
  const request = (path = '/probe/info', method = 'GET', token: string | null = TOKEN) => new Request(
    'https://test.workers.dev' + path, {
      method, headers: { ...(token ? { 'x-probe-token': token } : {}),
        'x-probe-marker': 'marker-1', 'x-probe-run-id': 'run-1' },
    },
  )
  const call = async (path = '/probe/info', method = 'GET') => {
    const response = await object.fetch(request(path, method))
    return { response, body: await response.json() as Record<string, any> }
  }
  return { data, state, env, object, request, call, loadCorpus, forwarded,
    embedQuery: (text: string) => queryEmbedder!(text) }
}

beforeEach(() => {
  vi.spyOn(console, 'log').mockImplementation(() => {})
  vi.spyOn(console, 'error').mockImplementation(() => {})
})
afterEach(() => { vi.restoreAllMocks(); vi.useRealTimers() })

async function passCompatibility(test: ReturnType<typeof setup>) {
  for (let index = 0; index < 13; index++) {
    const result = await test.call('/probe/compatibility', 'POST')
    expect(result.response.status).toBe(200)
    expect(result.body.checked).toBe(Math.min((index + 1) * 16, 200))
    expect(result.body.status).toBe(index === 12 ? 'passed' : 'running')
  }
}

describe('real-subset gateway', () => {
  it('rejects authorization and expiration before selecting an object or loading a corpus', async () => {
    const test = setup()
    const gateway = createRealProbeGateway()
    expect((await gateway.fetch(test.request('/', 'GET', null), test.env)).status).toBe(403)
    expect((await gateway.fetch(test.request('/', 'GET', 'wrong'), test.env)).status).toBe(403)
    expect((await gateway.fetch(test.request(), { ...test.env, PROBE_EXPIRES_AT: '' })).status).toBe(503)
    expect(test.env.SEARCH_PROBE.get).not.toHaveBeenCalled()
    expect(test.loadCorpus).not.toHaveBeenCalled()
    expect(test.env.ASSETS.fetch).not.toHaveBeenCalled()
    expect(test.env.AI.run).not.toHaveBeenCalled()
  })

  it('uses one fixed object, forwards the body unchanged and strips the secret', async () => {
    const test = setup()
    const gateway = createRealProbeGateway()
    const body = '{"jsonrpc":"2.0","method":"tools/list","id":1}'
    const request = new Request(test.request('/mcp?object=user-controlled', 'POST'), { body })
    expect((await gateway.fetch(request, test.env)).status).toBe(200)
    expect(test.env.SEARCH_PROBE.idFromName).toHaveBeenCalledWith(REAL_PROBE_OBJECT_NAME)
    expect(test.forwarded[0].headers.has('x-probe-token')).toBe(false)
    expect(await test.forwarded[0].text()).toBe(body)
    expect(JSON.stringify(vi.mocked(console.log).mock.calls)).not.toContain(TOKEN)
    expect(test.env.AI.run).not.toHaveBeenCalled()
    expect(test.loadCorpus).not.toHaveBeenCalled()
  })

  it('rejects oversized markers without namespace access', async () => {
    const test = setup()
    const request = test.request()
    request.headers.set('x-probe-marker', 'x'.repeat(129))
    expect((await createRealProbeGateway().fetch(request, test.env)).status).toBe(400)
    expect(test.env.SEARCH_PROBE.get).not.toHaveBeenCalled()
  })
})

describe('durable real-subset validation and AI budget', () => {
  it('labels the subset explicitly and blocks query embeddings before compatibility', async () => {
    const test = setup()
    const { response, body } = await test.call()
    expect(body).toMatchObject({ probe_type: 'real-subset', synthetic: false, scope: 'subset',
      passage_count: 300, manifest_sha256: HASH, compatibility: { status: 'not_started', expected: 200 } })
    expect(response.headers.get('x-probe-synthetic')).toBe('false')
    expect(response.headers.get('x-probe-object-id')).toBe('object-real')
    expect(response.headers.get('x-probe-cold-kind')).toBe('object-constructor')
    await expect(test.embedQuery('an uncached question')).rejects.toMatchObject({ code: 'embedding_compatibility_unverified' })
    expect(test.env.AI.run).not.toHaveBeenCalled()
    expect((await test.call()).response.headers.get('x-probe-cold-kind')).toBe('warm')
  })

  it('reports health and semantic search closed until compatibility, without implying production readiness', async () => {
    const test = setup()
    const pending = await test.call('/health')
    expect(pending.response.status).toBe(503)
    expect(pending.body).toMatchObject({ status: 'degraded', search_enabled: false,
      scope: 'subset', compatibility_gate: 'not_started', production_readiness: 'unverified' })
    const search = await test.call('/v1/search?q=question')
    expect(search.response.status).toBe(503)
    expect(search.body.error.code).toBe('embedding_compatibility_unverified')
    await passCompatibility(test)
    const ready = await test.call('/health')
    expect(ready.response.status).toBe(200)
    expect(ready.body).toMatchObject({ compatibility_gate: 'passed', scope: 'subset', production_readiness: 'unverified' })
  })

  it('reserves before inference and completes exactly 200 canonical comparisons in 13 batches', async () => {
    const test = setup()
    vi.mocked(test.env.AI.run).mockImplementation(async (_model, input) => {
      const ledger = [...test.data.values()][0] as any
      expect(ledger.total_texts).toBeGreaterThanOrEqual(input.text.length)
      expect(ledger.pending).toHaveLength(input.text.length)
      expect(ledger.input_tokens).toBeGreaterThan(0)
      expect(input.pooling).toBe('cls')
      return { data: input.text.map(() => [...VECTOR]) }
    })
    await passCompatibility(test)
    const extra = await test.call('/probe/compatibility', 'POST')
    expect(extra.body.status).toBe('passed')
    expect(extra.body.min_cosine).toBe(1)
    expect(extra.body.budget).toMatchObject({ compatibility_texts: 200, query_texts: 0, total_texts: 200, ai_calls: 13 })
    expect(vi.mocked(test.env.AI.run).mock.calls.map((args) => args[1].text.length)).toEqual([...Array(12).fill(16), 8])
    expect(extra.body.results.map((row: any) => row.index)).toEqual(Array.from({ length: 200 }, (_, i) => i))
  })

  it('shares concurrent compatibility calls without reserving or embedding twice', async () => {
    const test = setup()
    let release!: (value: { data: number[][] }) => void
    vi.mocked(test.env.AI.run).mockImplementation(() => new Promise((resolve) => { release = resolve }))
    const first = test.call('/probe/compatibility', 'POST')
    const second = test.call('/probe/compatibility', 'POST')
    await vi.waitFor(() => expect(test.env.AI.run).toHaveBeenCalledTimes(1))
    release({ data: Array.from({ length: 16 }, () => [...VECTOR]) })
    const replies = await Promise.all([first, second])
    expect(replies.map((reply) => reply.body.checked)).toEqual([16, 16])
    expect(replies.map((reply) => reply.body.budget.total_texts)).toEqual([16, 16])
    expect(test.loadCorpus).toHaveBeenCalledTimes(1)
  })

  it('persists query reservations across object re-creation and enforces 24 uncached query calls', async () => {
    const test = setup()
    await passCompatibility(test)
    const parallel = await Promise.allSettled(Array.from({ length: AI_LIMITS.query_texts + 1 },
      (_, index) => test.embedQuery(`question ${index}`)))
    expect(parallel.filter((result) => result.status === 'fulfilled')).toHaveLength(24)
    expect(parallel.filter((result) => result.status === 'rejected')).toHaveLength(1)
    const restarted = new StaticSearchProbe(test.state, test.env, { loadCorpus: test.loadCorpus })
    await restarted.fetch(test.request())
    await expect(test.embedQuery('one too many')).rejects.toMatchObject({ code: 'probe_ai_budget_exhausted' })
    expect(test.env.AI.run).toHaveBeenCalledTimes(13 + 24)
    const result = await restarted.fetch(test.request('/probe/compatibility'))
    expect(await result.json()).toMatchObject({ status: 'passed', budget: { query_texts: 24, total_texts: 224 } })
  })

  it('resumes after a completed persisted batch without embedding its rows again', async () => {
    const test = setup()
    expect((await test.call('/probe/compatibility', 'POST')).body.checked).toBe(16)
    const restarted = new StaticSearchProbe(test.state, test.env, { loadCorpus: test.loadCorpus })
    const response = await restarted.fetch(test.request('/probe/compatibility', 'POST'))
    expect(await response.json()).toMatchObject({ status: 'running', checked: 32,
      budget: { compatibility_texts: 32, ai_calls: 2 } })
    expect(vi.mocked(test.env.AI.run).mock.calls[1][1].text[0]).toBe('Canonical passage 16')
  })

  it('retains charged counters after an inference error and does not retry a failed batch', async () => {
    const test = setup()
    vi.mocked(test.env.AI.run).mockRejectedValue(new Error('provider failed with private details'))
    const first = await test.call('/probe/compatibility', 'POST')
    expect(first.body).toMatchObject({ status: 'failed', checked: 0, error: 'embedding_request_failed',
      budget: { total_texts: 16, ai_calls: 1 } })
    expect(JSON.stringify(first.body)).not.toContain('private details')
    expect((await test.call('/probe/compatibility', 'POST')).body.status).toBe('failed')
    expect(test.env.AI.run).toHaveBeenCalledTimes(1)
    await expect(test.embedQuery('query')).rejects.toMatchObject({ code: 'embedding_compatibility_unverified' })
  })

  it('does not declare compatibility when one local/remote vector disagrees', async () => {
    const test = setup()
    vi.mocked(test.env.AI.run).mockImplementation(async (_model, input) => ({ data: input.text.map((_text, index) =>
      index === 5 ? [0, 1, ...Array(766).fill(0)] : [...VECTOR]) }))
    const result = await test.call('/probe/compatibility', 'POST')
    expect(result.body).toMatchObject({ status: 'failed', checked: 16, min_cosine: 0,
      error: 'embedding_cosine_below_threshold' })
    await expect(test.embedQuery('query')).rejects.toMatchObject({ code: 'embedding_compatibility_unverified' })
  })

  it.each([
    { data: [[1, 2]] },
    { data: Array.from({ length: 16 }, () => Array(768).fill(0)) },
    { data: Array.from({ length: 16 }, () => [Number.NaN, ...Array(767).fill(0)]) },
  ])('rejects malformed or zero-norm AI vectors without claiming a match', async (value) => {
    const test = setup()
    vi.mocked(test.env.AI.run).mockResolvedValue(value)
    const result = await test.call('/probe/compatibility', 'POST')
    expect(result.body).toMatchObject({ status: 'failed', checked: 0, error: 'embedding_response_invalid' })
    expect(result.body.budget.total_texts).toBe(16)
  })

  it('treats an interrupted reserved batch as incomplete after a restart and never refunds it', async () => {
    const test = setup()
    await test.call()
    const [key, value] = [...test.data.entries()][0] as [string, any]
    value.compatibility.status = 'running'
    value.pending = Array.from({ length: 16 }, (_, i) => i)
    Object.assign(value, { compatibility_texts: 16, total_texts: 16, input_tokens: 100, ai_calls: 1 })
    test.data.set(key, value)
    const restarted = new StaticSearchProbe(test.state, test.env, { loadCorpus: test.loadCorpus })
    const response = await restarted.fetch(test.request('/probe/compatibility', 'POST'))
    expect(await response.json()).toMatchObject({ status: 'failed', error: 'interrupted_compatibility_batch',
      budget: { total_texts: 16, ai_calls: 1 } })
    expect(test.env.AI.run).not.toHaveBeenCalled()
  })

  it('rejects persisted state from another manifest and incomplete forged passed state', async () => {
    for (const change of [
      (value: any) => { value.manifest_sha256 = 'd'.repeat(64) },
      (value: any) => { value.compatibility.status = 'passed' },
    ]) {
      const test = setup()
      await test.call()
      const [key, value] = [...test.data.entries()][0] as [string, any]
      change(value)
      test.data.set(key, value)
      const restarted = new StaticSearchProbe(test.state, test.env, { loadCorpus: test.loadCorpus })
      const response = await restarted.fetch(test.request())
      expect(response.status).toBe(503)
      expect(test.env.AI.run).not.toHaveBeenCalled()
    }
  })

  it('requires a pinned manifest and refuses expired object requests before reading assets', async () => {
    for (const env of [{ PROBE_MANIFEST_SHA: '' }, { PROBE_EXPIRES_AT: '2000-01-01' }]) {
      const test = setup()
      const object = new StaticSearchProbe(test.state, { ...test.env, ...env }, { loadCorpus: test.loadCorpus })
      expect((await object.fetch(test.request())).status).toBe(503)
      expect(test.loadCorpus).not.toHaveBeenCalled()
    }
  })

  it('times out a stuck AI batch while preserving its reservation and terminal status', async () => {
    vi.useFakeTimers()
    const test = setup()
    vi.mocked(test.env.AI.run).mockImplementation(() => new Promise(() => {}))
    const work = test.call('/probe/compatibility', 'POST')
    await vi.advanceTimersByTimeAsync(AI_TIMEOUT_MS + 1)
    const result = await work
    expect(result.body).toMatchObject({ status: 'failed', error: 'embedding_timeout',
      budget: { compatibility_texts: 16, ai_calls: 1 } })
    expect(test.env.AI.run).toHaveBeenCalledTimes(1)
  })
})
