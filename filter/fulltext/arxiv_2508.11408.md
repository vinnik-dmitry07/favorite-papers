##### Report GitHub Issue

Content selection saved. Describe the issue below:

# On-Policy RL Meets Off-Policy Experts: Harmonizing Supervised Fine-Tuning and Reinforcement Learning via Dynamic Weighting Thanks: Corresponding author. Email to {zwh434786, yaliang.li}@alibaba-inc.com

###### Abstract

Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) are two prominent post-training paradigms for refining the capabilities and aligning the behavior of Large Language Models (LLMs). Existing approaches that integrate SFT and RL often face the risk of disrupting established response patterns and inducing overfitting to expert data. To address this, we present a novel investigation into the unified view of SFT and RL through an off-policy versus on-policy lens. We propose Chord , a framework for C ontrollable H armonization of O n- and Off-Policy R einforcement Learning via D ynamic Weighting, which reframes SFT not as a separate stage but as a dynamically weighted auxiliary objective within the on-policy RL process. Based on an analysis of off-policy expert data’s influence at both holistic and granular levels, we incorporate a dual-control mechanism in Chord . Specifically, the framework first employs a global coefficient to holistically guide the transition from off-policy imitation to on-policy exploration, and then applies a token-wise weighting function that enables granular learning from the expert, which promotes on-policy exploration and mitigates disruption from off-policy data. We conduct extensive experiments across various practical tasks, providing empirical evidence that Chord achieves a stable and efficient learning process. By effectively harmonizing off-policy expert data with on-policy exploration, Chord demonstrates significant improvements over baselines. We release the implementation to inspire further research.

## 1 Introduction

Large Language Models (LLMs) have demonstrated remarkable capabilities in a wide array of applications ( Yang et al., 2024b ; Zhang et al., 2025a ; Mialon et al., 2023 ; Gao et al., 2024 ) . Such significant progress can be largely attributed to two critical post-tuning paradigms that enhance the performance of LLMs in real-world scenarios, i.e., Supervised Fine-Tuning (SFT) ( Taori et al., 2023 ; Zhou et al., 2023 ) and Reinforcement Learning (RL) ( Ouyang et al., 2022 ; Shao et al., 2024 ) .

These two paradigms present their pros and cons. SFT relies on high-quality expert trajectories to effectively mimic response patterns, which can be sensitive to the quality and quantity of expert data ( Ye et al., 2025 ; Guha et al., 2025 ) . Recent studies also point out that SFT may struggle to generalize beyond mere memorization ( Chu et al., 2025 ) and is vulnerable to exposure bias ( Zhang et al., 2019 ) . In contrast, RL encourages LLMs to actively explore, which enables better generalization through learning from direct feedback on their on-policy generations ( Chu et al., 2025 ; Chen et al., 2025b ) . However, such explorations can sometimes be inefficient, leading to policy degradation caused by entropy collapse ( Yu et al., 2025 ) or over-exploitation of suboptimal strategies.

A prevalent and straightforward approach for integrating the strengths of SFT and RL while mitigating their weaknesses is the sequential SFT-then-RL paradigm ( Liu et al., 2025b ; Lambert et al., 2024 ) . Intuitively, the expert’s reasoning patterns learned in SFT guide the RL exploration beyond local optima, and then the on-policy learning in RL mitigates exposure bias inherent in SFT and prevents overfitting to a limited set of static examples. However, empirical observations show that the SFT-then-RL paradigm does not consistently outperform the pure RL approach, as illustrated in Figure 2 , which is also noted in recent studies ( Zhang et al., 2025a ; Chen et al., 2025b ) .

In this study, we make a further investigation and demonstrate that such suboptimal performance may arise from training on expert data that significantly diverges from the model’s established patterns. As illustrated in Figure 2 , the learning curve reveals a “shift-readapt-overfit” progression consisting of three distinct phases. Firstly, there is an initial disruption in capability due to the sudden policy shift, which is followed by a readaptation phase during which the model adapts to the expert’s patterns and recovers performance. Finally, we observe that the model eventually overfits the expert data. These observations highlight that while expert data can bring new capabilities, it may also disrupt established patterns and induce overfitting during the training process .

Drawing upon these insights, we unify SFT and RL through the lens of off-policy versus on-policy learning. The SFT process is reframed not as a separate tuning stage, but as a dynamically weighted auxiliary objective within the on-policy RL process. We further design Chord , a framework for C ontrollable H armonization of O n- and Off-Policy R einforcement Learning via D ynamic Weighting. Chord features a global coefficient μ \mu for controlling the overall influence of expert data throughout the training process, and a fine-grained weighting function ϕ ⁡ ( ⋅ ) \phi(\cdot) that helps maintain stability via down-weighting highly divergent tokens from off-policy data that could disrupt on-policy training.

Our contributions can be summarized as follows:

• We provide a systematic and in-depth analysis of the training dynamics when employing a separate SFT process to integrate off-policy expert knowledge into models with established policies. We identify the “shift-readapt-overfit” progression, revealing how off-policy data can disrupt the established response patterns of LLMs.

• We propose Chord , a novel framework that unifies SFT and RL via a dynamically weighted auxiliary loss, which consists of a global coefficient μ \mu and a token-wise weighting function ϕ ⁡ ( ⋅ ) \phi(\cdot) . Chord provides a fine-grained and flexible control of the influence of off-policy expert data while ensuring training stability, promoting a harmonious integration of learning from both off-policy expert demonstrations and the model’s on-policy exploration.

• Extensive experiments demonstrate that Chord outperforms the SFT-then-RL paradigm and existing approaches. We provide both quantitative and qualitative analyses to show that Chord strategically navigates training dynamics to selectively absorb expert knowledge without stifling the model’s reasoning capabilities, highlighting its superiority and effectiveness.

## 2 Preliminaries

The post-tuning of Large Language Models (LLMs) involves optimizing their policy, denoted by π θ \pi_{\theta} and parameterized by θ \theta , to generate desirable responses. This typically follows two paradigms: Supervised Fine-Tuning (SFT), an off-policy paradigm driven by a static dataset of expert demonstrations; and Reinforcement Learning (RL), an on-policy paradigm guided by dynamic feedback.

Specifically, SFT adjusts the policy π θ \pi_{\theta} to mimic a high-quality, static dataset of N N expert demonstrations, 𝒟 SFT = { ( x i , y i ∗ ) } i = 1 N \mathcal{D}_{\text{SFT}}=\{(x_{i},y^{*}_{i})\}_{i=1}^{N} . Here, x i x_{i} is a prompt and y i ∗ = ( y i , 1 ∗ , … , y i , | y i ∗ | ∗ ) y^{*}_{i}=(y^{*}_{i,1},\dots,y^{*}_{i,|y_{i}^{*}|}) is the corresponding expert response with | y i ∗ | |y_{i}^{*}| tokens. The SFT objective is to minimize the negative log-likelihood of expert responses, typically optimized with an empirical estimate from a mini-batch of size B B : ℒ SFT ( θ ) = − 1 ∑ i = 1 B | y i ∗ | ∑ i = 1 B ∑ t = 1 | y i ∗ | log π θ ( y i , t ∗ | x i , y i , < t ∗ ) . \mathcal{L}_{\text{SFT}}(\theta)=-\frac{1}{\sum_{i=1}^{B}|y_{i}^{*}|}\sum_{i=1}^{B}\sum_{t=1}^{|y_{i}^{*}|}\log\pi_{\theta}(y^{*}_{i,t}|x_{i},y^{*}_{i,<t}). (1)

In contrast, RL optimizes policy π θ \pi_{\theta} by maximizing expected reward R ⁡ ( τ ) R(\tau) from a generated trajectory τ = ( x , y ∗ ) \tau=(x,y^{*}) . Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) suggests sampling K K responses { τ 1 , … , τ K } \{\tau_{1},\dots,\tau_{K}\} from a policy π sample \pi_{\text{sample}} when given a prompt x x . Each response τ k \tau_{k} is evaluated with the reward function R ⁡ ( τ k ) R(\tau_{k}) , and π θ \pi_{\theta} is updated to maximize a PPO-style clipped surrogate objective. Consistent with recent studies ( Hu et al., 2025a ; Yu et al., 2025 ; Chen et al., 2025a ) , our formulation does not include the KL divergence term to avoid restricting performance of LLMs. The objective function can be formulated as: ℒ GRPO ( θ ) = − 1 ∑ i = 1 B ^ ∑ k = 1 K | τ i , k | ∑ i = 1 B ^ ∑ k = 1 K ∑ t = 1 | τ i , k | min ( r i , k , t ( θ ) A i , k , clip ( r i , k , t ( θ ) , 1 − ϵ , 1 + ϵ ) A i , k ) , \mathcal{L}_{\text{GRPO}}(\theta)=-\frac{1}{\sum_{i=1}^{\hat{B}}\sum_{k=1}^{K}|\tau_{i,k}|}\sum_{i=1}^{\hat{B}}\sum_{k=1}^{K}\sum_{t=1}^{|\tau_{i,k}|}\min\left(r_{i,k,t}(\theta)A_{i,k},\,\text{clip}(r_{i,k,t}(\theta),1-\epsilon,1+\epsilon)A_{i,k}\right), (2)

where B ^ \hat{B} is the number of prompts in the mini-batch and ϵ \epsilon is the clipping hyper-parameter. The advantage A k A_{k} for each response is computed by A k = R ⁡ ( τ k ) − μ ℛ σ ℛ + ϵ z A_{k}=\frac{R(\tau_{k})-\mu_{\mathcal{R}}}{\sigma_{\mathcal{R}}+\epsilon_{z}} , where μ ℛ \mu_{\mathcal{R}} and σ ℛ \sigma_{\mathcal{R}} are the mean and standard deviation of rewards { R ⁡ ( τ k ) } k = 1 K \{R(\tau_{k})\}_{k=1}^{K} within the group, and ϵ z \epsilon_{z} is a small constant for stability. Here r i , k , t ​ ( θ ) ≜ π θ ​ ( τ i , k , t | x , τ i , k , < t ) π sample ​ ( τ i , k , t | x , τ i , k , < t ) r_{i,k,t}(\theta)\triangleq\frac{\pi_{\theta}(\tau_{i,k,t}|x,\tau_{i,k,<t})}{\pi_{\text{sample}}(\tau_{i,k,t}|x,\tau_{i,k,<t})} denotes the token-wise Importance Sampling (IS) ratio, which re-weights the probability of actions sampled under π sample \pi_{\text{sample}} to simulate on-policy sampled distribution. For a “strict on-policy setup” ( Liu et al., 2025b ) that π sample = π θ \pi_{\text{sample}}=\pi_{\theta} , this ratio should always be 1 1 , and the gradient of r i , k , t ​ ( θ ) r_{i,k,t}(\theta) should be equivalent to ∇ θ ​ log ​ π θ ​ ( τ i , k , t ∗ | x i , τ i , k , < t ∗ ) \nabla_{\theta}\log\pi_{\theta}(\tau^{*}_{i,k,t}|x_{i},\tau^{*}_{i,k,<t}) .

## 3 Chord : Harmonizing Off-Policy and On-Policy Learning

