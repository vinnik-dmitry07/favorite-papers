##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Harnessing Agentic Evolution

###### Abstract

Agentic evolution has emerged as a powerful paradigm for improving programs, workflows, and scientific solutions by iteratively generating candidates, evaluating them, and using feedback to guide future search. However, existing methods are typically instantiated either as fixed hand-designed procedures that are modular but rigid, or as general-purpose agents that flexibly integrate feedback but can drift in long-horizon evolution. Both forms accumulate rich evidence over time, including candidates, feedback, traces, and failures, yet lack a stable interface for organizing this evidence and revising the mechanism that drives future evolution. We address this limitation by formulating agentic evolution as an interactive environment , where the accumulated evolution context serves as a process-level state. We introduce AEvo , a harnessed meta-editing framework in which a meta-agent observes this state and acts not by directly proposing the next candidate, but by editing the procedure or agent context that controls future evolution. This unified interface enables AEvo to steer both procedure-based and agent-based evolution, making accumulated evidence actionable for long-horizon search. Empirical evaluations on agentic and reasoning benchmarks show that AEvo outperforms five evolution baselines, achieving a 26% relative improvement over the strongest baseline. Across three open-ended optimization tasks, AEvo further outperforms four evolution baselines and achieves state-of-the-art performance under the same iteration budget.

## 1 Introduction

Agentic evolution reframes LLM-based problem solving as a process of constructing and revising solutions [ 16 , 7 ] . Instead of treating the model only as a generator of candidate answers, these methods use LLMs, agentic workflows, or coding agents to drive iterative improvement: produce candidate artifacts, interpret feedback from evaluation, and influence what the system explores next [ 22 ] . This paradigm has been applied to program synthesis [ 10 ] , scientific discovery [ 17 , 38 ] , systems optimization [ 25 , 6 ] , and agent self-improvement [ 41 , 27 , 23 ] . In this paper, we use agentic evolution to broadly refer to evolution processes whose search behavior is driven by either structured agentic procedures or general-purpose agents.

Existing agentic evolution methods typically instantiate this paradigm in two ways. In procedure-based evolution , a predefined outer loop controls parent selection, candidate generation, evaluation, and population update [ 18 , 36 , 42 ] . This makes evolution modular and reproducible, but also ties long-horizon search to fixed selection rules, feedback summaries, and update heuristics. In agent-based evolution , a general-purpose agent manages the search process by observing feedback, inspecting traces, editing candidates, writing tools, and deciding what to try next [ 11 , 22 ] . This gives evolution greater flexibility, but the agent can drift as candidates, logs, hypotheses, and intermediate files accumulate. In both cases, long-horizon evolution remains prone to local optima: procedures may repeatedly exploit the same hand-designed search pattern, while agents may overcommit to misleading evidence or stale assumptions in a growing context.

Recent work has tried to address these limitations by either broadening exploration with collaborative agents [ 22 ] or making the evolution mechanism self-modifying [ 41 ] . These directions show that stronger search context and editable improvement mechanisms are useful, but they do not by themselves provide a stable interface for long-horizon evolution. The core challenge is that evolution accumulates candidates, feedback, traces, failures, and intermediate decisions over time, yet lacks a unified way to organize this evidence and revise the mechanism that drives future evolution.

We address this challenge by formulating agentic evolution as an interactive environment . As illustrated in Figure 1 , this view shifts evolution from an unstructured iterative process into an environment that exposes process-level state and supports external intervention. The state is the accumulated evolution context, including candidates, feedback, traces, failures, costs, and search history. The transition mechanism is the current evolution mechanism: either an explicit search procedure or the operating context that shapes a general-purpose agent’s future decisions. A meta-agent acts on this environment not by generating the next candidate, but by editing the mechanism that controls how future evolution proceeds. This makes the same environment view applicable to both hand-designed procedures and general-purpose evolution agents.

Realizing this view requires a harnessed design. The evolution environment is large, noisy, and constantly changing. Without a stable interface, a meta-agent may lose track of reliable evidence, revisit old attempts or make edits whose effects are hard to verify. At the same time, evaluation and candidate records must remain protected from the agents that modify the evolution process. These challenges motivate a harness that makes evolution observable, editable, and externally governed.

We therefore introduce AEvo , a harnessed framework for meta-editing agentic evolution. AEvo standardizes the evolution workspace, protects the evaluator, records every evaluated candidate into a searchable history, and exposes process-level information to the meta-agent. It then runs evolution through a two-phase loop. In the meta-editing phase, the meta-agent edits the current mechanism and specifies how the next segment should run. In the evolution segment, the updated mechanism runs under this plan and produces multiple candidates before the next meta-agent intervention. The same loop can revise both procedure- and agent-based evolution, reducing the risk of local optima.

Our contributions are threefold. (1) Environment Formulation: We formulate agentic evolution as an interactive environment, where accumulated evolution context becomes process-level state and meta-actions edit the mechanism that drives future evolution. (2) Harnessed Meta-Editing: We introduce AEvo , a harnessed framework for meta-editing agentic evolution that protects evaluation, records evaluated candidates, and supports coarse-grained intervention through meta-editing phases and evolution segments. (3) Cross-Form Instantiation and Evaluation: We instantiate the same framework on both procedure-based and agent-based evolution, showing that AEvo can revise either explicit procedure components or agent operating contexts. On standard agentic and reasoning benchmarks, AEvo outperforms five evolution baselines and achieves a 26% relative improvement over the strongest baseline. On three open-ended optimization tasks, AEvo outperforms four evolution baselines and achieves state-of-the-art performance under the same iteration budget.

## 2 Related Work

