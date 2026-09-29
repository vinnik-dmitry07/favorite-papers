##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Latent Recurrent Thoughts: Recurrent Refinement of Proposed Latents for Reasoning with Frozen LLMs

###### Abstract

Chain-of-thought reasoning unfolds in discrete token space: each step is committed as text, errors propagate, and eliciting good traces presupposes traces to imitate. Reasoning instead in a model’s continuous representation space – where intermediate states are vectors rather than words – sidesteps these constraints, but leaves open how those latent states should be computed. We approach this along two axes. First, we keep a large language model (LLM) frozen and use it for what it is already good at – modeling and decoding sequences – while a small auxiliary network supplies continuous latent thoughts as input. Second, we produce those latents by recurrence : a tiny recurrent reasoner refines them over many steps, decoupling the depth of computation from the size of the model, so that the latents are a product of iterative processing rather than a single forward pass. We instantiate this as Latent Recurrent Thoughts (LRT) 1 1 1 Code is available at https://github.com/czl-david/latent-recurrent-thoughts . : a task-dedicated proposer supplies base latents, a recurrent reasoner refines them through bounded residual corrections, and the frozen LLM decodes the answer. On symbolic reasoning with answer supervision but no reasoning traces (Countdown-4, Sudoku) and on natural-language reasoning (HumanEval, MBPP, StrategyQA), LRT substantially outperforms prior frozen-decoder continuous-space reasoning methods under an identical decoder, prompt, data, and training budget, and outperforms non-thinking-mode chain-of-thought prompting on the same backbone at a small fraction of its inference compute.

## 1 Introduction

Large language models (LLMs) solve complex problems by externalizing intermediate steps as chain-of-thought (CoT) traces ( Wei et al., 2022 ; Kojima et al., 2022 ; Nye et al., 2021 ) , and recent systems push this further with sampling, search, and reinforcement learning ( Wang et al., 2023 ; Yao et al., 2023 ; Besta et al., 2024 ; Snell et al., 2025 ; Guo et al., 2025 ) . But CoT reasons in the discrete token space: each step must be verbalized from a fixed vocabulary, generation is autoregressive and error-propagating, and – most limiting – eliciting good CoT presupposes reasoning traces to imitate ( Zelikman et al., 2022 ; Brown et al., 2020 ) . This motivates reasoning that instead operates in a model’s continuous representation space.

Such continuous-space reasoning feeds latent vectors back into the model rather than decoded tokens ( Hao et al., 2025 ; Cheng and Van Durme, 2024 ; Su et al., 2025 ; Shen et al., 2025 ) , and existing methods realize it in many ways. One practical path – attractive when fine-tuning a capable LLM is too costly or risks catastrophic forgetting – keeps the decoder frozen : a small auxiliary model produces instance-conditioned latents that are injected into its input as soft tokens – the interface used by prefix and prompt tuning ( Li and Liang, 2021 ; Lester et al., 2021 ) . SoftCoT ( Xu et al., 2025b ) and EBM-CoT ( Chen et al., 2025b ) take this route, and so does our method.

Within this frozen-decoder approach, two components govern quality: the proposer that supplies the latents and the refiner that improves them. SoftCoT proposes with a frozen generic language assistant and performs no refinement at all; EBM-CoT keeps that proposer and adds a refiner that descends a learned scalar energy field, nudging latents toward lower-energy, “consistent” regions. We find both fragile. Off the natural-language substrate, a generic assistant’s proposed latents can be worse than no latents – they actively mislead the decoder – whereas a small proposer dedicated to the task family helps. And an energy refiner only follows the gradient of a fixed scalar field: it calibrates latents rather than computing with them, too shallow for multi-step search.

We introduce Latent Recurrent Thoughts (LRT) , which strengthens both links. A task-dedicated proposer, conditioned on the input x x , supplies base latents adapted to the task family; a recurrent reasoner then refines them – we use TRM ( Jolicoeur-Martineau, 2025 ) , a tiny recursive network that iteratively updates a latent state. Unlike an energy model, a recurrent reasoner applies a learned vector-valued transition that can implement constraint propagation and iterative correction, and can be unrolled to greater depth at no extra parameter cost. It predicts bounded residual corrections rather than regenerating the latent, keeping refinement anchored to the proposed base. Such recurrent reasoners – HRM, TRM, GRAM, EqR ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ; Baek et al., 2026 ; Huang et al., 2026 ) – have proven to be powerful and parameter-efficient computation engines, but they have so far been built only as standalone solvers trained from scratch on a single task. LRT instead pairs one with a frozen, pretrained LLM: the recurrent reasoner carries the iterative computation, while the LLM contributes the broad sequence-modeling and language ability that a from-scratch solver lacks. To our knowledge, this pairing is new.

SoftCoT, EBM-CoT, and LRT all inject latents through the identical interface into the same frozen LLM (Qwen3-8B; Yang et al., 2025 ), so the proposer and refiner are the only variables and comparisons are controlled. We evaluate on two substrates. Symbolic tasks – Countdown-4 and Sudoku – have answer supervision but no reasoning traces : the search that solves an instance is never recorded, so it cannot be imitated and must instead be carried out as latent computation. Natural-language tasks – HumanEval, MBPP, and StrategyQA – are the home turf of soft-CoT methods. The split is stark. On the natural-language tasks SoftCoT and EBM-CoT improve modestly over a zero-shot CoT baseline and LRT improves further; but on Countdown-4 both baselines collapse – to 5.9 % 5.9\% and 8.4 % 8.4\% , far below the 30.0 % 30.0\% of zero-shot CoT – whereas LRT reaches 56.7 % 56.7\% . Off the natural-language substrate a generic proposer is not merely suboptimal but actively destructive, and only a task-dedicated proposer paired with a recurrent refiner converts latent injection back into a consistent gain.

Two scoping notes frame these numbers, and we state them here rather than in the limitations alone. First, LRT trains its proposer and refiner per task family : it is a per-task-trained latent augmentation of a frozen decoder, not a single zero-shot general model, so its comparison class is other trained frozen-decoder modules at a matched budget. Second, the CoT baselines are prompted and training-free, and run Qwen3-8B in non-thinking mode so that their inference budget is comparable. § 4.3 adds thinking mode as a labeled reference point: it beats LRT on three of the five benchmarks while spending roughly 5 5 – 450 × 450\times more inference compute. Our claim is about how far a small recurrent latent module carries a frozen decoder at a fixed, small inference cost – not that latent reasoning dominates test-time scaling.

## 2 Related Work

#### Chain-of-thought and test-time compute.

CoT prompting elicits multi-step reasoning by having the model emit intermediate steps ( Wei et al., 2022 ; Kojima et al., 2022 ; Nye et al., 2021 ) , and many methods improve it by spending inference compute: self-consistency aggregates sampled traces ( Wang et al., 2023 ) , tree- and graph-structured search organizes them ( Yao et al., 2023 ; Besta et al., 2024 ) , and compute-optimal or RL-trained reasoners scale the process further ( Snell et al., 2025 ; Guo et al., 2025 ) . All of these reason in the discrete token space and lean on reasoning traces for supervision ( Zelikman et al., 2022 ; Brown et al., 2020 ) – a dependence that is itself the motivation for moving reasoning off the token substrate.

#### Continuous-space reasoning.

A complementary line moves reasoning into a model’s latent space, feeding back vectors rather than decoded tokens. The most direct is hidden-state recurrence : Coconut feeds the decoder’s last hidden state back as the next input embedding, so that one continuous thought can hold a superposition of alternative continuations ( Hao et al., 2025 ) ; theory shows this lets a shallow transformer explore graph-reachability problems in parallel, whereas discrete CoT must proceed sequentially ( Zhu et al., 2025a ) . A second family compresses explicit CoT into dense vectors: contemplation tokens ( Cheng and Van Durme, 2024 ) , self-distillation into continuous space ( Shen et al., 2025 ) , interleaved latent and text tokens ( Su et al., 2025 ) , and a latent head whose compression rate is tuned by reinforcement learning ( Tan et al., 2025 ) ; a training-free variant decodes probability-weighted mixtures of token embeddings as “concept tokens” ( Zhang et al., 2025 ) . Related mechanisms add computation rather than verbalize it: implicit-CoT absorbs rationales by distillation or curricula ( Deng et al., 2023 ; Deng et al., 2024 ) , pause and filler tokens grant extra forward computation without emitting content ( Goyal et al., 2024 ; Pfau et al., 2024 ) , and recurrent-depth pretraining unrolls layers at inference ( Geiping et al., 2025 ) ; Chen et al. (2025a) and Zhu et al. (2025b) survey the area. Almost all of these pretrain or fine-tune the backbone, leaving open how to obtain useful latents when the decoder must stay fixed.

#### Latent conditioning with a frozen decoder.

Closest to our setting are methods that keep the decoder frozen and train only a small module supplying latents, sidestepping both the cost of fine-tuning a capable LLM and the catastrophic-forgetting risk it carries. SoftCoT runs a frozen generic assistant LM to produce soft thoughts injected as input embeddings ( Xu et al., 2025b ) , and SoftCoT++ adds test-time scaling by sampling and aggregating several such thoughts ( Xu et al., 2025a ) ; EBM-CoT keeps that proposer and calibrates its soft thoughts by descending a learned scalar energy field ( Chen et al., 2025b ) . Differentiable cache augmentation instead trains an offline “coprocessor” that writes latent embeddings into the frozen decoder’s key–value cache in one forward pass ( Liu et al., 2025 ) . All share LRT’s frozen-decoder interface but differ in how the latents arise: each obtains them from a single feed-forward proposal, at most nudged by an energy gradient, rather than from multi-step computation unfolding through a recurrent model. LRT departs on exactly this axis, replacing the generic proposer with a task-dedicated encoder and adding a recurrent reasoner that refines the latents through many bounded residual updates before decoding.

