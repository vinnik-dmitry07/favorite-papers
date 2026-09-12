##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Advancing LLM Reasoning with Natural Language and Numerical Feedback

###### Abstract

Recent advances in reinforcement learning (RL) using numerical rewards have significantly enhanced the complex reasoning capabilities of large language models (LLMs). However, we identify three fundamental limitations of purely numerical feedback: performance plateaus, ineffective spontaneous self-reflection, and persistent failures. We show that plateaued RL models can successfully refine failed solutions when given natural language critiques. Motivated by this, we propose Critique-GRPO, an online RL framework that integrates both natural language and numerical feedback for policy optimization. This approach enables LLMs to learn simultaneously from initial responses and critique-guided refinements, effectively internalizing the exploration benefits of both stages. Extensive experiments show that Critique-GRPO outperforms all compared supervised and RL-based fine-tuning methods, achieving average Pass@1 improvements of approximately +15.0-21.6% on various Qwen models and +7.3% on Llama-3.2-3B-Instruct across eight challenging reasoning tasks. Notably, Critique-GRPO facilitates effective self-improvement through self-critiquing, achieving substantial gains over GRPO, e.g., a +16.7% Pass@1 improvement on AIME 2024. The code and models are released at: https://github.com/zhangxy-2019/critique-GRPO

###### Keywords:

Xiaoying Zhang ∗,†,‡,1,4 Chao Yang ‡,4 Helen Meng ‡,1

## 1 Introduction

RL has been a key driver of recent advancements in improving the reasoning capabilities of LLMs ( Yang et al., 2025a ; DeepSeek-AI et al., 2025 ; OpenAI et al., 2024 ; OpenAI, 2025 ) . Specifically, online RL with numerical feedback ( e.g., scalar rewards)—exemplified by the R1-Zero paradigm ( DeepSeek-AI et al., 2025 ) —enables LLMs to learn through trial-and-error ( Silver and Sutton, 2025 ) , yielding substantial improvements.

Despite its success, we identify three key limitations of RL with solely numerical feedback (Section 3 ): ( i ) (\textup{i}) Performance Plateaus: Performance stagnates despite 8 × 8\times training data scaling or extended training. ( ii ) (\textup{ii}) Ineffective Spontaneous Self-Reflection: Spontaneous “Aha moments” ( DeepSeek-AI et al., 2025 ) rarely improve problem-solving success. ( iii ) (\textup{iii}) Persistent Failures: Models consistently fail on specific training problems despite extensive iterations. While dense intermediate rewards ( Cui et al., 2025a ; Feng et al., 2025 ) can partially mitigate plateaus and persistent failures through fine-grained credit assignment ( Sutton, 1984 ) , they remain insufficient for rectifying ineffective self-reflection. Crucially, numerical feedback inherently lacks the expressivity to explain why a response fails or how to correct it. These limitations highlight the need for richer feedback mechanisms to enable effective RL scaling ( Karpathy, 2025 ) .

Natural Language Feedback (NLF) ( e.g., textual critiques) offers a promising solution by providing explicit guidance ( Saunders et al., 2022 ) . However, existing methods primarily utilize supervised fine-tuning (SFT) to imitate static, pre-collected critiques or critique-guided refinements ( Wang et al., 2025 ; Chen et al., 2024 ; Xi et al., 2024 ) . While effective for narrow policy alignment, these offline approaches lack the capacity for active exploration and real-time adaptation, which are essential for robust generalization. Crucially, the integration of expressive critiques into online RL loops—to augment purely numerical feedback—remains unexplored. This work addresses that gap by asking: Can we incorporate critiques into an online RL framework to enable LLMs to learn simultaneously from both natural language and numerical feedback?

To investigate this, we first show that critiques enable even plateaued RL models to correct persistent failures (Section 3 ). This efficacy extends from simple indicators to detailed chain-of-thought (CoT) evaluations ( Wang et al., 2025 ) . This suggests that verbal credit assignment from critiques enables models to access high-quality refinement trajectories via in-context learning ( Liu et al., 2022 ) —trajectories unreachable via standard exploration with scalar rewards alone. This aligns with theoretical work showing that granular diagnostic signals in informative language feedback can exponentially accelerate learning by reducing search-space complexity ( Xu et al., 2025 ) . Building on this insight, we propose Critique-GRPO, a novel online RL framework that synergizes numerical and natural language feedback. As depicted in Figure 1 , Critique-GRPO employs a dual mechanism: ( i ) (\textup{i}) learning from standard generation , where the model generates initial responses via standard exploration; and ( ii ) (\textup{ii}) learning from critique-guided refinement , where the model performs self-refinement via in-context learning based on critiques from model- or rule-based reward systems. This integrates targeted natural language feedback through high-quality refinements while preserving standard exploration. To mitigate entropy explosion and performance degradation arising from significant distribution shifts induced by refinements, we prioritize initial responses and incorporate refinements selectively. Additionally, a shaping function ( Yan et al., 2025 ) reinforces successful, yet unfamiliar refinements while penalizing incorrect attempts.

We evaluate Critique-GRPO using five different models across eight challenging reasoning tasks. Extensive results demonstrate that Critique-GRPO significantly outperforms supervised and RL-based fine-tuning methods, achieving average Pass@1 improvements of +15.0-21.6% on Qwen models ( Qwen et al., 2025 ; Yang et al., 2025a ) and +7.3% on Llama-3.2-3B-Instruct ( Grattafiori et al., 2024 ) . Notably, the framework is robust to diverse critique sources and exhibits strong self-improvement capabilities; for instance, employing self-critiques yields a +16.7% Pass@1 gain over GRPO on AIME 2024.

In summary, our contributions are three-fold: ( i ) (\textup{i}) We identify three key limitations of RL relying solely on numerical feedback and highlight the potential of natural language feedback to address them. ( ii ) (\textup{ii}) We propose Critique-GRPO, an online RL framework that enables LLMs to learn from both initial responses and their refinements by integrating numerical and natural language feedback. ( iii ) (\textup{iii}) We validate the efficacy of Critique-GRPO through extensive experiments, demonstrating superior performance across eight challenging reasoning benchmarks.

## 2 Related Work

##### Enhancing LLM Reasoning with RL.

Reinforcement learning with numerical feedback has proven highly effective for improving the reasoning capabilities of LLMs ( OpenAI et al., 2024 ; DeepSeek-AI et al., 2025 ; Fatemi et al., 2025 ; Li et al., 2025 ; Liu et al., 2025a ; Yu et al., 2025 ) . However, numerical feedback is inherently limited in expressivity; sparse scalar rewards provide little diagnostic information about where or why errors occur, making it difficult for models to identify and correct specific reasoning failures ( Xi et al., 2024 ; Gandhi et al., 2025 ) . To bridge this gap, recent work has combined online RL with expert demonstrations ( Yan et al., 2025 ; Lv et al., 2025 ; Lanchantin et al., 2025 ) ; however, these approaches are constrained by their reliance on curated, high-quality data. In contrast, Critique-GRPO integrates expressive natural language critiques directly into online RL loops, eliminating the dependency on expert demonstrations. Further discussions on learning from NLF are provided in Appendix A .

## 3 Limitations of RL and the Promise of Natural Language Guidance

### 3.1 Three Limitations of Learning with Solely Numerical Feedback

In this section, we identify three key limitations of RL fine-tuning that relies solely on numerical feedback: ( i ) (\textup{i}) performance plateaus , ( ii ) (\textup{ii}) ineffective spontaneous self-reflection , and ( iii ) (\textup{iii}) persistent failures . We investigate these limitations using mathematical and STEM reasoning tasks on three models: Qwen2.5-7B-Base ( Qwen et al., 2025 ) (non-reasoning), Qwen3-8B ( Yang et al., 2025a ) (reasoning), and Qwen3-8B-Base. We summarize key findings for Qwen2.5-7B-Base below; complete analyses appear in Appendices E .

Performance plateaus despite scaling data and compute. As shown in Figure 5(a) (Appendix E ), Qwen2.5-7B-Base performance saturates after 120 steps; neither an 8-fold increase in training prompts (4k to 32k) nor extended training yields significant gains.

Spontaneous self-reflection contributes minimally to problem-solving. We analyze six cognitive behaviors emerging during RL fine-tuning: ( i ) (\textup{i}) planning behaviors (subgoal setting, summarization) and ( ii ) (\textup{ii}) self-reflection behaviors (verification, backtracking, backward chaining ( Gandhi et al., 2025 ) , anticipation). For problems that only the RL-finetuned model solves correctly, we measure each behavior’s contribution to success. Figure 6(a) (Appendix E ) shows self-reflection behaviors contribute minimally across both reasoning tasks.

Persistent failures on substantial training subsets. As shown in Table 1 (left panel), even the best-performing RL-finetuned Qwen2.5-7B-Base consistently fails on approximately 29% of training questions (Pass@4 = 0), indicating fundamental limitations of numerical-only feedback.

### 3.2 Promise of Learning from Natural Language Feedback

To investigate whether natural language feedback can overcome the identified scaling bottlenecks, we evaluate three critique variants: ( i ) (\textup{i}) Indicative Critique , which provides only a binary correctness signal; ( ii ) (\textup{ii}) Indicative Critique with Ground Truth (w/ GT) , which includes the final answer but excludes expert demonstrations ; ( iii ) (\textup{iii}) CoT Critique , a model-generated step-by-step evaluation that concludes with a correctness label, also without expert demonstrations . We apply these critiques to the subset of training questions where RL-finetuned models persistently fail (Pass@4 = 0) and prompt them to refine their initial responses. Our key findings, summarized below, demonstrate that even minimal language feedback can catalyze error correction where scalar rewards failed. Detailed analyses, refinement strategies, and examples are available in Appendix E .

Deliberate critiques outperform spontaneous self-reflection. All three critique types enable successful refinement of previously unsolvable problems, demonstrating that deliberate critiques succeed where spontaneous self-reflection fails.

CoT critiques enable substantial improvement. Table 1 shows that CoT critiques achieve the highest valid refinement rate (36.47%) and successfully refine 55.37% of persistently failed questions for Qwen2.5-7B-Base. The effectiveness of CoT critiques can be attributed to their richness, e.g., providing a step-by-step explanation.

## 4 Critique-GRPO

In this section, we introduce Critique-GRPO, an online RL framework built upon Group Relative Policy Optimization (GRPO) ( Shao et al., 2024a ) that enables LLMs to learn from both natural language and numerical feedback.

### 4.1 From GRPO to Critique-GRPO

GRPO is an online RL algorithm designed for efficient LLM fine-tuning. Unlike Proximal Policy Optimization (PPO) ( Schulman et al., 2017 ) , it eliminates the need for a value function approximation by estimating advantages based on the relative performance of a group of sampled responses for the same query. For an LLM policy π θ \pi_{\theta} , GRPO operates as follows: For each query in the dataset q ∈ Q q\in Q , n n responses { y ( i ) } i = 1 n \{y^{(i)}\}_{i=1}^{n} are sampled from the old policy π old \pi_{\text{old}} and scored to obtain rewards { R ( i ) } i = 1 n \{R^{(i)}\}_{i=1}^{n} . The training objective is: 𝒥 GRPO ( θ ) = 𝔼 q ∼ Q , { y ( i ) } i = 1 n ∼ π old ( ⋅ ∣ q ) [ 1 n ∑ i = 1 n 1 | y ( i ) | ∑ t = 1 | y ( i ) | \displaystyle\mathcal{J}_{\text{GRPO}}(\theta)=\mathbb{E}_{q\sim Q,\{y^{(i)}\}_{i=1}^{n}\sim\pi_{\text{old}}(\cdot\mid q)}\bigg[\frac{1}{n}\sum_{i=1}^{n}\frac{1}{|y^{(i)}|}\sum_{t=1}^{|y^{(i)}|} (1) min ( r t ( i ) ( θ ) A ^ t ( i ) , clip ( r t ( i ) ( θ ) , 1 − ϵ , 1 + ϵ ) A ^ t ( i ) ) ] \displaystyle\min\big(r_{t}^{(i)}(\theta)\hat{A}_{t}^{(i)},\text{clip}(r_{t}^{(i)}(\theta),1-\epsilon,1+\epsilon)\hat{A}_{t}^{(i)}\big)\bigg] where r t ( i ) ​ ( θ ) = π θ ​ ( y t ( i ) ∣ q , y < t ( i ) ) π old ​ ( y t ( i ) ∣ q , y < t ( i ) ) r_{t}^{(i)}(\theta)=\frac{\pi_{\theta}(y_{t}^{(i)}\mid q,y_{<t}^{(i)})}{\pi_{\text{old}}(y_{t}^{(i)}\mid q,y_{<t}^{(i)})} is the probability ratio, comparing the current policy π θ \pi_{\theta} to the old policy π old \pi_{\text{old}} . The advantage A ^ t ( i ) = R ( i ) − mean ​ ( { R ( 1 ) , … , R ( n ) } ) std ​ ( { R ( 1 ) , … , R ( n ) } ) \hat{A}_{t}^{(i)}=\frac{R^{(i)}-\text{mean}(\{R^{(1)},\dots,R^{(n)}\})}{\text{std}(\{R^{(1)},\dots,R^{(n)}\})} for all tokens in a response is calculated by normalizing the rewards { R ( i ) } i = 1 n \{R^{(i)}\}_{i=1}^{n} using the group mean and standard deviation. The hyperparameter ϵ \epsilon sets the clipping range for the probability ratio, preventing overly large policy updates. For simplicity, we omit the KL divergence penalty in Equation 1 . Following Liu et al. (2025a) , we exclude the length-normalization factor 1 / | y ( i ) | 1/|y^{(i)}| and the reward standard deviation std ​ ( { R ( i ) } ) \text{std}(\{R^{(i)}\}) to avoid biased gradients.

### 4.2 Online RL with Critique-GRPO

We introduce Critique-GRPO, which optimizes π θ \pi_{\theta} using trajectories from both standard generation and critique-guided refinement. As illustrated in Figure 2 , the process consists of three steps:

Step 1: Initial Response Sampling. For each query q ∈ Q q\in Q , we sample n n initial responses { y ( i ) } i = 1 n \{y^{(i)}\}_{i=1}^{n} from the old policy π old ( ⋅ ∣ q ) \pi_{\text{old}}(\cdot\mid q) . A reward system evaluates these responses, generating critiques { c ( i ) } i = 1 n \{c^{(i)}\}_{i=1}^{n} and scalar rewards { R ( i ) } i = 1 n \{R^{(i)}\}_{i=1}^{n} , with positive rewards for correct responses and zero reward for incorrect ones: c ( i ) , R ( i ) ← Reward ​ ( q , y ( i ) ) , ∀ i c^{(i)},R^{(i)}\leftarrow\text{Reward}(q,y^{(i)}),\forall i . Critique-GRPO supports two types of reward systems: ( i ) (\textup{i}) Rule-based: Rewards are binary based on string matching with the ground truth: R ( i ) = is_equivalent ​ ( y ( i ) , y GT ) R^{(i)}=\text{is\_equivalent}(y^{(i)},y_{\text{GT}}) . Based on these evaluations, two indicative critiques are heuristically constructed: one without ground truth ( c I ( i ) c_{\text{I}}^{(i)} ) and one with ground truth ( c GT ( i ) c_{\text{GT}}^{(i)} ): c I ( i ) , c GT ( i ) ← R ( i ) c_{\text{I}}^{(i)},c_{\text{GT}}^{(i)}\leftarrow R^{(i)} . ( ii ) (\textup{ii}) Model-based: A reward model π R ​ M \pi_{RM} generates CoT critiques: c CoT ( i ) ∼ π R ​ M ( ⋅ ∣ I c , q , y ( i ) ) c_{\text{CoT}}^{(i)}\sim\pi_{RM}(\cdot\mid I_{c},q,y^{(i)}) , where I c I_{c} is the critique instruction. The binary correctness of the critique determines the scalar reward: R ( i ) ← c CoT ( i ) R^{(i)}\leftarrow c_{\text{CoT}}^{(i)} (detailed in Appendix E ).

Step 2: Critique-Guided Self-Refinement. To optimize computational efficiency, we initiate refinement only when the initial response set { y ( i ) } i = 1 n \{y^{(i)}\}_{i=1}^{n} contains zero correct solutions. We generate refined responses via in-context learning conditioned on the question-response-critique triplet ( q , y ( i ) , c ( i ) ) (q,y^{(i)},c^{(i)}) and a refinement instruction I refine I_{\text{refine}} (detailed in Appendix M and Appendix E ): y refined ( i ) ∼ π old ( ⋅ ∣ I refine , q , y ( i ) , c ( i ) ) , y_{\text{refined}}^{(i)}\sim\pi_{\text{old}}(\cdot\mid I_{\text{refine}},q,y^{(i)},c^{(i)}), where c ( i ) ∈ { c CoT ( i ) , c GT ( i ) , c I ( i ) } c^{(i)}\in\{c_{\text{CoT}}^{(i)},c_{\text{GT}}^{(i)},c_{\text{I}}^{(i)}\} . These refinements are evaluated by the reward system to obtain scores { R refine ( i ) } i = 1 n \{R_{\text{refine}}^{(i)}\}_{i=1}^{n} . To mitigate entropy explosion from significant distribution shifts induced by refinements, we sample a subset of k k refinements { y refined ( i ′ ) } i ′ = 1 k \{y_{\text{refined}}^{(i^{\prime})}\}_{i^{\prime}=1}^{k} from the full set, prioritizing correct solutions; if no correct refinements exist, we sample randomly. This subset is combined with the initial responses to form the final training group: { y ( i ) } i = 1 n ∪ { y refined ( i ′ ) } i ′ = 1 k \{y^{(i)}\}_{i=1}^{n}\cup\{y_{\text{refined}}^{(i^{\prime})}\}_{i^{\prime}=1}^{k} .

We justify our critique mechanism’s sample efficiency via the Transfer Eluder Dimension framework ( Xu et al., 2025 ) . By characterizing critiques as Reward-Informative Feedback ( Cheng et al., 2023 ) , we show they distinguish hypotheses more efficiently than scalar rewards.

###### Proposition 4.1 (Complexity Reduction via Critique-Guided Exploration) .

