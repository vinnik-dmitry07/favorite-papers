##### Report GitHub Issue

Content selection saved. Describe the issue below:

# ESPO: Entropy Importance Sampling Policy Optimization

###### Abstract

Reinforcement learning (RL) has become a central component of post-training for large language models (LLMs), particularly for complex reasoning tasks that require stable optimization over long generation horizons. However, achieving performance at scale often introduces a fundamental trade-off between training stability and training efficiency. Token-level optimization applies fine-grained updates at the individual units, but is prone to high variance in gradient estimation, which can result in unstable training dynamics. In contrast, Sequence-level optimization often relies on aggressive clipping mechanisms to ensure stable updates. However, such design may discard a large fraction of valid training samples, leading to inefficient gradient utilization and reduced training efficiency. We refer to this phenomenon as gradient underutilization . In this work, we propose E ntropy Importance S ampling P olicy O ptimization (ESPO), a novel framework that aims to combine fine-grained updates with stable training. ESPO decomposes sequences into groups based on predictive entropy, enabling (1) Entropy Grouping Importance Sampling to capture intra-sequence heterogeneity, and (2) Entropy Adaptive Clipping to dynamically allocate trust regions based on model uncertainty. Extensive experiments on mathematical reasoning benchmarks demonstrate that ESPO not only accelerates convergence but also achieves state-of-the-art performance, notably improving accuracy on the challenging mathematical benchmarks. 1 1 1 Code is available at: https://github.com/ShopeeLLM/ESPO

## 1 Introduction

Recent progress in LLM has increasingly emphasized their ability to perform complex reasoning, where correct outputs depend on multi-step logical inference rather than surface-level pattern matching. In such settings, post-training objectives extend beyond instruction following and require aligning the model’s generation process with verifiable reasoning correctness. Reinforcement learning has therefore become a key component of modern reasoning-oriented training pipelines. By allowing models to explore diverse reasoning trajectories and optimize towards task-level correctness, RL provides a natural framework for improving decision-making over long sequences.

However, current RL strategies face a fundamental trade-off induced by optimization granularity , which directly affects the balance between training stability and training efficiency. Early approaches like Proximal Policy Optimization (PPO) [ 9 ] operate at the token level, offering fine-grained control but suffering from high variance and the heavy computational burden of maintaining value networks. To address this, a series of variants have been proposed and can be broadly categorized into two classes: token-level (e.g., GRPO [ 12 ] , DAPO [ 19 ] , GMPO [ 24 ] , CISPO [ 2 ] , etc.) and sequence-level (e.g., GSPO [ 25 ] , etc.) optimization. In practice, token-level variants are prone to unstable training dynamics, while sequence-level approaches tend to exhibit low data utilization due to aggressive clipping.

To resolve these limitations, we introduce E ntropy Importance S ampling P olicy O ptimization (ESPO), a framework that restores fine-grained optimization without sacrificing the stability benefits of group-based methods. The core insight of ESPO is that policy entropy [ 10 ] serves as a natural indicator for optimization granularity . Previous work [ 16 ] proposes using entropy as the criterion for credit assignment by computing gradients only for the most uncertain tokens. This selective update improves efficiency by concentrating the learning on regions where the model exhibits greater uncertainty. Another line of work [ 15 ] categorizes tokens into distinct entropy types, and assigns each a fixed clipping range. These designs are motivated by the role of entropy, as illustrated in Figure 1 , high-entropy tokens correspond to pivotal decision points that steer the reasoning trajectory across alternative branches.

ESPO operates on token groups —dynamically grouped by their entropy profile. Specifically, it employs Entropy Grouping Importance Sampling to decompose the global sequence ratio into local group ratios, allowing gradients to flow freely in consistent segments while being carefully modulated in divergent ones. Furthermore, it introduces Entropy Adaptive Clipping , which assigns wider clipping bounds to high-entropy (uncertain) groups to encourage exploration, and tighter bounds to low-entropy (confident) groups to enforce stability.

The contributions of this work are summarized as follows:

• We identify limitations in existing methods with respect to training efficiency and training stability, and categorize these issues into token-level and sequence-level policy optimization.

• We propose E ntropy Importance S ampling P olicy O ptimization (ESPO), an entropy-based algorithm that control optimization granularity and improve data utilization.

• We provide detailed empirical analyses and ablation studies to examine the effects of core components, offering competitive performance on mathematical reasoning benchmarks.

## 2 Background

### 2.1 Related Works

