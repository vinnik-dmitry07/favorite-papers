# Follow-up to the audit of 8f23a2e

The supplied review contains seven medium-priority findings (C1–C7) and fifteen
lower-priority findings (N1–N15). It predates `3e73e30`, which already repaired
several of them. This follow-up distinguishes code fixes from evidence limits;
it does not claim production readiness or permission for a long run.

| Finding | Disposition |
|---|---|
| C1: Cloudflare secrets exposed to dependency installation | Fixed: credentials are step-scoped; probe defaults to a dedicated environment. Repository credentials remain an explicit choice. Install/test/full-encode steps receive no Cloudflare secrets. The canary and API operations still need their selected token; dependency packages are not a security sandbox. |
| C2: public Worker, cancellation and leftovers | Auth/expiry/cancelled cleanup were fixed in `3e73e30`. Added read-only leftover-Worker inventory before deployment. It blocks workload and never deletes discovered resources automatically. |
| C3: tokenizer-only change invalidates provider vectors | Fixed by preserving the exact legacy main provider signature (`df512606…`), with the full tokenizer configuration in the build signature. Same-slot and cross-slot cache reuse have regression tests. All 40,575 saved passage inputs/ranges are unchanged; only 97 token counts differ. Actual remote cache availability was not checked. |
| C4: synthetic CPU is not production CPU | Confirmed scope limitation. Documentation now explicitly lists route/candidate/cache/rate-limit differences. Historical results apply to that implementation, not all Worker designs. |
| C5: self-consistent gate files are forgeable | Trust boundary corrected: checksums establish consistency, not trusted execution. Garbage token IDs now fail structural/order/coverage validation. A repository writer can still fabricate plausible files or change the verifier; no signature or attestation claim is made. |
| C6: question freezing and data quality | Added a committed digest of all ordered query records and source inventory, checked before model setup. Gold coverage was fixed previously. Text/answer/gold selection is unchanged. Truncated extractive questions, boilerplate and duplicates remain known data-quality limitations; this is not held-out human evaluation. |
| C7: production depends on experimental tests | Fixed: `agent-publish.yml` is production-only **Agent API**. Existing `agent-api.yml` becomes **Agent probe**, preserving its dispatch entrypoint. Production validation no longer builds the probe fixture/WASM or runs its tests. |
| N1: squash breaks ancestry pin; assert removable | Fixed: exact historical run, source commit, artifact and archive SHA replace ancestry. Explicit checks survive Python optimization. Artifact expiry still fails closed and requires a reviewed replacement pin. |
| N2: host Unicode version mismatch | Confirmed known limitation. Local Python 3.12/Unicode 15 and Node 24/Unicode 17 disagree on `price 100\u20c1`. Corpus/fixture parity does not prove universal Unicode parity. Shared pinned Unicode semantics remain future work; a host version added to the signature alone would not fix it. |
| N3: mixed package indices | Removed `--extra-index-url`. Torch CPU is installed separately from its index; other dependencies resolve through PyPI. This reduces index ambiguity but is not a fully hash-locked transitive dependency set. |
| N4: cache corruption and execution provenance | Damaged entries become misses after admission/input validation; exact managed files are removed and recomputed. Execution parameters are retained per entry. Semantic reuse does not promise bitwise equality across batch/thread settings or attest that a model ran. |
| N5: direct token comparison | Already fixed in `3e73e30` with native `timingSafeEqual`. No practical timing exploit was demonstrated. |
| N6: stalled bodies occupy admission indefinitely | Fixed: absolute five-second body-read deadline and abort handling; cancellation cannot indefinitely retain a permit. Tested twelve stalled uploads and a never-settling cancellation callback. Service/AI work has a separate lifetime. |
| N7: buffered assets and inherited graph properties | Removed the redundant raw-buffer promise map; asset reads enforce streaming byte/chunk bounds. Graph neighbors use `Object.hasOwn`. The old local predicate was weak, but reverse-edge validation already rejected the simple inherited-key payload; end-to-end acceptance was not reproduced. |
| N8: failed initialization promise retained | Already fixed in `3e73e30`; concurrent failure and subsequent recovery are tested. |
| N9: snippet test does not prove memory release | Renamed and documented as a semantic Unicode/bounds regression. Retention is supported by the separate memory experiment, not this unit test. |
| N10: exact pre-fix memory implementation unavailable | Explicitly marked historical and not fully reproducible from committed code. Original raw measurements remain unchanged. |
| N11: 200/200 provider checks used tokenizer v1 | Explicitly documented. The historical bundle does not establish current v2 compatibility or satisfy the new canary. |
| N12: allowance described as provider-verified | Renamed to `free_allowance_operator_asserted`; the integer allowance and declared source are validated. No automatic account-balance verification is claimed. |
| N13: inconsistent gzip ignore exceptions | Added a scoped `worker/probe-results/*.json.gz` exception, keeping private export rules intact. No historical evidence or public metadata was rewritten or republished. Future evidence still requires content review. |
| N14: npm test needs unmentioned build; WASM unpinned | `pretest` builds the kernel; build output must match committed `scan.sha256`. Production tests bypass the probe build. Local real-subset instructions include both CPU dependencies and the kernel build. |
| N15: documentation drift | Updated workflow names/defaults/flags, Free confirmation, local authentication, reproduction output, provider signature semantics, evidence scope and 42,686 versus 42,688 input counts. |

Validation: 586 Python tests, 170 default TypeScript tests, 21 Pages tests,
both typechecks and three Wrangler dry-run bundles passed. Two opt-in real-vector
tests remain skipped. A source-only corpus rebuild retained 415 cards, 362
texts, 40,575 passages and 7,867,965 tokens; the reviewed 2,064-query pin passed.
No embeddings, provider calls, live deployments or full memory workload ran.

Independent follow-up reviewers checked the workflow/credential/fixture split,
cache recovery, stream deadlines and evidence/query-pin changes. The original
review used a minimal pytest-compatible runner; the tests above used the actual
installed pytest and Vitest runners.

The last full memory measurement remains 135.5 MiB versus the provisional
96 MiB filter. Current code needs fresh gates; the historical measurement is
not a certificate for this revision. Long execution remains blocked pending
memory work and explicit confirmation. Unicode coverage and diagnostic data
quality are separate open limitations.
