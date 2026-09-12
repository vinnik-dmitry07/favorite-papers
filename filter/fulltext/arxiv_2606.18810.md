##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards

###### Abstract

Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in training LLMs for reasoning tasks, but representative methods such as GRPO assign uniform credit across all tokens, wasting gradient on routine tokens while under-crediting pivotal reasoning steps. Existing token-level credit assignment methods require resources beyond the model’s own rollouts. GRPO variants rely on process reward models or ground-truth answers. Knowledge distillation assigns credit through per-token divergence but requires external teachers (On-Policy Distillation) or privileged information (On-Policy Self Distillation). However, these dependencies limit applicability in the pure RLVR setting. We observe that conditioning the model on its own verified trajectories induces a measurable per-token KL divergence between the original and conditioned distributions, and prove that distilling from a self-teacher constructed by verified trajectories leads to infeasible weighted-average solutions when multiple verified trajectories exist. We propose SC-GRPO ( S elf- C onditioned GRPO), which uses KL divergence mentioned before as a multiplicative weight on GRPO gradients. Across five benchmarks spanning math, code, and agentic tasks, SC-GRPO consistently outperforms 8.1% over GRPO and 5.9% over DAPO with stronger OOD performance. Moreover, SC-GRPO achieves higher performance than OPD.

## 1 Introduction

Large language models (LLMs) have shown strong capabilities in various tasks, but competition-level problems remain challenging. Reinforcement learning with verifiable rewards (RLVR) ( Guo et al., 2025 ; Yu et al., 2026 ; He et al., 2026a ) has driven substantial progress in tackling such problems. Representative methods in RLVR including GRPO Guo et al. (2025) ; Liu et al. () ; Zheng et al. (2025) ; Wang et al. (2025c) assign a single scalar reward per rollout, so every token shares the same advantage. This uniform credit cannot identify which tokens caused success or failure, diluting gradient across routine tokens while under-crediting pivotal reasoning steps ( He et al., 2026b ; Xie et al., 2025 ) .

To enable token-level credit assignment, existing approaches require resources beyond the model’s own rollouts (Figure 1 , top). Recent GRPO variants have explored different directions: some train process reward models on step-level annotations ( Wang et al., 2024b ; Cui et al., 2025 ) , while others rely on ground-truth answers ( Wang et al., 2025b ) . Alternatively, knowledge distillation directly assigns credit at the token level through per-position divergence between student and teacher distributions Hinton et al. (2015) . On-Policy Distillation (OPD) ( Agarwal et al., 2024 ; Ko et al., 2024 ) uses a stronger external teacher to provide token-level supervision, and On-Policy Self-Distillation (OPSD) ( Hübotter et al., 2026 ; Zhao et al., 2026 ) similarly requires privileged information. These dependencies limit applicability in the pure RLVR setting, where only a binary verifier is available.

However, we can identify which tokens carry credit by comparing predictions with and without access to the model’s own verified solution. Recent work has shown that conditioning models on their own verified trajectories improves generation quality ( Yao et al., 2026 ) . Building on this observation, we propose SC-GRPO ( S elf- C onditioned GRPO), which uses such conditioning to induce a measurable per-token distributional shift as a credit assignment signal. As shown in Figure 1 bottom, for problems where the model produces both correct and incorrect rollouts, SC-GRPO injects one verified correct solution as an in-context demonstration and re-scores all remaining rollouts under this prompt, constructing a self-conditioned teacher. A complete version of this example is provided in Figure 10 .

We quantify this shift via per-token Kullback–Leibler (KL) divergence between the original and demonstration-conditioned next-token distributions. Inspired by OPSD ( Zhao et al., 2026 ) , a natural approach would be to add this KL as an auxiliary distillation loss. However, when multiple distinct verified trajectories exist, the loss-minimizing student converges to a weighted average over these teachers, a distribution that does correspond to any feasible trajectory (we formalize this in § 4.2 ). Empirically, such additive formulations consistently fail to improve over GRPO (§ 7.1 ).

Instead, SC-GRPO uses the KL signal purely as a multiplicative weight on the GRPO gradient: the reward determines the update direction, and the KL determines only its intensity at each token. The same self-conditioned teacher handles both partial-solve groups, where a verified correct trajectory serves as the reference and the KL weight sharpens credit assignment, and solve-none groups, where a random rollout serves as the reference and the KL signal provides a slight exploration bonus that encourages diversity. On five benchmarks spanning math, code, and multi-turn agentic tasks, SC-GRPO improves Average@8 by 8.1% over GRPO and 5.9% over DAPO, while achieving more consistent and higher performance than OPD with external teachers.

Our contributions are as follows: • In RLVR, verified trajectories are the only supervision beyond the binary verifier. We prove that distilling from a teacher constructed using these trajectories leads to infeasible solutions, and demonstrate empirically that such formulations fail to improve over GRPO.

• We propose SC-GRPO, which constructs a teacher by conditioning the model on its own verified trajectories and uses the resulting token-level KL divergence as a multiplicative weight on GRPO gradients.

• Across five benchmarks spanning math, code, and agentic tasks, SC-GRPO consistently outperforms RL baselines and achieves higher and more stable performance than OPD.

## 2 Related Work

### 2.1 On-Policy Distillation

On-policy distillation trains on student generated rollouts with a divergence to the teacher distribution ( Agarwal et al., 2024 ; Gu et al., 2024 ; Ko et al., 2024 ; Shing et al., ) , eliminating the train-test mismatch of offline distillation ( Hinton et al., 2015 ) . The divergence objective has been refined through skew-KL ( Ko et al., 2024 ) , α \alpha - β \beta -divergence ( Wang et al., 2025a ) , and adaptive interpolation ( Shing et al., ) , highlighting the sensitivity of letting divergence set the gradient direction. Moreover, all variants require a stronger external teacher.

Self-distillation removes the external teacher dependency by constructing a teacher from the model itself, typically conditioned on privileged information such as textual feedback ( Hübotter et al., 2026 ) , ground truth ( Zhao et al., 2026 ; Ding, 2026 ; Yang et al., 2026 ) , or expert demonstrations ( Shenfeld et al., 2026 ) . SC-GRPO uses KL as a per-token weight, eliminating sensitivity to divergence form choice, and conditions the teacher solely on the model’s own verified rollouts.

### 2.2 Token-Level Credit Assignment in RL

Process reward models (PRMs) ( Lightman et al., 2023 ; Wang et al., 2024b ; Wang et al., 2024a ) provide step-level supervision but require training a separate reward model with large-scale annotation, and remain vulnerable to reward hacking ( Juneja et al., 2025 ; Gao et al., 2024 ) . Annotation-free alternatives estimate token values through Monte Carlo sampling ( Guan et al., ) or segment-level sampling ( Guo et al., 2026 ) , requiring additional rollout compute. GRPO-based methods also need external PRM models Cui et al. (2025) or ground truth Wang et al. (2025b) to gain token-level credit during training. In contrast, SC-GRPO only depends on the model’s own rollouts to obtain token-level reward without external resources.

## 3 Preliminaries

#### Notation

Let π θ \pi_{\theta} denote the policy parameterized by θ \theta . Given a query x x sampled from the training dataset 𝒟 \mathcal{D} , the policy generates a response o = ( o 1 , … , o | o | ) ∼ π θ ( ⋅ ∣ x ) o=(o_{1},\ldots,o_{|o|})\sim\pi_{\theta}(\cdot\mid x) , where o t o_{t} is the token at position t t and o < t o_{<t} denotes the prefix before position t t . Each response is evaluated by a verifier r r , yielding a scalar reward r ⁡ ( x , o ) ∈ [ 0 , 1 ] r(x,o)\in[0,1] .

### 3.1 GRPO

For each query x x , GRPO samples a group of G G responses { o i } i = 1 G \{o_{i}\}_{i=1}^{G} from the old policy π θ old \pi_{\theta_{\mathrm{old}}} . Each response is evaluated by the verifier, yielding r i = r ⁡ ( x , o i ) r_{i}=r(x,o_{i}) . Instead of learning a value function, GRPO normalizes rewards across the G G responses in the same group to obtain a sequence-level advantage. Equivalently, every token position t t in response o i o_{i} shares the same advantage: A ^ i , t = A ^ i = r ⁡ ( x , o i ) − mean ⁡ ( { r ⁡ ( x , o k ) } k = 1 G ) std ⁡ ( { r ⁡ ( x , o k ) } k = 1 G ) . \hat{A}_{i,t}=\hat{A}_{i}=\frac{r(x,o_{i})-\mathrm{mean}(\{r(x,o_{k})\}_{k=1}^{G})}{\mathrm{std}(\{r(x,o_{k})\}_{k=1}^{G})}. (1) The policy is then updated with following objective over response tokens:

𝒥 GRPO ( θ ) = 𝔼 x ∼ 𝒟 , { o i } i = 1 G ∼ π θ old ( ⋅ ∣ x ) [ 1 G ∑ i = 1 G 1 | o i | \displaystyle\mathcal{J}_{\mathrm{GRPO}}(\theta)=\mathbb{E}_{x\sim\mathcal{D},\,\{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid x)}\Bigg[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|} ∑ t = 1 | o i | min ( ρ i , t A ^ i , t , clip ( ρ i , t , 1 − ϵ , 1 + ϵ ) A ^ i , t ) ] , \displaystyle\sum_{t=1}^{|o_{i}|}\min\!\bigl(\rho_{i,t}\hat{A}_{i,t},\,\mathrm{clip}(\rho_{i,t},1-\epsilon,1+\epsilon)\hat{A}_{i,t}\bigr)\Bigg], with ρ i , t = π θ ​ ( o i , t ∣ x , o i , < t ) π θ old ​ ( o i , t ∣ x , o i , < t ) . \displaystyle\mathrm{with}\quad\rho_{i,t}=\frac{\pi_{\theta}(o_{i,t}\mid x,o_{i,<t})}{\pi_{\theta_{\mathrm{old}}}(o_{i,t}\mid x,o_{i,<t})}.

