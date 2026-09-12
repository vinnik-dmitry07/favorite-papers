##### Report GitHub Issue

Content selection saved. Describe the issue below:

# A Mechanistic Analysis of Looped Reasoning Language Models

###### Abstract

Reasoning has become a central capability in large language models. Recent research has shown that reasoning performance can be improved by looping an LLM’s layers in the latent dimension, resulting in looped reasoning language models . Despite promising results, few works have investigated how their internal dynamics differ from those of standard feedforward models. In this paper, we conduct a mechanistic analysis of the latent states in looped language models, focusing in particular on how the stages of inference observed in feedforward models compare to those observed in looped ones. To this end, we analyze cyclic recurrence and show that for many of the studied models each layer in the cycle converges to a distinct fixed point; consequently, the recurrent block follows a consistent cyclic trajectory in the latent space. We provide evidence that as these fixed points are reached, attention-head behavior stabilizes, leading to constant behavior across recurrences. Empirically, we discover that recurrent blocks learn stages of inference that closely mirror those of feedforward models, repeating these stages in depth with each iteration. We study how recurrent block size, input injection, and normalization influence the emergence and stability of these cyclic fixed points. We believe these findings help translate mechanistic insights into practical guidance for architectural design.

###### Keywords:

\printArXivAffiliationsAndNotice

## 1 Introduction

The vast majority of current LLMs are based on the Transformer architecture ( Vaswani et al., 2017 ) , which comprises a sequence of blocks traversed in a feedforward manner to predict the next token. As the capability of these models increased, attention turned to eliciting reasoning capabilities in LLMs by increasing test-time computation, commonly through chain-of-thought (CoT) prompting ( Wei et al., 2022 ) or reinforcement-learning-based fine-tuning, first popularized in the DeepSeek-R1 architecture ( Guo et al., 2025 ) . More recently, research has explored building reasoning capabilities directly into the model architecture via recurrent looping ( Geiping et al., 2025 ; Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ) , where additional test-time compute is spent by taking more recurrent steps, echoing early designs in this direction ( Graves, 2016 ) . Despite growing empirical success, the mechanisms underlying these models remain poorly understood, as well as their benefits and limitations when compared to feedforward computation.

In this paper, we compare how feedforward and looped LLMs organize computation across (effective) depth through the lens of stages of inference ( Lad et al., 2024 ; Queipo-de-Llano et al., 2025 ) , a perspective suggesting that LLM inference can be decomposed into several distinct computational stages. Building on prior observations that repeated application of a shared recurrent block can approach a fixed point or steady state ( Yang et al., 2023 ; Geiping et al., 2025 ) , we show that such behavior necessarily implies one of two possibilities: either the contribution of the component Transformer blocks vanishes asymptotically, or their sequential application traces out a constant cyclic trajectory in latent space. We further demonstrate empirically that the latter behavior arises in practice when certain architectural conditions are met, and that this appears to be emergent behavior from the Transformer architecture itself, appearing in both trained recurrent models and untrained, randomly initialized models.

## 2 Preliminaries

### 2.1 Looped Transformers

In this section we introduce Looped Transformers and define the notation that we will use throughout the paper. We represent the input sequence to our transformer of length T T and dimension D D as 𝑿 ∈ ℝ T × D {\bm{X}}\in\mathbb{R}^{T\times D} . Following the notation of Yudin et al. (2025) we define Attn \attn , the dot product self-attention mechanism, as a map f : ℝ T × D → ℝ T × D f:\mathbb{R}^{T\times D}\to\mathbb{R}^{T\times D} : Attn ⁡ ( 𝐗 ) \displaystyle\attn({\bm{X}}) = softmax ⁡ ( 𝑿 ​ 𝑾 Q ​ 𝑾 K ⊤ ​ 𝑿 ⊤ d ) ​ 𝑿 ​ 𝑾 V , \displaystyle=\mathrm{softmax}{\left(\frac{{\bm{X}}{\bm{W}}_{Q}{\bm{W}}_{K}^{\top}{\bm{X}}^{\top}}{\sqrt{d}}\right)}{\bm{X}}{\bm{W}}_{V}, (1) = softmax ⁡ ( A ⁡ ( 𝑿 ) ) ​ 𝑿 ​ 𝑾 V , \displaystyle=\mathrm{softmax}{\left(A({\bm{X}})\right)}{\bm{X}}{\bm{W}}_{V}, (2) where 𝑾 Q , 𝑾 K , 𝑾 V ∈ ℝ D × d {\bm{W}}_{Q},{\bm{W}}_{K},{\bm{W}}_{V}\in\mathbb{R}^{D\times d} are projection matrices and A A is defined for convenience.

A transformer block typically comprises an attention mechanism and a position-wise MLP as follows: 𝑿 ^ \displaystyle\hat{{\bm{X}}} = n 2 ​ ( 𝑿 + Attn ⁡ ( n 1 ​ ( 𝐗 ) ) CLOSE , \displaystyle=n_{2}\left({\bm{X}}+\attn(n_{1}({\bm{X}})\right), (3) 𝑿 ′ \displaystyle{{\bm{X}}}^{\prime} = n 4 ​ ( 𝑿 ^ + MLP ​ ( n 3 ​ ( 𝑿 ^ ) ) ) , \displaystyle=n_{4}\left(\hat{{\bm{X}}}+\text{MLP}(n_{3}(\hat{{\bm{X}}}))\right), (4) where n 1 , n 2 , n 3 , n 4 n_{1},n_{2},n_{3},n_{4} are each optional norms – here we are borrowing from the notation of Geiping et al. (2025) . We denote the action of a Transformer block B : ℝ T × D → ℝ T × D \block:\mathbb{R}^{T\times D}\to\mathbb{R}^{T\times D} as 𝑿 ′ = B ⁡ ( 𝑿 ) {\bm{X}}^{\prime}=\block({\bm{X}}) , and refer to the intermediate hidden-state matrices 𝑿 {\bm{X}} between blocks as the residual stream .

Looped Transformers are Transformers that utilize “recurrence in depth” – that is, they reapply layers to repeatedly act on the latent states. Recent research has identified that an effective way ( Bae et al., 2025 ) to achieve this is via cyclic recurrence : a fixed sequence of layers is repeated in a “cyclic” pattern. This is the approach that we focus on in this work, and we introduce it in more detail below. For convenience, we define a k k -stacked block as a composition of Transformer blocks, S k ⁡ ( 𝑿 ) = B k ⁡ ( B k − 1 ⁡ ( … ​ B 1 ⁡ ( 𝑿 ) ​ … ) ) \stack_{k}({\bm{X}})=\block_{k}(\block_{k-1}(\dots\block_{1}({\bm{X}})\dots)) .

In the case of Geiping et al. (2025) ; McLeish et al. (2025) this stacked block may also take an additional input 𝒁 ∈ ℝ T × D {\bm{Z}}\in\mathbb{R}^{T\times D} which is typically initialized from a Normal distribution, as well as the original input to the recurrent section: this is known as input injection ( Bai et al., 2019 ; Anil et al., 2022 ) , and the two inputs are projected into common feature space ℝ D \mathbb{R}^{D} before the block is applied. In the case of input injection, a k k -stacked block therefore becomes S k ⁡ ( 𝑿 , 𝒁 ) = B k ⁡ ( B k − 1 ⁡ ( … ​ B 1 ⁡ ( [ 𝑿 , 𝒁 ] ​ 𝑾 I ) ​ … ) ) , \stack_{k}({\bm{X}},{\bm{Z}})=\block_{k}(\block_{k-1}(\dots\block_{1}([{\bm{X}},{\bm{Z}}]{\bm{W}}_{I})\dots)), (5) where [ ⋅ , ⋅ ] [\cdot,\cdot] denotes concatenation in the channel dimension and 𝑾 I ∈ ℝ 2 ​ D × D {\bm{W}}_{I}\in\mathbb{R}^{2D\times D} is a learned projection matrix.

This allows us to define a ( k ⊗ l ) (k\otimes l) -Recurrent block as a k k -stacked block repeated l l times: R l , k ( 𝑿 ) = S k ( S k ( … S k ( ⏞ × l 𝑿 ) … ) ) , R_{l,k}({\bm{X}})=\overbrace{\stack_{k}(\stack_{k}(\dots\stack_{k}(}^{\times l}{\bm{X}})\dots)), (6)

which with input-injection becomes R l , k ​ ( 𝑿 , 𝒁 ) = OPEN S k ⁡ ( 𝑿 , S k ⁡ ( … ​ 𝑿 , S k ⁡ ( 𝑿 , 𝒁 ) ) ​ … ) ) ⏞ × l . R_{l,k}({\bm{X}},{\bm{Z}})=\overbrace{\stack_{k}({\bm{X}},\stack_{k}(\dots{\bm{X}},\stack_{k}({\bm{X}},{\bm{Z}}))\dots))}^{\times l}. (7)

Note that the input 𝑿 {\bm{X}} is only “injected” at the start of each stack of blocks – once per recurrence. Additionally, a complete looped Transformer may have multiple feedforward layers before the Recurrent block, and multiple feedforward layers after the Recurrent block: following the convention of Geiping et al. (2025) , we refer to these as prelude and coda layers respectively, and these are simply separate stacked blocks with non-tied layer weights. Where prelude and coda are used, we will frequently refer to this as a sandwich block structure.

We combine and adapt the nomenclature of Geiping et al. (2025) ; Saunshi et al. (2025) and refer to a looped Transformer with p p prelude layers, k k recurrent layers and c c coda layers with the tuple ( p , k , c ) (p,k,c) . Where input injection is used, we add an I I subscript ( p , k , c ) I (p,k,c)_{I} , and when referring to a recurrent layer looped a specific number of times l l , we denote this as ( p , k ⊗ l , c ) (p,k\otimes l,c) .

