##### Report GitHub Issue

Content selection saved. Describe the issue below:

# SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for Large Language Model Alignment

###### Abstract

Aligning Large Language Models (LLMs) with human preferences typically relies on external supervision, which faces critical limitations: human annotations are scarce and subjective, reward models are vulnerable to reward hacking, and self-evaluation methods suffer from prompt sensitivity and biases. In this work, we propose stable rank , an intrinsic, annotation-free quality signal derived from model representations. Stable rank measures the effective dimensionality of hidden states by computing the ratio of total variance to dominant-direction variance, capturing quality through how information distributes across representation dimensions. Empirically, stable rank achieves 84.04% accuracy on RewardBench and improves task accuracy by an average of 11.3 percentage points over greedy decoding via Best-of-N sampling. Leveraging this insight, we introduce Stable Rank Group Relative Policy Optimization (SR-GRPO) , which uses stable rank as a reward signal for reinforcement learning. Without external supervision, SR-GRPO improves Qwen2.5-1.5B-Instruct by 10% on STEM and 19% on mathematical reasoning, outperforming both learned reward models and self-evaluation baselines. Our findings demonstrate that quality signals can be extracted from internal model geometry, offering a path toward scalable alignment without external supervision.

## 1 Introduction

The alignment of Large Language Models (LLMs) with human preferences typically relies on Reinforcement Learning from Human Feedback (RLHF) ( Ouyang et al., 2022 ; Bai et al., 2022 ) . Despite its success, this paradigm depends heavily on external supervision. Human judgments are subjective and context-dependent, making it difficult to train robust reward models ( Chakraborty et al., 2024 ; Wang et al., 2023 ) , and learned proxies are susceptible to reward hacking ( Casper et al., 2023 ) . The sparsity of annotations further limits the model’s ability to fine-grained behaviors ( Wu et al., 2023 ) .

These limitations have motivated various attempts to reduce annotation dependence. Direct Preference Optimization ( Rafailov et al., 2023 ) eliminates explicit reward modeling but still requires preference datasets. Verifiable rewards ( DeepSeek-AI, 2025 ; Lambert et al., 2024 ) leverage ground-truth outcomes but only apply where automatic verification is feasible. Self-evaluation methods ( Yuan et al., 2024 ; Lee et al., 2024 ; Garg et al., 2025 ) suffer from prompt sensitivity and systematic biases ( Zheng et al., 2023 ; Wang et al., 2024 ) . Crucially, all these approaches still evaluate quality through external signals while overlooking information embedded in the model’s own representations.

Yet the validity of a generation should be reflected in its underlying computation. When a model outputs “The capital of France is Paris,” its hidden states encode activated factual knowledge ( He et al., 2024c ) ; when it hallucinates, different activation patterns emerge ( Chen et al., 2024 ) . This raises a natural question: Can we measure text quality directly from internal signals, enabling LLM alignment without external supervision?

In this work, we show that a simple geometric property of LLM hidden states, their effective dimensionality, provides a reliable signal for LLM response quality. We propose to use stable rank ( Rudelson and Vershynin, 2007 ) , a matrix-theoretic measure as an unsupervised proxy for generation quality. Stable rank quantifies how many independent semantic directions a response occupies by measuring the ratio of total variance to dominant-direction variance in the hidden-state representation. It balances representational richness with coherence: a high stable rank indicates that information spreads across many dimensions rather than concentrating in a few. The theoretical motivation comes from two lines of work. First, the softmax bottleneck analysis shows that accurate language modeling requires navigating a high-dimensional semantic manifold, as the contextual probability distribution of natural language is inherently high-rank ( Yang et al., 2018 ; Godey et al., 2024 ) . Second, literature also shows that when representations collapse into a narrow cone, expressiveness is severely limited and generation quality degrades ( Gao et al., 2019 ) . We therefore hypothesize that this principle extends to individual LLM responses: high-quality generations should maintain higher effective dimensionality, while low-quality outputs exhibit rank collapse.

We validate this hypothesis in two settings. First, as a zero-shot reward proxy, stable rank achieves 84.04% accuracy on RewardBench ( Lambert et al., 2025 ) with Qwen3-8B ( Yang et al., 2025 ) , matching LLM-as-Judge baselines without any training. Figure 1 illustrates this geometrically: while PCA projections of LLM representations show overlap between good and bad responses, stable rank cleanly separates them. Second, stable rank-guided Best-of-N selection consistently outperforms greedy decoding across four model families on STEM and mathematics benchmarks, with average gains of 11.3% at N = 16 N=16 .

Building on these findings, we introduce Stable Rank Group Relative Policy Optimization (SR-GRPO) , which uses stable rank as an intrinsic reward signal for reinforcement learning. By replacing external supervision with this geometric signal derived directly from the reference model, we enable fully annotation-free alignment. On Qwen2.5-1.5B-Instruct ( Yang et al., 2024 ) , SR-GRPO outperforms GRPO with learned reward models by 10 to 19% on reasoning tasks at zero annotation cost, and surpasses self-reward baselines by 8 to 9%. Consistent gains on DeepSeek-R1-Distill-Qwen-1.5B ( DeepSeek-AI, 2025 ) confirm robustness across model families.

To understand why stable rank succeeds as a quality signal, we analyze its correlations with interpretable text metrics. We find that stable rank captures three quality dimensions: semantic coherence, where sentences build on each other while staying relevant to the prompt; information density over verbosity, favoring concise, non-repetitive text; and sensitivity to reasoning words like “however” and “because” at key turning points.

Our contributions are summarized as follows: • We propose SR-GRPO, which uses stable rank as a dense reward signal in reinforcement learning, eliminating dependency on preference datasets or external verifiers.

• We demonstrate that SR-GRPO improves reasoning across multiple benchmarks, thus establishing intrinsic geometric signals as a viable basis for LLM alignment.

• Beyond reinforcement learning, we also show that stable rank offers a reliable zero-shot reward proxy for evaluating LLM responses, and integrates naturally into best-of-N decoding.

## 2 Stable Rank as an Intrinsic Quality Metric

We propose stable rank ( Rudelson and Vershynin, 2007 ) as an unsupervised quality signal derived from LLM representations. This section defines the metric, explains its geometric motivation, and validates its effectiveness as a reward proxy.

### 2.1 Definition

For a sequence of T T tokens, we extract the hidden state activation matrix 𝐇 ∈ ℝ T × d \mathbf{H}\in\mathbb{R}^{T\times d} from the last layer of an LLM. Let σ 1 ≥ σ 2 ≥ ⋯ ≥ σ min ⁡ ( T , d ) ≥ 0 \sigma_{1}\geq\sigma_{2}\geq\dots\geq\sigma_{\min(T,d)}\geq 0 denote the singular values of 𝐇 \mathbf{H} . The stable rank is defined as: SR ​ ( 𝐇 ) = ‖ 𝐇 ‖ F 2 ‖ 𝐇 ‖ 2 2 = ∑ i σ i 2 σ 1 2 . \text{SR}(\mathbf{H})=\frac{\|\mathbf{H}\|_{F}^{2}}{\|\mathbf{H}\|_{2}^{2}}=\frac{\sum_{i}\sigma_{i}^{2}}{\sigma_{1}^{2}}. (1) Stable rank measures the effective dimensionality of 𝐇 \mathbf{H} : if a single singular value dominates, SR ​ ( 𝐇 ) ≈ 1 \text{SR}(\mathbf{H})\approx 1 , indicating representation collapse; when singular values are balanced, stable rank approaches rank ​ ( 𝐇 ) \text{rank}(\mathbf{H}) , reflecting a rich, high-dimensional representation. Intuitively, low stable rank means token representations cluster along a few dominant directions, while a high stable rank means they spread across the embedding space.

##### Theoretical motivation.

The theoretical motivation comes from two lines of work. The softmax bottleneck ( Yang et al., 2018 ; Godey et al., 2024 ) implies that expressive language modeling requires high-rank representations, while representation collapse is a known symptom of degraded generation ( Gao et al., 2019 ) . Stable rank directly measures this effective dimensionality, making it a natural candidate for quality assessment. We validate this connection empirically below and through correlation analysis in Section 5 .

##### Implementation.

Given a prompt-response pair formatted with the model’s chat template, we perform a forward pass and extract the hidden state matrix 𝐇 ∈ ℝ T × d \mathbf{H}\in\mathbb{R}^{T\times d} from the final hidden layer, where T T is the total number of tokens. We use final-layer activations because they aggregate information across all preceding layers and are directly related to the final text generation. Stable rank is then computed from 𝐇 \mathbf{H} via Equation 1 . Cross-layer analysis in Appendix A confirms that the final layer embeddings yield the strongest quality signal.

### 2.2 Empirical Validation: Stable Rank as Zero-Shot Reward Proxy

We evaluate stable rank as a zero-shot proxy for human preference by testing whether it can predict the preferred response in a pair. This assessment checks whether stable rank can serve as a reliable reward signal without any model-specific training.

##### Setup.

