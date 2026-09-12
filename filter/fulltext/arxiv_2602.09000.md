##### Report GitHub Issue

Content selection saved. Describe the issue below:

# iGRPO: Self - Feedback–Driven LLM Reasoning

###### Abstract

Large Language Models (LLMs) have shown promise in solving complex mathematical problems, yet they still fall short of producing accurate and consistent solutions. Reinforcement Learning (RL) is a framework for aligning these models with task-specific rewards, improving overall quality and reliability. Group Relative Policy Optimization (GRPO) is an efficient, value-function-free alternative to Proximal Policy Optimization (PPO) that leverages group-relative reward normalization. We introduce Iterative Group Relative Policy Optimization (iGRPO), a two-stage extension of GRPO that adds dynamic self-conditioning through model-generated drafts. In Stage 1, iGRPO samples multiple exploratory drafts and selects the highest-reward draft using the same scalar reward signal used for optimization. In Stage 2, it appends this best draft to the original prompt and applies a GRPO-style update on draft-conditioned refinements, training the policy to improve beyond its strongest prior attempt. Under matched rollout budgets, iGRPO consistently outperforms GRPO across base models (e.g., Nemotron-H-8B-Base-8K and DeepSeek-R1 Distilled), validating its effectiveness on diverse reasoning benchmarks. Moreover, applying iGRPO to OpenReasoning-Nemotron-7B trained on AceReason-Math achieves new state-of-the-art results of 85.62% and 79.64% on AIME24 and AIME25, respectively. Ablations further show that the refinement wrapper generalizes beyond GRPO variants, benefits from a generative judge, and alters learning dynamics by delaying entropy collapse. These results underscore the potential of iterative, self-feedback-based RL for advancing verifiable mathematical reasoning.

\abscontent

## 1 Introduction

Reinforcement Learning (RL) has proven to be successful in improving reasoning capabilities of LLMs by optimizing against task-specific reward signals. Early successes in this direction include RL from Human Feedback (RLHF) for aligning LLMs with human intent, most notably in InstructGPT ( Ouyang et al., 2022 ) and ChatGPT ( Achiam et al., 2023 ) , which have demonstrated that incorporating preference-based rewards can dramatically improve both the usability and correctness of model outputs. Recently DeepSeek-R1 ( Guo et al., 2025 ) proposed a distinguishing feature which is the so-called zero configuration, wherein the RL process directly enhances the base language model. This breakthrough started several efforts which were targeted at replicating DeepSeek-R1’s methodology or refining its underlying RL mechanisms ( Zeng et al., 2025 ; Yu et al., 2025 ; Liu et al., 2025 ; Cui et al., 2025 ; Hu et al., 2025 ) .

Yet, in the realm of complex reasoning, RL algorithms typically do not incorporate any form of feedback or reflection on the model’s own outputs. Humans, by contrast, rarely solve nontrivial problems in a single pass: they often iterate on initial drafts, identify mistakes, and refine their solutions based on internal feedback ( Flower & Hayes, 1981 ; Simon, 2012 ; Braidotti, 2019 ; Flavell, 1979 ; Schön, 2017 ; Polya, 2014 ) . There is growing evidence that self-feedback mechanisms can bolster multi-step reasoning and the capacity to correct errors ( Madaan et al., 2023 ; Shinn et al., 2023 ) . However, existing RL frameworks do not capitalize on this iterative refinement process, leaving a critical gap between how humans naturally solve problems and how LLMs are typically trained to do so.

In this work, we propose to fill this gap with Iterative GRPO (iGRPO) which is a powerful extension of GRPO ( Shao et al., 2024 ) . As illustrated in Figure 1 , Our method operates in two stages. First, we draw multiple candidate completions from the model and compute their relative rewards via the group-based mechanism of GRPO. We then select the highest-scoring draft and this serves as the "first-draft" output of the model. We consider this highest-scoring response as a guide to improve the final output. Hence, it is provided as a self-feedback to the model. We feed it back to the model alongside the original prompt. By conditioning on this exemplar, the second stage encourages the model to refine and surpass its own best prior attempt. Notably, this design preserves the efficiency of GRPO while introducing only minimal extra overhead, as iGRPO still relies on the same set of group-based reward signals. In doing so, iGRPO offers a promising avenue for self-guided improvement, enabling LLMs to iteratively improve their reasoning capabilities.

We conduct a series of controlled experiments to compare iGRPO and GRPO under identical training conditions, using different base models trained on the Mathematics Aptitude Test of Heuristics (MATH) ( Hendrycks et al., 2021 ) dataset. Specifically, we evaluate DeepSeek-R1 Distilled ( Guo et al., 2025 ) and OpenMath-Nemotron ( Moshkov et al., 2025 ) on an extensive array of mathematical reasoning benchmarks, including AIME24 ( AI-MO, 2024a ) , AIME25 ( OpenCompass, 2025 ) , MATH500 ( Lightman et al., 2023 ) , AMC23 ( AI-MO, 2024b ) , GSM8K ( Cobbe et al., 2021 ) , and Minerva Math ( Lewkowycz et al., 2022 ) . For models with 7B and 14B parameters, iGRPO consistently outperforms standard GRPO. Moreover, by leveraging iGRPO algorithm with OpenReasoning-Nemotron-7B model ( NVIDIA, 2025 ) on the large-scale AceReason - Math ( Chen et al., 2025b ) dataset ( R1, 2024 ) , we push the state of the art on AIME24 and AIME25 to 85.62% and 79.64%, respectively. These findings underscore the effectiveness of incorporating a self-feedback stage into group-based RL optimization, particularly for complex mathematical reasoning tasks.

## 2 Related Work

##### RL for Reasoning.

Reinforcement learning (RL) has become an important tool for refining large language models on logical and analytical tasks ( Lambert et al., 2024 ) . Early self-improvement lines of work, such as STaR-style bootstrapping with verified outcomes and sampling-based selection (as discussed in ( Lambert et al., 2024 ) ), demonstrate that iteratively leveraging model-generated solutions can improve reasoning behavior. More recent systems scale outcome-driven training substantially ( Jaech et al., 2024 ) , and open-weight efforts such as DeepSeek-R1 report strong reasoning performance under similar training regimes ( Guo et al., 2025 ) . Beyond natural language tasks, RL on procedurally generated puzzles ( Xie et al., 2025 ) and settings with limited human demonstrations ( Wang et al., 2025 ) further highlight the breadth of RL as a mechanism for improving mathematical and logical reasoning.

##### GRPO and Variants.

There has also been rapid progress in refining and extending GRPO for large-scale LLM training. Dr. GRPO ( Liu et al., 2025 ) analyzes sources of bias in GRPO-style token-level objectives and proposes modifications such as removing divisions by sequence length and group-level standard deviation to better match unbiased policy gradients. DAPO ( Yu et al., 2025 ) targets long chain-of-thought training through dynamic sampling, decoupled clipping, and reward shaping designed to mitigate instability and reward noise. GSPO ( Zheng et al., 2025 ) instead operates at the sequence level, redefining importance ratios and applying sequence-level clipping to improve stability, especially in Mixture-of-Experts settings. Whereas these approaches primarily focus on stabilizing or correcting the underlying optimization objective, iGRPO is orthogonal: it introduces a two-stage mechanism that uses externally evaluated best drafts as additional training context, shaping the data distribution seen by the optimizer.

##### LLM Self-Learning and Self-Improvement.

LLM self-learning methods aim to improve a model by leveraging feedback signals produced by the model itself or by closely related agents. For example, SPIN and Self-Rewarding Language Models ( Chen et al., 2024 ; Yuan et al., 2024 ) use the model (or a closely coupled variant) as an internal evaluator to drive further learning. Other approaches incorporate self-play, verifier-based alignment, or proof-oriented training signals ( Kirchner et al., 2024 ; Ye et al., 2024 ) , though unreliable rewards can hinder complex reasoning ( Lambert et al., 2024 ) . More specialized self-play extensions, such as SPC ( Chen et al., 2025a ) and SPAG ( Cheng et al., 2024 ) , introduce curated tasks or adversarial scenarios to strengthen critique and robustness. Self-Verification ( Zhang et al., 2025a ) unifies problem-solving and generative verification within a single RL framework, enabling inference-time scaling by using the model’s own verification scores to reweight or aggregate sampled solutions. Critique-GRPO ( Zhang et al., 2025b ) augments GRPO with natural-language critiques by generating critique-conditioned refinements and optimizing over both initial answers and their refinements in an online RL loop. While these methods often blur the roles of reward provider and reward recipient within a single agent (or paired agents), iGRPO instead uses externally evaluated best-prior drafts as an in-context guide for subsequent generations during training. This maintains a clearer separation between the model’s generation process and the reward signal, while still leveraging the core self-improvement principle of learning from the model’s own outputs.

## 3 Methodology

### 3.1 Background: Group Relative Policy Optimization

GRPO is a value-function-free variant of proximal policy optimization that leverages group-based relative rewards for advantage estimation. Let π θ \pi_{\theta} denote the current policy and π θ old \pi_{\theta_{\text{old}}} the old policy. We begin with a pretrained language model ℳ \mathcal{M} and a set of training instances ℬ = { ( q , a ) } \mathcal{B}=\{(q,a)\} , where q q is a prompt (e.g., a math problem) and a a is a reference answer. Given a prompt q q , GRPO samples a group of G G candidate outputs { o 1 , o 2 , … , o G } \{o_{1},o_{2},\dots,o_{G}\} from π θ old \pi_{\theta_{\text{old}}} : o i ∼ π θ old ( ⋅ ∣ q ) for i = 1 , … , G . o_{i}\sim\pi_{\theta_{\text{old}}}(\cdot\mid q)\quad\text{for }i=1,\dots,G. A reward model then evaluates each sampled output o i o_{i} , resulting in scores { R 1 , … , R G } \{R_{1},\dots,R_{G}\} . GRPO normalizes these scores within the group to compute the advantage A ^ i , t \hat{A}_{i,t} at each token index t t of o i o_{i} : A ^ i , t = R i − mean ⁡ ( { R 1 , … , R G } ) std ⁡ ( { R 1 , … , R G } ) , \hat{A}_{i,t}\;=\;\frac{R_{i}\;-\;\mathrm{mean}(\{R_{1},\dots,R_{G}\})}{\mathrm{std}(\{R_{1},\dots,R_{G}\})}, where mean ⁡ ( ⋅ ) \mathrm{mean}(\cdot) and std ⁡ ( ⋅ ) \mathrm{std}(\cdot) denote the sample mean and sample standard deviation of the group’s reward scores. If std ⁡ ( { R 1 , … , R G } ) = 0 \mathrm{std}(\{R_{1},\dots,R_{G}\})=0 , we set the normalized advantages to 0 0 (equivalently, one may add a small constant δ \delta to the denominator); we apply the same convention in iGRPO. Note that all tokens t t in o i o_{i} share the same advantage A ^ i , t = A ^ i \hat{A}_{i,t}=\hat{A}_{i} , reflecting a single scalar reward for each sampled completion.

