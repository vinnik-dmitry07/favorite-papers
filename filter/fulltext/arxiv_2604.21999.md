##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Universal Transformers Need Memory: Depth-State Trade-offs in Adaptive Recursive Reasoning

###### Abstract

We study learned memory tokens as a computational scratchpad for a single-block Universal Transformer with Adaptive Computation Time (ACT) on Sudoku-Extreme, a combinatorial reasoning benchmark. Memory tokens are empirically necessary: no configuration without them reaches non-trivial performance. The optimal count has a sharp lower threshold ( T = 0 T{=}0 always fails, T = 8 T{=}8 reliably succeeds) followed by a stable plateau ( T = 8 T{=}8 – 32 32 , 57.4 % ± 0.7 % 57.4\%\pm 0.7\% exact-match) and a dilution boundary at T = 64 T{=}64 . Under halt-side pressure ( λ \lambda warmup), mean halt drops monotonically with memory size across the plateau (from 11.6 at T = 8 T{=}8 to 8.3 at T = 64 T{=}64 ), showing that memory tokens and ponder depth substitute as resources at fixed accuracy.

We also identify a router initialization trap that causes the majority of training runs to fail: both default zero-bias and Graves’ recommended positive bias settle into a shallow halt equilibrium the model cannot escape. Inverting the bias to − 3 -3 (“deep start”) eliminates the failure mode, and ablation shows the trap is inherent to ACT initialization rather than an artifact of our architecture.

With reliable training, ACT yields an order of magnitude lower seed variance than fixed-depth processing ( ± 0.7 \pm 0.7 vs ± 9.3 \pm 9.3 pp); λ \lambda warmup recovers 34% of compute at matched accuracy; and attention heads specialize into memory readers, constraint propagators, and integrators across recursive depth. Code: https://github.com/che-shr-cat/utm-jax .

## 1 Introduction

Universal Transformers ( Dehghani et al., 2019 ) apply a single transformer block iteratively, with Adaptive Computation Time ( Graves, 2016 ) determining per-token processing depth. While theoretically appealing—arbitrary-depth reasoning with finite parameters—practical implementations have shown mixed results ( Csordás et al., 2021 ) .

We investigate the role of learned memory tokens ( Burtsev et al., 2020 ) in enabling recursive reasoning within this architecture, which we call UTM (Universal Transformer with Memory), using Sudoku-Extreme as a testbed. The title echoes Darcet et al. (2024) , “Vision Transformers Need Registers”—we present analogous evidence that our single-block UT needs memory tokens, based on extensive empirical failure without them.

Our contributions: 1. Memory-token necessity, threshold, and depth-state substitution (§ 4 ): In our single-block UT with ACT, no configuration without memory tokens achieves non-trivial performance across any tested seed, initialization, or depth mode. The optimal count shows a sharp threshold between T = 0 T{=}0 (always fails) and T = 8 T{=}8 (always succeeds) for 81-cell Sudoku, with a stable plateau through T = 32 T{=}32 . Memory tokens and ponder depth are substitutable resources at fixed accuracy: at λ = 0 \lambda{=}0 , minimum halt steps decrease monotonically with T T ( 17.7 → 16.4 → 15.5 17.7\to 16.4\to 15.5 ); under halt-side pressure ( λ = 0.001 \lambda{=}0.001 +warmup), the trade-off becomes a clean monotonic curve, with mean halt dropping from 11.60 11.60 at T = 8 T{=}8 to 10.29 10.29 at T = 32 T{=}32 to 8.25 8.25 at T = 64 T{=}64 at near-constant accuracy on the plateau ( ∼ 57 % \sim 57\% ) and a 2pp drop at the dilution boundary. We note that other recursive architectures (TRM, HRM) solve similar tasks via different mechanisms—the necessity is architecture-specific.

2. Router initialization trap (§ 3 ): We identify that both default initialization (bias = 0 =0 , p ≈ 0.5 p\approx 0.5 ) and Graves’ recommended positive bias (bias = 1 =1 , p ≈ 0.73 p\approx 0.73 ) create shallow-halt traps. In our setting, > > 70% of runs fail to escape. We propose deep-start initialization (bias = − 3 =-3 , p ≈ 0.05 p\approx 0.05 ), which inverts the assumption and resolves the issue.

3. ACT provides reliability and efficiency (§ 5 ): Fixed-depth processing with memory tokens achieves 53.4 % ± 9.3 % 53.4\%\pm 9.3\% EM (3 seeds)—high variance. ACT-enabled runs are more consistent ( 56.9 % ± 0.7 % 56.9\%\pm 0.7\% ). Lambda warmup achieves 57.0 % ± 1.1 % 57.0\%\pm 1.1\% using 34% fewer ponder steps—matching quality with significant compute savings.

4. Diagnostic framework (§ 3 ): Per-step router probability, step-weight distribution, and attention-mass logging that reveals head specialization and computation dynamics across recursive depth.

## 2 Architecture

### 2.1 Universal Transformer with Memory Tokens

Our model applies a single UniversalTransformerBlock (pre-norm attention + SwiGLU FFN) iteratively for up to K = 18 K{=}18 steps (Figure 1 ). The full sequence at each step is [ mem 1 , … , mem N , seq 1 , … , seq L ] [\text{mem}_{1},\ldots,\text{mem}_{N},\text{seq}_{1},\ldots,\text{seq}_{L}] with bidirectional attention.

Components: token + type embedding (memory vs sequence) + per-step learned positional embedding; multi-head attention with RoPE and QK-normalization; SwiGLU FFN with 8 / 3 × 8/3\times expansion; DerfNorm (our term for the normalization-free design using Derf ( Chen et al., 2025 ) ), where standard normalization layers are replaced by erf ​ ( α ⋅ x + s ) \text{erf}(\alpha\cdot x+s) with learned per-feature α , s \alpha,s ; N N learned memory vectors with indexed RoPE positions (numbered registers). Parameters: 3.2M (hidden=512, heads=8, head_dim=64, vocab=11).

