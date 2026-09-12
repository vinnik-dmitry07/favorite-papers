##### Report GitHub Issue

Content selection saved. Describe the issue below:

# A Hippocampus for Linear Attention An Exact Memory for What the Recurrent State Forgets

###### Abstract

Linear-attention and state-space language models compress the prefix into a fixed-size recurrent state, yielding O ⁡ ( 1 ) O(1) memory at the cost of a lossy exact memory: when many key–value associations compete, earlier facts are overwritten and needle recall degrades. Inspired by Complementary Learning Systems, we give linear attention a hippocampal complement. HOLA (Hippocampal Linear Attention) keeps the usual delta-rule state as a compressive memory and adds a bounded exact KV cache, forming a semiparametric test-time memory: the state models linearly compressible structure, while the cache stores associations that should not be forced through that state. The cache writes without a learned eviction module, keeping tokens with large β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert , the prediction residual actually committed to the state; a decoupled RMSNorm- γ \gamma cache read then turns these exact KV pairs into sharp retrieval rather than soft averaging. At 340M parameters trained on 15B SlimPajama tokens, HOLA lowers Wikitext perplexity from 27.32 27.32 to 22.92 22.92 ( − 16.1 % -16.1\% ), below a full-attention Transformer++ ( 26.88 26.88 ), and improves LAMBADA perplexity from 30.95 30.95 to 30.26 30.26 . It also achieves the best linear in-context retrieval and remains much more robust than GDN or a matched HOLA+recency cache on RULER needle-in-a-haystack recall out to 32k tokens ( 16 × 16\times its training length).

## 1 Introduction

The human brain does not rely on a single memory. A hippocampus-centered system can record a specific, novel event in one shot and later recall it precisely ( Tse et al., 2007 ) , while a neocortex-centered system slowly distills generalizable structure across many experiences ( Frankland & Bontempi, 2005 ) ; Complementary Learning Systems (CLS) theory ( McClelland et al., 1995 ; Kumaran et al., 2016 ) argues that the two must be separate — a system built for slow, compressive generalization would suffer catastrophic interference if forced to write single facts quickly, and so cannot also serve fast, exact, one-shot memory. Efficient language models are missing exactly this complementarity.

Linear attention is precisely such a “neocortex”: a superb compressor, but a leaky exact memory. DeltaNet, Gated DeltaNet (GDN), and related linear-attention / state-space models ( Katharopoulos et al., 2020 ; Gu & Dao, 2023 ; Yang et al., 2024a ; Yang et al., 2024c ) replace softmax attention’s growing key–value cache with a fixed-size recurrent state S S , summarizing all history in O ⁡ ( 1 ) O(1) memory and processing a sequence in sub-quadratic time. The state is updated online — the delta rule writes the residual between each new value and the state’s current prediction — making it an efficient running summary. But a fixed-size state is a lossy memory: it holds only a bounded number of distinct key → \to value associations before new writes overwrite old ones along shared key directions. This shows up exactly where it hurts: multi-item associative recall ( Arora et al., 2023 ) , passkey / needle-in-a-haystack retrieval ( Mohtashami & Jaggi, 2023 ) , and copying a specific distant token verbatim ( Jelassi et al., 2024 ) . There, full softmax attention — which keeps every token exactly, at O ⁡ ( T ) O(T) memory and O ⁡ ( T 2 ) O(T^{2}) compute — remains the gold standard. The question becomes: can we keep linear attention’s cost while recovering its lost exact recall? CLS points to the answer — give this neocortex a hippocampus: a separate, exact, budget-limited episodic memory that preferentially stores surprise . We formalize this complement as semiparametric test-time memory regression : the recurrent state is the parametric estimator for linearly compressible structure, and a bounded exact cache is the non-parametric correction over KV pairs the state should not be forced to absorb. This framework dictates two design choices: what to store (the surprising items) and how to read it (exact retrieval, not soft averaging).

What to store: a surprise signal the model already computes. A budget-limited episodic memory is only useful if it keeps the right tokens — the surprising ones, which the compressed state could not absorb. The obvious choice is instead to keep the most recent tokens, a sliding window, as most linear-attention hybrids do ( Xiao et al., 2024 ; Zhang et al., 2023 ; Du et al., 2025 ; Wang et al., 2025 ; Fang et al., 2025 ) ; but recency cannot represent information that is far away yet still must be recalled exactly — once it slides out of the window it is as lost as if the state had overwritten it. Our key observation is that a delta-rule model already measures how surprising each token is to its state: if the state predicts the token’s value poorly and the model strongly commits the correction, that token is exactly the kind of support point the non-parametric cache should keep. We use this intrinsic write magnitude as the cache’s eviction score, retaining tokens that changed the state most rather than tokens that are merely recent. A matched control confirms the intended separation: at 340M, importance eviction beats a recency cache on perplexity and long-context retrieval, while commonsense remains within single-seed noise (Sec. 4 ).

How to read: retrieval, not averaging. An exact copy buys nothing if it is read like another linear summary. Directly reusing the L2-normalized queries and keys used by DeltaNet/GDN makes cache logits too small, so the cache softmax is nearly uniform and the exact memory degenerates into a lossy average. A simple fix is to use Qwen3-style RMSNorm- γ \gamma ( Qwen Team, 2025 ) on the cache path only, decoupled from the state update. This restores sharp, near-argmax retrieval while preserving the unit-norm keys required for the delta rule’s stable state update.

Together, these ideas give Hippocampal Linear Attention (HOLA) , which recovers the exact recall the state loses (Fig. 1 ). At 340M parameters trained on 15B SlimPajama tokens, the model reaches the lowest perplexity of every model we compare — below a full-attention Transformer++ (Wikitext 22.9 22.9 vs. 26.9 26.9 ) — and, unlike GDN, stays length-robust on hard RULER recall out to 32k tokens ( 16 × 16\times its 2k training length), where the recurrent state saturates and GDN decays.

