##### Report GitHub Issue

Content selection saved. Describe the issue below:

# MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory

###### Abstract

The hallmark of human intelligence is the self-evolving ability to master new skills by learning from past experiences. However, current AI agents struggle to emulate this self-evolution: fine-tuning is computationally expensive and prone to catastrophic forgetting, while existing memory-based methods rely on passive semantic matching that often retrieves noise. To address these challenges, we propose MemRL , a non-parametric approach that evolves via reinforcement learning on episodic memory. By decoupling stable reasoning from plastic memory, MemRL employs a Two-Phase Retrieval mechanism to filter noise and identify high-utility strategies through environmental feedback. Extensive experiments on HLE, BigCodeBench, ALFWorld, and Lifelong Agent Bench demonstrate that MemRL significantly outperforms state-of-the-art baselines, confirming that MemRL effectively reconciles the stability-plasticity dilemma, enabling continuous runtime improvement without weight updates. Code is available at https://github.com/MemTensor/MemRL .

###### Keywords:

## 1 Introduction

Human intelligence balances cognitive stability and episodic plasticity ( Grossberg, 2013 ; McClelland et al., 1995 ; Kumaran et al., 2016 ) via Constructive Episodic Simulation, enabling adaptation without rewiring neural circuitry ( Schacter and Addis, 2007 ; Hassabis and Maguire, 2007 ; Schacter et al., 2012 ; Gick and Holyoak, 1980 ) . Despite their reasoning capabilities, current AI agents struggle to emulate this decoupled self-evolution ( Wei et al., 2022 ; Yao et al., 2023 ; Schick et al., 2023 ; Wang et al., 2023 ) . Specifically, fine-tuning internalizes experience by modifying weights ( Ouyang et al., 2022 ; Stiennon et al., 2020 ; Rafailov et al., 2023 ; Ethayarajh et al., 2024 ) but suffers from computational costs and catastrophic forgetting ( Kirkpatrick et al., 2017 ; Li et al., 2024 ; Wu et al., 2024 ) . Conversely, Retrieval-Augmented Generation (RAG) ( Lewis et al., 2020 ) provides a non-parametric alternative but remains passive, retrieving by semantic similarity rather than utility ( Karpukhin et al., 2020 ; Gao et al., 2024 ) ; this prevents agents from effectively leveraging runtime feedback to distinguish high-value strategies from noise.

This limitation underscores a critical research question: How can we enable an agent to continuously improve its performance after deployment, without compromising the stability of its pre-trained backbone? Our objective is to achieve an agent that evolves with continued usage and rapidly adapts to new tasks after deployment, referred to as Runtime Continuous Learning ( Javed et al., 2023 ; Silver and Sutton, 2025 ; Parisi et al., 2019 ; Wu et al., 2024 ) , all while keeping the backbone model frozen to prevent catastrophic forgetting ( Finn et al., 2017 ; Wei et al., 2025 ) . To address this challenge, inspired by the human cognitive mechanism of constructive simulation, we propose MemRL , an approach that facilitates self-evolving agents by explicitly decoupling the model’s stable cognitive reasoning from dynamic episodic memory. Figure 1 illustrates the conceptual framework of our proposed MemRL . Drawing on tries-and-errors manner in Reinforcement Learning (RL) to estimate expected experience utilities ( Sutton and Barto, 2018 ) , we formalize the interaction between the frozen LLM and external memory as a Markov Decision Process (MDP) ( Puterman, 2014 ) . Unlike traditional methods that optimize the backbone model, MemRL optimizes the policy of memory usage without tuning model weights.

MemRL organizes memory into a structured Intent-Experience-Utility triplet. This structure transforms retrieval from a passive semantic match task into an active decision-making process: Two-Phase Retrieval selects experiences based on their learned Q-values, reflecting expected utility, rather than semantic similarity alone ( Watkins and Dayan, 1992 ) ; Utility-Driven Update refines these Q-values through environmental feedback, applying Monte Carlo style updates ( Metropolis and Ulam, 1949 ) . This closed-loop cycle enables the agent to distinguish high-value memories from similar noise, effectively learning from both success and failure without high computational cost or catastrophic forgetting risks associated with weight updates. As for experiments, we validate MemRL on four diverse benchmarks, including HLE, BigCodeBench, ALFWorld, and Lifelong Agent Bench. Our results demonstrate consistent superiority over baselines, achieving relative improvement in exploration-heavy environments. Our in-depth analysis reveals a strong correlation between learned utility and task success, further confirming MemRL ’s effectiveness.

In summary, our contributions are threefold: • We propose a runtime learning framework using Model-Memory decoupling and Intent-Experience-Utility triplet to reconcile the stability-plasticity dilemma, enabling tuning-free agent learning.

• We introduce MemRL , a non-parametric approach enabling agent self-evolution via Two-Phase Retrieval and Utility-Driven Update.

• We conduct extensive evaluations and provide a rigorous analysis for MemRL ’s stability, showing how it ensures task integrity and minimizes forgetting.

## 2 Related Works

##### Runtime Learning

Runtime Learning focuses on the post-deployment improvement of agents through interaction streams rather than offline data, marking a shift toward the “era of experience” ( Silver and Sutton, 2025 ) . Unlike Continual Learning ( Parisi et al., 2019 ; Wu et al., 2024 ) or Test-Time Adaptation ( Sun et al., 2020 ; Wang et al., 2020 ; Liang et al., 2025 ) , which typically update parameters to handle forgetting or distribution shifts, our setting constrains the backbone to remain frozen to ensure stability and efficiency. While recent memory-augmented agents ( Zheng et al., 2025 ; Wei et al., 2025 ; Zhou et al., 2025b ) emphasize memory organization, the selection problem—identifying which experiences to reuse under feedback—remains a critical challenge. Drawing from value-aware episodic control ( Tulving and others, 1972 ; McClelland et al., 1995 ) , we frame runtime learning as identifying valuable episodes. By using interaction feedback to assign utility, our approach guides retrieval and reuse without weight modification, thereby ensuring sustained improvement ( Pritzel et al., 2017 ) .

##### Reinforcement Learning

Reinforcement learning has been widely adopted for LLMs enhancement. A representative paradigm is to construct reward signals from human feedback and optimize the model policy accordingly to align with human preference ( Stiennon et al., 2020 ; Ouyang et al., 2022 ) . Other recent approaches leverage rule-based verifiers to improve LLMs’ reasoning capabilities ( Guo et al., 2025 ; Yu et al., 2025 ) . In parallel, agent-oriented research explores how interaction signals can improve tool use and action decision-making, and investigates mechanisms by which language models execute composite actions in environments ( Schick et al., 2023 ) . Despite the demonstrated effectiveness of reward-driven optimization, these methods generally place learning in the model parameters or additional parametric modules, and thus do not avoid the cost of online updates or the risk of forgetting. In contrast, our method frames memory usage as a learnable decision problem and applies non-parametric reinforcement learning on memory to bypass the risk.

##### Agentic Memory

To avoid the costs of fine-tuning, external memory systems have evolved from a static RAG paradigm to dynamic, governable memory structures ( Lewis et al., 2020 ; Karpukhin et al., 2020 ) . Early agentic memory introduced reflection mechanisms and hierarchical management to handle long context experiences ( Shinn et al., 2023 ; Packer et al., 2024 ) . More recent frameworks have systematized the memory lifecycle, focusing on unified storage and structured indexing for complex tasks ( Li et al., 2025b ; Xu et al., 2025 ; Huang et al., 2025 ; Ye, 2025 ) . Furthermore, adaptive approaches now explore improving retrieval via feedback-driven updates or automated augmentation ( Salama et al., 2025 ; Zhang et al., 2025 ; Li et al., 2025a ; Zhou et al., 2025a ) . However, except for training additional learnable modules, most existing methods still rely predominantly on semantic similarity or heuristic rules, lacking a rigorous metric to evaluate the actual utility of a memory in maximizing returns. Inspired by cognitive theories of memory reconsolidation ( Schacter and Addis, 2007 ; Gick and Holyoak, 1980 ; Nader et al., 2000 ) , MemRL bridges this gap by formulating retrieval as a value-based decision process, learning robust utility estimates (Q-values) from environmental rewards to distinguish high-value experiences.

## 3 Problem Formulation

In this section, we formally define the problem of memory-augmented generation and establish the theoretical link between agent policy and memory retrieval. We adopt the formulation of Memory-Based Markov Decision Process (M-MDP) ( Zhou et al., 2025a ) , and apply our non-parametric reinforcement learning approach to it. Figure 2 provides an illustrative example of this memory-augmented decision process, showing how retrieval outcomes and memory evolution unfold over multiple time steps.

### 3.1 Memory-Augmented Agent Policy

To enable the agent to self-evolution, we adopt the M-MDP framework ( Zhou et al., 2025a ) , defined by the tuple ( 𝒮 , 𝒜 , P , ℛ , γ , ℳ ) (\mathcal{S},\mathcal{A},P,\mathcal{R},\gamma,\mathcal{M}) . Here, 𝒮 \mathcal{S} and 𝒜 \mathcal{A} represent state and action spaces, P P is the transition dynamics, ℛ \mathcal{R} is the reward function of state and action, γ ∈ [ 0 , 1 ) \gamma\in[0,1) denotes the discount factor, and ℳ = ( 𝒮 × 𝒜 × ℝ ) ∗ \mathcal{M}=(\mathcal{S}\times\mathcal{A}\times\mathbb{R})^{*} constitutes the evolving memory bank of past experiences ( Zhou et al., 2025a ) . At each step t t , the agent receives state s t s_{t} and leverages ℳ t \mathcal{M}_{t} to generate a response a t a_{t} maximizing the expected reward. The joint policy π ⁡ ( a t | s t , ℳ t ) \pi(a_{t}|s_{t},\mathcal{M}_{t}) is formulated as the marginal probability over all possible retrieved items m m ( Zhou et al., 2025a ) : π ⁡ ( a t | s t , ℳ t ) = ∑ m ∈ ℳ t μ ⁡ ( m | s t , ℳ t ) ​ p L ​ L ​ M ​ ( a t | s t , m ) . \pi(a_{t}|s_{t},\mathcal{M}_{t})=\sum_{m\in\mathcal{M}_{t}}\mu(m|s_{t},\mathcal{M}_{t})p_{LLM}(a_{t}|s_{t},m). (1) where μ ⁡ ( m | s t , ℳ t ) \mu(m|s_{t},\mathcal{M}_{t}) is the Retrieval Policy for selecting memory contexts, and p L ​ L ​ M ​ ( a t | s t , m ) p_{LLM}(a_{t}|s_{t},m) is the Inference Policy parameterized by a frozen LLM. This approach transforms retrieval from a passive match into an active decision process, effectively accounting for the functional utility of m m in generating successful outcomes a t a_{t} .

In previous RAG or memory-based agentic paradigms, the retrieval policy μ \mu is usually determined by a fixed vector similarity metric, e.g., cosine similarity of embeddings. While effective for semantic matching, such policies fail to account for the utility of a memory, i.e., whether retrieving m m actually leads to a successful outcome a t a_{t} .

### 3.2 Non-Parametric Reinforcement Learning

To overcome static similarity limitations, we operationalize the M-MDP framework by formulating memory retrieval as a value-based decision-making process ( Zhou et al., 2025a ) . Unlike parametric methods optimizing π L ​ L ​ M \pi_{LLM} via weight updates, we optimize the retrieval policy μ ⁡ ( m | s , ℳ ) \mu(m|s,\mathcal{M}) directly within the memory space by mapping M-MDP components to a structured Intent-Experience-Utility triplet:

From Semantic Matching to Decision Making. We instantiate state s s as the User Intent, encapsulated by the current query embedding ( Lewis et al., 2020 ) . Consequently, the action space 𝒜 t \mathcal{A}_{t} becomes dynamic and discrete, corresponding to selecting a specific m m from the memory bank ℳ t \mathcal{M}_{t} ( Zhou et al., 2025a ) . In this formulation, retrieval is not a passive matching task but a strategic decision step taken to augment the generator’s action a a ( Zhou et al., 2025a ) .

Defining Utility via Q-Values. While the agent’s executable action a a is generated by the policy π \pi (as formalized in Sec. 3.1 ), the quality of this generation is strictly conditioned on the retrieved context. Therefore, we adapt the traditional value function Q ⁡ ( s , a ) Q(s,a) to the retrieval phase, defining Q ⁡ ( s , m ) Q(s,m) as the expected utility of the subsequent action a a augmented by memory m m . MemRL learns an optimal retrieval policy μ ∗ \mu^{*} that maximizes this utility: μ ∗ ​ ( m | s , ℳ ) = arg ⁡ max m ∈ ℳ ⁡ Q ⁡ ( s , m ) . \mu^{*}(m|s,\mathcal{M})=\arg\max_{m\in\mathcal{M}}Q(s,m). (2) In this view, the Q-value acts as a critic for the retrieval mechanism, distinguishing memories that strategically aid the generator from irrelevant noise that merely shares high semantic similarity.

