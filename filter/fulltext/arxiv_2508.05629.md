##### Report GitHub Issue

Content selection saved. Describe the issue below:

# On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification

###### Abstract

In this work, we present a simple yet theoretically motivated improvement to Supervised Fine-Tuning (SFT) for the Large Language Model (LLM), addressing its limited generalization compared to reinforcement learning (RL). Through mathematical analysis, we reveal that standard SFT gradients implicitly encode a problematic reward structure that may severely restrict the generalization capabilities of model compared to RL. To rectify this, we propose Dynamic Fine-Tuning (DFT), stabilizing gradient updates for each token by dynamically rescaling the objective function with the probability of this token. With just a single-line change, the method outperforms standard SFT on multiple difficult benchmarks and base models, from math reasoning to code generation and multi-modal tasks, demonstrating improved generalization. Additionally, DFT achieves competitive results in offline RL settings, providing an effective yet streamlined alternative. By bridging theoretical insights with practical solutions, this work advances the state of SFT. The source code will be available at https://github.com/yongliang-wu/DFT .

## 1 Introduction

Supervised Fine-Tuning (SFT), which adapts models to expert demonstrations, has become the standard post-training paradigm for Large Language Models (LLMs) ( Zhang et al., 2025c ; Zhang et al., 2024a ; Zhang et al., 2025b ; Zhang et al., 2025a ; Wang et al., 2025b ) . It enables efficient task adaptation and capability enhancement ( Chung et al., 2024 ; Zhang et al., 2024c ; Sanh et al., 2022 ; Ouyang et al., 2022 ; Chen et al., 2024 ; Chen et al., 2025a ; Fang et al., 2025 ) , and is popular for its ease of implementation and rapid acquisition of expert-like behaviors ( Wei et al., 2022 ; Zhou et al., 2023 ) . Despite these advantages, SFT often shows limited generalization compared to reinforcement learning (RL) ( Chu et al., 2024 ; Ouyang et al., 2022 ; Christiano et al., 2017 ; Bai et al., 2022 ; Huan et al., 2025 ; Swamy et al., 2025 ) . RL leverages explicit reward or verification signals to explore diverse strategies and thus generalizes better. However, RL requires substantial computation, careful hyperparameter tuning, and explicit reward signals—conditions often impractical in real-world settings ( Schulman et al., 2017 ; Ouyang et al., 2022 ; Sheng et al., 2025 ; Strubell et al., 2019 ; Liu and Yin, 2024 ; Winsta, 2025 ) . Moreover, RL can struggle to recover expert-like behaviors that SFT captures efficiently ( Mandlekar et al., 2022 ; Chen et al., 2025c ) .

To exploit the complementary strengths of both approaches, many hybrid methods combine SFT with RL ( Ouyang et al., 2022 ; Sheng et al., 2025 ; Rafailov et al., 2023 ; Liu et al., 2025 ; Qiu et al., 2025 ) . Yet a key question remains: can SFT itself be fundamentally improved? This is crucial, as SFT remains the only viable option when datasets contain only positive demonstrations, with no negative samples or reward model available.

In this work, we address this gap with a mathematical analysis of the connection between SFT and RL. We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions. Crucially, this reward is (i) sparse, and (ii) inversely proportional to the model’s probability of expert actions (see equation 6 ). As a result, when the model assigns low probability to expert actions, the gradient becomes excessively large, yielding an ill-posed reward structure and unstable optimization ( Pascanu et al., 2013 ; Yang et al., 2019 ) .

Building on this insight, we propose Dynamic Fine-Tuning (DFT), a principled fix. Our method rescales the SFT objective at each token by its probability, canceling the distortion introduced by inverse-probability weighting. This reframing turns the SFT gradient from a potentially unstable and biased estimator into a more stable, more uniformly weighted update rule that behaves closer to an RL-style.

Empirically, DFT delivers substantial improvements. On the Qwen-2.5-Math series ( Qwen Team et al., 2024a ) fine-tuned with NuminaMath-CoT ( LI et al., 2024 ) , DFT yields gains several times larger than standard SFT. More importantly, unlike SFT, which often degrades on challenging benchmarks such as OlympiadBench ( He et al., 2024 ) , AIME 2024 ( American Institute of Mathematics, 2024 ) , and AMC 2023 ( Mathematical Association of America, 2023 ) , our method consistently improves performance and generalization. These improvements hold across models, scales, and data sizes (Table 1 , Figure 1 ), and extend to code generation and multimodal reasoning (Tables 3 , 4 ) ( Zhao et al., 2025d ; Luo et al., 2025 ; Li et al., 2025a ; Li et al., 2025b ) ( Zhu et al., 2024b ; Zhu et al., 2024c ; Zhu et al., 2024a ; Zhu et al., 2020 ) .

We further test DFT in off-policy RL settings (Table 2 ), where dense rewards are available ( Levine et al., 2020 ) . Our method not only outperforms offline RL approaches such as DPO ( Rafailov et al., 2023 ) and RAFT ( Dong et al., 2023 ; Ahn et al., 2024 ) , but also achieves competitive or superior performance to online methods like GRPO and PPO on math tasks with Qwen2.5-Math-1.5B ( He et al., 2025 ; Tan et al., 2026 ; Zhao et al., 2025b ; Zhao et al., 2025a ) . Unlike these RL methods, DFT requires neither a reference model nor large batch sizes, making it a simpler and more resource-efficient alternative.

To understand its effect, we analyze token probability distributions after training (Figure 2 ). While traditional SFT uniformly pushes probabilities toward the training set, DFT selectively increases some while reducing others. In particular, the proportion of less strongly fitted tokens rises, suggesting improved regularization. We provide further discussion in Appendix A.3 .

The contributions of this work are theoretical and practical. On the theoretical side, we mathematically establish LLM SFT as a special RL in policy gradient space, pinpoint the underlying reasons for the limited generalization of SFT, and derive a method to improve it. On the experimental side, we show that such a simple solution, just one line of code, can enhance the performance and generalization capabilities of SFT across various tasks and models.

## 2 Related Work

The trade-off between supervised fine-tuning (SFT) and reinforcement learning (RL) is central to the alignment of large language models ( Song et al., 2024 ; Chai et al., 2024 ; Song et al., 2025c ; Song et al., 2025a ; Xu et al., 2025 ; Song et al., 2025b ; Zhu et al., 2025b ; Zhu et al., 2025c ; Zhu et al., 2025a ) . SFT is widely adopted due to its simplicity and efficiency in imitating expert demonstrations ( Chung et al., 2024 ; Zhou et al., 2023 ; Wei et al., 2022 ) , analogous to behavioral cloning in robotics ( Sammut, 2011 ; Mandlekar et al., 2022 ) . However, the literature consistently highlights its limitations, particularly the tendency to overfit and generalize poorly compared to RL, which leverages reward signals to discover more robust policies ( Ouyang et al., 2022 ; Christiano et al., 2017 ; Bai et al., 2022 ; Swamy et al., 2025 ; Zhang et al., 2025d ) . A recent systematic comparison by Chu et al. (2024) across textual and visual domains confirms this distinction, concisely summarized as “SFT memorizes while RL generalizes.” They further show that SFT remains indispensable as an initialization step, stabilizing output formatting prior to effective RL training. Nonetheless, RL faces significant practical hurdles, including computational expense, sensitivity to hyperparameters, and the requirement of an explicit reward function, all of which constrain its applicability ( Schulman et al., 2017 ; Strubell et al., 2019 ; Sheng et al., 2025 ) .

To combine the strengths of both paradigms, much recent work has pursued hybrid approaches. The most common strategy involves SFT pretraining followed by RL-based refinement with a learned reward model, as popularized by InstructGPT ( Ouyang et al., 2022 ) . More recent methods interleave SFT and RL updates to improve stability and performance ( Sheng et al., 2025 ; Liu et al., 2025 ; Qiu et al., 2025 ) . Other approaches, such as Direct Preference Optimization (DPO) ( Rafailov et al., 2023 ) , bypass reward modeling entirely by directly optimizing policies on preference data, thereby unifying imitation and reinforcement signals within a single loss function. Chen et al. (2025b) introduce Negative-aware Fine-Tuning (NFT), which models incorrect generations via an implicit negative policy, enabling self-improvement without explicit feedback. While powerful, these methods rely on reward signals, preference pairs, or negative samples. They enrich the training pipeline but do not fundamentally improve SFT in its native setting, where only positive demonstrations are available. Our work instead focuses on enhancing SFT itself without requiring external feedback.

A complementary line of theoretical research seeks to unify SFT and RL under a common formalism. Du and others (2025) reinterpret RLHF as a reward-weighted variant of SFT, preserving reliance on an explicit reward. Wang et al. (2025a) show that SFT can be cast as RL with an implicit reward, proposing adjustments such as smaller learning rates to manage the vanishing KL constraint. Abdolmaleki et al. (2025) analyze learning from both positive and negative feedback, studying how their balance affects convergence. Qin and Springenberg (2025) view SFT as a lower bound of RL and introduce importance weighting based on the data-generating policy. While these works establish connections between SFT and RL through weighting, they do not provide a precise mathematical equivalence between the SFT gradient and the offline policy gradient. Some methods approximate this connection in practice by reweighting training losses. For instance, MixCE ( Zhang et al., 2023 ) combines the forward and reverse KL divergences to form a unified objective, while GOLD ( Pang and He, 2021 ) adopts offline RL with demonstrations, introducing reliance on an unknown demonstration distribution π b \pi_{b} and a restrictive 1 / N 1/N assumption. Kantharaju and Sankar (2022) also provide a clear and insightful exposition of GOLD’s motivation and mechanics from an alternative perspective, offering useful intuition for understanding its underlying design. Zhao et al. (2025c) provide a promising method to combine RL and SFT during training. In contrast, our work offers a more formal perspective on this connection, highlighting the role of the inverse-probability weighting term in shaping the difference between SFT and RL-like updates. This perspective motivates a simple adjustment: multiplying the loss by the model’s token probability to neutralize the weighting.

