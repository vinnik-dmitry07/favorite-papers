##### Report GitHub Issue

Content selection saved. Describe the issue below:

# LLaDA2.0: Scaling Up Diffusion Language Models to 100B

###### Abstract

This paper presents LLaDA2.0 — a tuple of discrete diffusion large language models (dLLM) scaling up to 100B total parameters through systematic conversion from auto-regressive (AR) models — establishing a new paradigm for frontier-scale deployment. Instead of costly training from scratch, LLaDA2.0 upholds knowledge inheritance, progressive adaption and efficiency-aware design principle, and seamless converts a pre-trained AR model into dLLM with a novel 3-phase block-level WSD based training scheme: progressive increasing block-size in block diffusion (warm-up), large-scale full-sequence diffusion (stable) and reverting back to compact-size block diffusion (decay). Along with post-training alignment with SFT and DPO, we obtain LLaDA2.0-mini (16B) and LLaDA2.0-flash (100B), two instruction-tuned Mixture-of-Experts (MoE) variants optimized for practical deployment. By preserving the advantages of parallel decoding, these models deliver superior performance and efficiency at the frontier scale. Both models were open-sourced.

Huggingface: https://hf.co/collections/inclusionAI/llada-20

## 1 Introduction

Large Language Models have achieved remarkable success through the AR paradigm, modeling sequences via next-token prediction with strict left-to-right causal dependencies ( Hurst et al., 2024 , Grattafiori et al., 2024 , Yang et al., 2025 ) . This approach naturally aligns with the sequential structure of language and enables efficient training through next-token likelihood maximization. However, the very success of this paradigm creates fundamental limitations: the sequential generation process imposes severe inference bottlenecks, precluding parallelization, and increasing latency at scale, while the rigid causal structure can be suboptimal for tasks requiring bidirectional reasoning and holistic understanding.

Discrete Masked Diffusion Language Models (MDLM) have emerged as a compelling alternative to the prevailing AR paradigm. By reconstructing sequences from random masked inputs, these models inherently support parallel generation and leverage a full bidirectional context, offering a different architectural approach ( Gong et al., 2025 , Yu et al., 2025 ) . Although these conceptual advantages are clear, the field is still in an early developmental stage. Current research is actively focused on key challenges, including the refinement of specialized training regimes, the design of efficient sampling strategies, the efficient inference of opensource models, and reinforcement learning for MDLM. As a result of this ongoing exploration, most existing diffusion models, including recent advancements like Block Diffusion Language Models (BDLMs) ( Arriola et al., 2025 ) , operate at a smaller scale ( e.g. , ≤ \leq 8B parameters). Bridging this scale difference to the hundreds of billions of parameters seen in the leading mainstream AR models is a primary frontier for enabling diffusion models to fully capture complex linguistic patterns for practical deployment.

In this work, we introduce LLaDA2.0 series with 100B/16B total parameters diffusion language models that resolves these fundamental challenges through a novel two-stage continual pre-training (CPT) paradigm. Rather than attempting to train diffusion models from scratch, we leverage existing AR checkpoints as the foundation for a systematic conversion process that preserves linguistic knowledge while introducing diffusion capabilities.

The first stage, CPT aims to transform the foundational AR model into a capable diffusion language model. However, direct conversion is challenging due to the inherent data distribution gap between left-to-right generation and bidirectional denoising. Although the BDLM formulation partially reduces this gap through blockwise masked reconstruction, it suffers from low data utilization, limiting the effective exploitation of large-scale corpora. To this end, we introduce the Warmup–Stable–Decay (WSD) strategy, smoothly bridging the AR-to-dLLM gap while substantially improving CPT efficiency. WSD gradually expands the model’s receptive field to introduce diffusion-style context ( Warmup ), strengthens global denoising under full-sequence training ( Stable ), and then refines the model into an efficient blockwise structure ( Decay ). This progressive adjustment enables a stable and data-efficient transition to diffusion-based learning. Additionally, under full attention in packed training sequences, diffusion models risk forming spurious dependencies across document boundaries, leading to semantic confusion and instability in bidirectional training. To prevent such cross-document interference, we introduce a document-level attention mask that restricts self-attention within individual documents, ensuring coherent context modeling.

The second stage, Post-training for Practical Deployment, transitions the model from a raw predictive engine into a capable and efficient assistant. The random masking nature of the diffusion fine-tuning objective means any single sample provides only a partial learning signal. We address this by employing a complementary masking strategy, which ensures near-100% data utilization and accelerates convergence by guaranteeing every token contributes to the model’s learning. With an efficient foundation for instruction tuning, we then align the model with human preferences by adapting modern techniques like Direct Preference Optimization (DPO)—originally designed for AR models—by reformulating the objective over the model’s reconstruction loss. Beyond alignment, practical deployment hinges on inference speed. To realize the full promise of parallel decoding, which is often limited by a model’s lack of predictive confidence, we incorporate an auxiliary confidence prediction loss. This trains the model to be “sharper” and more certain, unlocking aggressive and efficient parallel generation without degrading quality.

We release instruction-tuned variants for practical deployment: LLaDA2.0-mini (16B parameters) for resource-constrained applications and LLaDA2.0-flash (100B parameters) for high-performance scenarios. Both variants retain the parallel decoding advantages of our diffusion training while being optimized for instruction following and safety through comprehensive post-training alignment.

Our contributions provide a practical recipe for the community to leverage AR stability while achieving diffusion parallelism, opening new possibilities for efficient large-scale language modeling.

## 2 Related Work

### 2.1 Train dLLMs from scratch

Auto-regressive language models ( Ling et al., 2025 , Moonshot, 2025 , Liu et al., 2024 , Meta-AI, 2025 ) are typically trained by maximizing the likelihood of predicting the next token. Under this paradigm, model performance has been shown to scale effectively with increasing model size, dataset volume, and computational resources, following well-established scaling laws. Recently, MDLMs ( Song et al., 2025 , Ye et al., 2025 , Nie et al., 2025 ) have emerged as an alternative generative framework, reformulating text generation as an iterative denoising process. In each forward step, a subset of tokens is randomly masked, and the model is trained to recover the original tokens conditioned on the remaining unmasked context.

Encouraged by this paradigm shift, several studies have explored training MDLMs from scratch to assess their full potential. For instance, LLaDA ( Nie et al., 2025 ) demonstrated that a 8B dense MDLM, trained entirely from scratch, achieves performance competitive with similarly sized AR counterparts. Building upon this, LLaDA-MoE ( Zhu et al., 2025 ) introduced the Mixture-of-Experts (MoE) architecture into the MDLM for the first time, showing that a scratch-trained MoE-based MDLM can surpass dense models in both efficiency and capability, thereby validating the compatibility and scalability of MDLMs with advanced MoE designs. Moreover, due to the fundamentally different training dynamics compared to AR models, established training practices and hyperparameter recipes from the AR domain are often suboptimal for MDLMs. To address this gap, recent efforts such as Quakka ( Ni et al., 2025 ) and OpenMoE2 ( Ni and team, 2025 ) have begun investigating the scaling properties and optimal training strategies specifically tailored for MDLMs, laying the groundwork for principled scaling in this emerging paradigm.

However, from-scratch trained MDLMs still lag behind state-of-the-art AR models in overall performance. This gap can be largely attributed to the disparity in training data volume and the maturity of infrastructure support—factors that have been extensively optimized over years of development for AR models. Moreover, due to the high computational cost and long training cycles required for pretraining from scratch, MDLMs mentioned above are typically limited in model scale ( ≤ \leq 8B), whereas leading AR models now routinely scale into tens or even hundreds of billions.

### 2.2 Scaling dLLMs with AR initialization

Given the strong knowledge capacity and performance of AR models, several recent studies have explored initializing dLLMs from pre-trained AR models to reduce training costs and narrow the performance gap between AR models and dLLMs. For instance, DiffusionLLaMA ( Gong et al., 2025 ) and Dream-7B ( Ye et al., 2025 ) adopt a mask annealing strategy to gradually transition from causal attention to bidirectional attention during training, while employing a CART-based loss reweighting scheme to balance token-level learning dynamics. In contrast, RND1 ( Keshigeyan et al., 2025 ) takes a more direct approach by immediately converting the causal attention mechanism of the AR model into a bidirectional one upon initialization. Notably, RND1 observes that when initializing DLM training from an AR model, preserving knowledge-intensive capabilities requires constraining updates to the model’s dense layers to prevent catastrophic forgetting.

