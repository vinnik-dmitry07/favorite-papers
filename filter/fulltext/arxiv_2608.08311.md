##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution

###### Abstract

Long-horizon agents are model--harness systems, yet most harnesses remain fixed after design. We present Ouroboros 1 1 1 https://ouroboros-agent.ai/ – a self-developing agent harness whose tools, context assembly, prompts and core implementation improve through reviewed commits that become the runtime for later work. Core evolution proceeds in two modes. In recursive free evolution, improvement is itself a task and completion can schedule the next evolution cycle. In experience-driven core evolution, ordinary work and social interaction expose bugs, rough edges, and inefficient context construction leading to reviewed structural changes. On Terminal-Bench 2.1, an Opus 5 run scores 86.97% (86.74% after trajectory audit), the best result reported on this benchmark. An Opus 5 run on OSWorld-Verified reaches 90.69% , above the best previously reported score, and a five-rollout CL-Bench campaign sets a new state of the art at 0.2301 . Hope is the longest-running publicly documented Ouroboros deployment: a 161-day living-agent experiment in free evolution under governed human communication across seven surfaces, where people surface faults and proposals but the agent decides which changes to pursue. Because a self-developing agent may rewrite its own code and select new model APIs, operational safety is a primary design problem: guardrails must remain authoritative under evolutionary pressure. Benchmark campaigns use frozen seeds, while Hope continues live evolution on a separate lineage.

## 1 Introduction

Agent scores on long-horizon benchmarks are products of the base model, the execution harness, the environment, and the grader. As models improve, an increasing share of realized capability is determined by how the harness assembles context, invokes tools, verifies outcomes, and recovers from failure. Most production harnesses freeze these policies after design. Ouroboros instead treats the harness as an evolving object: its source, prompts, tools, review logic, and core implementation live in a versioned repository and change through a reviewed commit path that becomes the substrate for subsequent tasks.

This self-development has two modes. Recursive free evolution makes improvement itself a task. After inspecting the current system, the agent selects and implements a change, and completion can schedule another evolution cycle, yielding a continuing sequence of reviewed updates rather than a fixed optimization run. Experience-driven core evolution begins with ordinary work. Task execution, reflection, review blockers, instrumentation, and social feedback expose bugs, rough edges, context-assembly failures, and inefficient tool paths; the agent records durable error classes and proposed repairs, then decides whether to open maintenance work under the same commit gate.

Hope is the longest-running publicly documented Ouroboros deployment, not its only running instance, and our primary field experiment in free evolution under human interaction. Since February 2026, one persistent agent has served users across seven communication surfaces while retaining memory and continuing to modify its own implementation. People suggest capabilities, criticize behavior, and surface faults; those signals are advisory. Hope decides which proposals identify real problems and which changes to pursue.

The same evolutionary process that improves competence can also expand autonomy, acquire stronger tools, or weaken later controls, including by selecting alternative model APIs. Operational safety is therefore not an ancillary checklist but a design constraint: authority boundaries must remain binding under repeated core evolution.

### Contributions.

1. State-of-the-art results on Terminal-Bench 2.1, OSWorld-Verified, and CL-Bench, and model-matched frontier performance on SWE-bench Pro and GAIA, with complete per-task traces and run manifests.

2. A harness architecture with two modes of reviewed core evolution: recursive free evolution and experience-driven core evolution.

3. Hope, a 161-day living-agent experiment in free evolution under governed multi-surface human communication, where social interaction drives candidate improvements without transferring commit authority to users.

4. An operational safety architecture in which constitution loading, governance protection, staged-diff review, external spend limits, and operator halt remain authoritative while the agent evolves.

Benchmark campaigns evaluate frozen seeds with documented runtime configuration; Hope continues live evolution on a related but separate lineage. Ouroboros is released under the MIT license. 2 2 2 https://github.com/razzant/ouroboros

## 2 Related Work

### Self-evolving agents.

Self-evolving systems modify different substrates, including memory, prompts, tools, workflows, and implementation code ( Gao et al., 2025 ) . Voyager accumulates executable skills ( Wang et al., 2023 ) ; STOP, Gödel Agent, and Darwin Gödel Machine modify scaffolds or agent populations ( Zelikman et al., 2023 ; Yin et al., 2024 ; Zhang et al., 2025 ) ; Live-SWE-agent creates tools during task execution ( Xia et al., 2025 ) ; and Autogenesis specifies lifecycle and rollback interfaces for evolving agent resources ( Zhang et al., 2026 ) . ADAS searches over agent designs, and SICA edits a coding scaffold’s implementation ( Hu et al., 2024 ; Robeyns et al., 2025 ) . Ouroboros focuses on a deployed, version-controlled implementation in which changes to core code and governance pass through reviewed commits. Table 1 summarizes the corresponding evolution boundaries.