#### Contributions.

1. A hippocampal exact memory for linear attention, motivated by CLS. We argue that a fixed recurrent state is a neocortex-like compressor but a leaky exact memory, and add a bounded, hippocampus-like KV store for precise one-shot associations.

2. A semiparametric test-time memory framework. We formalize memory readout as test-time regression over prefix key–value observations: pure GDN is the parametric estimator q ⊤ ​ S t q^{\!\top}S_{t} , full attention is an unbounded non-parametric kernel estimator, and HOLA is the bounded semiparametric case.

3. A concrete write/read algorithm. The cache writes by an intrinsic surprise signal already computed by the delta rule — the committed residual update to the state — and reads by a decoupled RMSNorm- γ \gamma cache path that makes exact KV pairs retrievable rather than softly averaged.

4. Large empirical gains in perplexity and retrieval. At 340M, HOLA sharply lowers Wikitext perplexity relative to the same-backbone GDN anchor ( → 22.92 27.32\!\to\!22.92 ), falls below a full-attention Transformer++ ( 26.88 26.88 ), achieves the best linear in-context retrieval, and remains much more robust than GDN or a recency cache on long-context needle recall.

## 2 Related Work

Our work connects three threads: linear-time recurrent attention, hybrid exact-memory mechanisms for efficient language models, and semiparametric memory.

#### Linear-time recurrent attention.

Linear attention ( Katharopoulos et al., 2020 ) , state-space models ( Gu & Dao, 2023 ; Dao & Gu, 2024 ) , and the DeltaNet family ( Schlag et al., 2021 ; Yang et al., 2024c ) replace softmax attention’s growing KV cache with a fixed-size recurrent state. Gated DeltaNet (GDN) ( Yang et al., 2024a ) strengthens DeltaNet with data-dependent decay, and GLA ( Yang et al., 2024b ) , GSA ( Zhang et al., 2024 ) , and Kimi Delta Attention (KDA) ( Kimi Team et al., 2025 ) are representative modern linear-attention baselines. This fixed state is efficient but lossy: as an associative memory, it has bounded capacity before new writes interfere with old ones ( Hopfield, 1982 ; Ramsauer et al., 2021 ) . Based and Zoology ( Arora et al., 2024 ; Arora et al., 2023 ) make this recall–throughput trade-off explicit, showing that efficient recurrent models lag softmax attention on multi-item associative recall. HOLA keeps the recurrent backbone, but adds a bounded exact memory for the KV pairs the state should not be forced to compress.

#### Hybrid exact memory for efficient LMs.

Many efficient LMs recover some exact recall by pairing a recurrent/SSM backbone with softmax attention. Inter-layer hybrids such as Jamba ( Lieber et al., 2024 ) , Samba ( Ren et al., 2024 ) , and Griffin ( De et al., 2024 ) mix recurrent layers with local attention layers; layer-internal hybrids such as NHA ( Du et al., 2025 ) , RAttention ( Wang et al., 2025 ) , and AHN ( Fang et al., 2025 ) combine recurrent memory with a recent-token window or learned compressed store. These designs differ architecturally, but their lossless component is primarily recency-based: once an old token leaves the window, it must be represented by the compressed state. HOLA instead makes the exact memory selective over the prefix, retaining surprising KV pairs even when they are far from the current query.

The closest work is LTE ( He & Garner, 2025 ) , which also augments GDN with a bounded evictable KV cache. The main difference is how the cache is selected and integrated: LTE learns eviction scores with an additional CNN module and alternates GDN with sparse-attention layers, whereas HOLA uses the delta rule’s own write magnitude as a parameter-free surprise score and attaches the cache inside every recurrent layer. Thus LTE shows that evictable caches can help delta-rule models, while HOLA argues that the recurrent update itself already exposes the right signal for what an exact memory should keep.

#### Semiparametric and retrieval-augmented memory.

Semiparametric language models pair parametric sequence modeling with explicit non-parametric memory, as in kNN-LM ( Khandelwal et al., 2020 ) , RETRO ( Borgeaud et al., 2022 ) , Memorizing Transformers ( Wu et al., 2022 ) , and SPALM ( Yogatama et al., 2021 ) . Those systems retrieve from an external or long-lived datastore. Our setting is in-sequence and test-time: the parametric part is the recurrent state S t S_{t} , the non-parametric part is a bounded set of exact in-context KV pairs, and the readout interpolates between the two. This semiparametric view also places softmax attention and GDN on the same spectrum: full attention is an unbounded non-parametric estimator over all prefix tokens, while GDN is the purely parametric state estimator.

## 3 Method

We derive HOLA from the delta-rule update equation: a single equation tells us both why a cache is necessary (Sec. 3.2 ) and what to store in it (Sec. 3.3 ); we then address how to read it (Sec. 3.4 ) and the full layer (Sec. 3.5 ). Figure 2 gives an overview.

### 3.1 Background: the delta rule and its lossiness

DeltaNet compresses history into a ( d k , d v ) (d_{k},d_{v}) matrix S S , an online associative memory : the read-out for key k k , k ⊤ ​ S k^{\!\top}S , gives its currently associated value. Let token t t have query/key/value q t , k t , v t q_{t},k_{t},v_{t} (with q t , k t q_{t},k_{t} L2-normalized to unit norm) and write strength β t ∈ [ 0 , 1 ] \beta_{t}\in[0,1] . The delta rule updates by “predict, then write the residual”: S t = S t − 1 + β t ​ k t ​ e t ⊤ , e t = v t − k t ⊤ ​ S t − 1 , o t state = q t ⊤ ​ S t . S_{t}\;=\;S_{t-1}+\beta_{t}\,k_{t}\,e_{t}^{\!\top},\qquad e_{t}\;=\;v_{t}-k_{t}^{\!\top}S_{t-1},\qquad o^{\mathrm{state}}_{t}\;=\;q_{t}^{\!\top}S_{t}. (1) Here e t e_{t} is the residual (innovation): the part of v t v_{t} that S S cannot already predict along k t k_{t} . Writing the residual (rather than v t v_{t} ) suppresses repeated same-key interference.

