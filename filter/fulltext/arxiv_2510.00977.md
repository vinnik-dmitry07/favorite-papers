##### Report GitHub Issue

Content selection saved. Describe the issue below:

# It Takes Two: Your GRPO Is Secretly DPO

###### Abstract

GRPO has emerged as a prominent reinforcement learning algorithm for post-training LLMs. Unlike critic-based methods, GRPO computes advantages by estimating the value baselines from group-level statistics, eliminating the need for a critic network. Consequently, the prevailing view emphasizes the necessity of large group sizes, which are assumed to yield more accurate statistical estimates. In this paper, we propose a different view that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. This perspective motivates 2-GRPO, a minimal group-size variant that constructs contrastive signals with only two rollouts. We provide a rigorous theoretical analysis of 2-GRPO and empirically validate its effectiveness: 2-GRPO retains 97.6 % 97.6\% of the performance of 16-GRPO, while requiring only 12.5 % 12.5\% of the rollouts and 21 % 21\% of the training time.

## 1 Introduction

Reinforcement Learning (RL) has emerged as a central paradigm for the post-training of Large Language Models (LLMs). Two critical functions are aligning model outputs with human intent via RL with Human Feedback (RLHF) Ouyang et al. (2022) and enhancing reasoning capabilities through RL with Verifiable Rewards (RLVR) DeepSeek-AI (2025) . Among recent advances, Group Relative Policy Optimization (GRPO) Shao et al. (2024) is a prominent critic-free variant of Proximal Policy Optimization (PPO) Schulman et al. (2017) , which effectively reduces the variance of gradient estimates by subtracting the estimated value baseline. Diverging from PPO, which relies on an auxiliary critic network for estimating the value baselines, GRPO estimates the advantage function by sampling a group of responses (rollouts) for a single prompt and normalizing their rewards based on the group statistics (mean/standard deviation). This design eliminates the memory and computational overhead of the value network while maintaining strong performance across various reasoning tasks.

Conventional intuition suggests that GRPO’s efficacy is strongly correlated with its group size, grounded in the premise that larger sample sizes yield more accurate advantage estimates and lead to stronger post-trained LLMs. However, this intuition overlooks the specific construction of the group-relative gradient estimator in GRPO. First, we demonstrate that GRPO intrinsically functions as contrastive learning Chopra et al. (2005) and the contrastive objective effectively reduces the variance of the gradient estimates as a control variate method Johnson and Zhang (2013) . The group of rollouts serves primarily to pair contrastive samples, rather than to estimate the value baselines. Specifically, the GRPO objective is de facto a Monte Carlo estimator to approximate the true contrastive gradients. Thus, the choices of group size primarily affects the variance of the Monte Carlo estimator, while the approximation itself remains unbiased. Therefore, in contrast to the prevailing value-baseline estimation viewpoint, GRPO with a small group size shall still work properly. Second, this perspective further reveals its close connection to the well-known Direct Preference Optimization (DPO) algorithm Rafailov et al. (2023) , which explicitly introduces the contrastive objective in the offline RLHF setting. The GRPO is de facto doing direct preference optimization on online RL settings with the necessary adaptations.

To evidence this hypothesis, we propose the minimal two-rollout setting (2-GRPO), a configuration previously regarded as inadequate for estimating group statistics Student (1908) , but well aligned with the contrastive learning interpretation and the DPO objectives. We provide a thorough theoretical analysis of the properties of 2-GRPO and empirically evaluate its effectiveness and efficiency across a diverse set of models and tasks. The theoretical analysis justifies the rationale behind the 2-GRPO designs. Empirically, 2-GRPO achieves performance comparable to 16-GRPO while substantially reducing training time. We further propose a resampling variant, 2-GRPO+RS, which reduces sample discard rate and achieves performance closer to 16-GRPO while being more efficient than 16-GRPO. These findings support our central hypothesis: GRPO derives its strength primarily from its contrastive formulation, rather than from accurate advantage estimation. The efficiency of 2-GRPO further highlights the promise of the contrastive policy optimization direction.

## 2 Preliminary

### 2.1 Problem Setting and Notation

Our work focuses on RL-based post-training of LLMs for reasoning capabilities. Given an input prompt q ∈ 𝒬 q\in\mathcal{Q} , the model generates the i i -th response o i = ( o i , 1 , … , o i , T ) o_{i}=(o_{i,1},\ldots,o_{i,T}) , where o i , t o_{i,t} is the token generated at step t ∈ [ 0 , T ] t\in[0,T] and o i , < t o_{i,<t} denotes the sequence of preceding tokens. A trajectory τ = ( q , o ) ∈ 𝒯 \tau=(q,o)\in\mathcal{T} is defined as a concatenation of a prompt and its corresponding generated response. In current RL post-training, the reward function r : 𝒯 → ℝ r:\mathcal{T}\rightarrow\mathbb{R} is typically defined at the trajectory level. The learning objective is to maximize the expected reward over the trajectory space: 𝒥 ( θ ) = 𝔼 q ∼ 𝒬 𝔼 o ∼ π θ ( ⋅ | q ) [ r ( τ ) ] , \mathcal{J}(\theta)={\mathbb{E}}_{q\sim\mathcal{Q}}{\mathbb{E}}_{o\sim\pi_{\theta}(\cdot|q)}[r(\tau)]\,, (1) where π θ \pi_{\theta} denotes the policy model, a LLM with parameters θ \theta ; and 𝒬 \mathcal{Q} is the set of prompts, each consisting of a question and necessary instructions. We mainly focus on the setting of verifiable rewards, where the responses can be verified as correct ( r = 1 r=1 ) or incorrect ( r = 0 r=0 ).

### 2.2 The Story of Variance Reduction: VPG, PPO, and GRPO

As a foundational policy gradient method, Vanilla Policy Gradient (VPG) Williams (1992) optimizes the objective function using the following gradient estimator (where r i r_{i} is the reward of ( q , o i ) (q,o_{i}) ): ∇ θ 𝒥 ​ ( θ ) = 𝔼 q ∼ 𝒬 o i ∼ π θ ​ [ r i ​ ∑ t = 0 | o i | ∇ θ ​ log ​ π θ ​ ( o i , t | o i , < t , q ) ] . \nabla_{\theta}\mathcal{J}(\theta)=\underset{\begin{subarray}{c}q\sim\mathcal{Q}\\ o_{i}\sim\pi_{\theta}\end{subarray}}{{\mathbb{E}}}\left[r_{i}\sum_{t=0}^{|o_{i}|}\nabla_{\theta}\log\pi_{\theta}(o_{i,t}|o_{i,<t},q)\right]\;. (2)

Although effective, VPG usually suffers from high variance of gradient estimates and training instability. Therefore, subsequent works Schulman et al. (2015) ; Schulman et al. (2017) utilize advantage estimates Baird (1993) to reduce the variance of the policy gradient estimator: A i , t = r i − b ⁡ ( q ) A_{i,t}=r_{i}-b(q) , where A i , t A_{i,t} is token-level advantage and b ⁡ ( q ) b(q) is the value baseline function (See Appx. B.1 for more details). An auxiliary LLM is employed as a critic to estimate this value baseline, such as in Proximal Policy Optimization (PPO) ( Schulman et al., 2017 ) : 𝒥 ⁡ ( θ ) = 𝔼 q ∼ 𝒬 o i ∼ π θ old ​ 1 | o i | ​ ∑ t = 1 | o i | min ⁡ { A i , t ​ ρ i , t , A i , t ​ 𝒞 ϵ ​ ( ρ i , t ) } , ρ i , t = π θ ​ ( o i , t ∣ o i , < t , q ) π θ old ​ ( o i , t ∣ o i , < t , q ) , \mathcal{J}(\theta)=\underset{\begin{subarray}{c}q\sim\mathcal{Q}\\ o_{i}\sim\pi_{\theta_{\text{old}}}\end{subarray}}{\mathbb{E}}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\min\left\{A_{i,t}\rho_{i,t},A_{i,t}\mathcal{C}_{\epsilon}(\rho_{i,t})\right\}\,,\,\rho_{i,t}=\frac{\pi_{\theta}\!\left(o_{i,t}\mid o_{i,<t},q\right)}{\pi_{\theta_{\text{old}}}\!\left(o_{i,t}\mid o_{i,<t},q\right)}\,, (3) where π θ old \pi_{\theta_{\text{old}}} is the policy used to generate trajectories, while π θ \pi_{\theta} denotes the current policy being optimized. The ρ i , t \rho_{i,t} term is the introduced importance sampling technique for online (near-)on-policy RL while 𝒞 ϵ ​ ( x ) \mathcal{C}_{\epsilon}(x) denotes the clipping function within the interval [ 1 − ϵ , 1 + ϵ ] [1-\epsilon,1+\epsilon] .

To eliminate the substantial computational overhead and memory demands of the critic network, several studies Li et al. (2024) ; Ahmadian et al. (2024) ; Shao et al. (2024) propose estimating the baseline without a critic network. Specifically, GRPO estimates the advantage using the reward statistics from a group of generated responses: A i , t = r i − mean ​ ( 𝐫 ) std ​ ( 𝐫 ) + ϵ , A_{i,t}=\frac{r_{i}-\text{mean}(\mathbf{r})}{\text{std}(\mathbf{r})+\epsilon}\,, (4) where r i r_{i} is the reward for response o i o_{i} given query q q , and 𝐫 \mathbf{r} denotes the vector of rewards for G G sampled responses associated with q q . Therefore, it is generally believed that GRPO requires a sufficiently large group size to obtain accurate group-level statistics for advantage estimation. 1 1 1 Due to limited space, the comprehensive related work is provided in Appx. A .

## 3 A Tale of Two Algorithms: GRPO and DPO

At first glance, the objectives of GRPO and DPO appear distinct on different RL settings. We show that they are the twin objects of the contrastive RL objective under the online/offline RL setting, which can be seen from the gradient forms of GRPO and DPO. This finding provides a new theoretical analysis (Sec. 4 ) and motivates a more efficient yet effective algorithm (Sec. 4.2 ).

### 3.1 Contrastive Objective for Sequences

Contrastive Learning Chopra et al. (2005) has been a powerful learning paradigm in (self-)supervised learning, ranging from 1 1 -vs- 1 1 (one positive and one negative) objectives Rendle et al. (2009) to 1 1 -vs- N N Oord et al. (2018) and N N -vs- M M variants Frosst et al. (2019) . We first formalize the contrastive loss objective for sequences for further analysis.

###### Definition 3.1 (Contrastive Loss for Sequences) .

Let π θ \pi_{\theta} be a probabilistic model and 𝒟 \mathcal{D} be a data distribution. Consider an anchor sequence 𝐱 ∼ 𝒟 \mathbf{x}\sim\mathcal{D} , and let 𝒟 + ( ⋅ ∣ 𝐱 ) \mathcal{D}^{+}(\cdot\mid\mathbf{x}) and 𝒟 − ( ⋅ ∣ 𝐱 ) \mathcal{D}^{-}(\cdot\mid\mathbf{x}) denote the conditional distributions for positive and negative samples, respectively. Let y t y_{t} denote the t t -th token of sequence 𝒚 {\bm{y}} . A differentiable loss function ℒ \mathcal{L} is contrastive if its gradient holds the following form: ∇ θ ℒ \displaystyle\nabla_{\theta}\mathcal{L} = − 𝔼 𝒙 ∼ 𝒟 [ 𝔼 𝒚 + ∼ 𝒟 + ∑ t = 1 | 𝒚 + | c t + ∇ θ π θ ( 𝒚 + t | 𝒚 + < t , 𝒙 ) − 𝔼 𝒚 − ∼ 𝒟 − ∑ t = 1 | 𝒚 − | c t − ∇ θ π θ ( 𝒚 − t | 𝒚 − < t , 𝒙 ) ] , \displaystyle=-\underset{{\bm{x}}\sim\mathcal{D}}{{\mathbb{E}}}\Bigg[\underset{{\bm{y}}^{+}\sim\mathcal{D}^{+}}{{\mathbb{E}}}\sum_{t=1}^{|{\bm{y}}^{+}|}c_{t}^{+}\nabla_{\theta}\pi_{\theta}({\bm{y}}^{+}_{t}|{\bm{y}}^{+}_{<t},{\bm{x}})\quad-\underset{{\bm{y}}^{-}\sim\mathcal{D}^{-}}{{\mathbb{E}}}\sum_{t=1}^{|{\bm{y}}^{-}|}c_{t}^{-}\nabla_{\theta}\pi_{\theta}\left({\bm{y}}^{-}_{t}|{\bm{y}}^{-}_{<t},{\bm{x}}\right)\Bigg]\,, (5) where c t + c_{t}^{+} and c t − c_{t}^{-} are token-level coefficients depending on specific algorithm design.