GRPO then updates the current policy π θ \pi_{\theta} by maximizing a clipped surrogate objective. Let r i , t ​ ( θ ) = π θ ​ ( o i , t ∣ q , o i , < t ) π θ old ​ ( o i , t ∣ q , o i , < t ) . r_{i,t}(\theta)\;=\;\frac{\pi_{\theta}(o_{i,t}\mid q,o_{i,<t})}{\pi_{\theta_{\text{old}}}(o_{i,t}\mid q,o_{i,<t})}.

Then the GRPO objective is: 𝒥 GRPO ​ ( θ ) = \displaystyle\mathcal{J}_{\text{GRPO}}(\theta)=\; 𝔼 ⁡ [ q ∼ P ⁡ ( Q ) , { o i } i = 1 G ∼ π θ old ] \displaystyle\mathbb{E}\Bigl[q\sim P(Q),\;\{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}\Bigr] × 1 G ​ ∑ i = 1 G 1 | o i | ​ ∑ t = 1 | o i | [ min ⁡ ( r i , t ​ ( θ ) ​ A ^ i , t , clip ⁡ ( r i , t ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ A ^ i , t ) − β ​ D ^ KL ( i , t ) ] , \displaystyle\times\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\Bigl[\min\!\Bigl(r_{i,t}(\theta)\,\hat{A}_{i,t},\;\mathrm{clip}\!\bigl(r_{i,t}(\theta),\;1-\epsilon,\;1+\epsilon\bigr)\,\hat{A}_{i,t}\Bigr)\;-\;\beta\,\widehat{D}_{\mathrm{KL}}^{(i,t)}\Bigr], (1) where ϵ \epsilon is the PPO clipping parameter, β \beta is a regularization coefficient on the KL divergence to a reference policy π ref \pi_{\text{ref}} , and | o i | |o_{i}| denotes the token length of completion o i o_{i} . We use the following non-negative per-token estimator D ^ KL ( i , t ) \widehat{D}_{\mathrm{KL}}^{(i,t)} as a practical KL penalty Schulman (2020) : D ^ KL ( i , t ) = π ref ​ ( o i , t ∣ q , o i , < t ) π θ ​ ( o i , t ∣ q , o i , < t ) − log ⁡ π ref ​ ( o i , t ∣ q , o i , < t ) π θ ​ ( o i , t ∣ q , o i , < t ) − 1 , \widehat{D}_{\mathrm{KL}}^{(i,t)}\;=\;\frac{\pi_{\text{ref}}(o_{i,t}\mid q,o_{i,<t})}{\pi_{\theta}(o_{i,t}\mid q,o_{i,<t})}\;-\;\log\!\frac{\pi_{\text{ref}}(o_{i,t}\mid q,o_{i,<t})}{\pi_{\theta}(o_{i,t}\mid q,o_{i,<t})}\;-\;1, which remains guaranteed to be non-negative. This estimator is unbiased for D KL ( π θ ∥ π ref ) D_{\mathrm{KL}}(\pi_{\theta}\,\|\,\pi_{\text{ref}}) when the expectation is taken under samples from π θ \pi_{\theta} , and it serves as a convenient sample-based penalty within PPO-style updates. By directly computing group-based advantages instead of estimating value functions, GRPO avoids the overhead of training a separate critic model, making it particularly appealing for large-scale language model fine-tuning.

### 3.2 Iterative Group Relative Policy Optimization

We introduce Iterative Group Relative Policy Optimization (iGRPO) , a reinforcement learning algorithm that implements bootstrapped policy improvement through dynamic self-conditioning. Unlike standard policy gradient methods that optimize single-shot generations, iGRPO establishes a closed-loop refinement process where the policy learns to systematically improve upon its own best attempts. The key insight is that by coupling exploration (Stage 1) with conditioned exploitation (Stage 2) within each optimization step, the model acquires a generalizable self-improvement capability that compounds in training.

#### 3.2.1 Motivation: From Static Examples to Dynamic Self-Conditioning

The standard GRPO objective (Eq. 1 ) treats each generation as independent, ignoring potentially valuable information from the model’s own generation process. In-context learning (ICL) addresses this by conditioning on fixed demonstrations: 𝒥 ICL ( θ ) = 𝔼 q ∼ P ⁡ ( Q ) [ 𝔼 o ∼ π θ ( ⋅ | q , e ) [ R ϕ ( o ) ] ] , \mathcal{J}_{\text{ICL}}(\theta)=\mathbb{E}_{q\sim P(Q)}\left[\mathbb{E}_{o\sim\pi_{\theta}(\cdot|q,e)}\left[R_{\phi}(o)\right]\right], where e e is a static example. However, ICL suffers from a fundamental limitation: the conditioning signal e e remains fixed throughout training and does not adapt to the evolving policy’s capabilities.

iGRPO introduces a different paradigm, dynamic self-conditioning , where the conditioning signal is generated by the policy itself and co-evolves with learning: 𝒥 iGRPO ​ ( θ ) \displaystyle\mathcal{J}_{\text{iGRPO}}(\theta) = 𝔼 q ∼ P ⁡ ( Q ) [ 𝔼 o ∼ π θ ( ⋅ ∣ q ′ θ ( q ) ) [ R ϕ ( o ) ] ] , \displaystyle=\mathbb{E}_{q\sim P(Q)}\!\left[\mathbb{E}_{o\sim\pi_{\theta}(\cdot\!\mid\!q^{\prime}_{\theta}(q))}\!\left[R_{\phi}(o)\right]\right], q θ ′ ​ ( q ) \displaystyle q^{\prime}_{\theta}(q) = Concat ⁡ ( q , d ^ θ ​ ( q ) ) \displaystyle=\mathrm{Concat}\!\bigl(q,\hat{d}_{\theta}(q)\bigr) where d ^ θ ​ ( q ) \hat{d}_{\theta}(q) is the best draft generated by the current policy (defined formally below). This creates a bootstrapped learning dynamic: as π θ \pi_{\theta} improves, so does the quality of d ^ θ \hat{d}_{\theta} , which in turn provides increasingly informative conditioning for subsequent generations.

Although the expressions above are written in terms of π θ \pi_{\theta} for clarity, iGRPO follows the PPO/GRPO convention for stable optimization. At each iteration, we take a snapshot π θ old \pi_{\theta_{\text{old}}} , sample both Stage 1 drafts and Stage 2 completions from π θ old \pi_{\theta_{\text{old}}} , and update θ \theta using importance ratios computed relative to π θ old \pi_{\theta_{\text{old}}} . Stage 1 is not differentiated through, but the distribution of selected drafts d ^ \hat{d} (and thus the self-conditioned prompts q ′ q^{\prime} ) shifts as θ \theta evolves across iterations. In addition, dynamic self-conditioning is used only during training. At inference time, we use the trained policy in the standard single-shot manner, generating directly from the original prompt q q without any draft generation, conditioning, or specialized selection scheme.

#### 3.2.2 Algorithmic Framework

iGRPO operates through two tightly coupled stages within each optimization step. Crucially, only Stage 2 outputs receive gradient updates, while Stage 1 serves as an adaptive exploration mechanism that shapes the optimization landscape.

##### Stage 1: Exploratory Draft Generation.

Given a prompt q q , we sample N N candidate drafts from the current policy snapshot: d i ∼ π θ old ( ⋅ ∣ q ) , i = 1 , … , N . d_{i}\sim\pi_{\theta_{\text{old}}}(\cdot\mid q),\quad i=1,\ldots,N. Each draft is evaluated using a reward function R ϕ R_{\phi} , and we identify the highest-scoring draft: d ^ = arg ⁡ max i ∈ { 1 , … , N } ​ R ϕ ​ ( d i ) . \hat{d}=\arg\max_{i\in\{1,\ldots,N\}}R_{\phi}(d_{i}). (2) This stage performs implicit curriculum generation : early in training, d ^ \hat{d} may be a weak solution, but as the policy improves, d ^ \hat{d} increasingly represents a high-quality attempt that approaches (but does not yet reach) optimal performance.

##### Stage 2: Conditioned Refinement.

We form an augmented prompt by appending the best draft immediately after the original prompt: q ′ = Concat ​ ( q , d ^ ) . q^{\prime}=\text{Concat}(q,\hat{d}). (3) We then sample a group of G G completions, mirroring the standard GRPO sampling: o j ∼ π θ old ( ⋅ ∣ q ′ ) , j = 1 , … , G . o_{j}\sim\pi_{\theta_{\text{old}}}(\cdot\mid q^{\prime}),\quad j=1,\ldots,G. These completions are scored, and GRPO-style advantage estimation and policy updates are applied exclusively to these Stage 2 outputs. In practice, the concatenation in Eq. 3 uses a fixed prompt template, which we provide in the supplementary materials.

#### 3.2.3 Theoretical Analysis: Bootstrapped Policy Improvement

###### Definition 1 (Self-Conditioned Prompt Construction) .

Given a prompt q q and policy π θ \pi_{\theta} , sample N N drafts d i ∼ π θ ( ⋅ ∣ q ) , i = 1 , … , N , d_{i}\sim\pi_{\theta}(\cdot\mid q),\quad i=1,\ldots,N, and select the best draft d ^ θ ​ ( q ) = arg ⁡ max i ∈ { 1 , … , N } ​ R ϕ ​ ( d i ) . \hat{d}_{\theta}(q)=\arg\max_{i\in\{1,\ldots,N\}}R_{\phi}(d_{i}). We then define the self-conditioned prompt by appending the best draft immediately after the original prompt: q θ ′ ​ ( q ) = Concat ​ ( q , d ^ θ ​ ( q ) ) . q^{\prime}_{\theta}(q)=\text{Concat}\bigl(q,\hat{d}_{\theta}(q)\bigr).

Unlike static ICL where the conditioning is independent of θ \theta , iGRPO’s conditioning is policy-dependent : the constructed prompt q θ ′ ​ ( q ) q^{\prime}_{\theta}(q) changes as θ \theta changes, since d ^ θ ​ ( q ) \hat{d}_{\theta}(q) is generated by π θ \pi_{\theta} . This creates a coupled dynamical system.

###### Proposition 3.1 (Progressive Conditioning Quality for Binary Rewards) .

Assume the reward is binary, R ϕ ​ ( o ) ∈ { 0 , 1 } R_{\phi}(o)\in\{0,1\} , and Stage 1 drafts { d i } i = 1 N \{d_{i}\}_{i=1}^{N} are sampled i.i.d. from π θ ( ⋅ | q ) \pi_{\theta}(\cdot|q) . Let V θ ( q ) = 𝔼 o ∼ π θ ( ⋅ | q ) [ R ϕ ( o ) ] V_{\theta}(q)=\mathbb{E}_{o\sim\pi_{\theta}(\cdot|q)}[R_{\phi}(o)] denote the expected reward under policy π θ \pi_{\theta} , which equals the success probability p θ ( q ) = Pr [ R ϕ ( o ) = 1 ] p_{\theta}(q)=\Pr[R_{\phi}(o)=1] in the binary case. Then the expected reward of the selected best draft d ^ θ ​ ( q ) = arg ⁡ max i ​ R ϕ ​ ( d i ) \hat{d}_{\theta}(q)=\arg\max_{i}R_{\phi}(d_{i}) satisfies 𝔼 ⁡ [ R ϕ ​ ( d ^ θ ​ ( q ) ) ] = 1 − ( 1 − V θ ​ ( q ) ) N , \mathbb{E}\bigl[R_{\phi}(\hat{d}_{\theta}(q))\bigr]=1-(1-V_{\theta}(q))^{N}, which is monotonically increasing in V θ ​ ( q ) V_{\theta}(q) . Consequently, if optimization increases V θ ​ ( q ) V_{\theta}(q) , then 𝔼 ⁡ [ R ϕ ​ ( d ^ θ ​ ( q ) ) ] \mathbb{E}[R_{\phi}(\hat{d}_{\theta}(q))] also increases, improving the conditioning quality for subsequent iterations in expectation.

###### Proof.

For binary rewards, R ϕ ​ ( d ^ θ ​ ( q ) ) = 1 R_{\phi}(\hat{d}_{\theta}(q))=1 if and only if at least one of the N N sampled drafts achieves reward 1 1 . Under i.i.d. sampling, this occurs with probability 1 − Pr ⁡ [ ∀ i , R ϕ ​ ( d i ) = 0 ] = 1 − ( 1 − V θ ​ ( q ) ) N . 1-\Pr\bigl[\forall i,\;R_{\phi}(d_{i})=0\bigr]=1-(1-V_{\theta}(q))^{N}. Since R ϕ ​ ( d ^ θ ​ ( q ) ) ∈ { 0 , 1 } R_{\phi}(\hat{d}_{\theta}(q))\in\{0,1\} , its expectation equals this probability. The function 1 − ( 1 − x ) N 1-(1-x)^{N} is increasing in x ∈ [ 0 , 1 ] x\in[0,1] , establishing monotonicity in V θ ​ ( q ) V_{\theta}(q) . ∎

This proposition captures the bootstrapping effect : better policies generate better drafts, which provide more informative conditioning, which enables learning better policies. The model does not merely learn to copy the conditioning; it learns a refinement function that maps draft attempts to improved solutions.

#### 3.2.4 Mathematical Formulation

Building on the GRPO objective in Eq. 1 , we present the complete iGRPO formulation. Let π θ \pi_{\theta} denote the policy being optimized, with π θ old \pi_{\theta_{\text{old}}} representing the policy snapshot at the start of each iteration for importance sampling.

##### Stage 1: Draft Selection.

For each prompt q q , Stage 1 samples N N drafts and selects the best: { d 1 , … , d N } ∼ π θ old ( ⋅ ∣ q ) , d ^ = arg max i ∈ { 1 , … , N } R ϕ ( d i ) . \{d_{1},\ldots,d_{N}\}\sim\pi_{\theta_{\text{old}}}(\cdot\mid q),\qquad\hat{d}=\arg\max_{i\in\{1,\ldots,N\}}R_{\phi}(d_{i}).

##### Stage 2: Conditioned Generation and Advantage Computation.

We form the augmented prompt by appending the selected draft to q q (Eq. 3 ) and sample G G completions: { o 1 , … , o G } ∼ π θ old ( ⋅ ∣ q ′ ) . \{o_{1},\ldots,o_{G}\}\sim\pi_{\theta_{\text{old}}}(\cdot\mid q^{\prime}). Each completion o j o_{j} receives a reward R ϕ ​ ( o j ) R_{\phi}(o_{j}) , and advantages are computed via group normalization as in standard GRPO: A ^ j = R ϕ ​ ( o j ) − mean ⁡ ( { R ϕ ​ ( o 1 ) , … , R ϕ ​ ( o G ) } ) std ⁡ ( { R ϕ ​ ( o 1 ) , … , R ϕ ​ ( o G ) } ) . \hat{A}_{j}=\frac{R_{\phi}(o_{j})-\mathrm{mean}(\{R_{\phi}(o_{1}),\ldots,R_{\phi}(o_{G})\})}{\mathrm{std}(\{R_{\phi}(o_{1}),\ldots,R_{\phi}(o_{G})\})}. (4) If std ⁡ ( { R ϕ ​ ( o 1 ) , … , R ϕ ​ ( o G ) } ) = 0 \mathrm{std}(\{R_{\phi}(o_{1}),\ldots,R_{\phi}(o_{G})\})=0 , we set the normalized advantages to 0 0 (equivalently, one may add a small constant δ \delta to the denominator). All tokens t t in o j o_{j} share the same advantage A ^ j , t = A ^ j \hat{A}_{j,t}=\hat{A}_{j} , consistent with the GRPO formulation.

##### Full Objective.

The complete iGRPO objective combines both stages: 𝒥 iGRPO ​ ( θ ) \displaystyle\mathcal{J}_{\text{iGRPO}}(\theta) = 𝔼 [ q ∼ P ( Q ) ] 𝔼 [ { d i } i = 1 N ∼ π θ old ( ⋅ ∣ q ) ⏟ Stage 1 , d ^ = arg max i R ϕ ( d i ) , q ′ = Concat ( q , d ^ ) , { o j } j = 1 G ∼ π θ old ( ⋅ ∣ q ′ ) ⏟ Stage 2 ] \displaystyle=\mathbb{E}\Bigl[q\sim P(Q)\Bigr]\;\mathbb{E}\Bigl[\underbrace{\{d_{i}\}_{i=1}^{N}\sim\pi_{\theta_{\text{old}}}(\cdot\mid q)}_{\text{Stage 1}},\;\hat{d}=\arg\max_{i}R_{\phi}(d_{i}),\;q^{\prime}=\mathrm{Concat}(q,\hat{d}),\;\underbrace{\{o_{j}\}_{j=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot\mid q^{\prime})}_{\text{Stage 2}}\Bigr] × 1 G ​ ∑ j = 1 G 1 | o j | ​ ∑ t = 1 | o j | [ min ⁡ ( r j , t ​ ( θ ) ​ A ^ j , clip ⁡ ( r j , t ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ A ^ j ) − β ​ D ^ KL ( j , t ) ] , \displaystyle\quad\times\frac{1}{G}\sum_{j=1}^{G}\frac{1}{|o_{j}|}\sum_{t=1}^{|o_{j}|}\Bigl[\min\!\Bigl(r_{j,t}(\theta)\,\hat{A}_{j},\;\mathrm{clip}\!\bigl(r_{j,t}(\theta),\,1-\epsilon,\,1+\epsilon\bigr)\,\hat{A}_{j}\Bigr)\;-\;\beta\,\widehat{D}_{\mathrm{KL}}^{(j,t)}\Bigr], (5) where the importance sampling ratio is computed with respect to the augmented prompt: r j , t ​ ( θ ) = π θ ​ ( o j , t ∣ q ′ , o j , < t ) π θ old ​ ( o j , t ∣ q ′ , o j , < t ) , r_{j,t}(\theta)=\frac{\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t})}{\pi_{\theta_{\text{old}}}(o_{j,t}\mid q^{\prime},o_{j,<t})}, and we use the same non-negative per-token KL penalty as in Section 3.1 , computed under the augmented prompt: D ^ KL ( j , t ) = π ref ​ ( o j , t ∣ q ′ , o j , < t ) π θ ​ ( o j , t ∣ q ′ , o j , < t ) − log ⁡ π ref ​ ( o j , t ∣ q ′ , o j , < t ) π θ ​ ( o j , t ∣ q ′ , o j , < t ) − 1 . \widehat{D}_{\mathrm{KL}}^{(j,t)}=\frac{\pi_{\text{ref}}(o_{j,t}\mid q^{\prime},o_{j,<t})}{\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t})}-\log\frac{\pi_{\text{ref}}(o_{j,t}\mid q^{\prime},o_{j,<t})}{\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t})}-1. The key structural difference from vanilla GRPO (Eq. 1 ) is that all Stage 2 completions are conditioned on the augmented prompt q ′ q^{\prime} , formed by appending the best Stage 1 draft immediately after the original prompt q q . This provides a self-feedback signal that encourages the policy to refine its solutions beyond its strongest initial attempt.