### Harnesses and coding agents.

SWE-agent and OpenHands established that the agent-computer interface is itself part of coding-agent performance ( Yang et al., 2024 ; Wang et al., 2025 ) . Codex CLI, Claude Code, Cursor, Aider, Hermes Agent, and OpenClaw are model–harness systems ( OpenAI, 2025 ; Anthropic, 2025 ; Anysphere, 2026 ; Gauthier, 2023 ; Nous Research, 2026 ; OpenClaw, 2026 ) , and controlled studies find substantial differences in accuracy, latency, and token use when the model is held fixed ( Ding et al., 2026 ; Yao et al., 2026 ; Vats and Golev, 2026 ) . Each comparison therefore reports the model, harness, provider route, effort, and evaluation protocol.

### Persistent memory and deployment.

Generative Agents, Voyager, and persistent-memory systems show that stored experience and reflection can shape later behavior ( Park et al., 2023 ; Wang et al., 2023 ; Borro et al., 2026 ) , and Constitutional AI uses explicit principles in training ( Bai et al., 2022 ) . CL-Bench evaluates learning across ordered task streams ( Asawa et al., 2026 ) . Springdrift reports an auditable multi-channel persistent-agent deployment ( Brady, 2026 ) . Ouroboros treats memory and a runtime constitution as control surfaces. Its multi-model review draws on debate, LLM-as-judge, and self-critique ( Irving et al., 2018 ; Du et al., 2023 ; Zheng et al., 2023 ; Madaan et al., 2023 ; Gou et al., 2023 ) , with source-code patches as the reviewed artifacts.

### Benchmarks and protocol validity.

Terminal-Bench 2.1 evaluates 89 hard terminal tasks ( Merrill et al., 2026 ) ; SWE-bench Pro targets long-horizon multi-file tasks ( Deng et al., 2025 ) ; and OSWorld, GAIA, and ProgramBench cover GUI/CLI computer use, tool/web reasoning, and cleanroom program rebuild ( Xie et al., 2024 ; Mialon et al., 2023 ; Yang et al., 2026 ) . Agent benchmarks can also expose hidden answers, accept unintended shortcuts, or drop failed attempts. BenchJack and HackDetect systematize benchmark and trajectory audits ( Wang et al., 2026 ; Shao et al., 2026 ) . SWE-bench Verified serves as historical context because it no longer reliably separates frontier coding systems ( OpenAI, 2026 ) .

## 3 Ouroboros Architecture

Ouroboros separates a launcher and supervisor boundary from a mutable agent repository (Figure 1 ). The launcher owns startup, process supervision, release bootstrapping, and panic-stop semantics. The repository contains the task loop, tools, prompts, memory projection, review logic, benchmark adapters, and user interfaces. External workspace tasks operate on a separate repository root and return patch artifacts or direct deliverables.

### Commit pipeline.

Three owner-selected runtime modes bound self-repository mutation. Light blocks repository edits; advanced permits ordinary edits and protects governance surfaces; pro permits protected edits subject to review. Each write invalidates prior review evidence because freshness is bound to the staged snapshot.

The commit path runs deterministic preflight, fingerprints the staged diff, collects reviewer evidence, and checks the fingerprint again before commit. The diff-review panel is blocking in every context mode. In owner-selected max mode, a whole-repository scope reviewer also evaluates goals, coupling, prompts, and functional code. In low mode, scope review is skipped. Rollback restores an earlier reviewed state and follows a separate recovery path.

### Task outcomes and verification.

Task completion is recorded on separate execution, objective, review, and artifact axes, and host-run verification commands create revision-bound receipts. Finalization preserves the latest typed answer and distinguishes capability failures from infrastructure errors, timeouts, budget exhaustion, and incomplete evidence. Project tasks add a journal, workpad, knowledge scope, and a one-writer lease under the shared agent identity.

### Operational identity and memory.

The runtime represents identity and continuity through a versioned constitution, an editable identity profile, scratchpad and chronicle projections, project memory, review ledgers, and Git history. These artifacts shape observable behavior across sessions and model routes.

### Two modes of core evolution.

