import { afterEach, describe, expect, it, vi } from 'vitest'

import { outputs } from './contracts'
import { handleRest } from './http'
import probe, { createProbeApp, createProbeService, createWorkerProbeGateway, type ProbeEnv } from './static-search-probe'
import { pointLength, WordPieceTokenizer } from './tokenize'

const VERSION = 'probe-v1'
const TOKEN = 'only-for-tests-not-a-real-secret-with-32-characters'
const authHeaders = { 'x-probe-token': TOKEN }
const PART_SIZE = 16000
const A = 'arxiv:a'
const B = 'arxiv:b'
const PREFIX_A = '/probe/papers/' + 'a'.repeat(64)
const PREFIX_B = '/probe/papers/' + 'b'.repeat(64)

type AssetFetcher = ProbeEnv['ASSETS']

class Assets implements AssetFetcher {
  readonly objects = new Map<string, string | ArrayBuffer>()
  readonly reads: string[] = []

  json(path: string, value: unknown): void {
    this.objects.set(path, JSON.stringify(value))
  }

  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url)
    expect(url.origin).toBe('https://assets.local')
    this.reads.push(url.pathname)
    const value = this.objects.get(url.pathname)
    return value === undefined ? new Response(null, { status: 404 })
      : new Response(typeof value === 'string' ? value : value.slice(0))
  }
}

function build(text = '😀'.repeat(15998) + 'Needle' + ' x'.repeat(17000)) {
  const assets = new Assets()
  const common = { corpus_version: VERSION, synthetic: true, offset_unit: 'unicode_code_points' }
  const papers = [
    { id: A, title: 'Paper A', url: 'https://example.test/a', path: PREFIX_A + '/paperinfo.json',
      available: true, total_length: pointLength(text), part_count: Math.ceil(pointLength(text) / PART_SIZE), ...common },
    { id: B, title: 'Paper B', url: null, path: PREFIX_B + '/paperinfo.json',
      available: true, total_length: 14, part_count: 1, ...common },
  ]
  assets.json('/probe/index.json', {
    ...common, format: 'pq-ip-v1', dimensions: 4, subquantizers: 2, centroids: 1, count: 6, seed: 42,
    record_shard_size: 2, text_part_size: PART_SIZE,
    codes: { path: '/probe/codes.bin' }, codebooks: { path: '/probe/codebooks.bin' },
    papers: { path: '/probe/papers.json', count: 2 }, records: { path: '/probe/records/{shard}.json', shards: 3 },
  })
  assets.objects.set('/probe/codes.bin', new ArrayBuffer(12))
  const books = new ArrayBuffer(16)
  const view = new DataView(books)
  for (let i = 0; i < 4; i++) view.setFloat32(i * 4, 1, true)
  assets.objects.set('/probe/codebooks.bin', books)
  assets.json('/probe/papers.json', papers)
  const fulltexts = [text, '# B\nText only.']
  papers.forEach((paper, index) => {
    assets.json(paper.path, { ...paper, sections: [{ title: paper.title, level: 1, offset: 0 }] })
    const points = Array.from(fulltexts[index])
    for (let offset = 0; offset < points.length; offset += PART_SIZE) {
      assets.json(paper.path.replace('paperinfo.json', `parts/${offset / PART_SIZE + 1}.json`), {
        ...common, paper_id: paper.id, offset, total_length: points.length,
        text: points.slice(offset, offset + PART_SIZE).join(''),
      })
    }
  })
  for (let shard = 0; shard < 3; shard++) {
    assets.json(`/probe/records/${shard}.json`, [0, 1].map((position) => {
      const index = shard * 2 + position
      const paper = papers[index === 2 || index === 3 || index === 5 ? 1 : 0]
      return { ...common, index, paper_id: paper.id, title: paper.title, url: paper.url,
        chunk_index: index, start: 0, end: Math.min(800, paper.total_length),
        snippet: paper.id === A ? '😀'.repeat(800) : fulltexts[1] }
    }))
  }
  const env = { ASSETS: assets, PROBE_TOKEN: TOKEN,
    PROBE_EXPIRES_AT: new Date(Date.now() + 60000).toISOString() }
  const service = createProbeService(env)
  return { assets, env, service, text }
}

