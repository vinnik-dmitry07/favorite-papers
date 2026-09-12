##### Report GitHub Issue

Content selection saved. Describe the issue below:

marginparsep has been altered. topmargin has been altered. marginparpush has been altered.

The page layout violates the ICML style.

Please do not change the page layout, or include packages like geometry, savetrees, or fullpage, which change it for you.

We’re not able to reliably undo arbitrary changes to the style. Please remove the offending package(s), or layout-changing commands and try again.

From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning

Xitai Jiang 1 , 2 ∗ † {}^{\,1,2\,*\,\dagger} , Zihan Tang 2 ∗ {}^{\,2\,*} , Wenze Lin 1 , 2 ∗ {}^{\,1,2\,*} , Yang Yue 1 , Shenzhi Wang 1 , and Gao Huang 1 ​ 🖂 {}^{\,1\,\textrm{\Letter}}

1 {}^{1\,} LeapLab, Tsinghua University 2 {}^{2\,} Qiuzhen College, Tsinghua University

∗ Equal Contribution † Project Lead 🖂 {}^{\textrm{\Letter}} Corresponding Author

## 1 Introduction

Reinforcement learning from verifiable rewards (RLVR) has emerged as a dominant paradigm for training large language models on mathematical reasoning, delivering strong empirical gains across benchmarks spanning grade-school arithmetic to olympiad-level competition ( Guo et al., 2025 ; Yu et al., 2025 ; Shao et al., 2024 ; Jaech et al., 2024 ; Wen et al., 2025 ) . The key to its success is that a correct final answer provides an unambiguous and automatically checkable reward signal. This removes the need for costly human annotation and avoids the reward hacking risks of learned reward models ( Skalse et al., 2022 ) .

A central goal of RLVR is to help models solve previously unsolved problems and improve their reasoning ability. However, prior work suggests that direct RLVR often improves sampling efficiency more than it substantially expands the model’s capability boundary ( Yue et al., 2025 ; Shojaee et al., 2025 ; Alam & Rastogi, 2025 ) . Further studies indicate that training at the edge of the model’s current capability with challenging problems is key for better reasoning ability ( Pikus et al., 2025 ; Li et al., 2026a ; Dai et al., 2026 ; Ma et al., 2025 ) . This makes hard problems particularly valuable for RL training. Yet typical RLVR methods like GRPO ( Guo et al., 2025 ) struggle precisely on these problems. First, rewards are normalized within a group of rollouts sampled from the same prompt, so a group in which all rollouts fail provides no learning signal. Second, outcome-based RLVR assigns one sample-level advantage to the entire rollout. Thus, a near-miss attempt receives the same credit as an immediate failure. It is therefore crucial to extract learning signals from such hard-but-informative problems.

A natural way to learn from hard problems is to make better use of expert trajectories. Existing methods mainly follow two routes. One route is compensating for sparse rewards by training the model to imitate expert-generated trajectories, such as supervised fine-tuning and some off-policy RL methods ( Li et al., 2025a ; Yan et al., 2025 ; Fu et al., 2025 ; Zhang et al., 2025a ; Lv et al., 2025 ) . However, they replace the model’s own on-policy exploration with supervised imitation, and the resulting distribution shift between the expert and student policies can hurt training stability and out-of-distribution generalization ( Shenfeld et al., 2025 ; Chu et al., 2025 ) . The other route uses on-policy curriculum RL. These methods provide an expert reasoning prefix or other hints and train the model to complete the remaining solution. ( Amani et al., 2025 ; Zhang et al., 2025b ; Wu et al., 2025a ; Qiyuan et al., 2026 ; Qu et al., 2026 ; Yan et al., 2025 ; Shi et al., 2026 ) . However, these hints are treated as fixed conclusions rather than targets the model must derive, so the model does not need to discover the critical reasoning steps on its own, and the supplied context still shifts the model away from its own generation distribution. In fact, solving hard problems requires the model to explore and master the intermediate conclusions behind these hints by itself. This raises a central question: how can we build a curriculum for hard problems that keeps the model exploring on its own, while also properly giving credit to the intermediate progress it solves along the way?

We propose SCRL ( Subproblem Curriculum Reinforcement Learning ), drawing inspiration from a familiar structure in mathematical competitions: the multi-part problem. In a competition exam, a hard problem is broken into a sequence of subproblems of increasing difficulty, all visible at once; solving an earlier part yields a result that serves as a natural basis for the next. Given the expert solution to a hard problem, we offline construct a sequence of K K verifiable subproblems using an external LLM. The subproblems are ordered from easier to harder, with each later subproblem building on the previous ones, and each subproblem has a verifiable answer. We fix the final subproblem as the original problem itself and ask the model to answer all K K subproblems in a single on-policy rollout . This organically realizes a curriculum learning structure: when the model correctly solves an earlier subproblem, its answer becomes a natural basis for the next, guiding the model toward increasingly difficult reasoning. Critically, the reasoning steps that bridge consecutive subproblems are self-produced, earned through the model’s own on-policy rollout. These intermediate results provide verifiable process-level supervision, naturally enabling finer-grained credit assignment within the rollout. We realize this through subproblem-level normalization , a novel RLVR training technique that normalizes rewards independently at each subproblem position and assigns the resulting advantages to the corresponding answer spans. In particular, to prevent the model from rewarding later subproblems without solving earlier ones, we align credit with curriculum progress by counting only the longest consecutively solved subproblem sequence. For example, the subproblem reward [ 1 , 1 , 0 , 1 ] [1,1,0,1] is treated as [ 1 , 1 , 0 , 0 ] [1,1,0,0] , because progress after the first failed subproblem is not credited.

We validate SCRL with both theory and experiments. Theoretically, we show that subproblem decomposition lifts hard problems out of gradient dead zones by recovering non-degenerate learning signals from earlier subproblems. We formalize this as a metric recovery result, where optimization is lifted from the original policy manifold to a subproblem product manifold and the recovery ratio grows with problem difficulty. The empirical results are consistent with this prediction: SCRL improves over strong curriculum-learning baselines across mathematical reasoning benchmarks. Ablations further confirm the effectiveness of subproblem-level credit assignment and show that SCRL does not rely on highly curated subproblems or strong subproblem generators.

Our main contributions are: • SCRL framework for curriculum learning. We propose a curriculum RL framework that turns each hard problem into a sequence of verifiable subproblems, enabling process-level supervision within a single on-policy rollout. This keeps the model exploring near the boundary of its current capability, making hard problems more effective for training.

• Subproblem-level normalization for fine-grained credit assignment. We introduce subproblem-level normalization , which normalizes rewards independently at each subproblem position and assigns the resulting advantages to the corresponding answer spans, enabling fine-grained credit assignment without external rubrics or additional reward models.

• Theoretical and empirical validation. We provide a metric recovery analysis showing that subproblem decomposition lifts hard problems out of gradient dead zones, with larger relative gains as the original problem becomes harder. Experiments across seven mathematical reasoning benchmarks verify these predictions and show consistent gains over strong baselines (+4.1/+1.9 average-point gains on Qwen3-4B/14B; +3.7 pass@ 1 1 and +4.6 pass@ 64 64 points on three hard benchmarks).

## 2 Related Work

##### Reinforcement Learning with Verifiable Rewards (RLVR)

Recent advances in Large Language Models (LLMs) have highlighted the effectiveness of Reinforcement Learning (RL) in domains with deterministic verifiers such as mathematics and programming Shao et al. (2024) ; Jaech et al. (2024) ; Trinh et al. (2024) ; Yang et al. (2024) ; Qu et al. (2025) ; Wang et al. (2025) . Unlike open-ended generation, these tasks provide unambiguous feedback, allowing for the optimization of policy models through algorithms like Proximal Policy Optimization (PPO) Schulman et al. (2017) or the more memory-efficient Group Relative Policy Optimization (GRPO) Guo et al. (2025) . However, RLVR faces a significant challenge: for difficult problems, the reward signal becomes extremely sparse, leading to a failure in obtaining meaningful policy gradients Uesato et al. (2022) . This challenge is often framed as a credit assignment problem: outcome-based rewards provide a global signal but fail to pinpoint which specific reasoning steps contributed to the final success or failure Lightman et al. (2023) . While iterative self-improvement methods like STaR Zelikman et al. (2022) and ReST Gulcehre et al. (2023) ; Zhang et al. (2024) attempt to bridge this gap through rejection sampling on easier instances, they still struggle when the task’s difficulty exceeds the model’s current exploration horizon. Consequently, curriculum learning Bengio et al. (2009) ; Yang et al. (2025) ; Li et al. (2025b) ; Parashar et al. (2025) ; Wu et al. (2025b) has become a common way to densify learning signals for hard problems by breaking hard tasks into manageable stages.

