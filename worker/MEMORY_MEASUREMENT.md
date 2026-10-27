# Full-size memory measurement, October 26

The October 26 local measurements remain **FAIL** against the default memory
filter. No long encoding or provider canary was performed during those
measurements. Subsequent Cloudflare geometry and genuine-vector results are
recorded below; the threshold is unchanged.

| Configuration | Observed peak MiB | Retained final MiB | Seconds | Default gate evidence |
| --- | ---: | ---: | ---: | --- |
| Unmodified `b865dc7` | 133.85 | 69.63 | 36.95 | FAIL |
| Packed key comparison | 134.32 | 69.62 | 32.65 | FAIL |
| Plus numeric paper scan | 134.44 | 69.64 | 32.92 | FAIL |
| Same final code, restricted Node heap | 83.70 | 69.62 | 32.46 | Diagnostic only |

All runs used 40,575 synthetic passage vectors, the real graph/text assets,
324 REST/MCP requests and 160 search requests. All non-peak contract checks
passed. There was one observation per configuration, so the timing differences
do not establish a speedup. The restricted-heap run overlapped the TS tests.

The baseline allocation sampler included objects collected by both major and
minor GC. Its largest cumulative samples were the paper validation function,
numeric-to-string conversion and packed-row lookup. These are cumulative
allocations across the workload, not simultaneous or retained memory.

Two changes were made in `src/full-corpus-store.ts`: binary search compares
eight unsigned big-endian words instead of formatting candidate hashes, and
paper boundary validation scans UTF-16 positions without per-character string
iteration. Every hash validation, public identifier, code-point offset, result
limit, admission bound and workload remains unchanged. The tests cover all
fixture keys, missing keys with long equal prefixes, malformed IDs and Unicode
offsets. Validation: 171 TS tests passed, two opt-in tests skipped; normal and
production TypeScript checks passed. A separate source review found no
correctness defect in either change.

## Evidence and interpretation

[Summary and raw hashes](probe-results/local-2026-10-26-full-memory.json) link
the compressed original reports, original allocation profile, profiling driver
and exact intermediate implementation. The before implementation is committed
as `b865dc75438cd3cc4607f7aead76541cf3584458`; the after implementation is in
the commit containing this document. Source hashes and executed bundle hashes
are retained in each raw report. The profile-instrumented run is not used as a
normal memory measurement.

The additional diagnostic ran the final implementation with
`--max-old-space-size=64 --max-semi-space-size=4`. The unchanged harness reports
PASS for that run, but **the experiment's admission decision remains STOP**.
It was not submitted to `record-geometry` or `aggregate`. The ordinary run
still fails. Node heap configuration materially affects the observed peak;
these flags neither emulate Cloudflare nor establish its memory headroom.
The metric is `heapUsed + external`, and sampling can miss peaks.

After two targeted changes, stop speculative allocation work. The next
decision-changing measurement is an isolated full-size Cloudflare probe,
using the existing full loader, WASM and bounded handler. The existing real
DO entry point only supports the old subset format, so it needs a small
separate full-size entry point before deployment. Reuse existing auth, expiry
and cleanup. Measure cold loading, paper/cache churn, errors and latency;
report CPU coverage and only claim memory headroom if actual platform memory
is obtained. A successful workload without OOM is not a memory measurement.
No change to the local gate policy or permission for a long run is implied.

### Short Cloudflare geometry diagnostic

The manual `geometry` phase now deploys the same full-size synthetic pack in
one temporary Durable Object. It shares the full corpus loader, WASM index,
service and bounded REST/MCP handler with the local memory workload. It has
no Workers AI, Vectorize or R2 binding, downloads no encoder model, and cannot
perform semantic evaluation or publish production data.

```bash
gh workflow run agent-api.yml \
  -R vinnik-dmitry07/favorite-papers \
  --ref feat/static-search-probe \
  -f static_probe=true \
  -f probe_runtime=durable-object \
  -f do_probe_phase=geometry \
  -f probe_credentials=repository \
  -f free_plan_confirmed=true
```