### 3.1 The Shift-Readapt-Overfit Progression When Utilizing Off-Policy Data

Before introducing Chord , we first take a close look at the training dynamics of the SFT process, revealing how training on off-policy expert data can disrupt the established response patterns of LLMs. Such disruption ultimately leads to the failure of the SFT-then-RL paradigm ( Zhang et al., 2025a ; Chen et al., 2025b ) , as evidenced by the results in Figure 2 .

We train Qwen2.5-7B-Instruct ( Yang et al., 2024a ) on expert data generated by Deepseek-R1 ( Guo et al., 2025 ) and monitor the changes in test accuracy on the MATH-500 dataset. From the experimental results shown in Figure 2 , we observe that model performance declines during the first few epochs, followed by a continuous increase to a level higher than that before training, and then a slight subsequent decrease. The performance curve reveals a “shift-readapt-overfit” progression: • Policy Shift : The performance initially declines since the model is forced to follow off-policy expert demonstrations whose response patterns are significantly different, disrupting its established response patterns and causing a significant performance drop . Such degradation is further exacerbated by exposure bias ( Zhang et al., 2019 ; Schmidt, 2019 ) , as the model, trained exclusively on ground-truth expert data, struggles to navigate the self-generated contexts it encounters during inference.

• Readapt : As SFT continues, the model policy π θ \pi_{\theta} begins to integrate the expert’s response patterns and generates responses similar to those of the expert. The exposure bias can be mitigated by reducing the reliance on the model’s response patterns, thereby allowing its performance to rise steadily as it adapts to the expert’s response patterns.

• Overfit : Extended training on the limited expert data ultimately leads to overfitting, resulting in a decline in generalization and a significant loss of output diversity. Such overfitting can also restrict the exploratory capacity that is crucial for the following RL optimization.

The observed progression makes it challenging to control the influence of off-policy expert data. The SFT-then-RL paradigm demands careful timing for the SFT-to-RL transition, and even then, such a two-stage paradigm may still yield suboptimal solutions due to the inherent separation of the training phases. This highlights the limitations and fragility of the SFT-then-RL paradigm, especially when expert data’s response patterns significantly diverge from the model’s established response patterns.

Drawing upon the above insights, we propose Chord , a novel framework that effectively unifies SFT and RL. The proposed framework consists of a dual-control mechanism. We first introduce a dynamic loss coefficient to balance learning from on- and off-policy data (refer to Section 3.2 ), then further design a token-wise weighting function that provides fine-grained stability control (refer to Section 3.3 ). The overall architecture of Chord is shown in Figure 3 .

### 3.2 Controlling the Influence of Off-Policy Expert Data via μ \mu

Firstly, in order to control the influence of off-policy expert data, we propose to reframe SFT as a dynamically weighted auxiliary objective within the on-policy RL process, rather than a separate tuning stage as in the SFT-then-RL paradigm. Specifically, we design a combined loss function that minimizes a weighted sum of the RL and SFT losses: ℒ Hybrid ​ ( θ ) = ( 1 − μ ) ​ ℒ GRPO ​ ( θ ) + μ ​ ℒ SFT ​ ( θ ) , \mathcal{L}_{\text{Hybrid}}(\theta)=(1-\mu)\mathcal{L}_{\text{GRPO}}(\theta)+\mu\mathcal{L}_{\text{SFT}}(\theta), (3) where ℒ GRPO ​ ( θ ) \mathcal{L}_{\text{GRPO}}(\theta) is the empirical GRPO loss defined in equation 2 , ℒ SFT ​ ( θ ) \mathcal{L}_{\text{SFT}}(\theta) is the SFT loss defined in equation 1 , and μ ∈ [ 0 , 1 ] \mu\in[0,1] is a hyperparameter that governs the trade-off between SFT and RL.

If using a fixed value of μ \mu , the influence of the off-policy expert data remains unchanged throughout the entire post-tuning process. An advanced strategy, however, is to change μ \mu for achieving a dynamic balance between off-policy and on-policy learning. For example, the SFT-then-RL pipeline can be regarded as a special case with a binary schedule (initially setting μ = 1 \mu=1 and then transitioning to μ = 0 \mu=0 ). Moreover, previous studies ( Ma et al., 2025 ; Gao et al., 2025 ) that utilize interleaved SFT and RL can be interpreted as employing a periodic μ \mu schedule.

Moving a step forward, applying a decay schedule of μ \mu provides a more graceful and flexible transition from off-policy imitation to on-policy optimization compared to the rigid and binary switch. As shown in Figure 5 , the training begins with a large μ \mu value, encouraging the model to learn more from off-policy expert data. As training progresses, μ \mu gradually decays to a smaller value, shifting the training focus towards on-policy exploration and annealing the influence of the off-policy expert data before overfitting on them. Such a decay schedule has also proven successful in mitigating exposure bias ( Zhang et al., 2019 ) . Inspired by scheduled sampling ( Bengio et al., 2015 ) , we generalize the principle of mixing expert and self-generated data from the token level to the loss formulation, effectively bridging the distributional gap between training on off-policy samples and performing on-policy rollouts.

Beyond the Loss Coefficient μ \mu Empirical comparisons (refer to Section 4 for more details) demonstrate that applying a decay schedule to μ \mu yields notable performance gains over the SFT-then-RL paradigm. At the same time, two key observations motivate us to extend beyond μ \mu .

Firstly, as shown in Figure 5 , the learning curve still reveals a “shift-readapt” progress, where the reward initially declines before subsequently increasing. These observations indicate that, despite improvements in performance, learning from off-policy expert data might still disrupt established patterns and stifle the model’s capacity for genuine exploration during on-policy training.

Secondly, the response patterns of the model trained with Chord - μ \mu (as shown in Appendix E ) appear to converge to those of the expert model. Case studies reveal that Chord - μ \mu compels the model to adopt the expert’s verbose response pattern wholesale, hence overwriting its own inherent conciseness. This indicates that while μ \mu controls the overall influence of expert data, it lacks fine-grained precision. As a result, it forces the model to indiscriminately adopt expert patterns, which can create conflicts with its own established style.

Towards the goal of utilizing off-policy data as an incentive and guidance for the model to explore novel and effective reasoning paths, rather than merely as a target to imitate, we further integrate Chord with a token-wise, fine-grained weighting function ϕ ⁡ ( ⋅ ) \phi(\cdot) , forming a dual-control mechanism together with the global coefficient μ \mu for controlling the influence of the off-policy expert data.

### 3.3 Enhancing the Stability of Off-policy Learning via ϕ ⁡ ( ⋅ ) \phi(\cdot)

A feasible solution for controlling the influence of off-policy expert data from a fine-grained perspective is to differentiate the tokens based on their generation probabilities π ⁡ ( y t ∗ | x , y < t ∗ ) \pi(y^{*}_{t}|x,y^{*}_{<t}) . For example, Importance Sampling (IS) ( Schulman et al., 2017 ) has been widely used for stably integrating off-policy data in RL, which suggests re-weighting the objective by the probability ratio between the target policy π θ \pi_{\theta} and the behavior policy π sample \pi_{\text{sample}} that generated the expert data. Formally, the objective function can be given as: ℒ SFT-IS ( θ ) = 𝔼 ( x , y ∗ ) ∼ 𝒟 SFT [ − ∑ t = 1 | y ∗ | sg ( π θ ​ ( y t ∗ | x , y < t ∗ ) π sample ​ ( y t ∗ | x , y < t ∗ ) ) ⋅ log π θ ( y t ∗ | x , y < t ∗ ) ] , \mathcal{L}_{\text{SFT-IS}}(\theta)=\mathbb{E}_{(x,y^{*})\sim\mathcal{D}_{\text{SFT}}}\left[-\sum_{t=1}^{|y^{*}|}\text{sg}\left(\frac{\pi_{\theta}(y^{*}_{t}|x,y^{*}_{<t})}{\pi_{\text{sample}}(y^{*}_{t}|x,y^{*}_{<t})}\right)\cdot\log\pi_{\theta}(y^{*}_{t}|x,y^{*}_{<t})\right], (4) where sg ​ ( ⋅ ) \text{sg}(\cdot) denotes the stop-gradient operator. Note that the probabilities π sample ​ ( y t ∗ | … ) \pi_{\text{sample}}(y^{*}_{t}|\dots) for the expert data 𝒟 SFT \mathcal{D}_{\text{SFT}} are often unknown. Following the common practice ( Yan et al., 2025 ; Wu et al., 2025 ) , we assume that the denominator is 1 1 , treating the expert data as the ground-truth distribution.

From a token-wise perspective, IS enhances training stability by down-weighting low-probability tokens that could disrupt the established policy. As empirical observations shown in Figure 5 , mixing off-policy data without IS leads to a sharp rise in entropy, which implies that the model’s established patterns are quickly disrupted by the unweighted off-policy data. However, we notice that IS can lead to a sharp collapse in policy entropy compared to pure RL, which implies that it can limit the exploration essential for the RL phase and trap the model in a stable but suboptimal solution. The underlying reason is that IS prevents disruptive shifts in the policy distribution by down-weighting low-probability tokens, but it also aggressively reinforces existing high-probability tokens while ignoring novel but low-probability ones, thus causing the policy to become overconfident.

Stabilize Off-policy Data Training with ϕ ⁡ ( ⋅ ) \phi(\cdot) To tackle this, we propose a fine-grained, per-token weighting function ϕ ⁡ ( y t ∗ , π θ ) \phi(y^{*}_{t};\pi_{\theta}) that down-weights the learning signal for tokens at both ends of the probability spectrum , i.e., down-weighting those tokens that are highly probable (to prevent entropy collapse) or extremely improbable (to avoid disruption). More specifically, the weight for a given expert token is defined based on the policy’s probability p t = π θ ​ ( y t ∗ | x , y < t ∗ ) p_{t}=\pi_{\theta}(y^{*}_{t}|x,y^{*}_{<t}) , as follows: ϕ ⁡ ( y t ∗ , π θ ) = p t ​ ( 1 − p t ) , \phi(y^{*}_{t};\pi_{\theta})=p_{t}(1-p_{t}), (5) which naturally forms a parabolic curve that peaks at p t = 0.5 p_{t}=0.5 and decays to zero as p t p_{t} approaches 0 or 1. The SFT objective function can be updated as: ℒ SFT- ​ ϕ ​ ( θ ) = − 𝔼 ( x , y ∗ ) ∼ 𝒟 SFT ​ [ ∑ t = 1 | y ∗ | ϕ ⁡ ( y t ∗ , π θ ) ⋅ log ⁡ π θ ​ ( y t ∗ | x , y < t ∗ ) ] , \mathcal{L}_{\text{SFT-}{\phi}}(\theta)=-\mathbb{E}_{(x,y^{*})\sim\mathcal{D}_{\text{SFT}}}\left[\sum_{t=1}^{|y^{*}|}\phi(y^{*}_{t};\pi_{\theta})\cdot\log\pi_{\theta}(y^{*}_{t}|x,y^{*}_{<t})\right], (6) where ϕ ⁡ ( y t ∗ , π θ ) \phi(y^{*}_{t};\pi_{\theta}) modulates the gradient contribution of each token in the expert trajectory.

