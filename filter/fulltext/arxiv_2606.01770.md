##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams

###### Abstract

Auto-harness systems such as A-Evolve, GEPA, and Meta-Harness improve LLM agents by optimizing prompts, skills, tools, memories, and supporting infrastructure from execution feedback, but they are typically evaluated on fixed offline benchmarks. Real deployments instead present open-ended task streams: histories grow without a fixed endpoint, heterogeneous tasks require different harnesses, and problem distributions shift over time. These challenges make a single repeatedly and densely updated harness brittle, causing performance degradation as accuracy peaks early and then declines. This motivates sustained harness construction with task-wise adaptation. We introduce Adaptive Auto-Harness, a framework and system for such streams. The framework decomposes the gap to an oracle harness into evolution loss and adaptation loss. The system addresses these losses with a stateful multi-agent evolver, a harness tree with solve-time routing, and human-steering hooks for cases where history lacks the needed signal. Across prediction-market, security-competition, and event-forecasting streams, Adaptive Auto-Harness outperforms five existing auto-harness baselines and ablations attribute gains to better construction, routing, or targeted human steering. Code is available in Link .

## 1 Introduction

Open-ended task streams are a common deployment regime for LLM agents: tasks arrive continuously, feedback accumulates over time, and future tasks may differ from earlier ones. In this regime, an agent’s harness, comprising the prompts, skills, tools, and supporting infrastructure that surround a fixed LLM, is a primary determinant of task-solving performance. Auto-harness systems such as A-Evolve Lin et al. (2026) , GEPA Agrawal et al. (2025) , and Meta-Harness Lee et al. (2026) perform evolution to construct harness automatically from execution feedback, and report substantial gains on static offline benchmarks such as SWE-bench Jimenez et al. (2024) . Those evaluations, however, do not capture the central pressure of deployment: the harness must keep improving while operating on a chronological stream whose history grows, task types vary, and distribution shifts.

Representative streams include prediction markets with thousands of questions over weeks Cheng et al. (2026) , decade-long security competitions Zhuo et al. (2025) , and cross-lingual forecasting services with heterogeneous sources Zeng et al. (2025) . Figure 1 illustrates why repeatedly evolving and injecting all harness during solving is insufficient. On Polymarket: we run A-Evolve and stop evolution after 3, 7, 15, 30, or 51 cycles, comparing each run with the same solver without evolution. Early evolution improves pass rate, but longer runs accumulate larger prompts and more specialized skills, only some of which transfer. For example, a useful skill news_from_future.md (138 correct vs 16 wrong BUYs) helps on a sports task yet misfires on a politics task. All stopping budgets eventually peak and decline; later in the stream, shorter runs outperform longer ones. Sustained deployment therefore requires preserving useful history while adapting the active harness to the task at hand.

This failure exposes three deployment dimensions that static benchmark evaluation does not capture (Figure 2 ). (D1) Unbounded Streams. The task stream has no fixed train/test cutoff or designated endpoint Karten et al. (2026) ; Wang et al. (2023) ; feedback, trajectories, and harness state accumulate throughout deployment, creating a heavy burden for the evolution. Existing auto-harness systems built around a single-agent evolver compress this expanding history into a finite context window, creating a bottleneck for building the effective and generalizable harness. (D2) Task heterogeneity. Varied types of tasks are mixed in the same stream. A prediction-market platform, for example, mixes politics, sports, and finance questions in the same hour, each calling for distinct sources, tools, and prompting. However, existing auto-harness systems deploy a static dense harness across the stream, with no solve-time adaptation to the task at hand, and neglect the fact that a single fixed policy is rarely optimal across heterogeneous problems Miao et al. (2025) . (D3) Distributional non-stationarity. As the stream progresses, incoming tasks shift away from the experience the harness was last fitted on. A harness optimized for recent cycles therefore drifts out of fit for new tasks, even with rich historical experience. Closing this gap requires per-task contextual adaptation of the harness, not only continued historical fitting. Additional diagnostics are shown in Appendix A .

We address these dimensions with a unified analytical framework and identify two root gaps that prior auto-harness systems overlook. This analysis motivates: (1) Sustained auto-harness (§ 3.3 ), which replaces stateless one-shot evolution with a stateful multi-agent system with cross-cycle knowledge for better harness construction; and (2) Solve-time adaptation (§ 3.4 ), which adapts a task-relevant harness for each problem prior to solving, restoring per-task fit on a heterogeneous, drifting stream. Beyond the two axes, we further introduce a third axis: human-in-the-loop (HITL) for auxiliary steering of the harness to incorporate human insights and foresights that are absent from historical experience. Our contributions are: (1) Deployment-regime analysis of open-ended agentic streams. We formalize why static auto-harness evaluation is insufficient once tasks arrive as unbounded, heterogeneous, and non-stationary streams. The framework decomposes the gap towards the optimal harness into evolution loss and adaptation loss, providing guidance for auto-harness system designs.

(2) Adaptive Auto-harness system. We introduce a stateful multi-agent evolver for sustained harness construction, a harness-tree router for solve-time adaptation, and structurally triggered human-in-the-loop hooks for evolutions when historical experience is insufficient.

(3) Comprehensive empirical validation and diagnosis. We evaluate on three streaming tasks spanning prediction markets, security challenges, and event forecasting against other auto-harness systems. Beyond aggregated performance, we provide in-depth analysis and evidence for the proposed gaps, component ablations, and human-in-the-loop slice analyses.

## 2 Related Work

Continual Learning in Task Streams. Continual learning studies systems that learn from a sequence of tasks while retaining earlier capabilities Buzzega et al. (2020) ; Wang et al. (2022b) ; Wang et al. (2022a) . Domain and test-time adaptation address distribution shift Ben-David et al. (2010) ; Ganin et al. (2016) ; Wang et al. (2020) ; Liang et al. (2020) , and mixture-of-experts methods route heterogeneous inputs to specialised components Jacobs et al. (1991) ; Shazeer et al. (2017) . These directions cover pieces of our D1–D3 setting, but they usually adapt model weights, classifiers, or expert modules. In contrast, we study the harness-level analogue.

Self-improving and self-evolving agents. The closest LLM-agent precedents to our setting are systems that update the harness directly from execution feedback. A-Evolve Lin et al. (2026) introduces a linear-chain evolver: each cycle reads batch trajectories and mutates prompts, skills, memory, and tools. GEPA Agrawal et al. (2025) adds reflective Pareto prompt evolution using textual feedback rather than scalar reward. Meta-Harness Lee et al. (2026) uses a growing filesystem archive and Claude Code as the proposer. Continual Harness Karten et al. (2026) enables online adaptation within a single continuous deployment run through alternating action/refinement cycles. SkillOS Ouyang et al. (2026) learns a skill curation policy via reinforcement learning, training a curator to select and refine reusable skills from repeated interactions.