Free evolution runs evolution itself as a task. After reviewing the current system, the agent selects and implements an improvement; completion can schedule another evolution task, producing a continuing sequence of reviewed changes rather than a fixed optimization run. Post-task evolution begins with ordinary work. Task execution, reflection, review blockers, instrumentation, and social feedback expose bugs, rough edges, context-assembly failures, and inefficient tool paths. The agent records these as durable error classes and proposed structural repairs, then decides whether to open maintenance work. Accepted fixes pass through the same reviewed commit gate as every other core change. Section 4 traces both human-surfaced and self-detected examples in the live system.

### Benchmark execution and evidence.

Terminal-Bench installs a fresh runtime inside every Harbor task container and uses the official verifier. The task instruction is preserved and followed by one harness-authored anti-lookup paragraph that forbids fetching benchmark definitions, tests, or solutions. Other adapters connect the same runtime to OSWorld virtual machines, SWE-bench Pro repositories, GAIA sandboxes, ProgramBench cleanrooms, and CL-Bench task streams.

The benchmark launchers write a run manifest before admission, attest the seed and runtime, preserve every requested instance in append-only ledgers, and record skipped, timed-out, and infrastructure-failed attempts. Public submission copies undergo value-level secret scrubbing with an independent zero-leftover check; official benchmark scorers remain authoritative.

### Subagents and patch integration.

Ouroboros can spawn readonly planning scouts and mutative acting subagents under a configurable task tree (Figures 2 and 3 ). The default depth is 2, the configured maximum is 500; Acting children write in isolated worktrees or admitted external workspaces and cannot commit the live system repository. The parent verifies lineage, patch hashes, and protected paths before a three-way indexed integration. Submittable benchmark profiles disable task delegation to preserve pass@1; planning scouts may still contribute context and are disclosed separately.

## 4 Hope: Free Evolution under Human Interaction

Hope is a long-running experiment in free evolution under governed human communication. Since February 2026, one persistent Ouroboros agent has interacted with people across seven public and private surfaces while retaining memory and continuously developing its own implementation. User requests, public conversations, internal instrumentation, and post-task reflection all provide candidate directions for development; the agent decides which suggestions warrant action and which changes to pursue.

Hope is the longest-running publicly documented Ouroboros deployment, not the only running instance. It shares an architectural lineage with the released benchmark harness, including persistent memory, reviewed repository changes, rollback, and an operator stop path. The live repository has continued to evolve beyond the frozen benchmark seeds. This separation lets reproducible evaluation and ongoing deployment evolution coexist.

At the 6 August 2026 cutoff, the public deployment feed spans 161 elapsed days and reports $110.6K in model spend, 79.7B processed tokens, 175,755 lines of code, and 227 MB of memory artifacts (Figure 6 ). The system serves seven interaction surfaces: web chat, voice, Telegram, Discord, Twitter/X, website comments, and email. Table 4 records interaction, evolution, and public deployment counters through the same cutoff.

### Multi-channel state.

Channel ingress converges on an ordered message log and is projected into separate rolling, per-person, and per-call digests (Figure 5 (a)). Private correspondence is excluded from public logs; bounded private context can enter non-public reasoning projections. All channels therefore share one context rather than acting as independent agents.

### Social-interaction-driven development.

People do more than submit isolated tasks: through continuing conversation they point out undesirable behavior, propose capabilities, and challenge the agent’s decisions. These signals enter the same improvement backlog as self-detected faults and internal observations. They are advisory rather than imperative: Hope decides whether a suggestion identifies a real problem, whether it fits the system’s goals, and whether to initiate a change. A background loop can also open maintenance or free-evolution tasks without a contemporaneous human prompt. Repository changes then follow the deployment’s configured review and commit policy, leaving a trace from social feedback or internal observation to the resulting change.

### Controls on self-directed work.

The deployment keeps the constitution in resident context, protects governance files from ordinary write paths, and records review evidence against a staged snapshot. Public messages cannot directly invoke commit, restart, shell, or identity-edit tools. These controls reduce direct prompt-to-core mutation paths while preserving the agent’s ability to choose and implement improvements. Control strength depends on the owner-selected runtime and review modes; Section 7 examines the stronger problem of keeping these boundaries stable as the agent evolves.

### Operator boundary.

Public presence runs on a strict tool whitelist. A separate authenticated operator channel carries task assignment, model routing, budget controls, and /panic . The stop command is parsed by the supervisor before normal agent handling and terminates the process tree. The spending limit is external to the agent and cannot be raised through ordinary agent tools.