##### Reward Function.

Following standard practice for verifiable reasoning tasks, we employ a rule-based reward function: R ϕ ( o ) = 𝟏 [ extract ( o ) = a ] , R_{\phi}(o)=\mathbf{1}\left[\texttt{extract}(o)=a\right], (6) where extract ​ ( ⋅ ) \texttt{extract}(\cdot) parses the final answer from the completion and a a is the ground-truth reference answer from the training instance ( q , a ) ∈ ℬ (q,a)\in\mathcal{B} . This binary reward, combined with group normalization (Eq. 4 ), provides sufficient signal for distinguishing solution quality within each prompt group. The complete iGRPO procedure is presented in Algorithm 1 .

#### 3.2.5 Computational Analysis

Although iGRPO uses two stages, its compute is primarily controlled by the total number of sampled completions per prompt. With a fixed sampling budget, iGRPO can be run at essentially the same dominant generation cost as GRPO.

Let C gen C_{\text{gen}} denote the cost of producing one sampled completion (including prompt encoding, autoregressive decoding, and reward evaluation). Let G GRPO G_{\text{GRPO}} denote the number of completions sampled per prompt in standard GRPO.

##### Baseline GRPO Cost.

Standard GRPO samples G GRPO G_{\text{GRPO}} completions per prompt, giving per-prompt rollout cost C GRPO ≈ G GRPO ​ C gen . C_{\text{GRPO}}\;\approx\;G_{\text{GRPO}}\,C_{\text{gen}}.

