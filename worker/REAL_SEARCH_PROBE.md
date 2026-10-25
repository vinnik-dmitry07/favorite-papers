# Real-subset search integration probe

This isolated experiment uses real paper text and pinned local BGE embeddings
through the production `CorpusStore`, `createService`, REST and MCP contracts.
It tests whether an agent can search, read the returned text and obtain a source
citation. It does not publish a production API or establish full-corpus quality.

The earlier synthetic Durable Object matrix still has **17 missing CPU records**
after recovery. Its CPU/sample gate remains **unverified**. This real-subset
implementation is independent work; it does not change that historical result.

## Corpus and implementation

The default canonical builder selects these complete papers:

| Paper ID | Passages |
| --- | ---: |
| `arxiv:2402.03300` — DeepSeekMath | 118 |
| `arxiv:2412.06769` | 69 |
| `arxiv:2412.14135` | 203 |
| Total | 390 |

The induced graph has two edges. Selection is deterministic by undirected graph
distance from DeepSeekMath, then paper ID, with a 200–500-passage bound. It uses
`build_agent_index.py::build_release`, preserves complete canonical text and
code-point offsets, and reindexes the original numeric graph edges.

The local encoder uses `BAAI/bge-base-en-v1.5` revision
`a5beb1e3e68b9ab74eb54cfd186867f64f240e1a`, CPU FP32, CLS pooling and L2
normalization. It checks every encoded input against the pinned Hugging Face
tokenizer, refuses truncation, and caches vectors by input hash and encoder
identity. The little-endian FP32 vector file and canonical assets have SHA-256
checksums. The deployment pins the manifest hash.

The static adapter validates file hashes, dimensions, vector norms, canonical
passage mappings and graph references before exposing the subset to the
production service. Search exhaustively scores the local FP32 vectors; the
production shortlist and paper deduplication remain in use. This small prototype
uses neither Vectorize nor R2. Tokenizer and corpus initialization live inside
one fixed, server-named Durable Object.

## Local evidence and its limits

The [encoder report](probe-results/local-2026-10-25-real-encoder.json) records
actual local embedding generation. The six fixed natural-language queries are
development integration cases, not a held-out relevance benchmark. With only
three papers, retrieving the expected paper in the first eight results is weak
evidence; exact passages and the subsequently read context are checked
separately.

The [original v1 report](probe-results/local-2026-10-25-real-integration-v1.json)
records two failed passage checks:

- The baseline query retrieved chunk 56. Source review confirmed it answers the
  question using “value function” and average group rewards; the original oracle
  incorrectly required the literal word “critic”.
- The GRPO-settings query retrieved chunk 59, which does not contain the requested
  settings. The actual answer passages remain chunks 66 and 67.

The [v2 diagnostic report](probe-results/local-2026-10-25-real-integration-v2.json)
retains that retrieval behavior. Oracle revision 2 was made **after observing
v1**, with source adjudication and explicit provenance. Its baseline alternatives
recognize chunks 7, 12 and 56; the settings criterion and gold chunks 66/67 are
unchanged. Query strings and vectors were not tuned or replaced. The
[provenance record](probe-results/local-2026-10-25-real-provenance.json) preserves
both oracle definitions and source/artifact hashes. The unchanged v1 report
checked the REST passage prefix; v2 strengthens this to full-window equality.

In v2, `passage_retrieval_gate` remains **failed** because of the settings miss.
The standard REST read of 6,000 code points from the returned offset and the MCP
16,000-code-point document part do include the settings answer, so
`answer_context_gate` is **passed**. Text, offsets and citations are checked
against canonical files. A successful search/read integration is not a claim
that the returned passage itself was correct. No external LLM agent evaluation
or full-corpus quality gate has run.

## One bounded live run

Actual local-versus-Workers-AI compatibility has **not yet been tested**. The
live phase first compares 200 deterministically spread canonical passages
against `@cf/baai/bge-base-en-v1.5`. Every cosine must be at least **0.999**.
Sixteen texts per batch require 13 batches. Semantic search remains blocked
until all compatibility checks pass.

```bash
gh workflow run agent-api.yml \
  -R vinnik-dmitry07/favorite-papers \
  --ref feat/static-search-probe \
  -f static_probe=true \
  -f probe_runtime=durable-object \
  -f do_probe_phase=real \
  -f probe_credentials=repository \
  -f free_plan_confirmed=true
```

Use the existing `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_API_TOKEN` secrets.
The workflow checks the Free-plan confirmation, builds the subset, downloads
pinned model weights, generates local vectors and runs the actual-model local
REST/MCP integration before deployment. It creates a masked temporary probe
token with a 45-minute expiry. The original synthetic pilot is not rerun.

The following limits are enforced, not just reported:

| Scope | Bound |
| --- | ---: |
| AI text inputs, compatibility plus queries | 300 |
| AI query text inputs | 24 |
| AI input tokens | 153,600 |
| Single Workers AI call | 20-second timeout |
| External service HTTP attempts | 60 |
| Load phase | 600 seconds |

AI counters are reserved in durable storage before calls. Failed calls and
interrupted compatibility batches remain charged; object restarts cannot reset
the allowance or silently replay an unknown result. These limits bound this
experiment, not other activity sharing the account's Free quotas.

After compatibility, the runner checks six REST and six MCP search/read
journeys, graph citations/traversal, non-BMP offsets, stale-version rejection
and oversized-query rejection. It preserves separate contract, passage,
answer-context, latency, budget and CPU results. Logs and traces are enabled;
the current collector reads Logs only, not root spans. Request-level CPU is
accepted only with validated platform invocation identity.
Missing CPU records remain unverified, and observed CPU failures fail the run.
A green integration job can coexist with an unverified CPU/sample gate and a
failed passage diagnostic; it does not promote either to a pass.

Cleanup runs after successful, failed or cancelled deployment. It removes the
owned DO class, verifies namespace absence, then deletes that run's Worker.
The artifact `real-search-probe-<run>-<attempt>` retains the report, exact corpus
and vector assets, query vectors, local encoder/integration reports, deployment
log and cleanup evidence for
90 days. No production Worker, discovery link or paid subscription is changed.

## Local reproduction

From the repository root:

```bash
python src/build_real_search_probe.py --out agent_real_probe
python -m pip install -r requirements-real-probe.txt
python src/embed_real_search_probe.py --out agent_real_probe \
  --cache-dir .cache/real-probe-embeddings --threads 4 --batch-size 8 \
  --query-vectors local-query-vectors.json --report local-encoder-report.json
cd worker
npm ci
REAL_PROBE_REPORT="$PWD/../local-real-integration.json" \
REAL_PROBE_DIR="$PWD/../agent_real_probe" \
REAL_PROBE_QUERY_VECTORS="$PWD/../local-query-vectors.json" \
  npx vitest run src/real-search-integration.test.ts
```

The local integration uses local query embeddings. It cannot establish Workers
AI compatibility, Cloudflare CPU, true isolate cold-start behavior or memory
headroom. Full-corpus fidelity, passage utility and an external agent journey
remain later stages before production publication.
