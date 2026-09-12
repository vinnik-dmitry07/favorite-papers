##### Report GitHub Issue

Content selection saved. Describe the issue below:

# GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning

###### Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the reasoning capabilities of Large Language Models (LLMs) by leveraging direct outcome verification instead of learned reward models. Building on this paradigm, Group Relative Policy Optimization (GRPO) eliminates the need for critic models but suffers from indiscriminate credit assignment for intermediate steps, which limits its ability to identify effective reasoning strategies and incurs overthinking. In this work, we introduce a model-free and verifiable process supervision via probing the model’s belief in the correct answer throughout its reasoning trajectory. By segmenting the generation into discrete steps and tracking the conditional probability of the correct answer appended at each segment boundary, we efficiently compute interpretable segment-wise progress measurements to refine GRPO’s trajectory-level feedback. This approach enables more targeted and sample-efficient policy updates, while avoiding the need for intermediate supervision derived from costly Monte Carlo rollouts or auxiliary models. Experiments on mathematical and general‑domain benchmarks show consistent gains over GRPO across diverse models: up to 2.6‑point accuracy improvements and 13.7% reasoning‑length reductions on math tasks, and up to 2.4 points and 4% on general‑domain tasks, demonstrating strong generalization.

## 1 Introduction

Advanced by Reinforcement Learning with Verifiable Rewards (RLVR) ( Shao et al., 2024 ; Yu et al., 2025a ) , Large Language Models (LLMs) have demonstrated remarkable capabilities in complex reasoning tasks, ranging from mathematical problem solving ( OpenAI, 2024 ; Team et al., 2025 ; Shao et al., 2024 ) to multi-hop question answering ( Huang et al., 2025 ; Song et al., 2025 ) . The success of RLVR is largely attributed to computing rewards via direct outcome verification, rather than relying on reward models that complicate the training pipeline and are prone to reward hacking ( Yu et al., 2025a ) . In a similar vein, Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) eliminates critic models for token-level advantage estimation, instead uniformly propagating trajectory-level advantages to intermediate steps. While this simplification avoids the challenges of training a critic model and reduces associated overhead, indiscriminate credit assignment hinders sample efficiency and limits the policy model’s ability to learn effective reasoning strategies ( Qu et al., 2025 ) .

To address this limitation, we explore enhancing GRPO with model-free, verifiable process supervision derived from the annotated final answer. Our key insight is that the contribution of intermediate reasoning steps can be probed by the probability increment of the reference answer appended at corresponding breakpoints. This is supported by observations in Figure 1 : (1) at the macro level, the average probed probability increases as reasoning progresses, with a more pronounced trend for trajectories that ultimately reach the correct answer; and (2) at the micro level, reasoning segments that reduce the probed probability tend to be of low quality. Based on these observations, our method leverages the model’s own reasoning trace to generate localized supervision signals, enabling more targeted and effective policy updates. Specifically, we segment the model’s response into discrete reasoning segments and strategically concatenate the correct final answer at each segment boundary. By extracting the model’s conditional probability of the correct answer at these positions, we obtain a proxy for its evolving belief state. The differences in these probabilities between adjacent segments serve as segment-wise supervision signals, complementing trajectory-level advantages and quantifying the contribution of each reasoning segment toward the final outcome.

This approach offers two key benefits: (1) it provides dense, interpretable feedback aligned with the model’s internal decision flow and (2) it avoids reliance on auxiliary models ( Schulman et al., 2017 ; Zha et al., 2025 ; Cui et al., 2025 ; He et al., 2024b ) or Monte Carlo rollouts ( Qu et al., 2025 ; Dai et al., 2025 ) , ensuring high efficiency and scalability and adhering to the design principles established by RLVR and GRPO. Through this fine-grained supervision mechanism, we aim to enhance the sample efficiency of RL training, paving the way for learning more effective and efficient reasoning behaviors.

Our experiments show substantial gains across four math reasoning benchmarks. Compared to GRPO, our method achieves up to +2.6 points Pass@1 on Qwen2.5-Math-1.5B and +1.1 point on Qwen2.5-Math-7B, while concurrently reducing reasoning length by 11.0% to 13.7%. It also consistently outperforms the GRPO variant ( Dai et al., 2025 ) that relies on costly Monte Carlo rollouts for segment-wise advantage estimation and auxiliary models ( Cui et al., 2025 ; He et al., 2024b ; Schulman et al., 2017 ) . Furthermore, evaluation on four general-domain reasoning benchmarks confirms strong generalization, with gains of 1.8 points on MMLUPro and 2.4 points on TheoremQA. These results highlight the effectiveness and scalability of our verifiable process supervision in delivering more accurate and concise reasoning.