Interestingly, our method modifies the standard cross-entropy (CE) loss in a way that inverts the weighting philosophy of the widely used Focal Loss ( Lin et al., 2017 ) . Specifically, our modified CE takes the form − p ​ log ⁡ ( p ) -p\log(p) , whereas focal loss is defined as − ( 1 − p ) γ ​ log ⁡ ( p ) -(1-p)^{\gamma}\log(p) . Focal Loss deliberately downweights well-classified samples to emphasize underrepresented or hard cases, whereas we deliberately downweight poorly classified samples to encourage generalization. This inversion reflects a fundamental shift in the LLM era: while underfitting was once a central challenge, overfitting and memorization now dominate, demanding a rethinking of objective design.

## 3 Method

### 3.1 Preliminaries

#### Supervised Fine-Tuning.

Let 𝒟 = { ( x , y ⋆ ) } \mathcal{D}=\{(x,y^{\star})\} denote a corpus of expert demonstrations, where y ⋆ y^{\star} is the complete reference response to the query x x . SFT minimizes the sentence-level cross-entropy: ℒ SFT ​ ( θ ) = 𝔼 ( x , y ⋆ ) ∼ 𝒟 ​ [ − log ⁡ π θ ​ ( y ⋆ ∣ x ) ] . \mathcal{L}_{\mathrm{SFT}}(\theta)\;=\;\mathbb{E}_{(x,y^{\star})\sim\mathcal{D}}\bigl[-\log\pi_{\theta}\bigl(y^{\star}\mid x\bigr)\bigr]. (1) Its gradient is: ∇ θ ℒ SFT ​ ( θ ) = 𝔼 ( x , y ⋆ ) ∼ 𝒟 ​ [ − ∇ θ ​ log ​ π θ ​ ( y ⋆ ∣ x ) ] . \nabla_{\theta}\mathcal{L}_{\mathrm{SFT}}(\theta)\;=\;\mathbb{E}_{(x,y^{\star})\sim\mathcal{D}}\bigl[-\nabla_{\theta}\log\pi_{\theta}\bigl(y^{\star}\mid x\bigr)\bigr]. (2)

#### Reinforcement Learning.

Let y y denote a response sampled from the policy π θ ( ⋅ ∣ x ) \pi_{\theta}(\cdot\mid x) for query x x . Given a reward function r ⁡ ( x , y ) ∈ ℝ r(x,y)\in\mathbb{R} , the policy objective is J ( θ ) = 𝔼 x ∼ 𝒟 x , y ∼ π θ ( ⋅ ∣ x ) [ r ( x , y ) ] . J(\theta)\;=\;\mathbb{E}_{x\sim\mathcal{D}_{x},\;y\sim\pi_{\theta}(\cdot\mid x)}\bigl[r(x,y)\bigr]. (3) Its policy gradient at the sentence level is ∇ θ J ( θ ) = 𝔼 x ∼ 𝒟 x , y ∼ π θ ( ⋅ ∣ x ) [ ∇ θ log π θ ( y ∣ x ) r ( x , y ) ] . \nabla_{\theta}J(\theta)\;=\;\mathbb{E}_{x\sim\mathcal{D}_{x},\;y\sim\pi_{\theta}(\cdot\mid x)}\bigl[\nabla_{\theta}\log\pi_{\theta}(y\mid x)\;r(x,y)\bigr]. (4)

### 3.2 Unify SFT and RL Gradient Expression

#### Rewriting SFT Gradient as Policy Gradient via Importance Sampling.

The SFT gradient in equation 2 is taken under the fixed demonstration distribution. We convert it to an on-policy expectation by inserting an importance weight that compares the expert (Dirac Delta) distribution with the model distribution. 𝔼 ( x , y ⋆ ) ∼ 𝒟 ​ [ − ∇ θ ​ log ​ π θ ​ ( y ⋆ ∣ x ) ] = 𝔼 x ∼ 𝒟 x ​ 𝔼 y ∼ π θ ( ⋅ ∣ x ) 𝟏 [ y = y ⋆ ] π θ ​ ( y ∣ x ) [ − ∇ θ log π θ ( y ∣ x ) ] ⏟ resample + reweight \mathbb{E}_{(x,y^{\star})\sim\mathcal{D}}\,\bigl[-\nabla_{\theta}\log\pi_{\theta}\bigl(y^{\star}\mid x\bigr)\bigr]=\mathbb{E}_{x\sim\mathcal{D}_{x}}\,\underbrace{\mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}\frac{\mathbf{1}[y=y^{\star}]}{\pi_{\theta}(y\mid x)}\,\bigl[-\nabla_{\theta}\log\pi_{\theta}\bigl(y\mid x\bigr)\bigr]}_{\text{resample + reweight}}\, (5)

Define the auxiliary variables (importance sampling weight) as w ( y ∣ x ) = 𝟏 π θ ​ ( y ∣ x ) , r ( x , y ) = 𝟏 [ y = y ⋆ ] . w(y\mid x)=\frac{\mathbf{1}}{\pi_{\theta}(y\mid x)},\quad r(x,y)=\mathbf{1}[y=y^{\star}]. Reorganizing equation 5 and rewriting it using the above auxiliary variables, we obtain the form ∇ θ ℒ SFT ( θ ) = − 𝔼 x ∼ 𝒟 x , y ∼ π θ ( ⋅ ∣ x ) [ w ( y ∣ x ) ∇ θ log π θ ( y ∣ x ) r ( x , y ) ] . \nabla_{\theta}\mathcal{L}_{\mathrm{SFT}}(\theta)=-\mathbb{E}_{x\sim\mathcal{D}_{x},\;y\sim\pi_{\theta}(\cdot\mid x)}\bigl[{\color[rgb]{0,0,1}w(y\mid x)}\,\nabla_{\theta}\log\pi_{\theta}(y\mid x)\,{\color[rgb]{0,0,1}r(x,y)}\bigr]. (6)

This form of the SFT gradient closely resembles the policy gradient in Equation equation 4 . Under this formulation, conventional SFT can be interpreted as an on-policy gradient method, where the reward is a sparse indicator function matching the expert trajectory, but biased by an importance weighting term 1 / π θ 1/\pi_{\theta} . We emphasize that this RL-style characterization serves solely as a theoretical lens: both the analysis and subsequent modifications are developed within the RL framework, while the final method remains fully implementable in standard SFT form for computational efficiency. Detailed derivations are provided in Appendix A.2 .

Due to the inherently sparse reward signal in the SFT setting, we identify the importance weight 1 / π θ 1/\pi_{\theta} as a key contributor to SFT’s generalization limitations compared to RL. When the model assigns low probability to the expert response, the resulting weight becomes excessively large, introducing an ill-posed reward landscape. This leads to disproportionately large gradients and training instability. The issue is compounded by the fact that the reward function r ( x , y ) = 𝟏 [ y = y ⋆ ] r(x,y)=\mathbf{1}[y=y^{\star}] is non-zero only for exact matches to the expert outputm causing optimization to overfit rare exact-match samples and weakening the model’s ability to generalize beyond the training data.

### 3.3 Proposed Method

#### Reward Rectification via Dynamic Reweighting.

To neutralize the skewed reward issue identified when viewing SFT under the RL objective, we dynamically reweight the reward by multiplying by a corrective inverse ratio given by the policy probability 1 / w 1/w . The resulting “dynamically fine-tuned” gradient is then

∇ θ ℒ SFT ( θ ) = − 𝔼 x ∼ 𝒟 x , y ∼ π θ ( ⋅ ∣ x ) [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇ θ log π θ ( y ∣ x ) r ( x , y ) ] . \nabla_{\theta}\mathcal{L}_{\mathrm{SFT}}(\theta)=-\mathbb{E}_{x\sim\mathcal{D}_{x},\;y\sim\pi_{\theta}(\cdot\mid x)}\bigl[\operatorname{sg}(\frac{1}{w})\cdot{\color[rgb]{0,0,1}w(y\mid x)}\,\nabla_{\theta}\log\pi_{\theta}(y\mid x)\,{\color[rgb]{0,0,1}r(x,y)}\bigr]. (7)

where sg ⁡ ( ⋅ ) \operatorname{sg}(\cdot) denotes the stop gradient operator, ensuring that gradients do not flow through the reward scaling term w w . To facilitate transition to later equations, we directly write 1 / w 1/w to be π θ ​ ( y ⋆ ∣ x ) \pi_{\theta}(y^{\star}\mid x) instead of π θ ​ ( y ∣ x ) \pi_{\theta}(y\mid x) because the indicator function in equation 5 or equation 6 would leave all cases where y ≠ y ⋆ y\neq y^{\star} is 0. Now since the gradient does not flow, the corrected SFT loss also becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT).

ℒ DFT ​ ( θ ) = 𝔼 ( x , y ⋆ ) ∼ 𝒟 ​ [ − sg ⁡ ( π θ ​ ( y ⋆ ∣ x ) ) ​ log ​ π θ ​ ( y ⋆ ∣ x ) ] . \mathcal{L}_{\text{DFT}}(\theta)=\mathbb{E}_{(x,y^{\star})\sim\mathcal{D}}\Bigl[-\operatorname{sg}\big(\pi_{\theta}(y^{\star}\mid x)\big)\log\pi_{\theta}(y^{\star}\mid x)\Bigr]. (8)

However, in practice, computing importance weights over the entire trajectory can induce numerical instability. A common treatment of this issue is to simply apply importance sampling at the token level, as was adopted in PPO ( Schulman et al., 2017 ) . This leads to the final DFT loss version:

ℒ DFT ( θ ) = 𝔼 ( x , y ⋆ ) ∼ 𝒟 [ − ∑ t = 1 | y ⋆ | sg ( π θ ( y t ⋆ ∣ y < t ⋆ , x ) ) log π θ ( y t ⋆ ∣ y < t ⋆ , x ) ] . \mathcal{L}_{\text{DFT}}(\theta)=\mathbb{E}_{(x,y^{\star})\sim\mathcal{D}}\Bigl[-\!\sum_{t=1}^{|y^{\star}|}\operatorname{sg}\big(\pi_{\theta}(y^{\star}_{t}\mid y^{\star}_{<t},x)\big)\log\pi_{\theta}(y^{\star}_{t}\mid y^{\star}_{<t},x)\Bigr]. (9)

Note that the reward of this corrected SFT (in RL form), i.e., DFT, now becomes 1 uniformly for all expert trajectory. This is akin to contemporary verification based reward approach RLVR ( DeepSeek-AI et al., 2025 ) that assigns uniform reward to all correct samples. Consequently, it avoids over-concentration on specific low-probability reference tokens, leading to more stable updates and improved generalization without introducing any additional sampling or reward models.

## 4 Experiments

We design four groups of experiments to comprehensively evaluate DFT. We first study the standard SFT setting on mathematical reasoning tasks to establish its core advantage over SFT (Section 4.1 ). We then extend to an offline RL setting, comparing DFT with representative offline and online RL methods (Section 4.2 ). To test cross-domain robustness, we further examine DFT on code generation benchmarks (Section 4.3 ) and its applicability to multi-modal reasoning math datasets (Section 4.4 ).

### 4.1 Main Experiment - Mathematical Reasoning Task

To examine whether DFT can outperform vanilla SFT across tasks, architectures, and scales, we use mathematical reasoning as a representative testbed.

#### Implementation details.

To efficiently manage computational resources, We andomly sample 100,000 instances from the the NuminaMath-CoT dataset ( LI et al., 2024 ) for training. We conduct experiments using multiple models, including Qwen2.5-Math-1.5B, Qwen2.5-Math-7B ( Qwen Team et al., 2024b ) , LLaMA-3.2-3B, LLaMA-3.1-8B ( Dubey et al., 2024 ) , and DeepSeekMath-7B ( Shao et al., 2024 ) . Our implementation builds upon the verl framework ( Sheng et al., 2025 ) , using recommended SFT hyper-parameters. Specifically, we employ the AdamW optimizer with learning rates of 5 × 10 − 5 5\times 10^{-5} for all models except the LLaMA-3.1-8B-Base, for which we adopt a lower learning rate of 2 × 10 − 5 2\times 10^{-5} . We set the mini-batch size to 256 and the maximum input length to 2048 tokens. The learning rate follows a cosine decay schedule with a warm-up ratio of 0.1. We evaluate on benchmarks including Math500 ( Hendrycks et al., 2021 ) , Minerva Math ( Lewkowycz et al., 2022 ) , Olympiad Bench ( He et al., 2024 ) , AIME 2024 ( American Institute of Mathematics, 2024 ) , and AMC 2023 ( Mathematical Association of America, 2023 ) through the official Qwen2.5-Math evaluation pipeline ( Qwen Team et al., 2024b ) . Each model uses the default chat template and Chain-of-Thought (CoT) prompting to stimulate step-by-step reasoning. All reported results represent average accuracy across 16 decoding runs, evaluated with a temperature of 1.0 and maximum generation length of 4096 tokens.

DFT consistently yields average performance improvements over base models compared to standard SFT across all benchmarks. Table 1 shows that, for Qwen2.5-Math-1.5B, DFT achieves an average gain of +15.66 points over the base model, which is over 5.9 × \times larger than the +2.09 point improvement from SFT. This pattern generalizes across other model families and sizes: LLaMA-3.2-3B benefits from a +3.46 point gain with DFT, exceeding the SFT gain (+2.05) by approximately 1.4 × \times ; LLaMA-3.1-8B achieves +10.02 from DFT, surpassing SFT’s +5.33 by 1.88 × \times ; DeepSeekMath-7B sees a +15.51 point improvement via DFT, which is 1.58 × \times larger than SFT’s +7.18; and Qwen2.5-Math-7B reaches a +15.90 point gain, nearly 3.8 × \times higher than the SFT improvement of +2.37.

DFT demonstrates generalization and robustness, especially on challenging benchmarks where standard SFT yields minimal or even negative impact. For instance, on Olympiad Bench, SFT degrades performance for Qwen2.5-Math-1.5B, dropping accuracy from 15.88 to 12.63, while DFT boosts it to 27.08, +11.20 point improvement over base model. On AIME24, SFT reduces accuracy for Qwen2.5-Math-7B by 4.20 points (from 6.68 to 2.48), whereas DFT improves performance to 8.56, achieving a +1.88 point gain over the base model despite the difficulty of the benchmark. A similar trend is observed on AMC23. SFT reduces the performance of Qwen2.5-Math-1.5B from 19.38 to 18.75, while DFT raises it to 38.13, a +18.75 point gain over base. For Qwen2.5-Math-7B, SFT yields only a marginal improvement (+1.86), whereas DFT achieves a +17.04 point gain. These results underscore that DFT not only scales more effectively across models of varying capacities, but also exhibits better resilience on difficult reasoning tasks where traditional SFT struggles.

DFT exhibits better learning efficiency and faster convergence characteristics. Figure 1 reveals clear differences in learning dynamics between DFT and standard SFT on Qwen2.5-Math-1.5B across all math reasoning benchmarks. Compared to SFT, our method demonstrates three distinct advantages: (1) Faster convergence, achieving peak performance within the first 120 training steps on most benchmarks; (2) Better early-stage performance, with DFT already outperforming best final accuracy of SFT within the first 10–20 steps; and (3) Higher sample efficiency, consistently requiring fewer updates to reach relatively optimal results. This accelerated convergence shows that the dynamic reweighting mechanism in DFT leads to more informative gradient updates, guiding the model toward high-quality solutions early in training. It also suggests that DFT helps avoid the optimization plateaus or noise-prone regions often encountered in standard SFT, thereby enabling more efficient acquisition of complex mathematical reasoning patterns.

We also report the results of parameter-efficient fine-tuning (PEFT) training setting ( Hu et al., 2022 ) and training on the OpenR1-Math dataset ( Hugging Face, 2025 ) with better quality in Appendix A.6 and Appendix A.5 , respectively. Comparison and Discussion with the concurrent method iw-SFT ( Qin and Springenberg, 2025 ) is provided in Appendix A.4 .

### 4.2 Exploratory Experiment - Offline RL Setting

Equation 7 shows that SFT suffers from reward sparsity, since in a constructed dataset each query x x has only a single reference answer y ⋆ y^{\star} . From the perspective of RL, RFT/RAFT ( Dong et al., 2023 ; Ahn et al., 2024 ) can be viewed as alleviating the sparse reward issue by effectively increasing reward density, thereby enhancing model performance. Motivated by this observation, we conduct an exploratory study applying DFT in an offline RL setting, where the reward sparsity problem is inherently less severe compared to standard SFT, to further validate the effectiveness.

#### Implementation details.

We sample responses for 100,000 math questions using a temperature of 1.0 and generate four responses per question from the base model itself. Correct responses are identified using math verify and retained as training data, resulting in approximately 140,000 examples. For DPO training, we construct 100,000 positive–negative preference pairs from the generated responses. We compare DFT with representative offline RL methods, including DPO ( Rafailov et al., 2023 ) and RFT ( Dong et al., 2023 ; Ahn et al., 2024 ) , as well as online RL methods PPO ( Schulman et al., 2017 ) and GRPO ( Shao et al., 2024 ) . For RFT and DFT, the training setup follows the configuration in Section 4.1 . For DPO, we use the ms-swift ( Zhao et al., 2024 ) with a learning rate of 1 × 10 − 6 1\times 10^{-6} , batch size of 128, and a warmup ratio of 0.05. For PPO and GRPO, training is performed using the verl ( Sheng et al., 2025 ) with a learning rate of 1 × 10 − 6 1\times 10^{-6} , batch size of 256, and a warmup ratio of 0.1. We set the number of response n = 4 n=4 for GRPO.

DFT demonstrates competitive performance in the offline RL setting, outperforming both offline and online RL baselines. Table 2 shows DFT achieves an average score of 35.43, exceeding the best offline method RFT by +11.46 points, and even outperforming the strongest online RL algorithm GRPO by +3.43 points. Specially, on Math500, DFT scores 64.71, slightly ahead of GRPO (62.86) and better than PPO (56.10) and RFT (48.23). The gains are also notable on more challenging benchmarks: on AMC23, DFT achieves 48.44, a +7.19 point margin over GRPO and a +17.66 point gain over RFT. Similarly, on Minerva Math, DFT reaches 25.16, outperforming GRPO by +6.23 points, PPO by +9.75, and all offline baseline methods.

These results highlight the strength of DFT as a simple yet effective fine-tuning strategy. Despite its lack of iterative reward modeling or environment interaction, it provides a stronger learning signal than both offline methods like DPO/RFT and online policy optimization algorithms like PPO/GRPO in certain scale train set. This suggests that DFT can serve as a more efficient and scalable alternative to traditional RL pipelines, particularly in domains where preference supervision is available but reward modeling or online response sampling is expensive or impractical.

### 4.3 Exploratory Experiment - Code Generation Task

#### Implementation details.

We adopt UltraFeedback ( Cui et al., 2024 ) as the training dataset. From this corpus, we sample 10,000 prompts and, for each prompt, select the response with the highest average score to perform supervised fine-tuning (SFT) ( Du and others, 2025 ) . Model performance is assessed on three widely used code generation benchmarks: HumanEval ( Chen et al., 2021 ) , HumanEval+ ( Liu et al., 2023 ) , and MultiPL-E ( Cassano et al., 2023 ) . Training is conducted for one epoch with a learning rate of 5 × 10 − 5 5\times 10^{-5} , a warm-up ratio of 0.05, and a batch size of 16.

