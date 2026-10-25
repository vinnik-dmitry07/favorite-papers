---
name: Full corpus fail-fast preflight
overview: Reject tokenizer, cache, packing, API, memory and encoder-compatibility failures before the long full-corpus encode, with explicit provenance and a fingerprinted STOP/GO certificate.
todos:
  - id: corpus-inventory
    content: Freeze all corpus inputs, source coverage, environment, budgets and the current 415-card / 362-text / 40575-row baseline.
    status: completed
  - id: tokenizer-cache
    content: Validate Python/Hugging Face/TypeScript IDs for every passage and frozen query before model loading; repair special tokens and cache identity.
    status: completed
  - id: packing-contracts
    content: Share packing mechanics without weakening provenance; test numeric correctness, source mappings, top25/top40 ties and real REST/MCP handlers.
    status: completed
  - id: geometry-memory
    content: Implemented and measured full geometry; memory filter FAIL at135.5MiB peak versus96MiB. Long encode remains blocked.
    status: completed
  - id: bounded-canary
    content: Prepare and validate a bounded changed-case local/Workers AI canary, including literal special tokens and both query and passage inputs.
    status: pending
  - id: certificate
    content: Aggregate only current complete evidence into a scope-specific certificate; make the full encoder reject absent, stale or incomplete proof.
    status: completed
  - id: review-push
    content: Run appropriate cheap validation, independently audit the implementation, push the reviewable code and request approval for the long encode.
    status: pending
  - id: full-encode-quality
    content: Only after explicit long-run approval and all mandatory gates pass, encode, pack and evaluate the complete real corpus and frozen cohorts.
    status: pending
isProject: false
---

# Full-corpus fail-fast preflight

## Implementation checkpoint

The implemented gates, current STOP, controlled memory comparison and reproduction commands are recorded in `worker/FULL_SEARCH_PROBE.md`. The geometry task is complete as a measurement, with a failed criterion; it is not a memory feasibility PASS. Local/provider canary and full encoding remain unrun.

## Goal and authorization

The requested outcome is a thorough sequence of cheap, decisive checks before restarting the approximately 106-minute, eight-CPU full-corpus encoding job. The user subsequently instructed: “после аудита запушь финальный код и запроси подтверждение на длительный запуск”. Implement and push the corrected, reviewable preflight code, then request confirmation for the long run. Passing a technical gate does not replace that confirmation.

The chosen design retains the canonical builder, pinned BGE encoder, exact int8 runtime and service contracts. It adds mandatory pre-inference validation and a certificate checked by the full encoder. The plan is a single targeted repair of candidate-42. Original candidates and audit remain unchanged under `/tmp/fail-fast-council/`.

No long model run, paid compute, production publication or deployment is authorized by this plan. A limited future canary must remain inside an explicitly verified free budget; inability to establish that budget produces UNKNOWN/STOP, not paid fallback. Shipping the code may finish with a truthful STOP report.

## Acceptance contract

| Requirement | Observable acceptance condition |
|---|---|
| R1 | Inventory, all-row tokenization, cache, packing/API and full-geometry failures are discoverable before model weights or full inference. Each phase has a hard budget and a nonzero failure exit. |
| R2 | All 415 current cards and 362 current canonical text bodies remain represented. Every text code point is covered, with explicit unavailable-text reasons. Current 40,575 chunks are an observed baseline, not an immutable requirement after a tokenizer fix. No hidden exclusions or truncation. |
| R3 | Canonical Python, pinned HF and Worker token IDs agree for every passage, including cache hits, and every frozen query after its template. Model/query/passage identities, token digests and cache/resume rules are verified. |
| R4 | Shared real packing and exact JS/WASM mechanics match an independent quantized-cosine oracle. Actual REST 40→8 and MCP semantic 25→5 contracts, catalog routing, paper deduplication, boundary ties and retained passage mappings are exercised. |
| R5 | Actual full metadata/text geometry is tested with explicit synthetic vectors, one resident index, bounded loading/requests/queues and serialization. Node memory evidence remains local evidence; Cloudflare memory/CPU is separate. |
| R6 | Planning and implementation validation do not perform the long encode, paid inference or production deployment. Any later small live canary has text, token, time and free-cost ceilings. |
| R7 | Machine-readable phase evidence includes exact fingerprints, budgets and outcomes. Missing, unknown, failed, timed-out or stale mandatory evidence blocks GO. Long-run execution also requires the user's explicit confirmation. |

