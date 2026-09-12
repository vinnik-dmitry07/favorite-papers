##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Beyond Scattered Acceptance : Fast and Coherent Inference for DLMs via Longest Stable Prefixes

###### Abstract

Diffusion Language Models (DLMs) promise highly parallel text generation, yet their practical inference speed is often bottlenecked by suboptimal decoding schedulers. Standard approaches rely on “scattered acceptance”—committing high-confidence tokens at disjoint positions throughout the sequence. This approach inadvertently fractures the Key-Value (KV) cache, destroys memory locality, and forces the model into costly, repeated repairs across unstable token boundaries. To resolve this, we present the Longest Stable Prefix (LSP) scheduler, a training-free and model-agnostic inference paradigm based on monolithic prefix absorption . In each denoising step, LSP evaluates token stability via a single forward pass, dynamically identifies a contiguous left-aligned block of stable predictions, and snaps its boundary to natural linguistic or structural delimiters before an atomic commitment. This prefix-first topology yields dual benefits: systemically, it converts fragmented KV cache updates into efficient, contiguous appends; algorithmically, it preserves bidirectional lookahead over a geometrically shrinking active suffix, drastically reducing token flip rates and denoiser calls. Extensive evaluations on LLaDA-8B and Dream-7B demonstrate that LSP accelerates inference by up to 3.4 × \times across rigorous benchmarks—including mathematical reasoning, code generation, multilingual (CJK) tasks, and creative writing—while matching or slightly improving output quality. By fundamentally restructuring the commitment topology, LSP bridges the gap between the theoretical parallelism of DLMs and practical hardware efficiency.

## 1 Introduction

Diffusion Language Models (DLMs) have emerged as a compelling alternative to autoregressive generation, offering an intrinsically parallel inference process that leverages bidirectional context ( Austin et al., 2021a ) . This paradigm holds the promise of significant latency reductions over traditional one-token-at-a-time decoding. However, this promise remains largely unfulfilled in practice. The iterative refinement process, central to DLM generation, is frequently bottlenecked not by the model’s architecture, but by the strategy used to commit intermediate predictions. This creates a stark paradox: models designed for parallelism are often constrained by the sequential nature of their own convergence.

At the heart of this inefficiency lies the prevalent strategy of scattered acceptance , where tokens are committed independently based on local confidence ( Nie et al., 2025 ) or in fixed-size, semi-autoregressive blocks ( Arriola et al., 2025 ) . This approach is fundamentally costly in two distinct ways. First, from an algorithmic perspective , it creates a fragmented sequence of frozen and mutable tokens. The numerous boundaries between these regions are unstable, requiring repeated, localized repairs that slow the convergence to a globally coherent output. Second, from a systems perspective , this fragmentation shatters the Key-Value (KV) cache into small, non-contiguous segments, destroying the memory locality that is critical for efficient Transformer inference. Consequently, the active (uncommitted) portion of the sequence remains long, keeping attention computationally expensive for many iterations.

In this work, we argue that overcoming this bottleneck requires a new commitment topology. We introduce the Longest Stable Prefix (LSP), a training-free, model-agnostic scheduling paradigm founded on the principle of monolithic prefix absorption . Instead of accepting scattered islands of confident tokens, LSP identifies and commits the longest contiguous, stable prefix of the remaining active sequence in a single atomic step. This is achieved through a lightweight, single-pass procedure: (1) it computes a logit margin score for each active position; (2) it adaptively selects a margin threshold to target a fractional block size (e.g., 25–50% of the active suffix); and (3) it snaps the candidate block’s boundary to a nearby structural delimiter (e.g., punctuation or a newline) before committing. A simple fallback rule guarantees progress by committing at least one token per iteration, even when the model is highly uncertain.

This prefix-first geometry fundamentally alters the computational dynamics of DLM inference. By design, the frozen prefix grows as a single, contiguous block. This maximizes KV cache reuse and ensures subsequent attention queries are focused on a rapidly shrinking active suffix. The adaptive thresholding strategy encourages the active sequence length to decay geometrically, leading to a near-quadratic total work complexity that scales gracefully with sequence length. Algorithmically, committing structurally-aligned monolithic blocks minimizes the cross-boundary conflicts inherent in scattered acceptance, reducing the number of repair cycles needed to achieve a coherent state.

Our contributions are threefold: • We identify scattered acceptance as a primary bottleneck in DLM inference and propose monolithic prefix absorption as a more efficient commitment topology. We instantiate this principle in LSP, a novel, training-free scheduler that uses a single forward pass, adaptive thresholding, and structural snapping to commit the longest stable prefix.

• We provide a computational analysis showing how LSP’s prefix-first strategy synergizes with KV caching to induce a geometric decay in the active sequence length, focusing computation on a shrinking suffix and yielding near-quadratic total work.

• Through extensive experiments on code generation and multi-step reasoning, we demonstrate that LSP significantly reduces end-to-end latency and memory traffic while matching or improving output quality compared to strong parallel baselines. Ablation studies validate the importance of each of its core design components.

## 2 Related Work

### 2.1 Diffusion Large Language Model