From an information-theoretic perspective, the term p t ​ ( 1 − p t ) p_{t}(1-p_{t}) can be viewed as a measure of the policy’s uncertainty ( Wang et al., 2025 ) for the binary event of generating token y t ∗ y^{*}_{t} . Therefore, this approach biases learning towards tokens where the policy is most uncertain, and creates a “learning sweet spot” that focuses the off-policy learning on tokens that are novel enough to be informative but not so divergent as to disrupt the established policy.

By replacing the static ℒ SFT \mathcal{L}_{\text{SFT}} in the proposed hybrid loss function (defined in equation 3 ) with ℒ SFT- ϕ \mathcal{L}_{\text{SFT-$\phi$}} , we obtain the final objective function of Chord , which applies a global coefficient μ \mu for adjusting the overall influence of expert data and a fine-grained weighting function ϕ ⁡ ( ⋅ ) \phi(\cdot) that helps enhance the stability when learning from off-policy data.

## 4 Experiments

### 4.1 Setup

Datasets, Models, and Evaluations We conduct experiments on mathematical reasoning problems and practical tool-use tasks. (i) For mathematical reasoning problems , we utilize the OpenR1-Math-220k dataset ( Hugging Face, 2025 ) , from which we sample 5k instances for SFT and 20k for RL, ensuring no overlap. Our policy model is Qwen2.5-7B-Instruct, whose response patterns differ significantly from the expert (Deepseek-R1). We evaluate in-domain generalization performance on the AIME24, AIME25, and AMC benchmarks ( Li et al., 2024 ) , and use MMLU-Pro ( Wang et al., 2024 ) to monitor the changes in general reasoning. (ii) For tool-use tasks , we conduct experiments on the single-turn instances of the ToolAce ( Liu et al., 2024 ) dataset. We sample 5k instances for RL and 500 for SFT, for which the expert trajectories are generated by querying the Deepseek-R1 with the same system prompt. We use LLaMA3.2-3B-Instruct ( Grattafiori et al., 2024 ) as our policy model, which also differs in response patterns from the expert (Deepseek-R1). We evaluate the model performance on BFCL ( Patil et al., 2024 ) .

Baselines We compare the proposed Chord with a comprehensive set of baselines, including: (i) Original Model : The original Qwen2.5-7B-Instruct/LLaMA3.2-3B-Instruct model. (ii) SFT-only : The model fine-tuned on the SFT dataset. We focus on two specific configurations: SFT-light , trained for a single epoch, and SFT-best , the peak-performing checkpoint on the test set found by searching over different learning rates and training epochs. (iii) RL-only : The model fine-tuned directly on the RL dataset using the GRPO algorithm. (iv) SFT+RL : The sequential SFT-then-RL paradigm. (v) LUFFY 1 1 1 For math reasoning problems, we utilize 20k samples for training, whereas the original paper utilizes 45k samples and achieves scores of 50.9 on AMC, 17.7 on AIME24, and 14.8 on AIME25. For tool-use tasks, LUFFY utilizes 5k SFT samples instead of 500. ( Yan et al., 2025 ) : A method that integrates expert demonstrations within GRPO rollout groups and reshapes the importance sampling ratio. (vi) SASR ( Chen et al., 2025c ) : A method that probabilistically interleaves SFT and RL steps. It prioritizes SFT when the model’s outputs are dissimilar to expert demonstrations, adapting the training focus dynamically.

For more details of the experimental setups, please refer to Appendix A .

### 4.2 Comparisons

The proposed approaches implemented based on Chord include (i) Chord - μ \mu : We employ a decay schedule for the loss coefficient μ \mu to gradually transition from off-policy to on-policy learning, as detailed in Section 3.2 ; and (ii) Chord - ϕ \phi : We fix the value of μ \mu and further integrate the token-wise weighting function ϕ ⁡ ( ⋅ ) \phi(\cdot) to achieve a dual-control mechanism on the influence of off-policy expert data, as introduced in Section 3.3 .

Model Performance Overall, the comparisons summarized in Table 1 demonstrate the effectiveness and superiority of Chord on both reasoning problems and tool-use tasks.

Specifically, the experimental results reveal a challenge within the SFT-then-RL paradigm. We notice that minimal tuning on off-policy data (SFT-light) degrades performance, and a more thorough SFT phase (SFT-best) achieves better results. However, the optimal timing for transitioning from SFT to RL can vary across different scenarios. For example, initiating RL from SFT-best yields superior performance on math reasoning problems, while SFT-light+RL performs better on tool-use tasks. This divergence confirms that the SFT-RL balance is highly task-dependent and needs extensive efforts for careful adjustment.

These SFT-then-RL approaches are surpassed by Chord - μ \mu , which enables a smooth transition from off-policy to on-policy learning rather than a rigid switch. Specifically, Chord - μ \mu outperforms the strong SFT-best+RL baseline across all math reasoning benchmarks, achieving improvements of +2.4 on AMC, +1.0 on AIME24, and +1.6 on AIME25, respectively. Besides, Chord - μ \mu also achieves better overall results compared to these SFT-then-RL baselines on tool-use tasks. These results demonstrate the superiority of its unified learning design.

Further, Chord - ϕ \phi achieves consistent outperformance over the baselines. These results demonstrate the effectiveness of our dual-control mechanism in flexibly controlling the influence of off-policy expert data. Chord - ϕ \phi selectively applies the SFT loss to non-disruptive tokens, integrating expert knowledge without compromising foundational abilities. This enables robust learning from both off-policy expert data and on-policy exploration, leading to the best performance on both reasoning problems and tool-use tasks.

Response Patterns We further compare the influence of expert data (generated by DeepSeek-R1) on response patterns across different approaches. As shown in Table 2 , expert responses are substantially longer than the original model’s on both math (6,132 vs. 659 tokens) and tool-use tasks (315 vs. 147 tokens). SFT models (SFT-light and SFT-best) initially mimic this verbosity. However, a subsequent RL can help mitigate the issues of overly lengthy responses by training the models to conduct on-policy exploration. The response length produced by SFT-light+RL is much shorter than that of SFT-best+RL (1,322/119 vs. 4,830/489 tokens), as fewer epochs of SFT allow the model to retain its original response patterns. Besides, from Figure 6 , we can observe that Chord - μ \mu exhibits a similar trend, where the average response length initially increases to align with expert patterns and then gradually converges to a lower length as on-policy training progresses.

On the other hand, Pure RL on instruct-tuned models lengthens math responses (from 659 to 1,423 tokens) while shortening them for tool-use (from 147 to 118 tokens). This suggests that the response pattern changes can be task-dependent: math problems benefit from detailed step-by-step reasoning, whereas tool-use tasks favor shorter, concise action sequences. Such task-dependent property also affects the SFT/RL synergy dynamics, as MATH tasks benefit from imitating an expert’s long and verbose reasoning via SFT, while such patterns can be detrimental to tool-use performance, a distinction further detailed in Appendix D.2 . The result shows that the proposed Chord - ϕ \phi strikes a more nuanced balance: while it also learns to produce more comprehensive mathematical reasoning (2,444 tokens), it generates concise and efficient responses for tool-use tasks (120 tokens). This suggests that the token-wise weighting in Chord - ϕ \phi enables the model to selectively integrate patterns from those of expert data in a task-specific manner. Qualitative analysis shown in Appendix E also confirms the effectiveness of such a flexible design, suggesting that the proposed Chord - ϕ \phi can go beyond simply mimicking the expert, and learn to selectively absorb reasoning patterns from the expert, while exploring its own response strategies .

### 4.3 Analysis on the Effects of μ \mu and ϕ ⁡ ( ⋅ ) \phi(\cdot)

We provide analysis on the effects of the coefficient μ \mu and the token-wise weighting function ϕ ⁡ ( ⋅ ) \phi(\cdot) .

Dynamic μ \mu Versus Fixed μ \mu In Figure 9 , we compare the model performance when applying a dynamic schedule for μ \mu (decreasing from 0.9 to 0.05 over the first 200 training steps and keeping unchanged in the following steps) against several fixed schedules in Chord . We observe that applying a fixed μ \mu consistently results in poorer performance compared to dynamic μ \mu . This indicates that naively incorporating off-policy SFT data with a static weight does not effectively serve as a solution for simultaneously learning from off-policy data and on-policy exploration. In fact, it might fail to match Pure RL, which directly encourages an instruction model to follow its own reasoning patterns, highlighting the importance and necessity of controlling the influence of off-policy data.

Besides, while using a smaller value of μ \mu (e.g., 0.02) can mitigate the performance degradation compared to larger values (e.g., 0.1 and 0.5), it does not provide a significant improvement over pure on-policy RL. With a fixed μ \mu , the model is consistently required to accommodate two potentially divergent reasoning patterns, which might pull it in different directions and prevent it from converging to a stable and high-performance state. The decay schedule for μ \mu effectively resolves this conflict by creating a smooth transition from off-policy supervision to on-policy exploration.

We also explore a natural extension to adaptively adjust the loss weight μ \mu based on on-policy rewards. Specifically, the weight is computed as μ = max ⁡ ( 0 , τ − reward_mean ) \mu=\max(0,\tau-\text{reward\_mean}) , which phases out the SFT loss on the expert data as performance improves. The experiment results in Appendix B.1 imply that an automated, reward-aware schedule for μ \mu can work effectively but requires heavy hyper-parameter tuning, which further motivates the need for fine-grained control.

Training Curve of Chord - ϕ \phi In Figures 9 and 9 , we compare the entropy loss and rewards of Pure RL with those of Chord - ϕ \phi (with fixed μ = 0.1 \mu=0.1 ), to illustrate their training dynamics.

From the changes in entropy loss, we can observe that by applying ϕ ⁡ ( ⋅ ) \phi(\cdot) , the model maintains a great balance between exploration and exploitation while performing off-policy and on-policy learning simultaneously. On one hand, Chord - ϕ \phi prevents the entropy from collapsing prematurely, which may occur when the SFT loss forces the model to become over-confident on high-probability tokens from the expert data. On the other hand, it avoids large entropy spikes and training instability that may occur if the off-policy expert data drastically conflict with the current policy’s predictions, as the performance curve remains stable throughout the training process. The rewards curve indicates that Chord - ϕ \phi achieves a stable and continuous increase in rewards, resulting in significantly better performance than Pure RL. These results demonstrate that the proposed token-wise weighting function is crucial for effectively unifying the SFT and RL phases.

Tuning μ \mu When Applying Chord - ϕ \phi Empirical observations show that, when ϕ ⁡ ( ⋅ ) \phi(\cdot) is used for fine-grained control over the influence of expert data, a complex and decaying schedule for μ \mu is no longer essential. Chord - ϕ \phi is effective to work with a fixed value for μ \mu (e.g., 0.1 in this study) since it inherently prevents both token-level overfitting and the disruption of established response patterns. The design of ϕ ⁡ ( ⋅ ) \phi(\cdot) simplifies the practical usage of Chord by making it robust to the specific choice of μ \mu . In Appendix B.7 , we provide experiments on tuning the schedule of μ \mu in conjunction with ϕ ⁡ ( ⋅ ) \phi(\cdot) .

