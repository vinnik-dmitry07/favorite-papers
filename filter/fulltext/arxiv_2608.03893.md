##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse

###### Abstract

Production deployments often swap between different-sized models in a family for cost-quality cascading, mid-conversation switching, and routing, and each swap forces the receiver to repay the prefill from scratch. We propose cross-model KV cache transfer , where the receiver reuses the source’s KV cache, skipping prefill. We find that cross-model KV has substantial linear structure across matched-KV pairs, where source and target share KV head count and per-head dimension. On Qwen3 14B → \to 32B, one source layer explains 56% of variance in the target’s keys and 32% in values, rising to 79% and 65% with multiple source layers. Building on this, we design a closed-form ridge mapper that operates per head and proceeds in three steps. First, for each target layer we select the top- k k most predictive source layers and concatenate their KV as input. Second, we strip RoPE from the keys before mapping, so the fit is position-free and reusable across context lengths. Third, we fit ridge regression on a small calibration set of 500 FineWeb-Edu sequences of 1,024 tokens each. Surprisingly, across six pairs in three families, this linear mapper retains 73–98% of the receiver’s standalone-prefill accuracy on four pairs, while two degrade sharply. A nonlinear MLP recovers up to + 37 +37 pp HellaSwag retention on the failures. The mapper runs 2.7–25 × \times faster than re-prefill and remains stable across multi-turn handoff, making cross-model KV cache transfer practical.

## 1 Introduction

Production LLM serving increasingly involves long agentic sessions, where context accumulates across many turns. It also relies on multi-model orchestration for cost-quality cascading, mid-conversation switching, and routing ( OpenAI, 2025 ) . These practices swap between different-sized members of a model family ( Yang et al., 2025 ; Grattafiori et al., 2024 ) . Family members share core architectural choices and substantial pretraining data, but differ in architectural details and training recipe across scales. Both trends compound prefill cost. Long sessions stretch the prompt, and each model swap re-prefills the accumulated context on the receiver. Prefill is the forward pass that populates the KV cache before generation. Its cost scales with model size and prompt length. Prefix caching mitigates this within a single model only.

Since prefill’s output is the KV cache, reusing it across models reduces to a representation problem of transforming one model’s KV cache into another’s expected format. We call this cross-model KV cache transfer and restrict the present study to within-family transfer. The mapping is bidirectional. Small-to-large transfer upgrades quality, and large-to-small reduces cost. Figure 1 illustrates the pipeline. This pipeline generalizes intra-model KV reuse. Cross-layer sharing ( Brandon et al., 2024 ; Wu and Tu, 2024 ; Chang et al., 2025 ) exploits redundancy within a model, and prefix caching ( Zheng et al., 2024 ; Gim et al., 2024 ) reuses KV across requests of the same model. Cross-model KV cache transfer maps the cache values from one model to another .

Cross-model KV cache transfer is challenging because source and target can differ in layer count, hidden dimension, and KV head configuration. Prior work bridges these gaps with neural fusers ( Fu et al., 2026 ) , learned latent-space adapters ( Dery et al., 2026 ) , attention-pattern mapping ( Zhao et al., 2025 ) , or same-architecture KV sharing ( Liu et al., 2026 ) , each requiring gradient-based training or strong architectural assumptions (§ 2.2 ).

In this study, we show that the cross-model KV relationship exhibits substantial linear structure, admitting a small-sample, gradient-free fit. On Qwen3 14B → \to 32B, a single source layer explains 56% of variance in the target’s keys and 32% in values, rising to 79% and 65% with multiple source layers (§ 2.3 ). Building on this observation, we propose a closed-form per-head ridge mapper (§ 3 ) that combines three components: per-head ridge regression fit from a small calibration set, cross-layer source selection where each target layer draws from its top- k k most predictive source layers, and content-space (RoPE-stripped) mapping that decouples positional rotation from semantic content so the fit transfers across context lengths.

Across six matched-KV pairs from three families, where source and target share KV head count and per-head dimension (§ 4.2 ), the linear mapper retains 73–98% of standalone accuracy averaged across five benchmarks on its best pairs. We further find that error placement, not error magnitude, determines per-pair retention. A nonlinear MLP redistributes residual error away from attention-sensitive subspaces and adds up to + 37 +37 pp HellaSwag retention on harder pairs (§ 4.4 ). Across 12 matched-KV pair evaluations from three families, attention-output similarity correlates with HellaSwag retention at Pearson r = + 0.57 r{=}{+}0.57 and outperforms R 2 R^{2} (§ 4.5 ).

#### Contributions.

(1) Closed-form mapping framework. We propose a gradient-free framework for cross-model KV cache transfer based on per-head ridge regression. Two design choices are central: each target layer is fit from its top- k k most predictive source layers, and keys are mapped in RoPE-stripped content space so the fit transfers across context lengths (§ 3 ). (2) Multi-family validation. We validate the framework on six matched-KV pairs across three families. Four pairs retain 73–98% of standalone accuracy on five benchmarks at 2.7–25 × \times lower prefill latency than re-prefill in the small-to-large direction (§ 4.7 ). (3) Nonlinear extension. A nonlinear MLP adds up to + 37 +37 pp HellaSwag retention on harder Ministral pairs by redistributing residual error away from attention-sensitive subspaces (§ 4.4 , § 4.5 ). (4) Attention-output cosine predicts cross-pair retention. Across 12 matched-KV pair evaluations from three families, attention-output cosine correlates with HellaSwag retention at Pearson r = + 0.57 r{=}{+}0.57 , outperforming R 2 R^{2} ( r = − 0.20 r{=}{-}0.20 ). The same concentration analysis explains the + 37 +37 pp MLP gain as error redistribution toward attention-irrelevant directions (§ 4.5 ).

## 2 Background and motivation

### 2.1 Problem formulation

Consider a source model 𝒮 \mathcal{S} with L s L_{s} layers and a target model 𝒯 \mathcal{T} with L t L_{t} layers. Both use grouped-query attention with n kv s n_{\text{kv}}^{s} and n kv t n_{\text{kv}}^{t} KV heads of dimension d h s d_{h}^{s} and d h t d_{h}^{t} , respectively. For an input sequence 𝐱 = ( x 1 , … , x T ) \mathbf{x}=(x_{1},\ldots,x_{T}) of length T T , layer l ∈ { 1 , … , L s } l\in\{1,\ldots,L_{s}\} , head h ∈ { 1 , … , n kv s } h\in\{1,\ldots,n_{\text{kv}}^{s}\} of the source model produces keys and values 𝐊 s l , h , 𝐕 s l , h ∈ ℝ T × d h s \mathbf{K}_{s}^{l,h},\mathbf{V}_{s}^{l,h}\in\mathbb{R}^{T\times d_{h}^{s}} . We write 𝒞 𝒮 \mathcal{C}_{\mathcal{S}} for the full source KV cache across all layers and heads, and 𝒞 𝒯 \mathcal{C}_{\mathcal{T}} analogously for the target. Source and target share a tokenizer within a family, so the input sequence has the same length T T for both. We say a transfer pair has matched KV when n kv s = n kv t n_{\text{kv}}^{s}=n_{\text{kv}}^{t} and d h s = d h t d_{h}^{s}=d_{h}^{t} , even if L s L_{s} , L t L_{t} , or parameter counts differ across scales.

