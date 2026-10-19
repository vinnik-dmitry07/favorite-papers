# Static search feasibility probe

This is the first gate of the free-search migration, **not a semantic search
service**. The production Worker and the independent static agent catalog keep
their existing behavior. Do not advertise the probe as a search endpoint.

The experiment uses random, reproducible product-quantized vectors alongside
real paper excerpts. It measures the complete REST/MCP request path, including
tokenization, exhaustive approximate inner-product scoring, result assembly,
bounded text reads, and response serialization. It does not call Workers AI,
train codebooks, or measure retrieval quality. The generated size fixture repeats
some character-based excerpts to reach the target row count; these are not the
production tokenizer's 40,575 passages.

## Current evidence

The [2026-10-19 local report](probe-results/local-2026-10-19.json) records
**600/600 successful measured requests**, plus six successful warm-up requests,
against the complete fixture in local workerd. All 12 REST/MCP cases passed
their functional checks. It includes source-file hashes and client wall-time
percentiles for reproduction, with every Cloudflare CPU/memory/cold-start gate
explicitly unverified. The test suite has 75 Python and 78 TypeScript tests.

**The deployment gate is still blocked on Cloudflare access.** No paid tier was
enabled, no real embeddings were generated, and no retrieval-quality result is
claimed. Run the isolated workflow below to obtain the next piece of evidence.

## What is built

| Component | Size / behavior |
| --- | --- |
| Encoded passages | 40,575 rows × 96 uint8 codes = 3,895,200 bytes |
| Codebooks | 96 × 256 × 8 float32 values = 786,432 bytes |
| Search | All encoded rows are scored; return up to eight distinct papers |
| Original dimension | 768; each of the 96 subspaces has eight dimensions |
| Paper data | Real cleaned Markdown, split into 16,000 Unicode code points |
| Result metadata | Shards of 128 records; bounded in-memory cache |
| Storage | Worker Static Assets; no R2 or Vectorize binding |
| Query vector | Deterministic synthetic vector, explicitly not an embedding |

The full fixture currently contains 415 paper cards and 362 available texts.
`agent_probe/probe/measurements.json` records counts, sizes, and limitations;
`agent_probe/probe/index.json` also records the binary hashes and corpus version.
Generated assets are ignored by Git.
The binary layout and exact reconstruction oracle are covered by tests.

## Local reproduction

From the repository root:

```bash
python -m pip install -r requirements-agent.txt
python -m pytest src/test_static_search_probe.py src/test_static_search_probe_run.py
python src/build_static_search_probe.py
cd worker
npm ci
npm run typecheck
npm test
npx wrangler deploy --config wrangler.probe.toml --dry-run
npx wrangler dev --config wrangler.probe.toml --ip 127.0.0.1 --port 8787 \
  --inspector-ip 127.0.0.1 --inspector-port 9229
```

In a second terminal, from the repository root:

```bash
python src/run_static_search_probe.py http://127.0.0.1:8787 \
  --local --samples 50 --output probe-report-local.json
```

Local runs establish functional correctness and client wall time only. Neither
Node timings nor `wrangler dev` establish deployed Cloudflare CPU consumption.
An unverified local CPU gate is expected.

## Run on Workers Free

Use an account whose **Workers plan is Free**, checked in the Cloudflare
dashboard. The workflow does not change subscriptions. A Paid account does not
establish Free-plan feasibility, even if this small experiment incurs no extra
charge.

Add these GitHub **repository secrets** under Settings → Secrets and variables
→ Actions → New repository secret:

- `CLOUDFLARE_ACCOUNT_ID`: the target account ID.
- `CLOUDFLARE_API_TOKEN`: a custom token restricted to that account, with
  **Workers Scripts: Edit** for deployment and **Workers Observability: Edit**
  for the CPU-log query API. API documentation calls these permissions
  `Workers Scripts Write` and `Workers Observability Write`.

No zone, R2, Vectorize, Workers AI, billing, or `AGENT_DIMENSION_BUDGET`
permission/configuration is used by this probe. The production workflow still
has its separate requirements. If a narrower existing token cannot query CPU
logs, the measurement remains unverified; do not broaden it to all resources.