In summary, a ( p , k ⊗ l , c ) (p,k\otimes l,c) looped Transformer is defined as 𝑿 0 \displaystyle{\bm{X}}_{0} ← S p ⁡ ( 𝑿 ) \displaystyle\leftarrow\stack_{p}({\bm{X}}) 𝑿 i \displaystyle{\bm{X}}_{i} ← S k ′ ⁡ ( 𝑿 i − 1 ) i ∈ { 1 , … , l } \displaystyle\leftarrow\stack_{k}^{\prime}({\bm{X}}_{i-1})\qquad i\in\{1,\dots,l\} 𝑿 \displaystyle{\bm{X}} ← S c ′′ ⁡ ( 𝑿 l ) , \displaystyle\leftarrow\stack_{c}^{\prime\prime}({\bm{X}}_{l}), where ′ \prime and ′′ \prime\prime indicates that these are different stacks between which weights are not shared. A ( p , k ⊗ l , c ) I (p,k\otimes l,c)_{I} looped Transformer (with input injection) is defined as 𝑿 \displaystyle{\bm{X}} ← S p ⁡ ( 𝑿 ) \displaystyle\leftarrow\stack_{p}({\bm{X}}) 𝒁 i \displaystyle{\bm{Z}}_{i} ← S k ′ ⁡ ( 𝑿 , 𝒁 i − 1 ) i ∈ { 1 , … , l } \displaystyle\leftarrow\stack_{k}^{\prime}({\bm{X}},{\bm{Z}}_{i-1})\qquad i\in\{1,\dots,l\} 𝑿 \displaystyle{\bm{X}} ← S c ′′ ⁡ ( 𝒁 l ) , \displaystyle\leftarrow\stack_{c}^{\prime\prime}({\bm{Z}}_{l}), where 𝒁 0 {\bm{Z}}_{0} is initialized such that each column is sampled from 𝒩 ⁡ ( 𝟎 , σ 2 ​ 𝕀 D ) \mathcal{N}(\bm{0},\sigma^{2}\mathbb{I}_{D}) .

We will describe our results via grouping : • No grouping : The value is visualized as it evolves through sequential layers of the model, irrespective of whether these layers are repeated.

• By recurrence : Separate lines are visualized for each complete pass through the recurrent block. The x x -axis is typically percentage scaled to represent relative depth within that block (including prelude/coda), allowing us to overlay and compare successive passes. Always presented with a green - yellow colorbar, with later recurrences colored more yellow.

• By layer : Separate lines are visualized for each unique layer, showing how the value evolves across recurrences. Always presented with a blue - green colorbar, with later layers colored more green.

### 2.2 Stages of Inference

The behavior of layers in feedforward Transformers appears to change sharply with depth: Lad et al. (2024) originate the term “stages of inference” and demonstrate how several different layer mechanisms emerge at different depths. Queipo-de-Llano et al. (2025) further develop this viewpoint, focusing on behaviors that can be characterized by the mixing (or lack thereof) induced by the attention heads. We focus on this latter perspective. Mixing in this context refers to the extent to which the attention mechanism incorporates information from previous tokens at each layer. Throughout the main text of this paper we quantify our study of mixing behavior through the ColSum Concentration metric introduced in Queipo-de-Llano et al. (2025) ; we introduce and discuss additional metrics in App. E .

We first define the column sum c j = ∑ i A i ​ j c_{j}=\sum_{i}A_{ij} to capture how much attention mass is received by token j j . We normalize this as c ^ j = c j / T \hat{c}_{j}=c_{j}/T to obtain a probability distribution, noting that ∑ i , j A i ​ j = T \sum_{i,j}A_{ij}=T since A A is row-stochastic. From this distribution, we define the ColSum Concentration via its normalized entropy as C = 1 − H col ∈ [ 0 , 1 ] = 1 + 1 log ⁡ T ​ ∑ j c j ​ log ⁡ c j C=1-H_{\text{col}}\in[0,1]=1+\frac{1}{\log T}\sum_{j}c_{j}\log c_{j} .

Large values of C C indicate a high concentration of attention mass: few columns receive most of the mass. We note therefore that this metric captures the well-studied attention sink ( Xiao et al., 2023 ; Barbero et al., 2025 ) behavior, but generalizes to capture concentration over any token position. This property is useful for our investigation as not all models studied herein exhibit sinks on the first token; in particular OLMo-2 frequently concentrates attention mass on punctuation, echoing a result in Sandoval-Segura et al. (2025) .

## 3 Related Work

#### Looped and Recurrent Transformers

Reusing the same Transformer block for multiple iterations is an idea that has been explored in the literature. This began with the introduction of Universal Transformers ( Dehghani et al., 2018 ) , which have also resulted in sparsified and conditional-computation extensions ( Tan et al., 2023 ; Csordás et al., 2024 ) . Other more recent recurrent style architectures with a higher focus on reasoning-style tasks have been HRM ( Wang et al., 2025 ) and TRM ( Jolicoeur-Martineau, 2025 ) . Within language modeling, we highlight Huginn-0125 ( Geiping et al., 2025 ) , Ouro ( Zhu et al., 2025 ) , and Mixture-of-Recursions ( Bae et al., 2025 ) as models that have been pretrained from random initialization, as well as recent work by ( McLeish et al., 2025 ; Koishekenov et al., 2025 ) that retrofit recurrence into pretrained LLMs.

In terms of mechanistic studies, we highlight Pappone et al. (2025) , who analyze “two-scale” latent dynamics in recurrent Transformers. However, the setting of their analysis is different from ours: they analyse a model in which each recurrent block comprises either 1 or 2 layers, and the model comprises multiple separate recurrent blocks. In this way, the two scales they refer to correspond to the outputs of each iteration of a given recurrent block, and outputs of recurrent blocks when transitioning between different recurrent blocks. We instead study a single looped block with deeper cycles (4+ layers), closer to common looped architectures, and we analyze the internals of these cyclic blocks by examining the latent states of each separate layer. We also highlight work related to looped model expressivity ( Xu and Sato, 2024 ; Saunshi et al., 2025 ) , as well as work on neural network stability and fixed-point dynamics ( Bai et al., 2019 ; Anil et al., 2022 ; Ke et al., 2024 ; Yudin et al., 2025 ) . The only work – of which we are aware – that analyses the internal states of the cyclic recurrent blocks is Lu et al. (2025) , who demonstrate cyclic behavior in logit lens prediction throughout recurrent blocks.

#### Stages of Inference and Attention Dynamics

The idea that LLMs organize their feedforward computation into several distinct stages of inference was first proposed by Lad et al. (2024) . Building on this, Queipo-de-Llano et al. (2025) explain the emergence of these stages through the behavior of attention heads, driven by massive activations ( Sun et al., 2024 ) . We also highlight a complementary line of work that analyzes LLM learning dynamics via attention patterns through the lens of mixing ( Barbero et al., 2024 ; Arroyo et al., 2026 ; Veličković et al., 2024 ; Barbero et al., 2025 ) , motivated by information propagation challenges originally studied in Graph Neural Networks (GNNs) ( Cai and Wang, 2020 ; Alon and Yahav, 2020 ; Arroyo et al., 2025 ; Hariri et al., 2025 ; Blayney et al., 2025 ) .

#### Test-time Computation

Test-time computation broadly refers to giving a model the ability to expend additional computational cycles at inference in proportion to the difficulty of the input, rather than committing to a fixed compute budget for all examples. In this paper, we focus specifically on recurrence as a mechanism for scaling computation at test time, as opposed to alternative strategies such as early-exit architectures ( Schuster et al., 2022 ) or continuous thought machines ( Darlow et al., 2025 ) . Classic approaches to adaptive test-time compute include Adaptive Computation Time ( Graves, 2016 ) and subsequent probabilistic halting frameworks such as PonderNet ( Banino et al., 2021 ) . Building on these foundations, recent work has begun to characterize when additional inference compute actually generalizes beyond training-time budgets ( Schwarzschild et al., 2021 ) , how to mitigate failures due to excessive computation (“overthinking”) ( Bansal et al., 2022 ) , how to ensure stable dynamics with repeated iteration ( Bear et al., 2024 ) , and how looped Transformers can better generalize to out of distribution tasks at test time ( McLeish et al., 2024 ) .

## 4 Looped Transformers Tend Towards the Same Attention Patterns

Recent work ( Bai et al., 2019 ; Bansal et al., 2022 ; Anil et al., 2022 ) has noted that weight-tied Transformer models often tend towards consistent behavior with repeated iterations. Often 1 1 1 As originally observed by Geiping et al. (2025) , other forms of limiting behavior can occur. In App. C we show that 1) this is rare, the vast majority of tokens reach a fixed-point and 2) even with other limiting behavior, stages of inference remain constant. , this takes the form of convergence to a fixed point 𝑿 ′ = S k ⁡ ( 𝑿 ′ ) {\bm{X}}^{\prime}=\stack_{k}({\bm{X}}^{\prime}) . We motivate our work by noting that if this is true for a model with cyclic recurrence, it is also true cyclically:

###### Proposition 4.1 (Cyclic recurrent blocks reach cyclic fixed points) .

Let ( l , k ) (l,k) -Recurrent block reach a fixed point 𝐗 ′ {\bm{X}}^{\prime} such that S k ⁡ ( 𝐗 ′ ) = 𝐗 ′ \stack_{k}({\bm{X}}^{\prime})={\bm{X}}^{\prime} . Then any cyclic permutation of blocks 1 , … , k 1,\dots,k will also have reached a fixed point.

We highlight however that these fixed points are not necessarily the same: the action of each successive layer doesn’t necessarily result in the same point, and the cycle of layers can instead trace out an arbitrary cycle in latent space. Indeed, in Sec. 4.1 we demonstrate that this cyclic fixed point behavior – illustrated in Fig. 1 – is observed frequently in practice. The alternative, where all layers result in the same fixed point, requires that the action of each Transformer block tends to zero.

Convergence to this cyclic behavior implies that the residual stream tends towards being similar across recurrences. Given that block weights are also shared across recurrent iterations -- and assuming that the inputs to each block are bounded 2 2 2 This is a reasonable assumption since all models considered in this work apply a norm before the attention block. – this implies that the attention patterns will converge, as shown in Proposition 4.2 .

###### Proposition 4.2 (Recurrent attention patterns change slowly under state convergence) .

