import { rankedCatalog } from './catalog-search'
import { CorpusCache, type CorpusStore, type NodeCard } from './corpus'
import { DomainError, fail, parseBoundedInt, parseId, parseOffset } from './schemas'
import { canonicalJson, signatures, sha256Hex } from './signatures'
import { embed, pointLength, slicePoints, type WordPieceTokenizer } from './tokenize'

export interface CitationArgs {
  id: string
  dir: 'out' | 'in' | 'both'
  limit: number
  cursor: string | null
}

export interface TraverseArgs {
  id: string
  dir: 'out' | 'in' | 'both'
  hops: number
  max_nodes?: number
}

export interface ContentArgs {
  id: string
  offset: number
  version: string | null
  length?: number
}

export interface SearchArgs {
  q: string
  k: number
  ip: string
}

export interface CatalogArgs {
  q?: string
  section?: string
  offset?: number
  limit?: number
  version?: string | null
}

const SITE = 'https://vinnik-dmitry07.github.io/favorite-papers'
export const CONTENT_MAX = 32000
export const FETCH_PART_SIZE = 16000


function contentsOf(text: string) {
  const result: { title: string, level: number, offset: number }[] = []
  const pattern = /^(#{1,6})\s+(.+)$/gm
  for (const match of text.matchAll(pattern)) {
    result.push({ title: match[2].trim(), level: match[1].length,
      offset: pointLength(text.slice(0, match.index)) })
  }
  return result
}

interface FetchIdentity { paper: string, version: string, start: number | null }

function fetchId(identity: FetchIdentity): string {
  const bytes = new TextEncoder().encode(JSON.stringify(identity))
  return 'doc:' + btoa(Array.from(bytes, (b) => String.fromCharCode(b)).join(''))
    .replaceAll('+', '-').replaceAll('/', '_').replaceAll('=', '')
}

function parseFetchId(id: string): FetchIdentity {
  try {
    if (!id.startsWith('doc:') || id.length > 4096) throw new Error('id')
    const binary = atob(id.slice(4).replaceAll('-', '+').replaceAll('_', '/'))
    const data = JSON.parse(new TextDecoder().decode(Uint8Array.from(binary, (c) => c.charCodeAt(0))))
    if (typeof data.paper !== 'string' || typeof data.version !== 'string'
        || !(data.start === null || (Number.isSafeInteger(data.start) && data.start >= 0))) {
      throw new Error('shape')
    }
    return data as FetchIdentity
  } catch {
    fail('invalid_argument', 400, 'fetch id must be copied unchanged from search results')
  }
}

interface Neighbor {
  id: string
  evidence: { direction: 'out' | 'in', evidence: string }[]
}

interface CursorPayload {
  direction: string
  paper: string
  position: number
  version: string
}

function summaryTitle(title: string): string {
  return slicePoints(title, 0, embed.limits.summary_title_code_points)
}

function missingCard(id: string): NodeCard {
  return {
    id,
    title: '',
    text: { available: false, reason: 'no_markdown', code_points: 0, chunks: 0 },
  }
}

function nodeSummary(node: NodeCard) {
  return {
    id: node.id,
    title: summaryTitle(node.title ?? ''),
    url: node.url ?? null,
    date: node.date ?? null,
    section: node.section ?? null,
  }
}

function neighborsOf(
  graph: { out: Record<string, { target: string, evidence: string }[]>, in: Record<string, { source: string, evidence: string }[]> },
  id: string,
  dir: 'out' | 'in' | 'both',
): Neighbor[] {
  const ordered: Neighbor[] = []
  const byId = new Map<string, Neighbor>()
  const add = (neighborId: string, direction: 'out' | 'in', evidence: string) => {
    let row = byId.get(neighborId)
    if (!row) {
      row = { id: neighborId, evidence: [] }
      byId.set(neighborId, row)
      ordered.push(row)
    }
    row.evidence.push({ direction, evidence })
  }
  if (dir === 'out' || dir === 'both') {
    for (const edge of graph.out[id] ?? []) {
      add(edge.target, 'out', edge.evidence)
    }
  }
  if (dir === 'in' || dir === 'both') {
    for (const edge of graph.in[id] ?? []) {
      add(edge.source, 'in', edge.evidence)
    }
  }
  return ordered
}

function encodeCursor(payload: CursorPayload): string {
  const bytes = new TextEncoder().encode(canonicalJson(payload))
  let binary = ''
  for (const byte of bytes) {
    binary += String.fromCharCode(byte)
  }
  return btoa(binary).replaceAll('+', '-').replaceAll('/', '_').replaceAll('=', '')
}

function decodeCursor(cursor: string): CursorPayload {
  if (!cursor || cursor.includes('=')) {
    fail('invalid_cursor', 400, 'cursor is not valid')
  }
  let padded = cursor.replaceAll('-', '+').replaceAll('_', '/')
  while (padded.length % 4) {
    padded += '='
  }
  let json = ''
  try {
    const binary = atob(padded)
    const bytes = Uint8Array.from(binary, (char) => char.charCodeAt(0))
    json = new TextDecoder().decode(bytes)
  } catch {
    fail('invalid_cursor', 400, 'cursor is not valid')
  }
  let parsed: unknown
  try {
    parsed = JSON.parse(json)
  } catch {
    fail('invalid_cursor', 400, 'cursor is not valid')
  }
  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
    fail('invalid_cursor', 400, 'cursor is not valid')
  }
  const row = parsed as Record<string, unknown>
  const keys = Object.keys(row).sort()
  if (keys.join(',') !== 'direction,paper,position,version') {
    fail('invalid_cursor', 400, 'cursor is not valid')
  }
  if (
    (row.direction !== 'out' && row.direction !== 'in' && row.direction !== 'both')
    || typeof row.paper !== 'string'
    || typeof row.version !== 'string'
    || typeof row.position !== 'number'
    || !Number.isInteger(row.position)
    || row.position < 0
  ) {
    fail('invalid_cursor', 400, 'cursor is not valid')
  }
  return {
    direction: row.direction,
    paper: row.paper,
    position: row.position,
    version: row.version,
  }
}