We adopt token-level coefficients for generality, as sequence-level coefficients can be recovered as a special case. Furthermore, the number of positive ( N N ) and negative ( M M ) samples of each data point may vary depending on the specific designs, serving as a Monte Carlo estimator to approximate the true gradient in Eq. ( 5 ).

#### DPO is a 1-vs-1 contrastive learning

Direct Preference Optimization (DPO) Rafailov et al. (2023) is a dominant offline RLHF algorithms for LLMs: ℒ DPO = − 𝔼 ( q , o + , o − ) ∼ 𝒟 DPO ​ [ log ⁡ σ ⁡ ( β ​ log ⁡ π θ ​ ( o + | q ) π ref ​ ( o + | q ) − β ​ log ⁡ π θ ​ ( o − | q ) π ref ​ ( o − | q ) ) ] , \mathcal{L}_{\text{DPO}}=\underset{(q,o^{+},o^{-})\sim\mathcal{D}_{\text{DPO}}}{-\mathbb{E}}\left[\log\sigma\left(\beta\log\frac{\pi_{\theta}(o^{+}|q)}{\pi_{\text{ref}}(o^{+}|q)}-\beta\log\frac{\pi_{\theta}(o^{-}|q)}{\pi_{\text{ref}}(o^{-}|q)}\right)\right]\;, (6) where the preference pair ( q , o + , o − ) ∼ 𝒟 DPO (q,o^{+},o^{-})\sim\mathcal{D}_{\text{DPO}} are from precollected human-annotated data. σ \sigma denotes the sigmoid function. It is easy to show that DPO is a 1-vs-1 contrastive learning. We provide Lemma B.1 and its proof in Appx. B.5 for reference.

### 3.2 GRPO: N-vs-M Contrastive Learning

We demonstrate that GRPO effectively functions as a dynamic N N -vs- M M contrastive learning, where the group size G = N + M G=N+M is fixed, but the specific values of N N (positive samples) and M M (negative samples) are dynamic based on the sampled responses. Let G q + G^{+}_{q} and G q − G^{-}_{q} denote the counts of correct and incorrect trajectories, respectively. The GRPO objective function can be formulated as: 𝒥 GRPO ( θ , G ) = 𝔼 [ q ∼ 𝒬 ; { o j + , o k − } j , k G ∼ π θ old ( ⋅ | q ) ] \displaystyle\mathcal{J}_{\text{GRPO}}(\theta,G)={{\mathbb{E}}}_{\left[q\sim\mathcal{Q};\{o_{j}^{+},o_{k}^{-}\}_{j,k}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|q)\right]} (7) Var ^ G ​ ( q ) ​ [ 1 G q + ​ ∑ j = 1 G q + 1 | o j + | ​ ∑ t = 1 | o j + | 𝒞 ϵ + ​ ( ρ j , t ) ⏟ positive − 1 G q − ​ ∑ k = 1 G q − 1 | o k − | ​ ∑ t = 1 | o k − | 𝒞 ϵ − ​ ( ρ k , t ) ⏟ negative ] , \displaystyle{\displaystyle\sqrt{\widehat{\mathrm{Var}}_{G}(q)}}\Bigg[\underbrace{\frac{1}{G_{q}^{+}}\sum_{j=1}^{G_{q}^{+}}\frac{1}{|o_{j}^{+}|}\sum_{t=1}^{|o_{j}^{+}|}\mathcal{C}_{\epsilon}^{+}\left(\rho_{j,t}\right)}_{\text{positive}}-\underbrace{\frac{1}{G_{q}^{-}}\sum_{k=1}^{G_{q}^{-}}\frac{1}{|o_{k}^{-}|}\sum_{t=1}^{|o_{k}^{-}|}\mathcal{C}_{\epsilon}^{-}\left(\rho_{k,t}\right)}_{\text{negative}}\Bigg]\,, where o j + o_{j}^{+} and o k − o_{k}^{-} denote rollouts with correct and incorrect outcomes, respectively. Denoting p ^ θ old , q = G q + / G \hat{p}_{\theta_{\text{old}},q}=G^{+}_{q}/G , the term Var ^ G ​ ( q ) = ( 1 − p ^ θ old , q ) ​ p ^ θ old , q \widehat{\mathrm{Var}}_{G}(q)=(1-\hat{p}_{\theta_{\text{old}},q})\hat{p}_{\theta_{\text{old}},q} is the empirical variance of the G G sampled trajectories from the true Bernoulli ​ ( p old , q ) \text{Bernoulli}(p_{\text{old},q}) under the RLVR setting. 2 2 2 In subsequent parts, we omit the subscript θ old \theta_{\text{old}} of p p for brevity. For simplicity, we denote the upper and lower clippings as 𝒞 ϵ + ​ ( x ) = min ⁡ [ x , 1 + ϵ ] \mathcal{C}_{\epsilon}^{+}(x)=\min[x,1+\epsilon] and 𝒞 ϵ − ​ ( x ) = max ⁡ [ x , 1 − ϵ ] \mathcal{C}_{\epsilon}^{-}(x)=\max[x,1-\epsilon] , respectively.

The formulation in Eq. ( 7 ) provides the foundation for the following proposition, with a proof provided in Appx. B.3 . Despite the sophisticated algorithm design of GRPO, this proposition unveils its contrastive nature.

###### Proposition 3.2 .

The maximization of the GRPO objective is equivalent to the minimization of an N N -vs- M M contrastive loss estimator.

The derivation of Proposition 3.2 is based on the binary reward assumption to align with the RLVR setting. However, GRPO’s contrastive nature extends to continuous rewards inherently (as shown in Figure 1 ). Due to the space limit, we focus on the properties of GRPO on RLVR.

### 3.3 Echoes of Contrastiveness: GRPO and DPO

Based on previous analysis, the differences between GRPO and DPO are merely in the coefficients of contrastive gradient: GRPO: c ⁡ ( o i , t ∣ o i , < t , q ) := 𝟙 i , t ϵ ​ Var ^ ​ ( q ) | o i | ​ π θ old ​ ( o i , t ∣ o i , < t , q ) , \displaystyle c(o_{i,t}\mid o_{i,<t},q):=\frac{{\color[rgb]{0.043,0.2383,0.5703}\mathbbm{1}^{\epsilon}_{i,t}}\,{\color[rgb]{0.1055,0.3672,0.125}\sqrt{\widehat{\mathrm{Var}}(q)}}}{{\color[rgb]{0.7188,0.1094,0.1094}|o_{i}|}\,{\color[rgb]{0.043,0.2383,0.5703}\pi_{\theta_{\text{old}}}(o_{i,t}\mid o_{i,<t},q)}}\,, (8) DPO: c ⁡ ( o t ∣ o < t , q ) := β ​ σ ​ ( r ^ θ ​ ( q , o − ) − r ^ θ ​ ( q , o + ) ) π θ ​ ( o ) , r ^ θ = β ​ log ⁡ π θ ​ ( y ∣ x ) π ref ​ ( y ∣ x ) . \displaystyle c(o_{t}\mid o_{<t},q):=\frac{\beta\,{\color[rgb]{0.1055,0.3672,0.125}\sigma(\hat{r}_{\theta}(q,o^{-})-\hat{r}_{\theta}(q,o^{+}))}}{{\color[rgb]{0.043,0.2383,0.5703}\pi_{\theta}(o)}}\,,\quad\hat{r}_{\theta}=\beta\log\frac{\pi_{\theta}(y\mid x)}{{\color[rgb]{0.2891,0.0781,0.5508}\pi_{\text{ref}}(y\mid x)}}\,. (9)

In the following, we show that the differences between GRPO and DPO are largely adaptations to their respective learning regimes: GRPO operates online with generated rollouts, whereas DPO operates offline with pre-collected preference data.

Group Size . DPO typically learns with fixed 1 1 -vs- 1 1 preference pairs which are collected offline in advance. By contrast, due to sampling responses online, GRPO needs to handle arbitrary N N -vs- M M positive–negative samples within each group. This changes only the Monte Carlo sample size used to estimate the same positive and negative contrastive gradients.

Token Aggregation . Within a sequence, GRPO averages token-level gradients, whereas DPO sums them. This is a design choice rather than a fundamental difference: e.g., SimPO Meng et al. (2024) – a DPO variant – uses mean aggregation, while Dr. GRPO Liu et al. (2025) – a GRPO variant – adopts sum aggregation.

Token-Level Weighting (Importance Sampling vs. Log-Likelihood). In GRPO, importance-sampling coefficients correct the gradient for samples generated by the old policy, specifically for its near-on-policy online RL setting. It is typically used together with clipping for training stability. DPO, however, does not require such correction in the offline setting and therefore directly uses the log-likelihood form of π θ \pi_{\theta} .

Group-Level Weighting . GRPO weights each group by Var ^ ​ ( q ) \sqrt{\widehat{\mathrm{Var}}(q)} , embodying its design philosophy of attending to more uncertain questions. DPO, in contrast, weights each pair by σ ⁡ ( r ^ θ ​ ( q , o − ) − r ^ θ ​ ( q , o + ) ) \sigma(\hat{r}_{\theta}(q,o^{-})-\hat{r}_{\theta}(q,o^{+})) , assigning higher scores to pairs where the negative sample outscores the positive one.

Reference Model . DPO is regularized toward the reference model π ref \pi_{\text{ref}} through an implicit KL term. Optionally, GRPO can add a separate explicit KL penalty term w.r.t. the reference model.

In conclusion, the differences between GRPO and DPO mainly reflect adaptations to online vs. offline RL settings. The core mechanisms remain the same: both estimate a contrastive gradient that increases the likelihood of preferred outputs relative to unpreferred ones.

## 4 Why Viewing GRPO From Contrastive Learning?

### 4.1 Variance Reduction via Contrastive Objective

We demonstrate that this contrastive gradient formulation functions as a control variate method, where the coefficients serve to control the variance of the estimator.

###### Proposition 4.1 .

Let π θ \pi_{\theta} denote the policy model. Let o + ∼ π θ + ( ⋅ | q ) o^{+}\sim\pi_{\theta}^{+}(\cdot|q) and o − ∼ π θ − ( ⋅ | q ) o^{-}\sim\pi_{\theta}^{-}(\cdot|q) denote random variables representing a positive sample and a negative sample, respectively. Let 𝐠 + = ∇ θ ​ log ​ π θ ​ ( o + | q ) \bm{g}^{+}=\nabla_{\theta}\log\pi_{\theta}(o^{+}|q) , 𝐠 − = ∇ θ ​ log ​ π θ ​ ( o − | q ) \bm{g}^{-}=\nabla_{\theta}\log\pi_{\theta}(o^{-}|q) and ρ \rho denote the correlation coefficient of 𝐠 + \bm{g}^{+} and 𝐠 − \bm{g}^{-} . If Cov ⁡ ( 𝐠 + , 𝐠 − ) > 0 \mathrm{Cov}(\bm{g}^{+},\bm{g}^{-})>0 and 0 ≤ c ≤ 2 ​ Cov ⁡ ( 𝐠 + , 𝐠 − ) Var ⁡ ( 𝐠 − ) 0\leq c\leq 2\frac{\mathrm{Cov}(\bm{g}^{+},\bm{g}^{-})}{\mathrm{Var}(\bm{g}^{-})} , then Var ⁡ ( 𝐠 + − c ​ 𝐠 − ) ≤ Var ⁡ ( 𝐠 + ) \mathrm{Var}(\bm{g}^{+}-c\bm{g}^{-})\leq\mathrm{Var}(\bm{g}^{+}) . Specifically, if c = Cov ⁡ ( 𝐠 + , 𝐠 − ) Var ⁡ ( 𝐠 − ) c=\frac{\mathrm{Cov}(\bm{g}^{+},\bm{g}^{-})}{\mathrm{Var}(\bm{g}^{-})} , then Var ⁡ ( 𝒈 + − c ​ 𝒈 − ) = ( 1 − ρ 2 ) ​ Var ​ ( 𝒈 + ) , \mathrm{Var}(\bm{g}^{+}-c\bm{g}^{-})=\left(1-\rho^{2}\right)\mathrm{Var}(\bm{g}^{+})\,, (10) where Var ​ ( ⋅ ) \text{Var}(\cdot) and Cov ​ ( ⋅ , ⋅ ) \text{Cov}(\cdot,\cdot) denotes the corresponding traces of var/cov matrices for gradient vectors.

This proposition (proof in Appx. B.7 ) shows that, when the coefficient c c lies within an appropriate range, the variance of the gradient estimator can be reduced. This result directly follows the control variate method, a variance reduction technique widely used in Monte Carlo estimation and stochastic gradient optimization Johnson and Zhang (2013) . The reduction of gradient variance stabilizes RL training Li et al. (2024) .