Table 3 shows DFT achieves improvements in most cases compared to both base models and SFT. For Qwen2.5-3B, DFT raises HumanEval from 43.3 to 45.7 and HumanEval+ from 36.0 to 39.0, with the MultiPL-E average also increasing from 40.05 (base) and 39.10 (SFT) to 41.84. Similar trends are observed for Qwen2.5-Coder-3B, where DFT improves HumanEval to 56.7 and HumanEval+ to 50.0, outperforming both base and SFT. For Qwen2.5-Coder-7B, DFT reaches 67.7 on HumanEval, 59.8 on HumanEval+, and 62.3 average on MultiPL-E, surpassing SFT by +12.8, +11.0, and +4.7 points respectively. The overall trend demonstrates that DFT generally provides stronger performance across different models and languages.

### 4.4 Exploratory Experiment - Multi-Modal Reasoning

#### Implementation details.

We use the WeThink dataset ( Yang et al., 2025 ) for training. The model is fine-tuned using LLaMA-Factory ( Zheng et al., 2024 ) and evaluated with VLMEvalKit ( Duan et al., 2024 ) . We train the model for 1 epoch with a learning rate of 5e-5. To comprehensively assess reasoning capabilities, we adopt a suite of multi-modal reasoning benchmarks including MathVerse ( Zhang et al., 2024b ) , MathVision ( Wang et al., 2024 ) , and WeMath ( Qiao et al., 2024 ) for evaluation.

DFT achieves consistent improvements over base models and SFT across all multi-modal reasoning benchmarks. Table 4 shows, on MathVerse, DFT boosts Qwen2.5-VL-3B from 33.83 to 37.54 average accuracy, outperforming the SFT gain of only +1.83 by +3.71 points. Consistent improvements are observed across all major vision-related subcategories. On MathVision, DFT improves performance from 21.25 (base) to 22.30, exceeding SFT which fails to provide gains (21.02). On WeMath, SFT already yields a +19.23 point gain, but DFT pushes performance slightly further to 23.71, maintaining superiority over both base and SFT. These results indicate that DFT not only strengthens text-only reasoning but also extends effectively to multi-modal domains.

### 4.5 Limitations of DFT: A Case Study on Factual Knowledge

While DFT consistently outperforms SFT on reasoning-heavy tasks, it may not always be the better choice, particularly in factual knowledge domains. We conduct an exploratory experiment on the Natural Questions dataset ( Kwiatkowski et al., 2019 ) , which consists of real-user, open-domain factual queries grounded in Wikipedia articles.

In this setting, we find that SFT improves performance from 31.24% to 36.62%, while DFT unexpectedly reduces it to 30.14%. This result reveals an important limitation of DFT: because it reweights samples based on the model’s own confidence, it tends to reinforce the model’s existing beliefs. When the model lacks sufficient factual knowledge, such reinforcement may hinder effective learning instead of facilitating it.

This case suggests that DFT is most effective when the task aligns well with the model’s prior competence, such as logical reasoning or structured prediction. In contrast, when the objective is to absorb new factual information, especially in domains beyond the model’s current capabilities, SFT remains a more reliable and stable fine-tuning strategy.

### 4.6 An Empirical Comparison with Sentence-Level Weighting

Our framework applies confidence-based weighting at the token level. While this design was primarily motivated by numerical stability, we also compared it against two sentence-level variants to better understand their behavior.

The first variant uses the full sequence probability to scale the loss. However, these values are extremely small in practice, making the loss nearly uninformative and producing a highly skewed weight distribution that is difficult to tune. To address this, we also evaluated a geometric-mean variant inspired by GSPO ( Zheng et al., 2025 ) , which rescales sentence probabilities to avoid numerical collapse. Although this version is more stable, it still provides a weak training signal and offers limited performance gains.

As shown in Table 5 , both sentence-level strategies lead to minimal changes over the base model, while our token-level formulation delivers substantial and consistent improvements, raising average accuracy from 15.92 to 31.58. These results demonstrate that token-level weighting provides a more reliable optimization signal and significantly stronger empirical performance.

### 4.7 Analysis of Probabilities

To understand how the model trained by DFT is different from SFT and other RL methods, we look into the token probability distribution of the model’s output over the training set in Figure 2 . SFT tends to uniformly increase token probabilities, shifting the entire distribution towards higher confidence, but mainly targeting the lower and lowest probability tokens. The highest probability token portion barely increases. In stark contrast, DFT exhibits a polarizing effect: it significantly boosts the probabilities of a subset of tokens while actively suppressing the probabilities of others. This leads to a bimodal distribution, with more tokens occupying both the highest and lowest probability bins. Other RL methods such as DPO, GPPO and PPO show the same trend as DFT, although the scale is much milder than it. We look into the words that belong to the lowest probability bin, and find that they are generally the conjunctive words or punctuations such as ‘the’, ‘let’, ‘,’, ‘.’ etc. These results suggest that for robust learning, models should not attempt to fit all tokens with uniform confidence. It may be beneficial to deprioritize fitting tokens that serve grammatical functions rather than carrying primary semantic content. This concept is analogous to human pedagogy, where students are taught to focus on substantive concepts rather than perfecting the usage of common connective words. Further analysis can be found in Appendix A.3 .

## 5 Conclusion

In this work, we revisit the well-known generalization gap between SFT and RL. We offer a theoretical perspective showing that the standard SFT gradient can be interpreted as a policy gradient with an ill-posed, implicitly defined reward inversely related to model confidence. This formulation helps explain the instability and limited generalization observed in SFT training. Motivated by this analysis, we introduce DFT, a simple yet effective method that dynamically reweights the SFT loss using the token probability. This one-line change improves gradient stability and leads to better generalization. Our empirical results show that DFT consistently improves over standard SFT across a range of models and challenging mathematical reasoning tasks. Beyond supervised settings, we adapt DFT to offline RL scenarios and find that it outperforms several established online and offline RL baselines, suggesting broader applicability. Overall, this work contributes both a refined understanding of SFT’s limitations and a lightweight, practical method that helps bridge the gap to more complex RL-based approaches.

#### Limitations.

While our experiments demonstrate the effectiveness of DFT on mathematical reasoning benchmarks and code generation tasks, the evaluation scope remains limited. We have not yet assessed its performance on broader task categories or with larger-scale LLM, which we leave for future exploration. Moreover, DFT can not offer universal benefits across all scenarios. In domains that primarily involve the acquisition of factual knowledge, conventional SFT still remains the most efficient approach. DFT may also not be an ideal choice for hard examples or domains underrepresented in the training data, since it assigns low initial probabilities to such samples, reducing their learning weight. Our aim is not to assert that DFT universally outperforms SFT, but rather to offer a new perspective on objective design by analyzing the distinction between RL and SFT. Besides, an important future direction is to explore non-uniform or quality-aware reward assignments for demonstrations.

## Acknowledgements

Supported by Jiangsu Province Carbon Peak Carbon Neutrality Science and Technology Innovation Special Fund Project (Grant No. BT2025029), National Natural Science Foundation of China (Grant No. 62576091), and Big Data Computing Center of Southeast University.

## Ethics Statement

This work adheres to the ICLR Code of Ethics. Our study does not involve human subjects, personally identifiable information, or proprietary data. All datasets used, including NuminaMath, OpenR1-Math, UltraFeedback, and WeThink, are publicly available and documented in the appendix. The proposed method is a simple training strategy that modifies gradient computation for improved generalization. It does not introduce any new capabilities that could cause harm, nor does it enable misuse beyond the standard capabilities of existing large language models. We are not aware of any potential risks related to bias, fairness, or security that arise specifically from the method proposed. Nonetheless, we acknowledge that like any fine-tuning strategy, DFT may inherit biases present in the underlying data or model, and future research may explore safeguards for these scenarios. No conflicts of interest, legal compliance issues, or sponsorship-related influences are present in this work.

## Reproducibility Statement

We have taken multiple steps to ensure the reproducibility of our work. All datasets used in our experiments are publicly available and properly cited in the main text and appendix. Training configurations, including model architectures, hyperparameters, optimizers, and evaluation settings, are described in detail in Section 4 and Appendi A.5 - A.6 . Theoretical claims, including the equivalence between SFT and policy gradient, are formally derived in Appendix A.2 . Experimental results include multiple model scales, tasks, and training settings to validate robustness. A complete implementation of our method is included in the supplementary material, along with scripts for reproducing all reported results. We will release the full source code and training logs upon publication to further support reproducibility.

## References

Abdolmaleki et al. (2025) A. Abdolmaleki, B. Piot, B. Shahriari, J. T. Springenberg, T. Hertweck, M. Bloesch, R. Joshi, T. Lampe, J. Oh, N. Heess, et al. Learning from negative feedback, or positive feedback or both . In ICLR , Cited by: §2 .

Ahn et al. (2024) J. Ahn, R. Verma, R. Lou, D. Liu, R. Zhang, and W. Yin Large language models for mathematical reasoning: progresses and challenges . In EACLW , pp. 225–237 . Cited by: §1 , §4.2 , §4.2 .

American Institute of Mathematics (2024) American Institute of Mathematics AIME 2024 competition mathematical problems . Cited by: §1 , §4.1 .

Bai et al. (2022) Y. Bai, A. Jones, K. Ndousse, A. Askell, A. Chen, N. Dasgupta, D. Drain, S. Fort, D. Ganguli, T. Hase, et al. Training a helpful and harmless assistant with reinforcement learning from human feedback . arXiv preprint arXiv:2204.05862 . Cited by: §1 , §2 .

Cassano et al. (2023) F. Cassano, J. Gouwar, D. Nguyen, S. Nguyen, L. Phipps-Costin, D. Pinckney, M. Yee, Y. Zi, C. J. Anderson, M. Q. Feldman, et al. Multipl-e: a scalable and polyglot approach to benchmarking neural code generation . IEEE Transactions on Software Engineering 49 ( 7 ), pp. 3675–3691 . Cited by: §4.3 .

