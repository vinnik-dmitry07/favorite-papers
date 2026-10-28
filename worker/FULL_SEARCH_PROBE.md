# Full-corpus evaluation: fail before inference

This is an isolated offline experiment. It does not publish a release, change
the production Worker, alter discovery links, or enable a paid plan. The next
long run needs explicit user confirmation **after the reviewed code is pushed**.

The earlier 390-passage result covers three papers and tokenizer v1. Its
200/200 provider comparisons do not establish compatibility for tokenizer v2;
the historical bundle is not a valid current release. Those vectors are reused
only for numerical regression, with their original provenance retained. The
result does not establish full-corpus memory, retrieval quality or Cloudflare
CPU. The full source currently
contains 415 cards, 362 available texts and 53 explicitly unavailable texts.

## Current result and offline admission policy

The local 96 MiB diagnostic still fails: the ordinary Node workload observed
134.44 MiB after the two allocation changes. That number is not a Cloudflare
memory measurement. The subsequent [live full-size run](probe-results/cloudflare-2026-10-26-full-geometry.json)
completed all 327 attempts in 57.985 seconds with one object boot, no unexpected
HTTP error, and verified removal of the temporary namespace and Worker.
CPU attribution and numerical memory headroom remain unverified.

The revised admission decision concerns bounded compatibility testing and
**offline encoding/evaluation only**. `geometry-contracts` requires fresh local
coverage, provenance, initialization, queue, retained-growth and structural
checks, together with the fixed reviewed live evidence. The raw local report
keeps its FAIL and 96 MiB threshold; a peak-only failure does not prohibit
independent offline quality measurements. Every other local failure still
blocks the canary and long run. This does not approve production deployment.

The fixed pin `probe-results/full-geometry-admission-pin.json` binds the original
live report and cleanup hashes, stable corpus identities, and the deployed
runtime/build inputs. Changed corpus content, runtime code, dependencies or
configuration invalidate that evidence. Documentation/preflight changes can
reuse the historical experiment because the measured runtime is unchanged.
Fresh local evidence and certificates still expire after 24 hours and bind the
current checkout, environment and query set. Older certificates cannot pass
the revised policy hash. Run 40448979121 subsequently passed the provider
canary and completed all corpus/query embeddings. Its post-encoding validator
timed out before quality evaluation; the historical data were then evaluated
without further inference. See [the full quality readout](FULL_SEARCH_QUALITY.md).

### Historical October 25 comparison

The [2026-10-25 local report](probe-results/local-2026-10-25-full-preflight.json)
retains both memory runs and their exact compressed raw evidence. The first
full-geometry workload found cached snippets retaining complete paper strings.
Copying only the bounded snippet reduced retained memory after search churn
from 139.2 to 69.6 MiB and the observed peak from 207.1 to 135.5 MiB. The same
324 REST/MCP requests and 160 synthetic-vector searches were used in both runs.
The exact pre-fix implementation used for the "before" run was not committed.
Its raw observations and hashes are retained, but that baseline cannot be fully
reproduced from this repository alone. The comparison is historical evidence,
not a reproducible benchmark of the current checkout.

The unchanged 96 MiB peak filter still fails. All other measured memory/contract
checks pass, including queue limits, one index initialization and retained
churn growth below 8 MiB. This is a local Node result, not proof that Cloudflare
uses 135.5 MiB. The new provider canary has **not** started; the interrupted full encode has **not** resumed.
The diagnostic threshold is not raised or relabeled PASS. The current offline admission policy is described above.

## Why the order changed

The interrupted full encode found a tokenizer mismatch in Uni[MASK]
(`arxiv:2211.10869`): the pinned Hugging Face tokenizer recognizes literal
`[MASK]`, while the previous Python and Worker implementations split it into
punctuation and a word. Testing only the next uncached batch found that error
after model work had already started.