Early attempts to transplant diffusion ideas into discrete domains date back to Sohl-Dickstein et al. (2015) and Hoogeboom et al. (2021) . Building on these foundations, D3PM ( Austin et al., 2021a ) introduced a unifying probabilistic view in which a discrete-state Markov forward process progressively corrupts clean sequences and a parameterized reverse model is trained via an ELBO objective to reconstruct text from noisy inputs. This discrete formulation was later recast in continuous time: Campbell et al. (2022) modeled the corruption dynamics as a continuous-time Markov chain (CTMC). A complementary line of work, SEDD ( Lou et al., 2023 ) , directly estimates likelihood ratios and adopts a denoising score entropy training criterion. Recent analyses—spanning MDLM ( Shi et al., 2024 ; Sahoo et al., 2024 ; Zheng et al., 2024 ) and RADD ( Ou et al., 2024 ) —further reveal that multiple parameterizations of masked/discrete diffusion models are mathematically equivalent, clarifying relationships among prior formulations.

Motivated by these advances, practitioners have scaled diffusion-style language models into real systems. Commercial offerings include Mercury ( Labs et al., 2025 ) , Gemini Diffusion ( DeepMind, 2025 ) , and Seed Diffusion ( Song et al., 2025b ) , while LLaDA ( Nie et al., 2025 ) and Dream ( Ye et al., 2025 ) exemplify open-source counterparts. Despite this progress, DLMs still face a speed–quality tension: decoding larger token blocks per denoising step tends to hurt accuracy, whereas smaller blocks increase latency. Moreover, because attention is bidirectional, DLMs cannot straightforwardly reuse AR-style optimizations such as KV caching, leaving inference less efficient than autoregressive models in many settings.

### 2.2 Acceleration Methods for Diffusion Language Models

Efforts to accelerate DLM inference while preserving quality broadly fall into three complementary tracks. First, several methods exploit the strong similarity of hidden states across adjacent denoising steps to enable approximate caching ( Ma et al., 2025 ; Liu et al., 2025 ; Hu et al., 2025 ) . A closely related strategy restructures generation into semi-/block-autoregressive schedules so that past blocks (or contexts) can be cached and selectively refreshed during decoding ( Wu et al., 2025 ; Arriola et al., 2025 ; Song et al., 2025a ) . Second, token-pruning approaches reduce attention cost by removing positions deemed less useful; DPad ( Chen et al., 2025 ) , for instance, treats distant suffix tokens as a temporary scratchpad and prunes them before computation. Third, sampling-focused techniques aim either to increase the number of tokens accepted per step or to cut the total number of steps—sometimes via reinforcement learning ( Song et al., 2025b ) . Within this vein, the number of simultaneously decoded tokens can be governed by confidence/entropy criteria, adjusted online with denoising dynamics ( Wei et al., 2025 ; Huang and Tang, 2025 ) , dynamically tailor classifier-free guidance via low-confidence re-masking ( Li et al., 2025a ) , or be aligned with small auxiliary AR models ( Israel et al., 2025 ) , or paired with speculative decoding that drafts using the DLM itself ( Agrawal et al., 2025 ) .

Our work departs from these optimization routes by capitalizing on an empirical property of DLMs: the correct final answer often appears at intermediate steps. We leverage this early answer convergence to perform training-free early commitments that reduce computation without sacrificing quality. Concurrently, MidTruth ( Wang et al., 2025 ) also identifies early convergence but pursues temporal ensembling across steps to boost accuracy, whereas we develop an early-commit decoding scheme that shortens inference while maintaining performance. Closely related to our acceleration objective is Prophet ( Li et al., 2025b ) , which similarly introduces an early-commit decoding paradigm, albeit driven specifically by top-2 confidence gaps.

## 3 Method

In this section, we detail our proposed approach for accelerating Diffusion Language Model (DLM) inference. We begin by formalizing the standard discrete diffusion framework and pinpointing the inherent inefficiencies of conventional scheduling strategies. We then introduce the Longest Stable Prefix (LSP) scheduler, a training-free, model-agnostic paradigm designed to overcome these limitations. We break down its core components: a stability diagnostic, an adaptive sizing mechanism, and a structural boundary snapping procedure, explaining how they synergize to enable fast and coherent generation.

### 3.1 Preliminary

Our work is situated within the established framework of discrete diffusion models for language, which have demonstrated remarkable scalability and generation quality ( Austin et al., 2021a ; Nie et al., 2025 ) . We briefly formalize this process to establish context for our contributions.

##### Forward Corruption Process.