We seek a mapping f : 𝒞 𝒮 → 𝒞 ^ 𝒯 f\colon\mathcal{C}_{\mathcal{S}}\to\hat{\mathcal{C}}_{\mathcal{T}} such that the target model, decoding from 𝒞 ^ 𝒯 \hat{\mathcal{C}}_{\mathcal{T}} in place of its own 𝒞 𝒯 \mathcal{C}_{\mathcal{T}} , produces equivalent outputs: m ⁡ ( 𝒯 ⁡ ( 𝐱 , 𝒞 ^ 𝒯 ) ) ≈ m ⁡ ( 𝒯 ⁡ ( 𝐱 , 𝒞 𝒯 ) ) , m\bigl(\mathcal{T}(\mathbf{x};\hat{\mathcal{C}}_{\mathcal{T}})\bigr)\;\approx\;m\bigl(\mathcal{T}(\mathbf{x};\mathcal{C}_{\mathcal{T}})\bigr), (1) for a downstream task τ \tau with metric m m . We decompose f f into per-head mappings f K l , h f_{K}^{l,h} and f V l , h f_{V}^{l,h} that produce the target’s keys and values for each layer and head. We measure transfer quality by the target model’s downstream accuracy, not by reconstruction metrics alone.

### 2.2 Prior approaches

Recent cross-model KV-reuse methods each require either gradient-based training or architectural constraints. C2C ( Fu et al., 2026 ) trains per-pair neural fusers. LatentAlign ( Dery et al., 2026 ) learns per-model adapters into a shared latent space. IAM ( Zhao et al., 2025 ) substitutes small-model attention patterns , not KV values. DroidSpeak ( Liu et al., 2026 ) requires identical architecture. Further training-time approaches ( Woo et al., 2026b ; Woo et al., 2026a ) share the same gradient-based constraint. To the best of our knowledge, none investigates whether the cross-model KV relationship is simple enough for a closed-form, training-free mapping. Three orthogonal lines compose with the present work: intra-model cross-layer KV reuse ( Brandon et al., 2024 ; Wu and Tu, 2024 ; Chang et al., 2025 ) , prefill acceleration ( Liu et al., 2025 ; Upasani et al., 2026 ; Qiao et al., 2025 ) , and linear cross-LLM representation alignment ( Huh et al., 2024 ; Chen et al., 2025 ; Bello et al., 2025 ; Huang et al., 2025 ) . Table 6 (Appendix A ) summarizes the cross-model comparison.

### 2.3 Linear structure in cross-model KV

Before committing to a mapper architecture, we ask what structure the cross-model KV relationship has. We analyze this structure on Qwen3. The linear-structure result generalizes to other matched-KV pairs. We probe three cache types. K rope K_{\text{rope}} denotes keys as the model uses them. K stripped K_{\text{stripped}} denotes keys with the position-dependent RoPE rotation removed via 𝐑 Θ − 1 \mathbf{R}_{\Theta}^{-1} (see § 3.3 ). V V denotes values, which carry no positional encoding. For each cache type C ∈ { K rope , K stripped , V } C\in\{K_{\text{rope}},K_{\text{stripped}},V\} and each triple of source layer l ′ ∈ { 1 , … , L s } l^{\prime}\in\{1,\ldots,L_{s}\} , target layer l ∈ { 1 , … , L t } l\in\{1,\ldots,L_{t}\} , and head h h , we fit a single-source ordinary least-squares regression at the token level. Each of the N N calibration tokens, subsampled from FineWeb-Edu sequences as detailed in § 3.1 , contributes one observation, mapping the source’s per-token feature vector C s l ′ , h ∈ ℝ d h s C_{s}^{l^{\prime},h}\in\mathbb{R}^{d_{h}^{s}} to the target’s C t l , h ∈ ℝ d h t C_{t}^{l,h}\in\mathbb{R}^{d_{h}^{t}} , C ^ t l , h = C s l ′ , h ​ 𝐖 + 𝐛 , 𝐖 ∈ ℝ d h s × d h t , 𝐛 ∈ ℝ d h t , \hat{C}_{t}^{l,h}=C_{s}^{l^{\prime},h}\,\mathbf{W}+\mathbf{b},\qquad\mathbf{W}\in\mathbb{R}^{d_{h}^{s}\times d_{h}^{t}},\ \mathbf{b}\in\mathbb{R}^{d_{h}^{t}}, (2) treating C s l ′ , h C_{s}^{l^{\prime},h} as a row vector to match the production-mapper convention in § 3 . This is a per-(triple, cache type) probe, not the production mapper of § 3 , which concatenates several source layers and adds ridge regularization. We measure fit quality by the coefficient of determination R 2 R^{2} , averaged across the n kv t n_{\text{kv}}^{t} target heads to give a head-averaged R 2 R^{2} for each ( l ′ , l ) (l^{\prime},l) pair. Visualizing this as a heatmap with rows indexing source layers and columns indexing target layers (Figure 2 ) reveals four qualitative patterns. Per-pair quantitative numbers are reported in § 4 .

(1) High linear fit: a single linear regression already captures a large fraction of cross-model KV variance on the most predictable target layers. Head-averaged R 2 R^{2} is well above zero along the diagonal, and the best single source–target cell reaches K stripped K_{\text{stripped}} R 2 = 0.81 R^{2}{=}0.81 on Qwen3 14B → \to 32B and 0.65 0.65 on the weaker 8B → \to 32B at the heatmap peaks. Layer-averaged production-ridge R 2 R^{2} is reported in Appendix C . (2) Closer models give sharper diagonals: larger architectural and depth gaps diffuse the pattern. (3) RoPE contaminates the fit: stripping RoPE generally sharpens the diagonal, motivating the position–content decomposition in § 3.3 . (4) K is more predictable than V: typically a ∼ \sim 0.2 gap in head-averaged R 2 R^{2} (Appendix B ).

#### How many source layers does the mapper need?

The probe uses a single source layer. We extend it with greedy forward selection, iteratively adding the source layer that maximally increases R 2 R^{2} . Complementary information is distributed across multiple source layers. On Qwen3 14B → \to 32B, k = 1 k{=}1 captures only 66 % 66\% of the k = all k{=}\text{all} R 2 R^{2} for K stripped K_{\text{stripped}} and 42 % 42\% for V V , with the largest gain from k = 1 k{=}1 to k = 4 k{=}4 and R 2 R^{2} close to its k = all k{=}\text{all} value by k = 6 k{=}6 (Appendices B and C ). This motivates the top- k k selection (§ 3.2 ).

## 3 Mapper design

Figure 3 illustrates the mapper for one target (layer l l , head h h ) pair. A top- k k subset of source layers is selected per target layer by R 2 R^{2} , the selected source keys and values are concatenated, and independent ridge regressions 𝐖 K \mathbf{W}_{K} , 𝐖 V \mathbf{W}_{V} map them to the target. Each mapper is a closed-form linear solve repeated independently for all L t × n kv t L_{t}\times n_{\text{kv}}^{t} target heads. The mapper has three components: per-head ridge (§ 3.1 ), cross-layer source selection (§ 3.2 ), and content-space mapping (§ 3.3 ).