##### iGRPO Rollout Cost.

iGRPO samples N N Stage 1 drafts and G G Stage 2 refinements per prompt (Section 3.2 ), so C iGRPO ≈ ( N + G ) ​ C gen , C iGRPO C GRPO = N + G G GRPO . C_{\text{iGRPO}}\;\approx\;(N+G)\,C_{\text{gen}},\qquad\frac{C_{\text{iGRPO}}}{C_{\text{GRPO}}}\;=\;\frac{N+G}{G_{\text{GRPO}}}. In our experiments, we keep the sampling budget fixed by setting N + G = G GRPO , N+G\;=\;G_{\text{GRPO}}, so iGRPO redistributes the same number of rollouts across Stage 1 and Stage 2 rather than increasing them. For example, with G GRPO = 16 G_{\text{GRPO}}=16 in GRPO, we use N = 8 N=8 and G = 8 G=8 in iGRPO, yielding C iGRPO ≈ ( N + G ) ​ C gen = G GRPO ​ C gen ≈ C GRPO , C_{\text{iGRPO}}\;\approx\;(N+G)\,C_{\text{gen}}\;=\;G_{\text{GRPO}}\,C_{\text{gen}}\;\approx\;C_{\text{GRPO}}, i.e., the dominant generation cost is comparable to GRPO.

## 4 Experiments

### 4.1 Setup

Our training data includes two datasets: MATH ( Hendrycks et al., 2021 ) (7,500 step-by-step competition problems) and AceReason-Math ( Chen et al., 2025b ) (9,400 problems). All models are trained for one epoch, with a KL divergence loss coefficient of 0 and no entropy regularization. We use a learning rate of 1 × 10 − 6 1\times 10^{-6} with a cosine schedule, generating eight completions per prompt (halved in each stage for iGRPO). The maximum prompt length is 1,024 tokens across all datasets. For all experiments, the completion length is capped at 4,096 tokens and the batch size at 1024. We evaluate model performance on well-known mathematical benchmarks, including AIME24/AIME25, MATH500, AMC23, GSM8K, and Minerva Math. For all benchmarks we report Pass@1 accuracy. However, for AIME24/AIME25 the reported value is averaged over 64 runs to ensure robustness. For other benchmarks, an average of 8 runs are reported. For evaluations, we use NeMo-Skills framework 1 1 1 https://github.com/NVIDIA/NeMo-Skills with decoding parameters such as a temperature of 0.6, top-p of 0.95, and generation length of 65,000. Additional training and evaluation details are provided in the supplementary materials.

### 4.2 Results

Our goal in this section is to isolate the practical benefit of adding a self-feedback refinement stage to GRPO. Concretely, we ask whether the two-stage training signal in iGRPO translates into better verifiable mathematical reasoning, and whether those gains persist across model families and scales.

##### Controlled study with matched sampling budget.

Table 1 compares iGRPO against vanilla GRPO and two recent self-improvement baselines, Self-Verification ( Zhang et al., 2025a ) and Critique-GRPO ( Zhang et al., 2025b ) , across model families and parameter scales (7B, 8B, 14B). All methods share the same training protocol and the same rule-based reward (Eq. 6 ). To ensure a fair compute comparison, we keep the total sampling budget fixed at eight completions per prompt for every method; iGRPO redistributes this budget across stages by using Stage 1 drafts to select self-feedback and Stage 2 completions to perform the GRPO-style update. As a result, differences in Table 1 reflect the effect of conditioning on the best draft rather than the effect of more sampling.

##### Generalist 8B model: the largest gains from self-feedback.

For Nemotron-H-8B-Base-8K , vanilla GRPO raises the macro-average from 29.65 % 29.65\% to 41.08 % 41.08\% . Self-Verification and Critique-GRPO further improve the average to 42.86 % 42.86\% and 43.39 % 43.39\% . iGRPO performs best at 45.04 % 45.04\% , which is +3.96 points over GRPO and +1.65 points over the strongest self-improvement baseline. The improvements are most visible on the benchmarks that most strongly penalize near-miss reasoning, including AIME25 ( 9.17 % 9.17\% ) and Minerva ( 32.72 % 32.72\% ), and iGRPO also reaches the highest GSM8K accuracy ( 91.26 % 91.26\% ). This is a setting where avoiding additional self-judgment tasks matters: iGRPO does not require the model to generate critiques or verification rationales; it provides the best draft as a direct, high-signal scaffold and trains the policy to refine beyond it.

##### Stronger 7B distilled reasoner: consistent gains concentrated on multi-step tasks.

For DeepSeek-R1-Distill-Qwen-7B , the base model is already strong ( 61.93 % 61.93\% average), and GRPO improves it to 68.29 % 68.29\% . Self-Verification and Critique-GRPO reach 69.08 % 69.08\% and 69.14 % 69.14\% . iGRPO remains best overall at 69.87 % 69.87\% . The gains concentrate on multi-step benchmarks where a mostly-correct attempt can fail due to a small late error (e.g., AIME24 at 56.30 % 56.30\% and AMC at 95.00 % 95.00\% ). This pattern fits the iGRPO mechanism: Stage 1 increases the chance that a strong reasoning trajectory appears in the context, and Stage 2 learns to reliably “finish the job” under the same verifiable reward.

##### Math-specialized 7B model: improvements persist when the base is already strong.

For OpenMath-Nemotron-7B , the base model starts at 74.83 % 74.83\% average. GRPO yields a small change to 75.02 % 75.02\% , suggesting limited headroom from standard one-shot RL updates in this regime. iGRPO increases performance to 76.07 % 76.07\% , with the most notable gains on the harder benchmarks, including AIME24 (from 73.28 % 73.28\% to 74.79 % 74.79\% ) and AMC (from 95.00 % 95.00\% to 97.50 % 97.50\% ). When drafts are already high-quality, the value of iGRPO is less about discovering a viable solution mode and more about systematically reinforcing the most reliable completion patterns.

##### Scaling to 14B parameters: benefits persist on complex reasoning.

At the 14B scale, iGRPO continues to improve on GRPO across both model families. For DeepSeek-R1-Distill-Qwen-14B , the macro-average increases from 71.29 % 71.29\% (GRPO) to 73.02 % 73.02\% (iGRPO), with a large gain on AIME24 from 60.26 % 60.26\% to 64.06 % 64.06\% . For OpenMath-Nemotron-14B , the macro-average improves from 76.73 % 76.73\% (GRPO) to 78.00 % 78.00\% (iGRPO), including gains on AIME25 from 64.53 % 64.53\% to 65.57 % 65.57\% and on AIME24 from 74.79 % 74.79\% to 76.72 % 76.72\% . While margins naturally shrink as models become stronger, the improvement pattern remains stable: iGRPO helps larger models correct residual errors that survive strong pretraining and standard RL fine-tuning, especially on long-horizon competition benchmarks.

##### Competitiveness against critique-style objectives.

Self-Verification and Critique-GRPO are strong baselines, but they ask the model to allocate capacity to additional behaviors (verifying, critiquing, or producing auxiliary text) that are only indirectly optimized by the outcome reward. iGRPO keeps the training loop tightly aligned with the verifiable objective while still capturing the benefit of iteration: Stage 1 supplies a high-quality draft as an explicit conditioning signal, and Stage 2 directly optimizes a refinement policy that can surpass that draft. Empirically, this design yields consistent improvements across model families and scales, with the strongest gains on benchmarks that are sensitive to small long-horizon reasoning mistakes.

### 4.3 Generalization to a Stronger Base and Harder Dataset

All prior controlled comparisons were trained on the 7,500-problem MATH set. We

next evaluate iGRPO in a harder regime by both strengthening the initialization and shifting to a more challenging training distribution. We start from OpenReasoning-Nemotron-7B and train on AceReason-Math ( Chen et al., 2025b ) , keeping the iGRPO configuration identical to Section 4 ; Figure 2 summarizes the results. iGRPO improves performance across all benchmarks, with the strongest gains on AIME24/25 ( +1.52 / +1.78 ) and clear transfer beyond math to GPQA ( +1.84 ) and MMLU-Pro ( +0.91 ), yielding a +1.23 overall average improvement. This indicates iGRPO remains effective with a stronger base model and harder training data, and that iterative self-feedback improves broadly useful refinement behaviors rather than only math-specific patterns.

## 5 Ablation

##### Beyond GRPO: self-feedback as a reusable refinement wrapper.

Our two-stage procedure is not tied to the GRPO objective itself: it can be layered on top of other group-based PPO variants by using Stage 1 to select a high-reward draft and Stage 2 to perform the base optimizer’s update on self-conditioned prompts. Table 2 applies this wrapper to DAPO and GSPO under matched rollout budgets (same total sampled completions per prompt, same reward, and identical training and evaluation settings). In both cases, self-feedback yields a consistent +1.1 to +1.2 macro-average improvement, indicating that the gains primarily stem from the refinement interface rather than GRPO-specific details.