type SearchHit = {
  paper_id: string
  title: string
  url: string | null
  chunk_index: number
  score: number
  snippet: string
  start: number
  end: number
  corpus_version: string
  content: string
}

type SearchBody = {
  corpus_version: string
  k: number
  hits: SearchHit[]
  metadata_hits: ReturnType<typeof nodeSummary>[]
}

function byteLength(value: unknown): number {
  return new TextEncoder().encode(JSON.stringify(value)).length
}

export function createService(
  store: CorpusStore,
  tokenizer: WordPieceTokenizer,
  options: { searchEnabled?: boolean } = {},
) {
  const searchEnabled = options.searchEnabled ?? embed.search_enabled
  const corpus = new CorpusCache(store)
  const searchCache = new Map<string, SearchBody>()
  let localSignatures: { build: string, embedding: string } | null = null

  async function sigs() {
    if (!localSignatures) {
      localSignatures = await signatures()
    }
    return localSignatures
  }

  function checkDeadline(started: number) {
    if (store.now() - started > embed.limits.deadline_seconds * 1000) {
      fail('deadline_exceeded', 503, 'request deadline exceeded')
    }
  }

  function finish<T>(started: number, body: T): T {
    checkDeadline(started)
    if (byteLength(body) > embed.limits.response_bytes_max) {
      fail('response_too_large', 503, 'response exceeds the size cap')
    }
    return body
  }

  async function requirePointer(started: number) {
    checkDeadline(started)
    const pointer = await corpus.pointerAt(store.now())
    if (pointer.reader_schema !== embed.reader_schema) {
      fail('config_mismatch', 503, 'reader schema does not match this worker', {
        expected: embed.reader_schema,
        actual: pointer.reader_schema,
      })
    }
    return pointer
  }

  async function requireGraph(started: number) {
    const pointer = await requirePointer(started)
    const graph = await corpus.graph(pointer.release_id)
    return { pointer, graph }
  }

  function requireNode(graph: { nodes: Record<string, NodeCard> }, id: string): NodeCard {
    const node = graph.nodes[id]
    if (!node) {
      fail('unknown_id', 404, 'catalog id was not found', { id })
    }
    return node
  }

  return {
    async catalog(args: CatalogArgs = {}) {
      const started = store.now()
      const { pointer, graph } = await requireGraph(started)
      if (args.version && args.version !== pointer.release_id) {
        fail('version_conflict', 409, 'catalog version changed; restart at offset 0', {
          corpus_version: pointer.release_id,
        })
      }
      const query = args.q ?? ''
      if (pointLength(query) > embed.limits.query_code_points_max) {
        fail('query_too_long', 400, 'catalog query is too long')
      }
      const offset = parseOffset(args.offset)
      const limit = parseBoundedInt(args.limit, 12, 1, 24, 'limit')
      const rows = rankedCatalog(graph.nodes, query, args.section)
      if (offset > rows.length) fail('invalid_offset', 400, 'offset is past the catalog result')
      const end = Math.min(rows.length, offset + limit)
      return finish(started, {
        corpus_version: pointer.release_id,
        total: rows.length,
        papers: rows.slice(offset, end).map(({ node, score }) => ({
          ...nodeSummary(node), quality: node.quality ?? null,
          text_available: node.text.available, match: score === 100 ? 'exact' : 'keyword',
        })),
        next_offset: end < rows.length ? end : null,
      })
    },

    async contents(id: string, version?: string | null) {
      const started = store.now()
      const { pointer, graph } = await requireGraph(started)
      if (version && version !== pointer.release_id) fail('version_conflict', 409, 'corpus version changed')
      const node = requireNode(graph, parseId(id))
      const doc = node.text.available ? await corpus.paper(pointer.release_id, node.id) : null
      return finish(started, {
        corpus_version: pointer.release_id, paper_id: node.id,
        available: node.text.available, reason: node.text.reason,
        total_length: doc ? pointLength(doc.text) : 0,
        sections: doc ? contentsOf(doc.text) : [],
      })
    },

    async find(args: { id: string, q: string, offset?: number, version?: string | null }) {
      const started = store.now()
      const { pointer, graph } = await requireGraph(started)
      if (args.version && args.version !== pointer.release_id) fail('version_conflict', 409, 'corpus version changed')
      const node = requireNode(graph, parseId(args.id))
      if (!args.q.trim() || pointLength(args.q) > 200) fail('invalid_query', 400, 'find query must be 1..200 code points')
      const offset = parseOffset(args.offset)
      const text = node.text.available ? (await corpus.paper(pointer.release_id, node.id)).text : ''
      const points = Array.from(text)
      if (offset > points.length) fail('invalid_offset', 400, 'offset is past the text')
      // RegExp indices refer to the original string, including case-folding expansions.
      const pattern = new RegExp(args.q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'giu')
      pattern.lastIndex = points.slice(0, offset).join('').length
      const matches = []
      let next: number | null = null
      for (let match = pattern.exec(text); match; match = pattern.exec(text)) {
        const start = pointLength(text.slice(0, match.index))
        const end = start + pointLength(match[0])
        if (matches.length === 12) { next = start; break }
        matches.push({ start, end, snippet: points.slice(Math.max(0, start - 120), end + 360).join('') })
      }
      return finish(started, { corpus_version: pointer.release_id, paper_id: node.id,
        available: node.text.available, matches, next_offset: next })
    },

    async fetchDocument(id: string) {
      const started = store.now()
      const identity = parseFetchId(id)
      const { pointer, graph } = await requireGraph(started)
      if (identity.version !== pointer.release_id) {
        fail('version_conflict', 409, 'search again to fetch this item from the current corpus')
      }
      const node = requireNode(graph, parseId(identity.paper))
      const url = `${SITE}/agents/papers/${await sha256Hex(node.id)}/`
      if (identity.start === null) {
        const text = `${node.title}\nCatalog id: ${node.id}\nSection: ${node.section ?? ''}\n`
          + `Date: ${node.date ?? 'unknown'}\nFull text available: ${node.text.available}\n`
          + `Original source: ${node.url ?? ''}\nRead text and all citation links: ${url}`
        return finish(started, { id, title: `${node.title} (catalog record)`, text, url,
          metadata: { paper_id: node.id, corpus_version: pointer.release_id, item_type: 'catalog',
            text_available: node.text.available,
            first_text_id: node.text.available ? fetchId({ ...identity, start: 0 }) : null } })
      }
      if (!node.text.available) fail('invalid_argument', 400, 'this record has no stored paper text')
      const doc = await corpus.paper(pointer.release_id, node.id)
      const total = pointLength(doc.text)
      if (identity.start >= total || identity.start % FETCH_PART_SIZE !== 0) {
        fail('invalid_offset', 400, 'fetch part is outside the document')
      }
      const end = Math.min(total, identity.start + FETCH_PART_SIZE)
      return finish(started, {
        id, title: `${node.title} (text part ${identity.start / FETCH_PART_SIZE + 1})`,
        text: slicePoints(doc.text, identity.start, end), url: node.url || url,
        metadata: { paper_id: node.id, corpus_version: pointer.release_id, item_type: 'text_part',
          start: identity.start, end, total_length: total, paper_url: url,
          next_id: end < total ? fetchId({ ...identity, start: end }) : null,
          previous_id: identity.start > 0 ? fetchId({ ...identity, start: identity.start - FETCH_PART_SIZE }) : null },
      })
    },

    async researchSearch(query: string, ip: string) {
      const started = store.now()
      const q = validateQuery(query, tokenizer)
      const { pointer, graph } = await requireGraph(started)
      const candidates = rankedCatalog(graph.nodes, q)
      const exact = candidates.filter(({ score }) => score === 100)
      if (exact.length) {
        return finish(started, { results: await Promise.all(exact.slice(0, 8).map(async ({ node }) => ({
          id: fetchId({ paper: node.id, version: pointer.release_id, start: node.text.available ? 0 : null }),
          title: `${node.title} (${node.text.available ? 'text part 1' : 'catalog record'})`,
          url: node.text.available && node.url ? node.url : `${SITE}/agents/papers/${await sha256Hex(node.id)}/`,
        }))) })
      }
      const passages = await this.search({ q, k: 5, ip })
      if (passages.corpus_version !== pointer.release_id) {
        fail('version_conflict', 409, 'corpus changed during search; retry')
      }
      const results = await Promise.all(candidates.slice(0, 3).map(async ({ node }) => ({
        id: fetchId({ paper: node.id, version: pointer.release_id, start: null }),
        title: `${node.title} (catalog record)`,
        url: `${SITE}/agents/papers/${await sha256Hex(node.id)}/`,
      })))
      for (const hit of passages.hits) {
        const start = Math.floor(hit.start / FETCH_PART_SIZE) * FETCH_PART_SIZE
        results.push({ id: fetchId({ paper: hit.paper_id, version: pointer.release_id, start }),
          title: `${hit.title} (text part ${start / FETCH_PART_SIZE + 1})`,
          url: hit.url || `${SITE}/agents/papers/${await sha256Hex(hit.paper_id)}/` })
      }
      return finish(started, { results })
    },

    async health() {
      const local = await sigs()
      const base = {
        reader_schema: embed.reader_schema,
        model: embed.model,
        pooling: embed.pooling,
        dimensions: embed.dimensions,
        build_signature: local.build,
        embedding_signature: local.embedding,
        search_enabled: searchEnabled,
        grace_seconds: embed.limits.grace_seconds,
      }
      let pointer
      try {
        pointer = await corpus.pointerAt(store.now())
      } catch (error) {
        const code = error instanceof DomainError ? error.code : 'corpus_unavailable'
        return {
          ...base,
          status: 'unavailable',
          error: code,
          release_id: null,
          slot: null,
          verified_passage_count: null,
          global_index_count: null,
          publication_check: null,
        }
      }
      const mismatch = (
        pointer.build_signature !== local.build
        || pointer.embedding_signature !== local.embedding
        || pointer.reader_schema !== embed.reader_schema
        || pointer.publication_check?.ok !== true
      )
      return {
        ...base,
        status: mismatch ? 'degraded' : 'ready',
        release_id: pointer.release_id,
        slot: pointer.slot,
        verified_passage_count: pointer.verified_passage_count,
        global_index_count: pointer.global_index_count,
        publication_check: pointer.publication_check,
        published_build_signature: pointer.build_signature,
        published_embedding_signature: pointer.embedding_signature,
      }
    },

    async paper(id: string) {
      const started = store.now()
      const paperId = parseId(id)
      const { pointer, graph } = await requireGraph(started)
      const node = requireNode(graph, paperId)
      const authors = (node.authors ?? []).filter((author) => typeof author === 'string')
      const shown = authors.slice(0, embed.limits.authors)
      return finish(started, {
        corpus_version: pointer.release_id,
        id: node.id,
        title: node.title,
        authors: shown,
        authors_total: authors.length,
        authors_truncated: authors.length > shown.length,
        date: node.date ?? null,
        section: node.section ?? null,
        topic: node.topic ?? null,
        kind: node.kind ?? null,
        url: node.url ?? null,
        quality: node.quality ?? null,
        quality_conf: node.quality_conf ?? null,
        quality_verdict: node.quality_verdict ?? null,
        quality_accepts: node.quality_accepts ?? null,
        quality_models: node.quality_models ?? null,
        text: {
          available: node.text.available,
          reason: node.text.available ? null : node.text.reason,
          code_points: node.text.code_points,
          chunks: node.text.chunks,
        },
      })
    },

    async citations(args: CitationArgs) {
      const started = store.now()
      const paperId = parseId(args.id)
      const pointer = await requirePointer(started)
      let position = 0
      if (args.cursor) {
        const decoded = decodeCursor(args.cursor)
        if (decoded.version !== pointer.release_id) {
          fail('version_conflict', 409, 'cursor is for a different corpus version', {
            corpus_version: pointer.release_id,
          })
        }
        if (decoded.paper !== paperId || decoded.direction !== args.dir) {
          fail('invalid_cursor', 400, 'cursor does not match this query')
        }
        position = decoded.position
      }
      const graph = await corpus.graph(pointer.release_id)
      requireNode(graph, paperId)
      const neighbors = neighborsOf(graph, paperId, args.dir)
      if (position > neighbors.length) {
        fail('invalid_cursor', 400, 'cursor position is past the end')
      }
      const page = neighbors.slice(position, position + args.limit)
      const next = position + page.length
      const truncated = next < neighbors.length
      return finish(started, {
        corpus_version: pointer.release_id,
        paper_id: paperId,
        direction: args.dir,
        total: neighbors.length,
        truncated,
        neighbors: page.map((neighbor) => ({
          ...nodeSummary(graph.nodes[neighbor.id] ?? missingCard(neighbor.id)),
          evidence: neighbor.evidence,
        })),
        next_cursor: truncated
          ? encodeCursor({
            direction: args.dir,
            paper: paperId,
            position: next,
            version: pointer.release_id,
          })
          : null,
      })
    },

    async traverse(args: TraverseArgs) {
      const started = store.now()
      const paperId = parseId(args.id)
      const { pointer, graph } = await requireGraph(started)
      requireNode(graph, paperId)
      const maxNodes = parseBoundedInt(args.max_nodes, embed.limits.traverse_nodes_max, 2, 100, 'max_nodes')
      const nodes = [{ ...nodeSummary(graph.nodes[paperId]), depth: 0 }]
      const treeEdges: { parent: string, child: string,
        citations: { source: string, target: string, evidence: string }[] }[] = []
      const visited = new Set<string>([paperId])
      const queue: { id: string, depth: number }[] = [{ id: paperId, depth: 0 }]
      let truncated = false
      let reason: string | null = null
      let index = 0
      while (index < queue.length && !truncated) {
        const current = queue[index]
        index += 1
        if (current.depth >= args.hops) {
          continue
        }
        for (const neighbor of neighborsOf(graph, current.id, args.dir)) {
          if (visited.has(neighbor.id)) {
            continue
          }
          if (nodes.length >= maxNodes || treeEdges.length >= maxNodes - 1) {
            truncated = true
            reason = 'node_cap'
            break
          }
          visited.add(neighbor.id)
          const card = graph.nodes[neighbor.id] ?? missingCard(neighbor.id)
          nodes.push({
            ...nodeSummary(card),
            depth: current.depth + 1,
          })
          treeEdges.push({
            parent: current.id,
            child: neighbor.id,
            citations: neighbor.evidence.map(({ direction, evidence }) => ({
              source: direction === 'out' ? current.id : neighbor.id,
              target: direction === 'out' ? neighbor.id : current.id,
              evidence,
            })),
          })
          queue.push({ id: neighbor.id, depth: current.depth + 1 })
        }
      }
      return finish(started, {
        corpus_version: pointer.release_id,
        seed: paperId,
        direction: args.dir,
        hops: args.hops,
        truncated,
        reason,
        nodes,
        tree_edges: treeEdges,
        edges: [...visited].flatMap((source) => (graph.out[source] ?? [])
          .filter((edge) => visited.has(edge.target)).map((edge) => ({ source, ...edge }))),
        continuation: truncated ? {
          method: 'citations', id: queue[index - 1].id, dir: args.dir,
          instruction: 'Page citations with next_cursor to recover omitted neighbors; repeat for each frontier node.',
          frontier: queue.slice(index - 1).filter((item) => item.depth < args.hops).map((item) => item.id),
        } : null,
      })
    },

    async content(args: ContentArgs) {
      const started = store.now()
      const paperId = parseId(args.id)
      parseOffset(args.offset)
      const length = parseBoundedInt(args.length, embed.limits.content_code_points, 1, CONTENT_MAX, 'length')
      const pointer = await requirePointer(started)
      if (args.version && args.version !== pointer.release_id) {
        fail('version_conflict', 409, 'version does not match the active corpus', {
          corpus_version: pointer.release_id,
        })
      }
      const graph = await corpus.graph(pointer.release_id)
      const node = requireNode(graph, paperId)
      if (!node.text.available) {
        return finish(started, {
          corpus_version: pointer.release_id,
          paper_id: paperId,
          available: false,
          reason: node.text.reason,
          offset: 0,
          next_offset: null,
          total_length: 0,
          text: '',
        })
      }
      const doc = await corpus.paper(pointer.release_id, paperId)
      const total = pointLength(doc.text)
      if (args.offset > total) {
        fail('invalid_offset', 400, 'offset is past the end', { total_length: total })
      }
      if (args.offset === total) {
        return finish(started, {
          corpus_version: pointer.release_id,
          paper_id: paperId,
          available: true,
          reason: null,
          offset: args.offset,
          next_offset: null,
          total_length: total,
          text: '',
        })
      }
      const end = Math.min(total, args.offset + length)
      return finish(started, {
        corpus_version: pointer.release_id,
        paper_id: paperId,
        available: true,
        reason: null,
        offset: args.offset,
        next_offset: end < total ? end : null,
        total_length: total,
        text: slicePoints(doc.text, args.offset, end),
      })
    },

    async search(args: SearchArgs) {
      const started = store.now()
      const query = validateQuery(args.q, tokenizer)
      if (!Number.isInteger(args.k) || args.k < 1 || args.k > embed.limits.search_k_max) {
        fail('invalid_argument', 400, 'k is outside the allowed range', { field: 'k' })
      }
      const { pointer, graph } = await requireGraph(started)
      const local = await sigs()
      if (
        pointer.embedding_signature !== local.embedding
        || pointer.build_signature !== local.build
        || pointer.publication_check?.ok !== true
      ) {
        fail('config_mismatch', 503, 'published corpus does not match this worker')
      }
      if (!searchEnabled) {
        fail('search_disabled', 503, 'search is disabled')
      }
      const cacheKey = [
        pointer.release_id,
        local.embedding,
        query,
        String(args.k),
      ].join('\n')
      const cached = searchCache.get(cacheKey)
      if (cached) {
        searchCache.delete(cacheKey)
        searchCache.set(cacheKey, cached)
        return finish(started, cached)
      }
      const allowed = await store.rateLimit(args.ip || 'unknown')
      if (!allowed) {
        fail('rate_limited', 429, 'uncached semantic search rate limit exceeded; retry after 60 seconds', { retry_after: 60 })
      }
      checkDeadline(started)
      const vector = await store.embed(embed.query_template ? embed.query_template + query : query)
      checkDeadline(started)
      if (
        !Array.isArray(vector)
        || vector.length !== embed.dimensions
        || vector.some((value) => typeof value !== 'number' || !Number.isFinite(value))
      ) {
        fail('config_mismatch', 503, 'embedding dimension or pooling did not match')
      }
      // Oversample to prevent overlapping chunks from one paper filling the page.
      const hits = await store.query(pointer.slot, vector, Math.min(40, args.k * 5))
      checkDeadline(started)
      const confirmed = await corpus.confirmed(pointer.slot, pointer.release_id)
      if (
        confirmed.release_id !== pointer.release_id
        || confirmed.embedding_signature !== pointer.embedding_signature
      ) {
        fail('config_mismatch', 503, 'vector map does not match the active release')
      }
      const rows = []
      const seenPapers = new Set<string>()
      for (const hit of hits) {
        const mapped = confirmed.vectors[hit.id]
        if (!mapped || !Number.isFinite(hit.score)) {
          fail('dangling_hit', 503, 'search hit is not in the active vector map', { id: hit.id })
        }
        if (seenPapers.has(mapped.paper_id)) continue
        const doc = await corpus.paper(pointer.release_id, mapped.paper_id)
        const chunk = doc.chunks.find((item) => item.index === mapped.chunk_index)
        if (!chunk || chunk.content_hash !== mapped.content_hash) {
          fail('dangling_hit', 503, 'search hit does not match the stored passage', { id: hit.id })
        }
        const passage = slicePoints(doc.text, chunk.start, chunk.end)
        const node = graph.nodes[mapped.paper_id]
        const params = new URLSearchParams({
          id: mapped.paper_id,
          offset: String(chunk.start),
          version: pointer.release_id,
        })
        rows.push({
          paper_id: mapped.paper_id,
          title: summaryTitle(node?.title ?? ''),
          url: node?.url ?? null,
          chunk_index: mapped.chunk_index,
          score: hit.score,
          // Cached String.slice views can retain an entire evicted paper in V8.
          // Joining this bounded code-point array creates independent snippet
          // storage while preserving astral characters and lone surrogates.
          snippet: Array.from(slicePoints(passage, 0, embed.limits.snippet_code_points)).join(''),
          start: chunk.start,
          end: chunk.end,
          corpus_version: pointer.release_id,
          content: `/v1/content?${params.toString()}`,
        })
        seenPapers.add(mapped.paper_id)
        if (rows.length >= args.k) break
      }
      const body = {
        corpus_version: pointer.release_id,
        k: args.k,
        hits: rows,
        metadata_hits: rankedCatalog(graph.nodes, query).slice(0, args.k)
          .map(({ node }) => ({ ...nodeSummary(node), text_available: node.text.available })),
      }
      searchCache.set(cacheKey, body)
      while (searchCache.size > embed.limits.search_cache_entries) {
        const oldest = searchCache.keys().next().value
        if (!oldest) {
          break
        }
        searchCache.delete(oldest)
      }
      return finish(started, body)
    },
  }
}

function validateQuery(q: unknown, tokenizer: WordPieceTokenizer): string {
  if (typeof q !== 'string' || q.trim() === '') {
    fail('invalid_query', 400, 'query is empty', { field: 'q' })
  }
  if (pointLength(q) > embed.limits.query_code_points_max) {
    fail('query_too_long', 400, 'query exceeds the code-point cap', { field: 'q' })
  }
  const ids = tokenizer.tokenIds(embed.query_template, q)
  if (ids.length > embed.max_input_tokens) {
    fail('query_too_long', 400, 'query exceeds the token budget', { field: 'q' })
  }
  return q
}

export type Service = ReturnType<typeof createService>
