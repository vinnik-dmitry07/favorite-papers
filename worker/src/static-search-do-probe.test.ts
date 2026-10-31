import { afterEach, describe, expect, it, vi } from 'vitest'

import { createDoProbeGateway, PROBE_OBJECT_NAME, StaticSearchProbe, type DoProbeEnv } from './static-search-do-probe'

const TOKEN = 'test-only-secret-token-with-32-characters'

function setup() {
  const id = { toString: () => 'object-id' } as DurableObjectId
  const forwarded: Request[] = []
  const fetch = vi.fn(async (request: Request) => {
    forwarded.push(request)
    return new Response('forwarded', { headers: { 'x-probe-runtime': 'durable-object' } })
  })
  const env = {
    PROBE_TOKEN: TOKEN,
    PROBE_EXPIRES_AT: new Date(Date.now() + 60000).toISOString(),
    ASSETS: { fetch: vi.fn(async () => new Response(null, { status: 404 })) },
    SEARCH_PROBE: { idFromName: vi.fn(() => id), get: vi.fn(() => ({ fetch })) },
  } as unknown as DoProbeEnv
  const request = (path = '/probe/stage?stage=noop', token: string | null = TOKEN) => new Request(
    'https://test.workers.dev' + path, { headers: {
      ...(token ? { 'x-probe-token': token } : {}), 'x-probe-marker': 'request-1', 'x-probe-run-id': 'run-1',
    } },
  )
  return { env, request, forwarded, fetch }
}

afterEach(() => vi.restoreAllMocks())

describe('Durable Object runtime probe', () => {
  it('fails closed before namespace access for missing, incorrect or expired authorization', async () => {
    const { env, request } = setup()
    const gateway = createDoProbeGateway()
    expect((await gateway.fetch(request('/', null), env)).status).toBe(403)
    expect((await gateway.fetch(request('/', 'wrong'), env)).status).toBe(403)
    expect((await gateway.fetch(request(), { ...env, PROBE_TOKEN: '' })).status).toBe(403)
    expect((await gateway.fetch(request(), { ...env, PROBE_EXPIRES_AT: '' })).status).toBe(503)
    expect((await gateway.fetch(request(), { ...env, PROBE_EXPIRES_AT: '2000-01-01' })).status).toBe(503)
    expect(env.SEARCH_PROBE.idFromName).not.toHaveBeenCalled()
    expect(env.ASSETS.fetch).not.toHaveBeenCalled()
  })

  it('always selects the one server-controlled object and strips the ingress secret', async () => {
    const log = vi.spyOn(console, 'log').mockImplementation(() => {})
    const { env, request, forwarded } = setup()
    const gateway = createDoProbeGateway()
    for (const path of ['/v1/search?q=first&object=bad', '/v1/content?id=other&version=bad', '/probe/info?cold=1']) {
      expect((await gateway.fetch(request(path), env)).status).toBe(200)
    }
    expect(env.SEARCH_PROBE.idFromName).toHaveBeenCalledTimes(3)
    for (const args of vi.mocked(env.SEARCH_PROBE.idFromName).mock.calls) expect(args).toEqual([PROBE_OBJECT_NAME])
    expect(forwarded.every((r) => !r.headers.has('x-probe-token'))).toBe(true)
    expect(forwarded[0].headers.get('x-probe-marker')).toBe('request-1')
    expect(log.mock.calls[0][0]).toMatchObject({ runtime_role: 'gateway', probe_marker: 'request-1', run_id: 'run-1' })
    expect(JSON.stringify(log.mock.calls)).not.toContain(TOKEN)
    expect(env.ASSETS.fetch).not.toHaveBeenCalled()
  })

  it('forwards MCP bodies without parsing and rejects unbounded marker input', async () => {
    vi.spyOn(console, 'log').mockImplementation(() => {})
    const { env, request, forwarded } = setup()
    const gateway = createDoProbeGateway()
    const body = '{"jsonrpc":"2.0","id":1,"method":"initialize"}'
    await gateway.fetch(new Request(request('/mcp'), { method: 'POST', body }), env)
    expect(await forwarded[0].text()).toBe(body)
    const bad = request()
    bad.headers.set('x-probe-marker', 'x'.repeat(129))
    expect((await gateway.fetch(bad, env)).status).toBe(400)
    expect(forwarded).toHaveLength(1)
  })

  it('owns caches per object and fixes the algorithm to wasm-json16', async () => {
    vi.spyOn(console, 'log').mockImplementation(() => {})
    const { env, request } = setup()
    const state = (name: string) => ({ id: { toString: () => name } }) as DurableObjectState
    const left = new StaticSearchProbe(state('left'), env)
    const right = new StaticSearchProbe(state('right'), env)
    const first = await left.fetch(request())
    const warm = await left.fetch(request())
    const reset = await left.fetch(request('/probe/stage?stage=noop&cold=1'))
    const other = await right.fetch(request())
    expect(first.status).toBe(200)
    expect(first.headers.get('x-probe-variant')).toBe('wasm-json16')
    expect(first.headers.get('x-probe-object-first-request')).toBe('true')
    expect(reset.headers.get('x-probe-object-first-request')).toBe('false')
    expect(warm.headers.get('x-probe-cache-id')).toBe(first.headers.get('x-probe-cache-id'))
    expect(reset.headers.get('x-probe-cache-id')).not.toBe(first.headers.get('x-probe-cache-id'))
    expect(other.headers.get('x-probe-boot-id')).not.toBe(first.headers.get('x-probe-boot-id'))
    expect((await left.fetch(request('/probe/stage?stage=noop&variant=js-json128'))).status).toBe(400)
    expect(env.ASSETS.fetch).not.toHaveBeenCalled()
  })
})
