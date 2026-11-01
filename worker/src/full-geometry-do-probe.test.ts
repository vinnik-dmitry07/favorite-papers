import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { fullCorpusFixture } from '../test-fixtures/full-corpus'
import { createGeometryGateway, GEOMETRY_OBJECT_NAME, GEOMETRY_REQUEST_CAP,
  StaticSearchProbe, type GeometryProbeEnv } from './full-geometry-do-probe'

const TOKEN = 'geometry-test-secret-at-least-32-characters'
async function setup() {
  const fixture = await fullCorpusFixture()
  const forwarded: Request[] = []
  const env: GeometryProbeEnv = {
    ASSETS: fixture.assets, PROBE_MANIFEST_SHA: fixture.manifestSha,
    PROBE_TOKEN: TOKEN, PROBE_EXPIRES_AT: new Date(Date.now() + 60000).toISOString(),
    SEARCH_PROBE: { idFromName: vi.fn(() => 'object-geometry'), get: vi.fn(() => ({
      fetch: async (request: Request) => { forwarded.push(request); return new Response('forwarded') },
    })) } as unknown as GeometryProbeEnv['SEARCH_PROBE'],
  }
  const state = { id: { toString: () => 'object-geometry' } } as DurableObjectState
  const object = new StaticSearchProbe(state, env)
  const request = (path = '/v1/catalog', headers: Record<string, string> = {}) => new Request(
    'https://test.workers.dev' + path, { headers: { 'x-probe-token': TOKEN,
      'x-probe-marker': 'marker-1', 'x-probe-run-id': 'run-1', ...headers } })
  return { fixture, env, object, forwarded, request }
}
beforeEach(() => {
  vi.spyOn(console, 'log').mockImplementation(() => {})
  vi.spyOn(console, 'error').mockImplementation(() => {})
})
afterEach(() => vi.restoreAllMocks())

describe('full geometry diagnostic', () => {
  it('rejects unauthorized, expired and malformed-marker calls before object selection', async () => {
    const t = await setup(), gateway = createGeometryGateway()
    expect((await gateway.fetch(t.request('/', { 'x-probe-token': 'wrong' }), t.env)).status).toBe(403)
    expect((await gateway.fetch(t.request(), { ...t.env, PROBE_EXPIRES_AT: '' })).status).toBe(503)
    expect((await gateway.fetch(t.request('/', { 'x-probe-marker': 'bad marker' }), t.env)).status).toBe(400)
    expect(t.env.SEARCH_PROBE.get).not.toHaveBeenCalled()
    expect(t.fixture.reads.size).toBe(0)
  })

  it('uses a fixed object and strips the ingress token without reading the body', async () => {
    const t = await setup(), gateway = createGeometryGateway()
    const request = new Request(t.request('/mcp'), { method: 'POST', body: '{"query":"test"}' })
    await gateway.fetch(request, t.env)
    expect(t.env.SEARCH_PROBE.idFromName).toHaveBeenCalledWith(GEOMETRY_OBJECT_NAME)
    expect(t.forwarded[0].headers.has('x-probe-token')).toBe(false)
    expect(await t.forwarded[0].text()).toBe('{"query":"test"}')
    expect(t.fixture.reads.size).toBe(0)
  })

  it('shares cold initialization and reports exact pinned identity without a memory PASS', async () => {
    const t = await setup()
    const replies = await Promise.all(Array.from({ length: 16 }, () => t.object.fetch(t.request())))
    expect(replies.every(r => [200, 503].includes(r.status))).toBe(true)
    expect(replies.filter(r => r.headers.get('x-probe-first-request') === 'true')).toHaveLength(1)
    expect(new Set(replies.map(r => r.headers.get('x-probe-boot-id'))).size).toBe(1)
    for (const response of replies) {
      expect(response.headers.get('x-probe-synthetic')).toBe('true')
      expect(response.headers.get('x-probe-manifest-sha256')).toBe(t.fixture.manifestSha)
      expect(response.headers.get('x-probe-object-id')).toBe('object-geometry')
    }
    expect(t.fixture.reads.get('probe.json')).toBe(1)
    const status = await (await t.object.fetch(t.request('/_probe/status'))).json() as any
    expect(status.passages).toBe(60)
    expect(status.papers).toBe(21)
    expect(status.memory.status).toBe('unverified')
    expect(status.quality.status).toBe('not_measured')
    expect(status.admission.max_active).toBeLessThanOrEqual(4)
    expect(status.admission.max_queued).toBeLessThanOrEqual(8)
  })

  it('prepares once, rejects arbitrary queries, and serves cached synthetic searches', async () => {
    const t = await setup()
    const search = (text: string) => t.request('/v1/search?q=' + encodeURIComponent(text))
    expect((await t.object.fetch(search('memory workload query 0'))).status).toBe(400)
    const prepared = await Promise.all([t.object.fetch(t.request('/_probe/prepare')),
      t.object.fetch(t.request('/_probe/prepare'))])
    expect(prepared.every(r => r.status === 200)).toBe(true)
    expect((await t.object.fetch(search('an arbitrary semantic question'))).status).toBe(400)
    expect((await t.object.fetch(search('memory workload query 160'))).status).toBe(400)
    expect((await t.object.fetch(search('memory workload query 0'))).status).toBe(200)
    expect((await t.object.fetch(search('memory workload query 0'))).status).toBe(200)
    const status = await (await t.object.fetch(t.request('/_probe/status'))).json() as any
    expect(status.prepared_queries).toBe(16)
    expect(status.embedded_queries).toBe(1)
  })

  it('expires inside the object and caps attempts without loading assets', async () => {
    const t = await setup()
    t.env.PROBE_EXPIRES_AT = '2000-01-01T00:00:00Z'
    expect((await t.object.fetch(t.request())).status).toBe(503)
    t.env.PROBE_EXPIRES_AT = new Date(Date.now() + 60000).toISOString()
    for (let i = 1; i < GEOMETRY_REQUEST_CAP; i++) {
      expect((await t.object.fetch(t.request('/_probe/unknown'))).status).toBe(404)
    }
    expect((await t.object.fetch(t.request('/_probe/status'))).status).toBe(429)
    expect(t.fixture.reads.size).toBe(0)
  })
})