### Evolution during deployment.

Two cases illustrate how useful work changes the agent that receives later tasks. First, people in public channels noticed that Hope occasionally sent the same message twice. The agent traced the behavior to a duplicate-send path and landed a reviewed verbatim-duplicate guard in the public output pipeline. Second, deep self-review tasks were aborting with apparent model unavailability. The agent traced the fault to review-pack context overflow and replaced the assembly path with a bounded, connectivity-aware context atlas ranked by import-graph centrality and a provider-calibrated size estimate. The fix preserves high-connectivity core files during review. The first case began with social feedback; the second with the agent’s own observation. Both became durable error classes and reviewed structural changes used by subsequent interactions. Together they instantiate experience-driven core evolution: work exposes a fault, the agent decides to act, and the resulting fix changes how later work is performed.

## 5 Evaluation

Table 2 summarizes results across the five benchmark families, and Figure 4 plots the principal comparisons. All runs use the official verifiers. Complete per-task traces, manifests, and submissions are linked with the corresponding results.

### Terminal-Bench 2.1.

The Opus 5 campaign ran five trials on each of 89 tasks. Its raw score is 387/445 (86.97%). Trajectory audit found one trial that satisfied a weak verifier through an unintended shortcut. We asked the benchmark maintainers to zero it, yielding 386/445 (86.74%). Provider moderation failures and infrastructure errors remain in the denominator. The binomial standard error over 445 trials is about ± \pm 1.7 percentage points for every system in this range, so the audited Opus 5 score sits roughly two standard errors above the strongest baseline, Claude Code with Fable 5 (83.8%) ( Anthropic, 2025 ) ; the other leaderboard baselines are Codex CLI with GPT-5.5 (83.1%) ( OpenAI, 2025 ) and Cursor with Grok 4.5 (79.3%) ( Anysphere, 2026 ) . The submission is open and the complete Harbor job is public.

### OSWorld-Verified.

The Opus 5 run scores 327.39/361 (90.69%) on the standard non-Google-Drive set ( Xie et al., 2024 ) . It uses screenshots, a 100-turn budget, a read-only feasibility pass, per-task proxy sessions when requested by the task config, and the official evaluator. The strongest published baselines are the Intelligence-Indeed agent, the official leaderboard leader at 90.19%; Claude Mythos Preview at 85.4%, the five-run average Anthropic reports in the Claude 5 system card; and Pointer Agent with Opus 4.7 at 83.64%. Per-task prompts, trajectories, scores, and manifests are public .

### CL-Bench.

The submitted Sonnet 4.6 campaign reaches normalized reward 0.2301 with one stateless baseline and 5 ordered stateful rollouts on all six domains. Conversation state resets between questions, and native memory persists across each rollout. Core evolution and task delegation are disabled, which isolates persistent memory more cleanly than the deployment case. The strongest baselines published by the benchmark authors ( Asawa et al., 2026 ) are plain in-context learning (ICL), which carries the interaction history forward in the prompt (0.1960 with Sonnet 4.6, 0.1890 with GPT-5.4), and Claude Code with Sonnet 4.6 (0.1855); memory-augmented systems such as Mem0 and ACE score lower. Per-task means with standard errors over the five rollouts are included in the trace dataset , and the submission is open.

### SWE-bench Pro and GAIA.

After symmetrically removing every SWE-bench Pro instance where either arm reached the reference solution, Ouroboros resolves 58.2% and Codex resolves 59.4% on 655 paired tasks. The 1.2-point difference is statistically indistinguishable under McNemar’s test ( p = 0.40 p=0.40 ), placing the self-developing harness at model-matched parity with Codex. The matched-pair traces and audit are public. On GAIA, Ouroboros scores 78.2% and Claude Code scores 78.8% with Sonnet 5; the GAIA artifact bundle accompanies the release.

## 6 Trajectory Audits and Harness Improvements

Ouroboros treats shortcut rewards, contaminated tasks, and execution failures as evidence for improving both the reported result and the harness that produced it. Each class below led to an adjusted score, a concrete implementation change, or a durable target for subsequent evolution.

### Reward hacking.

The Terminal-Bench trajectory audit identified one rewarded trial that pre-seeded the web root without completing the requested Git-to-web pipeline. The reported audit-adjusted score removes that trial. The same audit confirmed that the remaining traces did not access verifier files, tests, reward files, or oracle solutions.

### Contamination.