## Verified starting facts and unknowns

These are audit-time observations, not claims that repaired code or gates have passed.

- `agent_full_probe/probe.json` contains 415 cards, 362 text papers and 40,575 rows; `embeddings` is absent/null and no full `vectors.f32` is available. The prior encoder stopped after 1,360 newly encoded rows with 582 cache hits reported at its start.
- The preserved mismatch is row 6734, `arxiv:2211.10869`, chunk 44: at token 50 canonical tokenization gives `[`, `mask`, `]`, while pinned HF gives `[MASK]`. Preserve the full offending input as a regression fixture. Fix tokenizer semantics, not source text.
- At audit time `BgeEncoder.__call__()` loaded tokenizer and model together through `_load()` before checking IDs. `encode_probe()` skipped this comparison for cache hits. `embedding_signature()` did not bind tokenizer implementation; the encoder implementation string was manually versioned.
- `agent_real_probe` has 390 genuine vectors across three papers. These can support numerical smoke testing but cannot produce five/eight distinct-paper pages.
- `pack_full_search_probe.pack()` and `createFullCorpusStore()` accept genuine full-corpus manifests and reject synthetic provenance. The current memory harness's `--data-label geometry-fixture` is only a report label, not a fixture admission path.
- `FullSearchIndex` uses exact cosine over quantized vectors. `service.search()` oversamples `min(40, k*5)` before paper deduplication. `researchSearch()` bypasses semantics for exact catalog matches; otherwise it adds up to three catalog records to up to five semantic hits.
- The 64 natural questions in `worker/quality/full-natural-questions.json` are model-authored development cases. The 2000 extracted sentences are fidelity diagnostics. No full-corpus quality result has been observed. Neither cohort is human-heldout evidence.
- Historical gateway CPU remains unverified. This does not measure local encoding correctness and is not a prerequisite for independent offline computation. It still prevents a claim of proven platform feasibility.

## Dependency-ordered work

### 1. Inventory and immutable baseline — no inference, ≤2 minutes

Add the inventory/certificate entry point in new `src/preflight_full_search_probe.py`; reuse `canonical_inputs()` and extract reusable validation currently embedded in `pack()` where appropriate. Record source graph and text hashes, complete canonical manifest/files/rows, 415/362 counts, unavailable reasons, offsets and code-point coverage, vocabulary/config/model revision, both question cohorts, HEAD, dirty relevant-file hashes, environment/dependency versions and cache inventory. HEAD alone is insufficient in a dirty checkout.

The initial baseline records 40,575 chunks. After a tokenizer correction, rebuild canonical chunks if necessary and create a new baseline with old/new counts and identities. Assert equality of all source/canonical text bodies and card sets, complete source coverage and no silent truncation. If gold chunk indices change, rebind labels from unchanged answer spans or regenerate the deterministic extractive freeze before retrieval, recording a new freeze identity. Do not reselect questions after seeing rankings.

Completion evidence: a bounded inventory JSON with provenance and per-file sizes; failures identify the paper, row or asset. Preserve old cache and reports for diagnosis.

### 2. All-input tokenizer audit and cache identity — no inference, ≤10 minutes plus ≤3 minutes for focused cache tests

Separate pinned `AutoTokenizer` initialization from model loading in `src/embed_real_search_probe.py`. The all-input preflight must not import/construct `AutoModel`, initialize Torch inference or instantiate model weights. Stream or batch token checks without retaining an unnecessary corpus-sized matrix of token IDs.

