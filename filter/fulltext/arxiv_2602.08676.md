##### Report GitHub Issue

Content selection saved. Describe the issue below:

# LLaDA2.1: Speeding Up Text Diffusion via Token Editing

###### Abstract

While LLaDA2.0 showcased the scaling potential of 100B-level block-diffusion models and their inherent parallelization, the delicate equilibrium between decoding speed and generation quality has remained an elusive frontier. Today, we unveil LLaDA2.1 , a paradigm shift designed to transcend this trade-off. By seamlessly weaving Token-to-Token (T2T) editing into the conventional Mask-to-Token (M2T) scheme, we introduce a joint, configurable threshold-decoding scheme. This structural innovation gives rise to two distinct personas: the Speedy Mode (S Mode) , which audaciously lowers the M2T threshold to bypass traditional constraints while relying on T2T to refine the output; and the Quality Mode (Q Mode) , which leans into conservative thresholds to secure superior benchmark performances with manageable efficiency degrade. Furthering this evolution, underpinned by an expansive context window, we implement the first large-scale Reinforcement Learning (RL) framework specifically tailored for dLLMs, anchored by specialized techniques for stable gradient estimation. This alignment not only sharpens reasoning precision but also elevates instruction-following fidelity, bridging the chasm between diffusion dynamics and complex human intent. We culminate this work by releasing LLaDA2.1-Mini (16B) and LLaDA2.1-Flash (100B) . Across 33 rigorous benchmarks, LLaDA2.1 delivers strong task performance and lightning-fast decoding speed. Despite its 100B volume, on coding tasks it attains an astounding 892 TPS on HumanEval+, 801 TPS on BigCodeBench, and 663 TPS on LiveCodeBench.

## 1 Introduction

Discrete diffusion Large Language Models (dLLMs) have emerged as a compelling alternative to autoregressive generation, offering the potential for non-monotonic reasoning and parallel decoding. However, the standard absorbing-state framework—which enforces a rigid, monotonic transition from [MASK] to fixed tokens—faces inherent limitations in fidelity. As highlighted by Kang et al. (2025) , the independent nature of parallel decoding often amplifies token-level inconsistencies. While recent studies have attempted to mitigate this via confidence-based remasking ( Wang et al., 2025b ) or by employing external guide models ( Lee et al., 2025 ) . To bridge the gap between efficient parallel generation and high-fidelity reasoning, we align with the direction of generalizing discrete diffusion beyond absorbing states ( Rütte et al., 2025 ) and propose a comprehensive framework for Editable State Evolution.

Unlike prior work such as Song et al. (2025) , we first design a novel Error-Correcting Editable decoding strategy, which introduces a dynamic paradigm controlled by dual probability thresholds. This paradigm encompasses two types of operations: direct decoding from mask to token, and editing from one token to another. This strategy enables the model to directly refine its own outputs during the generation process, thereby effectively addressing the local inconsistencies commonly encountered in parallel decoding. To cultivate this editing capability, our CPT and SFT phases expose the model to both masked positions and stochastic noise, incentivizing it to not only generate new content but also identify and rectify existing errors.

Crucially, this architecture transforms the rigid trade-off between latency and fidelity into a flexible, user-configurable continuum. By allowing the model to retroactively correct errors, we can aggressively lower the confidence threshold for the initial Mask-to-Token (M2T) phase without collapsing the generation quality. This insight gives rise to two distinct operating personas: a Speedy Mode (S Mode) , which prioritizes high-throughput generation by accepting lower-confidence tokens and relying on subsequent Token-to-Token (T2T) passes for rectification; and a Quality Mode (Q Mode) , which adheres to conservative thresholds to maximize reasoning rigor. This duality demonstrates that editability is not merely a mechanism for error repair, but a fundamental lever for accelerating parallel decoding.

To further elevate the model’s capabilities, we integrate a Reinforcement Learning (RL) stage. While recent works such as SPG ( Wang et al., 2025a ) , TraceRL ( Wang et al., 2025c ) and ESPO ( Ou et al., 2025 ) have demonstrated the potential of RL in improving dLLMs, applying policy gradients to block-autoregressive models remains challenging due to the intractability of sequence log-likelihoods. We circumvent this by adopting an ELBO-based Block-level Policy Optimization (EBPO) framework tailored for our editable setting.