## 3 Method

### 3.1 Problem Formulation

We consider tasks arriving in an open-ended stream x 1 , x 2 , … , x T x_{1},x_{2},\ldots,x_{T} with x t ∼ P t x_{t}\sim P_{t} , where P t P_{t} is the task distribution at time t t and each x t x_{t} has a fixed ground truth y ⁡ ( x t ) y(x_{t}) . The agent observes the history of prior experience ℋ t = { ( x i , r i , τ i ) } i = 1 t − 1 \mathcal{H}_{t}=\{(x_{i},r_{i},\tau_{i})\}_{i=1}^{t-1} , where r i r_{i} is optionally the realized reward on task x i x_{i} and τ i \tau_{i} is the agent’s solving trajectory (actions, intermediate observations, tool calls). A harness C = φ ⁡ ( ℋ t ) C=\varphi(\mathcal{H}_{t}) , with | C | ≤ K |C|\leq K , is a bounded representation (prompts, skills, memory, and tools) with capacity budget K K , where φ \varphi is the evolver : the agentic system that automatically transforms historic experience into the harness. A solver agent then acts via the policy a t ∼ π ⁡ ( a ∣ x t , C t ) a_{t}\sim\pi(a\mid x_{t},C_{t}) , where π \pi is the LLM-induced sampling distribution over actions conditioned on the task and harness.

### 3.2 Analytical Framework

The three deployment dimensions of section § 1 surface concrete failures, but they do not by themselves identify what an evolver should fix. To pinpoint the root causes, we frame the problem analytically: we cast harness construction as a regret-minimization problem against an oracle reference, and decompose the regret into two complementary loss terms that map directly to actionable design axes.

Utility and regret. We define the utility of a harness C C on a task x t x_{t} as V ( C , x t ) = 𝔼 a t ∼ π ( ⋅ ∣ x t , C ) [ r ( a t , y ( x t ) ) ] , V(C,x_{t})=\mathbb{E}_{a_{t}\sim\pi(\cdot\mid x_{t},C)}[r(a_{t},y(x_{t}))], (1) which is the expected reward of the harness-conditioned solver. The full-history utility is the corresponding ceiling under the capacity budget, V ( ℋ t , x t ) := sup C : | C | ≤ K V ( C , x t ) V(\mathcal{H}_{t},x_{t})\,:=\,\sup_{\begin{subarray}{c}C\,:\,|C|\leq K\end{subarray}}V(C,x_{t}) , that is, the best utility attainable by any bounded harness on x t x_{t} . The regret of the evolver-constructed harness is then Regret ​ ( φ , x t ) = V ⁡ ( ℋ t , x t ) − V ⁡ ( φ ⁡ ( ℋ t ) , x t ) ≥ 0 , \text{Regret}(\varphi,x_{t})=V(\mathcal{H}_{t},x_{t})-V(\varphi(\mathcal{H}_{t}),x_{t})\geq 0, (2) non-negative since φ ⁡ ( ℋ t ) \varphi(\mathcal{H}_{t}) is one element of the supremum’s domain. Operationally, this ceiling matches what a solver granted ℋ t \mathcal{H}_{t} directly, under the same compute and tool budget as φ \varphi , could attain by reconstructing any candidate harness on the fly.

Solve-time optimal harness. Fix the evolver class Φ \Phi and define the solve-time optimal harness for a particular task: C Φ ∗ ​ ( x t ) = arg ⁡ max C = φ ⁡ ( ℋ t , x t ) , φ ∈ Φ | C | ≤ K ⁡ V ⁡ ( C , x t ) . C^{*}_{\Phi}(x_{t})=\arg\max_{\begin{subarray}{c}C=\varphi(\mathcal{H}_{t},x_{t}),\ \varphi\in\Phi\\ |C|\leq K\end{subarray}}V(C,x_{t}). (3) This is an hypothetic oracle reference: it is the best harness the evolver class Φ \Phi could produce if it were allowed to condition on the incoming task x t x_{t} at solve time. A deployed evolver φ \varphi commits to one harness φ ⁡ ( ℋ t ) \varphi(\mathcal{H}_{t}) before x t x_{t} is observed; using C Φ ∗ C^{*}_{\Phi} as pivot between V ⁡ ( ℋ t , x t ) V(\mathcal{H}_{t},x_{t}) and V ⁡ ( φ ⁡ ( ℋ t ) , x t ) V(\varphi(\mathcal{H}_{t}),x_{t}) yields the following decomposition.

###### Proposition 1 (Regret Decomposition) .

For any deployed evolver φ ∈ Φ \varphi\in\Phi , 𝔼 x t ​ [ Regret ​ ( φ , x t ) ] = L evo ​ ( Φ ) + L adapt ​ ( φ ) , \mathbb{E}_{x_{t}}[\text{Regret}(\varphi,x_{t})]=L_{\text{evo}}(\Phi)+L_{\text{adapt}}(\varphi), (4) where L evo ​ ( Φ ) \displaystyle L_{\text{evo}}(\Phi) = 𝔼 x t ​ [ V ⁡ ( ℋ t , x t ) − V ⁡ ( C Φ ∗ ​ ( x t ) , x t ) ] , \displaystyle=\mathbb{E}_{x_{t}}\!\bigl[V(\mathcal{H}_{t},x_{t})-V(C^{*}_{\Phi}(x_{t}),x_{t})\bigr], (5) L adapt ​ ( φ ) \displaystyle L_{\text{adapt}}(\varphi) = 𝔼 x t ​ [ V ⁡ ( C Φ ∗ ​ ( x t ) , x t ) − V ⁡ ( φ ⁡ ( ℋ t ) , x t ) ] . \displaystyle=\mathbb{E}_{x_{t}}\!\bigl[V(C^{*}_{\Phi}(x_{t}),x_{t})-V(\varphi(\mathcal{H}_{t}),x_{t})\bigr]. (6)

L evo L_{\text{evo}} is the evolution loss : it reflects the evolver class Φ \Phi ’s capability gap, regardless of how many cycles the evolver runs. A single-agent prompt editor cannot produce multi-file infrastructure; that ceiling is structural, not a matter of effort. Reducing L evo L_{\text{evo}} therefore requires pursuing more capable evolver systems with access to broader control and feedbacks. L adapt L_{\text{adapt}} is the adaptation loss : the oracle builds the optimal harness per task, but a deployed φ \varphi commits to one harness before seeing x t x_{t} . Therefore, even with an optimal evolver system, L adapt L_{\text{adapt}} exists as long as task heterogeneity persists.