Tokenizer v2 preserves the pinned added-token semantics before normalization.
Its algorithm and configuration are bound into the build identity and local
encoder identity. The Workers AI embedding identity retains the legacy
provider payload: unchanged model-input text can reuse its previous provider
hash. This does not assert that a provider-side cache is populated, nor permit
relabeling locally encoded vectors across tokenizer versions. Reusable
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
The early summary counted 42,686 inputs: 40,575 passages, 2,064 queries and
47 regression fixtures. The executable gate adds two token-limit boundary
inputs, yielding 42,688. The committed summaries are historical; the gate
retains complete raw input/ID records as an execution artifact.
Unicode categories depend on runtime versions. The audit reproduced a
Python/Node mismatch for newly classified characters; corpus/fixture parity
does not establish universal Unicode parity or the Workers runtime's behavior.
Fresh tokenizer and provider canaries remain required for the current inputs;
the historical v1 subset cannot discharge those checks.

## Gates and decision scope

| Order | Evidence | Failure action |
|---|---|---|
| 1 | Source coverage, pinned model/config, frozen queries, code and dependency hashes | STOP on stale or incomplete input |
| 2 | All canonical Python/HF/Worker token IDs, no truncation, model never loaded | STOP before inference, including cache hits |
| 3 | Existing genuine vectors, independent int8 reference, JS/WASM, ties around top25/top40, actual REST/MCP routes | Fix packing, ranking or API contracts |
| 4 | Fresh full-size local contracts plus pinned live completion and cleanup on the same runtime/corpus; retain Node peak separately | STOP on any non-peak failure or stale live evidence |
| 5 | At most 32 local and 32 provider input occurrences, including repeats; the actual failing input, all five special tokens, Unicode and query/passage inputs | STOP on model/provider mismatch or unavailable allowance |
| 6 | Fresh certificate with every mandatory gate PASS, plus explicit long-run flag | Encode only after user confirmation |

Missing, expired, interrupted or unknown evidence cannot become PASS. Gate
reports preserve raw artifact hashes and earlier attempts. The certificate is
valid only for its exact source, canonical release, frozen questions, code,
dependencies and encoder identity. A change invalidates it. A partially
completed encode can resume from validated cache entries; completion attaches
the vector artifact atomically.

This certificate checks consistency and the declared acceptance policy. It is
not a signature, remote attestation, or independent proof that the commands
ran. A party able to rewrite source and reports can manufacture mutually
consistent files. Trust in execution comes from the reviewed workflow, runner
and retained logs/artifacts. Malformed retained tokenizer IDs, row order and
coverage totals are rejected, but shape validation cannot prove HF execution.

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
These are provisional Node engineering diagnostics. Retained growth remains a
blocking contract; the 96 MiB observed-peak result is retained separately from
offline admission. Sampling can miss synchronous peaks, and passing does not
prove Cloudflare's memory limit is satisfied. This distinction also applies
after genuine vectors are packed: quality runs require validated runtime
contracts, while a peak-only diagnostic failure is recorded without hiding it.

Admission precedes initialization and body buffering. The isolated handler
bounds active requests, waiting requests, request/response bytes and embedding
work. A cached initialization promise prevents concurrent first requests from
allocating duplicate indices. Paper validation is also bounded. These controls
must be retained in any later full-corpus deployment.

## Bounded compatibility canary

`src/run_full_probe_canary.py` supervises one child with a hard five-minute
deadline. It runs only after the tokenizer, numeric and geometry-contracts gates pass.
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
batch behavior. For the current corpus these 18 occurrences total 1,782 tokens,
estimated at 11 neurons under the pinned model pricing. The executable maximum
is 32 occurrences/16,384 tokens (100 estimated neurons); reserve that maximum
when authorizing the run. An operator assertion is not provider-verified quota. Every vector must have 768 finite values; normalized local and
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
The check is named `free_allowance_operator_asserted`, and the measured value
is `available_neurons_operator_asserted`; neither claims provider verification.

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