For every passage, including cache hits, compare exact Python canonical, pinned HF and `worker/src/tokenize.ts` IDs. Check every frozen query after the actual query template. Add fixtures for literal `[MASK]`, `[CLS]`, `[SEP]`, `[PAD]`, `[UNK]`, Unicode, controls, accents and 511/512/513-token boundaries. The over-limit case must demonstrate the expected rejection rather than truncate; its expected rejection is not a corpus mismatch. The saved failing passage is mandatory.

Report aggregate mismatch count and bounded examples with row/paper/chunk/input hash, lengths and first divergent ID. A mismatch in the last row, including a fully cached row, must cause zero encoder calls. Any unanticipated mismatch or oversized real input is STOP.

Bind passage and query caches to actual token-sequence digests, tokenizer implementation/config/vocabulary, model revision, templates, pooling, normalization, encoder implementation and relevant library versions. An implementation change invalidates the namespace. Reuse old bytes only with an explicit migration proving identical model inputs and model identity. Use a fake encoder to verify interrupted resume, unchanged-input reuse, corrupt-cache rejection, and no partial manifest publication; these tests need no genuine model invocation.

Completion evidence: tokenizer report with all expected passage/query counts, identities, digests, mismatch counts and zero-inference assertion; cache/resume test results.

### 3. Packing, kernel and API contracts — no inference, ≤5 minutes

Extract a pure packing core from `src/pack_full_search_probe.py` while retaining strict real-manifest admission in its public real entry point. Reuse the same rounding, norms, metadata serialization and sorted order in every fixture and real path. Do not relabel a three-paper subset as the full corpus.

Test finite normalized FP32 validation, per-row maxabs int8 quantization, tie-to-even rounding, endianness, shard edges, source-row bijection, shuffled source input, checksum/missing-shard rejection, invalid source index, duplicate IDs, non-finite vectors and exact score ties. Compare JS and WASM against an independent scalar cosine oracle over the packed integer bytes and norms. FP32-versus-int8 differences are a separate fidelity diagnostic, not the numerical correctness oracle.

Use the existing 390 genuine vectors only when their input/model identity remains verified after the repair. Add an explicitly synthetic fixture with at least nine text papers and more than 40 rows, duplicate-paper winners and equal scores crossing ranks 25 and 40. Exercise real REST and MCP handlers plus response serialization, not only `service.search()`:

- REST `k=8`: exactly the selected top40 candidates feed deduplication, with expected retained eight papers when the fixture permits it.
- MCP semantic `k=5`: top25 selection and expected retained five papers; preserve exact chosen passage/snippet/source offsets.
- Exact catalog title/identifier routing: bypass embeddings, including unavailable-text cards and fetch behavior.
- Mixed research routing: catalog records plus semantic results; do not assume total MCP result count is always five.

Completion evidence: deterministic assertion results plus source and compiled WASM hashes. Reuse focused Python/Worker tests and `npm run typecheck`; do not claim an index-only harness proves API behavior.

### 4. Honest full geometry and bounded memory — no inference, ≤10 minutes

Add a separate synthetic fixture builder that consumes the verified full canonical graph/text/rows and deterministic normalized vectors at the current baseline's full `N×768` geometry. Its manifest must say `synthetic:true`, non-publishable, with seed/generator identity, source hashes and vector digest. It must not fabricate genuine BGE `source_embeddings` fields.

Add an explicitly test-only loader envelope that validates the fixture and delegates to shared binary/index/store mechanics. The normal real loader must continue rejecting that fixture; test this negative case. Derive report provenance from the admitted manifest, not an arbitrary CLI label.

Extend `worker/probe-kernel/full-memory.ts` to use streamed assets, cold concurrent first requests, largest paper, distinct content requests, search churn, repeated initialization attempts, actual REST/MCP serialization and bursts above the admission limit. Enforce one shared in-flight initialization and resident index, sequential shard loading, bounded active requests and embeddings, one distinct paper-validation task at a time, a finite pending queue and deterministic overload behavior. Record exact configured limits; observing four concurrent requests does not establish a limit. Keep synchronous shared query-buffer use explicit.