### 3.1 Per-head ridge regression

Source and target differ in layer count ( L s ≠ L t L_{s}\neq L_{t} ), head dimension ( d h s ≠ d h t d_{h}^{s}\neq d_{h}^{t} ), and potentially KV head count ( n kv s ≠ n kv t n_{\text{kv}}^{s}\neq n_{\text{kv}}^{t} ). We address this by fitting an independent linear mapping per target (layer, head): 𝐊 ^ t l , h = 𝐗 K l ​ 𝐖 K l , h + 𝐛 K l , h , 𝐕 ^ t l , h = 𝐗 V l ​ 𝐖 V l , h + 𝐛 V l , h , \hat{\mathbf{K}}_{t}^{l,h}=\mathbf{X}_{K}^{l}\mathbf{W}_{K}^{l,h}+\mathbf{b}_{K}^{l,h},\qquad\hat{\mathbf{V}}_{t}^{l,h}=\mathbf{X}_{V}^{l}\mathbf{W}_{V}^{l,h}+\mathbf{b}_{V}^{l,h}, (3) where 𝐗 K l \mathbf{X}_{K}^{l} concatenates source key features from the k k selected source layers (§ 3.2 ) and 𝐖 K l , h ∈ ℝ ( k ⋅ n kv s ⋅ d h s ) × d h t \mathbf{W}_{K}^{l,h}\in\mathbb{R}^{(k\cdot n_{\text{kv}}^{s}\cdot d_{h}^{s})\times d_{h}^{t}} is the weight matrix.

#### Fitting.

Stacking N N calibration tokens gives a design matrix 𝐗 ∈ ℝ N × ( k ​ n kv s ​ d h s ) \mathbf{X}\in\mathbb{R}^{N\times(k\,n_{\text{kv}}^{s}\,d_{h}^{s})} and a response matrix 𝐘 ∈ ℝ N × d h t \mathbf{Y}\in\mathbb{R}^{N\times d_{h}^{t}} . We use ridge with λ = 0.01 \lambda=0.01 rather than pure OLS for numerical conditioning. The feature dimension can reach tens of thousands at large k k and the top- k k selected source layers are by construction correlated, so 𝐗 ⊤ ​ 𝐗 \mathbf{X}^{\top}\mathbf{X} is near-singular. The Tikhonov term stabilizes the inverse with negligible fit bias. The closed-form solution is 𝐖 ∗ = ( 𝐗 ⊤ ​ 𝐗 + λ ​ 𝐈 ) − 1 ​ 𝐗 ⊤ ​ 𝐘 . \mathbf{W}^{*}=(\mathbf{X}^{\top}\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^{\top}\mathbf{Y}. (4) We center 𝐗 \mathbf{X} and 𝐘 \mathbf{Y} before solving, so 𝐖 ∗ \mathbf{W}^{*} above estimates the slope and the bias in Eq. 3 is recovered as 𝐛 = 𝐘 ¯ − 𝐗 ¯ ​ 𝐖 ∗ \mathbf{b}=\bar{\mathbf{Y}}-\bar{\mathbf{X}}\mathbf{W}^{*} . Calibration data consists of 500 FineWeb-Edu sequences of length 1024, stride-4 subsampled to N ≈ 128 N\approx 128 K tokens per target head. Total mapper size (K plus V) is 2 ​ L t ​ n kv t ​ ( k ​ n kv s ​ d h s ) ​ d h t 2\,L_{t}\,n_{\text{kv}}^{t}\,(k\,n_{\text{kv}}^{s}\,d_{h}^{s})\,d_{h}^{t} , with per-pair sizes in Appendix D . Fitting takes ∼ \sim 47–87 min per pair on a single 8 × 8\times H100 node with no gradient-based training. Fitting-time scaling is sub-linear in the target head count because forming 𝐗 ⊤ ​ 𝐗 \mathbf{X}^{\top}\mathbf{X} ( 𝒪 ⁡ ( N ​ d s 2 ) \mathcal{O}(Nd_{s}^{2}) , with d s = k ​ n kv s ​ d h s d_{s}=k\,n_{\text{kv}}^{s}\,d_{h}^{s} the source feature dimension) dominates wall time and is computed once per target layer, shared across its heads. Per-pair times are in Appendix E .

### 3.2 Cross-layer source selection

The source and target have different numbers of layers, raising the question of which source layers should inform each target layer’s mapping. § 2.3 showed that not all source layers are equally informative for a given target layer. For each target layer l l , we therefore select the top- k k source layers by head-averaged R 2 R^{2} averaged over RoPE-stripped keys and values, concatenate their KV features, and fit the multi-source ridge regression of § 3.1 : 𝐗 K l = [ 𝐊 ¯ s l 1 ∥ 𝐊 ¯ s l 2 ∥ ⋯ ∥ 𝐊 ¯ s l k ] , \mathbf{X}_{K}^{l}=[\bar{\mathbf{K}}_{s}^{l_{1}}\,\|\,\bar{\mathbf{K}}_{s}^{l_{2}}\,\|\,\cdots\,\|\,\bar{\mathbf{K}}_{s}^{l_{k}}], (5) where 𝐊 ¯ s l i ∈ ℝ T × ( n kv s ⋅ d h s ) \bar{\mathbf{K}}_{s}^{l_{i}}\in\mathbb{R}^{T\times(n_{\text{kv}}^{s}\cdot d_{h}^{s})} is the concatenation of all Key heads from source layer l i l_{i} , and { l 1 , … , l k } \{l_{1},\ldots,l_{k}\} are the top- k k source layers for target layer l l . 𝐗 V l \mathbf{X}_{V}^{l} is constructed analogously from Value heads. All heads within a target layer share the same selected source layers, enabling cross-head information flow. The number of source layers k k is a hyperparameter selected per pair by a sweep (§ 4.1 ). Cross-layer source selection is the largest single contributor among the three mapper components (§ 4.3 ).

### 3.3 Content-space mapping (RoPE factoring)

Standard RoPE ( Su et al., 2024 ) applies a position-dependent rotation to queries and keys. The KV cache stores only the rotated keys 𝐤 RoPE ​ ( t ) = 𝐑 Θ ​ ( t ) ​ 𝐤 content \mathbf{k}_{\text{RoPE}}(t)=\mathbf{R}_{\Theta}(t)\,\mathbf{k}_{\text{content}} , while queries are recomputed at decode time. Decoupling RoPE from content makes the mapping pipeline modular. The per-head ridge weights are computed in a position-free space, so they remain valid across pairs with different RoPE configurations and at any position the target’s RoPE supports. Fitting the mapper directly on RoPE-coupled keys also works within noise on short-context benchmarks (Table 2 ), but ties the weights to the 1024-token position distribution seen at fit. The decoupled formulation extends to longer contexts by construction, which matters for serving prompts up to 32k tokens (§ 4.7 ).

Concretely, we strip source RoPE, apply 𝐖 K \mathbf{W}_{K} in the position-free space, and re-encode with target RoPE: 𝐊 ^ t = ( 𝐊 s ​ 𝐑 Θ s − 1 ​ ( t ) ​ 𝐖 K + 𝐛 K ) ​ 𝐑 Θ t ​ ( t ) \hat{\mathbf{K}}_{t}=(\mathbf{K}_{s}\,\mathbf{R}_{\Theta_{s}}^{-1}(t)\,\mathbf{W}_{K}+\mathbf{b}_{K})\,\mathbf{R}_{\Theta_{t}}(t) . During calibration the regression targets 𝐘 \mathbf{Y} are constructed by stripping the target RoPE from the target’s ground-truth keys, so 𝐖 K \mathbf{W}_{K} is fit entirely in the position-free space. Since 𝐑 Θ \mathbf{R}_{\Theta} is orthogonal, the inversion is exact at negligible cost. Values carry no positional encoding and are mapped directly.

## 4 Experiments

We evaluate four questions: (1) How well does ridge match the target’s own KV across three families (§ 4.2 )? (2) Which components matter (§ 4.3 )? (3) Can a nonlinear mapper recover the pairs where ridge falls short (§ 4.4 ), and what determines per-pair outcomes (§ 4.5 )? (4) Does transfer hold up in multi-turn (§ 4.6 ), and what is the latency advantage (§ 4.7 )?

### 4.1 Setup

#### Model families.

We evaluate three matched-KV families (Qwen3, Llama 3.1, Ministral 3) where source and target share KV head count and per-head dimension across scales (full table in Appendix D ). All families use dense full-attention, so every target layer receives mapped KV. Models are post-trained (Qwen3, Ministral 3) or base (Llama 3.1), evaluated in completion mode.

#### Benchmarks.

We evaluate on five accuracy benchmarks plus WikiText-2 perplexity: ARC-Challenge ( Clark et al., 2018 ) , HellaSwag ( Zellers et al., 2019 ) , WinoGrande ( Sakaguchi et al., 2020 ) , MMLU 5-shot ( Hendrycks et al., 2021 ) , GSM8K 8-shot with chain-of-thought prompting ( Cobbe et al., 2021 ; Wei et al., 2022 ) , and prefix-conditioned WikiText-2 perplexity. CoQA ( Reddy et al., 2019 ) measures multi-turn handoff (§ 4.6 ). All five accuracy benchmarks are evaluated on all six pairs at each pair’s selected k k . Perplexity coverage and its protocol are in Appendix D . Retention is ( transfer accuracy ) / ( target standalone accuracy ) × 100 % (\text{transfer accuracy})/(\text{target standalone accuracy})\times 100\% . Benchmarks differ in their chance floor, so we also report floor-normalized retention, ( acc − chance ) / ( target − chance ) (\text{acc}-\text{chance})/(\text{target}-\text{chance}) , which places chance at 0% and the target’s own accuracy at 100% on every benchmark.

#### Mapper configuration.

All pairs use ridge ( λ = 0.01 \lambda=0.01 ) and content-space mapping. The number of source layers k k is swept over { 1 , 2 , 4 , 6 , 8 , 10 , 12 , 16 , 20 , 24 , all } \{1,2,4,6,8,10,12,16,20,24,\text{all}\} . We select a single k k per pair as the value that maximizes the arithmetic mean of the log-likelihood benchmark accuracies (ARC-C, HellaSwag, WinoGrande, MMLU), breaking near-ties toward larger k k for evaluation coverage. GSM8K, CoQA multi-turn, and prefill latency are held out from this selection. Including a benchmark in the criterion raises its own reported accuracy by at most 2.49 2.49 pp (Appendix H ). Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB), and the family table are in Appendix D .