#### Recurrent and recursive reasoning.

Latent recurrence – applying a shared transition repeatedly to a persistent state – underlies Universal and Looped Transformers ( Dehghani et al., 2019 ; Giannou et al., 2023 ) and deep equilibrium models ( Bai et al., 2019 ) , decoupling computation depth from parameter count. Recent recursive reasoners revisit it for structured tasks: HRM couples two recurrent modules at different timescales ( Wang et al., 2025 ) , TRM simplifies recursion to a single tiny network ( Jolicoeur-Martineau, 2025 ) , GRAM makes it stochastic and multi-trajectory ( Baek et al., 2026 ) , and EqR frames reasoning as convergence to task-conditioned attractors ( Huang et al., 2026 ) . Each is a standalone solver trained from scratch on one task with no language ability of its own; LRT instead repurposes one (TRM) as a refiner conditioning a frozen pretrained LLM, so that iterative latent computation and broad sequence modeling come from separate components.

#### Iterative reasoning in specialized models.

A separate line builds models that reason by iterative refinement, but outside the language-model paradigm. Energy-based reasoners cast inference as optimization over a learned energy landscape, by iterative energy minimization ( Du et al., 2022 ) , by annealing a learned sequence of energy functions ( Du et al., 2024 ) , or by composing separately learned energy terms ( Du et al., 2020 ) . Discrete-diffusion reasoners such as MGDM ( Ye et al., 2025 ) refine an entire candidate solution in parallel rather than left to right. These models are strong on structured symbolic problems but each is trained from scratch for a single task family on a fixed symbolic interface; extending them to open-ended natural-language reasoning is a standing challenge. LRT keeps their iterative-refinement principle while inheriting language ability for free, by attaching a recurrent reasoner to a frozen pretrained LLM rather than building a solver from scratch.

## 3 Method

### 3.1 Problem Setup

We target reasoning with a frozen decoder. Let ℳ \mathcal{M} be a pretrained autoregressive LLM with parameters θ \theta and token embedding table E ∈ ℝ | V | × d E\in\mathbb{R}^{|V|\times d} ( d = 4096 d{=}4096 ; we use Qwen3-8B). A problem instance is a tokenized question x x with gold answer y y . SoftCoT, EBM-CoT, and LRT share a common structure: a small model produces K K continuous latent vectors L ∈ ℝ K × d L\in\mathbb{R}^{K\times d} from x x , places them in ℳ \mathcal{M} ’s input as soft tokens immediately after the question, and lets ℳ \mathcal{M} autoregressively decode the answer. The decoder is never updated; only the modules that produce L L are trained, and only through the cross-entropy of ℳ \mathcal{M} ’s output (§ 3.5 ).

The three methods differ solely in how L L is produced. SoftCoT uses (proposer, refiner) = = (frozen generic assistant LM, none); EBM-CoT keeps that proposer and adds an energy-based refiner; LRT replaces both, pairing a task-dedicated encoder with a recurrent reasoner. We write the LRT pipeline as L ( 0 ) \displaystyle L^{(0)} = g ψ ( x ) , L ⋆ = L ( 0 ) + r ϕ ( L ( 0 ) ) , \displaystyle=g_{\psi}(x),\qquad L^{\star}=L^{(0)}+r_{\phi}\big(L^{(0)}\big), y ^ \displaystyle\hat{y} = ℳ ⁡ ( I , x , L ⋆ ) , \displaystyle=\mathcal{M}\big(I,\,x,\,L^{\star}\big), where g ψ g_{\psi} is the proposer (§ 3.2 ), r ϕ r_{\phi} the refiner (§ 3.3 ), and I I a task instruction; Figure 1 shows the full pipeline. Because the injection site and the frozen decoder are identical across all three methods, accuracy differences isolate the proposer and the refiner. All trainable modules operate in a small working dimension d ′ = 256 d^{\prime}{=}256 .

### 3.2 Task-Dedicated Proposer

#### Motivation.

SoftCoT obtains L L as the last-layer hidden states of a frozen generic assistant LM run on [ I assist ; x ; [UNK] × K ] [\,I_{\text{assist}};\,x;\,\texttt{[UNK]}^{\times K}\,] . A block of K K placeholder tokens appended to a prompt is off-distribution for a pretrained assistant, which therefore acts as little more than a fixed featurizer – most severely when x x is short, as with the handful of integers in a Countdown instance, where the placeholders dominate. We therefore discard the generic assistant and learn a small encoder purpose-built to emit latents for ℳ \mathcal{M} .

#### Architecture.

The proposer g ψ g_{\psi} is a bidirectional Transformer encoder. It encodes the bare question x x – with no task instruction, since a model trained from scratch has no instruction-following prior to invoke. The tokens of x x are embedded with the frozen decoder’s table E E , so the proposer and ℳ \mathcal{M} share an input geometry at no parameter cost; a trainable map P ↓ : ℝ d → ℝ d ′ \mathrm{P}_{\!\downarrow}:\mathbb{R}^{d}\!\to\!\mathbb{R}^{d^{\prime}} (its output scaled by d ′ \sqrt{d^{\prime}} ) reduces these embeddings to the working dimension. We append K K learnable query vectors and process the length- ( | x | + K ) (|x|{+}K) sequence with two bidirectional blocks (self-attention + + SwiGLU), so the queries attend to the whole problem and to one another, then read the K K query positions out and lift them back to the decoder’s embedding space with a trainable P ↑ : ℝ d ′ → ℝ d \mathrm{P}_{\!\uparrow}:\mathbb{R}^{d^{\prime}}\!\to\!\mathbb{R}^{d} , giving L ( 0 ) ∈ ℝ K × d L^{(0)}\in\mathbb{R}^{K\times d} . Producing all K K latents in one bidirectional pass mirrors SoftCoT’s single-pass proposal, isolating the proposer architecture as the variable under study.

#### Cost.

The proposer adds ≈ 4.2 {\approx}\,4.2 M trainable parameters ( P ↓ \mathrm{P}_{\!\downarrow} 1.0 1.0 M, query vectors 8 8 K, two blocks ≈ 2.2 {\approx}\,2.2 M, P ↑ \mathrm{P}_{\!\uparrow} 1.0 1.0 M) – essentially the budget SoftCoT already spends on its assistant-to-decoder projection alone.

### 3.3 Recurrent Refiner

The base latents L ( 0 ) L^{(0)} are produced in a single forward pass and are not themselves the product of multi-step computation. The refiner r ϕ r_{\phi} supplies that computation: it is the recursive reasoning module of TRM ( Jolicoeur-Martineau, 2025 ) , repurposed to iteratively improve a set of latents rather than to solve a puzzle end to end.

#### States and updates.

The refiner maintains two states in the working dimension – a fast scratch state z L z_{L} and a slow integrating state z H z_{H} , both in ℝ K × d ′ \mathbb{R}^{K\times d^{\prime}} – initialized from learned, input-independent buffers. The proposed latents enter as an external signal u = P ↓ ′ ​ ( L ( 0 ) ) ∈ ℝ K × d ′ u=\mathrm{P}^{\prime}_{\!\downarrow}(L^{(0)})\in\mathbb{R}^{K\times d^{\prime}} , where P ↓ ′ \mathrm{P}^{\prime}_{\!\downarrow} is a down-projection separate from the proposer’s. One high-level cycle performs T T fast updates followed by a single slow update (we write T T , not L L , to avoid collision with the latents L L ), z L \displaystyle z_{L} ← f ( z L , z H + u ) ( × T ) , \displaystyle\leftarrow f\big(z_{L},\;z_{H}+u\big)\qquad(\times T), z H \displaystyle z_{H} ← f ⁡ ( z H , z L ) , \displaystyle\leftarrow f\big(z_{H},\;z_{L}\big), where f f is a single transition block – of the same class as the proposer’s, with independent weights – applied recursively, as in TRM. Crucially, u u is re-injected at every fast update – not only at initialization – so refinement stays anchored to the problem while z H z_{H} integrates the scratch state across cycles. After unrolling, the refined latents are formed as a bounded residual correction to the proposed base: Δ = P ↑ ′ ​ ( z H ) ∈ ℝ K × d , L ⋆ = L ( 0 ) + Δ . \Delta=\mathrm{P}^{\prime}_{\!\uparrow}\big(z_{H}\big)\in\mathbb{R}^{K\times d},\qquad L^{\star}=L^{(0)}+\Delta. Predicting the correction Δ \Delta rather than regenerating L ⋆ L^{\star} keeps the refiner tied to the instance-conditioned proposal; a light penalty λ ​ ∥ Δ ∥ 2 \lambda\lVert\Delta\rVert^{2} with λ = 0.01 \lambda{=}0.01 (§ 3.5 ) discourages drift toward a generic, instance-agnostic latent.

#### Truncated-gradient unrolling.

Following TRM, the refiner is unrolled deeply but trained cheaply (Algorithm 1 ). We run S S outer iterations of H H high-level cycles each; every cycle but the last runs under stop-gradient, advancing z L , z H z_{L},z_{H} without building a computation graph, so backpropagation traverses only the final cycle while the preceding unroll merely warms up the latent state. Unlike TRM’s adaptive-computation variant, which supervises every step, we take the cross-entropy once , on the final L ⋆ L^{\star} . Gradients flow from ℳ \mathcal{M} ’s answer logits – through the frozen decoder, whose activations are differentiated but whose weights are untouched – into L ⋆ L^{\star} , Δ \Delta , the refiner and – in Stage 1 – the proposer.

