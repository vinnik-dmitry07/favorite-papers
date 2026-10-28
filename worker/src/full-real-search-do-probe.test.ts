import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import type { createFullCorpusStoreLoader } from './full-corpus-store'
import { PROBE_REQUEST_LIMITS } from './probe-admission'
import { AI_LIMITS, createRealProbeGateway, FULL_REAL_MANIFEST_SHA, FULL_REAL_PASSAGES,
  FULL_REAL_PROBE_OBJECT_NAME, StaticSearchProbe, type RealProbeEnv } from './real-search-do-probe'

const VECTOR = [1, ...Array(767).fill(0)]
const INDICES = Array.from({ length: 200 }, (_, index) => 40574 - index * 173)
const TOKEN = 'full-probe-test-token-with-at-least-32-characters'

function setup(overrides: Record<string, unknown> = {}) {
  const data = new Map<string, unknown>()
  const get = async <T>(key: string) => structuredClone(data.get(key)) as T | undefined
  const put = async (key: string, value: unknown) => { data.set(key, structuredClone(value)) }
  let previous: Promise<unknown> = Promise.resolve()
  const storage = { get, put,
    transaction: <T>(work: (transaction: { get: typeof get, put: typeof put }) => Promise<T>) => {
      const result = previous.then(() => work({ get, put }))
      previous = result.catch(() => {})
      return result
    } }
  const state = { storage, id: { toString: () => 'full-object' } } as unknown as DurableObjectState
  const env = {
    PROBE_CORPUS_MODE: 'full', PROBE_MANIFEST_SHA: FULL_REAL_MANIFEST_SHA,
    PROBE_TOKEN: TOKEN, PROBE_EXPIRES_AT: new Date(Date.now() + 60000).toISOString(),
    ASSETS: { fetch: vi.fn(async () => new Response(null, { status: 404 })) },
    AI: { run: vi.fn(async (_model: string, input: { text: string[] }) => ({ data: input.text.map(() => [...VECTOR]) })) },
    SEARCH_PROBE: { idFromName: vi.fn(() => 'full-object'),
      get: vi.fn(() => ({ fetch: vi.fn(async () => new Response('forwarded')) })) },
  } as unknown as RealProbeEnv
  let embedQuery!: (text: string) => Promise<number[]>
  const referencePassage = vi.fn(async (ordinal: number) => {
    // Asynchronous, non-contiguous packed indices deliberately differ from sample ordinals.
    await Promise.resolve()
    if (ordinal < 0 || ordinal >= 200) throw new Error('invalid sample ordinal')
    return { input: `full sample ${ordinal} packed ${INDICES[ordinal]}`, vector: [...VECTOR] }
  })
  const fullLoader = vi.fn((_assets, _hash, embedder) => {
    embedQuery = embedder
    const bundle = Promise.resolve({
      manifest: { kind: 'full-corpus-int8', synthetic: false, passage_count: FULL_REAL_PASSAGES,
        release_id: 'b'.repeat(64), paper_ids: ['arxiv:2402.03300'],
        source_manifest_sha256: 'c'.repeat(64), compatibility: { indices: INDICES }, ...overrides },
      store: { now: () => Date.now(), getJson: async () => null,
        embed: embedder, query: async () => [], rateLimit: async () => true },
      referencePassage,
    })
    return () => bundle
  }) as unknown as typeof createFullCorpusStoreLoader
  const loadCorpus = vi.fn(() => { throw new Error('subset fallback must never run') })
  const make = () => new StaticSearchProbe(state, env, { fullLoader, loadCorpus })
  let object = make()
  const request = (path = '/probe/info', method = 'GET', body?: string) => new Request(
    'https://test.workers.dev' + path, { method, body, headers: { 'x-probe-token': TOKEN } },
  )
  const call = async (path = '/probe/info', method = 'GET', body?: string) => {
    const response = await object.fetch(request(path, method, body))
    return { response, body: await response.json() as Record<string, any> }
  }
  return { data, env, call, request, fullLoader, loadCorpus, referencePassage,
    restart: () => { object = make() }, embedQuery: (text: string) => embedQuery(text) }
}

beforeEach(() => {
  vi.spyOn(console, 'log').mockImplementation(() => {})
  vi.spyOn(console, 'error').mockImplementation(() => {})
})
afterEach(() => vi.restoreAllMocks())

async function compatible(test: ReturnType<typeof setup>) {
  for (let i = 0; i < 13; i++) expect((await test.call('/probe/compatibility', 'POST')).response.status).toBe(200)
}