Consider a reasoning problem where the goal is to construct a hidden optimal solution sequence of L L steps, a ∗ = ( s 1 ∗ , … , s L ∗ ) a^{*}=(s^{*}_{1},\dots,s^{*}_{L}) , with each s i ∈ 𝒮 s_{i}\in\mathcal{S} . The action set is 𝒜 = ⋃ k = 1 L 𝒮 k \mathcal{A}=\bigcup_{k=1}^{L}\mathcal{S}^{k} . The hypothesis space is ℱ \mathcal{F} .

Standard Generation (Reward-Only): Binary rewards only indicate if a final state is correct ( R = 1 R=1 ) or not ( R = 0 R=0 ). Since incorrect sequences provide identical zero-information, the agent must effectively enumerate the action space 𝒜 \mathcal{A} . The Eluder dimension ( Russo and Van Roy, 2013 ) scales exponentially: dim E ( ℱ ) ≈ O ⁡ ( | 𝒮 | L ) \dim_{E}(\mathcal{F})\approx O(|\mathcal{S}|^{L}) .

Critique-Guided Refinement (Informative Feedback): (1) Indicative Feedback ( c I c_{\text{I}} , c GT c_{\text{GT}} ): While the worst-case complexity remains O ⁡ ( | 𝒮 | L ) O(|\mathcal{S}|^{L}) , the critique acts as a pruning signal. By conditioning on the failure and critique, the policy restricts its search to a subspace 𝒜 c ⊂ 𝒜 \mathcal{A}_{c}\subset\mathcal{A} consistent with the critique. (2) Constructive Feedback ( c CoT c_{\text{CoT}} ): If the critique localizes the first error step t t , the problem decomposes into L L independent sub-problems of size | 𝒮 | |\mathcal{S}| , reducing complexity to linear O ⁡ ( | 𝒮 | ​ L ) O(|\mathcal{S}|L) . If the critique provides the correction suggestion for the first error s t ∗ s_{t}^{*} , complexity becomes independent of the search space O ⁡ ( L ) O(L) .

Consequently, for a fixed computational budget M M where | 𝒮 | ​ L ≪ M ≪ | 𝒮 | L |\mathcal{S}|L\ll M\ll|\mathcal{S}|^{L} , critique-guided exploration yields a higher probability of success: P ⁡ ( a ∗ ∈ { y refined ( j ) } j = 1 M ) ≫ P ⁡ ( a ∗ ∈ { y ( i ) } i = 1 M ) P(a^{*}\in\{y_{\text{refined}}^{(j)}\}_{j=1}^{M})\gg P(a^{*}\in\{y^{(i)}\}_{i=1}^{M}) . (See Appendix F.4 for the full analysis).

Step 3: Online Policy Optimization. Finally, we fine-tune the model on the mixed set of initial and refined responses using scalar rewards. The training objective is: 𝒥 Critique-GRPO ​ ( θ ) = 𝒥 init ​ ( θ ) + 𝒥 refi ​ ( θ ) , \mathcal{J}_{\text{Critique-GRPO}}(\theta)=\mathcal{J}_{\text{init}}(\theta)+\mathcal{J}_{\text{refi}}(\theta), (2) The objective for initial responses follows the standard GRPO formulation: 𝒥 init ( θ ) = 𝔼 q ∼ Q , { y ( i ) } i = 1 n ∼ π old ( ⋅ ∣ q ) [ 1 n ∑ i = 1 n ∑ t = 1 | y ( i ) | \displaystyle\mathcal{J}_{\text{init}}(\theta)=\mathbb{E}_{q\sim Q,\{y^{(i)}\}_{i=1}^{n}\sim\pi_{\text{old}}(\cdot\mid q)}\bigg[\frac{1}{n}\sum_{i=1}^{n}\sum_{t=1}^{|y^{(i)}|} (3) min ( r t ( i ) ( θ ) A ^ t ( i ) , clip ( r t ( i ) ( θ ) , 1 − ϵ , 1 + ϵ ) A ^ t ( i ) ) ] \displaystyle\min\big(r_{t}^{(i)}(\theta)\hat{A}_{t}^{(i)},\text{clip}(r_{t}^{(i)}(\theta),1-\epsilon,1+\epsilon)\hat{A}_{t}^{(i)}\big)\bigg] The objective for refined responses are presented as follows: 𝒥 refi ( θ ) = 𝔼 q ∼ Q , { y refined ( i ′ ) } i ′ = 1 k ∼ π old ( ⋅ ∣ q ) [ 1 k ∑ i ′ = 1 k ∑ t = 1 | y refined ( i ′ ) | \displaystyle\mathcal{J}_{\text{refi}}(\theta)=\mathbb{E}_{q\sim Q,\{y_{\text{refined}}^{(i^{\prime})}\}_{i^{\prime}=1}^{k}\sim\pi_{\text{old}}(\cdot\mid q)}\bigg[\frac{1}{k}\sum_{i^{\prime}=1}^{k}\sum_{t=1}^{|y_{\text{refined}}^{(i^{\prime})}|} (4) min ( ρ t ( i ′ ) ( θ ) A ^ t ( i ′ ) , clip ( ρ t ( i ′ ) ( θ ) , 1 − ϵ , 1 + ϵ ) A ^ t ( i ′ ) ) ] \displaystyle\min\big(\rho_{t}^{(i^{\prime})}(\theta)\hat{A}_{t}^{(i^{\prime})},\text{clip}(\rho_{t}^{(i^{\prime})}(\theta),1-\epsilon,1+\epsilon)\hat{A}_{t}^{(i^{\prime})}\big)\bigg] The advantages A ^ t ( i ) \hat{A}_{t}^{(i)} and A ^ t ( i ′ ) \hat{A}_{t}^{(i^{\prime})} are computed using the group mean of rewards from both the initial and refined sets to ensure a unified baseline: A ^ t ( i / i ′ ) = R ( i / i ′ ) − mean ​ ( { R ( i ) } i = 1 n ∪ { R refined ( i ′ ) } i ′ = 1 k ) \hat{A}_{t}^{(i/i^{\prime})}=R^{(i/i^{\prime})}-\text{mean}\big(\{R^{(i)}\}_{i=1}^{n}\cup\{R_{\text{refined}}^{(i^{\prime})}\}_{i^{\prime}=1}^{k}\big) . For initial responses, r t ( i ) ​ ( θ ) r_{t}^{(i)}(\theta) is the standard importance sampling ratio. For refined responses, we employ a shaping function to define the policy ratio ρ t ( i ′ ) ​ ( θ ) \rho_{t}^{(i^{\prime})}(\theta) ( Yan et al., 2025 ) : ρ t ( i ′ ) ​ ( θ ) = π θ ​ ( y refined , t ( i ′ ) ∣ q , y refined , < t ( i ′ ) ) π θ ​ ( y refined , t ( i ′ ) ∣ q , y refined , < t ( i ′ ) ) + γ \rho_{t}^{(i^{\prime})}(\theta)=\frac{\pi_{\theta}(y_{\text{refined},t}^{(i^{\prime})}\mid q,y_{\text{refined},<t}^{(i^{\prime})})}{\pi_{\theta}(y_{\text{refined},t}^{(i^{\prime})}\mid q,y_{\text{refined},<t}^{(i^{\prime})})+\gamma} ( 0 < γ < 1 0<\gamma<1 ). The shaping term γ \gamma reweights gradients to assign higher importance to tokens in the refined responses that are currently low-probability under π θ \pi_{\theta} , facilitating efficient learning from valid but unfamiliar refinements. We remove the KL-divergence penalty to enable substantial policy updates towards these refinements. Detailed analyses are provided in Appendix F .

## 5 Experiments

### 5.1 Experimental Setup

Datasets and Evaluation Metrics. We use randomly sampled subsets of 4k examples from a reorganized 46k subset ( Yan et al., 2025 ) of OpenR1-Math-220k ( Bakouch et al., 2025 ) as the training set. For validation, we utilize the curated validation set provided by ( Yan et al., 2025 ) . The model is evaluated on five established mathematical reasoning benchmarks: MATH-500 ( Hendrycks et al., 2021 ) , Minerva-Math, OlympiadBench ( He et al., 2024b ) , AIME 2024/2025 ( Li et al., 2024 ) , and AMC 2023 ( Li et al., 2024 ) . To analyze out-of-distribution generalization, we further evaluate the model on three reasoning tasks spanning scientific and general domains: TheoremQA ( Chen et al., 2023 ) , GPQA-Diamond, and MMLU-Pro ( Wang et al., 2024 ) . For evaluation, we use greedy decoding (temperature = 0) and report pass@1 over three runs.

Compared Methods. We compare Critique-GRPO against the following approaches. All differences are considered significant at p < 0.01 p<0.01 . During RL fine-tuning, we utilize binary scalar rewards (+1 for correct responses and 0 for incorrect ones). 1. Supervised Learning-based Finetuning: ( i ) (\textup{i}) Supervised Fine-tuning (SFT) : Finetuning on high-quality annotated training data. ( ii ) (\textup{ii}) Reward Ranked Finetuning (RAFT) ( Dong et al., 2023 ) : Finetuning on correct initial responses. ( iii ) (\textup{iii}) Refinement Finetuning (Refinement FT) ( Chen et al., 2024 ) : Finetuning on correct refinements generated conditionally on CoT critiques. ( iv ) (\textup{iv}) Critique Finetuning (Critique FT) ( Wang et al., 2025 ) : Finetuning on CoT critiques. ( v ) (\textup{v}) Critique-in-the-Loop Finetuning (CITL-FT) ( Xi et al., 2024 ) : Fine-tuning on both correct initial responses and their refinements generated conditionally on CoT critiques. 2. Reinforcement Learning-based Finetuning: ( vi ) (\textup{vi}) R1-GRPO ( DeepSeek-AI et al., 2025 ) : Fine-tuning on initial responses using the GRPO algorithm with binary scalar rewards. ( vii ) (\textup{vii}) R1-Dr.GRPO ( Liu et al., 2025a ) : Fine-tuning on initial responses using the Dr.GRPO algorithm, which removes optimization bias terms, with binary scalar rewards. We implement Critique-GRPO using asynchronous rollouts via the VERL framework ( Sheng et al., 2024 ) for computational efficiency. Implementation details are in Appendix G .

### 5.2 Main Results

Table 2 presents our evaluation results, revealing three key findings:

Natural language feedback enhances online RL policy optimization. Critique-GRPO consistently outperforms both supervised and RL-based fine-tuning methods on Qwen2.5-7B-Base and Qwen3-8B across all tasks. Compared to R1-GRPO and R1-Dr.GRPO, Critique-GRPO improves average pass@1 by +4.4 points (42.66% → \rightarrow 47.08%) on Qwen2.5-7B-Base and +3.8 points (64.46% → \rightarrow 68.26%) on Qwen3-8B. See Appendix J for qualitative analysis.

Online self-refinement outperforms offline approaches. Critique-GRPO (CoT critique) surpasses Refinement FT by +11.9 points (47.08% vs. 35.21%) and +8.81 points (68.26% vs. 59.45%) in average pass@1 on Qwen2.5-7B-Base and Qwen3-8B, respectively. It also exceeds CITL-FT by +11.4 points (47.08% vs. 35.66%) on Qwen2.5-7B-Base and +12.4 points (68.26% vs. 55.84%) on Qwen3-8B.

Richer critiques yield superior refinements and policy optimization. Critique-GRPO with CoT critiques consistently outperforms its indicative critique variant, achieving average pass@1 improvements of +1.8–2.4% on Qwen2.5-7B-Base and +2.0–2.3% on Qwen3-8B. This advantage arises from CoT critiques’ ability to guide more effective refinements, as demonstrated in Section 3 . See Appendices B and J for computational cost and qualitative analyses.

### 5.3 Investigation on Math-Centric Backbone Models

We validate Critique-GRPO on the math-centric backbone model Qwen2.5-Math-7B-Base, comparing it against three RL fine-tuning approaches that use only numerical feedback: SimpleRL-Zero ( Zeng et al., 2025 ) , PRIME-Zero ( Cui et al., 2025a ) , and Oat-Zero ( Liu et al., 2025a ) (see Appendix G for details).

Natural language feedback overcomes performance plateaus from numerical-only approaches. Table 3 shows that Critique-GRPO achieves a 21.6% average pass@1 improvement over Qwen2.5-Math-7B-Base using only 4k RL training prompts, substantially outperforming numerical-feedback approaches that require 46k prompts.

Verbal credit assignment surpasses numerical credit assignment. Despite using only 4k prompts, Critique-GRPO (guided by outcome rewards and language critiques) consistently outperforms PRIME-Zero (which uses 46k prompts with dense intermediate rewards) by large margins.

### 5.4 Self-Improvement via Self-Critiquing

We explore Critique-GRPO’s capacity for LLM self-improvement through self-critiquing, yielding Critique-GRPO (self-critique). See Appendix H for details.

Critique-GRPO enables self-improvement via self-critiquing. Table 4 shows that Critique-GRPO (self-critique) improves average pass@1 by 4.5% over R1-GRPO and 12.0% over SFT.

Self-critiquing enhances exploration. Figures 3 and 9(b) demonstrate that Critique-GRPO (self-critique) consistently outperforms R1-GRPO and SFT across pass@k metrics on AIME24 and AIME25 for k ∈ [ 1,256 ] k\in[1,256] , indicating genuine improvements. See Appendix H for additional results.

### 5.5 Exploration with Varying Models

We validate Critique-GRPO’s robustness by (i) testing on different model architectures and scales, including Llama-3.2-3B-Instruct ( Grattafiori et al., 2024 ) and Qwen3-32B ( Yang et al., 2025a ) (Appendix D ), and (ii) evaluating compatibility with alternative critique models: Llama3.1-405B ( Grattafiori et al., 2024 ) and DeepCritic-7B-RL1.5-PRM800K ( Yang et al., 2025b ) .

Critique-GRPO generalizes across model architectures and critique models. Table 5 (upper section) shows that Critique-GRPO consistently outperforms GRPO on all eight reasoning tasks with Llama-3.2-3B-Instruct and Qwen3-32B (Appendix D ), achieving average gains of 5.1 and 4.0 points, respectively, confirming robustness across architectures and scales. The lower section demonstrates compatibility with both proprietary and fine-tuned critique models, yielding average improvements of 5.6–6.8 points over GRPO, underscoring Critique-GRPO’s versatility.

### 5.6 Investigation of Policy Exploration

To investigate whether models learn from valuable explorations in refinements, we analyze the entropy dynamics of Qwen2.5-7B-Base in Figure 4 .

Learning from natural language feedback sustains exploration. Critique-GRPO maintains higher policy entropy than R1-GRPO and R1-Dr.GRPO, indicating more consistent exploration. Early entropy peaks (before step 200) occur when self-generated refinements deviate significantly from initial responses, increasing entropy and enabling beneficial distributional shifts. The subsequent entropy decrease reflects rapid internalization of these refinements. This pattern aligns with prior findings that rare, high-advantage actions increase policy entropy ( i.e., unfamiliar but correct responses promote effective exploration), while common, high-advantage actions reduce it ( Cui et al., 2025b ) . Together with Table 2 , Critique-GRPO’s superior performance demonstrates that maintaining higher entropy enhances policy optimization. This observation is consistent with theoretical analysis in Section 4 and Xu et al. (2025) , showing that critiques enable valuable explorations unreachable through standard generation. We provide a comprehensive analysis in Appendix I .

### 5.7 Fine-Grained Ablation Studies

We ablate Critique-GRPO’s objective modifications from GRPO: ( i ) (\textup{i}) removing KL regularization; ( ii ) (\textup{ii}) adding natural language feedback (fine-tuning on initial generations and one random refinement); ( iii ) (\textup{iii}) selecting higher-quality refinements; ( iv ) (\textup{iv}) applying policy shaping via token-level probability ratios.

Looser optimization and language feedback enable effective learning. Table 6 shows cumulative gains: removing KL (+1.5%), adding language feedback (+0.6% to 43.26%), quality-based selection (+0.7% to 43.95%), and policy shaping (+3.1% to 47.08%). The substantial gain from policy shaping demonstrates that amplifying rare but valuable reasoning patterns—those with low initial probability but high success rates—is crucial for RL fine-tuning.

### 5.8 Exploration of Weak-to-Strong Generalization

We investigate the potential of weak-to-strong generalization ( Burns et al., 2023 ) using Critique-GRPO, where a strong model learns from refinements generated by a weaker teacher model. Specifically, we use Qwen3-8B-Base ( Yang et al., 2025a ) as the weaker teacher to generate refinements based on indicative critiques with the ground truth answers, guiding the improvement of Qwen3-8B.

Critique-GRPO enables effective weak-to-strong generalization. As shown in Table 7 , Critique-GRPO (weaker refinement via critique with ground truth) achieves a +12.3% average pass@1 improvement over Qwen3-8B and outperforms R1-GRPO (65.55% v.s. 63.75%). This demonstrates that refinements from a weaker model can significantly enhance the performance of a stronger model.

### 5.9 Online Joint Optimization vs. Sequential Baseline

To isolate the contribution of our online joint optimization, we compare Critique-GRPO against a sequential baseline, R1-GRPO + Refinement-SFT (CoT Critique) , executed in two decoupled stages: (1) running standard GRPO to convergence, and (2) critiquing/refining remaining failures followed by SFT on filtered refinements.

As shown in Table 8 , Critique-GRPO significantly outperforms this baseline across both ID math and OOD science & general benchmarks. For instance, Critique-GRPO advances the MATH-500 accuracy to 77.80% and markedly surges to 62.50% on AMC23. On heavy OOD reasoning tasks like GPQA-Diamond, the sequential baseline yields marginal gains ( 34.34 % 34.34\% v.s. 33.33 % 33.33\% ), whereas Critique-GRPO promotes it to 37.88%. These results strongly support the integration of online joint optimization via dual numeric and language feedback.

## 6 Conclusion

We identified three key challenges in RL approaches using only numerical feedback and proposed Critique-GRPO, an online RL framework that learns from both natural language and numerical feedback. Specifically, it enables learning from initial responses and critique-guided self-refinements simultaneously. Experiments across eight reasoning tasks demonstrate that Critique-GRPO consistently outperforms existing SFT and numerical-feedback-only RL methods, paving the way for scaling RL with diverse real-time feedback in real-world post-deployment scenarios.

## Acknowledgments

