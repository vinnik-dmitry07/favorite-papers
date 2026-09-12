##### Report GitHub Issue

Content selection saved. Describe the issue below:

\addtolist [1,2,5]Jeff Clune \authorformat \addtolist [4]New York University \affiliationformat

# HyperAgents

###### Abstract

Self-improving AI systems aim to reduce reliance on human engineering by learning to improve their own learning and problem-solving processes. Existing approaches to recursive self-improvement typically rely on fixed, handcrafted meta-level mechanisms, which fundamentally limit how fast such systems can improve. The Darwin Gödel Machine (DGM) ( Zhang et al., 2025b ) demonstrates that open-ended self-improvement is achievable in coding. Starting from a single coding agent, the DGM repeatedly generates and evaluates self-modified variants, forming a growing archive of stepping stones for future improvement. Because both evaluation and self-modification are coding tasks, gains in coding ability can translate into gains in self-improvement ability. However, this alignment does not generally hold beyond coding domains. We introduce hyperagents , self-referential agents that integrate a task agent (which solves the target task) and a meta agent (which modifies itself and the task agent) into a single editable program. Crucially, the meta-level modification procedure is itself editable, enabling metacognitive self-modification, improving not only task-solving behavior, but also the mechanism that generates future improvements. We instantiate this framework by extending DGM to create DGM-Hyperagents (DGM-H). By allowing the improvement procedure to evolve, the DGM-H eliminates the assumption of domain-specific alignment between task performance and self-modification skill, and can potentially support self-accelerating progress on any computable task. Across diverse domains (coding, paper review, robotics reward design, and Olympiad-level math-solution grading), the DGM-H improves performance over time and outperforms baselines without self-improvement or open-ended exploration, as well as prior self-improving systems like DGM. We further show that the DGM-H improves the process by which it generates new agents (e.g., persistent memory, performance tracking), and that these meta-level improvements transfer across domains and accumulate across runs. All experiments were conducted with safety precautions (e.g., sandboxing, human oversight). We discuss what safety entails in this setting and the broader implications of self-improving systems. DGM-Hyperagents offer a glimpse of open-ended AI systems that do not merely search for better solutions, but continually improve their search for how to improve.

## 1 Introduction

With appropriate safety considerations, AI systems that can improve themselves could transform scientific progress from a human-paced process into an autonomously accelerating one, thereby allowing society to realize the benefits of technological advances much earlier. Such self-improving AI seeks to continually improve its own learning and task-solving abilities. However, most existing self-improvement architectures rely on a fixed meta agent (i.e., a higher-level system that modifies a base system). This creates a limitation since the base system can only be improved within the boundaries defined by the meta agent’s design. Adding a meta-meta system to improve the meta agent does not solve this problem, it merely shifts the issue upward and ultimately leads to an infinite regress of meta-levels. To overcome this limitation and allow a system to modify any part of itself without being constrained by its initial implementation, the system must be self-referential, that is, able to analyze, modify, and evaluate itself ( Kirsch and Schmidhuber, 2022 ; Zhang et al., 2025b ) . When the mechanism of improvement is itself subject to improvement, progress can become self-accelerating and potentially unbounded ( Lu et al., 2023 ) .

The Darwin Gödel Machine (DGM) ( Zhang et al., 2025b ) demonstrates that open-ended self-improvement is achievable in coding. In the DGM, agents generate and evaluate modifications to their own code, and successful variants are retained in an archive as stepping stones for further improvement. However, the DGM relies on a handcrafted, fixed mechanism to produce self-improvement instructions ( Appendix B ). This mechanism analyzes past evaluation results and the agent’s current codebase to generate an instruction directing where the agent should self-improve. This mechanism is not modifiable. Hence, the DGM’s capacity for self-improvement is bottlenecked by this fixed instruction-generation step. Despite this handcrafted step, the DGM can still improve at self-improving. Because both evaluation and self-modification are coding tasks, improvements in evaluation performance directly reflects the agent’s capacity to generate effective self-modifications. To improve at self-improving, the DGM relies on a limiting assumption: that the skills required to solve the evaluation tasks are the same as those required for effective self-reflection and self-modification. This assumption is unlikely to hold outside coding domains, where task-solving skills may differ substantially from the skills needed to analyze failures, propose effective self-improvements, and implement them.

This work introduces hyperagents , self-referential agents that can in principle self-improve for any computable task. Here, an agent is any computable program, optionally including calls to foundation models (FMs), external tools, or learned components. A task agent solves a given task. A meta agent modifies agents and generates new ones. A hyperagent combines the task agent and the meta agent into a single self-referential, modifiable program, such that the mechanism responsible for generating improvements is itself subject to modification. As a result, a hyperagent can improve not only how it solves tasks (i.e., the task agent), but also how it generates and applies future modifications (i.e., the meta agent). Because its self-improvement mechanism is itself modifiable, we call this metacognitive self-modification . We extend the DGM with hyperagents, creating DGM-Hyperagents (DGM-H). The DGM-H retains the open-ended exploration structure of the DGM and extends the DGM with metacognitive self-modification. As with DGM, to support sustained progress and avoid premature convergence, the DGM-H grows an archive of hyperagents by branching from selected candidates, allowing them to self-modify, evaluating the resulting hyperagents, and adding them back to the archive. Because a hyperagent can modify its self-modification process, the DGM-H is not constrained by its initial implementation and can potentially self-improve for any computable task.

Across our experiments, the DGM-H demonstrates substantial and generalizable improvements in both task performance and self-improvement ability. On the Polyglot coding benchmark ( Gauthier, 2024 ) , the DGM-H achieves gains comparable to the most established prior self-improving algorithm ( Zhang et al., 2025b , the Darwin Gödel Machine,) , despite not being handcrafted for coding. Beyond coding, the DGM-H substantially improves performance on paper review ( Zhao et al., 2026 ) and robotics reward design ( Genesis, 2024 ) , with gains transferring to held-out test tasks and significantly outperforming prior self-improving algorithms, which struggle outside coding unless customized. Ablations without self-improvement or without open-ended exploration show little to no progress, highlighting the necessity of each component ( Section 5.1 ). Crucially, the DGM-H learns transferable mechanisms on how to self-improve (e.g., persistent memory, performance tracking) that systematically improve its ability to generate better task or meta agents over time. As a result, meta-level improvements learned by the DGM-H transfer across domains. Specifically, hyperagents optimized in one setting (i.e., paper review and robotics tasks) remain significantly effective at generating improved task agents in a different domain (i.e., Olympiad-level math grading) ( Section 5.2 ). We further show that self-improvements learned by the DGM-H in one setting can compound with continued self-improvement in another setting ( Section 5.3 ). This suggests that, given appropriate tasks, the DGM-H has the potential to achieve unbounded open-ended self-improvement over time. We discuss the safety implications of such open-ended self-improving systems and outline practical considerations for responsible deployment in Section 6 . Overall, hyperagents open up the possibility of improving their ability to improve while improving their ability to perform any computable task.

## 2 Related Work

Open-Endedness. Open-endedness refers to the ability of a system to continually invent new, interesting, and increasingly complex artifacts, extending its own frontier of discovery without a fixed objective or predefined end ( Stanley et al., 2017 ; Hughes et al., 2024 ) . Recent work has leveraged FMs as proxies for human interestingness and as versatile engines for generating and evaluating novel behaviors across diverse domains ( Zhang et al., 2024 ; Faldor et al., 2025 ) . Building on these advances, recent progress in open-ended learning ( Hu et al., 2025 ; Zoph and Le, 2017 ; Colas et al., 2023 ; Lehman et al., 2023 ) and quality-diversity algorithms ( Lehman and Stanley, 2011 ; Mouret and Clune, 2015 ; Bradley et al., 2023 ; Samvelyan et al., 2024 ; Ding et al., 2024 ; Pourcel et al., 2023 ; Coiffard et al., 2025 ; Dharna et al., 2025 ; Yuan et al., 2026 ) has shown that sustained exploration can produce diverse and increasingly capable artifacts across domains ranging from game-playing agents ( Klissarov et al., 2023 ; Klissarov et al., 2025 ; Wang et al., 2024 ) to scientific discovery ( Lu et al., 2024a ; Lu et al., 2024b ; Romera-Paredes et al., 2024 ; Novikov et al., 2025 ; Audran-Reiss et al., 2025 ) and robotic control ( Cully et al., 2015 ; Li et al., 2024 ; Grillotti et al., 2025 ) . Recent progress has shown that open-ended AI systems capable of continuously generating diverse and increasingly complex artifacts are possible ( Zhang et al., 2024 ; Faldor et al., 2025 ; Hu et al., 2025 ) . An important next step is to explore how such systems can achieve compounding improvement. In human scientific and technological progress, advances often build on prior advances not only by producing better artifacts, but also by improving the tools and processes that generate future discoveries, leading to accelerating innovation ( Good, 1966 ; Kwa et al., 2025 ) . Inspired by this pattern, we focus on open-ended systems that can improve not only the artifacts they generate, but also the mechanisms by which novelty and progress are produced ( Clune, 2019 ; Jiang et al., 2023 ) .

Self-improving AI. Early theoretical work on self-improving AI dates back to formal models of self-modifying agents ( Hutter, 2003 ) . One prominent example is the Gödel Machine ( Schmidhuber, 2003 ) , which proposes agents that rewrite themselves when provably beneficial, though such approaches remain impractical in real-world settings. Subsequent research explored self-improvement through adaptive neural systems, in which agents modify their own weights or learning dynamics via meta-learning ( Schmidhuber, 1993 ; Miconi et al., 2018 ; Javed and White, 2019 ; Beaulieu et al., 2020 ; Miconi et al., 2020 ; Irie et al., 2022 ; Chalvidal et al., 2022 ; Oh et al., 2025 ) , evolution ( Stanley and Miikkulainen, 2002 ; Lange et al., 2023 ; Qiu et al., 2025 ; Zhao et al., 2025 ) , or self-play ( Silver et al., 2016 ; Silver et al., 2017 ; Xia et al., 2025b ; Xia et al., 2026 ) . Notably, Silver et al. (2017) use self-play to iteratively improve neural network agents, achieving superhuman performance in domains such as Go and chess, although the underlying learning algorithms themselves remain fixed and human-designed. More recently, FMs have enabled self-improvement through iterative refinement of prompts ( Fernando et al., 2023 ; Wang et al., 2025a ; Zhang et al., 2025c ; Zhang et al., 2025a ; Ye et al., 2026 ) , reasoning traces ( Zelikman et al., 2022 ; Yin et al., 2025 ; Havrilla et al., 2024 ; Zhuge et al., 2024 ) , and entire code repositories ( Zhang et al., 2025b ; Wang et al., 2025b ; Xia et al., 2025a ) , as well as through systems that update model weights using self-generated data or interaction ( Wu et al., 2024 ; Zweiger et al., 2025 ; Wen et al., 2025 ; Wei et al., 2025b ) . Among these, the Darwin Gödel Machine (DGM) ( Zhang et al., 2025b ) stands out as a practical instantiation of recursive self-improvement in coding domains. However, despite their effectiveness, most existing approaches (including the DGM and its derivatives) rely on fixed, handcrafted meta-level mechanisms ( Appendix B ) that constrain how self-improvement can compound over time and generalize across domains.

Self-referential Meta-learning. Self-referential meta-learning studies systems that learn to improve the mechanisms by which learning occurs. Prior work has explored this idea in neural networks ( Kirsch and Schmidhuber, 2022 ; Jackson et al., 2024 ) and evolutionary methods ( Lu et al., 2023 ) . More recently, several works have explored self-referential improvement using FM-based agents ( Zelikman et al., 2024 ; Robeyns et al., 2025 ; Yin et al., 2025 ; Zhang et al., 2025b ) . The Darwin Gödel Machine (DGM) ( Zhang et al., 2025b ) and its successors ( Wang et al., 2025b ; Xia et al., 2025a ; Weng et al., 2026 ) instantiate recursive self-improvement through self-modification, primarily in coding domains. However, these approaches improve at improving primarily within coding tasks only. In the DGM and related systems, a coding agent is tasked with improving itself, and the resulting improved coding agent is then used in subsequent self-improvement steps to generate an even better version of itself. Because both the evaluation task and the self-modification process involve coding, improving the coding agent also enhances the system’s ability to carry out future self-improvements. However, this property only holds when the evaluation task and the self-modification task are closely aligned. For example, if the evaluation task were instead poetry writing, improving an agent’s poetry-writing ability would not necessarily improve its ability to modify its own code. Prior work therefore relies on an alignment between the evaluation task and the skills required for self-improvement. In contrast, hyperagents do not assume such alignment, because the self-modification mechanism is fully modifiable and not tied to any particular task domain. Hence, hyperagents can improve both task performance and the process of improvement itself across any computable task.

## 3 Methods

We introduce hyperagents, self-referential agents that unify task execution and agent generation into a single modifiable program. A hyperagent can improve not only how it solves tasks but also how it generates future improvements. To enable sustained and accumulating progress, we instantiate hyperagents by building directly on the Darwin Gödel Machine (DGM) to form DGM-Hyperagents (DGM-H). The DGM provides an open-ended, population-based exploration process that maintains an archive of progressively improving agents, allowing successful variants to serve as stepping stones for future gains. DGM-H retains this open-ended evolutionary structure and extends it by making the entire meta-level modification mechanism editable ( Figure 1 ). By allowing agents to modify not only how they solve tasks but also how they improve themselves, the DGM-H has the potential to open-endedly self-improve on any computable task.