In summary, our main contributions are: • We identify and empirically validate that a model’s evolving belief in the correct answer can serve as a model-free, interpretable signal for reasoning quality of intermediate steps. This enables fine-grained supervision without auxiliary models or Monte Carlo rollouts.

• We propose GRPO-VPS, a simple yet effective approach to enhance GRPO with granular, segment-wise process supervision, avoiding indiscriminate credit assignment and improving sample efficiency.

• Our empirical results show that the method achieves strong performance on challenging math reasoning tasks, demonstrating that our method enhances both reasoning effectiveness and efficiency in comparison with GRPO and its variants.

## 2 Related Work

Group Relative Policy Optimization (GRPO) . Reinforcement Learning with Verifiable Rewards (RLVR) has become a prominent paradigm for fine-tuning LLMs, using definitive signals from rule-based verifiers to circumvent the need for costly and potentially biased reward models ( Shao et al., 2024 ; Yu et al., 2025a ) . Within this paradigm, GRPO ( Shao et al., 2024 ) offers a lightweight and efficient alternative to critic-based algorithms like PPO ( Schulman et al., 2017 ) . By comparing final outcomes across a group of sampled trajectories, GRPO eliminates the need for a separate value network. However, this simplification comes at the cost of indiscriminate credit assignment: a single, trajectory-level reward is uniformly propagated to all intermediate tokens. This can inadvertently reinforce spurious reasoning steps in a successful trajectory or penalize promising partial logic in a failed one. Our work addresses this limitation by introducing a fine-grained process supervision mechanism, enhancing its credit assignment capabilities without sacrificing its lightweight nature.

Process supervision for reasoning . Recent work has explored injecting fine-grained supervision into the reasoning process to better guide long-form generation. These efforts can be broadly categorized into model-based and model-free approaches. Model-based supervision utilizes an auxiliary model to provide fine-grained feedback. Critic-based methods, often using PPO, train a value network to estimate the expected return from intermediate states ( Yue et al., 2025 ; Kazemnejad et al., 2024 ) . However, in long-horizon reasoning tasks, the critic’s signal can diminish or become unreliable due to the long delay in receiving the final outcome reward ( Shao et al., 2024 ; Yue et al., 2025 ) . Process Reward Models (PRMs) ( Lightman et al., 2023 ; Wang et al., 2023 ) offer an alternative but are typically trained offline, making them vulnerable to reward hacking and distributional shift. These approaches introduce significant system complexity, requiring an extra model to be trained, maintained, and served alongside the policy. Model-free process supervision aims to provide granular feedback without auxiliary models. Recent works have made progress in this direction. For instance, S-GRPO ( Dai et al., 2025 ) introduces a ”serial group” objective with decaying rewards to encourage earlier, more efficient reasoning. MRT ( Qu et al., 2025 ) frames the problem as meta reinforcement learning and computes a dense “progress” reward based on the change in the likelihood of eventual success. Their reward estimation can require complex, rollout-based procedures or multiple generation branches from intermediate states, which compromises training efficiency. In contrast, our method simplifies the process supervision workflow by deriving a high-quality signal from the known ground-truth answer, requiring only a single forward pass per generated trajectory. This makes our approach more efficient while still providing the benefits of fine-grained, verifiable process feedback.

## 3 Methodology: Process Supervisions from Verifiable Outcomes

LLMs trained under GRPO still suffer from indiscriminate credit assignment, where sparse outcome-based rewards fail to guide intermediate reasoning steps. To address this, we present a verifiable process supervision framework for enhancing GRPO with fine-grained credit assignment. We first introduce a segmentation strategy that uses token-level entropy to identify high-uncertainty transitions and partition trajectories into semantically meaningful reasoning steps (Section 3.1 ). We then introduce segment-wise progress estimation to quantify the contribution of each reasoning segment based on changes in model confidence (Section 3.2 ). Finally, we incorporate this localized feedback into GRPO’s token-level updates, forming a hybrid advantage that fuses outcome-based and process-level signals (Section 3.3 ).

### 3.1 Reasoning Process Segmentation

Recent studies have revealed that performance gains in RLVR are primarily driven by critical decision points characterized by high token-level uncertainty ( Yang et al., 2025 ; Wang et al., 2025 ) . Inspired by SPO ( Guo et al., 2025 ) , we adopt an Adaptive Entropy-based Cutpoint Partition strategy, leveraging token-level entropy to robustly identify reasoning ”junctions” where the model’s trajectory is likely to diverge.

