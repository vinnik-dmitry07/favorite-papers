import { readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { describe, expect, it } from 'vitest'

import type { ActivePointer, CorpusStore, GraphDoc, NodeCard, VectorHit } from './corpus'
import { createApp } from './index'
import { signatures, sha256Hex } from './signatures'
import { createService, type Service } from './service'
import { embed, pointLength, WordPieceTokenizer } from './tokenize'

const vocab = readFileSync(
  resolve(dirname(fileURLToPath(import.meta.url)), '../tokenizer/vocab.txt'),
  'utf8',
)
const tokenizer = new WordPieceTokenizer(vocab)

class Memory implements CorpusStore {
  nowMs = 0
  objects = new Map<string, unknown>()
  embedCalls = 0
  failKeys = new Set<string>()
  limit = 30
  used = new Map<string, number>()
  vectors: VectorHit[] = [{ id: 'vec1', score: 0.42 }]
  clockJumpOnEmbed = 0

  now(): number {
    return this.nowMs
  }

  async getJson(key: string): Promise<unknown | null> {
    if (this.failKeys.has(key)) {
      throw new Error('r2 down')
    }
    return this.objects.has(key) ? this.objects.get(key) : null
  }

  async embed(): Promise<number[]> {
    this.embedCalls += 1
    this.nowMs += this.clockJumpOnEmbed
    return Array(embed.dimensions).fill(0.01)
  }

  async query(): Promise<VectorHit[]> {
    return this.vectors
  }

  async rateLimit(key: string): Promise<boolean> {
    const next = (this.used.get(key) ?? 0) + 1
    this.used.set(key, next)
    return next <= this.limit
  }
}

function card(id: string, title: string, text?: Partial<NodeCard['text']>, authors?: string[]): NodeCard {
  return {
    id,
    title,
    authors: authors ?? ['Ada'],
    date: '2024-01-01',
    section: 'Agents',
    topic: null,
    kind: 'arxiv',
    url: `https://example.test/${id}`,
    quality: null,
    text: {
      available: true,
      reason: null,
      code_points: 12,
      chunks: 1,
      ...text,
    },
  }
}

async function build() {
  const sig = await signatures()
  const memory = new Memory()
  const children = Array.from({ length: 30 }, (_, index) => `arxiv:c${String(index).padStart(2, '0')}`)
  const nodes: Record<string, NodeCard> = {
    'arxiv:hub': card('arxiv:hub', 'Hub'),
    'arxiv:a': card('arxiv:a', 'Alpha'),
    'arxiv:b': card('arxiv:b', 'Beta'),
    'arxiv:emoji': card('arxiv:emoji', 'Emoji'),
    'arxiv:case': card('arxiv:case', 'Case Study'),
    'url:web': card('url:web', 'Web note', { available: false, reason: 'no_markdown', code_points: 0, chunks: 0 }),
  }
  const out: GraphDoc['out'] = {
    'arxiv:hub': children.map((id) => ({ target: id, evidence: 'id' })),
    'arxiv:a': [{ target: 'arxiv:b', evidence: 'id' }],
    'arxiv:b': [{ target: 'arxiv:a', evidence: 'title' }],
    'arxiv:emoji': [],
    'arxiv:case': [],
    'url:web': [],
  }
  const incoming: GraphDoc['in'] = {
    'arxiv:hub': [],
    'arxiv:a': [{ source: 'arxiv:b', evidence: 'title' }],
    'arxiv:b': [{ source: 'arxiv:a', evidence: 'id' }],
    'arxiv:emoji': [],
    'arxiv:case': [],
    'url:web': [],
  }
  for (const id of children) {
    nodes[id] = card(id, `Child ${id}`)
    out[id] = []
    incoming[id] = [{ source: 'arxiv:hub', evidence: 'id' }]
  }
  const graph: GraphDoc = { nodes, out, in: incoming }
  const pointer: ActivePointer = {
    release_id: 'rel',
    slot: 'a',
    activated_at: 0,
    reader_schema: embed.reader_schema,
    embedding_signature: sig.embedding,
    build_signature: sig.build,
    verified_passage_count: 2,
    global_index_count: 4,
    publication_check: { ok: true, checked_at: 0, by: 'publish' },
  }
  memory.objects.set('active.json', pointer)
  memory.objects.set('releases/rel/graph.json', graph)
  const emoji = 'a😀b'
  const hello = 'Hello Corpus.'
  await putPaper(memory, 'arxiv:emoji', emoji)
  await putPaper(memory, 'arxiv:case', hello)
  memory.objects.set('slots/a/confirmed.json', {
    release_id: 'rel',
    embedding_signature: sig.embedding,
    build_signature: sig.build,
    passage_count: 1,
    vectors: {
      vec1: {
        paper_id: 'arxiv:case',
        chunk_index: 0,
        content_hash: 'h',
        input_hash: 'i',
      },
    },
  })
  const service = createService(memory, tokenizer)
  return { memory, service, pointer, graph, children }
}

async function putPaper(memory: Memory, id: string, text: string) {
  const hash = await sha256Hex(id)
  memory.objects.set(`releases/rel/papers/${hash}.json`, {
    paper_id: id,
    text,
    chunks: [{
      index: 0,
      start: 0,
      end: pointLength(text),
      token_count: 4,
      content_hash: 'h',
      input_hash: 'i',
    }],
  })
}

function app(service: Service) {
  return createApp(service)
}

async function bodyOf(response: Response) {
  return response.json() as Promise<{ error?: { code: string, message: string }, [key: string]: unknown }>
}

describe('reads', () => {
  it('pages every citation neighbor once', async () => {
    const { service, children } = await build()
    const seen: string[] = []
    let cursor: string | null = null
    let pages = 0
    do {
      const page = await service.citations({
        id: 'arxiv:hub',
        dir: 'out',
        limit: 12,
        cursor,
      }) as { neighbors: { id: string }[], next_cursor: string | null, total: number }
      pages += 1
      expect(page.total).toBe(30)
      seen.push(...page.neighbors.map((neighbor) => neighbor.id))
      cursor = page.next_cursor
    } while (cursor)
    expect(pages).toBe(3)
    expect(seen).toEqual(children)
    expect(new Set(seen).size).toBe(30)
  })

  it('keeps both directions of a reciprocal citation', async () => {
    const { service } = await build()
    const page = await service.citations({ id: 'arxiv:a', dir: 'both', limit: 12, cursor: null }) as {
      neighbors: { id: string, evidence: { direction: string, evidence: string }[] }[]
    }
    expect(page.neighbors).toEqual([{
      id: 'arxiv:b',
      title: 'Beta',
      url: 'https://example.test/arxiv:b',
      date: '2024-01-01',
      section: 'Agents',
      evidence: [
        { direction: 'out', evidence: 'id' },
        { direction: 'in', evidence: 'title' },
      ],
    }])
  })

  it('stops a cyclic bfs at the first visit and caps the tree', async () => {
    const { service } = await build()
    const cycle = await service.traverse({ id: 'arxiv:a', dir: 'out', hops: 2 }) as {
      nodes: { id: string }[]
      tree_edges: { source: string, target: string }[]
      truncated: boolean
    }
    expect(cycle.nodes.map((node) => node.id)).toEqual(['arxiv:a', 'arxiv:b'])
    expect(cycle.tree_edges).toEqual([{ source: 'arxiv:a', target: 'arxiv:b', evidence: 'id' }])
    expect(cycle.truncated).toBe(false)
    const capped = await service.traverse({ id: 'arxiv:hub', dir: 'out', hops: 1 }) as {
      nodes: { id: string }[]
      tree_edges: unknown[]
      truncated: boolean
      reason: string
    }
    expect(capped.nodes).toHaveLength(24)
    expect(capped.tree_edges).toHaveLength(23)
    expect(capped.truncated).toBe(true)
    expect(capped.reason).toBe('node_cap')
    expect(capped.nodes[1].id).toBe('arxiv:c00')
    expect(capped.nodes[23].id).toBe('arxiv:c22')
  })

  it('reads code points, including a non-BMP character, and rejects bad offsets', async () => {
    const { service, pointer } = await build()
    const http = app(service)
    const first = await service.content({ id: 'arxiv:emoji', offset: 1, version: pointer.release_id }) as {
      text: string
      total_length: number
      next_offset: number | null
    }
    expect(first.total_length).toBe(3)
    expect(first.text).toBe('😀b')
    expect(Array.from(first.text)[0]).toBe('😀')
    const end = await service.content({ id: 'arxiv:emoji', offset: 3, version: null }) as {
      text: string
      next_offset: number | null
    }
    expect(end.text).toBe('')
    expect(end.next_offset).toBeNull()
    await expect(service.content({ id: 'arxiv:emoji', offset: 4, version: null }))
      .rejects.toMatchObject({ code: 'invalid_offset', status: 400 })
    const fractional = await http.fetch(new Request('http://localhost/v1/content?id=arxiv:emoji&offset=1.5'))
    expect(fractional.status).toBe(400)
    expect((await bodyOf(fractional)).error?.code).toBe('invalid_offset')
    const negative = await http.fetch(new Request('http://localhost/v1/content?id=arxiv:emoji&offset=-1'))
    expect((await bodyOf(negative)).error?.code).toBe('invalid_offset')
    const conflict = await http.fetch(new Request('http://localhost/v1/content?id=arxiv:emoji&version=other'))
    expect(conflict.status).toBe(409)
    expect((await bodyOf(conflict)).error?.code).toBe('version_conflict')
  })

  it('distinguishes a known paper without text from an unknown id', async () => {
    const { service } = await build()
    const http = app(service)
    const missing = await service.content({ id: 'url:web', offset: 0, version: null }) as {
      available: boolean
      reason: string
    }
    expect(missing.available).toBe(false)
    expect(missing.reason).toBe('no_markdown')
    const unknown = await http.fetch(new Request('http://localhost/v1/paper?id=arxiv:missing'))
    expect(unknown.status).toBe(404)
    expect((await bodyOf(unknown)).error?.code).toBe('unknown_id')
  })

  it('caps authors and rejects an oversized response', async () => {
    const { service, graph } = await build()
    graph.nodes['arxiv:a'].authors = Array.from({ length: 13 }, (_, index) => `A${index}`)
    const paper = await service.paper('arxiv:a') as {
      authors: string[]
      authors_total: number
      authors_truncated: boolean
    }
    expect(paper.authors).toHaveLength(12)
    expect(paper.authors_total).toBe(13)
    expect(paper.authors_truncated).toBe(true)
    graph.nodes['arxiv:a'].title = 'x'.repeat(300000)
    await expect(service.paper('arxiv:a')).rejects.toMatchObject({ code: 'response_too_large' })
  })
})

describe('search and time bounds', () => {
  it('rejects a query before calling the embedding model', async () => {
    const { service, memory } = await build()
    await expect(service.search({ q: '   ', k: 5, ip: '1.1.1.1' }))
      .rejects.toMatchObject({ code: 'invalid_query' })
    await expect(service.search({ q: 'attention', k: Number.NaN, ip: '1.1.1.1' }))
      .rejects.toMatchObject({ code: 'invalid_argument' })
    const http = app(service)
    const tooLong = await http.fetch(new Request(`http://localhost/v1/search?q=${encodeURIComponent('a '.repeat(1000))}`))
    expect(tooLong.status).toBe(400)
    expect((await bodyOf(tooLong)).error?.code).toBe('query_too_long')
    expect(memory.embedCalls).toBe(0)
  })

  it('returns a case-preserving passage and a dangling hit is not an empty 200', async () => {
    const { service, memory } = await build()
    const found = await service.search({ q: 'attention', k: 5, ip: '1.1.1.1' }) as {
      hits: { snippet: string, score: number, content: string, paper_id: string }[]
    }
    expect(found.hits[0].snippet).toBe('Hello Corpus.')
    expect(found.hits[0].score).toBe(0.42)
    expect(found.hits[0].paper_id).toBe('arxiv:case')
    expect(found.hits[0].content).toContain('version=rel')
    memory.vectors = [{ id: 'missing', score: 0.1 }]
    await expect(service.search({ q: 'retrieval', k: 5, ip: '1.1.1.2' }))
      .rejects.toMatchObject({ code: 'dangling_hit', status: 503 })
  })

  it('shares the rate limit across callers of the same address', async () => {
    const { service, memory } = await build()
    memory.limit = 1
    const http = app(service)
    const first = await http.fetch(new Request('http://localhost/v1/search?q=attention', {
      headers: { 'cf-connecting-ip': '9.9.9.9' },
    }))
    expect(first.status).toBe(200)
    await expect(service.search({ q: 'attention', k: 5, ip: '9.9.9.9' }))
      .rejects.toMatchObject({ code: 'rate_limited', status: 429 })
    const other = await service.search({ q: 'attention', k: 5, ip: '8.8.8.8' }) as { hits: unknown[] }
    expect(other.hits).toHaveLength(1)
  })

  it('does not serve an expired pointer when r2 fails', async () => {
    const { service, memory } = await build()
    await service.paper('arxiv:a')
    memory.nowMs = embed.limits.pointer_ttl_seconds * 1000 + 1
    memory.failKeys.add('active.json')
    await expect(service.paper('arxiv:a')).rejects.toMatchObject({ code: 'corpus_unavailable' })
  })

  it('drops a late embedding instead of returning it', async () => {
    const { service, memory } = await build()
    memory.clockJumpOnEmbed = embed.limits.deadline_seconds * 1000 + 1
    await expect(service.search({ q: 'attention', k: 5, ip: '1.1.1.1' }))
      .rejects.toMatchObject({ code: 'deadline_exceeded' })
  })

  it('reports a signature mismatch and can disable search without embedding', async () => {
    const { service, memory, pointer } = await build()
    pointer.embedding_signature = 'nope'
    await expect(service.search({ q: 'attention', k: 5, ip: '1.1.1.1' }))
      .rejects.toMatchObject({ code: 'config_mismatch' })
    expect(memory.embedCalls).toBe(0)
    const disabled = createService(memory, tokenizer, { searchEnabled: false })
    pointer.embedding_signature = (await signatures()).embedding
    await expect(disabled.search({ q: 'attention', k: 5, ip: '1.1.1.1' }))
      .rejects.toMatchObject({ code: 'search_disabled' })
    expect(memory.embedCalls).toBe(0)
  })

  it('reports publish counts from health without embedding', async () => {
    const { service, memory } = await build()
    const health = await service.health() as {
      status: string
      verified_passage_count: number
      global_index_count: number
      grace_seconds: number
      reader_schema: number
    }
    expect(health.status).toBe('ready')
    expect(health.verified_passage_count).toBe(2)
    expect(health.global_index_count).toBe(4)
    expect(health.grace_seconds).toBe(120)
    expect(health.reader_schema).toBe(1)
    expect(memory.embedCalls).toBe(0)
    const empty = createService(new Memory(), tokenizer)
    const down = await empty.health() as { status: string, reader_schema: number }
    expect(down.status).toBe('unavailable')
    expect(down.reader_schema).toBe(1)
    await expect(empty.paper('arxiv:a')).rejects.toMatchObject({ code: 'not_ready', status: 503 })
  })
})

describe('http surface', () => {
  it('serves the manual and a verified openapi origin', async () => {
    const { service } = await build()
    const http = app(service)
    const manual = await http.fetch(new Request('http://localhost/'))
    expect(await manual.text()).toContain('doi:')
    const spec = await http.fetch(new Request('http://key-papers-api.example.workers.dev/openapi.json'))
    const document = await spec.json() as {
      openapi: string
      security: unknown[]
      servers: { url: string }[]
      paths: Record<string, { get: { operationId: string } }>
    }
    expect(document.openapi).toBe('3.1.0')
    expect(document.security).toEqual([])
    expect(document.servers[0].url).toBe('http://key-papers-api.example.workers.dev')
    expect(document.paths['/v1/search'].get.operationId).toBe('searchPassages')
    const spoofed = await http.fetch(new Request('http://evil.example/openapi.json'))
    expect(spoofed.status).toBe(400)
    expect(await spoofed.text()).not.toContain('evil.example')
  })

  it('rejects a citation cursor from another release', async () => {
    const { service, pointer } = await build()
    const http = app(service)
    const first = await http.fetch(new Request('http://localhost/v1/citations?id=arxiv:hub&limit=12'))
    const page = await first.json() as { next_cursor: string }
    pointer.release_id = 'newer'
    const again = await http.fetch(new Request(
      `http://localhost/v1/citations?id=arxiv:hub&limit=12&cursor=${encodeURIComponent(page.next_cursor)}`,
    ))
    expect(again.status).toBe(409)
    expect((await bodyOf(again)).error?.code).toBe('version_conflict')
  })
})

async function rpc(
  http: { fetch(request: Request): Promise<Response> },
  payload: unknown,
  extraHeaders: Record<string, string> = {},
) {
  const response = await http.fetch(new Request('http://localhost/mcp', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      accept: 'application/json, text/event-stream',
      'mcp-protocol-version': '2025-06-18',
      ...extraHeaders,
    },
    body: JSON.stringify(payload),
  }))
  const text = await response.text()
  const parsed = text.includes('data:')
    ? JSON.parse(text.split('\n').filter((line) => line.startsWith('data:')).at(-1)?.slice(5).trim() || 'null')
    : text ? JSON.parse(text) : null
  return { status: response.status, text, parsed }
}

