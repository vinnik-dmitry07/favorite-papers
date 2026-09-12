##### Report GitHub Issue

Content selection saved. Describe the issue below:

# OPRD: On-Policy Representation Distillation

###### Abstract

On-policy distillation (OPD) supervises the student exclusively in the output space by matching next-token distributions. This paradigm suffers from two limitations: (i) a high-variance gradient estimator whose signal-to-noise ratio collapses as the student approaches the teacher, and (ii) an LM-head information bottleneck that discards the teacher’s intermediate hidden states. We propose On-Policy Representation Distillation (OPRD) , the first method to lift on-policy distillation into the hidden-state space . OPRD aligns student and teacher representations across selected layers on the same on-policy rollouts, providing dense, deterministic, per-layer supervision while bypassing the LM head entirely. Theoretically, OPRD provides a deterministic per-sample gradient, removing the token-level estimation variance that plagues OPD, and exposes structural information that any output-space objective necessarily discards. Empirically, OPRD closes the student–teacher gap on competition mathematics benchmarks (AIME 2024, AIME 2025, AIMO) where every output-space baseline plateaus below the teacher, while training 1.44 × 1.44\times faster and using up to 54 % 54\% less memory. We further extend OPRD to the cross-architecture setting via OPRD-Bridge : by exploiting the observation that heterogeneous models share a low-rank representational structure, we construct a frozen projector pair that aligns representations across arbitrary depth/width mismatches, shifting the alignment from the output space (which depends on a shared vocabulary) to the representation space. We validate OPRD-Bridge on both cross-architecture (Qwen3-4B → \to Qwen3-1.7B-Base) and cross-tokenizer (Phi-4-mini-reasoning → \to Qwen3-1.7B-Base) settings, demonstrating successful knowledge transfer even when the vocabulary-based alignment channel is unavailable. The code is available via https://github.com/ShenzhiYang2000/OPRD .

## 1 Introduction

On-policy distillation (OPD) has become a central building block in large language model (LLM) post-training. By letting the student sample its own responses and then scoring each token against the teacher’s conditional distribution, OPD provides a dense, token-level training signal that adapts to the student’s current policy, avoiding the exposure bias inherent in training on static teacher outputs [ 2 ] . Multiple production systems now rely on OPD as a primary post-training stage [ 39 , 37 , 47 , 5 ] , positioning it alongside supervised fine-tuning and outcome-reward reinforcement learning.

Despite this momentum, the design space of OPD has remained surprisingly narrow. Every variant proposed to date (sampled-token [ 37 , 41 ] , full-vocabulary, and top- k k ) differs only in how many output tokens are evaluated per position, yet they all operate inside the same output space : the divergence is computed over next-token probability distributions p t p_{t} and q t q_{t} . We argue that this output-only paradigm imposes two practical limitations that become increasingly damaging as training progresses.

Limitation 1: Variance dominates the late-stage signal. Sampled-token OPD estimates each token-level reverse KL from a single sample drawn from a vocabulary of size | 𝒱 | |\mathcal{V}| (e.g., ≈ 151 \approx\!151 K for Qwen3). The estimator is unbiased, but its variance shrinks much more slowly than the signal: letting δ ≜ ‖ p t − q t ‖ \delta\triangleq\|p_{t}-q_{t}\| measure the student–teacher gap, the expected gradient decays as O ⁡ ( δ 2 ) O(\delta^{2}) while the variance decays only as O ⁡ ( δ ) O(\delta) , so the signal-to-noise ratio collapses and training plateaus well below the teacher ( Figure 4 ). Top- k k OPD partially mitigates this by evaluating k k tokens per position, but trades sampling variance for truncation bias and still plateaus empirically.

Limitation 2: The output layer is an information bottleneck. Every output-space variant treats the teacher as a black-box probability oracle , querying only the LM-head output. Yet the teacher has computed, at every position, an entire stack of d d -dimensional hidden states encoding attention patterns, mid-layer reasoning state, and geometric structure. Nearly all of this is destroyed by the LM-head projection W head : ℝ d → ℝ | 𝒱 | W_{\mathrm{head}}\!:\mathbb{R}^{d}\!\to\!\mathbb{R}^{|\mathcal{V}|} and the subsequent softmax: output distributions that agree to within an arbitrary tolerance can correspond to hidden states differing along entire affine subspaces of ℝ d \mathbb{R}^{d} . The student is therefore graded only on what survives this projection, and receives no signal about how the teacher arrived at that distribution. This is particularly wasteful in the on-policy regime, where the teacher’s hidden states are already computed on every rollout but discarded before they reach the loss.

To overcome both limitations, we propose On-Policy Representation Distillation (OPRD) , the first method to lift on-policy distillation from the output space into the hidden-state space . On the same on-policy rollouts ( x , y ^ ) (x,\hat{y}) already used by standard OPD, OPRD aligns the student’s intermediate hidden representations with the teacher’s across selected transformer layers and response positions via a normalized mean-squared error objective. A single design choice (supervising at the representation level rather than at the output level) simultaneously addresses both limitations. First, deterministic, low-variance gradients: OPRD’s MSE objective is a deterministic function of the rollout; its gradient carries zero additional sampling variance, eliminating the late-stage signal-to-noise collapse of OPD by construction. Second, a richer supervision channel beyond logits: OPRD taps the teacher at any subset of its L L intermediate layers, exposing (layers × \times positions × \times hidden-dim) scalars of structural supervision per sample, orders of magnitude more than the signal extracted at the output. The student is graded on the same intermediate representations the teacher actually computed, without filtering through the LM-head projection. Both properties follow from a single conceptual shift: moving the supervision target from the output of the LM head to its input. Because the loss path never materialises the [ B , T , | 𝒱 | ] [B,T,|\mathcal{V}|] logits tensor, OPRD also reduces wall-clock time and peak GPU memory as a direct consequence of this design. OPRD is a self-contained training objective that can be used on its own; it also composes additively with any OPD variant at essentially zero infrastructure cost. Beyond the standard teacher–student setting studied here, we highlight two high-value scenarios where OPRD’s advantages are especially pronounced. (1) Multi-model RL merging. State-of-the-art RL pipelines increasingly merge multiple teacher or reward-model checkpoints into a single student. In this setting, full-vocabulary OPD requires materialising a [ B , T , | 𝒱 | ] [B,T,|\mathcal{V}|] logit tensor per teacher , quickly exhausting GPU memory and demanding heavy infrastructure work [ 5 ] . Top- k k OPD alleviates memory but introduces a truncation bias (tail tokens are ignored) and still plateaus below the teacher empirically. OPRD sidesteps both: its hidden-state loss never touches the vocabulary dimension, so memory and wall-clock scale with d d rather than | 𝒱 | |\mathcal{V}| , while its deterministic gradient avoids the variance trap entirely. (2) On-policy self-distillation (OPSD). A growing line of work constructs the teacher from the student itself by injecting privileged information (e.g., ground-truth solutions, step-level verification signals) into the prompt. Because teacher and student share exactly the same weights, the same-architecture requirement is satisfied by construction, and the hidden-state alignment signal is maximally informative. OPRD can therefore serve as a drop-in replacement for the output-space reverse-KL in any OPSD pipeline, delivering lower variance and lower cost without any architectural modification. We discuss both applications in detail in § 5 . The strict Pareto improvement over all output-space baselines is summarized in Figure 1 .

The above formulation, which we call OPRD-Vanilla , however, requires teacher and student to share the same architecture: identical depth, identical hidden dimension, and compatible initialization. The moment these conditions are violated, the method breaks down, since hidden states of different dimensionality cannot be directly compared, and even when dimensions happen to match across different architectures, the cosine similarity between corresponding hidden states is empirically zero. This same-architecture constraint excludes precisely the most common distillation scenario, namely distilling a large, expensive teacher into a smaller, deployable student, which inherently involves heterogeneous model pairs.

A useful perspective on this problem comes from asking why output-space distillation does not suffer from the same limitation. The answer is that logit distillation possesses a natural bridge : the shared vocabulary. Both teacher and student project their hidden states through their respective LM heads into the same probability simplex, making outputs directly comparable regardless of internal architecture. The vocabulary serves as a fixed, pre-established interface that neither model modifies during training, and knowledge flows through it. This bridge works, but it has a critical limitation of its own: it requires both models to share the same vocabulary. Moreover, it operates at only a single point in the network (the final layer) and is lossy, compressing all representational structure into a single next-token distribution. The natural question, then, is whether one can construct an analogous bridge for representations , one that carries richer information, operates at every layer, and does not depend on a shared vocabulary.

The Platonic Representation Hypothesis [ 15 ] provides theoretical grounds to believe such a bridge should exist. It posits that strong neural networks, regardless of architecture, are converging toward a shared statistical model of reality in their representation spaces. Empirically, models with higher downstream performance exhibit higher mutual representation alignment [ 22 ] , and a single linear projection suffices to bridge representations across architectures and even across modalities [ 27 , 26 ] . We confirm this directly: pairing a Qwen3-4B teacher (36 layers, d = 2560 d\!=\!2560 ) with a Qwen3-1.7B-Base student (28 layers, d = 2048 d\!=\!2048 ), a rank-8 linear subspace achieves 95% cosine similarity between the projected representations of the two models, despite their different depths and widths. Notably, this similarity decreases with higher rank, indicating that the shared structure concentrates in very few principal directions and that additional dimensions introduce noise rather than signal.

This finding leads directly to OPRD-Bridge . We construct a pair of linear projectors, one per model, that map their respective hidden states into a shared low-rank subspace. The teacher’s projector is obtained via PCA of its hidden-state covariance (extracting the principal variation directions); the student’s projector is trained to align with it. Once both projectors converge, they are frozen and serve as a fixed bridge through which representational structure flows from teacher to student during the main distillation phase, which optimizes only the student backbone. The design mirrors logit distillation: just as the vocabulary is a frozen interface through which output-level knowledge flows, the projector pair ( P T , P S ) (P_{T},P_{S}) is a frozen interface through which representation-level knowledge flows, but at every layer rather than only the last, and decoupled from the vocabulary. We validate this capability empirically by distilling across completely disjoint tokenizers (Phi-4-mini-reasoning → \to Qwen3-1.7B), a setting where the vocabulary-based alignment channel is unavailable.

Our main contributions are as follows: 1. OPRD-Vanilla: representation-level on-policy distillation. We propose On-Policy Representation Distillation, the first method to lift on-policy distillation from the output space into the hidden-state space. We provide a two-perspective theoretical analysis showing that OPRD (i) yields a deterministic per-sample gradient, removing the token-level estimation variance of OPD’s gradient estimator, and (ii) exposes per-layer structural information that the LM-head projection necessarily discards.

2. OPRD-Bridge: cross-architecture extension. We show that heterogeneous teacher–student pairs share a low-rank representational structure, and exploit this to construct a frozen projector pair that enables representation distillation across arbitrary architecture pairs (different depth, width, and potentially vocabulary), the first such method in the on-policy regime.

3. Empirical validation. On competition mathematics benchmarks (AIME 2024, AIME 2025, AIMO), OPRD-Vanilla closes the student–teacher gap where every output-space baseline plateaus, while training 1.44 × 1.44\times faster and using up to 54 % 54\% less memory.

## 2 Background and Problem Setup

This section formalizes the on-policy distillation problem we build upon. We introduce the necessary notation in § 2.1 , define the on-policy distillation framework in § 2.2 , and catalogue the three output-space supervision granularities used in prior work in § 2.3 . We close in § 2.4 by isolating the common structural property of these variants that motivates our hidden-state approach in the next section.

### 2.1 Notation

We consider two autoregressive language models with a shared vocabulary 𝒱 \mathcal{V} : a student π θ \pi_{\theta} with trainable parameters θ \theta , and a fixed teacher π T \pi_{T} . A training instance is a prompt x = ( x 1 , … , x n ) x=(x_{1},\ldots,x_{n}) drawn from a prompt distribution 𝒟 x = { x ( i ) } i = 1 N \mathcal{D}_{x}=\{x^{(i)}\}_{i=1}^{N} ; a model response is a token sequence y = ( y 1 , … , y m ) y=(y_{1},\ldots,y_{m}) produced autoregressively. For brevity we write the prefix up to step t t as y < t ≜ ( y 1 , … , y t − 1 ) y_{<t}\triangleq(y_{1},\ldots,y_{t-1}) , and use π ( ⋅ ∣ x , y < t ) \pi(\cdot\mid x,y_{<t}) to denote either model’s next-token distribution over 𝒱 \mathcal{V} conditioned on ( x , y < t ) (x,y_{<t}) . The notation y ∼ π θ ( ⋅ ∣ x ) y\sim\pi_{\theta}(\cdot\mid x) refers to an autoregressive sample drawn from the student.

Both models follow the standard transformer template: a stack of self-attention blocks producing intermediate hidden states h ( l ) ∈ ℝ d h^{(l)}\in\mathbb{R}^{d} at each layer l l and position, followed by a language-model head W head ∈ ℝ | 𝒱 | × d W_{\mathrm{head}}\in\mathbb{R}^{|\mathcal{V}|\times d} that maps the final hidden state to logits. We use L L and d d when the two models share the same depth and width; when they differ (§ 3.3 ), we write L S , L T L_{S},L_{T} and d S , d T d_{S},d_{T} explicitly. We write h θ , t ( l ) h_{\theta,t}^{(l)} and h T , t ( l ) h_{T,t}^{(l)} for the student and teacher hidden states at layer l l and response position t t , with both networks evaluated on the same input sequence.

### 2.2 The On-Policy Distillation Framework

##### Setup.

On-policy distillation (OPD) departs from classical knowledge distillation by drawing the supervision distribution from the student rather than from a fixed dataset. Concretely, at each training step the student first samples a response y ^ = ( y ^ 1 , … , y ^ T ) ∼ π θ ( ⋅ ∣ x ) \hat{y}=(\hat{y}_{1},\ldots,\hat{y}_{T})\sim\pi_{\theta}(\cdot\mid x) of length T ≜ | y ^ | T\triangleq|\hat{y}| , after which both models are evaluated on the student-generated prefixes. For each position t ∈ { 1 , … , T } t\in\{1,\ldots,T\} this yields a pair of next-token distributions over 𝒱 \mathcal{V} : p t ​ ( v ) ≜ π θ ​ ( v ∣ x , y ^ < t ) , q t ​ ( v ) ≜ π T ​ ( v ∣ x , y ^ < t ) , v ∈ 𝒱 . p_{t}(v)\;\triangleq\;\pi_{\theta}(v\mid x,\hat{y}_{<t}),\qquad q_{t}(v)\;\triangleq\;\pi_{T}(v\mid x,\hat{y}_{<t}),\qquad v\in\mathcal{V}. (1) The defining feature of OPD is that the teacher is queried on student-visited states , namely prefixes that arise from the current policy, rather than on canonical teacher trajectories. This eliminates the exposure-bias gap between training and inference distributions that plagues fixed-target distillation.

##### Objective.

The canonical OPD objective minimizes the trajectory-level reverse KL divergence between the student and teacher policies on student rollouts. By the chain rule for KL divergence, this trajectory-level quantity decomposes exactly into a sum of token-level reverse KL terms: ℒ OPD ( θ ) = 𝔼 x ∼ 𝒟 x , y ^ ∼ π θ ( ⋅ ∣ x ) [ ∑ t = 1 T D KL ( p t ∥ q t ) ] , \mathcal{L}_{\mathrm{OPD}}(\theta)\;=\;\mathbb{E}_{x\sim\mathcal{D}_{x},\;\hat{y}\sim\pi_{\theta}(\cdot\mid x)}\!\left[\sum_{t=1}^{T}D_{\mathrm{KL}}(p_{t}\,\|\,q_{t})\right], (2) where the token-level reverse KL at position t t is D KL ( p t ∥ q t ) = ∑ v ∈ 𝒱 p t ( v ) log [ p t ( v ) / q t ( v ) ] D_{\mathrm{KL}}(p_{t}\,\|\,q_{t})=\sum_{v\in\mathcal{V}}p_{t}(v)\log[p_{t}(v)/q_{t}(v)] . Eq. ( 2 ) is conceptually clean but computationally inconvenient: it requires summing over the full vocabulary 𝒱 \mathcal{V} at every position, which is prohibitive for modern LLMs with | 𝒱 | |\mathcal{V}| in the hundreds of thousands. Practical implementations differ in how they approximate this sum, and we review the three dominant choices below.

### 2.3 Three Output-Space Variants

We use a unified template to describe each variant: at each position t t , define a token subset S t ⊆ 𝒱 S_{t}\subseteq\mathcal{V} and a per-position loss ℓ t \ell_{t} that depends only on { p t ( v ) , q t ( v ) : v ∈ S t } \{p_{t}(v),q_{t}(v):v\in S_{t}\} . The three variants below correspond to different choices of S t S_{t} .

##### (a) Sampled-token OPD ( S t = { y ^ t } S_{t}=\{\hat{y}_{t}\} ).

The most lightweight and by far the most widely adopted choice in production deployments [ 37 , 41 ] . A single token y ^ t ∼ p t \hat{y}_{t}\sim p_{t} already drawn during rollout is reused as the supervision target, and the per-position loss takes the form of a log-ratio: ℓ t sample ≜ log ⁡ p t ​ ( y ^ t ) − log ⁡ q t ​ ( y ^ t ) , ℒ OPD sample ​ ( θ ) = 𝔼 x , y ^ ​ [ ∑ t = 1 T ℓ t sample ] . \ell_{t}^{\mathrm{sample}}\;\triangleq\;\log p_{t}(\hat{y}_{t})-\log q_{t}(\hat{y}_{t}),\qquad\mathcal{L}_{\mathrm{OPD}}^{\mathrm{sample}}(\theta)=\mathbb{E}_{x,\hat{y}}\!\left[\sum_{t=1}^{T}\ell_{t}^{\mathrm{sample}}\right]. (3) A straightforward calculation gives 𝔼 y ^ t ∼ p t [ ℓ t sample ] = D KL ( p t ∥ q t ) \mathbb{E}_{\hat{y}_{t}\sim p_{t}}[\ell_{t}^{\mathrm{sample}}]=D_{\mathrm{KL}}(p_{t}\,\|\,q_{t}) , so ℓ t sample \ell_{t}^{\mathrm{sample}} is an unbiased single-sample estimator of the token-level reverse KL. Memory cost is O ⁡ ( B ​ T ) O(BT) for batch size B B and response length T T ; teacher queries amount to one log-probability per token.

##### (b) Full-vocabulary OPD ( S t = 𝒱 S_{t}=\mathcal{V} ).

At the opposite extreme, one materializes the entire teacher distribution and computes the exact token-level KL at every position: ℒ OPD full ​ ( θ ) = 𝔼 x , y ^ ​ [ ∑ t = 1 T ∑ v ∈ 𝒱 p t ​ ( v ) ​ log ⁡ p t ​ ( v ) q t ​ ( v ) ] . \mathcal{L}_{\mathrm{OPD}}^{\mathrm{full}}(\theta)=\mathbb{E}_{x,\hat{y}}\!\left[\sum_{t=1}^{T}\sum_{v\in\mathcal{V}}p_{t}(v)\,\log\!\tfrac{p_{t}(v)}{q_{t}(v)}\right]. (4) The gradient signal is the densest possible, but the price is steep: storing teacher logits demands O ⁡ ( B ​ T ​ | 𝒱 | ) O(BT|\mathcal{V}|) memory, which becomes infeasible for long-context training at modern vocabulary sizes.

##### (c) Top- k k OPD ( S t = TopK ⁡ ( p t , k ) S_{t}=\mathrm{TopK}(p_{t},k) ).

Top- k k OPD interpolates between the two extremes by restricting attention to the k k tokens that the student ranks highest at position t t , then computing a KL between renormalized distributions on this support: ℒ OPD top- ​ k ( θ ) = 𝔼 x , y ^ [ ∑ t = 1 T D KL ( p ¯ t ( S t ) ∥ q ¯ t ( S t ) ) ] , p ¯ t ( S t ) ( v ) = p t ( v ) 1 [ v ∈ S t ] ∑ u ∈ S t p t ​ ( u ) , \mathcal{L}_{\mathrm{OPD}}^{\text{top-}k}(\theta)=\mathbb{E}_{x,\hat{y}}\!\left[\sum_{t=1}^{T}D_{\mathrm{KL}}\!\left(\bar{p}_{t}^{(S_{t})}\,\big\|\,\bar{q}_{t}^{(S_{t})}\right)\right],\quad\bar{p}_{t}^{(S_{t})}(v)=\frac{p_{t}(v)\,\mathbf{1}[v\in S_{t}]}{\sum_{u\in S_{t}}p_{t}(u)}, (5) and analogously for q ¯ t ( S t ) \bar{q}_{t}^{(S_{t})} . The hyperparameter k k trades supervision density against teacher-query cost, with k = 1 k=1 recovering (a deterministic version of) sampled-token OPD and k = | 𝒱 | k=|\mathcal{V}| recovering full-vocabulary OPD. Typical implementations use k ∈ [ 4 , 64 ] k\in[4,64] . We measure this cost empirically in § 4.1.4 , where top- 16 16 OPD’s actor-update transient memory is more than 2 × 2\times larger than OPRD’s at the same setting.