Reinforcement learning has emerged as a central paradigm for optimizing LLMs, particularly in tasks requiring verifiable reasoning such as mathematics, coding, and question answering. Early RL approaches were largely based on Proximal Policy Optimization (PPO) [ 9 ] , where policy updates are guided by reward models or rule-based verifiers. To reduce the computational cost and instability of value-function training in PPO, Group Relative Policy Optimization (GRPO) [ 11 ] eliminates the critic and estimates advantages through group-wise relative ranking, achieving strong performance without relying on explicit value models. Building on GRPO, a series of recent methods have further improved stability, credit assignment, and rollout efficiency. DAPO [ 19 ] introduces clip-higher and dynamic sampling to counter entropy collapse and filter zero-advantage groups, while GSPO [ 25 ] elevates optimization granularity to the sequence level, aligning the update unit with reward signals. The geometric average of importance sampling ratios is used in GMPO [ 24 ] and employs a narrower clip range to reduce the optimization variance. GTPO [ 14 ] and GRPO-S leverages entropy-weighted rewards to better handle outliers and sparse credit. DCPO [ 18 ] dynamically adapts clipping ranges by token to enhance exploration and make better use of otherwise degenerate rollouts. CISPO [ 2 ] further refines clipping behavior by applying clipping only to the importance sampling ratios, while leaving gradient magnitudes unclipped. Complementary efforts focus on reward shaping, advantage normalization, and data-centric strategies: EMPO [ 21 ] incorporates semantic entropy, BNPO [ 17 ] normalizes rewards via Beta distributions, and large-scale datasets with curriculum learning, such as Open-Reasoner-Zero [ 4 ] , have proven crucial for high-quality signal alignment. Beyond this, SPO [ 3 ] incorporates segment-level optimization as a principled design to address the credit assignment challenge, thereby achieving more accurate reward attribution. Together, these developments reflect a broader trend toward efficient, stable, and reasoning-aligned RL methods for LLMs.

### 2.2 Preliminary

Token-level policy optimization performs policy updates at the granularity of individual tokens. Representative approaches include GRPO, DAPO, GMPO and CISPO, which differ in their data utilization method, importance sampling computation, clipping strategies. We introduce GRPO as a concrete example in the following.

GRPO [ 11 ] is a reinforcement learning algorithm that evaluates candidate responses purely through relative preferences within a group. For a given query q q , GRPO generates a set of responses { y i } i = 1 G \{y_{i}\}_{i=1}^{G} and assigns a sequence-level advantage A i A_{i} to each response. The policy is updated using a PPO-inspired objective applied at the token level: 𝒥 GRPO ( θ ) = 𝔼 x ∼ 𝒟 , { y i } i = 1 G ∼ π θ old ( ⋅ | x ) [ 1 G ∑ i = 1 G 1 | y i | ∑ t = 1 | y i | min ( r i , t ( θ ) A i , clip ( r i , t ( θ ) , 1 − ϵ low token , 1 + ϵ high token ) A i ) ] \mathcal{J}_{\text{GRPO}}(\theta)=\mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\Bigg[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\\ \min\Big(r_{i,t}(\theta)A_{i},\ \operatorname{clip}(r_{i,t}(\theta),1-\epsilon_{\text{low}}^{\text{token}},1+\epsilon_{\text{high}}^{\text{token}})A_{i}\Big)\Bigg] (1) where r i , t ​ ( θ ) = π θ ​ ( y i , t ∣ q , y i , < t ) π θ old ​ ( y i , t ∣ q , y i , < t ) r_{i,t}(\theta)=\frac{\pi_{\theta}(y_{i,t}\mid q,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}\mid q,y_{i,<t})} represents the token-level importance ratio.

Despite its simplicity, GRPO faces significant challenges. Token-level ratios are inherently noisy, and this noise compounds across long sequences, leading to unstable gradients [ 24 ] . Clipping can exacerbate this instability by unevenly scaling token contributions, sometimes resulting in divergence or training collapse. Furthermore, since each token ratio is estimated from a single sample, it provides only a weak approximation of the underlying policy distribution, misaligning the optimization with actual reward signals [ 25 ] . Lastly, token-focused credit assignment ignores global sequence patterns, making it difficult to guide coherent long-horizon generation.

Sequence-level policy optimization aims to better align the optimization objective with sequence-level importance sampling by treating entire trajectories as optimization units. GSPO [ 25 ] is a representative approach in this category.