It is lossy. S S is fixed-size, of rank at most d k d_{k} : once the number of distinct associations exceeds capacity, new writes overwrite old ones along shared key directions, and a distant ( k , v ) (k,v) can no longer be recovered exactly from S S . This is the “neocortex-like” deficiency of Sec. 1 — good at generalizing, unable to keep distant exact detail. The next three subsections build HOLA on top; the specific backbone we use (GDN) is deferred to Sec. 3.5 .

### 3.2 Semiparametric memory as test-time regression

The previous subsection shows why a fixed recurrent state is lossy. We now give the framework that turns this observation into a design principle: memory readout is a test-time regression problem, and HOLA is a bounded semiparametric estimator for it.

Definition 1 (test-time memory regression). For a layer at position t t , let the causally available key–value observations be 𝒟 t = { ( k i , v i ) } i ≤ t \mathcal{D}_{t}=\{(k_{i},v_{i})\}_{i\leq t} . A test-time memory regression (TMR) mechanism is a memory state ℳ t \mathcal{M}_{t} together with two operations ℳ t = Write ⁡ ( ℳ t − 1 , k t , v t ) , o t = Read ⁡ ( q t , ℳ t ) = f ^ t ​ ( q t ) , \mathcal{M}_{t}=\mathrm{Write}(\mathcal{M}_{t-1},k_{t},v_{t}),\qquad o_{t}=\mathrm{Read}(q_{t},\mathcal{M}_{t})=\hat{f}_{t}(q_{t}), where f ^ t \hat{f}_{t} is an estimator, built from 𝒟 t \mathcal{D}_{t} , of the context-specific map f t : q ↦ v f_{t}:q\mapsto v . The choice of memory state ℳ t \mathcal{M}_{t} and estimator class f ^ t \hat{f}_{t} specifies the memory mechanism.

Definition 1 makes the comparison clean. GDN is a TMR mechanism whose memory state is only a fixed-size matrix ℳ t = S t \mathcal{M}_{t}=S_{t} and whose read operation is linear, o t = Read ⁡ ( q t , S t ) = f ^ state , t ​ ( q t ) = q t ⊤ ​ S t . o_{t}=\mathrm{Read}(q_{t},S_{t})=\hat{f}_{\mathrm{state},t}(q_{t})=q_{t}^{\!\top}S_{t}. (2) Here S t S_{t} is a test-time parameter: it is updated online from the context by the delta rule, not learned as an additional model weight. It is cheap and captures the linearly compressible part of the key–value map, but it cannot interpolate all observations in 𝒟 t \mathcal{D}_{t} once the context exceeds its capacity.

Definition 2 (semiparametric TMR). A TMR mechanism from Definition 1 is semiparametric if its memory decomposes as ℳ t = ( S t , 𝒜 t ) \mathcal{M}_{t}=(S_{t},\mathcal{A}_{t}) , where S t S_{t} is a fixed-size parametric state and 𝒜 t ⊆ 𝒟 t \mathcal{A}_{t}\subseteq\mathcal{D}_{t} is a set of exact KV pairs kept non-parametrically. Its Write operation updates both components, ( S t , 𝒜 t ) = Write ⁡ ( ( S t − 1 , 𝒜 t − 1 ) , k t , v t ) , (S_{t},\mathcal{A}_{t})=\mathrm{Write}((S_{t-1},\mathcal{A}_{t-1}),k_{t},v_{t}), where the state update changes the parametric estimator and the KV-set update may admit or evict exact KV pairs. Its Read operation returns o t = Read ⁡ ( q t , ℳ t ) = f ^ t ​ ( q t ) = q t ⊤ ​ S t + λ t ​ g t ​ ( q t ) . o_{t}=\mathrm{Read}(q_{t},\mathcal{M}_{t})=\hat{f}_{t}(q_{t})=q_{t}^{\!\top}S_{t}+\lambda_{t}\,g_{t}(q_{t}). (3) Here λ t \lambda_{t} is a read-side mixing coefficient, and g t g_{t} is a non-parametric model over the exact KV pairs in 𝒜 t \mathcal{A}_{t} .

This form also locates full softmax attention. It is the non-parametric TMR instance obtained by disabling the state term and using all causally available observations as exact KV pairs, i.e., set 𝒜 t = 𝒟 t \mathcal{A}_{t}=\mathcal{D}_{t} . In that case the non-parametric model g t g_{t} is exactly the softmax kernel estimator, g attn , t ​ ( q ) = ∑ ( k i , v i ) ∈ 𝒟 t exp ⁡ ( q ⊤ ​ k i / d ) ∑ ( k j , v j ) ∈ 𝒟 t exp ⁡ ( q ⊤ ​ k j / d ) ​ v i , g_{\mathrm{attn},t}(q)=\sum_{(k_{i},v_{i})\in\mathcal{D}_{t}}\frac{\exp(q^{\!\top}k_{i}/\sqrt{d})}{\sum_{(k_{j},v_{j})\in\mathcal{D}_{t}}\exp(q^{\!\top}k_{j}/\sqrt{d})}v_{i}, (4) i.e. a Nadaraya–Watson kernel estimator ( Nadaraya, 1964 ; Watson, 1964 ) . It can recover exact items because every token remains an exact KV pair, but the KV set grows with context length.