### 2.4 A Shared Structural Limitation

The three variants above span the full design space studied in prior work, yet they share a defining structural property: the supervision signal is always a function of the next-token distributions p t p_{t} and q t q_{t} that the LM head produces. Equivalently, the only way teacher knowledge reaches the student is through the projection W head : ℝ d → ℝ | 𝒱 | W_{\mathrm{head}}:\mathbb{R}^{d}\to\mathbb{R}^{|\mathcal{V}|} applied to the final hidden state. The internal representations { h T , t ( l ) } l < L \{h_{T,t}^{(l)}\}_{l<L} , which are the very features that encode the teacher’s intermediate reasoning, never enter the loss. This output-only view has two immediate consequences that will become focal points of our analysis. (i) Statistical: the most popular variant (sampled-token OPD) estimates each token-level KL from a single Monte Carlo draw, introducing variance that scales unfavorably with | 𝒱 | |\mathcal{V}| and dominates the optimization signal once p t p_{t} approaches q t q_{t} . (ii) Informational: because W head W_{\mathrm{head}} is low-rank ( d ≪ | 𝒱 | d\ll|\mathcal{V}| ), the loss imposes only d d effective constraints per position regardless of | S t | |S_{t}| , leaving large directions of the hidden-state space unsupervised. Our method, introduced next, attacks both issues by replacing W head ∘ h W_{\mathrm{head}}\!\circ\!h with h h itself as the alignment target.

## 3 On-Policy Representation Distillation

We now present On-Policy Representation Distillation (OPRD) , a novel distillation framework that supervises the student in the hidden-state space on student-generated trajectories. We define the method ( Section 3.1 ) and state two theorems, one on gradient variance and one on the LM-head information bottleneck ( Theorem 1 , Theorem 2 ), that explain why hidden-state supervision is a principled and effective complement to output-space distillation.

### 3.1 The OPRD Objective

The three OPD variants in § 2.3 all operate in the output space by matching next-token distributions p t p_{t} and q t q_{t} . OPRD instead supervises the student in the hidden-state space on the same on-policy trajectories. Intuitively, OPD asks the student to assign similar probabilities to tokens, whereas OPRD asks the student to produce similar internal representations at selected layers and positions. We refer to this basic same-architecture formulation as OPRD-Vanilla (or simply OPRD when unambiguous); the cross-architecture extension, OPRD-Bridge , is presented in § 3.3 .

Let ℒ layer ⊆ { 1 , … , L } \mathcal{L}_{\mathrm{layer}}\subseteq\{1,\ldots,L\} be the set of distilled layers (e.g. the last layer, all layers, or a parity subset such as even/odd layers), and let 𝒫 ⁡ ( y ^ ) ⊆ { 1 , … , T } \mathcal{P}(\hat{y})\subseteq\{1,\ldots,T\} be the set of supervised response positions (e.g. all tokens, the first k k tokens, or the last k k tokens). We use a position mask m t ∈ { 0 , 1 } m_{t}\in\{0,1\} to indicate whether t ∈ 𝒫 ⁡ ( y ^ ) t\in\mathcal{P}(\hat{y}) ; for short responses, positions beyond the valid length are masked out rather than padded into the loss. OPRD minimizes a layer-averaged, position-masked mean-squared error between student and teacher representations: ℒ OPRD ( θ ) = 𝔼 x ∼ 𝒟 x , y ^ ∼ π θ ( ⋅ ∣ x ) [ 1 | ℒ layer | ∑ l ∈ ℒ layer 1 ∑ t = 1 T m t ∑ t = 1 T m t 1 d ∥ h θ , t ( l ) − sg ( h T , t ( l ) ) ∥ 2 2 ] , \mathcal{L}_{\mathrm{OPRD}}(\theta)=\mathbb{E}_{x\sim\mathcal{D}_{x},\;\hat{y}\sim\pi_{\theta}(\cdot\mid x)}\left[\frac{1}{|\mathcal{L}_{\mathrm{layer}}|}\sum_{l\in\mathcal{L}_{\mathrm{layer}}}\frac{1}{\sum_{t=1}^{T}m_{t}}\sum_{t=1}^{T}m_{t}\,\frac{1}{d}\Bigl\|h_{\theta,t}^{(l)}-\mathrm{sg}\!\bigl(h_{T,t}^{(l)}\bigr)\Bigr\|_{2}^{2}\right], (6) where sg ⁡ ( ⋅ ) \mathrm{sg}(\cdot) denotes the stop-gradient operator on the teacher representation and d d is the hidden dimension. The 1 / d 1/d factor normalizes the loss across architectures with different hidden sizes; the position averaging 1 / ∑ t m t 1/\sum_{t}m_{t} makes the loss invariant to the choice of | 𝒫 ⁡ ( y ^ ) | |\mathcal{P}(\hat{y})| . The two design knobs ( ℒ layer \mathcal{L}_{\mathrm{layer}} , 𝒫 ⁡ ( y ^ ) \mathcal{P}(\hat{y}) ) offer flexibility along two axes: depth of supervision (single-layer vs. multi-layer) and breadth of supervision (single-position vs. all-position). For long chain-of-thought (CoT) responses common in mathematical reasoning, we typically set 𝒫 ⁡ ( y ^ ) \mathcal{P}(\hat{y}) to the last k k response tokens and ℒ layer \mathcal{L}_{\mathrm{layer}} to all transformer layers, yielding dense layer-wise supervision on a compact suffix while keeping memory bounded. We empirically study the effect of these design choices in § 4.1.5 . OPRD is a self-contained training objective and our main results (§ 4 ) are reported in the OPRD-only setting. For completeness, OPRD also composes additively with any output-space OPD variant as ℒ ⁡ ( θ ) = ℒ OPD ​ ( θ ) + μ ​ ℒ OPRD ​ ( θ ) , μ ≥ 0 , \mathcal{L}(\theta)=\mathcal{L}_{\mathrm{OPD}}(\theta)+\mu\,\mathcal{L}_{\mathrm{OPRD}}(\theta),\quad\mu\geq 0, (7) at essentially zero infrastructure cost since both terms are computed on the same on-policy rollout and share a single teacher forward pass.

### 3.2 Why OPRD Works

Two complementary properties, in one-to-one correspondence with the two limitations of § 1 , explain why hidden-state supervision is a principled complement to output-space OPD. We state both as informal theorems; precise statements and proofs are deferred to Appendix B .

###### Theorem 1 (Zero-variance gradient) .

Let g OPD g_{\mathrm{OPD}} and g OPRD g_{\mathrm{OPRD}} be the per-sample stochastic gradients of sampled-token OPD and OPRD ( 6 ) on an on-policy rollout y ^ ∼ π θ ( ⋅ ∣ x ) \hat{y}\sim\pi_{\theta}(\cdot\!\mid\!x) . Conditioned on ( x , y ^ ) (x,\hat{y}) , Var [ g OPRD | x , y ^ ] = 0 , Var [ g OPD | x , y ^ ] ∝ Var y ^ t ∼ p t [ log p t ( y ^ t ) − log q t ( y ^ t ) ] , \mathrm{Var}\!\left[g_{\mathrm{OPRD}}\,\big|\,x,\hat{y}\right]=0,\qquad\mathrm{Var}\!\left[g_{\mathrm{OPD}}\,\big|\,x,\hat{y}\right]\;\propto\;\mathrm{Var}_{\hat{y}_{t}\sim p_{t}}\!\bigl[\log p_{t}(\hat{y}_{t})-\log q_{t}(\hat{y}_{t})\bigr], (8) where the right-hand variance is over per-position token sampling.

The OPD variance in ( 8 ) does not vanish as p t → q t p_{t}\!\to\!q_{t} , and through the score-function term ∇ θ ​ log ​ p t ​ ( y ^ t ) \nabla_{\theta}\log p_{t}(\hat{y}_{t}) it dominates the policy gradient late in training; this is the mechanism behind the late-stage stagnation of pure OPD (Limitation 1 in § 1 ). OPRD adds zero conditional variance and therefore provides a stable optimization signal even after the output distribution has nearly converged.

##### Comparison with top- k k : no truncation bias.

Top- k k OPD eliminates the per-position sampling variance of sampled-token OPD by deterministically selecting the k k highest-probability tokens. However, it introduces a truncation bias : the loss is computed only over the student’s top- k k support S t S_{t} , so any teacher probability mass outside S t S_{t} is invisible to the gradient. When the student’s top- k k set does not coincide with the teacher’s (a common situation early in training and on difficult tokens), the student receives no signal to shift probability toward the teacher’s preferred tokens that lie outside S t S_{t} . This bias is systematic and cannot be reduced by training longer or increasing the batch size. OPRD avoids this problem entirely: its MSE objective ‖ h θ , t ( l ) − h T , t ( l ) ‖ 2 2 \|h_{\theta,t}^{(l)}-h_{T,t}^{(l)}\|_{2}^{2} operates on continuous d d -dimensional vectors with no token selection or truncation step, so every dimension of the teacher’s hidden state contributes to the gradient at every supervised position.

###### Theorem 2 (Hidden-state information beyond the LM head) .

Let W head ∈ ℝ | 𝒱 | × d W_{\mathrm{head}}\!\in\!\mathbb{R}^{|\mathcal{V}|\times d} have singular values σ 1 ≥ ⋯ ≥ σ d > 0 \sigma_{1}\!\geq\!\cdots\!\geq\!\sigma_{d}\!>\!0 with right-singular vectors v 1 , … , v d v_{1},\ldots,v_{d} , and define the effective null space 𝒩 W ≜ { Δ ​ h ∈ ℝ d : W head ​ Δ ​ h ∈ span ⁡ { 𝟏 } } \mathcal{N}_{W}\triangleq\{\Delta h\in\mathbb{R}^{d}:W_{\mathrm{head}}\,\Delta h\in\mathrm{span}\{\mathbf{1}\}\} , i.e., the set of hidden-state perturbations whose image under W head W_{\mathrm{head}} is an additive softmax-invariant shift. For any last-layer student/teacher hidden states h θ , h T ∈ ℝ d h_{\theta},h_{T}\!\in\!\mathbb{R}^{d} and any output-space OPD loss ℓ out \ell_{\mathrm{out}} (sampled-token, top- k k , or full-vocabulary reverse KL), ℓ out ​ ( h θ , h T ) = 0 whenever h θ − h T ∈ 𝒩 W , \ell_{\mathrm{out}}(h_{\theta},h_{T})=0\quad\text{whenever}\quad h_{\theta}-h_{T}\in\mathcal{N}_{W}, (9) and along h θ − h T = α ​ v d h_{\theta}-h_{T}=\alpha v_{d} with ‖ v d ‖ = 1 \|v_{d}\|=1 , ‖ h θ − h T ‖ 2 / ℓ out ​ ( h θ , h T ) ≳ ( σ 1 / σ d ) 2 , \|h_{\theta}-h_{T}\|^{2}/\ell_{\mathrm{out}}(h_{\theta},h_{T})\;\gtrsim\;(\sigma_{1}/\sigma_{d})^{2}, (10) where ≳ \gtrsim hides a constant depending only on ℓ out \ell_{\mathrm{out}} and the logit range (made precise in Section B.5 ).

The ratio in ( 10 ) scales as ( σ 1 / σ d ) 2 (\sigma_{1}/\sigma_{d})^{2} , which is typically very large for production LLMs due to the ill-conditioned singular spectrum of W head W_{\mathrm{head}} . This means hidden-state deviations along low-singular-value directions can be orders of magnitude larger than along top directions while producing the same output-space loss; moreover output-space OPD has no mechanism to constrain intermediate hidden states h ( l ) h^{(l)} for l < L l\!<\!L . OPRD ( 6 ) penalizes exactly the directions in 𝒩 W \mathcal{N}_{W} and supervises any subset of intermediate layers, exposing (layers × \times positions × \times hidden-dim) scalars of structural information per sample that the LM-head projection necessarily compresses away (Limitation 2 in § 1 ).

### 3.3 OPRD-Bridge: Cross-Architecture Extension

The OPRD-Vanilla objective defined in § 3.1 implicitly assumes that the student and teacher share a well-aligned representation space : the MSE in Eq. ( 6 ) directly compares h θ , t ( l ) h_{\theta,t}^{(l)} and h T , t ( l ) h_{T,t}^{(l)} in the same ℝ d \mathbb{R}^{d} , which is meaningful only when corresponding dimensions carry comparable semantics. Sharing the same model architecture is a sufficient condition but not the fundamental one. In the same-architecture experiments of § 3.1 , the two models share a common origin: JustRL-1.5B (teacher) was obtained by applying RL to R1-Distill-1.5B (student), which perturbs the representation space only mildly; the two models therefore retain a high degree of representational alignment, and the full ℝ d \mathbb{R}^{d} channel acts as a high-quality all-pass filter that transmits every dimension of the teacher’s hidden state faithfully. Conversely, two models with identical architecture but trained from different initialisations or with different tokenizers would have misaligned representation spaces, making direct MSE comparison meaningless despite matching dimensionality.

The true bottleneck, therefore, is representational alignment , not architectural identity. When this alignment is absent (as is typically the case for models that differ in depth ( L S ≠ L T L_{S}\neq L_{T} ), width ( d S ≠ d T d_{S}\neq d_{T} ), or training history), the hidden states are incommensurable, and we need a mechanism to bridge the gap. This section introduces OPRD-Bridge , which identifies and exploits a shared low-rank structure between heterogeneous models to construct such a bridge.

The key observation is that although the full representations are incomparable, their principal variation directions are not. We first demonstrate this empirically (§ 3.3.1 ), then show how to exploit it (§ 3.3.2 , 3.3.3 ), and finally explain why the resulting design takes the specific form it does (§ 3.3.4 ).

#### 3.3.1 The Shared Low-Rank Structure

Before presenting the method, we establish the empirical fact that motivates it. We take a Qwen3-4B teacher (36 layers, d T = 2560 d_{T}\!=\!2560 ) and a Qwen3-1.7B student (28 layers, d S = 2048 d_{S}\!=\!2048 ) as an illustrative example, sample 2K prompts from DAPO-Math-17K, generate responses with the student, and collect both models’ hidden states on these responses. We then perform PCA on the centered teacher hidden states at each layer, extracting the top- r r principal directions as a basis P T ∈ ℝ r × d T P_{T}\in\mathbb{R}^{r\times d_{T}} . Next, we train a simple linear map P S ∈ ℝ r × d S P_{S}\in\mathbb{R}^{r\times d_{S}} to minimize ‖ P S ​ h S − P T ​ ( h T − μ T ) ‖ 2 2 \|P_{S}h_{S}-P_{T}(h_{T}-\mu_{T})\|_{2}^{2} with both models frozen.

The result is striking. At r = 8 r\!=\!8 , the cosine similarity between P S ​ ( h S ) P_{S}(h_{S}) and P T ​ ( h T − μ T ) P_{T}(h_{T}-\mu_{T}) reaches 95% averaged across all layer pairs. Eight dimensions suffice to capture the shared structure between two models that, in their full representation spaces, show zero alignment.

Equally revealing: this similarity decreases as r r increases. At r = 32 r\!=\!32 it drops to 94.1 % 94.1\% , at r = 256 r\!=\!256 to 87.9 % 87.9\% , and continues declining to 77.0 % 77.0\% at full rank r = 2048 r\!=\!2048 . This is not a failure of the method; it is a signal about the data. The shared structure between teacher and student is concentrated in very few principal directions. Beyond those directions, the two models diverge, encoding architecture-specific information that is not shared and should not be distilled.

This observation has a direct methodological implication: the bridge should be low-rank by design, not as a computational shortcut, but because the shared structure itself is low-rank. Higher rank does not mean more information transfer; it means more noise.

#### 3.3.2 Stage 1: Bridge Construction

The bridge is built with both model weights frozen ; only the projectors are involved. We write h S h_{S} for the student hidden states in this stage (emphasizing that the student backbone is fixed), reserving h θ h_{\theta} for Stage 2 where the backbone parameters θ \theta are updated.

We first establish a layer correspondence. When L S ≠ L T L_{S}\neq L_{T} , we pair each student layer l S l_{S} with a teacher layer via proportional spacing: ϕ ⁡ ( l S ) = round ⁡ ( l S − 1 L S − 1 ⋅ ( L T − 1 ) ) + 1 , \phi(l_{S})=\mathrm{round}\!\left(\frac{l_{S}-1}{L_{S}-1}\cdot(L_{T}-1)\right)+1, (11) so that the first layers align, the last layers align, and intermediate layers are evenly distributed.

For each teacher layer l T l_{T} , we compute the PCA basis from the centered hidden states: P T ( l T ) = TopPrincipalDirections ⁡ ( h T ( l T ) − μ T ( l T ) , r ) ∈ ℝ r × d T . P_{T}^{(l_{T})}=\mathrm{TopPrincipalDirections}\!\left(h_{T}^{(l_{T})}-\mu_{T}^{(l_{T})},\;r\right)\in\mathbb{R}^{r\times d_{T}}. (12) This is computed once and permanently frozen. It captures the directions along which the teacher’s representations vary most. In practice, we obtain P T ( l T ) P_{T}^{(l_{T})} via PCA on the sample covariance rather than a thin SVD of the hidden-state matrix. Stacking the teacher’s response-token hidden states into H ∈ ℝ n × d T H\in\mathbb{R}^{n\times d_{T}} , the two are equivalent up to centering: the top- r r right singular vectors of the centered matrix H − 𝟏 ​ μ T ⊤ H-\mathbf{1}\mu_{T}^{\top} coincide with the top- r r eigenvectors of the sample covariance Σ = 1 n − 1 ​ ( H − 𝟏 ​ μ T ⊤ ) ⊤ ​ ( H − 𝟏 ​ μ T ⊤ ) ∈ ℝ d T × d T \Sigma=\frac{1}{n-1}(H-\mathbf{1}\mu_{T}^{\top})^{\top}(H-\mathbf{1}\mu_{T}^{\top})\in\mathbb{R}^{d_{T}\times d_{T}} . We therefore form Σ \Sigma and take its eigendecomposition, which is far cheaper than an SVD of H H in the typical regime n ≫ d T n\gg d_{T} (the cost is governed by the d T × d T d_{T}\times d_{T} eigensolve rather than the large row count n n ), and we subsample at most 16,384 16{,}384 token rows to estimate Σ \Sigma . A single eigendecomposition per layer yields the full ordered basis; the rank- r r projector for any r r is then obtained by slicing the top- r r eigenvectors, without re-running the decomposition.

For each student layer l S l_{S} , we then train a linear projector P S ( l S ) ∈ ℝ r × d S P_{S}^{(l_{S})}\in\mathbb{R}^{r\times d_{S}} to minimize: ℒ bridge = ∑ l S ∑ t ‖ P S ( l S ) ​ h S , t ( l S ) − P T ( ϕ ⁡ ( l S ) ) ​ ( h T , t ( ϕ ⁡ ( l S ) ) − μ T ( ϕ ⁡ ( l S ) ) ) ‖ 2 2 . \mathcal{L}_{\mathrm{bridge}}=\sum_{l_{S}}\sum_{t}\left\|P_{S}^{(l_{S})}h_{S,t}^{(l_{S})}-P_{T}^{(\phi(l_{S}))}\!\bigl(h_{T,t}^{(\phi(l_{S}))}-\mu_{T}^{(\phi(l_{S}))}\bigr)\right\|_{2}^{2}. (13) After 20 epochs of training (with both models frozen), P S P_{S} converges and is also frozen. The bridge is now complete: a pair of fixed linear maps ( P T , P S ) (P_{T},P_{S}) that project both architectures into a shared r r -dimensional subspace where their representations are directly comparable.

#### 3.3.3 Stage 2: Bridge-Based Distillation