Formally, given a response o o of length T T , We identify a set of candidate cutpoints 𝒰 ⊆ { 1 , … , T } \mathcal{U}\subseteq\{1,\dots,T\} by selecting tokens whose entropy exceeds an adaptive threshold: 𝒰 = { t ∣ e t i ≥ τ } , \mathcal{U}=\{t\mid e_{t}^{i}\geq\tau\}, (1) where τ \tau is determined from the entropy distribution of o o (e.g. via a perentile-based rule). To partition o o into M M reasoning segments ( z 1 , … , z M ) (z_{1},\dots,z_{M}) , we choose boundary indices { t 1 , … , t M + 1 } \{t_{1},\dots,t_{M+1}\} with t 1 = 1 t_{1}=1 and t M + 1 = T + 1 t_{M+1}=T+1 , such that the number of cutpoints in each segment is approximately balanced: | 𝒰 ∩ [ t m , t m + 1 ) | ≈ | 𝒰 | M , ∀ m ∈ { 1 , … , M } . |\mathcal{U}\cap[t_{m},t_{m+1})|\approx\frac{|\mathcal{U}|}{M},\quad\forall m\in\{1,\dots,M\}. (2) This heuristic ensures that each segment contains a comparable number of high-entropy positions, yielding a balanced and semantically meaningful segmentation of the reasoning trajectory. Our experiments demonstrate that this adaptive strategy yields superior performance compared to fixed-token partition (see Section 4.3 ).

### 3.2 Progress as Process Supervision

Based on the reasoning process segmentation, we propose to leverage segment-wise progress as a form of process supervision to address the indiscriminate credit assignment of GRPO. This formulation provides a dense, model-free, and scalable supervision signal that quantifies the incremental contribution of each reasoning segment toward the correct final answer.

Given an input prompt x x and a trajectory o o generated by the policy π θ \pi_{\theta} , we compute a segment-wise confidence score C ⁡ ( z ≤ k ) C(z_{\leq k}) representing the model’s conditional probability of the target answer y ∗ y^{*} after generating the first k k reasoning steps:

C ⁡ ( z ≤ k ) = π θ ​ ( y ∗ ∣ x , z ≤ k ) C(z_{\leq k})=\pi_{\theta}(y^{*}\mid x,z_{\leq k}) (3)

where x x is the input question and z ≤ k = ( z 1 , … , z k ) z_{\leq k}=(z_{1},\ldots,z_{k}) denotes partial reasoning trace up to segment k k . The initial value, before any reasoning, is C 0 = P ⁡ ( y ∗ ∣ x ) C_{0}=P(y^{*}\mid x) .

To quantify the contribution of each reasoning segment, we define a segment-wise progress score, denoted as Δ ​ C k \Delta C_{k} , is then computed as the change in this confidence score, effectively isolating the contribution of that specific step: Δ ​ C k \displaystyle\Delta C_{k} = C ⁡ ( z ≤ k ) − C ⁡ ( z ≤ k − 1 ) \displaystyle=C(z_{\leq k})-C(z_{\leq k-1}) = π θ ​ ( y ∗ ∣ x , z ≤ k ) − π θ ​ ( y ∗ ∣ x , z ≤ k − 1 ) \displaystyle=\pi_{\theta}(y^{*}\mid x,z_{\leq k})-\pi_{\theta}(y^{*}\mid x,z_{\leq k-1}) where Δ ​ C k ∈ [ − 1 , 1 ] \Delta C_{k}\in[-1,1] due to the probabilistic range of confidence scores. This results in a vector Δ ​ C = [ Δ ​ C 1 , … , Δ ​ C m ] \Delta C=[\Delta C_{1},\ldots,\Delta C_{m}] of segment-level supervision signals for each trajectory. It reflects how much each segment improves (or worsens) the model’s belief in the final answer.

### 3.3 GRPO with Process Supervision

We design a hybrid advantage signal that fuses sparse outcome-level feedback with dense, segment-level process supervision. For each prompt, we sample a group of G G trajectories { o 1 , o 2 , … , o G } \{o^{1},o^{2},\ldots,o^{G}\} from the policy π θ \pi_{\theta} . Each trajectory o i = ( z 1 i , … , z m i , y i ) o^{i}=(z_{1}^{i},\ldots,z_{m}^{i},y^{i}) with binary correctness label r i ∈ { 0 , 1 } r^{i}\in\{0,1\} , we compute the group-relative advantage: A i = r i − 1 G ​ ∑ j = 1 G r j , A^{i}=r^{i}-\frac{1}{G}\sum_{j=1}^{G}r^{j}, (5) where G G is the number of responses sampled for the same prompt. To complement this global signal, we inject a localized feedback term Δ ​ C k \Delta C_{k} , which quantifies the incremental gain in the model’s belief in the correct answer after each reasoning segment z k i z_{k}^{i} , as defined in Section 3.2 . The final hybrid advantage at step k k is: A ~ k i = A i ⏟ Outcome + α ⋅ Δ ​ C k ⏟ Process , \tilde{A}_{k}^{i}=\underbrace{A^{i}}_{\text{Outcome}}+\underbrace{\alpha\cdot\Delta C_{k}}_{\text{Process}}, (6) where α \alpha is a weighting factor balancing the two components. We empirically set α = 1.2 \alpha=1.2 and found it work well. Sensitivity to α \alpha can be found in Appendix A.4.3 .