The process begins with a clean text sequence 𝐱 0 = ( x 0 1 , … , x 0 L ) \mathbf{x}_{0}=(x_{0}^{1},\dots,x_{0}^{L}) of length L L , sampled from the data distribution p data p_{\text{data}} . A forward Markov process gradually corrupts this sequence over a series of discrete timesteps t ∈ { 1 , … , T } t\in\{1,\dots,T\} . At each step t t , a subset of tokens in the sequence 𝐱 t − 1 \mathbf{x}_{t-1} is replaced by a special ‘[MASK]‘ token to produce a noisier sequence 𝐱 t \mathbf{x}_{t} . The transition probability, q ⁡ ( 𝐱 t | 𝐱 t − 1 ) q(\mathbf{x}_{t}|\mathbf{x}_{t-1}) , is designed such that the degree of masking increases monotonically with t t . By the final step, the sequence 𝐱 T \mathbf{x}_{T} is composed entirely of ‘[MASK]‘ tokens. A key property of this process is that the state at any intermediate step t t can be sampled directly from the original sequence via q ⁡ ( 𝐱 t | 𝐱 0 ) q(\mathbf{x}_{t}|\mathbf{x}_{0}) , which models the probability that each token in 𝐱 0 \mathbf{x}_{0} has been absorbed into the ‘[MASK]‘ state after t t steps. This property is crucial for formulating a tractable training objective.

##### Reverse Generation Process.

The goal of a DLM, parameterized by θ \theta , is to learn the reverse of this corruption process. Given a noisy sequence 𝐱 t \mathbf{x}_{t} , the model is trained to predict the original clean sequence 𝐱 0 \mathbf{x}_{0} by optimizing a loss function based on the negative log-likelihood of the ground-truth tokens, thereby learning the conditional distribution p θ ​ ( 𝐱 0 | 𝐱 t ) p_{\theta}(\mathbf{x}_{0}|\mathbf{x}_{t}) .

Sequence generation, or sampling, is an iterative procedure that inverts the forward process, starting from a fully masked sequence 𝐱 T \mathbf{x}_{T} . For each timestep t t from T T down to 1, a two-stage refinement is performed. First, in a prediction step , the model p θ p_{\theta} is called to predict the entire clean sequence from the current noisy state: 𝐱 ^ 0 ∼ p θ ( ⋅ | 𝐱 t ) \hat{\mathbf{x}}_{0}\sim p_{\theta}(\cdot|\mathbf{x}_{t}) . Second, in a re-masking step , a new, less noisy state 𝐱 t − 1 \mathbf{x}_{t-1} is constructed by combining information from the current state 𝐱 t \mathbf{x}_{t} and the prediction 𝐱 ^ 0 \hat{\mathbf{x}}_{0} .

##### The Inefficiency of Conventional Schedulers.

The critical decision in the re-masking step lies with the scheduling strategy , which determines which tokens from the prediction 𝐱 ^ 0 \hat{\mathbf{x}}_{0} are accepted (or "committed") and which positions are re-masked for further refinement. Most existing schedulers operate on a principle of scattered acceptance: they identify and commit tokens independently based on local confidence scores (e.g., high probability or low entropy). This approach, while intuitive, introduces profound inefficiencies. Algorithmically, it creates a fragmented sequence of frozen (committed) and active (mutable) tokens. The numerous, unstable boundaries between these regions require the model to perform repeated, localized repairs, slowing global convergence. Systemically, this fragmentation shatters the Key-Value (KV) cache into small, non-contiguous segments. This destroys the memory locality essential for efficient Transformer inference, forcing re-computation and keeping the computationally expensive attention mechanism operating over a long, fragmented active sequence for many iterations. This fundamental bottleneck motivates a new commitment topology.

### 3.2 The Longest Stable Prefix (LSP) Scheduler

To address the aforementioned bottleneck, we introduce the Longest Stable Prefix (LSP) scheduler, a disciplined strategy of monolithic prefix absorption . Instead of accepting scattered islands of confident tokens, LSP’s core principle is to identify and commit the longest possible contiguous and stable block from the left of the active sequence in a single, atomic operation. This prefix-first topology is designed explicitly to maximize KV cache coherence, promote global text structure, and accelerate convergence.

At any generation iteration k k , we partition the full sequence into two parts: a frozen prefix X F ( k ) X_{F}^{(k)} , which is cached and immutable, and an active suffix X A ( k ) X_{A}^{(k)} of length N k N_{k} , which is the target of the current refinement step. LSP then executes a lightweight, three-stage procedure using just a single forward pass of the DLM.

##### Single-Pass Prediction and Stability Assessment.

The process begins with a single forward pass of the model p θ p_{\theta} on the current composite state ( X F ( k ) , X A ( k ) ) (X_{F}^{(k)},X_{A}^{(k)}) . This pass yields logits for all N k N_{k} positions in the active suffix. From these logits, we compute a stability diagnostic for each position i ∈ { 1 , … , N k } i\in\{1,\dots,N_{k}\} . We use the logit margin , defined as the difference between the top-two logit values: δ i ≜ z ( 1 ) ​ ( i ) − z ( 2 ) ​ ( i ) . \delta_{i}\triangleq z_{(1)}(i)-z_{(2)}(i). (1) The margin serves as a simple yet effective low-cost proxy for the model’s local decisiveness. A large margin indicates that the model has high confidence in its top prediction for token i i relative to all alternatives, suggesting this token is stable and unlikely to change in subsequent refinement steps. Conversely, a small margin signals ambiguity and a higher potential for future revision.

##### Distinction from Blockwise Autoregressive Decoding.