With the bridge frozen, we perform on-policy representation distillation. The student generates rollouts, both models perform forward passes, and the loss is computed through the frozen bridge : ℓ ( l ) ​ ( θ , y ^ ) = 1 ∑ t m t ​ ∑ t = 1 T m t ​ ‖ P S ( l ) ​ ( h θ , t ( l ) ) − P T ( ϕ ⁡ ( l ) ) ​ ( h T , t ( ϕ ⁡ ( l ) ) − μ T ( ϕ ⁡ ( l ) ) ) ‖ 2 2 , \ell^{(l)}(\theta;\hat{y})=\frac{1}{\sum_{t}m_{t}}\sum_{t=1}^{T}m_{t}\,\left\|P_{S}^{(l)}(h_{\theta,t}^{(l)})-P_{T}^{(\phi(l))}\!\bigl(h_{T,t}^{(\phi(l))}-\mu_{T}^{(\phi(l))}\bigr)\right\|_{2}^{2}, (14) where m t m_{t} is the same position mask as in Eq. ( 6 ) (defaulting to the last k = 2000 k\!=\!2000 tokens). The full objective averages over layers: ℒ OPRD-Bridge ( θ ) = 𝔼 x , y ^ ∼ π θ ( ⋅ ∣ x ) [ 1 | ℒ layer | ∑ l ∈ ℒ layer ℓ ( l ) ( θ ; y ^ ) ] . \mathcal{L}_{\text{OPRD-Bridge}}(\theta)=\mathbb{E}_{x,\,\hat{y}\sim\pi_{\theta}(\cdot\mid x)}\left[\frac{1}{|\mathcal{L}_{\mathrm{layer}}|}\sum_{l\in\mathcal{L}_{\mathrm{layer}}}\ell^{(l)}(\theta;\hat{y})\right]. (15) Only the student backbone θ \theta receives gradients. In practice, we L2-normalize both projected vectors before computing MSE, making the loss scale-invariant. As with OPRD-Vanilla, the bridge objective composes additively with any output-space OPD variant via Eq. ( 7 ).

Algorithm 1 summarizes the complete pipeline.

#### 3.3.4 Design Philosophy

Every design choice in OPRD-Bridge follows from a single principle: the bridge should behave like the vocabulary in logit distillation , a fixed, pre-established interface that neither model modifies during training. The frozen, low-rank bridge plays two complementary roles:

• A stable interface that preserves pre-existing alignment. The projectors ( P T , P S ) (P_{T},P_{S}) encode an alignment that already exists between the two models’ representations before any distillation takes place; Stage 1 merely discovers it and freezes it into a fixed pair of linear maps. This mirrors logit distillation, where the shared vocabulary provides a stable coordinate system that neither model modifies during training: if this common reference frame changed, the optimization target would be non-stationary and training would destabilize. Freezing the bridge in Stage 2 ensures the on-policy training signal flows through this stable channel rather than destroying it. If P S P_{S} were trained jointly with the backbone, the projection and the target would shift simultaneously, erasing the very alignment the bridge was built to exploit; empirically, joint training indeed performs worse.

• A low-pass filter that suppresses high-frequency noise. The shared structure between heterogeneous models is intrinsically low-rank: the top- r r principal components correspond to the “low-frequency” modes where teacher and student are already highly aligned, while the orthogonal complement carries “high-frequency” architecture-specific variation that acts as noise for distillation. By projecting through a rank- r r bridge, we retain the well-aligned signal and discard the misaligned noise, which is precisely why Stage 2 training remains stable even under on-policy distribution shift. It is instructive to contrast this with the two all-pass alternatives. Full-vocabulary logit distillation transmits every dimension of the output space through the shared vocabulary, a high-quality all-pass channel, but at O ⁡ ( | 𝒱 | ) O(|\mathcal{V}|) cost and without any denoising. OPRD-Vanilla likewise operates as an all-pass channel over the full ℝ d \mathbb{R}^{d} representation space; this works precisely because same-architecture models with shared initialisation are already well-aligned in every direction, so no dimension is noise. When this alignment breaks down (different depth, width, or training history), the all-pass property becomes a liability: high-frequency directions carry misaligned noise, and a low-pass bridge is needed to filter it out.

Table 1 makes the bridge–vocabulary analogy explicit.

Why PCA for the teacher side? Because the Platonic Representation Hypothesis predicts that strong models converge in their principal variation directions [ 15 ] , and PCA extracts exactly these directions. It is also deterministic, data-efficient (2K prompts suffice), and introduces no trainable parameters on the teacher side.

Why such a low rank? Because the shared structure is low-rank: our pre-experiment shows 95% alignment at r = 8 r\!=\!8 , reflecting the concentration of task-relevant information in very few directions. The rank is therefore not a computational budget; it is a statement about the geometry of the shared representation, and the low-pass property described above is what makes the bridge a robust supervision channel. We formalize this intuition in the following theorem (stated informally; the precise version with proof is in Section B.6 ).

###### Theorem 3 (Optimality and bias–variance trade-off of the low-rank bridge, informal) .

Assume teacher hidden states are drawn from a distribution with covariance Σ T \Sigma_{T} (eigenvalues λ 1 ≥ ⋯ ≥ λ d T \lambda_{1}\!\geq\!\cdots\!\geq\!\lambda_{d_{T}} ), and that the cross-model alignment in direction i i is ρ i ∈ [ 0 , 1 ] \rho_{i}\in[0,1] (decreasing in i i : high-eigenvalue directions are better aligned). Then: 1. (Rate–distortion optimality.) Among all rank- r r linear encodings of the teacher representation, PCA minimizes the expected distillation error under Gaussian assumptions. The bridge is the information-theoretically optimal channel at capacity r r .

2. (Bias–variance decomposition.) The expected distillation error decomposes as ℰ ( r ) = ∑ i > r λ i ​ ρ i 2 ⏟ Bias : discarded ​ aligned ​ signal + ∑ i = 1 r λ i ​ ( 1 − ρ i 2 ) ⏟ Variance : transmitted ​ misaligned ​ noise . \mathcal{E}(r)=\underbrace{\textstyle\sum_{i>r}\lambda_{i}\,\rho_{i}^{2}}_{\mathrm{Bias:\ discarded\ aligned\ signal}}\;+\;\underbrace{\textstyle\sum_{i=1}^{r}\lambda_{i}\,(1-\rho_{i}^{2})}_{\mathrm{Variance:\ transmitted\ misaligned\ noise}}. (16) When ρ i \rho_{i} decreases with i i (empirically verified), there exists an optimal rank r ∗ r^{*} that minimizes ℰ ⁡ ( r ) \mathcal{E}(r) : below r ∗ r^{*} , bias dominates (useful signal is discarded); above r ∗ r^{*} , variance dominates (misaligned noise is transmitted).

The theorem explains three empirical observations simultaneously: (i) why a very low rank suffices (the λ i \lambda_{i} decay fast and ρ i \rho_{i} decay fast, so both bias and variance are small at r ∗ ≈ 8 r^{*}\!\approx\!8 ); (ii) why increasing rank beyond the sweet spot hurts alignment (variance term grows); and (iii) why freezing the bridge is critical (a moving P S P_{S} would invalidate the ρ i \rho_{i} estimates on which the optimality rests).

Finally, we note that because the bridge performs alignment in representation space rather than in the output space, it is decoupled from the vocabulary: the teacher and student need not share a tokenizer. This opens a path toward cross-tokenizer and potentially cross-modal distillation, where the vocabulary-based alignment channel is unavailable.

## 4 Experiments

We evaluate both OPRD variants: OPRD-Vanilla in the same-architecture setting (§ 4.1 ), and OPRD-Bridge in the cross-architecture setting (§ 4.2 ).

### 4.1 OPRD-Vanilla: Same-Architecture Distillation

We evaluate OPRD-Vanilla on competition-level mathematical reasoning, against (i) a frozen teacher and an unmodified student baseline, and (ii) two strong on-policy distillation baselines that share the same on-policy rollout and teacher forward pass as OPRD but extract supervision from the LM-head output. The experiments test the two predictions of § 3.2 : OPRD provides a lower-noise, structurally richer training signal than any output-space OPD variant, and should therefore close the student–teacher gap that pure OPD cannot.

#### 4.1.1 Experimental Setup

##### Models.

Following [ 25 ] , we use JustRL-Deepseek-1.5B [ 10 ] (denoted JustRL-1.5B ) as the (frozen) teacher and DeepSeek-R1-Distill-Qwen-1.5B [ 9 ] (denoted R1-distill-1.5B ) as the student. Both models share the Qwen2.5-1.5B backbone ( L = 28 L\!=\!28 transformer layers, d = 1536 d\!=\!1536 hidden dimension, | 𝒱 | ≈ 151 |\mathcal{V}|\!\approx\!151 K vocabulary) and the same LM head W head W_{\mathrm{head}} , so OPRD-Vanilla’s hidden-state targets are directly comparable across the two models ( d S = d T d_{S}\!=\!d_{T} ). The student starts from the public R1-distill-1.5B checkpoint, which already places it close to but well below the teacher in reasoning ability ( Table 2 ).

##### Training data.

On-policy prompts x x are drawn from DAPO-Math-17K [ 45 ] . For each prompt the student samples 2 2 responses y ^ ∼ π θ ( ⋅ ∣ x ) \hat{y}\sim\pi_{\theta}(\cdot\!\mid\!x) at temperature 1.0 1.0 with a max generation length of 16,384 16{,}384 tokens; we use a global batch of 8 8 prompts per step.

##### Distillation objectives.

We compare three on-policy distillation variants, all sharing the same rollouts y ^ \hat{y} and the same single teacher forward pass per rollout: • OPD top-1 (sampled-token reverse KL): the per-position estimator ℓ t = log ⁡ p t ​ ( y ^ t ) − log ⁡ q t ​ ( y ^ t ) \ell_{t}=\log p_{t}(\hat{y}_{t})-\log q_{t}(\hat{y}_{t}) evaluated only at the sampled token y ^ t \hat{y}_{t} .

• OPD top-16 : the per-position estimator ∑ v ∈ 𝒱 16 t p t ​ ( v ) ​ [ log ⁡ p t ​ ( v ) − log ⁡ q t ​ ( v ) ] \sum_{v\in\mathcal{V}_{16}^{t}}\,p_{t}(v)\,[\log p_{t}(v)-\log q_{t}(v)] over the top- 16 16 tokens of p t p_{t} , a strictly informative-superset of OPD top-1 .

• OPRD-Vanilla (ours): the hidden-state objective ( 6 ) with ℒ layer = { 1 , … , L } \mathcal{L}_{\mathrm{layer}}\!=\!\{1,\ldots,L\} (all 28 28 layers) and 𝒫 ⁡ ( y ^ ) \mathcal{P}(\hat{y}) set to the last k = 2000 k\!=\!2000 response tokens (i.e. the suffix in which the chain-of-thought converges to a final answer); reported in the OPRD-only setting ( μ = 0 \mu\!=\!0 in ( 7 )).

##### Optimization.

All three methods are trained for 500 500 optimizer steps with AdamW (peak learning rate × 10 − 5 1\!\times\!10^{-5} , linear warm-up over 3 % 3\% of total steps, cosine decay), bf16 mixed precision, and FSDP over × 8\!\times\! A100 (80G) GPUs at a micro-batch of B = 8 B\!=\!8 and a maximum response length of T = 16,384 T\!=\!16{,}384 .

##### Evaluation.

We report Avg@16 (average accuracy across 16 16 independently sampled responses per prompt) at decoding temperature 0.7 0.7 on three competition-level mathematical reasoning benchmarks: AIME 2024 ( AIME24 , 30 30 problems), AIME 2025 ( AIME25 , 30 30 problems), and AIMO (AI-MO/aimo-validation-amc, comprising AMC 2022 and AMC 2023, 83 83 problems). Final answers are extracted with the standard boxed parser and graded by exact-match against the official solution.

#### 4.1.2 Main Results

Table 2 reports Avg@16 for the teacher, the unmodified student, and the three on-policy distillation methods; Figure 4 shows the corresponding training dynamics (discussed in detail in § 4.1.3 ). Three observations follow.

(1) Both OPD variants improve over the student but plateau noticeably below the teacher. The student starts from a 17.9 17.9 -/ 13.7 13.7 -/ 17.3 17.3 -point gap to the teacher on AIME24/AIME25/AIMO. OPD top-1 closes most of this gap on AIME25 (to within 2.1 2.1 points) but leaves 8.5 8.5 / 2.5 2.5 points on AIME24/AIMO; enriching the supervision to OPD top-16 helps substantially on AIME24 ( + 4.8 +4.8 ) and marginally on AIME25 ( + 0.5 +0.5 ) yet loses ground on AIMO ( − 0.5 -0.5 ). The absence of a clean ordering between top-1 and top-16 (more tokens in the loss is supposed to be strictly more informative) suggests that the output-space paradigm itself is the bottleneck: both variants are constrained by the LM-head information bottleneck ( Theorem 2 ), and top- k k ’s truncation bias means that enriching the support does not guarantee monotonic improvement.

(2) OPRD effectively closes the student–teacher gap. OPRD reaches 49.8 49.8 on AIME24, 34.6 34.6 on AIME25, and 79.1 79.1 on AIMO, leaving only 1.0 1.0 / 1.0 1.0 / 0.4 0.4 points to the teacher, all within the variance of 16 16 -sample Avg@16 evaluation, so the AIMO result is effectively a tie with the teacher (underlined in Table 2 ). Relative to the better OPD baseline on each benchmark, OPRD gains + 2.7 +2.7 / + 0.6 +0.6 / + 2.1 +2.1 points; relative to the unmodified student it gains + 16.9 +16.9 / + 12.7 +12.7 / + 16.9 +16.9 points. The advantage is most striking on AIMO, where OPRD recovers essentially all of the 17.3 17.3 -point student–teacher gap that no output-space variant fully bridges. OPRD’s gradient is conditionally deterministic ( Theorem 1 ), avoiding the late-stage variance collapse that limits OPD; it also exposes per-layer structural information that the LM-head projection compresses away ( Theorem 2 ), supervising directions in 𝒩 W \mathcal{N}_{W} that any output-space objective treats as invisible.

#### 4.1.3 Training Dynamics

The end-of-training numbers in Table 2 are only one slice of the story; we now examine how each method gets there. Three complementary views (per-step accuracy, response-length behaviour, and OPRD’s own internal alignment metric) together paint a consistent picture of OPD stalling in the late-training regime predicted by Theorem 1 , while OPRD continues to make progress.

##### Accuracy curves: OPRD climbs monotonically, OPD plateaus.

Figure 4 compares OPRD step-by-step against OPD top- 1 1 (top row) and OPD top- 16 16 (bottom row) on all three benchmarks; raw curves are drawn at α = 0.5 \alpha\!=\!0.5 and the solid curve with markers is the 5 5 -step centred rolling mean. The two methods in each panel share the same initialisation and quickly enter qualitatively different regimes: both OPD variants lift accuracy in the first few dozen steps but then plateau or oscillate without further improvement , whereas OPRD continues to climb essentially monotonically until it reaches the teacher level. Enriching the OPD supervision from top- 1 1 to top- 16 16 narrows the asymptotic gap to OPRD on AIME24 but does not change the qualitative shape: OPD top- 16 16 also plateaus, and on AIMO it does so ∼ 2.6 \sim\!2.6 points below OPRD despite passing strictly more output-distribution information into the loss. This is the SNR-collapse prediction of Theorem 1 in pictures: as p t → q t p_{t}\to q_{t} , the OPD gradient’s signal-to-noise ratio collapses and additional output-layer information cannot rescue the per-token sampling noise; only OPRD’s deterministic, hidden-state-level signal continues to make progress.

##### Behavioural view: OPRD produces shorter, more efficient reasoning.

The accuracy curves answer whether a method keeps improving; a complementary question is how the policy changes. Figure 5 reports the mean rollout length response_length/mean for the same three runs. OPRD converges to a mean response length of ∼ 5,700 {\sim}5{,}700 tokens, substantially shorter than the ∼ 7,000 {\sim}7{,}000 tokens produced by both OPD variants. Combined with OPRD’s higher accuracy ( Table 2 ), this indicates that hidden-state supervision guides the student toward more concise reasoning chains: the student learns to reach the correct answer with fewer tokens rather than relying on longer, less directed exploration. This also translates to a practical inference-time efficiency gain, since shorter responses require proportionally less compute at deployment.

##### Internal view: OPRD’s own loss is being optimised end-to-end.

A final, internal diagnostic is whether the representation-level loss OPRD is supposed to minimise actually decreases along training. Figure 6 plots rep/cosine_similarity , the cosine similarity between π θ \pi_{\theta} ’s and π T \pi_{T} ’s hidden states averaged across all transformer layers and OPRD-supervised positions, for the OPRD-only run from Table 2 . The curve rises sharply in the first few dozen steps and then drifts upward steadily for the rest of training. Two consequences follow: (i) the OPRD objective is well-conditioned for end-to-end optimisation at this scale: the gradient produced by ( 6 ) is consistent enough to monotonically pull the supervised hidden states towards the teacher’s; (ii) the downstream gains of Table 2 are matched by a corresponding internal trend: OPRD is improving on exactly the quantity its loss is defined on, confirming that the improvement, not a coincidental rollout-distribution shift, drives the gains.

#### 4.1.4 Efficiency

The OPRD loss path is computed entirely before the LM head: it never materializes the [ B , T , | 𝒱 | ] [B,T,|\mathcal{V}|] logits tensor on the student side, never invokes the | 𝒱 | |\mathcal{V}| -way log_softmax , and never backpropagates through W head ∈ ℝ | 𝒱 | × d W_{\mathrm{head}}\in\mathbb{R}^{|\mathcal{V}|\times d} for the distillation term. As a direct consequence, OPRD-only training is strictly cheaper than any output-space OPD variant at the same rollout/teacher budget. Table 3 quantifies this on the same training configuration as our main results.

Memory. The actor-update transient footprint ( Δ \Delta peak, the most direct proxy for the loss path’s own cost since always-resident state is subtracted out) is 30.2 30.2 GB for OPD top-1 and 45.0 45.0 GB for OPD top-16, vs. only 20.5 20.5 GB for OPRD, a 32 32 % and 54 54 % reduction, or equivalently a 1.47 × 1.47\times and 2.20 × 2.20\times ratio. The gap is dominated by the [ B , T , | 𝒱 | ] [B,T,|\mathcal{V}|] logits tensor (and its gradient buffer for top- k k ), which scales with | 𝒱 | ≈ 151 |\mathcal{V}|\!\approx\!151 K but is entirely absent in the OPRD-only loss path. The roughly 10 10 – 25 25 GB of saved transient memory is hardware-relevant: on 80 80 GB-class accelerators it is enough to either enlarge the micro-batch or extend the context at the same hardware budget.

Wall-clock. At identical schedules ( 500 500 steps, same rollout, same teacher forward pass), OPRD finishes in 563 563 minutes vs. 813 813 / 812 812 minutes for OPD top-1 / top-16, a 31 31 % wall-clock reduction, equivalent to a 1.44 × 1.44\times speed-up. We attribute this to the fact that the two OPD variants take essentially the same time, consistent with the observation that the cost is dominated by the [ B , T , | 𝒱 | ] [B,T,|\mathcal{V}|] matrix multiplication and log_softmax rather than by the top- k k slicing itself.

Putting it together. Combining Table 3 with the accuracy results in Table 2 , OPRD strictly Pareto-dominates both OPD baselines on this benchmark suite: at ∼ 69 % \sim\!69\% of the wall-clock and 46 46 – 68 % 68\% of the actor-update transient memory ( Δ \Delta peak), it reaches accuracies that are + 0.6 +0.6 to + 2.7 +2.7 points above the better OPD baseline and effectively close the gap to the teacher. These efficiency gains are a secondary consequence of OPRD’s design (the primary motivation, as developed in § 3.2 , is informational; see Theorem 2 ), but they make OPRD a more economical training objective in practice as well. We note that our current implementation reuses the existing OPD training framework without OPRD-specific infrastructure optimisation (e.g., the teacher still computes and discards the full logits tensor even though OPRD does not consume it). With a dedicated implementation that eliminates these redundant computations, we expect both peak memory and wall-clock to decrease further.

#### 4.1.5 Mechanistic Analysis

The experiments above show that OPRD outperforms OPD; we now ask why . We first study the effect of composing OPRD with OPD via the mixing weight μ \mu , and empirically motivate the choice of supervised positions. We then track three complementary diagnostics along training for the composite runs ℒ OPD + μ ⋅ ℒ OPRD \mathcal{L}_{\mathrm{OPD}}+\mu\cdot\mathcal{L}_{\mathrm{OPRD}} with μ ∈ { 0 , 1 , 10 } \mu\!\in\!\{0,1,10\} to reveal a consistent mechanistic picture: OPRD pre-aligns the student’s hidden states to the teacher’s, which propagates back to (a) a smaller residual policy-gradient signal, (b) higher next-token top- k k agreement, and (c) a student exploration distribution whose shape matches the teacher’s.

##### Composing OPD with OPRD ( μ \mu sweep).