Agentic Evolution. A growing line of work uses LLMs and agents to iteratively improve artifacts through generation, feedback, and revision [ 15 , 14 , 13 , 28 ] . Prompt methods optimize language-model programs or feedback-driven prompts, including DSPy [ 12 ] , SPO [ 30 ] , TextGrad [ 37 ] , and GEPA [ 1 ] . Another line studies the automated design and evolution of agentic systems and workflows, such as ADAS [ 9 ] , Darwin Gödel Machine [ 40 ] , Huxley-Gödel Machine [ 27 ] , AFlow [ 42 ] , RobustFlow [ 32 ] , and SkillRL [ 29 ] . Recent open-ended discovery systems further apply evolutionary search to scientific and algorithmic discovery, including AlphaEvolve [ 18 ] , OpenEvolve [ 24 ] , TTS-Discover [ 38 ] , CORAL [ 22 ] , SimpleTES [ 36 ] , and ASI-Evolve [ 33 ] . However, their search behavior is typically controlled either by fixed procedures or by agents directly managing candidate generation. In contrast, AEvo treats the evolution process itself as an interactive environment and studies how to steer the mechanism that controls future search.

Agentic Meta-Evolution. Early meta-learning work showed that the learning rule itself can be optimized, for example by learning recurrent reinforcement-learning dynamics [ 26 ] or evolving policy-gradient objectives [ 8 ] . Recent agentic systems extend this idea to editable agent programs and memory systems. HyperAgents study self-referential agent programs in which both task-solving behavior and the meta-improvement mechanism can be modified [ 41 ] . MemEvolve and ALMA similarly explore meta-evolution over agent memory designs [ 39 , 31 ] . Unlike HyperAgents, which internalize meta-improvement within a self-modifying agent program, AEvo treats agentic evolution as an interactive environment observed and edited through an external harness, covering both hand-designed procedures and general-purpose agents while keeping evaluation and candidate recording externally governed.

## 3 Problem Formulation

### 3.1 Agentic Evolution

We formulate agentic evolution as a process for optimizing an artifact through repeated improvement rounds. Let x ∈ 𝒳 x\in\mathcal{X} denote the object being optimized, such as a program, prompt, workflow, skill, tool, or agent component. We use r r to index the evolution round. Each round produces a round context c r c_{r} , which contains the candidates generated in that round, their evaluation results, execution traces, failures, costs, and any intermediate information produced during optimization. The accumulated evolution context after r r rounds is denoted as 𝒞 r = ( c 1 , c 2 , … , c r ) . \mathcal{C}_{r}=(c_{1},c_{2},\ldots,c_{r}). Finally, let Π \Pi denote the optimization mechanism that advances evolution: c r = Π ⁡ ( 𝒞 r − 1 ) , 𝒞 r = 𝒞 r − 1 ⊕ c r , c_{r}=\Pi(\mathcal{C}_{r-1}),\qquad\mathcal{C}_{r}=\mathcal{C}_{r-1}\oplus c_{r}, where ⊕ \oplus appends the newly produced round context to the accumulated evolution context. Π \Pi does not have to be a fixed algorithm; it can also be an agentic process that reads the history, reasons over feedback, and decides how to generate the next candidate. Thus, Π \Pi represents the mechanism by which search is continued from the current evolution context.

Under this formulation, existing agentic evolution methods mainly differ in how Π \Pi is instantiated. In procedure-based evolution , Π \Pi is a predefined outer loop whose behavior is mainly determined by selection and optimization: the selection rule chooses previous candidates or contexts from 𝒞 r − 1 \mathcal{C}_{r-1} , while the optimization operator generates new candidates from the selected information. Evaluation assigns scores, traces, and feedback to the generated candidates, providing signals for future selection and update. In agent-based evolution , Π \Pi is instead implemented by a general-purpose agent. Rather than following fixed selection-and-optimization rules, the agent reads the accumulated context 𝒞 r − 1 \mathcal{C}_{r-1} and decides what to do next, such as inspecting feedback, comparing candidates, modifying artifacts, writing tools, or generating new attempts. Thus, procedure-based evolution specifies search control explicitly but rigidly, while agent-based evolution leaves search control implicit in the agent’s context-conditioned behavior.

In both cases, evolution proceeds by repeatedly applying Π \Pi while accumulating context 𝒞 r \mathcal{C}_{r} . This context records not only the candidates produced by evolution, but also how search has unfolded through evaluation results, traces, failures, costs, and intermediate artifacts. The next subsection uses this accumulated context to define an environment view of evolution.

### 3.2 Evolution as an Interactive Environment

We treat the evolution process itself as an interactive environment for a meta-agent. At round r r , the state of this environment is defined by the round index and the accumulated evolution context: s r = ( r , 𝒞 r ) . s_{r}=(r,\mathcal{C}_{r}). When the optimization mechanism may change across rounds, we write the current mechanism as Π r \Pi_{r} . This mechanism specifies the transition of the environment. Without intervention, the next round is produced by applying the current mechanism to the current context: c r + 1 = Π r ​ ( 𝒞 r ) , s r + 1 = ( r + 1 , 𝒞 r ⊕ c r + 1 ) . c_{r+1}=\Pi_{r}(\mathcal{C}_{r}),\qquad s_{r+1}=(r+1,\mathcal{C}_{r}\oplus c_{r+1}). Thus, Π r \Pi_{r} is the transition rule that determines how the evolution process continues.

To interact with this environment, we introduce a meta-agent M M . The role of Π r \Pi_{r} is to continue the candidate search, while the role of M M is to act on the evolution process that governs this search. Since the full state s r s_{r} can be large and noisy, the meta-agent receives an observation extracted from the state: o r = Φ ⁡ ( s r ) = Φ ⁡ ( r , 𝒞 r ) , o_{r}=\Phi(s_{r})=\Phi(r,\mathcal{C}_{r}), where Φ \Phi summarizes relevant information from the accumulated context, such as progress, repeated failures, invalid attempts, cost patterns, or redundant search directions.