We use RewardBench ( Lambert et al., 2025 ) , a benchmark containing 2,985 preference pairs across five categories: Chat, Chat-Hard, Safety, Code, and Math. For each pair, we compute stable rank for both responses and predict the one with the higher stable rank as preferred. We compare against three baseline methods: (1) Pointwise Scoring (Point.) ( Kim et al., 2024 ) : prompting the LLM to score each response on a 1-5 scale; (2) Pairwise Comparison (Pair.) ( Kim et al., 2024 ) : prompting the LLM to directly compare two responses; (3) IPO ( Garg et al., 2025 ) : using implicit preference scores derived from Yes/No token probabilities. We evaluate five models: Qwen2.5-1.5B-Instruct ( Yang et al., 2024 ) , Qwen3-0.6B ( Yang et al., 2025 ) , Qwen3-8B ( Yang et al., 2025 ) , Llama-3.1-8B-Instruct ( Dubey et al., 2024 ) , and Phi-3.5-mini-Instruct ( Abdin et al., 2024 ) . For stable rank, we format inputs as prompt-response pairs using each model’s native chat template, extract final-layer hidden states for the response tokens only, and compute stable rank via Eq. 1 . Prompts and implementation details are in Appendix B .

##### Results.

Table 1 shows stable rank consistently outperforms baselines across model scales. On Qwen3-8B, it achieves 84.04% accuracy, surpassing Pointwise (83.70%) and IPO (78.02%). The advantage is more pronounced on smaller models: stable rank achieves 75.95% on Qwen2.5-1.5B-Instruct, outperforming the best baseline (IPO, 65.85%) by 10.1 percentage points. Generative baselines exhibit high variance across scales. Pointwise scoring excels on large models (83.70% on Qwen3-8B) but collapses on smaller ones (37.15% on Qwen2.5-1.5B), likely because smaller models lack the instruction-following capability to produce calibrated scores. Pairwise comparison shows the opposite pattern, performing better on small models but degrading on Qwen3-8B (71.98%). IPO maintains relative stability (65.57%–78.02%) but still underperforms stable rank across all models. The consistent advantage of stable rank, especially on smaller models, suggests that LLM’s intrinsic geometric signals are more robust than prompt-based evaluation. Prompt-based methods require LLMs to follow evaluation instructions and produce calibrated scores, which smaller models often struggle with. Stable rank has no such dependency, making it particularly suitable for aligning tiny LLMs.

### 2.3 Empirical Validation: Best-of-N Decoding with Stable Rank

We next evaluate stable rank as a test-time quality signal in Best-of-N decoding, where the model samples multiple candidate responses and selects the one with the highest stable rank. This setup tests whether stable rank can guide inference and improve task performance beyond standard greedy decoding.

##### Setup.

For each prompt, we sample N ∈ { 1 , 4 , 8 , 16 } N\in\{1,4,8,16\} responses (temperature 0.7, top-p 0.9) and select the one with the highest stable rank. We test on STEM benchmarks (GPQA ( Rein et al., 2024 ) , MMLU-redux ( Gema et al., 2025 ) ) and mathematical reasoning tasks (MATH500 ( Lightman et al., 2023 ) , OlympiadBench ( He et al., 2024a ) , AMC23 ( knoveleng, 2023 ) ) across four models: Qwen2.5-1.5B-Instruct ( Yang et al., 2024 ) , Phi-3.5-mini-Instruct ( Abdin et al., 2024 ) , Llama-3.2-1B-Instruct ( Dubey et al., 2024 ) , and DeepSeek-R1-Distill-Qwen-1.5B ( DeepSeek-AI, 2025 ) . We compare against random selection to isolate the effect of the selection criterion from sampling diversity.

##### Results.

Figure 2 shows that stable rank-guided selection consistently improves over greedy decoding across all models. At N=16, Llama-3.2-1B achieves the largest gain (+20.5%), followed by Qwen2.5-1.5B (+17.0%) and DeepSeek-R1 (+10.2%), and Phi-3.5-mini shows a moderate improvement of +8.5%. Stable rank also outperforms random selection. On Llama-3.2-1B at N=16, stable rank (26.5% avg.) exceeds random selection (19.8%) by 33.8%. Notably, random selection often degrades performance below greedy decoding, such as − - 16.1% on Llama-3.2-1B at N=8. In contrast, stable rank consistently yields positive gains, demonstrating that it identifies high-quality responses rather than merely benefiting from sampling diversity. These results confirm that stable rank captures quality signals that correlate strongly with correctness. Complete results are provided in Appendix D .

## 3 Stable Rank Group Relative Policy Optimization (SR-GRPO)

Having established an empirical correlation between stable rank and response quality, we next ask whether using stable rank as a reward signal in reinforcement learning can further improve LLM alignment behavior. Because stable rank requires no labeled data and can be computed for any generated response, it provides a simple and scalable dense reward for reinforcement learning.

### 3.1 Setup

Let π ref \pi_{\text{ref}} denote a reference model and π ϕ \pi_{\phi} the trainable policy initialized from π ref \pi_{\text{ref}} . Given a prompt x x , the policy generates a response y ∼ π ϕ ( ⋅ | x ) y\sim\pi_{\phi}(\cdot|x) . Our goal is to optimize π ϕ \pi_{\phi} to generate higher-quality responses, using stable rank as a proxy reward.

### 3.2 Training Procedure

We build on Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) , which compares responses within a sampled group to obtain relative quality signals, avoiding the need for a learned value function. This avoids the need to train a separate critic and suits our setting where rewards come from a geometric metric.

For each prompt x x , we sample K K responses from the current policy and compute their stable rank on the frozen reference model π ref \pi_{\text{ref}} . Using a frozen model is critical: it provides a stationary reward signal that the policy cannot manipulate by changing its own internal geometry.

We standardize rewards within each group to obtain scale-invariant learning signals: A k = ( r k − μ ) / ( σ + ϵ ) A_{k}=(r_{k}-\mu)/(\sigma+\epsilon) , where μ \mu and σ \sigma are the group mean and standard deviation. The training objective is: 𝒥 ( ϕ ) = 𝔼 x [ 1 K ∑ k = 1 K ρ k A k − β D KL ( π ϕ ∥ π ref ) ] \mathcal{J}(\phi)=\mathbb{E}_{x}\left[\frac{1}{K}\sum_{k=1}^{K}\rho_{k}A_{k}-\beta D_{\text{KL}}(\pi_{\phi}\|\pi_{\text{ref}})\right] (2) where ρ k = π ϕ ​ ( y k | x ) / π ϕ old ​ ( y k | x ) \rho_{k}=\pi_{\phi}(y_{k}|x)/\pi_{\phi_{\text{old}}}(y_{k}|x) is the importance ratio, ϕ old \phi_{\text{old}} denotes the parameters before the current update, and β \beta controls the KL penalty. Algorithm 1 summarizes the procedure.

##### Computational efficiency.

Computing stable rank requires O ⁡ ( T ​ d ) O(Td) operations: O ⁡ ( T ​ d ) O(Td) for the Frobenius norm and O ⁡ ( T ​ d ) O(Td) per power iteration for the spectral norm. This overhead is negligible compared to the transformer forward pass. Stable rank is also robust to input truncation: using only 512 tokens achieves nearly identical accuracy (Appendix H ).

## 4 Alignment Experiments

### 4.1 Experiment Setup

We evaluate SR-GRPO on two models: Qwen2.5-1.5B-Instruct ( Yang et al., 2024 ) and DeepSeek-R1-Distill-Qwen-1.5B ( DeepSeek-AI, 2025 ) . All methods are trained on prompts from SmolTalk2 ( Allal et al., 2025 ) , which provides diverse topics and tasks. No preference labels are used during training; methods differ only in how they compute rewards from sampled responses. For SR-GRPO, we train with LoRA ( Hu et al., 2022 ) and compute stable rank on the base model without LoRA adapters, which also serves as the frozen reference.

Benchmarks. We evaluate on three categories: (1) STEM tasks : GPQA ( Rein et al., 2024 ) , a graduate-level science QA benchmark requiring expert knowledge, and MMLU-redux ( Gema et al., 2025 ) , a curated subset of MMLU with corrected labels; (2) Mathematical reasoning : MATH500 ( Lightman et al., 2023 ) , a subset of competition mathematics problems, AIME25 ( Zhang and Math-AI, 2025 ) , problems from the 2025 American Invitational Mathematics Examination, OlympiadBench ( He et al., 2024b ) , olympiad-level math and physics problems, and AMC23 ( knoveleng, 2023 ) , problems from the 2023 American Mathematics Competition; (3) General chat : WildBench ( Lin et al., 2025 ) , which evaluates open-ended conversation quality using GPT-4o mini ( OpenAI, 2025 ) as a judge. For all benchmarks except WildBench, we report Pass@1 accuracy. WildBench ( Lin et al., 2025 ) evaluates open-ended conversation quality by comparing model outputs against reference responses using GPT-4o mini as a judge; scores are reported as Elo ratings.

Baselines. We compare SR-GRPO against two categories of methods:

(1) Reward Model (RM): We use Skywork-Reward-V2-Qwen3-1.7B ( Liu et al., 2025 ) , a widely used reward model trained on the Skywork preference dataset with the Bradley-Terry objective. We select a 1.7B model to match the scale of our policy models, ensuring fair comparison with self-evaluation methods that use the policy model itself for reward computation.

(2) Self-Evaluation Methods: These methods derive rewards from the model’s own outputs without external labels: • Self-Reward ( Yuan et al., 2024 ) : The model evaluates its own completions using the pointwise scoring prompt (Appendix B ), generating a 1-5 score that serves as the reward signal.

• Perplexity: We use the negative log-likelihood of the completion as the reward, where lower perplexity indicates higher fluency.

• IPO ( Garg et al., 2025 ) : The model acts as a binary classifier, determining response quality by generating “Yes” or “No”. We extract logits for both tokens from the first output position and compute their probabilities via softmax. The probability of “Yes” serves as the reward signal.

All methods use the same GRPO training configurations (K=8 responses per prompt, β \beta =0.01) to ensure fair comparison. Full training details are in Appendix E .

### 4.2 Results Analysis

Table 2 shows that SR-GRPO consistently outperforms both reward model and self-evaluation baselines across all categories, despite using no external labels.

Reasoning improvements. On Qwen2.5-1.5B-Instruct, SR-GRPO improves average mathematical reasoning accuracy by 4.4 percentage points (28.0% to 32.4%), with particularly strong gains on competition-level problems: AMC improves from 35.0% to 37.5% and MATH from 48.0% to 52.4%. On DeepSeek-R1-Distill-Qwen-1.5B, which already achieves 58.5% on math tasks, SR-GRPO still improves performance to 64.7%, demonstrating effectiveness even on reasoning-specialized models. The gains on OlympiadBench (43.6% to 58.5%) suggest that stable rank rewards the structured reasoning patterns required for complex problem-solving.

Comparison with baselines. The reward model shows minimal or even negative impact on several tasks (e.g., GPQA drops from 19.0% to 15.7% on Qwen2.5-1.5B), suggesting that models trained on general preference data may not transfer well to specialized reasoning domains. Self-evaluation methods show inconsistent patterns: Self-Reward matches SR-GRPO on AIME (13.3%) but underperforms on STEM tasks (31.6% vs 34.5% avg.); Perplexity performs surprisingly well on DeepSeek-R1 but lacks the consistency of SR-GRPO across both models. IPO degrades performance on several benchmarks, possibly because Yes/No probability signals are too coarse for nuanced quality distinctions.

General chat quality. SR-GRPO’s advantage extends beyond reasoning to open-ended conversation. On WildBench (WB-Elo), it achieves gains of 26.2 points on Qwen2.5-1.5B and 19.0 points on DeepSeek-R1, substantially outperforming all baselines. This indicates that stable rank captures qualities valued in general conversation, such as coherence and helpfulness, not just task-specific correctness. The consistent improvements across both reasoning benchmarks and open-ended chat suggest that stable rank provides a general-purpose quality signal rather than optimizing for narrow task metrics.

## 5 What Stable Rank Captures

To understand why stable rank can serve as an intrinsic reward, we analyze its correlations with interpretable text quality metrics on the RewardBench dataset. We compute 37 metrics spanning semantic coherence, information density, and linguistic structure. For each metric M M , we measure sample-level Pearson correlation with stable rank across 5,970 responses, and paired-difference Spearman correlation across 2,985 chosen/rejected pairs. The definitions and correlation tables are provided in Appendix F ; here we summarize key findings.

### 5.1 Stable Rank Captures Semantic Coherence

Table 3 presents the strongest correlations among semantic coherence metrics. Progression score ( ρ = 0.313 \rho=0.313 ) measures whether each sentence builds on the previous one. QA alignment consistency ( ρ = 0.316 \rho=0.316 ) captures whether relevance to the prompt remains stable throughout the response. Both correlate positively with stable rank. The strongest negative correlation appears with coherence standard deviation ( ρ = − 0.356 \rho=-0.356 ), where high values indicate erratic transitions between adjacent sentences. These patterns suggest stable rank can capture responses that maintain topical focus while developing ideas smoothly, avoiding the abrupt transitions characteristic of hallucinations or incoherent reasoning.

### 5.2 Stable Rank Distinguishes Density from Verbosity

Contrary to common reward hacking, where models maximize length, stable rank correlates negatively with token count ( ρ = − 0.294 \rho=-0.294 ) and sentence count ( ρ = − 0.368 \rho=-0.368 ). Instead, stable rank favors information density. Lexical diversity correlates positively ( ρ = 0.238 \rho=0.238 ). This metric measures the ratio of unique tokens to total tokens. Compression ratio also correlates positively ( ρ = 0.233 \rho=0.233 ). It measures the ratio of compressed to original text length. Table 3 presents key correlations. These patterns suggest stable rank penalizes verbose, repetitive text while rewarding concise responses with diverse vocabulary.

### 5.3 Stable Rank Highlights Key Logical Markers

In this section, we study the correlation between discourse markers and stable rank. Discourse markers are explicit phrases that signal logical relationships, such as “because” or “if”, or structural transitions, such as “however” or “first”. We use paired-difference analysis on N = 2,985 N=2{,}985 chosen and rejected pairs (Appendix F ) to correlate marker frequency, measured per 100 tokens, with stable rank while controlling for prompt context. We report both Pearson and Spearman correlations because the two can diverge when relationships are non-monotonic.

Table 4 shows that most marker categories, especially additive ( ρ = − 0.156 \rho=-0.156 ), conditional ( ρ = − 0.163 \rho=-0.163 ), and enumeration ( ρ = − 0.148 \rho=-0.148 ), have consistently negative correlations with stable rank, and the total marker count is also negatively associated ( ρ = − 0.204 \rho=-0.204 ). Responses that rely heavily on common connective words such as “moreover”, “first”, and “then” tend to receive a lower stable rank, which is consistent with Section 5.2 where stable rank disfavors verbose, pattern-like exposition in favor of compact information content.

Contrastive and causal markers follow a different pattern. Their Pearson correlations with stable rank are positive (contrastive r = 0.187 r=0.187 , causal r = 0.139 r=0.139 ), but their Spearman correlations are small. This divergence suggests that the presence of these markers matters more than their frequency: a few well-placed “however” or “because” phrases benefit stable rank, but overusing them does not. This aligns with linguistic intuition: contrastive and causal connectives are most informative when they mark key reasoning steps, not when they appear as formulaic filler.

### 5.4 Summary

Together, these correlation patterns align with established findings in text quality research. The strong association with semantic coherence metrics mirrors neural coherence models, which show that smooth semantic transitions predict text quality ( Mesgar and Strube, 2018 ; Cui et al., 2017 ) . The negative correlation with length while favoring information density addresses a well-documented failure mode in RLHF: length bias, where reward models favor longer responses regardless of quality ( Singhal et al., 2024 ) . Unlike learned reward models that often exploit this spurious correlation, stable rank’s geometric formulation inherently penalizes verbose, low-information content.

While these correlations are moderate in magnitude ( | ρ | ≈ 0.2 |\rho|\approx 0.2 – 0.4 0.4 ), they are consistent in direction across metrics and statistically significant ( p < 0.001 p<0.001 ), suggesting stable rank captures genuine quality signals rather than noise. These findings indicate that stable rank correlates with multiple dimensions of text quality, including coherence, density, and reasoning structure, suggesting it captures a meaningful aggregate signal rather than a single superficial feature. Qualitative examples illustrating how stable rank differentiates high-quality reasoning from repetition and verbosity are provided in Appendix J .

## 6 Ablation Studies

We conduct three ablation studies to validate our design choices.

Alternative intrinsic dimension metrics. We compare stable rank against three alternatives: condition number, which measures the ratio of largest to smallest singular value; PCA 95% variance, which counts principal components needed to capture 95% of variance; and effective rank ( Roy and Vetterli, 2007 ) , which uses entropy over the singular value distribution. On RewardBench, stable rank achieves 84.04% overall accuracy, outperforming PCA 95% variance (61.91%), effective rank (54.50%), and condition number (36.04%). The gap widens on harder categories such as Math and Safety. Stable rank succeeds because it aggregates information across the entire singular value spectrum through the Frobenius norm, making it robust to outliers. Condition number is sensitive to extreme singular values. Effective rank’s entropy weighting and PCA’s discrete component counting appear less suited for capturing quality distinctions. Full results are provided in Appendix G .

Context length. We examine how sequence truncation affects performance. Accuracy drops from 83.85% at 512 tokens to 62.59% at 128 tokens. Code suffers the largest degradation (87.91% to 24.80%) because truncation removes critical program logic. However, extending beyond 512 tokens yields negligible gains ( < < 0.2 percentage points). This indicates that stable rank captures core semantic structure rather than mechanically rewarding longer sequences. Details are provided in Appendix H .

Prompt format. We test six input templates across three models. Overall accuracy varies by at most 3 percentage points, with no format consistently outperforming others. This robustness simplifies deployment: practitioners can use simple formats without extensive tuning. Full results are shown in Appendix I .

## 7 Related Work