HOLA is the bounded semiparametric TMR instance. We take S t S_{t} to be the full GDN recurrent state and keep a bounded set of exact KV pairs selected from 𝒟 t \mathcal{D}_{t} by the score in Sec. 3.3 . Under this framework, HOLA has two design questions: which exact KV pairs to keep (Sec. 3.3 ), and how sharp the kernel read should be (Sec. 3.4 ).

### 3.3 What to store: the write magnitude β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert is “surprise”

We should store the tokens that are least well represented by the state memory. The same update equation already says which . Write the update as S t = S t − 1 + Δ t , Δ t = β t k t e t ⊤ ( rank-1 ) . S_{t}=S_{t-1}+\Delta_{t},\qquad\Delta_{t}=\beta_{t}\,k_{t}e_{t}^{\!\top}\quad(\text{rank-1}). (5) The token’s entire effect on S S is this one rank-1 matrix Δ t \Delta_{t} . How much a token “writes” is naturally the size of Δ t \Delta_{t} ; for a rank-1 matrix the Frobenius norm factorizes, and with ∥ k t ∥ = 1 \lVert k_{t}\rVert=1 collapses to a scalar: m t = ∥ Δ t ∥ F = β t ​ ∥ k t ∥ ​ ∥ e t ∥ = β t ​ ∥ e t ∥ . m_{t}\;=\;\lVert\Delta_{t}\rVert_{F}\;=\;\beta_{t}\,\lVert k_{t}\rVert\,\lVert e_{t}\rVert\;=\;\beta_{t}\,\lVert e_{t}\rVert. (6) We write this as β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert and use it directly as the eviction score. Its meaning is immediate: m t m_{t} is how much the token changed S S . A large change means the token brought information S S could not predict (large residual e t e_{t} , i.e. the innovation in the Kalman ( Kalman, 1960 ) sense; the delta rule is the Widrow–Hoff/LMS rule ( Widrow & Hoff, 1960 ) , where e e is its error term) and that the model actually wrote it in (large β t \beta_{t} ). A token with small residual is already well predicted by the state, so storing a verbatim copy is wasteful; a token with large committed residual is exactly where the compressed state needed the most help. In short, we spend the limited exact memory where the state-memory representation is weakest.

Cache = = the top- w w tokens seen so far by β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert . Each layer keeps a persistent exact cache of capacity w w (default w = 64 w{=}64 ). Its members are the exact ( k , v ) (k,v) copies of the w w highest- m m tokens in the causal history observed so far – keep what wrote most to S S , regardless of distance . Because m t m_{t} is fixed when the token is written, the same top- w w set can be maintained online or selected blockwise without order dependence; training and inference therefore use the same cache semantics.

Versus recency. Sliding-window memories, as used in StreamingLLM ( Xiao et al., 2024 ) , NHA ( Du et al., 2025 ) , and RAttention ( Wang et al., 2025 ) , choose exact KV pairs by position. This is useful for local context, but it cannot keep an old item solely because it remains important. Selection by β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert instead keeps surprising KV pairs across distance, compensating the state-memory failure described in Sec. 3.1 . An ablation (Sec. 4 ) shows why the product matters: the residual alone ( ∥ e ∥ \lVert e\rVert ) or the write strength alone ( β ​ ∥ v ∥ \beta\lVert v\rVert ) each underperform; their product is best.

For the read in Sec. 3.4 , we denote the bounded visible KV set by 𝒱 t \mathcal{V}_{t} . Its main persistent component is the top- w w exact cache above; in implementation we also include the causal tokens in the current processing block and one null sink. These additions are bounded bookkeeping for causal block processing and stability; the persistent exact memory is selected by β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert .

### 3.4 How to read: retrieval, not soft averaging

An exact copy is worthless if read like a linear attention. If the cache reuses the backbone’s unit-L2-normalized q , k q,k ( Yang et al., 2024c ; Yang et al., 2024a ) , the effective logit is τ ⋅ ( 1 / d ) cos ≈ 0.83 cos \tau\cdot(1/\sqrt{d})\cos\approx 0.83\cos (a learned τ ≈ 6.6 \tau\!\approx\!6.6 , head dimension d d ), ranging only over ± 0.83 \pm 0.83 : the softmax is nearly uniform — among w = 64 w{=}64 entries a perfectly matching key receives only ∼ 3.5 % {\sim}3.5\% of the mass. The cache degenerates into yet another soft-averaging lossy summary (explaining why a naive cache barely helps).

Sharpening via a decoupled RMSNorm- γ \gamma . We apply Qwen3-style RMSNorm with a learnable γ \gamma to the cache-path q , k q,k (keeping the norm at d ≈ 11 \sqrt{d}\!\approx\!11 rather than 1 1 ) and fix τ = 1 \tau{=}1 . The cache read is then a sharpened softmax attention over 𝒱 t \mathcal{V}_{t} : o t cache = ∑ j ∈ 𝒱 t softmax j ​ ( q ~ t ⊤ ​ k ~ j / d ) ​ v j , q ~ = RMSNorm γ ​ ( q ) , k ~ = RMSNorm γ ​ ( k ) . o^{\mathrm{cache}}_{t}\;=\;\sum_{j\in\mathcal{V}_{t}}\mathrm{softmax}_{j}\!\Big(\tilde{q}_{t}^{\!\top}\tilde{k}_{j}/\sqrt{d}\Big)\,v_{j},\qquad\tilde{q}=\mathrm{RMSNorm}_{\gamma}(q),\ \ \tilde{k}=\mathrm{RMSNorm}_{\gamma}(k). (7) Since ∥ q ~ ∥ ≈ ∥ k ~ ∥ ≈ d \lVert\tilde{q}\rVert\!\approx\!\lVert\tilde{k}\rVert\!\approx\!\sqrt{d} , the effective logit is ≈ d ​ cos ≈ 11 ​ cos {\approx}\sqrt{d}\cos\approx 11\cos (vs. 0.83 ​ cos 0.83\cos for unit-L2), so the cache finally performs near-argmax retrieval . This change acts only on the cache read and is decoupled from the state-update path — the q , k q,k feeding S S remain unit-L2-normalized. Decoupling is necessary: the delta rule relies on ∥ k ∥ = 1 \lVert k\rVert=1 to keep the update operator I − β ​ k ​ k ⊤ I-\beta\,kk^{\!\top} within [ 0 , 1 ] [0,1] eigenvalues (stable); a d \sqrt{d} norm in the state update would give eigenvalues 1 − β ​ d 1-\beta d and diverge. The learnable γ \gamma self-moderates sharpness: versus a fixed high temperature it reaches lower perplexity while avoiding “the state grows lazy and far recall collapses” (Sec. 4 ). Empirically, sharpening is the single largest lever in the design (perplexity → 60 70\!\to\!60 , ∼ 2 × {\sim}2\times multi-key capacity).