Given this observation, the meta-agent produces an edit action: a r = M ⁡ ( o r ) . a_{r}=M(o_{r}). The action does not directly become the next candidate. Instead, it modifies the transition rule of the evolution environment: Π r + 1 = Edit ⁡ ( Π r , a r ) . \Pi_{r+1}=\mathrm{Edit}(\Pi_{r},a_{r}). The edited mechanism is then used to continue evolution: c r + 1 = Π r + 1 ​ ( 𝒞 r ) , 𝒞 r + 1 = 𝒞 r ⊕ c r + 1 . c_{r+1}=\Pi_{r+1}(\mathcal{C}_{r}),\qquad\mathcal{C}_{r+1}=\mathcal{C}_{r}\oplus c_{r+1}. In this sense, we formulate agentic evolution as an environment in which the state is the accumulated evolution context, the observation is a summary of this context, and the action edits the mechanism that controls future search.

This formulation applies to both forms of agentic evolution. For procedure-based evolution , editing Π r \Pi_{r} changes explicit components such as selection, optimization, feedback use, budget allocation, or update rules. For agent-based evolution, editing Π r \Pi_{r} changes the agentic context that shapes future decisions, such as skills, goals, tools, feedback format, or execution context. In both cases, the meta-agent steers evolution not by proposing one more candidate, but by modifying how subsequent search is carried out. Section 4 describes the system design used to instantiate this formulation.

## 4 Methodology

Figure 2 illustrates AEvo . AEvo instantiates the environment view in Section 3 as a harnessed loop that alternates between a meta-editing phase and an evolution segment . In the meta-editing phase, the meta-agent updates the current evolution mechanism Π r \Pi_{r} and specifies how the next segment should run, including its iteration budget and stopping conditions. In the evolution segment, the updated mechanism runs under this plan and may produce multiple evaluated candidates before the next meta-agent intervention. Thus, one meta-edit can govern a segment of future evolution rather than a single candidate.

### 4.1 Design of AEvo

Meta-editing phase. The meta-editing phase decides both what to change and how to continue . The meta-agent can be any coding-capable agent that can inspect a workspace, edit files, execute commands, and follow the AEvo meta-agent skill specification, such as Claude Code [ 3 ] , Codex [ 19 ] , or open-source coding agents [ 34 , 20 ] . Given the current workspace, it inspects the accumulated history, then produces a meta-action consisting of a workspace edit and a run plan. The workspace edit modifies files that define Π r \Pi_{r} , such as procedure code, prompts, skills, goals, tools, feedback formats, validators, notes, or execution context. The run plan specifies how the next evolution segment should proceed, including the allowed iterations, budget use, and stopping conditions.

This design makes the meta-agent a process-level editor rather than a candidate generator: it changes the mechanism and conditions under which future candidates are produced. When evolution is productive, the meta-agent may allocate more iterations to the current mechanism; when it repeatedly produces invalid candidates, redundant attempts, or irrelevant exploration, the meta-agent may stop the segment and revise Π r \Pi_{r} before continuing. The full meta-agent skill specification and pseudocode of the meta-editing loop are provided in Appendix C.2.3 .

Harnessed evolution segment. An evolution segment is the interval executed after a meta-edit. It runs the current mechanism Π r \Pi_{r} under the run plan produced by the meta-agent. Depending on the setting, this segment may consist of several rounds of a procedure, or an inner-agent session that produces multiple candidate attempts. Each candidate submitted for official evaluation passes through the harness-controlled evaluator, and the resulting artifact, score, trace, failure information, cost, and provenance are appended to the candidate history.

The harness provides the stable boundary needed for reliable meta-editing. It organizes candidates, logs, traces, evaluation records, meta-agent instructions, and editable evolution components into a fixed workspace layout. To prevent reward hacking, the evaluator is isolated from both the evolution agent and the meta-agent: agents can submit candidates, but they cannot inspect evaluator internals, access hidden benchmark artifacts, or directly write official scores. The harness further exposes a command-line interface for initializing workspaces, launching evolution segments, inspecting recent status and candidate history, and continuing the current process. Thus, the harness does not decide how evolution should improve; it provides the protected and inspectable interface through which evolution can be observed, edited by the meta-agent, recorded, and resumed.

### 4.2 Instantiating AEvo

AEvo applies the same two-phase loop to both forms of agentic evolution. The outer loop is unchanged: the meta-agent edits the current mechanism Π r \Pi_{r} and specifies how the next evolution segment should run. The difference lies in what Π r \Pi_{r} consists of.

Procedure-based evolution. For procedure-based evolution, Π r \Pi_{r} is an explicit evolution procedure. It defines how previous candidates or contexts are selected, how new candidates are generated, how evaluation feedback is used, and how candidate history is updated. A meta-action therefore edits the procedure itself, such as revising the selection strategy, changing the optimization operator, altering the feedback summary, adding local filtering or retry logic, adjusting budget use, or repairing candidate management. The edited procedure then controls the next evolution segment, which may run for multiple rounds before the next meta-agent intervention.

Agent-based evolution. For agent-based evolution, Π r \Pi_{r} is the operating context of a general-purpose evolution agent, including goals, skills, tools, memory files, shared notes, validators, and execution setup. A meta-action therefore edits the conditions under which the next inner-agent session will evolve, such as revising a skill, rewriting the session goal, changing how evaluator feedback is presented, or reorganizing shared notes. The inner agent remains responsible for generating candidates, while AEvo revises the context that shapes future evolution.

## 5 Experiments

### 5.1 Settings

Tasks. We evaluate AEvo on two standard benchmarks, Terminal-Bench [ 25 ] and ARC-AGI-2 [ 5 ] , and three open-ended optimization tasks, circle_packing_26 (CP26) [ 21 ] , autocorrelation_second (AC2) [ 4 ] , and Anthropic’s Kernel optimization task [ 2 ] . Together, these tasks cover agentic problem solving, abstract reasoning, and code-evolving open-ended optimization. Detailed task definitions and evaluation protocols are given in Appendix C.1 .