#### Cost.

The refiner adds ≈ 7 {\approx}\,7 M trainable parameters, comparable to EBM-CoT’s energy module. LRT’s two modules together total ≈ 11 {\approx}\,11 M trainable parameters; the 8 8 B-parameter decoder is frozen throughout, so LRT trains fewer than 0.2 % 0.2\% of the parameters it reasons with.

### 3.4 Injection and Decoding

Following SoftCoT, ℳ \mathcal{M} receives the concatenation [ I ; x ; L ⋆ ] [\,I;\,x;\,L^{\star}\,] : a task instruction I I and the question x x mapped to input embeddings through E E , followed by the K K refined latents as additional input embeddings. Because P ↑ ′ \mathrm{P}^{\prime}_{\!\uparrow} and the residual already output in ℝ d \mathbb{R}^{d} , L ⋆ L^{\star} needs no further projection. The instruction supplies the decoder’s instruction-following prior and L ⋆ L^{\star} the instance-specific reasoning; θ \theta is never modified.

### 3.5 Training and Inference

#### Two-stage training.

LRT is trained in two stages, each optimizing a single module against the cross-entropy of the frozen decoder; gradients pass through ℳ \mathcal{M} ’s activations but never update θ \theta . Stage 1 trains the proposer alone: the base latents L ( 0 ) L^{(0)} are injected directly, as [ I ; x ; L ( 0 ) ] [I;x;L^{(0)}] , and g ψ g_{\psi} is optimized so that ℳ \mathcal{M} decodes the correct answer. Stage 2 freezes g ψ g_{\psi} and trains the refiner on ℒ = ℒ CE ​ ( ℳ ⁡ ( I , x , L ⋆ ) , y ) + λ ​ ∥ Δ ∥ 2 , \mathcal{L}=\mathcal{L}_{\text{CE}}\big(\mathcal{M}(I,x,L^{\star}),\,y\big)\;+\;\lambda\,\lVert\Delta\rVert^{2}, the answer cross-entropy under the refined latents plus the residual penalty of § 3.3 , with λ = 0.01 \lambda{=}0.01 . Since g ψ g_{\psi} is frozen, each instance’s base latents L ( 0 ) L^{(0)} are precomputed once and cached, so Stage 2 needs no forward pass through the proposer. Across both stages the only supervision is the final answer – or, for StrategyQA, the answer with its reference rationale – and never a record of the search that produced it.

#### Refiner unrolling.

We unroll the refiner for S = 3 S{=}3 outer iterations of H = 3 H{=}3 high-level cycles; each cycle applies T = 4 T{=}4 fast updates and one slow update – five passes through the transition block – for 3 × 3 × 5 = 45 3{\times}3{\times}5{=}45 passes in total. As described in § 3.3 , only the final cycle (five passes) is differentiated; the preceding 40 40 run under stop-gradient, and the cross-entropy is taken once, on L ⋆ L^{\star} .

#### Inference.

At test time the proposer emits its query latents and we keep the first K infer = 4 K_{\text{infer}}{=}4 before the refiner – a train/inference asymmetry ( K = 32 K{=}32 during training) adopted from EBM-CoT, whose latent-count ablation peaks near four. The refiner then runs the full S × H S{\times}H recursion (no stop-gradient is needed without a backward pass), and ℳ \mathcal{M} greedy-decodes the answer from [ I ; x ; L ⋆ ] [I;x;L^{\star}] . Optimization hyperparameters are reported with the experiments.

## 4 Experiments

### 4.1 Experimental Setup

#### Benchmarks.

We evaluate on two families of reasoning tasks. The symbolic family stresses computation away from the natural-language substrate: Countdown-4 (CD4), in which four integers must be combined with arithmetic operations to reach a target value ( Gandhi et al., 2024 ) , and Sudoku , 9 × 9 9{\times}9 constraint-satisfaction puzzles ( Ye et al., 2025 ) . Both supply answer supervision but no ground-truth search traces. The natural-language family comprises HumanEval ( Chen et al., 2021 ) and MBPP ( Austin et al., 2021 ) – Python function synthesis from docstrings – and StrategyQA ( Geva et al., 2021 ) , yes/no questions requiring implicit multi-step reasoning.

#### Metrics.

We report exact solve rate on Countdown-4 and Sudoku, pass@1 on HumanEval and MBPP, and accuracy on StrategyQA. All values are percentages. Table 1 reports mean ± \pm standard deviation over three random seeds; the ablation tables report single-seed values. Avg. is an unweighted mean, over the five benchmarks unless a caption states otherwise.

#### Backbone and baselines.

Every LLM-based method uses the same frozen Qwen3-8B decoder ( Yang et al., 2025 ) . Table 1 compares two groups under this single controlled setting. The first adds no trainable parameters: Zero-Shot CoT ( Kojima et al., 2022 ) (henceforth zero-shot CoT) and a Direct (no CoT) baseline that answers without intermediate steps. The second is the family of trained frozen-decoder latent modules to which LRT belongs: SoftCoT ( Xu et al., 2025b ) and EBM-CoT ( Chen et al., 2025b ) , 2 2 2 EBM-CoT has no official implementation; the EBM-CoT results reported here are from our own reproduction of the method as described by Chen et al. (2025b) and may deviate from the authors’ intended setup. which – like LRT – keep the decoder frozen and train only a small latent module. All of these share LRT’s interface exactly – same decoder, same prompt, same training data and budget – so the latent module is the only variable. Appendix C adds two parameter-efficient prompt-adaptation controls at a matched ≈ 11 {\approx}11 M trainable budget, Prefix-tuning ( Li and Liang, 2021 ) and P-tuning v2 ( Liu et al., 2022 ) , which test whether task supervision plus trainable soft prompts alone reproduce LRT’s gain; they do not.

#### What is deliberately not a baseline, and why.

Three families are excluded by design rather than oversight. (i) Methods that update decoder weights – Coconut ( Hao et al., 2025 ) , CODI ( Shen et al., 2025 ) , Token-Assorted ( Su et al., 2025 ) , and adapter- or LoRA-style tuning ( Houlsby et al., 2019 ; Hu et al., 2022 ) – leave the frozen-decoder setting that defines our study, and fine-tuning is known to degrade strong instruction-tuned backbones ( Xu et al., 2025b ) . (ii) Test-time scaling such as self-consistency ( Wang et al., 2023 ) and SoftCoT++ ( Xu et al., 2025a ) is orthogonal: it aggregates predictions from whatever base method is used, so it composes with LRT rather than competing. (iii) From-scratch symbolic solvers (MGDM, TRM, EqR) cannot process natural language at all, and appear in Table 2 as reference points. Comparisons crossing these boundaries are informative but uncontrolled, and labeled as such throughout.

#### Reproduction and harness notes.

Three details affect how the baseline numbers should be read; Appendix B states them in full. EBM-CoT has no official implementation, so its rows are our reproduction, validated against the authors’ reported StrategyQA result ( 70.96 70.96 vs. 71.04 71.04 ours). The CoT baselines run Qwen3 in non-thinking mode for budget comparability, which departs substantially from the official technical-report numbers; we validated the harness by reproducing the official MBPP result with thinking mode on. TRM is not natively a sequence-to-sequence model, so Countdown-4 required an adaptation of our own, whose limits we state in § 4.3 .

#### Training.

LRT is trained in the two stages of § 3.5 ; hyperparameters are in Appendix A .

### 4.2 Main Results

Table 1 reports results across all five benchmarks.

#### Symbolic reasoning.

The symbolic benchmarks expose a sharp failure of the existing latent-injection methods. On Countdown-4, SoftCoT and EBM-CoT reach only 5.9 5.9 and 8.4 8.4 – far below both the no-reasoning Direct baseline ( 27.8 27.8 ) and zero-shot CoT ( 30.0 30.0 ) – and the same ordering recurs on Sudoku. Injecting latents from a generic assistant is thus not merely unhelpful off the natural-language substrate but actively destructive, corroborating the diagnosis of § 3.2 . LRT reverses this: with a task-dedicated proposer and a recurrent refiner it reaches 56.7 56.7 on Countdown-4 and 49.2 49.2 on Sudoku, the only frozen-decoder method to improve over zero-shot CoT on either task, and by a wide margin ( + 26.7 +26.7 and + 25.3 +25.3 points). On Countdown-4 it even surpasses MGDM ( 52.0 52.0 ; Table 2 ), a diffusion model trained from scratch specifically for symbolic decoding.

#### Natural-language reasoning.

On HumanEval, MBPP, and StrategyQA – the substrate for which soft-thought methods were designed – latent injection behaves as intended: SoftCoT and EBM-CoT both improve over Direct prompting and zero-shot CoT. LRT is strongest on all three (e.g. 37.8 37.8 vs. 25.0 25.0 for EBM-CoT on HumanEval), showing that a task-dedicated proposer and a recurrent refiner help even where the generic pipeline already works. Averaged over the five benchmarks, LRT reaches 54.1 54.1 , against 33.5 33.5 for EBM-CoT and 35.0 35.0 for zero-shot CoT; notably, SoftCoT’s average ( 29.5 29.5 ) falls below the no-reasoning Direct baseline ( 30.9 30.9 ), as its symbolic collapse cancels its natural-language gains. Empirically, we observed that both SoftCoT and EBM-CoT collapse to predicting a near-uniform latent across instances, which may in part explain the sharp drop in performance. Note that injecting a constant latent is not the same as direct decoding, since those vectors still play a non-trivial part in the model’s attention patterns.