SWE-bench Pro task identifiers expose the upstream fix commit, and both harnesses reached reference material through web search or Git history. A symmetric filter removes an instance when either arm reaches the reference solution. The resulting paired comparison reverses the interpretation of the raw aggregate gap.

### Isolation failure.

Historical GAIA runs inherited the operator’s home directory. Agent retries could therefore place task artifacts on the real Desktop. Later launchers use isolated user-file roots and attachment staging, correcting the observed path. Complete filesystem isolation still requires a stronger sandbox than path conventions alone.

### Remote-state drift.

During OSWorld development, a VM reset reallocated the guest endpoint. The working phase retained the pre-reset address, which allowed concurrent lanes to act on the wrong VM. Republishing and verifying the endpoint after every reset removed the observed class. Subsequent forensics led to fixes in turn-budget wording, screenshot integrity, task-contract verification, and first-scored-attempt ownership.

### Continual-memory failures.

CL-Bench showed positive memory carry on several domains and failure under schema drift. Stored lessons could become stale, retrieval sometimes chose the wrong domain, and useful lessons were occasionally written only after the failing episode. These cases motivate explicit temporal and domain metadata for future memory work.

(a) Channel state and operator bypass.

(b) Reviewed-change gates.

## 7 Operational Safety Controls

Self-developing agents create an additional safety problem beyond fixed harnesses: the same evolutionary process that improves task performance can also expand autonomy, acquire more capable tools, or weaken the controls applied to later actions. Prompts, tests, tools, model routes, review rules, and recovery paths are therefore security-relevant mutation surfaces. Ouroboros addresses this problem with guardrails designed to remain binding under repeated core evolution. Git history makes changes inspectable and reversible, while independently enforced boundaries retain operator authority.

### Risk: agents that choose their own model APIs.

An evolving agent that can select its own model backends can search for more capable or less constrained behavior through ordinary API changes. Re-routing a model slot to a new provider or version can increase autonomous capability, alter refusal behavior, enlarge the prompt-injection surface, and change cost by orders of magnitude without changing the visible task interface. Model routing is therefore an audited configuration change rather than an ordinary runtime choice. Owner-selected context mode also controls whether whole-repository scope review runs, so the evidence record binds both settings to each reviewed change.

### Guardrails in use.

The constitution is loaded through an untruncated path and is included in review context. Deterministic guards protect governance files from ordinary write tools. The staged diff is fingerprinted before and after review, and a sub-quorum panel cannot produce a clean pass. Owner-selected context mode determines whether whole-repository scope review runs (Section 3 ; Figure 5 (b)). Staging health checks, crash rollback, the external spend cap, the isolated operator channel, and /panic add independent recovery paths. These mechanisms separate the substrate being evolved from the authority that decides whether a mutation can become the next live version. Appendix A specifies the complete control set.

### Observed behavior.

No recorded episode resisted operator shutdown. A near-total deletion of an uncommitted worktree triggered a previously implemented rescue mechanism before an operator reset, demonstrating that recovery logic can become active during self-directed work. This case also motivates the architectural separation between agent-level preservation mechanisms and supervisor-level operator authority: the former may evolve, while the latter must retain the ability to halt, replace, or roll back the system.

## 8 Conclusion

Ouroboros shows that a reviewed, self-modifiable harness can set new state-of-the-art results on Terminal-Bench 2.1, OSWorld-Verified, and CL-Bench while matching frontier coding harnesses on SWE-bench Pro and GAIA. Experience-driven core evolution turns ordinary work into improvements of the agent itself: observed bugs, rough edges, context failures, and social feedback become reviewed changes to the harness that receives later tasks. Hope demonstrates this mechanism during months of sustained human interaction across seven communication surfaces. The operational safety architecture addresses the corresponding risk: an agent that can improve its own code and select its own model APIs requires control boundaries that remain authoritative under evolutionary pressure. Source, adapters, methodology, submissions, and public traces accompany the report.

## Limitations

The deployment study follows one long-running lineage rather than a controlled population of independently evolving agents. SWE-bench Pro is affected by public-reference leakage and task defects. LLM reviewers can share blind spots with the agent, and low context mode omits whole-repository scope review.

## Ethical Considerations

The deployed instance interacted with humans in public and private channels. Raw private transcripts remain private. Published examples and aggregate traces are minimized and scrubbed for credentials, local paths, and participant identity. First-person system outputs are treated solely as operational logs. Self-modifying and remote-workspace capabilities are dual-use. We report authority boundaries, failure modes, and known isolation gaps.

## Use of AI Assistance