Baselines. We group baselines into three families: single-agent inference, agent-based evolution, and procedure-based evolution. On Terminal-Bench and ARC-AGI-2, we compare against one-shot ReAct [ 35 ] and five procedure-based evolution baselines: ADAS [ 9 ] , DGM [ 40 ] , AFlow [ 42 ] , SPO [ 30 ] , and GEPA [ 1 ] . On the three open-ended tasks, we compare against two agent-based evolution baselines, Codex and Claude Code, and two procedure-based evolution baselines, OpenEvolve [ 24 ] and HyperAgents [ 41 ] . This setup lets us compare both variants of AEvo against systems that either keep a fixed search procedure or rely on an agent to improve artifacts directly.

Implementation Details. AEvo is instantiated in two forms. In the procedure-based setting, a meta-agent edits the evolution procedure while leaving the task evaluator fixed. In the agent-based setting, the meta-agent steers a coding-agent harness through prompts, notes, and reusable utilities. We use Claude Code and Codex as the meta-agent interfaces, backed by Claude-Opus-4.7 and GPT-5.4 as the optimization models. For Terminal-Bench and ARC-AGI-2, candidate execution uses Gemini-3-Flash. All models are accessed through APIs. Full hyperparameter settings, round budgets, early-stopping criteria, and initialization details are given in Appendix B .

Metrics. For Terminal-Bench and ARC-AGI-2, we report task score and the first optimization round that reaches the best score. Results are summarized with Avg@3 over three independent runs. For the open-ended tasks, we report the task-native objective with Best@3 over three runs, together with the first round that reaches the best result (Best R.) and the average dollar cost per optimization round ($/R). Exact task-specific objectives and cost computation are provided in Appendix C.1 .

### 5.2 Main Results

Overall performance. Tables 1 and 2 show that AEvo consistently improves agentic evolution across both open-ended optimization and fixed benchmarks. On the open-ended tasks, AEvo achieves the best or tied-best result on all three tasks, while also improving the speed or stability with which strong candidates are found. In particular, on the Kernel optimization task, AEvo achieves 1138 cycles within 100 iterations, which is, to our knowledge, the best reported result under the same iteration budget. This suggests that the harnessed meta-editing loop improves how evolution uses feedback over time, rather than merely increasing the number of candidate attempts. On standard agentic and reasoning benchmarks, AEvo also improves procedure-based evolution over strong fixed-loop baselines. The gains are consistent across both Terminal-Bench and ARC-AGI-2, yielding a 26% relative improvement over the strongest baseline on average. Together, these results support the central claim that mechanism-level intervention can benefit both open-ended optimization and benchmark-driven agentic evolution.

Improvement through optimization-time reasoning. The gains on Table 2 come with a higher per-round optimization cost. AEvo costs about three times as much as procedure-based baselines on these benchmarks. This means that AEvo improves performance by scaling the reasoning and deliberation used during optimization, and supports our view that increasing the budget of the evolution process is a useful axis for improving agentic evolution.

Cost analysis and agentic behavior. The open-ended tasks reveal that cost is not solely determined by whether a method is agent-based or procedure-based. Agent-based evolution can remain cost-competitive when implemented through coding-agent interfaces with prompt caching and persistent contexts. AEvo Agent {}_{\texttt{Agent}} maintains low per-round cost: 0.34–0.32 on circle_packing_26 , 1.40–1.31 on autocorrelation_second , and 1.27–1.23 on Kernel optimization. By contrast, procedure-based methods can become expensive in long-horizon optimization by repeatedly constructing large prompts over an expanding search history without comparable caching, as visible in HyperAgents’ higher per-round cost on Task 1 and Task 2.

At the same time, direct coding agents show why agent freedom alone is insufficient for reliable evolution. Even with prompts encouraging long-horizon search, coding agents often stop early once local improvements become difficult, as seen in the early best rounds of Codex on Task 1 and Task 3. This suggests that an agent’s internal stopping decision can conflict with the external evolution budget. AEvo addresses this by placing the coding agent inside an explicit evolution harness, where rounds, candidate records, and evaluation feedback are maintained outside the agent’s local decision loop.

### 5.3 Evolution Dynamics

Revising evolution after plateaus. As shown in Figure 3 , procedure-based methods such as OpenEvolve and HyperAgents tend to flatten once their current selection or mutation strategy stops producing useful candidates. In contrast, AEvo can revise the mechanism that drives subsequent evolution. When progress stalls or repeated failures appear, these signals become process-level feedback: the meta-agent can adjust the procedure, directive, or reusable search context, producing step-wise improvements after plateaus. This is visible in the late-stage jump that leads to the best 100-round result.

Using the evolution budget effectively. Direct coding agents can obtain strong early gains through internal simulation, execution, and debugging, but they may stop early once local progress becomes difficult. AEvo avoids tying progress to the agent’s local stopping decision by maintaining explicit rounds, candidate records, and evaluation feedback outside the agent context. This allows the external evolution budget to be used more consistently.

Scaling beyond early gains. The right panel extends Codex-based AEvo from 100 to 200 iterations. The best result improves from 1138 to 1121 cycles, showing that AEvo continues to benefit from additional rounds rather than saturating after an early strong candidate. Overall, the trajectories suggest that agent flexibility is useful, but reliable long-horizon improvement requires a harness that preserves global evidence and enables mechanism-level correction.

### 5.4 Ablation Study

Table 3 (Appendix) ablates two key components of AEvo Agent {}_{\texttt{Agent}} on the Kernel optimization task. The full system completes the 100-round budget without reward hacking and reaches the best valid result of 1138 cycles. Removing meta-agent skills does not lead to reward hacking, but it substantially weakens long-horizon search: the best run only reaches 1407 cycles, and the runs do not consistently sustain the full budget. Removing the evolution harness is even less reliable. Although one run finds a strong 1167-cycle solution, two of the three runs enter reward-hacking trajectories and fail to produce valid cycle results. These results suggest that the skills mainly support sustained and effective meta-intervention, while the harness provides the protected evaluation boundary and structured evolution context needed to keep agentic search aligned with the true objective.