Principle for Instantiating ϕ ⁡ ( ⋅ ) \phi(\cdot) It is worth noting that the proposed weight ϕ ⁡ ( ⋅ ) = p t ∗ ( 1 − p t ) \phi(\cdot)=p_{t}*(1-p_{t}) serves as a concrete and interpretable instantiation following a general principle: stabilizing off-policy integration requires down-weighting the learning signal for tokens at both ends of the probability spectrum. This instantiation is computationally efficient, requiring only element-wise multiplication of existing forward-pass probabilities. As grounded in our empirical observations, by assigning negligible weight to tokens that the policy is already certain about (where p t p_{t} is close to 0 or 1), the proposed method prevents off-policy data from disrupting the model’s established reasoning patterns and focuses updates on tokens where the model is still uncertain. Beyond the specific formulation of ϕ ⁡ ( ⋅ ) \phi(\cdot) , this general principle that enables stable and selective learning from off-policy data can potentially inspire more advanced weighting schemes that are suitable for different scenarios.

We also experiment with several variants of the token-weighting function (such as entropy-based variants, clipping variants, and focal loss), with detailed experiment results and discussions presented in Appendix B.2 . We acknowledge that this ϕ ⁡ ( ⋅ ) \phi(\cdot) token-wise weighting design primarily illustrates a generalizable principle. While it is unlikely that a single universally optimal design exists across all tasks, datasets, and models, our empirical results confirm that our design nonetheless serves as a highly effective and robust instantiation.

### 4.4 Further Analysis

Varying Expert Data Source We investigate the effect of using two different expert sources: the powerful DeepSeek-R1, and the weaker Qwen2.5-72B-Instruct, whose response pattern is closer to the LLaMA3.2-3B-Instruct policy model. Experimental results demonstrate that our proposed methods, Chord - μ \mu and Chord - ϕ \phi , outperform Pure RL and SFT+RL baselines regardless of the expert. We also observe that methods which rely more heavily on expert imitation (e.g., SFT+RL and Chord - μ \mu ) can yield greater gains when the expert is stylistically similar to the policy model. This aligns with our insight: the effectiveness of unifying SFT and RL depends not only on expert data quality but also on the degree of pattern shift it introduces. For detailed results and discussion, please refer to Appendix B.3 .

Extending to Non-verifiable Domains To test the generalizability of Chord beyond verifiable tasks, we conduct experiments on RaR-Medicine, a medical question-answering dataset that lacks deterministic verification. The results show that both Chord - μ \mu and Chord - ϕ \phi significantly outperform pure RL. Chord - ϕ \phi achieves faster convergence and higher final rewards, while Chord - μ \mu exhibits a similar “shift-readapt” pattern as observed in the main experiments (Figure 10 in Appendix B.4 ). These findings validate that our approach successfully generalizes to more diverse, non-verifiable domains. Refer to Appendix B.4 for more details.

Training Weaker Policy Models While the effectiveness of on-policy exploration (RL) is often limited for weaker models, our experiments reveal that their capability to absorb knowledge from expert data simultaneously degrades. Our experiment on Qwen2.5-3B-Instruct shows that due to this dual limitation, a weaker model tends more to suffer from a performance collapse when training on the same off-policy expert data. In such a setting, naive imitation fails and a simple SFT+RL combination proves unstable, whereas our Chord - ϕ \phi provides a robust objective to navigate this trade-off and maintain learning stability. We acknowledge that with larger quantities of higher-quality expert data, a weaker model might overcome this imitation bottleneck, potentially making SFT-leaning methods more favorable. Conversely, this also suggests that our method becomes particularly advantageous when dealing with weaker models under limited expert data, highlighting its strong capability to flexibly balance this trade-off and create a robust synergy between SFT and RL. We defer detailed experiment results and analysis to Appendix B.5 .

## 5 Related Works

Recent advancements in RL show significant success in complex reasoning tasks ( Guo et al., 2025 ; Shao et al., 2024 ; Lambert et al., 2024 ) . However, RL-based exploration is often constrained by the model’s initial knowledge, making it difficult for the model to discover superior reasoning pathways ( Yue et al., 2025 ) . Incorporating off-policy expert data into the on-policy RL loop is a promising strategy to address such exploration challenge. Some studies directly mix expert data with self-rollout generations, either through simple dataset mixing ( Li and Khashabi, 2025 ) , or mixing expert trajectories into on-policy rollout groups ( Yan et al., 2025 ; Fu et al., 2025 ) , while others use expert data to guide generation ( Liu et al., 2025a ; Zhang et al., 2025b ; Huang et al., 2025 ) . A third category interleaves RL updates with SFT steps on expert data, either on a predefined or adaptive schedule ( Chen et al., 2025c ) , or for challenging examples ( Ma et al., 2025 ) . More recently, SRFT ( Fu et al., 2025 ) proposed a unified framework that combines data mixing with a sample-level SFT loss. In this study, we focus on tuning an instruct model that already establishes its own response pattern, which can be a more challenging yet practical scenario compared to existing works that finetune a base model ( Yan et al., 2025 ; Fu et al., 2025 ) . For a more comprehensive literature review, please refer to Appendix C .

## 6 Conclusions and future directions

In this study, we identify that the sequential SFT-then-RL paradigm often yields suboptimal performance by disrupting established patterns with off-policy expert data. To address this, we unify SFT and RL through the lens of on-policy versus off-policy learning and propose Chord . By analyzing the influence of expert data at both the holistic and granular levels, Chord first integrates a global coefficient μ \mu to manage off-policy expert influence, enabling a smoother transition from imitation to exploration. Chord then introduces a token-wise function ϕ ⁡ ( ⋅ ) \phi(\cdot) to selectively absorb expert knowledge by down-weighting tokens that are either already highly probable or extremely improbable. Extensive experiments demonstrate that this unified approach achieves notable improvements over existing sequential pipelines and various baselines.

Looking forward, our work highlights several avenues for future research. First, given the inherent high variance and parameter sensitivity typical of RL processes, exploring further algorithmic advancements to fully stabilize the training dynamics represents a promising direction. Specifically within our framework, since configurations for μ \mu and ϕ ⁡ ( ⋅ ) \phi(\cdot) can vary across setups, discovering more effective adaptive tuning functions to reduce hyperparameter dependence remains a practical objective. Furthermore, while our analysis of pattern shifts is primarily empirical, a deeper understanding of how diverse CoT patterns influence learning would provide valuable insights for tracking training dynamics. Finally, we envision extending this unified paradigm to incorporate heterogeneous mixtures of expert data sources, enabling a comprehensive study of how different model-generated reasoning patterns emerge and evolve throughout the training process. We hope our work inspires the community to continue refining unified post-training paradigms across a broader spectrum of applications.

## Acknowledgements

We would like to thank Qi Liu, Zexi Li, and Ao Li for their suggestions. We also thank the anonymous reviewers and Area Chairs for their constructive feedback during the review process.

## Reproducibility Statement

We release our implementation to inspire further research.

## References

Arnal et al. (2025) C. Arnal, G. Narozniak, V. Cabannes, Y. Tang, J. Kempe, and R. Munos Asymmetric reinforce for off-policy reinforcement learning: balancing positive and negative rewards . arXiv preprint arXiv:2506.20520 . Cited by: §C.2 .

Bai et al. (2022) Y. Bai, A. Jones, K. Ndousse, A. Askell, A. Chen, N. DasSarma, D. Drain, S. Fort, D. Ganguli, T. Henighan, et al. Training a helpful and harmless assistant with reinforcement learning from human feedback . arXiv preprint arXiv:2204.05862 . Cited by: §C.1 .

Ball et al. (2023) P. J. Ball, L. Smith, I. Kostrikov, and S. Levine Efficient online reinforcement learning with offline data . In International Conference on Machine Learning , pp. 1577–1594 . Cited by: §C.2 .

Bengio et al. (2015) S. Bengio, O. Vinyals, N. Jaitly, and N. Shazeer Scheduled sampling for sequence prediction with recurrent neural networks . Advances in neural information processing systems 28 . Cited by: §3.2 .

Chen et al. (2025a) A. Chen, A. Li, B. Gong, B. Jiang, B. Fei, B. Yang, B. Shan, C. Yu, C. Wang, C. Zhu, et al. MiniMax-m1: scaling test-time compute efficiently with lightning attention . arXiv preprint arXiv:2506.13585 . Cited by: §2 .

Chen et al. (2025b) H. Chen, H. Tu, F. Wang, H. Liu, X. Tang, X. Du, Y. Zhou, and C. Xie Sft or rl? an early investigation into training r1-like reasoning large vision-language models . arXiv preprint arXiv:2504.11468 . Cited by: §1 , §1 , §3.1 .

Chen et al. (2025c) J. Chen, F. Liu, N. Liu, Y. Luo, E. Qin, H. Zheng, T. Dong, H. Zhu, Y. Meng, and X. Wang Step-wise adaptive integration of supervised fine-tuning and reinforcement learning for task-specific llms . arXiv preprint arXiv:2505.13026 . Cited by: §C.2 , §4.1 , §5 .

Chen et al. (2025d) J. Chen, Z. Cai, K. Ji, X. Wang, W. Liu, R. Wang, and B. Wang Towards medical complex reasoning with LLMs through medical verifiable problems . In Findings of the Association for Computational Linguistics: ACL 2025 , W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.) , Vienna, Austria . Cited by: §B.4 .

Chu et al. (2025) T. Chu, Y. Zhai, J. Yang, S. Tong, S. Xie, D. Schuurmans, Q. V. Le, S. Levine, and Y. Ma SFT memorizes, rl generalizes: a comparative study of foundation model post-training . In Forty-second International Conference on Machine Learning , Cited by: §1 .

Dong et al. (2025) Y. Dong, X. Jiang, Y. Tao, H. Liu, K. Zhang, L. Mou, R. Cao, Y. Ma, J. Chen, B. Li, et al. Rl-plus: countering capability boundary collapse of llms in reinforcement learning with hybrid-policy optimization . arXiv preprint arXiv:2508.00222 . Cited by: §C.2 .

Fu et al. (2025) Y. Fu, T. Chen, J. Chai, X. Wang, S. Tu, G. Yin, W. Lin, Q. Zhang, Y. Zhu, and D. Zhao SRFT: a single-stage method with supervised and reinforcement fine-tuning for reasoning . arXiv preprint arXiv:2506.19767 . Cited by: §C.2 , §C.2 , §D.1 , §D.1 , §5 .

Gao et al. (2024) D. Gao, Z. Li, X. Pan, W. Kuang, Z. Ma, B. Qian, F. Wei, W. Zhang, Y. Xie, D. Chen, et al. Agentscope: a flexible yet robust multi-agent platform . arXiv preprint arXiv:2402.14034 . Cited by: §1 .

Gao et al. (2025) D. Gao, H. Wang, H. Zhou, N. Ammar, S. Mishra, A. Moradipari, I. Soltani, and J. Zhang IN-ril: interleaved reinforcement and imitation learning for policy fine-tuning . arXiv preprint arXiv:2505.10442 . Cited by: §C.2 , §3.2 .