##### Curriculum Learning for Reasoning

Existing curriculum learning methods for mathematical reasoning can be broadly categorized into two paradigms. The first category focuses on providing external hints or guidance when the model fails to solve a challenging problem. Notable works such as StepHint Zhang et al. (2025a) , Scaf-GRPO Zhang et al. (2025b) and other hint-driven RL frameworks Wu et al. (2025a) ; Qiyuan et al. (2026) ; Qu et al. (2026) ; Yan et al. (2025) ; Shi et al. (2026) , utilize teacher model or self-generated rationales as auxiliary prefixes to lower the exploration threshold. The second category involves rewriting the original problem into simpler versions or augmenting the prompt with supplementary information to facilitate reasoning Chen et al. (2026) ; Wu et al. (2025b) ; Li et al. (2026b) ; Dai et al. (2026) ; Li et al. (2026a) ; Liang et al. (2025) . As seen in MQR Dai et al. (2026) and QuestA Li et al. (2026a) , these methods effectively create a difficulty gradient by manipulating the problem context. However, a fundamental limitation shared by these methods is their reliance on additional context. By providing the hint or reformulated problem as a static prefix, these approaches primarily optimize the model’s continuation capability. As a result, the model fails to internalize the underlying scaffolding logic, as it is never required to generate the hints or auxiliary structures itself. In contrast, SCRL requires the model to generate the entire scaffolded multi-part sequence within a structured response, ensuring that the policy learns to both construct the intermediate reasoning steps and solve the final target problem.

## 3 Method

We propose SCRL ( Subproblem Curriculum Reinforcement Learning ), a curriculum RL framework that turns hard problems into verifiable subproblem curricula for finer-grained credit assignment. SCRL has three steps. First, given a reference solution, an external LLM derives K K verifiable subproblems from the reasoning chain and constructs the subproblem curriculum. Second, the policy answers all K K subproblems in one on-policy rollout. We then verify each subproblem answer and apply progress-aware correction to obtain progress-aware subproblem rewards. Subproblem-level normalization computes an advantage for each subproblem position, which is then used for token-level credit assignment. Finally, to reduce prompt mismatch, SCRL uses mixed-group training, jointly optimizing curriculum rollouts and original-problem rollouts in the same update.

### 3.1 Preliminaries: GRPO

Given a prompt q q , GRPO samples G G rollouts { o i } i = 1 G ∼ π θ ( ⋅ ∣ q ) \{o_{i}\}_{i=1}^{G}\sim\pi_{\theta}(\cdot\mid q) and assigns each rollout a scalar verifiable reward r i r_{i} . It then optimizes the clipped objective ℒ GRPO ( θ ) = − 1 ∑ i L i ∑ i = 1 G ∑ t = 1 L i min ( ρ i , t A i , clip ( ρ i , t , 1 − ε , 1 + ε ) A i ) − β D KL ( π θ ∥ π ref ) . \mathcal{L}_{\mathrm{GRPO}}(\theta)=-\frac{1}{\sum_{i}L_{i}}\sum_{i=1}^{G}\sum_{t=1}^{L_{i}}\min\!\Bigl(\rho_{i,t}A_{i},\;\mathrm{clip}(\rho_{i,t},1-\varepsilon,1+\varepsilon)A_{i}\Bigr)-\beta D_{\mathrm{KL}}(\pi_{\theta}\|\pi_{\mathrm{ref}}). (1)

Here A i = r i − mean ⁡ ( { r i } i = 1 G ) std ⁡ ( { r i } i = 1 G ) A_{i}=\frac{r_{i}-\mathrm{mean}(\{r_{i}\}_{i=1}^{G})}{\mathrm{std}(\{r_{i}\}_{i=1}^{G})} is the group-normalized advantage, and ρ i , t = π θ ​ ( o i , t ∣ q , o i , < t ) π θ old ​ ( o i , t ∣ q , o i , < t ) \rho_{i,t}=\frac{\pi_{\theta}(o_{i,t}\mid q,o_{i,<t})}{\pi_{\theta_{\mathrm{old}}}(o_{i,t}\mid q,o_{i,<t})} is the importance sampling ratio at token t t . Since the same A i A_{i} is assigned to every token in o i o_{i} , GRPO performs sample-level credit assignment.

### 3.2 SCRL Framework

##### Build subproblems.

For each hard problem x x , we start from an existing chain-of-thought reference solution. An external LLM rewrites its intermediate progress nodes into K K verifiable subproblems, rather than solving the problem from scratch. The exact generation prompt is provided in Appendix I , and the main guidelines are summarized below.

##### Curriculum prompt.

Let x x denote the original problem. We define the curriculum prompt t K ​ ( x ) t_{K}(x) as the prompt that presents all K K subproblems s ( 1 ) , … , s ( K ) s^{(1)},\ldots,s^{(K)} simultaneously and asks the model to solve them in order. Thus, x x corresponds to the original-problem rollout, while t K ​ ( x ) t_{K}(x) corresponds to the curriculum rollout. The detailed prompt template is provided in Appendix J.1 .

##### Response format.

During curriculum rollouts, the model is asked to answer the K K subproblems using explicit tags <pj> and </pj> : <p1> a ( 1 ) </p1> ⋯ <pK> a ( K ) </pK> , \texttt{<p1>}\;a^{(1)}\;\texttt{</p1>}\;\cdots\;\texttt{<pK>}\;a^{(K)}\;\texttt{</pK>}, where a ( j ) a^{(j)} is the response to subproblem j j . These tags not only specify the response format, but also mark the token span of each subproblem answer. This allows us to verify each answer separately and later assign the corresponding subproblem-level advantage back to the tokens inside that span.

#### 3.2.1 Progress-Aware Subproblem Rewards

##### Curriculum progress.

For a curriculum rollout o i ∼ π θ ( ⋅ ∣ t K ( x ) ) o_{i}\sim\pi_{\theta}(\cdot\mid t_{K}(x)) , verifying the K K extracted subproblem answers gives a raw reward vector 𝐫 i = ( r i ( 1 ) , … , r i ( K ) ) ∈ { 0 , 1 } K \mathbf{r}_{i}=(r_{i}^{(1)},\ldots,r_{i}^{(K)})\in\{0,1\}^{K} . If the response does not follow the required format, we set 𝐫 i = 𝟎 \mathbf{r}_{i}=\mathbf{0} . We define the curriculum progress k i ∈ { 0 , 1 , … , K } k_{i}\in\{0,1,\ldots,K\} as the maximum number of consecutively solved subproblems from the beginning: k i := max ⁡ { j ∈ { 0 , 1 , … , K } | r i ( 1 ) = ⋯ = r i ( j ) = 1 } . k_{i}:=\max\bigl\{j\in\{0,1,\ldots,K\}\;\big|\;r_{i}^{(1)}=\cdots=r_{i}^{(j)}=1\bigr\}. (2) Thus, k i = 0 k_{i}=0 means the first subproblem is incorrect, while k i = K k_{i}=K means all subproblems are solved. The curriculum progress k i k_{i} tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout.

##### Progress-aware correction.

Directly rewarding each subproblem independently may credit later subproblems despite earlier failures, creating a potential reward-hacking shortcut. We therefore align rewards with curriculum progress by keeping only the consecutively solved prefix: r ~ i ( j ) := { r i ( j ) , j ≤ k i , 0 , j > k i , 𝐫 ~ i = ( r ~ i ( 1 ) , r ~ i ( 2 ) , … , r ~ i ( K ) ) . \tilde{r}_{i}^{(j)}:=\begin{cases}r_{i}^{(j)},&j\leq k_{i},\\ 0,&j>k_{i},\end{cases}\qquad\tilde{\mathbf{r}}_{i}=\bigl(\tilde{r}_{i}^{(1)},\tilde{r}_{i}^{(2)},\ldots,\tilde{r}_{i}^{(K)}\bigr). (3) For example, when K = 4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) . For notational convenience, we use R i ( j ) := r ~ i ( j ) R_{i}^{(j)}:=\tilde{r}_{i}^{(j)} as the final subproblem reward for training.

#### 3.2.2 SCRL Training Algorithm

