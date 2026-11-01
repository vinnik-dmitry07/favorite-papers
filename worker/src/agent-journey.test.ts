import { createHash } from 'node:crypto'
import { describe, expect, it, vi } from 'vitest'
import { createJourneyAdapter, parseSessions, readQueryBank, type JourneyRecord } from '../probe-kernel/agent-journey'
import { embed, pointLength } from './tokenize'

const session = { id: 'agent-one', question_id: 'question-1', question: 'What does the paper show?', vector_row: 0 }
const base = 'http://127.0.0.1/session/agent-one'
const exactSearch = () => new Request(base + '/v1/search?' + new URLSearchParams({ q: session.question }))
const api = (path: string) => new Request(base + path)
const reply = (body: unknown) => new Response(JSON.stringify(body), { headers: { 'content-type': 'application/json' } })
function fixture(body: unknown = { hits: [] }, limits = { calls: 8, code_points: 48000 }) {
  const records: JourneyRecord[] = []
  const forward = vi.fn(async () => reply(body))
  const adapter = createJourneyAdapter({ sessions: [session], limits, forward,
    record: (_session, row) => records.push(row) })
  return { ...adapter, forward, records }
}

describe('local agent journey budgets and query boundary', () => {
  it('allows setup without charge, forwards an exact first query with default k=8, then rejects any semantic repeat', async () => {
    const adapter = fixture()
    const setup = await adapter.fetch(api('/setup'))
    expect((await setup.json()).usage.attempted_calls).toBe(0)
    expect(setup.headers.get('x-journey-delivered-code-points')).toBe('0')
    expect((await adapter.fetch(exactSearch())).status).toBe(200)
    const sent = adapter.forward.mock.calls[0][0] as Request
    expect(new URL(sent.url).searchParams.get('q')).toBe(session.question)
    expect(new URL(sent.url).searchParams.get('k')).toBe('8')
    expect(await (await adapter.fetch(exactSearch())).json()).toEqual({ error: { code: 'semantic_call_already_used' } })
    expect(adapter.forward).toHaveBeenCalledTimes(1)
    expect((await adapter.fetch(api('/v1/catalog?q=another+literal+title'))).status).toBe(200)
  })

  it('rejects altered questions, vector injection, unknown fields and duplicate parameters before runtime', async () => {
    for (const query of [new URLSearchParams({ q: session.question + ' ' }),
      new URLSearchParams({ q: session.question, vector: '[1]' }),
      new URLSearchParams([['q', session.question], ['q', session.question]])]) {
      const adapter = fixture()
      expect((await adapter.fetch(api('/v1/search?' + query))).status).toBe(400)
      expect(adapter.forward).not.toHaveBeenCalled()
    }
    const adapter = fixture()
    expect((await adapter.fetch(api('/v1/content?id=anything'))).status).toBe(400)
    expect(adapter.forward).not.toHaveBeenCalled()
  })

  it('counts every complete serialized body including repeated Unicode snippets and rejects overflow intact', async () => {
    const body = { snippet: '📚 café', repeated: '📚 café' }
    const wire = JSON.stringify(body)
    const chars = pointLength(wire)
    const adapter = fixture(body, { calls: 8, code_points: chars * 2 + 37 })
    const first = await adapter.fetch(exactSearch())
    expect(await first.text()).toBe(wire)
    expect(first.headers.get('x-journey-delivered-code-points')).toBe(String(chars))
    expect(first.headers.get('x-journey-delivered-bytes')).toBe(String(Buffer.byteLength(wire)))
    const second = await adapter.fetch(api('/v1/paper?id=a'))
    expect(await second.text()).toBe(wire)
    expect(second.headers.get('x-journey-delivered-code-points')).toBe(String(chars * 2))
    const exhausted = await adapter.fetch(api('/v1/paper?id=a'))
    expect(exhausted.status).toBe(429)
    expect(await exhausted.json()).toEqual({ error: { code: 'budget_exhausted' } })
    expect(Number(exhausted.headers.get('x-journey-delivered-code-points'))).toBeLessThanOrEqual(chars * 2 + 37)
    const after = await adapter.fetch(api('/v1/paper?id=a'))
    expect(after.headers.get('x-journey-error')).toBe('budget_exhausted')
    expect(await after.text()).toBe('')
    expect(adapter.records.filter((row) => row.event === 'response').at(-2)?.upstream_suppressed_for_budget).toBe(true)
  })

  it('counts failed attempts and serializes concurrent calls to preserve the 8 call cap', async () => {
    const adapter = fixture()
    await adapter.fetch(exactSearch())
    const responses = await Promise.all(Array.from({ length: 9 }, () => adapter.fetch(api('/v1/paper?id=a'))))
    expect(responses.map((response) => response.status)).toEqual([200, 200, 200, 200, 200, 200, 200, 429, 429])
    expect(adapter.forward).toHaveBeenCalledTimes(8)
    expect(responses.at(-1)!.headers.get('x-journey-attempted-calls')).toBe('10')
    expect(adapter.records.filter((row) => row.event === 'request')).toHaveLength(10)
    expect(adapter.records.filter((row) => row.event === 'response')).toHaveLength(10)
  })

  it('supports only ordinary basic MCP search/fetch and counts duplicate wire text', async () => {
    const adapter = fixture({ result: { structuredContent: { text: 'a' }, content: [{ text: 'a' }] } })
    const rpc = (name: string, args: unknown) => new Request(base + '/mcp', { method: 'POST',
      body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name, arguments: args } }) })
    const search = await adapter.fetch(rpc('search', { query: session.question }))
    expect(search.status).toBe(200)
    const wire = await search.text()
    expect(search.headers.get('x-journey-delivered-code-points')).toBe(String(pointLength(wire)))
    expect((await adapter.fetch(rpc('fetch', { id: 'doc:copied', gold: true }))).status).toBe(400)
    expect((await adapter.fetch(rpc('fetch', { id: 'doc:copied' }))).status).toBe(200)
    expect((await adapter.fetch(rpc('search', { query: session.question }))).status).toBe(400)
    expect((await adapter.fetch(rpc('list_files', {}))).status).toBe(400)
  })

  it('exposes neither registry, files, nor vector rows through the API', async () => {
    const adapter = fixture()
    const setup = await (await adapter.fetch(api('/setup'))).text()
    expect(setup).not.toContain('vector_row')
    for (const path of ['/sessions', '/query-vectors', '/session/other/setup', '/session/agent-one/files']) {
      expect((await adapter.fetch(new Request('http://127.0.0.1' + path))).status).toBe(404)
    }
    expect((await adapter.fetch(new Request('http://example.com/session/agent-one/setup'))).status).toBe(403)
  })
})

