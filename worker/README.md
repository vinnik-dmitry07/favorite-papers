# Key papers agent API

Public read API for the citation catalog. REST and stateless MCP expose the same five operations. The GitHub Pages map is a separate publish set and does not serve this API.

Acceptance criteria:

- **R1.** Catalog ids, edge direction, and evidence are preserved. An edge `[source, target, evidence]` means source cites target. `cites` on a node is the in-degree. `refs` is the out-degree. Evidence is `id`, `title`, or `url` (`title` is the weaker match). API ids are the catalog strings (`arxiv:`, `doi:`, `openreview:`, `acl:`, `url:`). They are case-sensitive and are never shortened to `safe_key()`.
- **R2.** Readable text keeps case and appendices. Bibliography headings are removed with the same rules as the map builder. Chunks are half-open code-point ranges `[start, end)` whose union is the cleaned text. Each chunk is at most 800 code points and at most 512 tokens including special tokens and the passage template. Offsets are Unicode code points, not UTF-8 bytes and not UTF-16 code units.
- **R3.** REST and MCP return the same domain payloads, limits, and error codes. MCP signals failure with `isError`. It does not copy HTTP status numbers into the tool result.
- **R4.** A stopped or repeated publish does not change the active release. Slot `a` and slot `b` use different vector ids. The active pointer moves only after the inactive slot is ready.
- **R5.** Pages keeps its current files: transformed `src/index.html`, `src/map.js`, `assets/graph_data.js`, `assets/fulltext_search.js`, D3, and `.nojekyll`. The workers.dev origin is written into the map and readme only after a successful live smoke.
- **R6.** Offline tests cover the builder, publisher, and worker. A live publish checks Cloudflare capacity and token rights, then probes a namespace that is not `a` or `b`, then promotes.

The graph is citations inside this catalog, not the open web. Semantic search returns passages. It does not rerank, blend keywords, or collapse hits to one row per paper. Papers with empty cleaned text stay on the graph and return `available: false`.

## Configuration

[`embed.json`](embed.json) is the only embedding and chunking configuration. Empty `query_template` and `passage_template` are explicit. A future prefix counts toward the 512-token budget. The model name alone does not fix preprocessing: index and query both send `pooling: "cls"`.

`build_signature` covers cleaning, chunking, and the tokenizer checksum. `embedding_signature` covers model, dimensions, metric, pooling, templates, and the tokenizer checksum. Rate limits and `search_enabled` are not part of those signatures.

Tokenizer assets are local. `tokenizer/vocab.txt` is BAAI/bge-base-en-v1.5 revision `a5beb1e3e68b9ab74eb54cfd186867f64f240e1a`. Tests check its sha256 and do not download it.

## Identifiers and storage

Clients pass `id` as a query parameter and apply URL encoding. The server decodes it once, does not change case, and never uses the raw id as an R2 path. Paper objects use the sha256 of the catalog id.

Vector ids are 64-character SHA-256 hex of the canonical JSON array `[slot, paper_id, chunk_index]`. Metadata may hold the full catalog id, including values longer than 64 bytes, and that field is not a metadata index. Vectors do not store `corpus_version`. The worker joins a hit through the vector map of the release it captured for the request.

`corpus_version` in responses is the active release id. A content `version` or citation cursor from another release returns 409. The client starts again.

## Operations

| Method | Use |
|---|---|
| `GET /` | Manual, id grammar, examples |
| `GET /openapi.json` | OpenAPI 3.1, `security: []`, server is the verified request origin |
| `GET /v1/paper?id=` | Card. Authors are capped and report `authors_total` / `authors_truncated`. Quality fields are null when absent |
| `GET /v1/citations?id=&dir=&limit=&cursor=` | `dir` is `out` (default), `in`, or `both`. Limit counts neighbors (default 12, max 24), not edges. `both` keeps every directed edge and its evidence. Pages are stable |
| `GET /v1/traverse?id=&dir=&hops=` | BFS over the full adjacency, not the first citation page. Default direction `out`. Hops default 1, max 2. At most 24 nodes including the seed, so at most 23 discovery edges. Cycles are visited once. The edge list is a discovery tree. `truncated` describes the cap inside the requested hop depth |
| `GET /v1/content?id=&offset=&version=` | Up to 6000 code points. Offset 0 is the default. `offset == length` is an empty page with `next_offset: null` |
| `GET /v1/search?q=&k=` | Passage hits. `k` default 5, max 8. Score is similarity, not a probability. Snippets are at most 480 code points of the original cleaned passage |
| `GET /health` | Reader schema, signatures, active release, passage count verified at publish, optional global index count recorded at publish. It does not embed a query |
| `POST /mcp` | Tools `search`, `get_paper`, `citations`, `read_content`, `traverse` |