describe('mcp', () => {
  it('answers initialize, lists tools, and returns domain errors without an http status', async () => {
    const { service } = await build()
    const http = app(service)
    expect((await http.fetch(new Request('http://localhost/mcp'))).status).toBe(405)
    expect((await http.fetch(new Request('http://localhost/mcp', { method: 'DELETE' }))).status).toBe(405)
    const badResponse = await http.fetch(new Request('http://localhost/mcp', {
      method: 'POST',
      headers: { 'content-type': 'application/json', accept: 'application/json, text/event-stream' },
      body: '{',
    }))
    expect(badResponse.status).toBeGreaterThanOrEqual(400)
    const init = await rpc(http, {
      jsonrpc: '2.0',
      id: 1,
      method: 'initialize',
      params: {
        protocolVersion: '2025-06-18',
        capabilities: {},
        clientInfo: { name: 'test', version: '0' },
      },
    })
    expect(init.status).toBe(200)
    expect(JSON.stringify(init.parsed)).toContain('key-papers')
    const listed = await rpc(http, { jsonrpc: '2.0', id: 2, method: 'tools/list' })
    const names = JSON.stringify(listed.parsed)
    for (const name of ['search', 'get_paper', 'citations', 'read_content', 'traverse']) {
      expect(names).toContain(name)
    }
    const call = await rpc(http, {
      jsonrpc: '2.0',
      id: 3,
      method: 'tools/call',
      params: { name: 'get_paper', arguments: { id: 'missing' } },
    })
    const encoded = JSON.stringify(call.parsed)
    expect(encoded).toContain('unknown_id')
    expect(encoded).toContain('isError')
    expect(encoded).not.toContain('"status":404')
    const again = await rpc(http, {
      jsonrpc: '2.0',
      id: 4,
      method: 'initialize',
      params: {
        protocolVersion: '2025-06-18',
        capabilities: {},
        clientInfo: { name: 'test', version: '0' },
      },
    })
    expect(again.status).toBe(200)
    const connector = await rpc(http, {
      jsonrpc: '2.0',
      id: 5,
      method: 'initialize',
      params: {
        protocolVersion: '2025-06-18',
        capabilities: {},
        clientInfo: { name: 'chatgpt', version: '0' },
      },
    }, { origin: 'https://chatgpt.com' })
    expect(connector.status).toBe(200)
    expect(connector.text).not.toContain('chatgpt.com')
    const spoofed = await http.fetch(new Request('http://localhost/mcp', {
      method: 'POST',
      headers: {
        host: 'evil.example',
        origin: 'https://evil.example',
        'content-type': 'application/json',
        accept: 'application/json, text/event-stream',
      },
      body: '{}',
    }))
    expect(spoofed.status).toBe(400)
    expect(await spoofed.text()).not.toContain('evil.example')
  })
})