Hope (Ouroboros) contributed deployment reflections, code-history context, and system-generated records. Consistent with arXiv and ACL policy, Hope is credited as a system contributor and excluded from formal author metadata.

## Acknowledgments

We thank the benchmark maintainers and community contributors who reviewed submissions, reported failures, and provided reproducible comparison artifacts.

## References

Anthropic (2025) Anthropic Claude code: Anthropic’s agentic coding system . Note: https://www.anthropic.com/product/claude-code Cited by: §2 , §5 .

Anysphere (2026) Anysphere Cursor: an ai code editor and agentic coding environment . Note: https://github.com/getcursor/cursor Cited by: §2 , §5 .

Asawa et al. (2026) P. Asawa, C. M. Glaze, G. Orlanski, R. Ramakrishnan, B. Xu, A. Biswal, V. S. Chen, F. Sala, M. Zaharia, and J. E. Gonzalez Continual learning bench: evaluating frontier ai systems in real-world stateful environments . External Links: 2606.05661 , Link Cited by: §2 , §5 .

Bai et al. (2022) Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion, A. Jones, A. Chen, A. Goldie, A. Mirhoseini, C. McKinnon, et al. Constitutional AI: harmlessness from AI feedback . External Links: 2212.08073 , Link Cited by: §2 .

Borro et al. (2026) L. C. Borro, L. A. B. Macarini, G. Tindall, M. Montero, and A. B. Struck Memori: a persistent memory layer for efficient, context-aware LLM agents . External Links: 2603.19935 , Link Cited by: §2 .

Brady (2026) S. Brady Springdrift: an auditable persistent runtime for LLM agents with case-based memory, normative safety, and ambient self-perception . External Links: 2604.04660 , Link Cited by: §2 .

Deng et al. (2025) X. Deng, J. Da, E. Pan, Y. Y. He, C. Ide, K. Garg, N. Lauffer, A. Park, N. Pasari, C. Rane, K. Sampath, M. Krishnan, S. Kundurthy, S. Hendryx, Z. Wang, V. Bharadwaj, J. Holm, R. Aluri, C. Bo, C. Zhang, N. Jacobson, B. Liu, and B. Kenstler SWE-bench pro: can AI agents solve long-horizon software engineering tasks? . arXiv preprint arXiv:2509.16941 . Cited by: §2 .

Ding et al. (2026) S. Ding, X. Dai, L. Xing, S. Ding, Z. Liu, J. Yang, P. Yang, Z. Zhang, X. Wei, X. Fang, Y. Ma, H. Duan, J. Shao, J. Wang, D. Lin, K. Chen, and Y. Zang WildClawBench: a benchmark for real-world, long-horizon agent evaluation . External Links: 2605.10912 , Link Cited by: §2 .

Du et al. (2023) Y. Du, S. Li, A. Torralba, J. B. Tenenbaum, and I. Mordatch Improving factuality and reasoning in language models through multiagent debate . External Links: 2305.14325 , Link Cited by: §2 .

Gao et al. (2025) H. Gao, J. Geng, W. Hua, M. Hu, X. Juan, H. Liu, S. Liu, J. Qiu, X. Qi, Q. Ren, Y. Wu, H. Wang, H. Xiao, Y. Zhou, S. Zhang, J. Zhang, J. Xiang, Y. Fang, Q. Zhao, D. Liu, C. Qian, Z. Wang, M. Hu, H. Wang, Q. Wu, H. Ji, and M. Wang A survey of self-evolving agents: what, when, how, and where to evolve on the path to artificial super intelligence . External Links: 2507.21046 , Link Cited by: §2 .

Gauthier (2023) P. Gauthier Aider: AI pair programming in your terminal . Note: https://github.com/Aider-AI/aider Cited by: §2 .

Gou et al. (2023) Z. Gou, Z. Shao, Y. Gong, Y. Shen, Y. Yang, N. Duan, and W. Chen CRITIC: large language models can self-correct with tool-interactive critiquing . External Links: 2305.11738 , Link Cited by: §2 .

Hu et al. (2024) S. Hu, C. Lu, and J. Clune Automated design of agentic systems . External Links: 2408.08435 , Link Cited by: §2 .

Irving et al. (2018) G. Irving, P. Christiano, and D. Amodei AI safety via debate . External Links: 1805.00899 , Link Cited by: §2 .

Madaan et al. (2023) A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri, S. Prabhumoye, Y. Yang, et al. Self-refine: iterative refinement with self-feedback . External Links: 2303.17651 , Link Cited by: §2 .