We then define the final on-policy gradient estimator as:

∇ θ J ​ ( θ ) = 1 G ​ ∑ i = 1 G ∑ k = 1 M ( A i + α ⋅ Δ ​ C k ) ⋅ ∇ θ ​ log ​ π θ ​ ( z k i ∣ x , z < k i ) \nabla_{\theta}J(\theta)=\frac{1}{G}\sum_{i=1}^{G}\sum_{k=1}^{M}\left(A^{i}+\alpha\cdot\Delta C_{k}\right)\cdot\nabla_{\theta}\log\pi_{\theta}(z_{k}^{i}\mid x,z_{<k}^{i}) (7) where the total advantage combines two signals: A i A^{i} provides sparse, trajectory-level feedback based on the final outcome, while α ⋅ Δ ​ C k \alpha\cdot\Delta C_{k} injects dense, segment-level guidance reflecting the progress toward the correct answer. The full algorithm of GRPO-VPS is shown in Algorithm 1 .

## 4 Experiment

### 4.1 Setup

Models and baselines. We conduct experiments on two model families, including Qwen2.5-Math-1.5B, Qwen2.5-Math-7B ( Yang et al., 2024 ) and Gemma-2-2B-it ( Team, 2024a ) . To ensure fair comparison, we include a comprehensive set of baselines categorized by their use of outcome-level vs. process-level supervision: • Outcome Supervision Only. This category includes methods that rely solely on final answer correctness for reward assignment. We consider GRPO and its recent variants, DrGRPO ( Liu et al., 2025 ) and GSPO ( Zheng et al., 2025 ) , which enhance group-wise comparison or propagate advantages with entropy-based mechanisms. We also include the BASE models without RL fine-tuning for reference.

• With Process Supervision. This group covers methods that incorporate intermediate supervision beyond outcome-level rewards. We evaluate S-GRPO ( Dai et al., 2025 ) , which relies on Monte Carlo rollouts with forced early stops to construct sub-trajectories, and assigns segment-level rewards based on their predicted outcomes. We also compare against PRIME-style reward modeling, represented by the public Eurus-2-7B-PRIME ( Cui et al., 2025 ; Yuan et al., 2024 ) , and a controlled variant where we fine-tune Qwen2.5-Math-1.5B and 7B with Skywork-o1-prm using GRPO. These baselines provide strong comparisons for evaluating the effectiveness of verifiable process supervision in our method.

Training setup. In line with prior work ( Liu et al., 2025 ) , we use MATH ( Hendrycks et al., 2021 ) , which contains 7,500 problems. We train the models using the verl framework ( Sheng et al., 2024 ) . We sample 8 rollouts per prompt, with a temperature of 1.0 and the maximum response length of 3,072 tokens. The batch size is set to 512, the mini-batch size to 128, and the learning rate to 1 × 10 − 6 1\times 10^{-6} . The training is conducted on a single node with 8 × H800 GPUs. More hyperparameter settings can be found in Appendix A.1 .

Evaluation setup. We evaluate on four widely used math reasoning benchmarks, including the test sets of MATH, AIME 2024 ( MAA, 2024 ) , AMC23 ( MAA, 2023 ) and OlympiadBench ( He et al., 2024a ) . We set temperature to 1.0, top p p set to 1, and maximum output length set to 3,072 tokens for inference. Due to the high variance of the outputs from reasoning models, we report the average Pass@1 over 4 runs. To ensure accurate evaluation, we utilize Math-Verify 1 1 1 https://github.com/huggingface/Math-Verify to check for answer equivalence.

### 4.2 Main Results

GRPO-VPS improves mathematical reasoning performance. As shown in Table 1 , our method achieves the highest average accuracy. On Qwen2.5-Math-1.5B, it yields an average gain of 27.7 points. On Qwen2.5-Math-7B, the gain reaches +31.0 points overall. Meanwhile, the average output length is reduced by 35.9% and 34.0% on the 1.5B and 7B models, respectively. Similar trends are observed on Gemma-2-2B-it, where our method improves average accuracy from 6.9 to 11.7 while substantially reducing output length compared to GRPO.