Chai et al. (2024) W. Chai, E. Song, Y. Du, C. Meng, V. Madhavan, O. Bar-Tal, J. Hwang, S. Xie, and C. D. Manning Auroracap: efficient, performant video detailed captioning and a new benchmark . arXiv preprint arXiv:2410.03051 . Cited by: §2 .

Chen et al. (2025a) H. Chen, P. Fang, Y. Chen, Y. Ren, J. Hao, F. Tang, X. Cai, S. Shan, and F. Liu HiFi-mamba: dual-stream w-laplacian enhanced mamba for high-fidelity mri reconstruction . arXiv preprint arXiv:2508.09179 . Cited by: §1 .

Chen et al. (2025b) H. Chen, K. Zheng, Q. Zhang, G. Cui, Y. Cui, H. Ye, T. Lin, M. Liu, J. Zhu, and H. Wang Bridging supervised learning and reinforcement learning in math reasoning . arXiv preprint arXiv:2505.18116 . Cited by: §2 .

Chen et al. (2021) M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al. Evaluating large language models trained on code . arXiv preprint arXiv:2107.03374 . Cited by: §4.3 .

Chen et al. (2024) Y. Chen, P. Fang, X. Zhong, J. Yu, X. Zhang, and T. Li Hi-resnet: edge detail enhancement for high-resolution remote sensing segmentation . IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 17 , pp. 15024–15040 . Cited by: §1 .

Chen et al. (2025c) Z. Chen, Y. Min, B. Zhang, J. Chen, J. Jiang, D. Cheng, W. X. Zhao, Z. Liu, X. Miao, Y. Lu, L. Fang, Z. Wang, and J. Wen An empirical study on eliciting and improving r1-like reasoning models . arXiv preprint arXiv:2503.04548 . Cited by: §1 .

Christiano et al. (2017) P. F. Christiano, J. Leike, T. Brown, M. Martic, S. Legg, and D. Amodei Deep reinforcement learning from human preferences . In NeurIPS , Vol. 30 . Cited by: §1 , §2 .

Chu et al. (2024) T. Chu, Y. Zhai, J. Yang, S. Tong, S. Xie, D. Schuurmans, Q. V. Le, S. Levine, and Y. Ma SFT memorizes, rl generalizes: a comparative study of foundation model post-training . In ICML , Cited by: §1 , §2 .

Chung et al. (2024) H. W. Chung, L. Hou, S. Longpre, B. Zoph, Y. Tay, W. Fedus, Y. Li, X. Wang, M. Dehghani, S. Brahma, et al. Scaling instruction-finetuned language models . Journal of Machine Learning Research 25 ( 70 ), pp. 1–53 . Cited by: §1 , §2 .

Cui et al. (2024) G. Cui, L. Yuan, N. Ding, G. Yao, B. He, W. Zhu, Y. Ni, G. Xie, R. Xie, Y. Lin, et al. ULTRAFEEDBACK: boosting language models with scaled ai feedback . In ICML , pp. 9722–9744 . Cited by: §4.3 .

DeepSeek-AI et al. (2025) DeepSeek-AI, D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Bao, H. Xu, H. Wang, H. Ding, H. Xin, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Wang, J. Chen, J. Yuan, J. Qiu, J. Li, J. L. Cai, J. Ni, J. Liang, J. Chen, K. Dong, K. Hu, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang, L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Li, M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang, Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang, R. J. Chen, R. L. Jin, R. Chen, S. Lu, S. Zhou, S. Chen, S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, S. Ye, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng, W. Zhao, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang, W. L. Xiao, W. An, X. Liu, X. Wang, X. Chen, X. Nie, X. Cheng, X. Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su, X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun, X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li, Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi, Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Xu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma, Y. Tang, Y. Zha, Y. Yan, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu, Z. Xie, Z. Zhang, Z. Hao, Z. Ma, Z. Yan, Z. Wu, Z. Gu, Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Pan, Z. Huang, Z. Xu, Z. Zhang, and Z. Zhang DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning . External Links: 2501.12948 Cited by: §A.5 , §3.3 .

Dong et al. (2023) H. Dong, W. Xiong, D. Goyal, Y. Zhang, W. Chow, R. Pan, S. Diao, J. Zhang, K. Shum, and T. Zhang RAFT: reward ranked finetuning for generative foundation model alignment . Transactions on Machine Learning Research 2023 . Cited by: §1 , §4.2 , §4.2 .

Du et al. (2025) Y. Du et al. Simplify rlhf as reward-weighted sft: a variational method . arXiv preprint arXiv:2502.11026 . Cited by: §2 , §4.3 .

Duan et al. (2024) H. Duan, J. Yang, Y. Qiao, X. Fang, L. Chen, Y. Liu, X. Dong, Y. Zang, P. Zhang, J. Wang, et al. Vlmevalkit: an open-source toolkit for evaluating large multi-modality models . In ACM MM , pp. 11198–11201 . Cited by: §4.4 .

Dubey et al. (2024) A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Yang, A. Fan, et al. The llama 3 herd of models . arXiv preprint arXiv:2407.21783 . Cited by: §4.1 .

Fang et al. (2025) P. Fang, Y. Chen, and R. Guo When and what: diffusion-grounded videollm with entity aware segmentation for long video understanding . arXiv preprint arXiv:2508.15641 . Cited by: §1 .

Freund (2009) Y. Freund A more robust boosting algorithm . arXiv preprint arXiv:0905.2138 . Cited by: §A.3 .

He et al. (2024) C. He, R. Luo, Y. Bai, S. Hu, Z. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, et al. OlympiadBench: a challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems . In ACL , pp. 3828–3850 . Cited by: §1 , §4.1 .

He et al. (2025) X. He, S. Fu, Y. Zhao, W. Li, J. Yang, D. Yin, F. Rao, and B. Zhang Tempflow-grpo: when timing matters for grpo in flow models . arXiv preprint arXiv:2508.04324 . Cited by: §1 .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt Measuring mathematical problem solving with the math dataset . In NeurIPS , Cited by: §4.1 .

Hu et al. (2022) E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al. Lora: low-rank adaptation of large language models. . ICLR 1 ( 2 ), pp. 3 . Cited by: §4.1 .

Huan et al. (2025) M. Huan, Y. Li, T. Zheng, X. Xu, S. Kim, M. Du, R. Poovendran, G. Neubig, and X. Yue Does math reasoning improve general llm capabilities? understanding transferability of llm reasoning . arXiv preprint arXiv:2507.00432 . Cited by: §1 .

Hugging Face (2025) Hugging Face Open r1: a fully open reproduction of deepseek-r1 . Cited by: §A.5 , §4.1 .

Kantharaju and Sankar (2022) P. Kantharaju and A. Sankar An understanding of learning from demonstrations for neural text generation . In ICLR Blog Track , Note: https://iclr-blog-track.github.io/2022/03/25/text-gen-via-lfd/ External Links: Link Cited by: §2 .

Kwiatkowski et al. (2019) T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikh, C. Alberti, D. Epstein, I. Polosukhin, J. Devlin, K. Lee, et al. Natural questions: a benchmark for question answering research . Transactions of the Association for Computational Linguistics 7 , pp. 453–466 . Cited by: §4.5 .

Levine et al. (2020) S. Levine, A. Kumar, G. Tucker, and J. Fu Offline reinforcement learning: tutorial, review, and perspectives on open problems . arXiv preprint arXiv:2005.01643 . Cited by: §1 .

Lewkowycz et al. (2022) A. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski, V. Ramasesh, A. Slone, C. Anil, I. Schlag, T. Gutman-Solo, et al. Solving quantitative reasoning problems with language models . NeurIPS 35 , pp. 3843–3857 . Cited by: §4.1 .

LI et al. (2024) J. LI, E. Beeching, L. Tunstall, B. Lipkin, R. Soletskyi, S. C. Huang, K. Rasul, L. Yu, A. Jiang, Z. Shen, Z. Qin, B. Dong, L. Zhou, Y. Fleureau, G. Lample, and S. Polu NuminaMath . Cited by: §1 , §4.1 .

Li et al. (2025a) O. Li, Y. Wang, X. Hu, H. Huang, R. Chen, J. Ou, X. Tao, P. Wan, X. Qi, and F. Feng Easier painting than thinking: can text-to-image models set the stage, but not direct the play? . arXiv preprint arXiv:2509.03516 . Cited by: §1 .

Li et al. (2025b) O. Li, Y. Wang, X. Hu, H. Jiang, T. Liang, Y. Hao, G. Ma, and F. Feng Speed: scalable, precise, and efficient concept erasure for diffusion models . arXiv preprint arXiv:2503.07392 . Cited by: §1 .

Lin et al. (2017) T. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár Focal loss for dense object detection . In ICCV , pp. 2999–3007 . Cited by: §2 .

Liu et al. (2023) J. Liu, C. S. Xia, Y. Wang, and L. Zhang Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation . NeurIPS 36 , pp. 21558–21572 . Cited by: §4.3 .

Liu et al. (2025) M. Liu, G. Farina, and A. Ozdaglar UFT: unifying supervised and reinforcement fine-tuning . arXiv preprint arXiv:2505.16984 . Cited by: §1 , §2 .

Liu and Yin (2024) V. Liu and Y. Yin Green ai: exploring carbon footprints, mitigation strategies, and trade offs in large language model training . Discover Artificial Intelligence 4 ( 49 ). Cited by: §1 .

Luo et al. (2025) G. Luo, X. Yang, W. Dou, Z. Wang, J. Liu, J. Dai, Y. Qiao, and X. Zhu Mono-internvl: pushing the boundaries of monolithic multimodal large language models with endogenous visual pre-training . In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pp. 24960–24971 . Cited by: §1 .