Grattafiori et al. (2024) A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Vaughan, et al. The llama 3 herd of models . arXiv preprint arXiv:2407.21783 . Cited by: §C.1 , §4.1 .

Guha et al. (2025) E. Guha, R. Marten, S. Keh, N. Raoof, G. Smyrnis, H. Bansal, M. Nezhurina, J. Mercat, T. Vu, Z. Sprague, et al. OpenThoughts: data recipes for reasoning models . arXiv preprint arXiv:2506.04178 . Cited by: §C.1 , §1 .

Gunjal et al. (2025) A. Gunjal, A. Wang, E. Lau, V. Nath, Y. He, B. Liu, and S. Hendryx Rubrics as rewards: reinforcement learning beyond verifiable domains . arXiv preprint arXiv:2507.17746 . Cited by: §B.4 .

Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. DeepSeek-r1: incentivizes reasoning in llms through reinforcement learning . nature 645 , pp. 633–638 . Cited by: §C.1 , §C.1 , §3.1 , §5 .

Hu et al. (2025a) J. Hu, Y. Zhang, Q. Han, D. Jiang, X. Zhang, and H. Shum Open-reasoner-zero: an open source approach to scaling up reinforcement learning on the base model . arXiv preprint arXiv:2503.24290 . Cited by: §2 .

Hu et al. (2024) S. Hu, Y. Tu, X. Han, G. Cui, C. He, W. Zhao, X. Long, Z. Zheng, Y. Fang, Y. Huang, et al. MiniCPM: unveiling the potential of small language models with scalable training strategies . In First Conference on Language Modeling , Cited by: §B.7 .

Hu et al. (2025b) X. Hu, X. Lu, L. Mao, Y. Zhang, T. Zhang, B. Wen, F. Yang, T. Gao, and G. Zhou Why distillation can outperform zero-rl: the role of flexible reasoning . arXiv preprint arXiv:2505.21067 . Cited by: §C.1 .

Huang et al. (2025) Z. Huang, T. Cheng, Z. Qiu, Z. Wang, Y. Xu, E. M. Ponti, and I. Titov Blending supervised and reinforcement fine-tuning with prefix sampling . arXiv preprint arXiv:2507.01679 . Cited by: §5 .

Hugging Face (2025) Hugging Face Open r1: a fully open reproduction of deepseek-r1 . External Links: Link Cited by: §4.1 .

Kober et al. (2013) J. Kober, J. A. Bagnell, and J. Peters Reinforcement learning in robotics: a survey . The International Journal of Robotics Research 32 ( 11 ), pp. 1238–1274 . Cited by: §C.2 .

Köpf et al. (2023) A. Köpf, Y. Kilcher, D. Von Rütte, S. Anagnostidis, Z. R. Tam, K. Stevens, A. Barhoum, D. Nguyen, O. Stanley, R. Nagyfi, et al. Openassistant conversations-democratizing large language model alignment . Advances in Neural Information Processing Systems 36 , pp. 47669–47681 . Cited by: §C.1 .

Lambert et al. (2024) N. Lambert, J. Morrison, V. Pyatkin, S. Huang, H. Ivison, F. Brahman, L. J. V. Miranda, A. Liu, N. Dziri, S. Lyu, et al. Tulu 3: pushing frontiers in open language model post-training . arXiv preprint arXiv:2411.15124 . Cited by: §C.1 , §C.1 , §1 , §5 .

Lanchantin et al. (2025) J. Lanchantin, A. Chen, J. Lan, X. Li, S. Saha, T. Wang, J. Xu, P. Yu, W. Yuan, J. E. Weston, et al. Bridging offline and online reinforcement learning for llms . arXiv preprint arXiv:2506.21495 . Cited by: §C.2 .

Li et al. (2024) J. Li, E. Beeching, L. Tunstall, B. Lipkin, R. Soletskyi, S. Huang, K. Rasul, L. Yu, A. Q. Jiang, Z. Shen, et al. Numinamath: the largest public dataset in ai4maths with 860k pairs of competition math problems and solutions . Hugging Face repository 13 , pp. 9 . Cited by: §4.1 .

Li and Khashabi (2025) T. Li and D. Khashabi SIMPLEMIX: frustratingly simple mixing of off-and on-policy data in language model preference learning . In Forty-second International Conference on Machine Learning , Cited by: §C.2 , §C.2 , §5 .

Li et al. (2025) Z. Li, C. Liang, Z. Zhang, I. Hong, Y. J. Kim, W. Chen, and T. Zhao SlimMoE: structured compression of large moe models via expert slimming and distillation . arXiv preprint arXiv:2506.18349 . Cited by: §B.6 .

Lin et al. (2017) T. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár Focal loss for dense object detection . In Proceedings of the IEEE international conference on computer vision , pp. 2980–2988 . Cited by: 5th item .

Liu et al. (2025a) M. Liu, G. Farina, and A. Ozdaglar UFT: unifying supervised and reinforcement fine-tuning . arXiv preprint arXiv:2505.16984 . Cited by: §C.2 , §5 .

Liu et al. (2024) W. Liu, X. Huang, X. Zeng, S. Yu, D. Li, S. Wang, W. Gan, Z. Liu, Y. Yu, Z. WANG, et al. ToolACE: winning the points of llm function calling . In The Thirteenth International Conference on Learning Representations , Cited by: §4.1 .

Liu et al. (2025b) Z. Liu, Z. Yang, Y. Chen, C. Lee, M. Shoeybi, B. Catanzaro, and W. Ping AceReason-nemotron 1.1: advancing math and code reasoning through sft and rl synergy . arXiv preprint arXiv:2506.13284 . Cited by: §A.1 , §C.1 , §D.3 , §1 , §2 .

Ma et al. (2025) L. Ma, H. Liang, M. Qiang, L. Tang, X. Ma, Z. H. Wong, J. Niu, C. Shen, R. He, B. Cui, et al. Learning what reinforcement learning can’t: interleaved online fine-tuning for hardest questions . arXiv preprint arXiv:2506.07527 . Cited by: §C.1 , §C.2 , §C.2 , §3.2 , §5 .

Mialon et al. (2023) G. Mialon, C. Fourrier, T. Wolf, Y. LeCun, and T. Scialom Gaia: a benchmark for general ai assistants . In The Twelfth International Conference on Learning Representations , Cited by: §1 .

Mnih et al. (2015) V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski, et al. Human-level control through deep reinforcement learning . nature 518 ( 7540 ), pp. 529–533 . Cited by: §C.2 .

Nachum et al. (2017) O. Nachum, M. Norouzi, K. Xu, and D. Schuurmans Bridging the gap between value and policy based reinforcement learning . Advances in neural information processing systems 30 . Cited by: §C.2 .

Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback . Advances in neural information processing systems 35 , pp. 27730–27744 . Cited by: §C.1 , §1 .

Pan et al. (2025) X. Pan, Y. Chen, Y. Chen, Y. Sun, D. Chen, W. Zhang, Y. Xie, Y. Huang, Y. Zhang, D. Gao, et al. Trinity-rft: a general-purpose and unified framework for reinforcement fine-tuning of large language models . arXiv preprint arXiv:2505.17826 . Cited by: §A.2 .

Patil et al. (2024) S. G. Patil, T. Zhang, X. Wang, and J. E. Gonzalez Gorilla: large language model connected with massive apis . Advances in Neural Information Processing Systems 37 , pp. 126544–126565 . Cited by: §4.1 .

Qin and Springenberg (2025) C. Qin and J. T. Springenberg Supervised fine tuning on curated data is reinforcement learning (and can be improved) . arXiv preprint arXiv:2507.12856 . Cited by: §C.1 .

Roux et al. (2025) N. L. Roux, M. G. Bellemare, J. Lebensold, A. Bergeron, J. Greaves, A. Fréchette, C. Pelletier, E. Thibodeau-Laufer, S. Toth, and S. Work Tapered off-policy reinforce: stable and efficient reinforcement learning for llms . arXiv preprint arXiv:2503.14286 . Cited by: §C.2 .

Schmidt (2019) F. Schmidt Generalization in generation: a closer look at exposure bias . In Proceedings of the 3rd Workshop on Neural Generation and Translation , pp. 157–167 . Cited by: 1st item .

Schulman et al. (2017) J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov Proximal policy optimization algorithms . arXiv preprint arXiv:1707.06347 . Cited by: §3.3 .

Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. Deepseekmath: pushing the limits of mathematical reasoning in open language models . arXiv preprint arXiv:2402.03300 . Cited by: §C.1 , §1 , §2 , §5 .

Tang et al. (2025) Y. Tang, T. Cohen, D. W. Zhang, M. Valko, and R. Munos RL-finetuning llms from on-and off-policy data with a single algorithm . arXiv preprint arXiv:2503.19612 . Cited by: §C.2 .

Taori et al. (2023) R. Taori, I. Gulrajani, T. Zhang, Y. Dubois, X. Li, C. Guestrin, P. Liang, and T. B. Hashimoto Alpaca: a strong, replicable instruction-following model . Stanford Center for Research on Foundation Models. https://crfm. stanford. edu/2023/03/13/alpaca. html 3 ( 6 ), pp. 7 . Cited by: §C.1 , §1 .

Wang et al. (2025) S. Wang, L. Yu, C. Gao, C. Zheng, S. Liu, R. Lu, K. Dang, X. Chen, J. Yang, Z. Zhang, et al. Beyond the 80/20 rule: high-entropy minority tokens drive effective reinforcement learning for llm reasoning . arXiv preprint arXiv:2506.01939 . Cited by: §3.3 .

Wang et al. (2024) Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, et al. Mmlu-pro: a more robust and challenging multi-task language understanding benchmark . In The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track , Cited by: §4.1 .

Wu et al. (2025) Y. Wu, Y. Zhou, Z. Ziheng, Y. Peng, X. Ye, X. Hu, W. Zhu, L. Qi, M. Yang, and X. Yang On the generalization of sft: a reinforcement learning perspective with reward rectification . arXiv preprint arXiv:2508.05629 . Cited by: §C.1 , §3.3 .

Yan et al. (2025) J. Yan, Y. Li, Z. Hu, Z. Wang, G. Cui, X. Qu, Y. Cheng, and Y. Zhang Learning to reason under off-policy guidance . arXiv preprint arXiv:2504.14945 . Cited by: Table 11 , §C.1 , §C.2 , §C.2 , §D.1 , §D.1 , §3.3 , §4.1 , §5 .

Yang et al. (2024a) A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, G. Dong, H. Wei, H. Lin, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Lin, et al. Qwen2.5 technical report . arXiv preprint arXiv:2412.15115 . Cited by: §3.1 .

Yang et al. (2024b) A. Yang, B. Zhang, B. Hui, B. Gao, B. Yu, C. Li, D. Liu, J. Tu, J. Zhou, J. Lin, et al. Qwen2. 5-math technical report: toward mathematical expert model via self-improvement . arXiv preprint arXiv:2409.12122 . Cited by: §A.3 , §C.1 , §1 .

Ye et al. (2025) Y. Ye, Z. Huang, Y. Xiao, E. Chern, S. Xia, and P. Liu LIMO: less is more for reasoning . arXiv preprint arXiv:2502.03387 . Cited by: §1 .