##### Generative judge study.

Because iGRPO only needs a scalar reward to (i) rank Stage 1 drafts and (ii) compute Stage 2 group-normalized advantages, we can swap the binary outcome checker (Eq. 6 ) for a generative judge. On DeepSeek-R1-Distill-Qwen-7B trained on MATH, GPT-5 scoring each solution in [ 0 , 1 ] [0,1] improves Pass@1 on all six benchmarks and increases the average from 69.87 to 70.81 ( +0.94 ; Table 3 ). The largest gains on AIME24/25 and Minerva are consistent with partial credit for near-miss traces, which lets them survive Stage 1 selection and be refined into correct answers in Stage 2.

##### Entropy analysis.

To probe how self-feedback alters learning dynamics, we track the per-token Shannon entropy of the policy during RL. For a decoding step t t with context h t h_{t} and vocabulary 𝒱 \mathcal{V} , we measure entropy in nats as ℋ ( π θ ( ⋅ ∣ h t ) ) = − ∑ w ∈ 𝒱 π θ ( w ∣ h t ) ln π θ ( w ∣ h t ) , \mathcal{H}\bigl(\pi_{\theta}(\cdot\mid h_{t})\bigr)=-\sum_{w\in\mathcal{V}}\pi_{\theta}(w\mid h_{t})\,\ln\pi_{\theta}(w\mid h_{t}), (7) and in practice compute it from the log-softmax of the logits (base e e ), then average over all valid completion tokens in the batch to obtain a single scalar per training step. On DeepSeek-R1-Distill-Qwen-7B trained on MATH, both methods start at 2.45 2.45 nats, but GRPO collapses rapidly ( 0.60 0.60 at 10 % 10\% , 0.42 0.42 by 30 % 30\% ) and then stays flat through the end. In contrast, iGRPO decays more gradually ( 0.80 0.80 at 15 % 15\% , 0.48 0.48 at 30 % 30\% ) and remains slightly higher through mid-training ( 0.46 0.46 at 60 % 60\% ) before converging near GRPO ( 0.44 0.44 vs. 0.42 0.42 at 100 % 100\% ). This suggests iGRPO delays premature mode collapse: conditioning on the best draft encourages refinement around a strong scaffold while preserving alternative continuations long enough to recover from near-miss reasoning traces. Since final entropies are close, the gains are better explained by sustained mid-training exploration rather than higher randomness at convergence.

## 6 Conclusion

We introduced Iterative Group Relative Policy Optimization (iGRPO) , a simple and effective extension of GRPO that injects an explicit self-feedback signal into outcome-driven RL for reasoning. iGRPO replaces single-shot optimization with a two-stage loop: Stage 1 samples multiple drafts and selects the highest-reward completion as feedback; Stage 2 conditions on this best draft and applies a standard GRPO-style update on refinements. This yields dynamic self-conditioning : the training context automatically improves as the policy improves, creating a bootstrapped refinement behavior that is absent from conventional group-based objectives. We also provided a clean theoretical characterization of the bootstrapping effect under binary rewards, showing that the expected quality of the selected draft increases monotonically with the policy’s success probability.

Empirically, iGRPO consistently improves verifiable math reasoning across model families and scales under matched rollout budgets. Across 7B, 8B, and 14B backbones, iGRPO outperforms vanilla GRPO as well as strong self-improvement baselines that rely on critique or verification behaviors (Table 1 ). In a harder generalization setting, training OpenReasoning-Nemotron-7B on AceReason-Math with iGRPO yields new best results on AIME24/AIME25 (85.62%/79.64%) and transfers gains beyond math to GPQA and MMLU-Pro (Figure 2 ). Our ablations further suggest that the benefit primarily comes from the refinement interface itself: the same two-stage wrapper improves other group-based PPO variants (Table 2 ), remains compatible with richer scalar rewards such as a generative judge (Table 3 ), and measurably alters learning dynamics by delaying premature entropy collapse (Figure 3 ).

## References

Achiam et al. (2023) Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 , 2023.

AI-MO (2024a) AI-MO. Aimo validation aime dataset. https://huggingface.co/datasets/AI-MO/aimo-validation-aime , 2024a.

AI-MO (2024b) AI-MO. Aimo validation amc dataset. https://huggingface.co/datasets/AI-MO/aimo-validation-amc , 2024b.

Braidotti (2019) Rosi Braidotti. A theoretical framework for the critical posthumanities. Theory, culture & society , 36(6):31–61, 2019.

Chen et al. (2025a) Jiaqi Chen, Bang Zhang, Ruotian Ma, Peisong Wang, Xiaodan Liang, Zhaopeng Tu, Xiaolong Li, and Kwan-Yee K. Wong. Spc: Evolving self-play critic via adversarial games for llm reasoning, 2025a. URL https://arxiv.org/abs/2504.19162 .

Chen et al. (2025b) Yang Chen, Zhuolin Yang, Zihan Liu, Chankyu Lee, Peng Xu, Mohammad Shoeybi, Bryan Catanzaro, and Wei Ping. Acereason-nemotron: Advancing math and code reasoning through reinforcement learning. arXiv preprint arXiv:2505.16400 , 2025b.

Chen et al. (2024) Zixiang Chen, Yihe Deng, Huizhuo Yuan, Kaixuan Ji, and Quanquan Gu. Self-play fine-tuning converts weak language models to strong language models. In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024 . OpenReview.net, 2024. URL https://openreview.net/forum?id=O4cHTxW9BS .

Cheng et al. (2024) Pengyu Cheng, Tianhao Hu, Han Xu, Zhisong Zhang, Yong Dai, Lei Han, Nan Du, and Xiaolong Li. Self-playing adversarial language game enhances LLM reasoning. In Amir Globersons, Lester Mackey, Danielle Belgrave, Angela Fan, Ulrich Paquet, Jakub M. Tomczak, and Cheng Zhang (eds.), Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024 , 2024.

Cobbe et al. (2021) Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168 , 2021.

Cui et al. (2025) Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, Jiarui Yuan, Huayu Chen, Kaiyan Zhang, Xingtai Lv, Shuo Wang, Yuan Yao, Xu Han, Hao Peng, Yu Cheng, Zhiyuan Liu, Maosong Sun, Bowen Zhou, and Ning Ding. Process reinforcement through implicit rewards. CoRR , abs/2502.01456, 2025. 10.48550/ARXIV.2502.01456 . URL https://doi.org/10.48550/arXiv.2502.01456 .

Flavell (1979) John H Flavell. Metacognition and cognitive monitoring: A new area of cognitive–developmental inquiry. American psychologist , 34(10):906, 1979.

Flower & Hayes (1981) Linda Flower and John R Hayes. A cognitive process theory of writing. College Composition & Communication , 32(4):365–387, 1981.

Guo et al. (2025) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. arXiv preprint arXiv:2501.12948 , 2025.

Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874 , 2021.

Hu et al. (2025) Jingcheng Hu, Yinmin Zhang, Qi Han, Daxin Jiang, Xiangyu Zhang, and Heung-Yeung Shum. Open-reasoner-zero: An open source approach to scaling up reinforcement learning on the base model. CoRR , abs/2503.24290, 2025. 10.48550/ARXIV.2503.24290 . URL https://doi.org/10.48550/arXiv.2503.24290 .

Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. arXiv preprint arXiv:2412.16720 , 2024.

Kirchner et al. (2024) Jan Hendrik Kirchner, Yining Chen, Harri Edwards, Jan Leike, Nat McAleese, and Yuri Burda. Prover-verifier games improve legibility of LLM outputs. CoRR , abs/2407.13692, 2024. 10.48550/ARXIV.2407.13692 . URL https://doi.org/10.48550/arXiv.2407.13692 .

Lambert et al. (2024) Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James V. Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, Yuling Gu, Saumya Malik, Victoria Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Bras, Oyvind Tafjord, Chris Wilhelm, Luca Soldaini, Noah A. Smith, Yizhong Wang, Pradeep Dasigi, and Hannaneh Hajishirzi. Tülu 3: Pushing frontiers in open language model post-training. CoRR , abs/2411.15124, 2024. 10.48550/ARXIV.2411.15124 . URL https://doi.org/10.48550/arXiv.2411.15124 .

Lewkowycz et al. (2022) Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, et al. Solving quantitative reasoning problems with language models. Advances in Neural Information Processing Systems , 35:3843–3857, 2022.

Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In The Twelfth International Conference on Learning Representations , 2023.

Liu et al. (2025) Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. Understanding r1-zero-like training: A critical perspective. CoRR , abs/2503.20783, 2025. 10.48550/ARXIV.2503.20783 . URL https://doi.org/10.48550/arXiv.2503.20783 .

Madaan et al. (2023) Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. Advances in Neural Information Processing Systems , 36:46534–46594, 2023.

Moshkov et al. (2025) Ivan Moshkov, Darragh Hanley, Ivan Sorokin, Shubham Toshniwal, Christof Henkel, Benedikt Schifferer, Wei Du, and Igor Gitman. Aimo-2 winning solution: Building state-of-the-art mathematical reasoning models with openmathreasoning dataset. arXiv preprint arXiv:2504.16891 , 2025.

NVIDIA (2025) NVIDIA. Openreasoning-nemotron-7b. https://huggingface.co/nvidia/OpenReasoning-Nemotron-7B , 2025.

OpenCompass (2025) OpenCompass. Aime2025. https://huggingface.co/datasets/opencompass/AIME2025 , 2025. MIT License.