In this section, we describe the training details of SCRL, including subproblem-level normalization for advantage computation, token-level credit assignment, and mixed-group training. The full training procedure is summarized in Appendix C .

##### Subproblem-level normalization.

Given G G curriculum rollouts o i o_{i} for i = 1 , … , G i=1,\ldots,G , we normalize the final subproblem rewards at each subproblem position j j across the rollout group: A i ( j ) = R i ( j ) − mean ⁡ ( { R i ( j ) } i = 1 G ) std ⁡ ( { R i ( j ) } i = 1 G ) . A_{i}^{(j)}=\frac{R_{i}^{(j)}-\mathrm{mean}\bigl(\{R_{i}^{(j)}\}_{i=1}^{G}\bigr)}{\mathrm{std}\bigl(\{R_{i}^{(j)}\}_{i=1}^{G}\bigr)}. (4) Thus, the subproblem-level advantage A i ( j ) A_{i}^{(j)} measures the relative success of rollout i i at subproblem position j j within the rollout group, independent of rewards at other subproblem positions.

##### Token-level credit assignment.

After computing the subproblem-level advantages, we assign them back to the tokens of the corresponding subproblem answers. Using the structured response format, we define sub i ​ ( t ) = j \mathrm{sub}_{i}(t)=j if token o i , t o_{i,t} lies between <pj> and </pj> ; then A i , t = A i ( sub i ​ ( t ) ) A_{i,t}=A_{i}^{(\mathrm{sub}_{i}(t))} gives the token-level advantage. Tokens outside all answer spans receive zero advantage, and if the response does not follow the required format, all tokens in that response receive zero advantage. This converts subproblem-level progress into token-level learning signals for the corresponding answer spans.

##### Mixed-group training.

Training only on the curriculum prompt t K ​ ( x ) t_{K}(x) can cause prompt mismatch, because evaluation uses the original prompt x x . We therefore use mixed-group training: for each problem x x , G / 2 G/2 rollouts are sampled from t K ​ ( x ) t_{K}(x) and optimized with token-level advantages from subproblem-level normalization, while the other G / 2 G/2 rollouts are sampled from x x and optimized with standard outcome-based GRPO. The final SCRL objective is ℒ SCRL ​ ( θ ) \displaystyle\mathcal{L}_{\mathrm{SCRL}}(\theta) = − 1 ∑ i = 1 G L i [ ∑ i = 1 G / 2 ∑ t = 1 L i min ( ρ i , t A i , t , clip ( ρ i , t , 1 − ε , 1 + ε ) A i , t ) \displaystyle=-\frac{1}{\sum_{i=1}^{G}L_{i}}\Bigg[\sum_{i=1}^{G/2}\sum_{t=1}^{L_{i}}\min\!\Bigl(\rho_{i,t}A_{i,t},\mathrm{clip}(\rho_{i,t},1-\varepsilon,1+\varepsilon)A_{i,t}\Bigr) + ∑ i = G / 2 + 1 G ∑ t = 1 L i min ( ρ i , t A i , clip ( ρ i , t , 1 − ε , 1 + ε ) A i ) ] − β D KL ( π θ ∥ π ref ) . \displaystyle\quad+\sum_{i=G/2+1}^{G}\sum_{t=1}^{L_{i}}\min\!\Bigl(\rho_{i,t}A_{i},\mathrm{clip}(\rho_{i,t},1-\varepsilon,1+\varepsilon)A_{i}\Bigr)\Bigg]-\beta D_{\mathrm{KL}}(\pi_{\theta}\,\|\,\pi_{\mathrm{ref}}). (5) The two bracketed terms correspond to curriculum rollouts and original-problem rollouts respectively. The complete training procedure is summarized in Algorithm 1 .

## 4 Theoretical Analysis

Using the information geometry of the policy manifold ℳ = { π θ : θ ∈ Θ } \mathcal{M}=\{\pi_{\theta}:\theta\in\Theta\} equipped with the Fisher–Rao metric ( Amari, 2016 ) , we show that hard problems can place outcome-based GRPO in a gradient dead zone , while subproblem decomposition lifts optimization to a product manifold that recovers useful gradient information. Full discussions and proofs are provided in Appendix B .

###### Definition 4.1 (Effective and Lifted Gradient Information Matrices) .

Under GRPO, let o 1 , … , o G ∼ i . i . d . π θ ( ⋅ ∣ x ) o_{1},\ldots,o_{G}\overset{\mathrm{i.i.d.}}{\sim}\pi_{\theta}(\cdot\mid x) be G G sampled rollouts. The effective gradient information matrix (EGIM) of x x and the lifted EGIM of its subproblem transformation 𝒯 ​ ( x ) = t K ​ ( x ) \mathcal{T}(x)=t_{K}(x) are 𝑭 x ​ ( θ ) \displaystyle\bm{F}_{x}(\theta) = 1 G ​ ∑ i = 1 G 𝔼 ⁡ [ g i ​ ( x ) ​ g i ​ ( x ) ⊤ ] , where ​ g i ​ ( x ) = A ^ i ​ ( x ) ​ ∇ θ ​ log ⁡ π θ ​ ( o i ∣ x ) , \displaystyle=\frac{1}{G}\sum_{i=1}^{G}\mathbb{E}\!\left[g_{i}(x)g_{i}(x)^{\top}\right],\qquad\text{where }g_{i}(x)=\hat{A}_{i}(x)\nabla_{\theta}\log\pi_{\theta}(o_{i}\mid x), (6) 𝑭 𝒯 ⁡ ( x ) ​ ( θ ) \displaystyle\bm{F}_{\mathcal{T}(x)}(\theta) = 1 K ​ ∑ j = 1 K 1 G ​ ∑ i = 1 G 𝔼 ⁡ [ A ^ i ( j ) ​ 2 ​ ∇ θ ​ log ⁡ π θ ​ ( o i ( j ) ∣ t K ​ ( x ) ) ​ ∇ θ ​ log ​ π θ ​ ( o i ( j ) ∣ t K ​ ( x ) ) ⊤ ] , \displaystyle=\frac{1}{K}\sum_{j=1}^{K}\frac{1}{G}\sum_{i=1}^{G}\mathbb{E}\!\left[\hat{A}_{i}^{(j)2}\nabla_{\theta}\log\pi_{\theta}(o_{i}^{(j)}\mid t_{K}(x))\nabla_{\theta}\log\pi_{\theta}(o_{i}^{(j)}\mid t_{K}(x))^{\top}\right], (7) Here A ^ i ​ ( x ) \hat{A}_{i}(x) and A ^ i ( j ) \hat{A}_{i}^{(j)} denote the original-problem and subproblem-position advantages respectively, and the smallest eigenvalue λ min ​ ( 𝐅 𝒯 ⁡ ( x ) ​ ( θ ) ) \lambda_{\min}(\bm{F}_{\mathcal{T}(x)}(\theta)) measures the weakest useful gradient signal.

###### Theorem 4.2 (Gradient Dead Zone) .

Let p ( x ; θ ) = Pr π θ [ r ( x , o ) = 1 ] p(x;\theta)=\Pr_{\pi_{\theta}}[r(x,o)=1] be the probability that the current policy solves x x . If p ⁡ ( x , θ ) < δ p(x;\theta)<\delta , then λ min ​ ( 𝑭 x ​ ( θ ) ) ≤ G ​ δ ⋅ C A ^ 2 ⋅ B s 2 = O ⁡ ( δ ) , \lambda_{\min}\!\left(\bm{F}_{x}(\theta)\right)\leq G\delta\cdot C_{\hat{A}}^{2}\cdot B_{s}^{2}=O(\delta), (8)

where C A ^ ≤ G − 1 C_{\hat{A}}\leq\sqrt{G-1} bounds the normalized advantage magnitude and B s B_{s} bounds the score norm (both derived in Appendix B.3 ).

Theorem 4.2 shows that direct RLVR training becomes ineffective on hard problems: when correct rollouts are rare, reward groups collapse and the worst-case effective gradient signal vanishes.

###### Theorem 4.3 (Metric Recovery via Subproblem Decomposition) .

