# Full-size memory measurement, October 26

The default local memory filter remains **FAIL**. No long encoding, provider
canary, deployment, production change, or threshold change was performed.

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

A source-review observation about concurrent same-paper cache misses
overcounting `CorpusCache.paperBytes` is deferred. It was not added as a third
implementation change and is not asserted to explain the measured peaks.

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
