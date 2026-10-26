# Full-corpus evaluation: fail before inference

This is an isolated offline experiment. It does not publish a release, change
the production Worker, alter discovery links, or enable a paid plan. The next
long run needs explicit user confirmation **after the reviewed code is pushed**.

The earlier 390-passage result covers three papers. It does not establish full
corpus memory, retrieval quality or Cloudflare CPU. The full source currently
contains 415 cards, 362 available texts and 53 explicitly unavailable texts.

## Current result: STOP

The [2026-10-25 local report](probe-results/local-2026-10-25-full-preflight.json)
retains both memory runs and their exact compressed raw evidence. The first
full-geometry workload found cached snippets retaining complete paper strings.
Copying only the bounded snippet reduced retained memory after search churn
from 139.2 to 69.6 MiB and the observed peak from 207.1 to 135.5 MiB. The same
324 REST/MCP requests and 160 synthetic-vector searches were used in both runs.

The unchanged 96 MiB peak filter still fails. All other measured memory/contract
checks pass, including queue limits, one index initialization and retained
churn growth below 8 MiB. This is a local Node result, not proof that Cloudflare
uses 135.5 MiB. The new provider canary has **not** started; the interrupted full encode has **not** resumed.
Do not bypass or raise the memory threshold just to obtain a certificate.

## Why the order changed

The interrupted full encode found a tokenizer mismatch in Uni[MASK]
(`arxiv:2211.10869`): the pinned Hugging Face tokenizer recognizes literal
`[MASK]`, while the previous Python and Worker implementations split it into
punctuation and a word. Testing only the next uncached batch found that error
after model work had already started.

Tokenizer v2 preserves the pinned added-token semantics before normalization.
Its algorithm and configuration are bound into both embedding and build
identities. Old cache namespaces are not silently relabelled as v2. Reusable
cache identity binds the numerical encoder/tokenizer syntax, configuration,
model revision and dependency versions; comments and unrelated CLI changes do
not invalidate vectors. Full source hashes still invalidate preflight evidence.
The workflow prunes each restored/saved cache root to the current namespace plus
one prior namespace and a 512 MiB payload budget. Evicted entries are cache misses,
never substitutes for newly admitted inference. A tokenizer-only scan includes every passage, cached or uncached,
every frozen query, and regression cases before any model weights load.

The canonical rebuild retained all source texts and 40,575 passages; token
count changed from 7,868,447 to 7,867,965. Source text equality is checked when
rebasing the frozen questions. Chunk counts may change in a future legitimate
tokenizer revision; preserving complete source coverage is the invariant.

## Gates and decision scope

| Order | Evidence | Failure action |
|---|---|---|
| 1 | Source coverage, pinned model/config, frozen queries, code and dependency hashes | STOP on stale or incomplete input |
| 2 | All canonical Python/HF/Worker token IDs, no truncation, model never loaded | STOP before inference, including cache hits |
| 3 | Existing genuine vectors, independent int8 reference, JS/WASM, ties around top25/top40, actual REST/MCP routes | Fix packing, ranking or API contracts |
| 4 | Full-size synthetic index with real metadata/text, cold concurrent initialization, bounded request/embedding queues, serialized responses, repeated cache churn | Fix memory/runtime implementation |
| 5 | At most 32 local and 32 provider input occurrences, including repeats; the actual failing input, all five special tokens, Unicode and query/passage inputs | STOP on model/provider mismatch or unavailable allowance |
| 6 | Fresh certificate with every mandatory gate PASS, plus explicit long-run flag | Encode only after user confirmation |

Missing, expired, interrupted or unknown evidence cannot become PASS. Gate
reports preserve raw artifact hashes and earlier attempts. The certificate is
valid only for its exact source, canonical release, frozen questions, code,
dependencies and encoder identity. A change invalidates it. A partially
completed encode can resume from validated cache entries; completion attaches
the vector artifact atomically.

The certificate means `GO_FOR_FULL_OFFLINE_ENCODE`. Platform CPU, platform
memory, held-out quality and production readiness remain separate unknowns.
Missing historical Cloudflare gateway CPU records do not prevent independent
offline checks, and are never upgraded by these checks.

## Memory and numeric fixtures

The geometry fixture uses a separate, explicitly synthetic schema. It shares
the quantizer, packed metadata, binary loader and search kernel with the real
path. The real-data loader rejects it. Generated vectors establish shape and
allocation behavior only; their search results are not semantic evidence.

The local memory filter is an observed `heapUsed + external` below 96 MiB,
with at most 8 MiB retained growth across comparable warmed churn rounds.
`arrayBuffers` is already included in `external`; RSS is reported separately.
These are provisional Node engineering filters. Sampling can miss synchronous
peaks, and passing does not prove Cloudflare's memory limit is satisfied.

Admission precedes initialization and body buffering. The isolated handler
bounds active requests, waiting requests, request/response bytes and embedding
work. A cached initialization promise prevents concurrent first requests from
allocating duplicate indices. Paper validation is also bounded. These controls
must be retained in any later full-corpus deployment.

