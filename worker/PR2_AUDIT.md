# PR #2 audit follow-up

The review targeted `132a1f6`. The first fixes landed in `8f23a2e`; this
follow-up checks all fourteen findings against that revision and repairs the
remaining cases. No live deployment, provider inference or full encoding was
used for this audit. The PR remains a draft.

The [subsequent review](PR2_SECOND_AUDIT.md) records the additional findings
against `8f23a2e`, later workflow/signature changes and remaining limitations.

| # | Finding and disposition | Regression evidence |
|---|---|---|
| 1 | Confirmed in the reviewed revision; already fixed. Main pushes validate only. Production requires an explicit manual confirmation on main. Actual re-encoding would also have required successful capacity/credential checks. | Actual job predicate tests reject push and default dispatch. |
| 2 | Confirmed. All four named dependencies now trigger validation. Publication remains explicitly manual. | Path tests cover cleaner, discovery writer, requirements and workflow. |
| 3 | Confirmed by interruption between records flush and checkpoint publication. Resume verifies the committed prefix, removes only the uncommitted tail and continues. | Interrupted integration test, partial/malformed tails, legacy checkpoints, corrupt committed prefix and stale binding tests. |
| 4 | Confirmed in the reviewed revision; already fixed. Missing probe flags cannot implicitly authorize production. | Dispatch intent tests, including matrix/real/full/collect combinations. |
| 5 | Confirmed. Public Worker routes require a per-run secret and 30-minute expiry before search, assets, cache reset or measurement logging. | Gateway tests verify forbidden/expired requests and unchanged cache after unauthorized cold reset; runner tests verify token destination and report omission. |
| 6 | Confirmed redundant canonical work. One canary execution reuses canonical tokenization while rechecking manifest/configuration and every asset's bytes on each reuse. Source/query/code/environment bindings are still refreshed. | Ten repeated uses require one canonical validation; changed bytes with restored mtime, manifest/config changes and initial mutation are rejected. Wall-time improvement has not been measured. |
| 7 | Confirmed; fixed in `8f23a2e`. Nullable/malformed error arrays neither crash cleanup nor prove resource absence. | Cleanup retry and exact not-found code tests. |
| 8 | Confirmed. Cancelled deployment now enters Worker cleanup. | Actual cleanup predicate tests cover success, failure, cancelled and skipped. |
| 9 | Confirmed in the reviewed revision; fixed in `8f23a2e`. Manual mutating Cloudflare modes share a concurrency group. | Workflow concurrency tests; log-only collection remains separate. |
| 10 | Confirmed. Failed corpus and readiness promises are cleared; later requests can retry initialization. | Asset failure shared by concurrent callers and transient storage failure both recover. |
| 11 | Confirmed. Pages enumerates discovery artifacts by exact name with pagination and verifies the producing run, instead of searching the last 20 successful runs. | Eighteen mocked API tests cover pagination, older production, forks, wrong workflows, expiry and request bounds. |
| 12 | Confirmed in fresh extractive preparation. Preparation and rebase now use all chunks containing the exact answer spans. | 137/2,000 original annotations expand; all 2,000 selected questions remain identical. The current rebased 2,064-question manifest was already correct. Historical files were not rewritten. |
| 13 | Confirmed. Reusable cache identity hashes selected numerical syntax and explicit model/config/dependency identity. Retention runs before encoding and before saving. | Comment/unrelated edit stability, numerical invalidation, namespace/byte eviction and path validation tests. Old identities are not relabelled. |
| 14 | Confirmed direct comparison; practical timing exploit was not demonstrated. All probe gateways now use native `timingSafeEqual` for equal-length token bytes. | Correct/incorrect same-length values and malformed/overlong inputs. |

Independent reviewers checked checkpoint recovery, workflow/auth wiring and
cache identity/retention after implementation. Local tests and dry-run bundles
do not establish deployed behavior or platform CPU/memory compliance.

Remaining limits:

- Last full-size local memory evidence is still STOP: 135.5 MiB observed peak
  versus the provisional 96 MiB filter. This audit did not rerun that workload.
- Auth and expiry stop unauthorized expensive work; rejected requests can still
  consume the shared request allowance. Expiry does not delete the Worker.
- A hard runner termination can prevent cleanup. Static synthetic assets remain
  downloadable; they contain no secrets.
- Discovery depends on retained, unexpired production artifacts. Pagination/API
  failures leave Pages static-only with a visible diagnostic.
- Each managed embedding cache root retains at most two numerical namespaces
  and 512 MiB of payload after pruning. Eviction causes recomputation only after
  normal full-run admission. The new identity schema causes one initial miss
  transition; existing vectors are not silently adopted.
- The 2,064 questions remain development/extractive diagnostics, not held-out
  human quality evidence. No search-quality or cost result was recomputed.