Comparison with outcome supervised RL. Compared to GRPO and its recent variants, GRPO-VPS achieves the highest overall accuracy across all benchmarks while substantially shortening the reasoning length. On Qwen2.5-Math-1.5B, it improves Pass@1 by more than 3% over GRPO and sustains a comparable margin on the 7B model, with an average reduction of 10–11% in output length. GRPO-VPS achieves larger gains in accuracy and produces shorter outputs. These results suggest that our method improves both effectiveness and efficiency of policy updates, leading to more focused reasoning traces. On Gemma-2-2B-it, our method further reduces the output length compared to GRPO while achieving higher accuracy. Although the Gemma base model exhibits shorter responses, training with reinforcement learning unlocks its long-chain reasoning behavior, as further evidenced in Appendix A.4.1 .

Comparison with model-based process supervision. Compared to S-GRPO, which uses multi-rollout early-exit probing to assign segment-level rewards, our method achieves higher accuracy and shorter outputs. To ensure a fair comparison, we adopt the same GRPO training pipeline to finetune both our method and Skywork-o1-prm. Under this controlled setup, GRPO-VPS consistently outperforms the Skywork baseline across both 1.5B and 7B model scales, achieving higher accuracy while generating more concise reasoning traces. We further compare our method with Eurus-2-7B-PRIME, a model trained using PRIME-style reward modeling. Notably, Eurus performs poorly on AIME24 with 15.0%, substantially lower than the 31.7% achieved by GRPO-VPS. This discrepancy reveals a lack of generalization in PRM-based methods, which tend to overfit to familiar patterns seen during training. In contrast, our process supervision, grounded in the model’s own belief dynamics, offers more robust and consistent improvements across tasks, while reducing reasoning length by up to 34.0%.

### 4.3 Ablation Study

Effect of segment granularity. To investigate the impact of segment granularity on the efficiency and performance of our adaptive strategy, we evaluate the impact of segment granularity by varying the average number of points n n per segment. As shown in Figure 2 (a), n = 4 n=4 achieves the optimal trade-off between training efficiency and performance under the same wall-clock time. While finer-grained segmentation ( n = 2 n=2 ) provides more precise local adjustments, it incurs prohibitive computational overhead that slows convergence. This confirms that our segment-level design effectively strikes a balance between computational economy and optimization precision, avoiding the excessive costs associated with fine-grained estimation while ensuring superior learning dynamics.

Comparison of Different segment strategies. We compare our adaptive segmentation strategy with a naive fixed token-count partition baseline, where each response is evenly divided into a fixed number of segments. For the fixed baseline, we set the number of segments to 6, exceeding the effective segmentation budget of our adaptive method. As shown in Figure 2 (b), the adaptive strategy converges faster, achieves higher accuracy, and maintains shorter responses throughout training. These results demonstrate that placing segment boundaries based on informative decision points is more effective than uniform partitioning, validating the design of our adaptive segmentation strategy.

Effect of outcome supervision signal. As shown in Table 2 , removing the outcome reward and relying solely on segment-level verifiable supervision results in degradation compared to the full method, confirming its essential role in guiding the model toward globally correct reasoning. While segment-level supervision alone provides fine-grained feedback, it lacks a reliable global anchor. Combining both signals yields the best performance, indicating their complementarity in stabilizing training and improving reasoning coherence.

### 4.4 Understanding How VPS Works

Quality analysis for segment-wise process signal. A core premise of our approach is that the segment-wise process signal ( Δ ​ C k \Delta C_{k} ) provides a reliable proxy for the correctness of intermediate reasoning steps. Unlike outcome-level signals, which uniformly credit or penalize every token in a trajectory, Δ ​ C k \Delta C_{k} directly reflects how each step changes the model’s belief in the correct answer.

To quantitatively validate this hypothesis, we align our progress signal with segment-level human annotations from the PRM800K dataset ( Lightman et al., 2023 ) ,which contains 800K reasoning steps labeled as -1 (incorrect/harmful), 0(neutral/uninformative), or +1 (correct/contributive). For evaluation, we randomly sample 100 held-out questions, each paired with six diverse model responses. For each reasoning segment, we discard neutral steps with label 0 and discretize Δ ​ C k \Delta C_{k} into predicted class labels.

Table 3 reports the precision, recall, and F1-score across model scales from 0.5B to 32B parameters ( Team, 2024b ) . We observe that even small models produce progress signals that meaningfully discriminate good from bad reasoning steps, with F1-scores exceeding 0.75 across the board. Larger models further improve both precision and recall, demonstrating that Δ ​ C k \Delta C_{k} scales naturally with model quality. These results confirm that our segment-wise progress signal serves as a lightweight yet effective indicator of reasoning quality, complementing trajectory-level outcome signals. Additional qualitative examples illustrating this alignment with human judgment are provided in the Appendix A.5 .