Instead of treating tokens independently, GSPO computes an importance ratio at the sequence level: s i ​ ( θ ) = ( π θ ​ ( y i ∣ q ) π θ old ​ ( y i ∣ q ) ) 1 | y i | s_{i}(\theta)=\Big(\frac{\pi_{\theta}(y_{i}\mid q)}{\pi_{\theta_{\text{old}}}(y_{i}\mid q)}\Big)^{\frac{1}{|y_{i}|}} (2) and projects it to individual tokens using a stop-gradient operation: s i , t ​ ( θ ) = sg ​ [ s i ​ ( θ ) ] ⋅ π θ ​ ( y i , t ∣ q , y i , < t ) sg ​ [ π θ ​ ( y i , t ∣ q , y i , < t ) ] s_{i,t}(\theta)=\text{sg}[s_{i}(\theta)]\cdot\frac{\pi_{\theta}(y_{i,t}\mid q,y_{i,<t})}{\text{sg}[\pi_{\theta}(y_{i,t}\mid q,y_{i,<t})]} (3)

The training objective combines sequence-level ratios with clipped advantages: 𝒥 GSPO ( θ ) = 𝔼 x ∼ 𝒟 , { y i } i = 1 G ∼ π θ old ( ⋅ | x ) [ 1 G ∑ i = 1 G 1 | y i | ∑ t = 1 | y i | min ( s i , t ( θ ) A i , clip ( s i , t ( θ ) , 1 − ϵ low seq , 1 + ϵ high seq ) A i ) ] \mathcal{J}_{\text{GSPO}}(\theta)=\mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\Bigg[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\\ \min\Big(s_{i,t}(\theta)A_{i},\,\operatorname{clip}\!\big(s_{i,t}(\theta),1-\epsilon_{\text{low}}^{\text{seq}},1+\epsilon_{\text{high}}^{\text{seq}}\big)A_{i}\Big)\Bigg] (4)

This sequence-level approach stabilizes training by reducing sensitivity to outlier tokens. However, all tokens within a sequence share the same ratio and advantage, making it difficult to attribute credit to specific positions. Additionally, conservative clipping thresholds, required to maintain stability, result in many samples being truncated and slow policy improvement. Relaxing the thresholds could improve learning but risks reintroducing the instability GSPO seeks to eliminate.

## 3 Entropy Importance Sampling Policy Optimization

ESPO is designed to improve data efficiency and training stability by structuring policy updates according to model uncertainty. At a high level, ESPO consists of two stages. First, ESPO performs Entropy Grouping Importance Sampling , where tokens within each sequence are grouped according to their entropy and the sequence-level importance ratio is decomposed into group-level ratios. This enables more fine-grained credit assignment by allowing updates to focus on high-uncertainty decision regions while maintaining coherence within low-uncertainty segments. Second, ESPO applies Entropy Adaptive Clipping , which assigns different clipping ranges to different entropy groups, encouraging exploration on uncertain tokens while enforcing stability on confident ones.

We first formulate the complete ESPO objective (Section 3.1), then elaborate on each component: entropy-adaptive clipping (Section 3.2), token grouping by entropy (Section 3.3), and token-level advantage normalization (Section 3.4).

### 3.1 Objective Formulation

Formally, given a query x ∼ 𝒟 x\sim\mathcal{D} and a group of G G sampled responses { y i } i = 1 G ∼ π θ old ( ⋅ | x ) \{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x) , we partition each sequence y i y_{i} into a collection of groups { τ } \{\tau\} , where each groups y τ y_{\tau} is not necessarily contiguous in the token space. Instead of relying on textual or syntactic boundaries, we group samples based on the model’s internal features that reflect uncertainty. Such uncertainty-related features can be defined at different orders, and ESPO specifically leverage second-order signals(e.g., policy entropy) for grouping. These features reflect the model’s internal uncertainty and confidence structure, allowing the groups to capture regions of similar policy behavior rather than continuous spans in surface form. ESPO defines the following objective:

𝒥 ESPO ( θ ) = 𝔼 x ∼ 𝒟 , { y i } i = 1 G ∼ π θ old ( ⋅ | x ) [ 1 G ∑ i = 1 G 1 | τ | ∑ τ 1 | y τ | ∑ t = 1 | y τ | min ( s τ i , t ( θ ) A ^ τ i , t , clip ( s τ i , t ( θ ) , 1 − ϵ τ , 1 + ϵ τ ) A ^ τ i , t ) ] \mathcal{J}_{\mathrm{ESPO}}(\theta)=\mathbb{E}_{x\sim\mathcal{D},\,\{y_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|x)}\bigg[\frac{1}{G}\sum_{i=1}^{G}{\color[rgb]{1,0,0}\frac{1}{|\tau|}\sum_{\tau}\frac{1}{|y_{\tau}|}}\\ \sum_{t=1}^{|y_{\tau}|}\min\big(s_{\tau}^{i,t}(\theta)\hat{A}_{\tau}^{i,t},\,\operatorname{clip}(s_{\tau}^{i,t}(\theta),1-{\color[rgb]{1,0,0}\epsilon_{\tau}},1+{\color[rgb]{1,0,0}\epsilon_{\tau}})\hat{A}_{\tau}^{i,t}\big)\bigg] (5) where s τ i , t ​ ( θ ) s_{\tau}^{i,t}(\theta) denotes the importance ratio at the token-level within groups τ \tau , ϵ τ \epsilon_{\tau} is the entropy adaptive clipping threshold, and A ^ i , t \hat{A}_{i,t} is the normalized token-level advantage.