### 4.3 Reference Points Outside the Controlled Setting

Table 1 holds the decoder, prompt, data, and budget fixed. Three comparisons that break one of those controls are nonetheless informative, and we report them separately so that they are not mistaken for baselines.

#### Thinking-mode prompting.

In thinking mode with Qwen3’s recommended sampling and a 32,768 32{,}768 -token budget, the same backbone reaches 85.3 85.3 on Countdown-4 and 92.1 92.1 on HumanEval, well above LRT; LRT leads on Sudoku ( 49.2 49.2 vs. 0.5 0.5 ) and MBPP ( 51.5 51.5 vs. 49.3 49.3 ), and thinking mode edges ahead on StrategyQA ( 76.4 76.4 vs. 75.1 ± 2.3 75.1\pm 2.3 , within one standard deviation) – while spending 8.9 8.9 – 453.9 453.9 TFLOP per example against LRT’s ≈ 1 {\approx}1 – 2 2 . Two things follow. Our claim must be read as scoped: LRT outperforms prompted, non-thinking CoT at a fraction of its cost, not test-time scaling in general. But a weak prompting setup cannot explain the main result either, since SoftCoT and EBM-CoT use the same decoder, prompts, data, and budget as LRT and reach 5.9 5.9 and 8.4 8.4 on Countdown-4. It is also notable that the task where thinking mode spends the most compute, Sudoku, is exactly where it fails ( 0.5 0.5 ) while a 7 7 M recurrent refiner reaches 49.2 49.2 : token-space search is not a substitute for iterative computation on a constraint-satisfaction substrate.

#### From-scratch symbolic solvers.

MGDM and TRM solve Sudoku almost perfectly ( 96.9 96.9 , 97.2 97.2 ) and EqR essentially completely ( 99.8 99.8 ), far above LRT’s 49.2 49.2 . We state this plainly: on Sudoku a specialized solver is much better than LRT, and the frozen-decoder route trades peak symbolic accuracy for one method that also handles language. Two observations qualify the comparison rather than rescue it. First, these models do not transfer: trained from scratch for symbolic decoding, they have no language interface at all. Second, their competence is uneven: TRM, the very reasoner LRT adopts as its refiner, scores 1.2 1.2 on Countdown-4 despite near-solving Sudoku. We attribute this partly to task structure: Countdown-4 admits an unusually sequential solution, a chain of arithmetic operations applied in order, which a from-scratch model with no sequence-modeling prior struggles to capture, whereas Sudoku suits TRM’s grid recurrence. The honest caveat is that TRM does not natively support sequence-to-sequence tasks; our adaptation (Appendix B ) is simple and stronger ones may exist. The central point survives: without some sequential prior, TRM struggles on a fundamentally sequential task, and LRT is built around exactly this division of labor.

#### Parameter-efficient prompt adaptation.

At a trainable budget matched to LRT’s ≈ 11 {\approx}11 M, prefix-tuning reaches 12.5 12.5 and P-tuning v2 28.4 28.4 on Countdown-4 (Appendix C ), the latter merely matching the no-latent Direct baseline ( 27.8 27.8 ): task supervision plus trainable soft prompts do not by themselves produce the gain. Making the injected vectors instance-conditioned adds + 13.6 +13.6 (to 42.0 42.0 ), and recurrent refinement a further + 14.7 +14.7 (to 56.7 56.7 ).

### 4.4 Scaling the Recurrent Refiner

In LRT the decoder is frozen, so all learned computation lives in the proposer and the refiner – and of the two, the refiner is where the iterative reasoning happens, making its capacity a natural lever. Table 1 uses a 7 7 M refiner, chosen for parity with EBM-CoT’s energy module (§ 3.3 ); we now enlarge it while everything else is held fixed .

Figure 2 scales the TRM refiner across 7 7 M, 14 14 M, and 28 28 M parameters and measures Countdown-4 and HumanEval. Both improve monotonically: Countdown-4 rises from 56.7 56.7 to 66.3 66.3 to 69.1 69.1 , and HumanEval from 37.8 37.8 to 44.0 44.0 to 46.1 46.1 . The gains are largest at the first doubling ( + 9.6 +9.6 and + 6.2 +6.2 points) and taper at 28 28 M ( + 2.8 +2.8 and + 2.1 +2.1 ). Crucially, the improvement is bought entirely with refiner capacity: the 8 8 B decoder never changes. Reasoning quality thus scales with the recurrent reasoner that carries the computation, separately from the LLM that supplies sequence modeling, and the 7 7 M setting used elsewhere is a conservative, parameter-matched operating point with clear headroom.

### 4.5 Mechanistic Ablations

The comparison in § 4.2 varies two things at once: relative to LRT, SoftCoT and EBM-CoT each swap both the proposer (task-dedicated → \rightarrow generic) and the refiner. We now isolate the two components.

#### Factorial decomposition.

LRT pairs a proposer and a refiner (§ 3.2 , § 3.3 ), so the natural ablation is the 2 × 3 2{\times}3 grid over proposer ∈ { \in\{ generic assistant, task-dedicated } \} and refiner ∈ { \in\{ none, energy, recurrent } \} . SoftCoT, EBM-CoT, and LRT are three of its six cells; Table 3 fills the rest, and two of the three new cells correspond to alternative pairings a reader might expect: task-dedicated + none is SoftCoT with our proposer substituted, and task-dedicated + energy is EBM-CoT with our proposer substituted. All six cells are reported. Holding the refiner at none , swapping the generic assistant for a task-dedicated proposer lifts the average from 12.3 12.3 to 37.2 37.2 ; holding the proposer task-dedicated, the recurrent refiner contributes roughly three times the energy refiner’s gain ( + 10.7 +10.7 vs. + 3.4 +3.4 ). The two also interact – the recurrent refiner adds + 10.7 +10.7 on a task-dedicated proposer but only + 9.3 +9.3 on a generic one, and on Countdown-4 every generic-proposer cell stays below the Direct baseline ( 27.8 27.8 ) whatever the refiner. Neither component alone accounts for LRT: the proposer must place the base latents on a usable manifold before the refiner can compute over them.

#### Depth versus capacity.

§ 4.4 scaled the refiner by parameters ; we now vary depth at fixed parameters (Appendix E ). A non-recurrent refiner with the same 7 7 M budget but a single feed-forward pass reaches only 47.5 / 33.0 47.5/33.0 on Countdown-4/HumanEval against LRT’s 56.7 / 37.8 56.7/37.8 ; and a refiner trained at S = H = 3 S{=}H{=}3 but unrolled deeper at test time only keeps improving, indicating a convergent iterative process rather than a fixed-length circuit.

#### Refinement is incremental.

Decoding the answer after each high-level cycle (Appendix G ) shows accuracy climbing monotonically across the unroll rather than appearing only at the final step, while the residual ∥ L ( t ) − L ( t − 1 ) ∥ \lVert L^{(t)}-L^{(t-1)}\rVert contracts toward a fixed point: the refiner performs incremental, convergent computation, not one-shot calibration. Appendix D confirms each design choice earns its place – regenerating L ⋆ L^{\star} instead of the residual Δ \Delta , or injecting the base only at initialization, each costs 3 3 – 4 4 average points.

### 4.6 Where Does the Computation Happen?

LRT combines a recurrent reasoner with a frozen LLM, inviting a natural worry: is the gain simply TRM, with the LLM reduced to a transcription device? Four measurements bound the answer from both sides.

TRM alone does not do the work. As a standalone solver it scores 1.2 1.2 on Countdown-4 against LRT’s 56.7 56.7 and cannot address the natural-language benchmarks at all (Table 2 ): on four of five benchmarks TRM alone is not merely worse but inapplicable, Sudoku being the exception noted in § 4.3 . The refiner needs on-manifold latents. The same refiner applied to latents from a generic proposer reaches only 14.8 14.8 on Countdown-4 (Table 3 ), below the no-latent Direct baseline of 27.8 27.8 : recurrence is not a free-standing engine, and anchoring it in the decoder’s representation space is what makes it useful. The decoder is load-bearing. Swapping it changes results meaningfully – 54.1 54.1 , 51.8 51.8 , 49.0 49.0 average for Qwen3-8B, Llama-3.1-8B, Qwen3-4B (Appendix H ) – and removing the instruction I I at inference costs 3.4 3.4 points (Appendix F ); neither should matter much if the decoder merely transcribed a finished answer, since any of these backbones can verbalize one. The answer is not sitting in the latent. A linear probe on cached L ⋆ L^{\star} predicting whether the decoder will solve the instance reaches 57.5 % 57.5\% against a 52.5 % 52.5\% majority baseline, with unrefined latents at chance (Appendix G ); even the outcome, let alone the answer string, is only weakly linearly readable. Nor can the answer have been memorized: Countdown-4 evaluation holds out targets.

This evidence is convergent but correlational: a linear probe bounds only linearly decodable information, and the decoder-swap argument presumes comparable verbalization ability across backbones. We claim the computation is distributed across refiner and decoder rather than concentrated in either, not that we have measured the split.

## 5 Conclusion

We presented Latent Recurrent Thoughts (LRT), which reasons with a frozen LLM by pairing a task-dedicated proposer with a TRM-based recurrent refiner, training fewer than 0.2 % 0.2\% of the parameters involved: the proposer maps a problem to base latents the frozen decoder can use, and the refiner computes over them, emitting a bounded residual correction. Across symbolic and natural-language reasoning LRT improves substantially over prior frozen-decoder latent-injection methods under an identical decoder, prompt, data, and budget, and over budget-matched zero-shot CoT; neither component suffices alone, and the computation is distributed across refiner and decoder rather than carried by either (§ 4.6 ). The result is scoped – modules are trained per task family, and large test-time budgets remain stronger on some tasks – but within it, a small recurrent module in front of a frozen LLM supplies much of the computation chain-of-thought otherwise externalizes.