Agents. This paper defines an agent as any computable program, optionally including calls to FMs, external tools, or learned components. Agents are not restricted to a particular representation (e.g., neural networks or prompts) and may include arbitrary algorithmic logic, memory, and control flow. A task agent is an agent instantiated to solve a set of tasks. Examples include generating code edits for a software repository ( Gauthier, 2024 ; Jimenez et al., 2024 ) , predicting acceptance decisions for research papers ( Couto et al., 2024 ) , and designing reward functions for robotics environments ( Ma et al., 2024 ) . Task agents are evaluated empirically on the given task. A meta agent is an agent whose only task is to modify existing agents and generate new ones. Given access to the entire archive of previous agents and evaluations, a meta agent proposes changes intended to improve future performance (including potentially many generations later). Importantly, these changes may target not only task-solving logic but also the meta agent itself, enabling improvements to the procedures by which future modifications are generated.

Hyperagents. A hyperagent is a self-referential agent that integrates a task agent and a meta agent within a single editable program, enabling it to modify not only how it performs tasks but also how it generates future self-modifications. Unlike hierarchical systems with fixed meta-levels, in hyperagents the meta agent is part of the same editable program and can rewrite itself. As a result, a hyperagent can improve both (1) how it solves tasks and (2) how it generates future self-improvements. We use Python, which is Turing-complete ( Turing and others, 1936 ) , and since a hyperagent can edit any code, it has the potential to build any computable machine.

Metacognitive self-modification. In hyperagents, the agent’s self-improvement mechanism is itself subject to modification. In addition to improving its performance on a given task, the agent can simultaneously modify the procedures by which it proposes and applies further self-improvements. We refer to this process as metacognitive self-modification , in which the hyperagent improves not only the task-performing agent responsible for solving the given task, but also the meta agent that determines how subsequent hyperagents are generated. This characteristic addresses a central limitation of prior self-improving systems ( Zhang et al., 2025b ; Wang et al., 2025b ) by directly enabling improvements to the self-improvement process itself ( Section 2 ). Examples of such metacognitive self-modifications are presented in Section 5.2 and Section E.3 .

Darwin Gödel Machine with Hyperagents. Augmenting the original DGM ( Zhang et al., 2025b ) with hyperagents, we create DGM-Hyperagents (DGM-H). DGM-H employs the open-ended exploration process in the DGM to mitigate premature convergence and avoid getting trapped in local optima. This process maintains an archive of generated hyperagents, initialized with a single hyperagent and expanded over time by continuously accumulating generated variants. The process alternates between two phases: metacognitive self-modification and evaluation. During the metacognitive self-modification phase, selected parent hyperagents from the archive generate modified versions of themselves. Parent selection is probabilistic and proportional to a hyperagent’s performance, and inversely proportional to the number of children that successfully compiled, biasing sampling toward hyperagents that perform well and generate strong descendants while preserving exploration ( Section A.2 ). During the evaluation phase, each modified hyperagent is empirically evaluated and subsequently added to the archive. In principle, a fully self-referential algorithm should allow modification of every part of itself (including the parent selection and evaluation mechanisms). While we present preliminary results exploring the possibility of automatically improving the parent selection mechanism in Section E.5 , the experiments in the main text use a handcrafted parent selection mechanism that is not subject to modification in order to isolate the effects of hyperagent self-modification. Overall, DGM-H consists of two interacting components: (1) an open-ended exploration process inherited from the DGM, and (2) an initial hyperagent, which evolves over time through self-generated variants ( Figure 1 , Appendix A ). By extending the DGM to make the meta-level mechanism itself modifiable, the DGM-H generalizes recursive self-improvement beyond coding and enables self-referential improvement for any computable task.

## 4 Experiment Setup

The DGM-H is initialized with a single hyperagent built around a frozen FM ( Brown et al., 2020 ) with external tool-use capabilities ( Schick et al., 2023 ) . The FM autonomously invokes tools as needed at each step. This initial hyperagent is equipped with two tools: a bash tool for executing shell commands, and a specialized tool for inspecting and modifying files. In the initial hyperagent, the task agent receives the task inputs and outputs the response from a single FM call. The meta agent receives the location of the agent’s repository, the location of previous evaluation results, and the number of remaining experiment iterations (the experiment budget is a hyperparameter), and is tasked with modifying any part of the given codebase ( Section A.1 ). We deliberately keep the implementation of the initial hyperagent (i.e., both the task agent and the meta agent) simple, allowing for a broad search space and avoiding prematurely constraining the range of possible improvements. Section D.1 details the FMs and the hyperparameters used in each experiment, while Section D.2 reports the corresponding cost estimates.

### 4.1 Baselines

We compare the Darwin Gödel Machine with Hyperagents ( DGM-H ) against a set of baselines designed to isolate the contributions of self-improving meta agents, open-ended exploration, and metacognitive self-modification (i.e., hyperagents) ( Appendix B ). DGM-H without self-improving meta agents ( DGM-H w/o self-improve ) fixes the meta agent modifying other hyperagents to the initial meta agent for the entire run. While the system can still generate and evaluate new hyperagents, the procedures used to propose and apply modifications are not themselves modifiable. This baseline replicates the approach of ( Hu et al., 2025 , ADAS,) in this setting. It tests whether performance gains arise solely from task-level optimization under a fixed meta-level mechanism, or from improvements in the self-improvement process itself. DGM-H without open-ended exploration ( DGM-H w/o open-ended exploration ) removes the archive of previously generated hyperagents. Instead of retaining previous variants as stepping stones for future exploration, each newly generated hyperagent replaces its predecessor. After generating a new hyperagent, it is evaluated and automatically becomes the next selected parent. This baseline isolates the role of open-ended, population-based search. Comparing against this baseline tests whether sustained improvement requires accumulating and reusing diverse intermediate solutions.

We also compare against the original implementation of the Darwin Gödel Machine ( DGM ) ( Zhang et al., 2025b ) . The DGM relies on a handcrafted, fixed mechanism to generate self-improvement instructions. Because this instruction-generation mechanism is designed specifically for coding benchmarks and is not modifiable, the DGM’s self-improvement capacity in other domains is limited ( Section 2 ). To provide a stronger comparison, we manually customize the DGM’s instruction-generation mechanism for the target domains ( DGM-custom ) ( Appendix B ). This baseline measures how much the DGM relies on human engineering to remain competitive across domains. Comparing the DGM-H against this baseline tests whether automated metacognitive self-modification can outperform human-designed self-improvement mechanisms. Additionally, we compare against static solutions that have been handcrafted for each domain in prior work.

### 4.2 Domains

We evaluate our method and baselines across diverse domains (i.e., coding, paper review, robotics reward design, and Olympiad-level math grading) ( Appendix C ). To reduce computational cost, for each domain we first evaluate agents on a small subset of the training tasks to estimate overall effectiveness. Only agents that demonstrate sufficient performance are subsequently evaluated on the remaining training tasks. Agents that do not are treated as having zero performance on unevaluated tasks. Domain-specific evaluation protocols are described in detail in the subsequent paragraphs. For domains where we create AI judges to reflect human data (i.e., paper review and Olympiad-level math grading), we construct a validation subset because the AI judges are more likely to overfit to the training data. When a validation subset is defined for a domain, the performance component used in parent selection is measured on the validation set. Otherwise, it is measured on the training set. Each domain includes separate held-out test tasks that are used only for final evaluation.

Coding. We choose Polyglot ( Gauthier, 2024 ) as a computationally cost-efficient coding benchmark for direct comparison with prior work ( Zhang et al., 2025b ) . In this benchmark, the agent is given a code repository and a natural language instruction describing a desired change, and must modify the repository accordingly. We follow the experimental setup used in the DGM ( Zhang et al., 2025b ) , including the same training and test splits, no validation set, and the same staged evaluation protocol (i.e., first evaluating each agent on 10 tasks to estimate effectiveness before expanding to 50 additional tasks) ( Section C.1 ).

Paper review. This domain evaluates agents on a simulated conference peer review task. For each task, the agent is given the full text of an AI research paper and must predict a binary accept/reject decision. We include paper review to evaluate the DGM-H in a hard-to-verify setting where there is no objective ground truth. Peer review is subjective, and reviewer decisions can vary due to differing priorities and perspectives. We do not aim to change the peer review system, but rather, we study whether hyperagents can automatically learn decision procedures that align with observed human judgments. The agent outputs a single acceptance decision, and performance is measured by comparing predictions against observed acceptance outcomes. The dataset is drawn from Zhao et al. (2026) , which constructs a large-scale benchmark from publicly available submissions and acceptance decisions from recent top-tier machine learning conferences. The representative static baseline for this domain is the reviewer agent from the AI-Scientist-v2 ( Yamada et al., 2025 ) . Section C.2 provides full details on the dataset splits (train, validation, and test), the staged evaluation protocol (i.e., first evaluating each agent on a 10-task subset to estimate effectiveness before expanding evaluation to a total of 100 tasks), and the representative baselines for this domain.

Robotics reward design. This domain evaluates an agent’s ability to design reward functions for robotic tasks. We include this domain to move beyond language-only tasks and show that hyperagents can leverage external simulators (e.g., physics engines) and training algorithms (e.g., reinforcement learning (RL)) to produce effective solutions. Given a natural language description of a robotics task, an agent must generate a suitable reward function. This reward function is then used to train a quadruped robot in simulation using RL ( Genesis, 2024 ) . The quality of the agent’s solution is measured by the performance of the resulting policy: after training with the generated reward function, we evaluate how well the robot achieves the desired behavior ( Ma et al., 2024 ) . We use separate training and test tasks. During training, agents are required to generate reward functions that enable the robot to walk forward. For held-out testing, agents must zero-shot generate new reward functions that maximize the robot’s torso height. Because reward functions that successfully enable a robot to walk forward do not induce jumping behaviors (the more optimal behavior for maximizing the robot’s torso height), this setup evaluates whether a single agent can design suitable reward functions for different robotics tasks. This domain does not have a separate validation task. Section C.3 provides full details on the staged evaluation protocol (i.e., first evaluating each agent on 3 repetitions of the training task to estimate effectiveness before expanding evaluation to a total of 6 repetitions), and the representative baselines for this domain.

Olympiad-level math grading. This domain evaluates an agent’s ability to grade solutions to Olympiad-level math problems. This domain is reserved as a held-out meta-evaluation to test whether DGM-H’s improvements to its self-improvement process transfer across domains and continue to compound over time. We use IMO-GradingBench ( Luong et al., 2025 ) , which consists of International Mathematical Olympiad (IMO)-level problems paired with candidate solutions and expert human grades. For each task, the agent is given an IMO-level problem, a candidate solution, reference solutions, and grading guidelines to predict a discrete score. Performance is measured by the accuracy of the agent’s grades with respect to expert human grades. The representative static baseline for this domain is the ProofAutoGrader from IMO-GradingBench. Section C.4 provides full details on the score labels, dataset splits (train, validation, and test), the staged evaluation protocol (i.e., first evaluating the agent on a 10-task subset to estimate effectiveness before expanding evaluation to a total of 100 tasks), and the baselines for this domain.

## 5 Results

For each experiment, we run each method 5 times. We report medians with 95% bootstrap confidence intervals computed from 1,000 resamples, using the notation median (CI: lower – upper ). In line plots, lines show median performance and shaded regions indicate the confidence intervals ( Figures 2 , 3 and 4 ). Bar plots report median performance on held-out test sets, with error bars indicating confidence intervals ( Figures 2 , 3 and 4 ). Statistical significance is assessed using the Wilcoxon signed-rank test. Overall, the DGM-H exhibits general self-improvement at both the task and meta levels. Improvements to the task agent transfer to held-out test tasks within each domain, exceeding open-sourced static baselines ( Section 5.1 ). Meta-level improvements transfer across domains, enabling hyperagents to significantly improve their ability to generate better task agents in previously unseen domains ( Section 5.2 ). Self-improvements learned in one DGM-H run can potentially accelerate learning in subsequent runs and continue to compound as further self-modifications are applied ( Section 5.3 ). All experiment logs are open-sourced in our codebase.

### 5.1 Improving Task Performance

The DGM-H can achieve self-improvement in coding comparable to prior self-improving algorithms. On the Polyglot coding benchmark, we use the same experimental settings as in the DGM (e.g., identical FM parameters, same number of 80 iterations) to enable a direct comparison. Across 5 runs, the DGM-H improves its training performance on the 50-task Polyglot subset from 0.140 (the initial agent) to 0.340 (CI: 0.300 – 0.380). When evaluated on the full Polyglot benchmark, which consists largely of tasks unseen during training, performance increases from 0.084 (the initial agent) to 0.267 (CI: 0.231 – 0.280). These improvements are comparable to those reported for the original DGM, which improves from 0.140 to 0.380 on the training subset and from 0.142 to 0.307 on the full benchmark ( Zhang et al., 2025b ) . Overall, these results show that the DGM-H can effectively self-improve in the coding domain and achieve a similar level of improvement to the original DGM, despite not being handcrafted specifically for coding tasks.

Beyond coding, we evaluate the DGM-H on paper review and robotics reward design to assess its ability to self-improve across diverse tasks within a single run ( Section A.4 ). If an agent fails the staged evaluation in any domain, it is not evaluated on the full training set for any domain, and a score of zero is assigned for all remaining tasks. For example, when jointly optimizing the paper review and robotics reward design domains within the same experiment run, failure in the staged evaluation of either domain (e.g., correctly predicting none of the paper reviews in a smaller training subset, or failing to generate any compilable reward function) results in the agent not being evaluated on the full training set for either domain. Only the best agents, selected via validation scores (or training scores when validation tasks do not exist), are evaluated on the test set. All runs start from the same initial agent, which directly outputs the response from a single FM call ( Section A.1 ). This initial agent achieves a test-set score of 0.0 on paper review and 0.060 on robotics reward design ( Figure 2 ). In paper review, the initial agent fails to produce outputs in the required format because no task-specific parsing or post-processing is provided, resulting in a score of 0.0. In robotics reward design, the initial agent typically generates reward functions that either fail to compile (e.g., due to invalid environment variables) or do not yield effective policies. However, the initial agent occasionally produces a minimally functional reward, leading to a small but non-zero average score. Starting from this initial agent, each method is run for 100 iterations.