Equation 7 suggests that OPRD can also be added on top of existing OPD objective, rather than used as a standalone replacement. We test this for the simplest output-space baseline, sampled-token OPD (i.e. OPD top- 1 1 ), by training the composite loss ℒ OPD + μ ⋅ ℒ OPRD \mathcal{L}_{\mathrm{OPD}}+\mu\cdot\mathcal{L}_{\mathrm{OPRD}} for μ ∈ { 0 , 1 , 10 } \mu\in\{0,1,10\} , keeping all other knobs identical to § 4.1.1 . Figure 7 shows that AIME24 avg@16 rises monotonically with μ \mu : from the vanilla OPD top- 1 1 baseline at 42.3 42.3 ( μ = 0 \mu\!=\!0 ), to 47.7 47.7 with a light OPRD contribution ( μ = 1 \mu\!=\!1 , + 5.4 +5.4 pt, already exceeding the OPD top- 16 16 baseline of 47.1 47.1 from Table 2 ), to 50.2 50.2 with a stronger contribution ( μ = 10 \mu\!=\!10 , + 2.5 +2.5 pt further, essentially matching the teacher’s 50.8 50.8 ). The trend confirms two things: (i) the hidden-state signal that OPRD exposes is additive to the output-space signal that OPD already uses, consistent with the information-bottleneck view of Theorem 2 ; and (ii) the improvement is monotonic in μ \mu within the swept range, so the composition is robust to the mixing weight and does not require careful tuning. We therefore view ℒ OPD + μ ⋅ ℒ OPRD \mathcal{L}_{\mathrm{OPD}}+\mu\cdot\mathcal{L}_{\mathrm{OPRD}} as a drop-in upgrade for existing OPD pipelines.

##### Where does the student diverge from the teacher? (motivation for last- k k supervision).

A natural design question for OPRD is which response positions the projector 𝒫 ⁡ ( y ^ ) \mathcal{P}(\hat{y}) in ( 6 ) should select. We answer this empirically by directly measuring where along the response the student and teacher representations still disagree. For the student initialisation π θ ( 0 ) = \pi_{\theta}^{(0)}\!=\! R1-distill-1.5B and the teacher π T = \pi_{T}\!=\! JustRL-1.5B , we sample on-policy rollouts from the student, run both models forward on each rollout, and compute the cosine similarity between their last-layer hidden states, restricted to either the first k k or the last k k tokens of every response. Figure 8 reports this similarity as a function of k k .

Two patterns emerge. (i) The early response is already teacher-aligned. The first- k k curve stays above 97 % 97\% for every k ≤ 1600 k\!\leq\!1600 and peaks at 97.69 % 97.69\% at k = 1600 k\!=\!1600 , meaning the prompt-following preamble and the opening of the chain-of-thought are essentially already matched by the student; there is little headroom for representation-level supervision to act on. (ii) The late response is where the gap lives. The last- k k curve starts at only 91.65 % 91.65\% for k = 50 k\!=\!50 and remains ≥ 4 \geq\!4 points below the first- k k curve until k k approaches the full response length, at which point both curves converge to the whole-sequence similarity of 95.42 % 95.42\% by construction. Almost all of the student–teacher representational disagreement is concentrated in the tail of the response, precisely where the chain-of-thought commits to a final answer.

This directly motivates our default choice 𝒫 ⁡ ( y ^ ) = last- ​ k \mathcal{P}(\hat{y})\!=\!\textsc{last-}k in § 4.1.1 : supervising the last k k tokens targets exactly the positions in which the student still deviates from the teacher, while sparing compute on the early positions where the signal has already been absorbed. It also explains why a small budget ( k = 2000 ≪ | y ^ | k\!=\!2000\ll|\hat{y}| on average) suffices to recover the gains reported in Table 2 , since OPRD’s representation loss is not diluted across positions that carry no residual signal.

##### (a) Policy-gradient loss: OPRD accelerates distillation and validates the bottleneck theory.

Figure 9 tracks actor/pg_loss along training for the OPD top- 1 1 + + OPRD composite runs with μ ∈ { 0 , 1 , 10 } \mu\!\in\!\{0,1,10\} . Two observations stand out. First , all three runs exhibit a pronounced loss spike during training, likely reflecting a phase transition in the student’s policy as it reorganises to absorb the teacher’s behaviour (the precise mechanism is under active investigation). Crucially, adding OPRD causes this spike to arrive earlier : the μ = 1 \mu\!=\!1 and μ = 10 \mu\!=\!10 spikes precede the μ = 0 \mu\!=\!0 spike, indicating that hidden-state supervision accelerates the distillation dynamics. Second , after the spike all three curves converge to approximately zero PG loss in late training, yet the accuracy gap persists ( + 5.4 +5.4 and + 7.9 +7.9 pt over μ = 0 \mu\!=\!0 on AIME24). This directly corroborates Theorem 2 : once the policy gradient vanishes ( p t ≈ q t p_{t}\approx q_{t} ), the output-space OPD signal can no longer drive further improvement because the remaining student–teacher gap lives in the null space 𝒩 W \mathcal{N}_{W} of the LM head; only OPRD’s representation-level signal, which bypasses this bottleneck, continues to make progress.

##### (b) Top- 16 16 overlap: hidden-state alignment propagates to next-token agreement.

Following Li et al. [25] , who show that higher student–teacher top- k k overlap is a reliable predictor of distillation quality, we log val-topk/overlap_ratio , defined as | top- ​ 16 ​ ( π θ ) ∩ top- ​ 16 ​ ( π T ) | / 16 |\text{top-}16(\pi_{\theta})\cap\text{top-}16(\pi_{T})|/16 (higher is better; 1.0 1.0 means the student’s top- 16 16 set is identical to the teacher’s). Figure 10 compares OPD top- 16 16 alone against OPD top- 16 16 + ⋅ ℒ OPRD +1\!\cdot\!\mathcal{L}_{\mathrm{OPRD}} .

The OPD-only run increases the overlap nearly monotonically throughout training, but its rate of improvement visibly slows after mid-training. The OPD + + OPRD run behaves differently: it initially rises alongside OPD-only, then undergoes a sudden dip in overlap (temporally coinciding with the PG-loss spike of Figure 9 , consistent with the hypothesised phase transition), after which it rebounds rapidly and surpasses the OPD-only curve by a clear margin. The dip-then-surge pattern mirrors the PG-loss spike discussed above and is consistent with OPRD driving the student through a transient reorganisation that ultimately lands it in a higher-overlap regime than OPD alone can reach. The representation-level and output-level supervisions are therefore not redundant: hidden-state alignment translates back into measurable improvement on exactly the metric OPD top- 16 16 was designed to optimise.

##### (c) Predictive entropy.

We log actor/entropy and teacher/entropy (per-token Shannon entropy of π θ \pi_{\theta} and π T \pi_{T} on the same rollout positions) along training for the same OPD top- 1 1 + + OPRD composite runs ( μ ∈ { 0 , 1 , 10 } \mu\!\in\!\{0,1,10\} ). The teacher’s entropy curve serves as a reference: since π T \pi_{T} is frozen, any drift is induced purely by the changing rollout distribution. Figure 11 shows the three runs side by side. All three runs eventually bring the student’s entropy into close agreement with the teacher’s by the end of training (note that the teacher’s entropy also drifts upward as the rollout distribution evolves, so alignment means tracking the teacher, not returning to a fixed level). However, they differ markedly in their early dynamics: each run exhibits an entropy-increase phase in which the student–teacher gap widens before narrowing. Adding OPRD causes this entropy-increase phase to begin earlier , temporally coinciding with the PG-loss spike of Figure 9 : the μ = 10 \mu\!=\!10 onset precedes the μ = 1 \mu\!=\!1 onset, which in turn precedes the μ = 0 \mu\!=\!0 onset. This is consistent with the picture that OPRD accelerates the student’s internal reorganisation (the same phase transition visible in the PG-loss and overlap diagnostics), after which the student’s entropy converges to the teacher’s more quickly.

### 4.2 OPRD-Bridge: Cross-Architecture and Cross-Tokenizer Distillation

We now evaluate OPRD-Bridge in settings where direct hidden-state comparison is impossible without the bridge mechanism introduced in § 3.3 : first in the cross-architecture setting, where the student and teacher differ in depth and width but share a vocabulary; then in the cross-tokenizer setting, where the two models additionally use completely disjoint tokenizers.

#### 4.2.1 Experimental Setup

##### Models.

We use Qwen3-4B [ 39 ] as the (frozen) teacher and Qwen3-1.7B-Base [ 39 ] as the student. The teacher has L T = 36 L_{T}\!=\!36 transformer layers with hidden dimension d T = 2560 d_{T}\!=\!2560 ; the student has L S = 28 L_{S}\!=\!28 layers with d S = 2048 d_{S}\!=\!2048 . Both share the same | 𝒱 | ≈ 151 |\mathcal{V}|\!\approx\!151 K vocabulary, but differ in depth ( 29 % 29\% more layers) and width ( 25 % 25\% wider hidden states), making naïve OPRD-Vanilla inapplicable ( d S ≠ d T d_{S}\neq d_{T} , L S ≠ L T L_{S}\neq L_{T} ). In the cross-tokenizer experiment (§ 4.2.4 ), we additionally test with Phi-4-mini-reasoning [ 38 ] ( L T = 32 L_{T}\!=\!32 , d T = 3072 d_{T}\!=\!3072 , | 𝒱 | ≈ 200 |\mathcal{V}|\!\approx\!200 K, tiktoken-based tokenizer) as teacher, paired with the same Qwen3-1.7B-Base student, where the two models have completely disjoint tokenizers.

##### Bridge construction (Stage 1).

We sample 2000 2000 prompts from DAPO-Math-17K, generate student rollouts, and collect both models’ hidden states. The teacher projector P T ( l ) ∈ ℝ r × d T P_{T}^{(l)}\in\mathbb{R}^{r\times d_{T}} is obtained via PCA (eigendecomposition of the hidden-state covariance) at each layer and permanently frozen. The student projector P S ( l ) ∈ ℝ r × d S P_{S}^{(l)}\in\mathbb{R}^{r\times d_{S}} (linear) is trained for 20 20 epochs to minimize Eq. ( 13 ) with both model backbones frozen, then also frozen. Layer correspondence follows proportional spacing (Eq. ( 11 )). Unless otherwise stated, we use rank r = 8 r\!=\!8 .

##### Distillation (Stage 2).

On-policy prompts are drawn from DAPO-Math-17K. For each prompt the student samples 2 2 responses at temperature 1.0 1.0 with max length 16,384 16{,}384 tokens; global batch size is 8 8 prompts per step. We supervise all 28 28 student layers and apply the position mask to the last 2000 2000 response tokens. The loss is normalized MSE (L2-normalize both projected vectors before MSE). By default we use OPRD-Bridge only. All methods are trained with AdamW (peak learning rate × 10 − 5 1\!\times\!10^{-5} , cosine decay), bf16 mixed precision, and FSDP over × 8\!\times\! A100 (80G) GPUs.

##### Baselines.

We compare against the unmodified Qwen3-1.7B-Base checkpoint (no distillation), OPD top-1 (sampled-token reverse KL), and OPD top-16. Note that output-space OPD baselines can be applied cross-architecture because they only require a shared vocabulary; they therefore serve as the natural comparison for OPRD-Bridge.

##### Evaluation.

We evaluate at decoding temperature 0.7 0.7 with 16 16 independently sampled responses per prompt on three competition-level mathematical reasoning benchmarks: AIME 2024 ( 30 30 problems), AIME 2025 ( 30 30 problems), and AIMO (AMC 2022/2023, 83 83 problems). We report four metrics: Avg@16 (average accuracy across the 16 16 samples), Best@16 (accuracy of the best sample, measuring the capability ceiling), Dist-4g (ratio of unique 4-grams to total 4-grams, measuring lexical diversity), and Avg Len (mean response length in tokens, measuring generation efficiency). Final answers are extracted with the standard boxed parser and graded by exact-match. We save checkpoints periodically and report results from the checkpoint that achieves the best average performance across AIME24, AIME25, and AIMO.

#### 4.2.2 Main Results

Tables 4 and 5 report the main cross-architecture distillation results. Three observations emerge from different facets of the evaluation.

(1) OPRD-Bridge matches OPD’s capability ceiling (Best@16). While OPRD-Bridge’s Avg@16 is lower than OPD top-1 on some benchmarks, its Best@16 tells a different story: on AIME24 and AIME25, OPRD-Bridge achieves 20.0 20.0 and 13.3 13.3 , matching OPD top-1 exactly and substantially outperforming OPD top-16. Best@16 reflects the upper bound of the student’s capability after distillation (the best answer the model can produce across 16 16 attempts) and is therefore a more direct measure of how much teacher knowledge has been successfully transferred. The parity in Best@16 indicates that OPRD-Bridge raises the student’s capability ceiling to the same level as output-space distillation, despite operating through a rank- 8 8 subspace rather than the full | 𝒱 | |\mathcal{V}| -dimensional vocabulary simplex.

(2) OPRD-Bridge produces substantially more diverse reasoning (Dist-4g). OPRD-Bridge achieves Dist-4g scores of 22.6 22.6 / 17.2 17.2 / 21.3 21.3 on AIME24/AIME25/AIMO, dramatically higher than both OPD top-1 ( 6.2 6.2 / 6.4 6.4 / 15.6 15.6 ) and OPD top-16 ( 9.9 9.9 / 11.7 11.7 / 13.6 13.6 ), and approaching the teacher’s own diversity levels ( 24.0 24.0 / 25.4 25.4 / 41.6 41.6 ). This indicates that hidden-state supervision through the bridge produces reasoning chains with far less repetition than output-space distillation. The OPD baselines, by contrast, appear to induce repetitive patterns, likely because the high-variance output-space gradient causes the student to “loop” through similar token sequences rather than making steady forward progress in its reasoning.

(3) OPRD-Bridge generates much shorter, more efficient responses (Avg Len). OPRD-Bridge converges to mean response lengths of 5,909 5{,}909 / 5,234 5{,}234 / 4,855 4{,}855 tokens, which are 2 2 – 3 × 3\times shorter than OPD top-1 ( 19,120 19{,}120 / 17,931 17{,}931 / 11,008 11{,}008 ) and 1.5 1.5 – 2.4 × 2.4\times shorter than OPD top-16 ( 12,222 12{,}222 / 10,175 10{,}175 / 11,833 11{,}833 ). Remarkably, OPRD-Bridge’s response lengths are close to the teacher’s own ( 6,542 6{,}542 / 4,426 4{,}426 / 2,384 2{,}384 ), suggesting that the bridge successfully transfers the teacher’s concise reasoning style in addition to its knowledge. Combined with the Best@16 parity, this means OPRD-Bridge achieves the same capability ceiling at a fraction of the inference cost, a significant practical advantage for deployment.

Summary. The Avg@16 gap between OPRD-Bridge and OPD reflects a difference in consistency (how often the model reaches its best answer), not in capability (what the best answer is). OPRD-Bridge compensates with dramatically better diversity and efficiency: it produces teacher-like reasoning chains that are concise, non-repetitive, and reach the same performance ceiling. This profile (matching capability ceiling with superior efficiency) makes OPRD-Bridge particularly attractive for inference-constrained deployment scenarios where shorter, more reliable responses are preferred over longer, repetitive ones.

(4) Composing OPRD-Bridge with OPD further raises the capability ceiling. The Avg@16 gap of OPRD-Bridge relative to OPD has a clear mechanistic explanation: OPRD-Bridge only trains the student backbone (hidden states), while the LM head W head W_{\mathrm{head}} (the final mapping from hidden states to token distributions) receives no gradient. Even when the backbone representations are well-aligned with the teacher’s, the untrained LM head may not translate this alignment into precise per-token output distributions, reducing sampling consistency. OPD, by contrast, directly supervises the output distribution and therefore calibrates the LM head implicitly through backpropagation.

This suggests a natural two-stage recipe: first use OPRD-Bridge to align the backbone representations, then fine-tune with OPD to calibrate the output distribution. The last row of Tables 4 and 5 (“ ↪ \hookrightarrow OPD top-1”) reports exactly this: we take the OPRD-Bridge checkpoint and continue training with OPD top-1. The results confirm the complementarity: (i) Best@16 rises from 30.8 30.8 to 33.9 \mathbf{33.9} (averaged across benchmarks), surpassing both standalone OPD top-1 ( 30.8 30.8 ) and OPD top-16 ( 27.1 27.1 ) and establishing a new best among all methods. This validates that OPRD-Bridge pre-aligns the backbone into a better initialisation from which OPD can extract more capability. (ii) Avg@16 improves from 11.2 11.2 to 13.6 13.6 , partially closing the gap to standalone OPD top-1 ( 15.3 15.3 ), consistent with the LM-head calibration hypothesis. (iii) The generation quality metrics shift toward a middle ground: Dist-4g decreases from 20.4 20.4 to 15.0 15.0 (still above OPD’s 9.4 9.4 – 11.7 11.7 ) and Avg Len increases from 5,333 5{,}333 to 7,169 7{,}169 (still well below OPD’s 11,410 11{,}410 – 16,020 16{,}020 ), reflecting the trade-off between output-level calibration and the concise reasoning style inherited from the bridge stage.

The two-stage pipeline thus combines the strengths of both approaches: OPRD-Bridge provides a high-quality backbone initialisation with teacher-like reasoning structure, and OPD fine-tunes the output distribution to improve consistency, yielding the highest capability ceiling overall.

#### 4.2.3 Ablation Studies

We ablate the key design choices of OPRD-Bridge to understand their individual contributions.

##### Effect of bridge rank r r .

Figure 12 reports the average cosine similarity between P S ​ ( h S ) P_{S}(h_{S}) and P T ​ ( h T − μ T ) P_{T}(h_{T}-\mu_{T}) across all layer pairs, before and after Stage 1 bridge training, for ranks r ∈ { 1 , 2 , 4 , 8 , 16 , 32 , 64 , 128 , 256 , 512 , 1024 , 2048 } r\in\{1,2,4,8,16,32,64,128,256,512,1024,2048\} . Three findings emerge.

(i) The bridge training is essential. Before Stage 1, the projected representations are nearly orthogonal at all ranks (cosine similarity ≤ 7.5 % \leq 7.5\% ), confirming that the two models’ hidden states are incommensurable without the learned alignment. After training, similarity jumps to 72.3 % 72.3\% even at rank 1 1 and exceeds 90 % 90\% for r ≥ 4 r\geq 4 .

(ii) The optimal rank is low. Similarity peaks at r = 8 r\!=\!8 ( 95.0 % 95.0\% ) and then declines monotonically: 94.1 % 94.1\% at r = 32 r\!=\!32 , 87.9 % 87.9\% at r = 256 r\!=\!256 , and 77.0 % 77.0\% at full rank r = 2048 r\!=\!2048 . This validates the low-pass filter interpretation from § 3.3.4 : the top- r r principal components correspond to the “low-frequency” modes where teacher and student are highly aligned; beyond this sweet spot, additional dimensions introduce architecture-specific variation (“high-frequency noise”) that the linear projector cannot align, diluting the overall similarity.

(iii) The rank controls the signal-to-noise trade-off. Too small a rank ( r = 1 r\!=\!1 – 2 2 ) under-represents the shared structure, leaving useful information on the table. Too large a rank ( r ≥ 64 r\geq 64 ) forces the bridge to transmit misaligned directions, degrading the supervision signal. The plateau at r = 4 r\!=\!4 – 16 16 ( 93.7 93.7 – 95.0 % 95.0\% ) defines the practical operating range; we default to r = 8 r\!=\!8 throughout.

#### 4.2.4 Cross-Tokenizer Distillation

Since OPRD-Bridge performs alignment in representation space, it remains applicable even when teacher and student use entirely different tokenizers. We verify this by distilling Phi-4-mini-reasoning (Microsoft, | 𝒱 | ≈ 200 |\mathcal{V}|\!\approx\!200 K, tiktoken-based BPE; L T = 32 L_{T}\!=\!32 , d T = 3072 d_{T}\!=\!3072 ) into Qwen3-1.7B-Base ( | 𝒱 | ≈ 151 |\mathcal{V}|\!\approx\!151 K, Qwen BPE; L S = 28 L_{S}\!=\!28 , d S = 2048 d_{S}\!=\!2048 ). All training details follow § 4.2.1 exactly, except that we set bridge rank r = 4 r\!=\!4 .

Table 6 reports the results. Two observations stand out.

(1) Representation-space alignment bypasses the vocabulary barrier. Standard OPD, which relies on the shared vocabulary as its alignment channel, collapses when the two tokenizers are incompatible. OPRD-Bridge instead aligns through the learned projector pair in representation space, lifting the student from near-zero performance ( 2.8 % 2.8\% Avg@16) to meaningful accuracy ( 5.0 % 5.0\% ).