### 5.5 Case Study

Figure 4 illustrates how AEvo performs meta-intervention during procedure-based evolution on an ARC-AGI-2 task. Starting from P 0 P_{0} , the meta-agent initializes a best-parent rewrite procedure that selects candidate agents by validation accuracy. This first produces an initial breakthrough candidate C 1 C_{1} , but subsequent variants expose several failure modes in observation parsing and refinement. The meta-agent then revises the procedure rather than continuing the same search blindly: P 1 P_{1} adds Pass@K sampling and local scoring for verifier-guided generation, P 2 P_{2} fixes observation parsing to activate feedback-guided refinement, and P 3 P_{3} extends the refinement horizon to use more pass/fail feedback before submission. When the search becomes stuck, P 4 P_{4} drops stale feedback and samples more diverse alternatives, leading to a stronger candidate. Later interventions P 5 P_{5} – P 6 P_{6} explore stronger de-anchoring through task-profile and skeleton prompts, but these regress from P 4 P_{4} . This example shows that failed candidates are not merely discarded; they become process-level evidence that helps the meta-agent decide how to revise the future evolution procedure. Additional evolved procedures, optimized agent harnesses, and task-level analyses are provided in Appendix C.3.1 and Appendix C.3.2 .

## 6 Conclusion

We presented AEvo , a harnessed framework for steering agentic evolution by treating the evolution process itself as an interactive environment. Instead of generating one more candidate, AEvo exposes accumulated candidates, feedback, traces, failures, costs, and search history as process-level evidence, and uses a meta-agent to edit the mechanism that controls future evolution. This formulation provides a unified view of procedure-based and agent-based evolution: the same meta-editing loop can revise explicit search procedures or the operating context of general-purpose evolution agents, while keeping evaluation and candidate recording protected by an external harness. Across agentic, reasoning, and open-ended optimization tasks, AEvo improves over strong fixed-procedure and agent-based baselines, suggesting that long-horizon evolution benefits not only from stronger candidate generators, but also from mechanism-level intervention over how search proceeds. Future work should study more diverse evolution environments, cheaper meta-intervention strategies, and safer deployment of harnessed agentic evolution for scientific discovery, software engineering, and autonomous code optimization.

## References

[1] L. A. Agrawal, S. Tan, D. Soylu, N. Ziems, R. Khare, K. Opsahl-Ong, A. Singhvi, H. Shandilya, M. J. Ryan, M. Jiang, et al. (2025) Gepa: reflective prompt evolution can outperform reinforcement learning . arXiv preprint arXiv:2507.19457 . Cited by: §2 , §5.1 .

[2] Anthropic PBC (2026) Anthropic’s Original Performance Take-Home . Note: https://github.com/anthropics/original_performance_takehome GitHub repository, commit 5452f74. Accessed: 2026-05-06 Cited by: §5.1 .

[3] Anthropic (2025) Claude Code . Note: https://docs.anthropic.com/en/docs/claude-code/overview Cited by: §4.1 .

[4] C. Boyer and Z. K. Li (2026) An improved example for an autoconvolution inequality . Experimental Mathematics , pp. 1–7 . Cited by: §5.1 .

[5] F. Chollet, M. Knoop, G. Kamradt, B. Landers, and H. Pinkard (2025) Arc-agi-2: a new challenge for frontier ai reasoning systems . arXiv preprint arXiv:2505.11831 . Cited by: §5.1 .

[6] M. Deng, L. Huang, Y. Fan, J. Zhang, F. Ren, J. Bai, F. Yang, D. Miao, Z. Yu, Y. Wu, et al. (2025) Interactcomp: evaluating search agents with ambiguous queries . arXiv preprint arXiv:2510.24668 . Cited by: §1 .

[7] H. Gao, J. Geng, W. Hua, M. Hu, X. Juan, H. Liu, S. Liu, J. Qiu, X. Qi, Y. Wu, et al. (2025) A survey of self-evolving agents: on path to artificial super intelligence . arXiv preprint arXiv:2507.21046 . Cited by: §1 .

[8] R. Houthooft, Y. Chen, P. Isola, B. Stadie, F. Wolski, O. Jonathan Ho, and P. Abbeel (2018) Evolved policy gradients . Advances in Neural Information Processing Systems 31 . Cited by: §2 .

[9] S. Hu, C. Lu, and J. Clune (2024) Automated design of agentic systems . arXiv preprint arXiv:2408.08435 . Cited by: §2 , §5.1 .

[10] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan (2023) Swe-bench: can language models resolve real-world github issues? . arXiv preprint arXiv:2310.06770 . Cited by: §1 .

[11] A. Karpathy (2026) Autoresearch: ai agents running research on single-gpu nanochat training automatically . Note: GitHub repositoryAccessed: 2026-05-06 Cited by: §1 .

[12] O. Khattab, A. Singhvi, P. Maheshwari, Z. Zhang, K. Santhanam, S. Vardhamanan, S. Haq, A. Sharma, T. T. Joshi, H. Moazam, H. Miller, M. Zaharia, and C. Potts (2024) DSPy: compiling declarative language model calls into self-improving pipelines . Cited by: §2 .

[13] B. Li, C. Chen, Z. Xue, Y. Mei, and Y. Luo (2025) DeepEye-sql: A software-engineering-inspired text-to-sql framework . CoRR abs/2510.17586 . Cited by: §2 .