A crucial distinction must be made between LSP and standard Blockwise Autoregressive (AR) decoding. In Blockwise AR, a block is generated greedily and frozen; the model never observes “future” tokens during that block’s generation. In contrast, LSP preserves the fundamental advantage of DLMs: bidirectional lookahead . During every diffusion step, the model performs a forward pass on the composite state ( X F ( k ) , X A ( k ) ) (X_{F}^{(k)},X_{A}^{(k)}) . The active suffix X A ( k ) X_{A}^{(k)} acts as a noisy, bidirectional lookahead buffer. This allows the model to refine the tokens in the candidate block based on the global context of the future sequence, resolving narrative and logical dependencies before the prefix is committed.

##### Approximate KV Caching for Prefix States.

In a strict bidirectional model, the internal representations (KV pairs) of the prefix tokens theoretically depend on the active suffix tokens. Recomputing the entire sequence at every step, however, defeats the purpose of caching. LSP employs an approximate KV caching strategy, treating the committed prefix as fixed context. This is supported by recent findings in diffusion acceleration ( Wu et al., 2025 ) , which demonstrate that KV activations exhibit high similarity across adjacent inference steps, and reusing cached KVs for stable tokens results in a negligible performance drop while unlocking massive systemic speedups.

##### Targeted Block Sizing via Adaptive Thresholding.

Using a fixed stability threshold to accept tokens is brittle; a threshold that is aggressive for one model or task may be too conservative for another. LSP therefore employs an adaptive strategy to dynamically determine the commitment block size. The goal is to ensure that the active sequence length N k N_{k} decays at a steady, geometric rate, which is the key to achieving a near-quadratic total work complexity.

To achieve this, we define L ′ ​ ( τ ) L^{\prime}(\tau) as the length of the longest consecutive run of positions, starting from the beginning of the active suffix, whose logit margins all exceed a given threshold τ \tau . Instead of fixing τ \tau , LSP efficiently searches for a threshold τ k \tau_{k} such that the resulting block length L ′ ​ ( τ k ) L^{\prime}(\tau_{k}) falls within a target fractional range of the current active sequence length: L ′ ​ ( τ k ) ∈ [ α ​ N k , β ​ N k ] , L^{\prime}(\tau_{k})\in[\alpha N_{k},\;\beta N_{k}], (2) where 0 < α ≤ β ≤ 1 0<\alpha\leq\beta\leq 1 are user-specified fractions (e.g., α = 0.25 , β = 0.50 \alpha=0.25,\beta=0.50 ). The parameter α \alpha prevents overly cautious steps that would slow down convergence, while β \beta prevents overly aggressive commitments that might introduce errors. This search can be implemented efficiently in O ⁡ ( N k ) O(N_{k}) time by first computing the prefix-minimum of the margin scores and then selecting a target length m ∈ [ ⌈ α ​ N k ⌉ , ⌊ β ​ N k ⌋ ] m\in[\lceil\alpha N_{k}\rceil,\lfloor\beta N_{k}\rfloor] that satisfies the condition. This adaptive sizing allows LSP to be aggressive when the model is confident and conservative when it is uncertain, ensuring robust and rapid progress.

##### Structural Coherence via Boundary Snapping and Monotone Progress.

Committing a block of tokens that ends mid-word or mid-sentence creates an unnatural and incoherent context for the subsequent generation step, potentially requiring costly repairs. To enhance global coherence, LSP trims the candidate block of length L ′ ​ ( τ k ) L^{\prime}(\tau_{k}) to a more natural structural boundary. Specifically, we snap the block’s right-hand boundary to the last occurring structural delimiter (e.g., punctuation, newline, or code-specific symbols) found within the candidate block.

Let 𝒟 \mathcal{D} be a set of such delimiters, L min ≥ 1 L_{\min}\geq 1 be a minimum guaranteed block size, and W ≥ 0 W\geq 0 be a lookback window. The final commitment length L L is determined as: L ≜ max ⁡ { L min , max ⁡ { j ≤ L ′ : y ^ j ∈ 𝒟 ∧ L ′ − j ≤ W } } . L\triangleq\max\Big\{L_{\min},\;\max\{j\leq L^{\prime}\;:\;\hat{y}_{j}\in\mathcal{D}\wedge L^{\prime}-j\leq W\}\Big\}. This snapping mechanism intelligently trades a few tokens of immediate progress for significantly improved downstream coherence, reducing the need for future revisions. To guarantee termination, if no suitable delimiters are found and the candidate block is shorter than L min L_{\min} , a fallback rule ensures that at least one token is committed ( L ← 1 L\leftarrow 1 ). This guarantees that the frozen prefix X F X_{F} grows monotonically in every iteration.

The complete, integrated procedure is detailed in Algorithm 1 . By design, each step contributes to a virtuous cycle: monolithic prefix absorption preserves KV cache contiguity, which enables efficient attention. Adaptive sizing ensures rapid, geometric decay of the active sequence, focusing computation where it’s most needed. Finally, structural snapping produces coherent intermediate states, leading to faster global convergence with fewer repair cycles.

## 4 Experiments

### 4.1 Experimental Setup

##### Models and Benchmarks.