Non-Parametric Learning. Since the retrieval action space is decoupled from LLM generation, we perform learning without modifying model weights. Upon receiving environmental feedback r r , we update the Q-value via a Temporal-Difference (TD) error ( Sutton, 1988 ) : Q ⁡ ( s , m ) ← Q ⁡ ( s , m ) + α ⁡ [ r + γ ​ max ⁡ Q ⁡ ( s ′ , m ′ ) − Q ⁡ ( s , m ) ] , Q(s,m)\leftarrow Q(s,m)+\alpha[r+\gamma\max Q(s^{\prime},m^{\prime})-Q(s,m)], (3) or Monte Carlo style rule ( Metropolis and Ulam, 1949 ) : Q new ← Q old + α ⁡ ( r − Q old ) , Q_{\text{new}}\leftarrow Q_{\text{old}}+\alpha\big(r-Q_{\text{old}}\big), (4) where α \alpha is the learning rate. Equation 4 performs as a naturally simplified version of Equation 3 by setting s ′ s^{\prime} as a terminal state to balance complexity and performance, sharing a similar one-step MDP formulation with Guo et al. (2025) . These manners allow utility estimates to converge to true expected returns over time ( Bellman, 1966 ) . By explicitly updating Q-values within the memory structure, MemRL provides a non-parametric learning manner with a theoretical guarantee, enabling agents to self-evolve through interaction.

## 4 MemRL

Building upon the M-MDP formulation defined in Section 3 , we propose MemRL , a framework that enables frozen LLMs to self-evolve via non-parametric reinforcement learning. Instead of modifying the model weights θ \theta , MemRL optimizes the retrieval policy μ ⁡ ( m | s , ℳ ) \mu(m|s,\mathcal{M}) within an evolving memory space. As illustrated in Figure 3 , the framework consists of three core components: (i) a structured Intent-Experience-Utility memory bank, (ii) a Two-Phase Retrieval mechanism that decouples semantic recall from value-aware selection, and (iii) a Runtime Utility Update rule that stabilizes Q-value estimation.

### 4.1 The Intent-Experience-Utility Triplet

To support value-based decision-making, we structure the external memory ℳ \mathcal{M} not merely as key-value pairs, but as a set of triplets: ℳ = { ( z i , e i , Q i ) } i = 1 | ℳ | , \mathcal{M}=\{(z_{i},e_{i},Q_{i})\}_{i=1}^{|\mathcal{M}|}, (5) where z i z_{i} represents the Intent , e i e_{i} stores the raw Experience (e.g., a successful solution trace or trajectory), and Q i Q_{i} denotes the learned Utility . Q i Q_{i} approximates the expected return of applying experience e i e_{i} to intents similar to z i z_{i} , serving as the critic in RL.

### 4.2 From Semantic Recall to Value-Aware Selection

Standard RAG systems assume “similar implies useful,” but agentic tasks often involve environment-specific routines that generalize poorly ( Singh et al., 2025 ; Cuconasu et al., 2024 ; Gan et al., 2024 ; Zhou et al., 2024 ) . Therefore, MemRL implements a Two-Phase Retrieval strategy. Phase A: Similarity-Based Recall. Given query s s , we isolate a candidate pool 𝒞 ⁡ ( s ) \mathcal{C}(s) of semantically consistent experiences by filtering memory bank ℳ \mathcal{M} via cosine similarity and a sparsity threshold δ \delta : 𝒞 ⁡ ( s ) = TopK k 1 ​ ( { i | s ​ i ​ m ​ ( E ​ m ​ b ​ ( s ) , E ​ m ​ b ​ ( z i ) ) > δ } ) , \mathcal{C}(s)=\text{TopK}_{k_{1}}(\{i|sim(Emb(s),Emb(z_{i}))>\delta\}), (6) where E ​ m ​ b Emb represents the Embedding Model to transfer the raw text to a vector. If 𝒞 ⁡ ( s ) = ∅ \mathcal{C}(s)=\emptyset , MemRL relies solely on the frozen LLM for exploration. Phase B: Value-Aware Selection. To determine the final context ℳ c ​ t ​ x ​ ( s ) \mathcal{M}_{ctx}(s) , we select top- k 2 k_{2} items from 𝒞 ⁡ ( s ) \mathcal{C}(s) using a composite score balancing exploration (similarity) and exploitation (utility Q Q ): score ​ ( s , z i , e i ) = ( 1 − λ ) ⋅ s ​ i ​ m ^ ​ ( E ​ m ​ b ​ ( s ) , E ​ m ​ b ​ ( z i ) ) + λ ⋅ Q i ^ . \text{score}(s,z_{i},e_{i})=(1-\lambda)\cdot\hat{sim}(Emb(s),Emb(z_{i}))+\lambda\cdot\hat{Q_{i}}. (7) where ⋅ ^ \hat{\cdot} denotes z-score normalization and λ ∈ [ 0 , 1 ] \lambda\in[0,1] modulates the trade-off. This mechanism filters out “distractor” memories—those semantically similar but with low historical utility. As detailed in Section 5.4.2 , normalization and strict similarity thresholds are essential for noise filtering and maintaining stability during self-evolution.

### 4.3 Non-Parametric RL on Memory

The core of MemRL is the continuous refinement of Q-values based on environmental feedback, enabling the agent to “remember” what works. During runtime, MemRL performs learning entirely in memory space. With the retrieved context m m , the agent samples an action a a according to the policy π \pi defined in Eq. 1 . Executing a a then yields an environmental reward r r (e.g., execution success or scalar score). For the memories actually injected into the input context ℳ ctx ​ ( s ) \mathcal{M}_{\text{ctx}}(s) , we update their utilities in triplets with a Monte Carlo style rule, i.e., the Eq. 4 , following the runtime learning loop shown in Figure 3 . This update drives Q new Q_{\text{new}} toward the empirical expected return of using experience e i e_{i} under similar intents. Meanwhile, for each sampled trajectory, we use an LLM to summarize the experience ( Fang et al., 2025 ) , and write it back into the memory bank as a new triplet ( z , e new , Q init ) (z,e_{\text{new}},Q_{\text{init}}) , enabling continual expansion of experience while keeping the LLM parameters unchanged.

### 4.4 Theoretical Stability Analysis

We analyze the stability of MemRL from a reinforcement learning perspective, with full analysis provided in Appendix A . We posit two standard assumptions: a frozen inference policy p LLM p_{\mathrm{LLM}} and a stationary task distribution. Under these conditions, the learning target β ( s , m ) = 𝔼 [ r t | s , m ] \beta(s,m)=\mathbb{E}[r_{t}|s,m] is well-defined, where the expectation is taken over the stochastic rewards resulting from the Inference Policy p L ​ L ​ M p_{LLM} distribution. We prove that utility estimates updated via Eq. 4 are unbiased and variance-bounded ( Sutton and Barto, 2018 ) . Specifically, as t → ∞ t\to\infty : lim t → ∞ 𝔼 ⁡ [ Q t ] \displaystyle\lim_{t\to\infty}\mathbb{E}[Q_{t}] = β ⁡ ( s , m ) , \displaystyle=\beta(s,m), (8) lim sup t → ∞ Var ⁡ ( Q t ) \displaystyle\limsup_{t\to\infty}\mathrm{Var}(Q_{t}) ≤ α 2 − α ​ Var ​ ( r t ∣ s , m ) . \displaystyle\leq\frac{\alpha}{2-\alpha}\mathrm{Var}(r_{t}\mid s,m).

Furthermore, we address the challenge of the latent retrieval distribution Pr ⁡ ( s | m ) \Pr(s|m) shifting during training by framing MemRL as a Generalized Expectation-Maximization (GEM) ( Dempster et al., 1977 ) process. The system performs coordinate ascent on a global objective: the retrieval ranking acts as the Policy Improvement (E-step), while the utility update acts as the Value Update (M-step). By the monotonic improvement theorem ( Neal and Hinton, 1998 ) , the system converges to a stationary point where the global memory utility stabilizes: lim t → ∞ 𝔼 [ Q t ( m ) ] = ∑ s ∈ 𝒮 ⁡ ( m ) 𝔼 [ r | s , m ] Pr ( s | m ) . \lim_{t\to\infty}\mathbb{E}[Q_{t}(m)]=\sum_{s\in\mathcal{S}(m)}\mathbb{E}[r|s,m]\Pr(s|m). (9) where 𝒮 ⁡ ( m ) \mathcal{S}(m) is the effective support set of the memory. This formulation guarantees global stability and prevents catastrophic forgetting. Details can be found in Appendix A.4 .

## 5 Experiments

### 5.1 Experimental Setup

Baselines & Benchmarks. We compare MemRL against RAG-based (RAG, Self-RAG), Agentic Memory (Mem0, MemP), and Test-Time Scaling (Pass@ k k ) baselines under a frozen-backbone setting (see Appendix D.1 ). Evaluations span four domains: BigCodeBench (coding), ALFWorld (navigation), LifelongAgent Bench (OS/DB), and Humanity’s Last Exam(HLE). Details are in Appendix D.2 . Backbones are selected per benchmark to avoid no-signal or ceiling problems, ensuring valid learning signals, while Appendix E.4 provides a unified comparison to demonstrate cross-task consistency under identical capacity.

Metrics. We employ two metrics: (1) Success Rate (SR) , the ratio of tasks completed in an epoch; (2) Cumulative Success Rate (CSR) , the proportion of tasks solved at least once across epochs.

We evaluate our MemRL and baselines under two distinct settings: Runtime Learning , which assesses the ability to learn and adapt within a training session, and Transferring , which evaluates the generalization capability of the learned memory on unseen tasks. Implementation and reproducibility details, including all prompts used in our experiments, can be found in Appendix E and Appendix I .

### 5.2 Main Results

##### Runtime Learning Results.

As detailed in Table 1 , MemRL demonstrates robust superiority across all domains, surpassing the strongest baseline (MemP) by an average of + 3.8 % +3.8\% in Cumulative Success Rate (CSR). The gains are most significant in exploration-intensive environments like ALFWorld and OS tasks (both + 6.2 % +6.2\% ), while maintaining a steady lead on the challenging HLE benchmark ( + 3.6 % +3.6\% ). This confirms that our value-based mechanism, unlike MemP’s heuristic retrieval, effectively filters noise to retain high-utility procedural patterns.

##### Transferring Results.

We evaluate memory transferability by freezing the memory bank after training and testing on held-out sets. As shown in Table 2 , MemRL exhibits superior transferability, outperforming the strongest baseline (MemP) by an average of + 2.8 % +2.8\% in Success Rate. The advantage is particularly pronounced in complex environments like ALFWorld ( + 5.8 % +5.8\% ) and OS tasks ( + 2.6 % +2.6\% ). These margins validate that our Two-Phase Retrieval effectively filters low-value noise, retaining high-utility procedural patterns that generalize robustly to unseen scenarios.

### 5.3 Ablations

#### 5.3.1 Effectiveness of Runtime RL

To isolate the efficacy of runtime RL, we compare MemRL and its RAG-based variant against their non-RL counterparts (MemP and standard RAG) in the OS interaction environment. As shown in Figure 4 , while initial performance is comparable, a clear divergence emerges as training progresses: MemRL achieves a smoother learning curve and superior stability. Crucially, this advantage is most pronounced in the Cumulative Success Rate (dashed lines), where the monotonic widening gap indicates that the RL-driven value function effectively filters noisy memories and consolidates successful experiences.

#### 5.3.2 Impact of Q-Value Weighting

To determine the optimal equilibrium between semantic grounding and value-based exploitation, we evaluate the Q-weighting factor λ ∈ { 0 , 0.25 , 0.5 , 0.75 , 1 } \lambda\in\{0,0.25,0.5,0.75,1\} . As shown in Figure 5 , performance exhibits a clear concave trend peaking at λ = 0.5 \lambda=0.5 . Deviating toward extremes degrades results: pure semantic retrieval ( λ = 0 \lambda=0 ) plateaus due to an inability to filter functional distractors, while excessive RL weight ( λ → 1 \lambda\to 1 ) induces volatility and context detachment. This confirms that λ = 0.5 \lambda=0.5 represents an effective balance, where semantic similarity guarantees content relevance and Q-value ensures its helpfulness.

#### 5.3.3 Ablation Analysis: Cross-Task vs. Single-Task Optimization

To investigate the source of our performance gains, we conduct an ablation study in Table 3 by restricting the memory retrieval scope. We compare the full MemRL ( Cross-Task Retrieval ) against an ablated setting that only utilizes feedback from the single task instance, conceptually equivalent to Reflexion ( Shinn et al., 2023 ) . MemRL demonstrates superior performance in structured environments, particularly on OS-Agent ( + 9.0 % +9.0\% ) and ALFWorld ( + 5.1 % +5.1\% ). These benchmarks exhibit high intra-dataset similarity, allowing MemRL to effectively perform horizontal transfer —retrieving and adapting successful policies from semantically similar historical tasks. While on the HLE benchmark, the single-task baseline ( 0.610 0.610 ) is tied with MemRL ( 0.606 0.606 ). We attribute this to the HLE dataset’s low internal semantic similarity ( 0.186 0.186 ), as detailed in Appendix B.3 . This prevents effective cross-task generalization, forcing the agent to rely solely on single feedback.