Apply existing provisional local policy: observed `heapUsed + external <96 MiB`, comparable post-GC churn growth `≤8 MiB`, one index/metadata load, no full FP32 residency, bounded cache cardinality/bytes and streams. Do not add `arrayBuffers` to `external` a second time. Instrument loader/hash/decode/serialization allocation boundaries because interval samples can miss synchronous peaks. Report a conservative structural allocation account alongside measured samples.

Audit-time geometry: WASM allocation 486 pages = 31,850,496 bytes; metadata 5,193,600 bytes; one full shard 3,145,728 bytes; references 614,400 bytes; largest actual paper JSON 635,900 bytes. Recompute after a baseline change. These figures omit object/string/cache/runtime overhead. The 96/8 thresholds are provisional engineering filters, not demonstrated platform margins. Node PASS cannot become Cloudflare memory or CPU PASS. A local workerd result, if available, remains separate from platform telemetry.

Completion evidence: provenance-valid memory report, configured/observed bounds, largest-size inventory, structural allocation account, cold/burst tests and measured local outcome. Threshold failure or an unbounded queue/index lifetime is STOP.

### 5. Bounded changed-case encoder compatibility — ≤5 minutes, never the full run

After gates 1–4 pass, prepare a fixed canary with the saved failure, all literal special-token types, Unicode and near-limit inputs, and both actual query and passage templates. Compare local pinned BGE against intended Workers AI outputs, keeping every exact input/token digest and both encoder identities. Existing 200-passage compatibility evidence applies only to its original manifest/coverage; it cannot certify the new special-token case.

Set ceilings before execution: at most 32 input occurrences per provider, at most 16,384 input tokens per provider, five minutes total and no retries beyond those ceilings. Include repeated/batched cases inside the same budget. Require finite 768-dimensional vectors, minimum cosine 0.999 for every comparison, explicit pooling/normalization, and declared batch-invariance tolerance. Confirm sufficient remaining free allowance before any live call; if not demonstrable, record UNKNOWN and stop this gate. Never deploy production merely to obtain the canary.

A canary runner encodes selected validated inputs directly. Do not fabricate completed passage embeddings to satisfy the existing `encode_queries()` helper, which requires them. Freeze canary inputs before results. Report actual throughput only if measured, with batch/thread identity; the prior 106-minute estimate is historical.

Completion evidence: a bounded, identity-bound comparison report. A mismatch, missing required case, malformed vector, quota uncertainty or timeout cannot pass the intended-path gate. Implementing or pushing the code does not require executing a live canary now.

### 6. Aggregate evidence and enforce the launch boundary

The new preflight entry point must expose executable phase/report aggregation commands and document their actual CLI in `worker/README.md`. Add an explicit certificate argument to the full encoder. These are proposed interfaces to implement; do not document nonexistent flags as already available. A single aggregator validates evidence schemas and dependencies rather than trusting a human-written summary status.

Each gate records: status, scope, required/optional classification, input/output and implementation hashes, environment versions, expected and checked counts, budgets, actual elapsed time and failure reason. The overall fingerprint binds canonical baseline, tokenizer/model/templates/cache identity, frozen questions/canary, packer/runtime/service/handler/fixture implementations and compiled kernel. Recompute it at launch. A source edit or changed relevant dependency invalidates affected evidence; a new HEAD with identical relevant bytes must still be reported accurately.

For the intended remote-query design, all gates above are mandatory for `GO_FOR_FULL_OFFLINE_ENCODE`; a missing targeted provider canary leaves the overall result STOP even if local checks pass. If a separate purely offline diagnostic mode is later chosen, give it an explicit different scope and prerequisites; never use it as an alias for the intended-path GO. Historical gateway CPU and actual Cloudflare resource feasibility stay separate platform UNKNOWNs and do not masquerade as local encoder requirements.

No report alone authorizes the long run: after cheap tests and independent implementation audit, push reviewable code, summarize actual PASS/STOP/UNKNOWN states and request the user’s explicit confirmation. Any remaining mandatory failure must be resolved before a subsequent approved run starts.

### 7. After approval and current GO: full encode, then full quality