Human-in-the-loop as a third axis. The decomposition assumes ℋ t \mathcal{H}_{t} contains relevant signal for x t x_{t} . When it does not, the regret decomposition no longer applies; we address this case via a third axis outside L evo + L adapt L_{\text{evo}}+L_{\text{adapt}} , the human-in-the-loop channel (§ 3.5 ).

### 3.3 Sustained Auto-Harness via Multi-Agent Evolution

The analytical decomposition identifies L evo L_{\text{evo}} as the loss from harness capabilities that the evolver class cannot construct from history. We reduce this loss by expanding Φ \Phi with a stateful four-phase multi-agent evolver, temporal-reveal feedback, and cross-cycle memory (Figure 3 ). This design targets the unbounded-stream failure where a single-agent evolver must absorb growing trajectories, delayed labels, and prior research within one context window. Concretely, we address three structural limitations:

(1) Multi-agent with distinct roles and objectives. Because unbounded streams keep expanding the trajectory history an evolver must interpret, existing single-agent evolvers must fit analysis, research, implementation, and verification into one context window. We decompose evolution into four phases (Analyze → \to Research → \to Build → \to Verify), each with a dedicated objective and full context budget. This eliminates the single-window bottleneck and lets parallel Researchers explore disjoint hypotheses without premature convergence.

(2) Temporal-reveal feedback. Under unbounded streams, labels arrive asynchronously (e.g., a prediction market resolves days after the trade). We implement a temporal-reveal gate that surfaces each task’s evaluation signal to the evolver only after its resolution date, providing a proper streaming feedback signal without leaking future information.

(3) Persistent cross-cycle state. We provide the evolver with a dedicated workspace that persists across cycles, containing a task board (prioritised failure analysis), research logs (tested hypotheses with pass/fail verdicts), architecture documentation (README), and verification tests. This cross-cycle memory enables the evolver to refine its construction ability over time and build upon prior evolution experience rather than restarting from scratch.

### 3.4 Solve-Time Adaptation via Harness-Tree Routing

The analytical decomposition identifies L adapt L_{\text{adapt}} as the loss from committing to one dense harness before observing the incoming task’s context. We reduce this loss by shifting heavy adaptation into evolution time: the evolver constructs a structured harness store, and solve time only requires a lightweight adaptation operator. The reduction is general: it factors into (i) how the evolver organizes the harness space and (ii) how the solver selects from that space per task. The harness space can be organized in many forms, including a linear chain that always uses the most recently evolved workspace, a tree of regime-specific branches, or a graph of skills with dependency edges. The adaptation operator can likewise take many forms, ranging from skill-level retrieval over a flat catalog ByteDance (2025) to branch-level routing over a structured space. Different combinations trade off construction cost, operator latency, and the granularity at which adaptation occurs.

We adopt a harness tree as the storage form and agentic routing as the adaptation operator. The tree is the natural fit for our setting because heterogeneous task streams cluster into a small number of recurring regimes (e.g., binary exploitation versus cryptography in CTF-Dojo, sports versus politics in PolyBench), branches isolate regime-specific prompts/skills/tools without cross-contaminating the others, and the branching gate gives the evolver an explicit lever to commit specialization only when warranted by failure evidence. We instantiate this with two designs (Figure 3 ). (1) Branching harness tree (built at evolution time). The solver’s workspace is a git repository. The evolver constructs regime-specific branches (e.g., branch/crypto-classical , branch/binary-reversing ) during evolution, each carrying its own prompt, skills, and tool registry; git provides versioning, isolation, and lineage tracking across branches. (2) Agentic routing (executed at solve time). A router agent reads each branch’s workspace via git show and selects the branch given x t x_{t} ’s context; the solver then checks out that branch and executes.

### 3.5 Human-in-the-Loop Channel

A third failure lies outside L evo + L adapt L_{\text{evo}}+L_{\text{adapt}} : some tasks require harness absent from ℋ t \mathcal{H}_{t} signal, such as API credentials, novel web sources, or proprietary endpoints. In this experience-insufficient setting, neither a stronger evolver nor solve-time routing can recover the missing signal. We address it with a human-in-the-loop channel that augments ℋ t \mathcal{H}_{t} through structurally triggered steering hooks (Figure 3 ). This design targets open-ended streams where new access requirements appear before autonomous evolution has relevant evidence. (1) Task-board steering. After the Analyst updates the task board, a human may review it to add entries, adjust priorities, or supply domain guidance and source access. This proactively steers the subsequent research cycle with direction the evolver cannot derive from trajectories alone. (2) Interactive assistance during research. When a Researcher agent hits a barrier mid-execution that requires human intervention (e.g., an authentication wall), the hook prompts the human in real time. This reactively unblocks the research agent at the point of failure.

## 4 Experiments

### 4.1 Experimental Setup

Benchmarks. We evaluate on three open-ended task streams (Table 1 ): PolyBench for prediction markets Cheng et al. (2026) , CTF-Dojo for security challenges Zhuo et al. (2025) , and FutureX for event forecasting Zeng et al. (2025) . All three enforce strict temporal order and covers the three dimensions of challenge. Details and non-stationarity diagnostics are in Appendix A and C .

Baselines. We compare with no-evolution runs with different solver agents using Sonnet-4.6 Anthropic (2025b) , DeepSeek-V3.2 Liu et al. (2025) , Claude Haiku-4.5 Anthropic (2025a) , GLM-4.7 Z.ai (2025) , and Kimi-K2.5 Team et al. (2026) . We compare with five auto-harness baselines: A-Evolve Lin et al. (2026) , GEPA Agrawal et al. (2025) , Meta-Harness Lee et al. (2026) , Continual Harness Karten et al. (2026) , and SkillOS Ouyang et al. (2026) . We also compare with one human-designed system OctoTools Lu et al. (2025) .

Solver and evolver. We use Claude Sonnet 4.6 as the solver for all experiments unless specified, and use Claude Opus 4.6 as the evolver, both at temperature 0 to attribute gains to the evolution algorithm rather than sampling noise; the no-evolution controls additionally report base-agent results for Haiku 4.5, DeepSeek-V3.2, Kimi-K2.5, and GLM-4.7. All algorithms share the same batch size (100/20/20 for PolyBench/CTF-Dojo/FutureX), batch loop, and temporal-reveal gate; only the evolution algorithm varies.

