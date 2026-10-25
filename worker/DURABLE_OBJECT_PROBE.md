# Durable Object runtime probe

This is the first stage of the free semantic-search migration. It tests whether
the existing full-size synthetic search workload can run behind a thin Worker
inside a SQLite-backed Durable Object. It does not publish a production API or
test semantic relevance.

The old ordinary-Worker result remains a failure of its strict `<8 ms` sample
CPU gate. A Durable Object is a different execution environment: Cloudflare
documents a default 30-second CPU allowance per request and supports SQLite
objects on Free. Both environments still have the Worker memory limit.
See [DO limits](https://developers.cloudflare.com/durable-objects/platform/limits/)
and [pricing](https://developers.cloudflare.com/durable-objects/platform/pricing/).

## What this experiment holds constant

- The deterministic 40,575-row fixture, 768 dimensions, PQ96 and `wasm-json16`.
- Existing synthetic query vectors, real paper metadata/text and REST/MCP adapters.
- No Workers AI calls, trained embeddings, Vectorize, R2 or paid subscription.

The public Worker validates an expiring, per-run probe token and forwards to one
fixed server-named object. Query text, paper IDs and versions cannot create
additional objects. The DO owns its tokenizer, WASM instance, index and caches.
Concurrent initialization shares loading promises. Application-cache resets
retain the tokenizer, matching the earlier workload. All asset routes also pass
through the authenticated Worker; corpus files are accessed through its binding.

The token is generated in Actions, masked, supplied as a Worker secret and never
saved in the report. The endpoint expires independently of cleanup. Expiration
does not delete the namespace: teardown must still be verified.

## Evidence and gates

Run a pilot first. It checks discovery, full-index REST/MCP search, separate platform
invocation telemetry and namespace teardown before the matrix is authorized.
The matrix uses 600 sequential measured requests, warm-ups and 24 requests in
batches of four, including long unfamiliar-word queries. Every HTTP attempt is
counted against a hard 1,500-request budget; load and telemetry have time bounds.

`probe_marker` joins structured logs to platform request IDs. The runner accepts
object CPU only when platform metadata identifies the Durable Object. Custom
CPU fields, wall clocks and periodic aggregate CPU are never substituted for
per-request CPU. Missing or unfamiliar layouts leave the gate unverified.

The provisional observed-sample targets are:

| Measurement | Target |
| --- | --- |
| Gateway invocation CPU | Every observed request below 8 ms |
| Durable Object invocation CPU | Below the documented 30-second allowance |
| Warm request wall time | Per-case p95 at most 2 seconds |
| Application-cache reload wall time | At most 10 seconds |
| Any service request | Within the existing 20-second client deadline |
| Functional/platform outcome | Successful, with no CPU or memory-limit errors |

These targets do not establish population p99 or a final production SLO.
`cold=1` resets application caches; it is not a new object or V8 isolate.
Object identity, constructor identity and cache generation are retained
separately. Object construction also does not prove a new V8 isolate.
The discovery request initializes the object but not the search index.

The runner always leaves memory, true-isolate cold starts and production
readiness unverified. Sampled isolate memory may later inform a separate memory
decision, but is neither per-object peak memory nor request-level telemetry.
Functional success on local workerd is not Cloudflare CPU evidence.

## Run the live pilot

The [first live attempt](probe-results/cloudflare-2026-10-25-do-preflight.json)
stopped before deployment: the namespace HTTP parser could not handle
`errors: null`. No workload or CPU measurement ran. The corrected parser accepts
null error collections and preserves HTTP status on failure. Re-running that
old Actions run would use its old source; dispatch the updated branch instead.

Use the existing repository secrets. No additional account secret is required:

```bash
gh workflow run agent-api.yml -R vinnik-dmitry07/favorite-papers \
  --ref feat/static-search-probe \
  -f static_probe=true -f probe_runtime=durable-object \
  -f do_probe_phase=pilot -f probe_credentials=repository \
  -f free_plan_confirmed=true
```

The Free-plan confirmation retains its existing meaning: the selected account
must actually use Workers Free. The workflow does not change its subscription.
The endpoint is named `key-papers-static-do-probe-<run>-<attempt>`, separate from
production and the previous ordinary-Worker probe. Before deployment, the job
refuses to proceed if any earlier DO probe namespace remains. It captures the
new namespace's ID, class and SQLite backend before sending requests.

Cleanup deploys a `state = "deleted"` class tombstone without the class export or
binding, verifies that the namespace disappeared, then deletes the Worker
without `force`. A cleanup failure fails the job even if measurements passed.
The expiring token limits a stranded endpoint; a future run still stops until
its namespace has been removed. On interrupted runs, inspect
`probe-do-lifecycle.json` and the cleanup log, then use the same helper with the
exact recorded name and checkpoint. Do not delete unrelated namespaces.

After a successful pilot, run the matrix at the **same commit**:

```bash
gh workflow run agent-api.yml -R vinnik-dmitry07/favorite-papers \
  --ref feat/static-search-probe \
  -f static_probe=true -f probe_runtime=durable-object \
  -f do_probe_phase=matrix -f do_pilot_run_id=REPLACE_WITH_PILOT_RUN_ID \
  -f probe_credentials=repository -f free_plan_confirmed=true
```

The workflow downloads the pilot artifact and checks repository, workflow,
commit, run attempt, account fingerprint, passed sample gate and verified
namespace cleanup. A changed commit requires a new pilot. The matrix also runs
its own telemetry pilot before sending the larger workload.

The `durable-object-probe-<run>-<attempt>` artifact contains the checkpointed raw
report, lifecycle evidence, deployment/cleanup logs and fixture manifest. It is
retained for 90 days. Preserve reviewed evidence in `worker/probe-results/` with
run ID, source SHA and hashes before relying on it for a migration decision;
the Actions artifact alone is not permanent evidence.

## Local reproduction

Build the fixture and pinned dependencies as in the existing probe guide. Start:

```bash
cd worker
npx wrangler dev --config wrangler.do-probe.toml \
  --var PROBE_TOKEN:local-only-token-at-least-32-characters \
  --var PROBE_EXPIRES_AT:2099-01-01T00:00:00Z
```

In a second terminal, from the repository root:

```bash
PROBE_TOKEN=local-only-token-at-least-32-characters \
  python src/run_static_search_do_probe.py http://localhost:8787 \
  --local --script-name key-papers-static-do-probe-1-1 \
  --phase matrix --samples 50 --output probe-do-local.json
```

Local mode skips platform telemetry. Its successful exit establishes functional
completion only; CPU, memory and runtime-readiness gates remain unverified.

## Next stages

Proceed only after the live pilot and matrix evidence justify the runtime:

1. Integrate 200–500 canonical real passages through the production
   `CorpusStore`, `createService`, REST and MCP contracts. Check local BGE versus
   Workers AI embeddings, then an external agent's search/read/citation journey.
2. Build the full canonical corpus and compare actual API results with an
   offline FP32 reference. Prefer exhaustive int8 as the simplest real candidate
   if DO memory and latency permit it; measure quantization loss. Keep fidelity,
   paper utility and passage utility separate.
3. Establish uncached-query latency, account-wide Free quotas, bounded embedding
   usage, Unicode offsets, version consistency, rollout and rollback before
   changing the public discovery links.

Neither a passed synthetic sample gate nor a passed pilot authorizes production
publication. A failed implementation calls for a causal diagnosis; it does not
select a paid plan or reject every static search design.