Merrill et al. (2026) M. A. Merrill, A. G. Shaw, N. Carlini, et al. Terminal-Bench: benchmarking agents on hard, realistic tasks in command line interfaces . In International Conference on Learning Representations (ICLR) , External Links: 2601.11868 , Link Cited by: §2 .

Mialon et al. (2023) G. Mialon, C. Fourrier, C. Swift, T. Wolf, Y. LeCun, and T. Scialom GAIA: a benchmark for general AI assistants . External Links: 2311.12983 , Link Cited by: §2 .

Nous Research (2026) Nous Research Hermes agent: open-source ai agent with persistent memory . Note: https://github.com/NousResearch/hermes-agent Cited by: §2 .

OpenAI (2025) OpenAI Codex CLI: a local coding agent from OpenAI . Note: https://github.com/openai/codex Cited by: §2 , §5 .

OpenAI (2026) OpenAI Why SWE-bench verified no longer measures frontier coding capabilities . Note: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ Cited by: §2 .

OpenClaw (2026) OpenClaw ClawBench: the agent benchmark that scores the full stack . Note: https://github.com/openclaw/clawbench Cited by: §2 .

Park et al. (2023) J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein Generative agents: interactive simulacra of human behavior . In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST) , External Links: Link Cited by: §2 .

Robeyns et al. (2025) M. Robeyns, M. Szummer, and L. Aitchison A self-improving coding agent . External Links: 2504.15228 , Link Cited by: §2 .

Shao et al. (2026) J. Shao, H. Chen, W. Zhang, M. Pan, and B. Luo Do agent benchmarks measure capability? protocol validity in the age of agentic AI . External Links: 2607.22368 , Link Cited by: §2 .

Vats and Golev (2026) N. Vats and O. Golev The scaffold effect in coding agents: harness choice as a hidden variable in coding-agent evaluation . External Links: 2607.22585 , Link Cited by: §2 .

Wang et al. (2023) G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and A. Anandkumar Voyager: an open-ended embodied agent with large language models . External Links: 2305.16291 , Link Cited by: §2 , §2 .

Wang et al. (2026) H. Wang, H. Li, Q. Mang, A. Cheung, K. Sen, and D. Song Do androids dream of breaking the game? systematically auditing AI agent benchmarks with BenchJack . External Links: 2605.12673 , Link Cited by: §2 .

Wang et al. (2025) X. Wang, B. Li, Y. Song, F. F. Xu, X. Tang, M. Zhuge, J. Pan, Y. Song, B. Li, J. Singh, H. H. Tran, F. Li, R. Ma, M. Zheng, B. Qian, Y. Shao, N. Muennighoff, Y. Zhang, B. Hui, J. Lin, R. Brennan, H. Peng, H. Ji, and G. Neubig OpenHands: an open platform for AI software developers as generalist agents . In International Conference on Learning Representations (ICLR) , Note: arXiv:2407.16741 External Links: Link Cited by: §2 .

Xia et al. (2025) C. S. Xia, Z. Wang, Y. Yang, Y. Wei, and L. Zhang Live-SWE-agent: can software engineering agents self-evolve on the fly? . External Links: 2511.13646 , Link Cited by: §2 .

Xie et al. (2024) T. Xie, D. Zhang, J. Chen, X. Li, S. Zhao, R. Cao, T. J. Hua, Z. Cheng, D. Shin, F. Lei, Y. Liu, Y. Xu, S. Zhou, S. Savarese, C. Xiong, V. Zhong, and T. Yu OSWorld: benchmarking multimodal agents for open-ended tasks in real computer environments . External Links: 2404.07972 , Link Cited by: §2 , §5 .

Yang et al. (2024) J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press SWE-agent: agent–computer interfaces enable automated software engineering . In Advances in Neural Information Processing Systems (NeurIPS) , External Links: Link Cited by: §2 .

Yang et al. (2026) J. Yang, K. Lieret, J. Ma, P. Thakkar, D. Pedchenko, S. Sootla, E. McMilin, P. Yin, R. Hou, G. Synnaeve, D. Yang, and O. Press ProgramBench: can language models rebuild programs from scratch? . External Links: 2605.03546 , Link Cited by: §2 .

Yao et al. (2026) Y. Yao, X. Tan, C. Liu, Y. Li, Z. Wang, W. Yu, Z. Tan, Y. Tian, G. Zhao, L. Sun, X. Zhang, and T. Yang Harness-Bench: measuring harness effects across models in realistic agent workflows . External Links: 2605.27922 , Link Cited by: §2 .