Mandlekar et al. (2022) A. Mandlekar, D. Xu, J. Wong, S. Nasiriany, C. Wang, R. Kulkarni, L. Fei-Fei, S. Savarese, Y. Zhu, and R. Martín-Martín What matters in learning from offline human demonstrations for robot manipulation . In CoRL , pp. 1678–1690 . Cited by: §1 , §2 .

Mathematical Association of America (2023) Mathematical Association of America AMC 2023 competition problems . Cited by: §1 , §4.1 .

Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback . NeurIPS 35 , pp. 27730–27744 . Cited by: §1 , §1 , §2 , §2 .

Pang and He (2021) R. Y. Pang and H. He TEXT generation by learning from demonstrations . In ICLR , Cited by: §2 .

Pascanu et al. (2013) R. Pascanu, T. Mikolov, and Y. Bengio On the difficulty of training recurrent neural networks . In ICML , pp. 1310–1318 . Cited by: §1 .

Qiao et al. (2024) R. Qiao, Q. Tan, G. Dong, M. Wu, C. Sun, X. Song, Z. GongQue, S. Lei, Z. Wei, M. Zhang, et al. We-math: does your large multimodal model achieve human-like mathematical reasoning? . arXiv preprint arXiv:2407.01284 . Cited by: §4.4 .

Qin and Springenberg (2025) C. Qin and J. T. Springenberg Supervised fine tuning on curated data is reinforcement learning (and can be improved) . arXiv preprint arXiv:2507.12856 . Cited by: §A.4 , §2 , §4.1 .

Qiu et al. (2025) H. Qiu, X. Lan, F. Liu, X. Sun, D. Ruan, P. Shi, and L. Ma Metis-rise: rl incentivizes and sft enhances multimodal reasoning model learning . arXiv preprint arXiv:2506.13056 . Cited by: §1 , §2 .

Qwen Team et al. (2024a) Qwen Team, A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, et al. Qwen2.5 technical report . arXiv preprint arXiv:2412.15115 . Cited by: §1 .

Qwen Team et al. (2024b) Qwen Team, A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, et al. Qwen2.5: a party of foundation models . arXiv preprint arXiv:2412.15115 . Cited by: §4.1 .

Rafailov et al. (2023) R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn Direct preference optimization: your language model is secretly a reward model . In NeurIPS , Vol. 36 . Cited by: §1 , §1 , §2 , §4.2 .

Sammut (2011) C. Sammut Behavioral cloning . Cited by: §2 .

Sanh et al. (2022) V. Sanh, A. Webson, C. Raffel, S. Bach, L. Sutton, Z. Alyafeai, A. Chaffin, A. Stiegler, T. L. Scao, A. Raja, et al. Multitask prompted training enables zero-shot task generalization . In ICLR , Cited by: §1 .

Sasaki and Yamashina (2020) F. Sasaki and R. Yamashina Behavioral cloning from noisy demonstrations . In ICLR , Cited by: §A.3 .

Schulman et al. (2017) J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov Proximal policy optimization algorithms . arXiv preprint arXiv:1707.06347 . Cited by: §1 , §2 , §3.3 , §4.2 .

Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. Deepseekmath: pushing the limits of mathematical reasoning in open language models . arXiv preprint arXiv:2402.03300 . Cited by: §4.1 , §4.2 .

Sheng et al. (2025) G. Sheng, C. Zhang, Z. Ye, X. Wu, W. Zhang, R. Zhang, Y. Peng, H. Lin, and C. Wu Hybridflow: a flexible and efficient rlhf framework . In ECCV , pp. 1279–1297 . Cited by: §1 , §1 , §2 , §2 , §4.1 , §4.2 .

Song et al. (2024) E. Song, W. Chai, G. Wang, Y. Zhang, H. Zhou, F. Wu, H. Chi, X. Guo, T. Ye, Y. Zhang, et al. Moviechat: from dense token to sparse memory for long video understanding . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 18221–18232 . Cited by: §2 .

Song et al. (2025a) E. Song, W. Chai, W. Xu, J. Xie, Y. Liu, and G. Wang Video-mmlu: a massive multi-discipline lecture understanding benchmark . In Proceedings of the IEEE/CVF International Conference on Computer Vision , pp. 6099–6113 . Cited by: §2 .

Song et al. (2025b) E. Song, W. Chai, S. Yang, E. Armand, X. Shan, H. Xu, J. Xie, and Z. Tu Videonsa: native sparse attention scales video understanding . arXiv preprint arXiv:2510.02295 . Cited by: §2 .

Song et al. (2025c) E. Song, W. Chai, T. Ye, J. Hwang, X. Li, and G. Wang Moviechat+: question-aware sparse memory for long video question answering . IEEE Transactions on Pattern Analysis and Machine Intelligence . Cited by: §2 .

Strubell et al. (2019) E. Strubell, A. Ganesh, and A. McCallum Energy and policy considerations for deep learning in nlp . In ACL , pp. 3645–3650 . Cited by: §1 , §2 .

Swamy et al. (2025) G. Swamy, S. Choudhury, W. Sun, Z. S. Wu, and J. A. Bagnell All roads lead to likelihood: the value of reinforcement learning in fine-tuning . arXiv preprint arXiv:2503.01067 . Cited by: §1 , §2 .

Tan et al. (2026) X. Tan, W. Weng, H. Lei, and H. Wang EasyTune: efficient step-aware fine-tuning for diffusion-based motion generation . arXiv preprint arXiv:2602.07967 . Cited by: §1 .

Wang et al. (2025a) B. Wang, Q. Cheng, R. Peng, R. Bao, P. Li, Q. Guo, L. Li, Z. Zeng, Y. Zhou, and X. Qiu Implicit reward as the bridge: a unified view of sft and dpo connections . arXiv preprint arXiv:2507.00018 . Cited by: §2 .

Wang et al. (2024) K. Wang, J. Pan, W. Shi, Z. Lu, H. Ren, A. Zhou, M. Zhan, and H. Li Measuring multimodal mathematical reasoning with math-vision dataset . In NeurIPS , Cited by: §4.4 .

Wang et al. (2025b) Z. Wang, J. Wu, Y. Lai, C. Zhang, and D. Zhou Seed: accelerating reasoning tree construction via scheduled speculative decoding . In Proceedings of the 31st International Conference on Computational Linguistics , pp. 4920–4937 . Cited by: §1 .

Wei et al. (2022) J. Wei, M. Bosma, V. Zhao, K. Guu, A. W. Yu, B. Lester, N. Du, A. M. Dai, and Q. V. Le Finetuned language models are zero-shot learners . In ICLR , Cited by: §1 , §2 .

Winsta (2025) J. Winsta The hidden costs of ai: a review of energy, e-waste, and inequality in model development . arXiv preprint arXiv:2507.09611 . Cited by: §1 .

Xu et al. (2025) W. Xu, E. Song, W. Chai, X. Wen, T. Ye, and G. Wang Auroralong: bringing rnns back to efficient open-ended video understanding . arXiv preprint arXiv:2507.02591 . Cited by: §2 .

Yan et al. (2025) J. Yan, Y. Li, Z. Hu, Z. Wang, G. Cui, X. Qu, Y. Cheng, and Y. Zhang Learning to reason under off-policy guidance . arXiv preprint arXiv:2504.14945 . Cited by: §A.5 .

Yang et al. (2019) G. Yang, J. Pennington, V. Rao, J. Sohl-Dickstein, and S. S. Schoenholz A mean field theory of batch normalization . In ICLR , Cited by: §1 .

Yang et al. (2025) J. Yang, F. Ma, Z. Wang, D. Yin, K. Rong, F. Rao, and R. Zhang WeThink: toward general-purpose vision-language reasoning via reinforcement learning . arXiv preprint arXiv:2506.07905 . Cited by: §4.4 .

Zhang et al. (2025a) C. Zhang, J. Peng, Z. Wang, Y. Lai, H. Sun, H. Chang, F. Ma, and W. Yu Vrest: enhancing reasoning in large vision-language models through tree search and self-reward mechanism . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 3922–3941 . Cited by: §1 .

Zhang et al. (2025b) C. Zhang, Z. Wang, Y. Ma, J. Peng, Y. Wang, Q. Zhou, J. Song, and B. Zheng ReWatch-r1: boosting complex video reasoning in large vision-language models through agentic data synthesis . arXiv preprint arXiv:2509.23652 . Cited by: §1 .

Zhang et al. (2025c) C. Zhang, L. Zhang, J. Wu, Y. He, and D. Zhou Causal prompting: debiasing large language model prompting based on front-door adjustment . In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 39 , pp. 25842–25850 . Cited by: §1 .

Zhang et al. (2024a) C. Zhang, L. Zhang, and D. Zhou Causal walk: debiasing multi-hop fact verification with front-door adjustment . In Proceedings of the AAAI conference on artificial intelligence , Vol. 38 , pp. 19533–19541 . Cited by: §1 .

Zhang et al. (2025d) Q. Zhang, H. Wu, C. Zhang, P. Zhao, and Y. Bian Right question is already half the answer: fully unsupervised llm reasoning incentivization . arXiv preprint arXiv:2504.05812 . Cited by: §2 .

Zhang et al. (2024b) R. Zhang, D. Jiang, Y. Zhang, H. Lin, Z. Guo, P. Qiu, A. Zhou, P. Lu, K. Chang, Y. Qiao, et al. Mathverse: does your multi-modal llm truly see the diagrams in visual math problems? . In ECCV , pp. 169–186 . Cited by: §4.4 .

Zhang et al. (2024c) S. Zhang, L. Dong, X. Li, S. Zhang, X. Sun, S. Wang, J. Li, R. Hu, T. Zhang, F. Wu, and G. Wang Instruction tuning for large language models: a survey . arXiv preprint arXiv:2308.10792 . Cited by: §1 .