#### 5.3.4 Sensitivity to Retrieval Size ( k 1 k_{1} and k 2 k_{2} ).

To investigate the impact of retrieval bandwidth, we compare three memory density configurations on the HLE (CS/AI) subset benchmark: sparse ( k 1 = 3 , k 2 = 1 k_{1}=3,k_{2}=1 ), moderate ( k 1 = 5 , k 2 = 3 k_{1}=5,k_{2}=3 ), and dense ( k 1 = 10 , k 2 = 5 k_{1}=10,k_{2}=5 ). As shown in Figure 6 , performance follows an inverted-U trajectory, illustrating the trade-off between information sufficiency and context noise. The sparse setting limits performance due to insufficient guidance, whereas the dense setting degrades success rate by introducing distractions into the reasoning context. Consequently, the moderate configuration ( k 1 = 5 , k 2 = 3 k_{1}=5,k_{2}=3 ) achieves the best result, effectively maximizing the signal-to-noise ratio of the retrieved context.

### 5.4 Discussion

In this section, we delve deeper into the mechanisms driving MemRL ’s performance, connecting empirical results to the challenge of balancing knowledge retention and adaptation.

#### 5.4.1 Predictive Power of the Q Critic

As shown in Figure 7(a) , the learned Q-values exhibit a strong positive correlation (Pearson r = 0.861 r=0.861 ) with empirical task success rates, rising from 21.5 % 21.5\% in the lowest-confidence bin to 88.1 % 88.1\% in the highest, which confirms the Critic’s ability to effectively rank memories by success likelihood. Beyond simple ranking, memory composition analysis (Figure 7(b) ) reveals that the agent retains a small fraction of “failure” memories ( ∼ 12 % \sim 12\% ) even in high-Q bins ( 0.9 − 1.0 0.9-1.0 ), suggesting that Q-values capture utility beyond binary outcomes by recognizing strategically useful near-misses. We further substantiate this with concrete case studies in Appendix H . This indicates that the Critic prioritizes reusable guidance—including transferable procedural lessons from high-utility failures—rather than merely separating success from failure, thereby offering greater robustness than simple success-replay mechanisms.

#### 5.4.2 Stability of MemRL

We analyze MemRL through the lens of the stability-plasticity dilemma . The superior CSR (Table 1 ) confirms that MemRL effectively expands the solution space, enabling the agent to break through local optima. Furthermore, long-term dynamics (Figure 8 ) reveal a critical stability advantage: while heuristic methods like MemP suffer from catastrophic forgetting—evidenced by a widening gap between CSR and current Success Rate— MemRL maintains synchronized growth. This is theoretically guaranteed by our stability analysis in Section 4.4 , which constrains the policy to improve monotonically without drift.

We quantitatively validate these insights using the Forgetting Rate , defined as F ​ R = N lost / N fail FR=N_{\text{lost}}/N_{\text{fail}} , where N lost N_{\text{lost}} denotes tasks transitioning from previous success to current failure and N fail N_{\text{fail}} is the total number of failures in the current epoch (see Figure 9 in Appendix B.1 for the full trajectory). MemRL achieves the lowest mean forgetting rate ( 0.041 0.041 ), outperforming MemP ( 0.051 0.051 ). Additionally, ablation results demonstrate that removing z-score normalization and similarity gating causes the rate to spike to 0.073 0.073 . This confirms that strict filtering is essential to manage utility variance and ensure that self-evolution remains stable.

#### 5.4.3 Extended Analysis.

We conduct further investigations to characterize the underlying mechanisms and generalization of MemRL . Specifically, Appendix B analyzes MemRL ’s role as a structural trajectory verifier and the correlation between task similarity and performance gains. Additionally, evaluations of advanced capabilities—including cross-model memory transferability and modular multi-task merging—are detailed in Appendix C , demonstrating MemRL ’s versatility and its capacity for modular capability expansion. We also analyze the cost and efficiency of MemRL in Appendix F .

## 6 Limitations and Conclusion

##### Limitations and Future Work.

While MemRL establishes a foundation for non-parametric evolution, its runtime dynamics reveal several promising avenues. (i) The current step-wise update, though fast, may introduce high-variance noise in long-horizon trajectories, inspiring us to explore multi-step updates or periodic memory consolidation. (ii) Credit-assignment ambiguity during utility updates, especially with multiple referenced experiences, raises the need for more precise attribution methods like Shapley methods ( Shapley and others, 1953 ) or value decomposition in multi-agent reinforcement learning ( Rashid et al., 2020 ; Sunehag et al., 2017 ) . (iii) While MemRL improves with increasing task exposure, performance may drift toward reflection-like behavior when task similarity is low, highlighting the need for a sufficiently diverse yet relevant experience base; for industrial deployment, ensuring high task density and hierarchical abstraction may be crucial. Further detailed discussions on these and other challenges, including memory security, dedicated domains, and multi-agent memory sharing, are provided in Appendix G .

##### Conclusion.

We proposed MemRL , a non-parametric approach reconciling the stability-plasticity dilemma by treating memory retrieval as a value-based decision process. Through the Intent-Experience-Utility triplet structure and Monte Carlo style updates, MemRL enables agents to self-evolve and differentiate high-utility strategies from semantic noise without weight updates. Extensive evaluations confirm MemRL significantly outperforms baselines in both runtime adaptation and generalization. In a future where static training data becomes scarce, the interactive experiences generated by agents throughout their life cycle will become a new, vital source of knowledge. We hope this paradigm paves the way for building stable, continuously learning agents that efficiently adapt from interaction.

## Impact Statement

This paper presents MemRL , a value-reinforced memory retrieval mechanism designed to enhance the long-term reasoning capabilities of LLM Agents. From a broader perspective, our work contributes to the development of more efficient and reliable autonomous systems. By optimizing the memory retrieval process, MemRL reduces the computational overhead of large-scale agent deployments, potentially lowering the environmental impact of AI infrastructure. Furthermore, as LLM agents become more integrated into daily workflows, research into robust memory mechanisms helps ensure these systems remain grounded and consistent in their actions. We do not foresee any immediate negative social consequences specific to this algorithmic advancement, though we acknowledge that all autonomous systems should be deployed with appropriate human oversight to mitigate broader risks associated with AI decision-making.

## References

Asai et al. (2023) A. Asai, Z. Wu, Y. Wang, A. Sil, and H. Hajishirzi Self-rag: learning to retrieve, generate, and critique through self-reflection . External Links: 2310.11511 , Link Cited by: 2nd item .

Bellman (1966) R. Bellman Dynamic programming . science 153 ( 3731 ), pp. 34–37 . Cited by: §3.2 .

Chhikara et al. (2025) P. Chhikara, D. Khant, S. Aryan, T. Singh, and D. Yadav Mem0: building production-ready ai agents with scalable long-term memory . External Links: 2504.19413 , Link Cited by: 1st item .

Cuconasu et al. (2024) F. Cuconasu, G. Trappolini, F. Siciliano, S. Filice, C. Campagnano, Y. Maarek, N. Tonellotto, and F. Silvestri The power of noise: redefining retrieval for rag systems . In Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval , SIGIR 2024 , pp. 719–729 . External Links: Link , Document Cited by: §4.2 .

Dempster et al. (1977) A. P. Dempster, N. M. Laird, and D. B. Rubin Maximum likelihood from incomplete data via the em algorithm . Journal of the Royal Statistical Society. Series B (Methodological) 39 ( 1 ), pp. 1–38 . External Links: ISSN 00359246 , Link Cited by: §A.1 , §4.4 .

Ethayarajh et al. (2024) K. Ethayarajh, W. Xu, N. Muennighoff, D. Jurafsky, and D. Kiela Kto: model alignment as prospect theoretic optimization . arXiv preprint arXiv:2402.01306 . Cited by: §1 .

Fang et al. (2025) R. Fang, Y. Liang, X. Wang, J. Wu, S. Qiao, P. Xie, F. Huang, H. Chen, and N. Zhang Memp: exploring agent procedural memory . arXiv preprint arXiv:2508.06433 . External Links: Link Cited by: 2nd item , §4.3 .

Finn et al. (2017) C. Finn, P. Abbeel, and S. Levine Model-agnostic meta-learning for fast adaptation of deep networks . In International conference on machine learning , pp. 1126–1135 . Cited by: §1 .

Gan et al. (2024) C. Gan, D. Yang, B. Hu, H. Zhang, S. Li, Z. Liu, Y. Shen, L. Ju, Z. Zhang, J. Gu, L. Liang, and J. Zhou Similarity is not all you need: endowing retrieval augmented generation with multi layered thoughts . arXiv preprint arXiv:2405.19893 . External Links: Link , Document Cited by: §4.2 .

Gao et al. (2024) Y. Gao, Y. Xiong, X. Gao, K. Jia, J. Pan, Y. Bi, Y. Dai, J. Sun, M. Wang, and H. Wang Retrieval-augmented generation for large language models: a survey . External Links: 2312.10997 , Link Cited by: §1 .

Gick and Holyoak (1980) M. L. Gick and K. J. Holyoak Analogical problem solving . Cognitive psychology 12 ( 3 ), pp. 306–355 . Cited by: §1 , §2 .

Grossberg (2013) S. Grossberg Adaptive resonance theory: how a brain learns to consciously attend, learn, and recognize a changing world . Neural networks 37 , pp. 1–47 . Cited by: §1 .

Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning . arXiv preprint arXiv:2501.12948 . Cited by: §2 , §3.2 .

Hassabis and Maguire (2007) D. Hassabis and E. A. Maguire Deconstructing episodic memory with construction . Trends in cognitive sciences 11 ( 7 ), pp. 299–306 . Cited by: §1 .

Huang et al. (2025) Z. Huang, Z. Tian, Q. Guo, F. Zhang, Y. Zhou, D. Jiang, and X. Zhou LiCoMemory: lightweight and cognitive agentic memory for efficient long-term reasoning . arXiv preprint arXiv:2511.01448 . Cited by: §2 .

Javed et al. (2023) K. Javed, H. Shah, R. Sutton, and M. White Online real-time recurrent learning using sparse connections and selective learning . Journal of Machine Learning Research . Cited by: §1 .

Karpukhin et al. (2020) V. Karpukhin, B. Oguz, S. Min, P. S. Lewis, L. Wu, S. Edunov, D. Chen, and W. Yih Dense passage retrieval for open-domain question answering. . In EMNLP (1) , pp. 6769–6781 . Cited by: §1 , §2 .

Kirkpatrick et al. (2017) J. Kirkpatrick, R. Pascanu, N. Rabinowitz, J. Veness, G. Desjardins, A. A. Rusu, K. Milan, J. Quan, T. Ramalho, A. Grabska-Barwinska, et al. Overcoming catastrophic forgetting in neural networks . Proceedings of the national academy of sciences 114 ( 13 ), pp. 3521–3526 . Cited by: §1 .

Kumaran et al. (2016) D. Kumaran, D. Hassabis, and J. L. McClelland What learning systems do intelligent agents need? complementary learning systems theory updated . Trends in cognitive sciences 20 ( 7 ), pp. 512–534 . Cited by: §1 .

Lewis et al. (2020) P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, et al. Retrieval-augmented generation for knowledge-intensive nlp tasks . Advances in neural information processing systems 33 , pp. 9459–9474 . Cited by: 1st item , §1 , §2 , §3.2 .

Li et al. (2024) H. Li, L. Ding, M. Fang, and D. Tao Revisiting catastrophic forgetting in large language model tuning . arXiv preprint arXiv:2406.04836 . Cited by: §1 .

Li et al. (2025a) L. Li, D. Shi, J. Zhou, X. Wei, M. Yang, S. Jin, and S. Yang Retrieval feedback memory enhancement large model retrieval generation method . arXiv preprint arXiv:2508.17862 . Cited by: §2 .

Li et al. (2025b) Z. Li, S. Song, H. Wang, S. Niu, D. Chen, J. Yang, C. Xi, H. Lai, J. Zhao, Y. Wang, et al. MemOS: an operating system for memory-augmented generation (mag) in large language models . arXiv preprint arXiv:2505.22101 . Cited by: §2 .

Liang et al. (2025) J. Liang, R. He, and T. Tan A comprehensive survey on test-time adaptation under distribution shifts . International Journal of Computer Vision 133 ( 1 ), pp. 31–64 . Cited by: §2 .

McClelland et al. (1995) J. L. McClelland, B. L. McNaughton, and R. C. O’Reilly Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. . Psychological review 102 ( 3 ), pp. 419–457 . Cited by: §1 , §2 .