Our empirical evaluation is conducted on two prominent open-source Diffusion Language Models, LLaDA-8B ( Nie et al., 2025 ) and Dream-7B ( Ye et al., 2025 ) , to demonstrate the general applicability of our scheduling approach. We select a focused but challenging set of benchmarks where the generation of coherent, long-form text with strong internal dependencies is paramount. For assessing performance on mathematical reasoning , we use GSM8K ( Cobbe et al., 2021 ) , a dataset of grade-school math word problems where correctness depends on a valid chain of thought. Performance is measured by exact match accuracy of the final answer. For code generation , a domain that demands strict syntactic and logical correctness, we employ the widely-used HumanEval ( Chen et al., 2021 ) and MBPP ( Austin et al., 2021b ) benchmarks. Success on these tasks is measured by the pass@1 metric, which evaluates whether the generated code passes a set of unit tests. To ensure deterministic and reproducible results, all experiments utilize a zero-shot prompting setup and employ greedy decoding.

##### Baseline and LSP Configuration.

We benchmark LSP’s performance against the most fundamental and widely-used decoding strategy, which we term Full decoding. This baseline represents the standard iterative refinement process of a DLM, using the complete step budget available ( T max = L T_{\max}=L , where L L is the generation length). The ‘Full‘ baseline serves as the reference for generation quality and provides the 1.0 × 1.0\times anchor for our speedup calculations. This direct comparison allows us to cleanly isolate the efficiency gains attributable solely to the LSP scheduling strategy, without confounding factors from other acceleration techniques. For LSP itself, we maintain a consistent set of hyperparameters across all models and tasks to showcase its robustness and ease of use. The fractional acceptance interval is set to [ α , β ] = [ 0.25 , 0.50 ] [\alpha,\beta]=[0.25,0.50] , encouraging a steady, geometric decay of the active suffix. We use a minimal block length of L min = 1 L_{\min}=1 to guarantee progress and a structural snapping window of W = 16 W=16 tokens, a modest value chosen to balance coherence with aggressive commitment. These parameters were determined from a brief, one-time validation sweep on a small subset of the GSM8K dataset.

### 4.2 Main Results and Analysis

Table 1 presents the main results of our evaluation. The findings clearly show that LSP provides a massive acceleration in inference speed—up to 3.4 × \times —while preserving the high generation quality of the full-budget baseline. In some cases, LSP even slightly improves performance, demonstrating its effectiveness as a robust and efficient decoding scheduler. On the GSM8K mathematical reasoning task, LSP achieves a 1.5 × \times speedup with LLaDA-8B while also delivering a marginal improvement in accuracy (+0.5%). This suggests that by committing a stable prefix of the reasoning chain early, LSP can prevent noisy, late-stage refinement steps from corrupting an already correct solution.

The benefits of monolithic prefix absorption are particularly evident in code generation, where structural integrity is paramount. On HumanEval, LSP accelerates inference by 1.2 × \times with a negligible impact on the success rate. This confirms that the prefix-first topology, augmented by structural snapping, is highly effective at generating coherent, syntactically valid code blocks more efficiently than iterative, full-sequence refinement. The results on Dream-7B show a similar trend, with even more substantial speedups, underscoring the general applicability of the LSP scheduling principle across different model architectures.

##### Global Planning in Creative Writing.

Unlike reasoning tasks that are highly sequential, creative writing stresses a model’s ability to perform global planning. We evaluated LSP on a subset of the WritingPrompts dataset ( N = 500 N=500 ). Using Gemini 2.5 Flash as an impartial judge on a 1-5 scale, LSP achieved a Coherence score of 4.38 and Creativity score of 4.31 (vs. Full Decoding’s 4.42 and 4.35), while being 1.82 × \times faster. The statistically indistinguishable coherence scores validate that LSP’s bidirectional lookahead buffer successfully resolves long-term narrative dependencies before the prefix is committed.

### 4.3 Ablation Studies and Analysis

To rigorously dissect the contributions of LSP’s core components, we conduct a series of ablation studies on the challenging GSM8K benchmark using the LLaDA-8B model. These experiments are designed to isolate the impact of each design choice—adaptive sizing, structural snapping, and the prefix-first topology—to validate that our method’s remarkable effectiveness stems from a principled, synergistic design rather than any single factor.

#### 4.3.1 The Critical Role of Adaptive Sizing

##### Motivation.

A core hypothesis of our work is that a model’s confidence is not uniform throughout the generation process. A rigid, fixed-size commitment strategy is therefore inherently suboptimal. Such a strategy is blind to the model’s internal state: it will be either too conservative during high-confidence phases (leading to an excessive number of refinement steps) or too aggressive during uncertain phases (introducing errors that degrade quality). Our adaptive sizing mechanism is designed to navigate this dynamic landscape intelligently.

##### Analysis.

To test this hypothesis, we compare the standard adaptive LSP against variants that commit a fixed-size prefix at each step, ranging from a cautious one token to an aggressive 8. As demonstrated in Table 2 , the fixed-size strategies are brittle, exposing a sharp trade-off between efficiency and accuracy.