describe('saved query registration integrity', () => {
  it('rejects missing vector rows, unknown/secret fields and duplicate sessions', () => {
    expect(parseSessions({ sessions: [session] }, 1)).toEqual([session])
    for (const value of [{ ...session, vector_row: undefined }, { ...session, vector_row: 1 },
      { ...session, gold: 'secret expected answer' }, { ...session, expected_paper_id: 'secret' }]) {
      expect(() => parseSessions([value], 1)).toThrow()
    }
    expect(() => parseSessions({ sessions: [session], gold: {} }, 1)).toThrow()
    expect(() => parseSessions([session, session], 1)).toThrow()
  })

  it('checks saved vector identity, dimensions, finite values and exact query template', () => {
    const bytes = Buffer.alloc(768 * 4)
    bytes.writeFloatLE(1, 0)
    const digest = (data: Buffer) => createHash('sha256').update(data).digest('hex')
    const metadata = { dtype: 'float32', byte_order: 'little', count: 1, dimensions: 768,
      query_template: embed.query_template, encoder: { embedding_signature: 'pinned' }, vectors_sha256: digest(bytes) }
    const manifest = { embedding_signature: 'pinned' }
    const bank = readQueryBank(bytes, metadata, manifest)
    expect(bank.vector(0)[0]).toBe(1)
    expect(() => bank.vector(1)).toThrow('Missing saved query vector')
    expect(() => readQueryBank(bytes, { ...metadata, query_template: 'different instruction' }, manifest)).toThrow('template')
    expect(() => readQueryBank(bytes, { ...metadata, vectors_sha256: 'wrong' }, manifest)).toThrow('checksum')
    expect(() => readQueryBank(bytes, metadata, { embedding_signature: 'other' })).toThrow('signature')
    const invalid = Buffer.from(bytes)
    invalid.writeFloatLE(NaN, 0)
    expect(() => readQueryBank(invalid, { ...metadata, vectors_sha256: digest(invalid) }, manifest).vector(0)).toThrow('Invalid saved query vector')
  })
})
