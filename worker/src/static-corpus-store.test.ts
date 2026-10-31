import { readFileSync } from 'node:fs'
import { createHash } from 'node:crypto'
import { resolve } from 'node:path'
import { describe, expect, it, vi } from 'vitest'

import { createStaticCorpusStore, type RealProbeManifest } from './static-corpus-store'
import { canonicalJson, sha256Hex, signatures, vectorIdOf } from './signatures'
import { embed, WordPieceTokenizer } from './tokenize'
import { createService } from './service'
import { handleRest } from './http'
import { handleMcp } from './mcp'
import { outputs } from './contracts'
import type { GraphDoc, PaperDoc } from './corpus'

const tokenizer = new WordPieceTokenizer(readFileSync(new URL('../tokenizer/vocab.txt', import.meta.url), 'utf8'))
const digest = (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex')
const encode = (value: unknown) => new TextEncoder().encode(canonicalJson(value))

async function fixture() {
  const sig = await signatures()
  const release = 'a'.repeat(64)
  const paperIds = ['arxiv:alpha', 'arxiv:beta']
  const files = new Map<string, Uint8Array>()
  const papers = new Map<string, PaperDoc>()
  const graph: GraphDoc = { nodes: {}, out: {}, in: {} }
  const manifest: RealProbeManifest = {
    schema_version: 1, reader_schema: embed.reader_schema, kind: 'real-subset', synthetic: false,
    publication_ready: false, scope: 'isolated-integration-subset-not-full-corpus', dimensions: 768,
    slot: 'real-probe', release_id: release, embedding_signature: sig.embedding,
    build_signature: sig.build, passage_count: 200, paper_ids: paperIds,
    sample_paper_id: paperIds[0], rows: [], files: {},
    compatibility_indices: Array.from({ length: 200 }, (_, i) => i),
    queries: [{ id: 'grouping', query: 'How do grouped advantages work?', expected_paper_id: paperIds[0] }],
    embeddings: { path: 'vectors.f32', sha256: '', model_id: embed.tokenizer.id,
      model_revision: embed.tokenizer.revision, pooling: 'cls', normalization: 'l2',
      dtype: 'float32', byte_order: 'little', dimensions: 768, count: 200 },
  }
  for (const id of paperIds) {
    const paper: PaperDoc = { paper_id: id, text: '', chunks: [] }
    for (let index = 0; index < 100; index++) {
      const passage = `😀 ${id} paragraph ${index}: Grouped policy advantages use relative normalization.\n`
      const start = Array.from(paper.text).length
      const end = start + Array.from(passage).length
      const chunk = { index, start, end, token_count: tokenizer.tokenIds('', passage).length,
        content_hash: await sha256Hex(passage),
        input_hash: await sha256Hex(canonicalJson({ embedding_signature: sig.embedding,
          input: embed.passage_template + passage })) }
      paper.chunks.push(chunk)
      paper.text += passage
      manifest.rows.push({ id: await vectorIdOf(manifest.slot, id, index), paper_id: id,
        chunk_index: index, start, end, token_count: chunk.token_count,
        content_hash: chunk.content_hash, input_hash: chunk.input_hash })
    }
    papers.set(id, paper)
    const paperHash = await sha256Hex(id)
    files.set(`releases/${release}/papers/${paperHash}.json`, encode(paper))
    graph.nodes[id] = { id, title: id === paperIds[0] ? 'Alpha report' : 'Beta report',
      authors: ['Ada'], url: `https://example.test/${id}`, section: 'Research', kind: 'arxiv',
      text: { available: true, reason: null, code_points: Array.from(paper.text).length,
        chunks: paper.chunks.length, object: paperHash } }
    graph.out[id] = id === paperIds[0] ? [{ target: paperIds[1], evidence: 'id' }] : []
    graph.in[id] = id === paperIds[1] ? [{ source: paperIds[0], evidence: 'id' }] : []
  }
  files.set(`releases/${release}/graph.json`, encode(graph))
  const actualRelease = await sha256Hex(canonicalJson({
    graph: digest(encode(graph)), papers: await sha256Hex(canonicalJson(Object.fromEntries(papers))),
    build_signature: sig.build, embedding_signature: sig.embedding,
  }))
  for (const [path, bytes] of [...files]) {
    files.delete(path)
    files.set(path.replace(release, actualRelease), bytes)
  }
  manifest.release_id = actualRelease
  const vectorBytes = new Uint8Array(200 * 768 * 4)
  const vectorView = new DataView(vectorBytes.buffer)
  for (let row = 0; row < 200; row++) {
    const pair = row % 3 === 0 ? [1, 0] : row % 3 === 1 ? [0, 1] : [0.6, 0.8]
    pair.forEach((value, dimension) => vectorView.setFloat32((row * 768 + dimension) * 4, value, true))
  }
  files.set('vectors.f32', vectorBytes)
  const updateManifest = () => {
    manifest.files = Object.fromEntries([...files].filter(([path]) => path !== 'probe.json')
      .map(([path, bytes]) => [path, digest(bytes)]))
    manifest.embeddings.sha256 = manifest.files['vectors.f32']
    files.set('probe.json', encode(manifest))
    return digest(files.get('probe.json')!)
  }
  const fetched: string[] = []
  const assets = { async fetch(request: Request) {
    const path = new URL(request.url).pathname.slice(1)
    fetched.push(path)
    const bytes = files.get(path)
    return bytes ? new Response(bytes.slice()) : new Response(null, { status: 404 })
  } }
  return { files, papers, graph, manifest, updateManifest, assets, fetched, manifestHash: updateManifest() }
}

const queryVector = () => [3, 4, ...Array(766).fill(0)]

describe('verified static subset', () => {
  it('matches an independent exhaustive cosine reference with stable tie ordering', async () => {
    const data = await fixture()
    const bundle = await createStaticCorpusStore(data.assets, data.manifestHash, async () => queryVector())
    const expected = data.manifest.rows.map((row, index) => {
      const bytes = data.files.get('vectors.f32')!
      const view = new DataView(bytes.buffer)
      const score = view.getFloat32(index * 768 * 4, true) * 0.6
        + view.getFloat32((index * 768 + 1) * 4, true) * 0.8
      return { id: row.id, score }
    }).sort((a, b) => b.score - a.score || (a.id < b.id ? -1 : 1)).slice(0, 40)
    const actual = await bundle.store.query('real-probe', queryVector(), 40)
    expect(actual.map((hit) => hit.id)).toEqual(expected.map((hit) => hit.id))
    actual.forEach((hit, index) => expect(hit.score).toBeCloseTo(expected[index].score, 12))
    expect(new Set(data.fetched).size).toBe(data.fetched.length)
    expect(await bundle.store.getJson('active.json')).toMatchObject({
      verified_passage_count: 200, publication_check: { ok: true, by: 'isolated-real-probe' },
    })
    expect(await bundle.store.getJson('unrelated.json')).toBeNull()
    const reference = bundle.referencePassage(2)
    expect(reference.input).toContain('paragraph 2:')
    expect(reference.input.startsWith('😀')).toBe(true)
    reference.vector[0] = 99
    expect(bundle.referencePassage(2).vector[0]).toBeCloseTo(0.6)
  })

  it('runs the production REST search → content path at canonical Unicode offsets', async () => {
    const data = await fixture()
    const calls: string[] = []
    const { store } = await createStaticCorpusStore(data.assets, data.manifestHash, async (text) => {
      calls.push(text)
      return queryVector()
    })
    const service = createService(store, tokenizer)
    const response = await handleRest(new Request('http://localhost/v1/search?q=grouped%20advantages&k=8'), service)
    expect(response.status).toBe(200)
    const found = outputs.passages.parse(await response.json())
    expect(found.hits).toHaveLength(2)
    expect(calls).toEqual(['grouped advantages'])
    for (const hit of found.hits) {
      const expected = Array.from(data.papers.get(hit.paper_id)!.text).slice(hit.start, hit.end).join('')
      expect(hit.snippet).toBe(expected)
      const content = await handleRest(new Request('http://localhost' + hit.content), service)
      expect(content.status).toBe(200)
      expect(outputs.content.parse(await content.json()).text.startsWith(expected)).toBe(true)
    }
    const stale = await handleRest(new Request('http://localhost/v1/content?id=arxiv:alpha&version=stale'), service)
    expect(stale.status).toBe(409)
    const traverse = outputs.traverse.parse(await service.traverse({ id: 'arxiv:beta', dir: 'in', hops: 1 }))
    expect(traverse.tree_edges[0]).toMatchObject({ parent: 'arxiv:beta', child: 'arxiv:alpha' })
  })

  it('runs actual MCP search → fetch with canonical IDs and source citations', async () => {
    const data = await fixture()
    const { store } = await createStaticCorpusStore(data.assets, data.manifestHash, async () => queryVector())
    const service = createService(store, tokenizer)
    const rpc = async (name: string, args: unknown) => {
      const response = await handleMcp(new Request('http://localhost/mcp', {
        method: 'POST', headers: { 'content-type': 'application/json',
          accept: 'application/json, text/event-stream', 'mcp-protocol-version': '2025-06-18' },
        body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name, arguments: args } }),
      }), service)
      expect(response.status).toBe(200)
      const text = await response.text()
      const body = JSON.parse(text.includes('data:')
        ? text.split('\n').filter((line) => line.startsWith('data:')).at(-1)!.slice(5).trim() : text)
      expect(body.result.isError).not.toBe(true)
      return body.result.structuredContent
    }
    const result = outputs.search.parse(await rpc('search', { query: 'How do grouped advantages work?' }))
    expect(result.results).toHaveLength(2)
    for (const hit of result.results) {
      expect(hit.id.startsWith('doc:')).toBe(true)
      const document = outputs.fetch.parse(await rpc('fetch', { id: hit.id }))
      expect(document.url).toBe(hit.url)
      expect(document.text).toContain('😀')
      expect(document.text).toContain('relative normalization')
      expect(document.metadata.corpus_version).toBe(data.manifest.release_id)
    }
  })

  it('does not bypass the injected query limiter or silently accept invalid vectors', async () => {
    const data = await fixture()
    let calls = 0
    const { store } = await createStaticCorpusStore(data.assets, data.manifestHash,
      async () => { calls++; return queryVector() }, async () => false)
    const service = createService(store, tokenizer)
    await expect(service.search({ q: 'grouped advantages', k: 5, ip: 'shared' }))
      .rejects.toMatchObject({ code: 'rate_limited' })
    expect(calls).toBe(0)
    await expect(store.query('other', queryVector(), 5)).rejects.toMatchObject({ code: 'config_mismatch' })
    await expect(store.query('real-probe', Array(768).fill(0), 5)).rejects.toMatchObject({ code: 'config_mismatch' })
    await expect(store.query('real-probe', [Number.NaN, ...Array(767).fill(0)], 5))
      .rejects.toMatchObject({ code: 'config_mismatch' })
  })
})