Ouyang et al. (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. Advances in neural information processing systems , 35:27730–27744, 2022.

Polya (2014) George Polya. How to solve it: A new aspect of mathematical method. In How to solve it . Princeton university press, 2014.

R1 (2024) Open R1. Openr1-math-220k. https://huggingface.co/datasets/open-r1/OpenR1-Math-220k , 2024.

Schön (2017) Donald A Schön. The reflective practitioner: How professionals think in action . Routledge, 2017.

Schulman (2020) John Schulman. Approximating kl divergence, 2020. URL http://joschu.net/blog/kl-approx.html .

Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. DeepseekMath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

Shinn et al. (2023) Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning. Advances in Neural Information Processing Systems , 36:8634–8652, 2023.

Simon (2012) Herbert A Simon. The architecture of complexity. In The Roots of Logistics , pp. 335–361. Springer, 2012.

Wang et al. (2025) Yiping Wang, Qing Yang, Zhiyuan Zeng, Liliang Ren, Lucas Liu, Baolin Peng, Hao Cheng, Xuehai He, Kuan Wang, Jianfeng Gao, Weizhu Chen, Shuohang Wang, Simon Shaolei Du, and Yelong Shen. Reinforcement learning for reasoning in large language models with one training example, 2025. URL https://arxiv.org/abs/2504.20571 .

Xie et al. (2025) Tian Xie, Zitian Gao, Qingnan Ren, Haoming Luo, Yuqian Hong, Bryan Dai, Joey Zhou, Kai Qiu, Zhirong Wu, and Chong Luo. Logic-rl: Unleashing LLM reasoning with rule-based reinforcement learning. CoRR , abs/2502.14768, 2025. 10.48550/ARXIV.2502.14768 . URL https://doi.org/10.48550/arXiv.2502.14768 .

Ye et al. (2024) Ziyu Ye, Rishabh Agarwal, Tianqi Liu, Rishabh Joshi, Sarmishta Velury, Quoc V. Le, Qijun Tan, and Yuan Liu. Evolving alignment via asymmetric self-play. CoRR , abs/2411.00062, 2024. 10.48550/ARXIV.2411.00062 . URL https://doi.org/10.48550/arXiv.2411.00062 .

Yu et al. (2025) Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan, Gaohong Liu, Lingjun Liu, Xin Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Guangming Sheng, Yuxuan Tong, Chi Zhang, Mofan Zhang, Wang Zhang, Hang Zhu, Jinhua Zhu, Jiaze Chen, Jiangjie Chen, Chengyi Wang, Hongli Yu, Weinan Dai, Yuxuan Song, Xiangpeng Wei, Hao Zhou, Jingjing Liu, Wei-Ying Ma, Ya-Qin Zhang, Lin Yan, Mu Qiao, Yonghui Wu, and Mingxuan Wang. DAPO: an open-source LLM reinforcement learning system at scale. CoRR , abs/2503.14476, 2025. 10.48550/ARXIV.2503.14476 . URL https://doi.org/10.48550/arXiv.2503.14476 .

Yuan et al. (2024) Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, and Jason Weston. Self-rewarding language models. URL https://arxiv. org/abs/2401.10020 , 2024.

Zeng et al. (2025) Weihao Zeng, Yuzhen Huang, Qian Liu, Wei Liu, Keqing He, Zejun Ma, and Junxian He. Simplerl-zoo: Investigating and taming zero reinforcement learning for open base models in the wild. CoRR , abs/2503.18892, 2025. 10.48550/ARXIV.2503.18892 . URL https://doi.org/10.48550/arXiv.2503.18892 .

Zhang et al. (2025a) Fuxiang Zhang, Jiacheng Xu, Chaojie Wang, Ce Cui, Yang Liu, and Bo An. Incentivizing llms to self-verify their answers. arXiv preprint arXiv:2506.01369 , 2025a.

Zhang et al. (2025b) Xiaoying Zhang, Hao Sun, Yipeng Zhang, Kaituo Feng, Chaochao Lu, Chao Yang, and Helen Meng. Critique-grpo: Advancing llm reasoning with natural language and numerical feedback. arXiv preprint arXiv:2506.03106 , 2025b.

Zheng et al. (2025) Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, et al. Group sequence policy optimization. arXiv preprint arXiv:2507.18071 , 2025.

## Appendix

## Appendix A Policy Gradient Derivation for iGRPO

In this sectin, we derive the iGRPO policy gradient update consistent with the methodology in Section 3.2 and the full objective in Eq. equation 5 . Throughout, π θ \pi_{\theta} is the trainable policy, π θ old \pi_{\theta_{\mathrm{old}}} is the frozen snapshot used for sampling (PPO/GRPO convention), π ref \pi_{\mathrm{ref}} is the reference policy, and R ϕ ​ ( ⋅ ) R_{\phi}(\cdot) is a scalar (verifier) reward. Importantly, iGRPO uses two stages per optimization step, but gradients are applied only to Stage 2 tokens.

### A.1 Two-stage sampling and the induced self-conditioned prompt distribution

For each prompt q ∼ P ⁡ ( Q ) q\sim P(Q) , iGRPO constructs an augmented prompt by first sampling Stage 1 drafts and selecting the best: d i \displaystyle d_{i} ∼ π θ old ( ⋅ ∣ q ) , i = 1 , … , N , \displaystyle\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid q),\quad i=1,\ldots,N, (8) d ^ \displaystyle\hat{d} = arg ⁡ max i ∈ { 1 , … , N } ​ R ϕ ​ ( d i ) , \displaystyle=\arg\max_{i\in\{1,\ldots,N\}}R_{\phi}(d_{i}), (9) q ′ \displaystyle q^{\prime} = Concat ⁡ ( q , d ^ ) . \displaystyle=\mathrm{Concat}(q,\hat{d}). (10) This defines an implicit sampling distribution over augmented prompts q ′ q^{\prime} induced by π θ old \pi_{\theta_{\mathrm{old}}} and the arg ⁡ max \arg\max selection. Within a single PPO-style update, q ′ q^{\prime} is treated as part of the sampled context (no differentiation through Stage 1 and no differentiation through the arg ⁡ max \arg\max ). Across iterations, the distribution over q ′ q^{\prime} shifts because π θ old \pi_{\theta_{\mathrm{old}}} changes.

Given the augmented prompt q ′ q^{\prime} , Stage 2 samples a group of G G completions: o j ∼ π θ old ( ⋅ ∣ q ′ ) , j = 1 , … , G . o_{j}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid q^{\prime}),\quad j=1,\ldots,G. (11) Let each completion be a token sequence o j = ( o j , 1 , … , o j , | o j | ) o_{j}=(o_{j,1},\ldots,o_{j,|o_{j}|}) with factorization π θ ​ ( o j ∣ q ′ ) = ∏ t = 1 | o j | π θ ​ ( o j , t ∣ q ′ , o j , < t ) . \pi_{\theta}(o_{j}\mid q^{\prime})\;=\;\prod_{t=1}^{|o_{j}|}\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t}). (12)

### A.2 From the self-conditioned expected reward to a REINFORCE-style gradient

Fix an augmented prompt q ′ q^{\prime} . Consider the (conceptual) self-conditioned objective 𝒥 ( θ ∣ q ′ ) = 𝔼 o ∼ π θ ( ⋅ ∣ q ′ ) [ R ϕ ( o ) ] . \mathcal{J}(\theta\mid q^{\prime})\;=\;\mathbb{E}_{o\sim\pi_{\theta}(\cdot\mid q^{\prime})}\bigl[R_{\phi}(o)\bigr]. (13) By the score-function (REINFORCE) identity, ∇ θ 𝒥 ​ ( θ ∣ q ′ ) \displaystyle\nabla_{\theta}\mathcal{J}(\theta\mid q^{\prime}) = 𝔼 o ∼ π θ ( ⋅ ∣ q ′ ) [ R ϕ ( o ) ∇ θ log π θ ( o ∣ q ′ ) ] \displaystyle=\mathbb{E}_{o\sim\pi_{\theta}(\cdot\mid q^{\prime})}\Bigl[R_{\phi}(o)\,\nabla_{\theta}\log\pi_{\theta}(o\mid q^{\prime})\Bigr] (14) = 𝔼 o ∼ π θ ( ⋅ ∣ q ′ ) [ R ϕ ( o ) ∑ t = 1 | o | ∇ θ log π θ ( o t ∣ q ′ , o < t ) ] , \displaystyle=\mathbb{E}_{o\sim\pi_{\theta}(\cdot\mid q^{\prime})}\Biggl[R_{\phi}(o)\,\sum_{t=1}^{|o|}\nabla_{\theta}\log\pi_{\theta}(o_{t}\mid q^{\prime},o_{<t})\Biggr], (15) where the second line uses Eq. equation 12 . Introducing any baseline b ⁡ ( q ′ ) b(q^{\prime}) that does not depend on the sampled tokens preserves unbiasedness and yields an advantage-weighted gradient: ∇ θ 𝒥 ( θ ∣ q ′ ) = 𝔼 o ∼ π θ ( ⋅ ∣ q ′ ) [ ( R ϕ ( o ) − b ( q ′ ) ) ∑ t = 1 | o | ∇ θ log π θ ( o t ∣ q ′ , o < t ) ] . \nabla_{\theta}\mathcal{J}(\theta\mid q^{\prime})=\mathbb{E}_{o\sim\pi_{\theta}(\cdot\mid q^{\prime})}\Biggl[\bigl(R_{\phi}(o)-b(q^{\prime})\bigr)\sum_{t=1}^{|o|}\nabla_{\theta}\log\pi_{\theta}(o_{t}\mid q^{\prime},o_{<t})\Biggr]. (16)

### A.3 Group-relative advantage used in iGRPO