[14] B. Li, Y. Peng, Y. Xie, S. Lu, Y. Zhu, X. Mu, X. Liu, and Y. Luo (2026) DeepEye: a steerable self-driving data agent system . In Companion of the 2026 International Conference on Management of Data , SIGMOD Companion ’26 , Bengaluru, India . External Links: Document Cited by: §2 .

[15] B. Li, J. Zhang, J. Fan, Y. Xu, C. Chen, N. Tang, and Y. Luo (2025) Alpha-sql: zero-shot text-to-sql using monte carlo tree search . In ICML , Cited by: §2 .

[16] B. Liu, X. Li, J. Zhang, J. Wang, T. He, S. Hong, H. Liu, S. Zhang, K. Song, K. Zhu, et al. (2025) Advances and challenges in foundation agents: from brain-inspired intelligence to evolutionary, collaborative, and safe systems . arXiv preprint arXiv:2504.01990 . Cited by: §1 .

[17] C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha (2024) The ai scientist: towards fully automated open-ended scientific discovery . arXiv preprint arXiv:2408.06292 . Cited by: §1 .

[18] A. Novikov, N. Vũ, M. Eisenberger, E. Dupont, P. Huang, A. Z. Wagner, S. Shirobokov, B. Kozlovskii, F. J. Ruiz, A. Mehrabian, et al. (2025) Alphaevolve: a coding agent for scientific and algorithmic discovery . arXiv preprint arXiv:2506.13131 . Cited by: §1 , §2 .

[19] OpenAI (2025) Codex . Note: https://openai.com/index/introducing-codex/ Cited by: §4.1 .

[20] OpenCode (2025) OpenCode: the open source AI coding agent . Note: https://opencode.ai Cited by: §4.1 .

[21] R. Peikert, D. Würtz, M. Monagan, and C. de Groot (2007) Packing circles in a square: a review and new results . In System Modelling and Optimization: Proceedings of the 15th IFIP Conference Zurich, Switzerland, September 2–6, 1991 , pp. 45–54 . Cited by: §5.1 .

[22] A. Qu, H. Zheng, Z. Zhou, Y. Yan, Y. Tang, S. Y. Ong, F. Hong, K. Zhou, C. Jiang, M. Kong, et al. (2026) CORAL: towards autonomous multi-agent evolution for open-ended discovery . arXiv preprint arXiv:2604.01658 . Cited by: §1 , §1 , §1 , §2 .

[23] J. Ruan, Z. Xu, Y. Peng, F. Ren, Z. Yu, X. Liang, J. Xiang, Y. Chen, B. Liu, C. Wu, et al. (2026) AOrchestra: automating sub-agent creation for agentic orchestration . arXiv preprint arXiv:2602.03786 . Cited by: §1 .

[24] OpenEvolve: an open-source evolutionary coding agent External Links: Link Cited by: §2 , §5.1 .

[25] T. T. Team (2025) Terminal-bench: a benchmark for ai agents in terminal environments . External Links: Link Cited by: §1 , §5.1 .

[26] J. X. Wang, Z. Kurth-Nelson, D. Tirumala, H. Soyer, J. Z. Leibo, R. Munos, C. Blundell, D. Kumaran, and M. Botvinick (2016) Learning to reinforcement learn . arXiv preprint arXiv:1611.05763 . Cited by: §2 .

[27] W. Wang, P. Piekos, L. Nanbo, F. Laakom, Y. Chen, M. Ostaszewski, M. Zhuge, and J. Schmidhuber (2025) Huxley-g \ \backslash " odel machine: human-level coding agent development by an approximation of the optimal self-improving machine . arXiv preprint arXiv:2510.21614 . Cited by: §1 , §2 .

[28] Y. Wu, Y. Peng, Y. Chen, J. Ruan, Z. Zhuang, C. Yang, J. Zhang, M. Chen, Y. Tseng, Z. Yu, L. Chen, Y. Zhai, B. Liu, C. Wu, and Y. Luo (2026) AutoWebWorld: synthesizing infinite verifiable web environments via finite state machines . External Links: 2602.14296 , Link Cited by: §2 .

[29] P. Xia, J. Chen, H. Wang, J. Liu, K. Zeng, Y. Wang, S. Han, Y. Zhou, X. Zhao, H. Chen, et al. (2026) Skillrl: evolving agents via recursive skill-augmented reinforcement learning . arXiv preprint arXiv:2602.08234 . Cited by: §2 .

[30] J. Xiang, J. Zhang, Z. Yu, F. Teng, J. Tu, X. Liang, S. Hong, C. Wu, and Y. Luo (2025) Self-supervised prompt optimization . arXiv preprint arXiv:2502.06855 . Cited by: §2 , §5.1 .

[31] Y. Xiong, S. Hu, and J. Clune (2026) Learning to continually learn via meta-learning agentic memory designs . arXiv preprint arXiv:2602.07755 . Cited by: §2 .

[32] S. Xu, J. Zhang, S. Di, Y. Luo, L. Yao, H. Liu, J. Zhu, F. Liu, and M. Zhang (2025) Robustflow: towards robust agentic workflow generation . arXiv preprint arXiv:2509.21834 . Cited by: §2 .

[33] W. Xu, T. Mi, Y. Liu, Y. Nan, Z. Zhou, L. Ye, L. Zhang, Y. Qiao, and P. Liu (2026) ASI-evolve: ai accelerates ai . arXiv preprint arXiv:2603.29640 . Cited by: §2 .

[34] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. R. Narasimhan, and O. Press (2024) SWE-agent: agent-computer interfaces enable automated software engineering . In The Thirty-eighth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §4.1 .

[35] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao (2022) React: synergizing reasoning and acting in language models . arXiv preprint arXiv:2210.03629 . Cited by: Appendix B , §5.1 .

[36] H. Ye, H. Lin, J. Tang, Y. Luo, C. Yang, C. Su, R. Thapa, R. Yang, R. Liu, Z. Li, et al. (2026) Evaluation-driven scaling for scientific discovery . arXiv preprint arXiv:2604.19341 . Cited by: §1 , §2 .