Let x x be in the gradient dead zone with p ⁡ ( x , θ ) < δ p(x;\theta)<\delta . Suppose the subproblem construction satisfies p j ​ ( x , θ ) := Pr ⁡ [ R ( j ) = 1 ∣ t K ​ ( x ) ] ∈ [ p ⋆ , 1 − p ⋆ ] for all ​ j < K , p_{j}(x;\theta):=\Pr[R^{(j)}=1\mid t_{K}(x)]\in[p^{\star},1-p^{\star}]\quad\text{for all }j<K, where p ⋆ ∈ ( δ , 1 / 2 ] p^{\star}\in(\delta,1/2] . Under the conditional identifiability assumption ( 𝔼 ⁡ [ ( v ⊤ ​ ∇ θ ​ log ⁡ π θ ) 2 ∣ r = r 0 ] ≥ σ min 2 > 0 \mathbb{E}[(v^{\top}\nabla_{\theta}\log\pi_{\theta})^{2}\mid r{=}r_{0}]\geq\sigma_{\min}^{2}>0 for all unit v v , r 0 ∈ { 0 , 1 } r_{0}\in\{0,1\} ), λ min ​ ( 𝑭 𝒯 ⁡ ( x ) ​ ( θ ) ) \displaystyle\lambda_{\min}\!\left(\bm{F}_{\mathcal{T}(x)}(\theta)\right) ≥ 1 K ​ c ​ ( p ⋆ , G , σ min ) > 0 , \displaystyle\geq\frac{1}{K}\,c(p^{\star},G,\sigma_{\min})>0, λ min ​ ( 𝑭 𝒯 ⁡ ( x ) ​ ( θ ) ) λ min ​ ( 𝑭 x ​ ( θ ) ) \displaystyle\frac{\lambda_{\min}(\bm{F}_{\mathcal{T}(x)}(\theta))}{\lambda_{\min}(\bm{F}_{x}(\theta))} = Ω ⁡ ( 1 δ ) , \displaystyle=\Omega\!\left(\frac{1}{\delta}\right), (9) where c ⁡ ( p ⋆ , G , σ min ) = ( 1 − ( p ⋆ ) G − ( 1 − p ⋆ ) G ) ​ σ min 2 c(p^{\star},G,\sigma_{\min})=\bigl(1-(p^{\star})^{G}-(1-p^{\star})^{G}\bigr)\sigma_{\min}^{2} is a positive constant independent of δ \delta .

Theorem 4.3 shows that subproblem curriculum helps hard problems by recovering a non-degenerate learning geometry, even when the original problem provides almost no useful gradient signal. Moreover, the recovery ratio grows as p ⁡ ( x , θ ) → 0 p(x;\theta)\to 0 , predicting larger relative gains on harder problems.

## 5 Experiment

### 5.1 Experimental Setup

##### Models.

To investigate the scalability and effectiveness of our proposed method across different model capacities, we conduct experiments on the Qwen and Llama series. Specifically, we utilize Qwen3-4B-Base , Qwen3-14B-Base and Llama3.2-3B-Instruct as our base policies.

##### Training Setup.

We use the training set hard_1024 , a subset of 1,024 problems randomly selected from the high-difficulty competition mathematics dataset provided by Yang et al. (2026) . For SCRL, subproblems are generated with the DeepSeek-V3.2 API with K = 4 K=4 . All models are trained using the Verl framework Sheng et al. (2025) for a total of 300 steps. Detailed hyperparameter configurations are provided in Appendix F.1 .

##### Benchmark.

We evaluate the models on seven widely used mathematical reasoning benchmarks: OlympiadBench , Minerva , MATH-500 , AIME 2024 , AIME 2025 , AMC , and IMO-Bench .

##### Baseline Settings.

We compare our method against the following competitive baselines: SFT , GRPO Guo et al. (2025) , DAPO Yu et al. (2025) , QuestA Li et al. (2026a) and NuRL Chen et al. (2025) .Implementation details are provided in Appendix F.3 .

### 5.2 Main Results and Further Analysis

The main results across seven mathematical reasoning benchmarks are summarized in Table 1 , with full experimental results provided in Appendix E .

##### Superior Performance Across All Benchmarks.

As shown in Table 1 , SCRL consistently outperforms vanilla GRPO and competitive baselines including DAPO, QuestA, and NuRL across three model scales: Llama3.2-3B, Qwen3-4B, and Qwen3-14B. In terms of average accuracy (Avg), SCRL achieves the best performance in all settings. The gain is especially clear on Qwen3-4B, where SCRL reaches an average score of 35.0% , improving over the second-best baseline QuestA ( 32.0% ) by 3.0 points and over vanilla GRPO ( 30.9% ) by 4.1 points. On challenging benchmarks such as AIME’25, SCRL also shows strong gains, achieving 15.3% compared with QuestA’s 11.7% .

##### Curriculum progress transfers to hard-problem solving.

Figure 4 shows pass@ k k curves on AIME24, AIME25, and IMO-Bench. SCRL consistently outperforms GRPO and other curriculum RL baselines across the entire evaluated range of k k , indicating stronger hard-problem solving ability.

Figure 6 further tracks the ratio of solvable problems during training, where a problem is counted as solvable once it is fully solved at least once. The full group statistic counts success in either the original-problem or curriculum format, while the half group statistic uses only half-budget original-problem rollouts, matching SCRL’s mixed-group setting. SCRL achieves a higher solvable ratio than GRPO under both protocols, showing that curriculum progress transfers back to direct hard-problem solving rather than only improving curriculum-format rollouts.

##### SCRL does not rely on highly curated subproblems.

We further examine whether SCRL depends on high-quality subproblem construction. Table 2 compares subproblems generated by DeepSeek-V3.2 and a weaker Qwen3-4B-Instruct generator, using the same generation prompt and downstream training pipeline. In both cases, the generator is given the dataset reference solution, so it only decomposes an already solved problem rather than solving it from scratch. SCRL remains effective with the weaker generator, improving over GRPO by +2.7 points on average, while DeepSeek-V3.2 further increases the gain to +3.9 points.

Figure 6 shows that even with DeepSeek-V3.2, the ratio of curriculum instances fully solved at k i = 4 k_{i}=4 remains lower than the GRPO solvable ratio (the GRPO bar at k i = 4 k_{i}=4 reports the ratio of original problems solved by GRPO under the same half-group counting protocol). Nevertheless, SCRL still achieves a substantial performance gain. This indicates that SCRL does not require subproblems to be easy or perfectly curated. At the same time, DeepSeek-V3.2 produces a larger k i = 4 k_{i}=4 ratio than Qwen3-4B-Instruct, suggesting that better subproblem quality can further increase SCRL’s gains.

##### Subproblem-level normalization enables better credit assignment.

We further ablate on Qwen3-4B-Base how credit is assigned within curriculum rollouts. Table 3 compares the full method with two alternatives: removing progress-aware correction, and Both-GRPO, which keeps mixed training but verifies only the final subproblem and applies sample-level GRPO to curriculum rollouts.

Subproblem-level normalization with progress-aware correction performs best. Without correction, dense subproblem signals may reward later steps after earlier failures, while Both-GRPO uses subproblems only as hints and cannot credit valid intermediate progress. Thus, effective curriculum training needs both subproblem-specific signals and progress-aware correction.

## 6 Conclusion

We propose SCRL, a subproblem curriculum RL framework for hard LLM reasoning with verifiable rewards. SCRL derives verifiable subproblems from reasoning chains and uses subproblem-level normalization to convert partial rollout progress into token-level learning signals, enabling fine-grained credit assignment without external reward models or process annotations. Our theory shows that subproblem decomposition can lift hard problems out of gradient dead zones, and experiments show consistent gains over strong RLVR and curriculum-learning baselines.

## References

Alam & Rastogi (2025) Alam, M. T. and Rastogi, N. Limits of generalization in rlvr: Two case studies in mathematical reasoning. arXiv preprint arXiv:2510.27044 , 2025.

Amani et al. (2025) Amani, M. H., Lotfi, A., Baldwin, N. M., Bengio, S., Farajtabar, M., Abbe, E., and West, R. Rl for reasoning by adaptively revealing rationales. ArXiv , abs/2506.18110, 2025. URL https://api.semanticscholar.org/CorpusID:280000657 .

Amari (2016) Amari, S.-i. Information Geometry and Its Applications , volume 194 of Applied Mathematical Sciences . Springer Japan, Tokyo, 2016. ISBN 978-4-431-55977-1. doi: 10.1007/978-4-431-55978-8 .

Bengio et al. (2009) Bengio, Y., Louradour, J., Collobert, R., and Weston, J. Curriculum learning. In Proceedings of the 26th annual international conference on machine learning , pp. 41–48, 2009.