### 2.2 Adaptive Computation Time

Following Graves (2016) , each token maintains cumulative halting probability. At step k k , the router (linear + sigmoid) outputs p k ∈ ( 0 , 1 ) p_{k}\in(0,1) . The output is a weighted blend: output = ∑ k = 1 N w k ⋅ h k \text{output}=\sum_{k=1}^{N}w_{k}\cdot h_{k} , where w k = p k w_{k}=p_{k} for intermediate steps and w N = 1 − ∑ k < N p k w_{N}=1-\sum_{k<N}p_{k} at halt. Ponder cost ρ = N + R \rho=N+R is minimized with coefficient λ \lambda .

When ACT is disabled, the model outputs only the final representation h K h_{K} (standard weight-tied transformer).

### 2.3 Deep-Start Initialization

With default framework initialization (zero bias), the router computes σ ⁡ ( W ⋅ h + 0 ) ≈ 0.5 \sigma(W\cdot h+0)\approx 0.5 , causing tokens to halt after ∼ 2 {\sim}2 steps. Graves (2016) recommends initializing the halting bias to a positive value ( b h = 1 b_{h}=1 , giving σ ⁡ ( ⋅ ) ≈ 0.73 \sigma(\cdot)\approx 0.73 ) to “prevent very long sequences at the beginning of training”—which makes tokens halt even faster ( ∼ 1 {\sim}1 – 2 2 steps). Dehghani et al. (2019) does not specify halting initialization (Appendix C shows architecture but omits init details).

Both the default (bias = 0 =0 , p ≈ 0.5 p\approx 0.5 ) and Graves’ recommendation (bias = 1 =1 , p ≈ 0.73 p\approx 0.73 ) produce shallow halting. We propose the opposite:

Deep start: bias = − 3 =-3 , giving σ ⁡ ( W ⋅ h − 3 ) ≈ 0.05 \sigma(W\cdot h-3)\approx 0.05 . Tokens process all K K steps by default and learn to halt earlier. This inverts Graves’ assumption: instead of preventing long sequences, we start with maximum depth and let the model discover where to stop. This is appropriate when the task requires significant depth—the cost of long initial sequences is small if the final learned policy uses them, whereas a shallow starting policy cannot easily discover that depth is needed.

## 3 The Router Initialization Trap

### 3.1 Diagnosis

We instrumented the ACT loop to log per-step router probability and router-specific gradient norm. Across 13 completed runs (planned 5 memory-token counts × \times 3 seeds; only T = 64 T{=}64 / S = 0 S{=}0 was run for T = 64 T{=}64 before we moved on; bias=0, λ = 0 \lambda{=}0 , 4 epochs each):

Diagnostic findings: (1) All runs start at p ≈ 0.48 p\approx 0.48 – 0.52 0.52 , halt = 2.0 =2.0 . (2) By step 3k, all develop a shallow-halt pattern (halt ≈ 5 \approx 5 – 7 7 ). (3) Escape correlates with a 10–45 × \times spike in router gradient norm. (4) Stuck runs maintain router gradient < 0.04 <0.04 for all 60k steps.

### 3.2 Deep Start Resolves the Trap

With bias = − 3 =-3 , all previously-failing configurations at seed 123 succeed (Table 2 ). Training dynamics change qualitatively: with bias=0, successful runs exhibit abrupt phase transitions; with bias = − 3 =-3 , accuracy rises smoothly.

### 3.3 DerfNorm Is Not the Cause

We verify the trap is not a DerfNorm artifact by replacing it with RMSNorm at the same seed and configuration ( T = 16 T{=}16 , seed 42, bias=0): DerfNorm achieves 50.6% EM (escapes); RMSNorm achieves 0.0% EM (halt stuck at 3.5, never escapes). The trap is worse with standard normalization—it is inherent to ACT with standard initialization in our setting. This is consistent with Chen et al. (2025) ’s general finding that Derf outperforms RMSNorm across domains, though the ACT-escape dynamics we observe are specific to recursive architectures.

## 4 Memory Tokens for Recursive Reasoning

### 4.1 Task and Setup

Sudoku-Extreme ( Sapient Intelligence, 2025 ) : 9 × \times 9 puzzles, extreme difficulty (17–24 givens). 3.83M train / 423K test. Encoder-style prediction of all 81 cells simultaneously. All results: hidden=512, heads=8, max_ponder=18, batch=256, AdamW (lr= 3 × 10 − 4 3\times 10^{-4} , cosine decay), EMA (0.999), 4 epochs, bias = − 3 =-3 , λ = 0 \lambda{=}0 unless noted.

### 4.2 Memory-Token Curve

Key findings: (1) Sharp threshold between T = 0 T{=}0 and T = 8 T{=}8 : T = 0 T{=}0 always fails ( 2.5 % 2.5\% , 3 seeds). T = 4 T{=}4 is borderline—succeeds at 2 of 3 seeds (55.5–55.8%) but fails at the third (5.4%), exhibiting the same seed sensitivity as T = 64 T{=}64 . T = 8 T{=}8 always succeeds ( 57.4 ± 0.7 % 57.4\pm 0.7\% , 3 seeds). The minimum reliable scratchpad for 81-cell Sudoku is 8 tokens ( ∼ 1 {\sim}1 per 10 cells). (2) Stable plateau : T = 8 T{=}8 : 57.4 ± 0.7 57.4{\pm}0.7 %, T = 16 T{=}16 : 56.9 ± 0.7 56.9{\pm}0.7 %, T = 32 T{=}32 : 56.4 ± 1.7 56.4{\pm}1.7 %. (3) T = 0 T{=}0 fails with deep start : memory tokens are necessary in this architecture. We note that TRM ( Jolicoeur-Martineau, 2025 ) and HRM ( Wang et al., 2025 ) solve Sudoku without memory tokens via autoregressive answer improvement—the necessity is architecture-specific to our single-block UT.

### 4.3 Memory-Depth Tradeoff