## Limitations

#### Per-task modules, and what that costs the claim.

LRT keeps the decoder frozen but trains a proposer and a refiner against it, per task family. It is therefore not a single general model applied zero-shot: each new task requires training new modules, and the method is best described as per-task-trained latent augmentation of a frozen decoder rather than a general reasoning method. This bounds the fair comparison class: the controlled comparison in Table 1 is against other trained frozen-decoder latent modules, and comparisons to prompting are reported at matched inference budget, with thinking-mode prompting reported separately as an unmatched reference point (§ 4.3 ). Training additionally relies on answer supervision and, for the symbolic benchmarks, on the ability to generate synthetic training sets – though Appendix C shows 1,000 1{,}000 Countdown-4 examples already reach 52.7 52.7 , so the requirement is for some answer-labeled data rather than a great deal of it. Tasks where even that is unavailable remain out of reach.

#### Generalization is within-task, not across tasks.

Our Countdown-4 evaluation holds out targets, so the reported accuracy does reflect systematic generalization to unseen instances rather than memorization. But we have not tested transfer across tasks or difficulty levels: whether modules trained on Countdown-4 help on harder Countdown variants, or Sudoku modules on Kakuro, is untested and we make no claim about it. The per-task protocol matches SoftCoT and EBM-CoT, which makes the comparison controlled but leaves cross-task generality an open question for all three.

#### Scope of evaluation.

Our experiments use a single 8 8 B-parameter decoder and five benchmarks. Appendix H varies the decoder, but all backbones are of comparable scale; whether the division of labor between a frozen decoder and a small recurrent reasoner holds at substantially larger scales, or across broader task distributions, remains open. The parameter-efficient controls of Appendix C were run on Countdown-4 only.

#### Method caveats.

On Sudoku, symbolic-specialized solvers remain far ahead of LRT (Table 2 ); the frozen-decoder route trades peak symbolic accuracy for a single method that also handles natural language. The refiner’s recurrent unroll adds inference compute that grows with depth (Appendices E and I ). Our mechanistic analyses (§ 4.5 , § 4.6 , Appendix G ) are correlational: the monotone intermediate-decoding curve, the contracting latent residual, and the weakly-above-baseline linear probe are evidence about where computation happens, not proof, and the probe in particular bounds only linear decodability.

## References

Austin et al. (2021) J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, and C. Sutton Program synthesis with large language models . arXiv preprint arXiv:2108.07732 . External Links: Link Cited by: §K.1 , §4.1 .

Baek et al. (2026) J. Baek, M. Jo, M. Kim, M. Ren, Y. Bengio, and S. Ahn Generative recursive reasoning . arXiv preprint arXiv:2605.19376 . External Links: Link Cited by: §1 , §2 .

Bai et al. (2019) S. Bai, J. Z. Kolter, and V. Koltun Deep equilibrium models . In Advances in Neural Information Processing Systems (NeurIPS) , External Links: Link Cited by: Appendix G , §2 .

Besta et al. (2024) M. Besta, N. Blach, A. Kubicek, R. Gerstenberger, M. Podstawski, L. Gianinazzi, J. Gajda, T. Lehmann, H. Niewiadomski, P. Nyczyk, and T. Hoefler Graph of thoughts: solving elaborate problems with large language models . In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 38 , pp. 17682–17690 . External Links: Link Cited by: §1 , §2 .

Brown et al. (2020) T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, et al. Language models are few-shot learners . In Advances in Neural Information Processing Systems (NeurIPS) , External Links: Link Cited by: §1 , §2 .

Chen et al. (2021) M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al. Evaluating large language models trained on code . arXiv preprint arXiv:2107.03374 . External Links: Link Cited by: §K.1 , §K.1 , §4.1 .

Chen et al. (2025a) X. Chen, A. Zhao, H. Xia, X. Lu, H. Wang, Y. Chen, W. Zhang, J. Wang, W. Li, and X. Shen Reasoning beyond language: a comprehensive survey on latent chain-of-thought reasoning . arXiv preprint arXiv:2505.16782 . External Links: Link Cited by: §2 .

Chen et al. (2025b) Z. Chen, S. Cui, D. Ye, Y. Zhang, Y. Bian, and T. Zhu Think consistently, reason efficiently: energy-based calibration for implicit chain-of-thought . arXiv preprint arXiv:2511.07124 . External Links: Link Cited by: §K.1 , Appendix B , §1 , §2 , §4.1 , Table 1 , footnote 2 .

Cheng and Van Durme (2024) J. Cheng and B. Van Durme Compressed chain of thought: efficient reasoning through dense representations . arXiv preprint arXiv:2412.13171 . External Links: Link Cited by: §1 , §2 .

Dehghani et al. (2019) M. Dehghani, S. Gouws, O. Vinyals, J. Uszkoreit, and L. Kaiser Universal transformers . In International Conference on Learning Representations (ICLR) , External Links: Link Cited by: §2 .

Deng et al. (2024) Y. Deng, Y. Choi, and S. Shieber From explicit CoT to implicit CoT: learning to internalize CoT step by step . arXiv preprint arXiv:2405.14838 . External Links: Link Cited by: §2 .

Deng et al. (2023) Y. Deng, K. Prasad, R. Fernandez, P. Smolensky, V. Chaudhary, and S. Shieber Implicit chain of thought reasoning via knowledge distillation . arXiv preprint arXiv:2311.01460 . External Links: Link Cited by: §2 .

Du et al. (2020) Y. Du, S. Li, and I. Mordatch Compositional visual generation with energy based models . In Advances in Neural Information Processing Systems (NeurIPS) , External Links: Link Cited by: §2 .

Du et al. (2022) Y. Du, S. Li, J. B. Tenenbaum, and I. Mordatch Learning iterative reasoning through energy minimization . In International Conference on Machine Learning (ICML) , External Links: Link Cited by: §2 .

Du et al. (2024) Y. Du, J. Mao, and J. B. Tenenbaum Learning iterative reasoning through energy diffusion . In International Conference on Machine Learning (ICML) , External Links: Link Cited by: §2 .

Gandhi et al. (2024) K. Gandhi, D. Lee, G. Grand, M. Liu, W. Cheng, A. Sharma, and N. D. Goodman Stream of search (SoS): learning to search in language . In Conference on Language Modeling (COLM) , External Links: Link Cited by: Appendix A , §K.1 , §4.1 .

Geiping et al. (2025) J. Geiping, S. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein Scaling up test-time compute with latent reasoning: a recurrent depth approach . In Advances in Neural Information Processing Systems (NeurIPS) , pp. 41340–41391 . External Links: Link Cited by: Appendix G , §2 .

Geva et al. (2021) M. Geva, D. Khashabi, E. Segal, T. Khot, D. Roth, and J. Berant Did Aristotle use a laptop? a question answering benchmark with implicit reasoning strategies . Transactions of the Association for Computational Linguistics (TACL) 9 , pp. 346–361 . External Links: Document , Link Cited by: §K.1 , §4.1 .

Giannou et al. (2023) A. Giannou, S. Rajput, J. Sohn, K. Lee, J. D. Lee, and D. Papailiopoulos Looped transformers as programmable computers . In International Conference on Machine Learning (ICML) , pp. 11398–11442 . External Links: Link Cited by: §2 .

Goyal et al. (2024) S. Goyal, Z. Ji, A. S. Rawat, A. K. Menon, S. Kumar, and V. Nagarajan Think before you speak: training language models with pause tokens . In International Conference on Learning Representations (ICLR) , External Links: Link Cited by: §2 .

Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, et al. DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning . Nature 645 , pp. 633–638 . External Links: Document , Link Cited by: §1 , §2 .

Hao et al. (2025) S. Hao, S. Sukhbaatar, D. Su, X. Li, Z. Hu, J. Weston, and Y. Tian Training large language models to reason in a continuous latent space . In Conference on Language Modeling (COLM) , External Links: Link Cited by: §1 , §2 , §4.1 .

Houlsby et al. (2019) N. Houlsby, A. Giurgiu, S. Jastrzebski, B. Morrone, Q. de Laroussilhe, A. Gesmundo, M. Attariyan, and S. Gelly Parameter-efficient transfer learning for NLP . In International Conference on Machine Learning (ICML) , External Links: Link Cited by: §4.1 .

Hu et al. (2022) E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen LoRA: low-rank adaptation of large language models . In International Conference on Learning Representations (ICLR) , External Links: Link Cited by: §4.1 .

Huang et al. (2026) B. Huang, Z. Geng, and J. Z. Kolter Equilibrium reasoners: learning attractors enables scalable reasoning . In International Conference on Machine Learning (ICML) , External Links: Link Cited by: Appendix G , §1 , §2 , Table 2 .

Jolicoeur-Martineau (2025) A. Jolicoeur-Martineau Less is more: recursive reasoning with tiny networks . arXiv preprint arXiv:2510.04871 . External Links: Link Cited by: §K.1 , §1 , §2 , §3.3 , Table 2 .

Kojima et al. (2022) T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa Large language models are zero-shot reasoners . In Advances in Neural Information Processing Systems (NeurIPS) , External Links: Link Cited by: §1 , §2 , §4.1 .

Lester et al. (2021) B. Lester, R. Al-Rfou, and N. Constant The power of scale for parameter-efficient prompt tuning . In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP) , pp. 3045–3059 . External Links: Document , Link Cited by: §1 .