### 3.2 Entropy Adaptive Clipping

Entropy provides a natural and model-intrinsic signal for measure token-level uncertainty. Following prior studies, we leverage predictive entropy to both token groups and determine their clipping range.

Specifically, we first compute the token-level entropy: e t i = − ∑ v ∈ 𝒱 π θ old ( v ∣ x , y i , < t ) log π θ old ( v ∣ x , y i , < t ) \displaystyle e_{t}^{i}=-\sum_{v\in\mathcal{V}}\pi_{\theta_{\text{old}}}(v\mid x,y_{i,<t})\log\pi_{\theta_{\text{old}}}(v\mid x,y_{i,<t}) (6) where 𝒱 \mathcal{V} denotes the vocabulary space. The entropy reflects how uncertain the model is about the next-token distribution, with higher values indicating less confidence.

In ESPO, we extend this signal to the fine-grained level. Tokens are grouped into separation { τ } \{\tau\} according to their entropy values, so that tokens with similar uncertainty belong to the same separation: τ k = { t ∣ e t i ∈ ℛ k } , { τ k } k = 1 K i = 𝒮 ⁡ ( y i ) , \displaystyle\tau_{k}=\{\,t\mid e_{t}^{i}\in\mathcal{R}_{k}\,\},\qquad\{\tau_{k}\}_{k=1}^{K_{i}}=\mathcal{S}(y_{i}), (7) where ℛ k \mathcal{R}_{k} denotes the entropy range corresponding to the k k -th group and 𝒮 \mathcal{S} represents the whole response sentence. In contrast to previous methods that apply fixed ranges, ESPO uses entropy statistics to dynamically compute each group’s clipping bound: ϵ τ = α log ⁡ | 𝒱 | ⋅ e t i | τ | , \displaystyle\epsilon_{\tau}=\frac{\alpha}{\log|\mathcal{V}|}\cdot\frac{e_{t}^{i}}{|\tau|}, (8)

where α \alpha is a global scaling factor and the denominator log ⁡ | 𝒱 | \log|\mathcal{V}| serves as the theoretical upper bound of the token entropy, normalizing the clipping coefficient across different vocabulary scales. Consequently, groups with higher average normalized entropy obtain larger clipping ranges, allowing more freedom for policy updates in uncertain regions, while low-entropy, confident groups are constrained by tighter clipping bounds to maintain stability.

This entropy-normalized adaptive design enables ESPO to dynamically balance exploration and stability, allocating larger optimization flexibility to uncertain regions while preserving GSPO’s stable training behavior across the entire sequence.

### 3.3 Entropy Grouping Importance Sampling

In the same way as GSPO-token decomposes the importance ratio to align optimization with the reward unit, we also decompose the ratio to allow token-wise advantage customization . Specifically, we define the entropy grouping importance ratio as follows: s τ i , t ​ ( θ ) := s ​ g ​ [ s τ i ​ ( θ ) ] ⋅ π θ ​ ( y i , t | x , y i , < t ) s ​ g ​ [ π θ old ​ ( y i , t | x , y i , < t ) ] , \displaystyle s_{\tau}^{i,t}(\theta):=sg\!\left[s_{\tau}^{i}(\theta)\right]\cdot\frac{\pi_{\theta}(y_{i,t}|x,y_{i,<t})}{sg\!\left[\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,<t})\right]}, (9) where s ​ g ​ [ ⋅ ] sg[\cdot] denotes the stop-gradient operator that blocks backpropagation through the detached component. The scaling term at the token grouping level s τ i ​ ( θ ) s_{\tau}^{i}(\theta) is defined as the length-normalized sequence ratio: s τ i ​ ( θ ) = ( π θ ​ ( y τ | x ) π θ old ​ ( y τ | x ) ) 1 | y τ | \displaystyle s_{\tau}^{i}(\theta)=\left(\frac{\pi_{\theta}(y_{\tau}|x)}{\pi_{\theta_{\text{old}}}(y_{\tau}|x)}\right)^{\!\tfrac{1}{|y_{\tau}|}} (10)