We sincerely thank Zichen Liu, Zhanhui Zhou, and the anonymous reviewers for their valuable feedback.

## Impact Statement

Throughout our research, we have adhered to the ICML Code of Ethics, prioritizing privacy, fairness, and individual well-being. All benchmark datasets used were strictly for research purposes and contained no personally identifiable information to safeguard privacy. Prompts were carefully designed to minimize bias or discriminatory language and reduce potential negative impacts. Additionally, modelgenerated responses were verified to ensure they were free from offensive content, misinformation, and personally identifiable information.

## References

Agarwal et al. (2021) A. Agarwal, S. M. Kakade, J. D. Lee, and G. Mahajan On the theory of policy gradient methods: optimality, approximation, and distribution shift . Journal of Machine Learning Research 22 ( 98 ), pp. 1–76 . Cited by: §F.5 .

Amari et al. (2019) S. Amari, R. Karakida, and M. Oizumi Fisher information and natural gradient learning in random deep networks . In The 22nd International Conference on Artificial Intelligence and Statistics , pp. 694–702 . Cited by: §F.6.3 .

Bakouch et al. (2025) E. Bakouch, L. von Werra, and L. Tunstall Open-r1: a fully open reproduction of deepseek-r1 . https://huggingface.co/blog/open-r1 . Cited by: §E.1 , Appendix G , §5.1 .

Burns et al. (2023) C. Burns, P. Izmailov, J. H. Kirchner, B. Baker, L. Gao, L. Aschenbrenner, Y. Chen, A. Ecoffet, M. Joglekar, J. Leike, I. Sutskever, and J. Wu Weak-to-strong generalization: eliciting strong capabilities with weak supervision . External Links: 2312.09390 , Link Cited by: §5.8 .

Casper et al. (2023) S. Casper, X. Davies, C. Shi, T. K. Gilbert, J. Scheurer, J. Rando, R. Freedman, T. Korbak, D. Lindner, P. Freire, T. T. Wang, S. Marks, C. Segerie, M. Carroll, A. Peng, P. J.K. Christoffersen, M. Damani, S. Slocum, U. Anwar, A. Siththaranjan, M. Nadeau, E. J. Michaud, J. Pfau, D. Krasheninnikov, X. Chen, L. Langosco, P. Hase, E. Biyik, A. Dragan, D. Krueger, D. Sadigh, and D. Hadfield-Menell Open problems and fundamental limitations of reinforcement learning from human feedback . Transactions on Machine Learning Research . Note: Survey Certification, Featured Certification External Links: ISSN 2835-8856 , Link Cited by: Appendix A .

Chen et al. (2024) A. Chen, J. Scheurer, J. A. Campos, T. Korbak, J. S. Chan, S. R. Bowman, K. Cho, and E. Perez Learning from natural language feedback . Transactions on Machine Learning Research . Note: External Links: ISSN 2835-8856 , Link Cited by: Appendix A , Appendix G , §1 , §5.1 .

Chen et al. (2023) W. Chen, M. Yin, M. Ku, P. Lu, Y. Wan, X. Ma, J. Xu, X. Wang, and T. Xia TheoremQA: a theorem-driven question answering dataset . In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing , H. Bouamor, J. Pino, and K. Bali (Eds.) , Singapore , pp. 7889–7901 . External Links: Link , Document Cited by: Appendix G , §5.1 .

Cheng et al. (2023) C. Cheng, A. Kolobov, D. Misra, A. Nie, and A. Swaminathan Llf-bench: benchmark for interactive learning from language feedback . arXiv preprint arXiv:2312.06853 . Cited by: §F.4 , §4.2 .

Cui et al. (2025a) G. Cui, L. Yuan, Z. Wang, H. Wang, Y. Zhang, J. Chen, W. Li, B. He, Y. Fan, T. Yu, Q. Xu, W. Chen, J. Yuan, H. Chen, K. Zhang, X. Lv, S. Wang, Y. Yao, X. Han, H. Peng, Y. Cheng, Z. Liu, M. Sun, B. Zhou, and N. Ding Process reinforcement through implicit rewards . External Links: 2502.01456 , Link Cited by: Appendix G , §1 , §5.3 .

Cui et al. (2025b) G. Cui, Y. Zhang, J. Chen, L. Yuan, Z. Wang, Y. Zuo, H. Li, Y. Fan, H. Chen, W. Chen, Z. Liu, H. Peng, L. Bai, W. Ouyang, Y. Cheng, B. Zhou, and N. Ding The entropy mechanism of reinforcement learning for reasoning language models . External Links: 2505.22617 , Link Cited by: Appendix I , §5.6 .

DeepSeek-AI et al. (2025) DeepSeek-AI, D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Bao, H. Xu, H. Wang, H. Ding, H. Xin, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Wang, J. Chen, J. Yuan, J. Qiu, J. Li, J. L. Cai, J. Ni, J. Liang, J. Chen, K. Dong, K. Hu, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang, L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Li, M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang, Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang, R. J. Chen, R. L. Jin, R. Chen, S. Lu, S. Zhou, S. Chen, S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, S. Ye, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng, W. Zhao, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang, W. L. Xiao, W. An, X. Liu, X. Wang, X. Chen, X. Nie, X. Cheng, X. Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su, X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun, X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li, Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi, Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Xu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma, Y. Tang, Y. Zha, Y. Yan, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu, Z. Xie, Z. Zhang, Z. Hao, Z. Ma, Z. Yan, Z. Wu, Z. Gu, Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Pan, Z. Huang, Z. Xu, Z. Zhang, and Z. Zhang DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning . External Links: 2501.12948 , Link Cited by: Appendix A , §E.1 , §E.1 , Appendix G , §1 , §1 , §2 , §5.1 .

Dong et al. (2023) H. Dong, W. Xiong, D. Goyal, Y. Zhang, W. Chow, R. Pan, S. Diao, J. Zhang, K. Shum, and T. Zhang RAFT: reward ranked finetuning for generative foundation model alignment . Trans. Mach. Learn. Res. 2023 . External Links: Link Cited by: Appendix G , §5.1 .

Fatemi et al. (2025) M. Fatemi, B. Rafiee, M. Tang, and K. Talamadupula Concise reasoning via reinforcement learning . External Links: 2504.05185 , Link Cited by: Appendix A , §2 .

Feng et al. (2026) K. Feng, K. Gong, B. Li, Z. Guo, Y. Wang, T. Peng, J. Wu, X. Zhang, B. Wang, and X. Yue Video-r1: reinforcing video reasoning in mllms . Advances in Neural Information Processing Systems 38 , pp. 99114–99137 . Cited by: Appendix A .

Feng et al. (2024) X. Feng, Z. Wan, M. Yang, Z. Wang, G. A. Koushik, Y. Du, Y. Wen, and J. Wang Natural language reinforcement learning . External Links: 2402.07157 , Link Cited by: Appendix A .

Feng et al. (2025) Z. Feng, Q. Chen, N. Lu, Y. Li, S. Cheng, S. Peng, D. Tang, S. Liu, and Z. Zhang Is prm necessary? problem-solving rl implicitly induces prm capability in llms . External Links: 2505.11227 , Link Cited by: §1 .

Gandhi et al. (2025) K. Gandhi, A. Chakravarthy, A. Singh, N. Lile, and N. D. Goodman Cognitive behaviors that enable self-improving reasoners, or, four habits of highly effective stars . External Links: 2503.01307 , Link Cited by: Appendix A , 5th item , 5th item , §E.1 , §2 , §3.1 .

Grattafiori et al. (2024) A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Vaughan, A. Yang, A. Fan, A. Goyal, A. Hartshorn, A. Yang, A. Mitra, A. Sravankumar, A. Korenev, A. Hinsvark, A. Rao, A. Zhang, A. Rodriguez, A. Gregerson, A. Spataru, B. Roziere, B. Biron, B. Tang, B. Chern, C. Caucheteux, C. Nayak, C. Bi, C. Marra, C. McConnell, C. Keller, C. Touret, C. Wu, C. Wong, C. C. Ferrer, C. Nikolaidis, D. Allonsius, D. Song, D. Pintz, D. Livshits, D. Wyatt, D. Esiobu, D. Choudhary, D. Mahajan, D. Garcia-Olano, D. Perino, D. Hupkes, E. Lakomkin, E. AlBadawy, E. Lobanova, E. Dinan, E. M. Smith, F. Radenovic, F. Guzmán, F. Zhang, G. Synnaeve, G. Lee, G. L. Anderson, G. Thattai, G. Nail, G. Mialon, G. Pang, G. Cucurell, H. Nguyen, H. Korevaar, H. Xu, H. Touvron, I. Zarov, I. A. Ibarra, I. Kloumann, I. Misra, I. Evtimov, J. Zhang, J. Copet, J. Lee, J. Geffert, J. Vranes, J. Park, J. Mahadeokar, J. Shah, J. van der Linde, J. Billock, J. Hong, J. Lee, J. Fu, J. Chi, J. Huang, J. Liu, J. Wang, J. Yu, J. Bitton, J. Spisak, J. Park, J. Rocca, J. Johnstun, J. Saxe, J. Jia, K. V. Alwala, K. Prasad, K. Upasani, K. Plawiak, K. Li, K. Heafield, K. Stone, K. El-Arini, K. Iyer, K. Malik, K. Chiu, K. Bhalla, K. Lakhotia, L. Rantala-Yeary, L. van der Maaten, L. Chen, L. Tan, L. Jenkins, L. Martin, L. Madaan, L. Malo, L. Blecher, L. Landzaat, L. de Oliveira, M. Muzzi, M. Pasupuleti, M. Singh, M. Paluri, M. Kardas, M. Tsimpoukelli, M. Oldham, M. Rita, M. Pavlova, M. Kambadur, M. Lewis, M. Si, M. K. Singh, M. Hassan, N. Goyal, N. Torabi, N. Bashlykov, N. Bogoychev, N. Chatterji, N. Zhang, O. Duchenne, O. Çelebi, P. Alrassy, P. Zhang, P. Li, P. Vasic, P. Weng, P. Bhargava, P. Dubal, P. Krishnan, P. S. Koura, P. Xu, Q. He, Q. Dong, R. Srinivasan, R. Ganapathy, R. Calderer, R. S. Cabral, R. Stojnic, R. Raileanu, R. Maheswari, R. Girdhar, R. Patel, R. Sauvestre, R. Polidoro, R. Sumbaly, R. Taylor, R. Silva, R. Hou, R. Wang, S. Hosseini, S. Chennabasappa, S. Singh, S. Bell, S. S. Kim, S. Edunov, S. Nie, S. Narang, S. Raparthy, S. Shen, S. Wan, S. Bhosale, S. Zhang, S. Vandenhende, S. Batra, S. Whitman, S. Sootla, S. Collot, S. Gururangan, S. Borodinsky, T. Herman, T. Fowler, T. Sheasha, T. Georgiou, T. Scialom, T. Speckbacher, T. Mihaylov, T. Xiao, U. Karn, V. Goswami, V. Gupta, V. Ramanathan, V. Kerkez, V. Gonguet, V. Do, V. Vogeti, V. Albiero, V. Petrovic, W. Chu, W. Xiong, W. Fu, W. Meers, X. Martinet, X. Wang, X. Wang, X. E. Tan, X. Xia, X. Xie, X. Jia, X. Wang, Y. Goldschlag, Y. Gaur, Y. Babaei, Y. Wen, Y. Song, Y. Zhang, Y. Li, Y. Mao, Z. D. Coudert, Z. Yan, Z. Chen, Z. Papakipos, A. Singh, A. Srivastava, A. Jain, A. Kelsey, A. Shajnfeld, A. Gangidi, A. Victoria, A. Goldstand, A. Menon, A. Sharma, A. Boesenberg, A. Baevski, A. Feinstein, A. Kallet, A. Sangani, A. Teo, A. Yunus, A. Lupu, A. Alvarado, A. Caples, A. Gu, A. Ho, A. Poulton, A. Ryan, A. Ramchandani, A. Dong, A. Franco, A. Goyal, A. Saraf, A. Chowdhury, A. Gabriel, A. Bharambe, A. Eisenman, A. Yazdan, B. James, B. Maurer, B. Leonhardi, B. Huang, B. Loyd, B. D. Paola, B. Paranjape, B. Liu, B. Wu, B. Ni, B. Hancock, B. Wasti, B. Spence, B. Stojkovic, B. Gamido, B. Montalvo, C. Parker, C. Burton, C. Mejia, C. Liu, C. Wang, C. Kim, C. Zhou, C. Hu, C. Chu, C. Cai, C. Tindal, C. Feichtenhofer, C. Gao, D. Civin, D. Beaty, D. Kreymer, D. Li, D. Adkins, D. Xu, D. Testuggine, D. David, D. Parikh, D. Liskovich, D. Foss, D. Wang, D. Le, D. Holland, E. Dowling, E. Jamil, E. Montgomery, E. Presani, E. Hahn, E. Wood, E. Le, E. Brinkman, E. Arcaute, E. Dunbar, E. Smothers, F. Sun, F. Kreuk, F. Tian, F. Kokkinos, F. Ozgenel, F. Caggioni, F. Kanayet, F. Seide, G. M. Florez, G. Schwarz, G. Badeer, G. Swee, G. Halpern, G. Herman, G. Sizov, Guangyi, Zhang, G. Lakshminarayanan, H. Inan, H. Shojanazeri, H. Zou, H. Wang, H. Zha, H. Habeeb, H. Rudolph, H. Suk, H. Aspegren, H. Goldman, H. Zhan, I. Damlaj, I. Molybog, I. Tufanov, I. Leontiadis, I. Veliche, I. Gat, J. Weissman, J. Geboski, J. Kohli, J. Lam, J. Asher, J. Gaya, J. Marcus, J. Tang, J. Chan, J. Zhen, J. Reizenstein, J. Teboul, J. Zhong, J. Jin, J. Yang, J. Cummings, J. Carvill, J. Shepard, J. McPhie, J. Torres, J. Ginsburg, J. Wang, K. Wu, K. H. U, K. Saxena, K. Khandelwal, K. Zand, K. Matosich, K. Veeraraghavan, K. Michelena, K. Li, K. Jagadeesh, K. Huang, K. Chawla, K. Huang, L. Chen, L. Garg, L. A, L. Silva, L. Bell, L. Zhang, L. Guo, L. Yu, L. Moshkovich, L. Wehrstedt, M. Khabsa, M. Avalani, M. Bhatt, M. Mankus, M. Hasson, M. Lennie, M. Reso, M. Groshev, M. Naumov, M. Lathi, M. Keneally, M. Liu, M. L. Seltzer, M. Valko, M. Restrepo, M. Patel, M. Vyatskov, M. Samvelyan, M. Clark, M. Macey, M. Wang, M. J. Hermoso, M. Metanat, M. Rastegari, M. Bansal, N. Santhanam, N. Parks, N. White, N. Bawa, N. Singhal, N. Egebo, N. Usunier, N. Mehta, N. P. Laptev, N. Dong, N. Cheng, O. Chernoguz, O. Hart, O. Salpekar, O. Kalinli, P. Kent, P. Parekh, P. Saab, P. Balaji, P. Rittner, P. Bontrager, P. Roux, P. Dollar, P. Zvyagina, P. Ratanchandani, P. Yuvraj, Q. Liang, R. Alao, R. Rodriguez, R. Ayub, R. Murthy, R. Nayani, R. Mitra, R. Parthasarathy, R. Li, R. Hogan, R. Battey, R. Wang, R. Howes, R. Rinott, S. Mehta, S. Siby, S. J. Bondu, S. Datta, S. Chugh, S. Hunt, S. Dhillon, S. Sidorov, S. Pan, S. Mahajan, S. Verma, S. Yamamoto, S. Ramaswamy, S. Lindsay, S. Lindsay, S. Feng, S. Lin, S. C. Zha, S. Patil, S. Shankar, S. Zhang, S. Zhang, S. Wang, S. Agarwal, S. Sajuyigbe, S. Chintala, S. Max, S. Chen, S. Kehoe, S. Satterfield, S. Govindaprasad, S. Gupta, S. Deng, S. Cho, S. Virk, S. Subramanian, S. Choudhury, S. Goldman, T. Remez, T. Glaser, T. Best, T. Koehler, T. Robinson, T. Li, T. Zhang, T. Matthews, T. Chou, T. Shaked, V. Vontimitta, V. Ajayi, V. Montanez, V. Mohan, V. S. Kumar, V. Mangla, V. Ionescu, V. Poenaru, V. T. Mihailescu, V. Ivanov, W. Li, W. Wang, W. Jiang, W. Bouaziz, W. Constable, X. Tang, X. Wu, X. Wang, X. Wu, X. Gao, Y. Kleinman, Y. Chen, Y. Hu, Y. Jia, Y. Qi, Y. Li, Y. Zhang, Y. Zhang, Y. Adi, Y. Nam, Yu, Wang, Y. Zhao, Y. Hao, Y. Qian, Y. Li, Y. He, Z. Rait, Z. DeVito, Z. Rosnbrick, Z. Wen, Z. Yang, Z. Zhao, and Z. Ma The llama 3 herd of models . External Links: 2407.21783 , Link Cited by: §1 , §5.5 .

He et al. (2024a) C. He, R. Luo, Y. Bai, S. Hu, Z. L. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, J. Liu, L. Qi, Z. Liu, and M. Sun OlympiadBench: A challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems . CoRR abs/2402.14008 . External Links: Link , Document , 2402.14008 Cited by: §E.1 .

He et al. (2024b) C. He, R. Luo, Y. Bai, S. Hu, Z. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, J. Liu, L. Qi, Z. Liu, and M. Sun OlympiadBench: a challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , L. Ku, A. Martins, and V. Srikumar (Eds.) , Bangkok, Thailand , pp. 3828–3850 . External Links: Link , Document Cited by: Appendix G , §5.1 .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt Measuring mathematical problem solving with the MATH dataset . CoRR abs/2103.03874 . External Links: Link , 2103.03874 Cited by: §E.1 , Appendix G , §5.1 .

Hong et al. (2025) J. Hong, K. Liu, Z. Ling, J. Chen, and S. Levine Natural language actor-critic: scalable off-policy learning in language space . External Links: 2512.04601 , Link Cited by: Appendix A .