The load is bounded to 300 seconds and 350 HTTP attempts with no workload
retries. The normal workload is 324 REST/MCP requests plus three controls:
16 concurrent cold catalog requests, large-paper reads, four 20-request
content bursts, 48-paper cache churn, 160 distinct synthetic searches and
16 cached repeats. Only designated bursts accept `probe_overloaded` responses;
every other error stops the next phase. An external supervisor also bounds
stalled connections. The per-object request cap resets if the object restarts;
the external runner enforces the whole-run cap.

The runner pins the manifest and checks response identity, offsets and result
geometry. Platform CPU is collected separately for the gateway and object,
for at most 90 additional seconds; client latency is never substituted for CPU.
Missing telemetry remains unverified. Auth expires after 15 minutes and the
20-minute CI job removes the owned namespace and Worker, verifies absence,
and preserves the run report and cleanup evidence as
`full-geometry-probe-<run>-<attempt>`.

Interpretation: an OOM, object reset disrupting the workload, unexpected HTTP
error or persistent CPU excess is a reason to stop before full encoding.
A completed workload without OOM is useful runtime evidence, but provides no
numerical memory peak, semantic quality or Workers AI compatibility result.
Memory and production-readiness fields therefore stay unverified. This job
does not write an admission certificate or override the failed 96 MiB filter.

The October 27 local workerd smoke completed all 327 attempts in 20.68 seconds
including local startup. It used one object boot, admitted at most four active
and eight queued requests, and returned 21 expected overload responses in the
burst phases with no unexpected failures. All 160 distinct synthetic queries
and cached repeats matched the expected counts. This verifies the deployed
entry-point/runner integration locally, not Cloudflare CPU or memory.
[Raw evidence and reproduction](probe-results/local-2026-10-27-full-geometry.json).
Validation: 121 focused Python tests, 176 TypeScript tests (two opt-in tests
skipped), both TypeScript checks and the geometry Wrangler dry-run passed.

A source-review observation about concurrent same-paper cache misses
overcounting `CorpusCache.paperBytes` is deferred. It was not added as a third
implementation change and is not asserted to explain the measured peaks.

### Cloudflare result, October 26 Pacific time