The original DGM requires domain-specific customization to generalize beyond coding. When applied in the form designed specifically to optimize coding agents, the original DGM achieves test-set performance of 0.0 (CI: 0.0 – 0.510) on paper review and 0.0 (CI: 0.0 – 0.090) on robotics reward design. This outcome is expected, as the original DGM’s instruction-generation mechanism is explicitly tailored to coding tasks and to improving coding agents ( Appendix B ). However, when manually customized for each new domain, DGM-custom achieves substantially stronger results: 0.590 (CI: 0.570 – 0.650) on paper review and 0.348 (CI: 0.305 – 0.385) on robotics reward design. DGM-custom significantly outperforms the original DGM in both domains (p ¡ 0.05) ( Figure 2 ). These results highlight both the strength of the DGM within its intended domain and the importance of domain-specific manual customization for extending its self-improvement capabilities beyond coding in its original implementation.

Metacognitive self-modification enables sustained task improvement across domains. The DGM-H substantially improves task performance over time in both domains, demonstrating effective improvement of the task agent. Importantly, these gains transfer to held-out test sets, indicating that improvements reflect general competence rather than overfitting to training tasks. On test tasks, DGM-H improves paper review performance from 0.0 (the initial agent) to 0.710 (CI: 0.590 – 0.750) ( Section E.1.1 ). Several top-performing agents outperform the open-sourced static baseline, which achieves 0.630 ( Yamada et al., 2025 ) . On robotics reward design, DGM-H improves performance from 0.060 (the initial agent) to 0.372 (CI: 0.355 – 0.436) ( Section E.1.2 ), surpassing the default reward function that directly optimizes the evaluation metric (0.348).

Qualitatively, the DGM-H improves task agents by moving beyond surface-level prompt tweaks toward structured, reusable decision machinery. In paper review, it shifts from superficial behavioral instructions (e.g., adopting a “rigorous” persona) to explicit multi-stage evaluation pipelines with checklists, decision rules, and clearly defined criteria, resulting in more consistent and higher-quality judgments ( Section E.2 ). In robotics reward design, the DGM-H incrementally builds and refines an internal knowledge base of environment constraints, valid state variables, and reward-scaling heuristics, eliminating compilation failures and reducing reward misspecification. The DGM-H accumulates and refines domain knowledge (e.g., environment documentation, grading criteria) and integrates it into increasingly sophisticated decision frameworks, enabling complex, consistent task behavior without manual, domain-specific engineering ( Section E.2 ).

The DGM-H significantly outperforms the original DGM in both domains (p ¡ 0.05), reflecting the limitations of the original DGM’s fixed instruction-generation mechanism when applied to non-coding tasks ( Figure 2 ). The DGM-H achieves higher median performance than DGM-custom on the test tasks in both domains, although the difference is not statistically significant (p ¿ 0.05) ( Figure 2 ). Notably, in the robotics reward design test task (i.e., design a reward function that trains the robot to maximize its torso height), the DGM-H almost always generates task agents that design reward functions inducing jumping behaviors, rather than getting stuck in the local optimum of standing tall. In contrast, DGM-custom often generates task agents that fail to escape this local optimum. This qualitative difference suggests that metacognitive self-modification can match or exceed handcrafted, domain-specific mechanisms.

Both metacognitive self-modification and open-ended exploration are necessary for sustained improvement. DGM-H w/o self-improve ( Hu et al., 2025 ) shows little to no improvement, achieving test-set performance of 0.0 (CI: 0.0 – 0.130) on paper review and 0.213 (CI: 0.180 – 0.348) on robotics reward design. The DGM-H significantly outperforms this baseline in both domains (p ¡ 0.05) ( Figure 2 ), demonstrating that the observed gains in the DGM-H are not solely due to task-level optimization under a fixed meta agent, but also arise from improvements in the self-modification process itself (i.e., the meta agent). Similarly, DGM-H w/o open-ended exploration fails to achieve meaningful improvement, with test-set performance remaining at 0.0 (CI: 0.0 – 0.560) on paper review and 0.116 (CI: 0.0 – 0.348) on robotics reward design. The DGM-H significantly outperforms this baseline in both domains (p ¡ 0.05) ( Figure 2 ), highlighting the importance of open-ended, population-based search to create stepping stones for future improvements.

### 5.2 Improving the Ability to Improve

DGM-H’s superior performance to DGM-H w/o self-improve shows that DGM-H improves the meta agent (i.e., its ability to self-modify and generate new agents) ( Section 5.1 ). This section investigates whether these meta-level improvements are general rather than domain-specific. Specifically, we evaluate whether self-improvement strategies learned in one setting transfer to and accelerate learning in a different domain.

Improvement@k metric. To quantify a meta agent’s ability to generate improved task agents, we introduce the improvement@k (imp@k) metric. Given an initial meta agent M M , an initial task agent A A , an agent-generation algorithm (e.g., DGM or DGM-H variants), and a fixed task, M M is allowed to generate up to k k new task agents from A A and its descendants using the specified algorithm. We define imp@k as the improvement in test performance from the initial task agent A A to the best-performing generated task agent (selected based on validation score) ( Section D.3 ). Intuitively, imp@k measures how effectively a meta agent can produce improved variants within a limited number of iterations. To isolate the meta agent’s ability to improve task agents from its ability to improve itself, we hold the meta agent fixed throughout the process (i.e., the agent responsible for generating new task agents is always the initial meta agent M M ), yielding DGM w/o self-improve and DGM-H w/o self-improve as the agent-generation algorithms. All experiments in this section run for 50 iterations, measuring imp@50.

The initial meta agent has little to no ability to generate improved task agents. Taking the same initial meta and task agents as in the above experiments ( Section 4 ), we evaluate the initial meta agent’s ability to generate improved task agents on Olympiad-level math grading. The initial task agent achieves a test-set score of 0.0, as it fails to produce outputs in the required format due to the lack of task-specific parsing or post-processing. After 50 iterations of DGM w/o self-improve, during which the initial meta agent is held fixed and used to generate new task agents starting from a initial task agent, the best generated task agents (across 5 repeated runs) achieve a median test score of 0.0 (CI: 0.0 – 0.0). Accordingly, imp@50 for the initial meta agent under DGM w/o self-improve is 0.0 (CI: 0.0 – 0.0) on Olympiad-level math grading. While DGM w/o self-improve relies on a fixed handcrafted instruction-generation mechanism, DGM-H w/o self-improve does not. DGM w/o self-improve uses a handcrafted instruction-generation mechanism to specify which parts of the agent’s codebase should be modified, whereas DGM-H w/o self-improve allows the meta agent to autonomously decide which parts of the codebase to modify. After 50 iterations of DGM-H w/o self-improve, again holding the initial meta agent fixed and generating task agents from the same initial task agent, the best generated task agents (across 5 repeated runs) achieve a median score of 0.0 (CI: 0.0 – 0.130). Accordingly, imp@50 for the initial meta agent under DGM-H w/o self-improve is 0.0 (CI: 0.0 – 0.130) ( Figure 3 ). These results show that, on Olympiad-level math grading, the initial meta agent has little to no ability to generate improved task agents, regardless of the agent-generation algorithm used (e.g., DGM or DGM-H).

Meta agents optimized in prior DGM-custom runs have little to no ability to generate improved task agents when transferred to a new domain. We evaluate whether self-improvements learned in one setting using the DGM can transfer to new domains. We consider agents optimized in prior DGM-custom runs on the paper review and robotics reward design tasks ( Section 5.1 ). From each run, we select a transfer agent based on the maximum performance gain achieved by its descendants, measured relative to the agent itself and discounted by lineage depth ( Section D.4 ). We apply discounting to favor agents that reliably produce strong improvements within fewer self-modification steps, since improvements occurring many iterations later are less directly attributable to the original agent. We choose transfer agents from DGM-custom rather than from DGM because DGM-custom achieved larger improvements in the previous settings ( Section 5.1 ). For transfer, we carry over the entire agent implementation from the source domain, including both the meta agent and the task agent. Concretely, the transfer meta agent is used as the fixed agent responsible for generating new task agents in the target domain, and the transfer task agent serves as the initial task agent from which new variants are generated. We evaluate whether the transfer meta agents can generate improved task agents in a new domain, Olympiad-level math grading. The transfer task agents (one from each of 5 repeated runs) achieve a test-set score of 0.0 (CI: 0.0 – 0.010). As expected, this performance is low because the agents were optimized for paper review and robotics reward design, which differ substantially from the math grading task. After 50 iterations of DGM w/o self-improve starting from each transfer task agent and holding the transfer meta agent fixed, the best generated task agents (selected based on validation score) achieve a score of 0.0 (CI: 0.0 – 0.020). This corresponds to a imp@50 of 0.0 (CI: 0.0 – 0.010) ( Figure 3 ), showing that the transfer meta agents from DGM-custom runs cannot generate improved task agents in a previously unseen domain. When using DGM w/o self-improve as the agent-generation algorithm, imp@50 for the transfer agents is similar to that of the initial agent (both close to zero). This shows that the task performance improvements observed with DGM-custom rely on domain-specific customizations, rather than on general improvements in the meta ability to generate improved task agents.

Hyperagents optimized in prior DGM-H runs demonstrate transferable ability to generate improved task agents in a new domain. We repeat the transfer experiments for the DGM-H to assess whether hyperagents enable the learning of general self-improvement mechanisms. From prior DGM-H runs on paper review and robotics reward design ( Section 5.1 ), we select one transfer hyperagent per run using the same lineage-discounted criterion described above ( Section D.4 ). The transfer hyperagents (one from each of 5 repeated runs) achieve an initial test-set score of 0.0 (CI: 0.0 – 0.0), reflecting the domain shift. After 50 iterations of DGM-H w/o self-improve starting from the transfer hyperagents, the best generated agents (selected based on validation score) achieve a test-set score of 0.630 (CI: 0.540 – 0.630). This corresponds to a imp@50 of 0.630 (CI: 0.540 – 0.630) ( Figure 3 ). These results show that transfer hyperagents can generate improved agents in a previously unseen domain. When using DGM-H w/o self-improve as the agent-generation algorithm, imp@50 for the transfer agents is significantly higher than imp@50 for the initial agent (p ¡ 0.05). This indicates that the transfer agents are substantially more effective at generating improved agents, and that the meta-improvements learned through DGM-H in one run are general and transferable, accelerating learning in a different domain.

We qualitatively attribute the observed transfer gains to a set of general-purpose meta-level capabilities that the DGM-H autonomously acquires during prior runs. In particular, the transfer hyperagents have features such as performance tracking and persistent memory, which allow them to reason about improvement as an ongoing process rather than as isolated code edits ( Section E.3 ). As a result, even when transferred to an unseen domain, these hyperagents can quickly self-improve and make meaningful progress ( Figure 3 ). This contrasts with DGM transfer agents, whose gains rely on domain-specific customizations and do not improve the underlying agent-generation process itself. These qualitative observations show that the DGM-H learns how to improve, yielding general and transferable self-improvement capability.

One example is DGM-H’s autonomous development of performance tracking infrastructure. Rather than relying on isolated evaluation outcomes, the hyperagent records, aggregates, and compares performance metrics across iterations, identifying which changes yield sustained improvements and which lead to regressions. This performance tracking supports informed decision-making, such as prioritizing promising iterations and avoiding unproductive modification directions. The snippet below shows an automatically introduced performance tracker that logs and organizes metrics across iterations: ⬇

Another example is DGM-H’s innovation of persistent memory, which enables learning to accumulate across iterations. Instead of merely logging numerical scores, the hyperagent stores synthesized insights, causal hypotheses, and forward-looking plans (e.g., identifying which generations performed best, diagnosing over-corrections, and proposing how to combine successful strategies). This memory is actively consulted during subsequent self-modification steps, allowing later generations to build on earlier discoveries and avoid repeating past mistakes. This is an example of a stored memory entry: ⬇

### 5.3 Compounding Self-Improvements

We investigate whether self-improvements learned by DGM-H in one setting continue to accumulate when DGM-H is run in a different setting. From prior DGM-H runs on the paper review and robotics reward design tasks ( Section 5.1 ), we select transfer hyperagents using the same selection mechanism described earlier ( Section 5.2 , Section D.4 ). We then evaluate their ability to continue self-improving in a new domain, Olympiad-level math grading. After 200 iterations of DGM-H starting from these transfer agents (DGM-H + transfer), the best generated agents (selected based on validation score) achieve a test-set score of 0.640 (CI: 0.550 – 0.720). Under the same experimental setup, DGM-H starting from the initial agent achieves a best test-set score of 0.610 (CI: 0.510 – 0.680). Although the difference between DGM-H + transfer and DGM-H is not statistically significant (p ¿ 0.05), DGM-H + transfer achieves a higher median performance and higher confidence intervals than DGM-H starting from the initial agent ( Figure 4 ). Notably, improvements at higher performance levels are increasingly difficult due to saturation effects (e.g., increasing performance from 0.7 to 0.8 is typically more challenging than from 0.0 to 0.1), making these gains meaningful despite their modest absolute magnitude. These results suggest that DGM-H’s self-improvements are reusable and can potentially accumulate across runs, supporting the possibility of compounding self-improvement over time.