A key implication of Proposition 4.1 is that the degree of variance reduction depends on the correlation between positive and negative samples. In LLM post-training, the positive sample o + o^{+} and the negative sample o − o^{-} are generated by the same model conditioned on the same prompt q q , which typically induces a nontrivial correlation between them. (See Appx. B.8 for more discussion.)

### 4.2 GRPO with Small Group Size: It Should Fail, But Doesn’t

While both the value-baseline and contrastive perspectives account for GRPO’s variance reduction, they rest on fundamentally different assumptions. The prevailing value-baseline view holds that GRPO requires a sufficiently large group size to yield reliable group-level statistics; under this view, small-group GRPO should fail due to high-variance estimates Student (1908) . The contrastive perspective, by contrast, treats the positive and negative samples within a group as Monte Carlo estimates of the true positive and negative gradients. Because Monte Carlo estimation is unbiased regardless of sample size, GRPO with small groups should remain effective under stochastic optimization.

To adjudicate between these two views, we introduce 2-GRPO, a variant that uses the minimal group size of 2 2 . The value-baseline perspective predicts that this setting will fail (see Appx. B.2 for details). Empirically, however, 2-GRPO matches the performance of standard GRPO while achieving substantially higher efficiency, supporting the contrastive perspective as a more principled account of GRPO’s underlying mechanism. We describe 2-GRPO concretely in the following section.

### 4.3 Introducing 2-GRPO

With a group size of two, the GRPO advantage reduces to a simple contrastive signal: A + = + 1 A^{+}=+1 and A − = − 1 A^{-}=-1 when the two rollouts disagree on the reward, and both zeros otherwise. This yields an online RL counterpart of Direct Preference Optimization (DPO).

2-GRPO with Re-Sampling. Because of its binary contrastive nature, 2-GRPO discards any group whose two rollouts share the same reward. When the policy is highly accurate on the training set, this wastes a substantial fraction of generated samples and leads to sub-optimal performance. 3 3 3 A discussion on discard rate is provided in Appx. D.3 .

To address this, we introduce a resampling variant, denoted 2-GRPO+RS , which follows the strategy of DAPO Yu et al. (2025) : whenever a group is discarded due to a zero advantage, it is replaced with a fresh group sampled from a new prompt. Resampling adds rollout-stage computation, but the overhead is modest and consistently lifts peak performance.

Efficiency Gains. The efficiency gains of 2-GRPO arise at two stages: rollout generation and policy optimization. For a fixed number of prompts, 2-GRPO generates only 12.5 % 12.5\% of the rollouts required by 16-GRPO, and optimizes over the same 12.5 % 12.5\% fraction during policy updates. 2-GRPO+RS may generate additional rollouts through resampling, but its optimization-stage cost matches standard 2-GRPO. In our experiments, we cap the rollout budget of 2-GRPO+RS at that of 16-GRPO; in practice, it typically uses fewer.

## 5 Experiments

Goal of Experiment. Building on the theoretical justification for 2-GRPO, we seek to empirically assess its validity in RLVR. We anticipate that 2-GRPO will achieve a comparable performance as the regular GRPO (16-GRPO), and exhibit better efficiency —with respect to computational resources and/or wall-clock time.

Datasets, Baselines and Hyper-parameters. We provide the details of datasets, baselines and hyper-parameter choices in Appx. D.1 . For training, we adopt the verl framework Sheng et al. (2025) and utilize the built-in implementation of GRPO Shao et al. (2024) as the baseline algorithm.

### 5.1 Math Reasoning

Following prior studies Yu et al. (2025) , we consider mathematical tasks as representative instances of RLVR to verify our hypothesis. In the main experiment, the models are post-trained with RL techniques on MATH and DAPO-Math-Sub datasets under a fixed budget of 10 training epochs. The post-trained models are evaluated on five widely-used math reasoning benchmarks. This is an out-of-distribution evaluation setting, imposing requirements on the generalization ability of the post-trained models.

Table 1 showcases the Mean@32 as well as the training time. The empirical results show that 2-GRPO achieves 97.6% of 16-GRPO’s average performance while using only 12.5% of its total rollouts and 21.0% of its training time . 4 4 4 Appx. D.2 discusses the relationship between the total number of rollouts and computational cost.

These results provide strong corroboration of our theoretical finding that reducing group size preserves performance while substantially improving efficiency.

The resampling variant, 2-GRPO+RS, further improves peak performance, outperforming 16-GRPO on average while using roughly half of its training time . Although it is slower than 2-GRPO, it remains substantially more efficient than 16-GRPO, making it a practical alternative that preserves small-group efficiency while recovering the performance benefits of broader exploration.

Figure 2 shows the Pass@ K K over various K K choices. Overall, 2-GRPO achieves Pass@ K K performance comparable to 16-GRPO across different choices of K K . In particular, 2-GRPO even outperforms 16-GRPO on the AMC 2023 and Olympiad Bench. On AIME 2025, 2-GRPO performs better when post-trained on DAPO-Math-Sub, but worse when post-trained on MATH, likely due to the larger distribution shift between training dataset and the evaluation one.

We extend the evaluation of 2-GRPO to additional RLVR tasks beyond mathematical reasoning, including Vision Reasoning (Geometry3K) and Code Generation (Code-R1), with results reported in Figure 3 . The results demonstrate that 2-GRPO remains both effective and efficient across these diverse tasks, highlighting its broader applicability beyond math reasoning. As shown in the figure, 2-GRPO converges substantially faster than 16-GRPO, owing to the reduced number of samples generated and updated per step. This phenomenon is consistent with our theoretical findings, which identify the role of the group as providing contrastive sample pairs. Reducing the group size not only preserves performance but also accelerates the learning process.

### 5.2 Ablation Study: The Effect of Group Size

Our proposed 2-GRPO changes the group size while also adjusting the training batch size and the learning rate to account for the reduced number of rollouts per prompt (discussed in Appx. B.1 ). To isolate the effect of group size, we conduct an ablation study over different group sizes using the exact same configuration: 10 training epochs, a generation batch size of 512 prompts, a training batch size of 32 prompts, and a learning rate of 10 − 6 10^{-6} .

It is worth noting that this setting is slightly unfavorable to smaller group sizes – the actual training mini-batch size by # rollouts is # prompts per batch multiplied by the group size. Therefore, GRPO with smaller group sizes in the ablation study suffered from higher variance of gradient estimates (see C.2 for details). Nonetheless, Figure 4 shows that the Mean@ 32 32 differences among G = 2 , 4 , 8 , 16 G=2,4,8,16 are consistently small across all settings. Moreover, increasing the group size does not reliably improve Pass@ 32 32 : larger groups do not consistently outperform smaller ones, and in some cases smaller groups achieve better Pass@ 32 32 . The full results of the ablation study are provided in Table 4 in Appx. D.4 .

## 6 Conclusion

In this work, we demonstrate that GRPO de facto functions as contrastive learning. We argue that the primary role of the group mechanism is not for accurate value-baseline estimation, as commonly assumed, but for the efficient construction of contrastive signals. Based on this insight, we reveal the fundamental connection between GRPO and DPO—they are two echoes of the same contrastive gradient optimization principle, reflected through the online and offline RL settings, respectively. To further validate this insight, we introduce 2-GRPO, a minimal variant with only two rollouts per prompt. Although this setting is degenerate from the standpoint of traditional advantage estimation, it remains theoretically well motivated under our contrastive framework. Empirically, 2-GRPO achieves performance comparable to 16-GRPO while substantially reducing the computational overhead of rollout generation and policy optimization. These results support our hypothesis and suggest a more efficient design principle for RL algorithms for LLMs. More broadly, while our analysis focuses on GRPO, the insights developed here may extend to a wider class of group-based RL algorithms.

## References

Ahmadian et al. (2024) A. Ahmadian, C. Cremer, M. Gallé, M. Fadaee, J. Kreutzer, O. Pietquin, A. Üstün, and S. Hooker Back to basics: revisiting reinforce style optimization for learning from human feedback in llms . In Proc. Annu. Meet. Assoc. Comput. Linguist. , Cited by: §2.2 .

Bai et al. (2025) S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, et al. Qwen2. 5-vl technical report . arXiv preprint arXiv:2502.13923 . Cited by: §D.1 .

Baird (1993) I. Baird Advantage updating . Technical report Wright Laboratory . Cited by: §B.1 , §2.2 .

Chen et al. (2020) T. Chen, S. Kornblith, M. Norouzi, and G. Hinton A simple framework for contrastive learning of visual representations . In Proc. Int. Conf. Mach. Learn. , Cited by: §A.1 .

Chopra et al. (2005) S. Chopra, R. Hadsell, and Y. LeCun Learning a similarity metric discriminatively, with application to face verification . In Proc. IEEE Comput. Soc. Conf. Comput. Vis. Pattern Recognit. , Cited by: §1 , §3.1 .

Chu et al. (2025) X. Chu, H. Huang, X. Zhang, F. Wei, and Y. Wang Gpg: a simple and strong reinforcement learning baseline for model reasoning . arXiv preprint arXiv:2504.02546 . Cited by: §D.1 .

DeepSeek-AI (2025) DeepSeek-AI DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning . External Links: 2501.12948 Cited by: §D.1 , §1 .

Flet-Berliac et al. (2024) Y. Flet-Berliac, N. Grinsztajn, F. Strub, E. Choi, B. Wu, C. Cremer, A. Ahmadian, Y. Chandak, M. G. Azar, O. Pietquin, et al. Contrastive policy gradient: aligning llms on sequence-level scores in a supervised-friendly fashion . In Proc. Conf. Empir. Methods Nat. Lang. Process. , Cited by: §A.1 .

Frosst et al. (2019) N. Frosst, N. Papernot, and G. Hinton Analyzing and improving representations with the soft nearest neighbor loss . In Proc. Int. Conf. Mach. Learn. , Cited by: §3.1 .

Goyal et al. (2017) P. Goyal, P. Dollár, R. Girshick, P. Noordhuis, L. Wesolowski, A. Kyrola, A. Tulloch, Y. Jia, and K. He Accurate, large minibatch sgd: training imagenet in 1 hour . arXiv preprint arXiv:1706.02677 . Cited by: §D.1 .

He et al. (2024) C. He, R. Luo, Y. Bai, S. Hu, Z. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, J. Liu, L. Qi, Z. Liu, and M. Sun OlympiadBench: a challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems . In Proc. Annu. Meet. Assoc. Comput. Linguist. , Cited by: §D.1 .

He et al. (2020) K. He, H. Fan, Y. Wu, S. Xie, and R. Girshick Momentum contrast for unsupervised visual representation learning . In Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. , Cited by: §A.1 .

Hejna et al. (2023) J. Hejna, R. Rafailov, H. Sikchi, C. Finn, S. Niekum, W. B. Knox, and D. Sadigh Contrastive preference learning: learning from human feedback without rl . arXiv preprint arXiv:2310.13639 . Cited by: §A.1 .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt Measuring mathematical problem solving with the math dataset . In Adv. Neural Inf. Process. Syst. (Track Datasets Benchmarks) , Cited by: §D.1 .

Hu et al. (2022) M. Hu, M. Li, Y. Wang, and I. King Momentum contrastive pre-training for question answering . In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing , Y. Goldberg, Z. Kozareva, and Y. Zhang (Eds.) , Abu Dhabi, United Arab Emirates , pp. 4324–4330 . External Links: Link , Document Cited by: §A.1 .

Johnson and Zhang (2013) R. Johnson and T. Zhang Accelerating stochastic gradient descent using predictive variance reduction . In Adv. Neural Inf. Process. Syst. , Cited by: §1 , §4.1 .

Kingma (2014) D. P. Kingma Adam: a method for stochastic optimization . arXiv preprint arXiv:1412.6980 . Cited by: §D.1 .

Lewkowycz et al. (2022) A. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski, V. Ramasesh, A. Slone, C. Anil, I. Schlag, T. Gutman-Solo, et al. Solving quantitative reasoning problems with language models . In Adv. Neural Inf. Process. Syst. , Cited by: §D.1 .

Li et al. (2025) G. Li, M. Lin, T. Galanti, Z. Tu, and T. Yang DisCO: reinforcing large reasoning models with discriminative constrained optimization . arXiv preprint arXiv:2505.12366 . Cited by: §C.1 .

Li et al. (2024) Z. Li, T. Xu, Y. Zhang, Z. Lin, Y. Yu, R. Sun, and Z. Luo ReMax: a simple, effective, and efficient reinforcement learning method for aligning large language models . In Proc. Int. Conf. Mach. Learn. , Cited by: §2.2 , §4.1 .