In iGRPO, the baseline is estimated per prompt by sampling a group of G G completions { o j } j = 1 G \{o_{j}\}_{j=1}^{G} and normalizing rewards within the group. Define R j = R ϕ ​ ( o j ) , R ¯ = mean ⁡ ( { R 1 , … , R G } ) , s R = std ⁡ ( { R 1 , … , R G } ) , R_{j}\;=\;R_{\phi}(o_{j}),\qquad\overline{R}\;=\;\mathrm{mean}(\{R_{1},\ldots,R_{G}\}),\qquad s_{R}\;=\;\mathrm{std}(\{R_{1},\ldots,R_{G}\}), (17) and the iGRPO advantage A ^ j = R j − R ¯ s R , with the convention ​ A ^ j = 0 ​ if ​ s R = 0 . \hat{A}_{j}\;=\;\frac{R_{j}-\overline{R}}{s_{R}},\qquad\text{with the convention }\hat{A}_{j}=0\text{ if }s_{R}=0. (18) As in GRPO, this advantage is a single scalar per completion, shared across all token indices. iGRPO additionally uses the token-averaged form (the 1 / | o j | 1/|o_{j}| factor) so that completions of different lengths contribute comparably: g on ​ - ​ policy ​ ( θ ∣ q ′ ) ≐ 1 G ​ ∑ j = 1 G A ^ j | o j | ​ ∑ t = 1 | o j | ∇ θ ​ log ​ π θ ​ ( o j , t ∣ q ′ , o j , < t ) . g_{\mathrm{on\text{-}policy}}(\theta\mid q^{\prime})\;\doteq\;\frac{1}{G}\sum_{j=1}^{G}\frac{\hat{A}_{j}}{|o_{j}|}\sum_{t=1}^{|o_{j}|}\nabla_{\theta}\log\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t}). (19) Eq. equation 19 is the basic (conceptual) iGRPO policy-gradient estimator when sampling from π θ \pi_{\theta} . The remainder of the derivation follows the standard PPO/GRPO stabilization used in the main methodology: sampling from π θ old \pi_{\theta_{\mathrm{old}}} and using importance ratios with clipping and a KL penalty.

### A.4 Off-policy sampling from π θ old \pi_{\theta_{\mathrm{old}}} and PPO-style clipping

Within each iteration, iGRPO samples Stage 2 completions from π θ old \pi_{\theta_{\mathrm{old}}} for stability. To relate gradients under π θ old \pi_{\theta_{\mathrm{old}}} to the updated policy π θ \pi_{\theta} , define the per-token importance ratio r j , t ​ ( θ ) = π θ ​ ( o j , t ∣ q ′ , o j , < t ) π θ old ​ ( o j , t ∣ q ′ , o j , < t ) . r_{j,t}(\theta)=\frac{\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t})}{\pi_{\theta_{\mathrm{old}}}(o_{j,t}\mid q^{\prime},o_{j,<t})}. (20) Following PPO/GRPO, iGRPO maximizes a clipped surrogate that replaces the on-policy factor by a clipped importance-weighted term: ℒ j , t clip ​ ( θ ) = min ⁡ ( r j , t ​ ( θ ) ​ A ^ j , clip ⁡ ( r j , t ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ A ^ j ) . \mathcal{L}^{\mathrm{clip}}_{j,t}(\theta)=\min\!\Bigl(r_{j,t}(\theta)\,\hat{A}_{j},\;\mathrm{clip}\bigl(r_{j,t}(\theta),\,1-\epsilon,\,1+\epsilon\bigr)\,\hat{A}_{j}\Bigr). (21) The per-token clipped objective in Eq. equation 21 yields the usual piecewise gradient behavior: when the ratio is clipped, the clipped branch is constant in r j , t ​ ( θ ) r_{j,t}(\theta) and contributes zero gradient through that branch.

A convenient way to write the gradient is via the indicator of the unclipped branch. Let 𝕀 j , t ​ ( θ ) = { 1 , A ^ j ≥ 0 ​ and ​ r j , t ​ ( θ ) ≤ 1 + ϵ , 1 , A ^ j < 0 ​ and ​ r j , t ​ ( θ ) ≥ 1 − ϵ , 0 , otherwise , \mathbb{I}_{j,t}(\theta)=\begin{cases}1,&\hat{A}_{j}\geq 0\text{ and }r_{j,t}(\theta)\leq 1+\epsilon,\\ 1,&\hat{A}_{j}<0\text{ and }r_{j,t}(\theta)\geq 1-\epsilon,\\ 0,&\text{otherwise},\end{cases} (22) which matches the standard PPO clipping rule. Then, using ∇ θ r j , t ​ ( θ ) = r j , t ​ ( θ ) ​ ∇ θ ​ log ⁡ π θ ​ ( o j , t ∣ q ′ , o j , < t ) \nabla_{\theta}r_{j,t}(\theta)=r_{j,t}(\theta)\,\nabla_{\theta}\log\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t}) , the gradient of the clipped surrogate is ∇ θ ℒ j , t clip ​ ( θ ) = 𝕀 j , t ​ ( θ ) ​ A ^ j ​ r j , t ​ ( θ ) ​ ∇ θ ​ log ⁡ π θ ​ ( o j , t ∣ q ′ , o j , < t ) . \nabla_{\theta}\mathcal{L}^{\mathrm{clip}}_{j,t}(\theta)=\mathbb{I}_{j,t}(\theta)\;\hat{A}_{j}\;r_{j,t}(\theta)\;\nabla_{\theta}\log\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t}). (23)

### A.5 Including the per-token KL penalty

As in Section 3.1 , iGRPO includes a per-token KL penalty to a reference policy π ref \pi_{\mathrm{ref}} using the non-negative estimator D ^ KL ( j , t ) = π ref ​ ( o j , t ∣ q ′ , o j , < t ) π θ ​ ( o j , t ∣ q ′ , o j , < t ) − log ⁡ π ref ​ ( o j , t ∣ q ′ , o j , < t ) π θ ​ ( o j , t ∣ q ′ , o j , < t ) − 1 . \widehat{D}_{\mathrm{KL}}^{(j,t)}=\frac{\pi_{\mathrm{ref}}(o_{j,t}\mid q^{\prime},o_{j,<t})}{\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t})}-\log\frac{\pi_{\mathrm{ref}}(o_{j,t}\mid q^{\prime},o_{j,<t})}{\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t})}-1. (24) Let ρ j , t ​ ( θ ) = π ref ​ ( o j , t ∣ q ′ , o j , < t ) / π θ ​ ( o j , t ∣ q ′ , o j , < t ) \rho_{j,t}(\theta)=\pi_{\mathrm{ref}}(o_{j,t}\mid q^{\prime},o_{j,<t})/\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t}) . Then D ^ KL ( j , t ) = ρ j , t − log ⁡ ρ j , t − 1 \widehat{D}_{\mathrm{KL}}^{(j,t)}=\rho_{j,t}-\log\rho_{j,t}-1 , and its gradient has a simple form: ∇ θ D ^ KL ( j , t ) = − ( ρ j , t ​ ( θ ) − 1 ) ​ ∇ θ ​ log ⁡ π θ ​ ( o j , t ∣ q ′ , o j , < t ) . \nabla_{\theta}\widehat{D}_{\mathrm{KL}}^{(j,t)}=-\bigl(\rho_{j,t}(\theta)-1\bigr)\;\nabla_{\theta}\log\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t}). (25) Therefore, the KL-regularized contribution in the objective, − β ​ D ^ KL ( j , t ) -\beta\,\widehat{D}_{\mathrm{KL}}^{(j,t)} , contributes − β ​ ∇ θ D ^ KL ( j , t ) = β ⁡ ( ρ j , t ​ ( θ ) − 1 ) ​ ∇ θ ​ log ⁡ π θ ​ ( o j , t ∣ q ′ , o j , < t ) . -\beta\,\nabla_{\theta}\widehat{D}_{\mathrm{KL}}^{(j,t)}=\beta\bigl(\rho_{j,t}(\theta)-1\bigr)\;\nabla_{\theta}\log\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t}). (26)

### A.6 Final iGRPO surrogate objective and resulting policy gradient

Putting the pieces together and reinstating the full two-stage sampling (where Stage 1 affects the distribution of q ′ q^{\prime} but is not differentiated through within an iteration), the iGRPO surrogate objective is: 𝒥 iGRPO ​ ( θ ) \displaystyle\mathcal{J}_{\mathrm{iGRPO}}(\theta) = 𝔼 [ q ∼ P ( Q ) ] 𝔼 [ { d i } i = 1 N ∼ π θ old ( ⋅ ∣ q ) , d ^ = arg max i R ϕ ( d i ) , q ′ = Concat ( q , d ^ ) , \displaystyle=\mathbb{E}\Bigl[q\sim P(Q)\Bigr]\;\mathbb{E}\Bigl[\{d_{i}\}_{i=1}^{N}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid q),\;\hat{d}=\arg\max_{i}R_{\phi}(d_{i}),\;q^{\prime}=\mathrm{Concat}(q,\hat{d}), { o j } j = 1 G ∼ π θ old ( ⋅ ∣ q ′ ) ] \displaystyle\hskip 78.00014pt\{o_{j}\}_{j=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid q^{\prime})\Bigr] × 1 G ​ ∑ j = 1 G 1 | o j | ​ ∑ t = 1 | o j | [ ℒ j , t clip ​ ( θ ) − β ​ D ^ KL ( j , t ) ] , \displaystyle\quad\times\frac{1}{G}\sum_{j=1}^{G}\frac{1}{|o_{j}|}\sum_{t=1}^{|o_{j}|}\Bigl[\mathcal{L}^{\mathrm{clip}}_{j,t}(\theta)-\beta\,\widehat{D}_{\mathrm{KL}}^{(j,t)}\Bigr], (27) where ℒ j , t clip ​ ( θ ) \mathcal{L}^{\mathrm{clip}}_{j,t}(\theta) is defined in Eq. equation 21 , r j , t ​ ( θ ) r_{j,t}(\theta) in Eq. equation 20 , and D ^ KL ( j , t ) \widehat{D}_{\mathrm{KL}}^{(j,t)} in Eq. equation 24 . This matches the structure given in Eq. equation 5 .