(2) Best@16 reveals substantial capability transfer. While Avg@16 gains are modest, Best@16 tells a more encouraging story: the student achieves 13.3 % 13.3\% on both AIME24 and AIME25 (up from 6.7 % 6.7\% and 3.3 % 3.3\% ), and 37.3 % 37.3\% on AIMO (up from 3.5 % 3.5\% ), representing a 4.7 × 4.7\times improvement in average Best@16 ( 21.3 % 21.3\% vs 4.5 % 4.5\% ). This indicates that the bridge successfully transfers the teacher’s reasoning capability into the student’s backbone, even across a tokenizer boundary. The gap between Best@16 and Avg@16 is consistent with the LM-head calibration hypothesis from § 4.2.2 : the backbone has acquired teacher-like representations, but the LM head (which was pre-trained with a different tokenizer’s embedding table) has not been calibrated to translate these representations into consistent token-level outputs.

This experiment validates the core theoretical promise of OPRD-Bridge: by shifting alignment from the output space to the representation space, distillation becomes decoupled from the vocabulary, enabling knowledge transfer across incompatible tokenizers.

## 5 Discussion

##### From representational alignment to cross-architecture distillation.

The unifying insight behind OPRD is that the quality of hidden-state distillation is governed by representational alignment between teacher and student (§ 3.3 ). When alignment is high (same architecture, shared initialisation), the full ℝ d \mathbb{R}^{d} channel is already an effective all-pass filter and OPRD-Vanilla suffices. When alignment is low (different depth, width, or training history), OPRD-Bridge constructs a low-rank, low-pass channel that transmits the shared structure and suppresses architecture-specific noise. Both regimes are instances of the same principle; the bridge rank r r simply controls the bandwidth of the supervision channel.

##### High-value application 1: multi-model RL merging.

In the same-architecture setting (e.g., multi-model RL merging where all models share a backbone), OPRD-Vanilla addresses a pressing practical pain point. In large-scale RL pipelines that merge multiple reward models or policy checkpoints, full-vocabulary OPD is the natural distillation objective but incurs prohibitive memory cost: materialising the [ B , T , | 𝒱 | ] [B,T,|\mathcal{V}|] logit tensor for | 𝒱 | |\mathcal{V}| demands extremely high transient GPU memory, often requiring extensive infrastructure modifications [ 5 ] . The common workaround, top- k k OPD, reduces memory but introduces a truncation bias (tail tokens are ignored) and remains subject to the LM-head information bottleneck analyzed in Theorem 2 . OPRD offers a third path: it simultaneously mitigates the variance problem (by providing a deterministic, hidden-state-level gradient) and dramatically reduces memory and wall-clock cost (by never materialising the vocabulary-sized tensor), making it an attractive drop-in component for multi-model RL consolidation.

##### High-value application 2: on-policy self-distillation (OPSD).

OPRD is a natural fit for on-policy self-distillation , where the teacher is constructed from the student itself by injecting privileged information (e.g., ground-truth solutions, step-level verification signals) into the prompt. Because the teacher and student share exactly the same weights, the same-architecture requirement is satisfied by construction, and the hidden-state alignment signal is maximally informative. In this setting OPRD can replace the reverse-KL computation in the output space with a cheaper and lower-variance representation-level objective, while retaining the full benefit of privileged-information guidance.

##### Toward alignment-aware pre-training.

Our framework reveals a clear division of labour: OPRD-Vanilla exploits existing representational alignment, while OPRD-Bridge constructs it post hoc via a low-rank projection. A natural question is whether the alignment itself could be established earlier, during pre-training, so that the bridge becomes unnecessary. Concretely, if a large model (e.g., Qwen3-32B) and a small model (e.g., Qwen3-1.7B) were pre-trained with an explicit alignment objective, for instance through shared initialisation of common layers, periodic representation-matching regularisation, or co-distillation, then the resulting pair would already inhabit a well-aligned representation space despite differing in depth and width. Post-training distillation could then proceed via OPRD-Vanilla (with a simple dimension adapter when d S ≠ d T d_{S}\neq d_{T} ), bypassing the bridge entirely: the full ℝ d S \mathbb{R}^{d_{S}} channel would serve as a high-quality all-pass filter, combining the fidelity of full-vocabulary distillation with the efficiency of representation-level supervision. In the language of our filter analogy, alignment-aware pre-training would shift the “cutoff frequency” upward, turning directions that are currently noise (and must be filtered out by the bridge) into signal. This perspective reframes the bridge not as a permanent architectural component but as a compensator for misalignment that better pre-training could eliminate.

## 6 Related Work

OPRD draws on three main lines of research: classical knowledge distillation, on-policy distillation, and feature-level / intermediate-representation distillation. We also discuss adjacent work on auxiliary losses and capacity-gap analyses. Throughout, we emphasize how OPRD differs from prior work that may at first appear similar.

##### Output-Space Knowledge Distillation.

The idea of compressing a large model into a smaller one by matching their output distributions dates back to Hinton et al. [12] . In the sequence-modelling setting, Kim and Rush [20] showed that training a student on teacher-generated translations is an effective form of sequence-level knowledge transfer; subsequent work applied the same principle to pre-trained language models [ 30 , 17 , 35 ] and to instruction-following LLMs via supervised fine-tuning on teacher rollouts [ 4 , 31 , 36 ] . A common thread across all these methods is that supervision is provided (i) off-policy , on data the student did not generate, and (ii) exclusively in the output space , at the LM-head logits or the softmax distribution derived from them. The first property introduces exposure bias [ 2 ] ; the second confines the learning signal to the ill-conditioned image of W head W_{\mathrm{head}} , leaving hidden-state deviations along its effective null space entirely unpenalised ( Theorem 2 ). OPRD departs from both properties simultaneously.

##### On-Policy Distillation.

The exposure-bias problem motivated a shift toward on-policy training. MiniLLM [ 8 ] optimised a reverse-KL objective on student-sampled responses via policy gradient, observing that the mode-seeking property of reverse KL discourages the student from placing mass where the teacher assigns low probability. GKD [ 1 ] generalised this to a family of divergences that interpolate between on- and off-policy data. More recently, Yang et al. [41] reinterpreted OPD through the lens of KL-constrained RL, revealing that the teacher’s per-token log-probability ratio serves as an implicit dense reward. Building on these foundations, OPD has been adopted in several production post-training pipelines [ 5 , 39 , 47 , 37 , 21 , 18 , 16 , 7 , 13 ] and extended to self-distillation settings where the teacher is derived from the student itself via privileged information [ 14 , 48 , 11 , 32 , 43 , 29 , 19 , 42 , 40 , 24 , 6 ] . A key observation, however, is that the entire design space explored so far (sampled-token, top- k k , and full-vocabulary variants) concerns only how many output tokens to supervise per position; the supervision itself never leaves the output space. OPRD is, to our knowledge, the first on-policy method whose learning signal originates strictly before the LM head , operating on the student’s own trajectories.

##### Feature / Intermediate-Representation Distillation.

A separate line of work supervises the student’s intermediate representations rather than its outputs. Early instances include FitNets [ 28 ] , which match a single “hint” layer of the student to the teacher; attention-transfer [ 46 ] , which matches per-pixel attention maps in CNNs; and FSP-matrix distillation [ 44 ] , which matches Gram matrices between layers. For BERT-style language models, TinyBERT [ 17 ] and MobileBERT [ 33 ] extend this idea by jointly matching hidden states and attention maps across all layers, and MiniLM/MiniLMv2 [ 35 , 34 ] match self-attention relation matrices. At first glance, OPRD may look like a straightforward port of these ideas to autoregressive LLMs, but two structural differences set it apart:

• On-policy vs. off-policy supervision. FitNets, TinyBERT, MiniLM, and their successors compute the feature-matching loss on fixed inputs from a pre-training or downstream corpus, i.e. inputs the student does not generate. The student is never exposed to its own rollout distribution during distillation, so exposure bias remains. OPRD, by contrast, computes the hidden-state loss on student-generated sequences y ^ ∼ π θ ( ⋅ ∣ x ) \hat{y}\sim\pi_{\theta}(\cdot\mid x) that evolve as training progresses. The teacher is queried on states the student actually visits, making the supervision signal adaptive to the student’s evolving policy.

• Encoder representations vs. autoregressive prefix representations. Prior feature-distillation work targets encoder models (BERT, vision CNNs) whose representations are computed once per input; the teacher and student process the same input and are aligned post-hoc. In the autoregressive LLM setting, each hidden state h ⋅ , t ( l ) h_{\cdot,t}^{(l)} (for either model) encodes the model’s belief just before predicting token y ^ t \hat{y}_{t} , conditional on the entire sampled prefix y ^ < t \hat{y}_{<t} . OPRD therefore aligns the student’s predictive computation at every decoding step under its own sampling distribution, a fundamentally on-policy object with no analog in encoder-style feature distillation.

##### Hint Learning, Auxiliary Losses, and Distribution Matching.

A related body of work uses intermediate signals to regularize or augment training rather than to distill from a separate teacher. Deeply-supervised nets [ 23 ] attach auxiliary classifiers to intermediate layers of a single model; DINO [ 3 ] aligns hidden states across augmented views of the same input in self-supervised learning; representation engineering [ 49 ] steers or interprets hidden states without explicit teacher supervision. OPRD shares the high-level intuition that intermediate representations carry useful signal, but differs in three crucial ways: it is (i) explicitly teacher–student rather than self-supervised, (ii) on-policy on student-generated autoregressive trajectories, and (iii) a self-contained training objective that can additionally compose with any output-space OPD variant via Eq. ( 7 ).

## 7 Conclusion and Future Work

We presented OPRD , the first on-policy distillation method that supervises the student in the hidden-state space rather than at the LM-head output. The central thesis is that all existing OPD variants (sampled-token, top- k k , and full-vocabulary) share two practical limitations inherent to the output-space paradigm: the dominant sampled-token variant suffers from a high-variance REINFORCE-style gradient estimator whose signal-to-noise ratio collapses as the student approaches the teacher, while top- k k and full-vocabulary variants trade this variance for a truncation bias or prohibitive memory cost; and all variants are subject to an LM-head projection that acts as an information bottleneck, compressing the teacher’s full stack of intermediate hidden states through an ill-conditioned, softmax-invariant mapping. By moving supervision from the output of the LM head to its input, OPRD yields a deterministic per-sample gradient that removes the token-level estimation variance by construction, and exposes per-position, per-layer structural information that any output-space objective necessarily discards. Empirically, OPRD enables monotonic improvement throughout training and closes the student–teacher gap on three competition mathematics benchmarks (AIME 2024, AIME 2025, AIMO), while every output-space baseline plateaus several points below the teacher. On the same hardware budget, OPRD is strictly Pareto-dominant: 1.44 × 1.44\times faster wall-clock training and up to 54 % 54\% less actor-update transient memory than top- k k OPD, because its loss path never materialises the [ B , T , | 𝒱 | ] [B,T,|\mathcal{V}|] logits tensor.

We further introduced OPRD-Bridge , which extends representation distillation to the cross-architecture setting by constructing a frozen low-rank bridge between heterogeneous teacher and student representations. By exploiting the empirical finding that models of different depth and width share a low-rank representational structure, OPRD-Bridge shifts alignment from the output space to the representation space, decoupling distillation from the vocabulary. We validated this capability on both cross-architecture (Qwen3-4B → \to Qwen3-1.7B) and cross-tokenizer (Phi-4-mini-reasoning → \to Qwen3-1.7B) settings, demonstrating successful knowledge transfer even when the vocabulary-based alignment channel is unavailable.

##### Future Work.

Several directions follow naturally from our framework: • Beyond mathematical reasoning. Our experiments focus on long-CoT math benchmarks. Whether OPRD’s gains transfer to code generation, agentic interaction, and open-ended dialogue, each with different position-level supervision characteristics, remains an open question.

• Cross-modal distillation. Our cross-tokenizer experiment (§ 4.2.4 ) validates that OPRD-Bridge transfers knowledge across incompatible tokenizers by aligning in representation space. The natural next step is cross-modal distillation (e.g., from a vision-language teacher to a language-only student), where the representation-space bridge may serve as the only viable supervision channel.

• Adaptive layer and position selection. We use uniform layer weighting and a simple last- k k position heuristic. Adaptively weighting layers and positions based on where the student–teacher gap is largest or where the gradient signal is most informative could further sharpen supervision.

• On-policy representation self-distillation (OPRSD). As discussed in § 5 , OPRD is a natural fit for self-distillation with privileged information, where the same-architecture requirement is satisfied by construction. Scaling OPRSD to multi-turn and multi-task settings is a promising next step.

• Understanding the phase transition. Our mechanistic analysis (§ 4.1.5 ) reveals a PG-loss spike and associated entropy/overlap dynamics when OPRD is active. Characterising the mechanism behind this transition would deepen the theoretical understanding of representation-level distillation.

• Attention-map distillation. OPRD aligns hidden-state vectors but does not supervise the attention patterns that produce them. Extending OPRD with an on-policy attention-matching objective could transfer the teacher’s routing and composition behaviour more directly.

• Alignment-aware pre-training. Our analysis shows that representational alignment, not architectural identity, is the true prerequisite for direct hidden-state distillation. If pre-training itself enforced alignment between large and small models (e.g., through shared layer initialisation or periodic representation-matching regularisation), the resulting pair might not require a low-rank bridge at all, making cross-architecture OPRD as seamless as the same-architecture case.

• Representation-level diagnostics for OPD. By opening up the hidden-state channel, OPRD enables representation-level diagnostics (cosine similarity, CKA, probing accuracy) to be tracked alongside traditional output-level metrics, providing a more complete mechanistic picture of how knowledge transfers between models during RL training.

• Tighter theoretical bounds. Our analysis identifies the qualitative mechanisms behind OPRD’s success. Quantifying these effects, including explicit convergence-rate bounds for OPRD vs. sampled-token OPD and spectral characterisations of which hidden-state directions the LM head nulls out, would solidify the theoretical foundation.

More broadly, our results suggest that hidden-state representations are an under-exploited resource in LLM distillation. We hope this work encourages the community to treat the teacher not merely as a probability oracle but as a structured source of layered internal computation that the student can learn to inhabit.

## References

[1] R. Agarwal, N. Vieillard, Y. Zhou, P. Stanczyk, S. Ramos Garea, M. Geist, and O. Bachem (2024) On-policy distillation of language models: learning from self-generated mistakes . In International Conference on Learning Representations , Vol. 2024 , pp. 21246–21263 . Cited by: §6 .

[2] S. Bengio, O. Vinyals, N. Jaitly, and N. Shazeer (2015) Scheduled sampling for sequence prediction with recurrent neural networks . Advances in neural information processing systems 28 . Cited by: §1 , §6 .

[3] M. Caron, H. Touvron, I. Misra, H. Jégou, J. Mairal, P. Bojanowski, and A. Joulin (2021) Emerging properties in self-supervised vision transformers . In Proceedings of the IEEE/CVF international conference on computer vision , pp. 9650–9660 . Cited by: §6 .

[4] H. W. Chung, L. Hou, S. Longpre, B. Zoph, Y. Tay, W. Fedus, Y. Li, X. Wang, M. Dehghani, S. Brahma, et al. (2024) Scaling instruction-finetuned language models . Journal of Machine Learning Research 25 ( 70 ), pp. 1–53 . Cited by: §6 .

[5] A. DeepSeek (2026) Deepseek-v4: towards highly efficient million-token context intelligence . Cited by: §1 , §1 , §5 , §6 .

[6] K. Ding (2026) Hdpo: hybrid distillation policy optimization via privileged self-distillation . arXiv preprint arXiv:2603.23871 . Cited by: §6 .

[7] Y. Fu, H. Huang, K. Jiang, J. Liu, Z. Jiang, Y. Zhu, and D. Zhao (2026) Revisiting on-policy distillation: empirical failure modes and simple fixes . arXiv preprint arXiv:2603.25562 . Cited by: §6 .

[8] Y. Gu, L. Dong, F. Wei, and M. Huang (2024) Minillm: knowledge distillation of large language models . In International Conference on Learning Representations , Vol. 2024 , pp. 32694–32717 . Cited by: §6 .

[9] D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, et al. (2025) DeepSeek-r1 incentivizes reasoning in llms through reinforcement learning . Nature 645 ( 8081 ), pp. 633–638 . Cited by: §4.1.1 .

[10] B. He, Z. Qu, Z. Liu, Y. Chen, Y. Zuo, C. Qian, K. Zhang, W. Chen, C. Xiao, G. Cui, et al. (2025) Justrl: scaling a 1.5 b llm with a simple rl recipe . arXiv preprint arXiv:2512.16649 . Cited by: §4.1.1 .

[11] B. He, Y. Zuo, Z. Liu, S. Zhao, Z. Fu, J. Yang, C. Qian, K. Zhang, Y. Fan, G. Cui, et al. (2026) How far can unsupervised rlvr scale llm training? . arXiv preprint arXiv:2603.08660 . Cited by: §6 .

[12] G. Hinton, O. Vinyals, and J. Dean (2015) Distilling the knowledge in a neural network . arXiv preprint arXiv:1503.02531 . Cited by: §6 .

[13] W. Hou, S. Peng, W. Wang, Z. Ruan, Y. Zhang, Z. Zhou, M. Gao, Y. Chen, K. Wang, H. Yang, et al. (2026) Uni-opd: unifying on-policy distillation with a dual-perspective recipe . arXiv preprint arXiv:2605.03677 . Cited by: §6 .

[14] J. Hübotter, F. Lübeck, L. Behric, A. Baumann, M. Bagatella, D. Marta, I. Hakimi, I. Shenfeld, T. K. Buening, C. Guestrin, et al. (2026) Reinforcement learning via self-distillation . arXiv preprint arXiv:2601.20802 . Cited by: §6 .

[15] M. Huh, B. Cheung, T. Wang, and P. Isola (2024) The platonic representation hypothesis . arXiv preprint arXiv:2405.07987 . Cited by: §1 , §3.3.4 .

[16] I. Jang, J. Yeom, J. Yeo, H. Lim, and T. Kim (2026) Stable on-policy distillation through adaptive target reformulation . arXiv preprint arXiv:2601.07155 . Cited by: §6 .

[17] X. Jiao, Y. Yin, L. Shang, X. Jiang, X. Chen, L. Li, F. Wang, and Q. Liu (2020) Tinybert: distilling bert for natural language understanding . In Findings of the association for computational linguistics: EMNLP 2020 , pp. 4163–4174 . Cited by: §6 , §6 .

[18] W. Jin, T. Min, Y. Yang, S. R. Kadhe, Y. Zhou, D. Wei, N. Baracaldo, and K. Lee (2026) Entropy-aware on-policy distillation of language models . arXiv preprint arXiv:2603.07079 . Cited by: §6 .

[19] J. Kim, X. Luo, M. Kim, S. Lee, D. Kim, J. Jeon, D. Li, and Y. Yang (2026) Why does self-distillation (sometimes) degrade the reasoning capability of llms? . arXiv preprint arXiv:2603.24472 . Cited by: §6 .

[20] Y. Kim and A. M. Rush (2016) Sequence-level knowledge distillation . In Proceedings of the 2016 conference on empirical methods in natural language processing , pp. 1317–1327 . Cited by: §6 .

[21] J. Ko, S. Abdali, Y. J. Kim, T. Chen, and P. Cameron (2026) Scaling reasoning efficiently via relaxed on-policy distillation . arXiv preprint arXiv:2603.11137 . Cited by: §6 .

[22] S. Kornblith, M. Norouzi, H. Lee, and G. Hinton (2019) Similarity of neural network representations revisited . In International conference on machine learning , pp. 3519–3529 . Cited by: §1 .

[23] C. Lee, S. Xie, P. Gallagher, Z. Zhang, and Z. Tu (2015) Deeply-supervised nets . In Artificial intelligence and statistics , pp. 562–570 . Cited by: §6 .

[24] G. Li, T. Yang, J. Fang, M. Song, M. Zheng, H. Guo, D. Zhang, J. Wang, and T. Chua (2026) Unifying group-relative and self-distillation policy optimization via sample routing . arXiv preprint arXiv:2604.02288 . Cited by: §6 .

[25] Y. Li, Y. Zuo, B. He, J. Zhang, C. Xiao, C. Qian, T. Yu, H. Gao, W. Yang, Z. Liu, et al. (2026) Rethinking on-policy distillation of large language models: phenomenology, mechanism, and recipe . arXiv preprint arXiv:2604.13016 . Cited by: §4.1.1 , §4.1.5 .