### 3.5 Instantiation

Instantiation (GDN). The derivation used only the delta rule. We instantiate on the strongest linear backbone, Gated DeltaNet, which adds a data-dependent decay gate α t ∈ ( 0 , 1 ] \alpha_{t}\in(0,1] (selective forgetting), making the prediction α t ​ k ⊤ ​ S t − 1 \alpha_{t}k^{\!\top}S_{t-1} and the residual e t = v t − α t ​ k ⊤ ​ S t − 1 e_{t}=v_{t}-\alpha_{t}k^{\!\top}S_{t-1} . The gate is orthogonal to our method and β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert is unchanged; all experiments use GDN.

Overhead over GDN. HOLA is almost iso-parametric with its GDN backbone. At 340M ( L = 24 L{=}24 , H = 4 H{=}4 , d = 256 d{=}256 ), the only learned cache-specific parameters are the cache-path Q/K RMSNorm scales plus a per-head sink and cache gate: L ⁡ ( 2 ​ d + 2 ​ H ) = 24 ​ ( 512 + 8 ) = 12,480 L(2d+2H)=24(512+8)=12{,}480 trainable scalars, less than 0.004 % 0.004\% of the full model (the frozen temperature adds only L ​ H = 96 LH{=}96 stored scalars). The cache itself is inference state rather than model weights: in bf16 decoding it stores at most ( w + C ) (w{+}C) K/V pairs per layer, about 24 ⋅ 320 ⋅ 4 ⋅ 256 ⋅ 2 ⋅ 2 ≈ 31 24\cdot 320\cdot 4\cdot 256\cdot 2\cdot 2\approx 31 MB plus negligible scores. Measured peak GPU allocation (weights included, bs = 1 =1 decode) is therefore close to GDN and flat with context: 0.75 0.75 GB for HOLA versus 0.72 0.72 GB for GDN at both 32k and 128k. Thus the gains do not come from a larger parametric model, and the exact-memory overhead over GDN is small ( ≈ 5 % \approx 5\% peak memory).

## 4 Experiments

### 4.1 Setup

Architecture. We use the GDN architecture at 340M ( Yang et al., 2024a ) : d model = 1024 d_{\mathrm{model}}{=}1024 , 24 layers, 4 4 heads × \times head-dim 256 256 , expand ​ _ ​ v = 1 \mathrm{expand\_v}{=}1 , hidden ​ _ ​ ratio = 4 \mathrm{hidden\_ratio}{=}4 , conv 4, tied embeddings, and vocabulary 32000 32000 . HOLA adds a per-layer cache: window w = 64 w{=}64 , chunk C = 256 C{=}256 , eviction score β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert , cache normalization RMSNorm- γ \gamma , τ = 1 \tau{=}1 frozen, gate init − 4 -4 . The GDN baseline and HOLA share an identical backbone ; the only difference is the cache, so internal comparisons are strictly controlled.

Training recipe. We follow the Preconditioned-DeltaNet 340M recipe ( Tumma et al., 2026 ) : SlimPajama 15.0B tokens ( Soboleva et al., 2023 ) , Mistral tokenizer ( Jiang et al., 2023 ) , context 2048; AdamW ( Loshchilov & Hutter, 2019 ) (peak lr 4 × 10 − 4 4{\times}10^{-4} , wd 0.01 0.01 , cosine, warmup 1000, grad-clip 1.0), batch 0.5M tokens, 1 epoch. This recipe match enables reuse of the published DeltaNet/KDA/GDN baseline rows. Trained on 8 × 8\times A800.

Baselines. We train our own GDN anchor and HOLA for the controlled same-backbone comparison, and borrow recipe-matched architecture rows for Transformer++, GLA, and GSA from Du et al. (2025) , and DeltaNet, KDA, and GDN from Tumma et al. (2026) ; KDA itself is from Kimi Linear ( Kimi Team et al., 2025 ) .

Evaluation. (1) Language modeling: Wikitext-103 perplexity, LAMBADA. (2) Commonsense (zero-shot): ARC-e/c, PIQA, HellaSwag, WinoGrande, BoolQ, SciQ, OpenBookQA, LAMBADA-acc. (3) In-context retrieval: FDA, SWDE, SQuAD. (4) Long context: RULER ( Hsieh et al., 2024 ) (2k → \to 32k; multi-key MK, multi-value MV, multi-query MQ, variable tracking VT) and passkey/needle.

### 4.2 Main results: language modeling, commonsense, retrieval

Table 1 reports the main comparison. The effect is large on the two axes the cache is designed to improve: HOLA sharply lowers perplexity and substantially boosts in-context retrieval . Wikitext perplexity drops from → 22.92 27.32\!\to\!22.92 relative to our same-backbone GDN anchor ( − 16.1 % {-}16.1\% ), and even falls below the full-attention Transformer++ ( 26.88 26.88 ). Retrieval improves just as strongly: FDA rises → 20.1 11.7\!\to\!20.1 ( + 72 % +72\% relative) and SWDE → 35.9 29.0\!\to\!35.9 ( + 24 % +24\% ), the best among linear models, while commonsense remains competitive on the six-task average.