Sample efficiency and optimization stability. Recent studies prove dense reward signals can improve the sample efficiency and optimization stability of reinforcement learning systems by providing more frequent and informative feedback during training ( Setlur et al., 2024 ; Chan et al., 2024 ) . Our method introduces verifiable, model-free process supervision to construct dense, segment-wise signals that guide the optimization process more precisely than trajectory-level binary rewards alone. As shown in Figure 3 , our method achieves faster convergence and more stable gradient updates compared to standard GRPO.

### 4.5 General Reasoning Benchmarks

To verify the generalization capabilities of our method beyond specific domain tasks, we extended our evaluation to a suite of general reasoning benchmarks. Following the experimental setup in RLPR ( Yu et al., 2025b ) , we utilized the WebInstruct dataset ( Ma et al., 2025 ) for training, this dataset is characterized by a diverse semantic distribution, covering a wide range of disciplines including Physics, Mathematics Business, and Economics, thereby requiring the model to possess robust multi-domain reasoning abilities. We employed Qwen3-1.7B ( Team, 2025 ) as the backbone model and compared our proposed method against the Base model and the GRPO baseline. The evaluation was conducted on four challenging benchmarks: GPQA ( Rein et al., 2024 ) , MMLUPro ( Wang et al., 2024 ) , TheoremQA ( Chen et al., ) , and the test split of WebInstruct. As shown in Figure 4 , GRPO-VPS consistently outperforms baselines across all tasks. On GPQA and TheoremQA, it achieves 37.8% and 37.3% accuracy, surpassing GRPO (by 1.6% and 2.4%) and significantly beating the Base model (by 20.0% and 12.8%). Similarly, on MMLUPro and WebInstruct, our method reaches 54.4% and 73.9%, exceeding GRPO by 1.7% and 3.6%, respectively. Furthermore, these gains are achieved with greater efficiency. Our method reduces the average generation length by nearly 50% compared to the Base model, surpassing the GRPO baseline in conciseness. These results confirm that our method effectively enhances robust, multi-domain reasoning. Additional results and training details can be found in Appendix A.4.2 .

## 5 Conclusion

We present GRPO-VPS, a model-free and verifier-free method that augments GRPO with segment-level credit assignment derived from conditional answer probabilities. Our method generates dense and interpretable supervision signals aligned with the model’s internal decision flow, enabling more efficient and targeted policy optimization. Experiments on four math reasoning benchmarks show that our method consistently improves both accuracy and reasoning conciseness over strong RL baselines and segment-aware methods, without relying on auxiliary models or costly rollouts. Furthermore, extensive evaluations on general reasoning benchmarks confirm the method’s strong generalization capabilities, demonstrating consistent gains in robust, multi-domain reasoning tasks. These findings underscore the potential of verifier-free, confidence-driven rewards as a scalable direction for future alignment and reasoning optimization in large language models.

## References

Chan et al. (2024) Alex J Chan, Hao Sun, Samuel Holt, and Mihaela Van Der Schaar. Dense reward for free in reinforcement learning from human feedback. arXiv preprint arXiv:2402.00782 , 2024.

(2) Wenhu Chen, Ming Yin, Max Ku, Pan Lu, Yixin Wan, Xueguang Ma, Jianyu Xu, Xinyi Wang, and Tony Xia. Theoremqa: A theorem-driven question answering dataset (2023). URL https://arxiv. org/abs/2305.12524 .

Cui et al. (2025) Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process reinforcement through implicit rewards. arXiv preprint arXiv:2502.01456 , 2025.

Dai et al. (2025) Muzhi Dai, Chenxu Yang, and Qingyi Si. S-grpo: Early exit via reinforcement learning in reasoning models. arXiv preprint arXiv:2505.07686 , 2025.

DeepSeek-AI (2025) DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL https://arxiv.org/abs/2501.12948 .

Guo et al. (2025) Yiran Guo, Lijie Xu, Jie Liu, Dan Ye, and Shuang Qiu. Segment policy optimization: Effective segment-level credit assignment in rl for large language models. arXiv preprint arXiv:2505.23564 , 2025.

He et al. (2024a) Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. arXiv preprint arXiv:2402.14008 , 2024a.

He et al. (2024b) Jujie He, Tianwen Wei, Rui Yan, Jiacai Liu, Chaojie Wang, Yimeng Gan, Shiwen Tu, Chris Yuhao Liu, Liang Zeng, Xiaokun Wang, Boyang Wang, Yongcong Li, Fuxiang Zhang, Jiacheng Xu, Bo An, Yang Liu, and Yahui Zhou. Skywork-o1 open series, November 2024b. URL https://doi.org/10.5281/zenodo.16998085 .

Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874 , 2021.