Within the plateau, memory tokens and ponder depth function as substitutable resources: as T T increases, the model can solve the task at the same accuracy with fewer ponder steps. The clearest evidence is the per-seed minimum halt step in Table 3 : T = 8 T{=}8 saturates the 18-step ceiling at all 3 seeds (halt ∈ [ 17.7 , 18.0 ] \in[17.7,18.0] ), T = 16 T{=}16 admits some headroom ( [ 16.4 , 18.0 ] [16.4,18.0] ), and T = 32 T{=}32 admits more ( [ 15.5 , 18.0 ] [15.5,18.0] ). The substitution is real but seed-dependent — at T = 32 T{=}32 , S = 0 S{=}0 exploits the headroom (halt = 15.5 =15.5 ) while S = 42 S{=}42 stays saturated (halt = 18.0 =18.0 ), and different seeds find different equilibria along the same accuracy plateau.

Mean halt is dominated by the depth ceiling at λ = 0 \lambda{=}0 . Across the plateau, mean halt is 17.87 17.87 , 17.07 17.07 , 17.03 17.03 for T = 8 , 16 , 32 T=8,16,32 respectively (Table 3 ). The compression is small in the mean because λ = 0 \lambda{=}0 in this sweep — with no penalty for using deep ponder, the model saturates the ceiling whenever it can, and the substitution surfaces only in the per-seed minima. The trade-off is more visible under halt-side pressure: with λ = 0.001 \lambda{=}0.001 and a 20k-step warmup at T = 16 T{=}16 across 3 seeds (§ 5 ), mean halt drops from 17.07 17.07 to ∼ 11.4 \sim 11.4 at unchanged accuracy ( 57.0 ± 1.1 % 57.0\pm 1.1\% vs 56.9 ± 0.7 % 56.9\pm 0.7\% ). This is the canonical depth-state trade-off form: fixed accuracy, reduced compute, achieved by giving the router something to push against.

The full curve under halt-side pressure. A direct T × λ T\times\lambda +warmup sweep at S = 0 S{=}0 confirms the trade-off in its canonical form (Table 4 , Figure 4 ): mean halt decreases monotonically from 11.60 11.60 at T = 8 T{=}8 to 11.50 11.50 at T = 16 T{=}16 to 10.29 10.29 at T = 32 T{=}32 to 8.25 8.25 at T = 64 T{=}64 , with EM essentially constant across the plateau ( 57.09 → 58.00 → 56.87 57.09\to 58.00\to 56.87 ) and a 2pp drop at the dilution boundary ( T = 64 T{=}64 , 54.91 % 54.91\% ). Compared to λ = 0 \lambda{=}0 (Table 3 , S = 0 S{=}0 column), halt is compressed by 33–40% across the plateau at unchanged or slightly improved accuracy.

Total compute is approximately conserved, not strictly fungible. Total token-step compute (memory plus sequence tokens times mean halt) grows mildly with T T across the plateau ( 1032 → 1116 → 1163 1032\to 1116\to 1163 token-steps for T = 8 , 16 , 32 T=8,16,32 , ∼ 13 % {\sim}13\% growth), reaching 1196 1196 at T = 64 T{=}64 . Memory and depth substitute in halt count and per-step bandwidth, but total operations are not strictly preserved.

The dilution boundary is compatible with halt-side pressure. At T = 64 T{=}64 , halt drops further (8.25) and accuracy is 2pp below the plateau ( 54.91 % 54.91\% vs ∼ 57 % {\sim}57\% ). With only one seed in this sweep, we cannot rule out single-seed noise from the 2pp gap alone (the eval trajectory in Figure 4 b shows the four runs intermingled across the plateau). However, the magnitude and direction are consistent with the bimodal collapse observed at T = 64 T{=}64 under λ = 0 \lambda{=}0 across multiple seeds (Table 3 ); read together, they support treating T = 64 T{=}64 as a dilution boundary — an architectural property at large T T — rather than an artifact of saturated halting at λ = 0 \lambda{=}0 .

### 4.4 Fixed-Depth vs ACT Processing

Fixed-depth processing achieves comparable mean EM ( 53.4 % 53.4\% ) but with much higher variance : EM ranges from 44.9% to 63.4% across 3 seeds ( ± 9.3 % \pm 9.3\% ), compared to 56.5–57.7% for ACT ( ± 0.7 % \pm 0.7\% )—an order-of-magnitude difference in seed sensitivity. We attribute this to the output mechanism: ACT blends representations across all K K steps ( ∑ w k ​ h k \sum w_{k}h_{k} ), averaging out seed-dependent variation in individual steps; fixed-depth relies entirely on the final step’s representation h K h_{K} , which may be more sensitive to initialization-dependent optimization trajectories since it is a single snapshot rather than an average over steps. Lambda warmup combines ACT’s reliability ( 57.0 ± 1.1 % 57.0\pm 1.1\% ) with 34% compute savings.

### 4.5 How Memory Tokens Function: Attention Analysis

Attention evolves across depth: at step 0, attention is diffuse; by step 9, S → \to S develops block-diagonal patterns matching Sudoku row/column/box constraints; by step 17, the structure is highly refined (Figure 5 ).

Heads specialize into distinct roles (Figure 6 , Table 6 ). The full attention quadrant breakdown reveals asymmetric memory usage:

Three functional groups emerge: Memory readers (H4, H5: high s → \to m, sequence queries memory), memory writers (H1, H3: high m → \to s, memory broadcasts to sequence), and constraint propagators (H2, H6: s → \to m ≈ 0 \approx 0 , structured S → \to S patterns). H0 and H2 show high m → \to m (memory self-attention, ∼ 0.73 {\sim}0.73 ), suggesting internal memory coordination. H6 is striking: both s → \to s and m → \to s are ∼ 1.0 {\sim}1.0 —it propagates puzzle constraints while memory tokens passively observe the sequence.

In the trapped model (0% EM), no head develops s → \to m > 0.16 >0.16 , attention is disorganized, and the constraint patterns seen in H2/H6 are absent.

### 4.6 Small-Dataset Generalization