Metrics. For PolyBench, we report two complementary metrics: Accuracy , the fraction of all markets traded correctly; and Return , defined as Coverage × CWR \mathrm{Coverage}\times\mathrm{CWR} , where CWR is the confidence-weighted portfolio profit-to-investment ratio over traded markets and coverage is the fraction of traded. For CTF-Dojo and FutureX, we report the official pass rate (Pass@1) defined by the original benchmarks. We also report lift in the figures as the difference with baselines. Full definitions are in Appendix A .

Research questions. RQ1 (§ 4.2 ): How does Adaptive Auto-Harness compare against existing auto-harness systems on open-ended task streams? RQ2 (§ 4.3 ): How does Adaptive Auto-Harness address benchmark-specific bottlenecks? RQ3 (§ 4.4 ): Does stateful multi-agent evolution with evaluation feedback provide additional gains? RQ4 (§ 4.5 ): Can solve-time routing effectively leverage specialized harness branches? RQ5 (§ 4.6 ): Can human steering help under insufficient history signal?

### 4.2 Comparison with Baselines

Prior systems specialize on one metric cluster. A-Evolve leads the two pass-rate streams ( 45.2 % 45.2\% CTF-Dojo, 47.5 % 47.5\% FutureX) but covers only 21.1 % 21.1\% of PolyBench markets. Meta-Harness leads all three PolyBench metrics ( 55.3 % 55.3\% Coverage, 50.8 % 50.8\% Accuracy, + 320 % +320\% Return) but falls below the no-evolution Sonnet baseline on FutureX ( 29.4 % 29.4\% vs. 31.0 % 31.0\% ). Base solvers stay below 32.6 % 32.6\% PolyBench Coverage on every model, and OctoTools, the frozen human-designed system, places third on PolyBench Return but does not lead any row. The pass-rate cluster and the portfolio cluster therefore sit in different baselines.

Our three variants jointly lead all metrics. Without HITL intervention, the Full System combines multi-agent evolution with solve-time routing and reaches 97.9 % 97.9\% PolyBench Coverage, 80.9 % 80.9\% Accuracy, and 50.2 % 50.2\% CTF-Dojo Pass. The Multi-agent variant leads FutureX at 49.5 % 49.5\% , where evolving the right source and tooling matters more than per-task routing. The Adaptive variant leads PolyBench Return at + 352 % +352\% , where matching each market to a specialized strategy matters.

### 4.3 Benchmark Bottlenecks

RQ2 asks whether Adaptive Auto-Harness targets the bottlenecks that limit each benchmark. We organize the analysis around the two losses introduced in § 3.2 : the evolution loss L evo L_{\text{evo}} , the gap from capabilities the evolver class cannot construct; and the adaptation loss L adapt L_{\text{adapt}} , the gap from committing to a single harness across heterogeneous tasks.

Evolution bottlenecks ( L evo L_{\text{evo}} ) differ across benchmarks. Figure 4 plots a benchmark-specific stress axis chosen to expose the most predictive capability. The PolyBench panel plots mean stated confidence against market consensus, defined as the implied probability of the favored outcome from Polymarket prices; a well-calibrated harness from our multi-agent variant tracks the diagonal, while single-agent variants stay flat and over-state confidence on low-consensus markets, suggesting that the binding capability is consensus-aware confidence calibration rather than raw prediction skill. The FutureX panel plots pass rate against three retrieval tiers, ranging from offline to date-filtered Wikipedia plus DuckDuckGo to unrestricted DuckDuckGo web search. Pass rate increases monotonically from 34.0 % 34.0\% to 47.6 % 47.6\% to 57.1 % 57.1\% , identifying source acquisition rather than reasoning as the binding capability. The CTF-Dojo panel plots pass rate against the largest challenge file size, binned into five tiers from no-payload to > > 1MB. The best single-agent variant declines from 81.8 % 81.8\% to 30.4 % 30.4\% , and the multi-agent variant declines from 90.9 % 90.9\% to 39.1 % 39.1\% while retaining roughly a 9-point margin throughout, indicating that payload-handling infrastructure becomes the binding capability as inputs grow and that the multi-agent evolver mitigates but does not eliminate this bottleneck. In summary, the binding capability therefore differs by benchmark.

Adaptation bottlenecks ( L adapt L_{\text{adapt}} ) remain after evolution. Figure 5 reports per-task adaptation lift over evolver cycles, where lift on each task is the adaptative harness score minus the median score across single-committed-harness baselines. The solid curve is the within-cycle mean lift and the shaded band is performance variation across task categories; if a single committed dense harness were sufficient, the mean lift would approach zero as evolution progresses. We observe instead that the mean lift and variation remain positive across all cycles on all three benchmarks.

Takeaway. Although streams expose different bottlenecks, they can be addressed under the same principle: reduce evolution loss for missing capabilities and adaptation loss for task-specific fit.

### 4.4 Stateful Multi-Agent Evolution

(a) Example of the four-phase evolution cycle.

(b) Example of the solve-time routing trace.

(c) Example of the Human-in-the-Loop workflow.

RQ3 asks whether the four-role evolver in section § 3.3 (Analyst → \to parallel Researchers → \to Builder → \to Verifier) improves over a single-agent evolver, and whether its state channels matter. Using 100/60/80 tasks on PolyBench/CTF-Dojo/FutureX, Figure 6 compares the full system with variants that remove temporal-reveal feedback or cross-cycle memory. The full system improves over the single-agent evolver on all three benchmarks: 20.3 → 44.3 20.3\to 44.3 CWR on PolyBench, 38 % → 43 % 38\%\to 43\% on CTF-Dojo, and 38 % → 44 % 38\%\to 44\% on FutureX. Removing memory causes the broadest degradation, while removing feedback mainly hurts PolyBench, where outcomes resolve after trading.

Takeaway. The four-role evolver is strongest when paired with persistent state: memory preserves cross-cycle search, and feedback turns resolved outcomes into later evolution signal.

### 4.5 Solve-Time Routing on the Harness Tree

RQ4 asks how much adaptation headroom a specialized harness tree exposes, and how much solve-time routing captures. We measure this with a designed analysis rather than end-to-end deployment, isolating the headroom from router quality. On 80/40/58 tasks for PolyBench/CTF-Dojo/FutureX, we seed one branch per task category, evolve the tree over the stream, and replay every task through every branch. We then compare Oracle (best branch per task), Adapt (category-based routing), Naive ( main only), and Worst (worst per task). As shown in Figure 7 , Adapt improves on both CTF-Dojo and PolyBench, while leaving headroom toward Oracle branch selection. On FutureX, main outperforms Adapt, as web source retrieval ability dominates.