describe('static subset evidence boundaries', () => {
  it.each([null, '1'])('bounds an oversized stream with content-length %s before buffering it all', async (declared) => {
    let chunks = 0
    const cancel = vi.fn(() => new Promise<void>(() => {}))
    const assets = { async fetch() {
      const body = new ReadableStream<Uint8Array>({
        pull(controller) { chunks++; controller.enqueue(new Uint8Array(1024 * 1024)) },
        cancel,
      })
      return new Response(body, { headers: declared === null ? {} : { 'content-length': declared } })
    } }
    await expect(createStaticCorpusStore(assets, 'a'.repeat(64), async () => queryVector()))
      .rejects.toThrow('assets exceed subset size bound')
    expect(cancel).toHaveBeenCalledOnce()
    // The stream could produce unbounded bytes; stop after the first excess,
    // allowing at most one native stream prefetch.
    expect(chunks).toBeLessThanOrEqual(6)
  })

  it.each(['-1', 'NaN', 'Infinity', '1.5', '5000000'])('rejects invalid asset length %s before reading', async (length) => {
    let reads = 0
    const body = new ReadableStream<Uint8Array>({
      pull(controller) { reads++; controller.enqueue(new Uint8Array([32])) },
    }, { highWaterMark: 0 })
    const assets = { async fetch() { return new Response(body, { headers: { 'content-length': length } }) } }
    await expect(createStaticCorpusStore(assets, 'a'.repeat(64), async () => queryVector()))
      .rejects.toThrow('asset exceeds size bound')
    expect(reads).toBe(0)
  })

  it('rejects a stale manifest hash or altered asset before exposing an active corpus', async () => {
    const data = await fixture()
    await expect(createStaticCorpusStore(data.assets, 'b'.repeat(64), async () => queryVector()))
      .rejects.toThrow('checksum mismatch: probe.json')
    const graphPath = `releases/${data.manifest.release_id}/graph.json`
    data.files.set(graphPath, encode({ ...data.graph, in: {} }))
    await expect(createStaticCorpusStore(data.assets, data.manifestHash, async () => queryVector()))
      .rejects.toThrow('checksum mismatch')
  })

  it.each(['dangling-row', 'unicode-offset', 'input-hash', 'duplicate-row', 'graph-edge',
    'nan-vector', 'unnormalized-vector', 'short-vector', 'traversal-path', 'unpinned-model', 'incomplete-vectors'])(
    'rejects %s even when a new manifest pins the corrupt bytes', async (kind) => {
      const data = await fixture()
      const row = data.manifest.rows[0]
      if (kind === 'dangling-row') row.chunk_index = 900
      if (kind === 'unicode-offset') row.start = 1
      if (kind === 'input-hash') row.input_hash = 'b'.repeat(64)
      if (kind === 'duplicate-row') data.manifest.rows[1] = { ...row }
      if (kind === 'graph-edge') {
        data.graph.out['arxiv:alpha'] = [{ target: 'arxiv:missing', evidence: 'id' }]
        data.files.set(`releases/${data.manifest.release_id}/graph.json`, encode(data.graph))
      }
      if (kind === 'nan-vector' || kind === 'unnormalized-vector') {
        const bytes = data.files.get('vectors.f32')!
        new DataView(bytes.buffer).setFloat32(0, kind === 'nan-vector' ? Number.NaN : 2, true)
      }
      if (kind === 'short-vector') data.files.set('vectors.f32', new Uint8Array(4))
      if (kind === 'traversal-path') data.files.set('../outside.json', encode({}))
      if (kind === 'unpinned-model') data.manifest.embeddings.model_revision = 'main'
      if (kind === 'incomplete-vectors') data.manifest.embeddings.count = 199
      const manifestHash = data.updateManifest()
      await expect(createStaticCorpusStore(data.assets, manifestHash, async () => queryVector()))
        .rejects.toMatchObject({ code: 'config_mismatch', status: 503 })
    },
  )
})