• Perplexity: HOLA’s Wiki 22.92 22.92 is a large drop from the same-backbone GDN anchor ( → 22.92 27.32\!\to\!22.92 , − 16.1 % {-}16.1\% ), below the strongest published sub-quadratic baseline (KDA 26.18 26.18 ), and even below the full-attention Transformer++ ( 26.88 26.88 ); LAMBADA perplexity is also the lowest in the table ( 30.26 30.26 ).

• Commonsense: the six-task average is effectively a tie among the strong models — HOLA 42.85 42.85 , the HOLA+recency control 43.17 43.17 , KDA 42.75 42.75 , and GDN ∼ 42.7 {\sim}42.7 all sit within ∼ 0.6 {\sim}0.6 (above Transformer++ 42.34 42.34 ); commonsense is not where the cache mechanism separates the models (perplexity and retrieval are). Over the 9-task accuracy mean, HOLA 0.446 0.446 vs. GDN 0.440 0.440 (BoolQ → 0.584 0.548\!\to\!0.584 , + 3.5 {+}3.5 pt; WinoGrande, LAMBADA-acc, and HellaSwag also higher).

• Retrieval: on in-context exact extraction HOLA beats all linear baselines by a wide margin — FDA → 20.1 11.7\!\to\!20.1 ( + 72 % +72\% rel.), SWDE → 35.9 29.0\!\to\!35.9 ( + 24 % +24\% ), SQuAD → 33.8 32.5\!\to\!33.8 . This is the cache’s intended regime: preserving exact tokens that the recurrent state would otherwise compress away. Only the full-attention Transformer++ (FDA 46.1 46.1 ) still leads pure extraction.

### 4.3 Consistency across scale

Table 2 asks whether the perplexity gain is confined to a single model size. Across 46M, 170M, and 340M, each comparison uses a matched GDN-vs-HOLA backbone within the same scale; App. A lists the architecture, corpus, and context length for each run. The gain is consistent: HOLA lowers Wikitext perplexity by 15 15 – 16 % 16\% relative to the same-backbone GDN anchor at every scale.

### 4.4 Long-Context Retrieval

We evaluate on the official RULER benchmark ( Hsieh et al., 2024 ) (synthetic tasks, our Mistral tokenizer, limit 100) at 2k/4k/8k/16k/32k — up to 16 × 16\times the 2k training length. On the headline single needle-in-a-haystack task, S-NIAH-1, the recurrent state (GDN) collapses with length while HOLA stays robust , with a matched HOLA+recency cache in between (Figure 1 b): at 32k, HOLA reaches 0.58 0.58 vs. HOLA+recency 0.24 0.24 vs. GDN 0.14 0.14 — a + 0.44 +0.44 margin over the state, and + 0.64 +0.64 at 16k.

The advantage extends to most above-floor RULER cells (Table 3 ), grouped into single-needle (S-NIAH-1/2/3) and multi-needle (multi-key/-value/-query): HOLA wins the harder single-needle variants by wide margins where they are not floored (S-NIAH-2 at 8k, 0.35 0.35 vs. 0.09 0.09 ) and most multi-needle cells (multi-value 0.28 0.28 vs. 0.17 0.17 at 2k), with a few near-tie exceptions. We also include a full-attention Transformer++ as a 2k full-attention ceiling: within its training length it is the strongest model (exact softmax retrieval), but this RoPE checkpoint is not a length-extrapolating baseline and every shown task drops to 0 0 at 4k and beyond — exactly the regime where HOLA remains useful.

### 4.5 Ablations

HOLA+recency vs. importance eviction (340M, matched memory). The sharpest test of contribution 1 is a matched control — the identical architecture ( w = 64 w{=}64 , same chunk, sharpened read, gate, and kernel), changing only the eviction signal: position (keep the most recent w w ) vs. surprise (keep top- w w by β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert ). We report the HOLA+recency control as a first-class row throughout, and importance wins on the axes the cache is designed to affect: lower perplexity (Wiki → 22.92 25.04\!\to\!22.92 ; Table 1 ) and far stronger long-context retrieval (Figure 1 b, Table 3 ; S-NIAH-1 at 32k, HOLA+recency 0.24 0.24 vs. HOLA 0.58 0.58 ). Most tellingly, the recency cache barely improves on no cache at all on the far needle : at 32k it recalls only 0.24 0.24 , marginally above the no-cache state (GDN 0.14 0.14 ) and far below importance eviction (HOLA 0.58 0.58 ) — a recency window gives little far-needle benefit, because the needle slides out of it, whereas surprise-based eviction keeps it. For a bounded exact memory, what to cache matters more than how recent . 1 1 1 For the recency control, we use full recomputation to avoid implementation-path confounds; this is the path used for the PPL, commonsense, retrieval, and RULER numbers we report.

Eviction signal (Table 4 ). We isolate the eviction rule with the same 46M backbone, cache size, and flat cache read, and evaluate the two axes a bounded cache is meant to balance: whether the state still carries a far needle after the cache window has moved on, and how many exact key–value facts the cache can retain within its span. The far-needle column uses a lightweight passkey-style probe inspired by Mohtashami & Jaggi (2023) : we place a numeric key at a controlled depth in a 4k context, teacher-force the answer tokens after the query, and report next-token accuracy. Pure residual surprise, ∥ e ∥ \lVert e\rVert , is not enough; it lacks the write-strength utility signal and performs poorly on the far needle. Multiplying by the GDN write gate gives β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert , the actual delta-rule update magnitude, which is best or tied-best on every diagnostic column while also giving the lowest WikiText perplexity.