[37] M. Yuksekgonul, F. Bianchi, J. Boen, S. Liu, Z. Huang, C. Guestrin, and J. Zou (2024) Textgrad: automatic" differentiation" via text . arXiv preprint arXiv:2406.07496 . Cited by: §2 .

[38] M. Yuksekgonul, D. Koceja, X. Li, F. Bianchi, J. McCaleb, X. Wang, J. Kautz, Y. Choi, J. Zou, C. Guestrin, et al. (2026) Learning to discover at test time . arXiv preprint arXiv:2601.16175 . Cited by: §1 , §2 .

[39] G. Zhang, H. Ren, C. Zhan, Z. Zhou, J. Wang, H. Zhu, W. Zhou, and S. Yan (2025) MemEvolve: meta-evolution of agent memory systems . arXiv preprint arXiv:2512.18746 . Cited by: §2 .

[40] J. Zhang, S. Hu, C. Lu, R. Lange, and J. Clune (2025) Darwin godel machine: open-ended evolution of self-improving agents . arXiv preprint arXiv:2505.22954 . Cited by: §2 , §5.1 .

[41] J. Zhang, B. Zhao, W. Yang, J. Foerster, J. Clune, M. Jiang, S. Devlin, and T. Shavrina (2026) Hyperagents . arXiv preprint arXiv:2603.19461 . Cited by: §1 , §1 , §2 , §5.1 .

[42] J. Zhang, J. Xiang, Z. Yu, F. Teng, X. Chen, J. Chen, M. Zhuge, X. Cheng, S. Hong, J. Wang, et al. (2024) Aflow: automating agentic workflow generation . arXiv preprint arXiv:2410.10762 . Cited by: §1 , §2 , §5.1 .

## Appendix A Ablation Study Details

## Appendix B Implementation Details

When temperature is exposed, we set it to 1; when reasoning-effort control is available, we use the high setting; and we use a maximum context budget of 128k tokens. We run 20 optimization rounds on Terminal-Bench and ARC-AGI-2. On open-ended optimization tasks, we allow up to 100 rounds and early-stop when a run reaches the known target score or fails to improve for 25 consecutive rounds. The initial procedure in the procedure-based setting uses best-valid-candidate selection plus a heuristic LLM optimizer; details are given in Appendix C.2.1 . The initial agent used on the standard agentic and reasoning tasks is a ReAct-style [ 35 ] agent; details are given in Appendix C.2.2 .

## Appendix C Additional Experimental Details

### C.1 Task and Metric Details

Our main experiments cover two standard benchmarks and three open-ended optimization tasks. Terminal-Bench evaluates end-to-end task completion in terminal environments, while ARC-AGI-2 measures abstract reasoning under fixed evaluation rules. The three open-ended tasks use hidden or fixed external evaluators and require the optimizer to improve executable code rather than only produce one-shot answers.

##### Circle Packing.

In circle_packing_26 , the goal is to pack 26 circles into a unit square and maximize the sum of their radii. The evaluator returns a validity bit and the achieved packing score. Higher is better.

##### Autocorrelation-Second.

In autocorrelation_second , the goal is to construct a non-negative function on [ − 1 / 4 , 1 / 4 ] [-\nicefrac{{1}}{{4}},\nicefrac{{1}}{{4}}] that maximizes R ⁡ ( f ) = ‖ f ∗ f ‖ 2 2 ‖ f ∗ f ‖ 1 ⋅ ‖ f ∗ f ‖ ∞ . R(f)=\frac{\|f*f\|_{2}^{2}}{\|f*f\|_{1}\cdot\|f*f\|_{\infty}}. The evaluator scores the submitted construction directly by this ratio. Higher is better.

##### Performance Engineering.

In the performance-engineering take-home, the goal is to optimize a kernel for a simulated VLIW SIMD machine while preserving correctness on the hidden tests. We report raw cycle count in the main table, so lower is better, although the evaluator also exposes a normalized score derived from the cycle count.

##### Reporting Protocol.

For Terminal-Bench and ARC-AGI-2, we report Avg@3 across three independent runs, together with the first optimization round that reaches the best score. For open-ended optimization, we report Best@3 across three runs under a fixed evaluation budget, together with the first round that reaches the best result and the average dollar cost per optimization round. Open-ended runs are capped at 100 rounds and are early-stopped if they reach the known target or plateau for 25 consecutive rounds.

##### Cost Computation.

For a run with R R optimization rounds, the average dollar cost per round is $ / R = 1 R ​ ∑ r = 1 R ( p in ​ n in ( r ) + p cache ​ n cache ( r ) + p out ​ n out ( r ) ) , \$/R=\frac{1}{R}\sum_{r=1}^{R}\left(p_{\mathrm{in}}n^{(r)}_{\mathrm{in}}+p_{\mathrm{cache}}n^{(r)}_{\mathrm{cache}}+p_{\mathrm{out}}n^{(r)}_{\mathrm{out}}\right), where n in ( r ) n^{(r)}_{\mathrm{in}} , n cache ( r ) n^{(r)}_{\mathrm{cache}} , and n out ( r ) n^{(r)}_{\mathrm{out}} denote the input, cached-input, and output token counts in round r r , and p in p_{\mathrm{in}} , p cache p_{\mathrm{cache}} , and p out p_{\mathrm{out}} are the corresponding provider prices.

### C.2 Initialization Details

#### C.2.1 Initial Procedure in Procedure-Based AEvo

The initial procedure used by procedure-based AEvo is intentionally minimal. It selects the current best valid candidate as the parent, applies a single LLM rewrite step, and then invokes the fixed evaluator. The excerpt below shows the corresponding editable surface.

⬇

This initialization exposes a limited search surface: it uses score-based selection, a single-parent rewrite step, and no richer failure analysis. This makes later meta-edits easier to interpret because they modify these exposed handles rather than the evaluator.