Intuitively, s τ i ​ ( θ ) s_{\tau}^{i}(\theta) captures global consistency throughout the group, while the token-level ratio π θ / π θ old \pi_{\theta}/\pi_{\theta_{\text{old}}} provides fine-grained local sensitivity. This hierarchical construction allows ESPO to adaptively modulate gradients within each group, preserving stable updates for globally consistent spans and emphasizing local corrections where necessary. As shown in Figure 2 , ESPO introduce entropy-based decomposition, enabling adaptive gradient modulation within each group.

### 3.4 Token Grouping Advantage Normalization

To address the long-standing issue of sparse reward signals and coarse credit assignment in reinforcement learning for large language models, many new works are emerging. For example, [ 5 ] , [ 26 ] , and [ 8 ] achieve fine-grained credit assignment by using the language model itself to perform a simple value function estimation, resulting in better performance than the baseline. This demonstrates the importance of fine-grained credit assignment in the online reinforcement learning (RL) training of reasoning models.

In this paper, We refine the advantage estimation at a finer granularity and compute token-wise normalized advantages within each group to better reflect local reward contributions. Formally, the token-level normalized advantage is defined as

A ^ τ i , t \displaystyle\hat{A}_{\tau}^{i,t} = 𝕀 [ i ∈ 𝒢 ] ⋅ R ⁡ ( y i , a ) − μ 𝒢 σ 𝒢 , \displaystyle=\mathbb{I}[i\in\mathcal{G}]\cdot\frac{R(y_{i},a)-\mu_{\mathcal{G}}}{\sigma_{\mathcal{G}}}, (11) where 𝒢 \displaystyle\text{where}\quad\mathcal{G} : = { i ∣ verifier succeeds } , \displaystyle:=\{\,i\mid\text{verifier succeeds}\,\}, μ 𝒢 \displaystyle\mu_{\mathcal{G}} : = mean ⁡ ( { R ⁡ ( y i , a ) } i ∈ 𝒢 ) , \displaystyle:=\operatorname{mean}\!\left(\{R(y_{i},a)\}_{i\in\mathcal{G}}\right), σ 𝒢 \displaystyle\sigma_{\mathcal{G}} : = std ⁡ ( { R ⁡ ( y i , a ) } i ∈ 𝒢 ) . \displaystyle:=\operatorname{std}\!\left(\{R(y_{i},a)\}_{i\in\mathcal{G}}\right).

Here R ⁡ ( y i , a ) R(y_{i},a) denotes the group-aware reward assigned by the verifier. Unlike GSPO, where the same advantage is propagated to all tokens in a sequence, ESPO allows each token (or group) to be weighted according to its relative contribution to the final reward. This design alleviates the sparsity of the reward signal by distributing gradients more precisely to informative regions, ensuring that learning is concentrated on tokens that are most responsible for success while suppressing noise from irrelevant or failed samples. As a result, ESPO enhances both the stability and efficiency of credit assignment across long and complex sequences.

## 4 Experiments

### 4.1 Experimental Setup

#### Baselines.

We compare ESPO with two classes of policy optimization baselines: (1) sequence-level methods (GSPO) and (2) token-level methods (DAPO, GMPO, CISPO). This covers the spectrum of granularity choices in contemporary LLM fine-tuning.

#### Configuration.

All experiments use the VERL framework [ 13 ] with vLLM [ 6 ] for rollouts. We train on SimpleRL [ 20 ] (8,192 prompts) for 3 epochs (200 steps) with a fixed learning rate of 1 × 10 − 6 1\times 10^{-6} . Each prompt generates G = 8 G=8 responses (temperature 1.0, max length 16,384) with batch size 128. Training runs on a 32-GPU H100 cluster.

#### Evaluation.

We report accuracy on MATH500 [ 7 ] and average@32 on AIME 2024/2025 [ 22 , 23 ] and HMMT [ 1 ] . All methods are evaluated on Qwen3 base models of varying scales and architectures: dense (1.7B, 4B, 14B) and MoE (30B-A3B), under identical initialization and hyperparameters.

### 4.2 Overall Performance Comparison

#### Comprehensive Benchmark Results.

Table 1 presents the performance of ESPO and baseline methods across four mathematical reasoning benchmarks and multiple model scales. ESPO achieves the highest average performance in all settings, demonstrating its consistent superiority.

On the smallest dense model (Qwen3-1.7B), ESPO matches or exceeds the best token-level baselines on AIME24 and MATH500 while providing a noticeable 3.1-point improvement on AIME25. This indicates that ESPO’s fine-grained yet stable optimization is particularly beneficial when model capacity is limited.

With medium-scale dense models (Qwen3-4B and 14B), ESPO maintains a narrow but consistent lead over strong token-level competitors like CISPO. While the absolute margins decrease as models become more capable, ESPO still attains the best average scores, suggesting it offers a robust trade-off between granularity and stability.

