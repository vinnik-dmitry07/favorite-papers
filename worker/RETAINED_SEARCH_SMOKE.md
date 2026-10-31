# Genuine-query smoke using the retained full corpus

This short manual experiment checks the missing connection between new query
text, Workers AI, the real 40,575-passage int8 index and returned-paper reading.
It does not encode the corpus again.

## Latest result: live integration passed

[Run 40806851930](https://github.com/vinnik-dmitry07/favorite-papers/actions/runs/40806851930)
completed on commit `02c18b9`: **23 HTTP requests, all 200**, with no startup
retry. The genuine 40,575-passage index passed **200/200** compatibility checks;
minimum cosine was **0.9999992676** against the unchanged 0.999 threshold.
Both new queries were absent from the frozen 2,064-question set and completed
search followed by a 6,000-code-point paper read. The read text matched the
authenticated corpus ranges. The namespace was confirmed absent after cleanup;
Worker deletion succeeded, without a separate saved absence GET.

| New query topic | First returned paper | Search wall time | Read wall time |
| --- | --- | ---: | ---: |
| Reduce long-conversation KV-cache memory | Recursive Language Models | 626.8 ms | 156.1 ms |
| Check and revise reasoning with extra inference computation | Physics of Language Models: Part 2.1 | 611.8 ms | 153.7 ms |

The measured scenario took **25.104 seconds**, including compatibility. The
internal ledger recorded 15 AI calls and 38,680 input tokens: 13 calls/38,631
tokens for compatibility, then one call per new query (26 and 23 tokens). Reads
added no provider work. These are client wall times and internal counters, not
platform CPU, memory or billing measurements. Two warmed searches do not
establish sustained Free-tier capacity. The temporary endpoint was removed.

**Useful answer evidence remains a separate question.** Independent qualitative
review of the delivered snippets and top-one reading windows found related
material, but neither window directly answered its exact question. The first
discusses context offloading rather than a specific KV-cache reduction method;
the second diagnoses reasoning errors rather than providing an inference-time
checking/revision procedure. A later result suggests answer aggregation as a
possible reading direction. Other full papers were not graded. This is not a
formal accuracy estimate or an autonomous-agent evaluation.

The next useful measurement is an agent journey with query reformulation and
further reading, followed by verification of the cited answer. No corpus
re-encoding or additional search infrastructure is needed for that comparison.
[Verified summary](probe-results/retained-smoke-40806851930.json) and
[original report and cleanup evidence](probe-results/retained-smoke-40806851930.evidence.json.gz)
preserve the observed result and its limits.

## Agent follow-up: reading and catalog recovery

Two fresh agents continued from the exact three-hit responses of the successful
live run. Each could choose catalog keyword queries and subsequent reading through
the current full-corpus service. Independent review graded **one supported direct
answer and one supported partial answer**; all eight quoted passages and citation
windows were valid. There were **16 successful API calls, zero API errors**, and
94,818 delivered Unicode code points in total.

| Question | Independently graded result | Evidence found | Calls / code points |
| --- | --- | --- | ---: |
| Reduce long-conversation KV-cache memory | Supported partial | TransformerFAM and Gist Tokens; learned compact-memory mechanisms, with conversation deployment and unchanged-model applicability explicitly unresolved | 8 / 47,058 |
| Check and revise reasoning before answering | Supported correct | Self-Refine and s1 for revision; self-consistency and prefix-consistency voting explicitly distinguished from revision | 8 / 47,760 |

Both agents used one replayed semantic response, three catalog queries and four
paper reads. They selected the queries, papers and ranges themselves; neither
received a target paper, reference answer or the prior relevance review. The
second answer found direct revision mechanisms beyond its original three hits.
The first recovered useful mechanisms but carefully retained the limits of the
retrieved evidence. No unsupported material claim was found.

This is **replayed live search followed by local navigation**, not another live
Cloudflare experiment. No new query embeddings, semantic reformulations or corpus
encoding were performed. The initial response bodies were preserved byte for
byte; follow-up reading used the authenticated 40,575-passage corpus and current
service handlers. Both agents used their full eight-call allowance and nearly all
of the 48,000-code-point allowance. Two deliberately revisited cases do not give a
general accuracy estimate or establish deployed MCP, public access or capacity.
The agents reported no display truncation; the HTTP transcripts independently
verify complete delivered bodies, not the outer client display.

The first agent proposed the unexecuted follow-up query: `Training-free key value
cache compression or eviction for long multi-turn conversations preserving
important earlier tokens`. The existing tools already support useful recovery;
this diagnostic does not justify changing ranking or adding another search backend.
Public deployment and unrestricted semantic follow-up remain to be verified.

[Verified summary](probe-results/retained-reading-2026-10-28.json) and
[original protocol, HTTP transcripts, frozen answers and independent reviews](probe-results/retained-reading-2026-10-28.evidence.json.gz)
record both successes and scope limitations. The evidence file stores original
UTF-8 files with their SHA256 hashes. Model revision/sampling parameters are not
exposed; conversational isolation was instructed, not an operating-system sandbox.
A launcher packaging error was caught before agent retrieval and corrected by an
explicit `--retained-reading` mode. No scored agent call was rerun. An answer-file
serialization typo in the second session was corrected without another API call.

To reproduce, restore the existing full-corpus artifact, extract the protocol and
session registry from the evidence, and build the pinned harness from `worker/`:

```bash
node_modules/.bin/esbuild probe-kernel/retained-reading-journey.ts \
  --bundle --platform=node --format=esm \
  --outfile=../full-probe-reports/retained-reading/runtime.mjs
```

From the repository root, run the existing Python interactive launcher with
`--retained-reading`, the recorded registry, bundle and manifest hash, and a new
output directory per fresh agent. The full command template and executed source
hashes are in the protocol. The harness never loads a query-vector bank; its
embedding callback fails if called. The production Worker and CI workflows are
unchanged. Validation covered 11 focused tests, TypeScript checking, Python
compilation, and an actual launcher/search/catalog preflight.

## Earlier startup failures

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
and compatibility requests are never retried. The later successful run reached
readiness on its first request, so the bounded retry branch itself has local
regression coverage rather than live execution evidence.

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