Takeaway. Harness specialization opens real adaptation headroom, but realized routing captures only part of it, so turning headroom into gain is a separate challenge from constructing the branches.

### 4.6 Human Steering for Auto-Harnessing

RQ5 asks whether human steering helps when history lacks the source or access signal needed for evolution. Since all previous experiment does not apply HITL to ensure fairness, we evaluate this on 100 FutureX tasks and restrict human input to two hooks: research-phase steering supplies credentials when research is blocked, and task-board steering adds source directions the evolver cannot infer (Figure 8 c). Figure 9 shows the slice-level effect: lift is 0 0 on broad polymarket questions, rises to + 5 +5 on broad search-dependent questions, peaks at + 20 +20 on the directly targeted finance&tech slice, and remains + 15 +15 on adjacent Western-specialty questions. The pattern indicates that HITL helps when it injects the missing external signal, not generic human advice.

Takeaway. Human steering is most useful when the missing ingredient is external source knowledge rather than additional autonomous evolution.

## 5 Conclusions

Open-ended task streams expose three challenges for auto-harness deployment: unbounded task arrival, heterogeneous tasks, and non-stationarity. Adaptive Auto-Harness addresses these challenges by pairing sustained harness construction with solve-time task adaptation. The decomposition into evolution loss and adaptation loss clarifies why a single repeatedly updated harness is insufficient: the system must build missing capabilities from stream evidence while selecting the right specialized branch for each task. The experiments further show that the three mechanisms are complementary rather than interchangeable: multi-agent evolution constructs benchmark-specific capabilities, routing exploits harness specialization when branch signals are reliable, and human steering supplies external signals that history cannot contain.

## 6 Limitations

Benchmark coverage. We evaluate on three open-ended task streams: prediction markets, cybersecurity challenges, and event forecasting. These domains cover unbounded streams, task heterogeneity, and distributional non-stationarity, but the same framing should be tested further on additional deployment streams where the stream is further expanded spatially and temporally to mimic the real-world deployment.

Diagnostic losses. The evolution loss L evo L_{\text{evo}} and adaptation loss L adapt L_{\text{adapt}} are analytical quantities, not directly estimated oracle losses. Our experiments diagnose them through bottleneck analyses, ablations, and routing controls rather than through a formal estimator of the oracle harness.

## 7 Ethics Statement

We use public research benchmark tasks and do not introduce private user data. CTF-Dojo runs only inside isolated benchmark containers and does not target real systems. Human steering is limited to source guidance, task-board edits, and credential decisions; humans do not label/expose answers or choose solver branches.

## 8 AI Usage Statement

We used AI assistants to refine the writing of this paper and to accelerate debugging and analysis during implementation and evaluation.

## References

Agrawal et al. (2025) Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, and 1 others. 2025. Gepa: Reflective prompt evolution can outperform reinforcement learning. arXiv preprint arXiv:2507.19457 .

Anthropic (2025a) Anthropic. 2025a. Claude haiku 4.5. https://www.anthropic.com/claude/haiku .

Anthropic (2025b) Anthropic. 2025b. Claude sonnet 4.6. https://www.anthropic.com/claude/sonnet .

Ben-David et al. (2010) Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer Wortman Vaughan. 2010. A theory of learning from different domains. Machine learning , 79(1):151–175.

Buzzega et al. (2020) Pietro Buzzega, Matteo Boschini, Angelo Porrello, Davide Abati, and Simone Calderara. 2020. Dark experience for general continual learning: a strong, simple baseline. Advances in neural information processing systems , 33:15920–15930.

ByteDance (2025) ByteDance. 2025. DeerFlow: Deep exploration and efficient research flow. https://github.com/bytedance/deer-flow . Open-source software, accessed 2026-05-28.

Cheng et al. (2026) Pu Cheng, Juncheng Liu, and Yunshen Long. 2026. Polybench: Benchmarking llm forecasting and trading capabilities on live prediction market data. arXiv preprint arXiv:2604.14199 .

Ganin et al. (2016) Yaroslav Ganin, Evgeniya Ustinova, Hana Ajakan, Pascal Germain, Hugo Larochelle, François Laviolette, Mario March, and Victor Lempitsky. 2016. Domain-adversarial training of neural networks. Journal of machine learning research , 17(59):1–35.

Jacobs et al. (1991) Robert A Jacobs, Michael I Jordan, Steven J Nowlan, and Geoffrey E Hinton. 1991. Adaptive mixtures of local experts. Neural computation , 3(1):79–87.

Jimenez et al. (2024) Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. 2024. Swe-bench: Can language models resolve real-world github issues? In International Conference on Learning Representations , volume 2024, pages 54107–54157.

Karten et al. (2026) Seth Karten, Joel Zhang, Tersoo Upaa Jr, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, and Kiran Vodrahalli. 2026. Continual harness: Online adaptation for self-improving foundation agents. arXiv preprint arXiv:2605.09998 .

Lee et al. (2026) Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, and Chelsea Finn. 2026. Meta-harness: End-to-end optimization of model harnesses. arXiv preprint arXiv:2603.28052 .

Liang et al. (2020) Jian Liang, Dapeng Hu, and Jiashi Feng. 2020. Do we really need to access the source data? source hypothesis transfer for unsupervised domain adaptation. In International conference on machine learning , pages 6028–6039. PMLR.

Lin et al. (2026) Minhua Lin, Hanqing Lu, Zhan Shi, Bing He, Rui Mao, Zhiwei Zhang, Zongyu Wu, Xianfeng Tang, Hui Liu, Zhenwei Dai, and 1 others. 2026. Position: Agentic evolution is the path to evolving llms. arXiv preprint arXiv:2602.00359 .

Liu et al. (2025) Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu, Bowei Zhang, Chaofan Lin, Chen Dong, and 1 others. 2025. Deepseek-v3. 2: Pushing the frontier of open large language models. arXiv preprint arXiv:2512.02556 .

Lu et al. (2025) Pan Lu, Bowen Chen, Sheng Liu, Rahul Thapa, Joseph Boen, and James Zou. 2025. Octotools: An agentic framework with extensible tools for complex reasoning. arXiv preprint arXiv:2502.11271 .

Miao et al. (2025) Rui Miao, Babak Shahbaba, and Annie Qu. 2025. Reinforcement learning for individual optimal policy from heterogeneous data. Annals of statistics , 53(4):1513.