The advantage becomes most pronounced on the large MoE model (Qwen3-30B-A3B). Here, ESPO outperforms both sequence-level and token-level baselines by substantial margins—achieving up to 12.1-point gains over GSPO on AIME24 and 1.4-point gains over CISPO on AIME25. This highlights ESPO’s effectiveness in heterogeneous architectures where fixed-granularity methods struggle to adapt.

Across all model sizes and architectures, ESPO delivers balanced improvements without task-specific tuning, confirming its value as a general-purpose optimization strategy.

#### Training Dynamics.

Figure 3 compares the training behavior of ESPO with representative sequence-level (GSPO) and token-level (CISPO) methods on Qwen3-30B-A3B. Three key observations emerge:

First, ESPO converges at a comparable or faster rate than baselines in terms of training accuracy (Fig. 3 a), indicating more efficient optimization. Second, while baseline methods stabilize or only slowly increase their response lengths, ESPO sustains a steady growth in generated sequence length throughout training (Fig. 3 b), demonstrating continued exploration of longer reasoning trajectories. Third, ESPO demonstrates more stable entropy reduction than CISPO while starting from a more moderate initial value than both CISPO and GSPO (Fig. 3 c). Its smooth descent leads to a final policy that is marginally more confident than GSPO’s, indicating effective exploration without excessive randomness.

Collectively, these dynamics suggest that ESPO optimizes more efficiently (faster accuracy rise), explores more thoroughly (longer trajectories), and refines its policy more stably (smooth entropy decay) than fixed-granularity baselines.

### 4.3 Analysis of ESPO’s Mechanisms

#### Addressing Gradient Underutilization.

The performance advantages of ESPO stem from its ability to overcome the core limitations of fixed-granularity optimization. Figure 4 compares the clipping fractions for both upper and lower bounds across methods, providing insights into their update efficiency and stability.

Sequence-level methods exhibit the highest clipping fractions, indicating that a large portion of samples are truncated during updates. This occurs because a single sequence-level importance ratio is shared across all tokens; once this ratio exceeds the clipping threshold, the entire trajectory is discarded. Consequently, many informative gradients are suppressed, leading to the gradient underutilization problem highlighted in our introduction.

Token-level methods alleviate excessive truncation by using wider clipping ranges and finer-grained importance ratios. However, this relaxed constraint permits updates with highly variable token-wise ratios to pass through, introducing substantial noise into gradient estimates. Such instability is particularly problematic when importance ratios vary sharply across tokens, undermining training robustness.

ESPO maintains low clipping fractions without resorting to overly permissive ranges. By grouping tokens based on entropy and applying group-aware clipping, ESPO selectively constrains high-variance updates while preserving informative gradients. This approach enables more efficient use of training samples, avoiding both the wastefulness of sequence-level methods and the instability of token-level alternatives.

#### Validating Adaptive Optimization.

ESPO achieves this balanced behavior through its entropy-adaptive clipping mechanism. Figure 5 validates that this mechanism operates as designed, dynamically aligning optimization strength with model uncertainty.

During early training stages, the policy exhibits high predictive entropy (orange dashed line), reflecting broad uncertainty about token predictions. In this phase, ESPO assigns wider clipping ranges (lower clipping fractions), allowing greater exploration and policy deviation. As learning progresses, entropy steadily decreases as the model gains confidence, and ESPO automatically tightens its clipping constraints—indicated by the rising clipping fractions (blue and green lines). This adaptive behavior ensures that more samples fall within the trusted region once the policy stabilizes.

The inverse relationship between entropy and clipping fraction confirms that ESPO successfully modulates exploration intensity according to the model’s own uncertainty: high entropy encourages learning diversity, while low entropy enforces conservative updates. This principled adaptation explains how ESPO maintains stable optimization throughout training while still exploring effectively.

### 4.4 Ablation Studies

Having established that ESPO’s adaptive mechanism effectively addresses the limitations of fixed-granularity methods, we now validate the necessity of its individual design choices through ablation experiments. All ablations use the Qwen3-30B-A3B model under identical training configurations.

#### Core Components.

We first examine the contribution of ESPO’s two key innovations: adaptive clipping and entropy grouping importance sampling. Table 2 shows that removing either component significantly degrades performance.

Removing adaptive clipping —by replacing it with fixed clipping schemes—consistently harms results. We test two variants: (1) aggressive sequence-level clipping (0.0003, 0.0004) and (2) conservative token-level clipping (0.2, 0.28). Both cause comparable performance drops despite their different granularities, confirming that static clipping cannot adapt to evolving training dynamics and that ESPO’s adaptive mechanism is essential.

