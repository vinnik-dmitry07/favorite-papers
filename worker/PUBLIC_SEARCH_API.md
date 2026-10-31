# Permanent REST and MCP search

The `publish` phase of **Agent probe** publishes a separate permanent Worker,
`key-papers-search`, with the authenticated 40,575-passage index. It restores
existing vectors; it does not encode the corpus, use Vectorize or R2, upgrade the
Cloudflare plan, replace `key-papers-api`, or merge the pull request.

The permanent API was published by [run 41007245038](https://github.com/vinnik-dmitry07/favorite-papers/actions/runs/41007245038)
at runtime commit `abe903d8c3e6ef39da0c57b20f10283ec76771c3` on
2026-10-30 UTC. Start at
[the public agent manual](https://key-papers-search.vinnik-dmitry07.workers.dev/llms.txt),
use [REST/OpenAPI](https://key-papers-search.vinnik-dmitry07.workers.dev/openapi.json),
or connect [MCP](https://key-papers-search.vinnik-dmitry07.workers.dev/mcp).
Publication remains manual; the stable Worker stays deployed after the job ends.
The [publication evidence](probe-results/public-publication-41007245038.json)
records the exact deployed identity and the limits of the checks.

## Publish

Future publications require current `main`, GitHub environment **public-search**,
a required reviewer, and exactly one deployment branch rule: branch `main`.
The job reads the actual environment rules before restoration or Cloudflare
access. A stale queued commit is rejected again immediately before live deploy.
The dedicated environment secrets are `PUBLIC_SEARCH_CLOUDFLARE_ACCOUNT_ID` and
`PUBLIC_SEARCH_CLOUDFLARE_API_TOKEN`; production/probe credentials are not used.

Use Cloudflare's [per-Worker Editor role](https://developers.cloudflare.com/workers/authorization/workers/)
for the existing `key-papers-search`, including its Previews. Do not grant
account-wide Workers Admin, DNS, R2, Vectorize or token-administration access
merely for this path. The deploy token cannot necessarily read its own policy;
a successful operation does not prove least privilege. After reviewing the
actual token scope, bind that exact credential's SHA-256 to environment variable
`PUBLIC_SEARCH_TOKEN_SCOPE_SHA256`. Reports explicitly label this review as
operator-attested, not machine-verified. Token rotation requires another review.

The connected GitHub tools cannot administer environment settings. Run this with
the repository owner's `gh` login after reviewing the token in Cloudflare:

```bash
python src/public_search_release.py setup --reviewer vinnik-dmitry07 --set-credentials --token-scope-reviewed --report public-api-reports/environment-setup.json
```

It configures required review and main-only branches, disables admin bypass,
removes other deployment rules, then sets the two secrets using hidden prompts.
For this single-maintainer setup, self-review is permitted; a reviewer can approve
their own manual dispatch. Nothing is deployed. Setup uses standard-library
Python and `gh`; credentials are never passed as command arguments or printed.
The command is tested with mocks. Actual account rules and token permissions
have not been changed by pushing the code. Environment-only secret placement is
part of setup: YAML cannot prevent an administrator from changing protections.

After review and merge, dispatch a fresh run; re-running an old job uses old code:

```bash
gh workflow run agent-api.yml --repo vinnik-dmitry07/favorite-papers --ref main -f static_probe=true -f probe_runtime=durable-object -f do_probe_phase=publish -f free_plan_confirmed=true
```

The earlier feature-branch publication with repository credentials is historical
evidence, not the current procedure. Pushes and PRs do not deploy Cloudflare.

The job requires the permanent Release archive and verifies reconstruction
without encoding. It then deploys a run-specific **Worker Preview**, with isolated
DO storage, its own secret, a private gateway and a 20-minute gateway expiry.
REST/MCP and model checks run there first. Cleanup deletes only this Preview
after every creation attempt. If candidate verification or cleanup fails, live
code is untouched. These are [Worker Previews](https://developers.cloudflare.com/workers/previews/),
not Version URLs. Preview responses use a preview credential; research checks
on the permanent endpoint remain anonymous.

Activation requires the retained 200-input baseline and **32 new model checks
for this publication**, cosine at least 0.999, completed within the previous
hour. The inputs are deterministically spread across the pinned reference set.
Old publications cannot satisfy the fresh gate. Baseline reuse is labeled.

Immediately before live deploy, the job records the exact previous version,
corpus and public identity. Failed or cancelled validation attempts to pause the
new publication and then restores that exact code version. The runner verifies
the previous identity and activation; it refuses to overwrite a later release.
Uncertain recovery remains unverified. No namespace or database is restored.
Activation/pause records are publication-specific, so previous state survives;
all charged daily ledgers stay charged. Class lifecycle changes require a new
recovery review. The first approved rollback target is the reviewed `abe903d`
publication; later targets must advertise this state-preservation protocol.

Local tests exercise these failure paths. Preview support, production rollout
and rollback still need an authorized live Cloudflare run. Tests do not certify
platform memory or production readiness. The changed loader still does not match
the historical live-geometry pin; that pin has not been rewritten.

## Use the endpoint

Given the verified origin as `API_BASE`, a browsing agent can start at
`API_BASE/llms.txt`, then make ordinary GET requests:

```text
/v1/catalog?q=DeepSeekMath
/v1/citations?id=arxiv:2402.03300&dir=in&limit=24
/v1/search?q=group%20relative%20policy%20optimization&k=5
/v1/contents?id=arxiv:2402.03300
/v1/content?id=arxiv:2402.03300&offset=0&length=6000
```

Follow citation `next_cursor`, catalog `next_offset`, and content continuation;
copy `corpus_version` into subsequent reads as `version`. Content ranges count
Unicode code points. A graph edge means a citation within this catalog, not all
citations on the internet. Use catalog keyword lookup and more reading when the
first semantic hit is insufficient.

Remote MCP clients use `API_BASE/mcp`, with no authentication for research tools.
The existing `search`/`fetch` pair and advanced navigation tools are unchanged.
`API_BASE/openapi.json` describes the REST interface. Hosting these endpoints
does not automatically register a connector in a client. Whether a particular
web agent can open this host still needs an external-agent check after publishing.

The current main-branch Pages deployment trusts its existing production discovery
workflow. This feature-branch publication does not alter that trust policy or
advertise an unverified URL on Pages. Its root, `llms.txt`, OpenAPI document, and
workflow discovery artifact provide the immediate entrypoints. Pages discovery
can be connected when the publication path is merged and verified.

## Bounded AI work on the shared Free account

The stable DO owns global UTC-day ledgers independent of publication IDs:
1,000 query inputs (512,000 reserved tokens), 200 baseline inputs (102,400 tokens),
and 200 fresh-check inputs (102,400 tokens). The old baseline ledger format and
ceiling stay unchanged for rollback compatibility. Preview storage/ledgers are
separate; its bounded verification work consumes additional shared account AI.
These application reservations are not an account-wide allocation or bill cap.

Uncached searches also share **200/day and 20/minute per client IP** across REST
and MCP. The client reservation is atomic with the global query reservation,
after actual AI admission. Cached answers, exact title matches and catalog,
text and citation reads do not consume embeddings. HTTP 429 reports the correct
minute/day `Retry-After`. Shared proxies share an allowance; distributed clients
can still exhaust the global quota. This is a fairness bound, not a complete
anti-abuse or authenticated per-user system. Stored address keys use a random,
durable private salt; raw client addresses are not stored in the limiter.

Reservations survive ambiguous failures, HTTP timeouts, restarts and rollback.
At most four provider promises remain pending. A full provider pool rejects a
new request before charging it. Research admission remains four active plus
eight queued requests with a two-second wait; this is a deliberately bounded
service, not an arbitrary-throughput promise. Provider HTTP timeout is 20 seconds.

Compatibility, activation and pause state are scoped by manifest and publication.
A matching baseline may be copied; fresh checks cannot be inherited. Historical
activation/pause records remain untouched. Expired daily counters reset before
validation; counters above a reduced cap return exhaustion instead of poisoning
catalog access. Corrupt AI state stops semantic operations and degrades health,
while valid catalog/text/graph data stays accessible. Another corpus still needs
a reviewed manifest, data/config update and fresh checks.

Cloudflare documents [SQLite Durable Objects on Free](https://developers.cloudflare.com/durable-objects/platform/pricing/)
and a [30-second default DO CPU limit](https://developers.cloudflare.com/durable-objects/platform/limits/),
which differs from the ordinary Worker Free CPU limit. The outer Worker only
routes requests; index loading and search run inside the DO. The [Workers AI
allocation](https://developers.cloudflare.com/workers-ai/platform/pricing/) is
10,000 neurons per day on Free, shared with other account workloads. Application
counters are not provider billing telemetry or a reservation of that account
allowance. Other traffic can exhaust platform request, storage or AI quotas;
Free-plan operations can then fail. This implementation does not promise
unlimited availability or establish the account's plan from a workflow flag.

## Pause and recovery

Administrative routes require the run's generated `x-publication-token`, with
`x-publication-id` binding mutations to the intended publication. They are not
research tools. Routes include state, compatibility, fresh-compatibility,
activate, deactivate and explicit reset of a failed baseline check. Reset never
refunds reservations. Failed fresh checks are not automatically retried.

Emergency `POST /admin/deactivate` writes only the publication's pause latch,
without loading assets, validating AI state or waiting behind research requests.
The CLI's `--deactivate-only` verifies its identified receipt directly. Only a
successful activation clears that publication's latch. A later publication and
code rollback do not erase prior ledgers or activation records.

Transient asset HTTP/network/stream failures retry after a shared five-second
backoff. Hash/schema/configuration failures remain latched for the immutable
release. This patch is pushed, not deployed; historical publication evidence
continues to describe its original runtime.

The original Actions artifact expires on January 25, 2027. **Preserve search
corpus** copies its 149,682,694 authenticated bytes to the
`retained-search-corpus-2026-10-26` GitHub Release and downloads them again to
verify the SHA-256. Existing assets are never overwritten. The workflow calls no
model or Cloudflare service. Future public publications require this Release,
so Actions expiry cannot trigger re-encoding. Wrong bytes stop before deploy.
Release assets have no Actions retention deadline; repository owners can still
delete them. The deployed Worker never downloads this archive during a request.

## Validation before the first publication

The retained artifact was restored locally with the historical hash checks intact:
40,575 passages and the same packed manifest. The permanent Worker passed a
Wrangler deployment dry-run with those assets (about 352 KiB gzipped script).
The full TypeScript suite passed 204 tests with two optional skips, and typechecking
passed. Python publication and existing workflow regressions passed; the focused
publication/workflow list contained 79 tests (the earlier summary said 80).
These checks preceded the
successful live publication described above.

Independent review checked authorization, durable reservations, activation,
provider timeouts, public contracts and publication failure handling. It led to
separate admission for still-pending AI calls, moving OpenAPI schema generation
inside the DO, and accepting legitimate catalog-only MCP search results in the
publication validator.

## First permanent publication

All four public integration checks passed: discovery/admin isolation, catalog/
graph/reading, REST query and reformulation, and MCP search/fetch. Of 37 HTTP
attempts, 36 returned 200 and one intentionally unauthenticated admin request
returned 403. All 200 compatibility inputs passed (minimum reported cosine
0.9999992676). Independent offline replay verified the pinned indices, all 67
incoming DeepSeekMath citation IDs, three 6,000-code-point REST reads and one
16,000-code-point MCP fetch against the canonical corpus. Raw provider vectors
are not in the report, so the reported cosines cannot be recomputed from it.

The two REST searches took 462 and 298 ms; MCP search took 430 ms and fetch
218 ms. These are client wall times from the publication runner, not platform
CPU or memory measurements. The final daily ledger recorded three query inputs,
200 compatibility inputs and 16 reservation attempts. Reserved tokens and
`ai_calls` are application accounting, not independent provider billing telemetry.

The scripted queries establish interface and source-text consistency. Their
top results do not by themselves establish answer quality: the refined
conversation-cache query still ranked Cache-to-Cache first. Full responses,
independent audit and subsequent external-agent evidence are preserved in
[the compressed evidence](probe-results/public-publication-41007245038.evidence.json.gz).

A fresh external HTTP agent then started at the public root and answered a
feedback-and-revision research question using only this live API. It made 12
requests, including two semantic searches, and consumed 63,470 response code
points; every request returned 200. Independent review verified all four text
windows and eleven recorded excerpts. The answer correctly explained Self-Refine
and its difference from Self-Consistency, and distinguished Critique-GRPO's
training contribution. The grade was **supported partial**: it established one
direct feedback/revision method when the task asked for papers in the plural.
Semantic results still mixed inference-time and training-time methods. This is
one development case, not a general quality score.

The fresh agent's median HTTP wall time was 4.13 seconds through its execution
environment's proxy, different from the CI timings above. Separately, direct
`/health` and `/llms.txt` requests returned 200 with search active. This chat's
web-browsing tool returned an empty error on two attempts to open the host;
the cause is unknown. These results establish public HTTP access, not native
ChatGPT browsing or a configured ChatGPT MCP connection. Main Pages discovery
and the draft PR status remain unchanged by these checks.

The user subsequently installed Favorite Papers in ChatGPT and invoked its
native tools in this conversation. All eight tool calls succeeded: title
search, fetch (16,000 code points), semantic search, catalog lookup, bounded
traversal, and three citation pages (24 + 24 + 19, all 67 distinct incoming
DeepSeekMath neighbors). This establishes native plugin access for that session;
it does not resolve the separate generic web-tool failures or establish general
retrieval quality. The observed semantic query ranked Self-Refine second.

## Recovery review and remaining release conditions

The recovery changes have local regression coverage and are not a new live
publication. They fix transient-load recovery, manifest-specific durable state,
UTC-budget rollover, quota rejection after cap reduction, admission-before-
reservation, and emergency pause independent of corpus/AI state. Only the public
publication path now uses the dedicated environment and secrets. Legacy probes
still offer repository credentials; protecting/removing broad repository tokens
and enforcing the new environment's branch/reviewer rules are account actions,
not security guarantees provided by YAML.

Local validation of this recovery patch: 751 Python tests passed, 214 TypeScript
tests passed with two optional skips, and typechecking passed. The broad gzip
ignore exception was replaced by an explicit allowlist of the 23 already reviewed
compressed JSON filenames; unreviewed compressed exports remain ignored.

Remaining issues are explicit: fresh compatibility checks on each publication,
availability-preserving deployment and state-aware recovery, anonymous quota
fairness, bounded single-object throughput, retention of the source artifact
before its expiry, and repository/evidence cleanup. A failed update currently
pauses search; it does not restore the previous code and activation state.

Do not replace the deployment command with `versions upload` and assume a
Version URL can test this DO: Cloudflare's [Version URL limitations](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/)
exclude Workers implementing Durable Objects. [Worker Previews](https://developers.cloudflare.com/workers/previews/)
are a separate isolation mechanism. [Worker versions](https://developers.cloudflare.com/workers/versions-and-deployments/)
also do not snapshot Durable Object storage, so code rollback alone cannot undo
durable activation, pause and budget changes. No new preview/deployment mechanism
was added in the recovery patch.

The retained manifest's `publication_ready: false` and `not-production` scope
remain historical provenance. The separately authorized, bounded public release
does not turn those fields into a production certificate. The local 96 MiB
diagnostic remains FAIL where measured, platform memory headroom remains
unverified, and neither field is relabeled PASS. The updated loader also no
longer matches the historical live-geometry source closure: the unchanged
preflight rejects it until matching reviewed live evidence is obtained. The
regression suite checks that rejection; it does not rewrite the historical pin.
Do not infer production readiness or permission for a long encoding run from
passing unit tests or from the earlier successful public workload.