`worker/quality/full-query-pin.json` commits a hash of the complete ordered
question payload, cohort counts and source graph/text hashes. CI regenerates
the deterministic file and verifies this pin before installing the model
environment. Changing wording, answer spans, gold chunks, order or source
inventory requires a reviewed pin update. The newly pinned preparation has the
same 2,064 questions, spans and gold sets as the prior rebased manifest; 120
`source_chunk_index` bookkeeping values differ because preparation records the
original extraction chunk while rebase records the first containing chunk.

Extraction operates on overlapping chunks, so some queries begin inside a
sentence or word. Rendering boilerplate and duplicate passages also remain in
the source corpus. These known defects limit absolute retrieval conclusions.
Cleaning source text or selecting a new question cohort is a separately
versioned data change; silently changing this frozen diagnostic while tuning
retrieval would invalidate the comparison. No held-out quality claim is made.

The [October 28 retained-vector replay](FULL_SEARCH_QUALITY.md) now measures
all 2,064 frozen questions through the actual full int8 runtime. Fidelity to
FP32 passes; useful answer evidence and a deployed external-agent journey
remain separate evaluation requirements.

## Running the stages

Ordinary PR CI runs the offline tests and bundle checks. Manual `Agent probe`
dispatch through `agent-api.yml` with `do_probe_phase=full` runs the offline
pipeline when `static_probe=true` and `probe_runtime=durable-object` are also
selected. These explicit probe-intent flags are required. Its default
`full_run_confirmed=false` disables all long encoding/evaluation steps.
`provider_available_neurons=0` also blocks provider calls by default. The prior
genuine-vector artifact is pinned by run, artifact ID and ZIP checksum and is
used only for numerical regression.

The provider canary also requires `free_plan_confirmed=true`, a sufficient
operator-asserted neuron allowance and the selected credential pair. Probe
credentials default to the separate `probe_environment`; using repository
credentials requires an explicit selection. A full-run confirmation does not
bypass any of these conditions, stale live evidence, or a failed geometry contract.

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

`record-geometry` validates the report, retained bundle and source hashes
against the reviewed harness. This is a consistency check within the trusted
execution boundary described above. It records `geometry-contracts` for offline
admission and preserves the raw memory diagnostic. `aggregate` still exits
nonzero if any mandatory gate is missing or fails; confirmation alone cannot
turn a failed contract into PASS. After packing genuine vectors, the same
non-peak contract validation must pass before quality evaluation proceeds.

## Deployment compatibility

Deploying tokenizer v2 against an old active semantic release intentionally
returns `503 config_mismatch` for semantic search. Catalog, text and graph
operations retain reader schema 1. Production deployment therefore needs a
coordinated, separately reviewed index publication after compatibility and
quality checks. This draft experiment does not perform that publication.

## Reviewable long-run request

After review and push, one manual `full` dispatch can perform the fail-fast
checks, bounded canary, and (only after a fresh PASS and explicit confirmation)
complete offline encoding and diagnostic evaluation. Existing repository
credentials are selected explicitly. The workflow does not deploy a Worker.

```bash
gh workflow run agent-api.yml \
  -R vinnik-dmitry07/favorite-papers \
  --ref feat/static-search-probe \
  -f static_probe=true \
  -f probe_runtime=durable-object \
  -f do_probe_phase=full \
  -f probe_credentials=repository \
  -f free_plan_confirmed=true \
  -f provider_available_neurons=100 \
  -f full_run_confirmed=true
```

This example asserts at least 100 free neurons remain; it must reflect the
operator's actual allowance. Expected current canary use is 11 neurons. Full
corpus and 2,064 diagnostic query embeddings run on the GitHub CPU runner,
not Workers AI. Existing step bounds are 240 minutes for corpus encoding,
45 minutes for query encoding, 10 minutes for quality, and 350 minutes for the
whole job. These are ceilings, not promised durations. Partial verified cache
entries are retained. A short canary or prerequisite failure stops the long
steps and preserves its diagnostic artifacts.