Removing entropy grouping causes the most severe degradation across all benchmarks. Without structured grouping based on entropy, clipping operates in an uncoordinated token-wise manner, significantly increasing gradient variance. This demonstrates that merely adjusting clipping ranges is insufficient; aligning clipping behavior with the model’s entropy structure is crucial for stable optimization.

The substantial performance gap between the full ESPO and these ablated versions validates that both components are necessary and work synergistically.

#### Grouping Proportion.

Given the importance of token grouping, we analyze the optimal proportion of high-entropy tokens to include. Figure 6 reveals a clear trade-off.

Selecting too few tokens (e.g., 10%) leads to weaker exploration. As observed in prior work [ 16 ] , overly aggressive filtering can remove certain useful tokens that still correspond to meaningful decision points, resulting in faster entropy decay and reduced diversity early in training. Consequently, the model may converge prematurely before sufficiently exploring the reasoning space.

Conversely, selecting too many tokens (e.g., 40%) introduces a substantial number of low-entropy tokens. These tokens are often highly certain and knowledge-driven, and contribute limited information for improving reasoning behavior. Including them in large proportions dilutes the influence of informative gradients and reduces exploration efficiency.

Across experiments, selecting approximately 20% of the highest-entropy tokens provides the optimal balance. This intermediate choice preserves enough informative decision points to sustain exploration while avoiding excessive inclusion of low-entropy tokens that can hinder optimization, validating our grouping strategy.

#### Hyperparameter Sensitivity.

Finally, we examine the sensitivity of ESPO to α \alpha , the global scaling factor controlling update strength (Table 3 ). Performance peaks at α = 0.02 \alpha=0.02 , with both smaller and larger values yielding suboptimal results.

When α \alpha is too small (0.01), clipping becomes overly aggressive, limiting exploration. When α \alpha is too large (0.05, 0.10), clipping becomes too permissive, reducing stability. This narrow optimal range underscores the importance of balanced exploration and confirms that our chosen α = 0.02 \alpha=0.02 represents an effective default setting.

## 5 Conclusion

We introduce Entropy Importance Sampling Policy Optimization (ESPO), an entropy-aware RL framework that groups tokens by uncertainty and clips adaptively. On challenging mathematical benchmarks, ESPO exhibits accelerated convergence, reduced clipping, and superior sample-efficiency versus strong baselines under equal compute. Future directions include alternative grouping criteria, learnable grouping mechanisms, and extensions to multi-turn dialogue and program synthesis.

## Ethical Statement

All experiments were conducted in accordance with the applicable institutional and national guidelines on research involving (open-source/public) data. The dataset(s) used in this study are publicly available and were originally released under permissive licenses that allow academic reuse. Our models follow standard practices for large-scale language model training; they may still produce biased, offensive, or factually incorrect outputs.

## References

[1] M. Balunović, J. Dekoninck, I. Petrov, N. Jovanović, and M. Vechev (2025) MathArena: evaluating llms on uncontaminated math competitions . SRI Lab, ETH Zurich . External Links: Link Cited by: §4.1 .

[2] A. Chen, A. Li, B. Gong, B. Jiang, B. Fei, B. Yang, B. Shan, C. Yu, C. Wang, C. Zhu, et al. (2025) MiniMax-m1: scaling test-time compute efficiently with lightning attention . arXiv preprint arXiv:2506.13585 . Cited by: §1 , §2.1 .

[3] Y. Guo, L. Xu, J. Liu, D. Ye, and S. Qiu (2025) Segment policy optimization: effective segment-level credit assignment in rl for large language models . arXiv preprint arXiv:2505.23564 . Cited by: §2.1 .

[4] J. Hu, Y. Zhang, Q. Han, D. Jiang, X. Zhang, and H. Shum (2025) Open-reasoner-zero: an open source approach to scaling up reinforcement learning on the base model . arXiv preprint arXiv:2503.24290 . Cited by: §2.1 .

[5] A. Kazemnejad, M. Aghajohari, E. Portelance, A. Sordoni, S. Reddy, A. Courville, and N. L. Roux (2025) VinePPO: refining credit assignment in rl training of llms . External Links: 2410.01679 , Link Cited by: §3.4 .

[6] W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. E. Gonzalez, H. Zhang, and I. Stoica (2023) Efficient memory management for large language model serving with pagedattention . In Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles , Cited by: §4.1 .

[7] H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe (2023) Let’s verify step by step . arXiv preprint arXiv:2305.20050 . Cited by: §4.1 .