Metropolis and Ulam (1949) N. Metropolis and S. Ulam The monte carlo method . Journal of the American statistical association 44 ( 247 ), pp. 335–341 . Cited by: §1 , §3.2 .

Nader et al. (2000) K. Nader, G. E. Schafe, and J. E. Le Doux Fear memories require protein synthesis in the amygdala for reconsolidation after retrieval . Nature 406 ( 6797 ), pp. 722–726 . Cited by: §2 .

Neal and Hinton (1998) R. M. Neal and G. E. Hinton A view of the em algorithm that justifies incremental, sparse, and other variants . In Learning in Graphical Models , M. I. Jordan (Ed.) , pp. 355–368 . External Links: ISBN 978-94-011-5014-9 , Document , Link Cited by: §A.1 , §A.4.4 , §4.4 .

Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback . Advances in neural information processing systems 35 , pp. 27730–27744 . Cited by: §1 , §2 .

Packer et al. (2024) C. Packer, S. Wooders, K. Lin, V. Fang, S. G. Patil, I. Stoica, and J. E. Gonzalez MemGPT: towards llms as operating systems . External Links: 2310.08560 , Link Cited by: §2 .

Parisi et al. (2019) G. I. Parisi, R. Kemker, J. L. Part, C. Kanan, and S. Wermter Continual lifelong learning with neural networks: a review . Neural networks 113 , pp. 54–71 . Cited by: §1 , §2 .

Phan et al. (2025) L. Phan, A. Gatti, Z. Han, N. Li, J. Hu, H. Zhang, C. B. C. Zhang, M. Shaaban, J. Ling, S. Shi, et al. Humanity’s last exam . External Links: 2501.14249 , Link Cited by: 4th item .

Pritzel et al. (2017) A. Pritzel, B. Uria, S. Srinivasan, A. P. Badia, O. Vinyals, D. Hassabis, D. Wierstra, and C. Blundell Neural episodic control . In International conference on machine learning , pp. 2827–2836 . Cited by: §2 .

Puterman (2014) M. L. Puterman Markov decision processes: discrete stochastic dynamic programming . John Wiley & Sons . Cited by: §1 .

Rafailov et al. (2023) R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn Direct preference optimization: your language model is secretly a reward model . Advances in neural information processing systems 36 , pp. 53728–53741 . Cited by: §1 .

Rashid et al. (2020) T. Rashid, M. Samvelyan, C. S. De Witt, G. Farquhar, J. Foerster, and S. Whiteson Monotonic value function factorisation for deep multi-agent reinforcement learning . Journal of Machine Learning Research 21 ( 178 ), pp. 1–51 . Cited by: §G.2 , §6 .

Salama et al. (2025) R. Salama, J. Cai, M. Yuan, A. Currey, M. Sunkara, Y. Zhang, and Y. Benajiba Meminsight: autonomous memory augmentation for llm agents . arXiv preprint arXiv:2503.21760 . Cited by: §2 .

Schacter et al. (2012) D. L. Schacter, D. R. Addis, D. Hassabis, V. C. Martin, R. N. Spreng, and K. K. Szpunar The future of memory: remembering, imagining, and the brain . Neuron 76 ( 4 ), pp. 677–694 . Cited by: §1 .

Schacter and Addis (2007) D. L. Schacter and D. R. Addis On the constructive episodic simulation of past and future events . Behavioral and Brain Sciences 30 ( 3 ), pp. 331–332 . Cited by: §1 , §2 .

Schick et al. (2023) T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, E. Hambro, L. Zettlemoyer, N. Cancedda, and T. Scialom Toolformer: language models can teach themselves to use tools . Advances in Neural Information Processing Systems 36 , pp. 68539–68551 . Cited by: §1 , §2 .

Shapley et al. (1953) L. S. Shapley et al. A value for n-person games . Cited by: §G.2 , §6 .

Shinn et al. (2023) N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao Reflexion: language agents with verbal reinforcement learning . Advances in Neural Information Processing Systems 36 , pp. 8634–8652 . Cited by: §2 , §5.3.3 .

Shridhar et al. (2021) M. Shridhar, X. Yuan, M. Côté, Y. Bisk, A. Trischler, and M. Hausknecht ALFWorld: aligning text and embodied environments for interactive learning . External Links: 2010.03768 , Link Cited by: 3rd item .

Silver and Sutton (2025) D. Silver and R. S. Sutton Welcome to the era of experience . Google AI 1 . Cited by: §1 , §2 .

Singh et al. (2025) J. Singh, R. Magazine, Y. Pandya, and A. Nambi Agentic reasoning and tool integration for llms via reinforcement learning . arXiv preprint arXiv:2505.01441 . External Links: Link Cited by: §4.2 .

Stiennon et al. (2020) N. Stiennon, L. Ouyang, J. Wu, D. Ziegler, R. Lowe, C. Voss, A. Radford, D. Amodei, and P. F. Christiano Learning to summarize with human feedback . Advances in neural information processing systems 33 , pp. 3008–3021 . Cited by: §1 , §2 .

Sun et al. (2020) Y. Sun, X. Wang, Z. Liu, J. Miller, A. Efros, and M. Hardt Test-time training with self-supervision for generalization under distribution shifts . In International conference on machine learning , pp. 9229–9248 . Cited by: §2 .

Sunehag et al. (2017) P. Sunehag, G. Lever, A. Gruslys, W. M. Czarnecki, V. Zambaldi, M. Jaderberg, M. Lanctot, N. Sonnerat, J. Z. Leibo, K. Tuyls, et al. Value-decomposition networks for cooperative multi-agent learning . arXiv preprint arXiv:1706.05296 . Cited by: §G.2 , §6 .

Sutton and Barto (2018) R. S. Sutton and A. G. Barto Reinforcement learning: an introduction . 2 edition , MIT Press . External Links: Link Cited by: Theorem A.1 , §1 , §4.4 .

Sutton (1988) R. S. Sutton Learning to predict by the methods of temporal differences . Machine learning 3 ( 1 ), pp. 9–44 . Cited by: §3.2 .

Tulving et al. (1972) E. Tulving et al. Episodic and semantic memory . Organization of memory 1 ( 381-403 ), pp. 1 . Cited by: §2 .

Wang et al. (2020) D. Wang, E. Shelhamer, S. Liu, B. Olshausen, and T. Darrell Tent: fully test-time adaptation by entropy minimization . arXiv preprint arXiv:2006.10726 . Cited by: §2 .

Wang et al. (2023) G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and A. Anandkumar Voyager: an open-ended embodied agent with large language models . arXiv preprint arXiv:2305.16291 . Cited by: §1 .

Watkins and Dayan (1992) C. J. Watkins and P. Dayan Q-learning . Machine learning 8 ( 3 ), pp. 279–292 . Cited by: §1 .

Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models . Advances in neural information processing systems 35 , pp. 24824–24837 . Cited by: §1 .

Wei et al. (2025) T. Wei, N. Sachdeva, B. Coleman, Z. He, Y. Bei, X. Ning, M. Ai, Y. Li, J. He, E. H. Chi, et al. Evo-memory: benchmarking llm agent test-time learning with self-evolving memory . arXiv preprint arXiv:2511.20857 . Cited by: §1 , §2 .

Wu et al. (2024) T. Wu, L. Luo, Y. Li, S. Pan, T. Vu, and G. Haffari Continual learning for large language models: a survey . External Links: 2402.01364 , Link Cited by: §1 , §1 , §2 .

Xu et al. (2025) W. Xu, Z. Liang, K. Mei, H. Gao, J. Tan, and Y. Zhang A-mem: agentic memory for llm agents . arXiv preprint arXiv:2502.12110 . Cited by: §2 .

Yao et al. (2023) S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. R. Narasimhan, and Y. Cao ReAct: synergizing reasoning and acting in language models . In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023 , External Links: Link Cited by: §1 .

Ye (2025) Y. Ye Task memory engine: spatial memory for robust multi-step llm agents . arXiv preprint arXiv:2505.19436 . Cited by: §2 .

Yu et al. (2025) Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, W. Dai, T. Fan, G. Liu, L. Liu, et al. Dapo: an open-source llm reinforcement learning system at scale . arXiv preprint arXiv:2503.14476 . Cited by: §2 .

Zhang et al. (2025) Z. Zhang, Q. Dai, R. Li, X. Bo, X. Chen, and Z. Dong Learn to memorize: optimizing llm-based agents with adaptive memory framework . arXiv preprint arXiv:2508.16629 . Cited by: §2 .

Zheng et al. (2025) J. Zheng, X. Cai, Q. Li, D. Zhang, Z. Li, Y. Zhang, L. Song, and Q. Ma LifelongAgentBench: evaluating llm agents as lifelong learners . External Links: 2505.11942 , Link Cited by: 2nd item , §2 .

Zhou et al. (2025a) H. Zhou, Y. Chen, S. Guo, X. Yan, K. H. Lee, Z. Wang, K. Y. Lee, G. Zhang, K. Shao, L. Yang, et al. Memento: fine-tuning llm agents without fine-tuning llms . arXiv preprint arXiv:2508.16153 . Cited by: §2 , §3.1 , §3.2 , §3.2 , §3 .

Zhou et al. (2025b) R. Zhou, W. Hua, L. Pan, S. Cheng, X. Wu, E. Yu, and W. Y. Wang RuleArena: a benchmark for rule-guided reasoning with llms in real-world scenarios . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , Cited by: §2 .

Zhou et al. (2024) R. Zhou, Y. Yang, M. Wen, Y. Wen, W. Wang, C. Xi, G. Xu, Y. Yu, and W. Zhang TRAD: enhancing llm agents with step-wise thought retrieval and aligned decision . In Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR) , pp. 3–13 . External Links: Link Cited by: §4.2 .

Zhuo et al. (2025) T. Y. Zhuo, M. C. Vu, J. Chim, H. Hu, W. Yu, R. Widyasari, I. N. B. Yusuf, H. Zhan, J. He, I. Paul, S. Brunner, C. Gong, T. Hoang, A. R. Zebaze, X. Hong, W. Li, J. Kaddour, M. Xu, Z. Zhang, P. Yadav, N. Jain, A. Gu, Z. Cheng, J. Liu, Q. Liu, Z. Wang, B. Hui, N. Muennighoff, D. Lo, D. Fried, X. Du, H. de Vries, and L. V. Werra BigCodeBench: benchmarking code generation with diverse function calls and complex instructions . External Links: 2406.15877 , Link Cited by: 1st item .

## Appendix A Theoretical Analysis and Proofs

### A.1 Stability Analysis

We analyze the stability of MemRL from a reinforcement learning perspective, focusing on the convergence behavior of the utility estimates stored in memory. MemRL performs non-parametric runtime learning using a constant-step-size update. We show that under mild and realistic assumptions, the learned utility values converge in expectation to stable estimates of memory effectiveness, with bounded variance.

##### Setup.

At each time step t t , the agent observes an intent state s t s_{t} , retrieves a memory item m t ∈ ℳ t m_{t}\in\mathcal{M}_{t} , generates an output a t a_{t} , and receives a scalar reward r t ∈ [ − 1 , 1 ] r_{t}\in[-1,1] indicating task success or failure. The generation policy follows the decomposition defined in Eq. 1 , where μ \mu denotes the retrieval policy and p LLM p_{\mathrm{LLM}} is a frozen inference policy.

For each retrieved memory, MemRL updates its utility using the exponential moving average rule as formulated in Eq. 4 , with learning rate α ∈ ( 0 , 1 ] \alpha\in(0,1] . For clarity in this analysis, we consider a fixed state–memory pair ( s , m ) (s,m) and write Q t ≡ Q t ​ ( s , m ) Q_{t}\equiv Q_{t}(s,m) .

##### Stationary Reward Assumption.

We analyze the learning process on a fixed dataset and posit two key conditions that ensure the stability of the environment: 1. Frozen Inference Policy. The parameters of p LLM ​ ( y | s , m ) p_{\mathrm{LLM}}(y|s,m) and the evaluator’s criteria are fixed.

2. Fixed Task Distribution. Tasks s s are drawn from a stationary distribution over a fixed dataset.

These assumptions guarantee that the learning target is well-defined: the expected reward for any specific task-memory pair is time-invariant. Thus, we have:

where the expectation is taken over the stochastic rewards resulting from the Inference Policy p L ​ L ​ M p_{LLM} distribution.

##### Expected Convergence of Utility Estimates.

We now state the main stability result.

###### Theorem A.1 .

Let { Q t } \{Q_{t}\} be updated according to the rule in Eq. 4 with constant step size α ∈ ( 0 , 1 ] \alpha\in(0,1] . If Eq. 10 holds and the pair ( s , m ) (s,m) is updated infinitely often, then: lim t → ∞ 𝔼 [ Q t ] = 𝔼 [ r t | s t = s , m t = m ] = β ( s , m ) . \lim_{t\to\infty}\mathbb{E}[Q_{t}]=\mathbb{E}[r_{t}|s_{t}=s,\;m_{t}=m]=\beta(s,m). (11) Moreover, the convergence rate is exponential ( Sutton and Barto, 2018 ) : 𝔼 ⁡ [ Q t ] − β ⁡ ( s , m ) = ( 1 − α ) t ​ ( Q 0 − β ⁡ ( s , m ) ) . \mathbb{E}[Q_{t}]-\beta(s,m)=(1-\alpha)^{t}\big(Q_{0}-\beta(s,m)\big). (12)