Committing a minimal prefix (1 or 2 tokens) is an overly conservative approach. While it preserves high accuracy by taking cautious, small steps, it requires a large number of iterations to complete the sequence, resulting in low efficiency. Conversely, committing a large fixed block (8 tokens) is overly aggressive. It drastically reduces the number of steps, making it very fast, but does so by prematurely committing unstable, low-margin tokens, leading to a significant drop in final accuracy. The 2-token strategy offers a reasonable, but still suboptimal, compromise.

LSP’s adaptive approach elegantly resolves this dilemma. By adjusting the commitment length based on the model’s real-time confidence, it significantly reduces the average number of steps compared to conservative strategies while maintaining the highest generation quality. It successfully balances aggressive commitment in confident regions with cautious refinement in uncertain ones, achieving the best overall performance.

#### 4.3.2 Enhancing Coherence with Structural Snapping

##### Motivation.

Raw token-level stability is not sufficient for generating coherent, long-form text. The semantic and syntactic integrity of the generated output is paramount. Committing a prefix that ends abruptly mid-statement, mid-expression, or even mid-word creates an unnatural and confusing context for the model’s subsequent refinement step. Structural snapping is designed to mitigate this by aligning commitment boundaries with natural linguistic or code-based delimiters.

##### Analysis.

We evaluate the impact of this mechanism by disabling it, which results in a greedier strategy that always commits the full candidate block L ′ L^{\prime} identified by adaptive sizing. The results in Table 3 are unambiguous. The version without snapping is slightly faster, requiring fewer total steps on average, because it commits more tokens per iteration. However, this aggressive approach comes at a significant cost to quality, with a noticeable drop in the final score. The reason is that committing incoherent prefixes (e.g., ‘the final answer is 3.141‘) pollutes the context for subsequent denoising steps. This forces the model to expend its capacity on correcting these unnatural boundaries rather than generating new, coherent content, ultimately leading to more errors. The small efficiency cost of snapping (a slightly higher step count) is overwhelmingly justified by the substantial gain in generation quality. This confirms that structural snapping is a crucial component for maintaining high-quality, coherent output within the LSP framework.

##### Qualitative Evidence.

To complement the aggregate ablation results, we provide a granular visualization of LSP on GSM8K in Table 4 . Each iteration commits the Longest Stable Prefix as a contiguous block, and the resulting commit boundaries consistently snap to natural reasoning units (e.g., clauses and arithmetic expressions) rather than arbitrary token positions. This behavior illustrates why structural snapping is critical: it prevents the model from freezing an incoherent partial phrase that would otherwise pollute the context for subsequent denoising, thereby reducing downstream repair and improving final correctness.

#### 4.3.3 Prefix-First vs. Scattered: The Power of Topology

##### Motivation.

Finally, we directly test our central thesis: that the topology of commitment is a primary driver of efficiency in DLM inference. We construct a strong baseline, "Scattered-Margin," which uses LSP’s margin-based adaptive sizing to determine how many tokens to commit, but then accepts the most confident tokens from anywhere in the active sequence, following the conventional scattered acceptance paradigm. This isolates the effect of a contiguous prefix-first topology from the token selection criteria.

##### Analysis.

Table 3 provides direct and compelling evidence for the superiority of the prefix-first topology. This performance gap stems from two synergistic sources of inefficiency.

Algorithmic Instability: The scattered approach creates numerous unstable "holes" and internal boundaries between frozen and masked tokens. This forces the diffusion model to reconcile disparate, non-local contexts in every step, leading to slower and less stable convergence. This is reflected in the significantly higher average number of steps required to complete generation. In contrast, LSP’s prefix-first topology maintains a single, clean boundary, allowing the model to focus its capacity on coherently extending a stable prefix.

Systemic Inefficiency: The performance difference is magnified at the hardware level. With a prefix-first topology, the Key-Value (KV) cache for the frozen prefix is contiguous in memory. It can be computed once and efficiently reused, with new states being appended in a simple, fast operation. A scattered topology, however, completely fragments the KV cache. This destroys memory locality, forcing the attention mechanism into costly gather operations or recomputations, which negates the parallel prediction benefit of the DLM architecture.

The Scattered-Margin baseline is thus both algorithmically and systemically inferior. Our results confirm that monolithic prefix absorption is the key to turning the parallel prediction power of DLMs into fast and effective generation on modern hardware.

#### 4.3.4 Quantifying Repair Costs via Token Flip Rate

A potential concern with early commitment is that freezing a prefix might restrict the model’s ability to correct early mistakes, thereby increasing the “repair cost” in the active suffix. To investigate this, we measure the Flip Rate —the percentage of tokens in the active suffix that change their top-1 prediction between consecutive diffusion steps. During the mid-stage of generation (25%–75% completion), the standard Scattered baseline exhibits a high Flip Rate of 14.2%, as the model constantly oscillates to reconcile a fragmented context. In contrast, under LSP, the Flip Rate in the remaining suffix plummets to just 4.3% . This empirical evidence proves that resolving and freezing a coherent prefix actually stabilizes the future generation context, drastically reducing the required repair operations rather than increasing them.

## 5 Conclusion