[26] J. Merullo, L. Castricato, C. Eickhoff, and E. Pavlick (2022) Linearly mapping from image to text space . arXiv preprint arXiv:2209.15162 . Cited by: §1 .

[27] L. Moschella, V. Maiorca, M. Fumero, A. Norelli, F. Locatello, and E. Rodolà (2022) Relative representations enable zero-shot latent space communication . arXiv preprint arXiv:2209.15430 . Cited by: §1 .

[28] A. Romero, N. Ballas, S. E. Kahou, A. Chassang, C. Gatta, and Y. Bengio (2014) FitNets: hints for thin deep nets (2014) . arXiv preprint arXiv:1412.6550 3 . Cited by: §6 .

[29] H. Sang, Y. Xu, Z. Zhou, R. He, Z. Wang, and J. Sun (2026) Crisp: compressed reasoning via iterative self-policy distillation . arXiv preprint arXiv:2603.05433 . Cited by: §6 .

[30] V. Sanh, L. Debut, J. Chaumond, and T. Wolf (2019) DistilBERT, a distilled version of bert: smaller, faster, cheaper and lighter . arXiv preprint arXiv:1910.01108 . Cited by: §6 .

[31] V. Sanh, A. Webson, C. Raffel, S. H. Bach, L. Sutawika, Z. Alyafeai, A. Chaffin, A. Stiegler, T. L. Scao, A. Raja, et al. (2021) Multitask prompted training enables zero-shot task generalization . arXiv preprint arXiv:2110.08207 . Cited by: §6 .

[32] I. Shenfeld, M. Damani, J. Hübotter, and P. Agrawal (2026) Self-distillation enables continual learning . arXiv preprint arXiv:2601.19897 . Cited by: §6 .

[33] Z. Sun, H. Yu, X. Song, R. Liu, Y. Yang, and D. Zhou (2020) Mobilebert: a compact task-agnostic bert for resource-limited devices . In Proceedings of the 58th annual meeting of the association for computational linguistics , pp. 2158–2170 . Cited by: §6 .

[34] W. Wang, H. Bao, S. Huang, L. Dong, and F. Wei (2021) Minilmv2: multi-head self-attention relation distillation for compressing pretrained transformers . In Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021 , pp. 2140–2151 . Cited by: §6 .

[35] W. Wang, F. Wei, L. Dong, H. Bao, N. Yang, and M. Zhou (2020) Minilm: deep self-attention distillation for task-agnostic compression of pre-trained transformers . Advances in neural information processing systems 33 , pp. 5776–5788 . Cited by: §6 , §6 .

[36] J. Wei, M. Bosma, V. Y. Zhao, K. Guu, A. W. Yu, B. Lester, N. Du, A. M. Dai, and Q. V. Le (2021) Finetuned language models are zero-shot learners . arXiv preprint arXiv:2109.01652 . Cited by: §6 .

[37] B. Xiao, B. Xia, B. Yang, B. Gao, B. Shen, C. Zhang, C. He, C. Lou, F. Luo, G. Wang, et al. (2026) Mimo-v2-flash technical report . arXiv preprint arXiv:2601.02780 . Cited by: §1 , §1 , §2.3 , §6 .

[38] H. Xu, B. Peng, H. Awadalla, D. Chen, Y. Chen, M. Gao, Y. J. Kim, Y. Li, L. Ren, Y. Shen, et al. (2025) Phi-4-mini-reasoning: exploring the limits of small reasoning language models in math . arXiv preprint arXiv:2504.21233 . Cited by: §4.2.1 .

[39] A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. (2025) Qwen3 technical report . arXiv preprint arXiv:2505.09388 . Cited by: §1 , §4.2.1 , §6 .

[40] C. Yang, C. Qin, Q. Si, M. Chen, N. Gu, D. Yao, Z. Lin, W. Wang, J. Wang, and N. Duan (2026) Self-distilled rlvr . arXiv preprint arXiv:2604.03128 . Cited by: §6 .

[41] W. Yang, W. Liu, R. Xie, K. Yang, S. Yang, and Y. Lin (2026) Learning beyond teacher: generalized on-policy distillation with reward extrapolation . arXiv preprint arXiv:2602.12125 . Cited by: §1 , §2.3 , §6 .

[42] T. Ye, L. Dong, Q. Dong, X. Wu, S. Huang, and F. Wei (2026) Online experiential learning for language models . arXiv preprint arXiv:2603.16856 . Cited by: §6 .

[43] T. Ye, L. Dong, X. Wu, S. Huang, and F. Wei (2026) On-policy context distillation for language models . arXiv preprint arXiv:2602.12275 . Cited by: §6 .

[44] J. Yim, D. Joo, J. Bae, and J. Kim (2017) A gift from knowledge distillation: fast optimization, network minimization and transfer learning . In Proceedings of the IEEE conference on computer vision and pattern recognition , pp. 4133–4141 . Cited by: §6 .

[45] Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, W. Dai, T. Fan, G. Liu, L. Liu, et al. (2026) Dapo: an open-source llm reinforcement learning system at scale . Advances in Neural Information Processing Systems 38 , pp. 113222–113244 . Cited by: §4.1.1 .

[46] S. Zagoruyko and N. Komodakis (2016) Paying more attention to attention: improving the performance of convolutional neural networks via attention transfer . arXiv preprint arXiv:1612.03928 . Cited by: §6 .

[47] A. Zeng, X. Lv, Z. Hou, Z. Du, Q. Zheng, B. Chen, D. Yin, C. Ge, C. Huang, C. Xie, et al. (2026) Glm-5: from vibe coding to agentic engineering . arXiv preprint arXiv:2602.15763 . Cited by: §1 , §6 .

[48] S. Zhao, Z. Xie, M. Liu, J. Huang, G. Pang, F. Chen, and A. Grover (2026) Self-distilled reasoner: on-policy self-distillation for large language models . arXiv preprint arXiv:2601.18734 . Cited by: §6 .

[49] A. Zou, L. Phan, S. Chen, J. Campbell, P. Guo, R. Ren, A. Pan, X. Yin, M. Mazeika, A. Dombrowski, et al. (2023) Representation engineering: a top-down approach to ai transparency . arXiv preprint arXiv:2310.01405 . Cited by: §6 .

## Appendix A Notation Summary

## Appendix B Formal Theoretical Guarantees

The two theorems in § 3.2 ( Theorems 1 and 2 ) establish OPRD’s properties at an intuitive level. We now state both formally, in one-to-one correspondence with the main conclusions stated in § 3.2 : • § B.1 formalizes Theorem 1 (gradient variance) : variance gap ( Theorems 4 , 5 and 1 ) and signal-to-noise collapse ( Theorem 6 ).

• § B.5 formalizes Theorem 2 (LM-head information bottleneck) : the null-direction identity ( Theorem 7 ) and the spectral gap ( Theorem 8 ).

Throughout this section, all expectations are taken over a single fixed prompt x x and a single response position t t ; the multi-position case follows by linearity. We use θ \theta to denote the student parameters, π θ \pi_{\theta} and π T \pi_{T} to denote the student and teacher policies, and write p ≡ p t = π θ ( ⋅ ∣ x , y ^ < t ) p\equiv p_{t}=\pi_{\theta}(\cdot\mid x,\hat{y}_{<t}) and q ≡ q t = π T ( ⋅ ∣ x , y ^ < t ) q\equiv q_{t}=\pi_{T}(\cdot\mid x,\hat{y}_{<t}) for brevity. We let u t ≜ log ⁡ p − log ⁡ q u_{t}\triangleq\log p-\log q denote the per-token log-density ratio.

### B.1 Setup and Assumptions

###### Definition 1 (Stochastic gradient estimators) .

Fix a student response position t t and a sampled-token estimator y ^ t ∼ p \hat{y}_{t}\sim p . The two per-position stochastic gradient estimators considered in this paper are g OPD ​ ( θ , y ^ t ) \displaystyle g_{\mathrm{OPD}}(\theta;\hat{y}_{t}) ≜ ∇ θ [ log ⁡ p ⁡ ( y ^ t ) − log ⁡ q ⁡ ( y ^ t ) ] = ∇ θ ​ log ​ p ​ ( y ^ t ) , \displaystyle\triangleq\nabla_{\theta}\bigl[\log p(\hat{y}_{t})-\log q(\hat{y}_{t})\bigr]=\nabla_{\theta}\log p(\hat{y}_{t}), (17) g OPRD ​ ( θ ) \displaystyle g_{\mathrm{OPRD}}(\theta) ≜ ∇ θ 1 d ​ ‖ h θ , t ( L ) − sg ⁡ ( h T , t ( L ) ) ‖ 2 2 , \displaystyle\triangleq\nabla_{\theta}\,\tfrac{1}{d}\,\bigl\|h_{\theta,t}^{(L)}-\mathrm{sg}(h_{T,t}^{(L)})\bigr\|_{2}^{2}, (18) where in ( 17 ) we used the fact that ∇ θ ​ log ​ q ​ ( y ^ t ) = 0 \nabla_{\theta}\log q(\hat{y}_{t})=0 because q q depends only on the (frozen) teacher. The corresponding population gradients are g ¯ OPD ​ ( θ ) ≜ 𝔼 y ^ t ∼ p ​ [ g OPD ] \bar{g}_{\mathrm{OPD}}(\theta)\triangleq\mathbb{E}_{\hat{y}_{t}\sim p}[g_{\mathrm{OPD}}] and g ¯ OPRD ​ ( θ ) ≜ g OPRD \bar{g}_{\mathrm{OPRD}}(\theta)\triangleq g_{\mathrm{OPRD}} (which is already deterministic in y ^ t \hat{y}_{t} ).

###### Assumption 1 (Standard regularity) .

The following standard conditions hold throughout: (R1) The log-densities log ⁡ p θ ​ ( v ) \log p_{\theta}(v) are twice continuously differentiable in θ \theta for every v ∈ 𝒱 v\in\mathcal{V} . (R2) The score s θ ​ ( v ) ≜ ∇ θ ​ log ​ p θ ​ ( v ) s_{\theta}(v)\triangleq\nabla_{\theta}\log p_{\theta}(v) satisfies 𝔼 p ​ [ ‖ s θ ‖ 2 2 ] < ∞ \mathbb{E}_{p}[\|s_{\theta}\|_{2}^{2}]<\infty (finite Fisher information). (R3) For each v v , | log ⁡ p θ ​ ( v ) − log ⁡ q ⁡ ( v ) | ≤ M |\log p_{\theta}(v)-\log q(v)|\leq M for some constant M < ∞ M<\infty on the trajectory of training (bounded log-ratio). (R4) The hidden state h θ , t ( L ) h_{\theta,t}^{(L)} is a continuously differentiable function of θ \theta with bounded Jacobian: ‖ ∇ θ h θ , t ( L ) ‖ op ≤ J < ∞ \|\nabla_{\theta}h_{\theta,t}^{(L)}\|_{\mathrm{op}}\leq J<\infty .

Conditions (R1)–(R2) hold for any LLM with softmax output; (R3) holds whenever both student and teacher assign nonzero probability to every supported token (e.g., after a small label-smoothing or temperature adjustment); (R4) holds for any Lipschitz transformer with bounded weights. These assumptions are mild and standard in the policy-gradient literature.

### B.2 Variance of Sampled-Token OPD

###### Lemma 1 (Score-function decomposition of OPD gradient) .

Under Assumption 1 , the OPD population gradient at position t t admits the score-function representation g ¯ OPD ​ ( θ ) = 𝔼 y ^ t ∼ p ​ [ u t ​ ( y ^ t ) ​ ∇ θ ​ log ⁡ p ⁡ ( y ^ t ) ] , u t ​ ( v ) ≜ log ⁡ p ⁡ ( v ) − log ⁡ q ⁡ ( v ) . \bar{g}_{\mathrm{OPD}}(\theta)\;=\;\mathbb{E}_{\hat{y}_{t}\sim p}\bigl[\,u_{t}(\hat{y}_{t})\,\nabla_{\theta}\log p(\hat{y}_{t})\,\bigr],\qquad u_{t}(v)\triangleq\log p(v)-\log q(v). (19)

###### Proof.

Starting from ( 17 ), write g ¯ OPD = 𝔼 p ​ [ ∇ θ ​ log ​ p ​ ( y ^ t ) ] \bar{g}_{\mathrm{OPD}}=\mathbb{E}_{p}[\nabla_{\theta}\log p(\hat{y}_{t})] . The unconditional expectation of the score is zero: 𝔼 p [ ∇ θ log p ( y ^ t ) ] = ∑ v p ( v ) ∇ θ log p ( v ) = ∑ v ∇ θ p ( v ) = ∇ θ ∑ v p ( v ) = ∇ θ 1 = 0 . \mathbb{E}_{p}[\nabla_{\theta}\log p(\hat{y}_{t})]=\sum_{v}p(v)\,\nabla_{\theta}\log p(v)=\sum_{v}\nabla_{\theta}p(v)=\nabla_{\theta}\!\sum_{v}p(v)=\nabla_{\theta}1=0. Therefore g ¯ OPD \bar{g}_{\mathrm{OPD}} vanishes, which would make it useless as a learning signal. This apparent paradox is resolved by recognizing that what we actually optimize is the OPD loss surrogate along its stochastic gradient, which by the REINFORCE identity satisfies ∇ θ 𝔼 y ^ t ∼ p ​ [ log ⁡ p ⁡ ( y ^ t ) − log ⁡ q ⁡ ( y ^ t ) ] = 𝔼 p ​ [ ( log ⁡ p − log ⁡ q ) ​ ∇ θ ​ log ​ p ] + 𝔼 p ​ [ ∇ θ ​ log ​ p ] , \nabla_{\theta}\,\mathbb{E}_{\hat{y}_{t}\sim p}\!\bigl[\log p(\hat{y}_{t})-\log q(\hat{y}_{t})\bigr]=\mathbb{E}_{p}\!\bigl[(\log p-\log q)\,\nabla_{\theta}\log p\bigr]+\mathbb{E}_{p}[\nabla_{\theta}\log p], where the last term vanishes by the calculation above, giving ( 19 ). ∎

Lemma 1 shows that the OPD gradient is essentially a REINFORCE estimator with u t u_{t} playing the role of the reward. This structural property is what makes it high-variance.

###### Theorem 4 (OPD gradient variance lower bound) .

Under Assumption 1 , the conditional variance (conditioned on the prompt x x and prefix y ^ < t \hat{y}_{<t} ) of the single-sample OPD gradient satisfies Var ⁡ [ g OPD ​ ( θ , y ^ t ) ] = 𝔼 p ​ [ u t 2 ​ ‖ ∇ θ ​ log ​ p ‖ 2 2 ] − ‖ g ¯ OPD ​ ( θ ) ‖ 2 2 . \mathrm{Var}\bigl[g_{\mathrm{OPD}}(\theta;\hat{y}_{t})\bigr]\;=\;\mathbb{E}_{p}\!\Bigl[u_{t}^{2}\,\|\nabla_{\theta}\log p\|_{2}^{2}\Bigr]\;-\;\bigl\|\bar{g}_{\mathrm{OPD}}(\theta)\bigr\|_{2}^{2}. (20) Moreover, near the optimum where p → q p\to q , the variance is bounded below by Var ⁡ [ g OPD ] ≥ Var p ​ ( u t ) ⋅ ℱ min ​ ( θ ) − o ⁡ ( 1 ) ​ as ​ p → q , \mathrm{Var}\bigl[g_{\mathrm{OPD}}\bigr]\;\geq\;\mathrm{Var}_{p}(u_{t})\;\cdot\;\mathcal{F}_{\min}(\theta)\;-\;o(1)\;\;\text{as }p\to q, (21) where ℱ min ​ ( θ ) ≜ λ min ​ ( 𝔼 p ​ [ ∇ θ ​ log ​ p ​ ∇ θ ​ log ​ p ⊤ ] ) \mathcal{F}_{\min}(\theta)\triangleq\lambda_{\min}\!\bigl(\mathbb{E}_{p}[\nabla_{\theta}\log p\,\nabla_{\theta}\log p^{\top}]\bigr) is the minimum eigenvalue of the Fisher information matrix. In particular, Var ⁡ [ g OPD ] = Ω ⁡ ( Var p ​ ( u t ) ) \mathrm{Var}[g_{\mathrm{OPD}}]=\Omega(\mathrm{Var}_{p}(u_{t})) does not vanish as the loss approaches zero.

###### Proof.

The exact identity ( 20 ) follows from the definition of variance applied to the score-weighted estimator in Lemma 1 : Var ⁡ [ g OPD ] \displaystyle\mathrm{Var}[g_{\mathrm{OPD}}] = 𝔼 p ​ [ ‖ u t ​ ∇ θ ​ log ⁡ p ‖ 2 2 ] − ‖ 𝔼 p ​ [ u t ​ ∇ θ ​ log ⁡ p ] ‖ 2 2 \displaystyle=\mathbb{E}_{p}\bigl[\|u_{t}\nabla_{\theta}\log p\|_{2}^{2}\bigr]-\bigl\|\mathbb{E}_{p}[u_{t}\nabla_{\theta}\log p]\bigr\|_{2}^{2} = 𝔼 p ​ [ u t 2 ​ ‖ ∇ θ ​ log ​ p ‖ 2 2 ] − ‖ g ¯ OPD ‖ 2 2 , \displaystyle=\mathbb{E}_{p}\bigl[u_{t}^{2}\,\|\nabla_{\theta}\log p\|_{2}^{2}\bigr]-\|\bar{g}_{\mathrm{OPD}}\|_{2}^{2}, which is ( 20 ).

For the lower bound ( 21 ), we decompose u t = u ¯ + ( u t − u ¯ ) u_{t}=\bar{u}+(u_{t}-\bar{u}) where u ¯ ≜ 𝔼 p [ u t ] = D KL ( p ∥ q ) \bar{u}\triangleq\mathbb{E}_{p}[u_{t}]=D_{\mathrm{KL}}(p\|q) . Substituting into ( 20 ) and applying the Cauchy–Schwarz inequality to bound the cross term, 𝔼 p ​ [ u t 2 ​ ‖ ∇ θ ​ log ​ p ‖ 2 2 ] \displaystyle\mathbb{E}_{p}\bigl[u_{t}^{2}\|\nabla_{\theta}\log p\|_{2}^{2}\bigr] = u ¯ 2 ​ 𝔼 p ​ [ ‖ ∇ θ ​ log ​ p ‖ 2 2 ] + 𝔼 p ​ [ ( u t − u ¯ ) 2 ​ ‖ ∇ θ ​ log ​ p ‖ 2 2 ] \displaystyle=\bar{u}^{2}\,\mathbb{E}_{p}[\|\nabla_{\theta}\log p\|_{2}^{2}]+\mathbb{E}_{p}\bigl[(u_{t}-\bar{u})^{2}\|\nabla_{\theta}\log p\|_{2}^{2}\bigr] + 2 ​ u ¯ ​ 𝔼 p ​ [ ( u t − u ¯ ) ​ ‖ ∇ θ ​ log ​ p ‖ 2 2 ] . \displaystyle\quad+2\bar{u}\,\mathbb{E}_{p}\bigl[(u_{t}-\bar{u})\|\nabla_{\theta}\log p\|_{2}^{2}\bigr]. By the Cauchy–Schwarz / Rayleigh quotient argument, the middle term satisfies 𝔼 p ​ [ ( u t − u ¯ ) 2 ​ ‖ ∇ θ ​ log ​ p ‖ 2 2 ] ≥ Var p ​ ( u t ) ⋅ ℱ min ​ ( θ ) , \mathbb{E}_{p}\bigl[(u_{t}-\bar{u})^{2}\|\nabla_{\theta}\log p\|_{2}^{2}\bigr]\;\geq\;\mathrm{Var}_{p}(u_{t})\cdot\mathcal{F}_{\min}(\theta), since the covariance matrix of ∇ θ ​ log ​ p \nabla_{\theta}\log p is precisely the Fisher information matrix and its minimum eigenvalue lower-bounds any positive-definite quadratic form averaged over p p .