### 4.2 Main results

Main results focus on small-to-large (S → \to L) transfer across six matched-KV pairs from three families. Large-to-small (L → \to S) evaluation is limited to HellaSwag and appears in the mechanism analysis (§ 4.5 ) and multi-turn evaluation (§ 4.6 ). All pairs are evaluated at their selected k k with the full pipeline. Outcomes vary widely (42–98% Avg retention). Table 1 reports the headline per-pair numbers. Full per-family tables are in Appendix F .

Two observations structure the rest of the paper. (1) Tier 1. Four matched-KV pairs retain 73 73 – 98 % 98\% of target accuracy averaged across the five benchmarks: Qwen3 14B → \to 32B, Qwen3 8B → \to 32B, Llama 3.1 8B → \to 70B (the most extreme parameter ratio in our evaluation), and Ministral 3B → \to 8B. (2) Tier 2. Two matched-KV pairs degrade sharply: Ministral 8B → \to 14B and Ministral 3B → \to 14B fall to 42–44% Avg, and to 11–15% once floor-normalized. Together, the two tiers show that matched KV correlates with success but does not guarantee it. § 4.4 and § 4.5 investigate what additional factors determine per-pair outcomes. Figure 8 (Appendix F ) visualizes retention across benchmarks.

### 4.3 Ablation

We characterize the mapper on Qwen3 14B → \to 32B, the highest-retention pair, where any degradation is most visible. Table 2 reports component ablations, and calibration sensitivity to λ \lambda , N N , and calibration domain is in Appendix C .

(1) Cross-layer source selection is the largest contributor. Reducing k k from 8 8 to 1 1 drops K R 2 R^{2} from 0.79 0.79 to 0.56 0.56 (Appendix C ). (2) Content-space mapping is benchmark-specific. Disabling inference-time RoPE handling collapses MMLU and GSM8K to near random while HellaSwag falls only ∼ \sim 5 pp. (3) Calibration is robust. A four-order-of-magnitude sweep of λ \lambda and a 50–1000 sequence sweep of N N both show wide flat regions, with collapse only at λ = 1 \lambda{=}1 . Sample count flattens after N = 200 N{=}200 , with N = 50 N{=}50 still within ∼ \sim 1.6 pp of production. Domain is the one axis with real cost: CodeAlpaca drops 5.24 pp on HellaSwag while Wikipedia stays within noise.

### 4.4 Substituting MLP for ridge

The natural follow-up to § 4.2 is whether a nonlinear mapper recovers the pairs where ridge falls short. We train a per-(target layer, head, K | | V) MLP on the same MSE loss as ridge and use it as a drop-in replacement at inference. The MLP has two 1,024-unit ReLU-activated hidden layers trained with Adam (full settings in Appendix E ). We evaluate four Qwen3 and Ministral 3 pairs covering the success-to-failure range using the same downstream evaluation pipeline as ridge, so the only factor that changes is the mapper functional form.

Table 3 shows two observations. On the pairs where ridge already succeeds, MLP slightly underperforms ridge. On the pairs where ridge fails, MLP recovers HellaSwag retention by + 24.3 +24.3 to + 36.8 +36.8 pp, which puts all four pairs above 90 % 90\% under the MLP. Linear ridge is sufficient where the cross-model KV relationship is already linear, and the MLP helps only where ridge falls short rather than dominating ridge across the board.

What changes between ridge and MLP on the failure pairs? On the HellaSwag tokens used for evaluation, ridge’s R K 2 R^{2}_{K} is deeply negative (Table 4 ), meaning the calibration-fit linear mapper does not extrapolate. MLP closes most of that gap. § 4.5 shows that calibration R 2 R^{2} does not predict retention across pairs, and that this gain coincides with lower error concentration and higher attention-output cosine.