it.skipIf(!process.env.REAL_PROBE_DIR)('loads the opt-in real BGE bundle and preserves canonical inputs', async () => {
  const directory = resolve(process.env.REAL_PROBE_DIR!)
  const bytes = readFileSync(resolve(directory, 'probe.json'))
  const manifest = JSON.parse(bytes.toString('utf8')) as RealProbeManifest
  const assets = { async fetch(request: Request) {
    const path = new URL(request.url).pathname.slice(1)
    try {
      return new Response(new Uint8Array(readFileSync(resolve(directory, path))))
    } catch {
      return new Response(null, { status: 404 })
    }
  } }
  const bundle = await createStaticCorpusStore(assets, digest(bytes), async () => {
    throw new Error('This integrity test does not call an embedding provider')
  })
  expect(bundle.manifest.passage_count).toBe(manifest.passage_count)
  const reference = bundle.referencePassage(0)
  const paperPath = `releases/${manifest.release_id}/papers/${await sha256Hex(reference.row.paper_id)}.json`
  const paper = JSON.parse(readFileSync(resolve(directory, paperPath), 'utf8')) as PaperDoc
  expect(reference.input).toBe(embed.passage_template
    + Array.from(paper.text).slice(reference.row.start, reference.row.end).join(''))
  const hits = await bundle.store.query(manifest.slot, reference.vector, 40)
  expect(hits[0].score).toBeGreaterThan(0.999)
  expect(hits.map((hit) => hit.id)).toContain(reference.row.id)
})