As p → q p\to q in total variation, the first and third terms above are O ⁡ ( u ¯ 2 ) + O ⁡ ( u ¯ ) O(\bar{u}^{2})+O(\bar{u}) , both of which vanish (since u ¯ = D KL ( p ∥ q ) → 0 \bar{u}=D_{\mathrm{KL}}(p\|q)\to 0 ). Meanwhile ‖ g ¯ OPD ‖ 2 2 = O ⁡ ( u ¯ 2 ) \|\bar{g}_{\mathrm{OPD}}\|_{2}^{2}=O(\bar{u}^{2}) , also o ⁡ ( 1 ) o(1) . Combining, Var ⁡ [ g OPD ] ≥ Var p ​ ( u t ) ⋅ ℱ min ​ ( θ ) − o ⁡ ( 1 ) \mathrm{Var}[g_{\mathrm{OPD}}]\geq\mathrm{Var}_{p}(u_{t})\cdot\mathcal{F}_{\min}(\theta)-o(1) , which is ( 21 ). Note that Var p ​ ( u t ) = Θ ⁡ ( δ ) \mathrm{Var}_{p}(u_{t})=\Theta(\delta) vanishes at the same rate as δ \delta , but crucially the signal ‖ g ¯ OPD ‖ 2 2 = O ⁡ ( δ 2 ) \|\bar{g}_{\mathrm{OPD}}\|_{2}^{2}=O(\delta^{2}) vanishes faster , leading to the SNR collapse formalized in Theorem 6 . ∎

### B.3 OPRD Gradient Is Deterministic

###### Theorem 5 (OPRD has zero conditional variance) .

Under Assumption 1 , the OPRD per-position gradient satisfies Var [ g OPRD ( θ ) | x , y ^ < t ] = 0 , \mathrm{Var}\bigl[g_{\mathrm{OPRD}}(\theta)\,\big|\,x,\hat{y}_{<t}\bigr]\;=\;0, (22) and is given in closed form by g OPRD ​ ( θ ) = 2 d ​ ( ∇ θ h θ , t ( L ) ) ⊤ ​ ( h θ , t ( L ) − h T , t ( L ) ) . g_{\mathrm{OPRD}}(\theta)\;=\;\frac{2}{d}\,\bigl(\nabla_{\theta}h_{\theta,t}^{(L)}\bigr)^{\!\top}\,\bigl(h_{\theta,t}^{(L)}-h_{T,t}^{(L)}\bigr). (23)

###### Proof.

Conditioned on the prompt x x and the prefix y ^ < t \hat{y}_{<t} , both h θ , t ( L ) h_{\theta,t}^{(L)} (a deterministic function of θ \theta , x x , y ^ < t \hat{y}_{<t} ) and h T , t ( L ) h_{T,t}^{(L)} (which has sg ⁡ ( ⋅ ) \mathrm{sg}(\cdot) applied, so it is treated as a constant in the gradient) are fixed. Hence the OPRD loss ℓ OPRD ≜ 1 d ​ ‖ h θ , t ( L ) − h T , t ( L ) ‖ 2 2 \ell_{\mathrm{OPRD}}\triangleq\tfrac{1}{d}\,\|h_{\theta,t}^{(L)}-h_{T,t}^{(L)}\|_{2}^{2} is a deterministic function of θ \theta given the conditioning. Therefore its gradient is also deterministic, giving ( 22 ).

The closed form ( 23 ) follows from the chain rule applied to the squared ℓ 2 \ell_{2} norm: ∇ θ 1 d ​ ‖ h θ , t ( L ) − h T , t ( L ) ‖ 2 2 \displaystyle\nabla_{\theta}\tfrac{1}{d}\|h_{\theta,t}^{(L)}-h_{T,t}^{(L)}\|_{2}^{2} = 2 d ​ J θ ​ ( h θ , t ( L ) ) ⊤ ​ ( h θ , t ( L ) − h T , t ( L ) ) , \displaystyle=\tfrac{2}{d}\,J_{\theta}(h_{\theta,t}^{(L)})^{\top}\,(h_{\theta,t}^{(L)}-h_{T,t}^{(L)}), where J θ ​ ( h θ , t ( L ) ) = ∇ θ h θ , t ( L ) ∈ ℝ d × dim ( θ ) J_{\theta}(h_{\theta,t}^{(L)})=\nabla_{\theta}h_{\theta,t}^{(L)}\in\mathbb{R}^{d\times\dim(\theta)} is the Jacobian. By (R4), ‖ J θ ‖ op ≤ J \|J_{\theta}\|_{\mathrm{op}}\leq J , so ‖ g OPRD ‖ 2 ≤ 2 ​ J d ​ ‖ h θ , t ( L ) − h T , t ( L ) ‖ 2 \|g_{\mathrm{OPRD}}\|_{2}\leq\tfrac{2J}{d}\,\|h_{\theta,t}^{(L)}-h_{T,t}^{(L)}\|_{2} , confirming that g OPRD g_{\mathrm{OPRD}} is well-defined and bounded. ∎

###### Corollary 1 (Variance gap) .

Combining Theorems 4 and 5 , the conditional variance gap between the two estimators is Var ⁡ [ g OPD ] − Var ⁡ [ g OPRD ] = 𝔼 p ​ [ u t 2 ​ ‖ ∇ θ ​ log ​ p ‖ 2 2 ] − ‖ g ¯ OPD ‖ 2 2 ≥ 0 , \mathrm{Var}\bigl[g_{\mathrm{OPD}}\bigr]-\mathrm{Var}\bigl[g_{\mathrm{OPRD}}\bigr]\;=\;\mathbb{E}_{p}\!\Bigl[u_{t}^{2}\,\|\nabla_{\theta}\log p\|_{2}^{2}\Bigr]-\|\bar{g}_{\mathrm{OPD}}\|_{2}^{2}\;\geq\;0, (24) with equality only in the degenerate case where p p is a point mass. In particular, OPRD’s gradient is always a lower-variance estimator (under the same conditioning), and the gap grows with the magnitude of the per-token log-ratio u t u_{t} and the spread of the policy.

### B.4 Signal-to-Noise Ratio Collapse of Sampled-Token OPD

We now formalize the most surprising prediction of our analysis: that the OPD signal-to-noise ratio collapses as training progresses, while OPRD’s signal-to-noise ratio remains bounded away from zero. This explains why pure OPD stagnates in late-stage training while OPD + + OPRD continues to improve monotonically.

###### Definition 2 (Signal-to-noise ratio) .

For a stochastic gradient estimator g g with population mean g ¯ = 𝔼 ⁡ [ g ] \bar{g}=\mathbb{E}[g] , the signal-to-noise ratio is SNR ⁡ ( g ) ≜ ‖ g ¯ ‖ 2 2 Tr ⁡ ( Cov ⁡ [ g ] ) . \mathrm{SNR}(g)\;\triangleq\;\frac{\|\bar{g}\|_{2}^{2}}{\mathrm{Tr}(\mathrm{Cov}[g])}. (25) SNR ⁡ ( g ) → 0 \mathrm{SNR}(g)\to 0 means the gradient is dominated by noise; SNR ⁡ ( g ) → ∞ \mathrm{SNR}(g)\to\infty means the gradient is essentially deterministic.

###### Theorem 6 (SNR collapse for OPD, SNR stability for OPRD) .

Define the symmetric divergence δ ( θ ) ≜ D KL ( p ∥ q ) + D KL ( q ∥ p ) \delta(\theta)\triangleq D_{\mathrm{KL}}(p\|q)+D_{\mathrm{KL}}(q\|p) . As training drives δ ⁡ ( θ ) → 0 \delta(\theta)\to 0 , 1. (OPD) SNR ⁡ ( g OPD ) = O ⁡ ( δ ) → 0 \mathrm{SNR}(g_{\mathrm{OPD}})=O(\delta)\to 0 at rate at least linear in δ \delta ;

2. (OPRD) SNR ⁡ ( g OPRD ) = + ∞ \mathrm{SNR}(g_{\mathrm{OPRD}})=+\infty as long as h θ , t ( L ) ≠ h T , t ( L ) h_{\theta,t}^{(L)}\neq h_{T,t}^{(L)} (i.e., the OPRD loss has not yet converged).

###### Proof.

(OPD case.) By Lemma 1 , ∥ g ¯ OPD ∥ 2 2 = ∥ 𝔼 p [ u t ∇ log p ] ∥ 2 2 \|\bar{g}_{\mathrm{OPD}}\|_{2}^{2}=\|\mathbb{E}_{p}[u_{t}\nabla\log p]\|_{2}^{2} . Applying Cauchy–Schwarz, ‖ g ¯ OPD ‖ 2 2 ≤ 𝔼 p ​ [ u t 2 ] ⋅ 𝔼 p ​ [ ‖ ∇ log ⁡ p ‖ 2 2 ] = ( Var p ​ ( u t ) + u ¯ 2 ) ⋅ Tr ⁡ ( ℱ ⁡ ( θ ) ) , \|\bar{g}_{\mathrm{OPD}}\|_{2}^{2}\;\leq\;\mathbb{E}_{p}[u_{t}^{2}]\cdot\mathbb{E}_{p}[\|\nabla\log p\|_{2}^{2}]\;=\;(\mathrm{Var}_{p}(u_{t})+\bar{u}^{2})\cdot\mathrm{Tr}(\mathcal{F}(\theta)), where ℱ ⁡ ( θ ) \mathcal{F}(\theta) is the Fisher information matrix. Since u ¯ = D KL ( p ∥ q ) ≤ δ \bar{u}=D_{\mathrm{KL}}(p\|q)\leq\delta and Var p ​ ( u t ) ≤ 2 ​ δ + O ⁡ ( δ 2 ) \mathrm{Var}_{p}(u_{t})\leq 2\delta+O(\delta^{2}) by a standard Pinsker-type expansion of log ⁡ ( p / q ) \log(p/q) around p = q p=q , we have ‖ g ¯ OPD ‖ 2 2 = O ⁡ ( δ ) . \|\bar{g}_{\mathrm{OPD}}\|_{2}^{2}\;=\;O(\delta). Meanwhile, by Theorem 4 (Eq. 21 ), Tr ⁡ ( Cov ⁡ [ g OPD ] ) ≥ Var p ​ ( u t ) ⋅ ℱ min ​ ( θ ) = Θ ⁡ ( δ ) \mathrm{Tr}(\mathrm{Cov}[g_{\mathrm{OPD}}])\geq\mathrm{Var}_{p}(u_{t})\cdot\mathcal{F}_{\min}(\theta)=\Theta(\delta) . Since the numerator is O ⁡ ( δ ) O(\delta) and the denominator is Ω ⁡ ( δ ) \Omega(\delta) , we have at first glance SNR ⁡ ( g OPD ) = O ⁡ ( δ ) Ω ⁡ ( δ ) = O ⁡ ( 1 ) ​ at best . \mathrm{SNR}(g_{\mathrm{OPD}})\;=\;\frac{O(\delta)}{\Omega(\delta)}\;=\;O(1)\;\;\text{at best}. A sharper analysis reveals that the numerator is in fact O ⁡ ( δ 2 ) O(\delta^{2}) : by the REINFORCE structure of Lemma 1 , ∥ g ¯ OPD ∥ 2 = ∥ 𝔼 p [ u t ∇ log p ] ∥ 2 ≤ 𝔼 p ​ [ u t 2 ] ⋅ Tr ⁡ ( ℱ ) \|\bar{g}_{\mathrm{OPD}}\|_{2}=\|\mathbb{E}_{p}[u_{t}\nabla\log p]\|_{2}\leq\sqrt{\mathbb{E}_{p}[u_{t}^{2}]}\cdot\sqrt{\mathrm{Tr}(\mathcal{F})} , and since 𝔼 p ​ [ u t 2 ] = Var p ​ ( u t ) + u ¯ 2 = Θ ⁡ ( δ ) + Θ ⁡ ( δ 2 ) = Θ ⁡ ( δ ) \mathbb{E}_{p}[u_{t}^{2}]=\mathrm{Var}_{p}(u_{t})+\bar{u}^{2}=\Theta(\delta)+\Theta(\delta^{2})=\Theta(\delta) , the Cauchy–Schwarz bound gives ‖ g ¯ OPD ‖ 2 2 = O ⁡ ( δ ) \|\bar{g}_{\mathrm{OPD}}\|_{2}^{2}=O(\delta) . However, this upper bound is not tight: the actual signal g ¯ OPD = 𝔼 p [ u t ∇ log p ] \bar{g}_{\mathrm{OPD}}=\mathbb{E}_{p}[u_{t}\nabla\log p] involves the correlation between u t u_{t} and ∇ log ⁡ p \nabla\log p , which is O ⁡ ( u ¯ ) = O ⁡ ( δ ) O(\bar{u})=O(\delta) in magnitude (since u t − u ¯ u_{t}-\bar{u} is mean-zero and contributes only through its correlation with ∇ log ⁡ p \nabla\log p , which is bounded by O ⁡ ( δ ) O(\sqrt{\delta}) ). Therefore ‖ g ¯ OPD ‖ 2 2 = O ⁡ ( δ 2 ) \|\bar{g}_{\mathrm{OPD}}\|_{2}^{2}=O(\delta^{2}) , giving SNR ⁡ ( g OPD ) = O ⁡ ( δ 2 ) / Ω ⁡ ( δ ) = O ⁡ ( δ ) → 0 \mathrm{SNR}(g_{\mathrm{OPD}})=O(\delta^{2})/\Omega(\delta)=O(\delta)\to 0 .

(OPRD case.) By Theorem 5 , Cov ⁡ [ g OPRD ] = 0 \mathrm{Cov}[g_{\mathrm{OPRD}}]=0 identically, so Tr ⁡ ( Cov ⁡ [ g OPRD ] ) = 0 \mathrm{Tr}(\mathrm{Cov}[g_{\mathrm{OPRD}}])=0 . As long as g OPRD ≠ 0 g_{\mathrm{OPRD}}\neq 0 (equivalently, h θ , t ( L ) ≠ h T , t ( L ) h_{\theta,t}^{(L)}\neq h_{T,t}^{(L)} ), the ratio in ( 25 ) is ‖ g OPRD ‖ 2 2 / 0 = + ∞ \|g_{\mathrm{OPRD}}\|_{2}^{2}/0=+\infty in the extended-real sense, meaning the gradient signal is completely noise-free. ∎

###### Remark 1 (Interpretation: late-stage stagnation of pure OPD) .

Theorem 6 predicts the following two-phase training dynamics for sampled-token OPD: • Phase 1 (effective learning). Initially δ ⁡ ( θ ) \delta(\theta) is large, so ‖ g ¯ OPD ‖ 2 \|\bar{g}_{\mathrm{OPD}}\|_{2} dominates the noise. The student improves rapidly along − g ¯ OPD -\bar{g}_{\mathrm{OPD}} .

• Phase 2 (stagnation). As δ ⁡ ( θ ) → 0 \delta(\theta)\to 0 , SNR ⁡ ( g OPD ) → 0 \mathrm{SNR}(g_{\mathrm{OPD}})\to 0 by Theorem 6 . The student’s update direction becomes effectively random, and under any positive learning rate the training accuracy plateaus or oscillates around an asymptote well below the teacher.

By contrast, OPRD’s SNR remains infinite throughout training (until convergence in hidden space), so the descent direction is always informative. This is exactly the empirical pattern we observe in § 4 : pure OPD plateaus or oscillates several points below the teacher, while OPD + + μ ⋅ \mu\cdot OPRD (and OPRD on its own) improves monotonically.

##### Sub-summary (Perspective 1).

The theorems above formalize two claims that explain OPRD’s variance advantage: (1) OPRD’s gradient is exactly deterministic and has zero conditional variance ( Theorem 5 ); (2) OPD’s gradient signal-to-noise ratio collapses to zero as the loss approaches its minimum ( Theorem 6 ), causing the late-stage stagnation we observe empirically.

### B.5 Formal Results for Theorem 2 : LM-Head Information Bottleneck

We now make precise the two claims of Theorem 2 : the null-direction identity ( 9 ) and the spectral gap ( 10 ). Fix a single response position t t and write z θ ≜ W head ​ h θ ∈ ℝ | 𝒱 | z_{\theta}\triangleq W_{\mathrm{head}}\,h_{\theta}\in\mathbb{R}^{|\mathcal{V}|} and z T ≜ W head ​ h T z_{T}\triangleq W_{\mathrm{head}}\,h_{T} for the corresponding logit vectors; let σ : ℝ | 𝒱 | → Δ | 𝒱 | − 1 \sigma:\mathbb{R}^{|\mathcal{V}|}\!\to\!\Delta^{|\mathcal{V}|-1} denote the softmax map and 𝟏 ∈ ℝ | 𝒱 | \mathbf{1}\in\mathbb{R}^{|\mathcal{V}|} the all-ones vector. Let W head = U ​ Σ ​ V ⊤ W_{\mathrm{head}}=U\Sigma V^{\top} be the (thin) SVD, with V = [ v 1 , … , v d ] ∈ ℝ d × d V=[v_{1},\ldots,v_{d}]\in\mathbb{R}^{d\times d} orthonormal, Σ = diag ⁡ ( σ 1 ≥ ⋯ ≥ σ d ≥ 0 ) \Sigma=\mathrm{diag}(\sigma_{1}\!\geq\!\cdots\!\geq\!\sigma_{d}\!\geq\!0) , and U ∈ ℝ | 𝒱 | × d U\in\mathbb{R}^{|\mathcal{V}|\times d} having orthonormal columns. We assume throughout that W head W_{\mathrm{head}} has full column rank ( σ d > 0 \sigma_{d}>0 ), which holds for any production LLM.

By an output-space OPD loss we mean any ℓ out ≥ 0 \ell_{\mathrm{out}}\geq 0 that is a fixed function of the two output distributions σ ⁡ ( z θ ) \sigma(z_{\theta}) and σ ⁡ ( z T ) \sigma(z_{T}) and that vanishes whenever σ ⁡ ( z θ ) = σ ⁡ ( z T ) \sigma(z_{\theta})=\sigma(z_{T}) ; this includes the sampled-token estimator, the top- k k truncated reverse KL, and the full-vocabulary reverse KL (§ 2.3 ).

###### Definition 3 (Effective null space of the LM head) .

Define 𝒩 W ≜ { Δ ​ h ∈ ℝ d : W head ​ Δ ​ h ∈ span ⁡ { 𝟏 } } = W head − 1 ​ ( span ⁡ { 𝟏 } ) . \mathcal{N}_{W}\;\triangleq\;\bigl\{\Delta h\in\mathbb{R}^{d}:W_{\mathrm{head}}\,\Delta h\in\mathrm{span}\{\mathbf{1}\}\bigr\}\;=\;W_{\mathrm{head}}^{-1}\!\bigl(\mathrm{span}\{\mathbf{1}\}\bigr). (26)

###### Lemma 2 (Softmax kernel) .

For any z ∈ ℝ | 𝒱 | z\in\mathbb{R}^{|\mathcal{V}|} and any c ∈ ℝ c\in\mathbb{R} , σ ⁡ ( z + c ​ 𝟏 ) = σ ⁡ ( z ) \sigma(z+c\mathbf{1})=\sigma(z) . Conversely, σ ⁡ ( z ) = σ ⁡ ( z ′ ) \sigma(z)=\sigma(z^{\prime}) implies z ′ − z ∈ span ​ { 𝟏 } z^{\prime}-z\in\mathrm{span}\{\mathbf{1}\} .

###### Proof.

For the forward direction, the i i -th coordinate of σ ⁡ ( z + c ​ 𝟏 ) \sigma(z+c\mathbf{1}) is e z i + c ∑ j e z j + c = e c ​ e z i e c ​ ∑ j e z j = σ ​ ( z ) i \frac{e^{z_{i}+c}}{\sum_{j}e^{z_{j}+c}}=\frac{e^{c}e^{z_{i}}}{e^{c}\sum_{j}e^{z_{j}}}=\sigma(z)_{i} . For the converse, σ ⁡ ( z ) = σ ⁡ ( z ′ ) \sigma(z)=\sigma(z^{\prime}) implies z i − z j = z i ′ − z j ′ z_{i}-z_{j}=z^{\prime}_{i}-z^{\prime}_{j} for all i , j i,j (by taking logs of coordinate ratios), so z ′ − z z^{\prime}-z is a constant vector. ∎

###### Theorem 7 (Null-direction identity; formal version of ( 9 )) .

For any output-space OPD loss ℓ out \ell_{\mathrm{out}} as above, h θ − h T ∈ 𝒩 W ⟹ ℓ out ​ ( h θ , h T ) = 0 . h_{\theta}-h_{T}\in\mathcal{N}_{W}\quad\Longrightarrow\quad\ell_{\mathrm{out}}(h_{\theta},h_{T})=0. (27)

###### Proof.

If h θ − h T ∈ 𝒩 W h_{\theta}-h_{T}\in\mathcal{N}_{W} , then by ( 26 ) there exists c ∈ ℝ c\in\mathbb{R} with W head ​ ( h θ − h T ) = c ​ 𝟏 W_{\mathrm{head}}(h_{\theta}-h_{T})=c\mathbf{1} , i.e. z θ = z T + c ​ 𝟏 z_{\theta}=z_{T}+c\mathbf{1} . By Lemma 2 , σ ⁡ ( z θ ) = σ ⁡ ( z T ) \sigma(z_{\theta})=\sigma(z_{T}) . Since ℓ out \ell_{\mathrm{out}} vanishes whenever the two output distributions coincide, ℓ out ​ ( h θ , h T ) = 0 \ell_{\mathrm{out}}(h_{\theta},h_{T})=0 . ∎