Fix a layer ℓ \ell in the recurrent block and consider its attention weight matrices to be tied across recurrences (so 𝐖 Q , ℓ , 𝐖 K , ℓ {\bm{W}}_{Q,\ell},{\bm{W}}_{K,\ell} are the same for all t t ). Let ∥ ⋅ ∥ \|\cdot\| denote a submultiplicative matrix norm that is invariant under transposition (e.g. Spectral or Frobenius norms). Assume the corresponding attention inputs are bounded under this norm as ‖ 𝐗 ℓ , t ‖ ≤ B \|{\bm{X}}_{\ell,t}\|\leq B for all t t . Define κ ℓ = ‖ 𝐖 Q , ℓ ​ 𝐖 K , ℓ ⊤ ‖ \kappa_{\ell}=\|{\bm{W}}_{Q,\ell}{\bm{W}}_{K,\ell}^{\top}\| . Then, writing 𝒮 ℓ ​ ( 𝐗 ) := softmax ⁡ ( A ℓ ​ ( 𝐗 ) ) \mathcal{S}_{\ell}({\bm{X}}):=\mathrm{softmax}(A_{\ell}({\bm{X}})) with A ℓ ​ ( ⋅ ) A_{\ell}(\cdot) as defined above, for any t ≥ 1 t\geq 1 , ‖ 𝒮 ℓ ​ ( 𝑿 ℓ , t ) − 𝒮 ℓ ​ ( 𝑿 ℓ , t − 1 ) ‖ ≤ L sm ​ 2 ​ B ​ κ ℓ d ​ ‖ 𝑿 ℓ , t − 𝑿 ℓ , t − 1 ‖ , \big\|\mathcal{S}_{\ell}({\bm{X}}_{\ell,t})-\mathcal{S}_{\ell}({\bm{X}}_{\ell,t-1})\big\|\;\leq\;L_{\mathrm{sm}}\,\frac{2B\,\kappa_{\ell}}{\sqrt{d}}\,\big\|{\bm{X}}_{\ell,t}-{\bm{X}}_{\ell,t-1}\big\|, where L sm L_{\mathrm{sm}} is a Lipschitz constant of the row-wise softmax with respect to the chosen norm.

Since these attention patterns are characteristic of the different mixing stages of inference (defining, for example, ColSum concentration), we see that mixing behavior will tend towards being constant across recurrences.

### 4.1 Empirical Validation

We focus our attention on three different pretrained looped language models: Ouro 1.4B ( Zhu et al., 2025 ) , Huginn-0125 ( Geiping et al., 2025 ) , and Llama with retrofitted recurrence ( McLeish et al., 2025 ) . Additional models can be found in App. D , with architecture and training choices summarized in Table 1 . These models cover a range of design choices; later in Sec. 4.2 we will isolate the impact of these architectural differences. Except where otherwise specified, all results are visualized on the same random subset of 256 examples from the GSM8k test set; additional results targetting non-reasoning behavior are presented in Sec. E.4 , but we observe no significant changes and the conclusions of the main text remain unchanged.

We start by plotting the norm of the residual stream difference between subsequent iterations in Fig. 3 (and the same for cosine similarities in Fig. 24 ). This validates the starting assumption of Proposition 4.2 that looped models tend towards behavior in which the layerwise residual stream does not significantly change between recurrences.

For each of these models, we plot Frobenius norm between the realized attention matrices at different layers, for 8 loops of the recurrent block in Fig. 2 . The diagonal patterns of high similarity demonstrate that the attention matrices of any given layer are most similar to those of the same layer at different recurrences – as predicted by Proposition 4.2 . We note that this convergence towards similar attention patterns occurs remarkably quickly : for looped Ouro attention patterns appear to converge after the first iteration, and both Huginn-0125 and the retrofitted Llama model demonstrate this cyclic behavior immediately following the prelude.

However, despite the tendency visible in Fig. 3 towards small changes between successive iterations we discover that it is not the case that looped models always reach a fixed point, or even consistent limiting behavior: for each model we find an “approximate fixed point” per layer by iterating 128 times, then compute the norm of the difference between the output of each layer at every recurrence and its corresponding fixed point. This is visualized in Fig. 4 . We see that while Huginn-0125 and Retrofitted Llama demonstrate fast convergence to a fixed point, Ouro does not. As discussed by Bansal et al. (2022) ; Anil et al. (2022) , this supports the suggestion that input injection encourages fixed-point convergence: we investigate this further in Sec. 4.2 .

Where a model does reach a fixed point, this implies that the action of the entire recurrent block tends towards tracing out a consistent cycle in latent space. We visualize this for retrofitted Llama in Fig. 5 .

### 4.2 Impact of Architecture Choices

Several existing works ( Bansal et al., 2022 ; Anil et al., 2022 ) have noted that input injection is important in order for a recurrent model to reach a fixed point: in this section we replicate this finding and supplement with additional insights on the impact of norm structure in reaching a fixed point. We conduct a series of experiments on randomly initialized models. These demonstrate similar cyclic behavior to their trained counterparts, suggesting that behavior observed here is likely to generalize to the cyclic behavior of trained models. We compare pre-norm (used by the retrofitted recurrent models) and the norms used by the Huginn-0125 and Ouro models, testing each both with and without input injection: in this way we test the most significant architectural differences between the pretrained Looped models tested; see Table 1 for details. Each model has 12 layers with no prelude or coda; see Fig. 31 for alternative configurations.

Our results are visualized in Fig. 6 , where we visualise the mean over 3 random model initializations for each configuration. We see that input injection results in stable fixed point behavior for all norm types other than Ouro, whereas omitting input injection means that only pre-norm reaches a stable fixed point. However, this fixed point reached by pre-norm without input injection is a “degenerate” one: each layer converges to the same fixed point. This can be determined from the rightmost frame of Fig. 6 , which demonstrates that the lowest cosine similarity between the first layer and any other layer’s fixed point still converges to 1.

## 5 Stages of Inference in Looped Models Mirror Feedforward Computation

The previous section shows that, empirically, a wide range of models converge to a regime in which attention patterns within individual layers change only minimally across recurrences. As a result, attention dynamics in looped Transformers are constrained in depth, since layers are cyclically weight-tied to earlier ones. This behavior contrasts with feedforward Transformers, which impose no such constraints and exhibit sharp, layer-wise changes in attention patterns across depth. Prior work has linked these sharp transitions to characteristic stages of inference ( Lad et al., 2024 ; Queipo-de-Llano et al., 2025 ) , introduced in Sec. 2.2 . In this section, we study how cyclic weight sharing alters these stages of inference in looped Transformers. In the main text we frame our analysis using ColSum concentration , a metric for identifying stages of inference introduced in Sec. 2.2 , with extensive additional results in Sec. E.3 .

We visualize ColSum concentration over the realized depth of Retrofitted Llama in Fig. 7 , revealing consistent mixing cycles that repeat with every iteration of the recurrent block. However, each individual layer (solid colorful lines) changes very little in realized depth: after an initial transitory phase they quickly converge towards constant behavior.

Instead of occurring throughout the realized depth of the looped model, we find that the familiar feedforward stages of inference occur within each looped block. Fig. 8 demonstrates that ColSum concentration within each looped block closely resembles that of feedforward models. We draw attention to two observations: 1) Ouro 1.4B, despite being trained from scratch with recurrence, mirrors Llama mixing stages and 2) the retrofitted models closely follow the stages of inference of their associated base model, but the initial and final stages are performed only once by the prelude and coda respectively, while the “middle” stages are repeated in the recurrent block. It is particularly remarkable that these stages of inference appear in each Ouro recurrent block when pretraining from initialization; we discuss further the formation of stages of inference, and attempt to isolate their formation from specific training procedures, in Sec. 5.1 .

However, Huginn-0125 does not demonstrate clear stages of inference ( Fig. 36 ). We suggest that this is likely due to the specific norm structures used by these models ( Table 1 ). Huginn-0125 and Ouro both use a “sandwich” norm structure, but Huginn-0125 implements this by normalizing the residual streams whereas Ouro instead normalizes the outputs of the attention and MLP units, only normalizing the residual stream at the end of each recurrent block. We demonstrate the impact of the different norms by plotting residual stream magnitudes for a range of models in Fig. 9 . This means that Huginn-0125 is unable to develop the growth in residual stream magnitude that Queipo-de-Llano et al. (2025, Section 3.3) note causes compression behavior, leading to sink formation and stages of inference.

### 5.1 Self-Organization Into Stages of Inference

An open question from our analysis of pretrained models ( Fig. 8 ) is whether stages of inference emerge naturally during pretraining, or whether they are instead induced by specific aspects of the training procedure. Several mechanisms may introduce an implicit bias toward feedforward stages of inference: retrofitted models ( McLeish et al., 2025 ) may inherit the inference stages of the underlying base model; models trained with recurrence schedulers that permit a single recurrence ( Geiping et al., 2025 ; McLeish et al., 2025 ) are partially optimized as feedforward models; training objectives that decompose into separate loss terms for each recurrence ( Zhu et al., 2025 ) partially correspond to feedforward model training.

Therefore in this section we seek to investigate whether stages of inference can arise in Looped Transformers without these training biases. To explore this we pre-train several small-scale Looped Transformers, explicitly removing the biases above: we pre-train from scratch with a constant recurrence of 4, using a standard loss that considers only the final latent state when predicting the next token. Our code and training procedure are adapted from Karpathy (2025) ; additional details can be found in App. B .

ColSum concentrations for these trained Looped Transformers with configurations ( 2 , 4 ⊗ 4 , 2 ) (2,4\otimes 4,2) , ( 2 , 8 ⊗ 4 , 2 ) (2,8\otimes 4,2) and ( 2 , 12 ⊗ 4 , 2 ) (2,12\otimes 4,2) are plotted in Fig. 10 . We compare these to a “control” feedforward network without recurrence, of depth 12. These experiments are on a small scale and as such need to be treated with caution. However, they appear to provide initial evidence that – even without training methods that may bias towards feedforward stages of inference – looped models have a tendency to self-organize into multiple different mixing stages in recurrent depth, which resemble feedforward stages. The fact that the optimization of these models results in these mixing stages of inference suggests that they are beneficial to language modeling even when applied repeatedly in recurrent depth. We additionally test the impact of input injection and sandwich layers in Sec. E.6 .

### 5.2 Stability to Unseen Numbers of Recurrences

Sec. 4 establishes that some looped Transformer architectures converge to a fixed point (such as the retrofitted series and Huginn-0125) while others do not (such as Ouro). However, when evaluating these looped Transformers within the range of recurrences on which they were trained ( Sec. 5 ), we see extremely similar behavior: convergence to feedforward stages of inference within each recurrent block.