Chen et al. (2025) Chen, J. C.-Y., Peng, B. X., Choubey, P. K., Huang, K.-H., Zhang, J., Bansal, M., and Wu, C.-S. Nudging the boundaries of llm reasoning. arXiv preprint arXiv:2509.25666 , 2025.

Chen et al. (2026) Chen, J. C.-Y., Prasad, A., Khan, Z., Singh, J., Tian, R., Stengel-Eskin, E., and Bansal, M. Cog-drift: Exploration on adaptively reformulated instances enables learning from hard reasoning problems. arXiv preprint arXiv:2604.04767 , 2026.

Chen (2021) Chen, M. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374 , 2021.

Chu et al. (2025) Chu, T., Zhai, Y., Yang, J., Tong, S., Xie, S., Schuurmans, D., Le, Q. V., Levine, S., and Ma, Y. Sft memorizes, rl generalizes: A comparative study of foundation model post-training. arXiv preprint arXiv:2501.17161 , 2025.

Dai et al. (2026) Dai, Y., Ji, Y., Zhang, X., Wang, Y., Chu, X., and Lu, Z. Harder is better: Boosting mathematical reasoning via difficulty-aware GRPO and multi-aspect question reformulation. In The Fourteenth International Conference on Learning Representations , 2026. URL https://openreview.net/forum?id=nfURupkdRJ .

Fu et al. (2025) Fu, Y., Chen, T., Chai, J., Wang, X., Tu, S., Yin, G., Lin, W., Zhang, Q., Zhu, Y., and Zhao, D. Srft: A single-stage method with supervised and reinforcement fine-tuning for reasoning. arXiv preprint arXiv:2506.19767 , 2025.

Gulcehre et al. (2023) Gulcehre, C., Paine, T. L., Srinivasan, S., Konyushkova, K., Weerts, L., Sharma, A., Siddhant, A., Ahern, A., Wang, M., Gu, C., et al. Reinforced self-training (rest) for language modeling. arXiv preprint arXiv:2308.08998 , 2023.

Guo et al. (2025) Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X., et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948 , 2025.

Jaech et al. (2024) Jaech, A., Kalai, A., Lerer, A., Richardson, A., El-Kishky, A., Low, A., Helyar, A., Madry, A., Beutel, A., Carney, A., et al. Openai o1 system card. arXiv preprint arXiv:2412.16720 , 2024.

Li et al. (2025a) Li, D., Cao, S., Griggs, T., Liu, S., Mo, X., Tang, E., Hegde, S., Hakhamaneshi, K., Patil, S. G., Zaharia, M., Gonzalez, J. E., and Stoica, I. Llms can easily learn to reason from demonstrations structure, not content, is what matters! ArXiv , abs/2502.07374, 2025a. URL https://api.semanticscholar.org/CorpusID:276258697 .

Li et al. (2026a) Li, J., Lin, H., Lu, H., Wen, K., Yang, Z., Gao, J., Wu, Y., and Zhang, J. Questa: Expanding reasoning capacity in LLMs via question augmentation. In The Fourteenth International Conference on Learning Representations , 2026a. URL https://openreview.net/forum?id=3MifB0f7qR .

Li et al. (2025b) Li, R., Huang, H., Wei, F., Xiong, F., Wang, Y., and Chu, X. Adacurl: Adaptive curriculum reinforcement learning with invalid sample mitigation and historical revisiting. ArXiv , abs/2511.09478, 2025b. URL https://api.semanticscholar.org/CorpusID:282939669 .

Li et al. (2026b) Li, X., Chen, J., Li, X., Liang, H., Zhou, X., Wang, T., and Zhang, W. Mathmixup: Boosting llm mathematical reasoning with difficulty-controllable data synthesis and curriculum learning. arXiv preprint arXiv:2601.17006 , 2026b.

Liang et al. (2025) Liang, X., zhi Li, Z., Gong, Y., Shen, Y., Wu, Y., Guo, Z., and Chen, W. Beyond pass@1: Self-play with variational problem synthesis sustains rlvr. ArXiv , abs/2508.14029, 2025. URL https://api.semanticscholar.org/CorpusID:280686520 .

Lightman et al. (2023) Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and Cobbe, K. Let’s verify step by step. In The twelfth international conference on learning representations , 2023.

Lv et al. (2025) Lv, X., Zuo, Y., Sun, Y., Liu, H., Wei, Y., Chen, Z., Zhu, X., Zhang, K., Wang, B., Ding, N., et al. Towards a unified view of large language model post-training. arXiv preprint arXiv:2509.04419 , 2025.

Ma et al. (2025) Ma, L., Liang, H., Qiang, M., Tang, L., Ma, X., Wong, Z. H., Niu, J., Shen, C., He, R., Cui, B., and Zhang, W. Learning what reinforcement learning can’t: Interleaved online fine-tuning for hardest questions. ArXiv , abs/2506.07527, 2025. URL https://api.semanticscholar.org/CorpusID:279251208 .

Parashar et al. (2025) Parashar, S., Gui, S., Li, X., Ling, H., Vemuri, S., Olson, B., Li, E., Zhang, Y., Caverlee, J., Kalathil, D. M., and Ji, S. Curriculum reinforcement learning from easy to hard tasks improves llm reasoning. ArXiv , abs/2506.06632, 2025. URL https://api.semanticscholar.org/CorpusID:279251658 .

Pikus et al. (2025) Pikus, B., Tiwari, P. R., and Ye, B. Hard examples are all you need: Maximizing grpo post-training under annotation budgets. ArXiv , abs/2508.14094, 2025. URL https://api.semanticscholar.org/CorpusID:280692329 .

Qiyuan et al. (2026) Qiyuan, D., Chen, K., Zhang, M., and Xu, Z. HiPO: Self-hint policy optimization for RLVR. In The Fourteenth International Conference on Learning Representations , 2026. URL https://openreview.net/forum?id=rcb20pHmT1 .

Qu et al. (2025) Qu, Y., Singh, A., Lee, Y., Setlur, A. R., Salakhutdinov, R., Finn, C., and Kumar, A. Rlad: Training llms to discover abstractions for solving reasoning problems. ArXiv , abs/2510.02263, 2025. URL https://api.semanticscholar.org/CorpusID:281724383 .

Qu et al. (2026) Qu, Y., Setlur, A., Smith, V., Salakhutdinov, R., and Kumar, A. Pope: Learning to reason on hard problems via privileged on-policy exploration. arXiv preprint arXiv:2601.18779 , 2026.

Schulman et al. (2017) Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and Klimov, O. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.

Shao et al. (2024) Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y., Wu, Y., et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

Shenfeld et al. (2025) Shenfeld, I., Pari, J., and Agrawal, P. Rl’s razor: Why online reinforcement learning forgets less. ArXiv , abs/2509.04259, 2025. URL https://api.semanticscholar.org/CorpusID:281103647 .

Sheng et al. (2025) Sheng, G., Zhang, C., Ye, Z., Wu, X., Zhang, W., Zhang, R., Peng, Y., Lin, H., and Wu, C. Hybridflow: A flexible and efficient rlhf framework. In EuroSys , pp. 1279–1297, 2025. URL https://doi.org/10.1145/3689031.3696075 .

Shi et al. (2026) Shi, W., Chen, Y., Li, Z., Pan, X., Sun, Y., Xu, J., Zhou, X., and Li, Y. R3l: Reflect-then-retry reinforcement learning with language-guided exploration, pivotal credit, and positive amplification. ArXiv , abs/2601.03715, 2026. URL https://api.semanticscholar.org/CorpusID:284532205 .

Shojaee et al. (2025) Shojaee, P., Mirzadeh, I., Alizadeh, K., Horton, M., Bengio, S., and Farajtabar, M. The illusion of thinking: Understanding the strengths and limitations of reasoning models via the lens of problem complexity. arXiv preprint arXiv:2506.06941 , 2025.

Skalse et al. (2022) Skalse, J. M. V., Howe, N. H. R., Krasheninnikov, D., and Krueger, D. Defining and characterizing reward hacking. ArXiv , abs/2209.13085, 2022. URL https://api.semanticscholar.org/CorpusID:252545256 .

Trinh et al. (2024) Trinh, T. H., Wu, Y., Le, Q. V., He, H., and Luong, T. Solving olympiad geometry without human demonstrations. Nature , 625(7995):476–482, 2024.