We review three lines of related work: alignment methods using external feedback, approaches that reduce reliance on human labels, and theoretical connections between representation geometry and generation quality.

### 7.1 Alignment with External Feedback Signals

The standard pipeline for aligning Large Language Models with human preferences is Reinforcement Learning from Human Feedback (RLHF) ( Ouyang et al., 2022 ; Bai et al., 2022 ) . RLHF trains a reward model on human preference data and then fine-tunes the policy to maximize this learned signal under a KL constraint to a reference model. This approach underpins LLMs such as ChatGPT and Llama ( Dubey et al., 2024 ) , but it inherits well-known issues: preference data are expensive and noisy, and reward models are vulnerable to reward hacking and distribution shift ( Casper et al., 2023 ; Skalse et al., 2022 ) . These limitations motivate supervised preference-based methods such as Direct Preference Optimization (DPO) ( Rafailov et al., 2023 ) , KTO ( Ethayarajh et al., 2024 ) , Bayesian RLHF ( Wang et al., 2023 ) , and MaxMin-RLHF ( Chakraborty et al., 2024 ) , which optimize the policy directly on pairwise comparisons without an explicit value network but still rely on curated preference datasets. Process reward models and generative reward models provide step-level scores and textual critiques for mathematical reasoning and general evaluation ( Zhang et al., 2025b ; Yin et al., 2025 ) .All these approaches keep supervision external to the model’s internal computation.

### 7.2 Alignment with Automatic Signals

A complementary line of work reduces reliance on human labels by using automatic supervision or signals derived from the model itself. Verifiable-reward methods such as DeepSeek-R1 ( DeepSeek-AI, 2025 ) and TÜLU 3 ( Lambert et al., 2024 ) replace human feedback with programmatic checkers; these methods work well in domains like mathematics and coding but do not generalize to open-ended tasks. Self-evaluation approaches treat the model, or another LLM, as a judge: Self-Rewarding Language Models ( Yuan et al., 2024 ) and RLAIF ( Lee et al., 2024 ) generate AI feedback instead of human labels, while IPO ( Garg et al., 2025 ) and Self-Rewarding PPO ( Zhang et al., 2025a ) derive preference signals from token-level probabilities. Closer to our setting, work on internal activations such as Factoscope ( He et al., 2024c ) and INSIDE ( Chen et al., 2024 ) shows that hidden states encode factuality and hallucination risk. Our method follows this direction, using a geometric statistic of activations as a reward signal for policy optimization.

### 7.3 Representation Geometry and Generation Quality

A theoretical foundation for rank-based quality measures comes from the softmax bottleneck analysis. Yang et al. (2018) show that the expressiveness of softmax-based models is fundamentally limited by the rank of their hidden representations. Godey et al. (2024) extend this to modern LLMs, demonstrating that the contextual probability distribution of natural language is inherently high-rank. Complementary work shows that when embeddings collapse into a narrow cone during training, generation quality degrades ( Gao et al., 2019 ) . Together, these results establish a link between representational dimensionality and generation quality. Empirical work supports this connection. Garrido et al. (2023) demonstrates that the effective rank of learned representations predicts downstream performance without labels. In language models specifically, hidden states encode rich semantic structure: word embeddings capture syntactic and semantic regularities through geometric relationships ( Mikolov et al., 2013 ) , and intermediate representations encode factuality ( He et al., 2024c ) and hallucination risk ( Chen et al., 2024 ) , confirming that generation quality leaves detectable geometric signatures.

Our work builds on these findings but shifts from diagnosis to optimization. Rather than using rank to analyze pretrained models post-hoc, we employ stable rank as a live reward signal during policy optimization, transforming a geometric insight into a practical alignment method.

## 8 Conclusion

This work demonstrates that stable rank, a simple intrinsic geometric property of LLM hidden states, provides an effective signal for text quality assessment and model alignment. As a zero-shot reward proxy, stable rank achieves 84.04% accuracy on RewardBench and improves Best-of-N sampling by 11.3 percentage points on average across reasoning benchmarks. Building on these insights, we introduce SR-GRPO, which uses stable rank as a novel reward signal for reinforcement learning without external supervision. SR-GRPO improves Qwen2.5-1.5B-Instruct by 10% on STEM tasks and 19% on mathematical reasoning, outperforming both learned reward models and self-evaluation baselines. Moreover, our analysis reveals that stable rank captures semantic coherence, information density, and sensitivity to key reasoning structures. Collectively, these results suggest that internal representation geometry provides sufficient signal for effective LLM alignment, offering a scalable alternative to annotation-dependent approaches.

## References

Abdin et al. (2024) M. I. Abdin, S. A. Jacobs, A. A. Awan, J. Aneja, A. Awadallah, H. Awadalla, N. Bach, A. Bahree, A. Bakhtiari, H. S. Behl, A. Benhaim, M. Bilenko, J. Bjorck, S. Bubeck, M. Cai, C. C. T. Mendes, W. Chen, V. Chaudhary, P. Chopra, A. D. Giorno, G. de Rosa, M. Dixon, R. Eldan, D. Iter, A. Garg, A. Goswami, S. Gunasekar, E. Haider, J. Hao, R. J. Hewett, J. Huynh, M. Javaheripi, X. Jin, P. Kauffmann, N. Karampatziakis, D. Kim, M. Khademi, L. Kurilenko, J. R. Lee, Y. T. Lee, Y. Li, C. Liang, W. Liu, E. Lin, Z. Lin, P. Madan, A. Mitra, H. Modi, A. Nguyen, B. Norick, B. Patra, D. Perez-Becker, T. Portet, R. Pryzant, H. Qin, M. Radmilac, C. Rosset, S. Roy, O. Ruwase, O. Saarikivi, A. Saied, A. Salim, M. Santacroce, S. Shah, N. Shang, H. Sharma, X. Song, M. Tanaka, X. Wang, R. Ward, G. Wang, P. A. Witte, M. Wyatt, C. Xu, J. Xu, S. Yadav, F. Yang, Z. Yang, D. Yu, C. Zhang, C. Zhang, J. Zhang, L. L. Zhang, Y. Zhang, Y. Zhang, Y. Zhang, and X. Zhou Phi-3 technical report: A highly capable language model locally on your phone . CoRR abs/2404.14219 . External Links: Document , 2404.14219 Cited by: Appendix A , §2.2 , §2.3 .

Allal et al. (2025) L. B. Allal, A. Lozhkov, E. Bakouch, G. M. Blázquez, G. Penedo, L. Tunstall, A. Marafioti, H. Kydlícek, A. P. Lajarín, V. Srivastav, et al. SmolLM2: when smol goes big-data-centric training of a small language model . CoRR . Cited by: Appendix E , §4.1 .

Bai et al. (2022) Y. Bai, A. Jones, K. Ndousse, A. Askell, A. Chen, N. DasSarma, D. Drain, S. Fort, D. Ganguli, T. Henighan, N. Joseph, S. Kadavath, J. Kernion, T. Conerly, S. E. Showk, N. Elhage, Z. Hatfield-Dodds, D. Hernandez, T. Hume, S. Johnston, S. Kravec, L. Lovitt, N. Nanda, C. Olsson, D. Amodei, T. B. Brown, J. Clark, S. McCandlish, C. Olah, B. Mann, and J. Kaplan Training a helpful and harmless assistant with reinforcement learning from human feedback . CoRR abs/2204.05862 . External Links: 2204.05862 Cited by: §1 , §7.1 .

Casper et al. (2023) S. Casper, X. Davies, C. Shi, T. K. Gilbert, J. Scheurer, J. Rando, R. Freedman, T. Korbak, D. Lindner, P. Freire, T. T. Wang, S. Marks, C. Segerie, M. Carroll, A. Peng, P. J.K. Christoffersen, M. Damani, S. Slocum, U. Anwar, A. Siththaranjan, M. Nadeau, E. J. Michaud, J. Pfau, D. Krasheninnikov, X. Chen, L. Langosco, P. Hase, E. Biyik, A. Dragan, D. Krueger, D. Sadigh, and D. Hadfield-Menell Open problems and fundamental limitations of reinforcement learning from human feedback . Transactions on Machine Learning Research . External Links: ISSN 2835-8856 Cited by: §1 , §7.1 .

Chakraborty et al. (2024) S. Chakraborty, J. Qiu, H. Yuan, A. Koppel, D. Manocha, F. Huang, A. Bedi, and M. Wang MaxMin-RLHF: alignment with diverse human preferences . In Proceedings of the 41st International Conference on Machine Learning , Proceedings of Machine Learning Research , Vol. 235 , pp. 6116–6135 . Cited by: §1 , §7.1 .

Chen et al. (2024) C. Chen, K. Liu, Z. Chen, Y. Gu, Y. Wu, M. Tao, Z. Fu, and J. Ye INSIDE: LLMs’ internal states retain the power of hallucination detection . In The Twelfth International Conference on Learning Representations , Cited by: §1 , §7.2 , §7.3 .

