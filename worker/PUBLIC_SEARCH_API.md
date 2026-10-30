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

The existing repository secrets `CLOUDFLARE_ACCOUNT_ID` and
`CLOUDFLARE_API_TOKEN` are sufficient; use the same account and token that passed
the retained-corpus Durable Object run. The selected account must be Workers
Free. No new user-supplied secret or dimension budget is required.

```bash
gh workflow run agent-api.yml \
  --repo vinnik-dmitry07/favorite-papers \
  --ref feat/static-search-probe \
  -f static_probe=true \
  -f probe_runtime=durable-object \
  -f do_probe_phase=publish \
  -f probe_credentials=repository \
  -f free_plan_confirmed=true
```

Run a fresh dispatch from the updated branch. Re-running an old workflow uses
its old source revision and does not select this publication phase. Ordinary
pushes and pull requests run offline checks only.

The job verifies the retained artifact and local reconstruction before touching
Cloudflare. A read-only ownership check permits an absent `key-papers-search` or
an existing instance with the expected bindings and manifest; an unrelated
Worker under that name stops publication. Deployment uses a new publication ID
and a masked administrative token. Prior activation does not activate a new
publication. Only a passing 200-input compatibility check can enable semantic
search, after which public REST and MCP checks run without the administrative
header. Failed or cancelled validation attempts to deactivate search and reports
that result. The stable namespace is retained; the probe cleanup script is never
used on it.

The public checks include catalog lookup, citation traversal and text reading,
plus three genuine semantic query submissions: an initial question, a refined
KV-cache question, and an MCP reasoning question followed by `fetch`. Complete
responses are retained for later answer-quality review. Passing these checks
establishes interface and data consistency, not that every returned passage
answers its query or that the endpoint sustains arbitrary traffic.

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

One fixed Durable Object owns the daily ledger, independently of release or
publication IDs. Reservations are persisted before an AI call and are not
refunded after a timeout or ambiguous failure. At most 1,000 query inputs are
reserved per UTC day, each charged conservatively as 512 input tokens. Admin-only
compatibility work has a separate limit of 200 inputs per day. Thus the maximum
reserved inputs are 512,000 query tokens plus 102,400 compatibility tokens.
Restarting or redeploying does not reset these counters. Completed compatibility
is retained for the pinned corpus, rather than repeated on every cold start.

The application resets its daily allowance at 00:00 UTC. Semantic exhaustion
returns an explicit error and retry information; catalog, graph and text reads
require no AI reservation. This is a shared global allowance, not a small per-IP
allowance that every user behind a common agent proxy must share. Concurrent
requests and outstanding provider calls are bounded; provider work is not retried
automatically. Some failed attempts may retain a conservative reservation even
when their provider call did not begin.

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

Administrative operations require the run's generated `x-publication-token`:
`GET /admin/state`, and POSTs to `/admin/compatibility`, `/admin/activate`,
`/admin/deactivate`, or `/admin/reset-compatibility`. They are not research tools.
The token is not put in the discovery artifact. A fresh publication rotates it.
Resetting failed compatibility is explicit, requires inactive search, and does
not refund its daily allowance.

To pause semantic search later without deleting the stored budget, change the
Worker's `PUBLICATION_ID` variable to `disabled` in Cloudflare and deploy that
configuration. This cannot match an activation generated by the publication job;
public catalog and text reads continue. Publish again with a new job to validate
and reactivate. Do not delete the stable namespace to reset limits. A failed
update is not silently rolled back to an old, apparently active publication.

The retained source artifact currently expires on January 25, 2027. The deployed
Worker's assets do not depend on that download at request time, but a future
republication needs the retained data. Expiry or a changed hash stops before
deployment. Preserve the authenticated artifact in durable release storage before
that date; this first publication does not add another storage service or rerun
the encoder.

## Validation before the first publication

The retained artifact was restored locally with the historical hash checks intact:
40,575 passages and the same packed manifest. The permanent Worker passed a
Wrangler deployment dry-run with those assets (about 352 KiB gzipped script).
The full TypeScript suite passed 204 tests with two optional skips, and typechecking
passed. Python publication and existing workflow regressions passed; the focused
publication/workflow selection covered 80 tests. These checks preceded the
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