### 3.2 On-Policy Distillation

OPD Agarwal et al. (2024) provides dense token-level signal along the student’s own trajectories.

Let π θ \pi_{\theta} and π T \pi_{T} denote the student and frozen teacher policies, respectively. Given a prompt x ∼ 𝒟 x\sim\mathcal{D} , the student samples a response o ∼ π θ ( ⋅ ∣ x ) o\sim\pi_{\theta}(\cdot\mid x) , which induces prefix states s t = ( x , o < t ) s_{t}=(x,o_{<t}) . At each prefix, the student and teacher next-token distributions are π θ ( ⋅ ∣ s t ) \pi_{\theta}(\cdot\mid s_{t}) and π T ( ⋅ ∣ s t ) \pi_{T}(\cdot\mid s_{t}) , and the token-level OPD objective is ℒ OPD ​ ( θ ) \displaystyle\mathcal{L}_{\mathrm{OPD}}(\theta) = 𝔼 x ∼ 𝒟 , o ∼ π θ ( ⋅ ∣ x ) [ 1 | o | ∑ t = 1 | o | \displaystyle=\mathbb{E}_{\,x\sim\mathcal{D},\;o\sim\pi_{\theta}(\cdot\mid x)}\Big[\frac{1}{|o|}\sum_{t=1}^{|o|} (2) D ( π T ( ⋅ ∣ s t ) ∥ π θ ( ⋅ ∣ s t ) ) ] , \displaystyle D\!\bigl(\pi_{T}(\cdot\mid s_{t})\,\|\,\pi_{\theta}(\cdot\mid s_{t})\bigr)\Big], where D D is a divergence such as the Kullback–Leibler (KL) divergence or the Jensen–Shannon divergence (JSD).

OPSD Ding (2026) ; Hübotter et al. (2026) ; Zhao et al. (2026) removes the requirement of external teacher by conditioning the same model on privileged information c c (e.g., ground-truth or expert demonstration). The student distribution remains π θ ( ⋅ ∣ s t ) \pi_{\theta}(\cdot\mid s_{t}) , while the self-teacher is instantiated as: π ~ θ ( ⋅ ∣ s t , c ) := sg [ π θ ( ⋅ ∣ x , c , o < t ) ] , \widetilde{\pi}_{\theta}(\cdot\mid s_{t},c)\;:=\;\operatorname{sg}\!\left[\pi_{\theta}(\cdot\mid x,c,o_{<t})\right], (3) where sg ⁡ [ ⋅ ] \operatorname{sg}[\cdot] denotes the stop-gradient operator, indicating that the teacher distribution is treated as a fixed target for the current update. The training objective keeps the same form as Eq. ( 2 ), with π T ( ⋅ ∣ s t ) \pi_{T}(\cdot\mid s_{t}) replaced by π ~ θ ( ⋅ ∣ s t , c ) \widetilde{\pi}_{\theta}(\cdot\mid s_{t},c) .

## 4 Why Self-Distillation Fails in RLVR

### 4.1 Available Supervision in RLVR

For a query x x , GRPO samples a group of responses { o i } i = 1 G ∼ π θ old ( ⋅ ∣ x ) \{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid x) , and a verifier assigns a sequence-level reward r i = r ⁡ ( x , o i ) ∈ { 0 , 1 } r_{i}=r(x,o_{i})\in\{0,1\} to each response. Let 𝒞 ( x ) = { o i : r ( x , o i ) = 1 , i ∈ { 1 , … , G } } \mathcal{C}(x)=\{\,o_{i}:r(x,o_{i})=1,\ i\in\{1,\dots,G\}\,\} denote the set of verifier-approved trajectories.

In conventional self-distillation mentioned before, the teacher is conditioned on some form of privileged information. In the RLVR setting, however, no such privileged information is available. Beyond the query x x and the scalar reward r r , the only additional information we can access is a verifier-approved trajectory drawn from the model’s own rollouts, i.e., a sample from 𝒞 ⁡ ( x ) \mathcal{C}(x) . A verified trajectory is not privileged information. It certifies only end-task correctness, not reasoning quality. The trajectory may contain exploratory steps, redundant derivations, or recoverable mistakes, and when multiple trajectories in 𝒞 ⁡ ( x ) \mathcal{C}(x) succeed, they may follow contradictory reasoning paths.

### 4.2 Why OPSD Fails in RLVR

Despite this limitation, verified trajectories are the only additional structure available in RLVR. A natural but naive adaptation is therefore to treat them as a substitute for privileged context. Concretely, for a student rollout o i o_{i} with prefix states s i , t = ( x , o i , < t ) s_{i,t}=(x,o_{i,<t}) and a verifier-approved trajectory τ j ∈ 𝒞 ⁡ ( x ) \tau_{j}\in\mathcal{C}(x) , we instantiate the generic OPSD formulation in Section 3 by taking τ j \tau_{j} as the privileged context: π ~ θ ( ⋅ ∣ s i , t , τ j ) := sg [ π θ ( ⋅ ∣ x , τ j , o i , < t ) ] . \widetilde{\pi}_{\theta}(\cdot\mid s_{i,t},\,\tau_{j})\;:=\;\operatorname{sg}\!\left[\pi_{\theta}(\cdot\mid x,\,\tau_{j},\,o_{i,<t})\right]. (4) The training objective keeps the same form as Eq. ( 2 ), replacing the external teacher π T \pi_{T} with the self-conditioned teacher π ~ θ ( ⋅ ∣ s i , t , τ j ) \widetilde{\pi}_{\theta}(\cdot\mid s_{i,t},\,\tau_{j}) .