Notice that LLaDA2.1 extends its previous version (LLaDA2.0) by prioritizing decoding versatility over mere parameter scaling or benchmark peaking. By keeping the model size constant and minimal change of training data, we prove that our novel editing scheme enables lightning-fast execution with minimal overhead. This work serves as a proof-of-concept for a new dLLM paradigm that balances high-quality generation with extreme operational efficiency.

## 2 Configurable Decoding Scheme

During LLM decoding, Exposure Bias —where errors compound as the model conditions on its own imperfect predictions—is inevitable. This phenomenon is particularly severe in dLLMs due to their parallel generation nature. We observe that once such decoding errors occur, dLLMs tend to become increasingly conservative in subsequent steps, significantly slowing down the generation process. In contrast, autoregressive models exhibit lower exposure bias and can self-correct through extended chain-of-thought reasoning. To address this challenge, we introduce an editing operation into the decoding process, enabling the model to retrospectively correct errors introduced during parallel generation, thereby achieving a much better balance between generation speed and quality.

Specifically, we extend standard discrete diffusion to support it. Unlike conventional absorbing-state models that enforce a rigid monotonic transition from [MASK] to fixed tokens, our framework introduces a dynamic “Draft-and-Edit” paradigm controlled by dual probability thresholds. We formalize the state evolution by defining two active update sets at timestep t t : the Unmasking Set Γ t \Gamma_{t} and the Editing Set Δ t \Delta_{t} .