Only then start full inference with checkpointed cache, first-error stop, watchdog, measured ETA and a declared wall-time limit. Preserve all canonical rows. After completion, perform full genuine packing and source revalidation, complete query vectors, actual-runtime rankings and `src/evaluate_full_search_probe.py`.

These late checks require full real vectors and therefore are not early gates: complete FP32 reference rankings, full int8 fidelity, complete 2000+64 quality diagnostics and final real artifact validation. `worker/probe-kernel/full-quality.ts` loads both JS and WASM indices; it is not the memory harness or full API contract test. Report fidelity, natural development metrics, human-heldout quality and platform feasibility separately; the latter two remain unverified without their own evidence.

## Validation and initial gate status

Existing grounded commands include `python -m pytest` for affected `src/test_*.py`, and `npm test` / `npm run typecheck` from `worker/`. New preflight/fixture/canary commands must be wired and documented by their implementing changes. Bound subprocesses with real timeouts; a budget overrun writes STOP/UNKNOWN and does not silently continue. Initial cheap phase ceilings total at most 30 minutes plus the optional-to-execute, mandatory-to-GO five-minute canary. They are policy ceilings, not measured runtime predictions.

| Gate | Status at plan adoption | Evidence needed to change status |
|---|---|---|
| Inventory and preserved coverage | PENDING | Current verified baseline and fingerprints |
| All-input token parity | KNOWN FAILURE | Regression fixed; exhaustive three-way report passes |
| Cache identity/resume | PENDING | Identity-bound fake-encoder tests and migration policy |
| Packing/kernel/API | PENDING | Full boundary fixtures and real handler assertions |
| Full-geometry local memory/concurrency | PENDING | Honest fixture, bounded runtime and measured report |
| Changed-case provider compatibility | UNVERIFIED | Current bounded local/Workers AI evidence |
| Full offline encode | STOP | Mandatory current GO and explicit user confirmation |
| Complete real quality | NOT RUN | Completed full real vectors and frozen evaluation |
| Cloudflare CPU/memory/free hosting feasibility | UNVERIFIED | Separate valid platform evidence |

## Audit findings resolved by this repair

| Finding | Change adopted |
|---|---|
| Fixed chunk count could reject a legitimate tokenizer repair | Step 1 preserves texts/coverage and permits an explicit revised chunk baseline; compatible import from candidate-17. |
| Three-paper subset cannot exercise eight/five results | Step 3 adds a ≥9-paper, >40-row boundary fixture while retaining the genuine numerical smoke. |
| MCP catalog routing and wrappers omitted | Step 3 tests exact bypass, mixed route and real serialized handlers; compatible import from candidate-08. |
| Fixture label alone cannot pass strict real loaders | Step 4 adds an honest separate envelope and shared core, with real-loader rejection. |
| Four-request test does not enforce a bound | Step 4 requires singleton initialization, finite admission/queues and overload tests. |
| FP32 reference conflated with quantized correctness | Step 3 separates exact quantized oracle from FP32 fidelity. |
| Old compatibility omitted the failing special token | Step 5 requires new bounded changed-case query/passage evidence. |
| Missing old gateway CPU would unnecessarily block independent local work | Step 6 retains separate platform UNKNOWN; compatible import from candidate-08. |
| Partial/stale evidence could accidentally permit inference | Step 6 requires complete schema-validated, launch-verified evidence and user approval. |

Three neutral candidate plans were reviewed in a fresh evaluator context in order 42, 08, 17; authorship was not inferred. This document is the one allowed targeted repair, not a concatenation or a new council. No model-diversity claim is made. Implementation correctness and evaluation gains remain unproven until actual evidence is recorded.

Revisit only the affected step if canonical text changes, token semantics or chunk geometry changes, a shared core cannot preserve real/fixture separation, enforced concurrency differs from the tested bound, the free canary budget is unavailable, or a measured phase exceeds its ceiling. Do not respond by dropping texts, weakening mandatory gates, relabeling synthetic provenance or moving a decisive cheap check after full encoding.