function queryUrl(path: string, params: Record<string, string | number> = {}): string {
  const url = new URL(path, 'http://localhost')
  for (const [key, value] of Object.entries(params)) url.searchParams.set(key, String(value))
  return url.href
}

async function rpc(env: ProbeEnv, name: string, args: Record<string, unknown>) {
  const response = await probe.fetch(new Request('http://localhost/mcp', {
    method: 'POST', headers: { ...authHeaders, 'content-type': 'application/json',
      accept: 'application/json, text/event-stream', 'mcp-protocol-version': '2025-06-18' },
    body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name, arguments: args } }),
  }), env)
  const text = await response.text()
  const payload = text.includes('data:')
    ? JSON.parse(text.split('\n').filter((line) => line.startsWith('data:')).at(-1)!.slice(5).trim())
    : JSON.parse(text)
  return { response, payload }
}

afterEach(() => vi.restoreAllMocks())

describe('isolated synthetic probe', () => {
  it('rejects unauthorized or expired public Worker requests before cache resets and asset access', async () => {
    const log = vi.spyOn(console, 'log').mockImplementation(() => {})
    const { env, assets } = build()
    const gateway = createWorkerProbeGateway()
    const request = (token: string | null = TOKEN, cold = false) => new Request(
      queryUrl('/probe/info', cold ? { cold: 1 } : {}),
      { headers: token === null ? {} : { 'x-probe-token': token } },
    )
    for (const token of [null, 'wrong', TOKEN.slice(0, -1) + 'x']) {
      expect((await gateway.fetch(request(token, true), env)).status).toBe(403)
    }
    for (const expiry of [undefined, '', '2000-01-01']) {
      expect((await gateway.fetch(request(TOKEN, true), { ...env, PROBE_EXPIRES_AT: expiry })).status).toBe(503)
    }
    expect((await gateway.fetch(request(), { ...env, PROBE_TOKEN: undefined })).status).toBe(403)
    expect(assets.reads).toHaveLength(0)
    expect(log).not.toHaveBeenCalled()
    const first = await gateway.fetch(request(), env)
    expect(first.headers.get('x-probe-first-request')).toBe('true')
    const loaded = assets.reads.length
    expect((await gateway.fetch(request(null, true), env)).status).toBe(403)
    const warm = await gateway.fetch(request(), env)
    expect(warm.headers.get('x-probe-cache')).toBe('warm')
    expect(assets.reads).toHaveLength(loaded)
    expect(JSON.stringify(log.mock.calls)).not.toContain(TOKEN)
  })

  it('keeps service caches per owner and coalesces concurrent initialization', async () => {
    const { assets, env } = build()
    const left = createProbeService(env)
    const right = createProbeService(env)
    await Promise.all(Array.from({ length: 4 }, () => left.search({ q: 'policy', k: 2, ip: 'test' })))
    expect(assets.reads.filter((path) => path === '/probe/codes.bin')).toHaveLength(1)
    await right.search({ q: 'policy', k: 2, ip: 'test' })
    expect(assets.reads.filter((path) => path === '/probe/codes.bin')).toHaveLength(2)
  })

  it('isolates app instances and gives a reset a new cache ID without a new constructor ID', async () => {
    vi.spyOn(console, 'log').mockImplementation(() => {})
    const { env } = build()
    const left = createProbeApp({ runtimeRole: 'durable_object', objectId: 'left' })
    const right = createProbeApp({ runtimeRole: 'durable_object', objectId: 'right' })
    const call = (app: ReturnType<typeof createProbeApp>, cold = false) => app.fetch(
      new Request(queryUrl('/probe/info', cold ? { cold: 1 } : {})), env,
    )
    const first = await call(left)
    const warm = await call(left)
    const reset = await call(left, true)
    const other = await call(right)
    expect(first.headers.get('x-probe-cold-kind')).toBe('object-constructor')
    expect(warm.headers.get('x-probe-cold-kind')).toBe('warm')
    expect(reset.headers.get('x-probe-cold-kind')).toBe('application-cache-reset')
    expect(reset.headers.get('x-probe-boot-id')).toBe(first.headers.get('x-probe-boot-id'))
    expect(warm.headers.get('x-probe-cache-id')).toBe(first.headers.get('x-probe-cache-id'))
    expect(reset.headers.get('x-probe-cache-id')).not.toBe(first.headers.get('x-probe-cache-id'))
    expect(other.headers.get('x-probe-boot-id')).not.toBe(first.headers.get('x-probe-boot-id'))
    expect(other.headers.get('x-probe-object-id')).toBe('right')
  })

  it('preserves tokenizer state across application resets without sharing it between owners', async () => {
    vi.spyOn(console, 'log').mockImplementation(() => {})
    const tokens = vi.spyOn(WordPieceTokenizer.prototype, 'tokenIds')
    const { env } = build()
    const left = createProbeApp()
    const right = createProbeApp()
    const search = (app: ReturnType<typeof createProbeApp>, cold = false) => app.fetch(
      new Request(queryUrl('/v1/search', { q: 'policy', ...(cold ? { cold: 1 } : {}) })), env,
    )
    expect((await search(left)).status).toBe(200)
    expect((await search(left, true)).status).toBe(200)
    expect((await search(right)).status).toBe(200)
    expect(tokens.mock.contexts[0]).toBe(tokens.mock.contexts[1])
    expect(tokens.mock.contexts[0]).not.toBe(tokens.mock.contexts[2])
  })

  it('runs actual REST search with bounded snippets, deduplication and cached binary assets', async () => {
    const { service, assets } = build()
    const response = await handleRest(new Request(queryUrl('/v1/search', { q: 'policy optimization', k: 2 })), service)
    expect(response.status).toBe(200)
    const body = outputs.passages.parse(await response.json())
    expect(body.hits.map((hit) => hit.paper_id)).toEqual([A, B])
    expect(body.hits[0].title).toContain('SYNTHETIC')
    expect(pointLength(body.hits[0].snippet)).toBe(480)
    expect(assets.reads.filter((path) => path.startsWith('/probe/records/'))).toEqual([
      '/probe/records/0.json', '/probe/records/1.json',
    ])
    const before = assets.reads.length
    await service.search({ q: 'another query', k: 2, ip: 'test' })
    expect(assets.reads.length).toBe(before)
    expect(assets.reads.filter((path) => path === '/probe/codes.bin')).toHaveLength(1)
  })

  it('uses real MCP search/fetch schemas and returns complete independently paginated text parts', async () => {
    vi.spyOn(console, 'log').mockImplementation(() => {})
    const { env, text } = build()
    const search = await rpc(env, 'search', { query: 'policy optimization' })
    expect(search.response.status).toBe(200)
    const results = outputs.search.parse(search.payload.result.structuredContent).results
    expect(results[0].title).toContain('SYNTHETIC')
    const fetched = await rpc(env, 'fetch', { id: results[0].id })
    expect(fetched.payload.result.isError).not.toBe(true)
    const first = outputs.fetch.parse(fetched.payload.result.structuredContent)
    expect(pointLength(first.text)).toBe(PART_SIZE)
    expect(first.text).toBe(Array.from(text).slice(0, PART_SIZE).join(''))
    expect(first.metadata.previous_id).toBe(null)
    expect(typeof first.metadata.next_id).toBe('string')
    const next = await rpc(env, 'fetch', { id: first.metadata.next_id })
    const second = outputs.fetch.parse(next.payload.result.structuredContent)
    expect(second.metadata.start).toBe(PART_SIZE)
    expect(second.metadata.previous_id).toBe(first.id)
    expect(second.text).toBe(Array.from(text).slice(PART_SIZE, PART_SIZE * 2).join(''))
  })

  it('avoids duplicate tokenization on MCP search without changing search behavior', async () => {
    const { service } = build()
    const tokenSpy = vi.spyOn(WordPieceTokenizer.prototype, 'tokenIds')

    const result = await service.researchSearch('policy optimization', 'test')
    expect(result.results.length).toBeGreaterThan(0)
    expect(tokenSpy).toHaveBeenCalledTimes(1)

    const direct = await service.search({ q: 'policy optimization', k: 5, ip: 'test' })
    expect(direct.hits.length).toBeGreaterThan(0)
    expect(tokenSpy).toHaveBeenCalledTimes(2)

    tokenSpy.mockClear()
    const exact = await service.researchSearch('Paper A', 'test')
    expect(exact.results[0].title).toContain('Paper A')
    expect(tokenSpy).toHaveBeenCalledTimes(1)
  })

  it('reads at most three static parts for arbitrary 32000-code-point windows', async () => {
    const { service, assets, text } = build()
    const result = outputs.content.parse(await service.content({ id: A, offset: 1, length: 32000, version: VERSION }))
    expect(result.text).toBe(Array.from(text).slice(1, 32001).join(''))
    expect(result.next_offset).toBe(32001)
    expect(assets.reads.filter((path) => path.includes('/parts/'))).toHaveLength(3)
    const before = assets.reads.length
    await service.content({ id: A, offset: 1, length: 32000, version: VERSION })
    expect(assets.reads.length).toBe(before)
  })

  it('serves precomputed contents without fetching text or the PQ index', async () => {
    const { service, assets } = build()
    const result = outputs.contents.parse(await service.contents(A, VERSION))
    expect(result.sections).toEqual([{ title: 'Paper A', level: 1, offset: 0 }])
    expect(assets.reads.some((path) => path.endsWith('.bin') || path.includes('/parts/'))).toBe(false)
  })

  it('finds Unicode-offset matches across boundaries and advances when a window has no matches', async () => {
    const { service, assets } = build()
    const first = outputs.find.parse(await service.find({ id: A, q: 'needle', offset: 0, version: VERSION }))
    expect(first.matches).toHaveLength(1)
    expect(first.matches[0]).toMatchObject({ start: 15998, end: 16004 })
    expect(first.next_offset).toBe(16004)
    expect(assets.reads.filter((path) => path.includes('/parts/'))).toHaveLength(2)
    const second = outputs.find.parse(await service.find({ id: A, q: 'needle', offset: first.next_offset!, version: VERSION }))
    expect(second.matches).toEqual([])
    expect(second.next_offset).toBe(32004)
  })

  it('returns a resumable position when the bounded match count is reached', async () => {
    const { service } = build('needle '.repeat(20))
    const first = await service.find({ id: A, q: 'needle', offset: 0 })
    expect(first.matches).toHaveLength(12)
    expect(first.next_offset).toBe(12 * 7)
    const second = await service.find({ id: A, q: 'needle', offset: first.next_offset! })
    expect(second.matches).toHaveLength(8)
    expect(second.next_offset).toBe(null)
    expect(new Set([...first.matches, ...second.matches].map((row) => row.start)).size).toBe(20)
  })

  it('treats find expressions literally', async () => {
    const { service } = build('abc .* def')
    const result = await service.find({ id: A, q: '.*' })
    expect(result.matches).toMatchObject([{ start: 4, end: 6 }])
  })

  it('guards supplied versions and opaque document versions', async () => {
    const { service } = build()
    await expect(service.content({ id: A, offset: 0, version: 'old' })).rejects.toMatchObject({ status: 409 })
    await expect(service.contents(A, 'old')).rejects.toMatchObject({ status: 409 })
    await expect(service.find({ id: A, q: 'x', version: 'old' })).rejects.toMatchObject({ status: 409 })
    const id = 'probe-doc:' + btoa(JSON.stringify({ paper: A, version: 'old', start: 0 }))
    await expect(service.fetchDocument(id)).rejects.toMatchObject({ status: 409 })
    await expect(service.fetchDocument('probe-doc:' + btoa(JSON.stringify({ paper: A, version: '', start: 0 }))))
      .rejects.toMatchObject({ status: 400 })
  })

  it('marks app-cache resets without pretending to restart the isolate', async () => {
    const log = vi.spyOn(console, 'log').mockImplementation(() => {})
    const { env, assets } = build()
    const call = (cold = false) => probe.fetch(new Request(queryUrl('/probe/info', {
      ...(cold ? { cold: 1 } : {}), probe_run: 'run', probe_case: 'info', probe_seq: 1,
    }), { headers: authHeaders }), env)
    const first = await call(true)
    const second = await call()
    const third = await call(true)
    expect([first, second, third].map((response) => response.headers.get('x-probe-cache'))).toEqual(['cold', 'warm', 'cold'])
    expect(first.headers.get('x-probe-boot-id')).toBe(third.headers.get('x-probe-boot-id'))
    expect(third.headers.get('x-probe-synthetic')).toBe('true')
    expect(assets.reads.filter((path) => path === '/probe/index.json')).toHaveLength(2)
    expect(log).toHaveBeenCalledTimes(3)
    expect(log.mock.calls[0][0]).toMatchObject({ probe_run: 'run', probe_case: 'info', probe_seq: '1' })
    const info = await third.json() as { synthetic: boolean, sample_query_max: string, longest_paper_id: string }
    expect(info.synthetic).toBe(true)
    expect(info.longest_paper_id).toBe(A)
    expect(info.sample_query_max.length).toBe(999)
  })

  it('accepts the near-limit token workload and rejects oversized queries', async () => {
    const { service } = build()
    const info = await service.probeInfo()
    await expect(service.search({ q: info.sample_query_max + ' probe 999 mcp', k: 8, ip: 'test' })).resolves.toBeDefined()
    await expect(service.search({ q: 'a '.repeat(512), k: 8, ip: 'test' })).rejects.toMatchObject({ code: 'query_too_long' })
    await expect(service.search({ q: 'x'.repeat(2001), k: 8, ip: 'test' })).rejects.toMatchObject({ code: 'query_too_long' })
    await expect(service.search({ q: 'hello', k: 9, ip: 'test' })).rejects.toMatchObject({ status: 400 })
  })

  it('fails closed on missing or mixed-version assets', async () => {
    const broken = build()
    broken.assets.objects.delete('/probe/codes.bin')
    const response = await handleRest(new Request(queryUrl('/v1/search', { q: 'query' })), broken.service)
    expect(response.status).toBe(503)
    const mixed = build()
    const path = PREFIX_A + '/parts/1.json'
    const part = JSON.parse(mixed.assets.objects.get(path) as string)
    mixed.assets.json(path, { ...part, corpus_version: 'other' })
    await expect(mixed.service.content({ id: A, offset: 0, version: VERSION })).rejects.toMatchObject({ status: 503 })
  })

  it('returns explicit unsupported errors and refuses malformed or unauthorized requests', async () => {
    vi.spyOn(console, 'log').mockImplementation(() => {})
    const { env, service } = build()
    expect((await handleRest(new Request(queryUrl('/v1/citations', { id: A })), service)).status).toBe(501)
    expect((await probe.fetch(new Request('https://attacker.example/probe/info', { headers: authHeaders }), env)).status).toBe(400)
    expect((await probe.fetch(new Request('http://localhost/mcp', { headers: authHeaders }), env)).status).toBe(405)
    await expect(service.fetchDocument('not-a-document')).rejects.toMatchObject({ status: 400 })
    await expect(service.content({ id: A, offset: Number.MAX_SAFE_INTEGER, version: VERSION }))
      .rejects.toMatchObject({ code: 'invalid_offset' })
  })
})

it('includes catalog candidates in MCP and publishes a stable full-text fetch workload', async () => {
  const { service } = build()
  const result = await service.researchSearch('Paper', 'test')
  const catalog = await service.fetchDocument(result.results[0].id)
  expect(catalog.metadata.item_type).toBe('catalog')
  const info = await service.probeInfo()
  const document = await service.fetchDocument(info.sample_fetch_id)
  expect(document.metadata.item_type).toBe('text_part')
  expect(pointLength(document.text)).toBe(PART_SIZE)
  await expect(service.researchSearch('x'.repeat(2001), 'test')).rejects.toMatchObject({ code: 'query_too_long' })
})

it('logs unexpected failures before REST sanitizes their response', async () => {
  const { assets, service } = build()
  assets.objects.set('/probe/codebooks.bin', new ArrayBuffer(1))
  const log = vi.spyOn(console, 'error').mockImplementation(() => {})
  const response = await handleRest(new Request(queryUrl('/v1/search', { q: 'policy' })), service)
  expect(response.status).toBe(503)
  expect(log).toHaveBeenCalledWith(expect.objectContaining({ operation: 'search', probe_error: expect.stringContaining('RangeError') }))
})
