import { fail } from './schemas'
import { sha256Hex } from './signatures'
import { embed } from './tokenize'

export interface ActivePointer {
  release_id: string
  slot: string
  activated_at: number
  reader_schema: number
  embedding_signature: string
  build_signature: string
  verified_passage_count: number
  global_index_count: number | null
  publication_check: { ok: boolean, checked_at: number, by: string }
}

export interface NodeCard {
  id: string
  title: string
  authors?: string[]
  date?: string | null
  section?: string | null
  topic?: string | null
  kind?: string | null
  url?: string | null
  quality?: number | null
  quality_conf?: number | null
  quality_verdict?: string | null
  quality_accepts?: number | null
  quality_models?: number | null
  text: {
    available: boolean
    reason: string | null
    code_points: number
    chunks: number
    object?: string
  }
}

export interface GraphDoc {
  nodes: Record<string, NodeCard>
  out: Record<string, { target: string, evidence: string }[]>
  in: Record<string, { source: string, evidence: string }[]>
}

export interface PaperDoc {
  paper_id: string
  text: string
  chunks: {
    index: number
    start: number
    end: number
    token_count: number
    content_hash: string
    input_hash: string
  }[]
}

export interface ConfirmedDoc {
  release_id: string
  embedding_signature: string
  build_signature: string
  passage_count: number
  vectors: Record<string, {
    paper_id: string
    chunk_index: number
    content_hash: string
    input_hash: string
  }>
}

export interface VectorHit {
  id: string
  score: number
  metadata?: Record<string, unknown>
}

export interface CorpusStore {
  now(): number
  getJson(key: string): Promise<unknown | null>
  embed(text: string): Promise<number[]>
  query(namespace: string, vector: number[], topK: number): Promise<VectorHit[]>
  rateLimit(key: string): Promise<boolean>
}

interface CacheEntry<T> {
  at: number
  value: T
}

export class CorpusCache {
  private pointer: CacheEntry<ActivePointer> | null = null
  private readonly graphs = new Map<string, GraphDoc>()
  private readonly confirmedDocs = new Map<string, ConfirmedDoc>()
  private readonly papers = new Map<string, { bytes: number, doc: PaperDoc }>()
  private paperBytes = 0

  constructor(readonly store: CorpusStore) {}

  async pointerAt(now: number): Promise<ActivePointer> {
    const ttl = embed.limits.pointer_ttl_seconds * 1000
    if (this.pointer && now - this.pointer.at <= ttl) {
      return this.pointer.value
    }
    this.pointer = null
    let raw: unknown
    try {
      raw = await this.store.getJson('active.json')
    } catch {
      fail('corpus_unavailable', 503, 'active pointer could not be read')
    }
    if (!raw) {
      fail('not_ready', 503, 'no active corpus')
    }
    const pointer = raw as ActivePointer
    this.pointer = { at: now, value: pointer }
    return pointer
  }

  async graph(releaseId: string): Promise<GraphDoc> {
    const cached = this.graphs.get(releaseId)
    if (cached) {
      return cached
    }
    const raw = await this.read(`releases/${releaseId}/graph.json`)
    if (!raw) {
      fail('corpus_unavailable', 503, 'release graph is missing', { release_id: releaseId })
    }
    const doc = raw as GraphDoc
    this.remember(this.graphs, releaseId, doc, 2)
    return doc
  }

  async paper(releaseId: string, paperId: string): Promise<PaperDoc> {
    const cacheKey = `${releaseId}:${paperId}`
    const cached = this.papers.get(cacheKey)
    if (cached) {
      this.papers.delete(cacheKey)
      this.papers.set(cacheKey, cached)
      return cached.doc
    }
    const hash = await sha256Hex(paperId)
    const raw = await this.read(`releases/${releaseId}/papers/${hash}.json`)
    if (!raw) {
      fail('corpus_unavailable', 503, 'paper text is missing', { id: paperId })
    }
    const doc = raw as PaperDoc
    const bytes = new TextEncoder().encode(doc.text).length
    this.papers.set(cacheKey, { bytes, doc })
    this.paperBytes += bytes
    while (
      this.papers.size > embed.limits.paper_cache_entries
      || this.paperBytes > embed.limits.paper_cache_bytes
    ) {
      const oldest = this.papers.keys().next().value
      if (!oldest) {
        break
      }
      const entry = this.papers.get(oldest)
      this.papers.delete(oldest)
      this.paperBytes -= entry?.bytes ?? 0
      if (oldest === cacheKey) {
        break
      }
    }
    return doc
  }

  async confirmed(slot: string, releaseId: string): Promise<ConfirmedDoc> {
    const cacheKey = `${slot}:${releaseId}`
    const cached = this.confirmedDocs.get(cacheKey)
    if (cached) {
      return cached
    }
    const raw = await this.read(`slots/${slot}/confirmed.json`)
    if (!raw) {
      fail('corpus_unavailable', 503, 'vector map is missing', { slot })
    }
    const doc = raw as ConfirmedDoc
    this.remember(this.confirmedDocs, cacheKey, doc, 2)
    return doc
  }

  private remember<K, V>(map: Map<K, V>, key: K, value: V, cap: number): void {
    map.set(key, value)
    if (map.size <= cap) {
      return
    }
    const oldest = map.keys().next().value
    if (oldest !== undefined) {
      map.delete(oldest)
    }
  }

  private async read(key: string): Promise<unknown | null> {
    try {
      return await this.store.getJson(key)
    } catch {
      fail('corpus_unavailable', 503, 'corpus object could not be read', { key })
    }
  }
}
