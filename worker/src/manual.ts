export const manual = `Key papers agent API

Start with GET /v1/catalog?q=DeepSeekMath to resolve a title, source URL or ID.
An empty q lists every record, including records without full text.
Copy ids verbatim: arxiv:2402.03300, doi:10.1038/s41586-023-06924-6,
openreview:, acl:, or url:. Case matters. URL-encode query parameters once.

An edge source -> target means source cites target, inside this catalog only.
out = papers this paper cites; in = papers citing this paper; both = both.
Evidence id/url is stronger than title. Missing edges are not proof of absence.
traverse.edges preserves citation direction. tree_edges uses parent/child for
visit order and citations for the actual edges. Follow continuation if truncated.
Use citations and next_cursor to read ALL neighbors, including hubs.

Examples using DeepSeekMath, a verified member of the catalog:
  GET /v1/catalog?q=DeepSeekMath
  GET /v1/paper?id=arxiv:2402.03300
  GET /v1/citations?id=arxiv:2402.03300&dir=in&limit=24
  GET /v1/traverse?id=arxiv:2402.03300&dir=in&hops=1&max_nodes=100
  GET /v1/contents?id=arxiv:2402.03300
  GET /v1/content?id=arxiv:2402.03300&offset=0&length=32000
  GET /v1/find?id=arxiv:2402.03300&q=group
  GET /v1/search?q=group%20relative%20policy%20optimization&k=5
  GET /health
  GET /openapi.json
  POST /mcp

Keep corpus_version in subsequent reads as version. On 409 restart the query.
Content offsets/lengths count Unicode code points, not bytes or UTF-16 units.
Content length defaults to 6000, max 32000. Use contents to jump to sections.
Bibliography is removed from cleaned text; static source Markdown retains it.

Search returns unique-paper passage hits plus separate keyword metadata_hits.
Scores are similarities, not probabilities. English BGE embeddings are used;
non-English relevance has not been established. At most 8 passage hits; bounded
oversampling may return fewer. Exact title lookup is always available via catalog.
Shared cached search responses do not consume the embedding burst budget.
Uncached semantic queries share a 30/minute budget per client IP. On 429 wait
Retry-After seconds. Read-only catalog/text/citation operations do not use it.

MCP search(query) returns {results:[{id,title,url}]} and fetch(id) returns
{id,title,text,url,metadata}. Copy opaque doc: IDs unchanged. A text part contains
at most 16000 code points; use metadata.next_id to continue. Catalog-only items
state text availability; metadata.first_text_id opens text when available.
Advanced tools: list_papers, get_paper, citations, traverse, read_content,
contents, find_in_paper, search_passages. All are read-only.

Import /openapi.json as a Custom GPT Action with authentication None, or connect
/mcp in a remote MCP client. Hosting a URL does not automatically connect it.
Without tools, browse https://vinnik-dmitry07.github.io/favorite-papers/agents/ .
`