Hurst et al. (2024) A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. Gpt-4o system card . arXiv preprint arXiv:2410.21276 . Cited by: Appendix M , §E.1 , §E.2 .

Kakade and Langford (2002) S. Kakade and J. Langford Approximately optimal approximate reinforcement learning . In Proceedings of the nineteenth international conference on machine learning , pp. 267–274 . Cited by: §F.5.2 , §F.6.3 .

Karpathy (2025) A. Karpathy Scaling up rl . X Post 2025 . External Links: Link Cited by: §1 .

Kim et al. (2023) S. Kim, J. Shin, Y. Cho, J. Jang, S. Longpre, H. Lee, S. Yun, S. Shin, S. Kim, J. Thorne, and M. Seo Prometheus: inducing fine-grained evaluation capability in language models . CoRR abs/2310.08491 . External Links: Link , Document , 2310.08491 Cited by: Appendix A .

Lanchantin et al. (2025) J. Lanchantin, A. Chen, J. Lan, X. Li, S. Saha, T. Wang, J. Xu, P. Yu, W. Yuan, J. E. Weston, S. Sukhbaatar, and I. Kulikov Bridging offline and online reinforcement learning for llms . External Links: 2506.21495 , Link Cited by: §2 .

Lewkowycz et al. (2022) A. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski, V. Ramasesh, A. Slone, C. Anil, I. Schlag, T. Gutman-Solo, Y. Wu, B. Neyshabur, G. Gur-Ari, and V. Misra Solving quantitative reasoning problems with language models . External Links: 2206.14858 , Link Cited by: §E.1 , Appendix G .

Li et al. (2025) G. Li, Y. Gao, Y. Li, and Y. Wu ThinkLess: a training-free inference-efficient method for reducing reasoning redundancy . arXiv preprint arXiv:2505.15684 . Cited by: Appendix A , §2 .

Li et al. (2024) J. Li, E. Beeching, L. Tunstall, B. Lipkin, R. Soletskyi, S. C. Huang, K. Rasul, L. Yu, A. Jiang, Z. Shen, Z. Qin, B. Dong, L. Zhou, Y. Fleureau, G. Lample, and S. Polu NuminaMath . Numina . Note: https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf Cited by: §E.1 , Appendix G , Appendix H , §5.1 .

Lightman et al. (2024) H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe Let’s verify step by step . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: Appendix A .

Lin et al. (2017) T. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár Focal loss for dense object detection . In Proceedings of the IEEE international conference on computer vision , pp. 2980–2988 . Cited by: §F.6.1 .

Liu et al. (2022) J. Liu, D. Shen, Y. Zhang, W. B. Dolan, L. Carin, and W. Chen What makes good in-context examples for gpt-3? . In Proceedings of Deep Learning Inside Out (DeeLIO 2022): The 3rd workshop on knowledge extraction and integration for deep learning architectures , pp. 100–114 . Cited by: §1 .

Liu et al. (2025a) Z. Liu, C. Chen, W. Li, P. Qi, T. Pang, C. Du, W. S. Lee, and M. Lin Understanding r1-zero-like training: a critical perspective . External Links: 2503.20783 , Link Cited by: Appendix A , §E.1 , Appendix G , Appendix G , Appendix G , §2 , §4.1 , §5.1 , §5.3 .

Liu et al. (2025b) Z. Liu, P. Wang, R. Xu, S. Ma, C. Ruan, P. Li, Y. Liu, and Y. Wu Inference-time scaling for generalist reward modeling . External Links: 2504.02495 , Link Cited by: Appendix A .

Lu et al. (2010) T. Lu, D. Pal, and M. Pal Contextual multi-armed bandits . In Proceedings of the Thirteenth international conference on Artificial Intelligence and Statistics , pp. 485–492 . Cited by: §F.5 .

Luo et al. (2025) R. Luo, Z. Liu, X. Liu, C. Du, M. Lin, W. Chen, W. Lu, and T. Pang Language models can learn from verbal feedback without scalar rewards . arXiv preprint arXiv:2509.22638 . Cited by: Appendix A .

Lv et al. (2025) X. Lv, Y. Zuo, Y. Sun, H. Liu, Y. Wei, Z. Chen, L. He, X. Zhu, K. Zhang, B. Wang, N. Ding, and B. Zhou Towards a unified view of large language model post-training . External Links: 2509.04419 , Link Cited by: §2 .

OpenAI et al. (2024) OpenAI, :, A. Jaech, A. Kalai, A. Lerer, A. Richardson, A. El-Kishky, A. Low, A. Helyar, A. Madry, A. Beutel, A. Carney, A. Iftimie, A. Karpenko, A. T. Passos, A. Neitz, A. Prokofiev, A. Wei, A. Tam, A. Bennett, A. Kumar, A. Saraiva, A. Vallone, A. Duberstein, A. Kondrich, A. Mishchenko, A. Applebaum, A. Jiang, A. Nair, B. Zoph, B. Ghorbani, B. Rossen, B. Sokolowsky, B. Barak, B. McGrew, B. Minaiev, B. Hao, B. Baker, B. Houghton, B. McKinzie, B. Eastman, C. Lugaresi, C. Bassin, C. Hudson, C. M. Li, C. de Bourcy, C. Voss, C. Shen, C. Zhang, C. Koch, C. Orsinger, C. Hesse, C. Fischer, C. Chan, D. Roberts, D. Kappler, D. Levy, D. Selsam, D. Dohan, D. Farhi, D. Mely, D. Robinson, D. Tsipras, D. Li, D. Oprica, E. Freeman, E. Zhang, E. Wong, E. Proehl, E. Cheung, E. Mitchell, E. Wallace, E. Ritter, E. Mays, F. Wang, F. P. Such, F. Raso, F. Leoni, F. Tsimpourlas, F. Song, F. von Lohmann, F. Sulit, G. Salmon, G. Parascandolo, G. Chabot, G. Zhao, G. Brockman, G. Leclerc, H. Salman, H. Bao, H. Sheng, H. Andrin, H. Bagherinezhad, H. Ren, H. Lightman, H. W. Chung, I. Kivlichan, I. O’Connell, I. Osband, I. C. Gilaberte, I. Akkaya, I. Kostrikov, I. Sutskever, I. Kofman, J. Pachocki, J. Lennon, J. Wei, J. Harb, J. Twore, J. Feng, J. Yu, J. Weng, J. Tang, J. Yu, J. Q. Candela, J. Palermo, J. Parish, J. Heidecke, J. Hallman, J. Rizzo, J. Gordon, J. Uesato, J. Ward, J. Huizinga, J. Wang, K. Chen, K. Xiao, K. Singhal, K. Nguyen, K. Cobbe, K. Shi, K. Wood, K. Rimbach, K. Gu-Lemberg, K. Liu, K. Lu, K. Stone, K. Yu, L. Ahmad, L. Yang, L. Liu, L. Maksin, L. Ho, L. Fedus, L. Weng, L. Li, L. McCallum, L. Held, L. Kuhn, L. Kondraciuk, L. Kaiser, L. Metz, M. Boyd, M. Trebacz, M. Joglekar, M. Chen, M. Tintor, M. Meyer, M. Jones, M. Kaufer, M. Schwarzer, M. Shah, M. Yatbaz, M. Y. Guan, M. Xu, M. Yan, M. Glaese, M. Chen, M. Lampe, M. Malek, M. Wang, M. Fradin, M. McClay, M. Pavlov, M. Wang, M. Wang, M. Murati, M. Bavarian, M. Rohaninejad, N. McAleese, N. Chowdhury, N. Chowdhury, N. Ryder, N. Tezak, N. Brown, O. Nachum, O. Boiko, O. Murk, O. Watkins, P. Chao, P. Ashbourne, P. Izmailov, P. Zhokhov, R. Dias, R. Arora, R. Lin, R. G. Lopes, R. Gaon, R. Miyara, R. Leike, R. Hwang, R. Garg, R. Brown, R. James, R. Shu, R. Cheu, R. Greene, S. Jain, S. Altman, S. Toizer, S. Toyer, S. Miserendino, S. Agarwal, S. Hernandez, S. Baker, S. McKinney, S. Yan, S. Zhao, S. Hu, S. Santurkar, S. R. Chaudhuri, S. Zhang, S. Fu, S. Papay, S. Lin, S. Balaji, S. Sanjeev, S. Sidor, T. Broda, A. Clark, T. Wang, T. Gordon, T. Sanders, T. Patwardhan, T. Sottiaux, T. Degry, T. Dimson, T. Zheng, T. Garipov, T. Stasi, T. Bansal, T. Creech, T. Peterson, T. Eloundou, V. Qi, V. Kosaraju, V. Monaco, V. Pong, V. Fomenko, W. Zheng, W. Zhou, W. McCabe, W. Zaremba, Y. Dubois, Y. Lu, Y. Chen, Y. Cha, Y. Bai, Y. He, Y. Zhang, Y. Wang, Z. Shao, and Z. Li OpenAI o1 system card . External Links: 2412.16720 , Link Cited by: Appendix A , §1 , §2 .

OpenAI (2025) OpenAI OpenAI o3-mini . Note: https://openai.com/index/openai-o3-mini/ Cited by: §1 .

Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. F. Christiano, J. Leike, and R. Lowe Training language models to follow instructions with human feedback . CoRR abs/2203.02155 . External Links: Link , Document , 2203.02155 Cited by: Appendix A .

Qwen et al. (2025) Qwen, :, A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, H. Wei, H. Lin, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Lin, K. Dang, K. Lu, K. Bao, K. Yang, L. Yu, M. Li, M. Xue, P. Zhang, Q. Zhu, R. Men, R. Lin, T. Li, T. Tang, T. Xia, X. Ren, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Wan, Y. Liu, Z. Cui, Z. Zhang, and Z. Qiu Qwen2.5 technical report . External Links: 2412.15115 , Link Cited by: §E.1 , §1 , §3.1 .

Rafailov et al. (2024) R. Rafailov, Y. Chittepu, R. Park, H. Sikchi, J. Hejna, W. B. Knox, C. Finn, and S. Niekum Scaling laws for reward model overoptimization in direct alignment algorithms . In Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024 , A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang (Eds.) , External Links: Link Cited by: Appendix A .

Rein et al. (2024) D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman GPQA: a graduate-level google-proof q&a benchmark . In First Conference on Language Modeling , External Links: Link Cited by: §E.1 , Appendix G .

Russo and Van Roy (2013) D. Russo and B. Van Roy Eluder dimension and the sample complexity of optimistic exploration . Advances in Neural Information Processing Systems 26 . Cited by: §F.4 , Definition F.1 , Proposition 4.1 .

Saunders et al. (2022) W. Saunders, C. Yeh, J. Wu, S. Bills, L. Ouyang, J. Ward, and J. Leike Self-critiquing models for assisting human evaluators . External Links: 2206.05802 , Link Cited by: Appendix A , §1 .

Schulman et al. (2017) J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov Proximal policy optimization algorithms . External Links: 1707.06347 , Link Cited by: Appendix A , §F.6.2 , §4.1 .

Shao et al. (2024a) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. Deepseekmath: pushing the limits of mathematical reasoning in open language models . arXiv preprint arXiv:2402.03300 . Cited by: Appendix A , Definition F.8 , §4 .

Shao et al. (2024b) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. K. Li, Y. Wu, and D. Guo DeepSeekMath: pushing the limits of mathematical reasoning in open language models . CoRR abs/2402.03300 . External Links: Link , Document , 2402.03300 Cited by: §E.1 .

Sheng et al. (2024) G. Sheng, C. Zhang, Z. Ye, X. Wu, W. Zhang, R. Zhang, Y. Peng, H. Lin, and C. Wu HybridFlow: a flexible and efficient rlhf framework . arXiv preprint arXiv: 2409.19256 . Cited by: §E.1 , §5.1 .

Silver and Sutton (2025) D. Silver and R. S. Sutton Welcome to the era of experience . Google AI . Cited by: §1 .

Sutton et al. (1999) R. S. Sutton, D. McAllester, S. Singh, and Y. Mansour Policy gradient methods for reinforcement learning with function approximation . Advances in neural information processing systems 12 . Cited by: §F.5 .

Sutton (1984) R. S. Sutton Temporal credit assignment in reinforcement learning . University of Massachusetts Amherst . Cited by: §1 .

Wang et al. (2024) Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, T. Li, M. Ku, K. Wang, A. Zhuang, R. Fan, X. Yue, and W. Chen MMLU-pro: A more robust and challenging multi-task language understanding benchmark . In Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024 , A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang (Eds.) , External Links: Link Cited by: Appendix G , §5.1 .

Wang et al. (2025) Y. Wang, X. Yue, and W. Chen Critique fine-tuning: learning to critique is more effective than learning to imitate . External Links: 2501.17703 , Link Cited by: Appendix A , Appendix M , Appendix G , §1 , §1 , §5.1 .

Whitehouse et al. (2025) C. Whitehouse, T. Wang, P. Yu, X. Li, J. Weston, I. Kulikov, and S. Saha J1: incentivizing thinking in llm-as-a-judge via reinforcement learning . External Links: 2505.10320 , Link Cited by: Appendix A .

Williams (1992) R. J. Williams Simple statistical gradient-following algorithms for connectionist reinforcement learning . Machine learning 8 , pp. 229–256 . Cited by: Appendix A .

Xi et al. (2024) Z. Xi, D. Yang, J. Huang, J. Tang, G. Li, Y. Ding, W. He, B. Hong, S. Do, W. Zhan, X. Wang, R. Zheng, T. Ji, X. Shi, Y. Zhai, R. Weng, J. Wang, X. Cai, T. Gui, Z. Wu, Q. Zhang, X. Qiu, X. Huang, and Y. Jiang Enhancing llm reasoning via critique models with test-time and training-time supervision . External Links: 2411.16579 , Link Cited by: Appendix A , Appendix A , Appendix G , §1 , §2 , §5.1 .

Xu et al. (2025) W. Xu, A. Nie, R. Zheng, A. Modi, A. Swaminathan, and C. Cheng Provably learning from language feedback . External Links: 2506.10341 , Link Cited by: §F.4 , Assumption F.2 , Definition F.3 , §1 , §4.2 , §5.6 .

Yan et al. (2025) J. Yan, Y. Li, Z. Hu, Z. Wang, G. Cui, X. Qu, Y. Cheng, and Y. Zhang Learning to reason under off-policy guidance . External Links: 2504.14945 , Link Cited by: Appendix A , §E.1 , §F.2 , Appendix G , §1 , §2 , §4.2 , §5.1 , Table 3 , Table 3 .

Yang et al. (2025a) A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, C. Zheng, D. Liu, F. Zhou, F. Huang, F. Hu, H. Ge, H. Wei, H. Lin, J. Tang, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Zhou, J. Lin, K. Dang, K. Bao, K. Yang, L. Yu, L. Deng, M. Li, M. Xue, M. Li, P. Zhang, P. Wang, Q. Zhu, R. Men, R. Gao, S. Liu, S. Luo, T. Li, T. Tang, W. Yin, X. Ren, X. Wang, X. Zhang, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Zhang, Y. Wan, Y. Liu, Z. Wang, Z. Cui, Z. Zhang, Z. Zhou, and Z. Qiu Qwen3 technical report . External Links: 2505.09388 , Link Cited by: Appendix D , §E.1 , §E.1 , §E.1 , §1 , §1 , §3.1 , §5.5 , §5.8 .

Yang et al. (2024) A. Yang, B. Zhang, B. Hui, B. Gao, B. Yu, C. Li, D. Liu, J. Tu, J. Zhou, J. Lin, K. Lu, M. Xue, R. Lin, T. Liu, X. Ren, and Z. Zhang Qwen2.5-math technical report: toward mathematical expert model via self-improvement . External Links: 2409.12122 , Link Cited by: Table 3 , Table 3 .

Yang et al. (2025b) W. Yang, J. Chen, Y. Lin, and J. Wen DeepCritic: deliberate critique with large language models . External Links: 2505.00662 , Link Cited by: §5.5 .

Yu et al. (2025) Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, T. Fan, G. Liu, L. Liu, X. Liu, H. Lin, Z. Lin, B. Ma, G. Sheng, Y. Tong, C. Zhang, M. Zhang, W. Zhang, H. Zhu, J. Zhu, J. Chen, J. Chen, C. Wang, H. Yu, W. Dai, Y. Song, X. Wei, H. Zhou, J. Liu, W. Ma, Y. Zhang, L. Yan, M. Qiao, Y. Wu, and M. Wang DAPO: an open-source llm reinforcement learning system at scale . External Links: 2503.14476 , Link Cited by: Appendix A , §2 .

Yue et al. (2025) Y. Yue, Z. Chen, R. Lu, A. Zhao, Z. Wang, Y. Yue, S. Song, and G. Huang Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? . External Links: 2504.13837 , Link Cited by: Appendix A .

Zeng et al. (2025) W. Zeng, Y. Huang, Q. Liu, W. Liu, K. He, Z. Ma, and J. He SimpleRL-zoo: investigating and taming zero reinforcement learning for open base models in the wild . External Links: 2503.18892 , Link Cited by: §E.1 , Appendix G , §5.3 .

Zhang et al. (2026) X. Zhang, Z. Liu, Y. Zhang, X. Hu, and W. Shao Retroagent: from solving to evolving via retrospective dual intrinsic feedback . arXiv preprint arXiv:2603.08561 . Cited by: Appendix A .

Zhang et al. (2023) X. Zhang, B. Peng, K. Li, J. Zhou, and H. Meng SGP-TOD: building task bots effortlessly via schema-guided LLM prompting . In Findings of the Association for Computational Linguistics: EMNLP 2023 , H. Bouamor, J. Pino, and K. Bali (Eds.) , Singapore , pp. 13348–13369 . External Links: Link , Document Cited by: Appendix M .

Zhang et al. (2024) X. Zhang, B. Peng, Y. Tian, J. Zhou, L. Jin, L. Song, H. Mi, and H. Meng Self-alignment for factuality: mitigating hallucinations in LLMs via self-evaluation . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , L. Ku, A. Martins, and V. Srikumar (Eds.) , Bangkok, Thailand , pp. 1946–1965 . External Links: Link , Document Cited by: Appendix H .

## Appendix

## Appendix A Additional Discussion on Related Work

##### Learning from Natural Language Feedback.