Before merging, dispatch the implementation branch with the GitHub CLI. The
existing `Agent API` workflow is already present on the default branch, and
`--ref` selects the version containing the new inputs:

```bash
gh workflow run agent-api.yml --ref feat/static-search-probe \
  -f static_probe=true -f free_plan_confirmed=true
```

Once these inputs are visible in Actions → **Agent API** → Run workflow, the
same run can be started there by selecting the branch and enabling both inputs.

The workflow deploys **`key-papers-static-probe`** and exercises six operations
in two cache conditions. It never deploys or promotes `key-papers-api` in probe
mode. It stores a small report and fixture manifest as a seven-day artifact;
the 79 MB generated fixture is not uploaded as a GitHub Actions artifact.

For a manual run, export the same credentials locally, then:

```bash
cd worker
npx wrangler deploy --config wrangler.probe.toml
cd ..
python src/run_static_search_probe.py https://key-papers-static-probe.ACCOUNT.workers.dev \
  --samples 50 --output probe-report.json
```

If logs arrive late, download/retain the report and retry collection within
Cloudflare's log retention window, without sending another measurement batch:

```bash
python src/run_static_search_probe.py \
  --collect-only probe-report.json --output probe-report.json
```

Exit status 1 means failed requests or a failed CPU gate. Online status 2 means
insufficient evidence. Online status 0 means the synthetic CPU matrix passed,
**not** that the full migration is ready.

## Evidence and stopping conditions

Each request has a unique correlation URL. CPU values must come from
`$workers.cpuTimeMs` in platform invocation events and match that exact URL.
Client response time and a custom JavaScript timer cannot substitute for CPU.
The probe enables Workers Logs at full sampling. Missing telemetry, malformed
responses, wrong corpus versions, and HTTP/MCP errors cannot pass the gate.

The CPU matrix covers REST search, MCP search, MCP fetch, a 32,000-code-point
content read, table of contents, and bounded find, each with 50 samples under
two application-cache conditions. Every tenth search uses a query close to the
512-token ceiling, within the 2,000-code-point input limit. Every case needs complete platform telemetry,
successful outcomes, and p99 CPU **below 8 ms**. This leaves headroom below the
Free plan's 10 ms per-invocation limit. Failure blocks the migration.

`cold=1` clears application caches. It does **not** restart the V8 isolate or
undo JIT compilation. `x-probe-boot-id` identifies an isolate's module instance;
`x-probe-cache` reports application-cache state. True isolate cold starts need
separate observations after fresh deployments/placement, with platform CPU
correlation. No claim of cold-start success follows from `cold=1`.

The runner deliberately leaves `runtime_gate`, `memory_gate`, and
`isolate_cold_gate` unverified. Before replacing production storage:

1. Measure actual deployed cold starts, the query-embedding adapter, and memory.
   Target under 96 MiB. Cloudflare's sampled isolate memory percentiles are
   useful evidence, but not a per-request peak bound. Their GraphQL API requires
   Account Analytics Read if used.
2. Build real embeddings with a resumable, budgeted bootstrap; persist checkpoints
   durably rather than relying on an evictable CI cache. Fit codebooks without
   using held-out queries. Freeze 60–100 evaluation queries first.
3. Compare against exact search over the original BGE vectors, at passage and
   paper level, plus human relevance checks. Proposed acceptance: at least 95%
   reference passage Recall@50 and no more than five percentage points loss in
   paper Hit@8. Synthetic rankings cannot answer this question.
4. Preserve versioned responses, immutable deployment assets, rollback, static
   agent discovery, and independent Pages access. Add account-wide query-budget
   enforcement before claiming a fixed free daily query allowance.

If CPU or retrieval quality fails, stop this design and evaluate the planned
centroid-routing fallback. Do not silently reduce the corpus, truncate candidate
sets, claim approximate scoring is exact, or enable a paid plan.

## Primary references

- [Workers limits](https://developers.cloudflare.com/workers/platform/limits/)
- [Static Assets configuration](https://developers.cloudflare.com/workers/static-assets/binding/)
- [Static Assets billing](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/)
- [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)
- [Workers telemetry query API](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/telemetry/methods/query/)
- [Workers memory metrics](https://developers.cloudflare.com/changelog/post/2026-06-30-memory-usage-metrics/)
