// Optional actual-model integration. Ordinary CI uses the separate unit fixtures;
// a real pilot must run this suite with pinned local BGE passage/query vectors.
import { createHash } from 'node:crypto'
import { readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { describe, expect, it } from 'vitest'

import { createStaticCorpusStore } from './static-corpus-store'
import { createService } from './service'
import { handleRest } from './http'
import { handleMcp } from './mcp'
import { WordPieceTokenizer } from './tokenize'
import { outputs } from './contracts'

const directory = process.env.REAL_PROBE_DIR
const queryFile = process.env.REAL_PROBE_QUERY_VECTORS
const hash = (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex')

describe.skipIf(!directory || !queryFile)('actual pinned BGE subset through production contracts', () => {
  it('preserves REST/MCP text and reports passage and answer-context evidence separately', async () => {
    const root = resolve(directory!)
    const manifestBytes = readFileSync(resolve(root, 'probe.json'))
    const manifest = JSON.parse(manifestBytes.toString('utf8'))
    const queryData = JSON.parse(readFileSync(queryFile!, 'utf8'))
    expect(queryData.kind).toBe('local-real-query-vectors')
    expect(queryData.release_id).toBe(manifest.release_id)
    expect(queryData.embedding_signature).toBe(manifest.embedding_signature)
    expect(queryData.vectors_sha256).toBe(manifest.embeddings.sha256)
    const queryVectors = new Map<string, number[]>(queryData.queries.map(
      (row: { query: string, vector: number[] }) => [row.query, row.vector],
    ))
    const assets = { async fetch(request: Request) {
      const path = resolve(root, '.' + new URL(request.url).pathname)
      if (!path.startsWith(root + '/')) return new Response(null, { status: 400 })
      try { return new Response(new Uint8Array(readFileSync(path))) }
      catch { return new Response(null, { status: 404 }) }
    } }
    const bundle = await createStaticCorpusStore(assets, hash(manifestBytes), async (text) => {
      const vector = queryVectors.get(text)
      if (!vector) throw new Error('Local query embedding is missing: ' + text)
      return vector
    })
    const tokenizer = new WordPieceTokenizer(readFileSync(
      new URL('../tokenizer/vocab.txt', import.meta.url), 'utf8',
    ))
    const service = createService(bundle.store, tokenizer)
    let rpcId = 0
    const rpc = async (name: string, args: unknown) => {
      const response = await handleMcp(new Request('http://localhost/mcp', {
        method: 'POST', headers: { 'content-type': 'application/json',
          accept: 'application/json, text/event-stream', 'mcp-protocol-version': '2025-06-18' },
        body: JSON.stringify({ jsonrpc: '2.0', id: ++rpcId, method: 'tools/call',
          params: { name, arguments: args } }),
      }), service)
      expect(response.status).toBe(200)
      const text = await response.text()
      const body = JSON.parse(text.includes('data:')
        ? text.split('\n').filter((line) => line.startsWith('data:')).at(-1)!.slice(5).trim() : text)
      expect(body.error).toBeUndefined()
      expect(body.result.isError).not.toBe(true)
      return body.result.structuredContent
    }
    const results: Record<string, unknown>[] = []
    const oracleFailures: string[] = []
    const answerFailures: string[] = []
    const matchesEvidence = (text: string, query: any) => {
      const lower = text.toLowerCase()
      return query.required_passage_terms.every((term: string) => lower.includes(term.toLowerCase()))
        && (!query.passage_evidence_any?.length || query.passage_evidence_any.some(
          (group: string[]) => group.every((term) => lower.includes(term.toLowerCase())),
        ))
    }
    let oracleCount = 0
    for (const query of manifest.queries) {
      const search = await handleRest(new Request('http://localhost/v1/search?'
        + new URLSearchParams({ q: query.query, k: '8' })), service)
      expect(search.status).toBe(200)
      const body = await search.json() as { hits: { paper_id: string, chunk_index: number,
        start: number, end: number, snippet: string, content: string, score: number }[] }
      expect(body.hits.length).toBeGreaterThan(0)
      const target = body.hits.find((hit) => hit.paper_id === query.expected_paper_id)
      expect(target).toBeDefined()
      const paperPath = `releases/${manifest.release_id}/papers/`
        + createHash('sha256').update(query.expected_paper_id).digest('hex') + '.json'
      const paper = JSON.parse(readFileSync(resolve(root, paperPath), 'utf8'))
      const passage = Array.from(paper.text).slice(target!.start, target!.end).join('')
      if (query.required_passage_terms?.length) {
        oracleCount++
        const termsMatch = matchesEvidence(passage, query)
        const chunkMatches = !query.gold_chunk_indices?.length
          || query.gold_chunk_indices.includes(target!.chunk_index)
        if (!termsMatch || !chunkMatches) oracleFailures.push(query.id)
      }
      const content = await handleRest(new Request('http://localhost' + target!.content), service)
      expect(content.status).toBe(200)
      const textBody = await content.json() as { text: string }
      expect(textBody.text).toBe(Array.from(paper.text).slice(target!.start, target!.start + 6000).join(''))
      const restAnswer = !query.required_passage_terms?.length || matchesEvidence(textBody.text, query)
      const found = outputs.search.parse(await rpc('search', { query: query.query }))
      let fetchedText = false
      let mcpAnswer = !query.required_passage_terms?.length
      for (const hit of found.results) {
        const fetched = outputs.fetch.parse(await rpc('fetch', { id: hit.id }))
        expect(fetched.id).toBe(hit.id)
        expect(fetched.url).toBe(hit.url)
        expect(fetched.metadata.corpus_version).toBe(manifest.release_id)
        if (fetched.metadata.paper_id === query.expected_paper_id
            && fetched.metadata.item_type === 'text_part') {
          const metadata = fetched.metadata as { start: number, end: number }
          expect(fetched.text).toBe(Array.from(paper.text).slice(metadata.start, metadata.end).join(''))
          fetchedText = true
          if (query.required_passage_terms?.length && matchesEvidence(fetched.text, query)) mcpAnswer = true
        }
      }
      expect(fetchedText, query.id).toBe(true)
      if (!restAnswer || !mcpAnswer) answerFailures.push(query.id)
      results.push({ id: query.id, paper_id: target!.paper_id,
        chunk_index: target!.chunk_index, score: target!.score,
        passage_oracle_checked: Boolean(query.required_passage_terms?.length),
        passage_oracle_passed: query.required_passage_terms?.length
          ? !oracleFailures.includes(query.id) : null,
        rest_answer_evidence: query.required_passage_terms?.length ? restAnswer : null,
        mcp_answer_evidence: query.required_passage_terms?.length ? mcpAnswer : null,
        rest_content_exact: true, mcp_fetch_exact: true })
    }
    expect(oracleCount).toBeGreaterThanOrEqual(2)
    if (process.env.REAL_PROBE_REPORT) writeFileSync(process.env.REAL_PROBE_REPORT,
      JSON.stringify({ scope: 'local-real-subset-contract-integration',
        cloudflare_compatibility: 'not_tested', external_llm_agent: 'not_tested',
        full_corpus_quality: 'not_tested', manifest_sha256: hash(manifestBytes),
        release_id: manifest.release_id, passage_count: manifest.passage_count,
        embeddings: manifest.embeddings, results, passage_oracles: oracleCount,
        oracle_revision: manifest.oracle_revision, oracle_note: manifest.oracle_note,
        passage_retrieval_gate: oracleFailures.length ? 'failed' : 'passed',
        answer_context_gate: answerFailures.length ? 'failed' : 'passed',
        passage_oracle_failures: oracleFailures, answer_context_failures: answerFailures }, null, 2) + '\n')
    // This is a development integration gate. Keep failed passage retrieval in
    // the report even when reading the returned context supplies the answer.
    expect(answerFailures, 'Search/read answer evidence is missing').toEqual([])
  }, 30000)
})