Block Diffusion Language Models (BDLMs) ( Arriola et al., 2025 ) provide a hybrid paradigm that balances efficiency and performance by combining diffusion and AR modeling. Tokens are generated block-wise: within each block, a diffusion process reconstructs masked tokens, while blocks are produced auto-regressively. This design enables variable-length generation and supports KV-cache reuse during decoding, enhancing inference efficiency. Consequently, BDLMs can be effectively initialized from AR models, narrowing the performance gap. For example, SDAR ( Cheng et al., 2025 ) leverages the Qwen-3 series ( Yang et al., 2025 ) to train more efficient BDLMs. By exploring various block sizes and optimization strategies, it achieves performance comparable to its AR base model.

However, one key limitation across all existing methods is their restricted model scale—ranging only from 7B to 30B parameters—leaving the feasibility and scalability of AR-initialized diffusion models largely unexplored at larger scales. Besides, the low training efficiency of block diffusion hinders its widely application to large-scale corpus for large-size models. Whether such initialization strategies can effectively generalize to models beyond the 30B scale remains an open question.

### 2.3 dLLMs post-training

Beyond pre-training, post-training is crucial for unlocking the full potential of dLLMs by aligning them with specific tasks and human preferences. This process typically involves supervised fine-tuning (SFT) to instill instruction-following capabilities, reinforcement learning (RL) to enhance complex reasoning, and inference optimization to address efficiency bottlenecks.

Recent work has explored SFT to adapt dLLMs for specialized domains. For instance, Dream-Coder ( Xie et al., 2025 ) fine-tunes a 7B dLLM for code generation, demonstrating unique abilities like adaptive ”sketch-then-fill” strategies for complex algorithms. Similarly, the general-purpose model Dream-7B ( Ye et al., 2025 ) leverages SFT to achieve performance on par with top-tier AR models, while uniquely excelling at tasks requiring complex planning and constraint satisfaction. Other studies have investigated specialized fine-tuning strategies to balance quality and efficiency. Seed-Diffusion ( Song et al., 2025 ) , for example, employs a two-stage curriculum learning strategy to train a high-speed code generation model, while LiDAR ( Liu et al., 2025 ) introduces a hybrid ”think in diffusion, generate in AR” architecture through fine-tuning, significantly boosting inference throughput while maintaining quality.

To further enhance dLLMs’ reasoning abilities, researchers have begun adapting reinforcement learning techniques. However, applying standard policy gradient methods is challenging due to the intractable log-likelihood of dLLMs. To address this, SPG ( Wang et al., 2025a ) proposes a novel Sandwich Policy Gradient algorithm that obtains a more robust and less biased gradient by maximizing an evidence lower bound for high-reward samples and minimizing an evidence upper bound for low-reward ones. Another line of work, TraceRL ( Wang et al., 2025d ) , focuses on aligning the training objective with the model’s multi-step generation trajectory. This framework led to the TraDo series of models, which have not only surpassed strong AR models on reasoning benchmarks but also produced the first dLLM capable of long-chain-of-thought reasoning.

A significant challenge for dLLMs is their slow inference speed, stemming from the iterative nature of the denoising process. To mitigate this, several acceleration methods have been proposed. DPad ( Chen et al., 2025a ) offers a training-free solution by treating future tokens as a dynamic ”scratchpad” and using a sliding window and distance-based pruning to reduce redundant computations, achieving a dramatic speedup, especially for long sequence generation. In contrast, D2F ( Wang et al., 2025c ) introduces a hybrid autoregressive-diffusion paradigm that enables parallel denoising of future text blocks even before preceding ones are fully generated. This approach allows dLLMs to leverage KV-caching and, for the first time, surpass the inference speed of equivalently sized AR models.

Despite these advances, the field of dLLM post-training is still nascent. Systematic exploration of how these techniques—SFT, RL, and acceleration—interact with one another, and how they scale to models with hundreds of billions of parameters, remains an open and critical area for future research.

## 3 LLaDA2.0 Training Paradigm

Figure ( 2 ) illustrates the holistic training pipeline of LLaDA2.0, a staged and scalable framework designed to transform AR language models into highly efficient diffusion language models. Our paradigm follows a three-stage progression: (1) Continual Pre-training from AR to MDLM, (2) Block Diffusion Pre-training to transition from token-level to block-level diffusion modeling, and (3) Post-training for alignment and task specialization.

The process begins with a strong AR base model. We first perform continual pre-training to adapt this model into an MDLM, where it learns to reconstruct randomly masked tokens in a bidirectional, denoising fashion. This phase bridges the gap between AR and diffusion-based generation while preserving the representational geometry of the original model.

Building upon the trained MDLM, we then introduce block diffusion pre-training , during which the model is further trained to denoise contiguous spans of text—referred to as “blocks”—rather than individual tokens. This shift enables higher computational efficiency and better long-range coherence during generation.

Finally, after mastering non-autoregressive generation at both token and block levels, the model undergoes post-training–including SFT and DPO to align its outputs with human intent, instruction-following capability, and downstream application requirements. This stage ensures that the powerful generative backbone developed during diffusion pre-training translates into practical performance gains across diverse tasks.

Overall, LLaDA2.0’s training paradigm emphasizes knowledge inheritance , progressive adaptation , and efficiency-aware design , enabling seamless evolution from AR models to fluent, flexible, and fast diffusion large language models.

## 4 Continual Pre-training via Warmup-Stable-Decay (WSD)

Converting a pre-trained AR language model into a high-performance diffusion language model is fundamentally challenging due to the misalignment in architectural inductive biases and training objectives. While AR models generate tokens sequentially from left to right, diffusion-based models rely on bidirectional context and learn to reconstruct corrupted sequences in arbitrary unmasking orders. A direct objective switch often leads to unstable optimization and severe degradation of pretrained knowledge.

To address this gap, we propose a Warmup–Stable–Decay (WSD) continual pre-training strategy that enables a smooth, stable, and effective transition from AR to dLLM. WSD decomposes the conversion into three coordinated phases: • Warmup : Progressively increase the block size in block diffusion language models (BDLM) to gradually transform the AR model into a full-sequence masked diffusion language model (MDLM).

• Stable : Stabilize and enrich the model’s understanding of diffusion dynamics through large-scale training under the MDLM paradigm.

• Decay : Revert back to a compact BDLM with smaller block sizes to achieve better speed-efficiency trade-offs during inference.

This progressive schedule preserves the AR model’s priors while steadily adapting it to the structural requirements of diffusion modeling.

Moreover, the document-level attention mask is applied throughout training to all input sequences. This mechanism is crucial for handling packed heterogeneous documents, preventing the model from forming spurious connections across unrelated texts, thereby ensuring semantic coherence and improving learning stability within each document. In addition, we adopt a top-k checkpoint merging strategy ( Tian et al., 2025 ) , to enhance generalization by averaging the parameters of the best-performing checkpoints, smoothing the parameter landscape, and yielding a more robust final model with boosted performance.

### 4.1 Warmup-Stable-Decay Conversion Strategy

We begin with the AR base models Ling-mini-2.0 and Ling-flash-2.0 ( Ling et al., 2025 ) , which can be viewed as a special case of BDLM with block size 1. This perspective allows us to treat AR models as the initial BDLM configuration with minimal granularity.

#### Phase-1: Progressive Block Size Warmup

The core idea of the warmup phase is to gradually increase the block size , thereby expanding the receptive field within which the model performs joint denoising. Starting from block size L B = 1 L_{B}=1 , we incrementally scale it up to 4, 32, then 64, and ultimately reach L B = 4096 L_{B}=4096 — at which point the entire sequence is treated as one single block. To avoid fragmented blocks, we require the sequence length to be divisible by the current block size. At the final enlargement, the BDLM becomes equivalent to a standard MDLM that operates over fully masked sequences with global attention. Crucially, each block-size transition is trained on moderate-scale data to ensure smooth adaptation. This progressive enlargement allows the model to smoothly adapt its internal representations to handle larger contextual spans and more complex masking patterns.

#### Phase-2: Large Scale Stable Training

Once the block size reaches 4096 and the model transitions to the MDLM pattern, the “clean” part of the attention computation (see Figure 2 ) no longer needs to be maintained. This significantly reduces the computational cost of attention, allowing data to be processed far more efficiently under the MDLM paradigm. With the model now fully adapted to this regime, the stable training phase focuses on deepening its understanding of diffusion dynamics through extensive training on large-scale corpora. At this stage, the block size is fixed at 4096, effectively making every input a single-block sequence, equivalent to the classical MDLM setting.

#### Phase-3: Block Size Decay

Finally, after large-scale MDLM training, we gradually reduce the block size from 4096 to a small block size (e.g., 32) to convert the model back into an efficient BDLM. This decay process distills the global contextual knowledge learned during MDLM into a compact blockwise structure. By decreasing the block size step-by-step (e.g., starting from 4096 to 2048) rather than abruptly, the model smoothly adapts from global to local conditioning, preserving its semantic understanding while regaining BDLM’s practical benefits such as KV-cache reuse and fast variable-length generation.