Uesato et al. (2022) Uesato, J., Kushman, N., Kumar, R., Song, F., Siegel, N., Wang, L., Creswell, A., Irving, G., and Higgins, I. Solving math word problems with process-and outcome-based feedback. arXiv preprint arXiv:2211.14275 , 2022.

Wang et al. (2025) Wang, S., Yu, L., Gao, C., Zheng, C., Liu, S., Lu, R., Dang, K., Chen, X., Yang, J., Zhang, Z., et al. Beyond the 80/20 rule: High-entropy minority tokens drive effective reinforcement learning for llm reasoning. arXiv preprint arXiv:2506.01939 , 2025.

Wen et al. (2025) Wen, X., Liu, Z., Zheng, S., Xu, Z., Ye, S., Wu, Z., Liang, X., Wang, Y., Li, J., Miao, Z., Bian, J., and Yang, M. Reinforcement learning with verifiable rewards implicitly incentivizes correct reasoning in base llms. ArXiv , abs/2506.14245, 2025. URL https://api.semanticscholar.org/CorpusID:279410727 .

Wu et al. (2025a) Wu, J., Liao, C., Feng, M., Zhang, S., Wen, Z., Shao, P., Xu, H., and Tao, J. Thought-augmented policy optimization: Bridging external guidance and internal capabilities. arXiv preprint arXiv:2505.15692 , 1(8):10, 2025a.

Wu et al. (2025b) Wu, M., Qian, Q., Liu, W., Wang, X., Huang, Z., Liang, D., Miao, L., Dou, S., Lv, C., Wang, Z., Xu, Z., Chen, L., Li, T., Zheng, X., and Huang, X. Progressive mastery: Customized curriculum learning with guided prompting for mathematical reasoning. ArXiv , abs/2506.04065, 2025b. URL https://api.semanticscholar.org/CorpusID:279154725 .

Yan et al. (2025) Yan, J., Li, Y., Hu, Z., Wang, Z., Cui, G., Qu, X., Cheng, Y., and Zhang, Y. Learning to reason under off-policy guidance. In The Thirty-ninth Annual Conference on Neural Information Processing Systems , 2025. URL https://openreview.net/forum?id=vO8LLoNWWk .

Yang et al. (2024) Yang, A., Zhang, B., Hui, B., Gao, B., Yu, B., Li, C., Liu, D., Tu, J., Zhou, J., Lin, J., et al. Qwen2. 5-math technical report: Toward mathematical expert model via self-improvement. arXiv preprint arXiv:2409.12122 , 2024.

Yang et al. (2025) Yang, C., Wu, J., Liu, Y., Zhang, S., Li, Y., Liang, Q., Wang, H., Nie, S., Xu, J., Shi, R., Huang, Y., and Zhang, G. From imitation to discrimination: Toward a generalized curriculum advantage mechanism enhancing cross-domain reasoning tasks. In AAAI Conference on Artificial Intelligence , 2025. URL https://api.semanticscholar.org/CorpusID:283458223 .

Yang et al. (2026) Yang, M. Y., Bai, H., Wu, I., Yang, G., Setlur, A., and Kumar, A. Int: Self-proposed interventions enable credit assignment in llm reasoning. arXiv preprint arXiv:2601.14209 , 2026.

Yu et al. (2025) Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma, B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang, W., Zhu, H., Zhu, J., Chen, J., Chen, J., Wang, C., Yu, H., Dai, W., Song, Y., Wei, X., Zhou, H., Liu, J., Ma, W., Zhang, Y.-Q., Yan, L., Qiao, M., Wu, Y.-X., and Wang, M. Dapo: An open-source llm reinforcement learning system at scale. ArXiv , abs/2503.14476, 2025. URL https://api.semanticscholar.org/CorpusID:277104124 .

Yue et al. (2025) Yue, Y., Chen, Z., Lu, R., Zhao, A., Wang, Z., Song, S., and Huang, G. Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? arXiv preprint arXiv:2504.13837 , 2025.

Zelikman et al. (2022) Zelikman, E., Wu, Y., and Goodman, N. D. Star: Self-taught reasoner. arXiv preprint arXiv:2203.14465 , 2022.

Zhang et al. (2024) Zhang, D., Zhoubian, S., Hu, Z., Yue, Y., Dong, Y., and Tang, J. Rest-mcts*: Llm self-training via process reward guided tree search. Advances in Neural Information Processing Systems , 37:64735–64772, 2024.

Zhang et al. (2025a) Zhang, K., Lv, A., Li, J., Wang, Y., Wang, F., Hu, H., and Yan, R. Stephint: Multi-level stepwise hints enhance reinforcement learning to reason. arXiv preprint arXiv:2507.02841 , 2025a.

Zhang et al. (2025b) Zhang, X., Wu, S., Zhu, Y., Tan, H., Yu, S., He, Z., and Jia, J. Scaf-grpo: Scaffolded group relative policy optimization for enhancing llm reasoning. arXiv preprint arXiv:2510.19807 , 2025b.

## Appendix A More Ablation Study

##### Number of subproblems.

We first ablate the number of subproblems K K . Our main setting uses K = 4 K=4 , with the final subproblem fixed as the original problem. For K = 3 K=3 and K = 2 K=2 , we take the last three or last two subproblems from the K = 4 K=4 sequence, so the shorter curricula preserve the nested structure and still end with the original problem.

Table 4 shows that increasing K K improves the average performance, with K = 4 K=4 performing best. This supports the role of subproblem curricula: more subproblems expose a finer progression toward the original problem, creating more verifiable intermediate signals within each rollout. Figure 7 explains why longer subproblem curricula help. As K K increases, fewer rollouts make zero progress, meaning more rollouts solve at least one subproblem and receive a non-empty learning signal. Thus, increasing K K improves both the granularity of credit assignment and the availability of reward signal on hard problems.

However, longer curricula also increase rollout complexity. The model must answer more subproblems, and progress-aware correction requires earlier subproblems to be solved before later ones can receive credit. If an intermediate subproblem is ambiguous or poorly constructed, it can block credit for later progress. We therefore use K = 4 K=4 as a practical trade-off between denser supervision and curriculum complexity.

##### Training data construction.

Each SCRL curriculum rollout contains K = 4 K=4 subproblems, so we ask whether the gain comes from the training algorithm or simply from exposing the model to more questions. We compare the default setting, hard_1024 with SCRL, against two data-scaling controls. hard_4096 expands the original-problem set by adding 3 × 1024 3\times 1024 hard problems from the InT dataset ( Yang et al., 2026 ) . subproblem_4096 instead splits each four-subproblem curriculum instance into four standalone questions; since the last subproblem is the original problem, it also contains hard_1024 .

Table 5 shows that SCRL outperforms both data-scaling controls. This suggests that the gain does not mainly come from seeing more questions, but from using subproblems as a curriculum inside each rollout. Subproblems serve as intermediate anchors: after solving an earlier subproblem, the model can build on that result when solving later ones, while subproblem-level normalization assigns credit to the corresponding answer spans. The average response length is computed over the first 20 training epochs. Although each SCRL curriculum rollout contains four subproblems, its average response length is only about 1.5 × 1.5\times that of GRPO on hard_1024 . This indicates that SCRL does not spend response length proportional to the number of subproblems, but instead uses the subproblem curriculum structure to support more efficient exploration.

The two controls further clarify this point. hard_4096 improves over hard_1024 , but the gain is limited, showing that simply adding more hard problems is less effective under our training budget. subproblem_4096 brings a slightly larger gain, but still falls behind SCRL, suggesting that training on isolated easier subproblems does not by itself teach the model to solve harder target problems. In contrast, SCRL keeps the model exploring near its current capability boundary by preserving the dependency among subproblems, making the curriculum more useful than either data scaling strategy.

## Appendix B Proofs for Section 4

### B.1 Proof of Theorem 4.2 (Bound on λ min ​ ( 𝑭 x ​ ( θ ) ) \lambda_{\min}(\bm{F}_{x}(\theta)) )

We bound λ min ​ ( 𝑭 x ​ ( θ ) ) \lambda_{\min}(\bm{F}_{x}(\theta)) when p ⁡ ( x , θ ) < δ p(x;\theta)<\delta .