Li and Liang (2021) X. L. Li and P. Liang Prefix-tuning: optimizing continuous prompts for generation . In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL) , pp. 4582–4597 . External Links: Document , Link Cited by: Appendix C , Table 7 , §1 , §4.1 .

Liu et al. (2025) L. Liu, J. Pfeiffer, J. Wu, J. Xie, and A. Szlam Deliberation in latent space via differentiable cache augmentation . In International Conference on Machine Learning (ICML) , pp. 39261–39274 . External Links: Link Cited by: §2 .

Liu et al. (2022) X. Liu, K. Ji, Y. Fu, W. Tam, Z. Du, Z. Yang, and J. Tang P-Tuning: prompt tuning can be comparable to fine-tuning across scales and tasks . In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) , pp. 61–68 . External Links: Document , Link Cited by: Appendix C , Table 7 , §4.1 .

Nye et al. (2021) M. Nye, A. J. Andreassen, G. Gur-Ari, H. Michalewski, J. Austin, D. Bieber, D. Dohan, A. Lewkowycz, M. Bosma, D. Luan, C. Sutton, and A. Odena Show your work: scratchpads for intermediate computation with language models . arXiv preprint arXiv:2112.00114 . External Links: Link Cited by: §1 , §2 .

Pfau et al. (2024) J. Pfau, W. Merrill, and S. R. Bowman Let’s think dot by dot: hidden computation in transformer language models . In Conference on Language Modeling (COLM) , External Links: Link Cited by: §2 .

Shen et al. (2025) Z. Shen, H. Yan, L. Zhang, Z. Hu, Y. Du, and Y. He CODI: compressing chain-of-thought into continuous space via self-distillation . In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP) , pp. 677–693 . External Links: Link Cited by: §1 , §2 , §4.1 .

Snell et al. (2025) C. Snell, J. Lee, K. Xu, and A. Kumar Scaling LLM test-time compute optimally can be more effective than scaling parameters for reasoning . In International Conference on Learning Representations (ICLR) , External Links: Link Cited by: §1 , §2 .

Su et al. (2025) D. Su, H. Zhu, Y. Xu, J. Jiao, Y. Tian, and Q. Zheng Token assorted: mixing latent and text tokens for improved language model reasoning . In International Conference on Machine Learning (ICML) , pp. 57144–57163 . External Links: Link Cited by: §1 , §2 , §4.1 .

Tan et al. (2025) W. Tan, J. Li, J. Ju, Z. Luo, R. Song, and J. Luan Think silently, think fast: dynamic latent compression of LLM reasoning chains . In Advances in Neural Information Processing Systems (NeurIPS) , pp. 4646–4668 . External Links: Link Cited by: §2 .

Wang et al. (2025) G. Wang, J. Li, Y. Sun, X. Chen, C. Liu, Y. Wu, M. Lu, S. Song, and Y. Abbasi Yadkori Hierarchical reasoning model . arXiv preprint arXiv:2506.21734 . External Links: Link Cited by: §1 , §2 .

Wang et al. (2023) X. Wang, J. Wei, D. Schuurmans, Q. V. Le, E. H. Chi, S. Narang, A. Chowdhery, and D. Zhou Self-consistency improves chain of thought reasoning in language models . In International Conference on Learning Representations (ICLR) , External Links: Link Cited by: §1 , §2 , §4.1 .

Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. H. Chi, Q. V. Le, and D. Zhou Chain-of-thought prompting elicits reasoning in large language models . In Advances in Neural Information Processing Systems (NeurIPS) , External Links: Link Cited by: §1 , §2 .

Xu et al. (2025a) Y. Xu, X. Guo, Z. Zeng, and C. Miao SoftCoT++: test-time scaling with soft chain-of-thought reasoning . arXiv preprint arXiv:2505.11484 . External Links: Link Cited by: §2 , §4.1 .

Xu et al. (2025b) Y. Xu, X. Guo, Z. Zeng, and C. Miao SoftCoT: soft chain-of-thought for efficient reasoning with LLMs . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 23336–23351 . External Links: Link Cited by: §K.1 , §1 , §2 , §4.1 , §4.1 , Table 1 .

Yang et al. (2025) A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, et al. Qwen3 technical report . arXiv preprint arXiv:2505.09388 . External Links: Link Cited by: §K.1 , §1 , §4.1 .

Yao et al. (2023) S. Yao, D. Yu, J. Zhao, I. Shafran, T. L. Griffiths, Y. Cao, and K. Narasimhan Tree of thoughts: deliberate problem solving with large language models . In Advances in Neural Information Processing Systems (NeurIPS) , External Links: Link Cited by: §1 , §2 .

Ye et al. (2025) J. Ye, J. Gao, S. Gong, L. Zheng, X. Jiang, Z. Li, and L. Kong Beyond autoregression: discrete diffusion for complex reasoning and planning . In International Conference on Learning Representations (ICLR) , External Links: Link Cited by: Appendix A , §K.1 , §2 , §4.1 , Table 2 .

Zelikman et al. (2022) E. Zelikman, Y. Wu, J. Mu, and N. D. Goodman STaR: bootstrapping reasoning with reasoning . In Advances in Neural Information Processing Systems (NeurIPS) , External Links: Link Cited by: §1 , §2 .

Zhang et al. (2025) Z. Zhang, X. He, W. Yan, A. Shen, C. Zhao, S. Wang, Y. Shen, and X. E. Wang Soft thinking: unlocking the reasoning potential of LLMs in continuous concept space . In Advances in Neural Information Processing Systems (NeurIPS) , pp. 168990–169012 . External Links: Link Cited by: §2 .

Zhu et al. (2025a) H. Zhu, S. Hao, Z. Hu, J. Jiao, S. Russell, and Y. Tian Reasoning by superposition: a theoretical perspective on chain of continuous thought . In Advances in Neural Information Processing Systems (NeurIPS) , pp. 79931–79963 . External Links: Link Cited by: §2 .

Zhu et al. (2025b) R. Zhu, T. Peng, T. Cheng, X. Qu, J. Huang, D. Zhu, H. Wang, K. Xue, X. Zhang, Y. Shan, et al. A survey on latent reasoning . arXiv preprint arXiv:2507.06203 . External Links: Link Cited by: §2 .

## Appendix A Implementation and Training Details

#### Architecture.

The proposer is a bidirectional encoder: an input projection P ↓ \mathrm{P}_{\!\downarrow} maps decoder embeddings of x x to working width d ′ = 256 d^{\prime}{=}256 , two pre-norm transformer blocks attend over K = 32 K{=}32 learned query vectors appended to the sequence, and an output projection P ↑ \mathrm{P}_{\!\uparrow} returns the K K base latents to decoder width d d . The refiner reuses one transition block of the same class (with independent weights) as f f , together with projections P ↓ ′ , P ↑ ′ \mathrm{P}^{\prime}_{\!\downarrow},\mathrm{P}^{\prime}_{\!\uparrow} and learned initial buffers z L 0 , z H 0 z_{L}^{0},z_{H}^{0} . Table 4 breaks down the trainable parameters; the Qwen3-8B decoder is frozen throughout, so LRT trains 11.2 11.2 M parameters, about 0.14 % 0.14\% of the model it reasons with.

#### Optimization.

Both stages use AdamW ( β 1 = 0.9 \beta_{1}{=}0.9 , β 2 = 0.999 \beta_{2}{=}0.999 , ϵ = 10 − 8 \epsilon{=}10^{-8} ) with a cosine learning-rate schedule, 5 % 5\% linear warmup, weight decay 0.01 0.01 , and gradient clipping at 1.0 1.0 , in bfloat16 . Stage 1 trains the proposer at peak learning rate 3 × 10 − 4 3{\times}10^{-4} ; Stage 2 trains the refiner at 2 × 10 − 4 2{\times}10^{-4} . Both run for 30 30 epochs at batch size 64 64 on a single 96 96 GB GPU, with gradient checkpointing. Table 5 collects the hyperparameters.

#### Datasets.

Table 6 lists sizes and splits. Countdown-4 instances are generated following Gandhi et al. (2024) and Sudoku puzzles following Ye et al. (2025) ; HumanEval, MBPP, and StrategyQA use their public splits. Countdown-4 evaluation holds out targets : no target value in the test set appears in training, so the reported accuracy reflects generalization to unseen targets rather than fitting the synthetic distribution.

#### What the supervision consists of.

The claim that LRT trains without reasoning traces is scoped to the symbolic benchmarks, and we state the full picture here. Countdown-4 and Sudoku are supervised strictly by the final answer; the search that produces it is never recorded and never used. StrategyQA is the one exception: in the main results its target text is the answer together with the dataset’s reference rationale, following prior work. Evaluation is unaffected – StrategyQA is scored by exact match on the normalized yes/no answer only, never on the rationale. To remove any ambiguity, we also trained StrategyQA with answer-only supervision: it reaches 76.9 76.9 , against 75.1 ± 2.3 75.1\pm 2.3 for the rationale-supervised setting reported in Table 1 . The rationale is therefore not necessary for LRT’s result, and no benchmark in this paper depends on trace supervision.

#### Inference.

At test time the proposer emits its K = 32 K{=}32 query latents and the first K infer = 4 K_{\text{infer}}{=}4 are kept (Table 13 ); the refiner runs the full S × H S{\times}H recursion with no stop-gradient, and the decoder greedy-decodes the answer from [ I ; x ; L ⋆ ] [I;x;L^{\star}] .

## Appendix B Reproduction and Harness Notes

#### Baseline reproduction.

