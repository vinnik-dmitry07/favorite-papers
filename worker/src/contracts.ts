import { z } from 'zod'
import { embed } from './tokenize'

const nullableText = z.string().nullable()
const offset = z.number().int().nonnegative()
const version = z.string().describe('corpus_version from the previous response. On version_conflict restart the query.')
const id = z.string().min(1).max(512).describe('Exact case-sensitive catalog ID, e.g. arxiv:2402.03300 or doi:10.1038/s41586-023-06924-6. Use list_papers to resolve a title or URL.')
const dir = z.enum(['out', 'in', 'both']).default('out')
  .describe('out = papers this paper cites; in = papers citing it; both = both directions. Only within this catalog.')
const summary = z.object({ id: z.string(), title: z.string(), url: nullableText,
  date: nullableText, section: nullableText })
const edge = z.object({ source: z.string(), target: z.string(), evidence: z.string() })
const evidence = z.object({ direction: z.enum(['out', 'in']), evidence: z.string() })
const textInfo = z.object({ available: z.boolean(), reason: nullableText,
  code_points: offset, chunks: offset })

export const inputs = {
  search: z.object({ query: z.string().min(1).max(2000).describe('Natural-language question, exact paper title, URL, or catalog ID. English works best with the current embedding model.') }),
  fetch: z.object({ id: z.string().min(1).max(4096).describe('Opaque id copied unchanged from search, or metadata.next_id from fetch. Each text part is a complete independently fetchable item.') }),
  paper: z.object({ id }),
  catalog: z.object({
    q: z.string().max(2000).default('').describe('Title, ID, URL, or keywords; empty lists every record, including records without text.'),
    section: z.string().optional().describe('Exact catalog section name.'),
    offset: offset.default(0), limit: z.number().int().min(1).max(24).default(12),
    version: version.optional(),
  }),
  citations: z.object({ id, dir,
    limit: z.number().int().min(1).max(24).default(12),
    cursor: z.string().optional().describe('Copy next_cursor unchanged until null. Do not infer total citations from one page.'),
  }),
  traverse: z.object({ id, dir, hops: z.number().int().min(1).max(2).default(1),
    max_nodes: z.number().int().min(2).max(100).default(24)
      .describe('Includes the seed. On truncation follow continuation with paginated citations.'),
  }),
  content: z.object({ id, offset: offset.default(0).describe('Unicode code-point offset, not bytes or UTF-16.'),
    length: z.number().int().min(1).max(32000).default(6000), version: version.optional(),
  }),
  contents: z.object({ id, version: version.optional() }),
  find: z.object({ id, q: z.string().min(1).max(200).describe('Literal case-insensitive text, not a regular expression or semantic query.'),
    offset: offset.default(0), version: version.optional(),
  }),
  passages: z.object({ q: z.string().min(1).max(2000),
    k: z.number().int().min(1).max(embed.limits.search_k_max).default(5),
  }),
}

export const outputs = {
  search: z.object({ results: z.array(z.object({ id: z.string(), title: z.string(), url: z.string() })) }),
  fetch: z.object({ id: z.string(), title: z.string(), text: z.string(), url: z.string(),
    metadata: z.record(z.string(), z.unknown()) }),
  paper: summary.extend({ corpus_version: z.string(), authors: z.array(z.string()),
    authors_total: offset, authors_truncated: z.boolean(), topic: nullableText, kind: nullableText,
    quality: z.number().nullable(), quality_conf: z.number().nullable(), quality_verdict: nullableText,
    quality_accepts: z.number().nullable(), quality_models: z.number().nullable(), text: textInfo }),
  catalog: z.object({ corpus_version: z.string(), total: offset, next_offset: offset.nullable(),
    papers: z.array(summary.extend({ quality: z.number().nullable(), text_available: z.boolean(),
      match: z.enum(['exact', 'keyword']) })) }),
  citations: z.object({ corpus_version: z.string(), paper_id: z.string(), direction: z.string(),
    total: offset, truncated: z.boolean(), next_cursor: nullableText,
    neighbors: z.array(summary.extend({ evidence: z.array(evidence) })) }),
  traverse: z.object({ corpus_version: z.string(), seed: z.string(), direction: z.string(),
    hops: offset, truncated: z.boolean(), reason: nullableText,
    nodes: z.array(summary.extend({ depth: offset })), edges: z.array(edge),
    tree_edges: z.array(z.object({ parent: z.string(), child: z.string(), citations: z.array(edge) })),
    continuation: z.object({ method: z.string(), id: z.string(), dir: z.string(),
      instruction: z.string(), frontier: z.array(z.string()) }).nullable(),
  }),
  content: z.object({ corpus_version: z.string(), paper_id: z.string(), available: z.boolean(),
    reason: nullableText, offset, next_offset: offset.nullable(), total_length: offset, text: z.string() }),
  contents: z.object({ corpus_version: z.string(), paper_id: z.string(), available: z.boolean(),
    reason: nullableText, total_length: offset,
    sections: z.array(z.object({ title: z.string(), level: offset, offset })) }),
  find: z.object({ corpus_version: z.string(), paper_id: z.string(), available: z.boolean(),
    next_offset: offset.nullable(), matches: z.array(z.object({ start: offset, end: offset, snippet: z.string() })) }),
  passages: z.object({ corpus_version: z.string(), k: offset,
    metadata_hits: z.array(summary.extend({ text_available: z.boolean() })),
    hits: z.array(z.object({ paper_id: z.string(), title: z.string(), url: nullableText,
      chunk_index: offset, score: z.number(), snippet: z.string(), start: offset, end: offset,
      corpus_version: z.string(), content: z.string() })),
  }),
}

export const descriptions = {
  search: 'Find papers by exact title/URL/ID or semantic passage search. Returns citable items for fetch. A catalog record is metadata; a text part contains at most 16000 code points. Search includes keyword matches for records without full text.',
  fetch: 'Fetch the complete item returned by search. Text parts include next_id/previous_id to read more. Catalog records state text availability and link to the static paper page. A version conflict requires a new search.',
  paper: 'Read a paper card, source URL, quality fields, and text availability. IDs come from list_papers; never guess them.',
  catalog: 'Resolve titles, source URLs, or IDs and browse all catalog entries without embeddings. Includes records without full text. Follow next_offset with version=corpus_version until null.',
  citations: 'Page ALL citation neighbors within the catalog. out means this paper cites the neighbor; in means the neighbor cites this paper. Preserve every evidence direction. title is weaker evidence than id. Follow next_cursor until null.',
  traverse: 'Explore at most two citation hops. edges preserve actual citation direction, including cycles. tree_edges use parent/child for discovery and citations for real edges. If truncated, use continuation and paginated citations.',
  content: 'Read cleaned paper text, preserving case, math source and appendices. Bibliography is omitted; the static paper page links source Markdown. Follow next_offset with version=corpus_version. length can be raised to 32000.',
  contents: 'Get section headings with Unicode code-point offsets; use read_content at a heading offset and preserve corpus_version.',
  find: 'Find literal text within one paper and return context and exact code-point offsets. Follow next_offset for more matches. No embedding call.',
  passages: 'Semantic passage search plus separate keyword metadata matches across the entire catalog. At most one passage per paper after bounded oversampling; results can be fewer than k. Score is similarity, not probability. English embedding model; non-English quality is not established.',
}