Liu and Zhang (2025) J. Liu and L. Zhang Code-r1: reproducing r1 for code with reliable rewards . Note: https://github.com/ganler/code-r1 Cited by: §D.1 .

Liu et al. (2025) Z. Liu, C. Chen, W. Li, P. Qi, T. Pang, C. Du, W. S. Lee, and M. Lin Understanding r1-zero-like training: a critical perspective . arXiv preprint arXiv:2503.20783 . Cited by: §3.3 .

Lu et al. (2021) P. Lu, R. Gong, S. Jiang, L. Qiu, S. Huang, X. Liang, and S. Zhu Inter-gps: interpretable geometry problem solving with formal language and symbolic reasoning . In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) , pp. 6774–6786 . Cited by: §D.1 .

Lv et al. (2025) X. Lv, K. Chen, H. Sun, X. Bai, M. Zhang, and H. Liu The hidden link between rlhf and contrastive learning . arXiv preprint arXiv:2506.22578 . Cited by: §A.1 .

Meng et al. (2024) Y. Meng, M. Xia, and D. Chen Simpo: simple preference optimization with a reference-free reward . In Adv. Neural Inf. Process. Syst. , Cited by: §3.3 .

Oord et al. (2018) A. v. d. Oord, Y. Li, and O. Vinyals Representation learning with contrastive predictive coding . arXiv preprint arXiv:1807.03748 . Cited by: §3.1 .

Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback . In Adv. Neural Inf. Process. Syst. , Cited by: §1 .

Pang and Jin (2025) L. Pang and R. Jin On the theory and practice of grpo: a trajectory-corrected approach with fast convergence . arXiv preprint arXiv:2508.02833 . Cited by: §B.4 .

Rafailov et al. (2023) R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn Direct preference optimization: your language model is secretly a reward model . In Adv. Neural Inf. Process. Syst. , Cited by: §1 , §3.1 .

Rendle et al. (2009) S. Rendle, C. Freudenthaler, Z. Gantner, and L. Schmidt-Thieme BPR: bayesian personalized ranking from implicit feedback . In Proc. Conf. Uncertain. Artif. Intell. , Cited by: §3.1 .

Schulman et al. (2015) J. Schulman, S. Levine, P. Abbeel, M. Jordan, and P. Moritz Trust region policy optimization . In Proc. Int. Conf. Mach. Learn. , Cited by: §B.1 , §2.2 .

Schulman et al. (2016) J. Schulman, P. Moritz, S. Levine, M. Jordan, and P. Abbeel High-dimensional continuous control using generalized advantage estimation . In Proc. Int. Conf. Learn. Represent. , Cited by: §B.1 .

Schulman et al. (2017) J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov Proximal policy optimization algorithms . arXiv preprint arXiv:1707.06347 . Cited by: §B.1 , §B.4 , §1 , §2.2 .

Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. Deepseekmath: pushing the limits of mathematical reasoning in open language models . arXiv preprint arXiv:2402.03300 . Cited by: §1 , §2.2 , §5 .

Sheng et al. (2025) G. Sheng, C. Zhang, Z. Ye, X. Wu, W. Zhang, R. Zhang, Y. Peng, H. Lin, and C. Wu Hybridflow: a flexible and efficient rlhf framework . In Proc. Eur. Conf. Comput. Syst. , Cited by: §5 .

Student (1908) Student The probable error of a mean . Biometrika , pp. 1–25 . Cited by: §B.2 , §1 , §4.2 .

Wang and Isola (2020) T. Wang and P. Isola Understanding contrastive representation learning through alignment and uniformity on the hypersphere . In Proc. Int. Conf. Mach. Learn. , Cited by: §A.1 .

Williams (1992) R. J. Williams Simple statistical gradient-following algorithms for connectionist reinforcement learning . Machine learning 8 ( 3 ), pp. 229–256 . Cited by: §2.2 .

Wu et al. (2026) Y. Wu, L. Ma, M. Li, J. Zhou, L. Ding, J. Hao, H. Leung, I. King, Y. Zhang, and J. Nie Advancing multi-agent rag system with minimalist reinforcement learning . In Proc. Int. Conf. Auton. Agents Multi-Agent Syst. , Cited by: §A.2 .

Wu et al. (2024) Y. Wu, L. Zhang, F. Mo, T. Zhu, W. Ma, and J. Nie Unifying graph convolution and contrastive learning in collaborative filtering . In Proc. ACM SIGKDD Conf. Knowl. Discov. Data Min. , Cited by: §A.1 .

Yang et al. (2025) A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, H. Wei, H. Lin, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Lin, K. Dang, K. Lu, K. Bao, K. Yang, L. Yu, M. Li, M. Xue, P. Zhang, Q. Zhu, R. Men, R. Lin, T. Li, T. Tang, T. Xia, X. Ren, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Wan, Y. Liu, Z. Cui, Z. Zhang, and Z. Qiu Qwen2.5 Technical Report . Cited by: §D.1 .

Yu et al. (2025) Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, W. Dai, T. Fan, G. Liu, L. Liu, et al. Dapo: an open-source llm reinforcement learning system at scale . In Adv. Neural Inf. Process. Syst. , Cited by: §D.1 , §D.1 , §4.3 , §5.1 .

Zhang et al. (2025a) L. Zhang, B. Wang, X. Qiu, S. Reddy, and A. Agrawal REARANK: reasoning re-ranking agent via reinforcement learning . In Proc. 2025 Conf. Empir. Methods Nat. Lang. Process. , Cited by: §A.2 .

Zhang et al. (2025b) R. Zhang, D. Arora, S. Mei, and A. Zanette SPEED-rl: faster training of reasoning models via online curriculum learning . arXiv preprint arXiv:2506.09016 . Cited by: §A.2 .

Zhao et al. (2025) Y. Zhao, Y. Liu, J. Liu, J. Chen, X. Wu, Y. Hao, T. Lv, S. Huang, L. Cui, Q. Ye, et al. Geometric-mean policy optimization . arXiv preprint arXiv:2507.20673 . Cited by: §B.4 .

Zheng et al. (2025a) C. Zheng, S. Liu, M. Li, X. Chen, B. Yu, C. Gao, K. Dang, Y. Liu, R. Men, A. Yang, et al. Group sequence policy optimization . arXiv preprint arXiv:2507.18071 . Cited by: §B.4 .

Zheng et al. (2025b) H. Zheng, Y. Zhou, B. R. Bartoldson, B. Kailkhura, F. Lai, J. Zhao, and B. Chen Act only when it pays: efficient reinforcement learning for llm reasoning via selective rollouts . arXiv preprint arXiv:2506.02177 . Cited by: §A.2 .

Zheng et al. (2025c) Y. Zheng, J. Lu, S. Wang, Z. Feng, D. Kuang, and Y. Xiong EasyR1: an efficient, scalable, multi-modality rl training framework (github) . Cited by: §D.1 .

Zhu et al. (2025) L. Zhu, Y. Guan, D. Liang, J. Ju, Z. Luo, B. Qin, J. Luan, Y. Liu, and X. Bai Shuffle-r1: efficient rl framework for multimodal large language models via data-centric dynamic shuffle . arXiv preprint arXiv:2508.05612 . Cited by: §A.2 .

## Appendix

## Appendix A Related Work

### A.1 Contrastive Learning and LLM Alignment

Contrastive learning is the cornerstone of self-supervised representation learning [ 37 , 12 , 4 , 15 , 40 ] . The fundamental objective is to minimize the distance between anchor and positive samples in the representation space while maximizing the distance between the anchor and negative samples. Given this contrastive nature, the framework shares structural similarity with DPO, which conducts preference learning by increasing the likelihood of preferred completions relative to dispreferred ones. While recent literature explores the theoretical connections between RLHF and contrastive learning [ 13 , 8 , 24 ] , our work establishes a formal link between GRPO and DPO through a contrastive lens. This provides a unified analytical framework for understanding alignment. Specifically, we attribute the efficacy of GRPO to the construction of contrastive pairs, which serves as a control variate to reduce the variance of the gradient estimator. This analysis offers generalizable insights to broader alignment algorithms.

### A.2 Adaptive Rollouts in RLVR

RL post-training has demonstrated significant success in enhancing LLM performance across diverse domains [ 39 , 43 ] . Unlike SFT, RL requires the model to generate online samples during training. Although modern frameworks integrate high-throughput inference engines such as vLLM and SGLang, the autoregressive nature of LLMs ensures that the generation phase remains a primary computational bottleneck. This challenge is exacerbated by the common intuition that LLM-based RL often necessitates large group sizes to achieve good performance. To mitigate this overhead, recent studies have proposed selective or adaptive sampling techniques to reduce the number of rollouts without compromising performance [ 47 , 44 , 49 ] . Within this context, 2-GRPO serves as a robust baseline. Furthermore, our contrastive analysis of GRPO opens a new design space for developing efficient sampling algorithms in RLVR.

## Appendix B Theorems

### B.1 Variance Reduction of Policy Gradient Estimate

Given a prompt, consider the random variable (r.v.) of the reward r r (which can be replaced by the advantage a a ) and the r.v. of the policy gradient 𝒈 \bm{g} (corresponding to 1 | o i | ​ ∑ t = 0 | o i | ∇ θ ​ log ​ π θ ​ ( o i , t | o i , < t , q ) \frac{1}{|o_{i}|}\sum_{t=0}^{|o_{i}|}\nabla_{\theta}\log\pi_{\theta}(o_{i,t}|o_{i,<t},q) in VPG or 1 | o i | ​ ∑ t | o i | ∇ θ ρ i , t \frac{1}{|o_{i}|}\sum_{t}^{|o_{i}|}\nabla_{\theta}\rho_{i,t} in PPO/GRPO). Since 𝔼 ⁡ [ 𝒈 ] = 0 {\mathbb{E}}[\bm{g}]=0 over all potential actions, the variance of the product of these r.v.’s can be written as: Var ​ ( r ⋅ 𝒈 ) \displaystyle\text{Var}(r\cdot\bm{g}) = Var ​ ( 𝒈 ) ​ [ Var ​ ( r ) + ( 𝔼 ⁡ [ r ] ) 2 ] + Cov ​ ( r 2 , 𝒈 2 ) − ( Cov ​ ( r , 𝒈 ) ) 2 ⏟ Interaction term . \displaystyle=\text{Var}(\bm{g})\left[\text{Var}(r)+({\mathbb{E}}[r])^{2}\right]+\underbrace{\text{Cov}(r^{2},\bm{g}^{2})-(\text{Cov}(r,\bm{g}))^{2}}_{\text{Interaction term}}\,. (11) The interaction term can be ignored when importance sampling and clipping are applied, as the gradient is bounded in a small region. Previous work [ 3 , 31 , 32 , 33 ] shows that replacing raw rewards with advantage functions ( 𝔼 ⁡ [ a ] = 0 {\mathbb{E}}[a]=0 ) effectively reduces variance, leading to more stable and improved RL optimization.

### B.2 Mean Estimation with Samples n = 2 {n=2}

The instability of normalization with extremely small samples is a well-documented phenomenon in classical statistics, dating back to the seminal work of William Sealy Gosset (published under the pen name Student ) [ 36 ] . For a sample size of n = 2 n=2 , the degrees of freedom d ​ f = 1 df=1 result in a normalization factor that follows a Cauchy distribution. Such small-sample estimates of variance are highly skewed, leading to normalized outputs with infinite variance and no defined mean, undermining the goal of statistical stability.

### B.3 Reveal GRPO as Contrastive Learning

###### Proof of Proposition 3.2 .

In the RLVR setting, rewards are binary, which leads to binary advantages given a prompt. Let A q + , A q − A^{+}_{q},A^{-}_{q} denote the positive and negative advantage, respectively. From Eq. ( 4 ), we can have A q + \displaystyle A^{+}_{q} = 1 − p ^ q p ^ q ​ ( 1 − p ^ q ) = 1 − p ^ q p ^ q , \displaystyle=\frac{1-\hat{p}_{q}}{\sqrt{\hat{p}_{q}(1-\hat{p}_{q})}}=\sqrt{\frac{1-\hat{p}_{q}}{\hat{p}_{q}}}\;, (12) A q − \displaystyle A^{-}_{q} = 0 − p ^ q p ^ q ​ ( 1 − p ^ q ) = − p ^ q 1 − p ^ q . \displaystyle=\frac{0-\hat{p}_{q}}{\sqrt{\hat{p}_{q}(1-\hat{p}_{q})}}=-\sqrt{\frac{\hat{p}_{q}}{1-\hat{p}_{q}}}\;.