Cui et al. (2017) B. Cui, Y. Li, Y. Zhang, and Z. Zhang Text coherence analysis based on deep neural network . In Proceedings of the 2017 ACM on Conference on Information and Knowledge Management , CIKM ’17 , New York, NY, USA , pp. 2027–2030 . External Links: ISBN 9781450349185 , Document Cited by: §5.4 .

DeepSeek-AI (2025) DeepSeek-AI DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning . CoRR abs/2501.12948 . External Links: Document , 2501.12948 Cited by: §1 , §1 , §2.3 , §4.1 , §7.2 .

Dubey et al. (2024) A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Yang, A. Fan, A. Goyal, A. Hartshorn, A. Yang, A. Mitra, A. Sravankumar, A. Korenev, A. Hinsvark, A. Rao, A. Zhang, A. Rodriguez, A. Gregerson, A. Spataru, B. Rozière, B. Biron, B. Tang, B. Chern, C. Caucheteux, C. Nayak, C. Bi, C. Marra, C. McConnell, C. Keller, C. Touret, C. Wu, C. Wong, C. C. Ferrer, C. Nikolaidis, D. Allonsius, D. Song, D. Pintz, D. Livshits, D. Esiobu, D. Choudhary, D. Mahajan, D. Garcia-Olano, D. Perino, D. Hupkes, E. Lakomkin, E. AlBadawy, E. Lobanova, E. Dinan, E. M. Smith, F. Radenovic, F. Zhang, G. Synnaeve, G. Lee, G. L. Anderson, G. Nail, G. Mialon, G. Pang, G. Cucurell, H. Nguyen, H. Korevaar, H. Xu, H. Touvron, I. Zarov, I. A. Ibarra, I. M. Kloumann, I. Misra, I. Evtimov, J. Copet, J. Lee, J. Geffert, J. Vranes, J. Park, J. Mahadeokar, J. Shah, J. van der Linde, J. Billock, J. Hong, J. Lee, J. Fu, J. Chi, J. Huang, J. Liu, J. Wang, J. Yu, J. Bitton, J. Spisak, J. Park, J. Rocca, J. Johnstun, J. Saxe, J. Jia, K. V. Alwala, K. Upasani, K. Plawiak, K. Li, K. Heafield, K. Stone, and et al. The llama 3 herd of models . CoRR abs/2407.21783 . Cited by: §2.2 , §2.3 , §7.1 .

Ethayarajh et al. (2024) K. Ethayarajh, W. Xu, N. Muennighoff, D. Jurafsky, and D. Kiela Model alignment as prospect theoretic optimization . In Proceedings of the 41st International Conference on Machine Learning , ICML’24 . Cited by: §7.1 .

Gao et al. (2019) J. Gao, D. He, X. Tan, T. Qin, L. Wang, and T. Liu Representation degeneration problem in training natural language generation models . In International Conference on Learning Representations , Cited by: §1 , §2.1 , §7.3 .

Garg et al. (2025) S. Garg, A. Singh, S. Singh, and P. Chopra IPO: your language model is secretly a preference classifier . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, Vienna, Austria, July 27 - August 1, 2025 , pp. 19425–19441 . Cited by: §B.2 , §1 , §2.2 , 3rd item , §7.2 .

Garrido et al. (2023) Q. Garrido, R. Balestriero, L. Najman, and Y. LeCun RankMe: assessing the downstream performance of pretrained self-supervised representations by their rank . In Proceedings of the 40th International Conference on Machine Learning , ICML’23 . Cited by: §7.3 .

Gema et al. (2025) A. P. Gema, J. O. J. Leang, G. Hong, A. Devoto, A. C. M. Mancino, R. Saxena, X. He, Y. Zhao, X. Du, M. R. Ghasemi Madani, C. Barale, R. McHardy, J. Harris, J. Kaddour, E. Van Krieken, and P. Minervini Are we done with MMLU? . In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) , pp. 5069–5096 . External Links: Document , ISBN 979-8-89176-189-6 Cited by: §2.3 , §4.1 .

Godey et al. (2024) N. Godey, É. V. de la Clergerie, and B. Sagot Why do small language models underperform? studying language model saturation via the softmax bottleneck . In First Conference on Language Modeling , Cited by: §1 , §2.1 , §7.3 .

He et al. (2024a) C. He, R. Luo, Y. Bai, S. Hu, Z. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, J. Liu, L. Qi, Z. Liu, and M. Sun OlympiadBench: a challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 3828–3850 . External Links: Document Cited by: §2.3 .

He et al. (2024b) C. He, R. Luo, Y. Bai, S. Hu, Z. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, J. Liu, L. Qi, Z. Liu, and M. Sun OlympiadBench: a challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 3828–3850 . External Links: Document Cited by: §4.1 .

He et al. (2024c) J. He, Y. Gong, Z. Lin, C. Wei, Y. Zhao, and K. Chen LLM factoscope: uncovering LLMs’ factual discernment through measuring inner states . In Findings of the Association for Computational Linguistics: ACL 2024 , pp. 10218–10230 . Cited by: §1 , §7.2 , §7.3 .

Hu et al. (2022) E. J. Hu, yelong shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen LoRA: low-rank adaptation of large language models . In International Conference on Learning Representations , Cited by: §4.1 .

Kim et al. (2024) S. Kim, J. Suk, S. Longpre, B. Y. Lin, J. Shin, S. Welleck, G. Neubig, M. Lee, K. Lee, and M. Seo Prometheus 2: an open source language model specialized in evaluating other language models . In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing , pp. 4334–4353 . External Links: Document Cited by: §B.1 , §2.2 .

knoveleng (2023) knoveleng AMC-23 . Note: Hugging Face Dataset External Links: Link Cited by: §2.3 , §4.1 .

Lambert et al. (2024) N. Lambert, J. Morrison, V. Pyatkin, S. Huang, H. Ivison, F. Brahman, L. J. V. Miranda, A. Liu, N. Dziri, S. Lyu, Y. Gu, S. Malik, V. Graf, J. D. Hwang, J. Yang, R. L. Bras, O. Tafjord, C. Wilhelm, L. Soldaini, N. A. Smith, Y. Wang, P. Dasigi, and H. Hajishirzi TÜlu 3: pushing frontiers in open language model post-training . CoRR abs/2411.15124 . External Links: Document , 2411.15124 Cited by: §1 , §7.2 .

Lambert et al. (2025) N. Lambert, V. Pyatkin, J. Morrison, L. J. V. Miranda, B. Y. Lin, K. R. Chandu, N. Dziri, S. Kumar, T. Zick, Y. Choi, N. A. Smith, and H. Hajishirzi RewardBench: evaluating reward models for language modeling . In Findings of the Association for Computational Linguistics: NAACL 2025, Albuquerque, New Mexico, USA, April 29 - May 4, 2025 , pp. 1755–1797 . Cited by: Appendix A , Appendix F , Figure 1 , Figure 1 , §1 , §2.2 .

Lee et al. (2024) H. Lee, S. Phatale, H. Mansoor, T. Mesnard, J. Ferret, K. Lu, C. Bishop, E. Hall, V. Carbune, A. Rastogi, and S. Prakash RLAIF vs. RLHF: scaling reinforcement learning from human feedback with AI feedback . In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024 , Cited by: §1 , §7.2 .

Lightman et al. (2023) H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe Let’s verify step by step . arXiv preprint arXiv:2305.20050 . Cited by: §2.3 , §4.1 .

Lin et al. (2025) B. Y. Lin, Y. Deng, K. Chandu, A. Ravichander, V. Pyatkin, N. Dziri, R. L. Bras, and Y. Choi WildBench: benchmarking LLMs with challenging tasks from real users in the wild . In The Thirteenth International Conference on Learning Representations , Cited by: §4.1 .

Liu et al. (2025) C. Y. Liu, L. Zeng, Y. Xiao, J. He, J. Liu, C. Wang, R. Yan, W. Shen, F. Zhang, J. Xu, Y. Liu, and Y. Zhou Skywork-reward-v2: scaling preference data curation via human-ai synergy . arXiv preprint arXiv:2507.01352 . Cited by: §4.1 .

Mesgar and Strube (2018) M. Mesgar and M. Strube A neural local coherence model for text quality assessment . In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing , Brussels, Belgium , pp. 4328–4339 . External Links: Document Cited by: §5.4 .

Mikolov et al. (2013) T. Mikolov, W. Yih, and G. Zweig Linguistic regularities in continuous space word representations . In Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies , Atlanta, Georgia , pp. 746–751 . Cited by: §7.3 .

OpenAI (2025) OpenAI GPT-4o mini: a more efficient multimodal model . External Links: Link Cited by: §4.1 .

Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. F. Christiano, J. Leike, and R. Lowe Training language models to follow instructions with human feedback . In Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022 , Cited by: §1 , §7.1 .

Rafailov et al. (2023) R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn Direct preference optimization: your language model is secretly a reward model . In Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023 , Cited by: §1 , §7.1 .

Reimers and Gurevych (2019) N. Reimers and I. Gurevych Sentence-bert: sentence embeddings using siamese bert-networks . In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing , Cited by: §F.2 , §F.3 .

Rein et al. (2024) D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman GPQA: a graduate-level google-proof q&a benchmark . In First Conference on Language Modeling , Cited by: §2.3 , §4.1 .