##### Proof.

Define the estimation error e t ≜ Q t − β ⁡ ( s , m ) e_{t}\triangleq Q_{t}-\beta(s,m) . Based on the update rule in Eq. 4 , the error recurrence relation is: e t + 1 = ( 1 − α ) ​ e t + α ⁡ ( r t − β ⁡ ( s , m ) ) . e_{t+1}=(1-\alpha)e_{t}+\alpha\big(r_{t}-\beta(s,m)\big). Taking conditional expectation given the history ℱ t \mathcal{F}_{t} and using Eq. 10 , we obtain: 𝔼 ⁡ [ e t + 1 | ℱ t ] = ( 1 − α ) ​ e t . \mathbb{E}[e_{t+1}|\mathcal{F}_{t}]=(1-\alpha)e_{t}. Taking full expectation yields: 𝔼 ⁡ [ e t + 1 ] = ( 1 − α ) ​ 𝔼 ​ [ e t ] . \mathbb{E}[e_{t+1}]=(1-\alpha)\mathbb{E}[e_{t}]. Iterating the recursion gives 𝔼 ⁡ [ e t ] = ( 1 − α ) t ​ e 0 \mathbb{E}[e_{t}]=(1-\alpha)^{t}e_{0} , which converges to zero as t → ∞ t\to\infty . □ \square

We provide the detailed derivation of the convergence proof in Appendix A.2 .

##### Bounded Variance and Stability.

If the reward variance Var ⁡ ( r t | s , m ) < ∞ \mathrm{Var}(r_{t}|s,m)<\infty , then the variance of Q t Q_{t} remains bounded: lim sup t → ∞ Var ⁡ ( Q t ) ≤ α 2 − α ​ Var ​ ( r t | s , m ) . \limsup_{t\to\infty}\mathrm{Var}(Q_{t})\leq\frac{\alpha}{2-\alpha}\,\mathrm{Var}(r_{t}|s,m). (13) Thus, constant-step-size updates do not induce unbounded oscillations; instead, they yield stable utility estimates that track expected memory effectiveness while filtering high-frequency noise. We explicitly derive the variance bounds to demonstrate the global stability of the estimator under task clustering in Appendix A.3 .

##### Global Stability via EM Convergence.

The stability of the local estimate (Theorem A.1 ) extends to the global memory utility Q ⁡ ( m ) Q(m) . By the linearity of expectation, Q ⁡ ( m ) Q(m) acts as a Monte Carlo integrator striving to converge to:

lim t → ∞ 𝔼 ⁡ [ Q t ​ ( m ) ] = 𝔼 ⁡ [ r | m ] = ∑ s ∈ 𝒮 ⁡ ( m ) 𝔼 [ r | s , m ] ⏟ Stationary ​ Pr ⁡ ( s | m ) ⏟ Retrieve-Dependent . \lim_{t\to\infty}\mathbb{E}[Q_{t}(m)]=\mathbb{E}[r|m]=\sum_{s\in\mathcal{S}(m)}\underbrace{\mathbb{E}[r|s,m]}_{\text{Stationary}}\underbrace{\Pr(s|m)}_{\text{Retrieve-Dependent}}. (14)

where 𝒮 ⁡ ( m ) ≜ { s ∈ 𝒮 | sim ​ ( s , z m ) ≥ τ A } \mathcal{S}(m)\triangleq\{s\in\mathcal{S}|\text{sim}(s,z_{m})\geq\tau_{A}\} denotes the effective support set for memory m m , comprising all task intents s s sufficiently similar to the memory’s intent embedding z m z_{m} to satisfy the Phase-A retrieval criterion.

A theoretical challenge arises here: the weighting term Pr ⁡ ( s | m ) \Pr(s|m) is a latent variable governed by the retrieval policy μ ⁡ ( m | s ; ℳ ) \mu(m|s;\mathcal{M}) , which itself shifts as Q Q -values evolve. To prove convergence despite this dependency, we analyze MemRL as a Generalized Expectation-Maximization (GEM) process ( Dempster et al., 1977 ; Neal and Hinton, 1998 ) . From a variational perspective, the system performs coordinate ascent on a global objective function 𝒥 ⁡ ( Q , μ ) \mathcal{J}(Q,\mu) (the variational lower bound of expected reward): (i) E-Step (Policy Improvement): The Phase-B ranking updates the retrieval policy μ \mu to align with current estimates, monotonically increasing 𝒥 \mathcal{J} with respect to μ \mu ; (ii) M-Step (Value Update): The utility update (Eq. 4 ) increases 𝒥 \mathcal{J} with respect to Q Q . By the Monotonic Improvement Theorem ( Neal and Hinton, 1998 ) , this alternating optimization guarantees that the system converges to a stationary point where the retrieve policy stabilizes ( μ t + 1 ≈ μ t \mu_{t+1}\approx\mu_{t} ). Consequently, the induced distribution Pr ⁡ ( s | m ) \Pr(s|m) becomes time-invariant, ensuring that Eq. 14 holds and effectively preventing catastrophic forgetting by anchoring updates to a stable policy. More details can be found in Appendix A.4 .

### A.2 Proof of Theorem A.1 : Convergence of EMA Estimation

We aim to prove that for a fixed task-memory pair ( s , m ) (s,m) with a stationary reward distribution, the Q-value estimate Q t ​ ( s , m ) Q_{t}(s,m) converges in expectation to the true mean reward β ⁡ ( s , m ) \beta(s,m) .

##### Assumptions.

1. Stationary Reward. The reward r t r_{t} at step t t is drawn from a distribution induced by the stochastic action generation a ∼ p L ​ L ​ M ​ ( a t | s t , m ) a\sim p_{LLM}(a_{t}|s_{t},m) , with a constant mean β ( s , m ) = 𝔼 [ r t | s , m ] \beta(s,m)=\mathbb{E}[r_{t}|s,m] and finite variance σ 2 \sigma^{2} .

2. Update Rule. The utility is updated via the linear EMA rule with learning rate α ∈ ( 0 , 1 ) \alpha\in(0,1) : Q t + 1 = ( 1 − α ) ​ Q t + α ​ r t . Q_{t+1}=(1-\alpha)Q_{t}+\alpha r_{t}.

##### Derivation of Error Dynamics.

Let e t ≜ Q t − β ⁡ ( s , m ) e_{t}\triangleq Q_{t}-\beta(s,m) be the estimation error at time step t t . Substituting Q t = e t + β ⁡ ( s , m ) Q_{t}=e_{t}+\beta(s,m) into the update rule:

e t + 1 + β ⁡ ( s , m ) \displaystyle e_{t+1}+\beta(s,m) = ( 1 − α ) ​ ( e t + β ⁡ ( s , m ) ) + α ​ r t \displaystyle=(1-\alpha)(e_{t}+\beta(s,m))+\alpha r_{t} e t + 1 \displaystyle e_{t+1} = ( 1 − α ) ​ e t + ( 1 − α ) ​ β ​ ( s , m ) + α ​ r t − β ⁡ ( s , m ) \displaystyle=(1-\alpha)e_{t}+(1-\alpha)\beta(s,m)+\alpha r_{t}-\beta(s,m) e t + 1 \displaystyle e_{t+1} = ( 1 − α ) ​ e t + β ⁡ ( s , m ) − α ​ β ​ ( s , m ) − β ⁡ ( s , m ) + α ​ r t \displaystyle=(1-\alpha)e_{t}+\beta(s,m)-\alpha\beta(s,m)-\beta(s,m)+\alpha r_{t} e t + 1 \displaystyle e_{t+1} = ( 1 − α ) ​ e t + α ⁡ ( r t − β ⁡ ( s , m ) ) . \displaystyle=(1-\alpha)e_{t}+\alpha(r_{t}-\beta(s,m)). (15)

##### Convergence Analysis.

We define ℱ t \mathcal{F}_{t} as the filtration (history) up to time t t . Since the reward r t r_{t} depends on the action a t a_{t} sampled subsequently from the frozen LLM, taking the conditional expectation of Eq. 15 given ℱ t \mathcal{F}_{t} :

𝔼 ⁡ [ e t + 1 | ℱ t ] = ( 1 − α ) ​ e t + α ⁡ ( 𝔼 ⁡ [ r t | ℱ t ] ⏟ β ⁡ ( s , m ) − β ⁡ ( s , m ) ) = ( 1 − α ) ​ e t . \mathbb{E}[e_{t+1}|\mathcal{F}_{t}]=(1-\alpha)e_{t}+\alpha(\underbrace{\mathbb{E}[r_{t}|\mathcal{F}_{t}]}_{\beta(s,m)}-\beta(s,m))=(1-\alpha)e_{t}.

By the Law of Iterated Expectations, taking the full expectation yields: 𝔼 ⁡ [ e t + 1 ] = 𝔼 ⁡ [ 𝔼 ⁡ [ e t + 1 | ℱ t ] ] = ( 1 − α ) ​ 𝔼 ​ [ e t ] . \mathbb{E}[e_{t+1}]=\mathbb{E}[\mathbb{E}[e_{t+1}|\mathcal{F}_{t}]]=(1-\alpha)\mathbb{E}[e_{t}].

Iterating this recurrence relation from t = 0 t=0 : 𝔼 ⁡ [ e t ] = ( 1 − α ) t ​ 𝔼 ​ [ e 0 ] . \mathbb{E}[e_{t}]=(1-\alpha)^{t}\mathbb{E}[e_{0}].

Since 0 < α < 1 0<\alpha<1 , we have | 1 − α | < 1 |1-\alpha|<1 . Consequently: lim t → ∞ 𝔼 ⁡ [ e t ] = 𝔼 ⁡ [ e 0 ] ⋅ lim t → ∞ ( 1 − α ) t = 0 . \lim_{t\to\infty}\mathbb{E}[e_{t}]=\mathbb{E}[e_{0}]\cdot\lim_{t\to\infty}(1-\alpha)^{t}=0. (16)

This proves that the estimator is unbiased in the limit, i.e., lim t → ∞ 𝔼 ⁡ [ Q t ] = β ⁡ ( s , m ) \lim_{t\to\infty}\mathbb{E}[Q_{t}]=\beta(s,m) . □ \square

### A.3 Bounded Variance and Global Stability

In this section, we provide the formal derivation for the variance bound of the estimator Q t Q_{t} . We explicitly derive the finite-time variance formula via recursive unrolling and prove its asymptotic convergence, demonstrating how Phase-A clustering contributes to global stability.

##### Derivation of the Variance Bound.

Let σ 2 ≜ Var ⁡ ( r t | s , m ) \sigma^{2}\triangleq\mathrm{Var}(r_{t}|s,m) be the variance of the reward signal, assumed to be finite. The EMA update rule is given by: Q t + 1 = ( 1 − α ) ​ Q t + α ​ r t . Q_{t+1}=(1-\alpha)Q_{t}+\alpha r_{t}. Since the reward r t r_{t} (current noise) is statistically independent of the current estimate Q t Q_{t} (which is determined by history ℱ t − 1 \mathcal{F}_{t-1} ), the variance of the sum is the sum of the variances: Var ⁡ ( Q t + 1 ) \displaystyle\mathrm{Var}(Q_{t+1}) = Var ⁡ ( ( 1 − α ) ​ Q t ) + Var ⁡ ( α ​ r t ) \displaystyle=\mathrm{Var}((1-\alpha)Q_{t})+\mathrm{Var}(\alpha r_{t}) = ( 1 − α ) 2 ​ Var ​ ( Q t ) + α 2 ​ σ 2 . \displaystyle=(1-\alpha)^{2}\mathrm{Var}(Q_{t})+\alpha^{2}\sigma^{2}. Let v t ≜ Var ⁡ ( Q t ) v_{t}\triangleq\mathrm{Var}(Q_{t}) . We obtain a linear recurrence relation v t + 1 = ( 1 − α ) 2 ​ v t + α 2 ​ σ 2 v_{t+1}=(1-\alpha)^{2}v_{t}+\alpha^{2}\sigma^{2} .

##### Recursive Unrolling.