Sharpened read (Table 5 ). With the eviction rule fixed to β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert , the decisive read-side change is not a larger fixed temperature but the normalization used to form cache logits. Unit-L2 queries and keys make the cache read too flat, so the cache behaves like a soft average. RMSNorm- γ \gamma keeps the natural d \sqrt{d} logit scale while letting the model tune it, turning the same bounded cache into an exact local memory: it lowers WikiText perplexity by more than ten points and sharply improves multi-key capacity, without losing the far-needle behavior of the recurrent state.

## 5 Conclusion and Limitations

#### Conclusion.

Starting from a semiparametric test-time regression view — a linear-attention recurrent state is the parametric estimator for compressible key–value structure, but needs a bounded set of exact KV pairs for exact associations — we attached a hippocampus-like KV cache to every layer of Gated DeltaNet. The cache is guided by two design choices: (i) eviction driven by a parameter-free, intrinsic surprise signal β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert (the delta-rule write magnitude) — keep what wrote most to the state, not what is most recent; and (ii) a read sharpened by a decoupled RMSNorm- γ \gamma , so the cache performs exact retrieval rather than soft averaging. At 340M parameters trained on 15B SlimPajama tokens, HOLA improves language modeling and recall together: lowest perplexity of all compared models (Wikitext 22.92, below a full-attention Transformer++), best linear in-context retrieval, and competitive commonsense (six-task average); it is length-robust on RULER needle-in-a-haystack recall out to 32k ( 16 × 16\times the training length), holding 0.58 0.58 where the recurrent baseline collapses to 0.14 0.14 and the 2k-trained full-attention checkpoint reaches 0 0 . The perplexity advantage holds from 46M to 340M. The take-away: a linear-attention model’s own update rule already diagnoses what it fails to remember; spending a small exact memory on exactly those “surprising” tokens recovers the long-range exact recall it loses.

#### Limitations.

The cache is deliberately bounded: it spans only w + C + 1 ≈ 321 w{+}C{+}1{\approx}321 tokens, so in very long or needle-dense contexts it cannot retain every relevant item, and single-needle recall is 0.58 0.58 rather than perfect at 32k. HOLA also narrows, but does not close, the gap to full attention on pure token-exact extraction such as FDA, where every token can matter. Finally, the main-scale results are single-seed up to 340M; while the matched recency comparison and 46M diagnostics support the β ⋅ ∥ e ∥ \beta\!\cdot\!\lVert e\rVert eviction rule, we have not run a matched-memory comparison against learned eviction modules such as LTE’s CNN.

## References

Arora et al. (2023) Simran Arora, Sabri Eyuboglu, et al. Zoology: Measuring and improving recall in efficient language models. arXiv:2312.04927 , 2023.

Arora et al. (2024) Simran Arora, Sabri Eyuboglu, et al. Simple linear attention language models balance the recall-throughput tradeoff. In ICML , 2024. arXiv:2402.18668.

Borgeaud et al. (2022) Sebastian Borgeaud et al. Improving language models by retrieving from trillions of tokens. In ICML , 2022. arXiv:2112.04426.

Dao & Gu (2024) Tri Dao and Albert Gu. Transformers are SSMs: Generalized models and efficient algorithms through structured state space duality. In ICML , 2024. arXiv:2405.21060.

De et al. (2024) Soham De et al. Griffin: Mixing gated linear recurrences with local attention for efficient language models. arXiv:2402.19427 , 2024.

Du et al. (2025) Jusen Du, Jiaxi Hu, Tao Zhang, Weigao Sun, and Yu Cheng. Native hybrid attention for efficient sequence modeling. arXiv:2510.07019 , 2025.

Fang et al. (2025) Yunhao Fang, Weihao Yu, Shu Zhong, Qinghao Ye, Xuehan Xiong, and Lai Wei. Artificial hippocampus networks for efficient long-context modeling. arXiv:2510.07318 , 2025.

Frankland & Bontempi (2005) Paul W. Frankland and Bruno Bontempi. The organization of recent and remote memories. Nature Reviews Neuroscience , 6(2):119–130, 2005.

Gu & Dao (2023) Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces. arXiv:2312.00752 , 2023.

He & Garner (2025) Mutian He and Philip N. Garner. Alleviating forgetfulness of linear attention by hybrid sparse attention and contextualized learnable token eviction. arXiv:2510.20787 , 2025.

Hopfield (1982) John J. Hopfield. Neural networks and physical systems with emergent collective computational abilities. PNAS , 79(8):2554–2558, 1982.

Hsieh et al. (2024) Cheng-Ping Hsieh et al. RULER: What’s the real context size of your long-context language models? arXiv:2404.06654 , 2024.

Jelassi et al. (2024) Samy Jelassi, David Brandfonbrener, Sham M. Kakade, and Eran Malach. Repeat after me: Transformers are better than state space models at copying. In ICML , 2024. arXiv:2402.01032.

Jiang et al. (2023) Albert Q. Jiang et al. Mistral 7b. arXiv:2310.06825 , 2023.

Kalman (1960) Rudolph E. Kalman. A new approach to linear filtering and prediction problems. Journal of Basic Engineering , 82(1):35–45, 1960.

Katharopoulos et al. (2020) Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and François Fleuret. Transformers are RNNs: Fast autoregressive transformers with linear attention. In ICML , 2020. arXiv:2006.16236.

Khandelwal et al. (2020) Urvashi Khandelwal, Omer Levy, Dan Jurafsky, Luke Zettlemoyer, and Mike Lewis. Generalization through memorization: Nearest neighbor language models. In ICLR , 2020. arXiv:1911.00172.

Kimi Team et al. (2025) Kimi Team, Yu Zhang, Zongyu Lin, Xingcheng Yao, et al. Kimi Linear: An expressive, efficient attention architecture. arXiv:2510.26692 , 2025.