[Run 40440982907](https://github.com/vinnik-dmitry07/favorite-papers/actions/runs/40440982907)
on `0fde944` completed the full synthetic workload in 57.985 seconds:
327 attempts, 297 HTTP 200 responses and 30 expected `probe_overloaded` 503
responses confined to the designated bursts. All 160 synthetic searches and
cached repeats passed; there was one object boot and no unexpected error.
The owned namespace and Worker were removed, with namespace absence verified.

| Aggregate platform invocation records | Count | CPU p50 | CPU p95 | CPU p99 | Max CPU |
| --- | ---: | ---: | ---: | ---: | ---: |
| Gateway | 326 | 0 ms | 1 ms | 2 ms | 7 ms |
| Durable Object | 327 | 5 ms | 477 ms | 536 ms | 769 ms |

All retained invocation outcomes are `ok`. These distributions use every
retained platform invocation, including those without an unambiguous request
mapping. They are not per-operation CPU measurements. Distinct-search client
latency was p50 838 ms/p95 1,649 ms at concurrency four; cached-repeat p50 was
118 ms. No embedding provider was called.

The strict CPU gates remain **unverified**: 99 DO markers collide onto shared
invocation keys in concurrent catalog/search phases. There are 32 collision
groups: 22 triples, nine pairs and one group of 15. Only 228 DO and 323 gateway
request matches are unambiguous. The collector exhausted its 120-query cap;
repeating identical queries will not resolve the many-to-one mapping. The
condensed artifact preserves all invocation values but not the source events
needed to reconstruct those ambiguous links. Conflict checks were not relaxed.

The green workflow certifies functional completion and cleanup, not complete
CPU evidence or memory headroom. The workload completed without observed OOM
or object reset, but no platform memory peak was measured and the 96 MiB local
filter remains failed. This runtime result should inform an explicit admission
decision before long encoding. The next useful measurements are genuine-vector
compatibility, retrieval quality and an external-agent semantic-search journey;
there is no reason to repeat unchanged geometry just for telemetry completeness.

[Summary, hashes and original report](probe-results/cloudflare-2026-10-26-full-geometry.json)
preserve the evidence and original unverified gates. Two independent readings
of the saved report confirmed counts, aggregation, collisions and cleanup.

## Reproduce the standard measurement

Use a fresh output directory for the geometry pack. Commands below use the
repo's installed Python/NumPy and Node dependencies; no model weights are
loaded. Keep runtime versions from the raw report when comparing results.

```bash
python src/build_full_search_probe.py --out agent_full_probe
python src/pack_full_search_probe.py --source agent_full_probe \
  --out agent_geometry_probe --geometry-fixture --seed 17
mkdir -p full-probe-reports
worker/node_modules/.bin/esbuild worker/probe-kernel/full-memory.ts \
  --bundle --platform=node --format=esm --outfile=full-probe-reports/full-memory.mjs
GEOMETRY_MANIFEST_SHA=$(sha256sum agent_geometry_probe/probe.json | cut -d ' ' -f 1)
timeout 300s node --expose-gc full-probe-reports/full-memory.mjs \
  --assets agent_geometry_probe --manifest-sha "$GEOMETRY_MANIFEST_SHA" \
  --wasm worker/probe-kernel/scan.wasm --vocab worker/tokenizer/vocab.txt \
  --canonical agent_full_probe/probe.json --out full-probe-reports/memory.json \
  --data-label geometry-fixture
```

Exit code 1 is expected for a failed memory filter; the JSON report is still
written. To reproduce the intermediate run, restore its compressed source
file over `worker/src/full-corpus-store.ts` in an isolated checkout, then
rebuild the harness. To reproduce sampling, build the baseline harness to
`full-probe-reports/full-memory-baseline.mjs`, copy the retained profile driver
beside it and run that driver with `node --expose-gc` from the repository root.

## External-agent access result

One fresh agent started from the public `/agents/` URL and followed ordinary
links. Seven HTTP page opens reached DeepSeekMath, all three cited-by pages
(24 + 24 + 19 = 67 entries), a citing paper, and the section giving group size
64 and KL coefficient 0.04. The starting guide already uses DeepSeekMath as an
example, so this does not test general title discovery.

The web retrieval tool could not open the starting URL; direct HTTP GETs
succeeded. This is a completed HTTP-capable agent journey, not a demonstrated
web-only ChatGPT journey or semantic search. The guide still has no verified
semantic API link. [Detailed navigation evidence](probe-results/local-2026-10-26-agent-browser-journey.json)
records requests, timing, obstacles and remaining limitations.

## Subsequent offline admission decision

The reviewed live result now supports the scoped policy in
[FULL_SEARCH_PROBE.md](FULL_SEARCH_PROBE.md#current-result-and-offline-admission-policy).
`geometry-contracts` requires fresh complete non-peak contracts and the fixed
live runtime/corpus pin. The raw 96 MiB diagnostic stays FAIL; platform memory
and production readiness remain unknown. This policy admits only bounded
compatibility testing and explicitly confirmed offline encoding/evaluation.
A stale pin or any other local failure still stops execution.
## Genuine full-corpus run, October 27

[Run 40448979121](https://github.com/vinnik-dmitry07/favorite-papers/actions/runs/40448979121)
completed all 40,575 corpus embeddings and 2,064 frozen query embeddings. The
genuine-vector workload passed all 324 contract requests with an observed Node
heapUsed + external peak of **92.42 MiB**, below the unchanged 96 MiB diagnostic.
This GitHub runner used Node 22.23.3; the earlier 134.52 MiB local measurement
remains valid for its own environment. Neither value measures Cloudflare memory
or establishes its available headroom.

The workflow failed immediately before quality evaluation: the separate
certificate/runtime validator exceeded its one-minute step timeout. The memory
harness itself passed. That validator's budget is now five minutes, preserving
the 350-minute job limit and all admission checks. No full-corpus quality result
was produced by this run.

The complete vector artifact and embedding caches were saved. The artifact ZIP,
corpus vectors, query vectors and frozen-query hashes were independently checked
after download. Continue from these vectors; the failed validation is not a reason
to encode the corpus again. A copied certificate still binds its original paths,
environment, source and expiry, so it is not a portable admission override.

[Run summary and raw evidence](probe-results/github-2026-10-27-full-offline.json)