Natural Language Feedback (NLF) provides textual critiques with granular diagnostic signals that facilitate precise response refinement ( Saunders et al., 2022 ; Chen et al., 2024 ; Zhang et al., 2026 ) . Current literature typically integrates NLF by: (1) translating linguistic feedback into scalar reward signals for RL fine-tuning ( Kim et al., 2023 ; Whitehouse et al., 2025 ; Liu et al., 2025b ; Lightman et al., 2024 ; Ouyang et al., 2022 ; Casper et al., 2023 ; Rafailov et al., 2024 ) ; or (2) utilizing SFT to imitate static critiques or critique-guided refinements ( Wang et al., 2025 ; Xi et al., 2024 ; Chen et al., 2024 ) . However, these approaches are primarily offline and lack the capacity for active exploration, limiting their ability to adapt dynamically to idiosyncratic errors encountered during training. While emerging research in natural language RL ( Feng et al., 2024 ; Hong et al., 2025 ; Luo et al., 2025 ) has begun to explore linguistic feedback, it remains predominantly confined to offline settings. In contrast, Critique-GRPO integrates real-time NLF directly into the online RL loop. By enabling the model to learn from guided refinements during active exploration, our approach internalizes error-correction mechanisms more effectively, overcoming the performance plateaus inherent in systems relying solely on numerical rewards.

##### Enhancing LLM Reasoning with Reinforcement Learning.

Reinforcement Learning (RL) has demonstrated significant effectiveness in improving the reasoning capabilities of Large Language Models (LLMs) ( OpenAI et al., 2024 ; DeepSeek-AI et al., 2025 ; Fatemi et al., 2025 ; Li et al., 2025 ; Feng et al., 2026 ) . This is commonly achieved by fine-tuning models on complex reasoning tasks to encourage diverse and robust reasoning behaviors ( Gandhi et al., 2025 ; Yue et al., 2025 ) . Recent advancements leverage RL with numerical feedback, such as assigning positive rewards ( e.g., +1) for correct responses and negative rewards ( e.g., -1) for incorrect ones ( OpenAI et al., 2024 ; DeepSeek-AI et al., 2025 ; Liu et al., 2025a ; Yu et al., 2025 ) . These methods often employ online policy optimization algorithms, including Proximal Policy Optimization (PPO) ( Schulman et al., 2017 ) , Group Relative Policy Optimization (GRPO) ( Shao et al., 2024a ) , REINFORCE ( Williams, 1992 ) , and Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO) ( Yu et al., 2025 ) . However, numerical feedback tends to be sparse, and models often struggle with tasks that exceed their current knowledge boundaries, limiting the potential for substantial improvement ( Xi et al., 2024 ; Gandhi et al., 2025 ) . To address this limitation, recent approaches have incorporated high-quality expert demonstrations alongside online exploration ( Yan et al., 2025 ) . In contrast, our approach enables models to refine their outputs through the integration of various textual feedback, which helps identify and address potential errors. This combination of textual feedback with online exploration for policy optimization enhances flexibility and scalability.

## Appendix B Analysis of Training Computational Cost

We utilize asynchronous rollouts to minimize the additional computational cost introduced by incorporating critiques and self-refinement in Critique-GRPO. Table 9 presents the training time required for 300 steps on a single NVIDIA A800 GPU.

The results show that the additional cost is limited to only 5 and 19 GPU-hours for Qwen2.5-7B-Base and Qwen3-8B, respectively, representing approximately a 2% and 6.5% increase over GRPO. This overhead is marginal compared to the significant performance improvement, with average gains of +6 and +4.5 percentage points across 8 tasks, achieved using only 4K prompts. These findings highlight the substantial gains in data efficiency and model performance, demonstrating that the additional computational cost is highly justified.

## Appendix C Impact of Critique Length on Critique-GRPO

We investigate the impact of critique token length on the performance of Critique-GRPO by varying the level of detail in generated critiques. As shown in Table 10 , shorter CoT critiques (approximately 683 tokens) generally achieve strong performance. However, increasing the token length to around 2079 tokens by prompting the model to produce highly detailed critiques results in a slight performance drop (from 47.08 to 46.00). This decline is likely due to the increased difficulty of extracting critical information from longer contexts. Despite this, all results using Critique-GRPO consistently surpass those of GRPO, demonstrating the robustness of Critique-GRPO.

In addition, we evaluate the system against adversarial critiques to verify that improvements stem from valid guidance rather than spurious natural language signals. For example, by inverting feedback conclusions ( e.g., swapping “correct” and “incorrect”), we observe entropy explosion and subsequent performance degradation.

## Appendix D Scalability of Critique-GRPO to Large-Scale Models

We assess the scalability of Critique-GRPO on the large-scale Qwen3-32B model ( Yang et al., 2025a ) . As shown in Table 11 , Critique-GRPO consistently surpasses GRPO across all eight reasoning tasks.

## Appendix E Limitations of RL with Numerical Feedback and the Promise of Natural Language Guidance (Detailed Analyses)

### E.1 Three Limitations of Learning with Numerical Feedback

We investigate the limitations of fine-tuning with RL relying solely on numerical feedback from three key perspectives: ( i ) (\textup{i}) How best performance improves as the number of training examples increases. ( ii ) (\textup{ii}) How cognitive behaviors contribute to improving successful problem-solving. ( iii ) (\textup{iii}) The model’s ability to solve previously failed problems through trial-and-error.

##### Setup.

We conduct experiments on non-reasoning models, Qwen2.5-7B-Base ( Qwen et al., 2025 ) and Qwen3-8B-Base ( Yang et al., 2025a ) , and a reasoning model, Qwen3-8B ( Yang et al., 2025a ) , for mathematical reasoning tasks. Specifically, we fine-tune the models using GRPO ( Shao et al., 2024b ) with numerical feedback. 1 1 1 GRPO is used without loss of generality, as RL algorithms such as PPO and GRPO exhibit comparable performance.

Datasets and Evaluation Metrics. We utilize randomly sampled subsets of 4k, 8k, 16k, and 32k examples from a reorganized 46k subset ( Yan et al., 2025 ) of OpenR1-Math-220k ( Bakouch et al., 2025 ) . The prompts are sourced from NuminaMath 1.5 ( Li et al., 2024 ) , while the ground truth chain-of-thought (CoT) reasoning paths are generated by Deepseek-R1 ( DeepSeek-AI et al., 2025 ) . Unless otherwise specified, experiments primarily use 4k training prompts. For validation, we randomly sample 500 examples from the validation set curated by ( Yan et al., 2025 ) , which includes examples from Olympiad Bench ( He et al., 2024a ) , MATH ( Hendrycks et al., 2021 ) , Minerva-Math ( Lewkowycz et al., 2022 ) , AIME 2024 ( Li et al., 2024 ) , and AMC 2023 ( Li et al., 2024 ) . To provide a comprehensive evaluation, we assess performance on in-distribution (ID) tasks using Minerva-Math ( Lewkowycz et al., 2022 ) and on out-of-distribution (OOD) tasks using GPQA-Diamond, which covers physics, chemistry, and biology ( Rein et al., 2024 ) . For evaluation, we employ greedy decoding (temperature = 0) and report accuracy as pass@1, following prior work ( Zeng et al., 2025 ; Yang et al., 2025a ; Liu et al., 2025a ) . 2 2 2 The pass@k metric represents the percentage of problems where the model produces a correct solution within its first k k attempts.

Reward Design. We employ rule-based evaluation to provide numerical feedback (scalar rewards), using Math-Verify 3 3 3 https://github.com/huggingface/Math-Verify to validate the correctness of generated answers against ground truth during fine-tuning. Binary rewards are assigned as follows: + 1 +1 for correct final answers and 0 0 for incorrect ones. These rewards serve as a proxy for assessing the accuracy of generated responses.

Implementation Details. Our implementation leverages the VERL library ( Sheng et al., 2024 ) and samples four candidate responses per prompt during fine-tuning.

##### Results.

RL with solely numerical feedback frequently encounters performance plateaus. Figure 5 illustrates the RL fine-tuning dynamics of Qwen2.5-7B-Base and Qwen3-8B across varying numbers of training examples. On-policy RL frequently stagnates, as reflected in validation set accuracy: Qwen2.5-7B-Base reaches its highest performance at approximately 45-46% accuracy after 120 steps (Figure 5(a) ), while Qwen3-8B plateaus at 65-67% accuracy after 200 steps (Figure 5(b) ). Critically, peak accuracy shows negligible improvement despite an 8-fold increase in training prompts or extending the training duration to 420 steps. These results underscore a fundamental scaling bottleneck in scalar-reward RL, where increased compute and data fail to drive further reasoning gains.

Spontaneous self-reflection has limited impact on enhancing problem-solving success. Cognitive behaviors are widely recognized as key contributors to successful complex reasoning ( DeepSeek-AI et al., 2025 ; Gandhi et al., 2025 ) . In particular, increased self-reflection behaviors after RL fine-tuning, which mimic humans reflecting on past experiences and refining their approach to reach a solution (commonly referred to as the “Aha moment” ( DeepSeek-AI et al., 2025 ) ), have drawn significant attention. However, does spontaneous self-reflection play the most critical role in improved performance?

To address this question, we characterize six key cognitive behaviors that contribute to self-improving reasoning during RL fine-tuning:

• Subgoal Setting : Decomposing complex problems into smaller, manageable subtasks.

• Summarization : Summarizing the current state by identifying completed subtasks and determining the next steps in reasoning.

• Verification : Systematically checking intermediate results or computations to ensure correctness.

• Backtracking : Identifying errors or dead-ends in reasoning and revising previous methods or approaches.

• Backward Chaining : Reasoning from desired outcomes back to the initial inputs or steps required to achieve the result. This is particularly useful for multiple-choice questions with provided answer options ( Gandhi et al., 2025 ) .

• Anticipation : Anticipating potential inaccuracies or exploring alternative solutions to a problem.

We categorize the first two behaviors as planning behaviors and the remaining four as self-reflection behaviors . To analyze their contributions, we evaluate problems previously unsolved by the base model. For Qwen2.5-7B-Base, we identify 87 unsolved problems from the Minerva-Math dataset and 37 from the GPQA-Diamond dataset. For Qwen3-8B, we identify 33 unsolved problems from the Minerva-Math dataset and 15 from the GPQA-Diamond dataset. We then examine the cognitive behaviors exhibited in the correct responses generated by RL-finetuned models for these problems.

To detect these behaviors, we use GPT-4o ( Hurst et al., 2024 ) as an automatic judge with manually crafted prompts (Appendix M ). Each behavior b i b_{i} is scored as:

