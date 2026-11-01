/** Independently assembled synthetic format fixture. Never an encoder result. */
import type { GraphDoc, PaperDoc } from '../src/corpus'
import type { FullCorpusManifest, FullCorpusRow } from '../src/full-corpus-store'
import { canonicalJson, sha256Hex, signatures, vectorIdOf } from '../src/signatures'
import { embed } from '../src/tokenize'

export async function fullCorpusFixture(paperCount = 20, chunksPerPaper = 3) {
  const identity = await signatures()
  const graph: GraphDoc = { nodes: {}, out: {}, in: {} }
  const papers = new Map<string, PaperDoc>()
  const rows: FullCorpusRow[] = []
  const query = [1, ...Array(767).fill(0)] as number[]
  for (let paper = 0; paper < paperCount; paper++) {
    const id = 'paper-' + String(paper).padStart(2, '0')
    const parts = Array.from({ length: chunksPerPaper }, (_, i) =>
      `Section ${i}. 😀 Evidence for distinct paper ${paper}, passage ${i}.\n`)
    const text = parts.join('')
    const doc: PaperDoc = { paper_id: id, text, chunks: [] }
    let start = 0
    for (const [index, part] of parts.entries()) {
      const end = start + [...part].length
      const chunk = { index, start, end, token_count: 20,
        content_hash: await sha256Hex(part), input_hash: await sha256Hex(canonicalJson({
          embedding_signature: identity.embedding, input: embed.passage_template + part })) }
      doc.chunks.push(chunk)
      rows.push({ id: await vectorIdOf('full-probe', id, index), paper_id: id,
        chunk_index: index, start, end, token_count: chunk.token_count,
        content_hash: chunk.content_hash, input_hash: chunk.input_hash, sourceIndex: rows.length })
      start = end
    }
    papers.set(id, doc)
    graph.nodes[id] = { id, title: 'Unique title ' + paper, authors: ['Test Author'],
      url: 'https://example.invalid/' + id, section: 'Fixture', kind: 'url',
      text: { available: true, reason: null, code_points: [...text].length,
        chunks: chunksPerPaper, object: await sha256Hex(id) } }
    graph.out[id] = []; graph.in[id] = []
  }
  const missing = 'unavailable-card'
  graph.nodes[missing] = { id: missing, title: 'Unavailable exact title', text: {
    available: false, reason: 'no_markdown', code_points: 0, chunks: 0 } }
  graph.out[missing] = []; graph.in[missing] = []
  const release = await sha256Hex(canonicalJson({ graph, papers: [...papers], fixture: true }))
  const packedRows = rows.slice().sort((a, b) => a.id < b.id ? -1 : 1)
  const paperIds = Object.keys(graph.nodes).sort()
  const files = new Map<string, Uint8Array>()
  const entries: FullCorpusManifest['files'] = {}
  const hashBytes = async (data: Uint8Array) => [...new Uint8Array(
    await crypto.subtle.digest('SHA-256', data))].map((n) => n.toString(16).padStart(2, '0')).join('')
  const put = async (path: string, data: Uint8Array | object) => {
    const bytes = data instanceof Uint8Array ? data : new TextEncoder().encode(canonicalJson(data))
    files.set(path, bytes)
    entries[path] = { bytes: bytes.byteLength, sha256: await hashBytes(bytes) }
  }
  const graphPath = `releases/${release}/graph.json`
  await put(graphPath, graph)
  const paperPaths = new Map<string, string>()
  for (const [id, doc] of papers) {
    const path = `releases/${release}/papers/${await sha256Hex(id)}.json`
    paperPaths.set(id, path); await put(path, doc)
  }
  const metadata = new Uint8Array(rows.length * 128), view = new DataView(metadata.buffer)
  const writeHex = (at: number, text: string) => {
    for (let n = 0; n < 32; n++) metadata[at + n] = Number.parseInt(text.slice(n * 2, n * 2 + 2), 16)
  }
  for (const [index, row] of packedRows.entries()) {
    const at = index * 128
    writeHex(at, row.id)
    const values = [paperIds.indexOf(row.paper_id), row.chunk_index, row.start, row.end, row.token_count, row.sourceIndex]
    values.forEach((value, column) => view.setUint32(at + 32 + column * 4, value, true))
    writeHex(at + 56, row.content_hash); writeHex(at + 88, row.input_hash)
  }
  const vectors = new Uint8Array(rows.length * 768)
  const norms = new Uint8Array(rows.length * 8), normView = new DataView(norms.buffer)
  const reference = new Uint8Array(rows.length * 768 * 4), referenceView = new DataView(reference.buffer)
  for (let i = 0; i < rows.length; i++) {
    vectors[i * 768] = 127; normView.setFloat64(i * 8, 1 / 127, true)
    referenceView.setFloat32(i * 768 * 4, 1, true)
  }
  await put('metadata.bin', metadata); await put('vectors-0000.i8', vectors)
  await put('norms.f64', norms); await put('references.f32', reference)
  const manifest: FullCorpusManifest = { schema_version: 1, reader_schema: embed.reader_schema,
    kind: 'full-corpus-int8-geometry-fixture', synthetic: true, publication_ready: false,
    scope: 'isolated-full-corpus-evaluation-not-production', slot: 'full-probe', release_id: release,
    embedding_signature: identity.embedding, build_signature: identity.build,
    passage_count: rows.length, dimensions: 768, paper_ids: paperIds, text_paper_ids: [...papers.keys()],
    graph_path: graphPath, files: entries, source_manifest_sha256: await sha256Hex(canonicalJson(graph)),
    source_rows_sha256: await sha256Hex(canonicalJson(rows)), fixture_vectors: {
      generator: 'independent-test-ties-v1', seed: 0, count: rows.length, dimensions: 768,
      dtype: 'float32', byte_order: 'little', normalization: 'l2', sha256: await hashBytes(reference),
      purpose: 'allocation-and-contract-testing-not-semantic-quality' },
    metadata: { path: 'metadata.bin', row_bytes: 128, order: 'vector-id-lexicographic' },
    index: { kind: 'exact-int8', quantization: 'per-row-maxabs-rint-127', norms_path: 'norms.f64',
      shards: [{ path: 'vectors-0000.i8', start: 0, count: rows.length }] },
    compatibility: { path: 'references.f32', indices: rows.map((_, i) => i),
      source_indices: packedRows.map((row) => row.sourceIndex) } }
  const syncManifest = async () => {
    const bytes = new TextEncoder().encode(canonicalJson(manifest)); files.set('probe.json', bytes)
    return hashBytes(bytes)
  }
  const manifestSha = await syncManifest()
  const reads = new Map<string, number>()
  const assets = { async fetch(request: Request) {
    const path = new URL(request.url).pathname.slice(1)
    reads.set(path, (reads.get(path) ?? 0) + 1)
    const data = files.get(path)
    return data ? new Response(data.slice(), { headers: { 'content-length': String(data.length) } })
      : new Response('missing', { status: 404 })
  } }
  return { manifest, manifestSha, assets, reads, files, graph, papers, paperPaths,
    rows, packedRows, query, put, syncManifest }
}