We formalize the state evolution by defining two active update sets at timestep t t : the Unmasking Set Γ t \Gamma_{t} and the Editing Set Δ t \Delta_{t} . Let v t i = arg ⁡ max v ​ p θ ​ ( v | 𝒙 t ) v_{t}^{i}=\arg\max_{v}p_{\theta}(v|\bm{x}_{t}) be the top-candidate. The update indices are identified as: Γ t \displaystyle\Gamma_{t} = { i ∣ x t i = [MASK] and ​ p θ ​ ( v t i | 𝒙 t ) > τ mask } , \displaystyle=\left\{i\mid x_{t}^{i}=\text{[MASK]}\text{ and }p_{\theta}(v_{t}^{i}|\bm{x}_{t})>\tau_{\text{mask}}\right\}, (1) Δ t \displaystyle\Delta_{t} = { i ∣ x t i ≠ v t i ​ and ​ p θ ​ ( v t i | 𝒙 t ) > τ edit } , \displaystyle=\left\{i\mid x_{t}^{i}\neq v_{t}^{i}\text{ and }p_{\theta}(v_{t}^{i}|\bm{x}_{t})>\tau_{\text{edit}}\right\}, (2) with τ mask , τ edit ∈ [ 0 , 1 ] \tau_{\text{mask}},\tau_{\text{edit}}\in[0,1] being the confidence thresholds configuring the decoding dynamics. The transition operator then applies the updates strictly on the union of these sets: x t − 1 i = { v t i if ​ i ∈ Γ t ∪ Δ t , x t i otherwise . x_{t-1}^{i}=\begin{cases}v_{t}^{i}&\text{if }i\in\Gamma_{t}\cup\Delta_{t},\\ x_{t}^{i}&\text{otherwise}.\end{cases} (3)

## 3 Training Paradigm

### 3.1 Training Alignment for “Draft-and-Edit”

To align the model with the “Draft-and-Edit” inference paradigm and mitigate the Exposure Bias inherent in standard mask-based training, we employ a unified Mixture of M2T and T2T objective. This objective is applied throughout both the Continual Pre-Training (CPT) and Supervised Finetuning (SFT) stages.

This dual-stream training objective enables the model to develop two complementary capabilities fundamental to our framework:

• Drafting Stream (Mask-to-Token): The model learns to predict the correct token at each masked position to generate initial content, establishing the foundational drafting capability.

• Editing Stream (Token-to-Token): The model learns to recover original tokens from random noise perturbations (rectifying errors), equipping it with the ability to identify and rewrite artifacts.

By consistently applying this dual-stream supervision from CPT through SFT, we ensure that LLaDA2.1 is fundamentally conditioned to function as both a fast drafter and a precise editor within a single parameter space. Additionally, we employ a Multi-turn Forward (MTF) data augmentation technique, by exposing the model to a wider variety of editing scenarios, enhance the model’s editing capabilities.

### 3.2 Reinforcement Learning Training

The application of policy gradient methods to diffusion models faces a fundamental hurdle: the intractability of the sequence-level log-likelihood, log ⁡ π θ ​ ( 𝒙 ) \log\pi_{\theta}(\bm{x}) , which is essential for computing policy updates. While prior works have explored various approximations, they have historically struggled with high variance and prohibitive computational costs, limiting RL to small-scale experiments ( Wang et al., 2025c , Ou et al., 2025 , Wang et al., 2025a ) . We overcome this bottleneck by synthesizing ELBO-based Block-level Policy Optimization (EBPO) with robust infrastructure optimizations. By utilizing the Evidence Lower Bound (ELBO) as a principled proxy for exact likelihood and implementing Vectorized Likelihood Estimation ( Arriola et al., 2025 ) to parallelize bound computation, we achieve orders-of-magnitude acceleration. This integration allows us to scale dLLMs RL to unprecedented context lengths and training magnitudes, establishing a stable and efficient pipeline for post-training.

Formally, we maximize a clipped surrogate objective, where the advantage is weighted by the probability ratio ρ \rho : 𝒥 EBPO ​ ( θ ) = 𝔼 𝒙 , 𝒚 ∼ π θ old ​ [ min ⁡ ( ρ ⁡ ( 𝒚 | 𝒙 ) ​ A ^ , clip ​ ( ρ ⁡ ( 𝒚 | 𝒙 ) , 1 − ϵ low , 1 + ϵ high ) ​ A ^ ) ] , \mathcal{J}_{\text{EBPO}}(\theta)=\mathbb{E}_{\bm{x},\bm{y}\sim\pi_{\theta_{\text{old}}}}\left[\min\left(\rho(\bm{y}|\bm{x})\hat{A},\text{clip}(\rho(\bm{y}|\bm{x}),1-\epsilon_{\text{low}},1+\epsilon_{\text{high}})\hat{A}\right)\right], (4) where A ^ \hat{A} is an estimator of the advantage function at timestep t t , quantifying the relative improvement of the chosen action over the average expectation under the current policy. For a set of discretized timesteps { t n } n = 1 N \{t_{n}\}_{n=1}^{N} and weights { w n } \{w_{n}\} , we construct a composite input 𝒛 n = 𝒚 t n ⊕ 𝒚 0 \bm{z}_{n}=\bm{y}_{t_{n}}\oplus\bm{y}_{0} to compute all block-conditional probabilities in parallel: log ⁡ ρ ⁡ ( 𝒚 | 𝒙 ) ≈ ∑ n = 1 N w n ​ ∑ b = 1 B ( log ⁡ p θ ​ ( 𝒚 b ∣ 𝒛 n , 𝒙 ; ℳ ) − log ⁡ p θ old ​ ( 𝒚 b ∣ 𝒛 n , 𝒙 ; ℳ ) ) . \log\rho(\bm{y}|\bm{x})\approx\sum_{n=1}^{N}w_{n}\sum_{b=1}^{B}\left(\log p_{\theta}(\bm{y}^{b}\mid\bm{z}_{n},\bm{x};\mathcal{M})-\log p_{\theta_{\text{old}}}(\bm{y}^{b}\mid\bm{z}_{n},\bm{x};\mathcal{M})\right). (5) Here, ℳ \mathcal{M} denotes a Block-Causal Mask ensuring the b b -th block attends only to valid history. By aggregating block-level contributions ( ∑ b = 1 B \sum_{b=1}^{B} ) within a single forward pass per timestep n n , we establish a computationally tractable pipeline for scaling reinforcement learning to long-context diffusion generation.

## 4 Infrastructure

### 4.1 Training Infrastructure

#### Continued Pre-Training and Supervised Fine-Tuning

For both continued pre-training (CPT) and supervised fine-tuning (SFT), we adopt the same training infrastructure as LLaDA2.0 ( Bie et al., 2025 ) , leveraging dFactory ( InclusionAI, 2025 ) , which provides efficient training recipes specifically designed for dLLMs, except that we introduce a dedicated optimized implementation for the multi-turn forward (MTF) stage.

#### RL Training

To enable effective policy optimization for dLLMs, we extend the AReaL framework ( Fu et al., 2025 , Mei et al., 2025 ) by developing specialized likelihood estimation and advantage estimation protocols that leverage diffusion sampling, explicitly supporting both T2T and M2T modes. This workflow is powered by ASystem ( Ling Team and others, 2025 ) for distributed orchestration and utilizes a customized version of SGLang ( Ant Group Team and SGLang Team, ) as the dedicated rollout engine.

### 4.2 Inference Infrastructure

We use a customized version of SGLang ( Ant Group Team and SGLang Team, ) for inference. To further accelerate the inference speed, we integrate Alpha-MoE ( Aleph-Alpha, ) , a MoE megakernel that combines the two FusedMoE computations into one kernel, and adopt per-block FP8 quantization to balance the inference speed and model accuracy. To accelerate inference on long-context sequences, we adopt block-wise causal masked attention, allowing the KV cache for the entire long context to be computed in a single forward pass. We further enable radix caching and batching support for block diffusion LLMs in SGLang.

### 4.3 Decoding Algorithm at Inference

In the inference stage, we adopt a decoding algorithm that combines Threshold Decoding ( Ma et al., 2025 ) with an explicit editing mechanism. In the basic setting, decoding and editing are performed within a single block: tokens are generated under a threshold-based constraint, and local edits are applied to revise intermediate outputs before the block is finalized.

Beyond single-block editing, we further introduce a Multiple Block Editing (MBE) mechanism. MBE allows the model to revisit and revise previously generated blocks based on the content of newly decoded blocks.

## 5 Evaluation

To comprehensively evaluate the quality of instruction-tuned models, we employ a diverse suite of benchmarks categorized into five dimensions:

• Knowledge : MMLU-Pro ( Wang et al., 2024 ) , GPQA-Diamond ( Rein et al., 2024 ) , C-Eval ( Huang et al., 2023 ) , PHYBench ( Qiu et al., 2025 ) , TriviaQA ( Joshi et al., 2017 )

• Reasoning : SQuAD 2.0 ( Rajpurkar et al., 2018 ) , DROP ( Dua et al., 2019 ) , KOR-Bench ( Ma et al., 2024 ) , HellaSwag ( Zellers et al., 2019 ) , BIG-Bench Hard ( Suzgun et al., 2023 ) , BIG-Bench Extra Hard ( Kazemi et al., 2025 ) , MuSR ( Sprague et al., 2023 ) , ZebraLogic ( Lin et al., 2025 ) , PrOntoQA ( Saparov and He, 2022 ) , PIQA ( Bisk et al., 2020 ) , OCNLI ( Hu et al., 2020 ) , BIG-Bench Hard-CN ( Opencompass Team, 2023 )

• Coding : CRUXEval ( Gu et al., 2024 ) , MultiPL-E ( Cassano et al., 2023 ) , BigCodeBench ( Zhuo et al., 2024 ) , LiveCodeBench ( Jain et al., 2024 ) , Spider ( Yu et al., 2018 ) , BIRD ( Li et al., 2023 ) , HumanEval+ ( Liu et al., 2023 ) , MBPP+ ( Liu et al., 2023 )

• Math : OlympiadBench ( He et al., 2024 ) , AIME 2025 ( AIME, 2025 ) , Omni-MATH ( Gao et al., 2024 ) , GSM-Plus ( Li et al., 2024 ) , CMATH ( Wei et al., 2023 )

• Agent & Alignment : BFCL ( Patil et al., 2025 ) , IFEval ( Zhou et al., 2023 ) , Nexus Function Calling Benchmark ( Nexusflow.ai Team, 2023 )

We report the comparative scores and TPF (tokens per forward) of LLaDA2.1-flash and LLaDA2.1-mini against other models in Tables 1 and 2 , respectively. From the results, we observe that LLaDA2.1’s scores under S Mode decrease compared to LLaDA2.0, but a substantial improvement in TPF is achieved. While under Q Mode , LLaDA2.1 surpasses the results of LLaDA2.0 on both mini and flash model.

In Table 3 , we focus on showcasing the speed performance of LLaDA2.1 in S Mode . It can be observed that LLaDA2.1 exhibits significant speed variations across different domains, being highest in the code domain and lowest in instruction following. Specifically, after quantization, LLaDA2.1-flash achieves a peak TPS of 891.74 on HumanEval+, while LLaDA2.1-mini reaches 1586.93 in peak TPS, demonstrating significant speed advantages.

As shown in Table 4 , under the same S Mode setting, Multi-Block Editing (MBE) yields consistent performance improvements across benchmarks for both Flash and Mini variants, at the cost of a modest reduction in throughput. The gains are particularly evident on reasoning and coding tasks, indicating that iterative cross-block refinement effectively corrects local errors and improves global consistency without substantially compromising decoding efficiency.

Figure 3 further illustrates the throughput (in terms of token per sec) comparison of LLaDA 2.1 variants against LLaDA 2.0, Ling, and Qwen-3 across 5 different benchmark domains as shown in Table 3 . This comparison spotlights LLaDA-2.1 (S Mode)’s striking speed advantage: it achieves dramatically faster inference while sacrificing only a negligible sliver of output quality.

## 6 Outlook and Limitation

#### Tradeoff Between Inference Speed and Accuracy

While LLaDA2.1 significantly improves inference speed, a clear speed-accuracy tradeoff persists, particularly with noticeable performance differences across various domains. It is necessary to adjust threshold parameters for different domains to balance speed and accuracy. In structured-data fields such as code and math, setting S Mode achieves high speed with little accuracy loss. However, in some general chat cases, these settings can cause undesirable output. In such cases, we recommend adjusting the parameters to Q Mode . Our conjecture is that this pattern may be related to the model’s inherent preference for structured data or the distributional characteristics of training dataset. Further validation will be conducted in our future research.

#### Editable Enhanced dLLM

Although dLLMs inherently support high parallelism, theoretically offering speed advantages over AR models, our experimental observations show that this high parallelism also introduces a higher error rate compared to AR models. These hidden errors can reduce the model’s confidence in subsequent reasoning, ultimately slowing down the overall process. Therefore, timely editing to correct errors is essential. In our case analysis of LLaDA2.1, we observed that prompt editing corrected decoding errors, helping to maintain higher inference speeds. However, research on the editing capabilities of dLLMs is still in its early stages. We anticipate that future work, such as integrating editing into reinforcement learning, will further enhance the performance of editable dLLMs.

#### LLaDA2.1 remains in an experimental phase. Although rare, certain edge cases may occur.

Empirical observations show that aggressively lowering the masking threshold τ mask \tau_{\text{mask}} can quickly generate “rough drafts”. Although the model’s self-correction can partially alleviate the “stuttering” artifacts (such as n-gram repetitions) caused by independent parallel sampling, balancing drafting speed with the quality of the initial structure remains a key operational frontier. Overall, by unifying dynamic inference, hybrid training, and principled reinforcement learning, our work establishes a solid foundation for self-correcting discrete diffusion language models.

#### Conclusion

Overall, LLaDA2.1 introduces an editing feature, which, through cumulative error correction, significantly lowered the decoding threshold of the dLLM and yielded considerable inference speed benefits. However, this model still faces many unresolved issues, and we anticipate that more powerful editable dLLMs will deliver even more unexpected and impressive results.

## References

AIME (2025) AIME AIME Problems and Solutions . External Links: Link Cited by: 4th item .

[2] Aleph-Alpha Alpha-MoE: a megakernel for faster tensor parallel inference . External Links: Link Cited by: §4.2 .

[3] Ant Group Team and SGLang Team Power Up Diffusion LLMs: Day-0 Support for LLaDA 2.0 | LMSYS Org . External Links: Link Cited by: §4.1 , §4.2 .

Arriola et al. (2025) M. Arriola, A. Gokaslan, J. T. Chiu, Z. Yang, Z. Qi, J. Han, S. S. Sahoo, and V. Kuleshov Block diffusion: interpolating between autoregressive and diffusion language models . arXiv preprint arXiv:2503.09573 . Cited by: §3.2 .

Bie et al. (2025) T. Bie, M. Cao, K. Chen, L. Du, M. Gong, Z. Gong, Y. Gu, J. Hu, Z. Huang, Z. Lan, C. Li, C. Li, J. Li, Z. Li, H. Liu, L. Liu, G. Lu, X. Lu, Y. Ma, J. Tan, L. Wei, J. Wen, Y. Xing, X. Zhang, J. Zhao, D. Zheng, J. Zhou, J. Zhou, Z. Zhou, L. Zhu, and Y. Zhuang LLaDA2.0: Scaling Up Diffusion Language Models to 100B . arXiv . External Links: 2512.15745 , Document Cited by: §4.1 .

Bisk et al. (2020) Y. Bisk, R. Zellers, J. Gao, Y. Choi, et al. Piqa: reasoning about physical commonsense in natural language . In Proceedings of the AAAI conference on artificial intelligence , Vol. 34 , pp. 7432–7439 . Cited by: 2nd item .

Cassano et al. (2023) F. Cassano, J. Gouwar, D. Nguyen, S. Nguyen, L. Phipps-Costin, D. Pinckney, M. Yee, Y. Zi, C. J. Anderson, M. Q. Feldman, et al. MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code Generation . IEEE Transactions on Software Engineering 49 ( 7 ), pp. 3675–3691 . Cited by: 3rd item .

Dua et al. (2019) D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning over Paragraphs . arXiv preprint arXiv:1903.00161 . Cited by: 2nd item .

Fu et al. (2025) W. Fu, J. Gao, X. Shen, C. Zhu, Z. Mei, C. He, S. Xu, G. Wei, J. Mei, J. Wang, T. Yang, B. Yuan, and Y. Wu AReaL: a large-scale asynchronous reinforcement learning system for language reasoning . External Links: 2505.24298 , Link Cited by: §4.1 .

Gao et al. (2024) B. Gao, F. Song, Z. Yang, Z. Cai, Y. Miao, Q. Dong, L. Li, C. Ma, L. Chen, R. Xu, et al. Omni-math: a universal olympiad level mathematic benchmark for large language models . arXiv preprint arXiv:2410.07985 . Cited by: 4th item .

Gu et al. (2024) A. Gu, B. Rozière, H. Leather, A. Solar-Lezama, G. Synnaeve, and S. I. Wang CruxEval: A Benchmark for Code Reasoning, Understanding and Execution . arXiv preprint arXiv:2401.03065 . Cited by: 3rd item .

He et al. (2024) C. He, R. Luo, Y. Bai, S. Hu, Z. L. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, et al. OlympiadBench: A Challenging Benchmark for Promoting AGI with Olympiad-Level Bilingual Multimodal Scientific Problems . arXiv preprint arXiv:2402.14008 . Cited by: 4th item .

Hu et al. (2020) H. Hu, K. Richardson, L. Xu, L. Li, S. Kübler, and L. S. Moss Ocnli: original chinese natural language inference . arXiv preprint arXiv:2010.05444 . Cited by: 2nd item .

Huang et al. (2023) Y. Huang, Y. Bai, Z. Zhu, J. Zhang, J. Zhang, T. Su, J. Liu, C. Lv, Y. Zhang, Y. Fu, et al. C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models . Advances in Neural Information Processing Systems 36 , pp. 62991–63010 . Cited by: 1st item .

InclusionAI (2025) InclusionAI dFactory: Easy and Efficient dLLM Fine-Tuning . External Links: Link Cited by: §4.1 .

Jain et al. (2024) N. Jain, K. Han, A. Gu, W. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica Livecodebench: holistic and contamination free evaluation of large language models for code . arXiv preprint arXiv:2403.07974 . Cited by: 3rd item .

Joshi et al. (2017) M. Joshi, E. Choi, D. S. Weld, and L. Zettlemoyer Triviaqa: a large scale distantly supervised challenge dataset for reading comprehension . arXiv preprint arXiv:1705.03551 . Cited by: 1st item .

Kang et al. (2025) W. Kang, K. Galim, S. Oh, M. Lee, Y. Zeng, S. Zhang, C. Hooper, Y. Hu, H. I. Koo, N. I. Cho, and K. Lee ParallelBench: Understanding the Trade-offs of Parallel Decoding in Diffusion LLMs . arXiv . Note: arXiv:2510.04767 [cs] External Links: Link , Document Cited by: §1 .

Kazemi et al. (2025) M. Kazemi, B. Fatemi, H. Bansal, J. Palowitch, C. Anastasiou, S. V. Mehta, L. K. Jain, V. Aglietti, D. Jindal, Y. P. Chen, et al. Big-bench extra hard . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 26473–26501 . Cited by: 2nd item .

Lee et al. (2025) S. Lee, S. Kim, S. Kim, J. Park, and D. Park Effective Test-Time Scaling of Discrete Diffusion through Iterative Refinement . arXiv . Note: arXiv:2511.05562 [cs] External Links: Link , Document Cited by: §1 .

Li et al. (2023) J. Li, B. Hui, G. Qu, J. Yang, B. Li, B. Li, B. Wang, B. Qin, R. Geng, N. Huo, et al. Can llm already serve as a database interface? a big bench for large-scale database grounded text-to-sqls . Advances in Neural Information Processing Systems 36 , pp. 42330–42357 . Cited by: 3rd item .

Li et al. (2024) Q. Li, L. Cui, X. Zhao, L. Kong, and W. Bi Gsm-plus: a comprehensive benchmark for evaluating the robustness of llms as mathematical problem solvers . arXiv preprint arXiv:2402.19255 . Cited by: 4th item .

Lin et al. (2025) B. Y. Lin, R. L. Bras, K. Richardson, A. Sabharwal, R. Poovendran, P. Clark, and Y. Choi Zebralogic: on the scaling limits of llms for logical reasoning . arXiv preprint arXiv:2502.01100 . Cited by: 2nd item .

Ling Team et al. (2025) Ling Team et al. Every step evolves: scaling reinforcement learning for trillion-scale thinking model . External Links: 2510.18855 , Link Cited by: §4.1 .

Liu et al. (2023) J. Liu, C. S. Xia, Y. Wang, and L. Zhang Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation . Advances in Neural Information Processing Systems 36 , pp. 21558–21572 . Cited by: 3rd item .

Ma et al. (2024) K. Ma, X. Du, Y. Wang, H. Zhang, Z. Wen, X. Qu, J. Yang, J. Liu, M. Liu, X. Yue, et al. Kor-bench: benchmarking language models on knowledge-orthogonal reasoning tasks . arXiv preprint arXiv:2410.06526 . Cited by: 2nd item .

Ma et al. (2025) Y. Ma, L. Du, L. Wei, K. Chen, Q. Xu, K. Wang, G. Feng, G. Lu, L. Liu, X. Qi, et al. Dinfer: an efficient inference framework for diffusion language models . arXiv preprint arXiv:2510.08666 . Cited by: §4.3 .

Mei et al. (2025) Z. Mei, W. Fu, K. Li, G. Wang, H. Zhang, and Y. Wu ReaL: efficient rlhf training of large language models with parameter reallocation . In Proceedings of the Eighth Conference on Machine Learning and Systems, MLSys 2025, Santa Clara, CA, USA, May 12-15, 2025 , Cited by: §4.1 .

Nexusflow.ai Team (2023) Nexusflow.ai Team NexusRaven-v2: surpassing gpt-4 for zero-shot function calling . External Links: Link Cited by: 5th item .

Opencompass Team (2023) Opencompass Team Open-compass/opencompass . External Links: Link Cited by: 2nd item .

Ou et al. (2025) J. Ou, J. Han, M. Xu, S. Xu, J. Xie, S. Ermon, Y. Wu, and C. Li Principled RL for Diffusion LLMs Emerges from a Sequence-Level Perspective . arXiv . Note: arXiv:2512.03759 [cs] External Links: Link , Document Cited by: §1 , §3.2 .

Patil et al. (2025) S. G. Patil, H. Mao, C. Cheng-Jie Ji, F. Yan, V. Suresh, I. Stoica, and J. E. Gonzalez The berkeley function calling leaderboard (bfcl): from tool use to agentic evaluation of large language models . In Forty-second International Conference on Machine Learning , Cited by: 5th item .

Qiu et al. (2025) S. Qiu, S. Guo, Z. Song, Y. Sun, Z. Cai, J. Wei, T. Luo, Y. Yin, H. Zhang, Y. Hu, et al. Phybench: holistic evaluation of physical perception and reasoning in large language models . arXiv preprint arXiv:2504.16074 . Cited by: 1st item .

Rajpurkar et al. (2018) P. Rajpurkar, R. Jia, and P. Liang Know what you don’t know: unanswerable questions for squad . arXiv preprint arXiv:1806.03822 . Cited by: 2nd item .

Rein et al. (2024) D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman GPQA: A Graduate-Level Google-Proof Q&Q Benchmark . In First Conference on Language Modeling , Cited by: 1st item .

Rütte et al. (2025) D. v. Rütte, J. Fluri, Y. Ding, A. Orvieto, B. Schölkopf, et al. Generalized Interpolating Discrete Diffusion . ( en ). External Links: Link Cited by: §1 .

Saparov and He (2022) A. Saparov and H. He Language models are greedy reasoners: a systematic formal analysis of chain-of-thought . arXiv preprint arXiv:2210.01240 . Cited by: 2nd item .

Song et al. (2025) Y. Song, Z. Zhang, C. Luo, P. Gao, F. Xia, H. Luo, Z. Li, Y. Yang, et al. Seed diffusion: a large-scale diffusion language model with high-speed inference . External Links: 2508.02193 Cited by: §1 .

Sprague et al. (2023) Z. Sprague, X. Ye, K. Bostrom, S. Chaudhuri, and G. Durrett Musr: testing the limits of chain-of-thought with multistep soft reasoning . arXiv preprint arXiv:2310.16049 . Cited by: 2nd item .

Suzgun et al. (2023) M. Suzgun, N. Scales, N. Schärli, S. Gehrmann, Y. Tay, H. W. Chung, et al. Challenging big-bench tasks and whether chain-of-thought can solve them . In Findings of the Association for Computational Linguistics: ACL 2023 , pp. 13003–13051 . Cited by: 2nd item .

Wang et al. (2025a) C. Wang, P. Rashidinejad, D. Su, S. Jiang, S. Wang, S. Zhao, C. Zhou, S. Z. Shen, F. Chen, T. Jaakkola, Y. Tian, and B. Liu SPG: sandwiched policy gradient for masked diffusion language models . arXiv preprint arXiv:2510.09541 . Cited by: §1 , §3.2 .

Wang et al. (2025b) G. Wang, Y. Schiff, S. S. Sahoo, and V. Kuleshov Remasking Discrete Diffusion Models with Inference-Time Scaling . ( en ). External Links: Link Cited by: §1 .

Wang et al. (2025c) Y. Wang, L. Yang, B. Li, Y. Tian, K. Shen, and M. Wang Revolutionizing reinforcement learning framework for diffusion large language models . arXiv preprint arXiv:2509.06949 . Cited by: §1 , §3.2 .

Wang et al. (2024) Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, et al. MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark . In The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track , Cited by: 1st item .

Wei et al. (2023) T. Wei, J. Luan, W. Liu, S. Dong, and B. Wang Cmath: can your language model pass chinese elementary school math test? . arXiv preprint arXiv:2306.16636 . Cited by: 4th item .

Yu et al. (2018) T. Yu, R. Zhang, K. Yang, M. Yasunaga, D. Wang, Z. Li, J. Ma, I. Li, Q. Yao, S. Roman, et al. Spider: a large-scale human-labeled dataset for complex and cross-domain semantic parsing and text-to-sql task . arXiv preprint arXiv:1809.08887 . Cited by: 3rd item .

Zellers et al. (2019) R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi Hellaswag: can a machine really finish your sentence? . arXiv preprint arXiv:1905.07830 . Cited by: 2nd item .

Zhou et al. (2023) J. Zhou, T. Lu, S. Mishra, S. Brahma, et al. Instruction-Following Evaluation for Large Language Models . arXiv preprint arXiv:2311.07911 . Cited by: 5th item .

Zhuo et al. (2024) T. Y. Zhuo, M. C. Vu, J. Chim, H. Hu, W. Yu, R. Widyasari, I. N. B. Yusuf, H. Zhan, J. He, I. Paul, et al. Bigcodebench: benchmarking code generation with diverse function calls and complex instructions . arXiv preprint arXiv:2406.15877 . Cited by: 3rd item .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
