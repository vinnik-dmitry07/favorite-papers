# Agent navigation measurement, October 28

Fresh agents answered **12 of 12 development questions with supported answers**
using the existing REST search, catalog, find and reading tools. Median use was
three API calls and 16,701 delivered Unicode code points. This measures navigation
after one fixed semantic query, not general search accuracy or public deployment.

The ordinary MCP `search`/`fetch` path answered three of the first four questions;
the remaining agent abstained after exhausting its reading allowance. Public
HTTP navigation worked, while the web retrieval tool could not open either Pages
entrypoint. The original arbitrary-agent goal therefore remains only partly
verified.

## Results

| Path | Supported answers | Other outcomes | API calls | Delivered code points |
| --- | ---: | --- | ---: | ---: |
| REST, 12 questions | 12/12 | Two corrected catalog-limit errors | 49, median 3, range 2–8 | 253,412 total; median 16,700.5 |
| Basic MCP, first four questions | 3/4 | One appropriate abstention | 9 total | 135,591 total |

Independent graders checked the frozen answers against the response text and
reference labels. REST grading covered 42 material claims and 20 citations;
MCP grading checked 14 asserted claims and seven citations. No unsupported
answers were found. Equivalent evidence outside the annotated gold span was
accepted. This is one execution per question with inherited Codex model settings,
not a held-out, repeated, cross-model or human-graded accuracy estimate.

The most informative REST case was `baseline-03` (`full-natural-009`). The correct
MetaOptimize paper was absent from its initial eight semantic paper results.
The agent searched the catalog, selected the paper, searched within it and read
the experiment. It answered correctly in eight calls. The corresponding MCP
agent did not receive the paper in its initial results; after reading another
paper, a second fetch exceeded the remaining allowance and was withheld. Its
abstention was appropriate.

REST and MCP are different client paths, not a controlled treatment comparison:
their tool menus, candidate pools, page sizes and response serialization differ.
The MCP budget counts the complete raw response, including repeated text in
structured and text fields. It does not assume that every MCP client presents
both copies to its model. The experiment also disallows further semantic
queries; it cannot establish how a live MCP agent would recover by reformulating.

These observations do not justify changing passage deduplication yet. Existing
navigation recovered the evidence on all 12 selected REST cases, including an
initial retrieval miss. No multiple-passage A/B or production contract change was
performed.

## What the agents could see and do

- The real 40,575-passage int8 index ran through the current corpus store and
  service handlers. No saved rankings or oracle-driven document selection were
  used.
- Twelve questions were selected by a frozen salted hash of question IDs, taking
  at most one question per paper from the existing 64-question development set.
  Selection did not use retrieval outcomes. The MCP follow-up used the first
  four unchanged questions after observing REST outcomes.
- Each fresh agent received its question and ordinary API responses, without
  the expected paper, answer, gold spans or previous failure analysis. Retrieval
  restrictions were instructed; this was not an operating-system sandbox.
- The first semantic query had to match the registered question exactly. Its
  authenticated saved vector was injected; other semantic queries were rejected.
  There were no new embedding/provider calls or corpus encoding.
- Each session allowed eight API attempts and 48,000 delivered Unicode code
  points, including JSON, snippets, repeated text and errors. A 37-code-point
  terminal-error reserve was disclosed. Setup was excluded. Oversized responses
  were withheld intact rather than silently truncated.
- Agents selected their subsequent actions. Answers were frozen before grading.
  Graders did not count withheld upstream bodies as agent-visible evidence.

Two REST agents requested catalog limits above 24, received a clear error and
corrected it. The experimental setup listed parameter names but omitted that
bound; the production contract already declares it. These are observed usability
costs in this setup, not evidence of an incorrect catalog endpoint.

## Public entrypoint checks

A separate fresh HTTP agent started with the repository URL, discovered the
guide, followed all three DeepSeekMath incoming-citation pages (24 + 24 + 19),
and read group size 64 and KL coefficient 0.04 in the paper. It used 11 GETs.
The edges are catalog-local, not all citations on the internet.