### 4.5 What determines transfer quality?

Calibration R 2 R^{2} is the natural a priori metric for transfer quality. If it predicted retention, deployment screening could rely on the fit alone. Across our six matched-KV pairs evaluated in both directions, however, R 2 R^{2} alone does not predict per-pair outcomes. Llama 3.1 8B → \to 70B fits ridge with R K 2 = 0.84 R^{2}_{K}{=}0.84 on calibration data and retains 94% HellaSwag small-to-large, but only 37% large-to-small. Ministral 3B → \to 8B fits at the same R K 2 = 0.84 R^{2}_{K}{=}0.84 and retains 93% in both directions. The same calibration R 2 R^{2} produces very different downstream outcomes. § 4.4 additionally showed that switching ridge for an MLP recovers up to + 37 +37 pp downstream on the pairs where ridge falls short. Two questions follow. What scalar predicts retention better than R 2 R^{2} across pairs, and what does the MLP do differently from ridge on the failure pairs?

#### Attention-output cosine.

R 2 R^{2} measures how closely the mapper reconstructs each K and V channel on average, weighting all dimensions equally. Attention does not. It scores K against the target’s queries 𝐐 \mathbf{Q} and weights V by the resulting attention pattern. The quantity that decides whether downstream behavior is preserved is the attention output the target would have computed. We measure it directly with cosine similarity between the attention output from mapped KV and from ground-truth KV, averaged over layers and heads. Across 12 matched-KV pair evaluations from three families (six S → \to L and six L → \to S directions), mean cosine correlates with HellaSwag retention at Pearson r = + 0.57 r{=}{+}0.57 , while calibration-domain R K 2 R^{2}_{K} shows essentially no correlation ( r = − 0.20 r{=}{-}0.20 ). R 2 R^{2} remains useful within a single pair, for example for source-layer selection, but is not the right scalar across pairs.

Cosine summarizes attention fidelity at the pair level. To explain why different mappers with similar R 2 R^{2} produce different cosine, we look at where the residual error lands per head.

#### Where the mapper’s error lands.

We measure error concentration per head. For K, we project the mapper’s per-token K error onto the right singular vectors of the target’s per-head query matrix 𝐐 h \mathbf{Q}_{h} and weight each component by the matching squared singular value. Dividing by the mean error across all components gives the K-concentration. For V, we weight per-position V error by the squared GT attention weight at that position and divide by the mean per-position error. Both quantities are averaged across heads. Concentration above 1 means the error concentrates where attention reads, while below 1 means it lands where attention ignores.

#### MLP intervention.

This explains the § 4.4 puzzle and clarifies the role of the nonlinear mapper. We compare ridge and MLP on the same four pairs, same calibration data, only the mapper changing. Table 4 shows the per-pair shifts. On the pairs where ridge falls short the MLP substantially lowers K-concentration ( Δ ≈ − 2.5 \Delta{\approx}{-}2.5 on average) and raises attention-output cosine ( Δ ≈ + 0.45 \Delta{\approx}{+}0.45 ), with HellaSwag retention rising by + 24.3 +24.3 to + 36.8 +36.8 pp. Where ridge already succeeds the shifts are far smaller and retention does not follow: Ministral 3B → \to 8B improves on both quantities and still loses ground on HellaSwag. Redistributing error is therefore not sufficient on its own. It changes downstream accuracy only where the misplaced error was large enough to bind, which is why linear ridge is enough wherever the cross-model KV relationship is already linear. The same shift lifts eval-domain R K 2 R^{2}_{K} from deeply negative to near zero on the failure pairs, though it stays below zero: ridge’s calibration-domain fit does not extrapolate to HellaSwag tokens, while the MLP closes most of that gap.

### 4.6 Multi-turn handoff

The mid-conversation switching scenario alternates between source and target across turns, so we measure drift on Qwen3 14B ↔ \leftrightarrow 32B with CoQA ( Reddy et al., 2019 ) on 100 conversations of ∼ \sim 15 turns each across five domains. We score each turn’s answer with F1 against the ground-truth and define drift at turn t t as the F1 gap between the target’s standalone accuracy and the mapper’s accuracy at the same turn. Drift stays small in both directions (Figure 4 ). The small-to-large gap widens by 1.7 1.7 pp from turn 1 to turn 10, with the mapper holding steady while the 32B ceiling rises. Large-to-small drift grows linearly at 0.33 0.33 pp/turn. Both slopes are too small for cascading failure within ten turns on this single-pair evaluation, though linear large-to-small drift would still accumulate over very long sessions. Tuning k k on the multi-turn task changes drift by at most 2.0 2.0 pp (dotted lines).

### 4.7 Prefill latency

The cost we want to skip is the receiver’s prefill, so we compare end-to-end re-prefill latency against KV cache transfer latency on Qwen3 14B ↔ \leftrightarrow 32B. The mapper replaces the target’s transformer body with a per-layer batched matrix multiply, letting the receiver decode directly from the mapped cache. Table 5 reports per-sequence-length latency. The mapper runs 4–25 × \times faster small-to-large and 3–7 × \times faster large-to-small across sequence lengths from 64 to 32,768 tokens. The large-to-small speedup widens with sequence length because the mapper’s wall time grows much slower than the receiver’s re-prefill. The full sequence-length sweep is in Appendix G .

## 5 Broader impact, future work, and limitations

#### Broader impact.

Cross-model KV cache transfer skips re-prefill on the receiver, reducing serving cost, energy, and tail latency for agentic workloads with frequent model swaps in cost-quality cascading, mid-conversation switching, and routing.

#### Future work.

(1) Trained mapper alternatives. Linear regression fits from a small calibration set without backpropagation, which made it the practical starting point. The MLP results in § 4.4 show that nonlinear variants can recover the matched-KV pairs where ridge falls short, so systematic comparison across MLP, MoE, and attention-aligned objectives that directly optimize cosine is a natural follow-up. (2) Predictive transferability. Attention-output cosine acts as a post-hoc diagnostic since it requires fitting the mapper. A signal that estimates transferability before fitting would accelerate deployment screening, with downstream retention on representative workloads such as HellaSwag as one candidate proxy. (3) Cross-family transfer. Whether the closed-form approach extends across families such as Qwen3 → \to Llama 3.1 is open. Different families may share enough representation structure to admit a similar mapping, or may require different machinery. (4) Hidden factors. Beyond architecture, training-data overlap, fine-tuning recipe, and other non-architectural factors may also influence transferability. We leave systematic study of these to future work. (5) Hybrid architectures. Extending the mapper to attention-restricted hybrids (sliding-window, local) and to attention-recurrent hybrids such as Nemotron 3 ( Blakeman et al., 2025 ) that carry SSM state alongside KV is a natural next step.

#### Limitations.

(1) Single-domain calibration. Calibration uses only FineWeb-Edu. Appendix C measures the cost of substituting Wikipedia or CodeAlpaca on one pair. Neither substitution separates subject matter from register, so the sweep does not bound calibration confined to a single field such as medicine or law. (2) k k selection. Per-pair k k is selected on the same log-likelihood benchmarks we report on. Appendix H measures the effect, at most 2.49 2.49 pp, and adds a held-out evaluation, though neither is a substitute for selecting k k out of sample. (3) Matched-KV is empirical. The closed-form mapper imposes no structural requirement on source or target dimensions, but our six pairs are all matched-KV by construction. We do not test mismatched-KV pairs. Whether ridge transfer can succeed under mismatched-KV conditions is left to future work. (4) Scope. Within-family transfer over dense full-attention models. Hybrid attention and attention-recurrent architectures are out of scope.