Zhang et al. (2023) S. Zhang, S. Wu, O. Irsoy, S. Lu, M. Bansal, M. Dredze, and D. Rosenberg MIXCE: training autoregressive language models by mixing forward and reverse cross-entropies . In ACL , pp. 9027–9050 . Cited by: §2 .

Zhao et al. (2025a) K. Zhao, J. Shi, B. Zhu, J. Zhou, X. Shen, Y. Zhou, Q. Sun, and H. Zhang Real-time motion-controllable autoregressive video diffusion . arXiv preprint arXiv:2510.08131 . Cited by: §1 .

Zhao et al. (2025b) K. Zhao, B. Zhu, Q. Sun, and H. Zhang Unsupervised visual chain-of-thought reasoning via preference optimization . arXiv preprint arXiv:2504.18397 . Cited by: §1 .

Zhao et al. (2025c) X. Zhao, J. Lin, T. Liang, Y. Zhou, W. Chai, Y. Gu, W. Wang, K. Chen, G. Luo, W. Zhang, et al. MM-helix: boosting multimodal long-chain reflective reasoning with holistic platform and adaptive hybrid policy optimization . arXiv preprint arXiv:2510.08540 . Cited by: §2 .

Zhao et al. (2025d) X. Zhao, P. Zhang, K. Tang, X. Zhu, H. Li, W. Chai, Z. Zhang, R. Xia, G. Zhai, J. Yan, et al. Envisioning beyond the pixels: benchmarking reasoning-informed visual editing . arXiv preprint arXiv:2504.02826 . Cited by: §1 .

Zhao et al. (2024) Y. Zhao, J. Huang, J. Hu, X. Wang, Y. Mao, D. Zhang, Z. Jiang, Z. Wu, B. Ai, A. Wang, W. Zhou, and Y. Chen SWIFT:a scalable lightweight infrastructure for fine-tuning . External Links: 2408.05517 Cited by: §4.2 .

Zheng et al. (2025) C. Zheng, S. Liu, M. Li, X. Chen, B. Yu, C. Gao, K. Dang, Y. Liu, R. Men, A. Yang, et al. Group sequence policy optimization . arXiv preprint arXiv:2507.18071 . Cited by: §4.6 .

Zheng et al. (2024) Y. Zheng, R. Zhang, J. Zhang, Y. YeYanhan, and Z. Luo LlamaFactory: unified efficient fine-tuning of 100+ language models . In ACL , pp. 400–410 . Cited by: §4.4 .

Zhou et al. (2023) C. Zhou, P. Liu, P. Xu, S. Iyer, J. Sun, Y. Mao, X. Ma, A. Efrat, P. Yu, L. Yu, et al. LIMA: less is more for alignment . In NeurIPS , Vol. 36 . Cited by: §1 , §2 .

Zhu et al. (2024a) X. Zhu, S. Wang, J. Lu, Y. Hao, H. Liu, and X. He Boosting few-shot learning via attentive feature regularization . In Proceedings of the AAAI conference on artificial intelligence , Vol. 38 , pp. 7793–7801 . Cited by: §1 .

Zhu et al. (2025a) X. Zhu, S. Wang, B. Zhu, M. Li, Y. Li, J. Fang, Z. Wang, D. Wang, and H. Zhang Dynamic multimodal prototype learning in vision-language models . In Proceedings of the IEEE/CVF international conference on computer vision , pp. 2501–2511 . Cited by: §2 .

Zhu et al. (2020) X. Zhu, X. Xu, and Z. Ye Robust adaptive beamforming via subspace for interference covariance matrix reconstruction . Signal Processing 167 , pp. 107289 . Cited by: §1 .

Zhu et al. (2025b) X. Zhu, B. Zhu, Y. Li, J. Fang, S. Wang, K. Zhao, and H. Zhang Hierarchical semantic alignment for image clustering . arXiv preprint arXiv:2512.00904 . Cited by: §2 .

Zhu et al. (2024b) X. Zhu, B. Zhu, Y. Tan, S. Wang, Y. Hao, and H. Zhang Enhancing zero-shot vision models by label-free prompt distribution learning and bias correcting . Advances in Neural Information Processing Systems 37 , pp. 2001–2025 . Cited by: §1 .

Zhu et al. (2024c) X. Zhu, B. Zhu, Y. Tan, S. Wang, Y. Hao, and H. Zhang Selective vision-language subspace projection for few-shot clip . In Proceedings of the 32nd ACM International Conference on Multimedia , pp. 3848–3857 . Cited by: §1 .

Zhu et al. (2025c) X. Zhu, B. Zhu, S. Wang, K. Zhao, and H. Zhang Enhancing clip robustness via cross-modality alignment . arXiv preprint arXiv:2510.24038 . Cited by: §2 .

## Appendix A Appendix

### A.1 Usage of LLM

We employ LLM primarily as writing assistants to refine and polish the manuscript. Their usage was limited to improving clarity, coherence, and presentation, while all conceptual and experimental contributions remain original.

### A.2 Detailed Derivation of Equation (5)

We start from the SFT gradient in Equation (2): ∇ θ ℒ SFT ​ ( θ ) = 𝔼 ( x , y ⋆ ) ∼ 𝒟 ​ [ − ∇ θ ​ log ​ π θ ​ ( y ⋆ ∣ x ) ] . \nabla_{\theta}\mathcal{L}_{\text{SFT}}(\theta)=\mathbb{E}_{(x,y^{\star})\sim\mathcal{D}}\big[-\nabla_{\theta}\log\pi_{\theta}(y^{\star}\mid x)\big]. (1)

For each query x x , the expectation over expert demonstrations ( x , y ⋆ ) (x,y^{\star}) can be written explicitly as a summation over all possible outputs y y : 𝔼 ( x , y ⋆ ) ∼ 𝒟 [ − ∇ θ log π θ ( y ⋆ ∣ x ) ] = 𝔼 x ∼ 𝒟 x ∑ y 𝟏 [ y = y ⋆ ] ] [ − ∇ θ log π θ ( y ∣ x ) ] . \mathbb{E}_{(x,y^{\star})\sim\mathcal{D}}\big[-\nabla_{\theta}\log\pi_{\theta}(y^{\star}\mid x)\big]=\mathbb{E}_{x\sim\mathcal{D}_{x}}\sum_{y}\mathbf{1}[y=y^{\star}]]\,\big[-\nabla_{\theta}\log\pi_{\theta}(y\mid x)\big]. (2)

We insert the model distribution π θ ​ ( y ∣ x ) \pi_{\theta}(y\mid x) , which allows us to express the summation in terms of importance weights: 𝔼 x ∼ 𝒟 x ​ ∑ y π θ ​ ( y ∣ x ) ⋅ 𝟏 [ y = y ⋆ ] ] π θ ​ ( y ∣ x ) ​ [ − ∇ θ ​ log ​ π θ ​ ( y ∣ x ) ] . \mathbb{E}_{x\sim\mathcal{D}_{x}}\sum_{y}\pi_{\theta}(y\mid x)\cdot\frac{\mathbf{1}[y=y^{\star}]]}{\pi_{\theta}(y\mid x)}\,\big[-\nabla_{\theta}\log\pi_{\theta}(y\mid x)\big]. (3)

Here, the term 𝟏 [ y = y ⋆ ] ] π θ ​ ( y ∣ x ) \tfrac{\mathbf{1}[y=y^{\star}]]}{\pi_{\theta}(y\mid x)} serves as an importance weight comparing the expert (Dirac delta) distribution with the model’s distribution.

The summation over y y can now be rewritten as an expectation under the policy distribution y ∼ π θ ( ⋅ ∣ x ) y\sim\pi_{\theta}(\cdot\mid x) : 𝔼 x ∼ 𝒟 x 𝔼 y ∼ π θ ( ⋅ ∣ x ) [ 𝟏 [ y = y ⋆ ] ] π θ ​ ( y ∣ x ) ( − ∇ θ log π θ ( y ∣ x ) ) ] . \mathbb{E}_{x\sim\mathcal{D}_{x}}\,\mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}\left[\frac{\mathbf{1}[y=y^{\star}]]}{\pi_{\theta}(y\mid x)}\big(-\nabla_{\theta}\log\pi_{\theta}(y\mid x)\big)\right]. (4)

Thus, we obtain Equation (5): 𝔼 ( x , y ⋆ ) ∼ 𝒟 [ − ∇ θ log π θ ( y ⋆ ∣ x ) ] = 𝔼 x ∼ 𝒟 x 𝔼 y ∼ π θ ( ⋅ ∣ x ) [ 𝟏 [ y = y ⋆ ] ] π θ ​ ( y ∣ x ) ( − ∇ θ log π θ ( y ∣ x ) ) ] . \mathbb{E}_{(x,y^{\star})\sim\mathcal{D}}\big[-\nabla_{\theta}\log\pi_{\theta}(y^{\star}\mid x)\big]=\mathbb{E}_{x\sim\mathcal{D}_{x}}\,\mathbb{E}_{y\sim\pi_{\theta}(\cdot\mid x)}\left[\frac{\mathbf{1}[y=y^{\star}]]}{\pi_{\theta}(y\mid x)}\big(-\nabla_{\theta}\log\pi_{\theta}(y\mid x)\big)\right]. (5)

This derivation shows that the SFT gradient can be expressed as an on-policy policy gradient with importance sampling, where the expert demonstration distribution is reweighted relative to the model distribution.

### A.3 Discussions and Insights

#### Gradient Analysis of DFT.