The requested Titans title was not found in the expected alphabetical range.
A separate post-journey catalog check confirmed that no matching title exists
among the 415 records. The agent did not invent a paper link; this task does not
demonstrate successful lookup of an unfamiliar title that is present.

A separate positive-title lookup attempt for VICReg stopped after one GET. Its
page-filtering script emitted 65,431 characters before the outer tool truncated
the output, so compliance with its 24,000-character delivery budget could not be
verified. This attempt is preserved as protocol-invalid, not scored as success
or an API failure, and was not rerun. Positive public title lookup remains open.

A web-tool-only agent found the repository instructions, but both observed
`/agents/` and `llms.txt` links returned “not accessible via this tool.” A search
fallback returned nothing. It stopped after five retrieval operations. This
establishes a failure of that access path, with an unknown cause; the successful
HTTP requests show that it is not evidence the site itself was down.

## Audit and reproduction limits

The adapter, compiled bundle, query bank, question mapping, packed manifest,
WASM and vocabulary identities were checked. The original `baseline-01` server
log lacks its first search-response row. A separate transcription from the
agent's original tool output matches the implied 4,919 code points / 4,921 bytes;
the original log is preserved. Its answer support is also fully present in the
later complete-paper response. No search was rerun to replace the missing row.

Server logs record complete response bodies, but alone do not prove that an outer
tool displayed every character to the model. Agents 01 and 03 explicitly checked
their original outputs; 09–12 and all MCP agents reported no visible truncation.
Full outer-output visibility for the other REST cases was not independently
attested. The complete quotes used in the answers occur in their recorded bodies.

Initial root-owned process IDs were inaccessible to the first three agents.
Before any API evidence was retrieved, each agent instead launched the same
fixed client/server pair in its own tool session. Questions, vectors, budgets
and grading rules were unchanged. This transport amendment is preserved.

Evidence files:

- [Summary and hashes](probe-results/journey-2026-10-28.json)
- [Frozen REST protocol](probe-results/journey-2026-10-28-protocol.json) and
  [MCP follow-up protocol](probe-results/journey-2026-10-28-mcp-protocol.json)
- [Answers, original transcripts, grades and public checks](probe-results/journey-2026-10-28.evidence.json.gz)
- [Executed Node bundle](probe-results/journey-2026-10-28.runtime.mjs.gz)

Restore the authenticated archive using the instructions in
[FULL_SEARCH_QUALITY.md](FULL_SEARCH_QUALITY.md). Extract `sessions` from the
relevant frozen protocol into a JSON registry, decompress the executed bundle,
and use `src/run_agent_journey_session.py` with `python -u -i`. Each fresh agent
must own its interactive process; use `get('/setup')`, then the permitted `get`
or `rpc` calls. Use a new output directory per run. The original source commit
is `9dbcb22d804a3cf5d5d9899cacbe6f4a908ef7e1`; execution and file hashes are in
the summary. The exact inherited model revision and sampling settings are not
exposed, so identical future model behavior is not promised.

## Subsequent live and reading measurements

The [retained-corpus smoke](RETAINED_SEARCH_SMOKE.md) subsequently passed on the
real 40,575-passage corpus: 200 compatibility inputs, two new semantic queries,
and returned-paper reads, without corpus re-encoding. Search HTTP wall times were
626.8 and 611.8 ms. The first-hit reading windows did not directly answer the two
questions; this was a wiring success rather than an autonomous answer test.

Two fresh agents then continued from those exact live search bodies using local
catalog and reading APIs. Independent graders found one supported correct answer
and one supported partial answer; all eight quotes/windows were valid. Each used
eight calls. This supports recovery through existing navigation, with the limits
and reproducible evidence recorded in the retained-corpus readout. It did not
execute a semantic reformulation. Public access, deployed MCP, unrestricted
semantic follow-up and sustained platform behavior remain unverified. The PR
remains a draft; these measurements require no new corpus encoding.