Huang et al. (2025) Jerry Huang, Siddarth Madala, Risham Sidhu, Cheng Niu, Hao Peng, Julia Hockenmaier, and Tong Zhang. Rag-rl: Advancing retrieval-augmented generation via rl and curriculum learning. arXiv preprint arXiv:2503.12759 , 2025.

Kazemnejad et al. (2024) Amirhossein Kazemnejad, Milad Aghajohari, Eva Portelance, Alessandro Sordoni, Siva Reddy, Aaron Courville, and Nicolas Le Roux. Vineppo: Refining credit assignment in rl training of llms. arXiv preprint arXiv:2410.01679 , 2024.

Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In The Twelfth International Conference on Learning Representations , 2023.

Liu et al. (2025) Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. Understanding r1-zero-like training: A critical perspective. arXiv preprint arXiv:2503.20783 , 2025.

Ma et al. (2025) Xueguang Ma, Qian Liu, Dongfu Jiang, Ge Zhang, Zejun MA, and Wenhu Chen. General-Reasoner: Advancing LLM reasoning across all domains. In The Thirty-ninth Annual Conference on Neural Information Processing Systems , 2025. URL https://openreview.net/forum?id=pBFVoll8Xa .

MAA (2023) MAA. American mathematics contest 12 (amc 12) - november 2023, 11 2023. URL https://artofproblemsolving.com/wiki/index.php/AMC_12_Problems_and_Solutions .

MAA (2024) MAA. American invitational mathematics examination (aime) - february 2024, 02 2024. URL https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions .

OpenAI (2024) OpenAI. Learning to reason with llms, 2024. URL https://openai.com/index/learning-to-reason-with-llms/ .

Qu et al. (2025) Yuxiao Qu, Matthew YR Yang, Amrith Setlur, Lewis Tunstall, Edward Emanuel Beeching, Ruslan Salakhutdinov, and Aviral Kumar. Optimizing test-time compute via meta reinforcement fine-tuning. arXiv preprint arXiv:2503.07572 , 2025.

Rein et al. (2024) David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R Bowman. Gpqa: A graduate-level google-proof q&a benchmark. In First Conference on Language Modeling , 2024.

Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.

Setlur et al. (2024) Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process verifiers for llm reasoning. arXiv preprint arXiv:2410.08146 , 2024.

Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

Sheng et al. (2024) Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. arXiv preprint arXiv: 2409.19256 , 2024.

Song et al. (2025) Huatong Song, Jinhao Jiang, Yingqian Min, Jie Chen, Zhipeng Chen, Wayne Xin Zhao, Lei Fang, and Ji-Rong Wen. R1-searcher: Incentivizing the search capability in llms via reinforcement learning. arXiv preprint arXiv:2503.05592 , 2025.

Team (2024a) Gemma Team. Gemma. 2024a. doi: 10.34740/KAGGLE/M/3301 . URL https://www.kaggle.com/m/3301 .

Team et al. (2025) Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. arXiv preprint arXiv:2501.12599 , 2025.

Team (2024b) Qwen Team. Qwen2.5: A party of foundation models, September 2024b. URL https://qwenlm.github.io/blog/qwen2.5/ .

Team (2025) Qwen Team. Qwen3 technical report, 2025. URL https://arxiv.org/abs/2505.09388 .

Wang et al. (2023) Peiyi Wang, Lei Li, Zhihong Shao, RX Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations. arXiv preprint arXiv:2312.08935 , 2023.

Wang et al. (2025) Shenzhi Wang, Le Yu, Chang Gao, Chujie Zheng, Shixuan Liu, Rui Lu, Kai Dang, Xionghui Chen, Jianxin Yang, Zhenru Zhang, et al. Beyond the 80/20 rule: High-entropy minority tokens drive effective reinforcement learning for llm reasoning. arXiv preprint arXiv:2506.01939 , 2025.

Wang et al. (2024) Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, et al. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark. Advances in Neural Information Processing Systems , 37:95266–95290, 2024.

Yang et al. (2024) An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement. arXiv preprint arXiv:2409.12122 , 2024.

Yang et al. (2025) Zhihe Yang, Xufang Luo, Zilong Wang, Dongqi Han, Zhiyuan He, Dongsheng Li, and Yunjian Xu. Do not let low-probability tokens over-dominate in rl for llms. arXiv preprint arXiv:2505.12929 , 2025.

Yu et al. (2025a) Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. arXiv preprint arXiv:2503.14476 , 2025a.

Yu et al. (2025b) Tianyu Yu, Bo Ji, Shouli Wang, Shu Yao, Zefan Wang, Ganqu Cui, Lifan Yuan, Ning Ding, Yuan Yao, Zhiyuan Liu, Maosong Sun, and Tat-Seng Chua. Rlpr: Extrapolating rlvr to general domains without verifiers, 2025b. URL https://arxiv.org/abs/2506.18254 .

