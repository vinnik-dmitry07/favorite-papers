# Reproduction of the supplied PR #2 review

The two supplied archives were inspected and rerun against the current corpus
and probe kernels. This is an exploratory subset evaluation, not a production
migration gate or a Cloudflare Free certification.

## Provenance

| Supplied archive | SHA-256 |
| --- | --- |
| audit-pr2.tar.gz | c83e83d112c346e9758e4abc08b0837392718fbb0832c2672597991ea644500a |
| repro-bench-pq.tar.gz | 3c8a5736ed80e1687f44b01a4c6d8878f27403de3e02816335276984ec7f526a |

The corpus builder reproduced 40,575 passages. All 2,000 sentence-query target
paper IDs, chunk indices, and quoted texts match the rebuilt corpus. The
supplied embeddings contain 12,135 passages from 103 whole papers. Evaluation
uses 2,000 sentence queries from 101 papers and 53 natural questions from 38
papers. Models were not downloaded or rerun; embedding provenance and Workers
AI compatibility remain external assumptions.

The original pr2_criteria.py was run with only its input paths and output
filename adapted. An independently structured, portable implementation is now
in src/reproduce_static_search_review.py. Both runs reproduce every published
metric except one: the mean-centered binary/SQ8 overlap@8 rounds to 0.9654 here
instead of 0.9653. Its paper outcomes and bootstrap bound are unchanged. The
cause of that tiny numerical difference has not been isolated.

The [generated report](probe-results/review-reproduction-2026-10-19.json)
records source/data hashes, package versions, complete metrics, and the
remaining external-report difference. It also runs the actual PqIndex,
WasmPqScorer and Int8Index implementations through
probe-kernel/review-quality.ts. JS, JS4 and WASM PQ return identical ordered
top-200 IDs for all 2,053 queries.

## Results on the 2,000 sentence queries

Paper Hit@8 is measured after deduplicating up to 200 candidate passages
(100 for PQ reranking). Loss is relative to exact FP32. The upper bound uses
the external review's one-sided 95% paper-cluster percentile bootstrap with
4,000 resamples, seed 7, and query-weighted means.

| Implementation | Overlap@8 with FP32 | Paper Hit@8 | Paper loss, pp | Upper bound, pp | Target chunk retained@8 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Exact FP32 | 1.0000 | 0.9260 | 0.00 | — | 0.6650 |
| External Faiss PQ96 | 0.6936 | 0.9160 | 1.00 | 1.51 | 0.6160 |
| External Faiss PQ96 → SQ8 top-100 | 0.9898 | 0.9260 | 0.00 | 0.20 | 0.6655 |
| External centered binary → SQ8 top-200 | 0.9654 | 0.9270 | -0.10 | 0.24 | 0.6645 |
| Actual probe PQ, all three kernels | 0.6912 | 0.9160 | 1.00 | 1.52 | 0.6160 |
| Actual probe exhaustive int8 | 0.9838 | 0.9270 | -0.10 | 0.05 | 0.6645 |
| Actual probe PQ → int8 top-100 | 0.9800 | 0.9265 | -0.05 | 0.20 | 0.6645 |
| Actual probe raw binary → int8 top-200 | 0.9614 | 0.9255 | 0.05 | 0.38 | 0.6625 |

These are different quantizers. External SQ8 learns a per-dimension minimum
and scale and scores decoded vectors by inner product. The probe rounds each
row symmetrically to [-127, 127] and normalizes its int8 norm. External binary
codes subtract the corpus mean before taking signs; the probe takes signs
after uncentered int8 quantization. Quality must be measured for each format.
For this real-vector evaluation, the int8 fixture is quantized directly from
the supplied FP32 embeddings. The synthetic runtime builder derives int8 from
synthetic PQ reconstructions because it has no real embeddings. A production
rerank store must retain the FP32-to-int8 path tested here.

Plain PQ retains the source target chunk 4.9 percentage points less often than
FP32 after paper deduplication, despite only a 1-point paper-level loss.
Reranking largely removes that difference. Exact target-chunk identity is
only a diagnostic proxy: an overlapping or alternative passage can also answer
the question. This is not a human relevance judgment.

All variants find the target paper on all 53 natural questions. However,
exact FP32 retains the particular source chunk on only 21/53 questions, and
plain PQ on 19/53. Those questions were written while reading the target
chunks; this small set is not a representative held-out retrieval benchmark.
Zero observed discordance gives a degenerate ordinary bootstrap interval,
not a guarantee of zero population risk.

Local timings in the report cover kernels over 12,135 rows in a shared Node
24 process. They exclude metadata hydration, REST/MCP assembly, embeddings,
rate limiting, and Cloudflare execution. First calls are not independent cold
isolates. They must not be extrapolated into a Workers Free pass.

## Audit disposition

The archive contains 31 findings; its stored verdicts say 28 confirmed and
three plausible, rather than the 30/one split in the accompanying summary.
The original performance measurements describe the old single-kernel probe.
This reproduction does not claim to independently rerun every old harness.

| Findings | Current disposition |
| --- | --- |
| kernel K1–K4; worker K1–K2; methodology D1–D2/D4 | Kernel/layout matrix, catalog work, tokenizer fix and stress input, explicit quality metrics, rerank candidates, and implementation-specific stopping rule are present. Real-kernel subset evidence is now added. |
| telemetry R1–R5; CI C2/C6; worker K5; methodology D5 | Marker → platform requestId correlation, pilot, retries, checkpoints, exclusions, error logging and sample-bound wording are present. Live telemetry still needs verification. |
| CI C1/C3/C4/C7 | Explicit credential-pair selection, scoped push paths, per-run Worker cleanup and generated source-hashed reports are present. Existing repository credentials are the user-selected default. |
| CI C5 | Fixed here: probe, production and PR checks no longer share one pending-run slot. |
| worker K3/K6/K7 | Bounded find/snippet differences are documented. Fetch error parity for unavailable papers remains a prototype difference; no production replacement is claimed. |
| kernel K5/K6; worker K4; methodology D3 | Buffer copying remains an optimization candidate, the big-endian branch lacks direct coverage, and app-level cache labels do not prove every cache is warm. Module first-request flags are not true cold-start measurements. |
| methodology D6 | MCP session setup, real inference/rate-limit bindings and their resource costs remain outside the synthetic probe. End-to-end agent acceptance is still required. |

## Reproduce

Extract the supplied repro-bench-pq.tar.gz into a directory, represented below
by /path/to/evidence. Use an isolated Python environment and install the
optional requirements. No credentials or paid services are needed.

From the repository root:

    python -m pip install -r requirements-probe-quality.txt
    python src/build_agent_index.py
    npm ci --prefix worker
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
      python src/reproduce_static_search_review.py \
      --evidence /path/to/evidence \
      --work-dir /tmp/pr2-review-kernels \
      --output worker/probe-results/review-reproduction-2026-10-19.json

The script checks target identities/texts, trains the same Faiss quantizers,
recalculates the reference metrics, compiles the committed WAT/TS kernels, and
evaluates their actual output. Large vectors and intermediate rankings stay
outside Git. The checked-in runtime fixture and deployment are unchanged.