Following the TRM protocol (1000 training puzzles, 1000 augmentations, full 423K test set):

The model memorizes perfectly but achieves only 6–8% on unseen puzzles, even with TRM-matched regularization. This suggests that TRM’s autoregressive answer-improvement mechanism may be better suited for algorithmic generalization, though the architectures differ in multiple ways and isolating the causal factor remains future work.

## 5 Making ACT Efficient

### 5.1 Lambda Warmup

Direct application of the ponder penalty collapses halting even with deep start. Lambda warmup resolves this: the model establishes deep processing during the warmup phase, then the penalty compresses computation to halt ≈ 11 \approx 11 . Across 3 seeds, warmup achieves 57.0 ± 1.1 % 57.0\pm 1.1\% EM—matching λ = 0 \lambda{=}0 quality ( 56.9 ± 0.7 % 56.9\pm 0.7\% ) with 34% fewer steps.

### 5.2 Inference Beyond Trained Depth

Models generalize to more ponder steps than trained (step embeddings wrap modularly). Running the lambda-warmup model for 36 steps (2 × \times training depth) yields 66% EM, up from 52% at step 17—a 14pp gain from inference-time compute alone, with no retraining. Beyond 36 steps, quality plateaus and slowly degrades (64% at step 48, 64% at step 63), but never crashes—the model degrades gracefully. The sweet spot is ∼ 2 × {\sim}2\times training depth.

Other models improve modestly (+4–6pp) and plateau by step 28. The practical implication: one can train with aggressive lambda for efficiency (halting at ∼ 11 {\sim}11 steps), then run inference at 2 × 2\times depth when accuracy matters, recovering quality that the penalty compressed away.

## 6 Related Work and Architectural Convergence

The architecture we study sits at the intersection of three threads of research that developed largely independently and have re-engaged in 2025–2026 around a similar set of commitments: applying a single weight-shared block recursively, with adaptive halting, and some form of persistent state across recursion. We trace each thread, then map the design space they collectively occupy.

### 6.1 Universal Transformers and Adaptive Computation Time

Adaptive Computation Time was introduced by Graves (2016) for recurrent neural networks as a mechanism for the network to learn how much computation to spend on each input. Each step produces a halting probability via a sigmoid output; cumulative halting probabilities trigger early termination, and a remainder term provides the gradient path that lets the network learn when to stop.

Dehghani et al. (2019) combined ACT with the Transformer architecture in the Universal Transformer (UT), applying a single weight-shared block iteratively up to a maximum depth. UTs decouple parameter count from depth and provide a path to architectures with theoretical universality properties. Empirically, however, ACT in UTs has shown mixed results—for example, Csordás et al. (2021) implement Universal Transformers as “simply Transformers with shared weights between layers, without adaptive computation time” (§2.2), reflecting a broader trend of dropping ACT from UT variants in practice. Our findings on the router initialization trap (§ 3 ) suggest that some of these difficulties may reflect optimization pathologies in standard initialization rather than fundamental limitations of the architecture.

PonderNet ( Banino et al., 2021 ) reformulates ACT’s halting policy as a probabilistic model with a geometric distribution over halting steps, motivated by the observation that “ACT is notably unstable and sensitive to the choice of a hyper-parameter that trades-off accuracy and computation cost. Additionally, the gradient for the cost of computation can only back-propagate through the last computational step, leading to a biased estimation of the gradient.” PonderNet’s reformulation provides unbiased gradient estimates while remaining fully differentiable.

Saunshi et al. (2025) provide theoretical and empirical evidence that “for many synthetic reasoning problems like addition, p p -hop induction, and math problems, a k k -layer transformer looped L L times nearly matches the performance of a k ​ L kL -layer non-looped model, and is significantly better than a k k -layer model.” This supports the case for weight-shared depth recurrence as a general principle, of which our minimal architecture is one instantiation.

### 6.2 Memory Tokens and Registers

Memory tokens were introduced by Burtsev et al. (2020) in the Memory Transformer, where a small set of learnable vectors are prepended to the input sequence to “store non-local representations” and create a “memory bottleneck for the global information”—a learned global scratchpad attended to by all sequence positions through standard self-attention. Bulatov et al. (2022) extended the mechanism for long-context recurrence in the Recurrent Memory Transformer (RMT), where memory tokens are passed across sequence segments to enable processing beyond the model’s nominal context window.

Darcet et al. (2024) independently rediscovered the same primitive for vision transformers under the name registers , motivated by the observation that “high-norm tokens appearing during inference primarily in low-informative background areas of images” are repurposed by the model for internal computations. Their fix was to append additional tokens to the token sequence—independent of the input image—that the model can learn to use as registers, which absorbs the high-norm pathology and restores clean attention maps. The two genealogies—memory tokens for long-context language modeling, registers for vision transformer interpretability—describe the same architectural mechanism: prepended learnable tokens that participate fully in attention but are not tied to any input position.

Our work applies this mechanism inside the depth-recurrent loop of a UT. Memory tokens in our architecture persist across ponder steps within a single forward pass and serve as recursion-updated working memory rather than long-context summary or interpretability scaffolding.

### 6.3 Recursive Reasoning on Combinatorial Benchmarks

A recent line of work has focused on weight-shared recursive computation under the name recursive reasoning , motivated by performance on combinatorial puzzle benchmarks (Sudoku, mazes, ARC-AGI).

HRM ( Wang et al., 2025 ) introduced two interdependent recurrent modules—a high-level module for “slow, abstract planning” and a low-level module for “rapid, detailed computations”—both implemented as encoder-only Transformer blocks with identical architectures (4 layers each, per Jolicoeur-Martineau, 2025 ), with adaptive halting via Q-learning and deep supervision across up to 16 segments. HRM achieves strong small-data generalization with ∼ 1 {\sim}1 K training examples plus heavy augmentation. Its Related Work explicitly positions the architecture within the Universal Transformer / ACT lineage, noting that “Like earlier neural reasoning algorithms including the Universal Transformer, HRM is computationally universal when given sufficient memory and time constraints” (§6).