Differentiating Eq. equation 27 yields the iGRPO policy gradient: ∇ θ 𝒥 iGRPO ​ ( θ ) = 𝔼 ⁡ [ ⋯ ] ​ 1 G ​ ∑ j = 1 G 1 | o j | ​ ∑ t = 1 | o j | [ ∇ θ ℒ j , t clip ​ ( θ ) − β ​ ∇ θ D ^ KL ( j , t ) ] , \displaystyle\nabla_{\theta}\mathcal{J}_{\mathrm{iGRPO}}(\theta)=\mathbb{E}\Bigl[\cdots\Bigr]\;\frac{1}{G}\sum_{j=1}^{G}\frac{1}{|o_{j}|}\sum_{t=1}^{|o_{j}|}\Bigl[\nabla_{\theta}\mathcal{L}^{\mathrm{clip}}_{j,t}(\theta)-\beta\,\nabla_{\theta}\widehat{D}_{\mathrm{KL}}^{(j,t)}\Bigr], (28) with the explicit per-token forms from Eqs. equation 23 and equation 25 . Concretely, combining them gives ∇ θ 𝒥 iGRPO ​ ( θ ) = 𝔼 ⁡ [ ⋯ ] ​ 1 G ​ ∑ j = 1 G 1 | o j | ​ ∑ t = 1 | o j | [ 𝕀 j , t ​ ( θ ) ​ A ^ j ​ r j , t ​ ( θ ) + β ⁡ ( ρ j , t ​ ( θ ) − 1 ) ] ​ ∇ θ ​ log ⁡ π θ ​ ( o j , t ∣ q ′ , o j , < t ) . \displaystyle\nabla_{\theta}\mathcal{J}_{\mathrm{iGRPO}}(\theta)=\mathbb{E}\Bigl[\cdots\Bigr]\;\frac{1}{G}\sum_{j=1}^{G}\frac{1}{|o_{j}|}\sum_{t=1}^{|o_{j}|}\Bigl[\mathbb{I}_{j,t}(\theta)\,\hat{A}_{j}\,r_{j,t}(\theta)+\beta\bigl(\rho_{j,t}(\theta)-1\bigr)\Bigr]\;\nabla_{\theta}\log\pi_{\theta}(o_{j,t}\mid q^{\prime},o_{j,<t}). (29)

##### Interpretation.

Eq. equation 29 makes the roles of the two stages explicit. Stage 1 defines the self-conditioned context q ′ q^{\prime} (and thus the learning problem presented to Stage 2) but does not contribute direct gradients within an iteration. Stage 2 contributes a standard GRPO/PPO-style token-level policy gradient, where each token is weighted by a group-normalized advantage A ^ j \hat{A}_{j} (shared across tokens of the completion), stabilized by importance-ratio clipping, and regularized by a KL penalty to π ref \pi_{\mathrm{ref}} .

## Appendix B Scaling OpenMath-Nemotron-14B with iGRPO

To further validate the effectiveness of iGRPO, we trained the OpenMath-Nemotron-14B with iGRPO on large scale dataset of OpenR1-Math-220k ( R1, 2024 ) which consists of 220,000 math problems with reasoning traces from DeepSeek-R1. For this study, we use 94,000 examples. As shown in Table S.1 , the reasoning performance of the model trained with iGRPO is significantly improved, achieving an impressive AIME25 score of 66.04%.

### B.1 Analysis of Pass@N on AIME Benchmarks

Figure S.1 shows how the accuracy of iOpenMath-Nemotron-14B evolves when increasing the number of attempts N N on the AIME24 and AIME25 benchmarks. As expected, we see consistent gains in performance as N N grows, indicating that the model can generate correct solutions among multiple sampled responses even if the top-1 guess is sometimes incorrect. Although our base SFT model already shows strong results at pass@1, the additional RL fine-tuning appears to capitalize on multi-sample scenarios. For example, on AIME25, the model improves from 66.04% (pass@1) to 86.67% at pass@8, demonstrating the effectiveness of producing multiple solutions for challenging competition problems.

Despite these gains, there are clear saturation points. AIME24 converges to its best score of 93.33% by N = 16 N=16 , with no further improvement at higher N N . On the contrary, the performance of AIME25 continues to improve even at high values of N N . While the performance seems to plateau briefly at 90.00% between N = 32 N=32 and N = 128 N=128 , it eventually increases to 96.67% at N = 256 N=256 . This contrast suggests that certain problem distributions, especially in AIME25, may benefit from a larger number of sampled attempts, whereas others, such as those in AIME24, can be adequately solved with fewer solution attempts.

## Appendix C Hyperparameter Setup

We conduct ablation studies on both 7B and 14B model variants, spanning core architectures such as DeepSeek-R1-Distill-Qwen and OpenMath-Nemotron. All models are trained for one epoch across two datasets: (1) the MATH dataset ( Hendrycks et al., 2021 ) of 7,500 step-by-step problems, and (2) AceReason - Math ( Chen et al., 2025b ) dataset (9400 problems). Our training uses a KL divergence loss coefficient of 0. We set a cosine learning rate schedule (minimum rate of 0.1) with a base learning rate of 1 × 10 − 6 1\times 10^{-6} . We use 8 rollouts for all experiments.

Table S.2 lists the concrete hyperparameters for training 7B iGRPO models. Notably, we run on 2 nodes with 8 × \times NVIDIA A100 GPUs each, and one of these nodes is fully allocated to vLLM for generation. We keep a global batch size of 128, with a per-device batch size of 16 and a gradient accumulation step size of 8. For the 14B models, we scale out to 5 nodes of 8 × \times NVIDIA A100 GPUs each (again, one node reserved for vLLM) and reduce the per-device batch size to 4 (maintaining the same global batch size of 128). In both 7B and 14B setups, we continue to use bfloat16 precision and the FlashAttention-2 kernel. The temperature is set to 0.7 for generation, and we apply two reward functions (accuracy and format) each with weight 1.0. This configuration provides a balanced trade-off between training stability, throughput, and alignment with complex mathematical reasoning tasks.

##### Prompt:

We use the following prompt for training model with iGRPO.

## Appendix D Memory and Throughput Comparisons

### D.1 Setup

To evaluate the resource utilization of our training setup, we replicate the exact environment and conditions under which our 7B models are typically trained. Specifically, we use DeepSeek-R1-Distill-Qwen-7B as our base model, which serves as a representative checkpoint for measuring throughput and memory consumption when training on the MATH dataset. Our training configuration employs a per-device batch size of 16, along with a global gradient accumulation step of 8, allowing us to effectively simulate heavier loads without exceeding GPU memory constraints. Additionally, we use a maximum completion length of 2048 tokens to benchmark model performance. We run experiments on two nodes, each equipped with 8 × NVIDIA A100 GPUs. One node is dedicated to vllm generation, ensuring that inference or generation processes do not interfere with the primary training workload, while the other node is reserved exclusively for model training.

We measure peak memory usage by periodically querying the GPU memory allocator for the maximum memory allocation that has occurred since the start of training. Specifically, at the beginning of training, we reset the peak memory statistics, and then after each iteration, we retrieve the current peak memory usage in bytes. We convert this value to gigabytes for readability and log it alongside other training metrics. To measure throughput, we track the total number of samples processed over time. We calculate this by multiplying the current global step by both the per-device batch size and the number of devices used in data parallelism. Dividing this product by the elapsed training time in seconds yields the throughput, expressed as samples processed per second. This real-time monitoring of memory and throughput allows us to evaluate hardware utilization efficiency, identify possible bottlenecks, and compare different training configurations in a consistent and quantifiable manner.

### D.2 Measurements

Table S.3 presents measured GPU usage and training throughput under iGRPO vs GRPO. Despite the two-stage nature of iGRPO, its peak memory usage of 54.9349 GB closely matches GRPO’s 54.9286 GB, a difference of roughly 0.0063 GB, which is practically negligible. This matches our theoretical expectation that the self-feedback mechanism adds minimal overhead, validating the feasibility of integrating iterative refinements even under constrained resource budgets.

Regarding throughput, iGRPO processes 0.34 samples/s compared to GRPO’s 0.41 samples/s, reflecting a mild slowdown tied to the additional round of generation. Crucially, this is neither an order-of-magnitude nor a large factor reduction. Instead, it shows that iGRPO’s second-stage refinement imposes only a modest computational cost. In summary, these measurements confirm our claims that iGRPO can be implemented with little additional overhead, supporting it as a practical strategy for enhancing mathematical reasoning performance without compromising resource efficiency.

Beyond instantaneous throughput, we also report full training cost measured in total GPU hours. Under the same compute budget and eight generations per prompt, GRPO requires 83.3 GPU hours while iGRPO uses 94.1 GPU hours, which corresponds to roughly a 13% increase in wall-clock training time. This overhead arises from the sequential Stage 1 plus Stage 2 decoding but does not demand more GPUs or additional memory capacity, since peak usage remains essentially unchanged. Given that this modest time increase delivers several-point gains on AIME24 and AIME25 and enables our 7B models to reach state-of-the-art performance, we view the tradeoff between 13% extra training time and substantially higher reasoning accuracy as a favorable and practical value proposition in real deployments.

## Appendix E Additional Ablation Studies

##### Training Dynamics and Response Length.

As shown in Fig. S.2 , we compare average rewards for iGRPO and GRPO at multiple checkpoints, observing that iGRPO consistently maintains a higher reward throughout training. The iterative refinement in iGRPO ultimately yields a superior reward trajectory. In addition, we measure the response length over training steps and find that both methods exhibit nearly identical lengths, with GRPO producing slightly longer outputs on average. Notably, iGRPO’s two-stage process does not manifest in lengthy completions but instead appears to refine solutions within a similar token budget. This indicates that the gains from iterative refinement arise more from improved response quality than from verbosity.

##### Effect of KL Divergence Term.

We vary the coefficient β ∈ { 0 , 0.0001 , 0.001 , 0.01 } \beta\in\{0,0.0001,0.001,0.01\} to examine how tightly the policy is regularized against the reference model. As shown in Table S.4 , while β = 0.0001 \beta=0.0001 achieves the highest overall score (70.23%), the difference among all settings is relatively small. The KL term, in principle, balances exploration with adherence to the current policy. However, given the marginal gains observed, setting β = 0 \beta=0 offers a simpler training pipeline without sacrificing significant performance. Hence, we use β = 0 \beta=0 to reduce overhead and maintain efficiency.

##### Effect of Number of Completions.

We study how the total number of completions in iGRPO affects performance, allocating 4 , 8 , 16 , 4,8,16, or 32 32 completions evenly across the two stages. As shown in Table S.4 , increasing from 4 4 to 8 8 completions gives a clear improvement, while gains beyond 8 8 are modest. Larger budgets also increase training time and inference latency for minimal returns.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