In this section, we demonstrate that a significant difference arises when generalizing to unseen test-time recurrence depths: models that do not reach a fixed point exhibit unstable stages of inference . Conversely, models with recurrent-block-wise stages of inference that also converge to a fixed point are guaranteed to keep enacting these stages of inference for arbitrary test time recurrences.

We first verify this stability in Fig. 11 , an extended plot of Fig. 7 . This demonstrates that for retrofitted Llama (results hold for other models using input injection), each individual layer quickly reaches a stable states and then exhibits consistent stages of inference behavior for an arbitrary number of test time recurrences. However, Ouro 1.4B does not exhibit this behavior, with individual layers changing continuously throughout later recurrences. The effect that this has on stages of inference is visualized in Fig. 12 .

Existing research implies that this stability correlates with out-of-domain performance. Models which exhibit “stable” stages of inference for arbitrary test time iterations also avoid performance deterioration in this extrapolation regime: whereas extrapolation beyond training recurrences harms the performance of Ouro ( Zhu et al., 2025 , Tab. 10) , Huginn-0125 performance remains constant in this extrapolation region ( Geiping et al., 2025 , Fig. 1) .

## 6 Conclusion

This paper examines the limiting behavior of Looped Transformers, exploring implications for “mixing” stages of inference observed in feedforward models. We demonstrate across a range of architectures that recurrent blocks tend to “mirror” the stages of a feedforward Transformer, and provide evidence that this may be emergent behavior learned during training, even when not explicitly encouraged by the training process. We further investigate the implications for these mixing stages when models converge to a stable fixed point, and when they do not.

#### Implications of Findings

The implications of our findings are bidirectional. On the one hand, the structure of looped architectures provides a novel lens to study stages of inference, while tracking these stages simultaneously reveals the internal mechanics of recurrent depth. In particular, since looped models decouple functional depth from parameter count, they provide an interesting new perspective on why these stages of inference form: previous work had suggested that these stages exist to mitigate the “harms” of transformer depth ( Barbero et al., 2025 ; Queipo-de-Llano et al., 2025 ) , however our work shows that looped models develop these same stages while simultaneously improving performance with greater recurrent depth. On the other hand, our findings that looped models exhibit (and self-organize into) similar stages of inference to feedforward models means that insights from the feedforward setting can be applied to looped models: predictable stages offer actionable pathways for efficient architectural design, including stage-dependent attention sparsification and the leaner parameterization of middle-stage MLPs where representations are reliably compressed and low-rank.

#### Limitations and Future Work

We focus exclusively on cyclic recurrence as this appears to be the dominant approach in the literature. However, this means our analysis does not extend to sequential recurrence with multiple separate recurrent blocks; for analysis of this setting we refer the reader to Pappone et al. (2025) . Despite empirically investigating the architectural choices that result in stable limiting behavior in looped models, we have not established analytically why this is the case, nor whether this stable limiting behavior is desirable or restrictive for reasoning tasks.

## Impact Statement

Ethical aspects and future societal consequences of this particular work are limited. The goal of our work is to advance understanding of looped Language Models, which themselves seem to demonstrate strong reasoning performance; as such, our work is in support of a field that has potential societal consequences if future models are able to undertake more advanced reasoning tasks. However, we do not within this work introduce any more powerful reasoning models, and the impact of our work is limited to understanding existing models, and potentially guiding future advancements.

## Acknowledgments

HB acknowledges funding support from the EPSRC Centre for Doctoral Training in Autonomous Intelligent Machines and Systems No. EP/S024050/1. MB is partially supported by the EPSRC Turing AI World-Leading Research Fellowship No. EP/X040062/1 and EPSRC AI Hub No. EP/Y028872/1.

## References

Alon and Yahav (2020) U. Alon and E. Yahav On the bottleneck of graph neural networks and its practical implications . arXiv preprint arXiv:2006.05205 . Cited by: §3 .

Anil et al. (2022) C. Anil, A. Pokle, K. Liang, J. Treutlein, Y. Wu, S. Bai, J. Z. Kolter, and R. B. Grosse Path independent equilibrium models can better exploit test-time computation . Advances in Neural Information Processing Systems 35 , pp. 7796–7809 . Cited by: §2.1 , §3 , §4.1 , §4.2 , §4 .

Arroyo et al. (2026) A. Arroyo, F. Barbero, H. Blayney, M. M. Bronstein, X. Dong, P. Lio, R. Pascanu, and P. Vandergheynst A survey on over-smoothing and over-squashing: unified propagation perspectives on graph neural networks and transformers . Transactions on Machine Learning Research . Note: External Links: ISSN 2835-8856 Cited by: §3 .

Arroyo et al. (2025) Á. Arroyo, A. Gravina, B. Gutteridge, F. Barbero, C. Gallicchio, X. Dong, M. Bronstein, and P. Vandergheynst On vanishing gradients, over-smoothing, and over-squashing in gnns: bridging recurrent and graph learning . arXiv preprint arXiv:2502.10818 . Cited by: §3 .

Bae et al. (2025) S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, et al. Mixture-of-recursions: learning dynamic recursive depths for adaptive token-level computation . arXiv preprint arXiv:2507.10524 . Cited by: §2.1 , §3 .

Bai et al. (2019) S. Bai, J. Z. Kolter, and V. Koltun Deep equilibrium models . Advances in neural information processing systems 32 . Cited by: §2.1 , §3 , §4 .

Banino et al. (2021) A. Banino, J. Balaguer, and C. Blundell Pondernet: learning to ponder . arXiv preprint arXiv:2107.05407 . Cited by: §3 .

Bansal et al. (2022) A. Bansal, A. Schwarzschild, E. Borgnia, Z. Emam, F. Huang, M. Goldblum, and T. Goldstein End-to-end algorithm synthesis with recurrent networks: logical extrapolation without overthinking . Advances in Neural Information Processing Systems 35 , pp. 20232–20242 . Cited by: §3 , §4.1 , §4.2 , §4 .

Barbero et al. (2025) F. Barbero, A. Arroyo, X. Gu, C. Perivolaropoulos, M. Bronstein, P. Veličković, and R. Pascanu Why do llms attend to the first token? . arXiv preprint arXiv:2504.02732 . Cited by: Appendix B , §E.2 , §2.2 , §3 , §6 .

Barbero et al. (2024) F. Barbero, A. Banino, S. Kapturowski, D. Kumaran, J. Madeira Araújo, O. Vitvitskyi, R. Pascanu, and P. Veličković Transformers need glasses! information over-squashing in language tasks . Advances in Neural Information Processing Systems 37 , pp. 98111–98142 . Cited by: §3 .

Bear et al. (2024) J. Bear, A. Prugel-Bennett, and J. Hare Rethinking deep thinking: stable learning of algorithms using lipschitz constraints . Advances in Neural Information Processing Systems 37 , pp. 97027–97052 . Cited by: §3 .

Blayney et al. (2025) H. Blayney, Á. Arroyo, X. Dong, and M. M. Bronstein GLSTM: mitigating over-squashing by increasing storage capacity . arXiv preprint arXiv:2510.08450 . Cited by: §3 .

Cai and Wang (2020) C. Cai and Y. Wang A note on over-smoothing for graph neural networks . arXiv preprint arXiv:2006.13318 . Cited by: §3 .

Cobbe et al. (2021) K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman Training verifiers to solve math word problems . arXiv preprint arXiv:2110.14168 . Cited by: Appendix B .

Csordás et al. (2024) R. Csordás, K. Irie, J. Schmidhuber, C. Potts, and C. D. Manning Moeut: mixture-of-experts universal transformers . Advances in Neural Information Processing Systems 37 , pp. 28589–28614 . Cited by: §3 .

Darlow et al. (2025) L. Darlow, C. Regan, S. Risi, J. Seely, and L. Jones Continuous thought machines . arXiv preprint arXiv:2505.05522 . Cited by: §3 .

Dehghani et al. (2018) M. Dehghani, S. Gouws, O. Vinyals, J. Uszkoreit, and Ł. Kaiser Universal transformers . arXiv preprint arXiv:1807.03819 . Cited by: §3 .

Geiping et al. (2025) J. Geiping, S. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein Scaling up test-time compute with latent reasoning: a recurrent depth approach . arXiv preprint arXiv:2502.05171 . Cited by: Table 1 , Appendix B , Figure 15 , §C.1 , §C.1 , §C.1 , §C.1 , §C.2 , §C.2 , Figure 19 , Figure 20 , Figure 21 , Figure 27 , Figure 27 , Figure 34 , Figure 48 , Figure 48 , §1 , §1 , §2.1 , §2.1 , §2.1 , §2.1 , Figure 2 , §3 , §4.1 , §5.1 , §5.2 , footnote 1 .

Graves (2016) A. Graves Adaptive computation time for recurrent neural networks . arXiv preprint arXiv:1603.08983 . Cited by: §1 , §3 .

Gu et al. (2024) X. Gu, T. Pang, C. Du, Q. Liu, F. Zhang, C. Du, Y. Wang, and M. Lin When attention sink emerges in language models: an empirical view . arXiv preprint arXiv:2410.10781 . Cited by: §E.2 .

Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning . arXiv preprint arXiv:2501.12948 . Cited by: §1 .

Gurnee et al. (2024) W. Gurnee, T. Horsley, Z. C. Guo, T. R. Kheirkhah, Q. Sun, W. Hathaway, N. Nanda, and D. Bertsimas Universal neurons in GPT2 language models . Transactions on Machine Learning Research . Note: External Links: ISSN 2835-8856 Cited by: §E.1 .

Hariri et al. (2025) A. Hariri, Á. Arroyo, A. Gravina, M. Eliasof, C. Schönlieb, D. Bacciu, K. Azizzadenesheli, X. Dong, and P. Vandergheynst Return of chebnet: understanding and improving an overlooked gnn on long range tasks . arXiv preprint arXiv:2506.07624 . Cited by: §3 .

Jolicoeur-Martineau (2025) A. Jolicoeur-Martineau Less is more: recursive reasoning with tiny networks . arXiv preprint arXiv:2510.04871 . Cited by: §1 , §3 .

Karpathy (2025) A. Karpathy Nanochat: the best ChatGPT that $100 can buy . GitHub . External Links: Link Cited by: Appendix B , §5.1 .

Ke et al. (2024) Y. Ke, X. Li, Y. Liang, Z. Shi, and Z. Song Advancing the understanding of fixed point iterations in deep neural networks: a detailed analytical study . arXiv preprint arXiv:2410.11279 . Cited by: §3 .