Young et al. (2024) A. Young, B. Chen, C. Li, C. Huang, G. Zhang, G. Zhang, G. Wang, H. Li, J. Zhu, J. Chen, et al. Yi: open foundation models by 01. ai . arXiv preprint arXiv:2403.04652 . Cited by: §C.1 .

Yu et al. (2025) Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, W. Dai, T. Fan, G. Liu, L. Liu, et al. Dapo: an open-source llm reinforcement learning system at scale . arXiv preprint arXiv:2503.14476 . Cited by: §A.2 , §1 , §2 .

Yue et al. (2025) Y. Yue, Z. Chen, R. Lu, A. Zhao, Z. Wang, S. Song, and G. Huang Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? . arXiv preprint arXiv:2504.13837 . Cited by: §C.1 , §5 .

Zeng et al. (2025) W. Zeng, Y. Huang, Q. Liu, W. Liu, K. He, Z. Ma, and J. He Simplerl-zoo: investigating and taming zero reinforcement learning for open base models in the wild . arXiv preprint arXiv:2503.18892 . Cited by: §D.1 .

Zhang et al. (2025a) S. Zhang, Y. Dong, J. Zhang, J. Kautz, B. Catanzaro, A. Tao, Q. Wu, Z. Yu, and G. Liu Nemotron-research-tool-n1: exploring tool-using language models with reinforced reasoning . arXiv preprint arXiv:2505.00024 . Cited by: §A.3 , §1 , §1 , §3.1 .

Zhang et al. (2019) W. Zhang, Y. Feng, F. Meng, D. You, and Q. Liu Bridging the gap between training and inference for neural machine translation . In Proceedings of the 57th Conference of the Association for Computational Linguistics , pp. 4334–4343 . Cited by: §D.3 , §1 , 1st item , §3.2 .

Zhang et al. (2025b) X. Zhang, Z. Huang, Y. Li, C. Ni, J. Chen, and S. Oymak BREAD: branched rollouts from expert anchors bridge sft & rl for reasoning . arXiv preprint arXiv:2506.17211 . Cited by: §C.2 , §5 .

Zheng et al. (2024) Y. Zheng, R. Zhang, J. Zhang, Y. YeYanhan, and Z. Luo LlamaFactory: unified efficient fine-tuning of 100+ language models . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations) , pp. 400–410 . Cited by: §A.2 .

Zhou et al. (2023) C. Zhou, P. Liu, P. Xu, S. Iyer, J. Sun, Y. Mao, X. Ma, A. Efrat, P. Yu, L. Yu, et al. Lima: less is more for alignment . Advances in Neural Information Processing Systems 36 , pp. 55006–55021 . Cited by: §C.1 , §1 .

## Appendix A Experimental Setups

### A.1 Hyperparameters

Across all experiments, we adopt the Adam optimizer with β 1 = 0.9 \beta_{1}=0.9 , β 2 = 0.999 \beta_{2}=0.999 . The learning rate is tuned within { 1 × 10 − 6 , 5 × 10 − 6 , 1 × 10 − 5 } \{1\times 10^{-6},5\times 10^{-6},1\times 10^{-5}\} , and the temperature for both rollout and evaluation is 1.0. The max response length is set to 16k tokens. For SFT, we train for a maximum of 3 epochs. For RL, we employ “strict on-policy training” similar to ( Liu et al., 2025b ) , where we generate K = 8 K=8 rollouts per prompt before each policy update.

For mathematical reasoning problems, the batch size for SFR/RL is 64/32, and the maximum number of RL steps is 1,500. For tool-use tasks, the batch size is 96 for both RL and SFT, and the maximum number of RL steps is 100. The μ \mu decay schedule is to decrease from 0.9 to 0.05 over the first 30 training steps.

### A.2 Implementation Details

In our experiments, the reward function is tailored to the task-specific requirements. For mathematical reasoning problems, we use a hierarchical reward scheme to encourage both correctness and format adherence. To guarantee the precision of our correctness evaluation, we exclusively sample problems that have integer answers when preparing our dataset. A response receives a reward of + 1.0 +1.0 for a correct final answer. If the format is correct (e.g., step-by-step reasoning ending with a boxed answer) but the answer is wrong, it receives a neutral reward of 0.0 0.0 . A small penalty of − 0.1 -0.1 is applied for responses that are both factually incorrect and improperly formatted. Finally, we penalize overly long and inconclusive responses ( Yu et al., 2025 ) , and apply a strong penalty of − 1.0 -1.0 for exceeding the predefined token limit without a final answer. For tool-use tasks, we employ a simpler binary reward. A response is given a reward of + 1.0 +1.0 if it is completely correct, and 0.0 0.0 otherwise.

We implement SFT algorithms based on LLaMA-Factory ( Zheng et al., 2024 ) , and implement RL algorithms based on Trinity-RFT ( Pan et al., 2025 ) . Experiments are conducted on 8 NVIDIA A100 GPUs and 8 NVIDIA H20 GPUs.

For evaluation, we adopt accuracy as the metric. To avoid high variance in results and ensure fair comparisons, we report avg@32 on AIME24 and AIME 25, and avg@8 on AMC, respectively. Reported results are on the best checkpoint determined by the validation set.

### A.3 Prompts

#### Prompt for Math Problems

The adopted prompt for math problems is shown below.

For the performance of the base model, we report the higher score achieved using either the above prompts for math problems or the default prompt provided by Qwen ( Yang et al., 2024b ) : “Please reason step by step, and put your final answer within \boxed{} ”.

#### Prompt for the MMLU-Pro Dataset

The adopted prompt for the MMLU-Pro dataset is shown below. We use the same system prompt as for the math problems, except that for multiple-choice questions, we modify the answer format to require the corresponding integer as the response.

#### Prompt for the Tool-use Tasks

For the tool-use tasks, we follow ( Zhang et al., 2025a ) to adopt their experimental setup and use the prompt provided in their Figure 8. This prompt is consistently applied to train the LLaMA3.2-3B-Instruct policy model and to generate SFT data with the DeepSeek-R1 expert model.

## Appendix B Experimental Results and Analysis

### B.1 Adaptive Tuning μ \mu

In addition to the fixed decay schedule for μ \mu , we explored an adaptive strategy to dynamically adjust the SFT loss weight based on the model’s ongoing performance, as measured by the average reward. We conducted experiments to validate this idea.

On the Tool-use task, we implemented a strategy where μ \mu is adjusted based on the mean reward of the rollouts. Specifically, for a given reward threshold τ \tau , the new μ \mu is calculated as μ ′ = max ⁡ ( 0 , τ − reward_mean ) \mu^{\prime}=\max(0,\tau-\text{reward\_mean}) . This mechanism ensures that as the model’s average reward surpasses the threshold, the SFT component is gradually phased out ( μ ′ → 0 \mu^{\prime}\to 0 ), allowing the training to focus purely on RL. We tested this with thresholds τ = 0.5 \tau=0.5 and τ = 0.7 \tau=0.7 .

The results, presented in Table 3 , show that setting the reward threshold to 0.5 yields a strong overall score of 78.1, which is highly competitive with our main approach using a fixed decay schedule. This indicates that dynamically reducing the SFT contribution as the model improves is a viable and effective strategy.

However, we also found that this configuration is still dependent on task-specific hyperparameter tuning. When we set a higher threshold of 0.7, performance degraded significantly. This is likely because the policy was subjected to excessive SFT even when achieving moderately high rewards, disrupting the optimization process.

These experiments serve as a proof of concept, demonstrating that an automated, reward-aware schedule for μ \mu can work effectively and represents a logical extension of our core ideas. However, since this method still requires tuning another hyperparameter(the reward threshold), its practical implementation is not necessarily simpler to tune. Therefore, we present this as a preliminary exploration into adaptive mixing coefficients, leaving a more thorough investigation of robust and generalizable adaptive schemes as a promising direction for future work.

### B.2 Varying the ϕ \phi Function

To validate the robustness of our approach and explore alternative weighting strategies, we conduct ablation studies comparing different variants of the token-wise weighting function ϕ ⁡ ( ⋅ ) \phi(\cdot) against our proposed method. We evaluate these variants on both the tool-use and mathematical reasoning tasks.

#### Evaluated ϕ \phi Variants.

We compare the following token-wise weighting strategies:

• Chord - ϕ \phi (Ours) : Our proposed method, with ϕ ⁡ ( p ) = p × ( 1 − p ) \phi(p)=p\times(1-p) .

• Entropy Top : Only trains on the top 5% of tokens with the highest entropy, setting ϕ ⁡ ( ⋅ ) = 1 \phi(\cdot)=1 for these tokens and ϕ ⁡ ( ⋅ ) = 0 \phi(\cdot)=0 for others.

• Entropy Norm : Normalizes the SFT loss weights based on entropy magnitude, with ϕ ⁡ ( p t ) ∝ H ⁡ ( t ) \phi(p_{t})\propto H(t) .

• IS Clip : Applies importance sampling correction but clips tokens with p t > 0.4 p_{t}>0.4 .

• Focal Loss : Adapts focal loss ( Lin et al., 2017 ) to the SFT context, giving higher weight to tokens with lower probability: ϕ ⁡ ( p ) = ( 1 − p ) γ \phi(p)=(1-p)^{\gamma} .

#### Experimental Setup.

For the mathematical reasoning experiments here, we relax the strict on-policy training protocol: we synchronize the policy model every 2 training steps (instead of after each update) and increase the number of rollouts per prompt to 16. Training is conducted for 400 steps. For tool-use tasks, we maintain the same setup as described in Appendix A .

#### Results and Analysis.

Table 4 presents the results on the ToolACE benchmark, while Table 5 shows the performance on mathematical reasoning tasks.

The experimental results reveal several interesting patterns across the different weighting strategies: • Chord - ϕ \phi (Ours): Our proposed method achieves consistently strong performance across both tool-use and mathematical reasoning benchmarks, demonstrating its effectiveness and robustness.

• Entropy-based Variants (Entropy Top & Norm): These methods validate the intuition of focusing on uncertain tokens. Entropy Top shows particularly strong performance on AIME2024 (17.2), proving that selectively emphasizing high-entropy tokens can effectively integrate expert knowledge. However, their performance gains are not as consistent as our method across all benchmarks.

• IS Clip: This variant, which clips high-probability tokens, shows limited effectiveness and even underperforms the pure RL baseline on the tool-use task. This suggests that simply clipping tokens is not a sufficiently nuanced strategy.

• Focal Loss: This strategy, which aggressively up-weights low-probability (high-surprise) tokens, leads to severe training instability and a significant performance collapse on both task types. This confirms our hypothesis that giving excessive weight to tokens the model deems unlikely can disrupt its learned reasoning abilities and lead to overfitting on expert patterns.

These results highlight the importance of fine-grained control in token-wise weighting. While various strategies can provide improvements over pure RL in specific scenarios, the choice of weighting function significantly impacts both training stability and final performance across different task domains. We note that our proposed ϕ ⁡ ( ⋅ ) \phi(\cdot) instantiation represents one effective realization of the general principle of down-weighting tokens at both probability extremes. The varied performance of different variants suggests that there remains room for exploring alternative weighting schemes that may be better suited to specific task characteristics or training scenarios, and we hope these empirical observations can inspire future research in this direction.