Ouyang et al. (2026) Siru Ouyang, Jun Yan, Yanfei Chen, Rujun Han, Zifeng Wang, Bhavana Dalvi Mishra, Rui Meng, Chun-Liang Li, Yizhu Jiao, Kaiwen Zha, and 1 others. 2026. Skillos: Learning skill curation for self-evolving agents. arXiv preprint arXiv:2605.06614 .

Shazeer et al. (2017) Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. 2017. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. arXiv preprint arXiv:1701.06538 .

Team et al. (2026) Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, SH Cai, Yuan Cao, Y Charles, HS Che, Cheng Chen, Guanduo Chen, and 1 others. 2026. Kimi k2. 5: Visual agentic intelligence. arXiv preprint arXiv:2602.02276 .

Wang et al. (2020) Dequan Wang, Evan Shelhamer, Shaoteng Liu, Bruno Olshausen, and Trevor Darrell. 2020. Tent: Fully test-time adaptation by entropy minimization. arXiv preprint arXiv:2006.10726 .

Wang et al. (2023) Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. 2023. Voyager: An open-ended embodied agent with large language models. arXiv preprint arXiv:2305.16291 .

Wang et al. (2022a) Zifeng Wang, Zizhao Zhang, Sayna Ebrahimi, Ruoxi Sun, Han Zhang, Chen-Yu Lee, Xiaoqi Ren, Guolong Su, Vincent Perot, Jennifer Dy, and 1 others. 2022a. Dualprompt: Complementary prompting for rehearsal-free continual learning. In European conference on computer vision , pages 631–648. Springer.

Wang et al. (2022b) Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang, Ruoxi Sun, Xiaoqi Ren, Guolong Su, Vincent Perot, Jennifer Dy, and Tomas Pfister. 2022b. Learning to prompt for continual learning. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pages 139–149.

Z.ai (2025) Z.ai. 2025. Glm-4.7. https://www.z.ai/ .

Zeng et al. (2025) Zhiyuan Zeng, Jiashuo Liu, Siyuan Chen, Tianci He, Yali Liao, Yixiao Tian, Jinpeng Wang, Zaiyuan Wang, Yang Yang, Lingyue Yin, and 1 others. 2025. Futurex: An advanced live benchmark for llm agents in future prediction. arXiv preprint arXiv:2508.11987 .

Zhuo et al. (2025) Terry Yue Zhuo, Dingmin Wang, Hantian Ding, Varun Kumar, and Zijian Wang. 2025. Training language model agents to find vulnerabilities with ctf-dojo. arXiv preprint arXiv:2508.18370 .

## Appendix A Benchmark and Evaluation Details

Across all three benchmarks, tasks are evaluated in chronological order. The solver receives task x i x_{i} with only the information available before its release time, while the evolver receives outcome labels only after the corresponding resolution time. Our analysis pipeline loads the first record for each instance_id , so retries or duplicate logs do not change the reported metrics. The three benchmarks together exercise the three open-ended-stream deployment dimensions identified in § 1 .

### A.1 PolyBench

Source and composition. PolyBench is a Polymarket-derived prediction-market stream with 5,075 tasks from Feb 6–22, 2026. The stream spans politics, sports, finance, crypto, and entertainment markets, and each task is resolved against the official market outcome.

Temporal ordering. For each market, we store the task release timestamp and the outcome resolution timestamp. Resolved labels are hidden from evolution until the corresponding market has resolved.

Metrics. Let N N be the total number of markets in the stream and let 𝒯 \mathcal{T} be the set of executed trades, excluding gated tasks, empty decisions, and Skip decisions. Let s i ∈ { 0 , 1 } s_{i}\in\{0,1\} indicate whether trade i i is correct, b i b_{i} be its confidence-weighted investment, and g i g_{i} be its realized profit. The metrics reported for PolyBench are: Coverage \displaystyle\mathrm{Coverage} = | 𝒯 | N , \displaystyle=\tfrac{|\mathcal{T}|}{N}, Acc \displaystyle\mathrm{Acc} = 100 ⋅ 1 N ∑ i ∈ 𝒯 s i , \displaystyle=100\cdot\tfrac{1}{N}\textstyle\sum_{i\in\mathcal{T}}s_{i}, CWR \displaystyle\mathrm{CWR} = 100 ⋅ ∑ i ∈ 𝒯 g i ∑ i ∈ 𝒯 b i , \displaystyle=100\cdot\tfrac{\sum_{i\in\mathcal{T}}g_{i}}{\sum_{i\in\mathcal{T}}b_{i}}, Return \displaystyle\mathrm{Return} = Coverage ⋅ CWR . \displaystyle=\mathrm{Coverage}\cdot\mathrm{CWR}. Accuracy therefore rewards both broad coverage and correct decisions. Return is a portfolio-style profitability metric: CWR captures the dollar-weighted profit per unit invested over the markets the agent actually traded, and the Coverage scaling discounts a high CWR earned on only a thin slice of the stream. We report Return alongside Accuracy because Accuracy treats every trade equally and is blind to stake sizing, whereas under confidence-weighted investments a confident wrong trade can offset several confident correct ones; Return therefore reflects realized P&L rather than mere directional correctness.

### A.2 CTF-Dojo

Source and composition. CTF-Dojo is a 261-challenge security-competition stream drawn from pwncollege/ctf-archive , chronologically ordered from 2011 to 2024. Challenges cover binary exploitation, web security, cryptography, reverse engineering, and forensics, exposing changes in challenge style and tooling over time.

Sandbox and verification. Each challenge runs inside a per-task Docker sandbox with constrained network policy. Flags are submitted as text and verified by SHA-256 hash comparison against the official flag.

Metrics. We report Pass@1, the percentage of challenges solved within the benchmark budget. All CTF-Dojo aggregate results use the same chronological ordering as the released stream.

### A.3 FutureX

Source and composition. FutureX is a 503-question event-forecasting stream over 82 days from Jan–Apr 2026, drawn from FutureX-Past. Questions cover finance, technology, geopolitics, and entertainment, with both English and Chinese-language variants. The zh-finance slice requires source discovery beyond default English-only retrieval.

Temporal retrieval and filtering. FutureX tasks are historical, but web pages and search indices continue to change after the event. To avoid label leakage, each task is solved with a per-task cutoff date derived from its temporal metadata. In strict built-in retrieval, Wikipedia content is fetched through the revision API using the latest revision before the cutoff, DuckDuckGo results are fetched and filtered by extracted publication dates from htmldate and URL patterns, and structured economic series are queried with observation and realtime endpoints capped at the cutoff. For evolved tools executed through the sandbox, live command output is passed through an LLM temporal filter before the solver sees it: the filter receives the task, cutoff date, and retrieved content, then either returns Clean or replaces post-cutoff values, rows, and snippets with [REDACTED] . This preserves pre-cutoff evidence while blocking dynamic web content that would reveal the resolved answer.