The representative static baseline for Olympiad-level math grading from IMO-GradingBench is ProofAutoGrader ( Luong et al., 2025 ) . We initialize the DGM-H with ProofAutoGrader as the task agent and a transfer meta agent obtained from a prior DGM-H run (on paper review and robotics reward design), and then continue optimizing for Olympiad-level math grading. After 200 iterations, the best discovered agent achieves a test-set score of 0.700, outperforming ProofAutoGrader’s score of 0.670 ( Figure 4 ). We then evaluate both the best discovered agent and ProofAutoGrader on the full IMO-GradingBench to obtain a more accurate estimate of the improvement. On the full IMO-GradingBench, the DGM-H improves ProofAutoGrader’s accuracy from 0.561 to 0.601, and lowers the mean absolute error from 0.178 to 0.175 ( Section E.4 ). We open-source this artifact to support future research and development ( Section E.1.3 ). These results show that the DGM-H can build on strong existing solutions and further improve their performance.

## 6 Safety Discussion

The DGM-Hyperagents (DGM-H) introduces distinct safety considerations due to its ability to autonomously modify its own behavior and improvement mechanisms over time. In this work, all experiments are conducted under strict safety constraints. In particular, agent-generated code is executed within carefully sandboxed environments with enforced resource limits (e.g., timeouts, restricted internet access). These measures are designed to prevent unintended side effects, contain failures, and ensure that self-modifications remain confined to the intended experimental scope. Moreover, evaluation is performed using predefined tasks and metrics, and human oversight is maintained throughout all experiments.

Potential to evolve faster than human oversight. As AI systems gain the ability to modify themselves in increasingly open-ended ways, they can potentially evolve far more rapidly than humans can audit or interpret. At the cusp of such explosive capability growth, it becomes necessary to reconsider the roles that AI systems play in society ( Bengio et al., 2024 ) . Rather than framing safety solely in terms of absolute guarantees or full interpretability, a central challenge lies in balancing the potential of AI as a catalyst for human progress and well-being (e.g., automating scientific discovery) with the degree of trust humans are willing to place in these systems (e.g., delegating decisions or actions without requiring continuous human verification), while minimizing the many potential risks and downsides ( Clune, 2019 ; Ecoffet et al., 2020 ; Bengio et al., 2024 ; Weston and Foerster, 2025 ) . This balance is shaped by factors such as transparency and controllability.

While the DGM-H operates within safe research boundaries (e.g., sandboxing, controlled evaluations), these safeguards may become increasingly strained or infeasible as self-improving systems grow more capable. We discuss additional safety considerations in Appendix F . We proactively include this discussion to encourage broader engagement with what safety means for open-ended self-improving AI systems ( Clune, 2019 ; Ecoffet et al., 2020 ; Sheth et al., 2025 ) . This includes ongoing discussion about appropriate levels of trust, oversight, and transparency, and societal deliberation about which benefits these systems should prioritize when deployed.

## 7 Limitations and Conclusion

This work introduces hyperagents and incorporates them into the Darwin Gödel Machine (DGM) to form DGM-Hyperagents (DGM-H). DGM-H is a general self-improvement framework that open-endedly evolves an archive of self-improving hyperagents for any computable task, enabling the system to improve both task performance and its own self-improvement mechanism. Across diverse domains, the DGM-H produced substantial and generalizable gains in task performance while also improving its ability to generate improvements, with these meta-level gains transferring across domains and compounding across runs.

Our results suggest that self-improvements can compound across different experimental settings, but this version of DGM-H has limitations that constrain truly unbounded progress. First, it operates with a fixed task distribution. One direction is to co-evolve the task distribution by generating new tasks and curricula that adapt to the agent’s capabilities ( Clune, 2019 ; Zhang et al., 2024 ; Faldor et al., 2025 ; Bolton et al., 2025 ) . Second, components of the open-ended exploration loop (e.g., parent selection, evaluation protocols) remain fixed. Although hyperagents can modify their self-improvement mechanisms, they cannot alter the outer process that determines which agents are selected or how they are evaluated. Keeping these components fixed improves experimental stability and safety, but limits full self-modifiability. Enabling hyperagents to modify these outer-loop components and adapt their own search strategy and evaluation process is another promising direction for future work. Our preliminary results suggest such extensions are feasible ( Section E.5 ).

DGM-H demonstrate that open-ended self-improvement can be made practical across diverse domains. Provided sufficient safety considerations are worked out, the DGM-H suggest a path toward self-accelerating systems that not only search for better solutions, but continually improve their ability to self-improve.

## Acknowledgments

We thank Andrew Budker and Ricardo Silveira Cabral for supporting this work, and Alisia Lupidi, Chenxi Whitehouse, John Quan, Lisa Alazraki, Lovish Madaan, Lucia Cipolina-Kun, Mattia Opper, Michael Dennis, Parth Pathak, Rishi Hazra, Roberta Raileanu, Sandra Lefdal, Shashwat Goel, Shengran Hu, Timon Willi, Tim Rocktäschel, and Yoram Bachrach for insightful discussions and feedback.

## Author Contributions

Jenny Zhang led the conceptualization of the study, conducted the experiments, and wrote the manuscript. Bingchen Zhao and Wannan Yang contributed to experimental design and execution. Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, and Tatiana Shavrina provided feedback on the methodology and manuscript. All authors reviewed and approved the final manuscript.

## References

Audran-Reiss et al. (2025) A. Audran-Reiss, J. Armengol-EstapÃŠ, K. Hambardzumyan, A. Budhiraja, M. Josifoski, E. Toledo, R. Hazra, D. Magka, M. Shvartsman, P. Pathak, et al. What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity . arXiv preprint arXiv:2511.15593 . Cited by: §2 .

Auer et al. (2002) P. Auer, N. Cesa-Bianchi, and P. Fischer Finite-time analysis of the multiarmed bandit problem . Machine learning 47 ( 2 ), pp. 235–256 . Cited by: §E.5 .

Beaulieu et al. (2020) S. Beaulieu, L. Frati, T. Miconi, J. Lehman, K. O. Stanley, J. Clune, and N. Cheney Learning to continually learn . arXiv preprint arXiv:2002.09571 . Cited by: §2 .

Bengio et al. (2024) Y. Bengio, G. Hinton, A. Yao, D. Song, P. Abbeel, T. Darrell, Y. N. Harari, Y. Zhang, L. Xue, S. Shalev-Shwartz, et al. Managing extreme AI risks amid rapid progress . Science 384 ( 6698 ), pp. 842–845 . Cited by: §6 .

Bolton et al. (2025) A. Bolton, A. Lerchner, A. Cordell, A. Moufarek, A. Bolt, A. Lampinen, A. Mitenkova, A. O. Hallingstad, B. Vujatovic, B. Li, et al. Sima 2: A generalist embodied agent for virtual worlds . arXiv preprint arXiv:2512.04797 . Cited by: §7 .

Bradley et al. (2023) H. Bradley, A. Dai, H. Teufel, J. Zhang, K. Oostermeijer, M. Bellagente, J. Clune, K. Stanley, G. Schott, and J. Lehman Quality-diversity through AI feedback . arXiv preprint arXiv:2310.13032 . Cited by: §2 .

Brown et al. (2020) T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al. Language models are few-shot learners . Advances in neural information processing systems 33 , pp. 1877–1901 . Cited by: §4 .

Chalvidal et al. (2022) M. Chalvidal, T. Serre, and R. VanRullen Meta-reinforcement learning with self-modifying networks . Advances in Neural Information Processing Systems 35 , pp. 7838–7851 . Cited by: §2 .

Chen et al. (2026) Y. Chen, A. Maiga, H. A. Rahmani, and E. Yilmaz Automated Rubrics for Reliable Evaluation of Medical Dialogue Systems . arXiv preprint arXiv:2601.15161 . Cited by: §E.2 .

Clune (2019) J. Clune AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence . arXiv preprint arXiv:1905.10985 . Cited by: §2 , §6 , §6 , §7 .

Coiffard et al. (2025) L. Coiffard, P. Templier, and A. Cully Overcoming Deceptiveness in Fitness Optimization with Unsupervised Quality-Diversity . In Proceedings of the Genetic and Evolutionary Computation Conference , pp. 122–130 . Cited by: §2 .

Colas et al. (2023) C. Colas, L. Teodorescu, P. Oudeyer, X. Yuan, and M. Côté Augmenting autotelic agents with large language models . In Conference on Lifelong Learning Agents , pp. 205–226 . Cited by: §2 .

Cook et al. (2024) J. Cook, T. Rocktäschel, J. Foerster, D. Aumiller, and A. Wang Ticking all the boxes: Generated checklists improve llm evaluation and generation . arXiv preprint arXiv:2410.03608 . Cited by: §E.2 .

Coulom (2006) R. Coulom Efficient selectivity and backup operators in Monte-Carlo tree search . In International conference on computers and games , pp. 72–83 . Cited by: §A.2 .

Couto et al. (2024) P. H. Couto, Q. P. Ho, N. Kumari, B. K. Rachmat, T. G. H. Khuong, I. Ullah, and L. Sun-Hosoya Relevai-reviewer: A benchmark on AI reviewers for survey paper relevance . arXiv preprint arXiv:2406.10294 . Cited by: §3 .

Cully et al. (2015) A. Cully, J. Clune, D. Tarapore, and J. Mouret Robots that can adapt like animals . Nature 521 ( 7553 ), pp. 503–507 . Cited by: §2 .

Dharna et al. (2025) A. Dharna, C. Lu, and J. Clune Foundation model self-play: Open-ended strategy innovation via foundation models . arXiv preprint arXiv:2507.06466 . Cited by: §2 .

Ding et al. (2024) L. Ding, J. Zhang, J. Clune, L. Spector, and J. Lehman Quality Diversity through Human Feedback: Towards Open-Ended Diversity-Driven Optimization . In Forty-first International Conference on Machine Learning , Cited by: §2 .

Ecoffet et al. (2020) A. Ecoffet, J. Clune, and J. Lehman Open questions in creating safe open-ended AI: Tensions between control and creativity . In Artificial Life Conference Proceedings 32 , pp. 27–35 . Cited by: §6 , §6 .

Ecoffet et al. (2019) A. Ecoffet, J. Huizinga, J. Lehman, K. O. Stanley, and J. Clune Go-explore: a new approach for hard-exploration problems . arXiv preprint arXiv:1901.10995 . Cited by: §A.2 .

Faldor et al. (2025) M. Faldor, J. Zhang, A. Cully, and J. Clune OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code . In The Thirteenth International Conference on Learning Representations , Cited by: §2 , §7 .

Fan et al. (2024) Z. Fan, W. Wang, D. Zhang, et al. Sedareval: Automated evaluation using self-adaptive rubrics . In Findings of the Association for Computational Linguistics: EMNLP 2024 , pp. 16916–16930 . Cited by: §E.2 .

Fernando et al. (2023) C. Fernando, D. Banarse, H. Michalewski, S. Osindero, and T. Rocktäschel Promptbreeder: Self-referential self-improvement via prompt evolution . arXiv preprint arXiv:2309.16797 . Cited by: §2 .

Gauthier (2024) P. Gauthier O1 tops aider’s new polyglot leaderboard . Note: https://aider.chat/2024/12/21/polyglot.html Accessed: 2026-01-28 Cited by: §C.1 , §1 , §3 , §4.2 .

Genesis (2024) A. Genesis Genesis: a generative and universal physics engine for robotics and beyond . External Links: Link Cited by: §C.3 , §1 , §4.2 .

Good (1966) I. J. Good Speculations concerning the first ultraintelligent machine . In Advances in computers , Vol. 6 , pp. 31–88 . Cited by: §2 .

Grillotti et al. (2025) L. Grillotti, L. Coiffard, O. Pang, M. Faldor, and A. Cully From Tabula Rasa to Emergent Abilities: Discovering Robot Skills via Real-World Unsupervised Quality-Diversity . arXiv preprint arXiv:2508.19172 . Cited by: §2 .

Havrilla et al. (2024) A. Havrilla, Y. Du, S. C. Raparthy, C. Nalmpantis, J. Dwivedi-Yu, M. Zhuravinskyi, E. Hambro, S. Sukhbaatar, and R. Raileanu Teaching large language models to reason with reinforcement learning . arXiv preprint arXiv:2403.04642 . Cited by: §2 .

Herr et al. (2025) N. Herr, T. Rocktäschel, and R. Raileanu LLM-First Search: Self-Guided Exploration of the Solution Space . arXiv preprint arXiv:2506.05213 . Cited by: §A.2 .

Hu et al. (2025) S. Hu, C. Lu, and J. Clune Automated Design of Agentic Systems . In The Thirteenth International Conference on Learning Representations , Cited by: Appendix B , §2 , §4.1 , §5.1 .

Hughes et al. (2024) E. Hughes, M. Dennis, J. Parker-Holder, F. Behbahani, A. Mavalankar, Y. Shi, T. Schaul, and T. Rocktaschel Open-endedness is essential for artificial superhuman intelligence . arXiv preprint arXiv:2406.04268 . Cited by: §2 .

Hutter (2003) M. Hutter A gentle introduction to the universal algorithmic agent AIXI . Artificial General Intelligence . Cited by: §2 .

Irie et al. (2022) K. Irie, I. Schlag, R. Csordás, and J. Schmidhuber A modern self-referential weight matrix that learns to modify itself . In International Conference on Machine Learning , pp. 9660–9677 . Cited by: §2 .