SoftCoT is reproduced from the authors’ released code; EBM-CoT, which has no public implementation, is reproduced from the description of Chen et al. (2025b) . Both use the same frozen Qwen3-8B decoder, the same assistant model for their generic proposer, and the same stage-wise training budget as LRT, so differences reflect the latent module rather than the backbone or compute. To check the faithfulness of the EBM-CoT reproduction we compare on StrategyQA, the one benchmark shared with the original paper: 70.96 70.96 reported by Chen et al. (2025b) against 71.04 71.04 for our reproduction. Reproduced numbers may nonetheless deviate from the authors’ intended setup on the benchmarks they did not report.

#### Thinking versus non-thinking mode.

Qwen3 exposes a “thinking” mode that emits a long internal trace before answering. All rows of Table 1 use non-thinking mode so that the prompted baselines and the latent methods spend comparable inference compute; this departs substantially from the official technical-report numbers, especially on the coding tasks. To verify that the deviation reflects the mode rather than a harness bug, we re-ran with thinking mode enabled and reproduced the official MBPP figure. Those runs appear as reference points in Table 2 and are discussed in § 4.3 .

Thinking-mode runs use Qwen3’s recommended sampling with a 32,768 32{,}768 -token budget ( 38,912 38{,}912 for Sudoku), and Countdown-4, Sudoku, and MBPP use fixed random test subsets ( n = 300 / 200 / 300 n{=}300/200/300 ) to bound the compute spent. Two entries in Table 2 carry footnotes. The Sudoku result ( 0.5 0.5 ) is not a truncation artifact: only 8 8 of 200 200 generations were cut off before emitting an answer, so thinking-mode accuracy is bounded at ≤ 4.5 % {\leq}4.5\% even if all eight would have been correct; the remaining generations produced complete but constraint-violating grids. The MBPP result is name-normalized, because the bare MBPP prompt does not pin the required function name and raw extraction therefore under-scores thinking mode.

#### Adapting TRM to Countdown-4.

Countdown-4 is a sequence-to-sequence task in which x x (four input integers and a target) and y y (a sequence of arithmetic expressions) occupy different spaces. This differs from Sudoku, where TRM operates on the input grid directly and the output shares the input’s shape. To adapt TRM we construct a padded sequence [ x , PAD ] [x,\text{PAD}] , so that the model attends to the x x tokens through bidirectional attention and writes its answer into the pad positions. This is a natural but not necessarily optimal construction, and TRM’s low Countdown-4 score should be read with that caveat (§ 4.3 ); a natively sequential TRM is left to future work.

## Appendix C Parameter-Efficient Baselines and Data Efficiency

#### Do soft prompts alone explain the gain?

A natural alternative hypothesis is that LRT’s improvement comes from task supervision plus trainable parameters in the decoder’s input, rather than from instance-conditioned latent computation. Table 7 tests this directly on Countdown-4 with two parameter-efficient prompt-adaptation methods trained on the same data at a matched ≈ 11 {\approx}11 M trainable budget. Prefix-tuning ( Li and Liang, 2021 ) reaches 12.5 12.5 and P-tuning v2 ( Liu et al., 2022 ) reaches 28.4 28.4 – the latter essentially matching the no-latent Direct baseline ( 27.8 27.8 ). Both are instance-independent : they learn one prompt shared by every problem. Making the injected vectors instance-conditioned adds + 13.6 +13.6 (task-dedicated proposer alone, 42.0 42.0 ), and refining them recurrently adds a further + 14.7 +14.7 ( 56.7 56.7 ). The gain therefore requires conditioning on the instance and computing over that conditioning, not merely spending parameters at the input.

We report Countdown-4 only, as it is the benchmark that separates the methods most sharply; extending these controls to the remaining four benchmarks is straightforward but was not run.

#### Is the gain bought with 100k synthetic examples?

The symbolic training sets contain 100,000 100{,}000 generated instances, which raises the question of whether LRT’s symbolic result is a data-scale artifact. Table 8 varies the Countdown-4 training-set size while holding everything else fixed. The curve is close to flat: 52.7 52.7 at 1,000 1{,}000 examples against 56.7 56.7 at 100,000 100{,}000 – two orders of magnitude more data for 4.0 4.0 points. (The small non-monotonicity between 1 1 k and 5 5 k is within seed noise.) Two comparisons make the point sharper. First, SoftCoT and EBM-CoT are trained on the same 100,000 100{,}000 examples and reach 5.9 5.9 and 8.4 8.4 : the data is available to them and does not help. Second, LRT at 1,000 1{,}000 examples ( 52.7 52.7 ) already exceeds every other frozen-decoder method trained on 100,000 100{,}000 . The natural-language benchmarks are low-resource to begin with – MBPP has 374 374 training examples and StrategyQA 2,061 2{,}061 (Table 6 ) – and LRT is trained on those splits as given.

## Appendix D Refiner Design Ablations

Table 9 ablates the refiner’s design; each run holds the proposer, decoder, and training recipe fixed at the Table 1 setting and changes one component. Replacing the residual parameterization L ⋆ = L ( 0 ) + Δ L^{\star}{=}L^{(0)}{+}\Delta with direct regeneration of L ⋆ L^{\star} removes the anchor to the instance-conditioned proposal and costs 3.9 3.9 average points. Injecting the proposed base u u only at refiner initialization – rather than at every fast update – costs 3.2 3.2 points, as the fast state drifts away from the problem. Collapsing the two-timescale state ( z L , z H ) (z_{L},z_{H}) to a single state costs 2.6 2.6 points. Full backpropagation through all 45 45 passes, rather than truncating to the final cycle, leaves accuracy essentially unchanged ( − 0.1 -0.1 ) while raising training memory ≈ 6 × {\approx}6\times and step time ≈ 3 × {\approx}3\times relative to the truncated variant; truncated unrolling is therefore the better operating point.

Table 10 sweeps the residual penalty λ \lambda of § 3.5 . With λ = 0 \lambda{=}0 the residual Δ \Delta grows large and the refined latents drift toward a generic, instance-agnostic point; with λ = 1.0 \lambda{=}1.0 the penalty suppresses Δ \Delta almost entirely and LRT collapses toward the proposer-only result. The value λ = 0.01 \lambda{=}0.01 used throughout sits at the optimum.

## Appendix E Scaling and Depth

#### Test-time depth extrapolation.

Table 11 takes the refiner trained at S = H = 3 S{=}H{=}3 ( 9 9 cycles) and unrolls it for more cycles at inference only . Accuracy continues to improve, consistent with the learned transition approximating a convergent process; we did not train a refiner at those depths for comparison.

#### Non-recurrent control.

Table 12 replaces the recurrent refiner with a non-weight-tied feed-forward refiner of equal ( 7 7 M) parameter count. At matched capacity it trails the recurrent refiner by 6.1 6.1 average points, isolating recurrence – not parameters – as the source of the gain.

#### Latent count and width.

Table 13 sweeps the inference latent count K infer K_{\text{infer}} (with K = 32 K{=}32 fixed in training) and the working width d ′ d^{\prime} . K infer = 4 K_{\text{infer}}{=}4 is best, confirming on our setup the train/inference asymmetry adopted from EBM-CoT; accuracy saturates at d ′ = 256 d^{\prime}{=}256 , with d ′ = 512 d^{\prime}{=}512 adding refiner parameters for a negligible gain.

#### Why K = 32 K{=}32 in training but K infer = 4 K_{\text{infer}}{=}4 at test?

We characterize this asymmetry from both directions. The training count matters and the inference count does not, much. Training with K = 4 K{=}4 instead of 32 32 – matching train and test – collapses Countdown-4 to 9.5 9.5 . Inspection shows well-formed but incorrect expressions rather than truncated output, so this is a capacity failure, not a decoding artifact: the 32 32 query positions act as scratch space inside the proposer’s bidirectional pass, shaping the four that are read out even though the rest are discarded. In the other direction, keeping more latents at inference degrades the five-benchmark average mildly and monotonically – 54.1 54.1 , 53.8 53.8 , 52.9 52.9 , 51.8 51.8 at K infer = 4 , 8 , 16 , 32 K_{\text{infer}}{=}4,8,16,32 (Table 13 ) – and every setting stays far above SoftCoT ( 29.5 29.5 ) and EBM-CoT ( 33.5 33.5 ). The effect is therefore robust rather than a knife-edge tuned in LRT’s favour. The protocol is inherited, not chosen post hoc : the train/inference asymmetry and the value 4 4 come from EBM-CoT, whose latent-count ablation peaks near four, and we apply the identical protocol to SoftCoT, EBM-CoT, and LRT.

## Appendix F Training Protocol Ablations

Table 14 ablates the training protocol. Training the proposer and refiner jointly , rather than in the two stages of § 3.5 , costs 3.1 3.1 average points and is less stable, as the refiner adapts to a proposer that is still moving. Leaving the proposer unfrozen during Stage 2 changes little ( − 0.5 -0.5 ), so freezing it – which lets the base latents be cached – is essentially free. Removing the task instruction I I at inference, leaving the decoder to work from L ⋆ L^{\star} alone, costs 3.4 3.4 points: the latents carry instance-specific computation but not the decoder’s instruction-following prior.

## Appendix G Mechanistic Analyses

#### Refinement trajectory.

Figure 3 (a) plots the accuracy of the answer decoded from the latents after each high-level cycle. Accuracy rises smoothly from the proposed base L ( 0 ) L^{(0)} to the final L ⋆ L^{\star} rather than jumping at the last step, so intermediate latents are partially correct and the refiner improves them incrementally.

#### Latent convergence.