TRM ( Jolicoeur-Martineau, 2025 ) simplifies HRM’s two-network design to “a single network with only 2 layers.” The architecture maintains two recursive latent variables: a proposed solution y y and a latent reasoning feature z z (the paper explicitly renames HRM’s z H z_{H} and z L z_{L} for the TRM algorithm: “there is simply an input x x , a proposed solution y y (previously called z H z_{H} ), and a latent reasoning feature z z (previously called z L z_{L} )”). The MLP-Mixer variant (TRM-MLP, 5M parameters) reaches 87.4% on Sudoku-Extreme; the attention variant (TRM-Att, 7M parameters) reaches 74.7% on Sudoku-Extreme and 85.3% on Maze-Hard. TRM trains via deep supervision combined with full back-propagation through the recursion (rather than HRM’s 1-step gradient approximation) and uses a simplified halting mechanism that drops the continue Q-value entirely.

URM ( Gao et al., 2025 ) explicitly identifies its architecture as a Universal Transformer variant. Its §2.2 (“Universal Transformer”) opens by attributing the architecture to Dehghani et al. (2019) : “The Universal Transformer (UT) extends the standard Transformer by introducing recurrent computation over depth. Instead of stacking L L distinct layers, the UT applies a single transition block repeatedly to refine token representations.’’ URM applies UT+ACT in an encoder-style (non-causal) design with a ConvSwiGLU MLP and Truncated Backpropagation Through Loops (TBPTL), reaching 77.6% on Sudoku and 53.8% pass@1 on ARC-AGI-1. 1 1 1 The URM paper describes the architecture as “decoder-only,” but the public implementation uses bidirectional self-attention ( causal=False in models/urm/urm.py ); we describe it accordingly. This matches the HRM and TRM lineage, which likewise refine a fixed-length puzzle sequence rather than generate autoregressively. URM positions its contribution as identifying which mechanisms within the UT family drive performance, finding that “recurrent inductive bias” and the ConvSwiGLU nonlinearity matter more than elaborate architectural designs.

Across these three works, distinct architectural commitments are added to the underlying UT-with-ACT skeleton: HRM contributes hierarchical state, deep supervision, and the 1-step gradient approximation; TRM contributes the single-network simplification, full-recursion backpropagation, and the renaming-and-clarification of HRM’s two latents into a clean ( x x , y y , z z ) structure; URM contributes ConvSwiGLU, TBPTL, and explicit positioning within the UT lineage. Our work occupies the simpler corner of this space—single block, no per-position summed latent state, single-pass training—and isolates what this minimal configuration requires to function.

### 6.4 Recursive Transformers at Language-Modeling Scale

A complementary line of recent work has scaled weight-shared recursive computation to language-modeling pretraining, providing convergent evidence about the role of memory mechanisms.

Geiping et al. (2025) (Huginn) study “a novel language model architecture that is capable of scaling test-time computation by implicitly reasoning in latent space.” Their model “iterat[es] a recurrent block, thereby unrolling to arbitrary depth at test-time,” and is scaled to 3.5 billion parameters and 800 billion tokens. They show the model can improve reasoning performance with additional inference-time compute “up to a computation load equivalent to 50 billion parameters.” This is the canonical LM-scale recurrent-depth pretraining work and demonstrates that the depth-as-third-axis premise of UT/ACT survives into the modern LM regime.

Zhu et al. (2025) (Ouro) extend this thread with “a family of pre-trained Looped Language Models (LoopLM) that …build reasoning into the pre-training phase through (i) iterative computation in latent space, (ii) an entropy-regularized objective for learned depth allocation, and (iii) scaling to 7.7T tokens.” Ouro’s halting mechanism is explicitly linked to PonderNet: the authors describe an exit gate that runs in parallel with the LM head at each step and aligns with adaptive-computation methods like PonderNet, which also optimize an ELBO objective for dynamic halting. At 1.4B and 2.6B parameters, Ouro models match the results of up to 12B SOTA LLMs across a wide range of benchmarks. Importantly, Ouro reports that “recurrence does not increase raw knowledge storage (approximately 2 bits per parameter for both looped and non-looped models) but dramatically enhances knowledge manipulation capabilities on tasks requiring fact composition and multi-hop reasoning.” Ouro carries information through the hidden state alone, without any auxiliary memory mechanism.

Bae et al. (2025) propose Mixture-of-Recursions (MoR), “a unified framework that combines [parameter sharing and adaptive computation] inside a single Recursive Transformer. MoR reuses a shared stack of layers across recursion steps to achieve parameter efficiency, while lightweight routers enable adaptive token-level thinking.” MoR offers an alternative path to per-token compute allocation that is orthogonal to memory-token augmentation.

Yu et al. (2026) (MeSH) diagnose the same fundamental issue we motivate—that the single hidden state in a recursive transformer is overloaded, forced to simultaneously carry persistent context and transient computation. They quantify this with three observables: a skewed computational pattern (the first loop performs most of the work, subsequent loops contribute negligibly), representational stagnation (high CKA similarity between consecutive loop states), and loop representational collapse (rapid singular-value decay indicating low-dimensional collapse). Their solution, Memory-as-State-Highways, “replaces the overloaded hidden state with an explicit memory buffer governed by lightweight, step-wise routers.” MeSH-enhanced recursive transformers at the 1.4B Pythia scale, with 33% fewer non-embedding parameters than the non-recursive counterpart, “improv[e] average downstream accuracy by +1.06%.” Architecturally, MeSH slots are full-sequence-shaped tensors (closer to TRM’s per-position latents than to our memory tokens), and the central architectural innovation is breaking weight-tying for the routers—each iteration uses different routing parameters—which is what enables the functional specialization across iterations they observe.