#### Overall Training Objective

The optimization objective of BDLM ( Arriola et al., 2025 ) is designed to enable the model to accurately reconstruct the original, uncorrupted tokens within these designated masked blocks using a standard cross-entropy loss. Specifically, we define the training loss during warmup and decay phases (phase-1&3) under the BDLM paradigm as: ℒ BDLM ( θ ) = − 𝔼 t , 𝒙 0 , 𝒙 𝒕 [ α t ′ 1 − α t ∑ k = 1 K ∑ i = 1 L B 𝟙 [ x t , k i = [MASK] ] log p θ ( 𝒙 0 , k i | 𝒙 0 , < k , 𝒙 t , k ) ] , \mathcal{L}_{\text{BDLM}}(\theta)=-\mathbb{E}_{t,\bm{x}_{0},\bm{x_{t}}}\left[\frac{\alpha_{t}^{\prime}}{1-\alpha_{t}}\sum_{k=1}^{K}\sum_{i=1}^{L_{B}}\mathbb{1}[x_{t,k}^{i}=\text{[MASK]}]\log p_{\theta}(\bm{x}_{0,k}^{i}|\bm{x}_{0,<k},\bm{x}_{t,k})\right], (1) where the expectation is over timestep t t , the clean sequence 𝒙 0 \bm{x}_{0} , and its corrupted version 𝒙 t \bm{x}_{t} (tokens masked with probability 1 − α t 1-\alpha_{t} ). Indicator 𝟙 ​ [ ⋅ ] \mathbb{1}[\cdot] ensures predictions are made only for masked tokens, and − α t ′ / ( 1 − α t ) -\alpha_{t}^{\prime}/(1-\alpha_{t}) is the diffusion‑derived time weight. Here K = L total / L B K=L_{\text{total}}/L_{B} is the number of blocks, L B L_{B} the block size, x t , k i x_{t,k}^{i} the i i -th token in block k k , 𝒙 0 , < k \bm{x}_{0,<k} the preceding clean blocks, and 𝒙 t , k \bm{x}_{t,k} the noisy version of the current block.

During the stable training (phase-2) of MDLM (i.e., K=1), the objective simplifies to: ℒ MDLM ( θ ) = − 𝔼 t , 𝒙 0 , 𝒙 t [ α t ′ 1 − α t ∑ i = 1 L 𝟙 [ x t i = [MASK] ] log p θ ( x 0 i | 𝒙 t ) ] . \mathcal{L}_{\text{MDLM}}(\theta)=-\mathbb{E}_{t,\bm{x}_{0},\bm{x}_{t}}[\frac{\alpha^{\prime}_{t}}{1-\alpha_{t}}\sum_{i=1}^{L}\mathbb{1}[x_{t}^{i}=\text{[MASK]}]\log p_{\theta}(x^{i}_{0}|\bm{x}_{t})]. (2)

### 4.2 Document-level Attention Mask

Our training sequences are formed by packing heterogeneous documents into fixed-length segments to maximize throughput. However, this introduces artificial long-range dependencies across semantically unrelated texts. Without careful handling, standard attention would incorrectly attend across document boundaries, leading to contextual confusion and significantly hindering the model’s ability to perform robust bidirectional modeling crucial for denoising.