[8] J. Liu, G. Liu, J. Liang, Y. Li, J. Liu, X. Wang, P. Wan, D. Zhang, and W. Ouyang (2025) Flow-grpo: training flow matching models via online rl . External Links: 2505.05470 , Link Cited by: §3.4 .

[9] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov (2017) Proximal policy optimization algorithms . arXiv preprint arXiv:1707.06347 . Cited by: §1 , §2.1 .

[10] C. E. Shannon (1948) A mathematical theory of communication . The Bell system technical journal 27 ( 3 ), pp. 379–423 . Cited by: §1 .

[11] Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. K. Li, Y. Wu, and D. Guo (2024) DeepSeekMath: pushing the limits of mathematical reasoning in open language models . External Links: 2402.03300 , Link Cited by: §2.1 , §2.2 .

[12] Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. (2024) Deepseekmath: pushing the limits of mathematical reasoning in open language models . arXiv preprint arXiv:2402.03300 . Cited by: §1 .

[13] G. Sheng, C. Zhang, Z. Ye, X. Wu, W. Zhang, R. Zhang, Y. Peng, H. Lin, and C. Wu (2024) HybridFlow: a flexible and efficient rlhf framework . arXiv preprint arXiv: 2409.19256 . Cited by: §4.1 .

[14] H. Tan, J. Pan, J. Lin, T. Chen, Z. Zheng, Z. Tang, and H. Yang (2025) Gtpo and grpo-s: token and sequence-level reward shaping with policy entropy . arXiv preprint arXiv:2508.04349 . Cited by: §2.1 .

[15] J. Wang, R. Liu, F. Zhang, X. Li, and G. Zhou (2025) Stabilizing knowledge, promoting reasoning: dual-token constraints for rlvr . arXiv preprint arXiv:2507.15778 . Cited by: §1 .

[16] S. Wang, L. Yu, C. Gao, C. Zheng, S. Liu, R. Lu, K. Dang, X. Chen, J. Yang, Z. Zhang, et al. (2025) Beyond the 80/20 rule: high-entropy minority tokens drive effective reinforcement learning for llm reasoning . arXiv preprint arXiv:2506.01939 . Cited by: §1 , §4.4 .

[17] C. Xiao, M. Zhang, and Y. Cao (2025) BNPO: beta normalization policy optimization . arXiv preprint arXiv:2506.02864 . Cited by: §2.1 .

[18] S. Yang, C. Dou, P. Guo, K. Lu, Q. Ju, F. Deng, and R. Xin (2025) Dcpo: dynamic clipping policy optimization . arXiv preprint arXiv:2509.02333 . Cited by: §2.1 .

[19] Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, W. Dai, T. Fan, G. Liu, L. Liu, et al. (2025) Dapo: an open-source llm reinforcement learning system at scale . arXiv preprint arXiv:2503.14476 . Cited by: §1 , §2.1 .

[20] W. Zeng, Y. Huang, Q. Liu, W. Liu, K. He, Z. Ma, and J. He (2025) Simplerl-zoo: investigating and taming zero reinforcement learning for open base models in the wild . arXiv preprint arXiv:2503.18892 . Cited by: §4.1 .

[21] Q. Zhang, H. Wu, C. Zhang, P. Zhao, and Y. Bian (2025) Right question is already half the answer: fully unsupervised llm reasoning incentivization . arXiv preprint arXiv:2504.05812 . Cited by: §2.1 .

[22] Y. Zhang and T. Math-AI (2024) American invitational mathematics examination (aime) 2024 . Cited by: §4.1 .

[23] Y. Zhang and T. Math-AI (2025) American invitational mathematics examination (aime) 2025 . Cited by: §4.1 .

[24] Y. Zhao, Y. Liu, J. Liu, J. Chen, X. Wu, Y. Hao, T. Lv, S. Huang, L. Cui, Q. Ye, et al. (2025) Geometric-mean policy optimization . arXiv preprint arXiv:2507.20673 . Cited by: §1 , §2.1 , §2.2 .

[25] C. Zheng, S. Liu, M. Li, X. Chen, B. Yu, C. Gao, K. Dang, Y. Liu, R. Men, A. Yang, et al. (2025) Group sequence policy optimization . arXiv preprint arXiv:2507.18071 . Cited by: §1 , §2.1 , §2.2 , §2.2 .

[26] Y. Zuo, K. Zhang, L. Sheng, S. Qu, G. Cui, X. Zhu, H. Li, Y. Zhang, X. Long, E. Hua, B. Qi, Y. Sun, Z. Ma, L. Yuan, N. Ding, and B. Zhou (2025) TTRL: test-time reinforcement learning . External Links: 2504.16084 , Link Cited by: §3.4 .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