In this work, we identified scattered token acceptance as a primary algorithmic and systemic bottleneck that throttles the practical inference speed of Diffusion Language Models. To address this, we introduced the Longest Stable Prefix (LSP) scheduler, a training-free, model-agnostic inference principle centered on monolithic prefix absorption . By atomically committing the longest contiguous and stable block of tokens in each iteration, LSP fundamentally improves the generation topology. Our empirical results demonstrate that LSP substantially accelerates inference across diverse models and challenging benchmarks, such as code generation and mathematical reasoning, while preserving or even slightly improving task performance. This work validates that a principled commitment strategy is key to unlocking the parallel generation promise of DLMs, bridging the gap between their theoretical potential and practical efficiency. While our experiments validate the effectiveness of LSP on prominent open-source DLMs, the current implementation relies on a simple yet effective logit margin as a stability proxy; future work could investigate more sophisticated, temporally-aware stability metrics that might offer a better trade-off between commitment aggression and accuracy. Furthermore, LSP is designed to be an orthogonal improvement to the diffusion process itself. A promising avenue for future research is to investigate its synergy with other acceleration techniques, such as speculative decoding or approximate caching methods, to potentially achieve compounding gains in inference speed. Finally, the efficacy of structural snapping was demonstrated on tasks with clear delimiters (code, reasoning steps), and its impact on more open-ended, creative generation tasks warrants further investigation.

##### Limitations

While LSP is highly effective for sequential (left-to-right) generation, its contiguous prefix assumption is not inherently suited for non-sequential tasks such as text in-filling or unconstrained editing. Extending the topological principles of LSP to support “stable islands” for bidirectional in-filling remains an exciting avenue for future work. Additionally, our current implementation of structural snapping relies on heuristic delimiter sets. While robust across English and CJK domains, future iterations could integrate a lightweight, learned boundary-detection head to provide tokenizer-agnostic structural alignment.

## References

Agrawal et al. (2025) S. Agrawal, R. Garrepalli, R. Goel, M. Lee, C. Lott, and F. Porikli Spiffy: multiplying diffusion llm acceleration via lossless speculative decoding . External Links: 2509.18085 , Link Cited by: §2.2 .

Arriola et al. (2025) M. Arriola, A. Gokaslan, J. T. Chiu, Z. Yang, Z. Qi, J. Han, S. S. Sahoo, and V. Kuleshov Block diffusion: interpolating between autoregressive and diffusion language models . arXiv preprint arXiv:2503.09573 . Cited by: §1 , §2.2 .

Austin et al. (2021a) J. Austin, D. D. Johnson, J. Ho, D. Tarlow, and R. Van Den Berg Structured denoising diffusion models in discrete state-spaces . Advances in neural information processing systems 34 , pp. 17981–17993 . Cited by: §1 , §2.1 , §3.1 .

Austin et al. (2021b) J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, et al. Program synthesis with large language models . arXiv preprint arXiv:2108.07732 . Cited by: §4.1 .

Campbell et al. (2022) A. Campbell, J. Benton, V. De Bortoli, T. Rainforth, G. Deligiannidis, and A. Doucet A continuous time framework for discrete denoising models . Advances in Neural Information Processing Systems 35 , pp. 28266–28279 . Cited by: §2.1 .

Chen et al. (2021) M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al. Evaluating large language models trained on code . arXiv preprint arXiv:2107.03374 . Cited by: §4.1 .

Chen et al. (2025) X. Chen, S. Huang, C. Guo, C. Wei, Y. He, J. Zhang, H. Li, Y. Chen, et al. DPad: efficient diffusion language models with suffix dropout . arXiv preprint arXiv:2508.14148 . Cited by: §2.2 .

Cobbe et al. (2021) K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems . arXiv preprint arXiv:2110.14168 . Cited by: §4.1 .

DeepMind (2025) G. DeepMind Gemini-diffusion . External Links: Link Cited by: §2.1 .

Hoogeboom et al. (2021) E. Hoogeboom, D. Nielsen, P. Jaini, P. Forré, and M. Welling Argmax flows and multinomial diffusion: learning categorical distributions . Advances in Neural Information Processing Systems 34 , pp. 12454–12465 . Cited by: §2.1 .

Hu et al. (2025) Z. Hu, J. Meng, Y. Akhauri, M. S. Abdelfattah, J. Seo, Z. Zhang, and U. Gupta Accelerating diffusion language model inference via efficient kv caching and guided diffusion . arXiv preprint arXiv:2505.21467 . Cited by: §2.2 .

Huang and Tang (2025) C. Huang and H. Tang Ctrldiff: boosting large diffusion language models with dynamic block prediction and controllable generation . arXiv preprint arXiv:2505.14455 . Cited by: §2.2 .

Israel et al. (2025) D. Israel, G. V. den Broeck, and A. Grover Accelerating diffusion llms via adaptive parallel decoding . External Links: 2506.00413 , Link Cited by: §2.2 .

Labs et al. (2025) I. Labs, S. Khanna, S. Kharbanda, S. Li, H. Varma, E. Wang, S. Birnbaum, Z. Luo, Y. Miraoui, A. Palrecha, S. Ermon, A. Grover, and V. Kuleshov Mercury: ultra-fast language models based on diffusion . External Links: 2506.17298 , Link Cited by: §2.1 .