This adaptation, however, does not work. A pointwise analysis (detailed in Appendix A ) shows that under both forward and reverse KL, the loss-minimizing student distribution at any prefix s i , t s_{i,t} is a aggregate of the self-conditioned teachers { p j } \{p_{j}\} across 𝒞 ⁡ ( x ) \mathcal{C}(x) : q ⋆ ∝ { ∑ j μ x ​ ( j ) ​ p j (Forward KL), ∏ j p j μ x ​ ( j ) (Reverse KL), \!\!q^{\star}\propto\begin{cases}\sum_{j}\mu_{x}(j)\,p_{j}&\text{(Forward KL),}\\[2.0pt] \prod_{j}p_{j}^{\,\mu_{x}(j)}&\text{(Reverse KL),}\end{cases} where p j := π ~ θ ( ⋅ ∣ s i , t , τ j ) p_{j}:=\widetilde{\pi}_{\theta}(\cdot\mid s_{i,t},\tau_{j}) and μ x \mu_{x} is the selection rule over 𝒞 ⁡ ( x ) \mathcal{C}(x) . This average distribution is problematic: (i) it need not correspond to any single feasible trajectory; (ii) it assigns equal weight to all prefixes, even those where verified trajectories disagree about the next token; and (iii) it inherits whatever each τ j \tau_{j} happens to take to reach the correct answer. These issues are fundamental to any distillation-based approach that treats the teacher as a target distribution.

## 5 SC-GRPO

#### Overview

Section 4.2 shows that directly using verified trajectories as OPSD distillation targets fails in RLVR. Therefore, we propose SC-GRPO ( S elf- C onditioned GRPO), which takes a different approach. We construct a self-conditioned teacher by conditioning the model on a verified trajectory, then measure the per-token distributional shift between the teacher and the original student.

This shift, quantified as token-level KL divergence, identifies which tokens depend on access to a verified solution. Tokens with small KL make the same prediction regardless of whether a verified solution is available. The token’s choice is unrelated to the rollout’s outcome, so applying sequence-level credit here misattributes success or failure. Tokens with large KL depend on verified solution, so the reward signal is informative. SC-GRPO uses this KL purely as a multiplicative weight on the GRPO gradient: the reward determines the update direction, and the KL determines its intensity at each token.

Figure 2 and Algorithm 1 illustrate the method. The core mechanism is described in § 5.1 : we construct a self-conditioned teacher by conditioning the model on a reference trajectory, compute token-level KL, and use it to weight the GRPO gradient. The reference is selected based on the number of correct rollouts n c n_{c} in the group: verified trajectories for partial-solve groups ( 2 ≤ n c < G 2\leq n_{c}<G ), random rollouts for solve-none groups ( n c = 0 n_{c}{=}0 ), and standard GRPO for n c = 1 n_{c}{=}1 or n c = G n_{c}{=}G . Section 5.2 analyzes the computational overhead.

### 5.1 Self-Conditioned GRPO

#### Teacher construction

For a rollout o i o_{i} with prefix states s i , t = ( x , o i , < t ) s_{i,t}=(x,o_{i,<t}) and a verified trajectory τ ∈ 𝒞 ⁡ ( x ) \tau\in\mathcal{C}(x) , we instantiate the self-conditioned teacher π ~ θ ( ⋅ ∣ s i , t , τ ) \widetilde{\pi}_{\theta}(\cdot\mid s_{i,t},\tau) via Eq. ( 4 ), where τ \tau appears only in the teacher’s system prompt. Appendix E provide the complete prompt templates. Both teacher and student are scored on the same prefix o i , < t o_{i,<t} of o i o_{i} . At each response token, we compute the forward KL from teacher to student: D i , t = KL ( π ~ θ ( ⋅ ∣ s i , t , τ ) ∥ π θ ( ⋅ ∣ s i , t ) ) . D_{i,t}=\mathrm{KL}\!\left(\widetilde{\pi}_{\theta}(\cdot\mid s_{i,t},\tau)\;\middle\|\;\pi_{\theta}(\cdot\mid s_{i,t})\right).

#### KL weighting

We map each D i , t D_{i,t} to a bounded weight f ⁡ ( D i , t ) ∈ [ 0 , 1 ) f(D_{i,t})\in[0,1) to modulate the GRPO gradient: tokens with small KL are downweighted, while tokens with large KL are preserved. We map each D i , t D_{i,t} to a bounded weight via f ⁡ ( D i , t ) \displaystyle f(D_{i,t}) = D i , t D i , t + c , \displaystyle=\frac{D_{i,t}}{D_{i,t}+c}, c \displaystyle c = max ⁡ ( P 75 ​ ( 𝒟 act ) , c min ) , \displaystyle=\max\!\left(P_{75}(\mathcal{D}_{\mathrm{act}}),\,c_{\min}\right), where 𝒟 act \mathcal{D}_{\mathrm{act}} is the set of active token KL values in the current micro-batch, P 75 P_{75} denotes its 75th percentile, and c min > 0 c_{\min}>0 is a small floor. We use P 75 P_{75} instead of median because token-level KL is sparse (most tokens have near-zero KL). P 75 P_{75} ensures low-KL tokens are suppressed while high-KL tokens are preserved. We visualize and analyze the KL distribution and weighting function in Appendix C.3 and Appendix C.4 . A detailed case study is provided in Appendix D .

#### Group routing

The reference trajectory τ \tau and advantage A ^ i \hat{A}_{i} are selected based on the group’s solve pattern. Partial-solve groups have both correct and incorrect rollouts, allowing us to use verified trajectories as references. Solve-none groups have zero GRPO gradient, so we extract exploration signal via diversity.

Partial-solve groups ( 2 ≤ n c < G 2\leq n_{c}<G ): For each rollout o i o_{i} , we sample a verified trajectory τ ∈ 𝒞 ⁡ ( x ) \tau\in\mathcal{C}(x) uniformly (with τ ≠ o i \tau\neq o_{i} when o i ∈ 𝒞 ⁡ ( x ) o_{i}\in\mathcal{C}(x) ). We use the GRPO advantage A ^ i \hat{A}_{i} in Eq. ( 1 ).

Solve-none groups ( n c = 0 n_{c}=0 ): We sample one rollout o r o_{r} uniformly as reference. For each remaining rollout o i o_{i} ( i ≠ r i\neq r ), we compute KL against the reference-conditioned teacher. The average KL weight over the reference-length prefix becomes a diversity score: s i = 1 L i ​ ∑ t = 1 L i f ⁡ ( D i , t ) , L i = min ⁡ ( | o i | , | o r | ) , s_{i}=\frac{1}{L_{i}}\sum_{t=1}^{L_{i}}f(D_{i,t}),\quad L_{i}=\min(|o_{i}|,|o_{r}|), where L i L_{i} truncates at the reference length. Since the reference itself is a failed trajectory, we apply stricter supervision to prevent reward hacking: tokens beyond the reference would have artificially high KL and inflate diversity scores for longer rollouts. Scores are normalized within the group to form a pseudo-advantage: A ^ i div = s i − mean ⁡ ( { s k } k = 1 G ) std ⁡ ( { s k } k = 1 G ) + ϵ , \hat{A}^{\mathrm{div}}_{i}=\frac{s_{i}-\mathrm{mean}(\{s_{k}\}_{k=1}^{G})}{\mathrm{std}(\{s_{k}\}_{k=1}^{G})+\epsilon}, (5) which replaces A ^ i \hat{A}_{i} with α ​ A ^ i div \alpha\hat{A}^{\mathrm{div}}_{i} in the SC-GRPO objective. Since all rollouts failed which bring zero GRPO advantage, this diversity signal encourages exploring new modes rather than repeating common ones.

Fallback ( n c = 1 n_{c}=1 or n c = G n_{c}=G ): Standard GRPO (no KL weighting).

SC-GRPO optimizes the weighted GRPO objective: J SC ​ - ​ GRPO ( θ ) = 𝔼 [ 1 G ∑ i = 1 G 1 | o i | ∑ t = 1 | o i | f ( D i , t ) min ( ρ i , t A ^ i , clip ( ρ i , t , 1 − ϵ , 1 + ϵ ) A ^ i ) ] , \begin{split}&J_{\mathrm{SC\text{-}GRPO}}(\theta)=\mathbb{E}\Big[\tfrac{1}{G}\!\sum_{i=1}^{G}\tfrac{1}{|o_{i}|}\!\sum_{t=1}^{|o_{i}|}\\ &\quad f(D_{i,t})\,\min\!\big(\rho_{i,t}\hat{A}_{i},\,\mathrm{clip}(\rho_{i,t},1{-}\epsilon,1{+}\epsilon)\hat{A}_{i}\big)\Big],\end{split}\vskip-5.69054pt where ρ i , t = π θ ​ ( o i , t ∣ s i , t ) / π θ old ​ ( o i , t ∣ s i , t ) \rho_{i,t}=\pi_{\theta}(o_{i,t}\mid s_{i,t})/\pi_{\theta_{\mathrm{old}}}(o_{i,t}\mid s_{i,t}) is the importance ratio, A ^ i \hat{A}_{i} is the advantage (GRPO advantage from Eq. ( 1 ) for partial-solve groups, α ​ A ^ i div \alpha\hat{A}^{\mathrm{div}}_{i} from Eq. ( 5 ) for solve-none groups). The KL weight f ⁡ ( D i , t ) f(D_{i,t}) is applied symmetrically: both correct and incorrect rollouts are downweighted at low-KL tokens, regardless of their advantage sign.

### 5.2 Computational Overhead

SC-GRPO adds a single new operation compared to GRPO: a teacher forward pass for per-token KL weighting. As shown in Figure 3 , this makes the actor update 51% slower on LiveCodeBench and 37% slower on DAPO-Math, but end-to-end step time grows by only 13% and 2% respectively, since rollout generation dominates total latency. Combined with the gains in Section 6.3 , this confirms that SC-GRPO’s improvements come from better use of existing rollouts rather than additional compute.

## 6 Experiments

### 6.1 Setup

#### Tasks

We train and evaluate on RLVR tasks spanning mathematical reasoning, code generation, and multi-turn agentic interaction. ( i ) Math : we train on DAPO-Math-17k ( Yu et al., 2026 ) and evaluate on AIME 2024 & 2025. ( ii ) Code : we use LiveCodeBench v6 ( Jain et al., 2025 ) (LCB), holding out half of each problem’s unit tests for training and using the rest for evaluation. ( iii ) AppWorld ( Trivedi et al., 2024 ) , ( iv ) WebShop ( Yao et al., 2022 ) . For both AppWorld and WebShop, we train and evaluated on the official splits. All runs share the same base model, Qwen3-8B with thinking disabled ( Yang et al., 2025 ) . Full per-task settings are detailed in Appendix B.1 .

#### Metrics

For each query we sample eight trajectories and report two metrics: Avg@8 , the mean verifier reward across the eight samples; and Pass@8 , the fraction of queries solved by at least one of the eight samples.

### 6.2 Baselines

We compare SC-GRPO against two families of baselines, all sharing the same base model, training data, rollouts-per-prompt, and step budget as our method.

#### Reinforcement learning

GRPO ( Guo et al., 2025 ) is the canonical RLVR algorithm. DAPO ( Yu et al., 2026 ) is a stronger GRPO variant incorporating decoupled clipping, dynamic sampling, and token-level loss normalization. REINFORCE++ ( Hu et al., 2025 ) simplifies PPO by removing the critic and shaping rewards with per-token KL penalties.

#### OPSD with external demonstrations

Following Zhao et al. (2026) , we report OPSD baselines that supply the teacher with demonstrations τ \tau produced by external LLMs and train student with the same OPSD objective. We consider three demonstration sources of progressively higher quality: MiniMax-M2.7 1 1 1 https://huggingface.co/MiniMaxAI/MiniMax-M2.7 , DeepSeekv4-Pro DeepSeek-AI (2026) , and Oracle , which obtain as many correct solutions as possible, simulating access to all reference solutions. Details and prompt templates are provided in Appendix B.2 .

### 6.3 Main Results

SC-GRPO consistently outperforms all baselines. Across all five benchmarks (Table 1 ), SC-GRPO achieves the highest Avg@8 and Pass@8, outperforming DAPO by 5.86% and 8.92% respectively. The largest improvements appear on multi-turn agentic tasks, where credit assignment over long horizons is most challenging. We provide detailed training dynamics in Appendix C .

#### REINFORCE++ exhibits unstable performance across tasks.

Despite also operating at the token level, REINFORCE++ shows inconsistent results: competitive on code generation but significantly weaker on mathematical reasoning, and collapsing on multi-turn agentic tasks. We analyze the training dynamics in Appendix B.4 . This instability highlights that removing the critic sacrifices robustness across diverse task structures. In contrast, SC-GRPO remains stable across all five benchmarks.

External demonstrations do not reliably help. The three OPSD variants all stay close to the Qwen3-8B base model, substantially below the RL baselines. Unexpectedly, Oracle fails to outperform DeepSeekv4-Pro and even underperforms the base model on LCB, suggesting that demonstration quantity and quality are not the bottleneck. These results indicate that OPSD constructed from external demonstrations provides an unreliable training signal, as we demonstrate in § 4.2 . SC-GRPO addresses this by drawing the teacher trajectory from the model’s own verifier-approved rollouts, achieving substantially stronger performance.

## 7 Analysis

In this section, we conduct a comprehensive analysis to answer the following research questions: RQ1: Why must the KL signal be a weight rather than a loss? (§ 7.1 ) RQ2: Which design choices within SC-GRPO matter most? (§ 7.2 ) RQ3: Do the gains transfer out of domain? (§ 7.3 )

### 7.1 RQ1: Additive Loss

A natural alternative to SC-GRPO is to add the self-conditioned teacher’s KL divergence as an auxiliary distillation loss: ℒ GRPO + β ​ ℒ distill \mathcal{L}_{\mathrm{GRPO}}+\beta\,\mathcal{L}_{\mathrm{distill}} . We test Forward KL, Reverse KL (both with fixed β = 0.1 \beta=0.1 and linear warm-up β : → 0.1 \beta:0.03\!\to\!0.1 ), and Bidirectional KL (combining both directions with complementary coefficients). Table 2 shows that all five variants underperform SC-GRPO.

Following Li et al. (2026) , we compare SC-GRPO against OPD under two configurations (Figure 4 ). The left panel (Qwen3-1.7B-Base student, Qwen3-4B-Base teacher) represents a failing OPD setting, the right panel (DeepSeek-R1-Distill-Qwen-1.5B ( Guo et al., 2025 ) student, JustRL-DeepSeek-1.5B ( He et al., 2025 ) teacher) represents a successful setting. Hyperparameters are detailed in Appendix B.3 . Figure 4 shows that SC-GRPO consistently outperforms OPD in both settings. When OPD fails (left), SC-GRPO achieves 23% improvement, when OPD succeeds (right), SC-GRPO still outperforms OPD on both AIME tasks, while requiring no external teacher.

### 7.2 RQ2: Ablation Study

We validate the three core design choices in SC-GRPO (Table 3 ).

#### A1 Group Routing

The KL weighting is designed to operate where meaningful contrast exists. Partial-solve groups ( 2 ≤ n c < G 2\leq n_{c}<G ) provide such contrast and benefit from KL weighting. Adding solve-none groups ( n c = 0 n_{c}=0 ) brings further improvement, as the diversity signal recovers useful updates from otherwise zero-gradient groups. Including single-correct groups ( n c = 1 n_{c}=1 ) violates the design premise: the single verified trajectory dominates the KL signal, causing entropy collapse. Including all-correct groups ( n c = G n_{c}=G ) similarly fails: without incorrect rollouts for contrast, self-conditioned teacher cannot separate critical decision points from routine tokens. Covering all groups combines both failure modes and drops below GRPO.

#### A2 Normalization threshold

The threshold c c separates the informative high-KL tail from the uninformative majority (visualization in Appendix C.3 ). When c = p 50 c=p_{50} (median), the heavily right-skewed KL distribution pushes c c below 10 − 4 10^{-4} , making f ⁡ ( KL ) ≈ 1 f(\mathrm{KL})\approx 1 for nearly all tokens and reducing to uniform weighting. Using c = max ⁡ ( p 75 , 10 − 4 ) c=\max(p_{75},10^{-4}) achieves the intended separation: p 75 p_{75} suppresses the low-KL majority while the floor prevents collapse when the entire batch has near-zero KL. A fixed constant achieves comparable performance but requires per-task calibration; p 75 p_{75} with floor is adaptive and hyperparameter-free.

#### A3 Diversity coefficient

The diversity signal rewards exploration rather than correctness, so it should serve as a weak exploration signal that does not override the reward gradient. The ablation confirms this: α = 0.1 \alpha{=}0.1 provides sufficient pressure to break repeated failure patterns, while α = 0.2 \alpha{=}0.2 lets the exploration signal compete with the RL objective and degrades performance.

### 7.3 RQ3: Out-of-Domain Performance

Both SC-GRPO and DAPO are trained exclusively on LiveCodeBench and evaluated on Codeforces without domain-specific fine-tuning. Figure 5 shows that SC-GRPO retains its advantage, achieving 5.2% relative gain on Avg@8 (nearly identical to the 6.1% in-domain gain on LCB v6) while maintaining comparable Pass@8. The consistent improvement across domains suggests that SC-GRPO’s gains stem from improved credit assignment rather than overfitting.

## 8 Conclusion

We propose SC-GRPO, a token-level credit assignment method for RLVR. By constructing a self-conditioned teacher from the model’s own verified rollouts and measuring token-level KL divergence, SC-GRPO assigns fine-grained credit to each token. This KL signal is used as a per-token weight on the GRPO gradient, eliminating sensitivity to divergence form choice and requiring no external resources beyond what RLVR already provides. Experiments show that SC-GRPO consistently outperforms GRPO and other baseline with minimal computational overhead, demonstrating the effectiveness and robustness of SC-GRPO.

### Limitations

Due to computational resource constraints, our experiments are limited to models up to 8B parameters and response lengths up to 12288 tokens. The effectiveness of SC-GRPO on larger models and longer responses remains to be explored. Similarly, resource limitations restrict our evaluation to models operating in standard reasoning mode. The applicability of SC-GRPO to extended thinking modes (e.g., chain-of-thought with explicit reasoning steps, multi-turn refinement) or structured output formats remains unexplored.

### Ethics Statement

This work focuses on improving token-level credit assignment in reinforcement learning with verifiable rewards. All LLMs, RL frameworks, and datasets used in our experiments are publicly available and used in accordance with their respective licenses. As a training algorithm, SC-GRPO does not introduce new ethical concerns

## References

Agarwal et al. (2024) R. Agarwal, N. Vieillard, Y. Zhou, P. Stanczyk, S. R. Garea, M. Geist, and O. Bachem On-policy distillation of language models: learning from self-generated mistakes . In The twelfth international conference on learning representations , Cited by: §1 , §2.1 , §3.2 .

Cui et al. (2025) G. Cui, L. Yuan, Z. Wang, H. Wang, Y. Zhang, J. Chen, W. Li, B. He, Y. Fan, T. Yu, et al. Process reinforcement through implicit rewards . arXiv preprint arXiv:2502.01456 . Cited by: §1 , §2.2 .

DeepSeek-AI (2026) DeepSeek-AI DeepSeek-v4: towards highly efficient million-token context intelligence . Cited by: §6.2 .

Ding (2026) K. Ding HDPO: hybrid distillation policy optimization via privileged self-distillation . arXiv preprint arXiv:2603.23871 . Cited by: §2.1 , §3.2 .

Gao et al. (2024) J. Gao, S. Xu, W. Ye, W. Liu, C. He, W. Fu, Z. Mei, G. Wang, and Y. Wu On designing effective rl reward at training time for llm reasoning . arXiv preprint arXiv:2410.15115 . Cited by: §2.2 .

Gu et al. (2024) Y. Gu, H. Zhou, F. Meng, J. Zhou, and M. Huang MiniPLM: knowledge distillation for pre-training language models . In The Thirteenth International Conference on Learning Representations , Cited by: §2.1 .

[7] X. Guan, L. L. Zhang, Y. Liu, N. Shang, Y. Sun, Y. Zhu, F. Yang, and M. Yang RStar-math: small llms can master math reasoning with self-evolved deep thinking . In Forty-second International Conference on Machine Learning , Cited by: §2.2 .

Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Xu, H. Ding, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Chen, J. Yuan, J. Tu, J. Qiu, J. Li, J. L. Cai, J. Ni, J. Liang, J. Chen, K. Dong, K. Hu, K. You, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang, L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Zhou, M. Li, M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang, Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang, R. J. Chen, R. L. Jin, R. Chen, S. Lu, S. Zhou, S. Chen, S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang, W. L. Xiao, W. An, X. Liu, X. Wang, X. Chen, X. Nie, X. Cheng, X. Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su, X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun, X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li, Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi, Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma, Y. Tang, Y. Zha, Y. Yan, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu, Z. Xie, Z. Zhang, Z. Hao, Z. Ma, Z. Yan, Z. Wu, Z. Gu, Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Pan, Z. Huang, Z. Xu, Z. Zhang, and Z. Zhang DeepSeek-r1 incentivizes reasoning in llms through reinforcement learning . Nature 645 ( 8081 ), pp. 633–638 . External Links: ISSN 1476-4687 , Link , Document Cited by: §1 , §6.2 , §7.1 .

Guo et al. (2026) Y. Guo, L. Xu, J. Liu, D. Ye, and S. Qiu Segment policy optimization: effective segment-level credit assignment in rl for large language models . Advances in Neural Information Processing Systems 38 , pp. 114399–114431 . Cited by: §2.2 .

He et al. (2025) B. He, Z. Qu, Z. Liu, Y. Chen, Y. Zuo, C. Qian, K. Zhang, W. Chen, C. Xiao, G. Cui, et al. Justrl: scaling a 1.5 b llm with a simple rl recipe . arXiv preprint arXiv:2512.16649 . Cited by: §7.1 .

He et al. (2026a) B. He, M. Hu, Z. Xu, H. Wang, L. Zong, Y. Chen, C. Ma, X. Liu, P. Zhou, and I. King Search-r2: enhancing search-integrated reasoning via actor-refiner collaboration . External Links: 2602.03647 , Link Cited by: §1 .

He et al. (2026b) Y. He, H. Wu, S. Liu, H. Ge, H. Zhou, K. Wu, Z. Zheng, Q. Lin, Z. Zhong, and Y. Zhang Rethinking token-level credit assignment in rlvr: a polarity-entropy analysis . arXiv preprint arXiv:2604.11056 . Cited by: §1 .

Hinton et al. (2015) G. Hinton, O. Vinyals, and J. Dean Distilling the knowledge in a neural network . arXiv preprint arXiv:1503.02531 . Cited by: §1 , §2.1 .

Hu et al. (2025) J. Hu, J. K. Liu, H. Xu, and W. Shen REINFORCE++: stabilizing critic-free policy optimization with global advantage normalization . External Links: 2501.03262 , Link Cited by: §B.4 , §6.2 .

Hübotter et al. (2026) J. Hübotter, F. Lübeck, L. Behric, A. Baumann, M. Bagatella, D. Marta, I. Hakimi, I. Shenfeld, T. K. Buening, C. Guestrin, et al. Reinforcement learning via self-distillation . arXiv preprint arXiv:2601.20802 . Cited by: §1 , §2.1 , §3.2 .

Jain et al. (2025) N. Jain, A. Gu, W. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica Livecodebench: holistic and contamination free evaluation of large language models for code . In International Conference on Learning Representations , Vol. 2025 , pp. 58791–58831 . Cited by: §B.1 , §6.1 .

Juneja et al. (2025) G. Juneja, D. Nathani, and W. Y. Wang Adversarial training for process reward models . arXiv preprint arXiv:2511.22888 . Cited by: §2.2 .

Ko et al. (2024) J. Ko, S. Kim, T. Chen, and S. Yun DistiLLM: towards streamlined distillation for large language models . In Forty-first International Conference on Machine Learning , Cited by: §1 , §2.1 .

Li et al. (2026) Y. Li, Y. Zuo, B. He, J. Zhang, C. Xiao, C. Qian, T. Yu, H. Gao, W. Yang, Z. Liu, and N. Ding Rethinking on-policy distillation of large language models: phenomenology, mechanism, and recipe . External Links: 2604.13016 , Link Cited by: §B.3 , §7.1 .

Lightman et al. (2023) H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe Let’s verify step by step . External Links: 2305.20050 , Link Cited by: §2.2 .

[21] Z. Liu, C. Chen, W. Li, P. Qi, T. Pang, C. Du, W. S. Lee, and M. Lin Understanding r1-zero-like training: a critical perspective . In Second Conference on Language Modeling , Cited by: §1 .

Shenfeld et al. (2026) I. Shenfeld, M. Damani, J. Hübotter, and P. Agrawal Self-distillation enables continual learning . External Links: 2601.19897 , Link Cited by: §2.1 .

[23] M. Shing, K. Misaki, H. Bao, S. Yokoi, and T. Akiba TAID: temporally adaptive interpolated distillation for efficient knowledge transfer in language models . In The Thirteenth International Conference on Learning Representations , Cited by: §2.1 .

Trivedi et al. (2024) H. Trivedi, T. Khot, M. Hartmann, R. Manku, V. Dong, E. Li, S. Gupta, A. Sabharwal, and N. Balasubramanian Appworld: a controllable world of apps and people for benchmarking interactive coding agents . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 16022–16076 . Cited by: §B.1 , §6.1 .

Wang et al. (2025a) G. Wang, Z. Yang, Z. Wang, S. Wang, Q. Xu, and Q. Huang ABKD: pursuing a proper allocation of the probability mass in knowledge distillation via α \alpha - β \beta -divergence . In International Conference on Machine Learning , pp. 65167–65212 . Cited by: §2.1 .

Wang et al. (2025b) G. Wang, S. Dai, G. Ye, Z. Gan, W. Yao, Y. Deng, X. Wu, and Z. Ying Information gain-based policy optimization: a simple and effective approach for multi-turn llm agents . arXiv preprint arXiv:2510.14967 . Cited by: §1 , §2.2 .

Wang et al. (2024a) H. Wang, W. Xiong, T. Xie, H. Zhao, and T. Zhang Interpretable preferences via multi-objective reward modeling and mixture-of-experts . In EMNLP , Cited by: §2.2 .

Wang et al. (2025c) H. Wang, C. Qian, W. Zhong, X. Chen, J. Qiu, S. Huang, B. Jin, M. Wang, K. Wong, and H. Ji Acting less is reasoning more! teaching model to act efficiently . External Links: 2504.14870 , Link Cited by: §1 .

Wang et al. (2024b) P. Wang, L. Li, Z. Shao, R. Xu, D. Dai, Y. Li, D. Chen, Y. Wu, and Z. Sui Math-shepherd: verify and reinforce llms step-by-step without human annotations . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 9426–9439 . Cited by: §1 , §2.2 .

Xie et al. (2025) C. Xie, R. Pan, X. Wu, Y. Zhang, J. Fu, T. Gao, and G. Zhou Unlocking exploration in rlvr: uncertainty-aware advantage shaping for deeper reasoning . arXiv preprint arXiv:2510.10649 . Cited by: §1 .

Yang et al. (2025) A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, C. Zheng, D. Liu, F. Zhou, F. Huang, F. Hu, H. Ge, H. Wei, H. Lin, J. Tang, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Zhou, J. Lin, K. Dang, K. Bao, K. Yang, L. Yu, L. Deng, M. Li, M. Xue, M. Li, P. Zhang, P. Wang, Q. Zhu, R. Men, R. Gao, S. Liu, S. Luo, T. Li, T. Tang, W. Yin, X. Ren, X. Wang, X. Zhang, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Zhang, Y. Wan, Y. Liu, Z. Wang, Z. Cui, Z. Zhang, Z. Zhou, and Z. Qiu Qwen3 technical report . External Links: 2505.09388 , Link Cited by: §6.1 .

Yang et al. (2026) C. Yang, C. Qin, Q. Si, M. Chen, N. Gu, D. Yao, Z. Lin, W. Wang, J. Wang, and N. Duan Self-distilled rlvr . External Links: 2604.03128 , Link Cited by: §2.1 .

Yao et al. (2026) J. Yao, H. Huang, S. Zeng, C. Luo, W. You, J. Tang, Q. Liu, Y. Guo, and Y. Kang Incorporating self-rewriting into large language model reasoning reinforcement . In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 40 , pp. 34405–34413 . Cited by: §1 .

Yao et al. (2022) S. Yao, H. Chen, J. Yang, and K. Narasimhan Webshop: towards scalable real-world web interaction with grounded language agents . Advances in Neural Information Processing Systems 35 , pp. 20744–20757 . Cited by: §B.1 , §6.1 .

Yu et al. (2026) Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, W. Dai, T. Fan, G. Liu, L. Liu, et al. Dapo: an open-source llm reinforcement learning system at scale . Advances in Neural Information Processing Systems 38 , pp. 113222–113244 . Cited by: §B.1 , §1 , §6.1 , §6.2 .

Zhao et al. (2026) S. Zhao, Z. Xie, M. Liu, J. Huang, G. Pang, F. Chen, and A. Grover Self-distilled reasoner: on-policy self-distillation for large language models . arXiv preprint arXiv:2601.18734 . Cited by: §B.2 , §B.2 , §1 , §1 , §2.1 , §3.2 , §6.2 .

Zheng et al. (2025) C. Zheng, S. Liu, M. Li, X. Chen, B. Yu, C. Gao, K. Dang, Y. Liu, R. Men, A. Yang, et al. Group sequence policy optimization . arXiv preprint arXiv:2507.18071 . Cited by: §1 .

## Appendix A Derivation for Direct OPSD in RLVR

This section formalizes why directly adapting OPSD in the standard RLVR setting induces a token-level target mismatch. We fix a query x x , a student rollout prefix o i , < t o_{i,<t} , and analyze the induced distribution over the next token.

### A.1 Setup

Following Section 3 , for a query x x let { o i } i = 1 G ∼ π θ old ( ⋅ ∣ x ) \{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid x) be the sampled response group, and let r ⁡ ( x , o i ) ∈ { 0 , 1 } r(x,o_{i})\in\{0,1\} be the verifier reward. The set of verifier-approved responses is 𝒞 ( x ) := { o i : r ( x , o i ) = 1 , i = 1 , … , G } . \mathcal{C}(x)\;:=\;\{\,o_{i}:r(x,o_{i})=1,\ i=1,\ldots,G\,\}. (A.1) Fix a student response o i o_{i} and token position t t , and let the prefix state be s i , t := ( x , o i , < t ) s_{i,t}:=(x,o_{i,<t}) . The student next-token distribution is π θ ( ⋅ ∣ s i , t ) = π θ ( ⋅ ∣ x , o i , < t ) . \pi_{\theta}(\cdot\mid s_{i,t})\;=\;\pi_{\theta}(\cdot\mid x,o_{i,<t}). (A.2) For each verifier-approved response τ j ∈ 𝒞 ⁡ ( x ) \tau_{j}\in\mathcal{C}(x) , direct OPSD constructs a self-conditioned teacher by additionally conditioning the same model on τ j \tau_{j} : π ~ θ ( ⋅ ∣ s i , t , τ j ) := sg [ π θ ( ⋅ ∣ x , τ j , o i , < t ) ] . \widetilde{\pi}_{\theta}(\cdot\mid s_{i,t},\,\tau_{j})\;:=\;\operatorname{sg}\!\left[\pi_{\theta}(\cdot\mid x,\,\tau_{j},\,o_{i,<t})\right]. (A.3) Let μ x \mu_{x} denote a selection distribution over 𝒞 ⁡ ( x ) \mathcal{C}(x) that specifies which verifier-approved response is used as the privileged context (e.g., uniform over 𝒞 ⁡ ( x ) \mathcal{C}(x) ).

The stop-gradient operator sg ⁡ [ ⋅ ] \operatorname{sg}[\cdot] indicates that the self-conditioned teacher is treated as a fixed target for the current update, and gradients do not backpropagate through teacher logits. We further assume all distributions are defined over a common finite vocabulary 𝒱 \mathcal{V} with shared support, which is satisfied by standard softmax LLM outputs.

### A.2 Forward-KL Direct OPSD

We use forward KL as a representative distillation objective and analyze direct OPSD pointwise at a single prefix.

#### Notation.

Fix a query x x , a student rollout o i o_{i} , and a token position t t , with prefix state s i , t = ( x , o i , < t ) s_{i,t}=(x,o_{i,<t}) . Throughout this subsection we suppress the dependence on ( i , t ) (i,t) and write q \displaystyle q := π θ ( ⋅ ∣ s i , t ) , \displaystyle:=\;\pi_{\theta}(\cdot\mid s_{i,t}), (A.4) p j \displaystyle p_{j} := π ~ θ ( ⋅ ∣ s i , t , τ j ) , τ j ∈ 𝒞 ( x ) . \displaystyle:=\;\widetilde{\pi}_{\theta}(\cdot\mid s_{i,t},\,\tau_{j}),\quad\tau_{j}\in\mathcal{C}(x). Here q q is the student next-token distribution and each p j p_{j} is a self-conditioned teacher distribution (treated as a fixed target via stop-gradient). All quantities are distributions over the vocabulary 𝒱 \mathcal{V} , for a distribution p p and a token y ∈ 𝒱 y\in\mathcal{V} , p ⁡ ( y ) ∈ [ 0 , 1 ] p(y)\in[0,1] denotes the probability assigned to y y .

The direct OPSD loss at this prefix is ℓ OPSD ( q ) := 𝔼 j ∼ μ x [ D KL ( p j ∥ q ) ] , \ell_{\mathrm{OPSD}}(q)\;:=\;\mathbb{E}_{j\sim\mu_{x}}\!\left[D_{\mathrm{KL}}\!\bigl(p_{j}\,\|\,q\bigr)\right], (A.5) and the μ x \mu_{x} -averaged teacher distribution is the per-token weighted average p ¯ ​ ( y ) := ∑ j μ x ​ ( j ) ​ p j ​ ( y ) , y ∈ 𝒱 . \bar{p}(y)\;:=\;\sum_{j}\mu_{x}(j)\,p_{j}(y),\qquad y\in\mathcal{V}. (A.6)

Inserting p ¯ ​ ( y ) \bar{p}(y) into the log ratio in Eq. ( A.5 ) and using 𝔼 j ​ [ p j ​ ( y ) ] = p ¯ ​ ( y ) \mathbb{E}_{j}[p_{j}(y)]=\bar{p}(y) yields ℓ OPSD ​ ( q ) \displaystyle\ell_{\mathrm{OPSD}}(q) = 𝔼 j ∼ μ x ​ ∑ y ∈ 𝒱 p j ​ ( y ) ​ log ⁡ p j ​ ( y ) q ⁡ ( y ) \displaystyle=\mathbb{E}_{j\sim\mu_{x}}\sum_{y\in\mathcal{V}}p_{j}(y)\,\log\tfrac{p_{j}(y)}{q(y)} (A.7) = 𝔼 j ∼ μ x ​ ∑ y ∈ 𝒱 p j ​ ( y ) ​ log ⁡ p j ​ ( y ) p ¯ ​ ( y ) \displaystyle=\mathbb{E}_{j\sim\mu_{x}}\sum_{y\in\mathcal{V}}p_{j}(y)\,\log\tfrac{p_{j}(y)}{\bar{p}(y)} + 𝔼 j ∼ μ x ∑ y ∈ 𝒱 p j ( y ) log p ¯ ​ ( y ) q ⁡ ( y ) \displaystyle+\mathbb{E}_{j\sim\mu_{x}}\sum_{y\in\mathcal{V}}p_{j}(y)\,\log\tfrac{\bar{p}(y)}{q(y)} = 𝔼 j ∼ μ x D KL ( p j ∥ p ¯ ) \displaystyle=\mathbb{E}_{j\sim\mu_{x}}\,D_{\mathrm{KL}}\!\bigl(p_{j}\,\|\,\bar{p}\bigr) + ∑ y ∈ 𝒱 p ¯ ( y ) log p ¯ ​ ( y ) q ⁡ ( y ) \displaystyle+\sum_{y\in\mathcal{V}}\bar{p}(y)\,\log\tfrac{\bar{p}(y)}{q(y)} = 𝔼 j ∼ μ x D KL ( p j ∥ p ¯ ) ⏟ 𝒟 disagree ≥ 0 + D KL ( p ¯ ∥ q ) . \displaystyle=\underbrace{\mathbb{E}_{j\sim\mu_{x}}\,D_{\mathrm{KL}}\!\bigl(p_{j}\,\|\,\bar{p}\bigr)}_{\mathcal{D}_{\mathrm{disagree}}\,\geq\,0}\;+\;D_{\mathrm{KL}}\!\bigl(\bar{p}\,\|\,q\bigr). where the expectation is over j ∼ μ x j\sim\mu_{x} and the sums are over y ∈ 𝒱 y\in\mathcal{V} . The first term 𝒟 disagree ≥ 0 \mathcal{D}_{\mathrm{disagree}}\geq 0 quantifies how much the self-conditioned teachers { p j } \{p_{j}\} disagree with each other at this prefix: it is zero exactly when all p j p_{j} coincide, and grows as they spread apart. Equivalently, when μ x \mu_{x} is uniform, 𝒟 disagree \mathcal{D}_{\mathrm{disagree}} is the generalized Jensen–Shannon divergence of { p j } \{p_{j}\} .

The disagreement term 𝒟 disagree \mathcal{D}_{\mathrm{disagree}} measures how much the self-conditioned teachers disagree at this prefix, crucially, it is constant in q q . The only q q -dependent term is D KL ( p ¯ ∥ q ) ≥ 0 D_{\mathrm{KL}}(\bar{p}\,\|\,q)\geq 0 , with equality if and only if q = p ¯ q=\bar{p} . Hence the unconstrained pointwise minimizer of Eq. ( A.5 ) is q ⋆ = p ¯ . q^{\star}\;=\;\bar{p}. (A.8)

Direct forward-KL OPSD does not target any particular verified trajectory’s local continuation, it targets the average p ¯ \bar{p} of the self-conditioned teacher distributions. The disagreement term 𝒟 disagree \mathcal{D}_{\mathrm{disagree}} shows that different verified trajectories can induce genuinely different local continuations, but this disagreement does not influence the optimizer because it is constant in q q . In a parametric policy class, the update can be viewed as projecting the student toward this average, an average that need not correspond to any single feasible trajectory.

### A.3 Reverse-KL Variant

The previous analysis is specific to forward KL. We now repeat the pointwise analysis for the reverse-KL variant of direct OPSD, using the same notation ( q , p j , μ x q,p_{j},\mu_{x} ) as in Appendix A.2 .

The reverse-KL direct OPSD loss at the prefix s i , t s_{i,t} is ℓ OPSD ( q ) := 𝔼 j ∼ μ x [ D KL ( q ∥ p j ) ] . \ell_{\mathrm{OPSD}}(q)\;:=\;\mathbb{E}_{j\sim\mu_{x}}\!\left[D_{\mathrm{KL}}\!\bigl(q\,\|\,p_{j}\bigr)\right]. (A.9)

Unfolding the KL by definition and using the linearity of expectation in j j : ℓ OPSD ​ ( q ) \displaystyle\ell_{\mathrm{OPSD}}(q) = 𝔼 j ​ ∑ y ∈ 𝒱 q ⁡ ( y ) ​ log ⁡ q ⁡ ( y ) p j ​ ( y ) \displaystyle=\mathbb{E}_{j}\sum_{y\in\mathcal{V}}q(y)\,\log\tfrac{q(y)}{p_{j}(y)} (A.10) = ∑ y ∈ 𝒱 q ⁡ ( y ) ​ log ⁡ q ⁡ ( y ) \displaystyle=\sum_{y\in\mathcal{V}}q(y)\log q(y) − ∑ y ∈ 𝒱 q ( y ) 𝔼 j [ log p j ( y ) ] , \displaystyle-\sum_{y\in\mathcal{V}}q(y)\,\mathbb{E}_{j}\!\left[\log p_{j}(y)\right],

Minimizing Eq. ( A.10 ) over q q subject to ∑ y q ⁡ ( y ) = 1 \sum_{y}q(y)=1 , we form the Lagrangian ℒ ⁡ ( q , λ ) \displaystyle\mathcal{L}(q,\lambda) = ∑ y q ⁡ ( y ) ​ log ⁡ q ⁡ ( y ) \displaystyle=\sum_{y}q(y)\log q(y) (A.11) − ∑ y q ( y ) 𝔼 j [ log p j ( y ) ] \displaystyle-\sum_{y}q(y)\,\mathbb{E}_{j}[\log p_{j}(y)] + λ ⁡ ( ∑ y q ⁡ ( y ) − 1 ) , \displaystyle+\lambda\!\left(\sum_{y}q(y)-1\right), where λ \lambda is the Lagrange multiplier for the normalization constraint. Setting ∂ ℒ / ∂ q ⁡ ( y ) = 0 \partial\mathcal{L}/\partial q(y)=0 yields the stationarity condition log ⁡ q ⁡ ( y ) + 1 − 𝔼 j ​ [ log ⁡ p j ​ ( y ) ] + λ = 0 , \log q(y)+1-\mathbb{E}_{j}\!\left[\log p_{j}(y)\right]+\lambda=0, (A.12) which gives q ⁡ ( y ) ∝ exp ⁡ ( 𝔼 j ​ [ log ⁡ p j ​ ( y ) ] ) q(y)\propto\exp\!\bigl(\mathbb{E}_{j}[\log p_{j}(y)]\bigr) . Enforcing the normalization constraint yields q ⋆ ​ ( y ) = exp ⁡ ( 𝔼 j ​ [ log ⁡ p j ​ ( y ) ] ) ∑ y ′ ∈ 𝒱 exp ⁡ ( 𝔼 j ​ [ log ⁡ p j ​ ( y ′ ) ] ) . q^{\star}(y)\;=\;\frac{\exp\!\bigl(\mathbb{E}_{j}[\log p_{j}(y)]\bigr)}{\sum_{y^{\prime}\in\mathcal{V}}\exp\!\bigl(\mathbb{E}_{j}[\log p_{j}(y^{\prime})]\bigr)}. (A.13) Equivalently, q ⋆ q^{\star} is the normalized weighted geometric mean of the teacher distributions: q ⋆ ​ ( y ) ∝ ∏ j p j ​ ( y ) μ x ​ ( j ) . q^{\star}(y)\;\propto\;\prod_{j}p_{j}(y)^{\mu_{x}(j)}. (A.14)

#### Interpretation

Reverse-KL direct OPSD replaces the per-token arithmetic average p ¯ \bar{p} from the forward-KL case (Eq. ( A.8 )) with a normalized geometric average of the self-conditioned teacher distributions. The two averages have very different behavior: the geometric mean q ⋆ ​ ( y ) q^{\star}(y) is large only when every p j ​ ( y ) p_{j}(y) is non-negligible, so reverse KL exhibits mode-seeking behavior, concentrating mass on tokens that all teachers find plausible. The arithmetic mean p ¯ ​ ( y ) \bar{p}(y) , in contrast, is large whenever any p j ​ ( y ) p_{j}(y) is large, exhibiting mode-covering behavior. Despite this difference, the overall conclusion is the same: changing the divergence merely changes the form of averaging, but the optimization target is still constructed from self-conditioned teacher distributions.

### A.4 Summary: Why Direct OPSD Fails in RLVR

Combining Appendices A.2 and A.3 , we obtain a unified characterization of direct OPSD at any prefix s i , t s_{i,t} .

#### Pointwise minimizers under different divergences.

Let { p j } j \{p_{j}\}_{j} denote the self-conditioned teacher distributions induced by verifier-approved trajectories τ j ∈ 𝒞 ⁡ ( x ) \tau_{j}\in\mathcal{C}(x) , weighted by the selection rule μ x \mu_{x} . Then the pointwise minimizer of direct OPSD takes the form q ⋆ ​ ( y ) = { ∑ j μ x ​ ( j ) ​ p j ​ ( y ) (forward KL), ∏ j p j ​ ( y ) μ x ​ ( j ) ∑ y ′ ∏ j p j ​ ( y ′ ) μ x ​ ( j ) (reverse KL), q^{\star}(y)\;=\;\begin{cases}\displaystyle\sum_{j}\mu_{x}(j)\,p_{j}(y)&\text{(forward KL),}\\[6.0pt] \displaystyle\frac{\prod_{j}p_{j}(y)^{\mu_{x}(j)}}{\sum_{y^{\prime}}\prod_{j}p_{j}(y^{\prime})^{\mu_{x}(j)}}&\text{(reverse KL),}\end{cases} (A.15) a weighted arithmetic average and a normalized weighted geometric average of the teachers, respectively.

#### Three structural problems.

Eq. ( A.15 ) exposes three problems that arise regardless of the choice of divergence:

The optimization target is an average, not a trajectory. Both minimizers are constructed by combining multiple self-conditioned teachers. Even if every individual p j p_{j} corresponded to a valid local continuation of τ j \tau_{j} , the average q ⋆ q^{\star} generally does not correspond to any single feasible trajectory. The student is trained to imitate a synthetic distribution that no verified rollout actually instantiates.

Disagreement between teachers carries information, but the loss discards it. The forward-KL decomposition in Eq. ( A.7 ) contains the disagreement term 𝒟 disagree ≥ 0 \mathcal{D}_{\mathrm{disagree}}\geq 0 , which measures how much the teachers { p j } \{p_{j}\} disagree about the next token at the current prefix. This quantity is large precisely at prefixes where different verified trajectories branch into different continuations—for example, a math prefix “ Solve 2 ​ x + 4 = 10 2x+4=10 , so ” where one verified trajectory continues with “ 2 ​ x = 6 2x=6 ” while another continues with “ subtract 4 from both sides ”. Such prefixes are arguably the most informative ones for the student: they mark decision points where multiple valid continuations exist. Yet because 𝒟 disagree \mathcal{D}_{\mathrm{disagree}} does not depend on q q , it contributes nothing to the gradient. As far as the loss is concerned, a prefix with strong teacher disagreement is treated identically to a prefix where all teachers agree. Direct OPSD therefore uses the disagreement signal only implicitly , through how it perturbs the average p ¯ \bar{p} , and never as a per-token quantity that could focus learning on these branch points.

The teacher is not a verifier-defined ground truth. Each p j p_{j} is constructed by conditioning the student on a single verifier-approved trajectory τ j \tau_{j} . As discussed in Section 5 , τ j \tau_{j} certifies only end-task success and may contain redundant, lucky, or even flawed reasoning. Treating p j p_{j} as a distillation target therefore propagates whatever artifacts τ j \tau_{j} contains into the student, weighted equally with genuinely informative predictions.

#### Implication.

The three problems above are not artifacts of a particular divergence choice or selection rule μ x \mu_{x} : they follow directly from the structural fact that direct OPSD uses self-conditioned teachers as distillation targets . Any objective that asks the student to move toward { p j } \{p_{j}\} in distribution will inherit some form of Eq. ( A.15 ), and hence inherit (P1)–(P3).

## Appendix B Experiment Details

### B.1 Training Details

Table 4 summarizes the training settings for each task. All experiments use Qwen3-8B (thinking disabled) as the base model. For mathematical reasoning (AIME 24&25), we randomly sample 4,000 problems from DAPO-Math-17k ( Yu et al., 2026 ) . For code generation (LCB v6), we randomly sample half of the unit tests per problem in LiveCodeBench v6 Jain et al. (2025) as our training set and reserve the other half for evaluation. For AppWorld Trivedi et al. (2024) , we train on the official training split. For WebShop Yao et al. (2022) , we randomly sample 2,400 tasks from the training split. All runs use 8 rollouts per prompt, a batch size of 8 prompts per update, and a learning rate of 1 × 10 − 6 1\times 10^{-6} . We conducted experiments using an 8-node cluster. Each node was equipped with 8 NVIDIA A100 80GB GPUs, 144-core AMD EPYC 7713 processors, and 960 GB of RAM, running Ubuntu as the operating system.

### B.2 OPSD Details

We follow the OPSD framework of Zhao et al. (2026) . In the original formulation, the teacher is conditioned on the ground-truth answer y ∗ y^{*} (e.g., an answer with reference chain-of-thought), and the training objective minimizes the per-token divergence between the privileged teacher and the student along the student’s own rollouts: ℒ OPSD ( θ ) = 𝔼 x , y ^ ∼ π θ ( ⋅ ∣ x ) [ 1 | y ^ | ∑ t = 1 | y ^ | D ( p T t ∥ p S t ) ] , \displaystyle\mathcal{L}_{\mathrm{OPSD}}(\theta)=\mathbb{E}_{x,\,\hat{y}\sim\pi_{\theta}(\cdot\mid x)}\left[\frac{1}{|\hat{y}|}\sum_{t=1}^{|\hat{y}|}D\big(p_{T}^{t}\,\big\|\,p_{S}^{t}\big)\right], where p T t = π θ ( ⋅ ∣ x , y ∗ , y ^ < t ) , \displaystyle\text{where}\quad p_{T}^{t}=\pi_{\theta}(\cdot\mid x,y^{*},\hat{y}_{<t}), p S t = π θ ( ⋅ ∣ x , y ^ < t ) . \displaystyle\phantom{\text{where}}\quad p_{S}^{t}=\pi_{\theta}(\cdot\mid x,\hat{y}_{<t}).

#### Demonstration Acquisition

The key requirement of OPSD is a ground-truth answer y ∗ y^{*} to serve as the teacher’s privileged context. How y ∗ y^{*} is obtained depends on whether ground-truth answers are available.

Math (DAPO-Math-17k). Ground-truth answers are available, so we directly use them as the privileged context y ∗ y^{*} to construct the self-conditioned teacher. To simulate varying teacher quality, we sample 500 questions and measure each external LLM’s accuracy; we then provide ground-truth to a corresponding fraction of training queries (matching that model’s coverage rate). Oracle provides ground truth to 100% of queries.

Code generation (LCB v6), AppWorld, and WebShop. No ground-truth solutions exist. We instead query each teacher LLM up to 3 times per query and retain any correct trajectory (verified by execution) as the demonstration τ \tau . Per-model coverage is reported in Table 5 .

#### Training Hyperparameters

All OPSD experiments use Qwen3-8B as the base model and train LoRA adapters with bfloat16 precision. Following ( Zhao et al., 2026 ) , we use LoRA rank r = 64 r=64 and scaling factor α = 128 \alpha=128 on all attention and MLP projection layers ( q_proj , k_proj , v_proj , o_proj , gate_proj , up_proj , and down_proj ). We optimize with learning rate 1 × 10 − 6 1\times 10^{-6} , gradient clipping at 1.0, per-device batch size 1, gradient accumulation 2, and 8 training processes, yielding an effective batch size of 16. For OPSD, we use a fixed teacher, β = 0 \beta=0 , λ = 1 \lambda=1 , temperature 1.0, top- p = 0.95 p=0.95 , and token-level JSD clipping threshold 0.05.

#### OPSD Prompt

The student prompt for each task follows that used in our main experiments. The teacher prompt injects a reference/answer block as privileged context. Below we show the teacher-specific prompt for each task type.

In all cases, the reference block is appended to the standard task prompt. The student never sees the reference block.

### B.3 OPD Details

To align with the settings in Li et al. (2026) , we use the same training and inference configurations as Li et al. (2026) in Figure 4 . See Table 6 for details. Due to computational resource constraints, we sample 3,600 examples for RL training, which corresponds to the 60 step performance reported in Li et al. (2026) .

### B.4 Analysis of Reinforce++

REINFORCE++ ( Hu et al., 2025 ) applies per-token credit assignment through discounted returns: G t = r t + γ ​ G t + 1 G_{t}=r_{t}+\gamma G_{t+1} . While competitive on short-horizon tasks (math, code), it collapses on long-horizon agentic tasks.

On AppWorld, validation performance peaked at 0.175@step40, then declined to 0.035@step101. On WebShop, performance dropped from 0.327 (base model) to 0.0@step80, with training reward also reaching 0.0 in the final steps.

The instability stems from gradient variance in long horizons. Early tokens accumulate returns from all subsequent tokens: G 1 = ∑ t = 1 T γ t − 1 ​ r t G_{1}=\sum_{t=1}^{T}\gamma^{t-1}r_{t} . With γ = 1.0 \gamma=1.0 and trajectories spanning hundreds of tokens, gradient variance grows exponentially. Combined with sparse episode-level rewards, advantage whitening fails to identify critical tokens, causing policy collapse.

In contrast, SC-GRPO uses trajectory-level GRPO advantages and applies token-level credit assignment only through KL-based gradient modulation, avoiding variance explosion in long-horizon settings.

## Appendix C Training Dynamics

### C.1 Training Dynamics on AIME 24 & 25

Figure 6 shows the validation performance throughout training on AIME 2024 and 2025. Both methods are trained on DAPO-Math-17k with identical hyperparameters and evaluated every 20 steps.

#### AIME 2024 (Top Row)

On Avg@8 (left), SC-GRPO establishes an early advantage and maintains it throughout training. Both methods exhibit some variance in the later stages of training, but SC-GRPO consistently stays above DAPO. On Pass@8 (right), the gap is more pronounced: SC-GRPO achieves 0.80 at step 280, while DAPO peaks at 0.72 around step 260 before declining slightly.

#### AIME 2025 (Bottom Row)

AIME 2025 is harder than AIME 2024, with both methods achieving lower absolute scores. On Avg@8 (left), SC-GRPO shows steady improvement throughout training, reaching 0.40 by step 500. The advantage is more consistent here than on AIME 2024, with less variance in the later stages. On Pass@8 (right), SC-GRPO maintains a 5-10% advantage throughout most of training, reaching 0.63 compared to DAPO’s 0.57.

#### Stability and convergence

Both methods exhibit training variance typical of RL with verifiable rewards, where validation performance fluctuates due to the discrete nature of the reward signal. However, SC-GRPO demonstrates more stable improvement on AIME 2025, the harder test set, suggesting that token-level credit assignment becomes increasingly valuable as problem difficulty increases. The consistent gap across both metrics and both test sets confirms that the gains are not due to overfitting to a particular evaluation protocol.

### C.2 Policy Entropy

Figure 7 shows the policy entropy throughout training. SC-GRPO maintains consistently higher entropy than DAPO across all training steps, with the gap widening after step 200. This suggests that SC-GRPO preserves exploration capacity: by selectively suppressing gradients on tokens where the student already matches the teacher and encouraging exploration when facing solve-none groups, SC-GRPO avoids premature convergence on the full trajectory. In contrast, DAPO’s uniform credit assignment drives the policy toward deterministic outputs more aggressively, reducing entropy and potentially limiting the model’s ability to explore alternative reasoning paths.

The entropy gap correlates with the performance advantage observed in Figure 6 : higher entropy enables the model to maintain diverse solution strategies, which is particularly valuable on harder problems (AIME 2025) where multiple reasoning approaches may be necessary to reach the correct answer.

### C.3 KL Weighting Function

Figure 8 illustrates why we use the 75th percentile of token-level KL divergence as the threshold c c in our weighting function. The function f ⁡ ( KL ) = KL / ( KL + c ) f(\text{KL})=\text{KL}/(\text{KL}+c) maps each token’s KL divergence to a weight between 0 and 1, which modulates the RL gradient for that token.

When c = p 25 c=p_{25} (orange curve), the threshold is near zero, so almost all tokens receive high weights ( f ⁡ ( KL ) ≈ 1 f(\text{KL})\approx 1 ), effectively reverting to uniform credit assignment. When c = p 90 c=p_{90} (red curve), the threshold is too high, causing many tokens with moderate KL divergence (0.05–0.15) to receive low weights, over-suppressing the gradient signal.

Our choice of c = p 75 c=p_{75} (blue curve) strikes a balance: tokens with KL below p 75 p_{75} (the bottom 75% of the distribution) receive weights below 0.5, indicating the student has already learned these tokens from the teacher. Only the top 25% of tokens, those with the highest KL divergence, receive weights above 0.5, preserving the RL gradient where the student and teacher genuinely differ. This adaptive threshold ensures that credit assignment focuses on critical difference tokens while avoiding both under-discrimination and over-suppression.

### C.4 KL Distribution Evolution

Figure 9 shows how the KL distribution evolves throughout training. The distribution exhibits a heavy-tailed structure: the bottom 75% of tokens (p25 to p75, dark blue region) have very low KL divergence, often near zero, indicating that the student policy has already learned to match the teacher on these tokens. Only the top 25% of tokens show significant divergence.

This distribution remains remarkably stable across training steps, with p75 fluctuating around 0.03–0.10 and p95 around 0.2–0.5. The stability validates our choice of using p75 as an adaptive threshold: it consistently identifies the boundary between learned tokens and critical difference tokens, regardless of training stage. The occasional spikes in the lower percentiles (visible as vertical streaks in the p25-p75 region) correspond to batches with particularly challenging problems where even common tokens require learning, but these are rare and do not affect the overall threshold selection.

## Appendix D Case Study: Token-Level KL Heatmap

Figure 10 shows the per-token KL distribution a real LiveCodeBench problem (counting the minimum number of edges to remove so that an undirected graph becomes a forest) . The student rollout o i o_{i} implements the standard Disjoint Set Union (DSU / Union-Find) approach, while the sampled verifier-approved trajectory τ \tau used to condition the teacher implements a stack-based Depth-First Search (DFS) over an adjacency list. Both solve the problem correctly, but follow distinct algorithmic paths.

Panels (a) show the sampled verifier-approved trajectory τ \tau that is injected into the teacher’s system prompt. Panel (b) shows the student rollout o i o_{i} , with each token shaded by its KL weight f t = D t / ( D t + c ) f_{t}=D_{t}/(D_{t}+c) . Near-white tokens correspond to positions where the student’s distribution is essentially unchanged by conditioning on τ \tau : the model would produce these tokens whether or not a verified solution was available. Deeply shaded tokens mark positions where τ \tau substantially redirects the next-token distribution, these are the tokens on which the GRPO update is preserved at full weight, while the near-white tokens are downweighted.

#### What tokens are selected

Most low-level scaffolding code (indentation, parentheses, simple variable assignments, generic loops) receives near-zero weight, since both DSU and DFS share these surface forms. The high-KL tokens concentrate at the points where the two algorithms genuinely diverge: the import of collections and the choice of stdin reader; the allocation of the DSU parent = list(range(N+1)) array (absent under DFS, which builds an adjacency list instead); the bodies of def find and def union , the merge predicate root_u != root_v , and the construction of the components set; and finally the closed-form answer answer = M - (N - K) . These are precisely the tokens whose choice distinguishes a DSU implementation from a DFS one, and on which a verified DFS trajectory shifts the student’s belief most strongly.

The pattern is consistent with the design intent of SC-GRPO: the self-teacher does not act as an additional supervision signal, it acts as a credit-assignment filter on the existing GRPO gradient. Sequence-level reward is preserved as the source of update direction, while gradient mass is concentrated on the small subset of tokens that actually carry the algorithmic decision.

## Appendix E Prompt Templates for SC-GRPO

### E.1 Prompt Construction

For a given problem instance, we construct student and teacher prompts as follows: The student prompt consists of a base system prompt followed by the problem specification. The teacher prompt extends this by concatenating three components: the base system prompt, the guide instruction, and the reference trajectory.

### E.2 LiveCodeBench Templates Example

We use LiveCodeBench as an example to illustrate our prompt templates. The same structure applies to other tasks (math and agentic tasks) with domain-specific guide instructions.

For math tasks (DAPO-Math-17K) and agentic tasks (AppWorld & Webshop), we use task-specific system prompts and guide instructions.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