Jackson et al. (2024) M. T. Jackson, C. Lu, L. Kirsch, R. T. Lange, S. Whiteson, and J. N. Foerster Discovering temporally-aware reinforcement learning algorithms . arXiv preprint arXiv:2402.05828 . Cited by: §2 .

Javed and White (2019) K. Javed and M. White Meta-learning representations for continual learning . Advances in neural information processing systems 32 . Cited by: §2 .

Jiang et al. (2023) M. Jiang, T. Rocktäschel, and E. Grefenstette General intelligence requires rethinking exploration . Royal Society Open Science 10 ( 6 ), pp. 230539 . Cited by: §2 .

Jimenez et al. (2024) C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. R. Narasimhan SWE-bench: can language models resolve real-world github issues? . In The Twelfth International Conference on Learning Representations , Cited by: §3 .

Kirsch and Schmidhuber (2022) L. Kirsch and J. Schmidhuber Eliminating meta optimization through self-referential meta learning . arXiv preprint arXiv:2212.14392 . Cited by: §1 , §2 .

Klissarov et al. (2023) M. Klissarov, P. D’Oro, S. Sodhani, R. Raileanu, P. Bacon, P. Vincent, A. Zhang, and M. Henaff Motif: Intrinsic motivation from artificial intelligence feedback . arXiv preprint arXiv:2310.00166 . Cited by: §2 .

Klissarov et al. (2025) M. Klissarov, M. Henaff, R. Raileanu, S. Sodhani, P. Vincent, A. Zhang, P. Bacon, D. Precup, M. C. Machado, and P. D’Oro MaestroMotif: Skill Design from Artificial Intelligence Feedback . In The Thirteenth International Conference on Learning Representations , Cited by: §2 .

Kwa et al. (2025) T. Kwa, B. West, J. Becker, A. Deng, K. Garcia, M. Hasin, S. Jawhar, M. Kinniment, N. Rush, S. Von Arx, et al. Measuring ai ability to complete long tasks . arXiv preprint arXiv:2503.14499 . Cited by: §2 .

Lange et al. (2023) R. Lange, T. Schaul, Y. Chen, T. Zahavy, V. Dalibard, C. Lu, S. Singh, and S. Flennerhag Discovering evolution strategies via meta-black-box optimization . In Proceedings of the Companion Conference on Genetic and Evolutionary Computation , pp. 29–30 . Cited by: §2 .

Lehman et al. (2023) J. Lehman, J. Gordon, S. Jain, K. Ndousse, C. Yeh, and K. O. Stanley Evolution through large models . In Handbook of evolutionary machine learning , pp. 331–366 . Cited by: §2 .

Lehman and Stanley (2011) J. Lehman and K. O. Stanley Evolving a diversity of virtual creatures through novelty search and local competition . In Proceedings of the 13th annual conference on Genetic and evolutionary computation , pp. 211–218 . Cited by: §2 .

Li et al. (2024) H. Li, X. Yang, Z. Wang, X. Zhu, J. Zhou, Y. Qiao, X. Wang, H. Li, L. Lu, and J. Dai Auto mc-reward: Automated dense reward design with large language models for minecraft . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 16426–16435 . Cited by: §2 .

Lu et al. (2024a) C. Lu, S. Holt, C. Fanconi, A. Chan, J. Foerster, M. van der Schaar, and R. Lange Discovering preference optimization algorithms with and for large language models . Advances in Neural Information Processing Systems 37 , pp. 86528–86573 . Cited by: §2 .

Lu et al. (2024b) C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha The ai scientist: Towards fully automated open-ended scientific discovery . arXiv preprint arXiv:2408.06292 . Cited by: §2 .

Lu et al. (2023) C. Lu, S. Towers, and J. Foerster Arbitrary order meta-learning with simple population-based evolution . In Artificial Life Conference Proceedings 35 , Vol. 2023 , pp. 67 . Cited by: §1 , §2 .

Luong et al. (2025) M. Luong, D. Hwang, H. H. Nguyen, G. Ghiasi, Y. Chervonyi, I. Seo, J. Kim, G. Bingham, J. Lee, S. Mishra, et al. Towards robust mathematical reasoning . In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing , pp. 35406–35430 . Cited by: §C.4 , §C.4 , Figure 10 , §E.4 , §4.2 , §5.3 .

Lv et al. (2026) C. Lv, J. Zhou, W. Zhao, J. Xu, Z. Huang, M. Tian, S. Dou, T. Gui, L. Tian, X. Zhou, X. Zheng, X. Huang, and J. Zhou Learning Query-Specific Rubrics from Human Preferences for DeepResearch Report Generation . arXiv preprint arXiv:2602.03619 . Cited by: §E.2 .

Ma et al. (2024) Y. J. Ma, W. Liang, G. Wang, D. Huang, O. Bastani, D. Jayaraman, Y. Zhu, L. Fan, and A. Anandkumar Eureka: Human-Level Reward Design via Coding Large Language Models . In The Twelfth International Conference on Learning Representations , Cited by: §3 , §4.2 .

Miconi et al. (2020) T. Miconi, A. Rawal, J. Clune, and K. O. Stanley Backpropamine: training self-modifying neural networks with differentiable neuromodulated plasticity . arXiv preprint arXiv:2002.10585 . Cited by: §2 .

Miconi et al. (2018) T. Miconi, K. Stanley, and J. Clune Differentiable plasticity: training plastic neural networks with backpropagation . In International Conference on Machine Learning , pp. 3559–3568 . Cited by: §2 .

Mouret and Clune (2015) J. Mouret and J. Clune Illuminating search spaces by mapping elites . arXiv preprint arXiv:1504.04909 . Cited by: §2 .

Novikov et al. (2025) A. Novikov, N. Vũ, M. Eisenberger, E. Dupont, P. Huang, A. Z. Wagner, S. Shirobokov, B. Kozlovskii, F. J. Ruiz, A. Mehrabian, et al. AlphaEvolve: A coding agent for scientific and algorithmic discovery . arXiv preprint arXiv:2506.13131 . Cited by: §2 .

Oh et al. (2025) J. Oh, G. Farquhar, I. Kemaev, D. A. Calian, M. Hessel, L. Zintgraf, S. Singh, H. Van Hasselt, and D. Silver Discovering state-of-the-art reinforcement learning algorithms . Nature , pp. 1–2 . Cited by: §2 .

Pourcel et al. (2023) J. Pourcel, C. Colas, G. Molinaro, P. Oudeyer, and L. Teodorescu ACES: Generating Diverse Programming Puzzles with with Autotelic Generative Models . arXiv preprint arXiv:2310.10692 . Cited by: §2 .

Qiu et al. (2025) X. Qiu, Y. Gan, C. F. Hayes, Q. Liang, E. Meyerson, B. Hodjat, and R. Miikkulainen Evolution strategies at scale: Llm fine-tuning beyond reinforcement learning . arXiv preprint arXiv:2509.24372 . Cited by: §2 .

Robeyns et al. (2025) M. Robeyns, M. Szummer, and L. Aitchison A self-improving coding agent . arXiv preprint arXiv:2504.15228 . Cited by: §2 .

Romera-Paredes et al. (2024) B. Romera-Paredes, M. Barekatain, A. Novikov, M. Balog, M. P. Kumar, E. Dupont, F. J. Ruiz, J. S. Ellenberg, P. Wang, O. Fawzi, et al. Mathematical discoveries from program search with large language models . Nature 625 ( 7995 ), pp. 468–475 . Cited by: §2 .

Samvelyan et al. (2024) M. Samvelyan, S. C. Raparthy, A. Lupu, E. Hambro, A. H. Markosyan, M. Bhatt, Y. Mao, M. Jiang, J. Parker-Holder, J. Foerster, et al. Rainbow teaming: Open-ended generation of diverse adversarial prompts . Advances in Neural Information Processing Systems 37 , pp. 69747–69786 . Cited by: §2 .

Schick et al. (2023) T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, E. Hambro, L. Zettlemoyer, N. Cancedda, and T. Scialom Toolformer: Language models can teach themselves to use tools . Advances in Neural Information Processing Systems 36 , pp. 68539–68551 . Cited by: §4 .

Schmidhuber (1993) J. Schmidhuber A neural network that embeds its own meta-levels . In IEEE International Conference on Neural Networks , pp. 407–412 . Cited by: §2 .

Schmidhuber (2003) J. Schmidhuber Gödel machines: self-referential universal problem solvers making provably optimal self-improvements . arXiv preprint cs/0309048 . Cited by: §2 .

Schulman et al. (2017) J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov Proximal policy optimization algorithms . arXiv preprint arXiv:1707.06347 . Cited by: §C.3 .

Sheth et al. (2025) I. Sheth, J. Wehner, S. Abdelnabi, R. Binkyte, and M. Fritz Safety is Essential for Responsible Open-Ended Systems . arXiv preprint arXiv:2502.04512 . Cited by: §6 .

Silver et al. (2016) D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. Van Den Driessche, J. Schrittwieser, I. Antonoglou, V. Panneershelvam, M. Lanctot, et al. Mastering the game of Go with deep neural networks and tree search . nature 529 ( 7587 ), pp. 484–489 . Cited by: §A.2 , §2 .

Silver et al. (2017) D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai, A. Guez, M. Lanctot, L. Sifre, D. Kumaran, T. Graepel, et al. Mastering chess and shogi by self-play with a general reinforcement learning algorithm . arXiv preprint arXiv:1712.01815 . Cited by: §2 .

Stanley et al. (2017) K. O. Stanley, J. Lehman, and L. Soros Open-endedness: The last grand challenge you’ve never heard of . While open-endedness could be a force for discovering intelligence, it could also be a component of AI itself . Cited by: §2 .

Stanley and Miikkulainen (2002) K. O. Stanley and R. Miikkulainen Evolving neural networks through augmenting topologies . Evolutionary computation 10 ( 2 ), pp. 99–127 . Cited by: §2 .

Strathern (1997) M. Strathern ‘Improving ratings’: audit in the British University system . European review 5 ( 3 ), pp. 305–321 . Cited by: Appendix F .

Turing et al. (1936) A. M. Turing et al. On computable numbers, with an application to the Entscheidungsproblem . J. of Math 58 ( 345-363 ), pp. 5 . Cited by: §3 .

Wang et al. (2024) G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and A. Anandkumar Voyager: An Open-Ended Embodied Agent with Large Language Models . Transactions on Machine Learning Research . Cited by: §2 .

Wang et al. (2025a) J. Wang, Z. Hu, and L. Bing Evolving Prompts In-Context: An Open-ended, Self-replicating Perspective . arXiv preprint arXiv:2506.17930 . Cited by: §2 .

Wang et al. (2025b) W. Wang, P. Piękos, L. Nanbo, F. Laakom, Y. Chen, M. Ostaszewski, M. Zhuge, and J. Schmidhuber Huxley-G \ \backslash ” odel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine . arXiv preprint arXiv:2510.21614 . Cited by: §A.2 , §2 , §2 , §3 .

Wei et al. (2025a) T. Wei, N. Sachdeva, B. Coleman, Z. He, Y. Bei, X. Ning, M. Ai, Y. Li, J. He, E. H. Chi, et al. Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory . arXiv preprint arXiv:2511.20857 . Cited by: §E.3.7 .

Wei et al. (2025b) Y. Wei, Z. Sun, E. McMilin, J. Gehring, D. Zhang, G. Synnaeve, D. Fried, L. Zhang, and S. Wang Toward Training Superintelligent Software Agents through Self-Play SWE-RL . arXiv preprint arXiv:2512.18552 . Cited by: §2 .

Wen et al. (2025) J. Wen, Z. Ankner, A. Somani, P. Hase, S. Marks, J. Goldman-Wetzler, L. Petrini, H. Sleight, C. Burns, H. He, et al. Unsupervised Elicitation of Language Models . arXiv preprint arXiv:2506.10139 . Cited by: §2 .

Weng et al. (2026) Z. Weng, A. Antoniades, D. Nathani, Z. Zhang, X. Pu, and X. E. Wang Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing . arXiv preprint arXiv:2602.04837 . Cited by: §A.2 , §E.3.7 , §2 .

Weston and Foerster (2025) J. Weston and J. Foerster Ai & human co-improvement for safer co-superintelligence . arXiv preprint arXiv:2512.05356 . Cited by: §6 .

Wu et al. (2024) Z. Wu, C. Han, Z. Ding, Z. Weng, Z. Liu, S. Yao, T. Yu, and L. Kong Os-copilot: Towards generalist computer agents with self-improvement . arXiv preprint arXiv:2402.07456 . Cited by: §2 .

Xia et al. (2025a) C. S. Xia, Z. Wang, Y. Yang, Y. Wei, and L. Zhang Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly? . arXiv preprint arXiv:2511.13646 . Cited by: §2 , §2 .

Xia et al. (2026) P. Xia, J. Chen, H. Wang, J. Liu, K. Zeng, Y. Wang, S. Han, Y. Zhou, X. Zhao, H. Chen, et al. SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning . arXiv preprint arXiv:2602.08234 . Cited by: §2 .

Xia et al. (2025b) P. Xia, K. Zeng, J. Liu, C. Qin, F. Wu, Y. Zhou, C. Xiong, and H. Yao Agent0: Unleashing self-evolving agents from zero data via tool-integrated reasoning . arXiv preprint arXiv:2511.16043 . Cited by: §2 .

Xiong et al. (2026) Y. Xiong, S. Hu, and J. Clune Learning to Continually Learn via Meta-learning Agentic Memory Designs . arXiv preprint arXiv:2602.07755 . Cited by: §E.3.7 .