## 6 Conclusion

Cross-model KV cache transfer within an LLM family admits a closed-form, training-free fit. The cross-model KV relationship is largely linear, and a closed-form per-head ridge mapping retains 73–98% of standalone accuracy on the four highest-retention matched-KV pairs in our evaluation, runs 2.7–25 × \times faster than re-prefill, and remains stable across multi-turn handoff. Per-pair retention is determined by where the residual error lands relative to the target’s attention-sensitive subspaces, not by its magnitude. Attention-output cosine captures this and predicts cross-pair retention better than R 2 R^{2} ( r = + 0.57 r{=}{+}0.57 vs. r = − 0.20 r{=}{-}0.20 over 12 matched-KV pair evaluations from three families), and a nonlinear MLP adds up to + 37 +37 pp HellaSwag retention on harder pairs by redistributing error toward attention-irrelevant directions. These results shift evaluation criteria for cross-model mappers from raw reconstruction metrics to subspace-aware diagnostics, and motivate attention-aligned objectives for future cross-model mappers.

## References

Bello et al. [2025] Femi Bello, Anubrata Das, Fanzhi Zeng, Fangcong Yin, and Leqi Liu. Linear representation transferability hypothesis: Leveraging small models to steer large models. arXiv preprint arXiv:2506.00653 , 2025.

Blakeman et al. [2025] Aaron Blakeman, Aaron Grattafiori, Aarti Basant, Abhibha Gupta, Abhinav Khattar, Adi Renduchintala, Aditya Vavre, Akanksha Shukla, Akhiad Bercovich, Aleksander Ficek, et al. Nvidia nemotron 3: Efficient and open intelligence. arXiv preprint arXiv:2512.20856 , 2025.

Brandon et al. [2024] William Brandon, Mayank Mishra, Aniruddha Nrusimha, Rameswar Panda, and Jonathan Ragan-Kelley. Reducing transformer key-value cache size with cross-layer attention. In Advances in Neural Information Processing Systems (NeurIPS) , 2024.

Chang et al. [2025] Chi-Chih Chang, Chien-Yu Lin, Yash Akhauri, Wei-Cheng Lin, Kai-Chiang Wu, Luis Ceze, and Mohamed S. Abdelfattah. xKV: Cross-layer SVD for KV-cache compression. arXiv preprint arXiv:2503.18893 , 2025.

Chen et al. [2025] Alan Chen, Jack Merullo, Alessandro Stolfo, and Ellie Pavlick. Transferring linear features across language models with model stitching. In Advances in Neural Information Processing Systems (NeurIPS) , 2025.

Clark et al. [2018] Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? Try ARC, the AI2 reasoning challenge. arXiv preprint arXiv:1803.05457 , 2018.

Cobbe et al. [2021] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168 , 2021.

Dery et al. [2026] Lucio M. Dery, Zohar Yahav, Henry Prior, Qixuan Feng, Jiajun Shen, and Arthur Szlam. Latent space communication via K-V cache alignment. arXiv preprint arXiv:2601.06123 , 2026.

Fu et al. [2026] Tianyu Fu, Zihan Min, Hanling Zhang, Jichao Yan, Guohao Dai, Wanli Ouyang, and Yu Wang. Cache-to-cache: Direct semantic communication between large language models. In International Conference on Learning Representations (ICLR) , 2026.

Gim et al. [2024] In Gim, Guojun Chen, Seung-seob Lee, Nikhil Sarda, Anirudh Khandelwal, and Lin Zhong. Prompt cache: Modular attention reuse for low-latency inference. In Conference on Machine Learning and Systems (MLSys) , 2024.

Grattafiori et al. [2024] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783 , 2024.

Hendrycks et al. [2021] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Measuring massive multitask language understanding. In International Conference on Learning Representations (ICLR) , 2021.

Huang et al. [2025] Youcheng Huang, Chen Huang, Duanyu Feng, Wenqiang Lei, and Jiancheng Lv. Cross-model transferability among large language models on the platonic representations of concepts. In Annual Meeting of the Association for Computational Linguistics (ACL) , 2025.

Huh et al. [2024] Minyoung Huh, Brian Cheung, Tongzhou Wang, and Phillip Isola. The platonic representation hypothesis. In International Conference on Machine Learning (ICML) , 2024.

Liu et al. [2025] Jingyu Liu, Beidi Chen, and Ce Zhang. Speculative prefill: Turbocharging TTFT with lightweight and training-free token importance estimation. In International Conference on Machine Learning (ICML) , 2025.

Liu et al. [2026] Yuhan Liu, Yuyang Huang, Jiayi Yao, Shaoting Feng, Zhuohan Gu, Kuntai Du, Hanchen Li, Yihua Cheng, Junchen Jiang, Shan Lu, Madan Musuvathi, and Esha Choukse. DroidSpeak: KV cache sharing across fine-tuned model variants. In USENIX Symposium on Networked Systems Design and Implementation (NSDI) , 2026.

OpenAI [2025] OpenAI. Introducing GPT-5. https://openai.com/index/introducing-gpt-5/, 2025.

Qiao et al. [2025] Aurick Qiao, Zhewei Yao, Samyam Rajbhandari, and Yuxiong He. SwiftKV: Fast prefill-optimized inference with knowledge-preserving model transformation. In Conference on Empirical Methods in Natural Language Processing (EMNLP) , 2025.

Reddy et al. [2019] Siva Reddy, Danqi Chen, and Christopher D. Manning. CoQA: A conversational question answering challenge. Transactions of the Association for Computational Linguistics , 2019.

Sakaguchi et al. [2020] Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. WinoGrande: An adversarial Winograd schema challenge at scale. In AAAI Conference on Artificial Intelligence (AAAI) , 2020.

Su et al. [2024] Jianlin Su, Murtadha Ahmed, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. RoFormer: Enhanced transformer with rotary position embedding. Neurocomputing , 2024.

Upasani et al. [2026] Shubhangi Upasani, Ravi Shanker Raju, Bo Li, Mengmeng Ji, John Long, Chen Wu, Urmish Thakker, and Guangtao Wang. Cross-family speculative prefill: Training-free long-context compression with small draft models. arXiv preprint arXiv:2603.02631 , 2026.

Wei et al. [2022] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. In Advances in Neural Information Processing Systems (NeurIPS) , 2022.

Woo et al. [2026a] Sunghyeon Woo, Jaeeun Kil, Hoseung Kim, Minsub Kim, Joonghoon Kim, Ahreum Seo, Sungjae Lee, Minjung Jo, Jiwon Ryu, Baeseong Park, Se Jung Kwon, and Dongsoo Lee. ICaRus: Identical cache reuse for efficient multi-model inference. In International Conference on Learning Representations (ICLR) , 2026a.