Koishekenov et al. (2025) Y. Koishekenov, A. Lipani, and N. Cancedda Encode, think, decode: scaling test-time reasoning with recursive latent thoughts . arXiv preprint arXiv:2510.07358 . Cited by: §3 .

Lad et al. (2024) V. Lad, J. H. Lee, W. Gurnee, and M. Tegmark The remarkable robustness of llms: stages of inference? . arXiv preprint arXiv:2406.19384 . Cited by: §E.1 , §1 , §2.2 , §3 , §5 .

Lu et al. (2025) W. Lu, Y. Yang, K. Lee, Y. Li, and E. Liu Latent chain-of-thought? decoding the depth-recurrent transformer . arXiv preprint arXiv:2507.02199 . Cited by: §3 .

McLeish et al. (2024) S. McLeish, A. Bansal, A. Stein, N. Jain, J. Kirchenbauer, B. Bartoldson, B. Kailkhura, A. Bhatele, J. Geiping, A. Schwarzschild, et al. Transformers can do arithmetic with the right embeddings . Advances in Neural Information Processing Systems 37 , pp. 108012–108041 . Cited by: §3 .

McLeish et al. (2025) S. McLeish, A. Li, J. Kirchenbauer, D. S. Kalra, B. R. Bartoldson, B. Kailkhura, A. Schwarzschild, J. Geiping, T. Goldstein, and M. Goldblum Teaching pretrained language models to think deeper with retrofitted recurrence . arXiv preprint arXiv:2511.07384 . Cited by: Table 1 , Figure 19 , Figure 20 , Figure 21 , Figure 34 , Figure 37 , Figure 37 , Figure 38 , Figure 38 , Figure 39 , Figure 39 , Figure 44 , Figure 44 , Figure 45 , Figure 45 , Figure 46 , Figure 46 , Figure 49 , Figure 49 , §2.1 , Figure 2 , §3 , Figure 5 , Figure 5 , §4.1 , Figure 7 , Figure 7 , Figure 8 , §5.1 .

Nair (2025) P. Nair Softmax is 1 / 2 1/2 -lipschitz: a tight bound across all ℓ p \ell_{p} norms . arXiv preprint arXiv:2510.23012 . Cited by: Appendix A .

Pappone et al. (2025) F. Pappone, D. Crisostomi, and E. Rodolà Two-scale latent dynamics for recurrent-depth transformers . arXiv preprint arXiv:2509.23314 . Cited by: §3 , §6 .

Queipo-de-Llano et al. (2025) E. Queipo-de-Llano, Á. Arroyo, F. Barbero, X. Dong, M. Bronstein, Y. LeCun, and R. Shwartz-Ziv Attention sinks and compression valleys in llms are two sides of the same coin . arXiv preprint arXiv:2510.06477 . Cited by: §E.2 , §E.2 , §1 , §2.2 , §3 , §5 , §5 , §6 .

Sandoval-Segura et al. (2025) P. Sandoval-Segura, X. Wang, A. Panda, M. Goldblum, R. Basri, T. Goldstein, and D. Jacobs Using attention sinks to identify and evaluate dormant heads in pretrained llms . arXiv preprint arXiv:2504.03889 . Cited by: §2.2 .

Saunshi et al. (2025) N. Saunshi, N. Dikkala, Z. Li, S. Kumar, and S. J. Reddi Reasoning with latent thoughts: on the power of looped transformers . arXiv preprint arXiv:2502.17416 . Cited by: §2.1 , §3 .

Schuster et al. (2022) T. Schuster, A. Fisch, J. Gupta, M. Dehghani, D. Bahri, V. Tran, Y. Tay, and D. Metzler Confident adaptive language modeling . Advances in Neural Information Processing Systems 35 , pp. 17456–17472 . Cited by: §3 .

Schwarzschild et al. (2021) A. Schwarzschild, E. Borgnia, A. Gupta, F. Huang, U. Vishkin, M. Goldblum, and T. Goldstein Can you learn an algorithm? generalizing from easy to hard problems with recurrent networks . Advances in Neural Information Processing Systems 34 , pp. 6695–6706 . Cited by: §3 .

Skean et al. (2025) O. Skean, M. R. Arefin, D. Zhao, N. N. Patel, J. Naghiyev, Y. LeCun, and R. Shwartz-Ziv Layer by layer: uncovering hidden representations in language models . In Forty-second International Conference on Machine Learning , Cited by: §E.2 .

Sun et al. (2024) M. Sun, X. Chen, J. Z. Kolter, and Z. Liu Massive activations in large language models . In First Conference on Language Modeling , Cited by: §3 .

Tan et al. (2023) S. Tan, Y. Shen, Z. Chen, A. Courville, and C. Gan Sparse universal transformer . arXiv preprint arXiv:2310.07096 . Cited by: §3 .

Vaswani et al. (2017) A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin Attention is all you need . Advances in neural information processing systems 30 . Cited by: §1 .

Veličković et al. (2024) P. Veličković, C. Perivolaropoulos, F. Barbero, and R. Pascanu Softmax is not enough (for sharp size generalisation) . arXiv preprint arXiv:2410.01104 . Cited by: §3 .

Wang et al. (2025) G. Wang, J. Li, Y. Sun, X. Chen, C. Liu, Y. Wu, M. Lu, S. Song, and Y. A. Yadkori Hierarchical reasoning model . arXiv preprint arXiv:2506.21734 . Cited by: §1 , §3 .

Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models . Advances in neural information processing systems 35 , pp. 24824–24837 . Cited by: §1 .

Xiao et al. (2023) G. Xiao, Y. Tian, B. Chen, S. Han, and M. Lewis Efficient streaming language models with attention sinks . arXiv preprint arXiv:2309.17453 . Cited by: §E.2 , §2.2 .

Xu and Sato (2024) K. Xu and I. Sato On expressive power of looped transformers: theoretical analysis and enhancement via timestep encoding . arXiv preprint arXiv:2410.01405 . Cited by: §3 .

Yang et al. (2023) L. Yang, K. Lee, R. Nowak, and D. Papailiopoulos Looped transformers are better at learning learning algorithms . arXiv preprint arXiv:2311.12424 . Cited by: §1 .

Yudin et al. (2025) N. Yudin, A. Gaponov, S. Kudriashov, and M. Rakhuba Pay attention to attention distribution: a new local lipschitz bound for transformers . arXiv preprint arXiv:2507.07814 . Cited by: §2.1 , §3 .

Zellers et al. (2019) R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi HellaSwag: can a machine really finish your sentence? . In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics , Cited by: §E.4 .

Zhu et al. (2025) R. Zhu, Z. Wang, K. Hua, T. Zhang, Z. Li, H. Que, B. Wei, Z. Wen, F. Yin, H. Xing, et al. Scaling latent reasoning via looped language models . arXiv preprint arXiv:2510.25741 . Cited by: Table 1 , Appendix B , Figure 19 , Figure 26 , Figure 26 , Figure 28 , Figure 28 , Figure 34 , Figure 40 , Figure 47 , Figure 47 , §E.3 , Figure 2 , §3 , §4.1 , Figure 8 , §5.1 , §5.2 .

## Appendix Contents

## Appendix A Proofs of Propositions

#### Proof of Proposition 4.1

###### Proof sketch.

Note S k ⁡ ( 𝑿 ′ ) = B k ⁡ ( B k − 1 ⁡ ( … ​ B 1 ⁡ ( 𝑿 ′ ) ​ … ) ) = 𝑿 ′ \stack_{k}({\bm{X}}^{\prime})=\block_{k}(\block_{k-1}(\dots\block_{1}({\bm{X}}^{\prime})\dots))={\bm{X}}^{\prime} Applying B 1 \block_{1} to both sides yields to B 1 ⁡ ( B k ⁡ ( B k − 1 ⁡ ( … ​ B 1 ⁡ ( 𝑿 ′ ) ​ … ) ) ) = B 1 ⁡ ( 𝑿 ′ ) . \block_{1}(\block_{k}(\block_{k-1}(\dots\block_{1}(\\ {\bm{X}}^{\prime})\dots)))=\block_{1}({\bm{X}}^{\prime}). Defining 𝒀 ′ = B 1 ⁡ ( 𝑿 ′ ) {\bm{Y}}^{\prime}=\block_{1}({\bm{X}}^{\prime}) , we obtain B 1 ⁡ ( B k ⁡ ( B k − 1 ⁡ ( … ​ B 2 ⁡ ( 𝒀 ′ ) ​ … ) ) ) = 𝒀 ′ \block_{1}(\block_{k}(\block_{k-1}(\dots\block_{2}({\bm{Y}}^{\prime})\dots)))={\bm{Y}}^{\prime} . The general proof follows by induction, and extends trivially to input injection. ∎

###### Proof.

