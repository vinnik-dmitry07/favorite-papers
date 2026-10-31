# Key papers agent API

Public read API for the citation catalog. Start with the [static agent guide](https://vinnik-dmitry07.github.io/favorite-papers/agents/) for a catalog, complete paginated citation lists, and readable text. It needs no API or JavaScript. REST and stateless MCP add title lookup, section navigation, literal search and semantic search. The guide advertises the API only after deployment and live checks succeed.

The [permanent static search publication](PUBLIC_SEARCH_API.md) reuses the verified
full-corpus index in a separate `key-papers-search` Worker. It exposes the same
REST/MCP tools, with a persistent daily AI allowance and explicit compatibility
and activation checks. Select the manual `publish` phase of **Agent probe**;
ordinary pushes do not deploy it. This path does not require Vectorize, R2 or a
new corpus encoding. [Publication run 41007245038](https://github.com/vinnik-dmitry07/favorite-papers/actions/runs/41007245038)
passed its public checks. Start at the permanent
[agent manual](https://key-papers-search.vinnik-dmitry07.workers.dev/llms.txt),
or connect [MCP](https://key-papers-search.vinnik-dmitry07.workers.dev/mcp).
Future permanent publications require current `main`, the protected
`public-search` environment and dedicated `PUBLIC_SEARCH_CLOUDFLARE_*` secrets;
the temporary probes' repository-credential option does not apply to that job.
Publication now checks a private isolated Worker Preview first, requires a fresh
32-input provider check for each publication, and has an exact-version recovery
path with preserved publication state and global quota. Uncached requests have
per-address limits in addition to the shared daily ceiling. The corpus is saved
in a pinned GitHub Release without re-encoding. These code changes are not a
deployment; external environment/token setup and live rollout/recovery checks
remain required. Historical geometry evidence does not certify the changed loader.

The [static-search feasibility probe](STATIC_SEARCH_PROBE.md),
[real subset](REAL_SEARCH_PROBE.md) and [full offline gates](FULL_SEARCH_PROBE.md)
test a possible Workers Free replacement for Vectorize. The synthetic stage
does not establish semantic quality; later stages use canonical text and real
vectors. Those experimental phases are not production deployments. The explicit `publish`
phase is described separately above. The **Agent probe** workflow
(`agent-api.yml`, retaining its existing dispatch entrypoint) defaults to the
`PROBE_CLOUDFLARE_*` environment credentials. Existing repository credentials
remain an explicit `probe_credentials=repository` option. Cloudflare secrets
are passed only to steps that use the API, not installation, tests or full-corpus
encoding. The bounded compatibility canary needs its selected provider token.
Production has its own **Agent API** workflow
(`agent-publish.yml`) and does not depend on the probe's tests or fixture builds.
The shared catalog/tokenizer optimizations are reviewed code changes; the experimental phases
do not deploy the production Worker or alter its Cloudflare bindings. The
permanent publication has its own name, bindings and daily ledger.

Acceptance criteria:

- **R1.** Catalog ids, edge direction, and evidence are preserved. An edge `[source, target, evidence]` means source cites target. `cites` on a node is the in-degree. `refs` is the out-degree. Evidence is `id`, `title`, or `url` (`title` is the weaker match). API ids are the catalog strings (`arxiv:`, `doi:`, `openreview:`, `acl:`, `url:`). They are case-sensitive and are never shortened to `safe_key()`.
- **R2.** Readable text keeps case and appendices. Bibliography headings are removed with the same rules as the map builder. Chunks are half-open code-point ranges `[start, end)` whose union is the cleaned text. Each chunk is at most 800 code points and at most 512 tokens including special tokens and the passage template. Offsets are Unicode code points, not UTF-8 bytes and not UTF-16 code units.
- **R3.** REST and the advanced MCP tools return the same domain payloads, limits, and error codes. MCP `search(query)` and `fetch(id)` are adapters for research clients; detailed passage search is `search_passages(q, k)`. MCP signals failure with `isError`. It does not copy HTTP status numbers into the tool result.
- **R4.** A stopped or repeated publish does not change the active release. Slot `a` and slot `b` use different vector ids. The active pointer moves only after the inactive slot is ready.
- **R5.** Pages keeps its current files: transformed `src/index.html`, `src/map.js`, `assets/graph_data.js`, `assets/fulltext_search.js`, D3, and `.nojekyll`. Pages also publishes `agents/` and `llms.txt`. A successful API smoke uploads a discovery artifact; Pages downloads it and checks health before adding its origin to the agent guide. README and map permanently link that guide. Failed API publication does not block static Pages publication.
- **R6.** Offline tests cover the builder, publisher, and worker. A live publish checks Cloudflare capacity and token rights, then probes a namespace that is not `a` or `b`, then promotes.

The graph is citations inside this catalog, not the open web. Semantic search returns passages. It oversamples up to 40 chunks and returns at most one passage per paper. Separate `metadata_hits` include keyword matches without full text; those are not semantic hits. BGE is an English model; non-English retrieval quality is unmeasured. Papers with empty cleaned text stay on the graph and return `available: false`.

## Configuration

[`embed.json`](embed.json) is the only embedding and chunking configuration. Empty `query_template` and `passage_template` are explicit. A future prefix counts toward the 512-token budget. The model name alone does not fix preprocessing: index and query both send `pooling: "cls"`.

`build_signature` covers cleaning, chunking and the full tokenizer configuration.
The provider `embedding_signature` retains the legacy payload: model, dimensions,
metric, pooling, templates, token budget, tokenizer revision and vocabulary hash.
Tokenizer v2's local algorithm settings change the build identity without
invalidating identical Workers AI input strings. Local FP32 caches separately
bind their full tokenizer and numerical implementation. Rate limits and
`search_enabled` are not part of those signatures.

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
| `GET /v1/catalog?q=&section=&offset=&limit=&version=` | Resolve title, ID, or source URL; empty q lists every catalog record. Limit 1–24; follow next_offset with corpus_version |
| `GET /v1/paper?id=` | Card. Authors are capped and report `authors_total` / `authors_truncated`. Quality fields are null when absent |
| `GET /v1/citations?id=&dir=&limit=&cursor=` | `dir` is `out` (default), `in`, or `both`. Limit counts neighbors (default 12, max 24), not edges. `both` keeps every directed edge and its evidence. Pages are stable |
| `GET /v1/traverse?id=&dir=&hops=&max_nodes=` | BFS, hops 1–2, max_nodes 2–100 (default 24). `edges` preserves citation directions including cycles. `tree_edges` separates discovery parent/child from citations. On truncation, follow `continuation` using paginated citations |
| `GET /v1/content?id=&offset=&length=&version=` | Default 6000, configurable up to 32000 code points. Offset 0 is the default. `offset == length` is an empty page with `next_offset: null` |
| `GET /v1/contents?id=&version=` | Section headings and code-point offsets |
| `GET /v1/find?id=&q=&offset=&version=` | Literal case-insensitive search in one paper, up to 12 contexts per page; follow next_offset |
| `GET /v1/search?q=&k=` | Passage hits. `k` default 5, max 8. Score is similarity, not a probability. Snippets are at most 480 code points of the original cleaned passage |
| `GET /health` | Reader schema, signatures, active release, passage count verified at publish, optional global index count recorded at publish. It does not embed a query |
| `POST /mcp` | Tools `search`, `fetch`, `list_papers`, `get_paper`, `citations`, `read_content`, `contents`, `find_in_paper`, `traverse`, `search_passages` |

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

The search rate limit is shared by REST and MCP and keyed by client IP. A shared egress IP shares one budget of 30 uncached semantic queries/minute. Cache hits, title lookup, graph traversal and reading do not consume it. A 429 includes Retry-After: 60; clients should retry after that interval. There is no reliable individual-user identity for an anonymous shared proxy. Cloudflare's limiter is local and approximate. It is a burst brake, not a global spend cap.

## Publish

`src/build_agent_index.py` only reads the repo and writes `agent_build/`. `src/publish_agent_index.py` is the only writer to R2 and Vectorize.

Two namespaces, `a` and `b`, share one Vectorize index. The publisher stages the inactive slot, drops that slot's previous release from the rollback set before the first mutation, upserts, deletes stale ids in that slot only, waits until mutations are visible, then writes the ready manifest. Switching `active.json` is the last step. Checkpoints are per batch. Resume is allowed only for the same input hash, signatures, slot, and release. A newer active release blocks promotion of an older staged resume. Quota exhaustion records `paused_quota` and leaves the active release in place.

Unchanged passage text is reused from the embedding cache across slots and is not upserted again, so those vectors do not gain a new release stamp. The new manifest still lists their existing vector ids.

Rollback is a pointer move while the previous slot remains ready. After that slot is staged again, restoring it means publishing the stored release, not flipping the pointer. Cleanup never deletes the active slot.

Local commands may build, dry-run, and run the isolated probe. Production promotion runs from the single GitHub Actions writer.

## Onboarding

Import `GET /openapi.json` into a Custom GPT Action with authentication None. Add `POST /mcp` as a custom MCP connector in a client that supports remote MCP, including ChatGPT where custom MCP connections are enabled for the account. A public URL does not register the tool by itself. Confirm the connector in the account that will call it.

## Offline checks

```bash
python -m pytest src/test_agent_index.py src/test_publish_agent_index.py src/test_agent_pages.py
python src/build_agent_pages.py --out site
npm --prefix worker ci
npm --prefix worker run typecheck
npm --prefix worker test
```

`npm test` first rebuilds the probe kernel from WAT with the pinned compiler
and checks the output against `probe-kernel/scan.sha256`. The production CI
uses only the API, tokenizer and catalog tests; it does not require that kernel.


## Research-client contract

`search` accepts exactly `{"query":"DeepSeekMath"}` and returns
`{"results":[{"id":"doc:...","title":"...","url":"..."}]}`.
`fetch` accepts an unchanged result id and returns `{id,title,text,url,metadata}`.
Both return the same JSON in `structuredContent` and one text content block.
An item is explicitly a catalog record or a complete text part (at most 16000
Unicode code points), not an implicitly truncated paper. Follow
`metadata.next_id` to continue; catalog records expose `first_text_id` when
text is available. A release change requires a fresh search.

This follows the [OpenAI research MCP contract](https://developers.openai.com/api/docs/mcp).
Other MCP clients can use the additional tools directly. Installing a connector
in ChatGPT still requires account setup; a link alone cannot install tools.

## Deployment setup

The static catalog needs only GitHub Pages with Actions as its source. The
Cloudflare publisher requires an existing account, resources and credentials.
Missing credentials fail early with a diagnostic; the workflow never claims a
successful API deployment or advertises an invented URL.

Merging or pushing to `main` runs offline validation only. Production
publication requires a manual dispatch on `main` with
`production_publish_confirmed=true`. The default manual dispatch does not
publish. This confirmation is separate from the probe and full-encode flags.

1. Enable R2, Vectorize and Workers AI in the intended Cloudflare account.
   Create the resources named in `embed.json` and `wrangler.toml`, once:

   ```bash
   cd worker
   npm ci
   npx wrangler r2 bucket create key-papers-corpus
   npx wrangler vectorize create paper-passages --dimensions=768 --metric=cosine
   ```

2. Create an account-scoped API token suitable for Workers deployment and
   read/write access to R2, Vectorize and Workers AI. Use Cloudflare's
   [CI configuration guide](https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/)
   and the permission descriptions in its token editor. Store it in repository
   **Settings → Secrets and variables → Actions** as `CLOUDFLARE_API_TOKEN`;
   store the account id as `CLOUDFLARE_ACCOUNT_ID`. Do not put either in a PR.

3. Run `python src/publish_agent_index.py preflight` for the offline capacity
   report. Set `AGENT_DIMENSION_BUDGET` to the actual dimension capacity you
   have provisioned and approved. The current 415-record snapshot needs
   62,329,344 dimensions for both slots and the probe; the configured free
   allowance is 5,000,000. Raising this variable does not buy capacity. Check
   current Cloudflare plan limits and costs before enabling publication.

4. After reviewing the capacity report and the target account's remaining AI
   allowance, run **Agent API → Run workflow** on main with
   `production_publish_confirmed=true` (`agent-publish.yml`). Tokenizer v2
   requires a new build/release, but identical provider input strings retain
   their legacy embedding-cache keys. This does not prove that the target
   account has those entries. A cold
   publication of the current corpus represents about 47,664 neurons under
   `embed.json`'s estimator, before the publisher's probe; this exceeds its
   configured 10,000-neuron daily free allowance. The capacity preflight checks
   permissions and dimensions, not remaining neurons, and this flag neither
   changes the plan nor grants quota. The workflow performs an isolated probe,
   stages data, deploys the reader,
   promotes the release, and runs live REST/MCP checks. A failed post-promotion
   smoke rolls back the active data pointer. A successful smoke persists a
   discovery artifact and triggers Pages to publish the verified endpoint.

5. Open the static agent guide, follow its API link, and connect `/mcp` or
   import `/openapi.json` into a compatible client. Until the workflow succeeds,
   use static citation navigation and text; semantic search is unavailable.

The A/B publisher is retained to avoid replacing a working corpus with a partial
upload. It is optional infrastructure for semantic search: the static browsing
path has no dependency on R2, Vectorize, tokens, or version handshakes.
Manual Cloudflare work shares one concurrency group, including
the full offline workflow because its canary can use the same account. Read-only
log collection and offline PR/main checks have separate groups. Running jobs are
not cancelled; `queue: max` keeps up to 100 pending runs instead of replacing
the single pending run. Additional runs are cancelled when that queue is full;
see [GitHub's concurrency rules](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).
This serializes this workflow's runs; it cannot reserve quota against unrelated
account usage.