describe('retained genuine full corpus with the existing durable AI ledger', () => {
  it('loads one genuine corpus for read-only readiness without inference and keeps search gated', async () => {
    const test = setup()
    const info = await test.call()
    expect(info.body).toMatchObject({ probe_type: 'real-full-corpus', synthetic: false, scope: 'full',
      passage_count: 40575, manifest_sha256: FULL_REAL_MANIFEST_SHA,
      production_readiness: 'unverified', compatibility: { status: 'not_started', expected: 200 },
      budget: { query_texts: 0, total_texts: 0, limits: AI_LIMITS },
      admission: { active_limit: 4, queue_limit: 8 } })
    expect(info.response.headers.get('x-probe-kind')).toBe('real-full-corpus')
    expect((await test.call('/probe/compatibility')).body.status).toBe('not_started')
    expect((await test.call('/health')).body).toMatchObject({ scope: 'full', search_enabled: false })
    expect((await test.call('/v1/search?q=a%20genuine%20new%20query')).body.error.code)
      .toBe('embedding_compatibility_unverified')
    expect(test.fullLoader).toHaveBeenCalledTimes(1)
    expect(test.loadCorpus).not.toHaveBeenCalled()
    expect(test.referencePassage).not.toHaveBeenCalled()
    expect(test.env.AI.run).not.toHaveBeenCalled()
  })

  it('awaits the correct sample ordinals while persisting original packed compatibility indices', async () => {
    const test = setup()
    const first = await test.call('/probe/compatibility', 'POST', '{"query":"do not embed this","index":99}')
    expect(first.body).toMatchObject({ status: 'running', checked: 16,
      budget: { compatibility_texts: 16, query_texts: 0, ai_calls: 1 } })
    expect(first.body.results.map((row: { index: number }) => row.index)).toEqual(INDICES.slice(0, 16))
    test.restart()
    const second = await test.call('/probe/compatibility', 'POST')
    expect(second.body.checked).toBe(32)
    expect(test.referencePassage.mock.calls.map(([ordinal]) => ordinal)).toEqual(Array.from({ length: 32 }, (_, i) => i))
    expect(vi.mocked(test.env.AI.run).mock.calls[1][1]).toEqual({
      text: Array.from({ length: 16 }, (_, i) => `full sample ${i + 16} packed ${INDICES[i + 16]}`), pooling: 'cls',
    })
  })

  it('embeds new text unchanged and preserves all 24 charged query submissions across restart', async () => {
    const test = setup()
    await compatible(test)
    for (let i = 0; i < AI_LIMITS.query_texts; i++) {
      await expect(test.embedQuery(`a completely new full-corpus question ${i}`)).resolves.toEqual(VECTOR)
    }
    expect(vi.mocked(test.env.AI.run).mock.calls.slice(13).map(([, input]) => input.text)).toEqual(
      Array.from({ length: 24 }, (_, i) => [`a completely new full-corpus question ${i}`]),
    )
    test.restart()
    const status = await test.call()
    expect(status.body).toMatchObject({ compatibility: { status: 'passed', checked: 200 },
      budget: { compatibility_texts: 200, query_texts: 24, total_texts: 224, ai_calls: 37 } })
    await expect(test.embedQuery('a 25th query')).rejects.toMatchObject({ code: 'probe_ai_budget_exhausted' })
    expect(test.env.AI.run).toHaveBeenCalledTimes(37)
    expect(test.loadCorpus).not.toHaveBeenCalled()
  })

  it.each([{ synthetic: true }, { kind: 'full-corpus-int8-geometry-fixture' }, { passage_count: 40574 }])(
    'rejects a noncanonical full bundle before ledger initialization or inference: %j', async (override) => {
      const test = setup(override)
      expect((await test.call()).body.error.code).toBe('probe_config_invalid')
      expect(test.data.size).toBe(0)
      expect(test.loadCorpus).not.toHaveBeenCalled()
      expect(test.referencePassage).not.toHaveBeenCalled()
      expect(test.env.AI.run).not.toHaveBeenCalled()
    },
  )

  it('rejects a different pin before loading and never falls back after a genuine loader failure', async () => {
    const wrong = setup()
    wrong.env.PROBE_MANIFEST_SHA = 'a'.repeat(64)
    expect((await wrong.call()).body.error.code).toBe('probe_config_invalid')
    expect(wrong.fullLoader).not.toHaveBeenCalled()
    const failed = setup()
    vi.mocked(failed.fullLoader).mockImplementation(() => () => Promise.reject(new Error('bad asset checksum')))
    expect((await failed.call()).response.status).toBe(503)
    expect((await failed.call()).response.status).toBe(503)
    expect(failed.fullLoader).toHaveBeenCalledTimes(1)
    expect(failed.loadCorpus).not.toHaveBeenCalled()
    expect(failed.env.AI.run).not.toHaveBeenCalled()
  })

  it('rejects an oversized MCP body before initializing the full corpus', async () => {
    const test = setup()
    const rejected = await test.call('/mcp', 'POST', 'x'.repeat(PROBE_REQUEST_LIMITS.request_bytes + 1))
    expect(rejected.response.status).toBe(413)
    expect(test.fullLoader).not.toHaveBeenCalled()
    expect(test.env.AI.run).not.toHaveBeenCalled()
  })

  it('routes every authenticated full query to one fixed object and rejects unauthorized callers first', async () => {
    const test = setup()
    const gateway = createRealProbeGateway()
    const unauthorized = test.request()
    unauthorized.headers.delete('x-probe-token')
    expect((await gateway.fetch(unauthorized, test.env)).status).toBe(403)
    expect(test.env.SEARCH_PROBE.get).not.toHaveBeenCalled()
    expect((await gateway.fetch(test.request('/mcp?object=another'), test.env)).status).toBe(200)
    expect(test.env.SEARCH_PROBE.idFromName).toHaveBeenCalledWith(FULL_REAL_PROBE_OBJECT_NAME)
    expect(test.env.AI.run).not.toHaveBeenCalled()
  })
})