We now analyze the gradient induced by the DFT surrogate loss. Recall the sequence-level definition: ℒ DFT ​ ( θ ) = − sg ⁡ ( π θ ​ ( y ⋆ ∣ x ) ) ​ log ​ π θ ​ ( y ⋆ ∣ x ) , \mathcal{L}_{\text{DFT}}(\theta)=-\,\operatorname{sg}\!\big(\pi_{\theta}(y^{\star}\mid x)\big)\;\log\pi_{\theta}(y^{\star}\mid x), (10) where sg ⁡ ( ⋅ ) \operatorname{sg}(\cdot) denotes the stop-gradient operator. Since the stop-gradient blocks backpropagation, the detached probability sg ⁡ ( π θ ​ ( y ⋆ ∣ x ) ) \operatorname{sg}(\pi_{\theta}(y^{\star}\mid x)) is treated as a constant during differentiation. Consequently, the gradient becomes ∇ θ ℒ DFT \displaystyle\nabla_{\theta}\mathcal{L}_{\text{DFT}} = − sg ⁡ ( π θ ​ ( y ⋆ ∣ x ) ) ​ 1 π θ ​ ( y ⋆ ∣ x ) ​ ∇ θ π θ ​ ( y ⋆ ∣ x ) \displaystyle=-\,\operatorname{sg}\!\big(\pi_{\theta}(y^{\star}\mid x)\big)\;\frac{1}{\pi_{\theta}(y^{\star}\mid x)}\,\nabla_{\theta}\pi_{\theta}(y^{\star}\mid x) (11) = − ( sg ⁡ ( π θ ​ ( y ⋆ ∣ x ) ) π θ ​ ( y ⋆ ∣ x ) ) ​ ∇ θ π θ ​ ( y ⋆ ∣ x ) . \displaystyle=-\,\Bigl(\tfrac{\operatorname{sg}(\pi_{\theta}(y^{\star}\mid x))}{\pi_{\theta}(y^{\star}\mid x)}\Bigr)\,\nabla_{\theta}\pi_{\theta}(y^{\star}\mid x). (12)

Since sg ⁡ ( π θ ​ ( y ⋆ ∣ x ) ) \operatorname{sg}(\pi_{\theta}(y^{\star}\mid x)) equals π θ ​ ( y ⋆ ∣ x ) \pi_{\theta}(y^{\star}\mid x) in the forward pass, the prefactor is numerically equal to 1 1 . Therefore, ∇ θ ℒ DFT = − ∇ θ π θ ​ ( y ⋆ ∣ x ) . \nabla_{\theta}\mathcal{L}_{\text{DFT}}=-\,\nabla_{\theta}\pi_{\theta}(y^{\star}\mid x). (13) This shows that DFT is mathematically equivalent to directly maximizing the model probability of the target token, rather than its log-probability as in cross-entropy.

For cross-entropy, the loss is ℒ CE ​ ( θ ) = − log ⁡ π θ ​ ( y ⋆ ∣ x ) , \mathcal{L}_{\text{CE}}(\theta)=-\log\pi_{\theta}(y^{\star}\mid x), yielding gradient ∇ θ ℒ CE = − 1 π θ ​ ( y ⋆ ∣ x ) ​ ∇ θ π θ ​ ( y ⋆ ∣ x ) . \nabla_{\theta}\mathcal{L}_{\text{CE}}=-\tfrac{1}{\pi_{\theta}(y^{\star}\mid x)}\nabla_{\theta}\pi_{\theta}(y^{\star}\mid x). Thus both CE and DFT share the same gradient direction but differ in scaling: CE amplifies updates for low-probability targets (factor 1 / π 1/\pi ), while DFT applies a uniform factor 1 1 . As a result, DFT avoids the instability caused by excessively large gradients on unlikely expert tokens, providing more conservative and stable updates.

From the reinforcement learning perspective, the reward of DFT becomes uniformly 1 1 across all expert trajectories, equivalent to a verification-style objective that treats all correct references equally. From the optimization perspective, DFT trades off aggressive fitting of rare tokens for better stability and calibration. Practically, this explains why DFT often yields smoother training and stronger generalization, while maintaining alignment with the pre-training distribution.

#### Learning from Noisy Data.

DFT offers a simple yet effective approach, prompting us to reflect on why it might actually work. One intuitive explanation lies in its ability to learn from noisy data ( Freund, 2009 ) . Sasaki and Yamashina (2020) propose an imitation learning algorithm for learning from noisy demonstrations, based on the core idea of avoiding the fitting of data that is difficult to model, as such data is likely to originate from suboptimal behaviors, i.e., noise. Their method introduces a weighted behavioral cloning objective, where the weights are derived from a previously trained policy’s confidence in each action. Similarly, the weighting mechanism in DFT shares the same intuition, but instead of relying on a fixed old policy model to compute confidence scores, it uses a single policy model to perform confidence-based weighting on-the-fly during training.

### A.4 Comparision with Concurrent work iw-SFT

We include a concurrent method, Importance-Weighted SFT (iw-SFT) ( Qin and Springenberg, 2025 ) , for comparison. All training settings follow those reported in the original paper, except that we set the number of training epochs to 1.

As shown in Table 6 , DFT achieves higher average accuracy than iw-SFT on most model families: LLaMA-3.2-3B (+2.39), LLaMA-3.1-8B (+4.15), DeepSeekMath-7B (+3.34), and Qwen2.5-Math-1.5B (+1.30). Although iw-SFT outperforms our method on Qwen2.5-Math-7B (+2.45), this improvement is not consistent across datasets. In particular, for LLaMA-3.2-3B, iw-SFT underperforms standard SFT on Math500 (5.13 vs. 8.65) and AMC23 (2.03 vs. 3.13). Similarly, for LLaMA-3.1-8B, iw-SFT results in worse performance than SFT on Minerva Math (4.31 vs. 5.78) and AMC23 (7.34 vs. 8.28). In contrast, DFT consistently improves upon both the base model and SFT across nearly all datasets, including those where iw-SFT fails. These results underline better generalization ability of DFT in diverse mathematical reasoning scenarios. Moreover, iw-SFT incurs additional computational overhead by requiring a separate reference model to compute importance weights, whereas DFT dynamically derives its own weighting directly from the token probabilities of model, resulting in a more efficient training procedure.

We also compare against iw-SFT under the offline setting, as shown in Table 7 . While iw-SFT performs competitively on certain datasets, achieving 60.80 on Math500 and 44.21 on AMC23, its overall average performance (31.86) remains below that of our method by +3.57 points. Moreover, iw-SFT shows only modest improvements compared to its standard SFT counterpart, with an average score of 31.86 in the offline RL setting versus 30.28 with SFT (+1.58). In contrast, DFT achieves a larger gain of +4.76 (from 30.67 to 35.43). These results indicate that iw-SFT provides limited benefits from reward supervision under offline constraints, whereas DFT is able to more effectively incorporate such signals, leading to better generalization and higher task performance.

### A.5 Exploratory Experiment - OpenR1-Math Training Dataset

Inspired by DeepSeek-R1 DeepSeek-AI et al. (2025) , several studies have attempted to train open-source models to reproduce its reasoning capabilities ( Hugging Face, 2025 ) . To this end, a high-quality dataset, OpenR1-Math-220k ( Hugging Face, 2025 ) , was constructed, where the prompts are drawn from NuminaMath 1.5 and the off-policy reasoning traces are generated by DeepSeek-R1. LUFFY ( Yan et al., 2025 ) further filtered out sequences longer than 8192 tokens as well as those verified incorrect by Math-Verify, resulting in about 45k prompts paired with off-policy reasoning traces. We adopt this dataset as the training corpus for SFT. All training details remain the same as previous experiments, except that the number of epochs is set to 3.

As shown in Table 8 , training on OpenR1-Math-220k consistently improves performance, and the use of higher-quality annotations yields additional gains. SFT on this dataset increases the average accuracy of Qwen2.5-Math-1.5B by +13.24 points compared to the base model, while DFT provides a further +9.03 gain, resulting in a total improvement of +22.27. These results suggest that DFT remains effective even when applied on top of high-quality training data, highlighting its potential as a general fine-tuning paradigm.

### A.6 Exploratory Experiment - PEFT Training Setting

To investigate whether DFT remains effective under parameter-efficient fine-tuning (PEFT) settings with limited compute, we apply DFT using LoRA adapters across two model families: LLaMA-3.2-3B and Qwen2.5-Math-1.5B. All training configurations remain identical to previous full-parameter experiments, except that LoRA is enabled with rank=8 and alpha=16.

As shown in Table 9 , DFT provides consistent improvements over both base and SFT baselines under LoRA-based PEFT. For Qwen2.5-Math-1.5B, DFT increases the average accuracy from 15.92 (base) and 16.87 (SFT) to 32.90. For LLaMA-3.2-3B, DFT achieves a gain of +3.44 over SFT (from 1.19 to 4.63). These results indicate that DFT can serve as an effective fine-tuning strategy in low-resource or compute-constrained settings, where full model updates are not practical.

### A.7 Training Hyper-Parameters Ablation

To assess the robustness and sensitivity of our approach (DFT) with respect to key training hyper-parameters, we conduct an ablation study focused on learning rate and batch size, using the Qwen2.5-Math-1.5B base model. This analysis aims to answer two central questions: (1) Is the performance gap between DFT and SFT due to a suboptimal hyperparameter configuration in SFT? (2) How sensitive are both methods to changes in learning rate and batch size?

We evaluate both DFT and SFT across four learning rates: 2e-4, 1e-4, 5e-5, and 1e-5. As shown in Figure 3 (left), both methods exhibit a certain degree of sensitivity to the learning rate. DFT consistently outperforms SFT under all configurations, suggesting that the performance gap cannot be attributed solely to suboptimal hyperparameter choices in SFT. For both methods, intermediate learning rates (1e-4 and 5e-5) yield the best results, while both lower (1e-5) and higher (2e-4) values lead to noticeable degradation.

We further assess the impact of batch size, sweeping values from 32 to 256. As shown in Figure 3 (right), both DFT and SFT exhibit relatively stable performance across the full range of batch sizes. While minor fluctuations are observed, there is no consistent trend indicating that larger or smaller batches significantly affect final accuracy. This suggests that batch size is not a dominant factor for either method in this setup, and that default values may suffice in practice.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