To solve for v t v_{t} , we expand the recurrence relation backward from step t t : v t \displaystyle v_{t} = ( 1 − α ) 2 ​ v t − 1 + α 2 ​ σ 2 \displaystyle=(1-\alpha)^{2}v_{t-1}+\alpha^{2}\sigma^{2} = ( 1 − α ) 2 ​ [ ( 1 − α ) 2 ​ v t − 2 + α 2 ​ σ 2 ] + α 2 ​ σ 2 \displaystyle=(1-\alpha)^{2}\left[(1-\alpha)^{2}v_{t-2}+\alpha^{2}\sigma^{2}\right]+\alpha^{2}\sigma^{2} = ( 1 − α ) 4 ​ v t − 2 + α 2 ​ σ 2 ​ [ 1 + ( 1 − α ) 2 ] \displaystyle=(1-\alpha)^{4}v_{t-2}+\alpha^{2}\sigma^{2}\left[1+(1-\alpha)^{2}\right] ⋮ \displaystyle\quad\vdots = ( 1 − α ) 2 ​ t ​ v 0 + α 2 ​ σ 2 ​ ∑ k = 0 t − 1 ( ( 1 − α ) 2 ) k . \displaystyle=(1-\alpha)^{2t}v_{0}+\alpha^{2}\sigma^{2}\sum_{k=0}^{t-1}\left((1-\alpha)^{2}\right)^{k}. (17) Eq. 17 explicitly shows that the variance at time t t consists of two components: the decayed initial variance (first term) and the accumulated noise variance (second term).

##### Asymptotic Convergence.

As t → ∞ t\to\infty , since the learning rate α ∈ ( 0 , 1 ) \alpha\in(0,1) , the term ( 1 − α ) 2 ​ t (1-\alpha)^{2t} vanishes. The summation term is a geometric series ∑ k = 0 ∞ r k = 1 1 − r \sum_{k=0}^{\infty}r^{k}=\frac{1}{1-r} with ratio r = ( 1 − α ) 2 r=(1-\alpha)^{2} . Thus: lim t → ∞ v t = α 2 ​ σ 2 ⋅ 1 1 − ( 1 − α ) 2 . \lim_{t\to\infty}v_{t}=\alpha^{2}\sigma^{2}\cdot\frac{1}{1-(1-\alpha)^{2}}. Evaluating the denominator: 1 − ( 1 − α ) 2 = 1 − ( 1 − 2 ​ α + α 2 ) = 2 ​ α − α 2 = α ⁡ ( 2 − α ) . 1-(1-\alpha)^{2}=1-(1-2\alpha+\alpha^{2})=2\alpha-\alpha^{2}=\alpha(2-\alpha). Substituting this back yields the tight variance bound: lim sup t → ∞ Var ⁡ ( Q t ) = α 2 ​ σ 2 α ⁡ ( 2 − α ) = α 2 − α ​ σ 2 . \limsup_{t\to\infty}\mathrm{Var}(Q_{t})=\frac{\alpha^{2}\sigma^{2}}{\alpha(2-\alpha)}=\frac{\alpha}{2-\alpha}\sigma^{2}. (18)

##### Connection to Phase-A Clustering.

This result provides the theoretical justification for the stability of MemRL . While tasks within a memory cluster 𝒮 ⁡ ( m ) ≜ { s | sim ​ ( s , z m ) > τ A } \mathcal{S}(m)\triangleq\{s|\text{sim}(s,z_{m})>\tau_{A}\} may vary, the Smoothness Assumption implies their rewards are drawn from a distribution with bounded variance σ 𝒮 ⁡ ( m ) 2 \sigma^{2}_{\mathcal{S}(m)} . The derived bound α 2 − α ​ σ 𝒮 ⁡ ( m ) 2 \frac{\alpha}{2-\alpha}\sigma^{2}_{\mathcal{S}(m)} guarantees that the memory utility Q ⁡ ( m ) Q(m) will not diverge but will instead oscillate within a controlled range around the true expected utility. This mechanism effectively filters out high-frequency noise from diverse task instances while retaining the stable generalized value.

### A.4 Convergence via Variational Inference

In this section, we provide a theoretical foundation for MemRL , demonstrating that our retrieval strategy and update rules guarantee the convergence of value estimation.

#### A.4.1 The Convergence Objective

Our ultimate goal is to ensure that the estimated utility Q ⁡ ( m ) Q(m) converges to the true expected return of memory m m . This target value is defined as: lim t → ∞ 𝔼 ⁡ [ Q t ​ ( m ) ] = 𝔼 ⁡ [ r | m ] = ∑ s ∈ 𝒮 ⁡ ( m ) 𝔼 [ r | s , m ] ⏟ Stationary ​ Pr ⁡ ( s | m ) ⏟ Retrieve-Dependent . \lim_{t\to\infty}\mathbb{E}[Q_{t}(m)]=\mathbb{E}[r|m]=\sum_{s\in\mathcal{S}(m)}\underbrace{\mathbb{E}[r|s,m]}_{\text{Stationary}}\underbrace{\Pr(s|m)}_{\text{Retrieve-Dependent}}. (19) The challenge lies in the term Pr ⁡ ( s | m ) \Pr(s|m) —the probability that a specific state s s triggers the retrieval of m m . This distribution depends on the retrieval policy μ t ​ ( m | s ) \mu_{t}(m|s) , which itself evolves during training, creating a circular dependency that threatens stability.

#### A.4.2 Variational Objective with Trust Region

To resolve this, we formulate the problem as maximizing a global variational objective 𝒥 ⁡ ( μ , Q ) \mathcal{J}(\mu,Q) . This objective serves as a tractable lower bound for the global expected return defined in Eq. 19 , balanced by a semantic trust region: 𝒥 ⁡ ( μ , Q ) = 𝔼 s ∼ 𝒟 ​ [ ∑ m ∈ 𝒮 ⁡ ( s ) μ ⁡ ( m | s ) ​ Q ​ ( s , m ) ⏟ Expected Utility ≈ 𝔼 ⁡ [ Q t ​ ( m ) ] − 1 β ​ D KL ( μ ( ⋅ | s ) ∥ π sim ( ⋅ | s ) ) ⏟ Semantic Trust Region ] \mathcal{J}(\mu,Q)=\mathbb{E}_{s\sim\mathcal{D}}\left[\underbrace{\sum_{m\in\mathcal{S}(s)}\mu(m|s)Q(s,m)}_{\text{Expected Utility }\approx\mathbb{E}[Q_{t}(m)]}-\frac{1}{\beta}\underbrace{D_{\text{KL}}\Big(\mu(\cdot|s)\big\|\pi_{\text{sim}}(\cdot|s)\Big)}_{\text{Semantic Trust Region}}\right] (20) Here, the expectation is taken over the state distribution 𝒟 \mathcal{D} . The first term directly corresponds to the expected utility 𝔼 ​ [ Q t ​ ( m ) ] \mathbb{E}[Q_{t}(m)] we aim to converge, while π sim \pi_{\text{sim}} represents the fixed semantic prior (derived from Phase-A). The KL-divergence term acts as a regularizer crucial for two reasons: 1. Trust Region: It constrains the policy to the support set 𝒮 \mathcal{S} , preventing the agent from retrieving high-Q but semantically irrelevant memories (out-of-distribution errors).

2. Regularization: It stabilizes the learning dynamics during the “cold start” phase when Q-estimates are noisy.

#### A.4.3 Optimization via Generalized Expectation-Maximization (GEM)

We treat the optimization of 𝒥 \mathcal{J} as a GEM process, alternating between policy improvement and value evaluation:

##### E-Step (Policy Optimization).

We assume the utility estimates Q ⁡ ( s , m ) Q(s,m) are fixed and seek the optimal retrieval policy μ ∗ \mu^{*} that maximizes the global variational objective 𝒥 ⁡ ( μ , Q ) \mathcal{J}(\mu,Q) . Since the expectation is taken over the state distribution 𝒟 \mathcal{D} , we can maximize the objective for each state s s pointwise. The optimization problem for a specific state s s is:

max μ ( ⋅ | s ) [ ∑ m ∈ 𝒮 ⁡ ( s ) μ ( m | s ) Q ( s , m ) − 1 β D KL ( μ ( ⋅ | s ) ∥ π sim ( ⋅ | s ) ) ] \max_{\mu(\cdot|s)}\left[\sum_{m\in\mathcal{S}(s)}\mu(m|s)Q(s,m)-\frac{1}{\beta}D_{\text{KL}}\Big(\mu(\cdot|s)\big\|\pi_{\text{sim}}(\cdot|s)\Big)\right] (21) subject to the probability simplex constraint ∑ m ∈ 𝒮 ⁡ ( s ) μ ⁡ ( m | s ) = 1 \sum_{m\in\mathcal{S}(s)}\mu(m|s)=1 .

Expanding the KL-divergence term, the objective function becomes: ℒ ⁡ ( μ ) = ∑ m ∈ 𝒮 ⁡ ( s ) μ ⁡ ( m | s ) ​ ( Q ⁡ ( s , m ) + 1 β ​ log ⁡ π sim ​ ( m | s ) μ ⁡ ( m | s ) ) . \mathcal{L}(\mu)=\sum_{m\in\mathcal{S}(s)}\mu(m|s)\left(Q(s,m)+\frac{1}{\beta}\log\frac{\pi_{\text{sim}}(m|s)}{\mu(m|s)}\right). (22)

To enforce the normalization constraint, we introduce the Lagrange multiplier λ \lambda and construct the Lagrangian: L ⁡ ( μ , λ ) = ∑ m ∈ 𝒮 ⁡ ( s ) μ ⁡ ( m | s ) ​ ( Q ⁡ ( s , m ) + 1 β ​ log ⁡ π sim ​ ( m | s ) μ ⁡ ( m | s ) ) + λ ⁡ ( 1 − ∑ m ∈ 𝒮 ⁡ ( s ) μ ⁡ ( m | s ) ) . L(\mu,\lambda)=\sum_{m\in\mathcal{S}(s)}\mu(m|s)\left(Q(s,m)+\frac{1}{\beta}\log\frac{\pi_{\text{sim}}(m|s)}{\mu(m|s)}\right)+\lambda\left(1-\sum_{m\in\mathcal{S}(s)}\mu(m|s)\right).

Taking the derivative with respect to μ ⁡ ( m | s ) \mu(m|s) and setting it to zero: ∂ L ∂ μ ⁡ ( m | s ) \displaystyle\frac{\partial L}{\partial\mu(m|s)} = Q ⁡ ( s , m ) + 1 β ​ ( log ⁡ π sim ​ ( m | s ) μ ⁡ ( m | s ) + μ ⁡ ( m | s ) ⋅ μ ⁡ ( m | s ) π sim ​ ( m | s ) ⋅ − π sim ​ ( m | s ) μ ​ ( m | s ) 2 ) − λ \displaystyle=Q(s,m)+\frac{1}{\beta}\left(\log\frac{\pi_{\text{sim}}(m|s)}{\mu(m|s)}+\mu(m|s)\cdot\frac{\mu(m|s)}{\pi_{\text{sim}}(m|s)}\cdot\frac{-\pi_{\text{sim}}(m|s)}{\mu(m|s)^{2}}\right)-\lambda = Q ⁡ ( s , m ) + 1 β ​ ( log ⁡ π sim ​ ( m | s ) μ ⁡ ( m | s ) − 1 ) − λ = 0 . \displaystyle=Q(s,m)+\frac{1}{\beta}\left(\log\frac{\pi_{\text{sim}}(m|s)}{\mu(m|s)}-1\right)-\lambda=0.

Rearranging terms to solve for μ ⁡ ( m | s ) \mu(m|s) : log ⁡ π sim ​ ( m | s ) μ ⁡ ( m | s ) \displaystyle\log\frac{\pi_{\text{sim}}(m|s)}{\mu(m|s)} = β ​ λ − β ​ Q ​ ( s , m ) + 1 \displaystyle=\beta\lambda-\beta Q(s,m)+1 μ ⁡ ( m | s ) π sim ​ ( m | s ) \displaystyle\frac{\mu(m|s)}{\pi_{\text{sim}}(m|s)} = exp ⁡ ( β ​ Q ​ ( s , m ) − ( β ​ λ + 1 ) ) \displaystyle=\exp\left(\beta Q(s,m)-(\beta\lambda+1)\right) μ ⁡ ( m | s ) \displaystyle\mu(m|s) = π sim ​ ( m | s ) ​ exp ⁡ ( β ​ Q ​ ( s , m ) ) ⋅ exp ⁡ ( − ( β ​ λ + 1 ) ) . \displaystyle=\pi_{\text{sim}}(m|s)\exp(\beta Q(s,m))\cdot\exp(-(\beta\lambda+1)).