Figure 3 (b) tracks the residual ∥ L ( t ) − L ( t − 1 ) ∥ \lVert L^{(t)}-L^{(t-1)}\rVert , which contracts geometrically toward a small value: the unrolled refiner approaches a fixed point. This is the behavior expected when recurrent refinement is viewed as relaxation toward a task-conditioned attractor ( Bai et al., 2019 ; Geiping et al., 2025 ; Huang et al., 2026 ) .

#### What the latents encode.

Decoding each refined latent to its nearest decoder token embedding yields fragments aligned with intermediate reasoning – partial arithmetic for Countdown-4, candidate digits for Sudoku – rather than fluent text, consistent with L ⋆ L^{\star} carrying computation in a form the decoder consumes but does not verbalize.

#### Linear probe on the refined latents.

To test more directly whether the answer is already present in L ⋆ L^{\star} and the decoder merely transcribes it (§ 4.6 ), we cache the refined latents for the Countdown-4 test set and fit a logistic-regression probe on the flattened K infer × d K_{\text{infer}}{\times}d representation to predict a binary label: whether the frozen decoder subsequently solves the instance. The probe is fit on an 80 / 20 80/20 train/test split of the cached latents, with ℓ 2 \ell_{2} regularization selected by cross-validation on the training portion, and evaluated on the held-out 20 % 20\% . It reaches 57.5 % 57.5\% accuracy against a 52.5 % 52.5\% majority-class baseline; the same probe on the unrefined L ( 0 ) L^{(0)} is at chance. Refinement therefore writes some outcome-relevant information into the latent, but only weakly linearly readable information – and predicting whether the instance will be solved is a far easier target than the answer string itself. Because Countdown-4 test targets are held out (Appendix A ), the answer also cannot have been memorized into the latent from training. We report this as bounding evidence, not proof: a linear probe measures linear decodability only, and a non-linear reader might extract more.

#### Why generic latents collapse.

Table 15 reports the frozen decoder’s negative log-likelihood of the reference answer on Countdown-4 under different latent sources. Latents from a generic assistant proposer raise NLL above the no-latent baseline – they actively mislead the decoder – whereas task-dedicated and refined latents lower it. The mean cosine similarity of each latent to its nearest decoder input embedding shows why: generic latents land far off the decoder’s input manifold, while task-dedicated and refined latents stay close to it.

## Appendix H Generality Across Decoders

Table 16 swaps the frozen decoder. LRT remains far above the frozen-decoder baselines of Table 1 for every backbone, and a stronger decoder yields a stronger LRT, consistent with the division of labor in which the decoder supplies the sequence prior and the trained modules supply iterative computation.

## Appendix I Compute and Efficiency

Table 17 compares inference cost. LRT injects only K infer = 4 K_{\text{infer}}{=}4 latent vectors and decodes the answer directly, against the ≈ 210 {\approx}210 chain-of-thought tokens zero-shot CoT must generate; the 45 45 refiner passes act on a 7 7 M-parameter block and add little next to a single forward pass of the 8 8 B decoder. Net latency is below zero-shot CoT despite the added recursion.

#### Training cost.

Table 18 reports the training side, which the inference table above does not cover. Both stages run for 30 30 epochs at batch size 64 64 on a single 96 96 GB GPU. The dominant cost is the forward pass through the frozen 8 8 B decoder, not the 11 11 M trainable modules; because Stage 2 freezes the proposer, the base latents L ( 0 ) L^{(0)} are precomputed once and cached, so Stage 2 skips the proposer’s forward pass entirely. Truncated-gradient unrolling is what keeps the deep recursion affordable: full backpropagation through all 45 45 passes raises peak training memory ≈ 6 × {\approx}6\times and step time ≈ 3 × {\approx}3\times for a 0.1 0.1 -point accuracy difference (Appendix D ), so truncation is strictly the better operating point rather than an accuracy compromise.

## Appendix J Potential Risks

As with any research involving large language models, our work carries a risk of misuse: the techniques we present could, in principle, be adapted to generate malicious code or other harmful outputs. This concern is heightened for a project focused specifically on enhancing the reasoning capabilities of LLMs, since stronger reasoning may also amplify a model’s capacity to produce sophisticated harmful content.

## Appendix K Licenses, Parameters, and Intended Use of Artifacts

This work uses several existing scientific artifacts – pretrained language models, baseline code, software packages, and evaluation datasets – and produces new artifacts of its own. We record below the license or terms of use of each artifact, the implementation and parameter settings of the packages we rely on, and confirm that our use is consistent with the intended use under which each artifact was released. We also state the intended use of the artifacts we create and its compatibility with the original access conditions.

### K.1 Existing Artifacts

#### Pretrained models.

The frozen decoders are used under their respective open-weight licenses. Qwen3-8B and Qwen3-4B ( Yang et al., 2025 ) are released under the Apache License 2.0, and Llama-3.1-8B is used under the Llama 3.1 Community License Agreement. The TRM recurrent reasoner ( Jolicoeur-Martineau, 2025 ) , which we repurpose as the LRT refiner, is released by its authors under the MIT License. All of these licenses permit use, reproduction, modification, and redistribution for research purposes. These models were released as general-purpose research artifacts for studying and building language and reasoning systems, and our use of them – as a frozen decoder and a refiner module within an academic study of latent reasoning – is consistent with that stated intended use.

#### Baseline code.

We reproduce SoftCoT ( Xu et al., 2025b ) from the authors’ publicly released implementation, which is distributed under the NTUITIVE Dual License Agreement (a non-commercial license that permits use, reproduction, modification, and distribution of derivative works for academic research purposes). Our use is strictly for non-commercial academic research and is therefore consistent with these terms. EBM-CoT ( Chen et al., 2025b ) has no public implementation; our results come from an independent reimplementation written by us from the method description, and we release it under the same license as our own code.

#### Evaluation datasets.

HumanEval ( Chen et al., 2021 ) is released under the MIT License, and MBPP ( Austin et al., 2021 ) under the Creative Commons Attribution 4.0 International License (CC BY 4.0). StrategyQA ( Geva et al., 2021 ) is distributed for research use under the terms accompanying its public release; we use only its public split. Each of these datasets was created and released as a benchmark for evaluating the reasoning ability of NLP systems, and we use them solely for benchmark evaluation in an academic study – the use for which they were intended and distributed. We use each dataset through its standard public split and do not redistribute the underlying data.

#### Generated data.

The Countdown-4 and Sudoku training and evaluation sets are synthetically generated by us following the public procedures of Gandhi et al. (2024) and Ye et al. (2025) , respectively. They contain no third-party or human-authored content and are not derived from any access-restricted source.

#### Software packages and parameter settings.

All training is implemented in PyTorch ( torch 2.11.0+cu128) and built on the Hugging Face transformers library (4.57.6), with accelerate 1.10.1, einops 0.8.1, and xformers 0.0.35; numerical and data utilities use numpy 2.4.4, scipy 1.16.2, scikit-learn 1.7.2, and pydantic 2.11.7. The Qwen3 and Llama-3.1 decoders are loaded together with their official pretrained tokenizers, and questions are tokenized with each decoder’s native tokenizer using default settings; no additional text normalization or stemming is applied. Optimization uses the AdamW implementation from PyTorch with the hyperparameters reported in Appendix A ( β 1 = 0.9 \beta_{1}{=}0.9 , β 2 = 0.999 \beta_{2}{=}0.999 , ϵ = 10 − 8 \epsilon{=}10^{-8} , weight decay 0.01 0.01 , gradient clipping 1.0 1.0 , cosine schedule with 5% warmup). Inference is served with SGLang ( sglang 0.5.12, flashinfer 0.6.11.post1, flash-attn 4.0.0b14, httpx 0.28.1); all reported results use greedy decoding, so no sampling temperature, top- p p , or top- k k parameters apply. For evaluation, pass@1 on HumanEval and MBPP is computed with the official human-eval execution harness ( Chen et al., 2021 ) with k = 1 k{=}1 , and a problem counts as solved only if the greedily decoded function passes all provided unit tests in the harness’s sandbox. Exact solve rate on Countdown-4 and Sudoku is computed by our own checker, which verifies that the decoded answer satisfies the task constraints (a valid arithmetic expression reaching the target, or a complete and consistent Sudoku grid). StrategyQA accuracy is exact match on the normalized yes/no answer. We do not use ROUGE, BLEU, or other learned or n-gram scoring packages. All package versions are pinned in the requirements files released with our code.

### K.2 Artifacts We Create

We release our LRT implementation under the MIT License at https://github.com/czl-david/latent-recurrent-thoughts . The intended use of these artifacts is non-commercial research on latent reasoning and frozen-decoder methods; this is stated explicitly in the accompanying documentation. This intended use is compatible with the access conditions of every artifact our work builds upon: the permissive licenses of Qwen3, TRM, HumanEval, and the baseline code allow research reuse and redistribution, the Llama 3.1 Community License permits research use subject to its attribution and naming requirements, and the CC BY 4.0 terms of MBPP permit reuse with attribution. Our released artifacts do not include or redistribute the MBPP, HumanEval, or StrategyQA data themselves; they consist only of our own code, our trained module weights, and synthetic data we generated. Consistent with the principle that derivatives of data accessed for research purposes should remain within research contexts, we restrict the distributed artifacts to research use and require any derivative works to retain compatible, research-oriented terms.

## Appendix L Use of AI Assistants

We used an AI-based coding assistant for minor, non-substantive help during implementation, limited to routine tasks such as autocompletion, boilerplate code, and debugging suggestions. We also used an AI writing assistant to check grammar and improve the clarity of phrasing in the manuscript.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