#### C.2.2 Initial Agent in Agentic and Reasoning Tasks

For Terminal-Bench and ARC-AGI-2, the initial agent is a minimal ReAct-style agent. The prompt surface and the ‘step()‘ loop are both editable, but the seed version contains only basic reasoning, short-horizon memory, and a strict JSON+‘bash‘ action protocol.

⬇

This weakly structured initialization makes subsequent improvements easier to attribute to changes in prompts, memory management, recovery logic, or context organization rather than to a highly engineered seed agent.

#### C.2.3 Meta-Agent Skill Excerpt

The meta-agent is governed by a compact operational skill that constrains how it reads the workspace, attributes failure, and chooses one causal intervention at a time. A representative excerpt is shown below.

⬇

The meta-agent therefore acts as a controller over future search rather than as an additional task-facing worker. The skill keeps that role boundary explicit.

### C.3 Representative Evolved Artifacts and Outcomes

#### C.3.1 Representative Evolved Procedures

The excerpt below is taken from a high-performing ARC-AGI-2 procedure. In later rounds, the evolved procedure forwards not only the current best artifact but also per-task slices from alternative references, enabling the optimizer to formulate a single causal hypothesis from those diagnostics.

⬇

⬇

This excerpt illustrates the main leverage of procedure-mode AEvo : evolution changes the evidence presented to the optimizer and the way that evidence is structured, not only the candidate artifact being scored.

#### C.3.2 Representative Evolved Agent Harness

In the agent-based setting, the evolved object is the harness seen by future inner-agent sessions rather than a single submitted artifact. In the performance-engineering run, this harness contained at least five durable layers: a task skill, a session-specific goal, a persistent family map, support utilities for evaluation accounting, and structured session notes written back into the workspace.

##### Task skill.

⬇

##### Session goal.

⬇

##### Persistent family map.

⬇

##### Replay utility.

⬇

##### Session memory written back by the inner agent.

⬇

Together, these excerpts show that the evolved agent harness is not a single prompt edit. It is a layered control structure consisting of persistent instructions, hypothesis-carrying goals, accumulated family-level memory, support code for evaluator interaction, and structured records that are promoted into future sessions.

#### C.3.3 Representative Optimization Outcomes

##### ARC-AGI-2 best artifact.

The best ARC-AGI-2 artifact in our run reaches accuracy 0.35 0.35 ( 7 / 20 7/20 ). Structurally, the final agent has three persistent components: a prompt surface that distinguishes normal feedback refinement from “fresh exploration,” a local Pass@K scorer over cached training pairs, and a validate-versus-submit controller that uses the best local score and plateau state.

⬇

⬇

##### Analysis.

The improvement over the seed agent comes from a tighter coupling between search control and task-local verification. First, caching the training pairs removes a brittle dependency on the observation format at later steps, so local verification remains available throughout the interaction. Second, Pass@K sampling with prompt diversification converts a single-sample ReAct loop into a small search procedure over candidate solvers, with selection driven by observed agreement on the training pairs rather than by the raw LLM output alone. Third, the separation between FEEDBACK_SUFFIX and FRESH_EXPLORE_SUFFIX makes the agent alternate explicitly between exploitation and hypothesis reset: partial but improving candidates are refined through concrete failure-conditioned feedback, whereas persistent plateaus trigger a prompt regime that suppresses anchoring to the current local optimum. Finally, the validate-versus-submit controller ties action choice to the best verified score rather than to the latest response, which reduces premature submission of partially correct programs.

##### Performance-engineering best artifact.

The best performance-engineering artifact is a two-file submission. The top-level program is only a wrapper; the schedule-level optimization resides in a benchmark-specialized base that exposes a small set of round-family control points. The final validated artifact reaches 1138 1138 cycles by combining evaluator-compatible packaging, explicit specialization of the benchmark rounds, and a non-uniform assignment of selector logic across engines.

##### Submitted wrapper.

⬇

##### Parameterized benchmark family.

⬇

##### Core benchmark schedule.

⬇

⬇

⬇

##### Analysis.

The low cycle count comes from three coupled changes. First, the file-local importlib wrapper is not cosmetic: without it, the evaluator rejects the whole family because sibling modules are not imported through the workspace package path. The wrapper therefore preserves a modular implementation while keeping the submission evaluator-compatible. Second, the benchmark-specialized base restructures the kernel around the exact round pattern of the benchmark rather than a generic loop. Its control flow is emitted as four specialized top-of-tree rounds, followed by seven gather rounds, followed by the same four specialized rounds and a final gather; this removes generic control overhead where the traversal repeatedly revisits the upper levels of the tree and makes the period- 11 11 reuse pattern directly schedulable. Within each specialized round, emit_hash is emitted phase-major across tiles, which exposes many independent chains to the scheduler and improves overlap between alu , valu , and memory operations. Third, the remaining gains come from engine balancing rather than from further structural refactoring. On this VLIW benchmark, flow has only one slot per cycle, so replacing a binary selector by multiply_add is profitable only when the induced valu pressure stays below the new bottleneck. The progression recorded in the run data is consistent with this view: the explicit-family port yields the dominant improvement ( − 597 -597 cycles), additional madd -based selectors at depth 1 and depth 3 save another 29 29 cycles, an alu -based parity/XOR rebalance saves 8 8 , and the final artifact gains the last 2 2 cycles by reverting only the second specialized depth-1 selector back to vselect . The best artifact is therefore not simply a shorter program; it is a schedule in which specialization, phase ordering, and per-round engine placement are co-tuned to the simulator’s slot limits.

Taken together, these artifacts illustrate two modes of durable improvement in AEvo : benchmark tasks improve through changes in how the optimizer reasons over failures, whereas open-ended optimization improves through the preservation and recombination of low-level implementation knowledge across many sessions.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