## Bounded compatibility canary

`src/run_full_probe_canary.py` supervises one child with a hard five-minute
deadline. It runs only after the tokenizer, numeric and geometry gates pass.
That deadline begins before child startup and includes source validation,
model setup and evidence validation. Each provider request checks the remaining
time before reserving its budget and caps its timeout to the remaining window.
Per-phase timings and the supervisor's completion record distinguish the total
process duration from measurements captured before final evidence validation.
Within that child, canonical validation and tokenization are reused once per
corpus/configuration. Every reuse rechecks the manifest and asset bytes; source,
query, code and environment bindings remain fresh. A changed input stops the
attempt. This removes repeated full tokenization without weakening the deadline.
The frozen plan has 16 distinct inputs and two repeated occurrences to compare
batch behavior. Every vector must have 768 finite values; normalized local and
Workers AI vectors must have cosine at least 0.999. The declared maximum
absolute difference for repeated batch embeddings is 1e-5.

An interrupted tokenizer scan can resume from its last committed checkpoint.
Recovery verifies the prefix hash and row/byte boundary before discarding an
uncommitted tail. Damage in the committed prefix or a stale fingerprint remains
STOP; recovery never accepts an incomplete scan as PASS.

Provider calls use the existing `CLOUDFLARE_ACCOUNT_ID` and
`CLOUDFLARE_API_TOKEN` environment variables. The runner requires an explicit
remaining free-neuron allowance before making calls. That value is an operator
confirmation, not an automatically queried billing balance. The fixed token
budget bounds this experiment, not other activity on the account.

An exclusive attempt ledger reserves provider calls before sending them.
Ambiguous failures still consume the reservation. There are no automatic
retries; a failed attempt needs inspection and a fresh run with newly confirmed
allowance. Local/provider vectors and repeat comparisons are retained for
independent recomputation. The REST endpoint is documented by
[Cloudflare](https://developers.cloudflare.com/workers-ai/models/bge-base-en-v1.5/).
This tests the provider model; it is not a new full-corpus Worker deployment.

## Long-run outputs

After the gates and user confirmation, the encoder writes the complete FP32
corpus, followed by frozen query vectors. The runtime packer emits int8 vectors
and fixed-width metadata with bounded text assets. The evaluator compares
actual JS/WASM rankings with an FP32 reference, including stable tie ordering.

The 2,000 extractive questions diagnose approximation fidelity. The 64
source-grounded, model-authored questions are development diagnostics. Neither
is representative held-out human evaluation. Report fragment recall, paper
hits, exact evidence containment and source read-window utility separately.
REST deduplicates top40 into at most eight papers; semantic MCP deduplicates
top25 into at most five, with separate catalog bypass/mixed-result behavior.

No real full-corpus quality result exists until that long run finishes.

## Running the stages

Ordinary PR CI runs the offline tests and bundle checks. Manual `Agent API`
dispatch with `static_probe=true`, `probe_runtime=durable-object`, and
`do_probe_phase=full` runs the new offline pipeline. Its default
`full_run_confirmed=false` disables all long encoding/evaluation steps.
`provider_available_neurons=0` also blocks provider calls by default. The prior
genuine-vector artifact is pinned by run, artifact ID and ZIP checksum and is
used only for numerical regression.

The workflow builds the complete corpus, freezes queries, installs the pinned
CPU environment, then runs `snapshot`, `tokenize`, `numeric`, the geometry
harness and `record-geometry`. It invokes the bounded canary only after those
checks pass. `aggregate` writes an explicit STOP or PASS certificate even when
an earlier gate failed. The full-corpus encoder and query evaluator revalidate
that certificate at their own entry points.

For local preflight after building the corpus and freezing its queries:

```bash
python src/preflight_full_search_probe.py snapshot \
  --corpus agent_full_probe --queries agent_full_probe/quality-combined-frozen.json \
  --out full-probe-reports/preflight
python src/preflight_full_search_probe.py tokenize --run full-probe-reports/preflight
python src/preflight_full_search_probe.py numeric \
  --run full-probe-reports/preflight --real-source agent_real_probe
python src/preflight_full_search_probe.py record-geometry \
  --run full-probe-reports/preflight --report full-probe-reports/geometry-memory.json
python src/preflight_full_search_probe.py aggregate --run full-probe-reports/preflight
```

`record-geometry` consumes the exact report generated by the reviewed harness,
not a hand-written PASS. The current memory result makes it and `aggregate`
exit nonzero. Fix the failed gate and obtain new evidence before enabling
`full_run_confirmed`; confirmation alone cannot turn a failed gate into PASS.

## Deployment compatibility

Deploying tokenizer v2 against an old active semantic release intentionally
returns `503 config_mismatch` for semantic search. Catalog, text and graph
operations retain reader schema 1. Production deployment therefore needs a
coordinated, separately reviewed index publication after compatibility and
quality checks. This draft experiment does not perform that publication.