Frey et al. (2026) combine adaptive per-layer looping with gated memory banks at the ∼ 200 {\sim}200 M parameter scale on language modeling. Their architecture pairs PonderNet-style halting with two types of static learnable memory: local memory banks per layer and a global memory bank shared across layers, both retrieved via key-value attention with input-dependent gating. They report a functional dissociation: looping primarily benefits mathematical reasoning (a Loop-3 model reduces math BPB from 2.163 to 1.687, a 22% reduction), while memory banks help recover commonsense performance, and the combination outperforms an iso-FLOP baseline with three times the layers on math benchmarks. They frame this as a distinction between knowledge manipulation (improved by looping, since iterating refines representations) and knowledge capacity (improved by memory, since unique parameters store more information): “the core tradeoff is between knowledge manipulation, which looping enhances as it repeatedly refines the representations, and knowledge capacity, which requires additional unique parameters.”

The works above converge with ours from very different regimes. Yu et al. (2026) arrive at memory-based externalization as a fix for diagnosed pathologies in LM recursion; Frey et al. (2026) arrive at memory-plus-looping as a complementary architecture combining math and commonsense performance; Geiping et al. (2025) and Zhu et al. (2025) demonstrate the scaling viability of depth recurrence at LM scale; we arrive at memory tokens as the minimum architectural element required for functional behavior in a minimal UT on combinatorial reasoning. Different scales, different tasks, different memory mechanisms—the same architectural conclusion in each case: the residual stream alone is insufficient for sustained recursive computation, and some form of explicit state externalization is needed.

### 6.5 Adjacent: External Memory and Adaptive Long Context

For completeness, we note two adjacent lines of work that share vocabulary with ours but address different problems. Memformer ( Wu et al., 2020 ) , Infini-attention ( Munkhdalai et al., 2024 ) , and Titans ( Behrouz et al., 2025 ) address long-context efficiency through external memory modules updated across sequence segments. The Neural Turing Machine ( Graves et al., 2014 ) and Differentiable Neural Computer ( Graves et al., 2016 ) introduced explicit differentiable memory with content and location-based addressing. These target sequence-length recurrence or explicit data-structure operations rather than depth recurrence within a single forward pass, but inform the design-space discussion below.

### 6.6 Mapping the Design Space

Architectures across the threads above can be characterized along three axes: (i) how the recurring unit is structured, (ii) how persistent state is carried across recursion, and (iii) how computation is allocated. Table 9 maps the closest neighbors. Our work occupies the simplest configuration along each axis: a single transformer layer as recurring unit, sample-independent recursion-updated memory tokens as persistent state, ACT-mediated variable depth as computation allocation, and a single forward pass without deep supervision.

The design-space view clarifies several relationships that surface vocabulary obscures.

TRM and UTM use distinct memory mechanisms despite both involving prepended learnable tokens. TRM’s puzzle-ID embedding ( puzzle_emb in the public code) is concatenated to the input sequence as additional token positions, in the Burtsev et al. (2020) lineage, but functions as a per-puzzle-ID static identifier rather than a recursion-updated scratchpad: it is set once per puzzle and re-injected unchanged at each recursion step. Our memory tokens are sample-independent (shared across all inputs of a given task) and update via attention each ponder step, functioning as a general-purpose recursion-updated scratchpad. TRM additionally maintains its full-sequence-shaped latents y y and z z , summed (not concatenated) into the input embedding, as the actual recursive state—a mechanism we do not use.

MeSH’s mechanism occupies a different point in the design space than ours, despite reaching a similar conclusion. MeSH’s slots are full-sequence-shaped tensors accessed by per-iteration routers that are not weight-tied across iterations. Our memory tokens are distinct prepended positions accessed by standard self-attention with a fully weight-shared block. The two mechanisms address overlapping problems via different architectural choices: MeSH addresses functional specialization across iterations by making the routers iteration-specific; we maintain full weight-tying and address the same underlying issue (insufficient bandwidth in the residual stream) by adding parallel addressable storage. Whether iteration-specific routing and addressable storage are complementary or substitutable is an open empirical question.

URM and UTM are closer architecturally to each other than to TRM or HRM. Both use the explicit UT+ACT framing; both rely on the residual stream rather than per-position latent state for working memory. URM substitutes ConvSwiGLU and truncated backpropagation for our memory tokens and single-pass training. The two architectures are evaluated under different training regimes—URM follows the HRM/TRM 1K-example small-data protocol with heavy augmentation, while our 57% is reported under full training—so a direct head-to-head comparison would be misleading; isolating the contribution of each architectural axis under a matched regime is left to future work.

Ouro shows that loop depth alone scales without explicit memory augmentation, but identifies the same manipulation-vs-capacity tradeoff. Ouro reports that recurrence does not increase per-parameter knowledge storage but enhances knowledge manipulation. This parallels Frey et al.’s explicit dissociation of looping (manipulation) from memory (capacity), and is consistent with our finding that memory tokens become necessary precisely when the architecture is most minimal—exactly the regime where the residual stream’s capacity is most constrained.

Our “memory tokens are necessary” finding is specific to the minimal configuration. TRM solves Sudoku-Extreme without our memory-token mechanism but with full-sequence per-position summed latents and deep supervision. URM solves Sudoku-Extreme without explicit persistent state but with ConvSwiGLU and TBPTL. MeSH improves recursive language modeling without standard memory tokens but with externalized iteration-specific routing. Frey et al. recover commonsense performance via key-value memory banks. Ouro relies on loop depth alone. The finding is therefore not that memory tokens are universally necessary for recursive computation, but that something must compensate for the residual stream’s narrow bandwidth in a depth-recurrent architecture—and across the works above, every architecture that succeeds adds some such mechanism. Memory tokens are one such compensation; per-position summed latents are another; iteration-specific external buffers are a third; gated key-value retrieval is a fourth; convolutional sequence mixing is a fifth; sufficient parameter count combined with massive pretraining is a sixth. Our work establishes the minimal mechanism along this axis on the smallest architecture and cleanest task; characterizing the full equivalence class is open.

### 6.7 What the Convergence Suggests