Assume that ( l , k ) (l,k) -Recurrent block S k S_{k} reaches a fixed point such that S k ​ ( 𝑿 ′ ) = 𝑿 ′ S_{k}({\bm{X}}^{\prime})={\bm{X}}^{\prime} . Note that S k ⁡ ( 𝑿 ′ ) = B k − 1 ⁡ ( B k − 2 ⁡ ( … ​ B 0 ⁡ ( 𝑿 ′ ) ​ … ) ) = 𝑿 ′ \stack_{k}({\bm{X}}^{\prime})=\block_{k-1}(\block_{k-2}(\dots\block_{0}({\bm{X}}^{\prime})\dots))={\bm{X}}^{\prime} define the cyclic shift function f n ​ ( i ) = ( i + n ) mod k f_{n}(i)=(i+n)\mod k . Now we aim to prove by induction ∀ n ∈ ℤ + ∪ { 0 } : B f n ​ ( k − 1 ) ⁡ ( B f n ​ ( k − 2 ) ⁡ ( … ​ B f n ​ ( 0 ) ⁡ ( 𝒁 ′ ) ​ … ) ) = 𝒁 ′ \forall n\in\mathbb{Z}_{+}\cup\{0\}:\block_{f_{n}(k-1)}(\block_{f_{n}(k-2)}(\dots\block_{f_{n}(0)}({\bm{Z}}^{\prime})\dots))={\bm{Z}}^{\prime} for some 𝒁 ′ {\bm{Z}}^{\prime} . The base case n = 0 n=0 is trivial as ∀ i < k : f 0 ​ ( i ) = i \forall i<k:f_{0}(i)=i . Now assume for some n = j n=j B f j ​ ( k − 1 ) ⁡ ( B f j ​ ( k − 2 ) ⁡ ( … ​ B f j ​ ( 0 ) ⁡ ( 𝒁 ′ ) ​ … ) ) = 𝒁 ′ \block_{f_{j}(k-1)}(\block_{f_{j}(k-2)}(\dots\block_{f_{j}(0)}({\bm{Z}}^{\prime})\dots))={\bm{Z}}^{\prime} (8) Now, let n = j + 1 n=j+1 . Note f j + 1 ​ ( i ) = ( i + j + 1 ) mod k = f j ​ ( i + 1 ) f_{j+1}(i)=(i+j+1)\mod k=f_{j}(i+1) Therefore B f j + 1 ​ ( k − 1 ) ⁡ ( B f j + 1 ​ ( k − 2 ) ⁡ ( … ​ B f j + 1 ​ ( 0 ) ⁡ ( 𝒀 ) ​ … ) ) \displaystyle\block_{f_{j+1}(k-1)}(\block_{f_{j+1}(k-2)}(\dots\block_{f_{j+1}(0)}({\bm{Y}})\dots)) = B f j ​ ( k ) ⁡ ( B f j ​ ( k − 1 ) ⁡ ( … ​ B f j ​ ( 1 ) ⁡ ( 𝒀 ) ​ … ) ) \displaystyle=\block_{f_{j}(k)}(\block_{f_{j}(k-1)}(\dots\block_{f_{j}(1)}({\bm{Y}})\dots)) (9) = B f j ​ ( 0 ) ⁡ ( B f j ​ ( k − 1 ) ⁡ ( … ​ B f j ​ ( 1 ) ⁡ ( 𝒀 ) ​ … ) ) \displaystyle=\block_{f_{j}(0)}(\block_{f_{j}(k-1)}(\dots\block_{f_{j}(1)}({\bm{Y}})\dots)) (10) Now take Eq. 8 and apply B f j ​ ( 0 ) \block_{f_{j}(0)} to both sides, defining a new fixed point 𝒁 ′′ = B f j ​ ( 0 ) ⁡ ( 𝒁 ′ ) {\bm{Z}}^{\prime\prime}=\block_{f_{j}(0)}({\bm{Z}}^{\prime}) : B f j ​ ( 0 ) ⁡ ( B f j ​ ( k − 1 ) ⁡ ( B f j ​ ( k − 2 ) ⁡ ( … ​ B f j ​ ( 0 ) ⁡ ( 𝒁 ′ ) ​ … ) ) ) \displaystyle\block_{f_{j}(0)}(\block_{f_{j}(k-1)}(\block_{f_{j}(k-2)}(\dots\block_{f_{j}(0)}({\bm{Z}}^{\prime})\dots))) = B f j ​ ( 0 ) ⁡ ( 𝒁 ′ ) \displaystyle=\block_{f_{j}(0)}({\bm{Z}}^{\prime}) (11) B f j ​ ( 0 ) ⁡ ( B f j ​ ( k − 1 ) ⁡ ( B f j ​ ( k − 2 ) ⁡ ( … ​ B f j ​ ( 1 ) ⁡ ( 𝒁 ′′ ) ​ … ) ) ) \displaystyle\block_{f_{j}(0)}(\block_{f_{j}(k-1)}(\block_{f_{j}(k-2)}(\dots\block_{f_{j}(1)}({\bm{Z}}^{\prime\prime})\dots))) = 𝒁 ′′ \displaystyle={\bm{Z}}^{\prime\prime} (12) Combining Eq. 12 and Eq. 10 , we see that there exists a fixed point 𝒁 ′′ {\bm{Z}}^{\prime\prime} such that B f j + 1 ​ ( k − 1 ) ⁡ ( B f j + 1 ​ ( k − 2 ) ⁡ ( … ​ B f j + 1 ​ ( 0 ) ⁡ ( 𝒁 ′′ ) ​ … ) ) = 𝒁 ′′ \block_{f_{j+1}(k-1)}(\block_{f_{j+1}(k-2)}(\dots\block_{f_{j+1}(0)}({\bm{Z}}^{\prime\prime})\dots))={\bm{Z}}^{\prime\prime} Therefore completing the induction step and proving the proposition. ∎

#### Proof of Proposition 4.2

###### Proof.

Define 𝒮 ℓ ​ ( 𝑿 ) := softmax ⁡ ( A ℓ ​ ( 𝑿 ) ) = softmax ⁡ ( 𝑿 ​ 𝑾 Q ​ 𝑾 K ⊤ ​ 𝑿 ⊤ d ) \mathcal{S}_{\ell}({\bm{X}}):=\mathrm{softmax}(A_{\ell}({\bm{X}}))=\mathrm{softmax}{\left(\frac{{\bm{X}}{\bm{W}}_{Q}{\bm{W}}_{K}^{\top}{\bm{X}}^{\top}}{\sqrt{d}}\right)} Let L sm L_{\mathrm{sm}} be the Lipschitz constant of the row-wise softmax such that ‖ 𝒮 ℓ ​ ( 𝑿 ℓ , t ) − 𝒮 ℓ ​ ( 𝑿 ℓ , t − 1 ) ‖ ≤ L sm ​ ‖ A ℓ ​ ( 𝑿 ℓ , t ) − A ℓ ​ ( 𝑿 ℓ , t − 1 ) ‖ \big\|\mathcal{S}_{\ell}({\bm{X}}_{\ell,t})-\mathcal{S}_{\ell}({\bm{X}}_{\ell,t-1})\big\|\leq L_{\mathrm{sm}}\big\|A_{\ell}({\bm{X}}_{\ell,t})-A_{\ell}({\bm{X}}_{\ell,t-1})\big\| (13) Recently Nair (2025) shows that L sm = 1 / 2 L_{\mathrm{sm}}=1/2 .

Define for convenience 𝑴 = 𝑾 Q ​ 𝑾 K ⊤ {\bm{M}}={\bm{W}}_{Q}{\bm{W}}_{K}^{\top} and Δ ℓ , t = 𝑿 ℓ , t − 𝑿 ℓ , t − 1 \Delta_{\ell,t}={\bm{X}}_{\ell,t}-{\bm{X}}_{\ell,t-1} . Then A ℓ ​ ( 𝑿 ℓ , t ) − A ℓ ​ ( 𝑿 ℓ , t − 1 ) \displaystyle A_{\ell}({\bm{X}}_{\ell,t})-A_{\ell}({\bm{X}}_{\ell,t-1}) = 𝑿 ℓ , t ​ 𝑾 Q ​ 𝑾 K ⊤ ​ 𝑿 ℓ , t ⊤ d − 𝑿 ℓ , t − 1 ​ 𝑾 Q ​ 𝑾 K ⊤ ​ 𝑿 ℓ , t − 1 ⊤ d \displaystyle=\frac{{\bm{X}}_{\ell,t}{\bm{W}}_{Q}{\bm{W}}_{K}^{\top}{\bm{X}}^{\top}_{\ell,t}}{\sqrt{d}}-\frac{{\bm{X}}_{\ell,t-1}{\bm{W}}_{Q}{\bm{W}}_{K}^{\top}{\bm{X}}^{\top}_{\ell,t-1}}{\sqrt{d}} = 1 d ​ ( ( Δ ℓ , t + 𝑿 ℓ , t − 1 ) ​ 𝑴 ​ ( Δ ℓ , t + 𝑿 ℓ , t − 1 ) ⊤ − 𝑿 ℓ , t − 1 ​ 𝑴 ​ 𝑿 ℓ , t − 1 ⊤ ) \displaystyle=\frac{1}{\sqrt{d}}\left(\left(\Delta_{\ell,t}+{\bm{X}}_{\ell,t-1}\right){\bm{M}}\left(\Delta_{\ell,t}+{\bm{X}}_{\ell,t-1}\right)^{\top}-{\bm{X}}_{\ell,t-1}{\bm{M}}{\bm{X}}^{\top}_{\ell,t-1}\right) = 1 d ​ ( Δ ℓ , t ​ 𝑴 ​ Δ ℓ , t ⊤ + Δ ℓ , t ​ 𝑴 ​ 𝑿 ℓ , t − 1 ⊤ + 𝑿 ℓ , t − 1 ​ 𝑴 ​ Δ ℓ , t ⊤ + 𝑿 ℓ , t − 1 ​ 𝑴 ​ 𝑿 ℓ , t − 1 ⊤ − 𝑿 ℓ , t − 1 ​ 𝑴 ​ 𝑿 ℓ , t − 1 ⊤ ) \displaystyle=\frac{1}{\sqrt{d}}\left({\Delta_{\ell,t}{\bm{M}}\Delta_{\ell,t}^{\top}}+\Delta_{\ell,t}{\bm{M}}{\bm{X}}_{\ell,t-1}^{\top}+{\bm{X}}_{\ell,t-1}{\bm{M}}\Delta_{\ell,t}^{\top}+\cancel{{\bm{X}}_{\ell,t-1}{\bm{M}}{\bm{X}}_{\ell,t-1}^{\top}}-\cancel{{\bm{X}}_{\ell,t-1}{\bm{M}}{\bm{X}}^{\top}_{\ell,t-1}}\right) = 1 d ​ ( Δ ℓ , t ​ 𝑴 ​ ( Δ ℓ , t + 𝑿 ℓ , t − 1 ) ⊤ + 𝑿 ℓ , t − 1 ​ 𝑴 ​ Δ ℓ , t ⊤ ) \displaystyle=\frac{1}{\sqrt{d}}\left(\Delta_{\ell,t}{\bm{M}}\left(\Delta_{\ell,t}+{\bm{X}}_{\ell,t-1}\right)^{\top}+{\bm{X}}_{\ell,t-1}{\bm{M}}\Delta_{\ell,t}^{\top}\right) = 1 d ​ ( Δ ℓ , t ​ 𝑴 ​ 𝑿 ℓ , t ⊤ + 𝑿 ℓ , t − 1 ​ 𝑴 ​ Δ ℓ , t ⊤ ) \displaystyle=\frac{1}{\sqrt{d}}\left(\Delta_{\ell,t}{\bm{M}}{\bm{X}}_{\ell,t}^{\top}+{\bm{X}}_{\ell,t-1}{\bm{M}}\Delta_{\ell,t}^{\top}\right) Therefore, ‖ A ℓ ​ ( 𝑿 ℓ , t ) − A ℓ ​ ( 𝑿 ℓ , t − 1 ) ‖ \displaystyle\big\|A_{\ell}({\bm{X}}_{\ell,t})-A_{\ell}({\bm{X}}_{\ell,t-1})\big\| = ‖ 1 d ​ ( Δ ℓ , t ​ 𝑴 ​ 𝑿 ℓ , t ⊤ + 𝑿 ℓ , t − 1 ​ 𝑴 ​ Δ ℓ , t ⊤ ) ‖ \displaystyle=\big\|\frac{1}{\sqrt{d}}\left(\Delta_{\ell,t}{\bm{M}}{\bm{X}}_{\ell,t}^{\top}+{\bm{X}}_{\ell,t-1}{\bm{M}}\Delta_{\ell,t}^{\top}\right)\big\| ≤ 1 d ​ ( ‖ Δ ℓ , t ​ 𝑴 ​ 𝑿 ℓ , t ⊤ ‖ + ‖ 𝑿 ℓ , t − 1 ​ 𝑴 ​ Δ ℓ , t ⊤ ‖ ) \displaystyle\leq\frac{1}{\sqrt{d}}\left(\big\|\Delta_{\ell,t}{\bm{M}}{\bm{X}}_{\ell,t}^{\top}\big\|+\big\|{\bm{X}}_{\ell,t-1}{\bm{M}}\Delta_{\ell,t}^{\top}\big\|\right) ≤ ‖ 𝑴 ‖ ​ ( ‖ 𝑿 ℓ , t ‖ + ‖ 𝑿 ℓ , t − 1 ‖ ) d ​ ‖ Δ ℓ , t ‖ \displaystyle\leq\frac{\big\|{\bm{M}}\big\|\left(\big\|{\bm{X}}_{\ell,t}\big\|+\big\|{\bm{X}}_{\ell,t-1}\big\|\right)}{\sqrt{d}}\big\|\Delta_{\ell,t}\big\| Assuming ‖ 𝑿 ℓ , t ‖ ≤ B \|{\bm{X}}_{\ell,t}\|\leq B for all t t , and defining κ ℓ = ‖ 𝑾 Q , ℓ ​ 𝑾 K , ℓ ⊤ ‖ = ‖ 𝑴 ‖ \kappa_{\ell}=\|{\bm{W}}_{Q,\ell}{\bm{W}}_{K,\ell}^{\top}\|=\big\|{\bm{M}}\big\| , we see ‖ A ℓ ​ ( 𝑿 ℓ , t ) − A ℓ ​ ( 𝑿 ℓ , t − 1 ) ‖ ≤ 2 ​ B ​ κ ℓ d ​ ‖ 𝑿 ℓ , t − 𝑿 ℓ , t − 1 ‖ \big\|A_{\ell}({\bm{X}}_{\ell,t})-A_{\ell}({\bm{X}}_{\ell,t-1})\big\|\leq\frac{2B\kappa_{\ell}}{\sqrt{d}}\big\|{\bm{X}}_{\ell,t}-{\bm{X}}_{\ell,t-1}\big\| (14) Combining Eq. 13 and Eq. 14 , we complete the proof: ‖ 𝒮 ℓ ​ ( 𝑿 ℓ , t ) − 𝒮 ℓ ​ ( 𝑿 ℓ , t − 1 ) ‖ ≤ L sm ​ 2 ​ B ​ κ ℓ d ​ ‖ 𝑿 ℓ , t − 𝑿 ℓ , t − 1 ‖ \big\|\mathcal{S}_{\ell}({\bm{X}}_{\ell,t})-\mathcal{S}_{\ell}({\bm{X}}_{\ell,t-1})\big\|\leq L_{\mathrm{sm}}\frac{2B\kappa_{\ell}}{\sqrt{d}}\big\|{\bm{X}}_{\ell,t}-{\bm{X}}_{\ell,t-1}\big\| (15) ∎