To formalize ( 10 ) we need a local Lipschitz upper bound on any output-space loss in terms of ‖ z θ − z T ‖ 2 \|z_{\theta}-z_{T}\|_{2} . Such a bound holds for every standard ℓ out \ell_{\mathrm{out}} under mild regularity (e.g., logits bounded in a compact set), with a constant depending only on ℓ out \ell_{\mathrm{out}} and the logit range:

###### Lemma 3 (Local Lipschitzness of output-space losses) .

Let ℓ out \ell_{\mathrm{out}} be the sampled-token, top- k k , or full-vocabulary reverse KL. On any compact logit region 𝒵 ⊂ ℝ | 𝒱 | \mathcal{Z}\subset\mathbb{R}^{|\mathcal{V}|} , there exists C ℓ < ∞ C_{\ell}<\infty such that ℓ out ​ ( h θ , h T ) ≤ C ℓ ​ ‖ z θ − z T − c ∗ ​ 𝟏 ‖ 2 2 for all z θ , z T ∈ 𝒵 , \ell_{\mathrm{out}}(h_{\theta},h_{T})\;\leq\;C_{\ell}\,\|z_{\theta}-z_{T}-c^{\!*}\mathbf{1}\|_{2}^{2}\quad\text{for all}\quad z_{\theta},z_{T}\in\mathcal{Z}, (28) where c ∗ = 1 | 𝒱 | ​ 𝟏 ⊤ ​ ( z θ − z T ) c^{\!*}=\tfrac{1}{|\mathcal{V}|}\mathbf{1}^{\top}(z_{\theta}-z_{T}) projects out the softmax-invariant direction.

###### Proof sketch.

The reverse KL D KL ( σ ( z T ) ∥ σ ( z θ ) ) D_{\mathrm{KL}}(\sigma(z_{T})\|\sigma(z_{\theta})) has gradient and Hessian in z θ z_{\theta} that are continuous in z θ z_{\theta} and vanish at z θ = z T + c ∗ ​ 𝟏 z_{\theta}=z_{T}+c^{\!*}\mathbf{1} ; on a compact 𝒵 \mathcal{Z} its Hessian is operator-norm bounded. A second-order Taylor expansion in z θ − z T z_{\theta}-z_{T} around the additive-invariance optimum then yields ( 28 ) with C ℓ C_{\ell} proportional to half the Hessian’s operator-norm bound on 𝒵 \mathcal{Z} . The sampled-token and top- k k estimators are pointwise convex combinations of the full-vocabulary log-ratios and inherit the same upper bound (up to a constant). ∎

###### Theorem 8 (Spectral gap; formal version of ( 10 )) .

Under the setup of this section and the bound ( 28 ), for any α ∈ ℝ ∖ { 0 } \alpha\!\in\!\mathbb{R}\setminus\{0\} and the bottom right-singular vector v d v_{d} with ‖ v d ‖ 2 = 1 \|v_{d}\|_{2}=1 , ‖ h θ − h T ‖ 2 2 ℓ out ​ ( h θ , h T ) ≥ 1 C ℓ ​ ( σ 1 σ d ) 2 when h θ − h T = α ​ v d . \frac{\|h_{\theta}-h_{T}\|_{2}^{2}}{\ell_{\mathrm{out}}(h_{\theta},h_{T})}\;\geq\;\frac{1}{C_{\ell}}\,\Bigl(\frac{\sigma_{1}}{\sigma_{d}}\Bigr)^{\!2}\quad\text{when}\quad h_{\theta}-h_{T}=\alpha v_{d}. (29) In particular, holding ℓ out \ell_{\mathrm{out}} fixed, hidden-state perturbations along v d v_{d} can grow σ 1 / σ d \sigma_{1}/\sigma_{d} times larger in ℓ 2 \ell_{2} norm than perturbations along the top singular direction v 1 v_{1} .

###### Proof.

Take Δ ​ h = α ​ v d \Delta h\!=\!\alpha v_{d} . Then ‖ Δ ​ h ‖ 2 2 = α 2 \|\Delta h\|_{2}^{2}=\alpha^{2} and, by the SVD, W head ​ Δ ​ h = α ​ σ d ​ u d W_{\mathrm{head}}\Delta h=\alpha\sigma_{d}u_{d} where u d u_{d} is the corresponding left-singular vector with ‖ u d ‖ 2 = 1 \|u_{d}\|_{2}=1 . Since u d ⟂ 𝟏 u_{d}\perp\mathbf{1} generically (or after subtracting its component along 𝟏 \mathbf{1} via the projector in ( 28 )), the residual after removing the additive-invariance direction satisfies ‖ z θ − z T − c ∗ ​ 𝟏 ‖ 2 ≤ ‖ W head ​ Δ ​ h ‖ 2 = α ​ σ d \|z_{\theta}-z_{T}-c^{\!*}\mathbf{1}\|_{2}\leq\|W_{\mathrm{head}}\Delta h\|_{2}=\alpha\sigma_{d} . By Lemma 3 , ℓ out ≤ C ℓ ​ α 2 ​ σ d 2 \ell_{\mathrm{out}}\leq C_{\ell}\,\alpha^{2}\sigma_{d}^{2} , i.e. α 2 ≥ ℓ out / ( C ℓ ​ σ d 2 ) \alpha^{2}\geq\ell_{\mathrm{out}}/(C_{\ell}\sigma_{d}^{2}) . Therefore ‖ h θ − h T ‖ 2 2 ℓ out = α 2 ℓ out ≥ 1 C ℓ ​ σ d 2 . \frac{\|h_{\theta}-h_{T}\|_{2}^{2}}{\ell_{\mathrm{out}}}\;=\;\frac{\alpha^{2}}{\ell_{\mathrm{out}}}\;\geq\;\frac{1}{C_{\ell}\sigma_{d}^{2}}. For comparison, the analogous bound along v 1 v_{1} is ‖ h θ − h T ‖ 2 2 / ℓ out ≤ 1 / ( c ℓ ​ σ 1 2 ) \|h_{\theta}-h_{T}\|_{2}^{2}/\ell_{\mathrm{out}}\leq 1/(c_{\ell}\sigma_{1}^{2}) for the lower Lipschitz constant c ℓ c_{\ell} of ℓ out \ell_{\mathrm{out}} , so the ratio between the two directions scales as ( σ 1 / σ d ) 2 (\sigma_{1}/\sigma_{d})^{2} up to constants determined by ℓ out \ell_{\mathrm{out}} , recovering ( 29 ) after absorbing constants into C ℓ C_{\ell} . ∎

###### Remark 2 (Intermediate layers) .

Theorems 7 and 8 concern only the last-layer hidden state, because any output-space ℓ out \ell_{\mathrm{out}} is computed solely from W head ​ h ( L ) W_{\mathrm{head}}\,h^{(L)} and therefore has no functional dependence on intermediate states h ( l ) h^{(l)} for l < L l\!<\!L . For any l < L l\!<\!L , an arbitrary perturbation of h ( l ) h^{(l)} that leaves h ( L ) h^{(L)} unchanged (e.g., a perturbation in the kernel of the residual stack from layer l l onwards) yields ℓ out = 0 \ell_{\mathrm{out}}=0 for every output-space objective. OPRD ( 6 ) with ℒ layer ∋ l \mathcal{L}_{\mathrm{layer}}\ni l directly penalizes ‖ h θ , t ( l ) − h T , t ( l ) ‖ 2 2 \|h_{\theta,t}^{(l)}-h_{T,t}^{(l)}\|_{2}^{2} at that layer and is therefore the only mechanism considered in this paper that can constrain intermediate hidden states.

##### Sub-summary ( Theorem 2 ).

Theorem 7 formalizes ( 9 ): every output-space distillation objective treats the entire affine subspace 𝒩 W \mathcal{N}_{W} as invisible, regardless of how much it inspects the output distribution. Theorem 8 formalizes ( 10 ): the LM head’s singular-value spread σ 1 / σ d \sigma_{1}/\sigma_{d} amplifies hidden-state deviations along v d v_{d} by a ( σ 1 / σ d ) 2 (\sigma_{1}/\sigma_{d})^{2} factor for the same output-space loss budget, empirically 10 6 ∼ 10 8 × 10^{6}\!\sim\!10^{8}\times for production LLMs. Remark 2 extends both observations to intermediate layers. OPRD ( 6 ) penalizes exactly the directions and layers that output-space OPD cannot.

##### Overall summary of § B .

The theorems above formalize Theorem 1 (gradient variance and SNR) in one-to-one correspondence with the intuitive claims of § 3.2 : they explain why OPRD provides a more reliable optimization signal than sampled-token OPD, especially in late-stage training, and why adding OPRD to OPD strictly improves the SGD convergence bound without introducing additional noise. These guarantees apply under mild regularity conditions that hold for any standard LLM, supporting our empirical observation that combining OPD with OPRD yields a stronger and more stable result than OPD alone.

### B.6 Formal Results for Theorem 3 : Optimality of the Low-Rank Bridge

We now formalize the claim that the PCA-based low-rank bridge is optimal in an information-theoretic sense and that the bridge rank r r controls a bias–variance trade-off.

#### B.6.1 Setup

Consider a single layer pair ( l S , l T ) (l_{S},l_{T}) (we drop layer indices for clarity). Let h T ∈ ℝ d T h_{T}\in\mathbb{R}^{d_{T}} denote the teacher hidden state at a response position, drawn from a distribution with mean μ T \mu_{T} and covariance Σ T ≻ 0 \Sigma_{T}\succ 0 . Denote the eigendecomposition Σ T = V ​ Λ ​ V ⊤ \Sigma_{T}=V\Lambda V^{\top} , where Λ = diag ⁡ ( λ 1 , … , λ d T ) \Lambda=\mathrm{diag}(\lambda_{1},\ldots,\lambda_{d_{T}}) with λ 1 ≥ ⋯ ≥ λ d T > 0 \lambda_{1}\geq\cdots\geq\lambda_{d_{T}}>0 , and V = [ v 1 , … , v d T ] V=[v_{1},\ldots,v_{d_{T}}] are the corresponding eigenvectors (principal directions).

Let h S ∈ ℝ d S h_{S}\in\mathbb{R}^{d_{S}} denote the student hidden state at the same position. We model the cross-model alignment via the per-direction correlation : after projecting both models into the teacher’s principal coordinate system, the correlation between teacher component i i and the best linear prediction from the student is ρ i ∈ [ 0 , 1 ] \rho_{i}\in[0,1] . Formally, let z T = V ⊤ ​ ( h T − μ T ) ∈ ℝ d T z_{T}=V^{\top}(h_{T}-\mu_{T})\in\mathbb{R}^{d_{T}} be the teacher’s whitened coordinates. Then ρ i 2 ≜ R 2 ​ ( z T , i ∣ h S ) \rho_{i}^{2}\triangleq R^{2}(z_{T,i}\mid h_{S}) , the coefficient of determination of the best linear predictor of the i i -th teacher component from the student.

###### Assumption 2 (Monotone alignment decay) .

The per-direction alignment ρ i \rho_{i} is non-increasing in i i : ρ 1 ≥ ρ 2 ≥ ⋯ ≥ ρ d T \rho_{1}\geq\rho_{2}\geq\cdots\geq\rho_{d_{T}} . That is, the principal (high-variance) directions of the teacher are better predicted by the student than the minor (low-variance) directions.

This assumption is empirically verified in our experiments: the rank-cosine curve ( Figure 12 ) shows that alignment concentrates in the top principal components and degrades monotonically as rank increases.

#### B.6.2 Rate–Distortion Optimality

###### Theorem 9 (PCA bridge is rate–distortion optimal) .

Assume h T ∼ 𝒩 ⁡ ( μ T , Σ T ) h_{T}\sim\mathcal{N}(\mu_{T},\Sigma_{T}) . Among all rank- r r linear encoders P ∈ ℝ r × d T P\in\mathbb{R}^{r\times d_{T}} , the PCA projection P ∗ = [ v 1 , … , v r ] ⊤ P^{*}=[v_{1},\ldots,v_{r}]^{\top} minimizes the reconstruction distortion: P ∗ = arg ⁡ min P ∈ ℝ r × d T rank ⁡ ( P ) = r ⁡ 𝔼 ⁡ [ ‖ h T − μ T − P ⊤ ​ P ​ ( h T − μ T ) ‖ 2 ] . P^{*}=\arg\min_{\begin{subarray}{c}P\in\mathbb{R}^{r\times d_{T}}\\ \mathrm{rank}(P)=r\end{subarray}}\;\mathbb{E}\left[\|h_{T}-\mu_{T}-P^{\top}P(h_{T}-\mu_{T})\|^{2}\right]. The minimum distortion is D ∗ ​ ( r ) = ∑ i = r + 1 d T λ i D^{*}(r)=\sum_{i=r+1}^{d_{T}}\lambda_{i} .

###### Proof.

This is a direct consequence of the Eckart–Young–Mirsky theorem applied to the centered data matrix, or equivalently, of the classical result that PCA minimizes mean-squared reconstruction error among all linear rank- r r projections. For Gaussian sources, this coincides with the rate–distortion function under squared-error distortion at rate R = 1 2 ​ ∑ i = 1 r log ⁡ ( λ i / θ ) R=\frac{1}{2}\sum_{i=1}^{r}\log(\lambda_{i}/\theta) (water-filling), where θ \theta is chosen so that exactly r r components are active. The optimal encoder projects onto the top- r r eigenvectors of Σ T \Sigma_{T} , which is precisely our PCA basis P T P_{T} . ∎

Interpretation. The PCA bridge is not merely a convenient heuristic; it is the information-theoretically optimal linear channel at capacity r r . Any other rank- r r projection would discard more teacher information.

#### B.6.3 Bias–Variance Decomposition of Distillation Error

We now analyze the distillation error (not reconstruction error), which accounts for the student’s ability to match the projected teacher.

###### Definition 4 (Distillation error at rank r r ) .

Given the PCA bridge P T = [ v 1 , … , v r ] ⊤ P_{T}=[v_{1},\ldots,v_{r}]^{\top} and an optimal student projector P S P_{S} (trained to minimize MSE in the r r -dimensional subspace), the expected per-position distillation error is: ℰ ⁡ ( r ) ≜ 𝔼 ⁡ [ ‖ P S ​ h S − P T ​ ( h T − μ T ) ‖ 2 ] . \mathcal{E}(r)\triangleq\mathbb{E}\left[\|P_{S}h_{S}-P_{T}(h_{T}-\mu_{T})\|^{2}\right].

###### Theorem 10 (Bias–variance decomposition) .

Under Assumption 2 and assuming P S P_{S} is the population-optimal linear map from h S h_{S} to the r r -dimensional bridge space, the total distillation error (including the contribution from discarded dimensions) decomposes as: ℰ total ​ ( r ) = ∑ i > r λ i ​ ρ i 2 ⏟ Bias ​ B ​ ( r ) + ∑ i = 1 r λ i ​ ( 1 − ρ i 2 ) ⏟ Variance ​ V ​ ( r ) , \mathcal{E}_{\mathrm{total}}(r)=\underbrace{\sum_{i>r}\lambda_{i}\,\rho_{i}^{2}}_{\text{Bias }B(r)}\;+\;\underbrace{\sum_{i=1}^{r}\lambda_{i}\,(1-\rho_{i}^{2})}_{\text{Variance }V(r)}, (30) where: • B ⁡ ( r ) = ∑ i > r λ i ​ ρ i 2 B(r)=\sum_{i>r}\lambda_{i}\rho_{i}^{2} is the bias : the aligned signal in directions i > r i>r that the bridge discards. This term decreases as r r increases.

• V ⁡ ( r ) = ∑ i = 1 r λ i ​ ( 1 − ρ i 2 ) V(r)=\sum_{i=1}^{r}\lambda_{i}(1-\rho_{i}^{2}) is the variance : the misaligned noise in directions i ≤ r i\leq r that the bridge transmits but the student cannot match. This term increases as r r increases.

Under Assumption 2 , ℰ total ​ ( r ) \mathcal{E}_{\mathrm{total}}(r) is quasi-convex in r r , and the minimizer r ∗ = arg ⁡ min r ​ ℰ total ​ ( r ) r^{*}=\arg\min_{r}\mathcal{E}_{\mathrm{total}}(r) satisfies:

The optimal rank is the direction at which alignment transitions from “mostly signal” to “mostly noise.”

###### Proof.

We decompose the total error into contributions from included and excluded directions.

Step 1: Error from included directions ( i ≤ r i\leq r ). In the r r -dimensional bridge space, the i i -th component of the teacher target is z T , i = v i ⊤ ​ ( h T − μ T ) z_{T,i}=v_{i}^{\top}(h_{T}-\mu_{T}) , which has variance λ i \lambda_{i} . The optimal linear predictor from h S h_{S} achieves R 2 = ρ i 2 R^{2}=\rho_{i}^{2} , so the residual variance (prediction error) in direction i i is: 𝔼 [ ( P S h S ) i − z T , i ) 2 ] = λ i ( 1 − ρ i 2 ) . \mathbb{E}[(P_{S}h_{S})_{i}-z_{T,i})^{2}]=\lambda_{i}(1-\rho_{i}^{2}). Summing over included directions gives V ⁡ ( r ) = ∑ i = 1 r λ i ​ ( 1 − ρ i 2 ) V(r)=\sum_{i=1}^{r}\lambda_{i}(1-\rho_{i}^{2}) .

Step 2: Error from excluded directions ( i > r i>r ). Directions i > r i>r are not transmitted through the bridge, so the student receives no supervision along them. However, these directions contain aligned signal (the student could have matched them if they were included). The “lost opportunity” is the signal that was discardable: λ i ​ ρ i 2 \lambda_{i}\rho_{i}^{2} per direction. Summing gives B ⁡ ( r ) = ∑ i > r λ i ​ ρ i 2 B(r)=\sum_{i>r}\lambda_{i}\rho_{i}^{2} .

Step 3: Optimality condition. The marginal effect of including direction r r is: Δ ⁡ ( r ) = ℰ total ​ ( r ) − ℰ total ​ ( r − 1 ) = λ r ​ ( 1 − ρ r 2 ) − λ r ​ ρ r 2 = λ r ​ ( 1 − 2 ​ ρ r 2 ) . \Delta(r)=\mathcal{E}_{\mathrm{total}}(r)-\mathcal{E}_{\mathrm{total}}(r-1)=\lambda_{r}(1-\rho_{r}^{2})-\lambda_{r}\rho_{r}^{2}=\lambda_{r}(1-2\rho_{r}^{2}). This is negative (including direction r r helps) when ρ r 2 > 1 / 2 \rho_{r}^{2}>1/2 and positive (including direction r r hurts) when ρ r 2 < 1 / 2 \rho_{r}^{2}<1/2 . Under Assumption 2 , ρ i 2 \rho_{i}^{2} is non-increasing, so Δ ⁡ ( r ) \Delta(r) transitions from negative to positive exactly once, establishing quasi-convexity and the optimality condition ρ r ∗ 2 ≈ 1 / 2 \rho_{r^{*}}^{2}\approx 1/2 . ∎

Connection to the low-pass filter analogy. The bias–variance decomposition provides a precise formulation of the low-pass filter intuition from § 3.3.4 : • The “cutoff frequency” of the filter is r ∗ r^{*} : directions below r ∗ r^{*} are “passed” (high ρ i \rho_{i} , mostly signal), directions above r ∗ r^{*} are “stopped” (low ρ i \rho_{i} , mostly noise).

• The “passband ripple” is V ⁡ ( r ∗ ) V(r^{*}) : even within the passed directions, some noise leaks through.

• The “stopband leakage” is B ⁡ ( r ∗ ) B(r^{*}) : even among the stopped directions, some signal is lost.

• The optimal filter (optimal r ∗ r^{*} ) minimizes the sum of ripple and leakage.

Empirical verification. In our Qwen3-4B → \to Qwen3-1.7B experiments, the rank-cosine curve ( Figure 12 ) peaks at r = 8 r\!=\!8 and declines thereafter, consistent with the prediction that r ∗ ≈ 8 r^{*}\approx 8 is the point where ρ i 2 \rho_{i}^{2} crosses 1 / 2 1/2 . The rapid spectral decay of Σ T \Sigma_{T} (verifiable from the PCA explained-variance ratio) ensures that both B ⁡ ( r ∗ ) B(r^{*}) and V ⁡ ( r ∗ ) V(r^{*}) are small at this operating point.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