To mitigate this fundamental challenge and preserve semantic coherence, we redefine the attention mechanism with a specialized block-wise document-level attention mask . This mask ensures that attention operates strictly within document boundaries, preventing cross-document contamination and allowing the model to fully leverage bidirectional context for accurate reconstruction of corrupted blocks. The native Block Diffusion vectorizes the training process to achieve parallel training of blocks, and this mask is applied accordingly. Specifically, for a concatenated sequence x f ​ u ​ l ​ l x_{full} of length 2 ​ L 2L (comprising x t x_{t} followed by x 0 x_{0} ), and assuming tokens i i and j j are already confined to the same document segment (as enforced by the initial document-level mask), the attention mask 𝑴 ∈ { 0 , 1 } 2 ​ L × 2 ​ L \bm{M}\in\{0,1\}^{2L\times 2L} is constructed by dividing each sequence ( x t x_{t} and x 0 x_{0} ) into contiguous blocks. Let b ⁡ ( k ) = ⌊ k / L B ⌋ b(k)=\lfloor k/L_{B}\rfloor denote the block index for token k k given a block size L B L_{B} . The mask is defined as: 𝑴 i ​ j = { 𝟙 b ⁡ ( i ) = b ⁡ ( j ) if ​ i ∈ x t ​ and ​ j ∈ x t 𝟙 b ⁡ ( i ) > b ⁡ ( j − L ) if ​ i ∈ x t ​ and ​ j ∈ x 0 𝟙 b ⁡ ( i − L ) ≥ b ⁡ ( j − L ) if ​ i ∈ x 0 ​ and ​ j ∈ x 0 0 otherwise \bm{M}_{ij}=\begin{cases}\mathbb{1}_{b(i)=b(j)}&\text{if }i\in x_{t}\text{ and }j\in x_{t}\\ \mathbb{1}_{b(i)>b(j-L)}&\text{if }i\in x_{t}\text{ and }j\in x_{0}\\ \mathbb{1}_{b(i-L)\geq b(j-L)}&\text{if }i\in x_{0}\text{ and }j\in x_{0}\\ 0&\text{otherwise}\end{cases} (3) Where i , j ∈ { 0 , 1 , … , 2 ​ L − 1 } i,j\in\{0,1,\dots,2L-1\} are the indices in the full sequence. The first condition ( 𝟙 b ⁡ ( i ) = b ⁡ ( j ) \mathbb{1}_{b(i)=b(j)} ) implements block-diagonal attention within the noisy sequence x t x_{t} . The second ( 𝟙 b ⁡ ( i ) > b ⁡ ( j − L ) \mathbb{1}_{b(i)>b(j-L)} ) enables cross-attention from x t x_{t} to x 0 x_{0} , but only from blocks in x t x_{t} to earlier blocks in x 0 x_{0} . The third ( 𝟙 b ⁡ ( i − L ) ≥ b ⁡ ( j − L ) \mathbb{1}_{b(i-L)\geq b(j-L)} ) imposes a causal block attention pattern within the clean sequence x x , allowing a block to attend to itself and all preceding blocks. The ”otherwise” condition corresponds to a zero matrix, explicitly preventing attention from queries in x 0 x_{0} to keys in x t x_{t} . This allows each block to leverage context from relevant blocks (according to the mask) for reconstruction, capturing inter-block dependencies while maintaining the causal and block-diagonal principles essential for stable diffusion training. During our exploration, we also experimented with other tricks like random-length ( Xie et al., 2025 ) and CART ( Ye et al., 2025 ) . However, the results demonstrate that the document-level attention mask is more fundamental in CPT training compared to these techniques, and it consistently achieves superior performance. As illustrated in Figure 2 , this forms a structured attention layout that balances locality and global document coherence.

For MDLM, the document-level attention mask simplifies to 𝑴 ∈ { 0 , 1 } L × L \bm{M}\in\{0,1\}^{L\times L} , where: 𝑴 i ​ j = { 1 , if i , j belong to the same document , 0 , otherwise . \bm{M}_{ij}=\begin{cases}1,&\text{if $i,j$ belong to the same document},\\ 0,&\text{otherwise}.\end{cases} (4)

### 4.3 Top-k Checkpoint Merge

To further enhance the generalization and robustness of our Block Diffusion Language Model, we employ a top-k checkpoint merging strategy. Upon completion of BDLM pre-training, we identify the top k k best-performing model checkpoints, typically selected based on validation metrics like perplexity. The parameters (weights and biases) of these k k checkpoints are then arithmetically averaged to form a single, unified BDLM. Based on WSM scheduler ( Tian et al., 2025 ) , this merge strategy can effectively ensemble diverse ”knowledge” captured by the model at various optimal or near-optimal training states. This smooths the parameter landscape, mitigates overfitting, and yields a more stable and generalizable model. A key advantage of the WSM approach is its optimizer-agnostic nature, allowing seamless integration without altering the underlying training pipeline. Crucially, this post-training Top-k Merge fundamentally differs from the Exponential Moving Average (EMA). While EMA is an in-training technique that continuously smooths parameters, merging is an offline procedure. It explicitly selects and averages distinct, high-performing model states, consolidating their strengths rather than merely smoothing the final training step.

## 5 Post-training

### 5.1 Supervised Fine-Tuning with Block Diffusion

Following the pre-training phase, the model is aligned to follow user instructions through supervised fine-tuning (SFT). This is achieved by adapting the diffusion training objective to be conditional on an input prompt, 𝒄 \bm{c} . The model is thus trained to generate the desired response 𝒙 0 \bm{x}_{0} by minimizing the following loss function: ℒ SFT ( θ ) = − 𝔼 t , ( 𝒄 , 𝒙 0 ) , 𝒙 t [ α t ′ 1 − α t ∑ k = 1 K ∑ i = 1 L B 𝟙 [ x t , k i = [MASK] ] log p θ ( x 0 , k i | 𝒄 , 𝒙 0 , < k , 𝒙 t , k ) ] . \mathcal{L}_{\text{SFT}}(\theta)=-\mathbb{E}_{t,(\bm{c},\bm{x}_{0}),\bm{x}_{t}}\left[\frac{\alpha_{t}^{\prime}}{1-\alpha_{t}}\sum^{K}_{k=1}\sum_{i=1}^{L_{B}}\mathbb{1}[x_{t,k}^{i}=\text{[MASK]}]\log p_{\theta}(x^{i}_{0,k}|\bm{c},\bm{x}_{0,<k},\bm{x}_{t,k})\right]. (5) Here, the model p θ p_{\theta} learns to predict the original tokens x 0 , k i x^{i}_{0,k} of a clean response from a noisy version 𝒙 t \bm{x}_{t} . The loss is computed only on masked tokens within the current noisy block 𝒙 t , k \bm{x}_{t,k} . To do this, the prediction is conditioned on the prompt 𝒄 \bm{c} , auto-regressive context from prior clean blocks 𝒙 0 , < k \bm{x}_{0,<k} , and the current noisy block 𝒙 t , k \bm{x}_{t,k} that it must denoise.

#### Padding strategies & Mask ratio bandwidth

To ensure compatibility with our block-wise attention mask, we quantize each sequence’s length. Specifically, the original length is rounded up to the nearest multiple of the block size, b b . This process defines an ”effective length” for each sequence, guaranteeing its boundaries align perfectly with the block boundaries required by the attention mechanism.

To optimize the training dynamics, we further implement a “mask ratio bandwidth” strategy. Standard discrete diffusion processes typically sample mask probabilities across the full unit interval, α t ∼ U ⁡ [ 0 , 1 ] \alpha_{t}\sim U[0,1] . However, as identified by Arriola et al. (2025) , extreme masking rates induce high gradient variance while offering minimal learning signal: near-zero masking renders reconstruction trivial, while near-total masking reduces the objective to simply learning data marginals. To mitigate this, we clip the noise schedule, constraining the sampling of mask rates to a bounded interval [ α min , α max ] [\alpha_{\min},\alpha_{\max}] rather than the full range. This bandwidth restriction focuses the training objective on the noise regimes that provide the most informative gradients, thereby stabilizing convergence and improving the model’s generative perplexity.

#### Complementary Masking

Complementary Masking ( Li et al., 2025 ) is a training optimization that enhances the data efficiency of the MDLM objective, ℒ MDLM ​ ( θ ) \mathcal{L}_{\text{MDLM}}(\theta) . The strategy’s core principle is to generate two antithetical training instances from a single source sequence 𝒙 0 \bm{x}_{0} . A primary noised sequence, 𝒙 t \bm{x}_{t} , is formed using a random mask, while a complementary sequence, 𝒙 t ′ \bm{x}^{\prime}_{t} , is simultaneously produced using that mask’s logical inverse 1 1 1 We also try complementary masking in CPT and find it only works fine on corpus less than 100B tokens, while it does not show advantages with more training data, so that we only adopt it in post-training. .

By incorporating both 𝒙 t \bm{x}_{t} and 𝒙 t ′ \bm{x}^{\prime}_{t} into the same training batch, this method provides a deterministic guarantee: every token position across the sequence length L L is presented to the model in its uncorrupted state exactly once within the pair. This not only doubles the effective data utilization from each sample, thereby accelerating convergence, but also entirely eliminates token-level sampling bias. Consequently, the model benefits from a more comprehensive and uniform learning signal at every optimization step, leading to enhanced robustness.

#### Data Recipe Curation

A balanced, high-quality SFT dataset underpins the model’s capabilities, achieved through a strategic composition of tasks spanning three principal pillars: Reasoning, General, and Industrial. The Reasoning pillar hones analytical and logical faculties through mathematics and code generation. The General pillar cultivates linguistic richness and social intelligence via creative and dialogic tasks. The Industrial pillar embeds domain-specific expertise by simulating end-to-end workflows under real-world constraints. This integrated methodology ensures a holistic skill profile, preventing capability skew and enabling fluid shifts between abstract reasoning and applied problem-solving.

### 5.2 Confidence-Aware Parallel Training

To enhance the model’s predictive confidence, which is crucial for efficient parallel decoding, we propose Confidence-Aware Parallel (CAP) Training. We incorporate an auxiliary confidence loss, ℒ conf \mathcal{L}_{\text{conf}} , inspired by dParallel ( Chen et al., 2025b ) . The primary objective, ℒ SFT \mathcal{L}_{\text{SFT}} , ensures correctness but provides diminishing incentive to sharpen the predictive distribution for tokens that are already correctly predicted. The confidence loss addresses this by selectively minimizing the entropy of the model’s output distribution, p θ ​ ( 𝒙 0 | 𝒙 t , 𝒄 ) p_{\theta}(\bm{x}_{0}|\bm{x}_{t},\bm{c}) , but only for the subset of tokens that are correctly predicted in a given step. This compels the model to increase its certainty on its correct predictions. The final training objective is a weighted combination of the two losses: ℒ ⁡ ( θ ) = ℒ SFT ​ ( θ ) + λ ​ ℒ conf ​ ( θ ) , \mathcal{L}(\theta)=\mathcal{L}_{\text{SFT}}(\theta)+\lambda\mathcal{L}_{\text{conf}}(\theta), (6) where λ \lambda is a hyperparameter that balances the two objectives. As illustrated in Figure 3 , CAP training effectively improves the decoding efficiency of LLaDA2.0-flash while maintaining competitive compression performance, demonstrating a favorable trade-off between generation quality and inference speed.

### 5.3 DPO

Building upon the SFT stage, we further align the policy model π θ \pi_{\theta} with human intent using Direct Preference Optimization. To support this, we constructed a comprehensive dataset comprising 1.5 million preference pairs across diverse domains, including general knowledge, mathematics, and instruction following. To ensure a stable transition in optimization, the learning rate for the DPO stage is initialized consistently with the final learning rate of the preceding SFT phase.

Since the policy model π θ \pi_{\theta} is trained to reconstruct clean tokens 𝒙 0 \bm{x}_{0} from noisy blocks 𝒙 t \bm{x}_{t} conditioned on context 𝒄 \bm{c} , the standard DPO formulation—which requires exact log-likelihoods—is intractable. Following established practices for diffusion models, we substitute the conditional log-likelihoods with their ELBO. We first define the conditional Block Diffusion ELBO, B BDLM ​ ( θ , 𝒙 | 𝒄 ) B_{\text{BDLM}}(\theta,\bm{x}|\bm{c}) , for a response 𝒙 \bm{x} . This term mirrors the inner objective of our SFT loss (equation 5 ) and is estimated via a single Monte Carlo sample over timesteps and noise: B BDLM ( θ , 𝒙 | 𝒄 ) = 𝔼 t , 𝒙 t [ α t ′ 1 − α t ∑ k = 1 K ∑ i = 1 L B 𝟙 [ x t , k i = [MASK] ] log p θ ( x k i | 𝒄 , 𝒙 < k , 𝒙 t , k ) ] . B_{\text{BDLM}}(\theta,\bm{x}|\bm{c})=\mathbb{E}_{t,\bm{x}_{t}}\left[\frac{\alpha_{t}^{\prime}}{1-\alpha_{t}}\sum_{k=1}^{K}\sum_{i=1}^{L_{B}}\mathbb{1}[x_{t,k}^{i}=\text{[MASK]}]\log p_{\theta}(x^{i}_{k}|\bm{c},\bm{x}_{<k},\bm{x}_{t,k})\right]. (7) Given a preference pair ( 𝒙 w , 𝒙 l ) (\bm{x}_{w},\bm{x}_{l}) , where 𝒙 w \bm{x}_{w} is the preferred response and 𝒙 l \bm{x}_{l} is the dispreferred response, the DPO objective maximizes the margin between the ELBO estimates of the policy π θ \pi_{\theta} and the frozen reference model π θ ref \pi_{\theta_{\text{ref}}} (initialized from the post-SFT model). The final loss function is defined as: ℒ DPO ​ ( θ ) = − 𝔼 ( 𝒄 , 𝒙 w , 𝒙 l ) ∼ 𝒟 ​ [ log ⁡ σ ⁡ ( β ⁡ [ Δ ​ B ​ ( 𝒙 w | 𝒄 ) − Δ ​ B ​ ( 𝒙 l | 𝒄 ) ] ) ] , \mathcal{L}_{\text{DPO}}(\theta)=-\mathbb{E}_{(\bm{c},\bm{x}_{w},\bm{x}_{l})\sim\mathcal{D}}\left[\log\sigma\left(\beta\left[\Delta B(\bm{x}_{w}|\bm{c})-\Delta B(\bm{x}_{l}|\bm{c})\right]\right)\right], (8) where Δ ​ B ​ ( 𝒙 | 𝒄 ) = B BDLM ​ ( θ , 𝒙 | 𝒄 ) − B BDLM ​ ( θ ref , 𝒙 | 𝒄 ) \Delta B(\bm{x}|\bm{c})=B_{\text{BDLM}}(\theta,\bm{x}|\bm{c})-B_{\text{BDLM}}(\theta_{\text{ref}},\bm{x}|\bm{c}) represents the ELBO advantage of the policy over the reference model, and β \beta is a hyperparameter (set to 0.1) that controls the deviation from the reference policy.

### 5.4 Inference

We sample one block at a diffusion step, conditioned on previously sampled blocks p θ ​ ( 𝒙 s b | 𝒄 , 𝒙 t < b ) p_{\theta}(\bm{x}^{b}_{s}|\bm{c},\bm{x}^{<b}_{t}) . The generation of each block is itself a multi-step iterative refinement process. At each step, candidate tokens are sampled for all remaining unfilled positions within the block. A hybrid acceptance strategy is then employed: we first accept all tokens whose sampling probability exceeds a predefined confidence ‘threshold‘. If an insufficient number of tokens meet this criterion, a low-confidence fallback is triggered, where we instead accept a fixed number of the most probable tokens regardless of their absolute confidence. This dual mechanism ensures steady generation progress.

## 6 Evaluation

### 6.1 Setup

To comprehensively evaluate the quality of instruction-tuned models, we employ a diverse suite of benchmarks categorized into five dimensions:

• Knowledge : MMLU ( Hendrycks et al., 2020 ) , MMLU-Pro ( Wang et al., 2024 ) , GPQA-Diamond ( Rein et al., 2024 ) , ARC ( Clark et al., 2018 ) , CMMLU ( Li et al., 2023a ) C-Eval ( Huang et al., 2023 ) , GAOKAO-Bench ( Zhang et al., 2023 ) , SciBench ( Wang et al., 2023 ) , PHYBench ( Qiu et al., 2025 ) , TriviaQA ( Joshi et al., 2017 )

• Reasoning : SQuAD 2.0 ( Rajpurkar et al., 2018 ) , DROP ( Dua et al., 2019 ) , KOR-Bench ( Ma et al., 2024 ) , HellaSwag ( Zellers et al., 2019 ) , BIG-Bench Hard ( Suzgun et al., 2023 ) , BIG-Bench Extra Hard ( Kazemi et al., 2025 ) , MuSR ( Sprague et al., 2023 ) , ZebraLogic ( Lin et al., 2025 ) , PrOntoQA ( Saparov and He, 2022 ) , PIQA ( Bisk et al., 2020 ) , OCNLI ( Hu et al., 2020 ) , BIG-Bench Hard-CN ( team, 2023c )

• Coding : CRUXEval ( Gu et al., 2024 ) , MBPP ( Austin et al., 2021 ) , MultiPL-E ( Cassano et al., 2023 ) , HumanEval ( Chen et al., 2021 ) , BigCodeBench ( Zhuo et al., 2024 ) , LiveCodeBench ( Jain et al., 2024 ) , Spider ( Yu et al., 2018 ) , BIRD ( Li et al., 2023b ) , HumanEval+ ( Liu et al., 2023 ) , MBPP+ ( Liu et al., 2023 ) , HumanEvalFix ( Muennighoff et al., 2023 ) , Aider ( team, 2023a ) , HumanEval-CN ( team, 2023c )

• Math : GSM8K ( Cobbe et al., 2021 ) , MATH ( Hendrycks et al., 2021 ) , OlympiadBench ( He et al., 2024 ) , AIME 2025 ( AIME, 2025 ) , Omni-MATH ( Gao et al., 2024 ) , HARDMath2 ( Roggeveen et al., 2025 ) , GSM-Plus ( Li et al., 2024 ) , CMATH ( Wei et al., 2023 )

• Agent & Alignment : BFCL ( Patil et al., 2025 ) , IFEval ( Zhou et al., 2023 ) , CodeIF-Bench ( Wang et al., 2025b ) , Nexus Function Calling Benchmark ( team, 2023b )

This extensive evaluation suite, comprising a total of 47 benchmarks, provides a holistic foundation for assessing model capabilities. In our experiments, we compare the LLaDA2.0 series against strong open-source auto-regressive (AR) models.

For all LLaDA2.0 models, we utilize a temperature of 0.0, a block size of 32, and a decoding threshold of 0.95.

### 6.2 Results

The overall results, presented in the following tables, indicate that the LLaDA2.0 architecture is not only highly competitive, but also shows a promising trend of closing the performance gap with, and even surpassing, AR models in specific key areas. Our models consistently demonstrate strong, and often superior, performance in complex, structured tasks. For instance, LLaDA2.0-mini already outperforms a comparable AR model (Qwen3-8B) in the domains of Reasoning, Coding, and Math. This signal is amplified in our larger model, as LLaDA2.0-flash achieves parity with the powerful Qwen3-30B-A3B-Instruct-2507 and establishes a lead in the critical Coding and Agent domains. This suggests that as diffusion models scale, their inherent strengths in structured generation and tool use become increasingly apparent.

As shown in Table 1 , LLaDA2.0-mini achieves a competitive average score of 64.34, closely approaching its AR peer, Ling-mini-2.0 (65.77). This demonstrates the fundamental viability of the diffusion approach. More importantly, it shows promising signals in complex tasks, outperforming its direct competitor on reasoning benchmarks like SQuAD 2.0 (86.50) and demonstrating more robust instruction following on IFEval (80.78). Its strong performance in coding tasks such as HumanEval (86.59) further suggests an early aptitude for structured generation.

This potential becomes even more evident with our larger model, LLaDA2.0-flash . As shown in Table 2 , with an average score of 73.18, it stands firmly on par with strong AR models such as Qwen3-30B-A3B-Instruct-2507 (73.60). Crucially, LLaDA2.0-flash begins to exhibit clear advantages in complex generative tasks, a sign that the diffusion architecture may hold inherent strengths. In the critical domain of coding, it consistently outperforms its AR peers, scoring higher on HumanEval (94.51), MBPP (88.29) and MultiPL-E (74.87). This trend of surpassing AR models also extends to agent capabilities (BFCL v3: 75.43) and advanced mathematics (AIME 2025: 60.00).

In conclusion, the LLaDA2.0 series successfully demonstrates that diffusion-based language models are a powerful and scalable alternative to the dominant auto-regressive paradigm. While rapidly narrowing the gap on general benchmarks, they are already showcasing the potential to surpass traditional architectures in complex, structured domains like code generation and tool use. This positions diffusion models as a highly promising direction for the future of language generation.

### 6.3 Analysis

#### Analysis of Inference Hyper-parameters

In addition to our main evaluation, we conducted a brief analysis to tune key inference hyperparameters. To ensure efficiency, this analysis was performed on our LLaDA2.0-mini model, using a representative subset of our benchmarks to understand the trade-off between generation quality (score) and inference speed (measured as TPF - Tokens Per Forward; higher is faster).

Denoising Threshold . We first investigate the impact of the Denoising Threshold. While keeping the Block Size fixed at 32, we varied the threshold and observed its effect on quality and speed. As shown in Figure 5 , the results reveal a clear trade-off. A threshold of 0.95 achieved the highest quality score (70.15) at the cost of the lowest inference speed (2.55 TPF). Lowering the threshold to 0.85 boosted the speed to its peak (3.31 TPF), but led to an unacceptable degradation in quality, with the score dropping to 67.90.

Block Size . Subsequently, we analyze the effect of Block Size. We set the Denoising Threshold to 0.95, the optimal value identified in the prior experiment. The results in Figure 5 demonstrate a similar trade-off. A block size of 16 yielded the highest score (70.26) but with the slowest inference (2.44 TPF). In contrast, increasing the block size to 32 substantially improved the speed to 2.55 TPF with only a marginal quality drop to 70.15. Further increasing the block size to 64 proved suboptimal, as it degraded both score and speed relative to the size-32 setting. Therefore, a block size of 32 emerges as the most compelling choice, offering a significant speed-up for a negligible performance cost.

In summary , based on this analysis, the configuration for our main evaluation is well-supported. The Denoising Threshold of 0.95 is the clear choice for maximizing quality. For block-size, the setting of 32 represents an optimal balance, providing the highest throughput with virtually no sacrifice in performance compared to the slightly higher-scoring but slower setting of 16.

#### Analysis of Context Length

To rigorously validate our model’s performance across various context lengths, we conducted a series of evaluations using the RULER benchmark.

As shown in Figure 5 , both models demonstrate strong performance and stability within context length of 32k. The LLaDA2.0-flash model is particularly robust, maintaining a score above 93 across all lengths from 4k to 32k. The LLaDA2.0-mini model also achieves high scores, starting at 93.29 for 4k but showing a degradation to 83.94 at 32k.

To test the models’ extrapolation capabilities, we extended the context length to 64k. This was achieved by employing dynamic RoPE scaling during inference, specifically using the YaRN method with a scaling factor of 2.0. However, this extension resulted in a performance degradation for both models, demonstrating a clear trade-off between context length extension and task accuracy.

In summary , this evaluation highlights two key findings: (1) The LLaDA2.0 models are exceptionally robust for long-context tasks within their native 32k window. (2) They can be successfully extended to handle 64k sequences via YaRN scaling, providing flexibility for extreme-length applications, albeit with a predictable performance cost.

## 7 Training & Inference Infrastructure

### 7.1 Pretraining

We adopt Megatron-LM ( Shoeybi et al., 2019 ) as the pretraining backend to enable efficient training of a 100B-parameter model with long sequences, leveraging data parallelism (DP), pipeline parallelism (PP), tensor parallelism (TP), context parallelism (CP), and expert parallelism (EP), as Figure 6 shows. To ensure consistency of masked tokens, we generate masked tokens on a single model-parallel (MP, that is, TP and PP) rank and then broadcast to all other ranks within the MP ranks.

#### Efficient Block Diffusion Training

For flexible support of arbitrary block diffusion attention mask, we utilize cuDNN as the backend for the attention mechanism. This approach achieves more than 1.3x end-to-end speedup and over 90% memory savings in the attention layer compared to the unfused attention implementation in TransformerEngine when training LLaDA2.0-mini. We further apply a zig-zag partitioning strategy to the block diffusion attention mask to achieve effective load balancing across the CP group.

#### Numerical Stability

During the transition from AR to diffusion models, training can suffer from gradient explosion, especially at high mask ratios within a document. This issue stems from the fact that masked token embeddings are set to zero during AR training, as these tokens are never observed, leading their corresponding weights to gradually decay to zero. A straightforward fix, randomly reinitializing the masked token embeddings upon loading the AR model, may disrupt other well-trained parameters, potentially causing catastrophic forgetting. To mitigate this while preserving pre-trained knowledge, we instead add independent Gaussian noise to the output of the embedding layer for each masked token during the initial iterations of training. This ensures that the L2 norm of the masked token’s embedding remains significant to avoid gradient explosion, thereby stabilizing the training process.

### 7.2 Post-Training

For the post-training phase, we leverage dFactory 2 2 2 https://github.com/inclusionAI/dFactory ( InclusionAI, 2025 ) , a repository providing efficient training recipes for dLLMs. Built upon the VeOmni ( Ma et al., 2025a ) distributed training framework, dFactory allows us to effectively implement complex parallelization schemes. Specifically, our setup for fine-tuning LLaDA2.0 combines Data Parallelism (DP) and Expert Parallelism (EP) to ensure scalable and stable training. To further enhance data throughput and hardware utilization, we adopt a data packing strategy analogous to those used in continued pre-training, which concatenates multiple short sequences into a single longer sequence. This integrated approach provides a robust and high-performance infrastructure for the post-training of our model.

### 7.3 Inference Engine

We adapt dInfer 3 3 3 https://github.com/inclusionAI/dInfer ( Ma et al., 2025b ) --originally built for high-performance diffusion LLM inference--to efficiently support block diffusion inference. This requires the inference engine to leverage optimization techniques traditionally designed for AR models. For instance, the framework can now effectively exploit KV-cache reuse to substantially reduce prefill computation. As block diffusion inference closely resembles auto-regressive generation in the execution pattern, we also incorporated block diffusion inference support into SGLang 4 4 4 https://github.com/sgl-project/sglang/issues/12766 ( Zheng et al., 2024 ) , allowing it to benefit from the same class of system-level optimizations designed for AR models. More mature features in dInfer are undergoing to transport to SGLang.

#### Inference speed

Figure 3 compares the average inference throughput (Tokens Per Second, TPS = #decoding tokens/#total-time) of our optimized LLaDA2.0-flash models against state-of-the-art AR models of similar scale on four reasoning and code-generation benchmarks (HumanEval, MBPP, GSM8K, and CRUXEval). All models are evaluated under a consistent generation setup. For diffusion-based models (LLaDA2.0-flash and LLaDA2.0-flash-CAP), we adopt a threshold decoder with a threshold of 0.95. The AR baselines (Ling-flash-2.0 and Qwen3-30B-A3B-Instruct-2507) are deployed using SGLang, while the diffusion models are served with dInfer, ensuring fair performance comparison in real inference environments. As shown, LLaDA2.0-flash-CAP reaches 535 TPS, outperforming the standard LLaDA2.0-flash (383 TPS) and providing up to 2.1× speed-up over the AR baselines (256 TPS and 237 TPS).

## 8 Conclusion

In this work, we introduced LLaDA2.0, discrete diffusion language models scaling up to 100B total parameters through systematic conversion from auto-regressive models, as well as a set of novel and comprehensive recipes designed to smooth and effectively transform traditional AR language models into highly efficient and performant Masked Diffusion Language Models.

Through extensive evaluations, it validates the feasibility of the training paradigm. The LLaDA2.0-mini and LLaDA2.0-flash models achieve performances that are competitive with their AR counterparts. Slightly surprisingly, LLaDA2.0-flash seems to have demonstrated advantages in complex, structured domains such as code generation, mathematical reasoning, and agentic tool use. These may have opened a new door to future work in the agentic LLM era while solidifying a gaugeable potential of dLLM for test-time scaling.

Future work may point to further scaling of the parameter volume, RL/thinking paradigm and extending the decoding speed to its extreme.

## References

AIME (2025) AIME AIME Problems and Solutions . External Links: Link Cited by: 4th item .

Arriola et al. (2025) M. Arriola, A. Gokaslan, J. T. Chiu, Z. Yang, Z. Qi, J. Han, S. S. Sahoo, and V. Kuleshov Block diffusion: interpolating between autoregressive and diffusion language models . arXiv:2503.09573 . Cited by: §1 , §2.2 , §4.1 , §5.1 .

Austin et al. (2021) J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, et al. Program synthesis with large language models . arXiv:2108.07732 . Cited by: 3rd item .

Bisk et al. (2020) Y. Bisk, R. Zellers, J. Gao, Y. Choi, et al. Piqa: reasoning about physical commonsense in natural language . In Proceedings of the AAAI conference on artificial intelligence , Vol. 34 , pp. 7432–7439 . Cited by: 2nd item .

Cassano et al. (2023) F. Cassano, J. Gouwar, D. Nguyen, S. Nguyen, L. Phipps-Costin, D. Pinckney, M. Yee, Y. Zi, C. J. Anderson, M. Q. Feldman, et al. MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code Generation . IEEE Transactions on Software Engineering 49 ( 7 ), pp. 3675–3691 . Cited by: 3rd item .

Chen et al. (2021) M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al. Evaluating large language models trained on code . arXiv:2107.03374 . Cited by: 3rd item .

Chen et al. (2025a) X. Chen, S. Huang, C. Guo, C. Wei, Y. He, J. Zhang, H. ”. Li, and Y. Chen DPad: Efficient Diffusion Language Models with Suffix Dropout . arXiv . Note: arXiv:2508.14148 Cited by: §2.3 .

Chen et al. (2025b) Z. Chen, G. Fang, X. Ma, R. Yu, and X. Wang dParallel: Learnable Parallel Decoding for dLLMs . arXiv:2509.26488 . Cited by: §5.2 .

Cheng et al. (2025) S. Cheng, Y. Bian, D. Liu, L. Zhang, Q. Yao, Z. Tian, W. Wang, Q. Guo, K. Chen, B. Qi, et al. SDAR: a synergistic diffusion-autoregression paradigm for scalable sequence generation . arXiv:2510.06303 . Cited by: §2.2 .

Clark et al. (2018) P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord Think you have solved question answering? try arc, the ai2 reasoning challenge . arXiv:1803.05457 . Cited by: 1st item .

Cobbe et al. (2021) K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training Verifiers to Solve Math Word Problems . arXiv:2110.14168 . Cited by: 4th item .

Dua et al. (2019) D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning over Paragraphs . arXiv:1903.00161 . Cited by: 2nd item .

Gao et al. (2024) B. Gao, F. Song, Z. Yang, Z. Cai, Y. Miao, Q. Dong, L. Li, C. Ma, L. Chen, R. Xu, et al. Omni-math: a universal olympiad level mathematic benchmark for large language models . arXiv:2410.07985 . Cited by: 4th item .

Gong et al. (2025) S. Gong, S. Agarwal, Y. Zhang, J. Ye, L. Zheng, M. Li, C. An, P. Zhao, W. Bi, J. Han, H. Peng, and L. Kong Scaling diffusion language models via adaptation from autoregressive models . In The Thirteenth International Conference on Learning Representations , Cited by: §1 , §2.2 .

Grattafiori et al. (2024) A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Vaughan, et al. The Llama 3 Herd of Models . arXiv:2407.21783 . Cited by: §1 .

Gu et al. (2024) A. Gu, B. Rozière, H. Leather, A. Solar-Lezama, G. Synnaeve, and S. I. Wang CruxEval: A Benchmark for Code Reasoning, Understanding and Execution . arXiv:2401.03065 . Cited by: 3rd item .

He et al. (2024) C. He, R. Luo, Y. Bai, S. Hu, Z. L. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, et al. OlympiadBench: A Challenging Benchmark for Promoting AGI with Olympiad-Level Bilingual Multimodal Scientific Problems . arXiv:2402.14008 . Cited by: 4th item .

Hendrycks et al. (2020) D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt Measuring Massive Multitask Language Understanding . arXiv:2009.03300 . Cited by: 1st item .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt Measuring Mathematical Problem Solving with the Math Dataset . arXiv:2103.03874 . Cited by: 4th item .

Hu et al. (2020) H. Hu, K. Richardson, L. Xu, L. Li, S. Kübler, and L. S. Moss Ocnli: original chinese natural language inference . arXiv:2010.05444 . Cited by: 2nd item .

Huang et al. (2023) Y. Huang, Y. Bai, Z. Zhu, J. Zhang, J. Zhang, T. Su, J. Liu, C. Lv, Y. Zhang, Y. Fu, et al. C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models . Advances in Neural Information Processing Systems 36 , pp. 62991–63010 . Cited by: 1st item .

Hurst et al. (2024) A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. GPT-4o System Card . arXiv:2410.21276 . Cited by: §1 .

InclusionAI (2025) InclusionAI dFactory: Easy and Efficient dLLM Fine-Tuning . External Links: Link Cited by: §7.2 .

Jain et al. (2024) N. Jain, K. Han, A. Gu, W. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica Livecodebench: holistic and contamination free evaluation of large language models for code . arXiv:2403.07974 . Cited by: 3rd item .

Joshi et al. (2017) M. Joshi, E. Choi, D. S. Weld, and L. Zettlemoyer Triviaqa: a large scale distantly supervised challenge dataset for reading comprehension . arXiv:1705.03551 . Cited by: 1st item .

Kazemi et al. (2025) M. Kazemi, B. Fatemi, H. Bansal, J. Palowitch, C. Anastasiou, S. V. Mehta, L. K. Jain, V. Aglietti, D. Jindal, Y. P. Chen, et al. Big-bench extra hard . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 26473–26501 . Cited by: 2nd item .

Keshigeyan et al. (2025) C. Keshigeyan, T. Armin, and others at Radical Numerics Training diffusion language models at scale using autoregressive models . Note: https://github.com/RadicalNumerics/RND1 Cited by: §2.2 .

Li et al. (2023a) H. Li, Y. Zhang, F. Koto, Y. Yang, H. Zhao, Y. Gong, N. Duan, and T. Baldwin CMMLU: Measuring Massive Multitask Language Understanding in Chinese . arXiv:2306.09212 . Cited by: 1st item .

Li et al. (2023b) J. Li, B. Hui, G. Qu, J. Yang, B. Li, B. Li, B. Wang, B. Qin, R. Geng, N. Huo, et al. Can llm already serve as a database interface? a big bench for large-scale database grounded text-to-sqls . Advances in Neural Information Processing Systems 36 , pp. 42330–42357 . Cited by: 3rd item .

Li et al. (2024) Q. Li, L. Cui, X. Zhao, L. Kong, and W. Bi Gsm-plus: a comprehensive benchmark for evaluating the robustness of llms as mathematical problem solvers . arXiv:2402.19255 . Cited by: 4th item .

Li et al. (2025) S. Li, K. Kallidromitis, H. Bansal, A. Gokul, Y. Kato, K. Kozuka, J. Kuen, Z. Lin, K. Chang, and A. Grover LaViDa: A Large Diffusion Language Model for Multimodal Understanding . arXiv . Note: arXiv:2505.16839 Cited by: §5.1 .

Lin et al. (2025) B. Y. Lin, R. L. Bras, K. Richardson, A. Sabharwal, R. Poovendran, P. Clark, and Y. Choi Zebralogic: on the scaling limits of llms for logical reasoning . arXiv:2502.01100 . Cited by: 2nd item .

Ling et al. (2025) T. Ling, A. Li, B. Liu, B. Hu, B. Li, B. Zeng, B. Ye, C. Tang, C. Tian, C. Huang, C. Zhang, et al. Every activation boosted: scaling general reasoner to 1 trillion open language foundation . arXiv:2510.22115 . Cited by: §2.1 , §4.1 .

Liu et al. (2024) A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, et al. DeepSeek-V3 Technical Report . arXiv:2412.19437 . Cited by: §2.1 .

Liu et al. (2023) J. Liu, C. S. Xia, Y. Wang, and L. Zhang Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation . Advances in Neural Information Processing Systems 36 , pp. 21558–21572 . Cited by: 3rd item .

Liu et al. (2025) J. Liu, X. Dong, Z. Ye, R. Mehta, Y. Fu, V. Singh, J. Kautz, C. Zhang, and P. Molchanov TiDAR: Think in Diffusion, Talk in Autoregression . arXiv . Note: arXiv:2511.08923 Cited by: §2.3 .

Ma et al. (2024) K. Ma, X. Du, Y. Wang, H. Zhang, Z. Wen, X. Qu, J. Yang, J. Liu, M. Liu, X. Yue, et al. Kor-bench: benchmarking language models on knowledge-orthogonal reasoning tasks . arXiv:2410.06526 . Cited by: 2nd item .

Ma et al. (2025a) Q. Ma, Y. Zheng, Z. Shi, Z. Zhao, B. Jia, Z. Huang, Z. Lin, Y. Li, J. Yang, Y. Peng, et al. VeOmni: scaling any modality model training with model-centric distributed recipe zoo . arXiv:2508.02317 . Cited by: §7.2 .

Ma et al. (2025b) Y. Ma, L. Du, L. Wei, K. Chen, Q. Xu, K. Wang, G. Feng, G. Lu, L. Liu, X. Q. X. Zhang, et al. DInfer: an efficient inference framework for diffusion language models . arXiv:2510.08666 . Cited by: §7.3 .

Meta-AI (2025) Meta-AI The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation . External Links: Link Cited by: §2.1 .

Moonshot (2025) Moonshot Kimi K2 . Note: https://github.com/MoonshotAI/Kimi-K2/ Cited by: §2.1 .

Muennighoff et al. (2023) N. Muennighoff, Q. Liu, A. Zebaze, Q. Zheng, B. Hui, T. Y. Zhuo, S. Singh, X. Tang, L. Von Werra, and S. Longpre Octopack: instruction tuning code large language models . In NeurIPS 2023 workshop on instruction tuning and instruction following , Cited by: 3rd item .

Ni et al. (2025) J. Ni, Q. Liu, C. Du, L. Dou, H. Yan, Z. Wang, T. Pang, and M. Q. Shieh Training optimal large diffusion language models . arXiv:2510.03280 . Cited by: §2.1 .

Ni and team (2025) J. Ni and team OpenMoE 2: sparse diffusion language models . Note: https://jinjieni.notion.site/OpenMoE-2-Sparse-Diffusion-Language-Models-277d8f03a8668065a4ecd23f23bd6aac Notion Blog Cited by: §2.1 .

Nie et al. (2025) S. Nie, F. Zhu, Z. You, X. Zhang, J. Ou, J. Hu, J. Zhou, Y. Lin, J. Wen, and C. Li Large language diffusion models . External Links: 2502.09992 Cited by: §2.1 , §2.1 .

Patil et al. (2025) S. G. Patil, H. Mao, C. Cheng-Jie Ji, F. Yan, V. Suresh, I. Stoica, and J. E. Gonzalez The berkeley function calling leaderboard (bfcl): from tool use to agentic evaluation of large language models . In Forty-second International Conference on Machine Learning , Cited by: 5th item .

Qiu et al. (2025) S. Qiu, S. Guo, Z. Song, Y. Sun, Z. Cai, J. Wei, T. Luo, Y. Yin, H. Zhang, Y. Hu, et al. Phybench: holistic evaluation of physical perception and reasoning in large language models . arXiv:2504.16074 . Cited by: 1st item .

Rajpurkar et al. (2018) P. Rajpurkar, R. Jia, and P. Liang Know what you don’t know: unanswerable questions for squad . arXiv:1806.03822 . Cited by: 2nd item .

Rein et al. (2024) D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman GPQA: A Graduate-Level Google-Proof Q&Q Benchmark . In First Conference on Language Modeling , Cited by: 1st item .

Roggeveen et al. (2025) J. V. Roggeveen, E. Y. Wang, W. Flintoft, P. Donets, L. S. Nathwani, N. Gutierrez, D. Ettel, A. M. Graf, S. Dandavate, A. Nageswaran, et al. HARDMath2: a benchmark for applied mathematics built by students as part of a graduate class . arXiv:2505.11774 . Cited by: 4th item .

Saparov and He (2022) A. Saparov and H. He Language models are greedy reasoners: a systematic formal analysis of chain-of-thought . arXiv:2210.01240 . Cited by: 2nd item .

Shoeybi et al. (2019) M. Shoeybi, M. Patwary, R. Puri, P. LeGresley, J. Casper, and B. Catanzaro Megatron-lm: training multi-billion parameter language models using model parallelism . arXiv:1909.08053 . Cited by: §7.1 .

Song et al. (2025) Y. Song, Z. Zhang, C. Luo, P. Gao, F. Xia, H. Luo, Z. Li, Y. Yang, H. Yu, X. Qu, Y. Fu, J. Su, G. Zhang, W. Huang, M. Wang, L. Yan, X. Jia, J. Liu, W. Ma, Y. Zhang, Y. Wu, and H. Zhou Seed diffusion: a large-scale diffusion language model with high-speed inference . External Links: 2508.02193 Cited by: §2.1 , §2.3 .

Sprague et al. (2023) Z. Sprague, X. Ye, K. Bostrom, S. Chaudhuri, and G. Durrett Musr: testing the limits of chain-of-thought with multistep soft reasoning . arXiv:2310.16049 . Cited by: 2nd item .

Suzgun et al. (2023) M. Suzgun, N. Scales, N. Schärli, S. Gehrmann, Y. Tay, H. W. Chung, A. Chowdhery, Q. Le, E. Chi, D. Zhou, et al. Challenging big-bench tasks and whether chain-of-thought can solve them . In Findings of the Association for Computational Linguistics: ACL 2023 , pp. 13003–13051 . Cited by: 2nd item .

team (2023a) A. team Aider-ai/aider . External Links: Link Cited by: 3rd item .

team (2023b) N. team NexusRaven-v2: surpassing gpt-4 for zero-shot function calling . External Links: Link Cited by: 5th item .

team (2023c) O. team Open-compass/opencompass . External Links: Link Cited by: 2nd item , 3rd item .

Tian et al. (2025) C. Tian, J. Wang, Q. Zhao, K. Chen, J. Liu, Z. Liu, J. Mao, W. X. Zhao, Z. Zhang, and J. Zhou WSM: decay-free learning rate schedule via checkpoint merging for llm pre-training . arXiv:2507.17634 . Cited by: §4.3 , §4 .

Wang et al. (2025a) C. Wang, P. Rashidinejad, D. Su, S. Jiang, S. Wang, S. Zhao, C. Zhou, S. Z. Shen, F. Chen, T. Jaakkola, Y. Tian, and B. Liu SPG: sandwiched policy gradient for masked diffusion language models . arXiv:2510.09541 . Cited by: §2.3 .

Wang et al. (2025b) P. Wang, L. Zhang, F. Liu, L. Shi, M. Li, B. Shen, and A. Fu Codeif-bench: evaluating instruction-following capabilities of large language models in interactive code generation . arXiv:2503.22688 . Cited by: 5th item .

Wang et al. (2023) X. Wang, Z. Hu, P. Lu, Y. Zhu, J. Zhang, S. Subramaniam, A. R. Loomba, S. Zhang, Y. Sun, and W. Wang Scibench: evaluating college-level scientific problem-solving abilities of large language models . arXiv:2307.10635 . Cited by: 1st item .

Wang et al. (2025c) X. Wang, C. Xu, Y. Jin, J. Jin, H. Zhang, and Z. Deng Diffusion LLMs Can Do Faster-Than-AR Inference via Discrete Diffusion Forcing . arXiv . Note: arXiv:2508.09192 Cited by: §2.3 .

Wang et al. (2025d) Y. Wang, L. Yang, B. Li, Y. Tian, K. Shen, and M. Wang Revolutionizing reinforcement learning framework for diffusion large language models . arXiv:2509.06949 . Cited by: §2.3 .

Wang et al. (2024) Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, et al. MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark . In The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track , Cited by: 1st item .

Wei et al. (2023) T. Wei, J. Luan, W. Liu, S. Dong, and B. Wang Cmath: can your language model pass chinese elementary school math test? . arXiv:2306.16636 . Cited by: 4th item .

Xie et al. (2025) Z. Xie, J. Ye, L. Zheng, J. Gao, J. Dong, Z. Wu, X. Zhao, S. Gong, X. Jiang, Z. Li, and L. Kong Dream-Coder 7B: An Open Diffusion Language Model for Code . arXiv . Note: arXiv:2509.01142 Cited by: §2.3 , §4.2 .

Yang et al. (2025) A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. Qwen3 Technical Report . arXiv:2505.09388 . Cited by: §1 , §2.2 .

Ye et al. (2025) J. Ye, Z. Xie, L. Zheng, J. Gao, Z. Wu, X. Jiang, Z. Li, and L. Kong Dream 7b: diffusion large language models . arXiv:2508.15487 . Cited by: §2.1 , §2.2 , §2.3 , §4.2 .

Yu et al. (2025) R. Yu, Q. Li, and X. Wang Discrete Diffusion in Large Language and Multimodal Models: A Survey . arXiv . Note: arXiv:2506.13759 Cited by: §1 .

Yu et al. (2018) T. Yu, R. Zhang, K. Yang, M. Yasunaga, D. Wang, Z. Li, J. Ma, I. Li, Q. Yao, S. Roman, et al. Spider: a large-scale human-labeled dataset for complex and cross-domain semantic parsing and text-to-sql task . arXiv:1809.08887 . Cited by: 3rd item .

Zellers et al. (2019) R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi Hellaswag: can a machine really finish your sentence? . arXiv:1905.07830 . Cited by: 2nd item .

Zhang et al. (2023) X. Zhang, C. Li, Y. Zong, Z. Ying, L. He, and X. Qiu Evaluating the performance of large language models on gaokao benchmark . arXiv:2305.12474 . Cited by: 1st item .

Zheng et al. (2024) L. Zheng, L. Yin, Z. Xie, C. Sun, J. Huang, C. H. Yu, S. Cao, C. Kozyrakis, I. Stoica, J. E. Gonzalez, C. Barrett, and Y. Sheng SGLang: efficient execution of structured language model programs . External Links: 2312.07104 Cited by: §7.3 .

Zhou et al. (2023) J. Zhou, T. Lu, S. Mishra, S. Brahma, S. Basu, Y. Luan, D. Zhou, and L. Hou Instruction-Following Evaluation for Large Language Models . arXiv:2311.07911 . Cited by: 5th item .

Zhu et al. (2025) F. Zhu, Z. You, Y. Xing, Z. Huang, L. Liu, Y. Zhuang, G. Lu, K. Wang, X. Wang, L. Wei, H. Guo, J. Hu, W. Ye, T. Chen, C. Li, C. Tang, H. Feng, J. Hu, J. Zhou, X. Zhang, Z. Lan, J. Zhao, D. Zheng, C. Li, J. Li, and J. Wen LLaDA-moe: a sparse moe diffusion language model . External Links: 2509.24389 Cited by: §2.1 .

Zhuo et al. (2024) T. Y. Zhuo, M. C. Vu, J. Chim, H. Hu, W. Yu, R. Widyasari, I. N. B. Yusuf, H. Zhan, J. He, I. Paul, et al. Bigcodebench: benchmarking code generation with diverse function calls and complex instructions . arXiv:2406.15877 . Cited by: 3rd item .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