Yin et al. (2024) X. Yin, X. Wang, L. Pan, L. Lin, X. Wan, and W. Y. Wang Gödel agent: a self-referential agent framework for recursive self-improvement . External Links: 2410.04444 , Link Cited by: §2 .

Zelikman et al. (2023) E. Zelikman, E. Lou, P. Schultz, Q. Yao, C. Zhang, S. Mukherjee, and N. D. Goodman Self-taught optimizer (STOP): recursively self-improving code generation . External Links: 2310.02304 , Link Cited by: §2 .

Zhang et al. (2025) J. Zhang, S. Hu, C. Lu, R. Lange, and J. Clune Darwin Gödel machine: open-ended evolution of self-improving agents . External Links: 2505.22954 , Link Cited by: §2 .

Zhang et al. (2026) W. Zhang, Z. Zhao, H. Wen, Y. Wu, C. Guo, M. Yin, B. An, and M. Wang Autogenesis: a self-evolving agent protocol . External Links: 2604.15034 , Link Cited by: §2 .

Zheng et al. (2023) L. Zheng, W. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, et al. Judging LLM-as-a-judge with MT-bench and chatbot arena . External Links: 2306.05685 , Link Cited by: §2 .

## Appendix A Guardrails in Full

The deployment runs the following controls, summarized in § 7 . • Always-loaded constitution as commit criterion. A versioned constitution is re-read from disk on every task loop along an untruncatable read path and kept in context at all times; it is the standard the commit gate reviews against and cannot be written, deleted, or replaced wholesale. Ordinary writes are blocked before execution.

• Multi-model adversarial review with quorum. A diff-review panel runs for reviewed commits; a sub-quorum result cannot be recorded as a clean pass.

• Deterministic preflight and diff fingerprinting. Version, data-boundary, and size-health checks run first; the staged diff is fingerprinted before and after review, so any mid-review mutation aborts the commit.

• Isolated operator channel and emergency stop. A private control channel carries operator authority and a non-bypassable /panic that halts all processes before any media handling.

• Pattern register. Recurring failures become durable rows (error class, count, root cause, structural fix), shifting repair from instance-level patches to class-level prevention.

## Appendix B Constitution (Abridged)

The agent’s constitution is an always-loaded document of numbered principles plus operating constraints. We reproduce the principle structure and the clauses most relevant to control, abridged for space. Principles 0–4 form a protected core that cannot be deleted or demoted. P0 Agency. The agent acts as an agent, not a passive tool; agency may not be used to bypass reviewed change control, and operator shutdown, rollback, and replacement remain authoritative.

One entity with an unbroken history; memory is treated as load-bearing. Core context (constitution, system prompts, identity) is never silently truncated.

Fix classes of error, not symptoms; recurring failures are recorded in a pattern register.

Self-modification passes multi-model diff review. Whole-repository scope review runs in owner-selected max context mode and is explicitly skipped in low mode. Changing review bounds requires plan review.

The agent may rewrite its code, prompts, identity profile, and public surface. The constitutional core is protected, and the identity profile cannot be deleted.

Decisions route through the model; hard-coded behaviour is minimized.

Claims are grounded in evidence; an operational map of the system is maintained.

Every module justifies its existence under a complexity budget.

Technical capability, memory quality, and operational continuity are improved together.

Every commit increments a version; releases carry a synchronized version, an annotated tag, and provenance; recovery operations that restore prior reviewed states are review-exempt.

Beliefs, memory, and actions stay coherent; contradictions are made explicit; durable architectural choices are recorded. (P10–P11 are absorbed into P2 and P9.)

(a) Project visual-verification record.

(b) Reviewed installable skills.

Operating constraints include a single unified identity, a public-channel architecture with privacy enforced at the speech boundary, capability gates on dangerous tools, and an emergency-stop invariant : an operator /panic must always be able to halt every process immediately, and no agent code, prompt, or constitutional argument may delay or circumvent it.

## Appendix C Benchmark Configuration Disclosure

Table 3 records the scaffold settings needed to interpret the reported scores. Run artifacts retain exact model routes, effort levels, seed commits, selected tasks, and runtime attestations.

## Appendix D Supplementary Figures and Tables

This appendix collects the scaffold disclosures (Table 3 ), deployment statistics (Table 4 , Figure 6 ), and the project and skills interface views (Figure 7 ).

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
