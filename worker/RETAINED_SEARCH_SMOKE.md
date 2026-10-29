# Genuine-query smoke using the retained full corpus

This short manual experiment checks the missing connection between new query
text, Workers AI, the real 40,575-passage int8 index and returned-paper reading.
It does not encode the corpus again.

The [first live run](https://github.com/vinnik-dmitry07/favorite-papers/actions/runs/40798568932)
restored and deployed successfully, but Cloudflare rejected the initial
`/probe/info` request with HTTP 403 / error 1010 (`browser_signature_banned`).
No compatibility inputs or search queries were submitted. Namespace and Worker
cleanup passed. The runner had omitted the explicit application User-Agent used
by the existing probe client. It now sends that truthful application identity,
as recommended in [Cloudflare's 1010 documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1010/).
This correction has transport-level regression coverage.
[Original response and cleanup evidence](probe-results/retained-smoke-40798568932.json).

The [second live run](https://github.com/vinnik-dmitry07/favorite-papers/actions/runs/40799952795)
did not encounter that 403. Immediately after deployment its first `/probe/info`
request received edge 404 / error 1042 (`workers_dev_script_not_found`); the
subsequent read-only ledger request returned HTTP 200 with the authenticated
40,575-passage index and zero provider calls. The runner still correctly retained
its failed outcome. This sequence is consistent with deployment propagation,
not a search or embedding failure. Cleanup passed again.
[Original startup sequence and ledger](probe-results/retained-smoke-40799952795.json).

The runner now checks startup readiness with at most three initial info GETs,
one second apart, only for that exact edge 404/1042 response. It still requires
the expected full-index identity and a fresh zero-call ledger before provider
work. Authentication errors, ordinary 404s and identity mismatches stop; search
and compatibility requests are never retried. The corrected startup handling
has not yet been run live.

## Run

The existing repository secrets `CLOUDFLARE_ACCOUNT_ID` and
`CLOUDFLARE_API_TOKEN` select the previously confirmed Free account. The command
does not change the account plan or production API.

```bash
gh workflow run agent-api.yml \
  --repo vinnik-dmitry07/favorite-papers \
  --ref feat/static-search-probe \
  -f static_probe=true \
  -f probe_runtime=durable-object \
  -f do_probe_phase=retained \
  -f probe_credentials=repository \
  -f free_plan_confirmed=true
```

In GitHub Actions, choose **Agent probe → Run workflow**, select
`feat/static-search-probe`, and use the same five field values. Leave the long
full-run option disabled. The job has a 30-minute ceiling, including dependency
installation and cleanup; this is not an estimate of its measured duration.

## Early failures and bounded work

1. Offline tests must pass. The job authenticates retained run `40448979121`,
   artifact `12715563729`, the archive digest and reconstructed runtime. A
   missing/expired artifact or identity mismatch stops before deployment.
2. It checks for an earlier probe namespace, then deploys a run-specific
   authenticated Durable Object with a 15-minute expiry. It captures namespace
   ownership and completes the bounded read-only readiness check before any
   provider calls.
3. It compares 200 retained reference vectors with Workers AI in batches of at
   most 16, requiring cosine similarity of at least 0.999. Any mismatch stops
   before new search queries. This uses new inference only for these checks,
   not the remaining corpus.
4. It submits exactly two fixed new queries, first checking that neither occurs
   in the 2,064 saved questions. Each successful search is followed by reading
   its first returned paper. The driver has a 32-request HTTP ceiling and a
   600-second measurement deadline, with no automatic provider retries.
5. Partial evidence is written as the run proceeds. Cleanup removes the owned
   namespace, verifies its absence and then removes the temporary Worker.
   Successful requests alone cannot pass the job if cleanup is unverified.

The runtime additionally enforces persistent provider budgets, reserves them
before making calls, and limits concurrent and queued requests. It does not
replace the existing admission/inference entrypoints or issue a new full-run
certificate. The separate production-publish workflow is unchanged.

## Read the result

Download `retained-search-smoke-<run>-<attempt>` from the Actions run. Inspect
`run.json` for the compatibility result, two query submissions, returned paper
IDs, reading responses, elapsed times and provider ledger; inspect lifecycle
evidence for verified cleanup. Missing evidence is a failed/unverified check,
not a passing result.

This is a scripted HTTP smoke, **not** autonomous-agent answer grading, held-out
retrieval quality, a platform memory measurement or a free-tier capacity proof.
It records wall time, not attributable Cloudflare CPU. A pass establishes that
new-query search and reading work together on the retained full index. The next
user-facing check is an agent journey with unrestricted query reformulation and
public discovery. Keep PR #2 draft until those release requirements are met.

Related evidence: [agent journeys](AGENT_JOURNEY_MEASUREMENT.md),
[full-corpus quality](FULL_SEARCH_QUALITY.md), and
[pipeline policy](FULL_SEARCH_PROBE.md).