Let E 0 E_{0} denote the event that all G G rollouts share the same reward (either all fail or all succeed). On E 0 E_{0} , the group is degenerate ( σ ^ r x = 0 \hat{\sigma}_{r_{x}}=0 ), so by the GRPO convention A ^ i = 0 \hat{A}_{i}=0 for all i i , and every term in ( 6 ) is zero. By the law of total expectation: 𝑭 x ​ ( θ ) = Pr ⁡ [ E 0 c ] ⋅ 𝔼 ⁡ [ 1 G ​ ∑ i A ^ i 2 ​ s i ​ s i ⊤ | E 0 c ] , \bm{F}_{x}(\theta)\;=\;\Pr[E_{0}^{c}]\cdot\mathbb{E}\!\left[\frac{1}{G}\sum_{i}\hat{A}_{i}^{2}s_{i}s_{i}^{\top}\,\Big|\,E_{0}^{c}\right], (10) where s i = ∇ θ ​ log ​ π θ ​ ( o i ∣ x ) s_{i}=\nabla_{\theta}\log\pi_{\theta}(o_{i}\mid x) . For any unit vector v v , using A ^ i 2 ≤ C A ^ 2 \hat{A}_{i}^{2}\leq C_{\hat{A}}^{2} a.s. and ( v ⊤ ​ s i ) 2 ≤ B s 2 (v^{\top}s_{i})^{2}\leq B_{s}^{2} a.s. (by regularity): v ⊤ ​ 𝑭 x ​ ( θ ) ​ v ≤ Pr ⁡ [ E 0 c ] ⋅ C A ^ 2 ⋅ B s 2 . v^{\top}\bm{F}_{x}(\theta)\,v\;\leq\;\Pr[E_{0}^{c}]\cdot C_{\hat{A}}^{2}\cdot B_{s}^{2}. (11) Since Pr ⁡ [ E 0 c ] = 1 − p G − ( 1 − p ) G ≤ 1 − ( 1 − p ) G ≤ 1 − ( 1 − δ ) G ≤ G ​ δ \Pr[E_{0}^{c}]=1-p^{G}-(1-p)^{G}\leq 1-(1-p)^{G}\leq 1-(1-\delta)^{G}\leq G\delta (using p < δ p<\delta and Bernoulli’s inequality): λ min ​ ( 𝑭 x ​ ( θ ) ) ≤ sup ‖ v ‖ = 1 v ⊤ ​ 𝑭 x ​ v ≤ G ​ δ ⋅ C A ^ 2 ⋅ B s 2 = O ⁡ ( δ ) . \lambda_{\min}\!\left(\bm{F}_{x}(\theta)\right)\;\leq\;\sup_{\|v\|=1}v^{\top}\bm{F}_{x}v\;\leq\;G\delta\cdot C_{\hat{A}}^{2}\cdot B_{s}^{2}\;=\;O(\delta). (12) This establishes Theorem 4.2 .∎

### B.2 Proof of Theorem 4.3

##### First claim.

We bound the column- 1 1 contribution to 𝑭 𝒯 ⁡ ( x ) ​ ( θ ) \bm{F}_{\mathcal{T}(x)}(\theta) . Let E 1 ≠ E_{1}^{\neq} denote the event that column 1 is non-degenerate.

Lower bound on Pr ⁡ [ E 1 ≠ ] \Pr[E_{1}^{\neq}] . Since p 1 ∈ [ p ⋆ , 1 − p ⋆ ] p_{1}\in[p^{\star},1-p^{\star}] by assumption, and g ⁡ ( p ) = 1 − p G − ( 1 − p ) G g(p)=1-p^{G}-(1-p)^{G} is symmetric around 1 / 2 1/2 and non-decreasing on [ 0 , 1 / 2 ] [0,1/2] , its minimum on [ p ⋆ , 1 − p ⋆ ] [p^{\star},1-p^{\star}] is attained at the endpoints: Pr ⁡ [ E 1 ≠ ] = g ⁡ ( p 1 ) ≥ g ⁡ ( p ⋆ ) = 1 − ( p ⋆ ) G − ( 1 − p ⋆ ) G = : q min > 0 . \Pr[E_{1}^{\neq}]\;=\;g(p_{1})\;\geq\;g(p^{\star})\;=\;1-(p^{\star})^{G}-(1-p^{\star})^{G}\;=:\;q_{\min}\;>\;0. (13)

Lower bound on the conditional EGIM. We compute v ⊤ ​ 𝑭 𝒯 ⁡ ( x ) ( 1 ) ​ v v^{\top}\bm{F}^{(1)}_{\mathcal{T}(x)}v by conditioning on the reward vector ( R 1 ( 1 ) , … , R G ( 1 ) ) (R_{1}^{(1)},\ldots,R_{G}^{(1)}) . Given the rewards, A ^ i ( 1 ) \hat{A}_{i}^{(1)} is fully determined, and since rollouts are i.i.d., o i ( 1 ) o_{i}^{(1)} is conditionally independent of ( R j ( 1 ) ) j ≠ i (R_{j}^{(1)})_{j\neq i} given R i ( 1 ) R_{i}^{(1)} , so 𝔼 ⁡ [ ( v ⊤ ​ s i ( 1 ) ) 2 ∣ ( R 1 ( 1 ) , … , R G ( 1 ) ) ] = 𝔼 ⁡ [ ( v ⊤ ​ s i ( 1 ) ) 2 ∣ R i ( 1 ) ] \mathbb{E}[(v^{\top}s_{i}^{(1)})^{2}\mid(R_{1}^{(1)},\ldots,R_{G}^{(1)})]=\mathbb{E}[(v^{\top}s_{i}^{(1)})^{2}\mid R_{i}^{(1)}] . By the tower property: v ⊤ ​ 𝑭 𝒯 ⁡ ( x ) ( 1 ) ​ v \displaystyle v^{\top}\bm{F}^{(1)}_{\mathcal{T}(x)}v = 1 G ​ ∑ i = 1 G 𝔼 ⁡ [ A ^ i ( 1 ) ​ 2 ​ 𝔼 ​ [ ( v ⊤ ​ s i ( 1 ) ) 2 ∣ R i ( 1 ) ] ] \displaystyle\;=\;\frac{1}{G}\sum_{i=1}^{G}\mathbb{E}\!\left[\hat{A}_{i}^{(1)2}\,\mathbb{E}\!\left[(v^{\top}s_{i}^{(1)})^{2}\mid R_{i}^{(1)}\right]\right] ≥ σ min 2 ⋅ 1 G ∑ i = 1 G 𝔼 [ A ^ i ( 1 ) ​ 2 ] , \displaystyle\;\geq\;\sigma_{\min}^{2}\cdot\frac{1}{G}\sum_{i=1}^{G}\mathbb{E}\!\left[\hat{A}_{i}^{(1)2}\right], (14) where the inequality uses the conditional identifiability assumption ( 𝔼 ⁡ [ ( v ⊤ ​ s ) 2 ∣ r = r i ( 1 ) ] ≥ σ min 2 \mathbb{E}[(v^{\top}s)^{2}\mid r=r_{i}^{(1)}]\geq\sigma_{\min}^{2} for all r i ( 1 ) ∈ { 0 , 1 } r_{i}^{(1)}\in\{0,1\} ) and A ^ i ( 1 ) ​ 2 ≥ 0 \hat{A}_{i}^{(1)2}\geq 0 . By definition of σ ^ r \hat{\sigma}_{r} , the sample average of squared advantages satisfies 1 G ∑ i = 1 G A ^ i ( 1 ) ​ 2 = 1 on E 1 ≠ and = 0 otherwise, \frac{1}{G}\sum_{i=1}^{G}\hat{A}_{i}^{(1)2}\;=\;1\quad\text{on }E_{1}^{\neq}\quad\text{and}\quad=0\text{ otherwise,} (15) so 1 G ​ ∑ i 𝔼 ⁡ [ A ^ i ( 1 ) ​ 2 ] = Pr ⁡ [ E 1 ≠ ] ≥ q min \frac{1}{G}\sum_{i}\mathbb{E}[\hat{A}_{i}^{(1)2}]=\Pr[E_{1}^{\neq}]\geq q_{\min} . Hence:

Conclusion: Substituting into ( 14 ): v ⊤ ​ 𝑭 𝒯 ⁡ ( x ) ( 1 ) ​ v ≥ σ min 2 ⋅ Pr ⁡ [ E 1 ≠ ] ≥ q min ⋅ σ min 2 . v^{\top}\bm{F}^{(1)}_{\mathcal{T}(x)}\,v\;\geq\;\sigma_{\min}^{2}\cdot\Pr[E_{1}^{\neq}]\;\geq\;q_{\min}\cdot\sigma_{\min}^{2}. (16) Since all terms in ( 7 ) are PSD, 𝑭 𝒯 ⁡ ( x ) ⪰ 1 K ​ 𝑭 𝒯 ⁡ ( x ) ( 1 ) \bm{F}_{\mathcal{T}(x)}\succeq\tfrac{1}{K}\bm{F}^{(1)}_{\mathcal{T}(x)} , hence: λ min ​ ( 𝑭 𝒯 ⁡ ( x ) ​ ( θ ) ) ≥ 1 K ⋅ q min ⋅ σ min 2 = : 1 K ⋅ c ⁡ ( p ⋆ , G , σ min ) > 0 . \lambda_{\min}\!\left(\bm{F}_{\mathcal{T}(x)}(\theta)\right)\;\geq\;\tfrac{1}{K}\cdot q_{\min}\cdot\sigma_{\min}^{2}\;=:\tfrac{1}{K}\cdot c(p^{\star},G,\sigma_{\min})\;>\;0. (17)

##### Second claim.

Combining ( 12 ) and ( 17 ): λ min ​ ( 𝑭 𝒯 ⁡ ( x ) ​ ( θ ) ) λ min ​ ( 𝑭 x ​ ( θ ) ) ≥ 1 K ⋅ c ⁡ ( p ⋆ , G , σ min ) G ​ δ ⋅ C A ^ 2 ⋅ B s 2 = Ω ⁡ ( 1 δ ) , \frac{\lambda_{\min}(\bm{F}_{\mathcal{T}(x)}(\theta))}{\lambda_{\min}(\bm{F}_{x}(\theta))}\;\geq\;\frac{\tfrac{1}{K}\cdot c(p^{\star},G,\sigma_{\min})}{G\delta\cdot C_{\hat{A}}^{2}\cdot B_{s}^{2}}\;=\;\Omega\!\left(\frac{1}{\delta}\right), (18) since the numerator is independent of δ \delta .∎

### B.3 Bound on C A ^ C_{\hat{A}}

We show that for binary rewards r i ∈ { 0 , 1 } r_{i}\in\{0,1\} , the group-normalized GRPO advantage satisfies C A ^ := sup i | A ^ i | ≤ G − 1 C_{\hat{A}}:=\sup_{i}|\hat{A}_{i}|\leq\sqrt{G-1} . For a non-degenerate group with k k successes ( 1 ≤ k ≤ G − 1 1\leq k\leq G-1 ), r ¯ = k / G \bar{r}=k/G and σ ^ r = ( k / G ) ​ ( 1 − k / G ) \hat{\sigma}_{r}=\sqrt{(k/G)(1-k/G)} . The advantage of a success rollout is: | A ^ success | = 1 − k / G ( k / G ) ​ ( 1 − k / G ) = 1 − k / G k / G = G − k k , |\hat{A}_{\text{success}}|\;=\;\frac{1-k/G}{\sqrt{(k/G)(1-k/G)}}\;=\;\sqrt{\frac{1-k/G}{k/G}}\;=\;\sqrt{\frac{G-k}{k}}, (19) which is maximized at k = 1 k=1 , giving | A ^ | = G − 1 |\hat{A}|=\sqrt{G-1} . By symmetry, the advantage of a failure rollout is k / ( G − k ) \sqrt{k/(G-k)} , also maximized at k = G − 1 k=G-1 , giving G − 1 \sqrt{G-1} . Hence C A ^ = G − 1 < G C_{\hat{A}}=\sqrt{G-1}<\sqrt{G} .∎

## Appendix C SCRL Training Algorithm

## Appendix D OOD Task Performance

##### SCRL generalizes to out-of-distribution tasks.

To examine whether the gains from SCRL transfer beyond the mathematical benchmarks used for training, we evaluate the Qwen3-14B-Base model on three out-of-distribution benchmarks: GPQA, HumanEval, and LiveCodeBench v6. These benchmarks cover different reasoning domains, including scientific question answering and code generation, and are not used for constructing the subproblem curriculum.

As shown in Table 6 , SCRL achieves the best average OOD score, reaching 51.67 compared with 47.20 for the base model and 48.37 for GRPO. SCRL also improves consistently across all three OOD benchmarks, with gains on GPQA (41.41 vs. 38.89 for the base model and 36.86 for GRPO), HumanEval (89.02 vs. 82.93 and 84.15), and LiveCodeBench v6 (24.57 vs. 19.80 and 24.10). These results suggest that SCRL does not merely overfit to the generated curriculum prompts or the training benchmark distribution. Instead, the subproblem curriculum appears to improve transferable reasoning behavior, including domains where solutions require multi-step reasoning or program synthesis rather than the exact mathematical format used during training.

## Appendix E Detailed Experimental Results

Here we provide the complete Pass@ k k performance ( k ∈ { 1 , 2 , 4 , 8 , 16 , 32 , 64 } k\in\{1,2,4,8,16,32,64\} ) for Qwen3-4B-Base.

## Appendix F Implementation Details

### F.1 Hyperparameters

We provide the detailed hyperparameter configurations used in our experiments in Table 8 . All models are trained using the Verl Sheng et al. (2025) framework with the settings specified below.

### F.2 Low-Variance pass@ k k Estimation

We follow the unbiased pass@ k k estimator of Chen (2021) . For each problem x i ∈ 𝒟 x_{i}\in\mathcal{D} , we generate n n sampled rollouts and let c i c_{i} be the number of correct responses. The estimator is pass ​ @ ​ k := 𝔼 x i ∼ 𝒟 ​ [ 1 − ( n − c i k ) ( n k ) ] . \mathrm{pass}@k:=\mathbb{E}_{x_{i}\sim\mathcal{D}}\left[1-\frac{\binom{n-c_{i}}{k}}{\binom{n}{k}}\right]. (20) For evaluation, we select the checkpoint with the best average validation score for each baseline. Using the selected checkpoint, we generate n = 64 n=64 rollouts for each test problem and compute pass@ k k with the estimator above. This protocol is used consistently for all methods and all reported pass@ k k values.

### F.3 Baseline Implementation Details

##### SFT.

We perform Supervised Fine-Tuning (SFT) on the training set using reasoning trajectories synthesized via the DeepSeek V3.2 API. Specifically, we leverage the API to elicit detailed Chain-of-Thought (CoT) reasoning paths for all training samples. The models are fine-tuned on these synthesized trajectories to establish a strong supervised baseline.

##### GRPO.

We utilize the standard implementation of Group Relative Policy Optimization Guo et al. (2025) without any additional reward shaping or gradient modification terms.

##### DAPO.

An RL algorithm featuring decoupled clipping and dynamic sampling mechanisms. We set the clip_ratio_high=0.28 and max_num_gen_batches=10 for filter groups.

##### QuestA.

A curriculum-based reinforcement learning baseline using question augmentation Li et al. (2026a) . We divide the training process into two 150-step phases: (1) an initial phase where the model is provided with a "partial-50" hint (50% of the solution), followed by (2) a second phase where the hint is reduced to "partial-25" (25% of the solution).

##### NuRL.

NuRL ( Chen et al., 2025 ) uses self-generated hints as abstract cues to reduce problem difficulty during RL. Following its offline hint collection setting, we first run 150 steps of GRPO in Stage 1, then use the DeepSeek-V3.2 API to construct a filtered dataset with abstract cues and train NuRL for another 150 steps in Stage 2.

## Appendix G Limitations and Future Work

SCRL has two main limitations. First, subproblem construction relies on an external LLM, which introduces additional preprocessing cost and makes the quality of the curriculum partly dependent on the generator. Second, SCRL is still based on RLVR and therefore requires verifiable answers for subproblems, making it less directly applicable to open-ended tasks without reliable automatic verifiers.

Future work may proceed in two directions. One direction is to extend SCRL’s credit-assignment mechanism to broader multi-turn agent settings, where tasks often naturally contain subgoal-like intermediate progress. Another direction is to design better subproblems, including more fine-grained, robust, and automatically validated curriculum construction methods.

## Appendix H Hardware Setup

All experiments in this work are conducted on three types of NVIDIA GPUs: NVIDIA GeForce RTX 5090, NVIDIA A100-PCIE-40GB, and NVIDIA H20-PCIE-96GB.

## Appendix I Prompt for Subproblem Generation

## Appendix J Chat Template

### J.1 Chat Template of Curriculum Learning

### J.2 Chat Template of Original Problem

## Appendix K Case Study

We present detailed comparisons between the baseline GRPO and our method.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