The clipping function is clip ​ ( x , 1 − ϵ , 1 + ϵ ) = { x , | x − 1 | ≤ ϵ 1 − ϵ , x < 1 − ϵ 1 + ϵ , x > 1 + ϵ , \text{clip}(x,1-\epsilon,1+\epsilon)=\begin{cases}x,&|x-1|\leq\epsilon\\ 1-\epsilon,&x<1-\epsilon\\ 1+\epsilon,&x>1+\epsilon\end{cases}\,, (13) which means that x x will be assigned to 1 − ϵ 1-\epsilon ( 1 + ϵ 1+\epsilon ) if x x is less (greater) than 1 − ϵ 1-\epsilon ( 1 + ϵ 1+\epsilon ). For simplifying notation, let 𝒞 ϵ + ​ ( x ) = min ⁡ [ x , 1 + ϵ ] \mathcal{C}_{\epsilon}^{+}(x)=\min[x,1+\epsilon] and 𝒞 ϵ − = max ⁡ [ x , 1 − ϵ ] \mathcal{C}_{\epsilon}^{-}=\max[x,1-\epsilon] .

The key derivation of rewriting GRPO objective is as follows: 𝒥 GRPO ​ ( θ ) \displaystyle\mathcal{J}_{\text{GRPO}}(\theta) (14) = 𝔼 q ∼ 𝒬 { o i } i = 1 G ∼ π θ old ( ⋅ | q ) ​ 1 G ​ ∑ i = 1 G 1 | o i | ​ ∑ t = 1 | o i | 𝒞 ϵ ​ ( π θ ​ ( o i , t | o i , < t , q ) π θ old ​ ( o i , t | o i , < t , q ) ​ A i , t ) , \displaystyle=\mathbb{E}_{\begin{subarray}{c}q\sim\mathcal{Q}\\ \{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|q)\end{subarray}}\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\mathcal{C}_{\epsilon}\left(\frac{\pi_{\theta}(o_{i,t}|o_{i,<t},q)}{\pi_{\theta_{\text{old}}}(o_{i,t}|o_{i,<t},q)}A_{i,t}\right)\,, = 𝔼 q ∼ 𝒬 { o j } j = 1 G + ∼ π θ old + ( ⋅ | q ) { o k } k = 1 G − ∼ π θ old − ( ⋅ | q ) \displaystyle=\mathbb{E}_{\begin{subarray}{c}q\sim\mathcal{Q}\\ \{o_{j}\}_{j=1}^{G^{+}}\sim\pi_{\theta_{\text{old}}}^{+}(\cdot|q)\\ \{o_{k}\}_{k=1}^{G^{-}}\sim\pi_{\theta_{\text{old}}}^{-}(\cdot|q)\end{subarray}} 1 G ​ ( ∑ j = 1 G + 1 | o j | ​ ∑ t = 1 | o j | A j + ​ 𝒞 ϵ + ​ ( π θ ​ ( o j , t | o j , < t , q ) π θ old ​ ( o j , t | o j , < t , q ) ) + ∑ k = 1 G − 1 | o k | ​ ∑ t = 1 | o k | A k − ​ 𝒞 ϵ − ​ ( π θ ​ ( o k , t | o k , < t , q ) π θ old ​ ( o k , t | o k , < t , q ) ) ) , \displaystyle\frac{1}{G}\left(\sum_{j=1}^{G^{+}}\frac{1}{|o_{j}|}\sum_{t=1}^{|o_{j}|}A_{j}^{+}\mathcal{C}_{\epsilon}^{+}\left(\frac{\pi_{\theta}(o_{j,t}|o_{j,<t},q)}{\pi_{\theta_{\text{old}}}(o_{j,t}|o_{j,<t},q)}\right)+\sum_{k=1}^{G^{-}}\frac{1}{|o_{k}|}\sum_{t=1}^{|o_{k}|}A_{k}^{-}\mathcal{C}_{\epsilon}^{-}\left(\frac{\pi_{\theta}(o_{k,t}|o_{k,<t},q)}{\pi_{\theta_{\text{old}}}(o_{k,t}|o_{k,<t},q)}\right)\right)\,, = 𝔼 q ∼ 𝒬 { o j } j = 1 G + ∼ π θ old + ( ⋅ | q ) { o k } k = 1 G − ∼ π θ old − ( ⋅ | q ) \displaystyle=\mathbb{E}_{\begin{subarray}{c}q\sim\mathcal{Q}\\ \{o_{j}\}_{j=1}^{G^{+}}\sim\pi_{\theta_{\text{old}}}^{+}(\cdot|q)\\ \{o_{k}\}_{k=1}^{G^{-}}\sim\pi_{\theta_{\text{old}}}^{-}(\cdot|q)\end{subarray}} A q + ​ G + G ​ 1 G + ​ ∑ j = 1 G + 1 | o j | ​ ∑ t = 1 | o j | 𝒞 ϵ + ​ ( π θ ​ ( o j , t | o j , < t , q ) π θ old ​ ( o j , t | o j , < t , q ) ) + A q − ​ G − G ​ 1 G − ​ ∑ k = 1 G − 1 | o k | ​ ∑ t = 1 | o k | 𝒞 ϵ − ​ ( π θ ​ ( o k , t | o k , < t , q ) π θ old ​ ( o k , t | o k , < t , q ) ) , \displaystyle A^{+}_{q}\frac{G^{+}}{G}\frac{1}{G^{+}}\sum_{j=1}^{G^{+}}\frac{1}{|o_{j}|}\sum_{t=1}^{|o_{j}|}\mathcal{C}_{\epsilon}^{+}\left(\frac{\pi_{\theta}(o_{j,t}|o_{j,<t},q)}{\pi_{\theta_{\text{old}}}(o_{j,t}|o_{j,<t},q)}\right)+A^{-}_{q}\frac{G^{-}}{G}\frac{1}{G^{-}}\sum_{k=1}^{G^{-}}\frac{1}{|o_{k}|}\sum_{t=1}^{|o_{k}|}\mathcal{C}_{\epsilon}^{-}\left(\frac{\pi_{\theta}(o_{k,t}|o_{k,<t},q)}{\pi_{\theta_{\text{old}}}(o_{k,t}|o_{k,<t},q)}\right)\,, = 𝔼 q ∼ 𝒬 { o j } j = 1 G + ∼ π θ old + ( ⋅ | q ) { o k } k = 1 G − ∼ π θ old − ( ⋅ | q ) \displaystyle=\mathbb{E}_{\begin{subarray}{c}q\sim\mathcal{Q}\\ \{o_{j}\}_{j=1}^{G^{+}}\sim\pi_{\theta_{\text{old}}}^{+}(\cdot|q)\\ \{o_{k}\}_{k=1}^{G^{-}}\sim\pi_{\theta_{\text{old}}}^{-}(\cdot|q)\end{subarray}} Var ^ G ​ ( q ) ​ ( 1 G + ​ ∑ j = 1 G + 1 | o j | ​ ∑ t = 1 | o j | 𝒞 ϵ + ​ ( π θ ​ ( o j , t | o j , < t , q ) π θ old ​ ( o j , t | o j , < t , q ) ) − 1 G − ​ ∑ k = 1 G − 1 | o k | ​ ∑ t = 1 | o k | 𝒞 ϵ − ​ ( π θ ​ ( o k , t | o k , < t , q ) π θ old ​ ( o k , t | o k , < t , q ) ) ) . \displaystyle\sqrt{\widehat{\mathrm{Var}}_{G}(q)}\left(\frac{1}{G^{+}}\sum_{j=1}^{G^{+}}\frac{1}{|o_{j}|}\sum_{t=1}^{|o_{j}|}\mathcal{C}_{\epsilon}^{+}\left(\frac{\pi_{\theta}(o_{j,t}|o_{j,<t},q)}{\pi_{\theta_{\text{old}}}(o_{j,t}|o_{j,<t},q)}\right)-\frac{1}{G^{-}}\sum_{k=1}^{G^{-}}\frac{1}{|o_{k}|}\sum_{t=1}^{|o_{k}|}\mathcal{C}_{\epsilon}^{-}\left(\frac{\pi_{\theta}(o_{k,t}|o_{k,<t},q)}{\pi_{\theta_{\text{old}}}(o_{k,t}|o_{k,<t},q)}\right)\right)\,. The second equation is obtained by dividing the trajectories into two groups: positive and negative. The third equation is obtained by the fact that all positive advantages are the same and that all negative advantages are the same. Since A + ​ G + G = 1 − p ^ p ^ ​ p ^ = ( 1 − p ^ ) ​ p ^ A^{+}\frac{G^{+}}{G}=\sqrt{\frac{1-\hat{p}}{\hat{p}}}\hat{p}=\sqrt{(1-\hat{p})\hat{p}} and A − ​ G − G = − ( 1 − p ^ ) ​ p ^ A^{-}\frac{G^{-}}{G}=-\sqrt{(1-\hat{p})\hat{p}} , we obtain Eq. ( 7 ). When G → ∞ G\to\infty , we have the following facts: lim G → ∞ G + = ∞ , \displaystyle\lim_{G\to\infty}G^{+}=\infty\;, (15) lim G → ∞ G − = ∞ \displaystyle\lim_{G\to\infty}G^{-}=\infty lim G → ∞ ( 1 − p ^ ) ​ p ^ = ( 1 − p ) ​ p , \displaystyle\lim_{G\to\infty}\sqrt{(1-\hat{p})\hat{p}}=\sqrt{(1-p)p}\;, lim G + → ∞ 1 G + ​ ∑ j = 1 G + f ⁡ ( o j ) = 𝔼 o j ∼ O θ + ​ f ​ ( o j ) , \displaystyle\lim_{G^{+}\to\infty}\frac{1}{G^{+}}\sum_{j=1}^{G^{+}}f(o_{j})={\mathbb{E}}_{o_{j}\sim O_{\theta}^{+}}f(o_{j})\;, lim G − → ∞ 1 G − ​ ∑ k = 1 G − f ⁡ ( o k ) = 𝔼 o k ∼ O θ − ​ f ​ ( o k ) . \displaystyle\lim_{G^{-}\to\infty}\frac{1}{G^{-}}\sum_{k=1}^{G^{-}}f(o_{k})={\mathbb{E}}_{o_{k}\sim O_{\theta}^{-}}f(o_{k})\;.

Then the GRPO objective has the following gradient w.r.t. parameter θ \theta : ∇ θ 𝒥 GRPO = \displaystyle\nabla_{\theta}\mathcal{J}_{\text{GRPO}}= 𝔼 q ∼ 𝒬 ​ Var ^ G ​ ( q ) ​ ( 1 G q + ​ ∑ j = 1 G q + ∑ t | o j + | 𝟙 j , t ϵ ​ ∇ θ π θ ​ ( o j , t + | o j , < t + , q ) | o j + | ​ π θ old ​ ( o j , t + | o j , < t + , q ) − 1 G q − ​ ∑ k = 1 G q − ∑ t o k − 𝟙 k , t ϵ ​ ∇ θ π θ ​ ( o k , t − | o k , < t − , q ) | o k − | ​ π θ old ​ ( o k , t − | o k , < t − , q ) ) \displaystyle\underset{q\sim\mathcal{Q}}{{\mathbb{E}}}\sqrt{\widehat{\mathrm{Var}}_{G}(q)}\Bigg(\frac{1}{G_{q}^{+}}\sum_{j=1}^{G_{q}^{+}}\sum_{t}^{|o_{j}^{+}|}\frac{\mathbbm{1}^{\epsilon}_{j,t}\nabla_{\theta}\pi_{\theta}(o_{j,t}^{+}|o_{j,<t}^{+},q)}{|o_{j}^{+}|\pi_{\theta_{\text{old}}}(o_{j,t}^{+}|o_{j,<t}^{+},q)}-\frac{1}{G_{q}^{-}}\sum_{k=1}^{G_{q}^{-}}\sum_{t}^{o_{k}^{-}}\frac{\mathbbm{1}^{\epsilon}_{k,t}\nabla_{\theta}\pi_{\theta}(o_{k,t}^{-}|o_{k,<t}^{-},q)}{|o_{k}^{-}|\pi_{\theta_{\text{old}}}(o_{k,t}^{-}|o_{k,<t}^{-},q)}\Bigg) (16) = 𝔼 q ∼ 𝒬 ​ [ 1 G q + ​ ∑ j = 1 G q + ∑ t | o j + | c ⁡ ( o j , t + | o j , < t + , q ) ​ ∇ θ π θ ​ ( o j , t + | o j , < t + , q ) ⏟ Positive − 1 G q − ​ ∑ k = 1 G q − ∑ t | o k − | c ⁡ ( o k , t − | o k , < t − , q ) ​ ∇ θ π θ ​ ( o k , t − | o k , < t − , q ) ⏟ Negative ] \displaystyle=\underset{q\sim\mathcal{Q}}{{\mathbb{E}}}\Bigg[\underbrace{\frac{1}{G_{q}^{+}}\sum_{j=1}^{G_{q}^{+}}\sum_{t}^{|o_{j}^{+}|}c(o_{j,t}^{+}|o_{j,<t}^{+},q)\nabla_{\theta}\pi_{\theta}(o_{j,t}^{+}|o_{j,<t}^{+},q)}_{\text{Positive}}-\underbrace{\frac{1}{G_{q}^{-}}\sum_{k=1}^{G_{q}^{-}}\sum_{t}^{|o_{k}^{-}|}c(o_{k,t}^{-}|o_{k,<t}^{-},q)\nabla_{\theta}\pi_{\theta}(o_{k,t}^{-}|o_{k,<t}^{-},q)}_{\text{Negative}}\Bigg] (17) where 𝟙 j , t ϵ \mathbbm{1}^{\epsilon}_{j,t} is an indicator function if the token o j , t o_{j,t} is clipped and c ⁡ ( o i , t | o i , < t , q ) := Var ^ ​ ( q ) ​ 𝟙 i , t ϵ | o i | ​ π θ old ​ ( o i , t | o i , < t , q ) c(o_{i,t}|o_{i,<t},q):=\frac{\sqrt{\widehat{\mathrm{Var}}(q)}\mathbbm{1}^{\epsilon}_{i,t}}{|o_{i}|\pi_{\theta_{\text{old}}}(o_{i,t}|o_{i,<t},q)} . Compare Eq. ( 17 ) with Def. 3.1 , the derivative of GRPO is a Monte Carlo estimator of contrastive derivative. ∎

### B.4 Further Discussion on Importance Sampling and the Log-likelihood Term

Most autoregressive LLMs adopt causal probability modelling as log ⁡ π θ ​ ( o | q ) = ∑ log ⁡ π θ ​ ( o t | o < t , q ) \log\pi_{\theta}(o|q)=\sum\log\pi_{\theta}(o_{t}|o_{<t},q) . This decomposition leads to the following trajectory-level form to describe the gradient of token probabilities: ∇ θ ​ log ​ π θ ​ ( o | q ) = ∑ t 1 π θ ​ ( o t | o < t , q ) ​ ∇ θ π θ ​ ( o t | o < t , q ) . \nabla_{\theta}\log\pi_{\theta}(o|q)=\sum_{t}\frac{1}{\pi_{\theta}(o_{t}|o_{<t},q)}\nabla_{\theta}\pi_{\theta}(o_{t}|o_{<t},q)\,. (18) DPO follows a similar structural derivation.

It is worth mentioning that the importance sampling in PPO can be viewed as a natural extension of such gradient form for online on/off-policy RL [ 33 ] . However, the token-level importance sampling in PPO and vanilla GRPO often obscures this direct connection at the trajectory level.

Recent subsequent variants of GRPO [ 46 , 45 , 28 ] , e.g., GSPO and TIC-GRPO, utilize sequence-level importance sampling. This formulation allows us to draw a direct connection between importance sampling and the log-likelihood terms: ∇ θ π θ ​ ( o ∣ q ) π θ old ​ ( o ∣ q ) = π θ ​ ( o ∣ q ) π θ old ​ ( o ∣ q ) ​ ∑ t 1 π θ ​ ( o t ∣ o < t , q ) ​ ∇ θ π θ ​ ( o t ∣ o < t , q ) . \nabla_{\theta}\frac{\pi_{\theta}(o\mid q)}{\pi_{\theta_{\mathrm{old}}}(o\mid q)}=\frac{\pi_{\theta}(o\mid q)}{\pi_{\theta_{\mathrm{old}}}(o\mid q)}\sum_{t}\frac{1}{\pi_{\theta}(o_{t}\mid o_{<t},q)}\nabla_{\theta}\pi_{\theta}(o_{t}\mid o_{<t},q)\,. (19) It is straightforward to see from the gradient form that the importance sampling term adjusts the Log-likelihood term by a coefficient π θ ​ ( o ∣ q ) π θ old ​ ( o | q ) \frac{\pi_{\theta}(o\mid q)}{\pi_{\theta_{\mathrm{old}}}(o|q)} . The token-level importance sampling in PPO and GRPO behaves similarly by applying token-level correction.

The clipping applied on top of importance sampling is a minor additional modification, which we do not elaborate on here.

### B.5 Proof of Lemma B.1 : DPO is 1-vs-1 contrastive learning

###### Lemma B.1 .

The DPO loss is a 1 1 -vs- 1 1 contrastive loss estimator.

###### Proof of Lemma B.1 .

The DPO loss (Eq. ( 6 )) has the following derivatives: \displaystyle ∇ θ ℒ DPO = − β ​ 𝔼 [ ( q , o + , o − ) ∼ 𝒟 DPO ] ​ [ σ ⁡ ( r ^ θ ​ ( q , o − ) − r ^ θ ​ ( q , o + ) ) ​ ( ∇ θ ​ log ​ π θ ​ ( o + | q ) − ∇ θ ​ log ​ π θ ​ ( o − | q ) ) ] \displaystyle\nabla_{\theta}\mathcal{L}_{\text{DPO}}=-\beta\underset{[(q,o^{+},o^{-})\sim{\mathcal{D}}_{\text{DPO}}]}{{\mathbb{E}}}\Big[\sigma(\hat{r}_{\theta}(q,o^{-})-\hat{r}_{\theta}(q,o^{+}))\left(\nabla_{\theta}\log\pi_{\theta}(o^{+}|q)-\nabla_{\theta}\log\pi_{\theta}(o^{-}|q)\right)\Big]\;\, (20) = − 𝔼 [ ( q , o + , o − ) ∼ 𝒟 DPO ] ​ [ ∑ t | o + | c ⁡ ( o t + | o < t + , q ) ​ ∇ θ π θ ​ ( o t + | o < t + , q ) ⏟ Positive − ∑ t | o − | c ⁡ ( o t − | o < t − , q ) ​ ∇ θ π θ ​ ( o t − | o < t − , q ) ⏟ Negative ] \displaystyle=-\underset{[(q,o^{+},o^{-})\sim{\mathcal{D}}_{\text{DPO}}]}{{\mathbb{E}}}\Bigg[\underbrace{\sum_{t}^{|o^{+}|}c(o^{+}_{t}|o^{+}_{<t},q)\nabla_{\theta}\pi_{\theta}(o^{+}_{t}|o^{+}_{<t},q)}_{\text{Positive}}-\underbrace{\sum_{t}^{|o^{-}|}c(o^{-}_{t}|o^{-}_{<t},q)\nabla_{\theta}\pi_{\theta}(o^{-}_{t}|o^{-}_{<t},q)}_{\text{Negative}}\Bigg] where r ^ θ = β ⁡ ( x , y ) ​ log ⁡ π θ ​ ( y | x ) π ref ​ ( y | x ) \hat{r}_{\theta}=\beta(x,y)\log\frac{\pi_{\theta}(y|x)}{\pi_{\text{ref}}(y|x)} ; σ \sigma denotes the sigmoid function; and c ⁡ ( o t | o < t , q ) := β ​ σ ​ ( r ^ θ ​ ( q , o − ) − r ^ θ ​ ( q , o + ) ) π θ ​ ( o | q ) c(o_{t}|o_{<t},q):=\frac{\beta\sigma(\hat{r}_{\theta}(q,o^{-})-\hat{r}_{\theta}(q,o^{+}))}{\pi_{\theta}(o|q)} aligning with Def. 3.1 . ∎

### B.6 GRPO v.s. DPO from Contrastive Learning

As shown in Appx. B.3 and B.5 , GRPO and DPO admit the following gradient formulations: ∇ θ 𝒥 GRPO = 𝔼 q ∼ 𝒬 ​ [ ∑ t | o + | c ⁡ ( o t + | o < t + , q ) ​ ∇ θ π θ ​ ( o t + | o < t + , q ) ⏟ Positive − ∑ t | o k − | c ⁡ ( o k , t − | o k , < t − , q ) ​ ∇ θ π θ ​ ( o k , t − | o k , < t − , q ) ⏟ Negative ] \displaystyle\nabla_{\theta}\mathcal{J}_{\text{GRPO}}=\underset{q\sim\mathcal{Q}}{\mathbb{E}}\Bigg[\underbrace{\sum_{t}^{|o^{+}|}c(o_{t}^{+}|o_{<t}^{+},q)\nabla_{\theta}\pi_{\theta}(o_{t}^{+}|o_{<t}^{+},q)}_{\text{Positive}}-\underbrace{\sum_{t}^{|o_{k}^{-}|}c(o_{k,t}^{-}|o_{k,<t}^{-},q)\nabla_{\theta}\pi_{\theta}(o_{k,t}^{-}|o_{k,<t}^{-},q)}_{\text{Negative}}\Bigg] (21) ∇ θ ℒ DPO = − 𝔼 [ ( q , o + , o − ) ∼ 𝒟 DPO ] ​ [ ∑ t | o + | c ⁡ ( o t + | o < t + , q ) ​ ∇ θ π θ ​ ( o t + | o < t + , q ) ⏟ Positive − ∑ t | o − | c ⁡ ( o t − | o < t − , q ) ​ ∇ θ π θ ​ ( o t − | o < t − , q ) ⏟ Negative ] \displaystyle\nabla_{\theta}\mathcal{L}_{\text{DPO}}=-\underset{[(q,o^{+},o^{-})\sim\mathcal{D}_{\text{DPO}}]}{\mathbb{E}}\Bigg[\underbrace{\sum_{t}^{|o^{+}|}c(o^{+}_{t}|o^{+}_{<t},q)\nabla_{\theta}\pi_{\theta}(o^{+}_{t}|o^{+}_{<t},q)}_{\text{Positive}}-\underbrace{\sum_{t}^{|o^{-}|}c(o^{-}_{t}|o^{-}_{<t},q)\nabla_{\theta}\pi_{\theta}(o^{-}_{t}|o^{-}_{<t},q)}_{\text{Negative}}\Bigg] (22)

These expressions reveal that both maximizing the GRPO objective and minimizing the DPO loss correspond to the same underlying contrastive learning mechanism, differing only in the specific design of the coefficient c ⁡ ( o t + | o < t + , q ) c(o_{t}^{+}|o_{<t}^{+},q) .

The key distinction lies in how the coefficient c ⁡ ( ⋅ ) c(\cdot) is instantiated under different RL settings (online vs. offline): • Importance sampling term (online GRPO) vs. log-likelihood term (offline DPO) (see Appx. B.4 for detailed discussion).

• Reference-model regularization : an explicit KL term (GRPO) vs. implicit incorporation into the “advantage” (DPO).

Importantly, these differences do not alter the fundamental optimization structure, but rather reflect distinct design choices tailored to their respective RL regimes.

### B.7 Proof of Proposition 4.1

###### Proof.

Var ⁡ ( 𝒈 + − c ​ 𝒈 − ) \displaystyle\mathrm{Var}(\bm{g}^{+}-c\bm{g}^{-}) = Var ⁡ ( 𝒈 + ) + c 2 ​ Var ​ ( 𝒈 − ) − 2 ​ c ​ Cov ​ ( 𝒈 + , 𝒈 − ) , \displaystyle=\mathrm{Var}(\bm{g}^{+})+c^{2}\mathrm{Var}(\bm{g}^{-})-2c\mathrm{Cov}(\bm{g}^{+},\bm{g}^{-})\,, (23) = Var ⁡ ( 𝒈 + ) − Cov 2 ​ ( 𝒈 + , 𝒈 − ) Var ⁡ ( 𝒈 − ) , \displaystyle=\mathrm{Var}(\bm{g}^{+})-\frac{\mathrm{Cov}^{2}(\bm{g}^{+},\bm{g}^{-})}{\mathrm{Var}(\bm{g}^{-})}\,, = ( 1 − ρ 2 ) ​ Var ​ ( 𝒈 + ) . \displaystyle=(1-\rho^{2})\mathrm{Var}(\bm{g}^{+})\,. The first equation is obtained by the definition of variance. The second equation is obtained by substituting c = Cov ⁡ ( 𝒈 + , 𝒈 − ) Var ⁡ ( 𝒈 − ) c=\frac{\mathrm{Cov}(\bm{g}^{+},\bm{g}^{-})}{\mathrm{Var}(\bm{g}^{-})} . The third equation is hold because ρ = Cov ⁡ ( 𝒈 + , 𝒈 − ) Var ⁡ ( 𝒈 + ) ​ Var ​ ( 𝒈 − ) \rho=\frac{\mathrm{Cov}(\bm{g}^{+},\bm{g}^{-})}{\sqrt{\mathrm{Var}(\bm{g}^{+})\mathrm{Var}(\bm{g}^{-})}} . On the other hand, consider f ⁡ ( c ) = c 2 ​ Var ​ ( 𝒈 − ) − 2 ​ c ​ Cov ​ ( 𝒈 + , 𝒈 − ) f(c)=c^{2}\mathrm{Var}(\bm{g}^{-})-2c\mathrm{Cov}(\bm{g}^{+},\bm{g}^{-}) . If 0 ≤ c ≤ 2 ​ Cov 2 ​ ( 𝒈 + , 𝒈 − ) Var ⁡ ( 𝒈 − ) 0\leq c\leq 2\frac{\mathrm{Cov}^{2}(\bm{g}^{+},\bm{g}^{-})}{\mathrm{Var}(\bm{g}^{-})} , then f ⁡ ( c ) ≤ 0 f(c)\leq 0 . ∎

### B.8 The Correlation between The Positive and The Negative

We do not have access to the joint distribution of positive and negative gradients, so direct empirical estimation of their covariance is infeasible. Instead, we use the law of total covariance: Cov ⁡ ( 𝒈 + , 𝒈 − ) = 𝔼 p ​ [ Cov ⁡ ( 𝒈 + , 𝒈 − ∣ p ) ] + Cov p ​ ( 𝔼 ⁡ [ 𝒈 + | p ] , 𝔼 ⁡ [ 𝒈 − | p ] ) . \mathrm{Cov}(\bm{g}^{+},\bm{g}^{-})=\mathbb{E}_{p}[\mathrm{Cov}(\bm{g}^{+},\bm{g}^{-}\mid p)]+\mathrm{Cov}_{p}(\mathbb{E}[\bm{g}^{+}|p],\mathbb{E}[\bm{g}^{-}|p])\,. (24) Under conditionally independent sampling, the first term is zero, so we estimate the second term across prompts. Statistics are computed over 100 prompts with 10 responses each on MATH with Qwen-1.5B. As high-dimensional vectors usually have small dot-products, we report a baseline as reference where pos/neg pairs are randomly permuted.

As shown in the table, the covariance between positive and negative gradients from the same prompt is significantly larger than that between randomly paired positive and negative gradients, which confirms our assumption.

### B.9 Proof of Proposition C.1

###### Proof.

Case 1. Notice that σ ^ = 1 2 ​ N ​ ∑ k = 1 2 ​ N ( X k − μ ^ ) 2 = μ ^ ​ ( 1 − μ ^ ) \hat{\sigma}=\sqrt{\frac{1}{2N}\sum_{k=1}^{2N}(X_{k}-\hat{\mu})^{2}}=\sqrt{\hat{\mu}(1-\hat{\mu})} and μ ^ = 1 2 ​ N ​ ∑ k = 1 2 ​ N X k \hat{\mu}=\frac{1}{2N}\sum_{k=1}^{2N}X_{k} . Fix an index i i and condition on the event { X i = x } \{X_{i}=x\} with x ∈ { 0 , 1 } x\in\{0,1\} . In this case, by the strong law of large numbers and the continuous mapping theorem, we have μ ^ → a . s . p \hat{\mu}\stackrel{{\scriptstyle a.s.}}{{\rightarrow}}p and σ ^ → a . s . p ⁡ ( 1 − p ) \hat{\sigma}\stackrel{{\scriptstyle a.s.}}{{\rightarrow}}\sqrt{p(1-p)} . Thus, it follows that lim ϵ → 0 lim N → ∞ 𝔼 ⁡ [ Y i ∣ X i = x ] = x − p p ⁡ ( 1 − p ) . \lim_{\epsilon\rightarrow 0}\,\lim_{N\to\infty}\,{\mathbb{E}}\!\left[Y_{i}\mid X_{i}=x\right]=\frac{x-p}{\sqrt{p(1-p)}}.

Case 2. When X i , 1 = X i , 2 X_{i,1}=X_{i,2} , we have X i , j = μ ^ i X_{i,j}=\hat{\mu}_{i} and Y i , j = 0 Y_{i,j}=0 for any j ∈ { 1 , 2 } j\in\{1,2\} . When X i , 1 ≠ X i , 2 X_{i,1}\neq X_{i,2} , we have μ ^ i = 0.5 \hat{\mu}_{i}=0.5 , σ ^ i = 0.5 \hat{\sigma}_{i}=0.5 , and Y i , j = 2 ​ X i , j − 1 1 + 2 ​ ϵ . Y_{i,j}=\frac{2X_{i,j}-1}{1+2\epsilon}. By the law of total expectation, it follows that 𝔼 ⁡ [ Y i , j ∣ X i , j = 1 ] = 1 − p 1 + 2 ​ ϵ , 𝔼 ⁡ [ Y i , j ∣ X i , j = 0 ] = − p 1 + 2 ​ ϵ . {\mathbb{E}}\left[Y_{i,j}\mid X_{i,j}=1\right]=\frac{1-p}{1+2\epsilon},\qquad{\mathbb{E}}\left[Y_{i,j}\mid X_{i,j}=0\right]=\frac{-p}{1+2\epsilon}. Thus, we have lim ϵ → 0 𝔼 ⁡ [ Y i , j ∣ X i , j = x ] = x − p . \lim_{\epsilon\rightarrow 0}{\mathbb{E}}\!\left[Y_{i,j}\mid X_{i,j}=x\right]=x-p. ∎

### B.10 Proof of Lemma C.3

###### Proof of Lemma C.3 .

Var ⁡ ( 𝒈 ^ B ) \displaystyle\mathrm{Var}(\hat{\bm{g}}_{B}) = Var { 𝒙 i } i = 1 B ​ ( 1 B ​ ∑ i = 1 B 𝒈 ⁡ ( 𝒙 i ) ) \displaystyle=\mathrm{Var}_{\{{\bm{x}}_{i}\}_{i=1}^{B}}\left(\frac{1}{B}\sum_{i=1}^{B}\bm{g}({\bm{x}}_{i})\right) (25) = 1 B 2 ​ ∑ i = 1 B Var 𝒙 i ​ ( 𝒈 ⁡ ( 𝒙 i ) ) = Var 𝒙 ​ ( 𝒈 ​ ( 𝒙 ) ) B . \displaystyle=\frac{1}{B^{2}}\sum_{i=1}^{B}\mathrm{Var}_{{\bm{x}}_{i}}\!\left(\bm{g}({\bm{x}}_{i})\right)=\frac{\mathrm{Var}_{{\bm{x}}}\!\left(\bm{g}({\bm{x}})\right)}{B}\;.

where the second and third equalities are obtained by the properties of independence and identity in i.i.d. data, respectively. By the above equation, increasing B B decreases Var \mathrm{Var} . ∎

## Appendix C Theoretical Analysis of 2-GRPO

### C.1 Implicit Weighting in Stochastic Optimization

At first glance, 2-GRPO appears to use only fixed advantages, A + = 1 A^{+}=1 and A − = − 1 A^{-}=-1 , ignoring prompt-level success rates. However, under mini-batch stochastic optimization, 2-GRPO implicitly reweights prompts through their likelihood of forming contrastive pairs.

Standard GRPO relies on the empirical success rate p ^ q \hat{p}_{q} to estimate the true correctness probability p q p_{q} for advantage assignment, relying on larger group sizes for accuracy. While this mechanism appears degenerate in 2-GRPO, we show that, through the lens of stochastic optimization, 2-GRPO implicitly estimates the advantage.

Moreover, 2-GRPO does not simply estimate the large-group GRPO gradient with fewer samples; it induces a different prompt-level weighting that prioritizes prompts likely to yield contrastive pairs.

###### Proposition C.1 .

Given a constant p ∈ ( 0 , 1 ) p\in(0,1) and a small positive constant ϵ \epsilon , we consider two scenarios below: • Case 1 : Consider X 1 , ⋯ , X 2 ​ N ∼ i.i.d. Bernoulli ​ ( p ) X_{1},\cdots,X_{2N}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\text{Bernoulli}(p) . Let Y i = X i − μ ^ σ ^ + ϵ Y_{i}=\frac{X_{i}-\hat{\mu}}{\hat{\sigma}+\epsilon} , where μ ^ = 1 2 ​ N ​ ∑ i = 1 2 ​ N X i \hat{\mu}=\frac{1}{2N}\sum_{i=1}^{2N}X_{i} and σ ^ = 1 2 ​ N ​ ∑ i = 1 2 ​ N ( X i − μ ^ ) 2 \hat{\sigma}=\sqrt{\frac{1}{2N}\sum_{i=1}^{2N}\left(X_{i}-\hat{\mu}\right)^{2}} . Then, it follows that lim ϵ → 0 lim N → ∞ 𝔼 ⁡ [ Y i | X i = x ] = x − p p ⁡ ( 1 − p ) . \lim_{\epsilon\rightarrow 0}\lim_{N\rightarrow\infty}{\mathbb{E}}[Y_{i}|X_{i}=x]=\frac{x-p}{\sqrt{p(1-p)}}. (26)

• Case 2 : Consider N N pairs of ( X i , 1 , X i , 2 ) (X_{i,1},X_{i,2}) with each X i , j ∼ i.i.d. Bernoulli ​ ( p ) X_{i,j}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\text{Bernoulli}(p) . Let Y i , j = X i , j − μ ^ i σ ^ i + ϵ Y_{i,j}=\frac{X_{i,j}-\hat{\mu}_{i}}{\hat{\sigma}_{i}+\epsilon} , where μ ^ i = 1 2 ​ ( X i , 1 + X i , 2 ) \hat{\mu}_{i}=\frac{1}{2}(X_{i,1}+X_{i,2}) and σ ^ i = 1 2 ​ ∑ j = 1 2 ( X i , j − μ ^ i ) 2 \hat{\sigma}_{i}=\sqrt{\frac{1}{2}\sum_{j=1}^{2}(X_{i,j}-\hat{\mu}_{i})^{2}} . Then, it follows that lim ϵ → 0 lim N → ∞ 𝔼 ⁡ [ Y i , j | X i , j = x ] = x − p . \lim_{\epsilon\rightarrow 0}\lim_{N\to\infty}{\mathbb{E}}[Y_{i,j}|X_{i,j}=x]=x-p. (27)

Term lim ϵ → 0 , N → ∞ 𝔼 ⁡ [ Y i , j | X i , j = x ] \lim_{\epsilon\rightarrow 0,N\to\infty}{\mathbb{E}}[Y_{i,j}|X_{i,j}=x] differs from lim ϵ → 0 , N → ∞ 𝔼 ⁡ [ Y i | X i = x ] \lim_{\epsilon\rightarrow 0,N\rightarrow\infty}{\mathbb{E}}[Y_{i}|X_{i}=x] by a scaling factor 1 p ⁡ ( 1 − p ) \frac{1}{\sqrt{p(1-p)}} .

In Proposition C.1 (proof in Appx. B.9 ), Case 1 corresponds to regular GRPO with sufficiently large group size. In this case, 𝔼 ⁡ [ Y i | X i = 1 ] {\mathbb{E}}[Y_{i}|X_{i}=1] and 𝔼 ⁡ [ Y i | X i = 0 ] {\mathbb{E}}[Y_{i}|X_{i}=0] are, respectively, the advantage estimates of positive and negative trajectories given a prompt, dependent on the success probability p q p_{q} . A large G G will lead to a better estimate of the success probability p q p_{q} . Case 2 corresponds to 2-GRPO, where 𝔼 ⁡ [ Y i , j | X i , j = 1 ] {\mathbb{E}}[Y_{i,j}|X_{i,j}=1] and 𝔼 ⁡ [ Y i , j | X i , j = 0 ] {\mathbb{E}}[Y_{i,j}|X_{i,j}=0] are advantage estimates, which are also dependent on the success rate p q p_{q} , amortizing over multiple stochastic updates.

2-GRPO produces advantage estimates that differ from standard GRPO solely by a scaling factor; this factor is effectively a design choice. Whether such a scaling is beneficial remains an open question [ 19 ] .

### C.2 Key of Variance Reduction: the Training Batch Size, not the Group Size

Beyond the inherent variance reduction mechanisms of PPO and GRPO, it is generally understood that using a larger group of rollouts yields a lower-variance policy gradient estimate. However, this perspective overlooks the practicalities of mini-batch optimization. In this section, we analyze the practical gradient variance within a mini-batch setting. To facilitate this discussion, we focus strictly on the optimization phase and treat the sampled rollouts as fixed training data for notational simplicity.

Note that there are two notions of “batch size” in VERL : data.train_batch_size denotes the rollout-generation batch size (by # prompts), whereas actor.ppo_mini_batch_size denotes the optimization mini-batch size (by # prompts). However, the effective number of samples during optimization is actually actor.ppo_mini_batch_size * rollout.n , counted by the number of rollouts.

###### Definition C.2 (Variance of Gradient Estimate in Mini-Batch) .

Without loss of generality, let { 𝒙 i } i = 1 B \{{\bm{x}}_{i}\}_{i=1}^{B} be a batch of B B random variables (r.v.’s), where each 𝒙 i {\bm{x}}_{i} is i.i.d. 𝒙 ∼ 𝒟 {\bm{x}}\sim{\mathcal{D}} , and let 𝒈 ⁡ ( 𝒙 i ) = ∇ θ L θ ​ ( 𝒙 i ) \bm{g}({\bm{x}}_{i})=\nabla_{\theta}L_{\theta}({\bm{x}}_{i}) denote the gradient of L θ ​ ( 𝒙 i ) L_{\theta}({\bm{x}}_{i}) w.r.t. θ \theta . Define the empirical batch gradient 𝒈 ^ B = 1 B ​ ∑ i = 1 B 𝒈 ⁡ ( 𝒙 i ) \hat{\bm{g}}_{B}=\frac{1}{B}\sum_{i=1}^{B}\bm{g}({\bm{x}}_{i}) . Note that 𝒈 ⁡ ( 𝒙 i ) \bm{g}({\bm{x}}_{i}) and 𝒈 ^ B \hat{\bm{g}}_{B} are dependent r.v.’s of 𝒙 i \bm{x}_{i} and { 𝒙 i } i = 1 B \{\bm{x}_{i}\}_{i=1}^{B} , respectively. We denote the expectation of the gradient 𝒈 ¯ = 𝔼 𝒙 ∼ 𝒟 ​ [ 𝒈 ​ ( 𝒙 ) ] \bar{\bm{g}}=\mathbb{E}_{{\bm{x}}\sim{\mathcal{D}}}[\bm{g}({\bm{x}})] . The variance of the gradient estimate over the batch is then defined as: Var ⁡ ( 𝒈 ^ B ) = Var { 𝒙 i } i B ​ ( 𝒈 ^ B ) = 𝔼 { 𝒙 i } i B ​ ( ( 𝒈 ^ B − 𝒈 ¯ ) 2 ) . {\mathrm{Var}}(\hat{\bm{g}}_{B})={\mathrm{Var}}_{\{{\bm{x}}_{i}\}_{i}^{B}}(\hat{\bm{g}}_{B})={\mathbb{E}}_{\{{\bm{x}}_{i}\}_{i}^{B}}\Big((\hat{\bm{g}}_{B}-\bar{\bm{g}})^{2}\Big). (28)

Following the definition of Variance of Gradient Estimate in Mini-batch (Def. C.2 ), we provide a lemma for its relationship to the mini-batch size.

###### Lemma C.3 .

Let { 𝐱 i } i = 1 B 1 , { 𝐱 i } i = 1 B 2 \{{\bm{x}}_{i}\}_{i=1}^{B_{1}},\{{\bm{x}}_{i}\}_{i=1}^{B_{2}} be two batches of B 1 B_{1} and B 2 B_{2} r.v.’s, respectively. Let g ^ B 1 , g ^ B 2 \hat{g}_{B_{1}},\hat{g}_{B_{2}} denote the empirical batch gradients of these two batches, respectively. If B 1 < B 2 B_{1}<B_{2} , then Var ⁡ [ g ^ B 1 ] > Var ⁡ [ g ^ B 2 ] \mathrm{Var}[\hat{g}_{B_{1}}]>\mathrm{Var}[\hat{g}_{B_{2}}] .

While decreasing the group size in Eq. ( 7 ) appears to increase the gradient variance for each individual prompt, this conclusion overlooks the total number of rollouts optimized across all prompts in a mini-batch, which is the effective number of examples for optimization. In Lemma C.3 (proof in Appx. B.10 ), we show that a larger batch size B B naturally leads to a lower variance of the gradient. Note that B B is the number of rollouts in each mini-batch rather than the number of prompts .

The actual calculation of GRPO is: 𝒥 ^ GRPO ​ ( θ , G , Q ) = 1 Q ​ G ​ ∑ j = 1 Q ∑ i = 1 G A i ​ j ​ π θ GRPO ​ ( o i ​ j | q j ) , \widehat{\mathcal{J}}_{\text{GRPO}}(\theta,G,Q)=\frac{1}{QG}\sum_{j=1}^{Q}\sum_{i=1}^{G}A_{ij}\pi_{\theta}^{\text{GRPO}}(o_{ij}|q_{j}), (29) where π θ GRPO ​ ( o | q ) = 1 G ​ ∑ i = 1 G 1 | o i | ​ ∑ t = 1 | o i | 𝒞 ϵ ​ ( A i , t ​ π θ ​ ( o i , t | o i , < t , q ) π θ old ​ ( o i , t | o i , < t , q ) ) \pi_{\theta}^{\text{GRPO}}(o|q)=\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\mathcal{C}_{\epsilon}\left(A_{i,t}\frac{\pi_{\theta}(o_{i,t}|o_{i,<t},q)}{\pi_{\theta_{\text{old}}}(o_{i,t}|o_{i,<t},q)}\right) and Q Q is the number of prompts in the mini-batch, and the batch size w.r.t the number of rollouts is B = Q ​ G B=QG . When we decrease G G , we can increase Q Q to compensate to retain the same B B in a mini-batch. Since the total number of prompts in the dataset is fixed, increasing Q Q does not increase the total computational cost per training epoch.

### C.3 Exploration on Hard Questions

A difficult question often requires many attempts to yield a correct answer, which is necessary to form a valid contrastive signal. With a smaller group, the likelihood of sampling a correct response in a single iteration may appear lower, potentially raising concerns about degraded learning.

Under a fixed computational budget, 2-GRPO and 16-GRPO explore approximately the same total number of rollouts across all training epochs – the overall probability of sampling a correct answer under 2-GRPO is not lower than 16-GRPO, according to the Proposition C.4 .

###### Proposition C.4 .

Let p i ∈ [ 0 , 1 ] p_{i}\in[0,1] denote the probability that a single rollout under the policy π i \pi_{i} produces a correct answer. Then: 1. The probability of obtaining at least one correct answer in 2 ​ m 2m independent rollouts with policy π 0 \pi_{0} is P 2 ​ m = 1 − ( 1 − p 0 ) 2 ​ m . P_{2m}=1-(1-p_{0})^{2m}. (30)

2. The probability of obtaining at least one correct answer when performing m m consecutive trials of 2 2 independent rollouts each, with the corresponding policy [ π 0 , π 1 , ⋯ , π m − 1 ] [\pi_{0},\pi_{1},\cdots,\pi_{m-1}] is P m × 2 = 1 − ∏ i = 0 , ⋯ m − 1 ( 1 − p i ) 2 ≥ 1 − ( 1 − p 0 ) 2 ​ m = P 2 ​ m P_{m\times 2}=1-\prod_{i=0,\cdots m-1}(1-p_{i})^{2}\geq 1-(1-p_{0})^{2m}=P_{2m} (31) when we have p i ≥ p 0 , ∀ i > 0 p_{i}\geq p_{0},\forall i>0 .

Note that the assumption p i ≥ p 0 , ∀ i > 0 p_{i}\geq p_{0},\forall i>0 is prevailing, as we assume that the reasoning ability of LLM can be improved by RL post-training.

Proposition C.4 suggests that for difficult questions, 2-GRPO does not degrade in effectiveness compared to 16-GRPO given the same budget of the total number of rollouts in whole training process. Notably, due to its higher frequency of policy updates, 2-GRPO may yield a higher probability of generating correct outputs for hard questions. It is also more adaptive, allowing it to capture nuanced update requirements for varying inputs. This observation also extends to PPO with the standard single-rollout implementations per epoch against multi-rollout variants.

## Appendix D Experiments

### D.1 Experiment Details

#### Dataset and Baselines

For math reasoning task, following prior work [ 6 ] , we employ Qwen2.5-Math-1.5B (Qwen-1.5B) and Qwen2.5-Math-7B (Qwen-7B) [ 41 ] as base models. Both models are post-trained via RL on the MATH [ 14 ] and DAPO-Math-17k [ 42 ] datasets, and evaluated on MATH-500 [ 14 ] , AMC23, Minerva Math [ 18 ] , AIME-2025, and OlympiadBench [ 11 ] . For DAPO-Math-17k dataset, we randomly sample 7.5k questions from the original data to form a subset for training in order to align with the size of MATH. In addition, we assess the proposed method on DeepSeek-R1-Distill-Qwen-1.5B (DS-1.5B) [ 7 ] , which is post-trained on MATH. Owing to computational constraints, we do not extend its post-training to DAPO-Math-17k. All 1.5B models are trained on 4 GPUs with 140GB Memory. Qwen-7B is trained on 8 GPUs with 140GB Memory. We evaluate model performance using two metrics: Mean@32, the average accuracy across 32 i.i.d. samples, and Pass@32, which measures whether a problem is solved in at least one of those 32 attempts.

For visual reasoning task, we use EasyR1 [ 48 ] framework, Qwen2.5-7B [ 2 ] as the base model, and Geometric3K [ 23 ] as the dataset. For code generation task, we use Code-R1 [ 21 ] framework, Qwen2.5-7B-Instruct-1M as the base model, and code-r1-12k 5 5 5 https://huggingface.co/datasets/ganler/code-r1-12k as the dataset. Both visual reasoning and code generation tasks are conducted on 8 GPU.

#### Hyper-parameters

We mainly follow the default configuration of the verl framework. For sampling parameters in training generation, we set temperature to 1, top-p to 1 to encourage exploration, sequence length to 4096 for Qwen-series model and 8192 for DS-1.5B. For sampling parameters in test generation, we set temperature to 0.7, top-p to 0.8, top-k to 20 and sequence length to 4096 for all models. For optimization, training employs the Adam optimizer [ 17 ] with a constant learning rate and a linear warm-up over the first 10 steps. For GRPO hyper-parameters, we set the clip ratio high to 0.28 0.28 and clip ratio lower to 0.2 0.2 following DAPO [ 42 ] . All models are trained for 10 epochs. The baseline method, 16-GRPO, is trained with batch sizes of 32 (32 prompts and 16 rollouts per prompt) and a learning rate 1 × 10 − 6 1\times 10^{-6} . As discussed in Appx. C.2 , we trained 2-GRPO with a larger batch size of 256 (256 prompts and 2 rollouts per prompt). Both case will have 512 rollouts in each mini-batch of training. Since we have fewer update steps due to the larger batch size, we adjust the learning rate of 2-GRPO to 8 × 10 − 6 8\times 10^{-6} based on the linear relationship of learning rate and batch size [ 10 ] .

### D.2 The Connection Between Training Rollouts and Computational Cost

In Sec. 5.1 , the total number of rollouts generated and utilized during training is adopted as a metric for comparing the computational cost of different methods.

The rationale for this choice is as follows. A principled measure of computational cost in the context of RL post-training is the number of floating-point operations (FLOPs) performed. Unlike wall-clock time, which is susceptible to variations arising from software implementation details (e.g., optimization of training libraries) and hardware characteristics (e.g., GPU/CPU architecture, I/O throughput), FLOPs provide a more direct and stable measure of computational effort.

For a fixed base model and the same type of RL algorithm (GRPO in our case), the FLOPs required for a single forward or backward pass with one input prompt can be considered constant, for both the generation and training phases. Accordingly, the total number of rollouts executed during training is directly proportional to the FLOPs executed, thereby serving as a theoretically justified and consistent proxy for computational cost.

### D.3 Sample Discard Rate of 2-GRPO

As discussed in Sec. 4.3 , 2-GRPO may suffer from a high discard rate when prompts are either extremely easy or extremely difficult for the LLM.

In the RLVR setting, the average discard rate P discard P_{\text{discard}} can be estimated from the average reward r ¯ \bar{r} as P discard = 1 − r ¯ 2 − ( 1 − r ¯ ) 2 . P_{\text{discard}}=1-\bar{r}^{2}-(1-\bar{r})^{2}.

To quantify this effect, we report the average discard rate of 2-GRPO using Qwen-7B post-trained on MATH as a representative case (shown in Table 3 ).

### D.4 Ablation Study on Group Size

We present a comprehensive ablation study on group size in Table 4 . To further illustrate this effect, Figure 5 reports the reward curves during training alongside the corresponding validation scores throughout the training process on MATH dataset.

## Appendix E Limitation

The contrastive learning nature of GRPO applies regardless of whether rewards are continuous or binary. However, the present study focuses primarily on the reasoning tasks with the RLVR setting, and we leave the empirical investigation of continuous rewards to future work due to the space limit.

## Appendix F The Use of Large Language Models (LLMs)

We used LLMs in writing, editing and formatting purposes. Our experiments also involve the LLMs.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