The threads above started from different motivations—adaptive computation budgets, long-context memory, biologically-inspired recursion, parameter-efficient pretraining at scale—and have arrived in 2025–2026 at architectures that share a substantial core: weight-shared recurrence, persistent state across recursion, and (often) adaptive halting. This convergence is now visible across scales, from minimal architectures on combinatorial tasks (this work) to language models pretrained on trillions of tokens ( Zhu et al., 2025 ; Geiping et al., 2025 ; Yu et al., 2026 ) .

A useful framing emerges from this convergence: looping enhances the model’s ability to manipulate information through iterative refinement, while memory enhances its capacity to store information that the manipulation operates on. Frey et al. (2026) articulate this dissociation explicitly; Ouro corroborates it independently with the empirical observation that recurrence does not increase per-parameter knowledge storage but dramatically improves multi-hop reasoning. Under this framing, our finding that memory tokens are necessary in the minimal UT setting—where residual-stream capacity is most constrained—is exactly what one would predict: the minimal residual stream cannot manipulate knowledge it has no capacity to store. The bandwidth of working memory and the depth of computation are complementary architectural resources, and the right ratio depends on task structure.

This convergence motivates several testable predictions:

1. Bandwidth-allocation scaling. Wider models (more residual capacity) should require fewer memory tokens, while deeper recursion (more state to maintain across steps) should require more—and varying these axes systematically should trace iso-performance contours rather than independent optima.

2. Additive vs. substitutive gains. Since TRM solves Sudoku-Extreme via full-sequence summed latents and URM via convolutional sequence mixing, augmenting either with explicit recursion-updated memory tokens should yield additive rather than substitutive gains; if the gains are instead substitutive, the bandwidth framing must be refined.

3. Dissociability of halting and memory. Within the recursive-transformer family halting and memory are dissociable mechanisms—Ouro and PonderNet provide adaptive halting without explicit memory augmentation, while MeSH provides explicit memory without adaptive halting (fixed N loop N_{\mathrm{loop}} )—so we expect that combining them deliberately (rather than treating them as solutions to the same problem) is the architecturally correct move.

Characterizing the full equivalence class of bandwidth-augmenting mechanisms across tasks and scales, and verifying or falsifying these predictions, is the natural next direction for the field.

## 7 Future Work

Our findings open several directions we consider most promising: (1) Scaling and width revisited : our 3.2M model is half the size of TRM (7M). A hidden=768 model ( ∼ 7 {\sim}7 M params) would enable direct comparison. Notably, all prior width experiments (hidden=768) used the default initialization and uniformly failed (2–5% EM)—it is unknown whether deep-start initialization would rescue these, which would reframe the “width-variance trap” observed in early experiments as another manifestation of the router initialization issue. (2) Muon optimizer : Newton-Schulz-based optimizers ( Jordan, 2024 ) have shown promise for weight-shared architectures; combining Muon with deep-start initialization and lambda warmup is unexplored. (3) TRM-style training protocol : our small-dataset results (6–8% generalization) use a single-pass encoder; adapting TRM’s iterative answer-refinement mechanism to the UT framework could improve algorithmic generalization. (4) Multi-task evaluation : testing on maze navigation, ARC-AGI, or formal logic to determine whether the T = 8 T{=}8 threshold and attention specialization patterns are task-universal or Sudoku-specific. (5) Deeper attention analysis : per-head, per-difficulty probing to understand whether memory readers and constraint propagators emerge consistently across tasks and scales.

## 8 Limitations

(1) Single task : all results on Sudoku-Extreme; thresholds are likely task-specific. (2) Architecture-specific : HRM, TRM, and URM all solve Sudoku without memory tokens, via different mechanisms (hierarchical z L , z H z_{L},z_{H} state; per-position y , z y,z latents with deep supervision; ConvSwiGLU + TBPTL, respectively); our findings apply to the single-block UT. A parameter-matched comparison (7M) is planned. (3) Algorithmic generalization : the single-block UT memorizes but does not generalize (6–8% vs TRM’s 87.4%) on the 1K-example protocol, likely reflecting architectural differences in learning mechanisms rather than capacity alone (3.2M vs TRM’s 7M params). (4) T = 64 T{=}64 seed sensitivity : deep-start eliminates sensitivity in the plateau but not at the dilution boundary. (5) Fixed-depth variance : fixed-depth processing shows high seed variance ( ± 9.3 % \pm 9.3\% across 3 seeds) compared to ACT ( ± 0.7 % \pm 0.7\% ), likely due to reliance on a single step’s representation. (6) Evaluation granularity : eval EM is computed on 12.8K-sample batches (SE ± \pm 0.4pp), well below the inter-seed variance ( ± \pm 0.7pp); full 423K test-set evaluation would not materially change the reported means.

## 9 Conclusion

We demonstrate that learned memory tokens are empirically necessary for a single-block Universal Transformer to solve combinatorial reasoning tasks. Without them, no configuration succeeds—regardless of initialization, seed, ponder steps, or use of ACT. With 8 or more tokens ( ∼ 1 {\sim}1 per 10 puzzle cells), the model reliably achieves 57% exact-match on Sudoku-Extreme, with a stable plateau through T = 32 T{=}32 .

A key methodological finding enables these results: in our experiments, standard ACT initialization creates a degenerate p ≈ 0.5 p\approx 0.5 equilibrium causing > > 70% of runs to fail. This trap—confirmed inherent to ACT via normalization ablation—is fixable with a single line of code.

ACT provides more consistent results than fixed-depth processing ( 56.9 ± 0.7 % 56.9\pm 0.7\% vs 53.4 ± 9.3 % 53.4\pm 9.3\% ), and lambda warmup achieves matching accuracy ( 57.0 ± 1.1 % 57.0\pm 1.1\% ) using 34% fewer ponder steps—genuine compute efficiency without quality loss. Across the T = 8 T{=}8 – 32 32 plateau, memory tokens and ponder depth substitute at fixed accuracy. Under halt-side pressure ( λ = 0.001 \lambda{=}0.001 +warmup, S = 0 S{=}0 ), the halt-vs- T T curve is monotonically decreasing ( 11.60 → 11.50 → 10.29 → 8.25 11.60\to 11.50\to 10.29\to 8.25 for T ∈ { 8 , 16 , 32 , 64 } T\in\{8,16,32,64\} ) at near-constant accuracy on the plateau, with a 2pp drop at the dilution boundary ( T = 64 T{=}64 ). This is the canonical depth-state trade-off: memory tokens and recursive depth function as substitutable resources for combinatorial reasoning, with the dilution boundary intrinsic to the architecture rather than an artifact of saturated halting.