Woo et al. [2026b] Sunghyeon Woo, Hoseung Kim, Sunghwan Shim, Minjung Jo, Hyunjoon Jeong, Jeongtae Lee, Joonghoon Kim, Sungjae Lee, Baeseong Park, Se Jung Kwon, and Dongsoo Lee. PrefillShare: A shared prefill module for KV reuse in multi-LLM disaggregated serving. arXiv preprint arXiv:2602.12029 , 2026b.

Wu and Tu [2024] Haoyi Wu and Kewei Tu. Layer-condensed KV cache for efficient inference of large language models. In Annual Meeting of the Association for Computational Linguistics (ACL) , 2024.

Yang et al. [2025] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388 , 2025.

Zellers et al. [2019] Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. HellaSwag: Can a machine really finish your sentence? In Annual Meeting of the Association for Computational Linguistics (ACL) , 2019.

Zhao et al. [2025] Yi Zhao, Zuchao Li, and Hai Zhao. IAM: Efficient inference through attention mapping between different-scale LLMs. In Annual Meeting of the Association for Computational Linguistics (ACL) , 2025.

Zheng et al. [2024] Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Sun, Jeff Huang, Cody Hao Yu, Shiyi Cao, Christos Kozyrakis, Ion Stoica, Joseph E. Gonzalez, Clark Barrett, and Ying Sheng. SGLang: Efficient execution of structured language model programs. In Advances in Neural Information Processing Systems (NeurIPS) , 2024.

## Appendix A Cross-model KV cache transfer methods

This appendix tabulates the cross-model KV cache transfer methods discussed in the prose comparison of § 2.2 . Each row records whether the method is gradient-free, whether it works cross-scale (different parameter counts), whether it transfers KV values rather than attention patterns, and whether the mapping is closed-form. Our method is the only one that satisfies all four criteria.

† DroidSpeak transfers KV only between architecturally identical models (same hidden size, layer count, head configuration). The cross-scale and closed-form columns are therefore marked “—” as inapplicable rather than absent.

## Appendix B Linear structure analysis

This appendix collects the empirical evidence for the linear-structure claim in § 2.3 : the greedy forward-selection curves that quantify how many source layers the mapper actually needs. The pairwise R 2 R^{2} heatmaps that motivate the four qualitative patterns are inlined as Figure 2 in § 2.3 , and the production-ridge R 2 R^{2} at k = 1 , 8 , all k{=}1,8,\text{all} is in Appendix C .

#### Source layer selection by greedy forward selection.

The single-source R 2 R^{2} probe in § 2.3 measures how predictable each target layer is from a single source layer. Here we ask how many source layers the mapper actually needs by greedy forward selection. Starting from the best single source layer, we iteratively add the source layer that maximally increases joint R 2 R^{2} at each step, producing curves from k = 1 k{=}1 to k = all k{=}\text{all} .

The curves climb steeply from k = 1 k{=}1 to k = 4 k{=}4 and are close to their k = all k{=}\text{all} value by k = 6 k{=}6 . Quantitatively, even on the sharpest pair (Qwen3 14B → \to 32B), picking the best single source layer per target and averaging across target layers reaches only R 2 = 0.56 R^{2}{=}0.56 for K stripped K_{\text{stripped}} and 0.32 0.32 for V V , while k = 8 k{=}8 aggregation reaches 0.79 0.79 and 0.65 0.65 respectively. The same 0.56 0.56 appears as the production-ridge k = 1 k{=}1 row of Table 7 ; this is a weaker quantity than the per-cell heatmap peak of 0.81 0.81 in § 2.3 , which singles out the most predictable target layer. Complementary information is distributed across layers for both K and V, motivating top- k k cross-layer selection in our mapper design (§ 3.2 ). Figure 5 uses greedy forward selection (joint R 2 R^{2} maximization per target layer and head). Our production mapper (§ 3.2 ) uses fixed top- k k by single-source head-averaged R 2 R^{2} for tractability. Both support the same qualitative conclusion that complementary information is distributed across multiple source layers.

## Appendix C Extended ablation

This appendix collects the ablation tables and figures supporting § 4.3 : the source layer count sweep, the full sequential-removal table, and calibration sensitivity to ridge λ \lambda , sample count N N , and domain.

#### Source layer count.

The fit R 2 R^{2} increases with k k but with diminishing returns:

Going from k = 1 k{=}1 to k = 8 k{=}8 provides the largest K R 2 R^{2} gain. k = 8 k{=}8 to k = all k{=}\text{all} yields diminishing returns.

Downstream, the same saturation pattern holds across pairs and benchmarks (Figure 6 ). k = 1 k{=}1 is uniformly insufficient. Every pair drops sharply on at least one benchmark. Closer pairs saturate earlier. Qwen3 14B → \to 32B reaches within 0.3 0.3 pp of peak HellaSwag by k = 8 k{=}8 , while the more distant Llama 3.1 8B → \to 70B keeps improving until k = 24 k{=}24 .

#### Sequential component removal.

Removing each mapper component in turn isolates its contribution (Figure 7 and Table 2 ). § 4.3 already highlights cross-layer source selection ( k = 8 → k = 1 k{=}8\to k{=}1 ) as the largest contributor. Fitting and inferring on RoPE-coupled keys (the “ − - all RoPE” row) lands within noise of the full decoupled pipeline on every benchmark at the 1,024-token fit context. The decoupled formulation is preferred because it generalizes across RoPE configurations and to longer contexts by construction (§ 3.3 ), not because the coupled variant fails on the calibration distribution.

The numerical sequential-removal table is in the body (Table 2 , § 4.3 ).

#### Calibration protocol sensitivity.

Both ridge λ \lambda (four orders of magnitude around the production 0.01 0.01 ) and sample count N N (50–1000 sequences) have wide flat regions around the production value, because the per-head system is over-determined. Collapse appears only at extremes. λ = 1 \lambda{=}1 ( − 15.79 -15.79 pp on HellaSwag) drives the ridge penalty past the least-squares objective. N N flattens after 200 sequences, with N = 50 N{=}50 still within ∼ \sim 1.6 pp of production. Domain is the one axis with a real cost (Table 8 ).

#### Calibration domain across benchmarks.

We repeat the domain sweep across seven log-likelihood benchmarks, evaluating each of the three domain-calibrated mappers on all of them (Table 9 ). Scoring every cell by log-likelihood separates the calibration-domain effect from the additional variance of generation decoding.

Retention stays above 90 % 90\% in every cell. The two out-of-domain corpora differ in how their cost is spread. Wikipedia holds 99.4 % 99.4\% on average and varies little from benchmark to benchmark. CodeAlpaca averages 95.9 % 95.9\% but ranges over 11.1 11.1 pp, matching FineWeb-Edu on MMLU and BoolQ while costing the most on coreference and hard science QA.

## Appendix D Experimental setup details

This appendix collects the experimental-setup details referenced from § 4.1 and § 3 : the architectural axes of the transfer pairs we study (Table 10 ), the benchmarks evaluated (Table 11 ), benchmark coverage caveats, the perplexity protocol used in our family tables, and per-pair mapper sizes (Table 12 ).

#### Benchmarks.