## Appendix B Additional Experimental Details

Unless stated otherwise, all of our experiments are averaged over the same subset of 256 random examples from the test split of the GSM8k ( Cobbe et al., 2021 ) dataset. A few illustrative plots (for example, latent space trajectories) are instead produced with a test sequence that we obtain from Barbero et al. (2025) : “Hello! I’ve been well. I hope that you’re doing well.” Additional results targetting non-reasoning behavior using the HellaSwag dataset (following an identical setup of running inference on the same 256 random examples from the test split) can be found in Sec. E.4 .

All pretrained models are obtained from Huggingface, model references provided in Table 2 . We use standard settings for the tokenizers of each model, and as such some models prepend a BOS token whereas others do not: we make this clear in the ‘Prepends BOS’ column of the same table.

Our small training runs in Sec. 5.1 are performed by adapting a publicly available fork of Nanochat ( Karpathy, 2025 ) , https://github.com/TrelisResearch/nanochat/tree/recursive . For all experiments we use a model dimension (residual stream) of 512 (4 heads of dimension 128) and train for 3.7B tokens. As discussed in the main text, loss is the same as that of a regular feedforward model: cross entropy loss on the final output representation (as opposed to the summed loss of Zhu et al. (2025) ). Each model is trained for a constant 4 recurrences (as opposed to the Poisson sampling of Geiping et al. (2025) ). All models use pre-norm only: this norm does not result in the stability issues reported by Geiping et al. (2025) ; Zhu et al. (2025) , but this is likely because we are operating at a far smaller scale.

## Appendix C Non-Fixed-Point Limiting Behavior

### C.1 How Frequent is Non-Fixed-Point Behavior?

In this section we investigate more closely the “orbits” and “sliders” initially observed by Geiping et al. (2025) . These are important as they appear to represent stable limiting behavior that are not fixed points .

We develop a heuristic algorithm to detect these behaviors, presented in Algorithm 1 . We use the sequence of cosine similarities from the final recurrent layer (per token), where the output residual stream after each of 128 recurrences is compared to the final residual stream (as in Fig. 22 ). This is visualized in the leftmost column of Fig. 13 . We set threshold τ = 0.05 \tau=0.05 and fixed-point fraction ρ = 0.9 \rho=0.9 .

Using this algorithm, we classify the limiting behavior over all tokens in the GSM8k test set for the Huginn-0125 and Retrofitted Llama models. We discover that the system prompt used before presenting the GSM8k question has a large impact on the limiting behavior types and as such we test the following prompts across both models:

#### Long Persona

This is the system prompt used by Geiping et al. (2025) to produce their Orbit plots:

#### Long Persona (Padded)

This is the same prompt as above but with all tokens replaced with the padding token: we include this to test whether the behavior arises purely due to the length of the input.

#### Short Math

This is the system prompt used by Geiping et al. (2025) in their GSM8k benchmark evaluation:

We present the percentage of GSM8k tokens that exhibit each classification of limiting behavior in Table 3 and the percentage of GSM8k examples that exhibit each classification of limiting behavior across any of their tokens in Table 4 .

These results reveal that these non-fixed-point limiting behaviors appear to be extremely rare in practice: without a system prompt (the setting used throughout this paper) only approximately 0.02% of tokens exhibit non-fixed-point behavior. This percentage can be significantly increased with the longer system prompt, but these behaviors remain rare at 0.14%. Curiously, the “Persona” system prompt used by Geiping et al. (2025) seems to increase the occurrence of these orbits and sliders more than a comparable prompt of padding tokens, suggesting that the effect is not purely to do with sequence length.

We highlight that these exact results need to be treated with caution: the absolute values vary significantly depending on the algorithm hyperparameters chosen, and in the absence of a good external metric we selected these hyperparameters manually via visual inspection of the trajectories and cosine similarities to ensure the results agreed with intuition. However, across different hyperparameters the results consistently showed that non-fixed-point behavior is rare and that the long persona prompt results in a greater rate of non-fixed-point behavior. We leave in-depth classification and explanation of this phenomena to future work.

### C.2 Do Intermediate Layers Exhibit Non-Fixed-Point Behavior?

Geiping et al. (2025) observe orbits and sliders in the latent states after each application of the entire recurrent block. Here we investigate what occurs in the latent states of the intermediate layers within the recurrent block.

We first extend Figure 16 of Geiping et al. (2025) (visualizing latent trajectories on a math prompt), visualizing also the trajectories of the intermediate layer residual streams: this can be found in Fig. 15 . This demonstrates that in this particular case, where Orbits occur, they also occur in the intermediate layers. This implies – viewed in realized depth – latent trajectories exhibiting multi-scale cyclic behavior.

We investigate this across all GSM8k test examples in Fig. 14 by plotting the conditional probability of observing each behavior on a given token for any layer, given an observation of observing another behavior on that same token. We discover that orbits and sliders do not co-occur across looped layers, but that orbits and sliders both frequently co-occur with fixed point behavior. “Unknown” behavior often co-occurs with orbits, which we suggest may be due to mis-classification of the behavior algorithm.

### C.3 How Does Non-Fixed-Point Behavior Impact Stages of Inference?

To complete the link between non-fixed-point behavior and our work we additionally investigate how this behavior impacts the observed stages of inference.

To attempt to isolate the “worst case” scenario for stages of inference stability, we plot stages of inference for the GSM8k test prompt that exhibits the greatest orbit amplitude. We first plot in realized depth the extended stages of inference metrics used throughout the paper, see Fig. 16 . This demonstrates that sink rates show some variability with the orbiting behavior, but the other metrics remain broadly consistent. We plot also the same metrics in block depth (showing only the final 64 loops) in Fig. 17 : this demonstrates clearly that the stages of inference remain very consistent despite the orbiting behavior.

We plot the same for the largest amplitude orbit on the Retrofitted Llama model in Fig. 18 , demonstrating that the same behavior holds.

## Appendix D Additional Fixed Point Results

### D.1 Cyclic Similarity

We include here additional plots to validate our cyclic similarity claims in Sec. 4 .

