# Full-corpus retained-vector quality measurement, October 28

The full int8 runtime preserves the FP32 retrieval ordering closely. The
remaining weakness in this diagnostic is selecting useful evidence inside the
right paper. These are measurements on frozen development questions, not a
held-out evaluation or a deployed-agent acceptance test.

The subsequent [fresh-agent navigation measurement](AGENT_JOURNEY_MEASUREMENT.md)
now covers 12 REST journeys and four basic MCP journeys. It tests whether agents
can recover evidence with follow-up tools; the fixed-span results below remain
a separate diagnostic.

## What was measured

The replay used all **40,575 saved corpus vectors** and **2,064 saved query
vectors** from [run 40448979121](https://github.com/vinnik-dmitry07/favorite-papers/actions/runs/40448979121).
No embeddings were recomputed and no provider was called. The original ZIP,
vectors and question hashes were verified. Canonical assets were rebuilt from
the unchanged source; the repacked manifest and every asset hash matched the
historical run. The existing inference and admission entrypoints are unchanged.

All queries ran through the actual `FullSearchIndex` WASM implementation. On 64
fixed, evenly spaced queries, JavaScript returned identical rankings and scores.
The reference used the saved FP32 vectors with float64 accumulation and the
original deterministic tie-breaking and metric functions. The old certificate
was not rewritten or reissued: this is read-only historical analysis.

## Quantization fidelity

| Metric | 2,000 extractive queries | 64 natural questions |
| --- | ---: | ---: |
| Mean FP32 top-8 overlap with int8 top-8 | 98.575% | 98.438% |
| FP32 top-8 retained inside int8 top-50 | 100% | 100% |
| Queries retaining fewer than half of FP32 top-8 | 0 | 0 |

The frozen fidelity criterion (at least 95% reference top-8 containment in
candidate top-50) passes. This criterion measures agreement with FP32, not
whether either representation retrieves the answer. On the extractive cohort,
REST paper hits decrease from 1,872 to 1,870 of 2,000 (0.10 percentage points),
and answer-window hits decrease from 1,413 to 1,410 (0.15 points).

## Natural questions: answer evidence remains the bottleneck

These 64 model-authored development questions cover 32 papers, two questions
per paper. Results below therefore equal the paper-macro averages as well as
the query averages. The gold source passages were frozen before this replay.

| Metric | FP32 | int8 |
| --- | ---: | ---: |
| Gold source chunk anywhere in top-50 | 41/64 (64.06%) | 41/64 (64.06%) |
| Correct paper in REST semantic results | 55/64 (85.94%) | 54/64 (84.38%) |
| Correct paper in MCP semantic results | 50/64 (78.13%) | 51/64 (79.69%) |
| Selected chunk contains all marked answer spans, REST or MCP | 14/64 (21.88%) | 14/64 (21.88%) |
| REST reading window contains all marked answer spans | 30/64 (46.88%) | 30/64 (46.88%) |
| MCP reading window contains all marked answer spans | 40/64 (62.50%) | 42/64 (65.63%) |

The projections use the existing REST top-40 to eight distinct papers and MCP
top-25 to five distinct papers. They retain one selected chunk per paper and
model the existing 6,000-code-point REST and 16,000-code-point MCP reading
windows. They exclude catalog routing and agent follow-up tools. A missed marked
span does not prove that no equivalent answer exists elsewhere in the paper.
These numbers do not measure generated-answer correctness.

Int8 loses one REST paper hit and gains one MCP paper hit on this small cohort.
The MCP reading-window gain is two cases; it is not evidence of a general
quality improvement. Both representations miss the same marked source chunk
in 23 of 64 top-50 lists. Changing quantization alone cannot resolve that result.

All 64 questions have one annotated answer span and at least one valid gold
chunk. Among correct papers already selected for output, keeping only the
best-scoring chunk drops an available gold chunk in **26 REST / 25 MCP cases**.
For `full-natural-002`, the correct paper ranks first through chunk 5, while the
gold chunk 46 ranks seventh and is discarded. In `full-natural-003`, the returned
chunk starts just after the answer: REST's forward window misses it, whereas
MCP's aligned window contains it. For `full-natural-004`, both representations
miss the correct paper entirely in their top-50.

A post-hoc calculation on the same saved rankings holds the selected papers
and candidate pools fixed, then retains multiple hits for each selected paper:

| Hits retained per selected paper | REST answer-window coverage | MCP answer-window coverage |
| --- | ---: | ---: |
| 1 (current projection) | 30/64 | 42/64 |
| 2 | 38/64 | 45/64 |
| 3 | 41/64 | 47/64 |
| 5 | 46/64 | 50/64 |
| All existing candidates | 49/64 | 50/64 |

This is available-context coverage, not agent answer accuracy or a validated
improvement. Reading every retained hit can cost several times the current
reading budget. Questions, embeddings, ordering and gold spans were unchanged.
[Failure cases and post-hoc counts](probe-results/replay-2026-10-28-full-quality.failures.json)
retain the inputs and projection parameters.

The subsequent agent journeys recovered supported answers on all 12 selected
REST cases, including an initial retrieval miss. These results do not justify
changing passage deduplication yet. The next measurement uses genuine new query
text against the retained corpus; no corpus re-encoding is needed. Any future
passage-layout comparison should use separate development cases before a
held-out test.

## Reproduction and limits

[Execution commands, file hashes and compiled bundle identity](probe-results/replay-2026-10-28-full-quality.execution.json)
bind the [summary](probe-results/replay-2026-10-28-full-quality.json),
[per-query results](probe-results/replay-2026-10-28-full-quality.queries.jsonl.gz),
[runtime rankings](probe-results/replay-2026-10-28-full-quality.rankings.json.gz),
and [restoration receipt](probe-results/replay-2026-10-28-full-quality.restoration.json).
Download artifact 12715563729, install `requirements-agent.txt` and NumPy 2.3.4,
run `npm ci` and `npm run build:probe` under `worker`, then follow those commands.

The replay used Python 3.12.14, NumPy 2.3.4 and Node 24.22.1. Kernel ranking took
95.42 seconds and reference/scoring took 8.18 seconds in this environment. These
are local execution times, not Cloudflare CPU measurements or performance
benchmarks. Platform memory, end-to-end external-agent usefulness and production
readiness remain unverified. The original GitHub run remains failed because
its final validator timed out; this replay does not change that historical status.