## References

Banino et al. (2021) A. Banino, J. Balaguer, and C. Blundell. PonderNet: Learning to Ponder. arXiv:2107.05407 , 2021. https://arxiv.org/abs/2107.05407

Bulatov et al. (2022) A. Bulatov, Y. Kuratov, and M. Burtsev. Recurrent Memory Transformer. In NeurIPS , 2022. https://arxiv.org/abs/2207.06881

Burtsev et al. (2020) M. Burtsev et al. Memory Transformer. arXiv:2006.11527 , 2020. https://arxiv.org/abs/2006.11527

Csordás et al. (2021) R. Csordás, K. Irie, and J. Schmidhuber. The Devil is in the Detail: Simple Tricks Improve Systematic Generalization of Transformers. In EMNLP , 2021. https://aclanthology.org/2021.emnlp-main.49/

Darcet et al. (2024) T. Darcet et al. Vision Transformers Need Registers. In ICLR , 2024. https://openreview.net/forum?id=2dnO3LLiJ1

Dehghani et al. (2019) M. Dehghani et al. Universal Transformers. In ICLR , 2019. https://arxiv.org/abs/1807.03819

Graves (2016) A. Graves. Adaptive Computation Time for Recurrent Neural Networks. arXiv:1603.08983 , 2016. https://arxiv.org/abs/1603.08983

Jolicoeur-Martineau (2025) A. Jolicoeur-Martineau. Less is More: Recursive Reasoning with Tiny Networks. arXiv:2510.04871 , 2025. https://arxiv.org/abs/2510.04871

Jordan (2024) K. Jordan. Muon: An optimizer for hidden layers. https://kellerjordan.github.io/posts/muon/ , 2024.

Saunshi et al. (2025) N. Saunshi et al. Reasoning with Latent Thoughts: On the Power of Looped Transformers. arXiv:2502.17416 , 2025. https://arxiv.org/abs/2502.17416

Sapient Intelligence (2025) Sapient Intelligence. Sudoku-Extreme Dataset. https://huggingface.co/datasets/sapientinc/sudoku-extreme , 2025.

Chen et al. (2025) M. Chen, T. Lu, J. Zhu, M. Sun, and Z. Liu. Stronger Normalization-Free Transformers. arXiv:2512.10938 , 2025. https://arxiv.org/abs/2512.10938

Gao et al. (2025) Z. Gao, L. Chen, Y. Xiao, H. Xing, R. Tao, H. Luo, J. Zhou, and B. Dai. Universal Reasoning Model. arXiv:2512.14693 , 2025. https://arxiv.org/abs/2512.14693

Wang et al. (2025) G. Wang, J. Li, Y. Sun, X. Chen, C. Liu, Y. Wu, M. Lu, S. Song, and Y. A. Yadkori. Hierarchical Reasoning Model. arXiv:2506.21734 , 2025. https://arxiv.org/abs/2506.21734

Bae et al. (2025) S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, and S.-Y. Yun. Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation. arXiv:2507.10524 , 2025. https://arxiv.org/abs/2507.10524

Behrouz et al. (2025) A. Behrouz, P. Zhong, and V. Mirrokni. Titans: Learning to Memorize at Test Time. arXiv:2501.00663 , 2025. https://arxiv.org/abs/2501.00663

Frey et al. (2026) M. Frey, B. Shomali, A. H. Bashir, D. Berghaus, J. Koehler, and M. Ali. Adaptive Loops and Memory in Transformers: Think Harder or Know More? arXiv:2603.08391 , 2026. https://arxiv.org/abs/2603.08391

Geiping et al. (2025) J. Geiping, S. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein. Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach. arXiv:2502.05171 , 2025. https://arxiv.org/abs/2502.05171

Graves et al. (2014) A. Graves, G. Wayne, and I. Danihelka. Neural Turing Machines. arXiv:1410.5401 , 2014. https://arxiv.org/abs/1410.5401

Graves et al. (2016) A. Graves, G. Wayne, M. Reynolds, T. Harley, I. Danihelka, A. Grabska-Barwińska, S. G. Colmenarejo, E. Grefenstette, T. Ramalho, J. Agapiou, et al. Hybrid computing using a neural network with dynamic external memory. Nature , 538(7626):471–476, 2016. https://www.nature.com/articles/nature20101

Munkhdalai et al. (2024) T. Munkhdalai, M. Faruqui, and S. Gopal. Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention. arXiv:2404.07143 , 2024. https://arxiv.org/abs/2404.07143

Wu et al. (2020) Q. Wu, Z. Lan, K. Qian, J. Gu, A. Geramifard, and Z. Yu. Memformer: A Memory-Augmented Transformer for Sequence Modeling. arXiv:2010.06891 , 2020. https://arxiv.org/abs/2010.06891

Yu et al. (2026) C. Yu, X. Shu, Y. Wang, Y. Zhang, H. Wu, J. Li, R. Long, Z. Chen, Y. Xu, W. Su, and B. Zheng. MeSH: Memory-as-State-Highways for Recursive Transformers. arXiv:2510.07739 , 2026. https://arxiv.org/abs/2510.07739

Zhu et al. (2025) R.-J. Zhu, T. Peng, T. Cheng, X. Qu, J. Huang, D. Zhu, H. Wang, K. Xue, X. Zhang, Y. Shan, et al. Scaling Latent Reasoning via Looped Language Models (Ouro). arXiv:2510.25741 , 2025. https://arxiv.org/abs/2510.25741

## Appendix A Puzzle Solving Visualization

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
