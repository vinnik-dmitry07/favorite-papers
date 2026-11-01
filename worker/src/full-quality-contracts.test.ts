// Synthetic routing fixture: no learned vectors or retrieval-quality claim.
import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'

import type { CorpusStore, GraphDoc, NodeCard, PaperDoc, VectorHit } from './corpus'
import { handleRest } from './http'
import { handleMcp } from './mcp'
import { createService } from './service'
import { sha256Hex, signatures } from './signatures'
import { WordPieceTokenizer } from './tokenize'

const tokenizer = new WordPieceTokenizer(readFileSync(
  new URL('../tokenizer/vocab.txt', import.meta.url), 'utf8',
))

async function fixture(order: number[]) {
  const release = 'a'.repeat(64)
  const sig = await signatures()
  const objects = new Map<string, unknown>()
  const graph: GraphDoc = { nodes: {}, out: {}, in: {} }
  const mappings: Record<string, unknown> = {}
  const vectors: VectorHit[] = []
  const papers = Array.from({ length: 10 }, (_, i) => `arxiv:2601.${String(i).padStart(5, '0')}`)
  const documents = new Map<string, PaperDoc>()
  for (const [i, id] of papers.entries()) {
    const text = ('😀 boundary evidence for paper ' + i + '. ').repeat(100)
    const card: NodeCard = { id, title: `Boundary paper ${i}`, url: `https://example.test/${i}`,
      text: { available: true, reason: null, code_points: Array.from(text).length, chunks: order.length } }
    graph.nodes[id] = card; graph.out[id] = []; graph.in[id] = []
    documents.set(id, { paper_id: id, text, chunks: [] })
  }
  // More than40 ranked candidates, with independently controlled paper overlap.
  for (const [rank, paperIndex] of order.entries()) {
    const paperId = papers[paperIndex]
    const id = rank.toString(16).padStart(64, '0')
    const chunk = { index: rank, start: 0, end: 100, token_count: 30,
      content_hash: 'synthetic-content-' + rank, input_hash: 'synthetic-input-' + rank }
    documents.get(paperId)!.chunks.push(chunk)
    mappings[id] = { paper_id: paperId, chunk_index: rank,
      content_hash: chunk.content_hash, input_hash: chunk.input_hash }
    vectors.push({ id, score: 1 - rank / 1000 })
  }
  const catalogId = 'url:catalog-only'
  graph.nodes[catalogId] = { id: catalogId, title: 'Exact catalog-only title',
    text: { available: false, reason: 'no_markdown', code_points: 0, chunks: 0 } }
  graph.out[catalogId] = []; graph.in[catalogId] = []
  objects.set('active.json', { release_id: release, slot: 'full-probe', activated_at: 0,
    reader_schema: 1, embedding_signature: sig.embedding, build_signature: sig.build,
    verified_passage_count: order.length, global_index_count: order.length,
    publication_check: { ok: true, checked_at: 0, by: 'synthetic-contract-test' } })
  objects.set(`releases/${release}/graph.json`, graph)
  objects.set('slots/full-probe/confirmed.json', { release_id: release,
    embedding_signature: sig.embedding, build_signature: sig.build,
    passage_count: order.length, vectors: mappings })
  for (const [id, doc] of documents) objects.set(`releases/${release}/papers/${await sha256Hex(id)}.json`, doc)
  const calls = { embed: 0, limits: [] as number[] }
  const store: CorpusStore = {
    now: () => 0, getJson: async (key) => objects.get(key) ?? null,
    rateLimit: async () => true,
    embed: async () => { calls.embed++; return Array(768).fill(0.01) },
    query: async (_slot, _vector, topK) => { calls.limits.push(topK); return vectors.slice(0, topK) },
  }
  const service = createService(store, tokenizer)
  const rest = async () => {
    const response = await handleRest(new Request('http://localhost/v1/search?q=boundary&k=8'), service)
    expect(response.status).toBe(200)
    return await response.json() as { hits: { paper_id: string, chunk_index: number }[] }
  }
  const mcp = async (query: string) => {
    const response = await handleMcp(new Request('http://localhost/mcp', {
      method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json, text/event-stream' },
      body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call',
        params: { name: 'search', arguments: { query } } }),
    }), service)
    expect(response.status).toBe(200)
    const text = await response.text()
    const payload = JSON.parse(text.includes('data:')
      ? text.split('\n').filter((line) => line.startsWith('data:')).at(-1)!.slice(5) : text)
    expect(payload.error).toBeUndefined()
    expect(payload.result.isError).not.toBe(true)
    return payload.result.structuredContent.results.map((item: { id: string }) =>
      JSON.parse(Buffer.from(item.id.slice(4), 'base64url').toString('utf8')),
    ) as { paper: string, start: number | null }[]
  }
  return { rest, mcp, calls, papers, catalogId }
}

describe('full-quality projections through production REST and MCP', () => {
  it('applies top40 before deduplication, excluding the41st candidate', async () => {
    const f = await fixture([...Array(39).fill(0), 1, 2, 3, 4, 5, 6, 7, 8, 9])
    expect((await f.rest()).hits.map((hit) => hit.paper_id)).toEqual(f.papers.slice(0, 2))
    expect(f.calls.limits).toEqual([40])
  })

  it('applies MCP top25 before deduplication and preserves mixed catalog routing', async () => {
    const f = await fixture([...Array(24).fill(0), 1, 2, 3, 4, 5, 6, 7, 8, 9, ...Array(15).fill(9)])
    const results = await f.mcp('boundary')
    expect(results.filter((row) => row.start !== null).map((row) => row.paper)).toEqual(f.papers.slice(0, 2))
    expect(results.filter((row) => row.start === null)).toHaveLength(3)
    expect(f.calls.limits).toEqual([25])
    expect(f.calls.embed).toBe(1)
  })

  it('limits distinct paper results to eight REST and five MCP semantic hits', async () => {
    const f = await fixture(Array.from({ length: 60 }, (_, i) => i % 10))
    expect((await f.rest()).hits.map((hit) => hit.paper_id)).toEqual(f.papers.slice(0, 8))
    const results = await f.mcp('boundary')
    expect(results.filter((row) => row.start !== null).map((row) => row.paper)).toEqual(f.papers.slice(0, 5))
    expect(results).toHaveLength(8)
    expect(f.calls.limits).toEqual([40, 25])
  })

  it('bypasses semantic embedding for an exact catalog-only match', async () => {
    const f = await fixture(Array.from({ length: 60 }, (_, i) => i % 10))
    expect(await f.mcp('Exact catalog-only title')).toEqual([{ paper: f.catalogId, version: 'a'.repeat(64), start: null }])
    expect(f.calls.embed).toBe(0)
    expect(f.calls.limits).toEqual([])
  })
})