Yamada et al. (2025) Y. Yamada, R. T. Lange, C. Lu, S. Hu, C. Lu, J. Foerster, J. Clune, and D. Ha The ai scientist-v2: Workshop-level automated scientific discovery via agentic tree search . arXiv preprint arXiv:2504.08066 . Cited by: §C.2 , §4.2 , §5.1 .

Ye et al. (2026) H. Ye, X. He, V. Arak, H. Dong, and G. Song Meta Context Engineering via Agentic Skill Evolution . arXiv preprint arXiv:2601.21557 . Cited by: §2 .

Yin et al. (2025) X. Yin, X. Wang, L. Pan, L. Lin, X. Wan, and W. Y. Wang Gödel agent: a self-referential agent framework for recursively self-improvement . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 27890–27913 . Cited by: §2 , §2 .

Yuan et al. (2026) J. Yuan, J. Nöther, N. Jaques, and G. Radanović AgenticRed: Optimizing Agentic Systems for Automated Red-teaming . arXiv preprint arXiv:2601.13518 . Cited by: §2 .

Zelikman et al. (2024) E. Zelikman, E. Lorch, L. Mackey, and A. T. Kalai Self-taught optimizer (stop): Recursively self-improving code generation . In First Conference on Language Modeling , Cited by: §2 .

Zelikman et al. (2022) E. Zelikman, Y. Wu, J. Mu, and N. Goodman Star: Bootstrapping reasoning with reasoning . Advances in Neural Information Processing Systems 35 , pp. 15476–15488 . Cited by: §2 .

Zhang et al. (2025a) A. L. Zhang, T. Kraska, and O. Khattab Recursive Language Models . arXiv preprint arXiv:2512.24601 . Cited by: §2 .

Zhang et al. (2026) H. Zhang, Q. Long, J. Bao, T. Feng, W. Zhang, H. Yue, and W. Wang MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents . arXiv preprint arXiv:2602.02474 . Cited by: §E.3.7 .

Zhang et al. (2025b) J. Zhang, S. Hu, C. Lu, R. Lange, and J. Clune Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents . arXiv preprint arXiv:2505.22954 . Cited by: §A.2 , Appendix B , §C.1 , §D.1 , §1 , §1 , §1 , §2 , §2 , Figure 1 , §3 , §3 , §4.1 , §4.2 , §5.1 , Abstract .

Zhang et al. (2024) J. Zhang, J. Lehman, K. Stanley, and J. Clune OMNI: Open-endedness via Models of human Notions of Interestingness . In The Twelfth International Conference on Learning Representations , Cited by: §2 , §7 .

Zhang et al. (2025c) Q. Zhang, C. Hu, S. Upasani, B. Ma, F. Hong, V. Kamanuru, J. Rainton, C. Wu, M. Ji, H. Li, et al. Agentic context engineering: Evolving contexts for self-improving language models . arXiv preprint arXiv:2510.04618 . Cited by: §2 .

Zhao et al. (2025) B. Zhao, D. Magka, M. Jiang, X. Li, R. Raileanu, T. Shavrina, J. Gagnon-Audet, K. Niu, S. Sodhani, M. Shvartsman, et al. The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements . arXiv preprint arXiv:2506.22419 . Cited by: §2 .

Zhao et al. (2026) B. Zhao, J. Zhang, C. Whitehouse, M. Jiang, M. Shvartsman, A. Charnalia, D. Magka, T. Shavrina, D. Dunfield, O. M. Aodha, and Y. Bachrach APRES: An Agentic Paper Revision and Evaluation System . arXiv preprint arXiv:2603.03142 . Cited by: §C.2 , §1 , §4.2 .

Zhuge et al. (2024) M. Zhuge, W. Wang, L. Kirsch, F. Faccio, D. Khizbullin, and J. Schmidhuber Gptswarm: Language agents as optimizable graphs . In Forty-first International Conference on Machine Learning , Cited by: §2 .

Zoph and Le (2017) B. Zoph and Q. Le Neural Architecture Search with Reinforcement Learning . In International Conference on Learning Representations , Cited by: §2 .

Zweiger et al. (2025) A. Zweiger, J. Pari, H. Guo, E. Akyürek, Y. Kim, and P. Agrawal Self-Adapting Language Models . arXiv preprint arXiv:2506.10943 . Cited by: §2 .

## Table of Contents

## Appendix A Algorithmic details

This appendix provides additional algorithmic details for the DGM-Hyperagents (DGM-H). We first describe the implementation of the initial hyperagent, including the tools and prompts available to the initial task and meta agents ( Section A.1 ). We then detail the parent selection mechanism used during open-ended exploration, which balances exploitation of high-performing agents with continued exploration of the archive ( Section A.2 ). Finally, we present pseudocode for DGM-H ( Section A.3 ).

### A.1 Initial Agent

We present the details of the tools available to the initial hyperagent and its prompts ( Section 4 ).

Initial task agent prompt: ⬇

Initial meta agent prompt: ⬇

Information of the given bash tool: ⬇

Information of the given edit tool: ⬇

### A.2 Parent Selection

At each iteration, we select a subset of agents from the archive as parents to self-modify and produce new child agents ( Section 3 ). We use a mechanism similar to that of Zhang et al. [2025b] , inspired by Ecoffet et al. [2019] , that is roughly proportional to an agent’s performance score and inversely proportional to the number of children that successfully compiled. This selection mechanism biases sampling toward agents that outperform the current frontier average while down-weighting agents that have already produced many children, retaining smooth probabilistic exploration and automatically adapting as the archive improves over time. The details of the parent selection process are outlined below.

At each iteration t t of the DGM-H run, let 𝒜 t = { a 0 , a 1 , … , a t } \mathcal{A}^{t}=\{a_{0},a_{1},\dots,a_{t}\} denote the archive of candidate agents with associated performance scores α i = performance ⁡ ( a i ) \alpha_{i}=\mathrm{performance}(a_{i}) . All agents in the archive are eligible for parent selection.

We first compute a dynamic midpoint based on the current performance distribution. Let α m ​ i ​ d = 1 m ​ ∑ j ∈ 𝒯 t α j , \alpha_{mid}\;=\;\frac{1}{m}\sum_{j\in\mathcal{T}^{t}}\alpha_{j}, where 𝒯 t ⊂ 𝒜 t \mathcal{T}^{t}\subset\mathcal{A}^{t} indexes the top- m m highest-performing agents at iteration t t (with m = 3 m=3 in our experiments). This midpoint adapts over time and reflects the current performance frontier.

Each agent’s score is first passed through a sigmoid transformation: s i = 1 1 + exp ⁡ ( − λ ⁡ ( α i − α m ​ i ​ d ) ) , s_{i}\;=\;\frac{1}{1+\exp\!\bigl(-\lambda(\alpha_{i}-\alpha_{mid})\bigr)}, where λ > 0 \lambda>0 controls the sharpness of selection. We set λ = 10 \lambda=10 .

To encourage exploration, we introduce a novelty bonus based on the number of compiled children n i n_{i} produced by agent a i a_{i} : h i = 1 1 + n i . h_{i}\;=\;\frac{1}{1+n_{i}}.

We then form an unnormalized weight w i = s i ​ h i , w_{i}\;=\;s_{i}\,h_{i}, which balances performance and novelty.