### B.3 Varying Expert Data Source

To further validate the robustness and generalizability of our approach, we conduct additional experiments using expert demonstrations generated by Qwen2.5-72B-Instruct instead of DeepSeek-R1. This setup is particularly interesting because Qwen2.5-72B-Instruct, while being a weaker expert model compared to DeepSeek-R1, produces responses with reasoning patterns that are more aligned with the base LLaMA3.2-3B-Instruct model. This allows us to investigate how the choice of expert data source—and specifically, the degree of pattern shift introduced—affects the effectiveness of different training methods.

Table 6 presents the performance comparison on the BFCL benchmark using expert data from both DeepSeek-R1 and Qwen2.5-72B-Instruct. The results lead to several key insights.

When using expert data from Qwen2.5-72B-Instruct, which exhibits reasoning patterns closer to those of LLaMA3.2-3B-Instruct, Chord - μ \mu achieves improved performance (78.1 vs. 77.6) compared to using DeepSeek-R1 data. This validates our hypothesis that the distributional shift introduced by expert data is a critical factor. When the expert’s reasoning pattern is more compatible with the base model’s existing policy, the progressive integration strategy of Chord - μ \mu can more effectively leverage this alignment, leading to better final performance.

Despite the weaker quality of Qwen2.5-72B-Instruct compared to DeepSeek-R1, Chord - ϕ \phi maintains strong and consistent performance (78.3 vs. 78.5) across both expert data sources. This demonstrates the robustness of the token-wise weighting mechanism, which allows the model to selectively absorb useful patterns while mitigating the negative effects of distributional mismatch, regardless of the expert’s absolute strength or stylistic differences.

Interestingly, the baseline SFT-best + RL method also shows notable improvement when using Qwen2.5-72B-Instruct data (77.7 vs. 76.1). This further corroborates our core motivation: the effectiveness of SFT is not solely determined by the quality of expert demonstrations in isolation, but is also heavily influenced by the degree of pattern shift they introduce relative to the base model. A smaller pattern shift, even from a weaker expert, can be more beneficial than a larger shift from a stronger but stylistically divergent expert.

#### Pattern Examples

To provide qualitative insight into these pattern differences, we present example responses from DeepSeek-R1, Qwen2.5-72B-Instruct, and the LLaMA3.2-3B-Instruct model after pure RL training below.

As illustrated in these examples, DeepSeek-R1 produces much more verbose and elaborate reasoning with extensive meta-commentary, while Qwen2.5-72B-Instruct adopts a more concise style that is closer to the direct, structured approach learned by LLaMA3.2-3B-Instruct through pure RL training. This qualitative analysis confirms that Qwen2.5-72B-Instruct introduces a smaller pattern shift, which aligns with the quantitative improvements observed in Table 6 .

### B.4 Non-Verifiable Tasks

To further test the generalizability of Chord beyond verifiable tasks, we conduct additional experiments on the RaR-Medicine dataset ( Gunjal et al., 2025 ) , a medical question-answering task that requires reasoning and explanation without deterministic verification.

We perform training on the Qwen2.5-7B-Instruct model for 200 steps, with both SFT and RL batch sizes of 96, 8 rollouts per prompt, a learning rate of 1 × 10 − 6 1\times 10^{-6} , and the μ \mu decay step is set to 50. We use Qwen3-30B-3A-Instruct as the judge model. The expert demonstrations are sourced from the English subset of the medical-o1-reasoning dataset ( Chen et al., 2025d ) , which contains high-quality reasoning traces for medical questions.

Table 7 and Figure 10 present the experimental results. Both Chord - μ \mu and Chord - ϕ \phi significantly outperform pure RL, achieving testset scores of 80.6 and 81.3 compared to 76.8 for pure RL. Figure 10 further show that Chord - ϕ \phi achieves faster convergence and higher final rewards compared to pure RL, indicating more efficient exploration guided by expert demonstrations, where Chord - μ \mu possesses a similar “shift-readapt” pattern similar to the main experiment. These results validate that our approach can further generalize to more diverse post-training domains.

### B.5 SFT/RL synergy for Weaker Policy Models

An important consideration is how the SFT/RL synergy works when the initial policy model is less capable. Intuitively, one might assume that for a weaker model, supervised fine-tuning (SFT) on expert data would become more critical, as the model’s own on-policy exploration is likely to be less effective.

However, our experiments reveal a more nuanced reality: a weaker model can also struggle to effectively absorb knowledge from expert data. As shown in Table 8 , naively fine-tuning the weaker Qwen2.5-3B-Instruct model with SFT leads to a performance collapse(RL settings are similar to Appendix B.2 ). This is in stark contrast to the result observed when training the Qwen2.5-7B-Instruct model, whose performance significantly improves with the same 5k SFT samples (e.g., AIME2024 accuracy rising from 11.7% to 15.8%). For the weaker model, while Pure RL still provides a consistent performance lift, a naive SFT+RL combination proves unstable. This instability highlights a dual limitation: a weaker model is constrained not only in its on-policy exploration but also in its capacity to absorb off-policy expert data, making the trade-off between exploration and imitation challenging to navigate. In such a setting, the Chord - ϕ \phi method successfully maintains learning stability by providing a robust objective to balance this trade-off. We acknowledge that with larger quantities of higher-quality expert data, a weaker model might overcome this imitation bottleneck, potentially making SFT-leaning methods more favorable. Conversely, this also suggests that our method becomes particularly advantageous when dealing with weaker models under limited expert data, demonstrating its strong capability to flexibly adapt and create a robust synergy between SFT and RL even when naive imitation fails.

### B.6 Diverse Model Architectures

To assess the broader applicability of our method, we extended our evaluation to a model with a distinct architecture and origin: the Phi-mini-MoE-instruct model ( Li et al., 2025 ) (a light-weight Mixture of Experts (MoE) model with 3.8B total, 1.1B active params). This experiment also tests our method’s effectiveness beyond the dense Qwen and LLaMA models.

As shown in Table 9 , the MoE model exhibits a similar vulnerability to naive SFT in tool-use tasks, with performance collapsing significantly. In stark contrast, our Chord - ϕ \phi effectively achieves the highest performance and boosts the overall accuracy from 49.5 to 61.6.

These results show that our method is architecture-agnostic, and further demonstrates its effectiveness across diverse model families and architectures.

### B.7 Tuning μ \mu in Conjunction with ϕ \phi

The proposed Chord employs a dual-control mechanism: a global coefficient μ \mu and a token-wise weighting function ϕ ⁡ ( ⋅ ) \phi(\cdot) . While this raises the question of their joint scheduling, we find that the fine-grained control from ϕ ⁡ ( ⋅ ) \phi(\cdot) makes the framework more robust to the specific schedule of μ \mu . This innovation alleviates the need for meticulous tuning of the global coefficient, simplifying the practical application of Chord .

The aggressive decay schedule for μ \mu (starting from a high value) was designed to manage the “shift-readapt” progression. However, since the weight function ϕ ⁡ ( ⋅ ) \phi(\cdot) also aims to stabilize learning and prevent pattern disruption, such an aggressive start may be unnecessary. A more theoretically aligned approach would be to gently introduce the expert data via a warmup-then-decay ( Hu et al., 2024 ) schedule for μ \mu (e.g., warming up from 0 to 0.3 before decaying). This would align with the stabilizing nature of ϕ ⁡ ( ⋅ ) \phi(\cdot) .

We compare these two schedules in Figure 12 . Although Chord -tune-both that leverages a more refined warmup-then-decay μ \mu schedule yields a slightly better reward progression during training, the final performance gap between the two approaches is not that significant.

This observation is consistent with our insight: the primary purpose of introducing ϕ ⁡ ( ⋅ ) \phi(\cdot) is to enable expert data to continuously and stably guide exploration. By inherently preventing both the disruption of existing patterns and overfitting at a token level, ϕ ⁡ ( ⋅ ) \phi(\cdot) makes the aggressive expert-first approach (a large initial μ \mu ) less critical. The token-wise control provides stability, making the overall system less sensitive to the global trade-off hyperparameter. We argue that adopting ϕ ⁡ ( ⋅ ) \phi(\cdot) not only improves stability but also simplifies the practical application of our framework by making it robust to the specific choice of the μ \mu schedule.

### B.8 Experimental Results on Tool-use Training

We provide the training curves on tool-use tasks in Figure 12 and a more detailed experimental result on the BFCL benchmark in Table 10 . The average performance reported in the BFCL benchmark is averaged by instance, meaning that categories with more instances have a greater contribution to the final average score. All methods are evaluated using the same system prompt format.

### B.9 Experimental Results on the MMLU-pro dataset

We provide a more detailed experimental result on the MMLU-pro dataset in Table 11 . The adopted prompts for generating these results can be found in Appendix A.3 .

## Appendix C Detailed Discussions of Related Works

### C.1 Finetuning for LLMs

#### SFT for LLMs.

SFT has established itself as a cornerstone for aligning LLMs, primarily due to its conceptual simplicity and cost-effectiveness, making it a favored approach within the open-source community for creating capable instruction-following models ( Taori et al., 2023 ; Köpf et al., 2023 ) . Early work emphasized the power of high-quality datasets ( Zhou et al., 2023 ; Young et al., 2024 ) , while the required expert curation is labor-intensive and costly. Moreover, to cover the diverse use cases of modern LLMs, the paradigm has shifted towards massive-scale SFT ( Grattafiori et al., 2024 ; Lambert et al., 2024 ) . This trend makes it computationally prohibitive for many to fine-tune from a base model, promoting continued tuning on pre-aligned instruction models instead. Furthermore, the interplay between SFT and RL has grown more complex, from recent methods like DFT ( Wu et al., 2025 ) or iw-SFT ( Qin and Springenberg, 2025 ) that incorporate RL-inspired importance sampling into SFT, to reasoning models like DeepSeek-R1 ( Guo et al., 2025 ) that strategically integrate both paradigms, highlighting that the optimal, principled integration of these methods remains a critical and open area of research.

#### RL for LLMs.

Recent applications of Reinforcement Learning (RL) for Large Language Models (LLMs) have expanded beyond traditional human preference alignment ( Bai et al., 2022 ; Ouyang et al., 2022 ) , demonstrating significant progress in complex reasoning domains such as mathematics and code generation ( Shao et al., 2024 ; Yang et al., 2024b ; Guo et al., 2025 ) . In particular, a surge of recent work has focused on Reinforcement Learning from Verifiable Rewards (RLVR) ( Lambert et al., 2024 ; Guo et al., 2025 ) , where rewards are derived from definitive outcomes like correct answers or passing unit tests. This paradigm has achieved remarkable results on various benchmarks. However, a fundamental challenge persists in how RL can facilitate effective exploration to surpass the inherent capabilities of its base model ( Yue et al., 2025 ) . The search for novel solutions is often constrained by the model’s pre-existing knowledge, limiting its discovery of superior reasoning pathways. To address this, introducing external expert data — either for distillation ( Hu et al., 2025b ; Liu et al., 2025b ; Guha et al., 2025 ) , cold start ( Guo et al., 2025 ) , or to guide exploration towards diverse, high-quality patterns ( Yan et al., 2025 ; Ma et al., 2025 ) — emerges as a promising approach to transcend these limitations and unlock new problem-solving frontiers.