Kumaran et al. (2016) Dharshan Kumaran, Demis Hassabis, and James L. McClelland. What learning systems do intelligent agents need? complementary learning systems theory updated. Trends in Cognitive Sciences , 20(7):512–534, 2016.

Lieber et al. (2024) Opher Lieber et al. Jamba: A hybrid transformer-mamba language model. arXiv:2403.19887 , 2024.

Loshchilov & Hutter (2019) Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In ICLR , 2019. arXiv:1711.05101.

McClelland et al. (1995) James L. McClelland, Bruce L. McNaughton, and Randall C. O’Reilly. Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. Psychological Review , 102(3):419–457, 1995.

Mohtashami & Jaggi (2023) Amirkeivan Mohtashami and Martin Jaggi. Landmark attention: Random-access infinite context length for transformers. arXiv:2305.16300 , 2023.

Nadaraya (1964) Elizbar A. Nadaraya. On estimating regression. Theory of Probability and Its Applications , 9(1):141–142, 1964.

Qwen Team (2025) Qwen Team. Qwen3 technical report. arXiv:2505.09388 , 2025.

Ramsauer et al. (2021) Hubert Ramsauer et al. Hopfield networks is all you need. In ICLR , 2021. arXiv:2008.02217.

Ren et al. (2024) Liliang Ren et al. Samba: Simple hybrid state space models for efficient unlimited context language modeling. arXiv:2406.07522 , 2024.

Schlag et al. (2021) Imanol Schlag, Kazuki Irie, and Jürgen Schmidhuber. Linear transformers are secretly fast weight programmers. In ICML , 2021. arXiv:2102.11174.

Soboleva et al. (2023) Daria Soboleva et al. SlimPajama: A 627b token cleaned and deduplicated version of RedPajama. https://www.cerebras.net/blog/slimpajama , 2023.

Tse et al. (2007) Dorothy Tse, Rosamund F. Langston, Masaki Kakeyama, Ingrid Bethus, Patrick A. Spooner, Emma R. Wood, Menno P. Witter, and Richard G. M. Morris. Schemas and memory consolidation. Science , 316(5821):76–82, 2007.

Tumma et al. (2026) Neehal Tumma, Noel Loo, and Daniela Rus. Preconditioned DeltaNet: Curvature-aware sequence modeling for linear recurrences. arXiv:2604.21100 , 2026.

Wang et al. (2025) Bailin Wang, Chang Lan, Chong Wang, and Ruoming Pang. RATTENTION: Towards the minimal sliding window size in local-global attention models. arXiv:2506.15545 , 2025.

Watson (1964) Geoffrey S. Watson. Smooth regression analysis. Sankhya: The Indian Journal of Statistics, Series A , 26(4):359–372, 1964.

Widrow & Hoff (1960) Bernard Widrow and Marcian E. Hoff. Adaptive switching circuits. In IRE WESCON Convention Record , 1960.

Wu et al. (2022) Yuhuai Wu, Markus N. Rabe, DeLesley Hutchins, and Christian Szegedy. Memorizing transformers. In ICLR , 2022. arXiv:2203.08913.

Xiao et al. (2024) Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. Efficient streaming language models with attention sinks. In ICLR , 2024. arXiv:2309.17453.

Yang et al. (2024a) Songlin Yang, Jan Kautz, and Ali Hatamizadeh. Gated delta networks: Improving mamba2 with delta rule. arXiv:2412.06464 , 2024a.

Yang et al. (2024b) Songlin Yang, Bailin Wang, Yikang Shen, Rameswar Panda, and Yoon Kim. Gated linear attention transformers with hardware-efficient training. In ICML , 2024b. arXiv:2312.06635.

Yang et al. (2024c) Songlin Yang, Bailin Wang, Yu Zhang, et al. Parallelizing linear transformers with the delta rule over sequence length. In NeurIPS , 2024c. arXiv:2406.06484.

Yogatama et al. (2021) Dani Yogatama, Cyprien de Masson d’Autume, and Lingpeng Kong. Adaptive semiparametric language models. Transactions of the ACL (TACL) , 2021. arXiv:2102.02557.

Zhang et al. (2024) Yu Zhang, Songlin Yang, Ruijie Zhu, Yue Zhang, Leyang Cui, Yiqiao Wang, Bolun Wang, Freda Shi, Bailin Wang, Wei Bi, Peng Zhou, and Guohong Fu. Gated slot attention for efficient linear-time sequence modeling. arXiv:2409.07146 , 2024.

Zhang et al. (2023) Zhenyu Zhang et al. H2O: Heavy-hitter oracle for efficient generative inference of large language models. In NeurIPS , 2023. arXiv:2306.14048.

## Appendix A Scale configurations

Table 6 lists the architecture, corpus size, and context length for the scaling comparison in Table 2 . Within each row, GDN and HOLA use the same backbone and training recipe; HOLA only adds the bounded exact KV cache.

For 170M and 340M, the architecture family follows the GDN recipe: 4 4 heads × \times head-dim 256 256 , expand ​ _ ​ v = 1 \mathrm{expand\_v}{=}1 , hidden ​ _ ​ ratio = 4 \mathrm{hidden\_ratio}{=}4 , conv 4, tied embeddings, vocabulary 32000 32000 , Mistral tokenizer, and AdamW with peak lr 4 × 10 − 4 4{\times}10^{-4} . The 46M row uses a smaller 12-layer, d model = 512 d_{\mathrm{model}}{=}512 architecture trained on FineWeb-Edu for 0.5B tokens at ctx 4096; this is the scale used for the component studies in Tables 4 – 5 .

HOLA cache hyperparameters: evict=betae, window=64, chunk=256, gate_init= − 4.0 -4.0 , cache_norm=rms, tau_init=1.0, tau_freeze=true, cache_kernel=sdpa . The GDN baseline shares all other settings within each row.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