We evaluate transfer quality on five accuracy benchmarks plus WikiText-2 perplexity, with CoQA for multi-turn handoff. Log-likelihood scoring follows the lm-evaluation-harness defaults. MMLU uses 5-shot prompts and GSM8K uses 8-shot chain-of-thought prompts [ Wei et al., 2022 ] . The rest are zero-shot.

#### Coverage.

All five accuracy benchmarks are evaluated on all six pairs at each pair’s selected k k . Transfer perplexity is reported for the Qwen3 pairs and Llama 3.1. Ministral 3 is reasoning-tuned, and its standalone WikiText-2 perplexity is orders of magnitude above the other two families’, so prefix-KV perplexity is not a meaningful comparison for it and is not reported. Missing entries appear as “—” in the per-family tables.

#### Perplexity protocol.

Standard sliding-window perplexity does not isolate KV-cache quality from the target model’s own forward pass. We split WikiText-2 into non-overlapping 2,048-token chunks and score each chunk’s second 1,024 tokens conditioned on a 1,024-token prefix KV cache, taken from either the target’s own forward pass (standalone) or from the source via the mapper (transfer). Both modes score identical continuation tokens, isolating prefix-KV quality.

#### Mapper configuration.

ARC-Challenge, HellaSwag and MMLU are evaluated at every k k . WinoGrande, the generation benchmarks and PPL are evaluated only at the selected k k and at k = all k{=}\text{all} , to bound compute cost. For Ministral 3B → \to 8B, the criterion-optimal k = 20 k{=}20 and k = all k{=}\text{all} differ by < 0.6 <0.6 pp on log-likelihood benchmarks. We use k = all k{=}\text{all} to provide a single configuration across all benchmarks.

#### Serving cost.

Mapper size is 2 ⋅ L t ⋅ n kv t ⋅ ( k ⋅ n kv s ⋅ d h s ) ⋅ d h t 2\cdot L_{t}\cdot n_{\text{kv}}^{t}\cdot(k\cdot n_{\text{kv}}^{s}\cdot d_{h}^{s})\cdot d_{h}^{t} for K and V together. It is set by target depth and head count and by k k , and does not grow with sequence length or cache size.

Mappers need not be GPU-resident: inference is one batched matmul per target layer, so a serving stack can hold them on CPU memory or disk and page in the active pair. At an assumed 25–50 GB/s host-to-device link (PCIe Gen4/Gen5), that is ∼ \sim 80–480 ms across the 4–12 GB range, paid once when a pair becomes active and amortized over its requests. These figures are computed from size and bandwidth, not measured.

The ridge fit is directional, so each direction needs its own mapper and a router over P P models covers up to P ⁡ ( P − 1 ) P(P{-}1) ordered pairs. At the average size above ( ∼ \sim 6.5 GB), 3-, 4- and 5-model fleets come to roughly 39, 79 and 131 GB. The growth is quadratic in P P , but the budget is disk or host memory, not VRAM. The six mappers in the table span 3 × 3\times around that average.

## Appendix E Run information

This appendix records the calibration data, precision regime, MLP optimization settings, and compute used. All experiments use a single 8 × 8\times H100 node.

## Appendix F Extended main results

This appendix collects the per-family standalone vs. transfer accuracies that back the headline numbers in § 4.2 (Table 13 ), the per-benchmark floor-normalized retention (Table 15 ), and a per-pair retention visualization on ARC-C, HellaSwag and MMLU (Figure 8 ).

#### Floor-normalized retention.

Table 14 reads the metric of § 4.1 at two anchors on the Qwen3 32B target. The target’s own ground-truth cache should score 100%. The 8B → \to 32B mapper stripped of RoPE separation and cross-layer selection ( k = 1 k{=}1 ), the counterpart of the fourth row of Table 2 , scores at or below chance on ARC-C, WinoGrande and MMLU, so a retention-like metric should read ≈ \approx 0% there.

Normalization changes the per-benchmark ordering. WinoGrande has the highest floor and moves the most, falling from 87.1% to 58.5% on Llama 3.1 8B → \to 70B. GSM8K is unchanged, its floor already being ≈ \approx 0, and on the strongest pair it now outranks WinoGrande.

## Appendix G Prefill latency details

This appendix extends the single-pair measurement of § 4.7 to seven pairs across the three families in both transfer directions.

#### Setup.

Measured on a single 8 × 8\times H100 node with NVLink, bf16, 50 warmup and 30 timed trials per cell. KV cache transfer latency includes the cross-GPU transfers needed to move the source cache to the target. Re-prefill runs the target’s transformer body with flash_attention_2 , excluding the LM head. The mapper runs in eager mode, with no torch.compile or CUDA graphs. At short sequences a fixed floor from Python dispatch and cross-GPU transfers dominates the mapper’s wall time (14.0 ms for the Qwen3 14B → \to 32B mapper).

#### Caveats.

Both conditions operate on synthetic inputs, which isolates compute cost. End-to-end transfer would also include shipping the mapped cache to the target process, which we do not measure. Ministral 3 re-prefill is timed on the language-model decoder body, excluding the vision tower, which is the correct comparison for text cache transfer but not a full-model forward.

## Appendix H Source-layer count selection

The source-layer count k k is chosen per pair on benchmarks that also appear in the results. This appendix gives the selection protocol and bounds how much a benchmark’s own inclusion raises its reported accuracy.

#### Protocol.

For each pair we sweep k ∈ { 1 , 2 , 4 , 6 , 8 , 10 , 12 , 16 , 20 , 24 , all } k\in\{1,2,4,6,8,10,12,16,20,24,\text{all}\} and take the k k maximizing the arithmetic mean of the log-likelihood benchmark accuracies. The criterion nominally covers ARC-Challenge, HellaSwag, WinoGrande and MMLU, but WinoGrande is absent at most k k for these six pairs, so in practice the argmax is over ARC-Challenge, HellaSwag and MMLU. Near-ties break toward larger k k for evaluation coverage: five pairs take the argmax outright, and Ministral 3B → \to 8B takes k = all k{=}\text{all} over the argmax at k = 20 k{=}20 , which it trails by 0.38 0.38 pp (Appendix D ). GSM8K, CoQA and prefill latency never enter selection: the argmax is computed over the three benchmarks above, so they are holdouts by construction.

#### Leave-one-benchmark-out re-selection.

We drop one selection benchmark, re-select k k by argmax on the remaining two, and read the dropped benchmark at both the full-selection k k and the leave-one-out k k . This isolates how much a benchmark’s own inclusion raises its reported accuracy. The Ministral 3B → \to 8B rows use the data-driven argmax ( k = 20 k{=}20 ), not its manual override to k = all k{=}\text{all} .

The largest shift, 2.49 2.49 pp, occurs on Ministral 8B → \to 14B, a Tier 2 pair. Across the four Tier 1 pairs it is at most 1.45 1.45 pp.

#### Held-out benchmarks.

We evaluate each pair’s selected mapper on three benchmarks that played no part in selection (Table 18 ). Neither the fit nor k k is changed, so this measures the reported configuration out of sample.

Retention is at or above in-sample retention for every pair, and the tier structure of § 4.2 reappears: the four Tier 1 pairs stay above 96% and the two Tier 2 pairs below 64%. PIQA and ARC-Easy are easier than the selection benchmarks, so absolute levels are not comparable across the two sets.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