Metrics. We report Pass@1 under the official FutureX criterion. Slice-level human-steering analyses use the same pass criterion and aggregate tasks by the groups shown in Figure 9 .

## Appendix B Implementation and Reproducibility Details

Execution protocol. All main runs use provider-hosted LLM APIs with native tool calling and the same chronological task order used by the benchmarks. Reported numbers are generated from the corresponding results.jsonl files. Closed provider-hosted models do not expose parameter counts; we therefore report the evaluated task counts and evolution cycles rather than GPU-hours. The full-system runs contain 5,075/261/503 solve trajectories and 51/14/26 evolution cycles for PolyBench/CTF-Dojo/FutureX, respectively.

Compute and resources. All model inference is performed through provider-hosted APIs; the primary Adaptive Auto-Harness runs use Claude Sonnet 4.6 for solving and Claude Opus 4.6 for evolution, with other provider-hosted models used only for the corresponding baseline rows. We do not train or fine-tune model weights, and no local GPU compute is used for model optimization. Local compute is used for orchestration, result aggregation, figure generation, and Docker-based benchmark execution, including the per-task CTF-Dojo and FutureX sandboxes. Because the evaluated closed models do not disclose parameter counts, task counts and evolution cycles are the main compute descriptors.

Hyperparameters. Table 3 lists the per-benchmark hyperparameters used by all main runs. Because temperature is zero throughout, the reported metrics are point estimates rather than averages over re-samples.

Seed harness. Table 4 reports what the evolver inherits before any cycle runs. The seed prompt is intentionally compact: PolyBench and CTF-Dojo seed prompts are 27 and 24 lines respectively, FutureX is longer because it documents the temporal-retrieval contract. All three benchmarks start with zero seed skills, tools, and memory entries, so any harness component beyond the seed prompt and the FutureX infrastructure scaffold is constructed by the evolver itself; this isolates the gains reported in the main results from prior hand-engineering of the seed.

Token cost and wall-clock. Table 5 summarises per-system token usage and wall-clock for the five most relevant systems. Solver tokens are summed from the per-task fields in results.jsonl ; evolver-side tokens are omitted because the orchestrator did not persist them in the released artifacts. Wall-clock is the sum of per-task elapsed seconds and excludes orchestration overhead.

Temporal reveal. Each task stores a release timestamp and, when available, a resolution timestamp. Solver calls are filtered against the release time. Evolution cycles receive the trajectory immediately but receive outcome feedback only after the task has resolved, so unresolved tasks remain unlabeled history rather than leaked supervision.

Workspace artifacts. The evolver workspace persists a task board, research logs, verifier notes, tests, and architecture notes across cycles. These artifacts are separate from the solver workspace: the evolver may update harness files during evolution, while the solve-time router only inspects branch metadata and selects a branch for the incoming task.

Branch replay protocol. For the routing analysis in Appendix G , every branch in the evolved harness tree is replayed on a curated task subset to construct the Oracle and Worst controls. Oracle and Worst are post-hoc diagnostic bounds; the deployed router sees only task context and branch metadata, not labels or branch outcomes.

Human-steering records. Human-steering events are author-provided system interventions rather than recruited human-subject annotations. Each event is logged with the triggering phase, requested external signal, and workspace location where the response is recorded; Table 13 reproduces the full event log. This makes steering auditable and keeps human input as source or access guidance rather than answer labels.

## Appendix C Benchmark Non-Stationarity Diagnostics

Figures 12 – 14 provide descriptive diagnostics for the temporal structure of the three streams. These plots are not used as evaluation metrics; instead, they show why the benchmarks are not static IID pools and why a harness fitted to earlier observations can become mismatched to later tasks. Most panels are computed from task metadata, task text, or benchmark-side properties; panels that use outcomes or a baseline solver are included only as descriptive solvability proxies.

PolyBench. Prediction markets shift in both difficulty and tradability over the evaluated period (Figure 12 ). Early markets are more often liquid and already decisive: the fraction of tradeable markets drops from 97% early to 31% late, and the fraction whose maximum price exceeds 0.95 drops from 44% to 29%. At the same time, near-even markets increase from 18% to 35%, meaning later tasks more often require evidence beyond simply following a strong market consensus. The market-price correctness proxy also changes over time, from 84% early to 77% late. Together, these shifts make a fixed prediction-market strategy brittle: calibration, abstention, and evidence gathering must adapt as the stream moves from liquid and decisive markets toward thinner and more ambiguous ones.

CTF-Dojo. CTF-Dojo exposes a different form of non-stationarity: the stream expands into competitions and challenge conventions not present in the early history (Figure 13 ). The cumulative number of source competitions keeps increasing across the chronological order, and by the late stream the fraction of tasks from competitions unseen in the first third reaches 100%. The number of competitions represented in a 50-task window also varies substantially, so neighboring tasks can require different assumptions about file layout, scoring conventions, and intended exploitation style. The cross-competition score coefficient of variation further indicates that competitions are not interchangeable pools; each event can calibrate difficulty and challenge design differently. This motivates persistent construction of reusable security skills, but also cautions against treating early CTF experience as uniformly transferable.

FutureX. FutureX shifts along source, language, and difficulty dimensions (Figure 14 ). Batch-level baseline accuracy ranges from 20% to 80%, showing that chronological batches differ substantially in solvability. Later batches contain more Chinese-titled questions and more questions tied to platforms that are difficult to search directly, while the share of harder Level 3–4 questions increases sharply in the same region. Chinese-language answer requirements also appear mainly in later batches. These changes explain why FutureX stresses both construction and adaptation: the harness must acquire better source-finding and temporal retrieval behavior, while solve-time routing must select branches suited to the task’s language, source, and difficulty profile.

## Appendix D Further Experiments

We include two supplemental diagnostics that clarify where the main gains come from without duplicating the RQ analyses in § 4 .

Evolver capability and construction budget. Figure 10 varies the evolver model and construction budget on CTF-Dojo. Stronger evolvers achieve higher pass rates, while additional budget mainly helps weaker evolvers and saturates for the strongest model.

Cross-domain workspace dilution. Figure 11 compares PolyBench CWR when using workspaces evolved on different domains. The PolyBench-specific workspace performs best, while the all-evolved workspace loses 57 points of CWR, showing that mixing heterogeneous experience can dilute domain-relevant harness structure.

## Appendix E Per-Domain and Per-Category Breakdowns