Yuan et al. (2024) Lifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free process rewards without process labels. arXiv preprint arXiv:2412.01981 , 2024.

Yue et al. (2025) Yu Yue, Yufeng Yuan, Qiying Yu, Xiaochen Zuo, Ruofei Zhu, Wenyuan Xu, Jiaze Chen, Chengyi Wang, TianTian Fan, Zhengyin Du, et al. Vapo: Efficient and reliable reinforcement learning for advanced reasoning tasks. arXiv preprint arXiv:2504.05118 , 2025.

Zha et al. (2025) Kaiwen Zha, Zhengqi Gao, Maohao Shen, Zhang-Wei Hong, Duane S Boning, and Dina Katabi. Rl tango: Reinforcing generator and verifier together for language reasoning. arXiv preprint arXiv:2505.15034 , 2025.

Zheng et al. (2025) Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, et al. Group sequence policy optimization. arXiv preprint arXiv:2507.18071 , 2025.

## Appendix A Appendix

### A.1 Experimental Settings

All hyperparameter settings are listed in Table 4 , our experiments are performed on 8 × H100 GPUs.

### A.2 Prompt Templates

For math reasoning tasks, we adopt the prompt templates for Qwen Math families ( Yang et al., 2024 ) and Gemma ( Team, 2024a ) .

For general reasoning tasks, we adopt the prompt templates for Qwen3 ( Team, 2025 ) model.

### A.3 Disclosure of LLM usage.

This paper benefited from language editing and phrasing suggestions provided by ChatGPT (OpenAI), which was used solely for grammar correction and clarity improvement. No LLM was used for generating research ideas, experimental design, data analysis, or writing substantive technical content.

### A.4 Extended Empirical Results

#### A.4.1 Response Length Dynamics across Model Families

We observe opposite response-length dynamics between Gemma and Qwen Math models under reinforcement learning, as illustrated in Figure 5 . Gemma base model exhibits extremely short responses at initialization, due to its instruction-tuned alignment, which explicitly suppresses verbosity and favors concise, direct answers. As training progresses, both methods gradually increase the response length, as longer reasoning trajectories are consistently associated with higher success probability and thus receive positive reinforcement.

In contrast, Qwen base models initially tend to produce more redundant or repetitive content during training process, the models learn to compress these redundant reasoning steps, leading to significantly shorter and more focused outputs.

#### A.4.2 Additional Analysis on General Reasoning Benchmarks

Fine-grained results on MMLU-Pro. We provide detailed results on the MMLU-Pro test set by reporting accuracy across individual subject domains. Following prior work, we adopt abbreviated domain names with the full nomenclature as follows: Math (Mathematics), Bio (Biology), Econ (Economics), Chem (Chemistry), Bus (Business), CS (Computer Science), Phys (Physics), Psy (Psychology), Eng (Engineering), Health (Health), Other (Other), Phil (Philosophy), Hist (History), and Law (Law). Table 5 reports per-domain accuracy together with the average response length. Compared to both the Base model and GRPO, our method achieves the highest average accuracy while producing shorter responses.

Training and evaluation performance for general reasoning. Figure 6 further illustrates the training entropy loss curves and test accuracy on TheoremQA. Compared to GRPO, our method exhibits a consistently lower entropy loss throughout training, indicating more stable and confident policy updates.

#### A.4.3 Sensitivity Analysis on α \alpha

We further analyze the sensitivity of the weighting factor α \alpha , which balances the trajectory-level outcome advantage and the segment-level process supervision in Eq. ( 6 ). Specifically, α \alpha controls the relative contribution of the segment-wise progress signal Δ ​ C k \Delta C_{k} to the overall hybrid advantage.

We conduct a sensitivity study by varying α \alpha over a wide range while keeping all other training settings fixed. As shown in Table 6 , our method achieves the best performance at α \alpha = 1.2. Moreover, performance is relatively insensitive to α \alpha within the range [0.8, 1.4].

### A.5 Qualitative Analysis of Segment-wise Process Signals.

To qualitatively evaluate the effectiveness of our progress signal, we present representative cases where the segment-wise signal Δ ​ C k \Delta C_{k} successfully distinguishes contributive from harmful reasoning steps. As shown in Figure 8 and 7 , positive increments in Δ ​ C k \Delta C_{k} correspond to steps that strengthen the model’s belief in the correct answer, while negative increments highlight misleading or incorrect reasoning. These examples demonstrate that our process supervision can reliably identify the strengths and weaknesses within a model’s reasoning trajectory, providing interpretable and fine-grained feedback throughout the generation process.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