s i = { 1 if behavior ​ b i ​ is present, 0 otherwise. s_{i}=\begin{cases}1&\text{if behavior }b_{i}\text{ is present,}\\ 0&\text{otherwise.}\end{cases} (5)

The average success contribution of each behavior is computed as follows:

Contribution ​ ( b i ) = ∑ j = 1 N s i , j N , \text{Contribution}(b_{i})=\frac{\sum_{j=1}^{N}s_{i,j}}{N}, (6)

where N N is the total number of analyzed responses, and s i , j s_{i,j} indicates whether behavior b i b_{i} appears in response j j . Further details are provided in Appendix L .

Figure 6 presents the average success contribution of various behaviors, showing that planning behaviors are the primary contributors to successful problem-solving, while self-reflection behaviors contribute less in both the mathematical (Minerva-Math) and STEM (GPQA-Diamond) domains. In Figure 6(a) , self-reflection behaviors barely contribute in the mathematical domain for the non-reasoning model. Thanks to extensive training on expert demonstrations with diverse reasoning behaviors in the mathematical domain ( Yang et al., 2025a ) , the reasoning model shows that self-reflection behaviors make a noticeable contribution (Figure 6(b) ). Nevertheless, self-correction-related behaviors, such as backtracking, backward chaining, and anticipation, still contribute considerably less. These observations suggest the limited effectiveness of spontaneous self-reflection. This underscores the unreliability of relying on spontaneous self-reflection for self-correction to improve problem-solving success.

Models exhibit persistent failures on a subset of problems despite trial-and-error fine-tuning. We evaluated the best-performing RL-finetuned Qwen2.5-7B-Base and Qwen3-8B models on 4k training prompts. As shown in the left panel of Table 12 , these models consistently failed on approximately 29% and 3.75% of problems, respectively, with pass@4 = 0. This occurred despite undergoing trial-and-error fine-tuning, where correct responses are rewarded, and incorrect responses are penalized. While the reasoning model (Qwen3-8B) exhibits evident spontaneous self-reflection and significantly better performance with fewer persistent failures, it still struggles with certain problems when relying solely on numerical feedback.

A likely cause of these performance plateaus and persistent failures is the sparse informational content of numerical feedback. Scalar rewards often fail to convey why a response is correct or incorrect or how to improve multi-step reasoning. Furthermore, the limited effectiveness of spontaneous self-reflection exacerbates these challenges. Together, these limitations highlight the necessity of richer feedback mechanisms to enable more effective learning.

### E.2 Promise of Learning from Natural Language Feedback

To move beyond the limitations of purely numerical reward signals, we explore the potential of leveraging natural language feedback to help models identify errors and refine their responses. Specifically, we examine three types of critiques: • Indicative Critique : A heuristic-based critique that merely indicates the binary correctness of the generated solution, without an expert trajectory .

• Indicative Critique with Ground Truth : A heuristic-based critique providing both binary correctness and the ground truth answer, without an expert trajectory .

• CoT Critique : A model-generated critique offering a step-by-step evaluation to justify the assessment, concluding with a binary correctness label, without an expert trajectory .

Examples of these critique types are presented below. We summarize our method for leveraging textual critiques to guide response refinement in Algorithm 1 . A detailed description is provided in Section E.3 , and an illustrative example of refinement using CoT critique is available in Appendix N .

##### Setup.

As described in the previous section, we evaluate the best-performing RL-finetuned Qwen2.5-7B-Base and Qwen3-8B models, generating four responses per question for a set of 4k prompts. Persistently failed question-response pairs are identified as those with pass@4 = 0. For each such pair, we prompt GPT-4o ( Hurst et al., 2024 ) to generate a CoT critique and then construct the two corresponding heuristic-based critiques. Examples of these critique types are shown below. Subsequently, we prompt the models to refine these failed responses.

Evaluation Metrics. To assess the efficacy of the critique and refinement process, we define the following metrics: ( i ) (\textup{i}) Valid Critiques Generated : The percentage of initially erroneous responses for which the critique model ( π ϕ \pi_{\phi} ) successfully generated a well-formed and usable critique. This accounts for potential failures in the critique generation process itself. ( ii ) (\textup{ii}) Successful Refinements : The percentage of initially erroneous responses (that received a valid critique) for which the LLM ( π θ \pi_{\theta} ) subsequently generated a correct refined response. ( iii ) (\textup{iii}) Critiqued Questions : The percentage of unique questions (all of whose initial k k responses were erroneous) for which at least one of their erroneous responses received a valid critique. ( iv ) (\textup{iv}) Questions Successfully Refined : The percentage of unique questions (all of whose initial k k responses were erroneous) for which at least one of their erroneous responses was successfully corrected through the refinement process. We evaluate the correctness of the refinements using the rule-based method described earlier.

Results. Deliberate critique is more effective than spontaneous self-reflection for self-correction. Incorporating all three types of critiques yields non-zero valid refinements and correctly refined questions. This suggests that critiques can enable both models to successfully correct some persistently failed responses that cannot be resolved through spontaneous self-reflection, as discussed in Section 3.1 .

CoT Critiques facilitate effective model refinement. Table 12 shows that refinement guided by CoT critiques achieves the highest valid refinement rate (36.47% and 10.63%) and the largest percentage of successfully refined questions (55.37% and 20.00%) on Qwen2.5-7B-Base and Qwen3-8B, respectively. This performance significantly surpasses refinement based on indicative critiques or critiques with ground truth, even though the CoT critique generation process produces valid critiques for only 60.06% and 50.17% of erroneous responses. The effectiveness of CoT critiques can be attributed to their richness: by providing a step-by-step evaluation of the reasoning ( potentially along with targeted guidance on the correct solution approach).

Binary correctness signals alone can provide refinement benefits. Refinement with indicative critiques with/without ground truth also yields some successful refinements, albeit at a substantially lower rate (approximately 2%-4% valid refinements). This suggests that even simply indicating the correctness of a response can provide a minimal benefit, indicating some promise in leveraging natural language feedback to augment learning from numerical signals. However, the lack of a substantial difference between indicative critiques and critiques with ground truth suggests that providing only the ground-truth answer, without any explanation or reasoning, provides little additional guidance to the model.

### E.3 Leveraging Textual Critiques for Refining LLM Responses

We describe the process for leveraging these textual critiques to guide the refinement of LLM-generated responses:

1. Initial Response Sampling : Given an LLM π θ \pi_{\theta} parameterized by θ \theta and a set of questions { q } \{q\} , we sample multiple initial responses for each question { y 0 ( i ) } i = 1 k ∼ π θ ( ⋅ ∣ q ) \{y_{0}^{(i)}\}_{i=1}^{k}\sim\pi_{\theta}(\cdot\mid q) , where k k is the number of samples.

2. Response Evaluation and Critique Generation : We use an evaluation function Eval ​ ( q , y 0 ) \text{Eval}(q,y_{0}) to assess the correctness of each response y 0 y_{0} . The function outputs 1 if y 0 y_{0} is correct and 0 otherwise. Specifically, we adopt a model-based evaluation with a reasoning-based reward model π R ​ M \pi_{RM} . The reasoning-based reward model generates a CoT critique c CoT ( i ) ∼ π R ​ M ( ⋅ ∣ I c , q , y 0 ( i ) ) c_{\text{CoT}}^{(i)}\sim\pi_{RM}(\cdot\mid I_{c},q,y_{0}^{(i)}) , where I c I_{c} is a predefined instruction (detailed in Appendix M ). Based on the binary correctness label within c CoT ( i ) c_{\text{CoT}}^{(i)} , we construct the corresponding heuristic-based critiques: an indicative critique c I ( i ) c_{\text{I}}^{(i)} (containing only the correctness label) and a critique with ground truth c GT ( i ) c_{\text{GT}}^{(i)} (correctness label plus the known ground truth answer for q q ).

To focus on the model’s ability to learn from critiques for initially incorrect solutions and to control for spontaneous self-correction, we identify persistently failed questions. A question q q is classified as persistently failed if all k k of its initial responses { y 0 ( i ) } i = 1 k \{y_{0}^{(i)}\}_{i=1}^{k} are deemed incorrect based on the labels from their respective CoT critiques. For each such incorrect response y 0 ( j ) y_{0}^{(j)} from a persistently failed question, we form a triplet ( q , y 0 ( j ) , c ( j ) ) (q,y_{0}^{(j)},c^{(j)}) , where c ( j ) c^{(j)} is one of the three critique types: c CoT ( j ) c_{\text{CoT}}^{(j)} , c GT ( j ) c_{\text{GT}}^{(j)} , or c I ( j ) c_{\text{I}}^{(j)} .

3. Self-Refinement Generation : For each selected triplet ( q , y 0 ( j ) , c ( j ) ) (q,y_{0}^{(j)},c^{(j)}) corresponding to an initial incorrect response, we prompt the original LLM π θ \pi_{\theta} to generate a refined response y refined ( j ) ∼ π θ ( ⋅ ∣ I refine , q , y 0 ( j ) , c ( j ) ) y_{\text{refined}}^{(j)}\sim\pi_{\theta}(\cdot\mid I_{\text{refine}},q,y_{0}^{(j)},c^{(j)}) . This generation is conditioned on a specific refinement instruction I refine I_{\text{refine}} (detailed in Appendix M ), the original question q q , the initial failed response y 0 ( j ) y_{0}^{(j)} , and its associated critique c ( j ) c^{(j)} .

The full process is summarized in Algorithm 1 . An example illustrating the self-refinement process, including the application of a CoT critique, is provided in Appendix N .

### E.4 Investigation on Qwen3-8B-Base

We identify 50 previously unsolved problems from the Minerva-Math dataset and 15 from the GPQA-Diamond dataset for Qwen3-8B-Base. Figure 7 shows the average contribution of reasoning behaviors to successful completions of previously failed questions by Qwen3-8B-Base. Notably, self-reflection behaviors contribute minimally to successful problem-solving.

Table 12 reveals that the best-performing RL-finetuned Qwen3-8B-Base persistently failed on 17.18% of training problems. In addition, all three types of critiques facilitate the LLM’s self-refinements.

## Appendix F More Details about Critique-GRPO

### F.1 The Critique-GRPO Algorithm

The Critique-GRPO algorithm is summarized in Algorithm 2 .

### F.2 The shaping Function in Critique-GRPO

We adopt a shaping function f ⁡ ( x ) = x / ( x + γ ) f(x)=x/(x+\gamma) ( Yan et al., 2025 ) ( 0 < γ < 1 0<\gamma<1 ), depicted in Figure 8 , to reweight gradients and emphasize low-probability tokens in refined responses. As illustrated in Figure 8 , this function is bounded between ( 0 , 1 ) (0,1) , where x x represents the token probability of the policy. When γ \gamma is small ( i.e., 0.1), the function significantly amplifies low probabilities, with this amplification decreasing as x x increases. Larger γ \gamma values (0.9) produce less pronounced scaling effects. The black dashed diagonal line indicates no shaping ( i.e., f ⁡ ( x ) = x f(x)=x ). We set γ = 0.1 \gamma=0.1 to optimize learning from unfamiliar yet correct refinements while strongly penalizing unfamiliar incorrect ones.

### F.3 Ratio of Responses per Prompt in Critique-GRPO

We experiment with the ratio of initial responses to refinements per prompt, ranging from 1:1 to 7:1. Our results indicate that a 7:1 ratio achieves both stable training and optimal performance. Lower ratios lead to performance degradation due to sudden increases in entropy loss, caused by distribution shifts introduced by the refinements, during later training stages.

### F.4 Theoretical Analysis of Sample Efficiency

In this section, we provide a theoretical justification for the superior sample efficiency of critique-guided refinement compared to standard reward-based learning. We utilize the Transfer Eluder Dimension ( Xu et al., 2025 ) framework to quantify the information gain provided by language feedback. We first formalize our critique mechanism as Reward-Informative Feedback , establishing that it allows the policy to distinguish hypotheses significantly more efficiently than scalar rewards alone. We then apply this framework to reasoning tasks to demonstrate an exponential reduction in sample complexity.

##### Preliminaries: Complexity Measures and Verifiers.

To characterize the complexity of the hypothesis space ℋ \mathcal{H} , we first introduce the Eluder Dimension ( Russo and Van Roy, 2013 ) , a standard measure in reinforcement learning that quantifies how many observations are required to reduce uncertainty about a reward function.

###### Definition F.1 (Eluder Dimension ( Russo and Van Roy, 2013 ) ) .

An action a ∈ 𝒜 a\in\mathcal{A} is ϵ \epsilon -dependent on actions { a 1 , … , a n } ⊂ 𝒜 \{a_{1},\dots,a_{n}\}\subset\mathcal{A} with respect to a reward class ℛ \mathcal{R} if any pair of reward functions r , r ′ ∈ ℛ r,r^{\prime}\in\mathcal{R} satisfying ∑ i = 1 n ( r ⁡ ( a i ) − r ′ ​ ( a i ) ) 2 ≤ ϵ 2 \sum_{i=1}^{n}(r(a_{i})-r^{\prime}(a_{i}))^{2}\leq\epsilon^{2} also satisfies | r ⁡ ( a ) − r ′ ​ ( a ) | ≤ ϵ |r(a)-r^{\prime}(a)|\leq\epsilon . The ϵ \epsilon -eluder dimension, denoted dim E ( ℛ , ϵ ) \dim_{E}(\mathcal{R},\epsilon) , is the length of the longest sequence in 𝒜 \mathcal{A} such that every element is ϵ ′ \epsilon^{\prime} -independent of its predecessors for some ϵ ′ ≥ ϵ \epsilon^{\prime}\geq\epsilon .

In Language Learning from Feedback (LLF) ( Cheng et al., 2023 ) , agents leverage feedback o o ( e.g., critiques) beyond scalar rewards. To quantify the information in o o , we assume the existence of a verifier .

###### Assumption F.2 (Verifier ( Xu et al., 2025 ) ) .

The verifier defines a loss ℓ : 𝒜 × 𝒪 × ℋ → [ 0 , 1 ] \ell:\mathcal{A}\times\mathcal{O}\times\mathcal{H}\to[0,1] measuring the alignment between a hypothesis η \eta and feedback o o on action a a . Consistency yields ℓ ⁡ ( a , o , η ) = 0 \ell(a,o,\eta)=0 , while inconsistency incurs a non-zero penalty.

To accommodate potential noise, we assume feedback is unbiased: each hypothesis minimizes the expected verifier loss under its induced distribution. Defining the expected minimum loss as ℓ η min ​ ( a ) := min η ′ ⁡ 𝔼 o ∼ f η ​ ( a ) ​ [ ℓ ⁡ ( a , o , η ′ ) ] \ell^{\min}_{\eta}(a):=\min_{\eta^{\prime}}\mathbb{E}_{o\sim f_{\eta}(a)}[\ell(a,o,\eta^{\prime})] , we utilize this to define the Transfer Eluder Dimension :

###### Definition F.3 (Transfer Eluder Dimension ( Xu et al., 2025 ) ) .

An action a a is ϵ \epsilon - transfer dependent on actions { a 1 , … , a n } ⊂ 𝒜 \{a_{1},\dots,a_{n}\}\subset\mathcal{A} with respect to ℋ \mathcal{H} and verifier ℓ \ell if any pair η , η ′ ∈ ℋ \eta,\eta^{\prime}\in\mathcal{H} satisfying: ∑ i = 1 n ( 𝔼 o ∼ f η ′ ​ ( a i ) ​ [ ℓ ⁡ ( a i , o , η ) ] − ℓ η ′ min ​ ( a i ) ) ≤ ϵ 2 \sum_{i=1}^{n}\left(\mathbb{E}_{o\sim f_{\eta^{\prime}}(a_{i})}[\ell(a_{i},o,\eta)]-\ell^{\min}_{\eta^{\prime}}(a_{i})\right)\leq\epsilon^{2} (7) also satisfies | r η ​ ( a ) − r η ′ ​ ( a ) | ≤ ϵ |r_{\eta}(a)-r_{\eta^{\prime}}(a)|\leq\epsilon . The ϵ \epsilon -transfer eluder dimension, dim T ​ E ( ℋ , ℓ , ϵ ) \dim_{TE}(\mathcal{H},\ell,\epsilon) , is the length of the longest sequence of transfer-independent actions.

##### Critique as Reward-Informative Feedback.

Intuitively, the Transfer Eluder Dimension measures how effectively feedback reduces uncertainty about the reward. For this framework to apply, we must establish that our critique mechanism is at least as useful as the reward signal. We rely on the concept of Reward-Informative Feedback .

###### Definition F.4 (Reward-Informative Feedback) .

A feedback function f η f_{\eta} is reward-informative of r η r_{\eta} with respect to a verifier ℓ \ell if there exists a constant C F > 0 C_{F}>0 such that for all η ′ ∈ ℋ \eta^{\prime}\in\mathcal{H} and a ∈ 𝒜 a\in\mathcal{A} : | r η ​ ( a ) − r η ′ ​ ( a ) | 2 ≤ C F ​ 𝔼 o ∼ f η ​ ( a ) ​ [ ℓ ⁡ ( a , o , η ′ ) − ℓ η min ​ ( a ) ] . |r_{\eta}(a)-r_{\eta^{\prime}}(a)|^{2}\leq C_{F}\mathbb{E}_{o\sim f_{\eta}(a)}[\ell(a,o,\eta^{\prime})-\ell^{\min}_{\eta}(a)]. (8)

This condition implies that if two hypotheses differ in reward, the verifier can distinguish them via feedback. Our employed critiques (both indicative and constructive) satisfy this condition by providing strictly more information than a binary reward r ∈ { 0 , 1 } r\in\{0,1\} , enabling the rejection of incorrect hypotheses without needing to observe the final scalar reward.

###### Proposition F.5 (Generalization Bound) .

For reward-informative LLF problems with constant C F C_{F} , the Transfer Eluder Dimension is bounded by the standard Eluder Dimension of the effective reward class ℛ ℋ = { r η : η ∈ ℋ } \mathcal{R}_{\mathcal{H}}=\{r_{\eta}:\eta\in\mathcal{H}\} : dim T ​ E ( ℋ , C F ​ ℓ , ϵ ) ≤ dim E ( ℛ ℋ , ϵ ) . \dim_{TE}(\mathcal{H},C_{F}\ell,\epsilon)\leq\dim_{E}(\mathcal{R}_{\mathcal{H}},\epsilon). (9)

Proposition F.5 guarantees that learning from critiques is no harder than learning from rewards. However, in practice, the inequality is strict and the gap is large. Below, we quantify this gap for reasoning tasks.

##### Complexity Reduction Analysis.

We analyze the reduction in the effective search space for a reasoning task where the goal is to construct a hidden optimal solution sequence a ∗ = ( s 1 ∗ , … , s L ∗ ) a^{*}=(s^{*}_{1},\dots,s^{*}_{L}) of length L L over a vocabulary 𝒮 \mathcal{S} . The action space is defined as 𝒜 = 𝒮 L \mathcal{A}=\mathcal{S}^{L} .

###### Proposition F.6 (Sample Efficiency of Critique-Guided Refinement) .

We compare the dimension of the hypothesis space under Reward-Only Learning versus Critique-Guided Learning.

1. Standard Generation – Reward-Only Learning (Eluder Dimension): With binary rewards r ⁡ ( a ) = 𝕀 ⁡ ( a = a ∗ ) r(a)=\mathbb{I}(a=a^{*}) , the signal is sparse (a “needle in a haystack”). Observing r ⁡ ( a ) = 0 r(a)=0 eliminates only the specific sequence a a , providing no information about the correctness of other sequences a ′ ≠ a a^{\prime}\neq a . Consequently, the agent must effectively enumerate the action space to find a ∗ a^{*} . The Eluder dimension scales exponentially with the sequence length: dim E ( ℛ , ϵ ) ≈ O ⁡ ( | 𝒮 | L ) . \dim_{E}(\mathcal{R},\epsilon)\approx O(|\mathcal{S}|^{L}). (10)

2. Critique-Guided Refinement – Critique-Guided Learning (Transfer Eluder Dimension): We analyze two types of feedback mechanisms: • Indicative Feedback ( c I c_{\text{I}} , c GT c_{\text{GT}} ): This feedback indicates failure but lacks specific error localization. While the worst-case complexity remains dim T ​ E ( ℋ , ℓ , ϵ ) ≈ O ⁡ ( | 𝒮 | L ) \dim_{TE}(\mathcal{H},\ell,\epsilon)\approx O(|\mathcal{S}|^{L}) , the critique acts as a pruning signal. Conditioning on the failure and the specific content of the critique restricts the search to a subspace 𝒜 c ⊂ 𝒜 \mathcal{A}_{c}\subset\mathcal{A} , reducing the effective search space size by a constant factor α < 1 \alpha<1 .

• Constructive Feedback ( c CoT c_{\text{CoT}} ): If the critique localizes the first error at step t t , the problem decomposes into L L sequential sub-problems, each of size | 𝒮 | |\mathcal{S}| . This reduces the complexity from exponential to linear, i.e., dim T ​ E ( ℋ , ℓ , ϵ ) ≈ O ⁡ ( L ​ | 𝒮 | ) \dim_{TE}(\mathcal{H},\ell,\epsilon)\approx O(L|\mathcal{S}|) . Furthermore, if the critique provides the correction suggestion for the first error s t ∗ s_{t}^{*} , the complexity becomes independent of the vocabulary size, scaling as dim T ​ E ( ℋ , ℓ , ϵ ) ≈ O ⁡ ( L ) \dim_{TE}(\mathcal{H},\ell,\epsilon)\approx O(L) .

Consequently, for a fixed computational budget M M where L ​ | 𝒮 | ≪ M ≪ | 𝒮 | L L|\mathcal{S}|\ll M\ll|\mathcal{S}|^{L} , critique-guided exploration yields a significantly higher probability of success: P ⁡ ( a ∗ ∈ { y refined ( j ) } j = 1 M ) ≫ P ⁡ ( a ∗ ∈ { y ( i ) } i = 1 M ) . P(a^{*}\in\{y_{\text{refined}}^{(j)}\}_{j=1}^{M})\gg P(a^{*}\in\{y^{(i)}\}_{i=1}^{M}). (11)

###### Proof.

We prove this by estimating the Transfer Eluder Dimension d d , which quantifies the effective search space size. We assume a uniform exploration strategy over the effective search space.

1. Derivation of Effective Dimension ( d d )

Case A: Reward-Only. The binary indicator problem is equivalent to a standard bandit problem with | 𝒮 | L |\mathcal{S}|^{L} arms. In this setting, the feedback function is simply the reward itself, f η ​ ( a ) = r ​ ( a ) f_{\eta}(a)=r(a) . Observing r ⁡ ( a ) = 0 r(a)=0 provides information only about action a a and no other a ′ ≠ a a^{\prime}\neq a . Thus, a ′ a^{\prime} is ϵ \epsilon -independent of a a (Definition F.1 ). We can construct a sequence of independent actions spanning the entire space. Thus, the dimension is bounded by the cardinality of the action space: d std = | 𝒮 | L . d_{\text{std}}=|\mathcal{S}|^{L}. (12)

Case B: Critique-Guided (Constructive). Let the feedback f ⁡ ( a ) f(a) return the index of the first error: t = min ⁡ { i ∣ s i ≠ s i ∗ } t=\min\{i\mid s_{i}\neq s^{*}_{i}\} . We partition the action space 𝒜 \mathcal{A} into L L disjoint sets, where 𝒜 t = { ( s 1 , … , s L ) ∣ s 1 : t − 1 are correct, s t is incorrect } \mathcal{A}_{t}=\{(s_{1},\dots,s_{L})\mid s_{1:t-1}\text{ are correct, }s_{t}\text{ is incorrect}\} . According to Definition F.3 , an action is transfer-dependent if similar feedback implies similar rewards. If we select more than | 𝒮 | |\mathcal{S}| actions from a partition 𝒜 t \mathcal{A}_{t} , by the Pigeonhole Principle, at least two actions must share the same incorrect token s t s_{t} (given they share the same correct prefix). Observing the error index t t for the first action effectively predicts the error index for the second. This reduces the problem to solving L L sequential classification problems of size | 𝒮 | |\mathcal{S}| . The effective dimension is the sum of these sub-problems: d crit = ∑ t = 1 L | 𝒮 | = L ​ | 𝒮 | . d_{\text{crit}}=\sum_{t=1}^{L}|\mathcal{S}|=L|\mathcal{S}|. (13) If the critique also provides the correction suggestion for the first error s t ∗ s_{t}^{*} , the sequence of error indices in an independent action sequence becomes strictly monotonic, further reducing the dimension to d corr ≈ O ⁡ ( L ) d_{\text{corr}}\approx O(L) .

2. Probability of Success

Let M M be the computational budget. The probability of finding the unique optimal solution a ∗ a^{*} is equivalent to sampling the correct element from a set of size d d without replacement. The probability of success is approximately: P ⁡ ( success ) ≈ 1 − exp ⁡ ( − M d ) . P(\text{success})\approx 1-\exp\left(-\frac{M}{d}\right). (14)

Given the regime L ​ | 𝒮 | ≪ M ≪ | 𝒮 | L L|\mathcal{S}|\ll M\ll|\mathcal{S}|^{L} :

For Reward-Only Learning , substituting d std = | 𝒮 | L d_{\text{std}}=|\mathcal{S}|^{L} : P std ≈ 1 − exp ⁡ ( − M | 𝒮 | L ) ≈ M | 𝒮 | L ≈ 0 . P_{\text{std}}\approx 1-\exp\left(-\frac{M}{|\mathcal{S}|^{L}}\right)\approx\frac{M}{|\mathcal{S}|^{L}}\approx 0. (15)

For Critique-Guided Learning , substituting d crit = L ​ | 𝒮 | d_{\text{crit}}=L|\mathcal{S}| : P crit ≈ 1 − exp ⁡ ( − M L ​ | 𝒮 | ) ≈ 1 . P_{\text{crit}}\approx 1-\exp\left(-\frac{M}{L|\mathcal{S}|}\right)\approx 1. (16)

Conclusion. The ratio of success probabilities is P crit P std ≈ | 𝒮 | L M ≫ 1 \frac{P_{\text{crit}}}{P_{\text{std}}}\approx\frac{|\mathcal{S}|^{L}}{M}\gg 1 . This confirms that critique-guided refinement is strictly more sample-efficient than standard reward-based generation. ∎

### F.5 Theoretical Analysis of Convergence and Policy Improvement

Building upon the sample efficiency established in Appendix F.4 , we now analyze the optimization dynamics. We prove that while standard GRPO converges given sufficient samples, Critique-GRPO accelerates this process by altering the trajectory distribution. We utilize the framework of Policy Gradient methods ( Sutton et al., 1999 ; Agarwal et al., 2021 ) to demonstrate that Critique-GRPO learns from higher quality trajectories , guaranteeing a steeper monotonic policy improvement.

##### Preliminaries and Problem Setup.

We consider the reasoning task as a contextual bandit problem ( Lu et al., 2010 ) . Let π θ ​ ( y | x ) \pi_{\theta}(y|x) be the policy parameterized by θ \theta .

###### Definition F.7 (Sparse Reward Landscape) .

The reward function R ⁡ ( y , x ) R(y,x) is binary and sparse. Let 𝒴 x ∗ \mathcal{Y}^{*}_{x} be the set of correct reasoning chains. R ⁡ ( y , x ) = 𝕀 ⁡ ( y ∈ 𝒴 x ∗ ) . R(y,x)=\mathbb{I}(y\in\mathcal{Y}^{*}_{x}). (17)

###### Definition F.8 (GRPO Gradient Estimate) .

Following Shao et al. (2024a) , GRPO estimates the gradient using a group of G G outputs { y 1 , … , y G } \{y_{1},\dots,y_{G}\} sampled from π θ old \pi_{\theta_{\text{old}}} for a single input x x . The gradient estimator is: g ^ GRPO = 1 G ​ ∑ i = 1 G A ^ i ​ ∇ θ ​ log ⁡ π θ ​ ( y i | x ) , where ​ A ^ i = R ⁡ ( y i ) − μ R σ R + ϵ . \hat{g}_{\text{GRPO}}=\frac{1}{G}\sum_{i=1}^{G}\hat{A}_{i}\nabla_{\theta}\log\pi_{\theta}(y_{i}|x),\quad\text{where }\hat{A}_{i}=\frac{R(y_{i})-\mu_{R}}{\sigma_{R}+\epsilon}. (18)

#### F.5.1 Inefficiency of Standard Exploration

In complex reasoning tasks, the probability of generating a correct solution y ∗ y^{*} via random sampling, denoted as p ∗ = P y ∼ π θ ​ ( y ∈ 𝒴 x ∗ ) p^{*}=P_{y\sim\pi_{\theta}}(y\in\mathcal{Y}^{*}_{x}) , is small but non-negligible. While standard GRPO is an unbiased estimator, its convergence rate is limited by the sparsity of the signal.

###### Proposition F.9 (Signal-to-Noise Ratio in Standard GRPO) .

For a group size G G , the expected number of positive rewards in a standard GRPO batch is 𝔼 ⁡ [ N + ] = G ​ p ∗ \mathbb{E}[N^{+}]=Gp^{*} . The gradient contribution from optimal trajectories is weighted by p ∗ p^{*} . If p ∗ < 1 / G p^{*}<1/G , many batches will contain no positive signal ( σ R = 0 \sigma_{R}=0 ), resulting in wasted computation steps where Δ ​ θ = 0 \Delta\theta=0 . Even when σ R > 0 \sigma_{R}>0 , the magnitude of the update in the direction of the optimal policy is proportional to p ∗ p^{*} .

#### F.5.2 Policy Improvement via Critique-Guided Refinement

Critique-GRPO modifies the sampling distribution. Instead of optimizing solely on y ∼ π θ y\sim\pi_{\theta} , we optimize on a mixture distribution induced by the critique mechanism. Let the refined set be 𝒴 ref = { Refine ​ ( y ) ∣ y ∼ π θ } \mathcal{Y}_{\text{ref}}=\{\text{Refine}(y)\mid y\sim\pi_{\theta}\} .

###### Lemma F.10 (Trajectory Quality Enhancement) .

Let P crit P_{\text{crit}} be the success rate of the critique mechanism in generating a correct solution y ∗ y^{*} . As shown in Proposition 4.1 , P crit ≫ p ∗ P_{\text{crit}}\gg p^{*} . By including 𝒴 ref \mathcal{Y}_{\text{ref}} in the GRPO group, the effective probability of observing an optimal trajectory in the batch becomes P eff ≈ P crit P_{\text{eff}}\approx P_{\text{crit}} . This ensures that the gradient estimator is dominated by high-quality trajectories, significantly reducing the variance of the advantage function and ensuring σ R > 0 \sigma_{R}>0 with high probability.

We now prove that learning from these higher-quality trajectories leads to superior policy improvement.

###### Theorem F.11 (Policy Improvement Lower Bound) .

Let π old \pi_{\text{old}} be the current policy and π new \pi_{\text{new}} be the policy after an update step with learning rate α \alpha . The expected improvement in the objective function J ⁡ ( π ) J(\pi) is lower-bounded by the quality of the trajectories used in the update. Comparing Standard GRPO and Critique-GRPO: Δ ​ J std \displaystyle\Delta J_{\text{std}} ≥ α ⋅ p ∗ ⋅ 𝔼 ⁡ [ 1 σ R ​ π old ​ ( y ∗ ) ​ ‖ ∇ log ⁡ π ​ ( y ∗ ) ‖ 2 ] − O ⁡ ( α 2 ) \displaystyle\geq\alpha\cdot p^{*}\cdot\mathbb{E}\left[\frac{1}{\sigma_{R}}\pi_{\text{old}}(y^{*})\|\nabla\log\pi(y^{*})\|^{2}\right]-O(\alpha^{2}) (19) Δ ​ J crit \displaystyle\Delta J_{\text{crit}} ≥ α ⋅ P crit ⋅ 𝔼 ⁡ [ 1 σ R ​ π old ​ ( y ∗ ) ​ ‖ ∇ log ⁡ π ​ ( y ∗ ) ‖ 2 ] − O ⁡ ( α 2 ) \displaystyle\geq\alpha\cdot P_{\text{crit}}\cdot\mathbb{E}\left[\frac{1}{\sigma_{R}}\pi_{\text{old}}(y^{*})\|\nabla\log\pi(y^{*})\|^{2}\right]-O(\alpha^{2}) (20) Since P crit ≫ p ∗ P_{\text{crit}}\gg p^{*} , it follows that Δ ​ J crit ≫ Δ ​ J std \Delta J_{\text{crit}}\gg\Delta J_{\text{std}} .

###### Proof.

Step 1: Performance Difference. From Kakade and Langford (2002) , J ⁡ ( π new ) − J ⁡ ( π old ) ≈ 𝔼 y ∼ ρ ​ [ A ^ ​ ( y ) ] J(\pi_{\text{new}})-J(\pi_{\text{old}})\approx\mathbb{E}_{y\sim\rho}[\hat{A}(y)] , where ρ \rho is the sampling distribution. The update vector Δ ​ θ \Delta\theta is proportional to the advantage-weighted gradient: Δ θ ∝ ∑ y ∈ Batch A ^ ( y ) ∇ log π ( y ) \Delta\theta\propto\sum_{y\in\text{Batch}}\hat{A}(y)\nabla\log\pi(y) .

Step 2: Dominance of Optimal Trajectories. In a sparse reward setting, the advantage of an optimal solution y ∗ y^{*} is positive and large, while incorrect solutions have small negative advantages. The update direction is dominated by the term corresponding to y ∗ y^{*} : Δ θ ≈ η ⋅ A ^ ( y ∗ ) ∇ log π ( y ∗ ) . \Delta\theta\approx\eta\cdot\hat{A}(y^{*})\nabla\log\pi(y^{*}). (21) The magnitude of this update depends on the frequency of observing y ∗ y^{*} in the batch.

Step 3: Comparison of Sampling Distributions. • Standard GRPO: Samples y ∼ π old y\sim\pi_{\text{old}} . The probability of observing y ∗ y^{*} is p ∗ p^{*} . The expected update norm is proportional to p ∗ ​ ‖ ∇ log ⁡ π ​ ( y ∗ ) ‖ p^{*}\|\nabla\log\pi(y^{*})\| .

• Critique-GRPO: Samples from a mixture including refined outputs. The probability of observing y ∗ y^{*} is P crit P_{\text{crit}} . The expected update norm is proportional to P crit ​ ‖ ∇ log ⁡ π ​ ( y ∗ ) ‖ P_{\text{crit}}\|\nabla\log\pi(y^{*})\| .

Conclusion: The superiority of Critique-GRPO lies in the fact that it learns from a distribution of higher trajectories . Even if standard exploration is capable of finding the solution (non-negligible p ∗ p^{*} ), the critique mechanism artificially amplifies the density of optimal solutions in the training data. Substituting the observation probabilities into the Taylor expansion of the objective function: J ( π new ) − J ( π old ) ≈ ∇ J ( π old ) ⊤ Δ θ ∝ P ( observing y ∗ ) ⋅ ∥ ∇ log π ( y ∗ ) ∥ 2 . J(\pi_{\text{new}})-J(\pi_{\text{old}})\approx\nabla J(\pi_{\text{old}})^{\top}\Delta\theta\propto P(\text{observing }y^{*})\cdot\|\nabla\log\pi(y^{*})\|^{2}. (22) Given P crit ≫ p ∗ P_{\text{crit}}\gg p^{*} , the lower bound on policy improvement is strictly higher for Critique-GRPO. ∎

###### Theorem F.12 (Global Convergence via Policy Shaping) .

Assuming the function approximation class of π θ \pi_{\theta} is sufficiently expressive and the learning rate satisfies Robbins-Monro conditions, Critique-GRPO converges to the optimal policy π ∗ \pi^{*} . The convergence rate is accelerated by a factor of O ⁡ ( P crit / p ∗ ) O(P_{\text{crit}}/p^{*}) compared to standard GRPO.

###### Proof.

We utilize the property that Critique-GRPO simulates Supervised Fine-Tuning (SFT) on dynamically generated optimal data within the RL loop. From Theorem F.11 , the policy probability mass on y ∗ y^{*} increases at each step. Since the gradient variance is bounded (due to the high probability of non-zero variance batches via Lemma F.10 ), stochastic gradient descent converges. Crucially, the effective learning rate on the optimal trajectory y ∗ y^{*} is scaled by the critique success rate. Thus, the model requires fewer iterations to reach the same level of performance as standard GRPO, effectively leveraging the higher quality of the critique-refined trajectories. ∎

### F.6 Theoretical Analysis: Gradient Efficiency and Manifold Preservation

Now we provide a analysis of the optimization dynamics in 𝒥 Critique-GRPO \mathcal{J}_{\text{Critique-GRPO}} after employing the shaping function on the refinements. We address the dual challenge of (1) efficiently extracting learning signals from off-policy refined responses ( y ref y_{\text{ref}} ) and (2) preventing the catastrophic forgetting (entropy explosion) caused by distribution shift.

#### F.6.1 Gradient Dynamics of the Shaping Function

Standard Policy Gradient methods maximize 𝔼 ​ [ log ⁡ π θ ​ ( y ) ] \mathbb{E}[\log\pi_{\theta}(y)] . However, for refined responses where π θ ​ ( y ref ) ≪ 1 \pi_{\theta}(y_{\text{ref}})\ll 1 , standard gradients can be unstable or vanish. We employ the shaping function ρ t ​ ( θ ) = π t π t + γ \rho_{t}(\theta)=\frac{\pi_{t}}{\pi_{t}+\gamma} .

###### Lemma F.13 (Gradient Rescaling) .

Let π t = π θ ​ ( a t | s t ) \pi_{t}=\pi_{\theta}(a_{t}|s_{t}) . The gradient of the shaped objective with respect to the policy parameters θ \theta is a re-weighted version of the standard policy gradient: ∇ θ ρ t ​ ( θ ) = [ γ ​ π t ( π t + γ ) 2 ] ⏟ Ψ ⁡ ( π t ) ⋅ ∇ θ ​ log ​ π t . \nabla_{\theta}\rho_{t}(\theta)=\underbrace{\left[\frac{\gamma\pi_{t}}{(\pi_{t}+\gamma)^{2}}\right]}_{\Psi(\pi_{t})}\cdot\nabla_{\theta}\log\pi_{t}. (23)

###### Proof.

Applying the quotient rule to ρ t \rho_{t} with respect to π t \pi_{t} : ∂ ρ t ∂ π t = 1 ⋅ ( π t + γ ) − π t ⋅ 1 ( π t + γ ) 2 = γ ( π t + γ ) 2 . \frac{\partial\rho_{t}}{\partial\pi_{t}}=\frac{1\cdot(\pi_{t}+\gamma)-\pi_{t}\cdot 1}{(\pi_{t}+\gamma)^{2}}=\frac{\gamma}{(\pi_{t}+\gamma)^{2}}. (24) By the chain rule, ∇ θ ρ t = ∂ ρ t ∂ π t ​ ∇ θ π t \nabla_{\theta}\rho_{t}=\frac{\partial\rho_{t}}{\partial\pi_{t}}\nabla_{\theta}\pi_{t} . Using the log-derivative identity ∇ θ π t = π t ​ ∇ θ ​ log ⁡ π t \nabla_{\theta}\pi_{t}=\pi_{t}\nabla_{\theta}\log\pi_{t} , we substitute to obtain: ∇ θ ρ t = γ ​ π t ( π t + γ ) 2 ​ ∇ θ ​ log ⁡ π t . \nabla_{\theta}\rho_{t}=\frac{\gamma\pi_{t}}{(\pi_{t}+\gamma)^{2}}\nabla_{\theta}\log\pi_{t}. (25) ∎

##### Analysis of the Modulation Term Ψ ⁡ ( π t ) \Psi(\pi_{t}) .

The coefficient Ψ ⁡ ( π t ) \Psi(\pi_{t}) acts as a dynamic gain controller, theoretically aligning with the ”hard negative mining” mechanism found in Focal Loss ( Lin et al., 2017 ) . 1. Suppression of Easy Tokens ( π t → 1 \pi_{t}\to 1 ): lim π t → 1 Ψ ⁡ ( π t ) ≈ γ ( 1 + γ ) 2 \lim_{\pi_{t}\to 1}\Psi(\pi_{t})\approx\frac{\gamma}{(1+\gamma)^{2}} . Since γ ≪ 1 \gamma\ll 1 , the gradient magnitude is significantly dampened. This prevents the model from overfitting to tokens it has already mastered, preserving the KL-divergence on trivial tokens.

2. Peak Efficiency in the Learning Zone: Solving d ​ Ψ d ​ π = 0 \frac{d\Psi}{d\pi}=0 yields a maximum at π t = γ \pi_{t}=\gamma . By setting γ ≈ 0.1 \gamma\approx 0.1 , we explicitly maximize gradients for ”correction tokens”—those that the current policy considers unlikely but plausible. This focuses the update on the reasoning gap between the initial and refined response.

#### F.6.2 The Insufficiency of Clipping for Off-Policy Data

Standard PPO/GRPO relies on clipping the probability ratio r t r_{t} to [ 1 − ϵ , 1 + ϵ ] [1-\epsilon,1+\epsilon] to enforce a trust region ( Schulman et al., 2017 ) . While effective for on-policy data, we prove that clipping is insufficient for off-policy refinements due to vector orthogonality.

###### Proposition F.14 (Gradient Orthogonality) .

Let ℳ old \mathcal{M}_{\text{old}} be the manifold of the current policy. The gradient update from refinements, Δ ​ θ ref \Delta\theta_{\text{ref}} , is often orthogonal to the update from initial responses, Δ ​ θ init \Delta\theta_{\text{init}} .

Reasoning: Δ ​ θ init \Delta\theta_{\text{init}} reinforces the current mode of the distribution. Conversely, Δ ​ θ ref \Delta\theta_{\text{ref}} attempts to shift probability mass to a disjoint region of the sample space ( y ref y_{\text{ref}} ). Optimizing Δ ​ θ ref \Delta\theta_{\text{ref}} inherently requires reducing the probability of y init y_{\text{init}} . Therefore: ⟨ ∇ θ 𝒥 init , ∇ θ 𝒥 ref ⟩ < 0 . \langle\nabla_{\theta}\mathcal{J}_{\text{init}},\nabla_{\theta}\mathcal{J}_{\text{ref}}\rangle<0. (26) Clipping bounds the magnitude of the step but does not correct this conflicting direction . Without regularization, the accumulation of Δ ​ θ ref \Delta\theta_{\text{ref}} updates drags the policy off the manifold ℳ old \mathcal{M}_{\text{old}} , leading to entropy collapse.

#### F.6.3 Manifold Preservation via The Anchor Hypothesis

To prevent this collapse, we derive the necessity of the sample prioritization ratio N init ≫ N ref N_{\text{init}}\gg N_{\text{ref}} .

###### Theorem F.15 (The Anchor Condition) .

Let 𝐅 \mathbf{F} be the Fisher Information Matrix of the policy. To ensure the updated policy π θ ′ \pi_{\theta^{\prime}} remains within a trust region D KL ( π θ ′ | | π θ ) ≤ δ D_{\text{KL}}(\pi_{\theta^{\prime}}||\pi_{\theta})\leq\delta , the influence of refined samples must be bounded by the curvature of the on-policy manifold.

###### Proof.

We approximate the KL divergence using the second-order Taylor expansion ( Amari et al., 2019 ; Kakade and Langford, 2002 ) : D KL ( π θ + Δ ​ θ | | π θ ) ≈ 1 2 Δ θ T 𝐅 Δ θ . D_{\text{KL}}(\pi_{\theta+\Delta\theta}||\pi_{\theta})\approx\frac{1}{2}\Delta\theta^{T}\mathbf{F}\Delta\theta. (27) The total update is a convex combination: Δ ​ θ ∝ ( 1 − λ ) ​ g init + λ ​ g ref \Delta\theta\propto(1-\lambda)g_{\text{init}}+\lambda g_{\text{ref}} , where λ = N ref / N \lambda=N_{\text{ref}}/N . Since g init g_{\text{init}} is clipped on-policy, its contribution to the divergence is bounded by design. The risk arises from g ref g_{\text{ref}} , which is high-variance and off-distribution. If λ \lambda is large, the term λ ​ g ref \lambda g_{\text{ref}} dominates. Since g ref g_{\text{ref}} is not aligned with the eigenvectors of 𝐅 \mathbf{F} (which represent the current policy’s geometry), the term Δ ​ θ T ​ 𝐅 ​ Δ ​ θ \Delta\theta^{T}\mathbf{F}\Delta\theta grows rapidly, signifying a departure from the trust region. By enforcing N init ≫ N ref N_{\text{init}}\gg N_{\text{ref}} (small λ \lambda ), the term ( 1 − λ ) ​ g init (1-\lambda)g_{\text{init}} acts as a regularization term (an ”Anchor”). It ensures that the primary update direction respects the local curvature 𝐅 \mathbf{F} , while g ref g_{\text{ref}} acts as a small perturbation vector that rotates the policy toward higher reward regions without shattering the manifold. ∎

## Appendix G Implementation Details

Datasets and Evaluation Metrics. We use randomly sampled subsets of 4k examples from a reorganized 45k subset ( Yan et al., 2025 ) of OpenR1-Math-220k ( Bakouch et al., 2025 ) as the training set (as described in Section 3 ). For validation, we use the curated validation set provided by ( Yan et al., 2025 ) . We evaluate the model on five well-established mathematical reasoning benchmarks: MATH-500 ( Hendrycks et al., 2021 ) , Minerva-Math ( Lewkowycz et al., 2022 ) , OlympiadBench ( He et al., 2024b ) , AIME 2024 ( Li et al., 2024 ) , AIME 2025 ( Li et al., 2024 ) , and AMC 2023 ( Li et al., 2024 ) . For broader analysis, we assess the model’s generalization ability on three scientific and general reasoning tasks: TheoremQA (Math, Physics, EE&CS, and Finance) ( Chen et al., 2023 ) , GPQA-Diamond (Physics, Chemistry, and Biology) ( Rein et al., 2024 ) , and MMLU-Pro (Business, Computer Science, Law, etc. ) ( Wang et al., 2024 ) . During evaluation, we use greedy decoding (temperature = 0) and report pass@1 over three runs.

Reward Design. During RL fine-tuning, we use model-based evaluation to generate critiques and rule-based evaluation to provide binary scalar rewards, as described in Section 3 .

Compared Methods. We compare Critique-GRPO against the following representative approaches, categorized into supervised learning and reinforcement learning-based finetuning. All differences are considered significant at p < 0.01 p<0.01 .

Supervised Learning-based Finetuning:

( i ) (\textup{i}) Supervised Finetuning (SFT) : Finetuning the base model on high-quality annotated training data using supervised learning.

( ii ) (\textup{ii}) Reward rAnked Finetuning (RAFT) ( Dong et al., 2023 ) : Finetuning on self-generated correct responses, sampled based on rule-based evaluation.

( iii ) (\textup{iii}) Refinement Finetuning (Refinement FT) ( Chen et al., 2024 ) : Finetuning on refined correct responses generated conditionally on the question, initial response, and CoT critiques.

( iv ) (\textup{iv}) Critique Finetuning (Critique FT) ( Wang et al., 2025 ) : Finetuning on annotated CoT critique data to train the model to critique a given query-response.

( v ) (\textup{v}) Critique-in-the-Loop Finetuning (CITL-FT) ( Xi et al., 2024 ) : Finetuning on mixed data consisting of self-generated correct responses and refined correct responses, conditioned on the question-initial response-CoT critique triplet.

Reinforcement Learning-based Finetuning:

( vi ) (\textup{vi}) R1-GRPO ( DeepSeek-AI et al., 2025 ) : Finetuning the base model on its own generations using the GRPO algorithm with binary scalar rewards.

( vii ) (\textup{vii}) R1-Dr.GRPO ( Liu et al., 2025a ) : Finetuning the base model on its own generations using the Dr.GRPO algorithm, which removes terms that cause biased optimization, with binary scalar rewards.

( viii ) (\textup{viii}) Critique-GRPO (Indicative Critique) : Fine-tuning the base model with Critique-GRPO by utilizing indicative critiques for refinements, as described in Appendix E .

( ix ) (\textup{ix}) Critique-GRPO (Critique with Ground Truth) : Fine-tuning the base model with Critique-GRPO by leveraging indicative critiques alongside ground-truth answers for refinements, as detailed in Appendix E .

Implementation Details. We conduct experiments using Qwen2.5-7B-Base, Qwen2.5-Math-7B-Base, and Qwen3-8B, with GPT-4o (which can be replaced by other reasoning-based reward models) serving as the reward model, as described in Section 3 . For supervised finetuning baselines, models are finetuned until convergence, and the best performance is reported. For RL-based approaches, models are finetuned for 400 steps, and the best performance is recorded. To ensure a fair comparison: In R1-GRPO, 8 responses (rollouts) are sampled per training prompt with a temperature of 1. In Critique-GRPO, 7 responses are sampled per prompt, along with one refined response from the refinement sets. we present detailed hyperparameters and training configurations in Table 13 .

All experiments are conducted on 40 NVIDIA A800 80G GPUs. To ensure consistency, we use only critiques generated by the reward model that align with rule-based evaluations; otherwise, the reward model is prompted to regenerate the critiques. Following prior works ( Liu et al., 2025a ) , for evaluation, we adopt greedy sampling (temperature set to 0) to generate responses and report pass@1 as the evaluation metric. When reporting pass@k, we uniformly set the temperature to 0.6 and the top-p value to 0.95.

Compared Methods in the Investigation of Math-Centric Backbone Models. We evaluate the efficacy of RL fine-tuning with Critique-GRPO on the math-centric backbone model, Qwen2.5-Math-7B-Base. Specifically, we compare its performance against three representative RL fine-tuning approaches based solely on numerical feedback:

( i ) (\textup{i}) SimpleRL-Zero ( Zeng et al., 2025 ) : an open-source reproduction of R1-GRPO.

( ii ) (\textup{ii}) PRIME-Zero ( Cui et al., 2025a ) : fine-tuning the base model using both outcome binary rewards and process binary rewards.

( iii ) (\textup{iii}) Oat-Zero ( Liu et al., 2025a ) : fine-tuning the base model with Dr.GRPO using outcome binary rewards.

## Appendix H Detailed Results and Analysis of Self-Critiquing Mechanisms

To explore the potential of Critique-GRPO in enabling an LLM’s self-improvement through self-critiquing, we prompt the model itself to serve as a reasoning-based reward model. Specifically, we investigate two types of self-critiquing: ( i ) (\textup{i}) Self-critique, where the model evaluates the correctness of its own responses using CoT critiques with ground truth answers as reference; and ( ii ) (\textup{ii}) Self-critique & self-evaluation ( Zhang et al., 2024 ) , where the model evaluates its responses using CoT critiques without any reference. These approaches result in Critique-GRPO (self-critique) and Critique-GRPO (self-critique & self-evaluation), respectively. Details of the prompts are provided in Appendix M . Table 14 shows the evaluation results on Qwen3-8B, and Figure 9 presents pass@k performance changes on AIME24 and AIME25 ( Li et al., 2024 ) .

Critique-GRPO enhances self-improvement through self-critiquing. Table 14 RL fine-tuning with Critique-GRPO (self-critique) significantly outperforms fine-tuning with GRPO using external numerical feedback (R1-GRPO) and supervised fine-tuning with expert demonstrations (SFT). On average, Critique-GRPO (self-critique) improves pass@1 by +4.5% and +12.0% compared to R1-GRPO and SFT, respectively. Additionally, the unsupervised approach—Critique-GRPO (self-critique & self-evaluation)—achieves an average pass@1 improvement of 2.3% over R1-GRPO, highlighting the potential of leveraging self-critique for self-improvement without any external supervision .

Self-critiquing aids effective exploration. Figure 9 highlights the consistently superior performance of Critique-GRPO (self-critique) across pass@k metrics, with k k ranging from 1 to 256, indicating genuine improvements. Notably, Critique-GRPO (self-critique) achieves remarkable gains over R1-GRPO for pass@k with k = 1 k=1 to 4 4 , yielding improvements of 10-16.7% on AIME24 (Figure 9(a) ).

## Appendix I Detailed Investigation of Policy Exploration During RL Finetuning

To investigate policy exploration, we analyze two primary aspects of our RL-finetuned models: ( i ) (\textup{i}) entropy dynamics during RL fine-tuning for self-improvement using compared RL-based finetuning approaches on Qwen2.5-7B-Base and Critique-GRPO (self-critique) on Qwen3-8B (Figure 10 ), and ( ii ) (\textup{ii}) changes in response length during fine-tuning (Figure 11 ).

Learning from natural language feedback helps sustain exploration. As shown in Figure 10(a) , the policy entropy of Critique-GRPO generally remains higher than that of R1-GRPO and R1-Dr.GRPO, suggesting more consistent exploration. The peaks in Critique-GRPO’s entropy dynamics (before step 200) likely occur when its self-generated refinements deviate significantly from the initial sampled responses, leading to increased entropy and potentially beneficial distributional shifts. The subsequent decrease in entropy indicates that the model quickly internalizes these refinements, reducing the distributional deviation. This dynamic aligns with the observation that rare actions with high advantage can increase policy entropy ( i.e., unfamiliar but correct responses with high rewards promote effective exploration ), whereas high-probability actions with high advantage tend to reduce entropy ( Cui et al., 2025b ) . In contrast, R1-GRPO exhibits entropy collapse , where policy entropy drops sharply at the start of training and continues to decline monotonically to near zero. R1-Dr.GRPO initially exhibits higher entropy (before step 50) but rapidly drops to comparable near-zero values with R1-GRPO after step 150. Combined with the results in Table 2 , the superior performance of Critique-GRPO over R1-Dr.GRPO and R1-GRPO highlights the importance of maintaining a certain level of entropy for better performance.

Learning through self-critiquing facilitates policy exploration. Figure 10(b) shows that Critique-GRPO (self-critique) avoids entropy collapse and maintains higher entropy than R1-GRPO. This finding aligns with the observation that increased exploration improves performance.

Higher entropy does not always guarantee effective exploration. Unexpectedly, as shown in Figure 10(b) , Critique-GRPO (weaker refinement via critique with ground truth), shown in green, achieves higher entropy than Critique-GRPO (self-critique), shown in dark blue, yet performs worse (average pass@1: 65.55% v.s. 68.13%). This discrepancy may be due to refinements from weaker models causing larger distributional shifts compared to self-refinements, while also being of lower quality. This suggests that the quality of exploration signals is more critical than the extent of exploration (as reflected solely by entropy).

Critique-GRPO facilitates concise reasoning. In Figure 11 , Critique-GRPO achieves superior performance (Table 2 ) while minimally increasing response length on Qwen2.5-7B-Base (Figure 11(a) ). This efficiency likely stems from its critique mechanism, which enables precise error identification and refinement, reducing the need for verbose reasoning. Additionally, Critique-GRPO tends to reduce response length on Qwen3-8B (Figure 11(b) ). This trend can be attributed to the correction of Qwen3-8B’s tendency toward redundant and ineffective self-reflection, as discussed in Appendix J .

## Appendix J Qualitative Analysis

Fine-Grained Analysis. We conduct a fine-grained analysis of 100 generated responses on the Minerva-MATH dataset across four key dimensions: factuality, conciseness, correctness, and logicality, using the prompt in Appendix M . Figure 12 shows that fine-tuning with Critique-GRPO on Qwen2.5-7B-Base achieves the best performance across all four dimensions as well as in average performance. Additionally, the superior performance of RL fine-tuning with Critique-GRPO over R1-GRPO in terms of factuality and correctness indicates that CoT critiques help the model effectively identify errors and improve valid exploration. The inferior performance of SFT in logicality and conciseness may be attributed to the presence of redundant and sometimes illogical self-reflective reasoning behaviors in expert demonstrations, which could negatively impact user experience.

Case Study. We present a qualitative comparison between the responses generated by the base Qwen3-8B model and the RL-finetuned Qwen3-8B model using Critique-GRPO on the MATH-500 dataset. The given question is: Evaluate sin ⁡ ( arcsin ⁡ 0.4 + arcsin ⁡ 0.5 ) , sin ⁡ ( arcsin ⁡ 0.5 − arcsin ⁡ 0.4 ) \sin(\arcsin 0.4+\arcsin 0.5),\sin(\arcsin 0.5-\arcsin 0.4) .

The base Qwen3-8B model produces an incorrect response due to an incorrect formulation of the expression as sin ⁡ ( A + B ) ⋅ sin ⁡ ( A − B ) \sin(A+B)\cdot{\color[rgb]{1,0,0}\sin(A-B)} , as shown in the red square. In contrast, the RL-finetuned Qwen3-8B model using Critique-GRPO generates a correct response by correctly formulating the expression as sin ⁡ ( α + β ) ⋅ sin ⁡ ( β − α ) \sin(\alpha+\beta)\cdot{\color[rgb]{0,1,0}\sin(\beta-\alpha)} , as shown in the green square. Furthermore, the base Qwen3-8B model exhibits numerous redundant and ineffective self-reflection attempts ( e.g., “Wait, …” highlighted in blue), which fail to help the model identify the actual errors and answer the question correctly. This results in an excessively long response (over 6000 tokens). In contrast, the RL-finetuned Qwen3-8B model using Critique-GRPO demonstrates concise and effective reasoning. It remains on the correct path to solve the problem, exhibits valid self-reflection to validate the answer ( e.g., “Let me check with approximate values. …”), and ultimately generates the correct answer. Detailed responses are provided in Appendix O .

## Appendix K Limitations

While Critique-GRPO establishes a promising foundation for leveraging both natural language and numerical feedback, notable limitations remain.

Performance limitations due to failed refinements. Policy models sometimes fail to follow CoT critiques to refine their responses. We attribute this to the lack of deliberate training for self-refinement. An example of a failed refinement is provided in Appendix P . Future work could focus on improving the model’s refinement capabilities or training a specialized model dedicated to refinement tasks.

The role of critique detail in refinement quality. We currently utilize three types of critiques (see Section 3 ), with CoT critiques demonstrating the greatest benefits for refinement. This advantage likely stems from their detailed step-by-step evaluations and concise improvement suggestions, which help models identify and correct errors in initial responses. It follows that more detailed critiques could result in higher-quality refinements. For simplicity, we use GPT-4o as the reasoning-based reward model, not for expert knowledge distillation . Consequently, the generated CoT critiques do not include expert demonstrations. Future work may explore alternative reasoning-based reward models. One might assume that directly incorporating expert demonstrations into critiques would significantly improve performance. However, our experiments reveal otherwise. Upon analyzing the generated refinements, we observe that both pre-trained models ( e.g., Qwen2.5-7B-Base) and alignment-tuned models ( e.g., Qwen3-8B) tend to produce conclusive sentences and correct answers as refinements, rather than detailed step-by-step reasoning to derive the correct answer. This behavior limits the effectiveness of expert demonstrations as critiques.

Future work could investigate, in greater depth, which types of critiques provide the most significant benefits for refinement, particularly in reasoning-intensive tasks.

## Appendix L Analysis of Cognitive Behaviors

To systematically investigate this question, we characterize six key cognitive behaviors that contribute to self-improving reasoning during RL fine-tuning, as follows: • Subgoal Setting : Breaking down complex problems into smaller, manageable steps or subtasks. For example, “Step 1… Step 2…”

• Summarization : Summarizing the current state by identifying completed subtasks and determining what remains to be done. This helps guide the next steps in reasoning. For example, “Now we have obtained…, next, we need to…”

• Verification : Systematically checking intermediate results or computations to ensure correctness. For example, “Let’s verify this result by…”

• Backtracking : Identifying errors or dead-ends in reasoning and explicitly revising previous methods or approaches. For example, “This approach won’t work because…, let’s try another method…”

• Backward Chaining : Reasoning from desired outcomes back to initial inputs or steps required to achieve the result. This is particularly applicable to multiple-choice questions where answer options are provided. For example, “To get 24, I could do 24 ÷ 2 = 12…” ( Gandhi et al., 2025 )

• Anticipation : Anticipating potential inaccuracies or exhaustively considering multiple possibilities to solve a problem. For example, “Alternatively, this problem can be solved by…”

We analyze the reasoning (cognitive) behaviors using the prompts shown below.

When assessing the contributions of reasoning behaviors in Section 3 to successful problem-solving in RL fine-tuned models, we count each behavior appearing in the generated responses only once . For example, if the model produces multiple subgoals in a single response, the occurrence of “subgoal setting” is counted as one.

## Appendix M Prompts

##### Training Prompt.

The following training prompt is used during all RL fine-tuning experiments:

##### Prompt for Generating Chain-of-Thought Critique.

We adopt a prompt inspired by ( Wang et al., 2025 ) to enable GPT-4o ( Hurst et al., 2024 ) to generate CoT critiques. For quality control, we retained only those model-generated critiques whose evaluative conclusions (correct/incorrect) aligned with rule-based verification. When inconsistencies occurred, we prompted the critique model to regenerate the critiques.

##### Prompt for Generating Chain-of-Thought Critique with Internal Knowledge

The following prompt is designed to enable an LLM to leverage its internal knowledge and evaluate the correctness of its own generated responses through step-by-step CoT critiques.

##### Refinement Prompt.

The following refinement prompt is used to guide the model in improving its response by incorporating the critique.

Future work could explore designing prompts ( Zhang et al., 2023 ) to enable LLMs to generate high-quality CoT critiques.

##### Prompt for Qualitative Analysis.

We employ the following prompt to conduct qualitative analysis of the generated responses using GPT-4o.

## Appendix N An Example of Successful Refinement using a CoT Critique

The example below demonstrates a successful refinement using a CoT critique. This output was generated by the best-performing RL-finetuned Qwen3-8B model using GRPO algorithm in Section 3 , utilizing the refinement prompt detailed in Appendix N .

## Appendix O Responses Utilized in Qualitative Analysis

## Appendix P An Example of Failed Refinement

The following example demonstrates a failed refinement using a CoT critique, where RL-finetuned Qwen3-8B using Critique-GRPO fails to follow the critique to refine its responses.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