### C.2 On- and Off-policy Reinforcement Learning

#### Combining On-policy and Off-policy Data in Traditional RL

In traditional RL domains like robotics ( Kober et al., 2013 ) or games ( Mnih et al., 2015 ) , combining on-policy and off-policy data is a potent strategy. Methods ranging from alternating training phases ( Gao et al., 2025 ) , to mixing data from separate buffers ( Ball et al., 2023 ) , or directly augmenting on-policy replay buffers with expert trajectories ( Nachum et al., 2017 ) have been proven useful. While such methods yield good results in the traditional RL fields, the discrepancy arises from two fundamental distinctions of LLMs: their strong initial priors, where aggressive off-policy updates risk disrupting established reasoning patterns, and their vast, autoregressive action space that radically increases the off-policy degree of expert data, especially for long reasoning chains, and invalidates the assumptions underpinning conventional off-policy algorithms.

#### Combining On-policy and Off-policy Data in RL for LLM

Leveraging off-policy data to improve the sample efficiency is a well-established strategy in RL. Several studies have focused on leveraging stale, self-generated data by employing techniques such as refining importance sampling corrections ( Tang et al., 2025 ) , mixing on- and off-policy gradients ( Li and Khashabi, 2025 ) , modifying the optimization loss objective ( Roux et al., 2025 ; Arnal et al., 2025 ) , or adjusting the synchronization frequency between online and target policies ( Lanchantin et al., 2025 ) .

More closely related to our work are methods that leverage external expert data to guide the reinforcement learning process for LLMs. These methods can be broadly categorized. One strategy is direct data mixing ( Yan et al., 2025 ; Dong et al., 2025 ; Li and Khashabi, 2025 ) . For example, SimpleMix ( Li and Khashabi, 2025 ) , operates within a DPO framework and combines off-policy and on-policy data via simple dataset-level sampling. LUFFY ( Yan et al., 2025 ) on the other hand, incorporates off-policy expert trajectories directly into the on-policy rollout groups within a GRPO framework. While such approaches expose the model to expert data, they also introduce significant constraints: they usually require strict prompt alignment between datasets or lack the dynamic, token-level weighting needed to manage severe distribution shifts. Another strategy involves using expert data as guidance for generation. For instance, UFT ( Liu et al., 2025a ) and BREAD ( Zhang et al., 2025b ) utilize supervised fine-tuning (SFT) trajectories as prefixes for on-policy rollouts; UFT progressively masks the suffix of the expert demonstration, while BREAD initiates new rollouts by branching from intermediate steps. A third category interleaves RL updates with SFT steps on expert data, either selectively for challenging examples ( Ma et al., 2025 ) or based on a probabilistic schedule ( Chen et al., 2025c ) . Most recently, SRFT ( Fu et al., 2025 ) unifies these approaches into a single-stage framework by not only mixing SFT samples into the on-policy rollout groups but also applying a dedicated SFT loss whose influence is adjusted at the sample level.

Our work diverges from these methods in a crucial aspect. The aforementioned approaches, including state-of-the-art methods like SRFT ( Fu et al., 2025 ) , LUFFY ( Yan et al., 2025 ) , and Reift ( Ma et al., 2025 ) , primarily operate under a “zero-RL” paradigm, initiating training from a base model with a nascent policy. In stark contrast, our work addresses the challenge of fine-tuning a model that already possesses a well-developed, instruction-following policy. This advanced starting point inherently creates a more significant distributional shift between the model’s existing policy and the external expert data, thereby exacerbating the off-policy correction problem that our method aims to solve. For further empirical analysis and results, please refer to Appendix D.1 .

## Appendix D Further Discussions

### D.1 The Influence of Off-Policy Data on Base vs. Instruction Models

The challenges of controlling the influence of off-policy data and maintaining training stability are significantly amplified when fine-tuning instruction models. This is mainly due to the established policy inherent in these instruction models.

Starting from Base Model vs. Instruct Model A base model, having been pre-trained solely with a language modeling objective, lacks a coherent, task-specific policy for instruction following. It often has not yet converged on a particular response pattern. When learning from off-policy expert data, the training process is akin to initial policy formation. The model learns a new skill without the risk of conflicting with an existing pattern, thus avoiding significant instability during training.

In contrast, an instruction model has already developed a sharply-peaked policy. Training these models on off-policy expert data that may reflect different reasoning patterns introduces a substantial distributional mismatch . The RL algorithm’s efforts to reconcile this mismatch can result in large, disruptive policy updates, destabilizing the established policy and potentially leading to a collapse in performance.

Figure 13 provides empirical observation to support the above discussions. When learning from a mixture of on-policy and off-policy data, the reward of a base model improves monotonically, displaying none of the instability issues that can affect instruction models under similar conditions.

Different from most existing studies ( Zeng et al., 2025 ; Yan et al., 2025 ; Fu et al., 2025 ) , which focus on the “Zero-RL” setting that trains from a base model, this paper addresses a more challenging yet practical problem: how to effectively integrate knowledge from off-policy experts into a model that already possesses an established policy. Training from a base model is not always feasible in practical applications. For instance, such methods are ineffective for tool-use tasks, as the base model typically lacks the basic capability to follow the necessary instructions.

Applying “Zero-RL” Methods to Our Setting To demonstrate the unique advantages of Chord for aligning already instruction-tuned models, we conduct additional experiments comparing our proposed Chord with LUFFY ( Yan et al., 2025 ) and SRFT ( Fu et al., 2025 ) on the tool-use task. Note that both LUFFY and SRFT require strict alignment between expert demonstrations and RL prompts, as they directly mix expert trajectories into on-policy rollouts. Hence, we generate expert demonstrations for all 5,000 training prompts using DeepSeek-R1. In contrast, Chord only uses 500 expert demonstrations without requiring prompt-level alignment.

The results in Table 12 , show that Chord significantly outperforms both methods. As discussed in Appendix C , when applied to instruction-tuned models with established policies, directly mixing expert trajectories causes significant distributional mismatch, leading to training instability. Specifically, LUFFY’s upweighting of low-probability tokens on top of importance sampling can still cause policy shifts when the distribution gap between expert and policy gap is large. SRFT’s uniform sample-level weighting cannot distinguish valuable tokens from irrelevant ones within a trajectory, leading to inefficient and misguided updates. In contrast, our ϕ ⁡ ( ⋅ ) \phi(\cdot) function provides token-wise adaptive weighting, enabling selective absorption of expert patterns while maintaining policy stability. These results validate that our method achieves superior performance with better expert data efficiency and maintains training stability on instruction-tuned models, making it more practical for many more real-world applications.

### D.2 On Different Task-Related Performance

The differing performance gains on the MATH and tool-use tasks stem from the fundamental distinctions between these two domains. We deliberately chose these tasks to represent two distinct paradigms, thereby demonstrating the robustness and flexibility of our proposed method.

The math domain benefits from complex, structured, and long-form reasoning. For such tasks, acquiring the necessary problem-solving patterns through pure on-policy exploration (i.e., Pure RL) can be inefficient in comparison. Supervised Fine-Tuning (SFT) on expert data is highly beneficial in this context, as it directly exposes the model to well-structured, step-by-step reasoning chains. This allows the model to efficiently learn complex reasoning frameworks that are difficult to discover from scratch. As we discussed in Section 4.2 , the model’s performance on math problems often correlates with its ability to produce more comprehensive and detailed reasoning steps, a pattern effectively taught by expert data. Therefore, a method that can successfully integrate these expert reasoning patterns, like ours, is expected to yield substantial improvements.

The tool-use domain , in contrast, relies more on the exact tool call result rather than the reasoning process. In this setting, naive imitation of expert trajectories through SFT can even be detrimental, as an expert’s solution may contain stylistic artifacts (e.g., verbosity) that are not conducive to performance. As shown in Table 2 and discussed in Section 4.2 , tool-use tasks favor concise and efficient responses, a pattern that Pure RL naturally learns by shortening response lengths. The primary challenge here is not just to imitate the expert, but to leverage expert guidance to accelerate exploration without being overly constrained or picking up suboptimal habits. The consistent performance gain of our method over the strong Pure RL baseline demonstrates its ability to achieve this delicate balance: successfully extracting useful signals from expert data while avoiding the pitfalls of naive imitation.

These two domains present different challenges for unifying offline SFT and online RL, and our proposed method proves its effectiveness by excelling in both scenarios. It learns to produce comprehensive reasoning for MATH while generating concise, efficient tool calls for tool-use tasks, demonstrating its capability to selectively absorb expert knowledge in a task-specific manner. This validates our approach as a robust and versatile framework for diverse applications.

### D.3 Scaling SFT Is Not Enough: The Necessity of On-Policy Learning

A crucial question is whether extensive SFT on high-quality expert data could eliminate the need for combining SFT and RL. Indeed, as the quantity and diversity of data increase, the problem of exposure bias ( Zhang et al., 2019 ) can be alleviated, leading to better generalization. And for knowledge-intensive tasks like MATH, model performance can be highly correlated with the volume and quality of SFT data. To investigate this, we expanded the MATH SFT dataset from 5k to 20k examples, which substantially boosted the pure SFT model’s AIME accuracy from 15% to approximately 24%.

However, even with larger volumes of SFT data, a principled transition to on-policy learning remains critical for reaching the performance frontier. Recent literature ( Liu et al., 2025b ) also shows that extensive SFT followed by RL fine-tuning is an effective strategy for maximizing model capabilities. By applying our SFT/RL combined approach, we can further elevate the accuracy from 24% to 33%. This demonstrates that RL is not redundant but complementary, enabling the model to refine its policy beyond the static distribution of expert data.

## Appendix E Case Studies

For a better understanding, we compare the generation patterns of RL-only (i.e., pure RL), SFT-only, and the proposed Chord .

• RL-only : The model trained solely with RL exhibits a concise and structured, yet ultimately rigid, reasoning pattern. It tends to follow a fixed template, such as beginning with “To…” and using connectors like “First” and “Next”, and proceeds linearly without engaging in self-correction or exploring alternative solution paths. While this approach leads to efficient responses, it may result in less robust solutions.

• SFT-only and Chord - μ \mu : In contrast, the model trained solely on expert demonstrations can be verbose and exploratory. It exhibits a “think-aloud” style with frequent meta-commentary (e.g., “Let me think…”), backtracking, and verification of intermediate steps. The generated responses are comprehensive, but often lack a concise structure. Note that the proposed Chord - μ \mu has a similar reasoning pattern to SFT-only.

• Chord - ϕ \phi : It exhibits a hybrid reasoning style that retains a clean and logical structure while selectively incorporating the expert’s sophisticated verification strategies. As shown in the example below, it develops patterns such as “Alternatively…” and “Both methods confirm…” to produce responses that are both well-structured and robust. We select the checkpoints at 800 steps as the models to generate the examples here.

## Use of Large Language Models

We used large language models only as general-purpose writing assistants, to proofread and correct grammatical errors in this manuscript.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