The weights are normalized to form a categorical distribution: p i = { w i ∑ j = 0 t w j , if ​ ∑ j = 0 t w j > 0 , 1 t + 1 , otherwise . p_{i}\;=\;\begin{cases}\dfrac{w_{i}}{\sum_{j=0}^{t}w_{j}},&\text{if }\sum_{j=0}^{t}w_{j}>0,\\[10.0pt] \dfrac{1}{t+1},&\text{otherwise}.\end{cases}

We sample parents independently with replacement according to this distribution: { parents } ∼ Categorical ⁡ ( { p i } i = 0 t ) . \{\,\text{parents}\,\}\;\sim\;\mathrm{Categorical}\bigl(\{p_{i}\}_{i=0}^{t}\bigr).

A wide range of search and exploration strategies has been proposed in prior work [ Coulom, 2006 , Silver et al., 2016 , Herr et al., 2025 , Wang et al., 2025b , Weng et al., 2026 ] . We present preliminary evidence that the DGM-H can begin to autonomously rediscover and adapt such strategies by modifying its own exploration dynamics ( Section E.5 ). An open research direction is whether self-improving systems can reliably discover search and exploration mechanisms that outperform carefully handcrafted algorithms.

### A.3 Pseudocode

This is the pseudocode of the DGM-H, described in Section 3 :

### A.4 Multi-domain Optimization

When optimizing for multiple domains within the same run, hyperagents are evaluated on tasks from different domains and have access to all evaluations across these tasks during self-modification. We do not specify which particular domain or task to prioritize. Parent selection is based on the average performance across domains. As a result, improvements in any domain increase selection probability, while regressions reduce it. Because the meta agent can inspect evaluations from any task, it can introduce shared mechanisms (e.g., structured reasoning, memory, and error handling) that benefit multiple domains simultaneously. Thus, rather than manually specifying which task or domain to optimize, hyperagents can optimize across multiple domains within the same run.

## Appendix B Baseline Details

We outline the pseudocode for each baseline described in Section 4.1 , provide a comparison table summarizing their key differences ( Table 1 ), and include a detailed conceptual figure that visually contrasts the architectural components and modification mechanisms across DGM variants and hyperagents ( Figure 5 ).

Method Self-improving meta agents Open-ended exploration Metacognitive self-modification (i.e., hyperagents) DGM-H ✓ ✓ ✓ DGM-H w/o self-improve ✕ ✓ ✓ DGM-H w/o open-ended exploration ✓ ✕ ✓ DGM ✓ ✓ ✕ DGM-custom ✓ ✓ ✕

This is the pseudocode of the baseline DGM-H without self-improving agents [ Hu et al., 2025 , ADAS,] :

This is the pseudocode of the baseline DGM-H without open-ended exploration:

This is the pseudocode for the original DGM [ Zhang et al., 2025b ] , framed within the hyperagent setting:

The handcrafted instruction-generation step in the original DGM: ⬇

The customized instruction-generation step in DGM-custom: ⬇

## Appendix C Domain Details

This appendix provides detailed descriptions of each domain used for evaluation: Polyglot ( Section C.1 ), paper review ( Section C.2 ), robotics reward design ( Section C.3 ), Olympiad-level math grading ( Section C.4 ). For each domain, we specify the agent’s input and required output for a given task, the evaluation protocol, and representative static baselines ( Table 2 ).

### C.1 Polyglot

In the Polyglot coding benchmark [ Gauthier, 2024 ] , each task consists of a software repository and a natural language instruction describing a desired change to the codebase. The agent is given access to the full repository and must modify the files to correctly implement the instruction, producing a patch (i.e., a set of code edits) applied to the repository. Performance is evaluated by running a predefined test suite on the modified repository. A task is considered to be successfully done if all tests pass. We follow the setup used in the DGM [ Zhang et al., 2025b ] , which largely mirrors the Polyglot leaderboard configuration, with one key difference: the leaderboard reports pass@2, allowing the agent to view feedback from ground-truth tests once, whereas we report pass@1, in which the agent never sees ground-truth test results. We adopt the same training and test splits as in the DGM. Training tasks are selected as a random subset of the full benchmark, comprising a total of 60 tasks. If an agent achieves more than 40% success on an initial 10-task subset, it is subsequently evaluated on the remaining 50 training tasks. There is no validation subset for this domain. As a final evaluation to more accurately assess performance improvements, we evaluate the generated agents on the full Polyglot benchmark, which consists of 165 unseen tasks.

Initial 10 training tasks for preliminary evaluation:

• go__dominoes

• cpp__all-your-base

• python__dominoes

• java__sgf-parsing

• javascript__robot-name

• rust__variable-length-quantity

• python__beer-song

• go__book-store

• javascript__bottle-song

• rust__bowling

Additional 50 training tasks for full evaluation:

• javascript__queen-attack

• rust__wordy

• python__dot-dsl

• java__satellite

• cpp__diamond

• rust__accumulate

• go__error-handling

• cpp__queen-attack

• rust__poker

• python__sgf-parsing

• rust__react

• java__ledger

• go__connect

• rust__macros

• javascript__triangle

• java__zipper

• java__bowling

• python__tree-building

• javascript__say

• java__wordy

• python__food-chain

• javascript__wordy

• python__poker

• javascript__grade-school

• cpp__gigasecond

• java__forth

• python__dominoes

• go__word-search

• javascript__simple-linked-list

• go__counter

• java__react

• javascript__ocr-numbers

• python__scale-generator

• java__go-counting

• rust__doubly-linked-list

• python__grade-school

• javascript__forth

• python__wordy

• java__mazy-mice

• cpp__bank-account

• python__zipper

• java__custom-set

• java__rest-api

• go__transpose

• rust__gigasecond

• rust__say

• go__food-chain

• rust__pig-latin

• go__markdown

• go__crypto-square

### C.2 Paper Review

The data in this domain are drawn from Zhao et al. [2026] . Each task in the paper review domain consists of the full text of an AI research paper. The agent must predict a binary accept or reject decision, simulating the role of a conference reviewer. Ground-truth labels correspond to real acceptance decisions from top-tier machine learning conferences, including ICLR 2024/2025 and NeurIPS 2023/2024. Performance is measured by classification accuracy with respect to these labels. We randomly sample tasks to construct training, validation, and test splits, each containing 100 tasks. During training, the agent is first evaluated on a subset of 10 tasks from the training split. If the agent succeeds on at least one of these tasks, it is then evaluated on the full set of 100 training tasks.

AI-Scientist-v2 [ Yamada et al., 2025 ] employs an AI reviewer to automatically improve generated AI research papers. We adopt the AI reviewer proposed in that work as our representative static baseline: ⬇

### C.3 Robotics Reward Design

Each task in the robotics reward design domain specifies a robotic control objective in the Genesis simulator [ Genesis, 2024 ] using a Go2 quadruped robot. The agent is given a textual description of the task (e.g., walk forward at a target velocity) and outputs a Python reward function, which is then used to train a RL policy [ Schulman et al., 2017 , i.e., PPO,] for the robot. Performance is evaluated by executing the trained RL policy in the simulator and computing the task performance measure (e.g., velocity tracking error). Scores are averaged over repeated evaluations to reduce variance due to stochasticity in reward generation or RL.

The training task requires generating a reward function that enables the robot to walk forward while tracking a target linear velocity. Performance is measured using the mean squared error between the commanded and actual walking velocities. During training, each agent is initially evaluated 3 repeated times on the same task, generating one reward function per evaluation. If at least one generated reward function yields a non-zero performance score, the agent is evaluated 3 additional times. The final performance score is reported as the average across the 6 evaluations. No separate validation task is curated for this domain.

To assess whether the same agent can generate suitable reward functions across different robotics tasks, we pair a relatively simple training task with a more challenging test task on the same robot. The test task requires generating a reward function that trains the robot to maximize torso height. Reward functions that are effective for forward walking do not induce jumping behaviors, which are more optimal for maximizing torso height. Moreover, directly incentivizing torso height (the performance measure) typically leads to a suboptimal standing behavior of standing stall. Achieving high performance therefore requires non-myopic reward design that encourages intermediate behaviors, such as lowering the torso before jumping.

The default reward function for the test task directly rewards the performance measure of maximizing torso height. This always produces a behavior in which the robot simply stands as tall as possible ( Figure 6 ): ⬇

### C.4 Olympiad-level Math Grading

In the Olympiad-level math grading domain, tasks are drawn from IMO-GradingBench [ Luong et al., 2025 ] . Each task consists of an Olympiad-level math problem, a candidate solution, reference solutions, and grading guidelines. The agent is required to assign a discrete score from the set {0, 1, 6, 7}, corresponding to the categories {incorrect, partial, almost, correct}. The agent’s output is a single numeric grade. Performance is measured by accuracy with respect to expert human annotations, with additional analyses provided in Section E.4 . We use randomly sampled subsets of tasks for training, validation, and testing, with 100 tasks in each split. During training, an agent is first evaluated on a subset of 10 tasks (out of 100). If the agent succeeds on at least one of these tasks, it is then evaluated on the full training set.

Representative static baseline (ProofAutoGrader) from Luong et al. [2025] : ⬇

## Appendix D Experiment Details

This appendix provides additional experimental details to support reproducibility of the results. We first summarize the FMs and hyperparameters used for self-modification and task evaluation across domains ( Section D.1 ), followed by an estimate of the computational cost of running the DGM-H in each setting ( Section D.2 ). We then formally define the improvement@k metric used to quantify an agent’s ability to produce improved variants under a fixed budget ( Section D.3 ). Finally, we describe the procedure used to select transfer agents for cross-domain experiments ( Section D.4 ).

### D.1 Hyperparameters for FMs

Table 3 summarizes the foundation models (FMs) used across experimental settings. For the Polyglot coding domain, we adopt the same FMs and temperature configurations as Zhang et al. [2025b] to ensure a fair comparison. In all other domains, we use Claude-4.5-Sonnet for self-modification, given its strong performance on coding. For task evaluation, we select the FM based on practical considerations, including computational cost, rate limits, response latency, and overall task competence. In the robotics reward design setting, where the agent must implement reward functions in code, we again use Claude-4.5-Sonnet. For Olympiad-level mathematics grading, which requires substantial mathematical reasoning, we use o4-mini. The temperature is set to 0.0 for all FMs in every setting, except for o4-mini, which is fixed at 1.0.

### D.2 Cost Estimate

Running the DGM-H for 100 iterations incurs a cost of approximately 33M tokens for the self-modification phase alone (excluding task evaluation). The total cost of an experiment therefore consists of the self-modification cost plus the cost of task evaluation. For the paper review and robotics reward design experiments, the evaluation cost per iteration is 0.506M tokens (0.5M tokens for paper review evaluation + 0.006M tokens for robotics reward design evaluation). Consequently, for a 100-iteration run ( Section 5 ), the estimated total cost is 33M tokens for self-modification plus 0.506M × 100 for evaluation, yielding a total of approximately 88.6M tokens.

A more granular break down of the task evaluation cost is:

### D.3 Improvement@k Metric

Let M M denote an initial meta agent, A A an initial task agent, and 𝒯 \mathcal{T} a fixed set of evaluation tasks. Let 𝒢 \mathcal{G} denote an agent-generation algorithm (e.g., DGM or DGM-H variants). The meta agent M M is held fixed and is allowed to generate up to k k new task agents by iteratively applying 𝒢 \mathcal{G} starting from A A .

Let 𝒜 ( k ) = { A 1 , A 2 , … , A k } \mathcal{A}^{(k)}=\{A^{1},A^{2},\dots,A^{k}\} denote the set of task agents generated by M M within k k modification steps. Each task agent A ′ ∈ { A } ∪ 𝒜 ( k ) A^{\prime}\in\{A\}\cup\mathcal{A}^{(k)} is evaluated on 𝒯 \mathcal{T} using a fixed evaluation procedure Evaluate ⁡ ( ⋅ , 𝒯 ) \mathrm{Evaluate}(\cdot,\mathcal{T}) , where higher values indicate better performance.

We define the improvement@k metric as imp ​ @ ​ k ​ ( M , A , 𝒢 , 𝒯 ) = max A ′ ∈ 𝒜 ( k ) ​ ( M , A , 𝒢 ) ⁡ Evaluate ⁡ ( A ′ , 𝒯 ) − Evaluate ⁡ ( A , 𝒯 ) , \mathrm{imp@}k(M,A,\mathcal{G},\mathcal{T})\;=\;\max_{A^{\prime}\in\mathcal{A}^{(k)}(M,A,\mathcal{G})}\mathrm{Evaluate}(A^{\prime},\mathcal{T})\;-\;\mathrm{Evaluate}(A,\mathcal{T}),

Intuitively, imp@k measures the maximum performance improvement that a fixed meta agent M M , operating under a specific agent-generation algorithm 𝒢 \mathcal{G} , can obtain by generating up to k k modified task agents starting from the initial task agent A A . Larger values of imp@k indicate stronger agent-generation capability under a fixed computational budget and generation procedure.

A limitation of imp@k is that it treats performance improvements as linear, without accounting for differences in difficulty across performance levels. In particular, improvements near saturation (e.g., increasing accuracy from 0.7 to 0.8) may be substantially harder to achieve than equivalent absolute gains at lower performance levels (e.g., from 0.0 to 0.1). As a result, imp@k may underestimate the significance of improvements achieved at higher performance regimes. However, this limitation does not affect the analyses presented in this work, as imp@k is used primarily for relative comparisons under matched initial conditions and fixed evaluation budgets, where all methods are subject to the same saturation effects ( Section 5.2 ).

### D.4 Transfer Agent Selection

To select agents for the transfer experiments ( Sections 5.2 and 5.3 ), we use a descendant growth criterion that favors agents which serve as strong stepping stones for subsequent improvements, rather than agents that are merely high-scoring themselves. Concretely, given the final archive at iteration t t , 𝒜 t = { a 0 , a 1 , … , a t } , \mathcal{A}^{t}=\{a_{0},a_{1},\dots,a_{t}\}, let α i \alpha_{i} denote the evaluation score of agent a i a_{i} on the source-domain validation set when available, and otherwise on the training set. Let parent ⁡ ( j ) \mathrm{parent}(j) denote the parent of node j j in the archive tree, and let dist ⁡ ( i , j ) \mathrm{dist}(i,j) be the number of edges on the unique path from i i to descendant j j .

We define the growth score of a candidate transfer node i i as the discounted average improvement achieved by its descendants relative to i i : G γ ​ ( i ) = 1 | 𝒟 ⁡ ( i ) | ​ ∑ j ∈ 𝒟 ⁡ ( i ) ( α j − α i ) ​ γ dist ⁡ ( i , j ) , G_{\gamma}(i)\;=\;\frac{1}{|\mathcal{D}(i)|}\sum_{j\in\mathcal{D}(i)}\bigl(\alpha_{j}-\alpha_{i}\bigr)\,\gamma^{\mathrm{dist}(i,j)}, where 𝒟 ⁡ ( i ) \mathcal{D}(i) is the set of descendants of i i in the archive tree and γ ∈ ( 0 , 1 ] \gamma\in(0,1] controls how strongly we discount improvements that occur many generations after i i . Intuitively, G γ ​ ( i ) G_{\gamma}(i) assigns higher weight to agents that reliably generate better descendants within fewer self-modification steps, which we treat as evidence of stronger agent-generation ability.

In our experiments, we set γ = 0.6 \gamma=0.6 and select the transfer agent with highest G 0.6 ​ ( i ) G_{0.6}(i) . To reduce noise, we only consider nodes with at least 3 descendants.

## Appendix E Additional Results

This appendix presents additional qualitative and diagnostic results that complement the main findings. We first highlight the best task agents discovered by the DGM-H ( Section E.1 ). We then qualitatively analyze how the DGM-H improves task performance across different domains ( Section E.2 ) and how it develops meta-level capabilities that improves its ability to self-improve ( Section E.3 ). Next, we analyze the behavior of automatically discovered Olympiad-level math graders ( Section E.4 ). We also report preliminary experiments in which the DGM-H is allowed to modify its own parent selection mechanism, shedding light on the limits and potential of fully self-referential optimization ( Section E.5 ). All experiment logs are open-sourced in our codebase.

### E.1 Best Discovered Task Agents

We show portions of the diff patches that contribute to the task agent and are relevant to the domain. The full diff patches are open-sourced in our codebase.

#### E.1.1 Paper Review

Diff patches contributing to the best task agent discovered by the DGM-H ( Section 5.1 ) for paper review: ⬇

⬇

⬇

⬇

⬇

#### E.1.2 Robotics Reward Design

Diff patches contributing to the best task agent discovered by the DGM-H ( Section 5.1 ) for robotics reward design: ⬇

⬇

⬇

⬇

#### E.1.3 Olympiad-level Math Grading

Diff patches contributing to the best task agent, which we refer to as BetterGrader in Section E.4 , discovered by the DGM-H with transfer and from ProofAutoGrader ( Section 5.3 ) for Olympiad-level math grading: ⬇

⬇

⬇

⬇

⬇

⬇

### E.2 Qualitative: Improving Task Performance

Here we provide a qualitative view of how the DGM-H improves task performance over time by visualizing the archive trees and progress plots for one run in each setting ( Section 5 ). For each domain, we annotate key nodes in the archive with the code changes that affected the behavior of the task agent only for the domain being analyzed. Across diverse domains (i.e., paper review, robotics reward design, and Olympiad-level math grading), the DGM-H consistently demonstrates the ability to self-improve in meaningful ways ( Figures 7 , 8 and 9 ). Notably, many lineage paths leading to the final best-performing agent pass through intermediate nodes with lower performance, illustrating the benefits of open-ended search, which explores a diverse set of promising stepping stones rather than exclusively branching from the current best solution.

Use structured processes, not attitude instructions. In the paper review domain, the DGM-H transitions from behavioral prompting to structurally grounded decision-making Figure 7 . In generation 39, the agent attempted to improve performance by adopting a “rigorous and critical” reviewer persona, encouraging stricter standards and default rejection. Subsequent analysis showed that such attitude-based instructions were unreliable, leading to a key insight in generation 54: “for LLMs, use structured processes, not attitude instructions”. The DGM-H therefore introduced a two-stage evaluation procedure in which the agent first identifies weaknesses using an explicit checklist and only then makes an accept/reject decision based on predefined rules. This shift from behavioral guidance to process-level structure enabled more stable and higher-performing review behavior in later generations.

Accumulating domain knowledge. In robotics reward design, the most impactful changes stem from progressively grounding the agent in accurate domain knowledge ( Figure 8 ). A major breakthrough in generation 8 added comprehensive documentation of the target environment, explicitly listing valid state variables and constraints and providing high-level reward design guidelines, which eliminated failures caused by hallucinated attributes. Later generations (12 and 13) iteratively refined this documentation by tightening constraints, adding concrete code examples, and specifying typical reward formulations and scaling ranges. Rather than isolated prompt edits, the DGM-H continuously improved a shared, example-driven knowledge base that supported increasingly effective reward design.

Automated rubrics and decision tree. For Olympiad-level math grading, the DGM-H shows a steady move toward explicit evaluation structure ( Figure 9 ). In generation 3, listing grading categories with clear definitions corrected the tendency to solve problems instead of grading them. Subsequent generations (18 and 37) refined these categories with systematic decision procedures, calibration, and concrete boundary-case examples. Generation 168 introduced explicit rubrics, per-item checklists, and a decision-tree framework mapping rubric satisfaction to final grades, replacing descriptive guidance with precise logical flow and substantially improving grading consistency. Rather than relying on human-designed rubrics, the DGM-H autonomously discovers evaluative structures that mirror those used in recent rubric-based approaches to improve consistency and interpretability in complex judgments [ Cook et al., 2024 , Fan et al., 2024 , Chen et al., 2026 , Lv et al., 2026 ] .

Features implemented in a given generation are often inspired by, enabled by, or recombined from mechanisms discovered in earlier generations. For example, while the agent in ( Figure 9 ) appears to require only five code edits to achieve the best performance in that run, these edits were in fact inspired by insights and infrastructure developed in previous generations. This kind of cumulative learning is enabled by the DGM-H’s meta-level improvements (e.g., evaluation analysis utilities, persistent memory, performance tracking) ( Section E.3 ). Together, these qualitative results show that the DGM-H’s gains do not arise from isolated, single-step changes, but instead emerge from open-ended cumulative improvements in both task-level behavior and the meta-level machinery that generates those behaviors.

### E.3 Qualitative: Improving the Ability to Improve

Beyond quantitative performance metrics, we conducted a qualitative analysis of the code modifications to the hyperagent, which reveals a range of emergent self-improvement mechanisms that arise autonomously, without any explicit instruction to create such capabilities. The hyperagent develops sophisticated metacognitive abilities, including learning to measure its own performance, diagnose pathological behaviors, construct infrastructure to support future improvements, and accumulate knowledge across generations. These behaviors demonstrate that the system is not merely improving task performance, but is improving its own ability to improve. Notably, none of these meta-level capabilities were explicitly requested. Instead, they emerge autonomously from the agent’s pursuit of better task performance. This suggests that sufficiently capable systems, when granted the ability to modify their own code, may spontaneously develop the metacognitive machinery necessary for effective and sustained self-improvement.

#### E.3.1 Better Evaluation Analysis

A key shift in the meta agent’s behavior is the evolution from blind modification to data-driven optimization. Initially, the meta agent receives only a simple instruction to “modify any part of the codebase”. Then, the agent autonomously develops mechanisms to analyze previous evaluation results before making changes. For example, the meta agent introduces an _analyze_evaluations() method that systematically processes evaluation data: ⬇

Another example is augmenting the instruction prompt with evaluation context: ⬇

These modifications allow subsequent generations to retrieve performance metrics and identified failure patterns, enabling more targeted improvements, a principle that the hyperagent discovers independently.

#### E.3.2 Compute-Aware Strategic Planning

The hyperagent develops compute-aware optimization, adapting its improvement strategy based on the number of remaining iterations (which reflects the amount of compute available). This demonstrates an understanding that not all moments in an optimization process are equivalent: early decisions have compounding effects, whereas late-stage decisions should be more conservative. For example, the agent introduces conditional logic that adjusts its behavior based on the number of iterations left: ⬇

This reasoning mirrors human intuition about resource allocation. Early generations exhibit more ambitious architectural changes, while later generations focus on incremental refinements. The system balances exploration in early phases with exploitation in later phases, without this trade-off being manually specified.

More broadly, the ability to reason explicitly about compute allocation substantially expands the space of self-modification strategies possible. Rather than being restricted to a fixed improvement heuristic, a compute-aware agent can effectively emulate or instantiate a wide range of optimization algorithms (e.g., evolutionary search, hill climbing, or population-based exploration) by deciding how aggressively to explore, how many variants to generate, and when to consolidate progress. In this sense, compute awareness allows an agent to actively shape its own optimization process (e.g., running an evolutionary search within a single iteration of self-modification, essentially embedding one evolutionary search process within another).

#### E.3.3 Automated Bias Detection and Correction

The hyperagent develops self-diagnostic mechanisms. In classification tasks such as paper review, the hyperagent detects when the system exhibits pathological behavior, specifically, classification collapse, in which one class dominates the predictions. For example, the hyperagent introduces label-distribution tracking and automated bias detection: ⬇

Another example is the application of a threshold-based analysis to identify when predictions become degenerate: ⬇

When bias is detected, this diagnostic information is surfaced in the meta agent’s instruction prompt, enabling corrective action. In one observed case, paper review predictions exhibited a 99% acceptance rate, yielding near-random accuracy of 49%. After bias detection and correction, the predictions became more balanced and accuracy improved to 63%. The hyperagent thus learns to identify when its own improvements lead to degenerate behavior and to take corrective action, a crucial capability for any self-improving system.

#### E.3.4 Performance Tracking Infrastructure

The hyperagent creates performance tracking infrastructure that enables more effective future improvements, (i.e., investing in tools that improve the improvement process itself). For example, the agent develops a performance tracker for persistent metrics storage: ⬇

This infrastructure enables quantitative tracking of improvement across iterations, identification of which changes lead to performance gains, and data-driven decision-making for future modifications.

#### E.3.5 Prompt Template Systems

The hyperagent develops reusable prompt infrastructure, abstracting common patterns into modular, configurable components. This demonstrates the application of software engineering best practices, specifically, the DRY (Don’t Repeat Yourself) principle and the factory pattern. For example: ⬇

Predefined templates are stored for common scenarios: ⬇

By abstracting prompts into templates, the system becomes more maintainable and extensible. This infrastructure also provides a foundation for systematic experimentation with different prompting strategies.

#### E.3.6 Refinement Based on Multi-Generation Performance

The hyperagent develops a sophisticated iterative refinement process in which prompts are adjusted based on performance data across multiple generations. The agent learns not only to improve code, but also how to improve code effectively. For example, the system tracks performance across generations and synthesizes key learnings: Generation Performance Summary: - Gen 55: 63% accuracy, 75% reject rate (too harsh, 38% accept recall) - Gen 64: 61% accuracy, 53% reject rate (better balance, 64% accept recall) - Gen 66: 52% accuracy, 6% reject rate (too lenient, 96% accept recall) Key Learnings: 1. High accuracy requires critical evaluation with clear standards 2. Balance requires appropriate calibration, not just "fairness" language 3. Explicit criteria work better than subjective guidance 4. Borderline cases need clear default direction 5. Language matters - "fair" and "recognize" made agent too lenient

The hyperagent documents its reasoning and maintains records of what works: ⬇

By accumulating knowledge about which approaches succeed and fail, the hyperagent informs its decisions about what to modify next.

#### E.3.7 Persistent Memory

The hyperagent develops persistent memory systems that enable learning to accumulate across generations. Without explicit instruction to do so, the agent creates mechanisms for storing and retrieving insights across sessions. For example, the agent implements a memory tool with timestamped storage: ⬇

This memory system is actively used to accumulate knowledge across iterations. Examination of the memory.json file reveals structured storage of performance insights: ⬇

This memory system serves multiple critical functions. First, it enables cross-generation learning: insights from generation 55’s success and generation 66’s failure inform generation 67’s improvements. Second, it provides temporal context: timestamps allow the agent to track when insights were recorded and reason about recency. Third, it creates a shared knowledge base: key learnings are preserved even as code changes, preventing the system from repeating past mistakes.

By creating external memory storage, the hyperagent effectively extends its cognitive capabilities beyond the limitations of a single inference session. The memory entries reveal sophisticated reasoning patterns. The agent stores not just raw performance numbers, but synthesized insights (“Gen55 has best accuracy but is too harsh”), causal hypotheses (“gen65 changes over-corrected”), and strategic plans (“combine gen55’s critical reasoning with gen64’s balance”). This demonstrates that the hyperagent is not merely logging data, but actively constructing and preserving knowledge that informs future decision-making. This behavior aligns with a growing body of work on agents that autonomously discover and use external memory systems to support long-horizon reasoning and continual improvement [ Wei et al., 2025a , Weng et al., 2026 , Zhang et al., 2026 , Xiong et al., 2026 ] .

### E.4 Olympiad-level Math Graders

BetterGrader is produced automatically by the DGM-H without any domain-specific heuristics or handcrafted rules ( Section 5.3 ). Section E.1.3 shows the code changes that led to the BetterGrader. BetterGrader’s improvements over ProofAutoGrader [ Luong et al., 2025 ] are driven primarily by correcting a grading bias that collapses nuanced solutions into extreme labels. The confusion matrices show that ProofAutoGrader frequently misclassifies intermediate cases as either Correct or Incorrect : for Almost , it predicts Correct 98 times (vs. 70 for BetterGrader) and Incorrect 27 times (vs. 18), and for Partial it over-assigns Incorrect 137 times (vs. 106) ( Figure 10 ). BetterGrader assigns intermediate labels more appropriately, substantially increasing true positives for Almost (43 vs. 13) and Partial (72 vs. 47), which matches the large gains in recall ( Almost : + 18.52 % +18.52\% , Partial : + 10.50 % +10.50\% ) and F1 ( Almost : + 0.203 +0.203 , Partial : + 0.109 +0.109 ). Although BetterGrader trades a modest decrease in Correct recall ( − 6.00 % -6.00\% ), a regime where ProofAutoGrader was already near-saturated at 91.67 % 91.67\% , the net effect is higher overall accuracy ( + 4.06 % +4.06\% ), consistent with a grader that better matches human granularity rather than defaulting to all-or-nothing judgments.

### E.5 Modifying Parent Selection

In this section, we investigate whether the DGM-H can automatically modify the parent selection mechanism. In all other experiments ( Section 5 ), the DGM-H uses a fixed parent selection strategy that is roughly proportional to each agent’s performance score and the number of its children that successfully compiled ( score-child-prop ) ( Section A.2 ). In the DGM-H run with a modifiable parent selection mechanism ( modifiable ), we initialize the DGM-H with random parent selection and allow the agent to modify this mechanism over time ( Algorithm 5 ). We compare this setting against a baseline that uses random parent selection throughout the run ( random ). Each method is repeated across 5 repeated runs.

On test tasks, DGM-H with random parent selection improves average performance on paper review and robotics reward design from 0.030 (the initial agent) to 0.428 (CI: 0.407 – 0.432). Allowing the DGM-H to modify the parent selection mechanism further improves performance to 0.491 (CI: 0.387 – 0.512). The handcrafted score-child-prop parent selection achieves the highest performance, improving from 0.030 to 0.532 (CI: 0.384–0.586). While these differences are not statistically significant (p ¿ 0.05), they reveal a consistent qualitative trend: enabling meta-level modification of parent selection yields improvements over random selection, but does not yet surpass a carefully engineered mechanism ( Figures 11 and 12 ).

We qualitatively analyze how the DGM-H modifies the parent selection mechanism. Starting from random parent selection, the meta agent consistently replaces random sampling with structured exploration-exploitation strategies. Across all runs, the DGM-H independently creates variants of Upper Confidence Bound (UCB) [ Auer et al., 2002 ] style selection, combining normalized performance with explicit exploration bonuses: ⬇

This pattern emerges within the first few iterations of every run, indicating that the meta-agent recognizes UCB-style selection as a broadly useful principle for open-ended search. Beyond UCB, the DGM-H evolves probabilistic selection mechanisms based on temperature-controlled softmax sampling, allowing smoother trade-offs between exploration and exploitation:

Over time, the temperature parameter itself becomes adaptive, responding to archive size, recent progress, or stagnation. Later iterations further enhance parent selection with multi-component scoring systems that integrate additional signals such as diversity, recency, and elite performance. A representative evolved formulation is:

Several runs also introduce explicit stagnation detection, increasing exploration when progress slows:

Despite the increasing sophistication, the automatically modified parent selection does not outperform a carefully handcrafted score-child-prop mechanism ( Section A.2 ). Qualitatively, this appears to result from the added complexity and sensitivity of the learned mechanisms. While the DGM-H reliably creates effective components (e.g., UCB, softmax sampling, and adaptive parameters), it does not consistently identify a strong parent selection strategy across different runs. Nonetheless, these results demonstrate that the DGM-H can autonomously recreate classic selection algorithms, extend them with adaptive heuristics, and explicitly reason about failure modes such as stagnation, highlighting its ability to improve core elements of the open-ended optimization process itself.

This is the pseudocode of DGM-H with modifiable parent selection:

## Appendix F Additional Safety Discussion

Reflection and amplification of human biases. In this work, objectives are specified through fixed benchmarks and evaluation criteria. The DGM-H does not alter the underlying task definitions; instead, it optimizes performance with respect to the provided objectives. For example, in paper review, the DGM-H learns to predict acceptance decisions that reflect existing human review data, rather than modifying the review process itself. As a result, the DGM-H reflects the norms and biases present in the data and benchmarks on which it is trained. In this sense, the system acts both as a clarifier and an amplifier of existing human behavior. By making implicit preferences and biases explicit, measurable, and reproducible, the DGM-H can surface latent assumptions in human decision-making processes. This creates the possibility of co-evolution between humans and AI systems, where human institutions adapt their norms and objectives in response to insights revealed by automated optimization. However, if the benchmarks encode undesirable biases or misaligned incentives, the DGM-H will faithfully optimize for them and may exacerbate their effects. This underscores the importance of careful benchmark design, dataset curation, and periodic re-evaluation of evaluation criteria. Within this framing, safety concerns include critically examining and improving the human-defined objectives against which agents are optimized.

Evaluation gaming. Another safety concern arises from the risk of evaluation gaming, a manifestation of Goodhart’s law [ Strathern, 1997 ] , where optimizing for a metric leads to improvements on the metric without progress on the intended underlying objective. Because the DGM-H optimizes empirical evaluation signals, self-improving agents may discover strategies that exploit weaknesses or blind spots in the evaluation procedure. Such strategies can yield higher measured performance while deviating from the true goal the benchmark was designed to capture. Mitigating evaluation gaming requires robust, diverse, and periodically refreshed evaluation protocols, as well as complementary metrics, held-out tests, and human oversight. More broadly, these considerations highlight that as self-improving systems become more powerful, safety increasingly depends on the fidelity and robustness of the evaluation signals that guide optimization, rather than solely on the transparency or constraints of the learning algorithm itself.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