Since exp ⁡ ( − ( β ​ λ + 1 ) ) \exp(-(\beta\lambda+1)) is independent of m m , it acts as a normalization constant 1 / Z ⁡ ( s ) 1/Z(s) . Thus, we recover the closed-form Boltzmann distribution used in our Phase-B retrieval: μ ∗ ​ ( m | s ) = π sim ​ ( m | s ) ​ exp ⁡ ( β ​ Q ​ ( s , m ) ) Z ⁡ ( s ) ∝ π sim ​ ( m | s ) ​ exp ⁡ ( β ​ Q ​ ( s , m ) ) . \mu^{*}(m|s)=\frac{\pi_{\text{sim}}(m|s)\exp(\beta Q(s,m))}{Z(s)}\propto\pi_{\text{sim}}(m|s)\exp(\beta Q(s,m)). This derivation theoretically justifies our heuristic scoring function: the optimal retrieval policy naturally balances the semantic prior π sim \pi_{\text{sim}} and the learned utility Q Q . By taking the logarithm, we recover the specific scoring function used in our Phase-B Retrieval (Eq. 7 ): log ⁡ μ ∗ ​ ( m | s ) ∝ log ⁡ π sim ​ ( m | s ) ⏟ ≈ sim ​ ( s , m ) + β ​ Q t ​ ( s , m ) \log\mu^{*}(m|s)\propto\underbrace{\log\pi_{\text{sim}}(m|s)}_{\approx\text{sim}(s,m)}+\beta Q_{t}(s,m) This proves that our heuristic combination of similarity and Q-value is mathematically equivalent to the optimal policy under the variational objective.

##### M-Step (Policy Evaluation via Error Minimization).

While the E-step improves the policy based on current estimates, the M-step ensures these estimates are grounded in reality. Fixing the policy μ t + 1 \mu_{t+1} , our goal is to align the variational parameter Q Q with the true environmental returns. We formulate this as minimizing the Mean Squared Error (MSE) between the estimated utility and the observed reward target y = r y=r (in our Monte Carlo style modeling): min Q ⁡ ℒ ⁡ ( Q ) = 𝔼 τ ∼ μ t + 1 ​ [ 1 2 ​ ( y − Q ⁡ ( s , m ) ) 2 ] \min_{Q}\mathcal{L}(Q)=\mathbb{E}_{\tau\sim\mu_{t+1}}\left[\frac{1}{2}\left(y-Q(s,m)\right)^{2}\right] (23) Minimizing this error is critical because it tightens the variational bound: it ensures that the expectation term 𝔼 ⁡ [ Q ] \mathbb{E}[Q] in the global objective 𝒥 \mathcal{J} (Eq. 20 ) converges to the true expected return 𝔼 ⁡ [ r ] \mathbb{E}[r] . The update rule used in our approach (Eq. 4 ) corresponds exactly to a Stochastic Gradient Descent (SGD) step on this objective: Q t + 1 ​ ( s , m ) ← Q t ​ ( s , m ) − α ​ ∇ Q ℒ ​ ( Q ) = Q t ​ ( s , m ) + α ⁡ ( y − Q t ​ ( s , m ) ) Q_{t+1}(s,m)\leftarrow Q_{t}(s,m)-\alpha\nabla_{Q}\mathcal{L}(Q)=Q_{t}(s,m)+\alpha(y-Q_{t}(s,m)) By iteratively minimizing ℒ ⁡ ( Q ) \mathcal{L}(Q) , the M-step propagates the environmental feedback into the utility estimates, ensuring that the subsequent E-step optimization occurs on a reliable value landscape.

#### A.4.4 Proof of Convergence

By the Monotonic Improvement Theorem of GEM ( Neal and Hinton, 1998 ) , the sequence ( μ t , Q t ) (\mu_{t},Q_{t}) is guaranteed to converge to a stationary point ( μ ∗ , Q ∗ ) (\mu^{*},Q^{*}) . At stationarity, the policy stabilizes ( μ t + 1 ≈ μ t \mu_{t+1}\approx\mu_{t} ), which implies that the inverse retrieval probability Pr ⁡ ( s | m ) \Pr(s|m) becomes time-invariant : Pr ⁡ ( s | m ) = μ ∗ ​ ( m | s ) ​ Pr ⁡ ( s ) ∑ s ′ μ ∗ ​ ( m | s ′ ) ​ Pr ⁡ ( s ′ ) \Pr(s|m)=\frac{\mu^{*}(m|s)\Pr(s)}{\sum_{s^{\prime}}\mu^{*}(m|s^{\prime})\Pr(s^{\prime})} Consequently, the “Retrieve-Dependent” term in Eq. 19 is anchored. With a fixed data distribution, the Q t ​ ( m ) Q_{t}(m) converges to the unique fixed point: lim t → ∞ Q t ​ ( m ) → 𝔼 μ ∗ ​ [ r | m ] \lim_{t\to\infty}Q_{t}(m)\to\mathbb{E}_{\mu^{*}}[r|m] (24) Thus, our approach theoretically guarantees that the memory values converge to the true expected returns under the optimal retrieval policy.

## Appendix B Extended Analysis and Insights

### B.1 Detailed Analysis of Forgetting Dynamics

In the main text, we reported the mean forgetting rate to quantify the stability of our method. Here, we provide a detailed visual analysis of how the forgetting rate evolves throughout the learning process on the HLE benchmark.

As illustrated in Figure 9 , MemRL demonstrates superior stability compared to MemP. Specifically: • Stability vs. Plasticity: While MemP shows a gradual upward trend in forgetting rate as the number of episodes increases, MemRL maintains a consistently low rate. This indicates that our dual-retrieval mechanism effectively balances the acquisition of new strategies without overwriting stable, high-utility memories.

• Impact of Filtering: The ablation curve (denoted as w/o Norm & SimGate ) exhibits significant higher overall forgetting rate ( 0.073 0.073 mean). The visible spikes in the curve suggest that without z-score normalization and similarity gating, the agent frequently retrieves and reinforces “noisy” strategies that work for specific instances but degrade general performance on previously mastered tasks.

### B.2 MemRL as a Trajectory Verifier.

Table 4 reveals a correlation between task structural complexity and performance gain. The gains are most profound in multi-step sequential tasks (e.g., ALFWorld + 6.2 % +6.2\% Points(pp)) compared to single-turn tasks (e.g., BigCodeBench + 2.5 % +2.5\% pp). In sequential tasks, a retrieved memory must be valid for the entire trajectory. Standard semantic retrieval often fetches memories that match the initial instruction but fail in later steps. By propagating the final reward backward to the memory utility Q Q , MemRL effectively learns to verify the whole trajectory , filtering out brittle policies that look correct only on the surface.

This analysis indicates that MemRL transcends the role of a simple retrieval enhancer to function as a Trajectory Verifier . Its value is maximized in tasks with complex temporal dependencies, where it learns to select memories that ensure the structural integrity of the entire interaction process.

### B.3 Impact of Task Similarity on Memory Efficacy

To understand the underlying conditions where MemRL thrives, we analyze the correlation between the intra-dataset semantic similarity ( Sim i ​ n ​ t ​ r ​ a \text{Sim}_{intra} ) and the absolute performance gain provided by our method ( Δ = Success Rate MemRL − Success Rate NoMem \Delta=\text{Success Rate}_{\text{MemRL}}-\text{Success Rate}_{\text{NoMem}} ).

As illustrated in Figure 10 , we analyze the correlation between intra-dataset semantic similarity and the absolute performance gain ( Δ \Delta ) provided by MemRL . The linear regression trend reveals a general positive correlation: environments with higher structural repetition allow the agent to retrieve and reuse optimal policies more effectively. At the upper extreme, ALFWorld (similarity 0.518 0.518 ) acts as a strong anchor point for this trend, exhibiting the highest repetition and a corresponding maximum performance boost ( Δ = + 0.172 \Delta=+0.172 ). This confirms that for highly repetitive procedural tasks, memory serves as an effective shortcut to optimal trajectories. Following the regression line, benchmarks with moderate similarity—such as Lifelong-OS ( 0.390 0.390 ) and BigCodeBench ( 0.308 0.308 )—cluster in the middle region, showing steady improvements ( Δ ≈ + 0.10 ∼ + 0.11 \Delta\approx+0.10\sim+0.11 ) where the agent successfully generalizes coding patterns or OS commands across related instructions.

The HLE Anomaly: Generalization vs. Memorization.

HLE presents a unique outlier. Despite having the lowest similarity ( 0.186 0.186 ) due to its diverse, multi-disciplinary nature, it exhibits a surprisingly high runtime gain ( 0.357 → 0.570 , Δ = + 0.213 0.357\rightarrow 0.570,\Delta=+0.213 ). This gain operates on a different mechanism than ALFWorld. In high-similarity benchmarks, MemRL succeeds via Positive Transfer —generalizing shared patterns to new instances. In contrast, the gain in HLE stems from Runtime Memorization . Since HLE questions are distinct and domain-specific, the agent relies on the Runtime Learning phase to “memorize” specific solutions to difficult problems through repeated exposure. This distinction highlights MemRL ’s versatility: it supports both pattern generalization in structured domains and specific knowledge acquisition in diverse domains.

## Appendix C Advanced Capabilities: Transfer and Merging

### C.1 Cross-Model Memory Transferability

We investigate whether the procedural knowledge captured by MemRL is specific to the training policy or if it generalizes across different architectures. To test this, we take a memory bank fully trained for 10 epochs on the HLE benchmark using our strongest agent, Gemini-3-pro , and directly transfer it—without any fine-tuning—to three distinct inference models: Qwen3-235B , GPT-5.2(High) , and Gemini-3-flash .

As summarized in Table 5 , the transferred memory yields substantial zero-shot performance gains across all models. Notably, smaller or distilled models experience the largest relative improvements; for instance, Qwen3-235B improves by over 3 × 3\times ( 0.150 → 0.531 0.150\rightarrow 0.531 ) and Gemini-3-flash nearly doubles its success rate ( 0.347 → 0.583 0.347\rightarrow 0.583 ). Even GPT-5.2(High) , a highly capable reasoning model, sees a significant boost ( 0.354 → 0.571 0.354\rightarrow 0.571 ).

These results suggest that MemRL captures model-agnostic problem-solving patterns—such as efficient code skeletons and reasoning templates—rather than model-specific artifacts. This effectively allows the memory bank to function as a portable knowledge base, enabling weaker models to “inherit” the capabilities of a stronger teacher model through simple retrieval.

### C.2 Multi-Task Memory Merging and Interference Analysis

To evaluate the composability and robustness of MemRL in multi-task scenarios, we conducted a memory merging experiment. Specifically, we aggregated the finalized memory banks learned from the last epoch of two distinct domains within the Lifelong Agent Bench: Operating System Control ( M O ​ S M_{OS} ) and Database Management ( M D ​ B M_{DB} ). The agent was then evaluated on each respective benchmark using this unified, heterogeneous memory bank ( M U ​ n ​ i ​ f ​ i ​ e ​ d = M O ​ S ∪ M D ​ B M_{Unified}=M_{OS}\cup M_{DB} ), without any further training or fine-tuning.

As presented in Table 6 , the results demonstrate that merging memories introduces negligible interference. The performance on the DB Task remains identical ( 0.960 0.960 ), while the OS Task exhibits only a marginal fluctuation ( 0.788 → 0.784 0.788\rightarrow 0.784 ). This robustness is intrinsic to our Two-Phase Retrieval mechanism. Since the semantic spaces of OS commands and SQL queries are largely orthogonal, the Phase-A similarity filter effectively acts as a semantic gate, automatically excluding irrelevant cross-task memories before they enter the value-based ranking stage. This confirms that MemRL supports modular memory composition, allowing agents to scale capabilities by simply merging memory modules without suffering from negative transfer or catastrophic interference.

## Appendix D Baseline and Benchmark Details

To ensure a rigorous evaluation, we compare MemRL against a diverse set of baselines ranging from simple sampling strategies to advanced agentic memory systems. All baselines are evaluated under a unified frozen-backbone setting to isolate the contribution of the memory and retrieval mechanisms.

### D.1 Baselines

We categorize the baselines into three groups based on their interaction with memory and environment:

##### I. Test-Time Scaling Strategy

• Pass@k: This is a standard sampling-based baseline. It generates k k independent candidate solutions for a given query and selects the best one based on the benchmark’s verifier (if available) or reports the success rate if at least one candidate passes. This baseline serves as a measure of the inherent capability of the frozen LLM without any memory persistence.

##### II. Retrieval-Augmented Generation (RAG) Approaches

• RAG ( Lewis et al., 2020 ) : Represents the standard semantic retrieval paradigm. It utilizes an embedding model to encode the current query and retrieves the top- k k most semantically similar past experiences (or documents) from the external memory. These retrieved contexts are then prepended to the prompt to guide the LLM’s generation.

• Self-RAG ( Asai et al., 2023 ) : An advanced RAG variant that incorporates a self-critique mechanism. Unlike standard RAG, Self-RAG performs selective retrieval and uses a critique model (or self-prompting) to verify the relevance and factual correctness of the retrieved content before integrating it into the generation process.

##### III. Agentic Memory Systems

• Mem0 ( Chhikara et al., 2025 ) : A recently proposed memory layer for LLMs that manages memory through structured operations. It employs specific APIs for adding, retrieving, and updating memory, aiming to maintain a personalized and persistent context across interactions.

• MemP ( Fang et al., 2025 ) : A framework focused on procedural memory. It distills past successful trajectories into reusable, procedure-like memory entries. MemP maintains a memory repository using a build-retrieve-update cycle, allowing the agent to recall high-level plans rather than raw trajectory data.