Li et al. (2025a) P. Li, S. Yan, J. Tsai, R. Zhang, R. An, Z. Guo, and X. Gao Adaptive classifier-free guidance via dynamic low-confidence masking . arXiv preprint arXiv:2505.20199 . Cited by: §2.2 .

Li et al. (2025b) P. Li, Y. Zhou, D. Muhtar, L. Yin, S. Yan, L. Shen, S. Vosoughi, and S. Liu Diffusion language models know the answer before decoding . arXiv preprint arXiv:2508.19982 . Cited by: §2.2 .

Liu et al. (2025) Z. Liu, Y. Yang, Y. Zhang, J. Chen, C. Zou, Q. Wei, S. Wang, and L. Zhang DLLM-cache: accelerating diffusion large language models with adaptive caching . External Links: 2506.06295 , Link Cited by: §2.2 .

Lou et al. (2023) A. Lou, C. Meng, and S. Ermon Discrete diffusion language modeling by estimating the ratios of the data distribution . arXiv preprint arXiv:2310.16834 . Cited by: §2.1 .

Ma et al. (2025) X. Ma, R. Yu, G. Fang, and X. Wang DKV-cache: the cache for diffusion language models . External Links: 2505.15781 , Link Cited by: §2.2 .

Nie et al. (2025) S. Nie, F. Zhu, Z. You, X. Zhang, J. Ou, J. Hu, J. Zhou, Y. Lin, J. Wen, and C. Li Large language diffusion models . arXiv preprint arXiv:2502.09992 . Cited by: §1 , §2.1 , §3.1 , §4.1 .

Ou et al. (2024) J. Ou, S. Nie, K. Xue, F. Zhu, J. Sun, Z. Li, and C. Li Your absorbing discrete diffusion secretly models the conditional distributions of clean data . arXiv preprint arXiv:2406.03736 . Cited by: §2.1 .

Sahoo et al. (2024) S. Sahoo, M. Arriola, Y. Schiff, A. Gokaslan, E. Marroquin, J. Chiu, A. Rush, and V. Kuleshov Simple and effective masked diffusion language models . Advances in Neural Information Processing Systems 37 , pp. 130136–130184 . Cited by: §2.1 .

Shi et al. (2024) J. Shi, K. Han, Z. Wang, A. Doucet, and M. K. Titsias Simplified and generalized masked diffusion for discrete data . arXiv preprint arXiv:2406.04329 . Cited by: §2.1 .

Sohl-Dickstein et al. (2015) J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli Deep unsupervised learning using nonequilibrium thermodynamics . In International conference on machine learning , pp. 2256–2265 . Cited by: §2.1 .

Song et al. (2025a) Y. Song, X. Liu, R. Li, Z. Liu, Z. Huang, Q. Guo, Z. He, and X. Qiu Sparse-dllm: accelerating diffusion llms with dynamic cache eviction . External Links: 2508.02558 , Link Cited by: §2.2 .

Song et al. (2025b) Y. Song, Z. Zhang, C. Luo, P. Gao, F. Xia, H. Luo, Z. Li, Y. Yang, H. Yu, X. Qu, Y. Fu, J. Su, G. Zhang, W. Huang, M. Wang, L. Yan, X. Jia, J. Liu, W. Ma, Y. Zhang, Y. Wu, and H. Zhou Seed diffusion: a large-scale diffusion language model with high-speed inference . External Links: 2508.02193 , Link Cited by: §2.1 , §2.2 .

Wang et al. (2025) W. Wang, B. Fang, C. Jing, Y. Shen, Y. Shen, Q. Wang, H. Ouyang, H. Chen, and C. Shen Time is a feature: exploiting temporal dynamics in diffusion language models . arXiv preprint arXiv:2508.09138 . Cited by: §2.2 .

Wei et al. (2025) Q. Wei, Y. Zhang, Z. Liu, D. Liu, and L. Zhang Accelerating diffusion large language models with slowfast sampling: the three golden principles . External Links: 2506.10848 , Link Cited by: §2.2 .

Wu et al. (2025) C. Wu, H. Zhang, S. Xue, Z. Liu, S. Diao, L. Zhu, P. Luo, S. Han, and E. Xie Fast-dllm: training-free acceleration of diffusion llm by enabling kv cache and parallel decoding . arXiv preprint arXiv:2505.22618 . Cited by: §2.2 , §3.2 .

Ye et al. (2025) J. Ye, Z. Xie, L. Zheng, J. Gao, Z. Wu, X. Jiang, Z. Li, and L. Kong Dream 7b: diffusion large language models . arXiv preprint arXiv:2508.15487 . Cited by: §2.1 , §4.1 .

Zheng et al. (2024) K. Zheng, Y. Chen, H. Mao, M. Liu, J. Zhu, and Q. Zhang Masked diffusion models are secretly time-agnostic masked models and exploit inaccurate categorical sampling . arXiv preprint arXiv:2409.02908 . Cited by: §2.1 .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