Unknown catalog id: 404 `unknown_id`. Known id without usable text: 200 `available: false` and a `reason` (`no_markdown` or `empty_cleaned`). A file on disk is not enough.

Invalid cursor, non-integer offset, offset past the end, empty query, oversized id or query, or a query that does not fit in 512 tokens: 400. The query is tokenized with the query template and special tokens and is never silently truncated. Numeric fields reject blanks and `NaN`. Values above the documented maxima are 400 rather than clamped.

`version` or cursor release mismatch: 409 `version_conflict`.

Missing corpus, signature mismatch, dangling vector hit, or disabled search: 503 with a diagnostic `error.code`, not an empty 200. Search runs only in the active namespace. `SEARCH_ENABLED` applies to REST and MCP.

## Cursors

A citation cursor is unpadded base64url of canonical JSON:

```json
{"version":"<release>","paper":"<catalog id>","direction":"out","position":12}
```

Canonical JSON sorts object keys, has no extra whitespace, and keeps non-ASCII characters unescaped. `position` is the next neighbor index. A cursor for a different paper or direction is 400. A cursor for a different release is 409.

## Errors

```json
{"error":{"code":"unknown_id","message":"...","details":{}}}
```

Codes: `unknown_id`, `invalid_cursor`, `invalid_offset`, `invalid_query`, `query_too_long`, `invalid_argument`, `version_conflict`, `not_ready`, `config_mismatch`, `dangling_hit`, `search_disabled`, `rate_limited`, `deadline_exceeded`, `corpus_unavailable`, `response_too_large`.

## Time bounds

The active pointer is cached for at most 30 seconds. One request, including an MCP tool call, dies at 20 seconds and does not return a late payload. A slot that just stopped being active cannot be mutated again for 120 seconds. After the pointer TTL, an R2 error is a failure. The worker does not keep serving an expired pointer. Adjacency is cached per release. Paper text is cached with a memory cap.

The search rate limit is shared by REST and MCP and keyed by client IP. A shared egress IP shares one budget. Cloudflare's limiter is local and approximate. It is a burst brake, not a global spend cap.

## Publish

`src/build_agent_index.py` only reads the repo and writes `agent_build/`. `src/publish_agent_index.py` is the only writer to R2 and Vectorize.

Two namespaces, `a` and `b`, share one Vectorize index. The publisher stages the inactive slot, drops that slot's previous release from the rollback set before the first mutation, upserts, deletes stale ids in that slot only, waits until mutations are visible, then writes the ready manifest. Switching `active.json` is the last step. Checkpoints are per batch. Resume is allowed only for the same input hash, signatures, slot, and release. A newer active release blocks promotion of an older staged resume. Quota exhaustion records `paused_quota` and leaves the active release in place.

Unchanged passage text is reused from the embedding cache across slots and is not upserted again, so those vectors do not gain a new release stamp. The new manifest still lists their existing vector ids.

Rollback is a pointer move while the previous slot remains ready. After that slot is staged again, restoring it means publishing the stored release, not flipping the pointer. Cleanup never deletes the active slot.

Local commands may build, dry-run, and run the isolated probe. Production promotion runs from the single GitHub Actions writer.

## Onboarding

Import `GET /openapi.json` into a Custom GPT Action with authentication None. Add `POST /mcp` as a custom MCP connector in a client that supports remote MCP, including ChatGPT Pro read/fetch connectors where that account allows them. A public URL does not register the tool by itself. Confirm the connector in the account that will call it.

## Offline checks

```bash
python -m pytest src/test_agent_index.py src/test_publish_agent_index.py
npm --prefix worker ci
npm --prefix worker run typecheck
npm --prefix worker test
```