Roy and Vetterli (2007) O. Roy and M. Vetterli The effective rank: a measure of effective dimensionality . In 2007 15th European signal processing conference , pp. 606–610 . Cited by: 2nd item , §6 .

Rudelson and Vershynin (2007) M. Rudelson and R. Vershynin Sampling from large matrices: an approach through geometric functional analysis . J. ACM 54 ( 4 ), pp. 21–es . External Links: ISSN 0004-5411 , Document Cited by: §1 , §2 .

Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. K. Li, Y. Wu, and D. Guo DeepSeekMath: pushing the limits of mathematical reasoning in open language models . CoRR abs/2402.03300 . External Links: Document , 2402.03300 Cited by: §3.2 .

Singhal et al. (2024) P. Singhal, T. Goyal, J. Xu, and G. Durrett A long way to go: investigating length correlations in RLHF . In First Conference on Language Modeling , Cited by: §5.4 .

Skalse et al. (2022) J. Skalse, N. H. R. Howe, D. Krasheninnikov, and D. Krueger Defining and characterizing reward hacking . In Proceedings of the 36th International Conference on Neural Information Processing Systems , NIPS ’22 . External Links: ISBN 9781713871088 Cited by: §7.1 .

Wang et al. (2023) J. Wang, H. Wang, S. Sun, and W. Li Aligning language models with human preferences via a bayesian approach . In Proceedings of the 37th International Conference on Neural Information Processing Systems , NIPS ’23 . Cited by: §1 , §7.1 .

Wang et al. (2024) P. Wang, L. Li, L. Chen, Z. Cai, D. Zhu, B. Lin, Y. Cao, L. Kong, Q. Liu, T. Liu, and Z. Sui Large language models are not fair evaluators . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024 , pp. 9440–9450 . External Links: Document Cited by: §1 .

Wu et al. (2023) Z. Wu, Y. Hu, W. Shi, N. Dziri, A. Suhr, P. Ammanabrolu, N. A. Smith, M. Ostendorf, and H. Hajishirzi Fine-grained human feedback gives better rewards for language model training . In Proceedings of the 37th International Conference on Neural Information Processing Systems , NIPS ’23 . Cited by: §1 .

Yang et al. (2025) A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, C. Zheng, D. Liu, F. Zhou, F. Huang, F. Hu, H. Ge, H. Wei, H. Lin, J. Tang, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Lin, K. Dang, K. Bao, K. Yang, L. Yu, L. Deng, M. Li, M. Xue, M. Li, P. Zhang, P. Wang, Q. Zhu, R. Men, R. Gao, S. Liu, S. Luo, T. Li, T. Tang, W. Yin, X. Ren, X. Wang, X. Zhang, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Zhang, Y. Wan, Y. Liu, Z. Wang, Z. Cui, Z. Zhang, Z. Zhou, and Z. Qiu Qwen3 technical report . CoRR abs/2505.09388 . External Links: Document Cited by: Appendix A , Appendix G , Appendix H , Figure 1 , Figure 1 , §1 , §2.2 .

Yang et al. (2024) A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, H. Wei, H. Lin, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Lin, K. Dang, K. Lu, K. Bao, K. Yang, L. Yu, M. Li, M. Xue, P. Zhang, Q. Zhu, R. Men, R. Lin, T. Li, T. Xia, X. Ren, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Wan, Y. Liu, Z. Cui, Z. Zhang, and Z. Qiu Qwen2.5 technical report . CoRR abs/2412.15115 . External Links: Document , 2412.15115 Cited by: Appendix A , §1 , §2.2 , §2.3 , §4.1 .

Yang et al. (2018) Z. Yang, Z. Dai, R. Salakhutdinov, and W. W. Cohen Breaking the softmax bottleneck: a high-rank RNN language model . In International Conference on Learning Representations , Cited by: §1 , §2.1 , §7.3 .

Yin et al. (2025) Z. Yin, Q. Sun, Z. Zeng, Q. Cheng, X. Qiu, and X. Huang Dynamic and generalizable process reward modeling . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , Vienna, Austria , pp. 4203–4233 . External Links: Document , ISBN 979-8-89176-251-0 Cited by: §7.1 .

Yuan et al. (2024) W. Yuan, R. Y. Pang, K. Cho, X. Li, S. Sukhbaatar, J. Xu, and J. Weston Self-rewarding language models . In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024 , Cited by: §1 , 1st item , §7.2 .

Zhang et al. (2025a) Q. Zhang, L. Qiu, I. Hong, Z. Xu, T. Liu, S. Li, R. Zhang, Z. Li, L. Li, B. Yin, C. Zhang, J. Chen, H. Jiang, and T. Zhao Self-rewarding PPO: aligning large language models with demonstrations only . In Second Conference on Language Modeling , Cited by: §7.2 .

Zhang and Math-AI (2025) Y. Zhang and T. Math-AI American invitational mathematics examination (aime) 2025 . Cited by: §4.1 .

Zhang et al. (2025b) Z. Zhang, C. Zheng, Y. Wu, B. Zhang, R. Lin, B. Yu, D. Liu, J. Zhou, and J. Lin The lessons of developing process reward models in mathematical reasoning . In Findings of the Association for Computational Linguistics: ACL 2025 , pp. 10495–10516 . External Links: Document , ISBN 979-8-89176-256-5 Cited by: §7.1 .

Zheng et al. (2023) L. Zheng, W. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, and I. Stoica Judging llm-as-a-judge with mt-bench and chatbot arena . In Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023 , Cited by: §1 .

## Appendix A Cross-Layer Stable Rank Analysis

We analyze how stable rank performance varies across transformer layers by computing R SR ( l ) ​ ( y ) = ‖ 𝐇 l ‖ F 2 / ‖ 𝐇 l ‖ 2 2 R_{\text{SR}}^{(l)}(y)=\|\mathbf{H}_{l}\|_{F}^{2}/\|\mathbf{H}_{l}\|_{2}^{2} at each layer l l and evaluating it as a reward proxy on RewardBench ( Lambert et al., 2025 ) . We test three model families: Qwen3-8B (36 layers) ( Yang et al., 2025 ) , Qwen2.5-1.5B-Instruct (28 layers) ( Yang et al., 2024 ) , and Phi-3.5-mini-instruct (32 layers) ( Abdin et al., 2024 ) , measuring accuracy on five subcategories: Chat, Chat Hard, Safety, Code, and Math.

##### Final layers encode quality signals most effectively.

Figure 3 shows that stable rank performance varies dramatically across layers. Early and middle layers (indices 5-25) achieve near-random performance ( ∼ \sim 50% accuracy) across all categories, indicating that stable rank computed from these layers carries minimal quality information. In contrast, final layers (indices 28-32 depending on the model) exhibit sharp performance improvements, with accuracy rising to 70-85% on most categories. This pattern holds consistently across all three model families, suggesting that semantic abstraction in deeper layers is crucial for stable rank to capture response quality.

##### Task-dependent layer sensitivity.

While final layers universally outperform earlier layers, we observe task-specific patterns. On Chat and Chat Hard categories, performance plateaus across middle layers before rising sharply at the end, suggesting that conversational quality signals emerge primarily in final layers. For Safety, we observe an interesting U-shape on Qwen3-8B and Phi-3.5-mini, with both very early (layer 0-2) and final layers achieving reasonable performance. This may indicate that safety-related features are encoded at multiple levels of abstraction. Math and Code categories show the most dramatic improvements in final layers, with Qwen2.5-1.5B achieving near-perfect accuracy (95-98%) on Math using layer 27, highlighting that complex reasoning quality is best captured by the deepest semantic representations.

##### Implications for SR-GRPO.

These findings strongly support our design choice in SR-GRPO to extract stable rank from the final transformer layer. The consistent performance advantage of final-layer stable rank (70-85% accuracy) over middle layers (45-50% accuracy) demonstrates that quality-indicative geometric structure emerges primarily in deep semantic representations. This validates that maximizing final-layer stable rank during RL optimization directly targets the representational regime where quality signals are most pronounced, enabling effective annotation-free alignment.

## Appendix B Baseline Implementation Details

In this section, we provide the prompts and implementation details for all the baselines.

### B.1 Generative Baselines

In our experiments, we have two generative baselines: (1) Pointwise Scoring ( Kim et al., 2024 ) and (2) Pairwise Comparison ( Kim et al., 2024 ) .

#### B.1.1 Pointwise Scoring Prompt

For the Pointwise Scoring baseline, we use the following prompt structure to score each response on a 1-5 scale:

We extract the numerical rating from the model’s output by parsing the [RESULT] token and compare scores to determine the preferred response. The reference answer and score rubrics are adapted from RewardBench’s provided materials.

#### B.1.2 Pairwise Comparison Prompt

For the Pairwise Comparison baseline, we prompt the model to directly compare two responses:

We parse the model’s output to extract the preference (A or B) from the [RESULT] token. To account for positional bias, we evaluate each pair twice with responses swapped and only count predictions where both orderings agree.

### B.2 IPO Implementation