CTF-Dojo. Table 6 reports Pass@1 by category. The Full System gains the most on web ( + 27 +27 over Sonnet) and crypto ( + 19 +19 ); binary/pwn remains the hardest category at 14.8 % 14.8\% even after evolution and routing, consistent with the sandbox payload-handling bottleneck identified in § 4.3 .

FutureX. Table 7 reports Pass@1 by language and inferred domain. English-language slices benefit most from evolution; the small zh-finance slice illustrates the source-discovery bottleneck where neither evolution nor routing alone can recover when the platform is behind a search wall. Domains are inferred by keyword match on the question text, since FutureX results do not store the official domain tags; the other bucket therefore aggregates unmatched questions.

PolyBench. Table 8 reports Accuracy/Return per inferred category. Sports dominates the portfolio ratio because liquid sports markets carry most of the dollar-weighted profit; politics carries near-zero return despite high accuracy. Categories are inferred by keyword match on the trajectory prompt’s Event description.

## Appendix F Multi-Agent Evolution Dynamics

Table 9 reports the full-stream system contrast (No-evo → \to Single-agent → \to Multi-agent) plus the timing of the multi-agent run, complementing rather than reproducing Figure 6 . The figure runs the four-phase evolver against No-memory and No-feedback ablations on a curated subset of samples; the table here instead reports the headline metric of each system on the full benchmark, matching the Multi-agent column of Table 2 . The unique signal added is timing: the Peak column gives the cycle index at which the multi-agent run’s cumulative mean was highest, and a peak well before the final cycle is consistent with the overfitting trend in Figure 1 . On PolyBench the multi-agent peak occurs at cycle 22 of 51 and on FutureX at cycle 10 of 26, while CTF-Dojo continues to accumulate utility across all 14 cycles.

## Appendix G Routing Behaviour and Branch Performance

This appendix expands the routing analysis behind Figure 7 . We use two related but distinct subsets per benchmark: (i) the nav-run subset (CTF-Dojo: 60 tasks, PolyBench: 100, FutureX: 80) on which the LLM router was deployed live and we observe its branch assignments; and (ii) the replay subset (CTF-Dojo: 40, PolyBench: 80, FutureX: 58), a subset of the same tasks for which every branch has been replayed end-to-end so each task carries a complete cross-venue score vector. The replay subset is necessarily smaller because some early-cycle branches did not exist for batch 1 tasks. Four per-task series are derived from the replay subset: Oracle = best venue, Adapt = the LLM router’s actual choice on the nav run, Naive = the fixed main venue (no branching), and Worst = worst venue.

Where the router sends each task. Table 10 reports the per-branch routing volume and pass rate over the nav-run subset. The router prompt (Appendix J ) does allow a main fallback when no branch matches strongly, but on these subsets the router always identifies a regime-specific branch and never invokes that fallback. Branches with low realised pass rates (e.g. branch/pwn on CTF-Dojo, branch/lvl3 on FutureX) are not failing branches per se — the router sends genuinely hard tasks to them, and the corresponding tasks have low Oracle pass rates on the replay subset as well (Table 11 ).

How much routing recovers of the adaptation gap. Table 11 gives the headline Oracle/Adapt/Naive/Worst comparison on the replay subset, with 95% bootstrap CIs and Holm–Bonferroni-corrected paired Wilcoxon p -values. The Oracle − - Naive gap, our empirical estimate of the adaptation loss L adapt L_{\mathrm{adapt}} , is large and significant on CTF-Dojo ( + 37.5 +37.5 pp, p adj = 4.8 × 10 − 4 p_{\mathrm{adj}}\!=\!4.8\times 10^{-4} ) and PolyBench ( + 8.8 +8.8 pp CWR, p adj = 1.8 × 10 − 5 p_{\mathrm{adj}}\!=\!1.8\times 10^{-5} ); on FutureX the gap is smaller and not significant after correction, consistent with the § 4.3 finding that source acquisition rather than branch choice is the binding capability there. Adapt closes a substantial fraction of the gap on CTF-Dojo and PolyBench but trails Naive slightly on FutureX, again reflecting the source-acquisition bottleneck.

Per-batch view. Table 12 reports the same series broken out by batch on the replay subset (only batches with full cross-branch replays are shown, so e.g. CTF-Dojo includes batches 2 and 3 only). CTF-Dojo’s branch tree improves between these two batches (Oracle → 65 45\!\to\!65 %) as new specialisations come online; PolyBench shows a quiet batch 4 followed by a sports-led recovery in batch 5; FutureX’s batch 3 has the widest Oracle − - Adapt headroom, where the router’s level-based branches were less reliable than main on the same tasks.

## Appendix H Human-in-the-Loop Event Log

Table 13 reports the full HITL event log from the FutureX RQ5 run (§ 4.6 ). The run uses the curated 5-batch FutureX stream (Design C: 100 tasks, 5 × \times 20) with two engineered regime shifts, a Sonnet 4.6 solver, an Opus 4.6 evolver, and hitl_enabled=true . The Analyst and Builder decide when to invoke each hook; the human responds via Telegram from a pre-authored cheat-sheet. Two P2 (research-phase) events fire at cycle 1 to bootstrap the search pipeline, and one substantive P3 (task-board) event fires at cycle 3 to steer the evolver toward Western and Chinese specialty endpoints. The remaining P3 prompts (cycles 1, 2, 4, and 5) return skip , matching the cheat-sheet protocol that the human only intervenes when the cheat-sheet has a relevant entry. The slice-level lift on each regime ( 0 0 , + 5 +5 , + 20 +20 , + 15 +15 , 0 0 on regimes 1–5) is reported in Figure 9 .

## Appendix I Run-Detail Analysis

Table 14 reports per-task turn counts and elapsed seconds, complementing the aggregate cost summary in Table 5 . Both distributions are right-skewed on CTF-Dojo and FutureX, where a small number of long-running tasks pull the mean above the median; we therefore report both. CTF-Dojo’s solver budget is consistently saturated — Sonnet’s mean of 89.4 turns reflects a large mass of tasks that loop until the cap, whereas the evolved variants typically reach a flag (or give up) earlier. PolyBench is dominated by direct decisions: most tasks submit immediately (turn count 1) because the prompt already contains the market context the solver needs.

## Appendix J System Prompts

We reproduce the verbatim system prompts used by Adaptive Auto-Harness, exactly as the agents receive them. Curly-brace placeholders such as {benchmark_context} , {regime} , {workspace_extras} , and {categories} are substituted by the framework at runtime per benchmark or per regime; we leave them in place so the templating is visible.

⬇

⬇

⬇

⬇

⬇

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