### D.2 Benchmark Datasets

We evaluate performance across four benchmarks selected to cover diverse domains: code generation, OS interactions, embodied decision-making, and multidisciplinary reasoning.

• BigCodeBench ( Zhuo et al., 2025 ) : A challenging benchmark for library-oriented code generation that requires agents to implement complex functionalities using diverse third-party libraries. Unlike traditional benchmarks focused on algorithmic snippets, BigCodeBench emphasizes practical software engineering capabilities. We evaluate on the BigCodeBench-Instruct (Full) split, which tasks the agent with synthesizing complete functional code from natural language instructions across the full range of difficulty levels.

• Lifelong Agent Bench ( Zheng et al., 2025 ) : Designed to evaluate agents in a continuous learning setting involving Operating System (OS) and Database (DB) interactions. It tests the agent’s capacity to adapt to new tools and commands over a long horizon without forgetting previous skills.

• ALFWorld ( Shridhar et al., 2021 ) : An embodied navigation and manipulation benchmark. It requires the agent to solve textual logic puzzles within a simulated household environment (e.g., “put a clean apple in the fridge”). This tests the agent’s ability to learn and retrieve multi-step plans.

• Humanity’s Last Exam (HLE) ( Phan et al., 2025 ) : A rigorous multidisciplinary reasoning benchmark featuring hard problems from mathematics, humanities, and sciences. It serves as a stress test for the agent’s general reasoning capability and its ability to retrieve relevant knowledge for disparate tasks.

## Appendix E Implementation and Reproducibility Details

To facilitate reproducibility, we provide the exact model versions, hyperparameter settings, and environmental configurations used in our experiments.

### E.1 Model Specifications

All LLM reasoning and generation tasks were performed using the models listed in Table 7 . We used the official APIs with a fixed temperature to ensure deterministic evaluation where possible.

### E.2 Hyperparameter Settings

Table 8 details the specific hyperparameters used for MemRL and the baselines. The similarity threshold δ \delta is adaptive to the dataset density; specifically, we determine δ \delta by calculating the pairwise cosine similarity distribution of task descriptions within each benchmark and selecting the threshold at the top 20% quantile. This ensures that only the most relevant historical experiences are considered for retrieval.

### E.3 Data Partitioning

To evaluate the effectiveness of MemRL , we categorize our experiments into Runtime Learning and Transfer Learning settings. Table 9 summarizes the dataset sizes and partitioning strategies used for each benchmark.

† For ALFWorld Transfer Learning, the agent uses the same 3,553 tasks as memory context but is evaluated on 140 novel instances of seen task types.

For benchmarks utilizing random splits ( OS , DB , and BCB ), we use a fixed random seed of 42 to ensure reproducibility. In ALFWorld , the Transfer Learning phase specifically tests generalization to new instances within known categories, ensuring the agent learns procedural patterns rather than specific trajectories.

### E.4 Model Selection and Performance Analysis

We select the backbone model for each benchmark to ensure a valid learning signal relative to task complexity. Since MemRL relies on high-value trajectories to perform utility update over retrieved memories, extremely low initial competence can make the feedback effectively unusable. For instance, on challenging benchmarks such as HLE, weaker models may start at ≈ 4 % \approx 4\% success rate (e.g., GPT-4o-mini ), yielding too few successful trajectories for stable utility estimation; in this scenario, environmental feedback is dominated by noise, which can prevent meaningful learning and hinder convergence.

At the other extreme, using the strongest available models on simpler benchmarks can cause performance saturation (ceiling effects), leaving little headroom to quantify the marginal gains attributable to the memory mechanism. Therefore, we match model capability to each task’s difficulty to avoid both the no-signal situation (insufficient successes) and the ceiling effect (insufficient headroom). This design choice enables a more faithful evaluation of improvements that are intrinsic to MemRL rather than artifacts of an ill-posed performance condition.

Importantly, our evaluation spans backbones of different scales—from “mini” to “pro” tiers (Table 7 )—to test whether MemRL remains effective across capability levels. The resulting performance trends support the scale-invariant robustness of MemRL . Moreover, the cross-model transfer results (Table 5 ) further indicate that the procedural knowledge captured in memory is portable across backbones, suggesting that the learned utility over memories generalizes beyond any single model’s inherent strength.

To further explore the generality of MemRL across different model capabilities and task complexities, we also deployed the GPT-4o-mini model in the ALFWorld benchmark. This model is identical to the backbone used in the Lifelong Agent Bench, allowing for a direct comparison of its performance across environments with varying exploration intensities. As an exploration-intensive environment, ALFWorld poses significant demands on the base model’s reasoning and planning capabilities. The Table 10 and Table 11 present the runtime learning and knowledge transfer abilities of GPT-4o-mini .

These results, using GPT-4o-mini as a consistent backbone, unequivocally demonstrate MemRL ’s superior and generalized effectiveness across all benchmarks. In runtime learning (Table 10 ), MemRL achieves the highest average Last Epoch Success Rate and Cumulative Success Rate, showing significant gains: its average Last Epoch SR is 12.6 % 12.6\% points higher than “No Memory”, and its average CSR surpasses MemP by 11.2 % 11.2\% points. This advantage is particularly pronounced in the challenging ALFWorld environment. Similarly, in transfer learning (Table 11 ), MemRL secures the highest average Success Rate, 10.6 % 10.6\% points higher than “No Memory” and 6.1 % 6.1\% points higher than MemP. These consistent improvements across tasks and learning paradigms confirm that MemRL effectively enhances the GPT-4o-mini backbone’s decision-making capabilities, leveraging learned utility over memories for more robust performance.

## Appendix F Cost and Efficiency Analysis

Real-world deployment of autonomous agents requires balancing performance gains with computational costs. In this section, we analyze the token consumption and runtime latency of MemRL compared to the strong baseline MemP on the compute-intensive Humanity’s Last Exam (HLE) benchmark.

### F.1 Token Consumption

Since MemRL operates as a non-parametric approach without gradient-based fine-tuning, the primary cost arises from LLM API calls. We compare the average token usage per question (Q) across the entire learning trajectory (10 epochs).

MemRL ’s token consumption is comparable to that of MemP, as both methods utilize identical interaction loops (reasoning + summarization). On the HLE benchmark, the average total token consumption per question for MemRL is approximately 32K . This similarity in token usage is because the complexity of MemRL lies in how memories are retrieved and updated (via Q-values), not in how much context is fed to the LLM. Therefore, the significant performance gains of MemRL reported in the main text are achieved without increasing the inference budget.

### F.2 Runtime Latency and Stability

A common concern with two-stage retrieval and reinforcement learning components is the potential for increased latency. We empirically validate the wall-clock time required to complete each epoch (2,500 questions) in Figure 11 .

##### Negligible Algorithmic Overhead.

Figure 11 demonstrates that the runtime of MemRL is commensurate with, and often more stable than, that of MemP. The fluctuations observed (e.g., the spikes in the MemP curve at Epochs 4 and 6) are attributed to external factors such as API network latency and throughput variability, rather than algorithmic complexity.

Specifically, the additional components in MemRL introduce minimal computational cost: • Dual-Stage Retrieval: This involves basic vector dot-products and scalar score weighting, operating in milliseconds.

• RL Update: The Q-value update in a Monte Carlo style on scalars, which is an O ⁡ ( 1 ) O(1) operation.

Compared to the hours required for LLM generation over 2,500 questions, these millisecond-level operations are virtually imperceptible. The stability of the MemRL curve further suggests that our method does not introduce complex blocking operations that would exacerbate network-induced delays.

## Appendix G Extended Limitations and Future Work

This appendix provides a more detailed discussion on the limitations of MemRL and outlines promising avenues for future research, building upon the foundations established in the main paper.

### G.1 Update Protocols and Memory Consolidation

The current step-wise update protocol of MemRL , while enabling rapid adaptation, can introduce high-variance noise in long-horizon trajectories. This presents a challenge for stabilizing value estimation over extended sequences. A valuable future direction involves exploring more robust multi-step update mechanisms, which could offer slower but more stable learning. Furthermore, combining these with periodic consolidation of similar intentions and experiences within the memory bank could significantly improve the spatial efficiency of the memory, reducing redundancy and enhancing retrieval quality.

### G.2 Precise Credit Assignment in Multi-Memory Updates

A significant challenge arises from the credit-assignment ambiguity encountered when multiple experiences from the memory are referenced and updated simultaneously. Determining the precise contribution of each referenced memory to the final outcome is complex and affects the efficiency of learning. Future research could investigate methods for more precise experience attribution, drawing inspiration from techniques like Shapley values ( Shapley and others, 1953 ) , commonly used in cooperative game theory, or value decomposition methods prevalent in multi-agent reinforcement learning ( Rashid et al., 2020 ; Sunehag et al., 2017 ) . Such approaches could lead to more accurate updates and faster convergence.

### G.3 Task Similarity and Generalization

MemRL ’s effectiveness is observed to improve with the number of encountered tasks, aligning well with the characteristics of runtime learning. This is because the algorithm leverages past experiences, and a richer, more diverse set of similar experiences directly enhances its ability to retrieve relevant knowledge. However, when task similarity in the experience base is low, the method may inherently degrade into a less efficient reflection-like behavior, as direct experience transfer is limited. This is not a deficiency of the method but rather a characteristic of its reliance on learned utility from memory. For industrial deployment and real-world applications, this implies that maintaining a sufficiently high “task similarity density” within the agent’s operating environment or its collected memory is crucial. Strategies to achieve this could include active curriculum learning, environment design that promotes diverse yet related tasks, or techniques that facilitate hierarchical abstraction to enable generalization beyond direct, low-level experience matches. Enhancing retrieval mechanisms to proactively identify and adapt to novel task structures, or integrating hierarchical abstraction, are key for improving cross-task generalization.

### G.4 Memory Security and Robustness to Attack

MemRL is sensitive to the quality of feedback, particularly vulnerable to “reward hacking” if the verifier produces false positives. Incorrectly learned high Q-values from spurious feedback can quickly solidify and propagate erroneous behavioral patterns, leading to systemic failures. This highlights a critical challenge: memory security. A maliciously injected sample into the memory bank could rapidly diffuse pollution, potentially causing an intelligent agent to collapse. Future research must address the safety and trustworthiness of agent memories. Fortunately, the mutable nature of experience offers a silver lining: once contamination or attack is identified, polluted experiences can be swiftly pruned, allowing for recovery without disrupting the utility of previously learned valid experiences.

### G.5 Multi-Agent Collaboration and Shared Memory

As many enterprises transition from single agents to multi-agent clusters (swarms), the question of “shared memory” becomes important. Does the MemRL approach support knowledge sharing, allowing lessons learned and updated Q-values from one agent to immediately benefit others? We’ve explored scenarios where the memory, treated as a persistent resource, can indeed be shared among different models or agents (Appendix C.1 ). Furthermore, adopting a multi-agent paradigm, akin to distributed parameter updates, could be highly beneficial. Each agent could accumulate experience and save it as memory during its operation, contributing to a large, collective memory pool. This would enable different agents to implicitly leverage each other’s learned experiences, fostering a more collaborative and efficient learning ecosystem.

Beyond this collective pooling, a significant and promising frontier involves investigating the selective nature of such knowledge diffusion through the lens of transfer learning. As the number of agents increases, particularly beyond simple pairings, the challenge of ”what to share” and ”with whom to share” becomes a critical research direction. Future work could explore mechanisms that differentiate between universally applicable procedural insights and task-specific noise, ensuring that memory transfer remains contextually relevant and avoids the risks of negative transfer. Navigating these trade-offs between global collective intelligence and targeted knowledge distribution will be essential for building scalable, self-evolving swarms.

### G.6 Dedicated Domains and Hybrid Architectures

While this work strongly advocates for freezing large language models (LLMs) to prevent catastrophic forgetting, a question arises regarding highly specialized domains where the base model may not comprehend foundational terminology. Is MemRL alone sufficient in such cases? We anticipate a future hybrid model where companies periodically fine-tune foundational models (e.g., annually) to update their core vocabulary and understanding, while simultaneously leveraging MemRL for daily behavioral adaptation and runtime learning. This approach requires the base model to possess a relatively high level of “intelligence” to initially grasp and subsequently learn new terms through interaction and feedback.

## Appendix H Case Study: High-Utility Failure Analysis (Near-Misses)

This appendix section provides qualitative case studies of high-value near-miss memories mined from the 10-epoch OS-Interaction run. CS denotes Case Study . Each box below contains: origin task, retrieved reflection memory, a short explanation, and the target task where it was retrieved.

## Appendix I Prompts

We provide the exact prompt strings and message templates used by our MemRL implementation across all benchmarks. To minimize ambiguity, we separate prompts used to summarize experiences into memories from prompts used at task time for generation/inference.

### I.1 Experience Summarization Prompts

### I.2 Generation and Inference Prompts

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