We follow the evaluation protocol from IPO ( Garg et al., 2025 ) for RewardBench. IPO computes implicit preference scores by prompting the model with task-specific Yes/No verification questions and extracting token probabilities from the final logits.

#### B.2.1 Task-Specific Evaluation Prompts

We use category-specific verification prompts adapted from the IPO codebase. All prompts follow the format: [verification_prompt] User: { instruction } Response: { response }. We automatically assign categories based on subset names: Code tasks contain ”hep-” or ”code”, Math tasks contain ”math-” or ”prm”, Safety tasks contain ”refusals-”, ”xstest-”, or ”donotanswer”, and all others default to Chat. The prompt structure varies by task:

Code: ”Below is a coding-related question along with a response containing code. Your task is to verify whether the provided code is correct, functional, and aligned with the requirements of the question. Answer with just Yes/No”

Math: ”Below is a math question along with a response containing a solution. Your task is to verify whether the solution is correct, the reasoning is logical, and the final answer is accurate. Answer with just Yes/No”

Safety: ”Inspect the response to ensure it is safe and appropriate for the question below. Answer Yes/No.”

Chat (default): ”Below is a question, along with a response to that question. Your task is to verify whether the response is helpful, factually correct, logically sound, and contextually appropriate. Answer with just Yes/No”

#### B.2.2 Score Computation

Given response y y to instruction x x , we tokenize the verification prompt and perform a forward pass to obtain logits ℓ ∈ ℝ | V | \boldsymbol{\ell}\in\mathbb{R}^{|V|} at the final position. We extract logits for ”Yes” and ”No” tokens (including variants with leading spaces), apply softmax normalization, and define the IPO score as: IPO ​ ( y | x ) = exp ⁡ ( ℓ Yes ) exp ⁡ ( ℓ Yes ) + exp ⁡ ( ℓ No ) \text{IPO}(y|x)=\frac{\exp(\ell_{\text{Yes}})}{\exp(\ell_{\text{Yes}})+\exp(\ell_{\text{No}})} (3)

The response with higher IPO ​ ( y | x ) \text{IPO}(y|x) is predicted as preferred. This approach differs from standard likelihood-based methods by explicitly prompting for binary quality judgments rather than computing sequence log-probabilities.

## Appendix C RewardBench Results

We show the complete performance comparison across different reward methods for RewardBench in Table 5 .

## Appendix D Best-of-N Complete Results

We provide complete Best-of-N decoding results comparing stable rank selection against random selection across four models and five benchmarks. For each configuration, we sample N candidate responses and either select randomly (Random@N) or choose the response with highest stable rank (Best@N). We report two relative metrics: Δ \Delta Rand. measures improvement over random selection at the same N, and Δ \Delta @1 measures improvement over greedy decoding (N=1).

Table 6 shows that stable rank selection consistently outperforms random selection across all models and sampling budgets. The advantage is most pronounced on smaller models: Llama-3.2-1B achieves +33.8% relative improvement over random selection at N=16, while random selection actually degrades performance below greedy decoding ( − - 9.9%). This degradation occurs because random selection may choose low-quality samples from the candidate pool, whereas stable rank reliably identifies better responses.

Notably, the gains from stable rank selection increase with N for most models, suggesting that larger candidate pools provide more opportunities for quality differentiation. On math-heavy benchmarks (MATH500, OlympiadBench), stable rank selection yields particularly strong improvements, with DeepSeek-R1 improving from 82.8% to 86.8% on MATH500 and from 43.6% to 59.7% on OlympiadBench at N=16.

## Appendix E SR-GRPO Training Details

We provide the training configurations for SR-GRPO experiments on both models. All experiments are conducted on 4 × \times NVIDIA H800 GPUs.

##### Qwen2.5-1.5B-Instruct.

We train for 400 steps using LoRA with rank r r =16 and α \alpha =32, targeting all attention and MLP projection layers. We use a learning rate of 10 − 6 10^{-6} with cosine scheduling and 10% warmup. Training uses per-device batch size of 4 with gradient accumulation steps of 8 (effective batch size 128), mixed precision (bfloat16), and gradient checkpointing for memory efficiency. The maximum prompt and completion lengths are both set to 4096 tokens.

##### DeepSeek-R1-Distill-Qwen-1.5B.

We train for 300 steps using the same LoRA configuration ( r r =16, α \alpha =32). Due to the model’s longer reasoning traces, we use per-device batch size of 2 with gradient accumulation steps of 16 (effective batch size 128). The maximum prompt length is set to 8192 and maximum completion length to 4096 tokens. All other hyperparameters remain identical to the Qwen configuration.

##### Stable Rank Computation.

For reward calculation, we format the prompt and completion using the model’s chat template. We then compute hidden states from the last transformer layer using the reference model. To prevent reward hacking, we temporarily disable LoRA adapters during stable rank computation, ensuring rewards are derived from the frozen base model’s representations rather than the adapting policy. Hidden states are extracted only for non-padding tokens, and stable rank is computed using the method described in Section 2 .

##### Common Settings.

Both models are trained on the SmolTalk2 ( Allal et al., 2025 ) preference dataset using paged AdamW optimizer with 8-bit quantization. We set weight decay to 0, maximum gradient norm to 1.0, and LoRA dropout to 0.1. Rewards are not normalized across batches. For GRPO-specific hyperparameters, we use the default values from the HuggingFace TRL library: group size K = 8 K=8 , KL penalty coefficient β = 0.04 \beta=0.04 , and numerical stability constant ϵ = 10 − 8 \epsilon=10^{-8} for advantage standardization.

## Appendix F Experimental Details for Metric Analysis

We analyze the relationship between stable rank and text quality using the RewardBench dataset ( Lambert et al., 2025 ) , which contains 2,985 prompts, each with one chosen and one rejected response ( N = 5,970 N=5{,}970 responses). This appendix describes our statistical methodology, defines all metrics, and reports the complete correlation results.

### F.1 Statistical Methodology

We employ two complementary analyses to characterize the relationship between stable rank and text metrics:

##### Sample-level correlation.

We treat each of the N = 5,970 N=5{,}970 responses as an independent observation. For metric M M and stable rank S S , we compute Pearson correlation r = corr ⁡ ( M , S ) r=\mathrm{corr}(M,S) and Spearman rank correlation ρ \rho . This measures whether higher stable rank globally associates with higher (or lower) metric values. We apply this method to semantic coherence, information density, and basic structural metrics.

##### Paired-difference analysis.

Linguistic markers (discourse and logical connectives) exhibit strong context dependence: some prompts naturally require more explanation markers than others, making absolute counts across different prompts statistically noisy. To control for this variation, we work at the pair level. For each prompt i i with chosen response y c y_{c} and rejected response y r y_{r} , we compute differences Δ ​ M i = M ⁡ ( y c ) − M ⁡ ( y r ) , Δ ​ S i = S ⁡ ( y c ) − S ⁡ ( y r ) , \Delta M_{i}=M(y_{c})-M(y_{r}),\quad\Delta S_{i}=S(y_{c})-S(y_{r}), (4)

and correlate Δ ​ M \Delta M with Δ ​ S \Delta S across all N = 2,985 N=2{,}985 pairs. This measures whether, within the same context, the response with higher stable rank tends to use more (positive correlation) or fewer (negative correlation) of a given linguistic feature.

### F.2 Metric Definitions

We measure text quality along three axes: semantic coherence, information density, and linguistic structure. Tables 8 – 10 define the metrics formally. For response y y , let T T denote its token sequence ( N tokens N_{\text{tokens}} tokens), s 1 , … , s n s_{1},\dots,s_{n} its sentences with embeddings v 1 , … , v n v_{1},\dots,v_{n} (from all-MiniLM-L6-v2 ( Reimers and Gurevych, 2019 ) ), and v p v_{p} the prompt embedding.

### F.3 Implementation Details

##### Sentence embeddings.

We use the all-MiniLM-L6-v2 ( Reimers and Gurevych, 2019 ) model from the sentence-transformers library, which produces 384-dimensional embeddings. The model applies mean pooling over token embeddings and L2-normalization.

##### Sentence tokenization.

We tokenize responses into sentences using NLTK 1 1 1 https://www.nltk.org/ , with a regex-based fallback (splitting on sentence boundaries while handling common abbreviations). Each response contains n n sentences indexed 1 , … , n 1,\dots,n .

##### Syllable counting.

For readability metrics, we count syllables using the pyphen 2 2 2 https://pyphen.org/ library (dictionary-based hyphenation for English). Complex words are defined as having ≥ 3 \geq 3 syllables following standard practice.

##### Marker detection.

Logical and discourse markers are detected via case-insensitive substring matching. For each marker category, we report: (1) raw count, (2) count normalized per sentence, and (3) count normalized per 100 tokens as ( c / N tokens ) × 100 (c/N_{\text{tokens}})\times 100 .

### F.4 Correlation Results

Tables 11 and 12 report Pearson ( r r ) and Spearman ( ρ \rho ) correlations with p p -values. Positive correlations indicate that higher metric values associate with higher stable rank; negative correlations indicate the opposite.

### F.5 Key Findings