Fig. 19 complements Fig. 2 by visualizing the cosine similarity between the residual streams after each layer for the range of Looped Transformers visualized in the original figure. Additional models (Huginn-0125 and all retrofitted models) are visualized in Fig. 19 for 32 recurrences, demonstrating that the cyclic similarity is consistent for larger numbers of recurrences. We note that Huginn-0125 continues its previous trend of all layer outputs converging to similar representations, with some cyclic similarity still visible. Fig. 21 similarly provides an extended version of Fig. 2 , demonstrating that attention matrix cyclic similarity holds to 32 recurrences.

### D.2 Fixed Point and Successive Differences

In Sec. 4 we demonstrate that retrofitted Llama and Huginn-0125 reach a fixed point but Ouro does not. We do so by – for each layer – computing an “approximate fixed point” after 128 recurrences and then plotting the norm of the difference for each layer at successive recurrences to this fixed point. In Fig. 22 we demonstrate that this same behavior is observed when considering cosine similarity to the fixed point, and in Fig. 23 we see that it holds for attention matrices.

We then demonstrated in Fig. 3 that all models, independent of whether they reach a strict fixed point or not, demonstrate converge towards very low difference norms between successive residual streams. We verify this same behavior holds for residual stream cosine similarities and attention matrix Frobenius norms in Figs. 24 and 25 respectively.

### D.3 Latent Space Trajectories

In this section we visualize additional latent space trajectories, supplementing Fig. 5 . All trajectories are plotted by taking all latent states of the final token position on the test sequence described in App. B , computing PCA on these latent state vectors and resultant dimensional reduction of this sequence of vectors. They are intended as illustrations to demonstrate qualitative behavior. Ouro is visualized in Fig. 26 and Huginn-0125 in Fig. 27 .

The Ouro trajectory is of particular interest as we are aware from the results in the main body of the paper that this model does not reach a strict fixed point. Fig. 26 demonstrates that – on this test sequence – Ouro reaches an approximately constant trajectory, but with visibly larger deviations even at later recurrences than Huginn-0125 in Fig. 27 .

However, we find evidence that this “approximately stable trajectory” behavior is not universal: for a simple “maths” test prompt ( The square root of 16 is ) shown in Fig. 28 , Ouro appears to reach a stable trajectory in recurrences 8-16 before departing from this and appearing to become “unstable”.

### D.4 Architecture Choices

Here we provide more complete results to supplement Sec. 4.2 , visualizing fixed point difference norms and cosine similarities for various architecture choices in Figs. 29 and 30 respectively.

We also verify that the results presented are not particular to 12 layers by visualising results for both 4 and 16 layers in Fig. 31 , showing qualitatively identical behavior.

## Appendix E Additional Stages of Inference Results

In this appendix we explore in more detail the mixing behavior presented in the main body via additional metrics, and considering a wider range of models.

### E.1 Input Independent Metrics

As our work is concerned largely with how the functionality of layers change throughout depth as the residual stream is iteratively updated, our primary concern is with input-dependent measures of stages of inference: ColSum concentration as presented in the main text of the paper is one such input-dependent metric, and the later sections of this appendix will introduce and present results for a wider range of such metrics.

However, to bridge the gap between our work and that of Lad et al. (2024) , we also present results for the fraction of prediction and suppression neurons ( Gurnee et al., 2024 ) in successive layers of both feedforward and looped Transformers. We highlight however that these are unable to change with successive recurrences , and are thus secondary to our focus. Fig. 32 presents results for a selection of feedforward models used throughout the paper, and Fig. 33 presents results for a selection of looped models used throughout the paper. Similar to our results elsewhere, we find that the looped model stages of inference in these metrics tend to mirror those of feedforward models.

### E.2 Input Dependent Metrics

One well-studied phenomenon by which Transformers drastically reduce the mixing in given layer is that of the attention sink ( Xiao et al., 2023 ; Barbero et al., 2025 ) , whereby the layer focuses the majority of the attention “weight” onto the first token in the sequence; often this is the BOS (beginning of sequence) token, and thus completely uninformative. To measure this behavior, we adopt the attention sink score and sink rate of Gu et al. (2024) : for token position k k and sequence length T T , the sink score at layer ℓ \ell and head h h is defined as: sink-score k ( ℓ , h ) = 1 T ​ ∑ t = 0 T − 1 A t ​ k ( ℓ , h ) , \text{sink-score}_{k}^{(\ell,h)}=\frac{1}{T}\sum_{t=0}^{T-1}A_{tk}^{(\ell,h)}, (16) where A t ​ k ( ℓ , h ) A_{tk}^{(\ell,h)} corresponds to the realized attention matrix of Eq. 2 at layer ℓ \ell , head h h . The sink rate is then defined as the fraction of heads for which the sink score lies above a certain threshold: sink-rate k ( ℓ ) = 1 H ​ ∑ h = 1 H 𝕀 ⁡ ( sink-score k ( ℓ , h ) ≥ τ ) , \text{sink-rate}^{(\ell)}_{k}=\frac{1}{H}\sum_{h=1}^{H}\mathbb{I}\!\left(\text{sink-score}_{k}^{(\ell,h)}\geq\tau\right), (17) where following related work we define a threshold of τ = 0.3 \tau=0.3 , and 𝕀 \mathbb{I} denotes the indicator function.

We also adopt the Mixing score of Queipo-de-Llano et al. (2025) : for sequence length T T , layer ℓ \ell and head h h this is defined as the average row entropy of the attention matrices: mixing-score ( ℓ , h ) = 1 T ∑ i = 1 T H ( A i , : ( ℓ , h ) ) . \text{mixing-score}^{(\ell,h)}=\frac{1}{T}\sum_{i=1}^{T}H(A_{i,:}^{(\ell,h)}). (18)

Following Skean et al. (2025) ; Queipo-de-Llano et al. (2025) we additionally measure the compression of the residual stream 𝑿 {\bm{X}} via the matrix-based entropy H ⁡ ( 𝑿 ) H({\bm{X}}) .

In the plots that follow we average sink rates, Mixing scores and ColSum concentrations over all the heads in a layer, and over all input sequences. Residual entropy is averaged over all input sequences.

### E.3 Cyclic Stages of Inference

Supplementing the cyclic recurrence in realized depth for retrofitted Llama in Fig. 7 , we additionally overlay cycles in realized depth for Ouro and Huginn-0125 in Fig. 34 , where all models are run for 8 recurrences. This demonstrates that for sink rates and mixing scores , the cyclic behavior and lack of significant depth-wise changes hold both for the other investigated models, and the additional stages of inference metrics.

The results for residual entropy are more nuanced: while the results for Huginn-0125 and the retrofitted models show broadly the same behavior as the attention-based metrics, Ouro demonstrates different behavior. As shown in Fig. 35 , the residual entropies both change significantly with successive recurrences and do not closely follow the feedforward behavior. We believe that the divergence from feedforward behavior may derive from the norm structure of this model: the residual stream is normalised after each recurrent block, as visualised in Fig. 9 , thus periodically shutting down massive activations. This is not the case for the retrofitted series of models, which lack this norm and show much closer alignment with feedforward stages of inference.

For completeness, we plot these stages of inference for all other models referenced in the paper. See Fig. 35 (Ouro 1.4B), Fig. 36 (Huginn-0125), Figs. 37 , 38 and 39 (retrofitted Llama, OLMo and TinyLlama).

We plot stages of inference for Ouro 2.6B in Fig. 40 . This model is interesting due to the training regime followed by Zhu et al. (2025) , which “upcycles” a 48 layer model from the 24 layer 1.4B parameter model. As a consequence, the first and second half of each recurrent block each independently align with the Llama feedforward stages of inference.

In Sec. 5 we suggested that the lack of stages of inference in Huginn-0125 is likely due to the normalization of the residual stream resulting in massive activations being unable to form. Here we further support this suggestion by ablating the massive activations from the Retrofitted Llama model (which does display stages of inference) via zeroing the output of the MLP in the second layer, which is responsible for its massive activations. In this setting, visualized in Fig. 41 , we see that the model no longer exhibits stages of inference comparable to the feedforward model, suggesting that the presence of massive activations is required for stages of inference to emerge in looped models.

### E.4 Non-Reasoning Stages of Inference

Throughout the rest of the paper, experiments are conducted on the GSM8k dataset. In this appendix we verify that the stages of inference we observe are not specific to this dataset, and also occur in a non-reasoning setting, for which we use the HellaSwag dataset ( Zellers et al., 2019 ) . We follow an identical experimental setup to the GSM8k experiments, running inference on 256 random examples from the test split.

We present results in Fig. 42 (Ouro 1.4B), Fig. 43 (Huginn-0125), Figs. 44 , 45 and 46 (retrofitted Llama, OLMo and TinyLlama). These show very few deviations from the GSM8k results, and the conclusions throughout the rest of the paper hold. However, we highlight the following small differences: • Across the board, sink rates tend to be higher in the HellaSwag setting.

• In Retrofitted OLMo-2, ColSum concentration appears to be slightly higher in the HellaSwag setting.

### E.5 Stability To Unseen Test-Time Recurrences

This section extends the results presented in Sec. 5.2 .

We supplement Fig. 11 by plotting how stages of inference change per-layer throughout recurrences for additional models: these can be found in Figs. 47 , 48 and 49 . The large standard deviations in Huginn-0125 and retrofitted Llama mixing scores reflect the fact that these models tend to reach different, but still stable, constant states.

We additionally plot the extended versions of Fig. 12 in Figs. 50 , 51 and 52 .

### E.6 How Architecture Choices Affect the Formation of Stages of Inference

Here we present additional results to supplement those in Sec. 5.1 . The extended stages of inference metrics for the models visualized in Fig. 10 are presented in Figs. 54 , 55 and 56 . Equivalent models with added input injection are visualized in Figs. 57 , 58 and 59 , and equivalent models without sandwich layers in Figs. 60 , 61 and 62 .

It appears in these small scale experiments that feedforward stages of inference are most closely replicated without input injection, and using sandwich layers, as in Figs. 54 , 55 and 56 . The addition of input injection appears to mean that the final recurrence follows the feedforward stages of inference more closely, but to the detriment of earlier recurrences.

## Appendix F Looped Floorplan

To illustrate the “similar attention patterns between recurrences” that we have discussed throughout the paper, in Fig. 63 we visualize all attention patterns for the Retrofitted Llama model on the test prompt. Increasing depth in the model is aligned with increased height up the page; Prelude and coda are outlined in blue and red respectively and separate recurrences are separated by a space.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