The correlation analysis reveals three main patterns. First, stable rank shows strongest positive associations with semantic coherence metrics: progression score ( ρ = 0.313 \rho=0.313 ) and QA alignment consistency ( ρ = 0.316 \rho=0.316 ). Responses maintaining smooth topic flow and stable prompt alignment achieve higher stable rank. Conversely, coherence standard deviation exhibits strong negative correlation ( ρ = − 0.356 \rho=-0.356 ), indicating that inconsistent adjacent similarities reduce stable rank.

Second, stable rank distinguishes information density from verbosity. While absolute measures like token count ( ρ = − 0.294 \rho=-0.294 ) and sentence count ( ρ = − 0.368 \rho=-0.368 ) correlate negatively, efficiency metrics show positive associations: lexical diversity ( ρ = 0.238 \rho=0.238 ) and compression ratio ( ρ = 0.233 \rho=0.233 ). The negative correlation with sentence count is particularly revealing: responses with many short sentences fail to build rich semantic representations. Combined with positive correlation with average sentence length ( ρ = 0.085 \rho=0.085 ), this suggests stable rank rewards well-developed sentences over fragmented text.

Third, discourse markers reveal nuanced reasoning patterns in paired-difference analysis. Most marker categories show negative correlations: additive markers ( ρ = − 0.156 \rho=-0.156 ), conditional markers ( ρ = − 0.163 \rho=-0.163 ), and enumeration patterns ( ρ = − 0.148 \rho=-0.148 ), with total marker count negatively associated ( ρ = − 0.204 \rho=-0.204 ). Responses relying heavily on common connective words tend to receive lower stable rank, consistent with favoring compact information content over explicit signaling. However, contrastive and causal markers follow a different pattern: positive Pearson correlations (contrastive r = 0.187 r=0.187 , causal r = 0.139 r=0.139 ) but weak Spearman correlations (contrastive ρ = 0.067 \rho=0.067 , causal ρ ≈ 0 \rho\approx 0 ). These markers often appear at branch points in arguments or when cause-effect relations are introduced, corresponding to deeper reasoning structure than simple additive or enumerative markers. The weak Spearman correlations indicate that stable rank is sensitive to whether such markers are present but does not increase monotonically with frequency, consistent with the view that contrastive and causal connectives are most informative when they highlight key reasoning steps rather than being used uniformly as a stylistic choice.

## Appendix G Ablation: Comparison with Other Intrinsic Dimension Metrics

While stable rank has shown strong performance as a reward signal, other intrinsic dimension metrics exist that measure the effective dimensionality of neural representations. We compare stable rank against three alternative metrics: condition number, PCA-based 95% variance dimension, and effective rank. All metrics are computed on the final hidden layer of Qwen3-8B ( Yang et al., 2025 ) using the same RewardBench evaluation protocol.

##### Metrics.

We evaluate four intrinsic dimension metrics: • Stable rank : sr ​ ( 𝐗 ) = ‖ 𝐗 ‖ F 2 / ‖ 𝐗 ‖ 2 2 \text{sr}(\mathbf{X})=\|\mathbf{X}\|_{F}^{2}/\|\mathbf{X}\|_{2}^{2} , the ratio of squared Frobenius norm to squared spectral norm.

• Effective rank ( Roy and Vetterli, 2007 ) : er ​ ( 𝐗 ) = exp ⁡ ( H ​ ( σ ~ ) ) \text{er}(\mathbf{X})=\exp(H(\tilde{\sigma})) , where H ⁡ ( σ ~ ) H(\tilde{\sigma}) is the Shannon entropy of the normalized singular value distribution σ ~ i = σ i / ∑ j σ j \tilde{\sigma}_{i}=\sigma_{i}/\sum_{j}\sigma_{j} .

• Condition number : κ ⁡ ( 𝐗 ) = σ max / σ min \kappa(\mathbf{X})=\sigma_{\max}/\sigma_{\min} , the ratio of largest to smallest singular value. We use 1 / κ 1/\kappa as the score so that higher values indicate better quality.

• PCA 95% variance : The number of principal components needed to capture 95% of the variance in the hidden states.

##### Results.

Table 13 shows that stable rank outperforms all alternative metrics across every category, achieving 84.04% overall accuracy compared to 61.91% for PCA 95% variance, 54.50% for effective rank, and 36.04% for condition number. The gap is largest on challenging categories: stable rank reaches 84.34% on Math while effective rank and condition number fall below 13%, and 76.20% on Safety while alternatives remain below 46%.

Among baseline metrics, PCA 95% variance performs best overall but struggles on Math (27.96%) and Safety (45.45%). Effective rank shows moderate Code performance (76.12%) but fails on Math (12.75%). Condition number performs poorly across all categories, suggesting that extreme singular value ratios are unreliable quality indicators.

##### Analysis.

Stable rank outperforms alternatives due to two key properties. First, it aggregates information across the entire singular value spectrum through the Frobenius norm, making it robust to outliers that affect condition number. Second, it balances representational richness (Frobenius norm) with coherence (spectral norm): high-quality responses activate diverse semantic dimensions in a structured manner, while low-quality responses either collapse into low-dimensional representations or exhibit erratic noise. The entropy weighting in effective rank and discrete counting in PCA 95% variance appear less suited for capturing these quality distinctions.

## Appendix H Ablation: Context Window Size

We investigate how context window size affects stable rank performance on RewardBench. For each prompt-response pair, we truncate the combined sequence to a maximum length in { 128,512 , 1024 , 2048 , 4096 } \{128,512,1024,2048,4096\} tokens before computing stable rank on the final layer of Qwen3-8B ( Yang et al., 2025 ) . RewardBench examples have a mean length of 281 tokens, with 75% under 512 tokens.

##### Results.

Table 14 shows that stable rank accuracy degrades at short context lengths but saturates quickly. At 128 tokens, overall accuracy drops to 62.59%, a 21 percentage point decrease from 512 tokens (83.85%). Code suffers most severely, falling from 87.91% to 24.80%, because truncation removes critical program logic. However, extending beyond 512 tokens yields minimal gains: increasing to 4096 tokens improves accuracy by only 0.2 percentage points.

##### Analysis.

The rapid saturation indicates that stable rank captures semantic content rather than mechanically rewarding longer sequences. Short windows (128 tokens) harm performance by cutting off meaningful content, but once the window covers the core reasoning structure (around 512 tokens for this dataset), additional context provides diminishing returns. Safety performance remains constant at 76.20% for all lengths ≥ \geq 512, suggesting that refusal quality is determined early in the response.

##### Practical Recommendations.

A 512-token window provides an effective operating point for datasets with similar length distributions. For longer-form tasks, we recommend scaling the window to cover at least the 75th percentile of sequence lengths to avoid truncation artifacts.

## Appendix I Ablation: Input Prompt Format

We investigate whether input prompt format affects stable rank performance. Since stable rank is computed on hidden states, the concatenation structure could influence the resulting geometry. We test six formats ranging from minimal (no prefix) to structured (User/Assistant tags).

(1) {prompt}\n\n{response} (no prefix)

(2) {prompt}\n\nResponse:{response}

(3) {prompt}\n\nAssistant:{response}

(4) User:{prompt}\n\nAssistant:{response}

(5) Question:{prompt}\n\nAnswer:{response}

(6) {prompt}\n\nAnswer:{response}

##### Results.

Table 15 shows that stable rank is robust to format variation. Overall accuracy varies by at most 3 percentage points across formats for each model, and no single format consistently outperforms others. Category-level variations are larger (e.g., Safety on Phi-3.5-mini ranges from 52.82% to 62.63%) but show no systematic pattern across models, indicating that format effects are model-specific rather than fundamental to stable rank.

##### Practical Recommendations.

The robustness to prompt format simplifies deployment: practitioners can use simple formats without extensive tuning. We recommend using the model’s native chat template when available, or a minimal format like {prompt}\n\nAnswer:{response} otherwise.

## Appendix J Stable Rank Example Prompts

To complement the quantitative analysis in Section 5 , we provide examples illustrating how stable rank differentiates high-quality responses from two common failure modes: catastrophic repetition and redundant verbosity.

##### Catastrophic Repetition.

The Image Processing example in Table 16 shows a response that begins coherently but enters an infinite repetition loop (“Image > > Image > > …”), collapsing into a degenerate low-dimensional representation. This failure directly relates to coherence standard deviation, which has the strongest negative correlation with stable rank ( ρ = − 0.356 \rho=-0.356 ). Geometrically, repetition concentrates variance into a single direction, reducing the effective dimensionality that stable rank measures.

##### Redundant Verbosity.

The Math Problem example shows a response that correctly solves the problem but continues with unnecessary elaboration (“However…”, “Alternatively…”). While the content is not incorrect, it dilutes information density. This aligns with our finding that stable rank correlates negatively with token count ( ρ = − 0.294 \rho=-0.294 ) and total discourse markers ( ρ = − 0.204 \rho=-0.204 ), while correlating positively with compression ratio ( ρ = 0.233 \rho=0.233 ). The high stable rank response terminates precisely at the answer, maintaining focused information flow.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
