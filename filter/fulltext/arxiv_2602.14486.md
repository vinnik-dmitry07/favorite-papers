##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Revisiting the Platonic Representation Hypothesis: An Aristotelian View

###### Abstract

The Platonic Representation Hypothesis suggests that representations from neural networks are converging to a common statistical model of reality. We show that the existing metrics used to measure representational similarity are confounded by network scale : increasing model depth or width can systematically inflate representational similarity scores. To correct these effects, we introduce a permutation-based null-calibration framework that transforms any representational similarity metric into a calibrated score with statistical guarantees. We revisit the Platonic Representation Hypothesis with our calibration framework, which reveals a nuanced picture: the apparent convergence reported by global spectral measures largely disappears after calibration, while local neighborhood similarity, but not local distances, retains significant agreement across different modalities. Based on these findings, we propose the Aristotelian Representation Hypothesis : representations in neural networks are converging to shared local neighborhood relationships.

###### Keywords:

## 1 Introduction

Quantifying the similarity between neural network representations is central to understanding the geometry of learned representation spaces ( Raghu et al., 2017 ; Nguyen et al., 2021 ) , guiding transfer learning decisions ( Kornblith et al., 2019 ; Neyshabur et al., 2020 ; Gröger et al., 2025 ) , and relating artificial representations to neural measurements in neuroscience ( Schrimpf et al., 2018 ) . The Platonic Representation Hypothesis ( Huh et al., 2024 ) posits that as neural networks scale, representations across different modalities become increasingly similar, suggesting convergence to a shared statistical model of reality. This hypothesis has motivated a growing literature that uses representational similarity to study whether scaling produces universal structure across models ( Huh et al., 2024 ; Maniparambil et al., 2024 ; Tjandrasuwita et al., 2025 ; Zhu et al., 2026 ) . To measure representational similarity across models, different metrics have been proposed, such as Centered Kernel Alignment ( Kornblith et al., 2019 ) , Canonical Correlation Analysis ( Weenink, 2003 ) , Representational Similarity Analysis ( Kriegeskorte et al., 2008 ) , and mutual k k -Nearest Neighbors ( Huh et al., 2024 ) .

In this work, we identify two pervasive confounders that distort representational similarity measurements. The first is the model width : when the embedding dimension increases relative to the sample size, interaction-matrix-based similarity metrics exhibit a systematic positive baseline even when representations are independent. This spurious similarity is a general consequence of dimensionality-driven null inflation: the expected similarity under independence does not vanish but instead depends on both the representation dimensionality and the sample size ( Figure 2 a). As a result, wider models can appear more aligned simply because their representations live in higher-dimensional spaces. The second confounder is the model depth . Many analyses do not compare individual layer pairs, because it is unknown where similarity arises ( Schrimpf et al., 2018 ; Huh et al., 2024 ) . Instead, they search over all pairs and report a summary statistic such as the maximum. This is widespread practice: studies routinely compute similarity over many layer pairs and report an aggregate such as the maximum or best-matching layer ( Raghu et al., 2017 ; Kornblith et al., 2019 ; Schrimpf et al., 2018 ; Huh et al., 2024 ; Kapoor et al., 2025 ) . Taking a maximum over many comparisons inflates the reported score even if there is no similarity, since the expected maximum of independent draws exceeds the mean. This inflation grows with the number of comparisons, so deeper models can appear more aligned simply because more layer pairs are compared ( Figure 2 b). Together, these confounders undermine the comparative use of representational similarity without calibration.

To address these issues, we introduce the null-calibration for representational similarity , a general permutation-based framework that transforms any similarity metric into a calibrated score with a principled null reference, here defined as no relationship ( Figure 2 ). The core idea is to measure how extreme an observed similarity is relative to an empirical null distribution obtained by breaking sample correspondences. For scalar comparisons ( i.e. , width confounder), we estimate a critical threshold from the null distribution and define a calibrated score that is zero when the observed similarity falls below this threshold and rescaled to preserve the maximum at one. For selection-based summaries ( i.e. , depth confounder), we apply aggregation-aware calibration. We compute the null distribution of the same aggregate statistic that is ultimately reported ( e.g. , the maximum over all layer pairs), thereby calibrating the selection step itself.

These observations raise a question: Does the Platonic Representation Hypothesis still hold once similarity is calibrated? We find that, after calibration, the previously reported convergence in global metrics ( Huh et al., 2024 ; Maniparambil et al., 2024 ; Tjandrasuwita et al., 2025 ) largely disappears, suggesting it was driven primarily by width and depth confounders, whereas local neighborhood-based metrics retain significant cross-modal alignment ( Figure 2 c). However, we also observe that the convergence in local distances is not preserved, suggesting that only local neighborhood relationships are aligned. Motivated by these results, we refine the original Platonic Representation Hypothesis and propose the Aristotelian Representation Hypothesis 1 1 1 Calling this refinement Aristotelian : it emphasizes learned representations converging on relations among instances (who is near whom) rather than the idea of convergence toward a globally matching structure. : Neural networks, trained with different objectives on different data and modalities, converge to shared local neighborhood relationships ( Figure 1 ). We name it after the Greek philosopher Aristotle, who was a student of Plato and, in his Categories, established the principles of relatives ( Aristotle, ca. 350 B.C.E ) .

## 2 Related work

##### Representational similarity metrics.

A long line of work compares representation spaces using a variety of similarity measures. Canonical Correlation Analysis (CCA) ( Hotelling, 1992 ) and variants such as Singular Vector Canonical Correlation Analysis (SVCCA) ( Raghu et al., 2017 ) and Projection Weighted Canonical Correlation Analysis (PWCCA) ( Morcos et al., 2018 ) compare subspaces up to linear transformations, while Procrustes- and shape-based distances compare representations up to restricted alignment classes ( Ding et al., 2021 ; Williams et al., 2021 ) . Centered Kernel Alignment (CKA) ( Kornblith et al., 2019 ) has become a dominant tool for comparing deep representations, with kernelized variants extending to nonlinear similarity. Representational Similarity Analysis (RSA) ( Kriegeskorte et al., 2008 ) , originating in neuroscience, compares representational dissimilarity matrices rather than feature bases. Neighborhood-based approaches, such as mutual k k -Nearest Neighbors (mKNN) ( Huh et al., 2024 ) , capture local topological consistency rather than global alignment. However, recent evaluations stress that different metrics encode different invariances and can yield qualitatively different conclusions, motivating more robust reporting practices ( Klabunde et al., 2025a ; Klabunde et al., 2025b ; Ding et al., 2021 ; Harvey et al., 2024 ; Bo et al., 2024 ) . This sensitivity is especially consequential in the neuro-AI literature, where the choice of similarity measure can profoundly change conclusions about which models best align with the brain ( Soni et al., 2024 ) , which is why scores that are calibrated and comparable across metrics and scales are needed.

##### Reliability of representational similarity metrics.

In finite-sample, high-dimensional regimes, raw similarity scores can be systematically biased. Recent works ( Murphy et al., 2024 ; Chun et al., 2025 ) propose debiased CKA , but these corrections are metric-specific . For neighborhood-based metrics, no analogous debiasing methods exist despite distance concentration effects that inflate random k k -NN overlap ( Beyer et al., 1999 ; Aggarwal et al., 2001 ) . Other approaches address confounding from input population structure . For instance, Cui et al. (2022) propose regression-style deconfounding to remove effects of shared input statistics on RSA / CKA . Analogous concerns arise for regression-based predictivity in neuroscience, where high-dimensional fits can inflate alignment scores and may fail to identify genuinely brain-like models ( Schaeffer et al., 2024 ) . A separate reliability issue arises from layer search, where max or top- k k aggregation across many layer pairs introduces multiple-comparison inflation. While resampling-based “maxT” procedures ( Westfall and Young, 1993 ; Nichols and Holmes, 2002 ) can calibrate such aggregates, this has not yet been applied in representational similarity studies. Our calibration framework addresses both finite-sample bias and selection inflation in a unified, metric-agnostic way.

##### The Platonic Representation Hypothesis.

A growing body of work examines whether neural networks trained under different conditions converge toward similar representations. The Platonic Representation Hypothesis ( Huh et al., 2024 ) posits that as models scale, their representations increasingly converge across architectures and even across modalities such as vision and language, with convergence reported under both global and local similarity measures. Follow-up work has examined factors influencing these trends, including model size, training duration, and data distribution ( Raugel et al., 2025 ) , and has explored analogous convergence effects in broader settings such as video models ( Zhu et al., 2026 ) and comparisons to biological vision ( Marcos-Manchón and Fuentemilla, 2025 ) . Prior work attributes convergence to shared factors such as training data distribution, scale, and objective functions ( Raugel et al., 2025 ; Huh et al., 2024 ) . Our calibration-based analysis does not contradict these findings but refines their interpretation, showing that the evidence for convergence depends on whether it is measured by global or local similarity. In this work, we revisit the Platonic Representation Hypothesis using our null-calibration framework that controls for width and depth confounders.

## 3 Problem setup

### 3.1 Representation spaces and similarity score

Let 𝒳 ⊆ ℝ d x \mathcal{X}\subseteq\mathbb{R}^{d_{x}} and 𝒴 ⊆ ℝ d y \mathcal{Y}\subseteq\mathbb{R}^{d_{y}} be two representation spaces, where d x d_{x} and d y d_{y} are the respective space dimensions. For a set of n n input samples, let 𝐗 ∈ ℝ n × d x \mathbf{X}\in\mathbb{R}^{n\times d_{x}} and 𝐘 ∈ ℝ n × d y \mathbf{Y}\in\mathbb{R}^{n\times d_{y}} be the corresponding embeddings in 𝒳 \mathcal{X} and 𝒴 \mathcal{Y} . We assume row-wise alignment such that the i i -th row of 𝐗 \mathbf{X} and 𝐘 \mathbf{Y} correspond to paired inputs. We use a similarity score s ⁡ ( 𝒳 , 𝒴 ) ∈ ℝ s(\mathcal{X},\mathcal{Y})\in\mathbb{R} to quantify the agreement between 𝒳 \mathcal{X} and 𝒴 \mathcal{Y} . In practice, we compute it from 𝐗 , 𝐘 \mathbf{X},\mathbf{Y} and, by a slight abuse of notation, denote it with s ⁡ ( 𝐗 , 𝐘 ) s(\mathbf{X},\mathbf{Y}) .

We consider three families of metrics: (i) spectral: metrics defined on the spectrum of cross-covariance or Gram matrices ( e.g. , CKA , CCA ), (ii) neighborhood: metrics measuring local topological overlap ( e.g. , mKNN ), and (iii) geometric: second-order isomorphism metrics ( e.g. , RSA ). Appendix B provides definitions of the metrics used in this paper.

### 3.2 The null hypothesis of independence

We claim that a similarity score s ⁡ ( 𝐗 , 𝐘 ) s(\mathbf{X},\mathbf{Y}) is uninterpretable without a baseline. To provide this baseline, we define the null hypothesis H 0 H_{0} as the absence of a relationship between 𝐗 \mathbf{X} and 𝐘 \mathbf{Y} beyond their marginal statistics. We operationalize H 0 H_{0} via a permutation group Π n \Pi_{n} acting on sample indices: draw π ∼ Unif ⁡ ( Π n ) \pi\sim\mathrm{Unif}(\Pi_{n}) independently of ( 𝐗 , 𝐘 ) (\mathbf{X},\mathbf{Y}) and evaluate s ⁡ ( 𝐗 , π ⁡ ( 𝐘 ) ) s(\mathbf{X},\pi(\mathbf{Y})) , where π ⁡ ( 𝐘 ) \pi(\mathbf{Y}) permutes the rows of 𝐘 \mathbf{Y} .

###### Assumption 3.1 (Exchangeability under the null) .

Under H 0 H_{0} , the joint distribution of paired samples is invariant to relabeling of correspondences. For any permutation π ∈ Π n \pi\in\Pi_{n} , ℙ H 0 ​ ( 𝐗 , 𝐘 ) = ℙ H 0 ​ ( 𝐗 , π ⁡ ( 𝐘 ) ) \mathbb{P}_{H_{0}}(\mathbf{X},\mathbf{Y})=\mathbb{P}_{H_{0}}(\mathbf{X},\pi(\mathbf{Y})) .

This assumption implies that if no true relationship exists, the observed pairing is statistically indistinguishable from a random shuffling of the data. It allows us to construct an empirical null distribution by holding 𝐗 \mathbf{X} fixed and shuffling the rows of 𝐘 \mathbf{Y} .

### 3.3 Baseline problem: non-zero null expectations

Ideally, under H 0 H_{0} , we desire 𝔼 π ​ [ s ⁡ ( 𝐗 , π ⁡ ( 𝐘 ) ) ] ≈ 0 \mathbb{E}_{\pi}[s(\mathbf{X},\pi(\mathbf{Y}))]\approx 0 . However, for commonly used raw or biased estimators, the expected similarity under the null is not zero , μ 0 ​ ( n , d x , d y ) ≔ 𝔼 π ​ [ s ⁡ ( 𝐗 , π ⁡ ( 𝐘 ) ) ] . \mu_{0}(n,d_{x},d_{y})\,\coloneqq\,\mathbb{E}_{\pi}[s(\mathbf{X},\pi(\mathbf{Y}))]. (1) This baseline μ 0 \mu_{0} is metric- and preprocessing-dependent and can deviate from zero in finite samples. It also varies with sample size and dimension, thus acting as a confounding variable in comparative studies.

## 4 Theoretical motivation: spurious alignment

We motivate and formalize why raw representational similarity metrics fail in cross-scale model comparisons. We identify two distinct sources of confounding: (i) the width confounder driven by representation dimension, and (ii) the depth confounder driven by the number of layers considered when comparing models.

### 4.1 The width confounder

Many spectral-family similarity metrics, e.g. , linear/kernel CKA and the RV coefficient, can be written as functionals of an interaction operator constructed from two representations. One such operator is the (normalized) cross-covariance 𝐂 ~ = 1 n − 1 ​ 𝐗 c ⊤ ​ 𝐘 c ∈ ℝ d x × d y , \widetilde{\mathbf{C}}\;=\;\frac{1}{n-1}\mathbf{X}_{c}^{\top}\mathbf{Y}_{c}\in\mathbb{R}^{d_{x}\times d_{y}}, (2) where 𝐗 c \mathbf{X}_{c} and 𝐘 c \mathbf{Y}_{c} denote row-centered representations ( Section B.1 ).

A common but misleading intuition is that if 𝐗 \mathbf{X} and 𝐘 \mathbf{Y} are independent, then 𝐂 ~ ≈ 𝟎 \widetilde{\mathbf{C}}\approx\mathbf{0} and therefore spectral aggregates should be near zero. In high dimension this fails: the null interaction energy is typically non-zero.

###### Proposition 4.1 (Non-vanishing null interaction energy) .

Assume the rows are i.i.d. with 𝔼 ⁡ [ 𝐱 i ] = 𝔼 ⁡ [ 𝐲 i ] = 0 \mathbb{E}[\mathbf{x}_{i}]=\mathbb{E}[\mathbf{y}_{i}]=0 , Cov ⁡ ( 𝐱 i ) = 𝐈 d x \mathrm{Cov}(\mathbf{x}_{i})=\mathbf{I}_{d_{x}} , Cov ⁡ ( 𝐲 i ) = 𝐈 d y \mathrm{Cov}(\mathbf{y}_{i})=\mathbf{I}_{d_{y}} , and 𝐱 i \mathbf{x}_{i} and 𝐲 i \mathbf{y}_{i} are independent. Then 𝔼 H 0 ​ [ ‖ 𝐂 ~ ‖ F 2 ] = d x ​ d y n − 1 . \mathbb{E}_{H_{0}}\left[\|\widetilde{\mathbf{C}}\|_{F}^{2}\right]\;=\;\frac{d_{x}d_{y}}{n-1}. (3)

Proof. See Section C.4 .

Since CKA is scaled by the normalized self-similarity terms, which each scale as 𝒪 ⁡ ( d ) \mathcal{O}(\sqrt{d}) , the resulting null baseline for the metric is thus 𝒪 ⁡ ( d / n ) \mathcal{O}(d/n) to leading order. We refer to this 𝒪 ⁡ ( d / n ) \mathcal{O}(d/n) effect as the width confounder : at a fixed sample size n n it grows with the representation width d d , and it persists even when two representations share a genuine signal ( Proposition C.5 ).

This aligns with insights from random matrix theory: in high-dimensional regimes ( d ∼ n d\sim n ), the null singular spectrum of interaction operators (after centering/whitening) concentrates into a non-trivial “noise bulk” whose upper edge depends on d / n d/n and preprocessing, rather than collapsing to zero ( Wachter, 1978 ; Müller, 2002 ; Livan et al., 2018 ) . Our framework estimates this null baseline directly via permutation, providing a metric- and pipeline-independent alternative to asymptotic formulas.

##### Neighborhood metrics follow a different regime.

While spectral metrics have null baselines scaling as 𝒪 ⁡ ( d / n ) \mathcal{O}(d/n) , neighborhood-based metrics such as mutual k k -NN exhibit different behavior, as they rely on set comparisons rather than interactions.

###### Proposition 4.2 (Null baseline for neighborhood metrics) .

Assume the rows are i.i.d. with 𝐱 i \mathbf{x}_{i} and 𝐲 i \mathbf{y}_{i} independent, and that pairwise distances are almost surely distinct (e.g., under absolutely continuous distributions). Then for any k < n k<n , 𝔼 H 0 ​ [ mKNN ⁡ ( 𝐗 , 𝐘 ) ] = k n − 1 . \mathbb{E}_{H_{0}}\bigg[\mathrm{mKNN}(\mathbf{X},\mathbf{Y})\bigg]\;=\;\frac{k}{n-1}. (4)

Proof. See Section C.6 .

In particular, neighborhood metrics have null baselines scaling as 𝒪 ⁡ ( k / n ) \mathcal{O}(k/n) .

The difference in null baseline between spectral and neighborhood metrics is substantial: (i) The neighborhood scale k k can be fixed consistently across experiments, whereas the embedding dimension d d is determined by the model architecture, making it difficult to control in comparison studies. (ii) The neighborhood metrics are much less confounded since k ≪ d k\ll d in typical settings.

Geometric metrics ( e.g. , Procrustes), similarly to the spectral metrics, are functions of all-pairs distances or inner products, which are the interaction quantities of Proposition 4.1 . They thus inherit a width-dependent 𝒪 ⁡ ( d / n ) \mathcal{O}(d/n) baseline rather than the 𝒪 ⁡ ( k / n ) \mathcal{O}(k/n) baseline of rank-based neighborhood metrics. We verify this empirically in Section E.7 .

### 4.2 The depth confounder

A subtle yet pervasive issue is the comparison of selection-based alignment summaries across models. Let S ℓ , ℓ ′ := s ⁡ ( 𝐗 ℓ ( A ) , 𝐘 ℓ ′ ( B ) ) S_{\ell,\ell^{\prime}}:=s(\mathbf{X}^{(A)}_{\ell},\mathbf{Y}^{(B)}_{\ell^{\prime}}) be the similarity between layer ℓ \ell of model A A and layer ℓ ′ \ell^{\prime} of model B B . It is common to summarize the similarity between two models by the maximum alignment score T max = max ℓ , ℓ ′ ⁡ S ℓ , ℓ ′ T_{\max}=\max_{\ell,\ell^{\prime}}S_{\ell,\ell^{\prime}} ( Schrimpf et al., 2018 ; Huh et al., 2024 ; Raghu et al., 2017 ; Kornblith et al., 2019 ) . Let M = L A ​ L B M=L_{A}L_{B} be the number of layer pairs searched, where L A L_{A} and L B L_{B} are the depths of models A A and B B . Even under H 0 H_{0} , taking a maximum over M M comparisons inflates the reported score, a “look-elsewhere” effect. This is an instance of the classical multiple comparisons problem ( Benjamini and Hochberg, 1995 ; Bonferroni, 1936 ) : as M M increases, the probability that at least one null similarity exceeds any fixed threshold grows, inflating the expected maximum. Consequently, when alignment is summarized via a max or top- k k statistic without correction, unrelated representations can exhibit spuriously high reported similarity, as the inflation depends on model depth, making raw summaries non-comparable across architectures.

Characterizing this inflation does not require independence across pairs. It follows from a uniform right-tail bound. Assume there exist a common mean μ ∈ ℝ \mu\in\mathbb{R} and σ > 0 \sigma>0 such that the null fluctuations satisfy, for all ( ℓ , ℓ ′ ) (\ell,\ell^{\prime}) and all t ≥ 0 t\geq 0 , ℙ ⁡ ( S ℓ , ℓ ′ − μ ≥ t ) ≤ exp ⁡ ( − t 2 2 ​ σ 2 ) . \mathbb{P}(S_{\ell,\ell^{\prime}}-\mu\geq t)\leq\exp\!\left(-\frac{t^{2}}{2\sigma^{2}}\right). (5) For bounded similarities S ℓ , ℓ ′ ∈ [ s min , s max ] S_{\ell,\ell^{\prime}}\in[s_{\min},s_{\max}] , Hoeffding’s inequality implies a sub-Gaussian right-tail bound of the form Equation 5 with σ ≤ ( s max − s min ) / 2 \sigma\leq(s_{\max}-s_{\min})/2 . This covers many common bounded metrics ( e.g. , CKA / RSA / mKNN ). Crucially, only the right tail is needed for bounding the maximum. Then a union bound gives ℙ ⁡ ( T max − μ ≥ t ) ≤ M ​ exp ⁡ ( − t 2 2 ​ σ 2 ) , \mathbb{P}(T_{\max}-\mu\geq t)\leq M\exp\!\left(-\frac{t^{2}}{2\sigma^{2}}\right), (6) and consequently for a constant C C 𝔼 H 0 ​ [ T max ] ≤ μ + C ​ σ ​ log ⁡ M . \mathbb{E}_{H_{0}}\left[T_{\max}\right]\;\leq\;\mu+C\,\sigma\sqrt{\log M}. (7) Proof. See Section C.5 .

This creates a depth confounder. Deeper models (larger M = L A ​ L B M=L_{A}L_{B} ) can attain higher raw “max-alignment” scores purely because of a larger search space. Correlations across neighboring layers reduce the effective number of comparisons, but the inflation remains monotone in the search space size in typical workflows. Therefore, raw scaling plots of T max T_{\max} (or top- k k summaries) are not comparable across architectures unless the selection step itself is calibrated.

The two confounders are not independent but hierarchical: the depth confounder operates on top of the width confounder. The width confounder gives each individual layer pair a positive chance similarity, and deeper models supply a larger pool of such chance similarities, so the selection maximum drifts higher.

## 5 Representational similarity calibration

To overcome the issues of the width and depth confounders, we introduce the null-calibration for representational similarity. The key idea is to compare observed similarity scores against an empirical null distribution obtained by permuting sample correspondences, thereby establishing a principled zero point that accounts for finite-sample, high-dimensional artifacts.

### 5.1 Null-calibrated similarity

We propose null-calibrated similarity measures to correct for width and depth confounders by transforming raw similarity scores into an effect size with a principled zero point.

Given representations 𝐗 ∈ ℝ n × d x \mathbf{X}\in\mathbb{R}^{n\times d_{x}} and 𝐘 ∈ ℝ n × d y \mathbf{Y}\in\mathbb{R}^{n\times d_{y}} aligned by rows, we operationalize the null hypothesis H 0 H_{0} (no relationship beyond marginal statistics) by permuting sample correspondences. For permutations π k ∈ Π n \pi_{k}\in\Pi_{n} drawn i.i.d. uniformly from Π n \Pi_{n} and independently of ( 𝐗 , 𝐘 ) (\mathbf{X},\mathbf{Y}) , we form null scores s ( k ) = s ( 𝐗 , π k ( 𝐘 ) ) , k = 1 , … , K . s^{(k)}=s(\mathbf{X},\pi_{k}(\mathbf{Y})),\qquad k=1,\dots,K. (8) Let s obs := s ⁡ ( 𝐗 , 𝐘 ) s_{\mathrm{obs}}:=s(\mathbf{X},\mathbf{Y}) denote the observed score. Let s ( 1 ) ≤ s ( 2 ) ≤ ⋯ ≤ s ( K + 1 ) s_{(1)}\leq s_{(2)}\leq\cdots\leq s_{(K+1)} denote the order statistics of the combined multiset { s obs , s ( 1 ) , … , s ( K ) } \{s_{\mathrm{obs}},s^{(1)},\dots,s^{(K)}\} (with ties allowed). We define a right-tail rank-based critical value: τ α := s ( ⌈ ( 1 − α ) ​ ( K + 1 ) ⌉ ) , \tau_{\alpha}\;:=\;s_{(\lceil(1-\alpha)(K+1)\rceil)}, (9) where ⌈ ( 1 − α ) ​ ( K + 1 ) ⌉ \lceil(1-\alpha)(K+1)\rceil is the ( 1 − α ) (1-\alpha) -quantile of the ( K + 1 ) (K+1) -sized multiset and the empirical right-tail p p -value: p = 1 + # ⁡ { k ∈ { 1 , … , K } : s ( k ) ≥ s obs } K + 1 . p\;=\;\frac{1+\#\{k\in\{1,\dots,K\}:s^{(k)}\geq s_{\mathrm{obs}}\}}{K+1}. (10)

The critical value τ α \tau_{\alpha} defines a robust zero point: values below τ α \tau_{\alpha} are typical under H 0 H_{0} at level α \alpha , while p p provides an evidence measure that can be combined with multiple-testing correction when many comparisons are performed.

The proposed calibration framework relies on randomization (permutation) to construct a null distribution for any similarity statistic. This yields finite-sample guarantees under an exchangeability condition ( Assumption 3.1 ), and it implies useful invariances that make calibrated scores comparable across metrics and implementations.

The permutation p p -value in Equation 10 is super-uniform under H 0 H_{0} ( i.e. , ℙ H 0 ​ ( p ≤ α ) ≤ α \mathbb{P}_{H_{0}}(p\leq\alpha)\leq\alpha for all α ∈ [ 0 , 1 ] \alpha\in[0,1] ), a standard consequence of randomization inference ( Nichols and Holmes, 2002 ; Phipson and Smyth, 2010 ; Good, 2005 ) (see Section C.1 for formal definitions and proofs).

###### Corollary 5.1 (Type-I control for calibrated scores) .

Let s obs = s ⁡ ( 𝐗 , 𝐘 ) s_{\mathrm{obs}}=s(\mathbf{X},\mathbf{Y}) and s ( k ) = s ⁡ ( 𝐗 , π k ​ ( 𝐘 ) ) s^{(k)}=s(\mathbf{X},\pi_{k}(\mathbf{Y})) for k = 1 , … , K k=1,\dots,K . Define the add-one permutation p p -value p p as in Equation 10 , and equivalently define the rank-based critical value τ α := s ( ⌈ ( 1 − α ) ​ ( K + 1 ) ⌉ ) \tau_{\alpha}:=s_{(\lceil(1-\alpha)(K+1)\rceil)} from the sorted combined set { s obs , s ( 1 ) , … , s ( K ) } \{s_{\mathrm{obs}},s^{(1)},\dots,s^{(K)}\} . Under Assumption 3.1 , ℙ H 0 ​ ( p ≤ α ) ≤ α and hence ℙ H 0 ​ ( s obs > τ α ) ≤ α , \mathbb{P}_{H_{0}}\big(p\leq\alpha\big)\leq\alpha\quad\text{and hence}\quad\mathbb{P}_{H_{0}}\big(s_{\mathrm{obs}}>\tau_{\alpha}\big)\leq\alpha, (11) so the gating rule “ s cal > 0 s_{\mathrm{cal}}>0 ” (where s cal s_{\mathrm{cal}} is the calibrated score defined in Equation 12 , which implies p ≤ α p\leq\alpha ) is a finite-sample α \alpha -level declaration of similarity above chance.

Proof. Follows directly from Lemma C.2 ; see Section C.1 .

##### Calibrated score (scalar case).

While p p -values and null percentiles are rank-based and therefore invariant under monotone transformations of the raw score ( Proposition C.3 ; see Section C.2 ), effect sizes serve a complementary purpose: they quantify how much similarity exceeds chance on an interpretable scale. The calibrated score achieves this by rescaling the excess over the null threshold τ α \tau_{\alpha} to the interval [ 0 , 1 ] [0,1] . This rescaling is not monotone-invariant, by design. A purely rank-based calibration would be equivalent to a score shift and would be unable to correct for the scale-dependent null baselines identified in Section 4 . The calibrated score instead adapts to the actual null distribution, providing a meaningful zero point.

For similarity metrics with a known maximum (upper bound) s max s_{\max} (often s max = 1 s_{\max}=1 ), we define a max-preserving calibrated score s cal = max ⁡ ( s obs − τ α s max − τ α , 0 ) . s_{\mathrm{cal}}=\max\!\left(\frac{s_{\mathrm{obs}}-\tau_{\alpha}}{s_{\max}-\tau_{\alpha}},0\right). (12) This calibrated score depends on the chosen level α \alpha through τ α \tau_{\alpha} ( Equation 9 ). We therefore also report the corresponding permutation p p -value and/or null percentile for an α \alpha -free summary. This score satisfies s cal = 0 s_{\mathrm{cal}}=0 whenever s obs ≤ τ α s_{\mathrm{obs}}\leq\tau_{\alpha} ( i.e. , below the estimated right-tail critical value of the permutation null), and s cal = 1 s_{\mathrm{cal}}=1 when s obs = s max s_{\mathrm{obs}}=s_{\max} ( i.e. , perfect similarity remains 1 1 ). When s max s_{\max} is unknown, or the metric is unbounded, we default to the unnormalized effect size [ s − τ α ] + = max ⁡ ( s − τ α , 0 ) [s-\tau_{\alpha}]_{+}=\max(s-\tau_{\alpha},0) .

### 5.2 Aggregation-aware null-calibration

To analyze the similarity between two models A A and B B with depths L A L_{A} and L B L_{B} , a common approach is to compute a layer-by-layer similarity matrix 𝐒 ∈ ℝ L A × L B \mathbf{S}\in\mathbb{R}^{L_{A}\times L_{B}} by evaluating a similarity score for every pair of layers: S ℓ , ℓ ′ = s ⁡ ( 𝐗 ℓ ( A ) , 𝐘 ℓ ′ ( B ) ) , S_{\ell,\ell^{\prime}}=s\!\left(\mathbf{X}^{(A)}_{\ell},\mathbf{Y}^{(B)}_{\ell^{\prime}}\right), (13) where 𝐗 ℓ ( A ) ∈ ℝ n × d ℓ \mathbf{X}^{(A)}_{\ell}\in\mathbb{R}^{n\times d_{\ell}} and 𝐘 ℓ ′ ( B ) ∈ ℝ n × d ℓ ′ \mathbf{Y}^{(B)}_{\ell^{\prime}}\in\mathbb{R}^{n\times d_{\ell^{\prime}}} are the representations of models A A and B B at layers ℓ \ell and ℓ ′ \ell^{\prime} respectively, evaluated on n n samples, and s ⁡ ( ⋅ , ⋅ ) s(\cdot,\cdot) is a similarity metric. A common practice is then to summarize 𝐒 \mathbf{S} by a selection-based aggregation operator, such as taking the maximum. These summaries are attractive because they support statements such as “there exists a layer in A A that matches some layer in B B ” or “each layer of A A best matches a layer in B B ”. However, selection introduces a statistical effect: even under the null hypothesis of no relationship between representations, selection-based summaries are systematically inflated.

As analyzed in Section 4.2 , this inflation grows with the number of layer pairs and makes naïve post-selection p p -values anti-conservative. Our aggregation-aware calibration addresses this by calibrating the reported statistic directly: the null distribution must match the entire analysis pipeline. Let the aggregate score be T ⁡ ( 𝐒 ) T(\mathbf{S}) ( e.g. , a maximum), then the appropriate null is the distribution of T ⁡ ( 𝐒 ) T(\mathbf{S}) under a valid null transformation ( e.g. , permuting sample correspondences). We therefore define an aggregation-aware permutation null. When T T is the maximum over layer pairs, this recovers the classical “maxT” procedure of Westfall and Young (1993) . Our formulation generalizes it to arbitrary selection-based aggregates ( e.g. , top- k k ) and to any similarity metric.

##### Consistency of permutations across layers.

For each draw π k ∈ Π n \pi_{k}\in\Pi_{n} , we apply the same sample permutation to all layers of model B B and define S ℓ , ℓ ′ ( k ) := s ⁡ ( 𝐗 ℓ ( A ) , π k ​ ( 𝐘 ℓ ′ ( B ) ) ) , \displaystyle S^{(k)}_{\ell,\ell^{\prime}}:=s\!\left(\mathbf{X}^{(A)}_{\ell},\pi_{k}\!\left(\mathbf{Y}^{(B)}_{\ell^{\prime}}\right)\right), (14) ℓ = 1 , … , L A , ℓ ′ = 1 , … , L B , \displaystyle\ell=1,\dots,L_{A},\quad\ell^{\prime}=1,\dots,L_{B}, then compute T ( k ) := T ⁡ ( 𝐒 ( k ) ) T^{(k)}:=T(\mathbf{S}^{(k)}) . Let T obs := T ⁡ ( 𝐒 ) T_{\mathrm{obs}}:=T(\mathbf{S}) denote the observed aggregate. Let T ( 1 ) ≤ ⋯ ≤ T ( K + 1 ) T_{(1)}\leq\cdots\leq T_{(K+1)} denote the order statistics of the combined set { T obs , T ( 1 ) , … , T ( K ) } \{T_{\mathrm{obs}},T^{(1)},\dots,T^{(K)}\} (with ties allowed). We define τ α agg := T ( ⌈ ( 1 − α ) ​ ( K + 1 ) ⌉ ) , \tau_{\alpha}^{\mathrm{agg}}:=T_{(\lceil(1-\alpha)(K+1)\rceil)}, (15) where ⌈ ( 1 − α ) ​ ( K + 1 ) ⌉ \lceil(1-\alpha)(K+1)\rceil is the ( 1 − α ) (1-\alpha) -quantile of the ( K + 1 ) (K+1) -sized multiset. We report the right-tail permutation p p -value p agg = 1 + # ⁡ { k ∈ { 1 , … , K } : T ( k ) ≥ T obs } K + 1 , p_{\mathrm{agg}}=\frac{1+\#\{k\in\{1,\ldots,K\}:T^{(k)}\geq T_{\mathrm{obs}}\}}{K+1}, (16) By the same exchangeability argument as for scalar calibration, p agg p_{\mathrm{agg}} is super-uniform under H 0 H_{0} (see Proposition C.4 ).

##### Calibrated score (aggregate case).

For bounded similarities with maximum s max s_{\max} (often s max = 1 s_{\max}=1 ), we report a max-preserving calibrated aggregate T cal = max ⁡ ( T obs − τ α agg s max − τ α agg , 0 ) . T_{\mathrm{cal}}=\max\!\left(\frac{T_{\mathrm{obs}}-\tau_{\alpha}^{\mathrm{agg}}}{s_{\max}-\tau_{\alpha}^{\mathrm{agg}}},\,0\right). (17) This score satisfies T cal = 0 T_{\mathrm{cal}}=0 when T obs ≤ τ α agg T_{\mathrm{obs}}\leq\tau_{\alpha}^{\mathrm{agg}} and T cal = 1 T_{\mathrm{cal}}=1 when T obs = s max T_{\mathrm{obs}}=s_{\max} . As above, T cal T_{\mathrm{cal}} depends on α \alpha via τ α agg \tau_{\alpha}^{\mathrm{agg}} ; we therefore report both T cal T_{\mathrm{cal}} (magnitude above null) and p agg p_{\mathrm{agg}} (evidence against null), applying multiplicity correction ( Holm, 1979 ; Benjamini and Hochberg, 1995 ) when many model pairs are evaluated.

### 5.3 Summary

To compute a calibrated similarity score: (i) fix a significance level α \alpha ( e.g. , α = 0.05 \alpha=0.05 ); (ii) generate K K null scores by permuting sample correspondences; (iii) compute critical value τ \tau as the ⌈ ( 1 − α ) ​ ( K + 1 ) ⌉ \lceil(1-\alpha)(K+1)\rceil -th order statistic of the combined set (observed + null scores); (iv) return calibrated score, either s cal s_{\mathrm{cal}} or T cal T_{\mathrm{cal}} .

Use scalar calibration ( Section 5.1 ) when comparing a single pair of representations. Use aggregation-aware calibration ( Section 5.2 ) when reporting a summary statistic ( e.g. , maximum) over multiple layer pairs. Appendix D provides pseudocode for both procedures.

## 6 Experiments

We quantify the effects of the width and depth confounders in controlled synthetic experiments and show that our calibration framework effectively removes them. We then revisit the Platonic Representation Hypothesis using our calibration framework, assessing which convergence trends remain robust after controlling for these confounding factors.

### 6.1 Null-calibration removes width confounder

We validate that our calibration eliminates width-related inflation of similarity across metrics, regimes, and noise distributions, without metric-specific derivations.

We design controlled synthetic experiments as follows. Under H 0 H_{0} , we draw 𝐗 , 𝐘 ∈ ℝ n × d \mathbf{X},\mathbf{Y}\in\mathbb{R}^{n\times d} independently from Gaussian and heavy-tailed (Student- t t , Laplace) distributions. We vary the number of samples n ∈ { 128,256,512 , 1024 , 2048 , 4096 } n\in\{128,256,512,1024,2048,4096\} and the dimension d ∈ { 128,256,512 , 1024 , 2048 } d\in\{128,256,512,1024,2048\} . Under H 1 H_{1} , we inject a shared low-rank signal component and vary the signal-to-noise ratio. We evaluate representative metrics spanning three families. For spectral similarity, we use linear and RBF CKA , as well as CCA /SVCCA/PWCCA; for neighborhood similarity, we use mKNN (with k = 10 k=10 ); and for geometric similarities, we use RSA and Procrustes. Figure 3 reports a subset of these metrics for readability; additional metrics are reported in Section E.7 . For calibration, we use K = 200 K=200 permutations with α = 0.05 \alpha=0.05 .

Under H 0 H_{0} , uncalibrated scores are systematically inflated, while our calibrated scores stay at zero across settings ( Figure 3 ). This confirms that the similarity scores of wider models can arise purely from high-dimensional finite-sample effects, and our calibration removes this spurious baseline. Importantly, the magnitude of the null baseline is metric-dependent, consistent with our theory: CKA’s baseline scales as 𝒪 ⁡ ( d / n ) \mathcal{O}(d/n) ( Proposition 4.1 ), while mKNN ’s baseline scales as 𝒪 ⁡ ( k / n ) \mathcal{O}(k/n) ( Proposition 4.2 ). Intuitively, mKNN compares local neighborhood overlap at a fixed k k , thus only comparing relationships instead of local distances, making its null baseline insensitive to representation width d d , which explains the order-of-magnitude gap observed in raw scores. The same pattern holds for heavy-tailed noise ( Section E.7 ).

The same width inflation arises under a genuine shared signal, and calibration corrects it there as well, as we show analytically ( Proposition C.5 ) and on real networks at fixed n n ( Section E.5 ).

Next, we verify the statistical guarantees of our empirical null calibration. For Type-I error control, rejection rates stay at or below the nominal α = 0.05 \alpha=0.05 across ( n , d / n ) (n,d/n) configurations ( Figure 4 a). Crucially, our calibration does not sacrifice sensitivity to real alignment: detection rates increase rapidly with signal strength ( Figure 4 b). Overall, our calibration preserves signal structure: in the high-signal regime, raw and calibrated scores show the same pattern, while in the low-signal regime, calibration correctly gates scores to zero ( Section E.2 ).

Furthermore, we verify that our empirical calibration closely matches existing analytical bias corrections for CKA ( Murphy et al., 2024 ) , recovering the width correction without metric-specific derivation ( Section E.4 ).

Additionally, we perform ablations on different noise distributions used in the synthetic experiments ( Section E.1 ), different calibration approaches ( Section E.3 ), and an ablation on the influence of the number of permutations K K used for calibration ( Section E.6 ).

### 6.2 Null-calibration removes depth confounder

We validate that our aggregation-aware null-calibration eliminates the depth confounder. To build a controlled synthetic setting, we construct two synthetic models, A A and B B , each with L L layers. Under H 0 H_{0} , we sample layer representations { 𝐗 ℓ } ℓ = 1 L \{\mathbf{X}_{\ell}\}_{\ell=1}^{L} and { 𝐘 ℓ ′ } ℓ ′ = 1 L \{\mathbf{Y}_{\ell^{\prime}}\}_{\ell^{\prime}=1}^{L} , where each 𝐗 ℓ , 𝐘 ℓ ′ ∈ ℝ n × d \mathbf{X}_{\ell},\mathbf{Y}_{\ell^{\prime}}\in\mathbb{R}^{n\times d} has i.i.d. 𝒩 ⁡ ( 0 , 1 ) \mathcal{N}(0,1) entries (independent across layers and between models), using d / n = 8 d/n=8 to match the upper range of the Platonic Representation Hypothesis setting. We then compute the layerwise similarity matrix S ℓ , ℓ ′ = CKA ⁡ ( 𝐗 ℓ , 𝐘 ℓ ′ ) S_{\ell,\ell^{\prime}}=\operatorname{CKA}(\mathbf{X}_{\ell},\mathbf{Y}_{\ell^{\prime}}) and summarize it with standard aggregates.

The uncalibrated max-aggregated scores inflate with layer count even under H 0 H_{0} ( Figure 6 ): raw max-scores are systematically higher at L = 128 L=128 than at L = 2 L=2 , despite no true signal. Our aggregation-aware calibration eliminates this bias: calibrated aggregates remain stable regardless of depth. We further show that naively calibrating each scalar comparison still leads to inflation, highlighting the importance of calibrating the final statistic. Furthermore, since deeper models tend to be wider as well, raw comparisons are doubly confounded.

### 6.3 Revisiting the Platonic Representation Hypothesis

A central claim behind the Platonic Representation Hypothesis is that, as models become more capable, their representations begin to converge across modalities. We revisit this claim through our calibration framework to determine whether the observed alignment reflects genuine shared representation structure or instead arises from width and depth confounders.

We follow the experimental protocol of Huh et al. (2024) using n = 1024 n=1024 image–text pairs (WIT; Srinivasan et al. (2021) ) and embeddings from three language model families (BLOOM, OpenLLaMA, LLaMA) and five vision model families (ImageNet-21K, MAE, DINOv2, CLIP, CLIP-finetuned) across multiple scales. As in Huh et al. (2024) , we extract per-layer representations using the class token for vision models and mean pooling over tokens for language models. This yields 204 vision–language model pairs spanning d / n ∈ [ 0.19 , 8 ] d/n\in[0.19,8] . For each pair, we compute layer-wise similarity and report the maximum across layers, as in the original work. We evaluate both global spectral metrics ( CKA linear/RBF) and local neighborhood metrics ( mKNN , cycle- k k NN, CKNNA). Following Huh et al. (2024) , we evaluate mKNN , cycle- k k NN, and CKNNA with k = 10 k=10 . We further apply Benjamini-Hochberg FDR correction ( Benjamini and Hochberg, 1995 ) to control for multiple comparisons across model pairs.

For the global similarity, we find that uncalibrated CKA scores increase with model scale (dotted lines in Figure 5 a), reproducing the trend interpreted as evidence of cross-modal convergence ( Huh et al., 2024 ) . However, this trend disappears after our calibration (solid lines): calibrated CKA shows no systematic increase with model size. This indicates that global convergence in uncalibrated CKA is largely attributable to width and depth confounders rather than a genuine increase in representational similarity. The same holds for the other global metrics, including shape- and geometry-based ones: SVCCA , the RV coefficient, and Procrustes distance all lose their apparent scaling trend after calibration ( Section E.8 ).

In contrast, for the local similarity, evidence of cross-modal convergence remains strong for neighborhood-based metrics even under our calibration ( Figure 5 b). The same qualitative conclusion holds for other neighborhood-based measures (cycle- k k NN and CKNNA; Section E.8 ) and different choices of α \alpha ( Section E.11 ). Further analysis ( Section E.10 ) reveals that models converge in local neighborhood structure: models increasingly agree on which points are neighbors, but do not agree on the pairwise distances, since CKA-RBF with a small bandwidth shows no alignment after calibration.

CKA and mKNN capture different invariances, so their raw magnitudes are not directly comparable. We therefore compare, for each metric separately, how strongly its score tracks language-model capability before and after calibration (its Pearson correlation with the model ranking). After calibration this correlation collapses for global metrics (for linear CKA it falls from 0.86 0.86 to 0.45 0.45 , and for Procrustes distance from 0.89 0.89 to 0.39 0.39 ) but is essentially unchanged for local ones ( mKNN stays near 0.85 0.85 and CKNNA near 0.87 0.87 ). Section E.8 reports all metrics.

To test whether these findings generalize beyond images and text, we extend our analysis to video–language alignment following Zhu et al. (2026) . We compare video encoders (VideoMAE small/base/large/huge, fine-tuned on Kinetics) against the same language model families. Consistent with our previous findings, the global similarity ( CKA ) shows no trend with model capacity ( Figure 7 ). In contrast, for local similarity ( mKNN ), a clear scaling trend emerges with VideoMAE-Large/Huge, whereas smaller video encoders appear to act as a bottleneck, limiting alignment regardless of language model size. This confirms that local neighborhood convergence extends to video–language alignment, provided that representations are sufficiently powerful. Section E.9 further compares non-finetuned VideoMAE versions and a variety of image models at the frame level on the same dataset, showing the same trend.

Taken together, these results suggest a refined version of the Platonic Representation Hypothesis. After calibration, we find little evidence that representations converge in global spectral structure as models scale, at least under the considered setting. What reliably persists is local geometric alignment: different models preserve similar neighborhood relationships among inputs. We therefore propose the alternative Aristotelian Representation Hypothesis : As models become capable, their representations converge to shared local neighborhood relationships .

## 7 Conclusion

Representational similarity metrics are widely used to study learned features, but their interpretation is systematically distorted by two artifacts: width-dependent null baselines and depth-dependent selection inflation. We introduced a unified null-calibration framework that corrects both, turning similarity scores into effect sizes with principled zero points and valid p p -values. Applying our framework to the Platonic Representation Hypothesis reveals that previously reported global spectral convergence is largely confounded by width and depth, whereas local neighborhood alignment remains significant, motivating an Aristotelian Representation Hypothesis.

##### Relationship to the Platonic hypothesis.

The Aristotelian hypothesis refines rather than refutes the Platonic one. Global convergence implies local convergence, because matching the full geometry preserves neighborhoods, but the converse does not hold. The Platonic hypothesis therefore implies the Aristotelian one, which is a weaker criterion. Our experiments support this local form and, after calibration, find little evidence for the global one. Prior reports of convergence thus remain compatible with our analysis, and the Aristotelian hypothesis offers a more precise lens on what converges across models and modalities.

##### Limitations and outlook.

Our conclusions come with two caveats. First, representational similarity has no ground-truth scale, so we report the presence or absence of calibrated evidence for convergence rather than proving it. Second, our guarantees assume exchangeability, so grouped or clustered samples require restricted permutations that preserve their dependence structure. Why representations converge in local neighborhoods but not in global geometry remains the key open question.

## Acknowledgements

We thank Artyom Gadetsky, Siba Smarak Panigrahi, Debajyoti Dasgupta, David Frühbuss, Shin Matsushima, Rishubh Singh, Adriana Moreno Castan, and Gioele La Manno for their valuable suggestions, which helped improve the manuscript. We are especially grateful to Simone Lionetti for additional input and support. We gratefully acknowledge the support of the Swiss National Science Foundation (SNSF) starting grant TMSGI2_226252/1, SNSF grant IC00I0_231922, SNSF grant 10.004.411, and the Swiss AI Initiative Large Call #32. M.B. is a CIFAR Fellow in the Multiscale Human Program.

## Impact statement

This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.

## References

Aggarwal et al. (2001) C. C. Aggarwal, A. Hinneburg, and D. A. Keim On the surprising behavior of distance metrics in high dimensional space . In International Conference on Database Theory , Cited by: §2 .

Aristotle (ca. 350 B.C.E) Aristotle Categories . Cited by: §1 .

Benjamini and Hochberg (1995) Y. Benjamini and Y. Hochberg Controlling the false discovery rate: a practical and powerful approach to multiple testing . Journal of the Royal Statistical Society: Series B (Methodological) . Cited by: §4.2 , §5.2 , §6.3 .

Beyer et al. (1999) K. Beyer, J. Goldstein, R. Ramakrishnan, and U. Shaft When is “nearest neighbor” meaningful? . In International Conference on Database Theory , Cited by: §2 .

Bo et al. (2024) Y. Bo, A. Soni, S. Srivastava, and M. Khosla Evaluating representational similarity measures from the lens of functional correspondence . arXiv preprint arXiv:2411.14633 . Cited by: §2 .

Bolya et al. (2025) D. Bolya, P. Huang, P. Sun, J. H. Cho, A. Madotto, C. Wei, T. Ma, J. Zhi, J. Rajasegaran, H. A. Rasheed, J. Wang, M. Monteiro, H. Xu, S. Dong, N. Ravi, S. Li, P. Dollar, and C. Feichtenhofer Perception Encoder: The best visual embeddings are not at the output of the network . Advances in Neural Information Processing Systems . Cited by: §E.9 .

Bonferroni (1936) C. Bonferroni Teoria statistica delle classi e calcolo delle probabilità . Pubblicazioni del R Istituto Superiore di Scienze Economiche e Commerciali di Firenze . Cited by: §4.2 .

Cai et al. (2019) M. B. Cai, N. W. Schuck, J. W. Pillow, and Y. Niv Representational structure or task structure? Bias in neural representational similarity analysis and a Bayesian method for reducing bias . PLoS Computational Biology . Cited by: Table 1 .

Cho et al. (2025) J. H. Cho, A. Madotto, E. Mavroudi, T. Afouras, T. Nagarajan, M. Maaz, Y. Song, T. Ma, S. Hu, S. Jain, M. Martin, H. Wang, H. A. Rasheed, P. Sun, P. Huang, D. Bolya, N. Ravi, S. Jain, T. Stark, S. Moon, B. Damavandi, V. Lee, A. Westbury, S. Khan, P. Kraehenbuehl, P. Dollar, L. Torresani, K. Grauman, and C. Feichtenhofer PerceptionLM: Open-Access Data and Models for Detailed Visual Understanding . Advances in Neural Information Processing Systems . Cited by: §E.9 .

Chun et al. (2025) C. Chun, A. Canatar, S. Chung, and D. D. Lee Estimating Neural Representation Alignment from Sparsely Sampled Inputs and Features . arXiv preprint arXiv:2502.15104 . Cited by: Table 1 , §E.4 , §2 .

Cramér (1999) H. Cramér Mathematical methods of statistics . Cited by: §C.5 .

Cui et al. (2022) T. Cui, Y. Kumar, P. Marttinen, and S. Kaski Deconfounded representation similarity for comparison of neural networks . Advances in Neural Information Processing Systems . Cited by: Table 1 , §2 .

Diedrichsen et al. (2021) J. Diedrichsen, E. Berlot, M. Mur, H. H. Schütt, M. Shahbazi, and N. Kriegeskorte Comparing representational geometries using whitened unbiased-distance-matrix similarity . Neurons, Behavior, Data Analysis, and Theory . Cited by: Table 1 .

Ding et al. (2021) F. Ding, J. Denain, and J. Steinhardt Grounding representation similarity through statistical testing . Advances in Neural Information Processing Systems . Cited by: §2 .

Embrechts et al. (2013) P. Embrechts, C. Klüppelberg, and T. Mikosch Modelling Extremal Events: for Insurance and Finance . Stochastic Modelling and Applied Probability . Cited by: §C.5 .

Good (2005) P. Good Permutation, parametric and bootstrap tests of hypotheses . Cited by: §5.1 .

Gröger et al. (2025) F. Gröger, S. Wen, H. Le, and M. Brbic With limited data for multimodal alignment, let the STRUCTURE guide you . Advances in Neural Information Processing Systems . Cited by: §1 .

Harvey et al. (2024) S. E. Harvey, D. Lipshutz, and A. H. Williams What Representational Similarity Measures Imply about Decodable Information . In Proceedings of UniReps: the Second Edition of the Workshop on Unifying Representations in Neural Models , Cited by: §2 .

Holm (1979) S. Holm A simple sequentially rejective multiple test procedure . Scandinavian Journal of Statistics . Cited by: §5.2 .

Hotelling (1992) H. Hotelling Relations between two sets of variates . In Breakthroughs in Statistics: Methodology and Distribution , Cited by: §2 .

Huh et al. (2024) M. Huh, B. Cheung, T. Wang, and P. Isola Position: The platonic representation hypothesis . In International Conference on Machine Learning , Cited by: §B.2.3 , §B.2.3 , §B.2.3 , §B.2 , §E.8 , §E.8 , §1 , §1 , §1 , §2 , §2 , §4.2 , Figure 5 , Figure 5 , §6.3 , §6.3 .

Kapoor et al. (2025) C. Kapoor, S. Srivastava, and M. Khosla Bridging Critical Gaps in Convergent Learning: How Representational Alignment Evolves Across Layers, Training, and Distribution Shifts . Advances in Neural Information Processing Systems . Cited by: §1 .

Klabunde et al. (2025a) M. Klabunde, T. Schumacher, M. Strohmaier, and F. Lemmerich Similarity of neural network models: A survey of functional and representational measures . ACM Computing Surveys . Cited by: §2 .

Klabunde et al. (2025b) M. Klabunde, T. Wald, T. Schumacher, K. Maier-Hein, M. Strohmaier, and F. Lemmerich ReSi: A Comprehensive Benchmark for Representational Similarity Measures . In International Conference on Learning Representations , Cited by: §2 .

Kornblith et al. (2019) S. Kornblith, M. Norouzi, H. Lee, and G. Hinton Similarity of neural network representations revisited . In International Conference on Machine Learning , Cited by: §B.2.1 , §B.2.1 , §B.2.1 , §B.2 , §1 , §1 , §2 , §4.2 .

Kriegeskorte et al. (2008) N. Kriegeskorte, M. Mur, and P. A. Bandettini Representational similarity analysis–connecting the branches of systems neuroscience . Frontiers in Systems Neuroscience . Cited by: §B.2.2 , §B.2 , §1 , §2 .

Lehmann and Romano (2005) E. L. Lehmann and J. P. Romano Testing statistical hypotheses . Cited by: Proposition C.3 .

Livan et al. (2018) G. Livan, M. Novaes, and P. Vivo Introduction to Random Matrices: Theory and Practice . SpringerBriefs in Mathematical Physics . Cited by: §4.1 .

Maniparambil et al. (2024) M. Maniparambil, R. Akshulakov, Y. A. D. Djilali, M. El Amine Seddik, S. Narayan, K. Mangalam, and N. E. O’Connor Do Vision and Language Encoders Represent the World Similarly? . In Conference on Computer Vision and Pattern Recognition , Cited by: §1 , §1 .

Marcos-Manchón and Fuentemilla (2025) P. Marcos-Manchón and L. Fuentemilla Convergent transformations of visual representation in brains and models . arXiv preprint arXiv:2507.13941 . Cited by: §2 .

Morcos et al. (2018) A. Morcos, M. Raghu, and S. Bengio Insights on representational similarity in neural networks with canonical correlation . Advances in Neural Information Processing Systems . Cited by: §B.2.1 , §B.2.1 , §B.2.1 , §2 .

Müller (2002) R. R. Müller A random matrix model of communication via antenna arrays . IEEE Transactions on information theory . Cited by: §4.1 .

Murphy et al. (2024) A. Murphy, J. Zylberberg, and A. Fyshe Correcting biased centered kernel alignment measures in biological and artificial neural networks . arXiv preprint arXiv:2405.01012 . Cited by: Table 1 , §E.4 , §2 , §6.1 .

Neyshabur et al. (2020) B. Neyshabur, H. Sedghi, and C. Zhang What is being transferred in transfer learning? . Advances in Neural Information Processing Systems . Cited by: §1 .

Nguyen et al. (2021) T. Nguyen, M. Raghu, and S. Kornblith Do Wide and Deep Networks Learn the Same Things? Uncovering How Neural Network Representations Vary with Width and Depth . In International Conference on Learning Representations , Cited by: §1 .

Nichols and Holmes (2002) T. E. Nichols and A. P. Holmes Nonparametric permutation tests for functional neuroimaging: a primer with examples . Human Brain Mapping . Cited by: §2 , §5.1 .

Phipson and Smyth (2010) B. Phipson and G. K. Smyth Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn. . Statistical Applications in Genetics & Molecular Biology . Cited by: §C.1 , §5.1 .

Raghu et al. (2017) M. Raghu, J. Gilmer, J. Yosinski, and J. Sohl-Dickstein SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability . In Advances in Neural Information Processing Systems , Cited by: §B.2.1 , §B.2.1 , §1 , §1 , §2 , §4.2 .

Raugel et al. (2025) J. Raugel, M. Szafraniec, H. V. Vo, C. Couprie, P. Labatut, P. Bojanowski, V. Wyart, and J. King Disentangling the factors of convergence between brains and computer vision models . arXiv preprint arXiv:2508.18226 . Cited by: §2 .

Robert and Escoufier (1976) P. Robert and Y. Escoufier A unifying tool for linear multivariate statistical methods: the RV-coefficient . Journal of the Royal Statistical Society: Series C (Applied Statistics) . Cited by: §B.2.1 .

Schaeffer et al. (2024) R. Schaeffer, M. Khona, S. Chandra, M. Ostrow, B. Miranda, and S. Koyejo Position: Maximizing Neural Regression Scores May Not Identify Good Models of the Brain . In NeurIPS 2024 Workshop on Unifying Representations in Neural Models (UniReps) , Cited by: §2 .

Schrimpf et al. (2018) M. Schrimpf, J. Kubilius, H. Hong, N. J. Majaj, R. Rajalingham, E. B. Issa, K. Kar, P. Bashivan, J. Prescott-Roy, F. Geiger, et al. Brain-score: Which artificial neural network for object recognition is most brain-like? . BioRxiv . Cited by: §1 , §1 , §4.2 .

Smilde et al. (2009) A. K. Smilde, H. A. Kiers, S. Bijlsma, C. Rubingh, and M. Van Erk Matrix correlations for high-dimensional data: the modified RV-coefficient . Bioinformatics . Cited by: Table 1 , §B.2.1 .

Song et al. (2012) L. Song, A. Smola, A. Gretton, J. Bedo, and K. Borgwardt Feature Selection via Dependence Maximization . Journal of Machine Learning Research . Cited by: §B.2.1 , §E.4 .

Soni et al. (2024) A. Soni, S. Srivastava, K. Kording, and M. Khosla Conclusions about Neural Network to Brain Alignment are Profoundly Impacted by the Similarity Measure . bioRxiv . Cited by: §2 .

Srinivasan et al. (2021) K. Srinivasan, K. Raman, J. Chen, M. Bendersky, and M. Najork Wit: Wikipedia-based image text dataset for multimodal multilingual machine learning . In International ACM SIGIR Conference on Research and Development in Information Retrieval , Cited by: §6.3 .

Tjandrasuwita et al. (2025) M. Tjandrasuwita, C. Ekbote, L. Ziyin, and P. P. Liang Understanding the Emergence of Multimodal Representation Alignment . In International Conference on Machine Learning , Cited by: §1 , §1 .

Tong et al. (2022) Z. Tong, Y. Song, J. Wang, and L. Wang VideoMAE: Masked autoencoders are data-efficient learners for self-supervised video pre-training . Advances in Neural Information Processing Systems . Cited by: §E.9 .

Wachter (1978) K. W. Wachter The strong limits of random matrix spectra for sample matrices of independent elements . The Annals of Probability . Cited by: §4.1 .

Weenink (2003) D. Weenink Canonical correlation analysis . Proceedings of the Institute of Phonetic Sciences of the University of Amsterdam . Cited by: §B.2.1 , §1 .

Westfall and Young (1993) P. H. Westfall and S. S. Young Resampling-based multiple testing: Examples and methods for p-value adjustment . Cited by: §2 , §5.2 .

Williams et al. (2021) A. H. Williams, E. Kunz, S. Kornblith, and S. W. Linderman Generalized Shape Metrics on Neural Representations . In Advances in Neural Information Processing Systems , Cited by: §B.2.2 , §2 .

Zhu et al. (2026) T. Zhu, T. Han, L. Guibas, V. Pătrăucean, and M. Ovsjanikov Dynamic Reflections: Probing Video Representations with Text Alignment . In International Conference on Learning Representations , Cited by: §E.9 , §1 , §2 , §6.3 .

## Appendix A Existing calibration approaches for representational similarity metrics

## Appendix B Metrics and score definitions

This appendix gives the definitions of the similarity metrics s ⁡ ( 𝐗 , 𝐘 ) s(\mathbf{X},\mathbf{Y}) used throughout the paper. The main text focuses on the calibration procedure ( Sections 5.1 and 5.2 ). Here we provide concrete instantiations of the metrics referenced in Section 3 and Section 6 .

### B.1 Preprocessing and basic notation

Let 𝐗 ∈ ℝ n × d x \mathbf{X}\in\mathbb{R}^{n\times d_{x}} and 𝐘 ∈ ℝ n × d y \mathbf{Y}\in\mathbb{R}^{n\times d_{y}} denote row-aligned representations evaluated on the same n n inputs. We use the centering matrix 𝐇 = 𝐈 n − 1 n ​ 𝟙 n ​ 𝟙 n ⊤ , \mathbf{H}\;=\;\mathbf{I}_{n}-\frac{1}{n}\mathbbm{1}_{n}\mathbbm{1}_{n}^{\top}, (18) where 𝐈 n ∈ ℝ n × n \mathbf{I}_{n}\in\mathbb{R}^{n\times n} is the identity matrix and 𝟙 n ∈ ℝ n \mathbbm{1}_{n}\in\mathbb{R}^{n} is the all-ones vector. We define row-centered representations 𝐗 c = 𝐇𝐗 \mathbf{X}_{c}=\mathbf{H}\mathbf{X} and 𝐘 c = 𝐇𝐘 \mathbf{Y}_{c}=\mathbf{H}\mathbf{Y} . Unless stated otherwise, similarities are computed on centered representations.

### B.2 Raw similarity metrics

This section provides formal definitions of the similarity metrics used throughout the paper. In the main text, we primarily use CKA (linear and RBF kernel) ( Kornblith et al., 2019 ) , RSA ( Kriegeskorte et al., 2008 ) , and mutual k k -NN ( Huh et al., 2024 ) as representative metrics from the spectral, geometric, and neighborhood families, respectively. Additional metrics (SVCCA, PWCCA, cycle- k k NN, CKNNA, RV coefficient, Procrustes) are included for completeness and used in supplementary experiments.

#### B.2.1 Spectral metrics

##### Linear Centered Kernel Alignment (CKA) .

Linear CKA ( Kornblith et al., 2019 ) can be written as a normalized Frobenius energy of the sample cross-covariance operator. With 𝐗 c , 𝐘 c \mathbf{X}_{c},\mathbf{Y}_{c} as above, define the sample (cross-)covariances 𝚺 ~ X ​ X := 1 n − 1 ​ 𝐗 c ⊤ ​ 𝐗 c , 𝚺 ~ Y ​ Y := 1 n − 1 ​ 𝐘 c ⊤ ​ 𝐘 c , 𝐂 ~ := 𝚺 ~ X ​ Y := 1 n − 1 ​ 𝐗 c ⊤ ​ 𝐘 c . \widetilde{\mathbf{\Sigma}}_{XX}:=\frac{1}{n-1}\mathbf{X}_{c}^{\top}\mathbf{X}_{c},\qquad\widetilde{\mathbf{\Sigma}}_{YY}:=\frac{1}{n-1}\mathbf{Y}_{c}^{\top}\mathbf{Y}_{c},\qquad\widetilde{\mathbf{C}}:=\widetilde{\mathbf{\Sigma}}_{XY}:=\frac{1}{n-1}\mathbf{X}_{c}^{\top}\mathbf{Y}_{c}. (19) The biased linear Hilbert-Schmidt Independence Criterion (HSIC) energy equals ‖ 𝐂 ~ ‖ F 2 \|\widetilde{\mathbf{C}}\|_{F}^{2} . The commonly used linear CKA normalization can be written as CKA lin ​ ( 𝐗 , 𝐘 ) = ‖ 𝐂 ~ ‖ F 2 ‖ 𝚺 ~ X ​ X ‖ F ​ ‖ 𝚺 ~ Y ​ Y ‖ F = ‖ 𝐗 c ⊤ ​ 𝐘 c ‖ F 2 ‖ 𝐗 c ⊤ ​ 𝐗 c ‖ F ​ ‖ 𝐘 c ⊤ ​ 𝐘 c ‖ F ∈ [ 0 , 1 ] , \mathrm{CKA}_{\mathrm{lin}}(\mathbf{X},\mathbf{Y})\;=\;\frac{\|\widetilde{\mathbf{C}}\|_{F}^{2}}{\|\widetilde{\mathbf{\Sigma}}_{XX}\|_{F}\,\|\widetilde{\mathbf{\Sigma}}_{YY}\|_{F}}\;=\;\frac{\|\mathbf{X}_{c}^{\top}\mathbf{Y}_{c}\|_{F}^{2}}{\|\mathbf{X}_{c}^{\top}\mathbf{X}_{c}\|_{F}\,\|\mathbf{Y}_{c}^{\top}\mathbf{Y}_{c}\|_{F}}\;\in\;[0,1], (20) where the second equality follows by cancellation of common 1 / ( n − 1 ) 1/(n-1) factors. What it measures: linear CKA treats two representations as similar when pairs of points with high inner product in one space also have high inner product in the other, i.e. , when their global second-order geometry agrees. It is invariant to rotations and isotropic rescaling, but not to general invertible linear maps.

##### Kernel Centered Kernel Alignment .

Kernel CKA ( Kornblith et al., 2019 ) generalizes linear CKA by replacing dot products with kernel functions. Let k X : ℝ d x × ℝ d x → ℝ k_{X}:\mathbb{R}^{d_{x}}\times\mathbb{R}^{d_{x}}\to\mathbb{R} and k Y : ℝ d y × ℝ d y → ℝ k_{Y}:\mathbb{R}^{d_{y}}\times\mathbb{R}^{d_{y}}\to\mathbb{R} be positive semidefinite kernel functions ( e.g. , RBF kernel k X ( 𝐱 , 𝐱 ′ ) = exp ( − ∥ 𝐱 − 𝐱 ′ ∥ 2 / 2 σ 2 ) k_{X}(\mathbf{x},\mathbf{x}^{\prime})=\exp(-\|\mathbf{x}-\mathbf{x}^{\prime}\|^{2}/2\sigma^{2}) ). Let 𝐊 X ∈ ℝ n × n \mathbf{K}_{X}\in\mathbb{R}^{n\times n} and 𝐊 Y ∈ ℝ n × n \mathbf{K}_{Y}\in\mathbb{R}^{n\times n} be Gram matrices with entries ( 𝐊 X ) i ​ j = k X ​ ( 𝐱 i , 𝐱 j ) (\mathbf{K}_{X})_{ij}=k_{X}(\mathbf{x}_{i},\mathbf{x}_{j}) and ( 𝐊 Y ) i ​ j = k Y ​ ( 𝐲 i , 𝐲 j ) (\mathbf{K}_{Y})_{ij}=k_{Y}(\mathbf{y}_{i},\mathbf{y}_{j}) . Let 𝐊 ~ X = 𝐇𝐊 X ​ 𝐇 \widetilde{\mathbf{K}}_{X}=\mathbf{H}\mathbf{K}_{X}\mathbf{H} and 𝐊 ~ Y = 𝐇𝐊 Y ​ 𝐇 \widetilde{\mathbf{K}}_{Y}=\mathbf{H}\mathbf{K}_{Y}\mathbf{H} denote centered Gram matrices. Kernel CKA is defined as: CKA k X , k Y ​ ( 𝐗 , 𝐘 ) = ⟨ 𝐊 ~ X , 𝐊 ~ Y ⟩ F ‖ 𝐊 ~ X ‖ F ​ ‖ 𝐊 ~ Y ‖ F . \mathrm{CKA}_{k_{X},k_{Y}}(\mathbf{X},\mathbf{Y})\;=\;\frac{\langle\widetilde{\mathbf{K}}_{X},\widetilde{\mathbf{K}}_{Y}\rangle_{F}}{\|\widetilde{\mathbf{K}}_{X}\|_{F}\,\|\widetilde{\mathbf{K}}_{Y}\|_{F}}. (21) where ⟨ A , B ⟩ F = tr ⁡ ( A ⊤ ​ B ) \langle A,B\rangle_{F}=\mathrm{tr}(A^{\top}B) . With positive semidefinite kernels and the biased HSIC estimator, the numerator is nonnegative, and kernel CKA typically lies in [ 0 , 1 ] [0,1] . What it measures: kernel CKA treats representations as similar when their kernel-induced similarity patterns over points agree. With an RBF kernel of small bandwidth, this emphasizes local, nonlinear similarity structure rather than global linear geometry.

##### Unbiased Centered Kernel Alignment .

The biased HSIC estimator can yield inflated similarity scores at finite sample sizes. Song et al. (2012) derived an unbiased HSIC estimator by recognizing that HSIC can be formulated as a U-statistic. Following Kornblith et al. (2019) , we substitute the unbiased estimator into the CKA formula. Let 𝐊 ̊ X \mathring{\mathbf{K}}_{X} denote the Gram matrix 𝐊 X \mathbf{K}_{X} with its diagonal entries set to zero (and likewise 𝐊 ̊ Y \mathring{\mathbf{K}}_{Y} ). The unbiased HSIC estimator is: HSIC u ​ ( 𝐊 X , 𝐊 Y ) = 1 n ⁡ ( n − 3 ) ​ ( tr ⁡ ( 𝐊 ̊ X ​ 𝐊 ̊ Y ) + 𝟏 ⊤ ​ 𝐊 ̊ X ​ 𝟏 ⋅ 𝟏 ⊤ ​ 𝐊 ̊ Y ​ 𝟏 ( n − 1 ) ​ ( n − 2 ) − 2 n − 2 ​ 𝟏 ⊤ ​ 𝐊 ̊ X ​ 𝐊 ̊ Y ​ 𝟏 ) . \mathrm{HSIC}_{u}(\mathbf{K}_{X},\mathbf{K}_{Y})=\frac{1}{n(n-3)}\left(\mathrm{tr}(\mathring{\mathbf{K}}_{X}\mathring{\mathbf{K}}_{Y})+\frac{\mathbf{1}^{\top}\mathring{\mathbf{K}}_{X}\mathbf{1}\cdot\mathbf{1}^{\top}\mathring{\mathbf{K}}_{Y}\mathbf{1}}{(n-1)(n-2)}-\frac{2}{n-2}\mathbf{1}^{\top}\mathring{\mathbf{K}}_{X}\mathring{\mathbf{K}}_{Y}\mathbf{1}\right). (22) Unbiased CKA replaces both numerator and denominator of Equation 21 with this estimator. Unlike the biased version, unbiased CKA can take small negative values at finite n n . What it measures: the same agreement of similarity patterns as kernel CKA , but with the finite-sample inflation of HSIC removed, so a value near zero indicates no more agreement than expected by chance.

##### Canonical Correlation Analysis (CCA) -based similarity.

CCA ( Weenink, 2003 ) measures linear subspace alignment. The sample canonical correlations { ρ i } i = 1 r \{\rho_{i}\}_{i=1}^{r} (with r = rank ⁡ ( 𝚺 ~ X ​ Y ) r=\mathrm{rank}(\widetilde{\mathbf{\Sigma}}_{XY}) ) are the singular values of the whitened cross-covariance operator 𝐓 ~ CCA = 𝚺 ~ X ​ X − 1 2 ​ 𝚺 ~ X ​ Y ​ 𝚺 ~ Y ​ Y − 1 2 . \widetilde{\mathbf{T}}_{\mathrm{CCA}}\;=\;\widetilde{\mathbf{\Sigma}}_{XX}^{-\tfrac{1}{2}}\,\widetilde{\mathbf{\Sigma}}_{XY}\,\widetilde{\mathbf{\Sigma}}_{YY}^{-\tfrac{1}{2}}. (23) Common scalar summaries include the mean canonical correlation 1 r ​ ∑ i = 1 r ρ i \frac{1}{r}\sum_{i=1}^{r}\rho_{i} or a weighted average as used in SVCCA ( Raghu et al., 2017 ) and PWCCA ( Morcos et al., 2018 ) . What it measures: CCA treats two representations as similar when one can be mapped onto the other by an invertible linear transformation, i.e. , when they span the same linear subspace. It ignores rotations, scaling, and other invertible linear changes within each space.

##### Singular Vector Canonical Correlation Analysis (SVCCA) .

SVCCA ( Raghu et al., 2017 ) combines dimensionality reduction via singular value decomposition (SVD) with CCA . First, truncated SVD is applied to each representation to retain the top principal components, yielding 𝐗 ′ ∈ ℝ n × p \mathbf{X}^{\prime}\in\mathbb{R}^{n\times p} and 𝐘 ′ ∈ ℝ n × q \mathbf{Y}^{\prime}\in\mathbb{R}^{n\times q} . Then CCA is applied to the reduced representations, yielding canonical correlations { ρ i } i = 1 r \{\rho_{i}\}_{i=1}^{r} . The SVCCA similarity is the mean canonical correlation: SVCCA ⁡ ( 𝐗 , 𝐘 ) = 1 r ​ ∑ i = 1 r ρ i . \mathrm{SVCCA}(\mathbf{X},\mathbf{Y})=\frac{1}{r}\sum_{i=1}^{r}\rho_{i}. (24) What it measures: SVCCA treats representations as similar when their high-variance subspaces are linearly aligned, discarding low-variance (noise) directions before measuring linear correspondence.

##### Projection Weighted Canonical Correlation Analysis (PWCCA) .

PWCCA ( Morcos et al., 2018 ) improves upon SVCCA by weighting canonical correlations according to their importance in explaining the original representations. Let 𝐡 i X \mathbf{h}_{i}^{X} and 𝐡 i Y \mathbf{h}_{i}^{Y} denote the i i -th canonical variables (projections onto canonical directions). The weight for the i i -th canonical correlation is the overall magnitude of the corresponding canonical variable across the dataset: α i = ∑ m = 1 n | ( 𝐡 i X ) m | = ∥ 𝐡 i X ∥ 1 , \alpha_{i}=\sum_{m=1}^{n}\left|(\mathbf{h}_{i}^{X})_{m}\right|=\lVert\mathbf{h}_{i}^{X}\rVert_{1}, (25) the ℓ 1 \ell_{1} norm of the i i -th canonical variable over the n n samples, following the reference implementation of Morcos et al. (2018) . The PWCCA similarity is the weighted mean: PWCCA ⁡ ( 𝐗 , 𝐘 ) = ∑ i = 1 r α i ​ ρ i ∑ i = 1 r α i . \mathrm{PWCCA}(\mathbf{X},\mathbf{Y})=\frac{\sum_{i=1}^{r}\alpha_{i}\rho_{i}}{\sum_{i=1}^{r}\alpha_{i}}. (26) This weighting ensures that canonical correlations corresponding to principal directions receive higher weight than those corresponding to noise dimensions. What it measures: like CCA , PWCCA treats representations as similar when they linearly correspond, but it counts agreement along high-variance directions more, so two representations are similar when their dominant directions align.

##### RV coefficient.

The RV (“Relation between two sets of Variables”) coefficient ( Robert and Escoufier, 1976 ; Smilde et al., 2009 ) is a multivariate generalization of the squared Pearson correlation. It measures the similarity between two configuration matrices via their inner-product (Gram) matrices. Let 𝐖 X = 𝐗 c ​ 𝐗 c ⊤ \mathbf{W}_{X}=\mathbf{X}_{c}\mathbf{X}_{c}^{\top} and 𝐖 Y = 𝐘 c ​ 𝐘 c ⊤ \mathbf{W}_{Y}=\mathbf{Y}_{c}\mathbf{Y}_{c}^{\top} be the inner-product (Gram) matrices of the centered representations 𝐗 c , 𝐘 c \mathbf{X}_{c},\mathbf{Y}_{c} . The RV coefficient is: RV ⁡ ( 𝐗 , 𝐘 ) = tr ⁡ ( 𝐖 X ​ 𝐖 Y ) tr ⁡ ( 𝐖 X 2 ) ​ tr ​ ( 𝐖 Y 2 ) ∈ [ 0 , 1 ] . \mathrm{RV}(\mathbf{X},\mathbf{Y})=\frac{\mathrm{tr}(\mathbf{W}_{X}\mathbf{W}_{Y})}{\sqrt{\mathrm{tr}(\mathbf{W}_{X}^{2})\ \mathrm{tr}(\mathbf{W}_{Y}^{2})}}\;\in\;[0,1]. (27) What it measures: the RV coefficient treats representations as similar when their point-by-point inner-product (Gram) matrices match. Like linear CKA , it captures global second-order geometry and is invariant to rotation but sensitive to scaling. Computed on centered representations (our default convention), the RV coefficient coincides exactly with linear CKA ; we list it separately as it arises from a different historical motivation and include it for completeness.

#### B.2.2 Geometric metrics

##### Representational Similarity Analysis (RSA) via Spearman correlation of dissimilarity matrices.

RSA ( Kriegeskorte et al., 2008 ) compares the geometry induced by pairwise dissimilarities. Let δ ⁡ ( ⋅ , ⋅ ) \delta(\cdot,\cdot) be a dissimilarity on representation vectors ( e.g. , correlation distance δ ⁡ ( 𝐮 , 𝐯 ) = 1 − corr ⁡ ( 𝐮 , 𝐯 ) \delta(\mathbf{u},\mathbf{v})=1-\mathrm{corr}(\mathbf{u},\mathbf{v}) , cosine distance). Define Representational Dissimilarity Matrices (RDMs) ( 𝐃 X ) i ​ j = δ ⁡ ( 𝐱 i , 𝐱 j ) , ( 𝐃 Y ) i ​ j = δ ⁡ ( 𝐲 i , 𝐲 j ) , (\mathbf{D}_{X})_{ij}=\delta(\mathbf{x}_{i},\mathbf{x}_{j}),\qquad(\mathbf{D}_{Y})_{ij}=\delta(\mathbf{y}_{i},\mathbf{y}_{j}), (28) and let vec △ ​ ( 𝐃 ) ∈ ℝ n ⁡ ( n − 1 ) / 2 \mathrm{vec}_{\triangle}(\mathbf{D})\in\mathbb{R}^{n(n-1)/2} denote vectorization of the strict upper triangle. RSA is then computed as a rank correlation between the two RDM vectors: RSA ⁡ ( 𝐗 , 𝐘 ) = ρ S ​ ( vec △ ​ ( 𝐃 X ) , vec △ ​ ( 𝐃 Y ) ) , \mathrm{RSA}(\mathbf{X},\mathbf{Y})\;=\;\rho_{S}\!\left(\mathrm{vec}_{\triangle}(\mathbf{D}_{X}),\;\mathrm{vec}_{\triangle}(\mathbf{D}_{Y})\right), (29) where Spearman’s ρ \rho can be expressed as Pearson correlation of ranks, ρ S ​ ( 𝐮 , 𝐯 ) = corr ⁡ ( rank ⁡ ( 𝐮 ) , rank ⁡ ( 𝐯 ) ) . \rho_{S}(\mathbf{u},\mathbf{v})\;=\;\mathrm{corr}\!\left(\mathrm{rank}(\mathbf{u}),\;\mathrm{rank}(\mathbf{v})\right). (30) What it measures: RSA treats two representations as similar when they rank pairs of points in the same order of (dis)similarity. It compares the relational geometry of distances rather than the coordinates, and depends only on the pattern of pairwise dissimilarities.

##### Procrustes distance.

The orthogonal Procrustes distance ( Williams et al., 2021 ) measures the minimal Euclidean distance between two representations after optimal orthogonal alignment. Assuming d x = d y = d d_{x}=d_{y}=d , the optimal orthogonal matrix 𝐐 ∗ ∈ 𝒪 ⁡ ( d ) \mathbf{Q}^{*}\in\mathcal{O}(d) is: 𝐐 ∗ = argmin 𝐐 ∈ 𝒪 ⁡ ( d ) ‖ 𝐗 − 𝐘𝐐 ‖ F 2 , \mathbf{Q}^{*}=\operatorname*{argmin}_{\mathbf{Q}\in\mathcal{O}(d)}\|\mathbf{X}-\mathbf{Y}\mathbf{Q}\|_{F}^{2}, (31) which has the closed-form solution 𝐐 ∗ = 𝐕𝐔 ⊤ \mathbf{Q}^{*}=\mathbf{V}\mathbf{U}^{\top} where 𝐔 ​ 𝚺 ​ 𝐕 ⊤ = 𝐗 ⊤ ​ 𝐘 \mathbf{U}\mathbf{\Sigma}\mathbf{V}^{\top}=\mathbf{X}^{\top}\mathbf{Y} is the SVD. The Procrustes distance is: d Proc ​ ( 𝐗 , 𝐘 ) = ‖ 𝐗 − 𝐘𝐐 ∗ ‖ F . d_{\mathrm{Proc}}(\mathbf{X},\mathbf{Y})=\|\mathbf{X}-\mathbf{Y}\mathbf{Q}^{*}\|_{F}. (32) We convert this distance to a similarity score s Proc = 1 − d Proc / ‖ 𝐘 c ‖ F s_{\mathrm{Proc}}=1-d_{\mathrm{Proc}}/\|\mathbf{Y}_{c}\|_{F} , evaluated on centered representations, where 𝐘 c \mathbf{Y}_{c} denotes the centered 𝐘 \mathbf{Y} . It equals 1 1 at perfect orthogonal alignment ( d Proc = 0 d_{\mathrm{Proc}}=0 ) and can be negative for poorly aligned pairs. What it measures: Procrustes treats two representations as similar when one can be rotated and reflected onto the other with small residual. It compares absolute geometry up to rigid motion and, unlike neighborhood metrics, is sensitive to the actual pairwise distances.

#### B.2.3 Neighborhood metrics

##### Mutual k k -Nearest Neighbors (mKNN) .

mKNN ( Huh et al., 2024 ) focuses on local topology. For each anchor sample i i , define the set of its k k nearest neighbors according to a distance measure dist ⁡ ( ⋅ , ⋅ ) \operatorname{dist}(\cdot,\cdot) in 𝐗 \mathbf{X} and 𝐘 \mathbf{Y} , N 𝐗 ​ ( i ) = KNN k ⁡ ( i ; 𝐗 ) , N 𝐘 ​ ( i ) = KNN k ⁡ ( i ; 𝐘 ) , N_{\mathbf{X}}(i)=\operatorname{KNN}_{k}(i;\mathbf{X}),\qquad N_{\mathbf{Y}}(i)=\operatorname{KNN}_{k}(i;\mathbf{Y}), (33) where KNN k ⁡ ( i , 𝐗 ) \operatorname{KNN}_{k}(i;\mathbf{X}) denotes the indices of the k k samples (excluding i i ) that minimize dist ⁡ ( 𝐱 i , 𝐱 j ) \mathrm{dist}(\mathbf{x}_{i},\mathbf{x}_{j}) . mKNN is then defined as the average fraction of shared neighbors: mKNN k ​ ( 𝐗 , 𝐘 ) = 1 n ​ ∑ i = 1 n | N 𝐗 ​ ( i ) ∩ N 𝐘 ​ ( i ) | k ∈ [ 0 , 1 ] . \mathrm{mKNN}_{k}(\mathbf{X},\mathbf{Y})\;=\;\frac{1}{n}\sum_{i=1}^{n}\frac{|N_{\mathbf{X}}(i)\cap N_{\mathbf{Y}}(i)|}{k}\;\in\;[0,1]. (34) What it measures: mKNN treats two representations as similar when each point keeps the same set of nearest neighbors in both spaces. It captures local topology, depends only on the rank order of distances, and is therefore invariant to any transformation that preserves k k -nearest-neighbor sets, ignoring exact distances and global geometry.

##### Cycle- k k NN (bidirectional k k -NN).

While mKNN measures one-directional neighborhood overlap, cycle- k k NN enforces a round-trip consistency between the two spaces ( Huh et al., 2024 ) . An anchor i i counts as consistent if at least one of its nearest neighbors j j in 𝐘 \mathbf{Y} has i i among its nearest neighbors in 𝐗 \mathbf{X} : cycle - kNN k ( 𝐗 , 𝐘 ) = 1 n ∑ i = 1 n [ i ∈ ⋃ j ∈ N 𝐘 ​ ( i ) N 𝐗 ( j ) ] ∈ [ 0 , 1 ] . \mathrm{cycle\text{-}kNN}_{k}(\mathbf{X},\mathbf{Y})\;=\;\frac{1}{n}\sum_{i=1}^{n}\mathbbm{1}\!\left[\,i\in\bigcup_{j\in N_{\mathbf{Y}}(i)}N_{\mathbf{X}}(j)\,\right]\;\in\;[0,1]. (35) This is stricter than mKNN , as it requires neighbor relations to be mutually recognized across the two spaces.

What it measures: cycle- k k NN treats points as similar only when neighborhood membership is reciprocated across spaces, a stricter local-topology criterion than mKNN .

##### CKA with Neighborhood Alignment (CKNNA).

CKNNA ( Huh et al., 2024 ) combines the kernel formulation of CKA with local neighborhood structure, restricting the kernel interaction to mutual k k -nearest-neighbor edges. Let 𝐊 X = 𝐗𝐗 ⊤ \mathbf{K}_{X}=\mathbf{X}\mathbf{X}^{\top} and 𝐊 Y = 𝐘𝐘 ⊤ \mathbf{K}_{Y}=\mathbf{Y}\mathbf{Y}^{\top} be the (linear) Gram matrices, and let 𝐌 X , 𝐌 Y ∈ { 0 , 1 } n × n \mathbf{M}_{X},\mathbf{M}_{Y}\in\{0,1\}^{n\times n} be the k k -NN indicator matrices with ( 𝐌 X ) i ​ j = 𝟙 [ j ∈ N 𝐗 ( i ) ] (\mathbf{M}_{X})_{ij}=\mathbbm{1}[\,j\in N_{\mathbf{X}}(i)\,] and ( 𝐌 Y ) i ​ j = 𝟙 [ j ∈ N 𝐘 ( i ) ] (\mathbf{M}_{Y})_{ij}=\mathbbm{1}[\,j\in N_{\mathbf{Y}}(i)\,] . Let 𝐀 = 𝐌 X ⊙ 𝐌 Y \mathbf{A}=\mathbf{M}_{X}\odot\mathbf{M}_{Y} retain only edges that are k k -NN in both spaces, where ⊙ \odot is the Hadamard product. CKNNA aligns the neighbor-masked Gram matrices with CKA ’s normalization: CKNNA k ​ ( 𝐗 , 𝐘 ) = ⟨ 𝐇 ⁡ ( 𝐀 ⊙ 𝐊 X ) ​ 𝐇 , 𝐇 ⁡ ( 𝐀 ⊙ 𝐊 Y ) ​ 𝐇 ⟩ F ‖ 𝐇 ⁡ ( 𝐌 X ⊙ 𝐊 X ) ​ 𝐇 ‖ F ​ ‖ 𝐇 ⁡ ( 𝐌 Y ⊙ 𝐊 Y ) ​ 𝐇 ‖ F . \mathrm{CKNNA}_{k}(\mathbf{X},\mathbf{Y})\;=\;\frac{\langle\mathbf{H}(\mathbf{A}\odot\mathbf{K}_{X})\mathbf{H},\;\mathbf{H}(\mathbf{A}\odot\mathbf{K}_{Y})\mathbf{H}\rangle_{F}}{\|\mathbf{H}(\mathbf{M}_{X}\odot\mathbf{K}_{X})\mathbf{H}\|_{F}\,\|\mathbf{H}(\mathbf{M}_{Y}\odot\mathbf{K}_{Y})\mathbf{H}\|_{F}}. (36) What it measures: CKNNA treats representations as similar when kernel values on shared (mutual) nearest-neighbor edges agree, combining CKA ’s normalization with a purely local notion of neighborhood structure.

## Appendix C Theoretical Derivations

In this section, we provide the theoretical justification for the confounding factors identified in Section 4 .

### C.1 Permutation validity, super-uniformity, and gating

This section formalizes the finite-sample validity of permutation calibration.

###### Definition C.1 (Super-uniformity) .

A p p -value p p is super-uniform under H 0 H_{0} if for all t ∈ [ 0 , 1 ] t\in[0,1] , ℙ H 0 ​ ( p ≤ t ) ≤ t . \mathbb{P}_{H_{0}}(p\leq t)\leq t. (37) Equivalently, p p -values under H 0 H_{0} are stochastically larger than Unif ⁡ ( 0 , 1 ) \mathrm{Unif}(0,1) , which is sufficient for valid Type-I error control.

###### Lemma C.2 (Permutation p p -values are super-uniform) .

Under Assumption 3.1 , the permutation p p -value in Equation 10 satisfies super-uniformity: ℙ H 0 ​ ( p ≤ α ) ≤ α \mathbb{P}_{H_{0}}(p\leq\alpha)\leq\alpha for all α ∈ [ 0 , 1 ] \alpha\in[0,1] (finite-sample validity).

###### Proof of Lemma C.2 .

Let s obs = s ⁡ ( 𝐗 , 𝐘 ) s_{\mathrm{obs}}=s(\mathbf{X},\mathbf{Y}) be the observed statistic and let s ( k ) = s ⁡ ( 𝐗 , π k ​ ( 𝐘 ) ) s^{(k)}=s(\mathbf{X},\pi_{k}(\mathbf{Y})) for k = 1 , … , K k=1,\dots,K be the statistics computed on permuted pairings. Under Assumption 3.1 , the vector ( s obs , s ( 1 ) , … , s ( K ) ) (s_{\mathrm{obs}},s^{(1)},\dots,s^{(K)}) is exchangeable : its joint distribution is invariant to permutations of the indices. Consider the (upper) rank R = 1 + # ⁡ { k ∈ { 1 , … , K } : s ( k ) ≥ s obs } ∈ { 1 , … , K + 1 } . R\;=\;1+\#\{k\in\{1,\dots,K\}:s^{(k)}\geq s_{\mathrm{obs}}\}\ \in\ \{1,\dots,K+1\}. (38) If the scores are almost surely distinct, exchangeability implies that the rank of s obs s_{\mathrm{obs}} among { s obs , s ( 1 ) , … , s ( K ) } \{s_{\mathrm{obs}},s^{(1)},\dots,s^{(K)}\} is uniform on { 1 , … , K + 1 } \{1,\dots,K+1\} . With possible ties, the add-one p p -value of Phipson and Smyth (2010) , p = R K + 1 , p=\frac{R}{K+1}, (39) is conservative, implying ℙ H 0 ​ ( p ≤ α ) ≤ α \mathbb{P}_{H_{0}}(p\leq\alpha)\leq\alpha for all α ∈ [ 0 , 1 ] \alpha\in[0,1] . ∎

###### Proof of Corollary 5.1 .

Let s obs = s ⁡ ( 𝐗 , 𝐘 ) s_{\mathrm{obs}}=s(\mathbf{X},\mathbf{Y}) and s ( k ) = s ⁡ ( 𝐗 , π k ​ ( 𝐘 ) ) s^{(k)}=s(\mathbf{X},\pi_{k}(\mathbf{Y})) for k = 1 , … , K k=1,\dots,K . Under Assumption 3.1 , the vector ( s obs , s ( 1 ) , … , s ( K ) ) (s_{\mathrm{obs}},s^{(1)},\dots,s^{(K)}) is exchangeable. Let τ α := s ( ⌈ ( 1 − α ) ​ ( K + 1 ) ⌉ ) \tau_{\alpha}:=s_{(\lceil(1-\alpha)(K+1)\rceil)} be the ( 1 − α ) (1-\alpha) -quantile defined via the order statistic of the combined multiset { s obs , s ( 1 ) , … , s ( K ) } \{s_{\mathrm{obs}},s^{(1)},\dots,s^{(K)}\} . Define the (upper) rank R = 1 + # ⁡ { k ∈ { 1 , … , K } : s ( k ) ≥ s obs } ∈ { 1 , … , K + 1 } , R\;=\;1+\#\{k\in\{1,\dots,K\}:s^{(k)}\geq s_{\mathrm{obs}}\}\ \in\ \{1,\dots,K+1\}, and the corresponding add-one p p -value p = R / ( K + 1 ) p=R/(K+1) . By construction of τ α \tau_{\alpha} , the rejection event { s obs > τ α } \{s_{\mathrm{obs}}>\tau_{\alpha}\} implies that s obs s_{\mathrm{obs}} lies among the largest ⌊ α ⁡ ( K + 1 ) ⌋ \lfloor\alpha(K+1)\rfloor values of { s obs , s ( 1 ) , … , s ( K ) } \{s_{\mathrm{obs}},s^{(1)},\dots,s^{(K)}\} , hence R ≤ α ⁡ ( K + 1 ) R\leq\alpha(K+1) and therefore p ≤ α p\leq\alpha . By Lemma C.2 , ℙ H 0 ​ ( p ≤ α ) ≤ α \mathbb{P}_{H_{0}}(p\leq\alpha)\leq\alpha , which yields ℙ H 0 ​ ( s obs > τ α ) ≤ ℙ H 0 ​ ( p ≤ α ) ≤ α . \mathbb{P}_{H_{0}}(s_{\mathrm{obs}}>\tau_{\alpha})\leq\mathbb{P}_{H_{0}}(p\leq\alpha)\leq\alpha. ∎

##### Restricted permutations under dependence.

Assumption 3.1 treats the n n row pairs as exchangeable units. In practice, exchangeability can be violated even without sequential structure ( e.g. , grouped or clustered samples). Validity is then recovered by using restricted permutations that preserve the dependence structure ( e.g. , permuting within blocks or permuting block labels) and re-running under each restricted permutation.

### C.2 Monotone invariance of rank-based calibration

The following proposition is a standard result in randomization inference; we state it here for completeness and to clarify its role in justifying the calibrated score design.

###### Proposition C.3 (Monotone invariance of rank-based calibration ( Lehmann and Romano, 2005 ) ) .

Let g : ℝ → ℝ g:\mathbb{R}\to\mathbb{R} be strictly increasing. Define p g p_{g} by applying Equation 10 to the transformed statistic g ∘ s g\circ s using the same permutations. Then p g = p p_{g}=p , and likewise the null percentile (the rank of s obs s_{\mathrm{obs}} among the combined set) is invariant under g g .

###### Proof.

Let g g be strictly increasing. For any two real numbers a , b a,b , we have a ≥ b a\geq b if and only if g ⁡ ( a ) ≥ g ⁡ ( b ) g(a)\geq g(b) . Therefore, for each permutation draw k k , 𝟙 { s ( k ) ≥ s obs } = 𝟙 { g ( s ( k ) ) ≥ g ( s obs ) } . \mathbbm{1}\{s^{(k)}\geq s_{\mathrm{obs}}\}=\mathbbm{1}\{g(s^{(k)})\geq g(s_{\mathrm{obs}})\}. (40) Summing over k k shows that the permutation rank R R (and thus the add-one p p -value) is unchanged by applying g g to both the observed and permuted statistics. The same argument applies to the null percentile, since the ordering of samples is preserved under g g . ∎

### C.3 Post-selection inflation and aggregation-aware validity

###### Proposition C.4 (Validity for aggregation-aware calibration) .

Let T T be any measurable aggregation operator applied to a layer-wise similarity matrix 𝐒 \mathbf{S} (e.g., max, row-max, top- k k ). If T obs = T ⁡ ( 𝐒 ) T_{\mathrm{obs}}=T(\mathbf{S}) is calibrated against the permutation null { T ⁡ ( 𝐒 ( k ) ) } k = 1 K \{T(\mathbf{S}^{(k)})\}_{k=1}^{K} as in Equation 16 , then the resulting p agg p_{\mathrm{agg}} is super-uniform under H 0 H_{0} .

###### Proof of Proposition C.4 .

Let T T be any measurable functional of the full data (representations across all layers), producing the scalar report T obs T_{\mathrm{obs}} . Under Assumption 3.1 and consistent layer-wise permutation of sample correspondences, the vector ( T obs , T ( 1 ) , … , T ( K ) ) (T_{\mathrm{obs}},T^{(1)},\dots,T^{(K)}) is exchangeable. Applying the same rank argument as in Section C.1 yields super-uniformity for the add-one p p -value in Equation 16 . ∎

### C.4 The width confounder

This appendix provides concrete calculations that justify the width confounder using Random Matrix Theory (RMT) : even under independence, interaction operators have non-trivial magnitude and spectrum when d d is not negligible relative to n n .

###### Proof of Proposition 4.1 .

Let 𝐗 ∈ ℝ n × d x \mathbf{X}\in\mathbb{R}^{n\times d_{x}} and 𝐘 ∈ ℝ n × d y \mathbf{Y}\in\mathbb{R}^{n\times d_{y}} have i.i.d. rows with mean 0 0 , identity covariance, and 𝐱 i \mathbf{x}_{i} and 𝐲 i \mathbf{y}_{i} independent. Let 𝐇 = 𝐈 n − 1 n ​ 𝟙 n ​ 𝟙 n ⊤ \mathbf{H}=\mathbf{I}_{n}-\frac{1}{n}\mathbbm{1}_{n}\mathbbm{1}_{n}^{\top} be the centering matrix, so 𝐗 c = 𝐇𝐗 \mathbf{X}_{c}=\mathbf{H}\mathbf{X} and 𝐘 c = 𝐇𝐘 \mathbf{Y}_{c}=\mathbf{H}\mathbf{Y} . Since 𝐇 \mathbf{H} is symmetric and idempotent ( 𝐇 2 = 𝐇 \mathbf{H}^{2}=\mathbf{H} ), the sample cross-covariance is 𝐂 ~ = 1 n − 1 ​ 𝐗 c ⊤ ​ 𝐘 c = 1 n − 1 ​ 𝐗 ⊤ ​ 𝐇𝐘 . \widetilde{\mathbf{C}}=\frac{1}{n-1}\mathbf{X}_{c}^{\top}\mathbf{Y}_{c}=\frac{1}{n-1}\mathbf{X}^{\top}\mathbf{H}\mathbf{Y}. (41) Denote entry ( a , b ) (a,b) as C ~ a ​ b \widetilde{C}_{ab} . Expanding via H i ​ j = δ i ​ j − 1 n H_{ij}=\delta_{ij}-\frac{1}{n} : C ~ a ​ b = 1 n − 1 ​ ( ∑ i = 1 n X i ​ a ​ Y i ​ b − 1 n ​ ( ∑ i = 1 n X i ​ a ) ​ ( ∑ j = 1 n Y j ​ b ) ) . \widetilde{C}_{ab}=\frac{1}{n-1}\left(\sum_{i=1}^{n}X_{ia}Y_{ib}-\frac{1}{n}\Bigl(\sum_{i=1}^{n}X_{ia}\Bigr)\Bigl(\sum_{j=1}^{n}Y_{jb}\Bigr)\right). (42) We compute 𝔼 ⁡ [ C ~ a ​ b 2 ] \mathbb{E}[\widetilde{C}_{ab}^{2}] using independence of 𝐱 i \mathbf{x}_{i} and 𝐲 j \mathbf{y}_{j} for all i , j i,j , zero means, and identity covariance.

Term 1: 𝔼 ⁡ [ ( ∑ i X i ​ a ​ Y i ​ b ) 2 ] = ∑ i , j 𝔼 ⁡ [ X i ​ a ​ X j ​ a ] ​ 𝔼 ​ [ Y i ​ b ​ Y j ​ b ] \mathbb{E}\bigl[(\sum_{i}X_{ia}Y_{ib})^{2}\bigr]=\sum_{i,j}\mathbb{E}[X_{ia}X_{ja}]\mathbb{E}[Y_{ib}Y_{jb}] . For i ≠ j i\!\neq\!j , independence across rows and zero mean give 𝔼 ⁡ [ X i ​ a ​ X j ​ a ] = 𝔼 ⁡ [ X i ​ a ] ​ 𝔼 ​ [ X j ​ a ] = 0 \mathbb{E}[X_{ia}X_{ja}]=\mathbb{E}[X_{ia}]\mathbb{E}[X_{ja}]=0 . For i = j i=j , we have 𝔼 ⁡ [ X i ​ a 2 ] ​ 𝔼 ​ [ Y i ​ b 2 ] = 1 \mathbb{E}[X_{ia}^{2}]\mathbb{E}[Y_{ib}^{2}]=1 . Thus 𝔼 ⁡ [ ( ∑ i X i ​ a ​ Y i ​ b ) 2 ] = n \mathbb{E}\bigl[(\sum_{i}X_{ia}Y_{ib})^{2}\bigr]=n .

𝔼 ⁡ [ ( ∑ i X i ​ a ​ Y i ​ b ) ​ ( ∑ j X j ​ a ) ​ ( ∑ k Y k ​ b ) ] = ∑ i , j , k 𝔼 ⁡ [ X i ​ a ​ X j ​ a ] ​ 𝔼 ​ [ Y i ​ b ​ Y k ​ b ] \mathbb{E}\bigl[(\sum_{i}X_{ia}Y_{ib})(\sum_{j}X_{ja})(\sum_{k}Y_{kb})\bigr]=\sum_{i,j,k}\mathbb{E}[X_{ia}X_{ja}]\mathbb{E}[Y_{ib}Y_{kb}] . This is nonzero only when i = j i=j and i = k i=k , yielding ∑ i 1 ⋅ 1 = n \sum_{i}1\cdot 1=n .

𝔼 ⁡ [ ( ∑ i X i ​ a ) 2 ​ ( ∑ j Y j ​ b ) 2 ] = 𝔼 ⁡ [ ( ∑ i X i ​ a ) 2 ] ​ 𝔼 ​ [ ( ∑ j Y j ​ b ) 2 ] = n ⋅ n = n 2 \mathbb{E}\bigl[(\sum_{i}X_{ia})^{2}(\sum_{j}Y_{jb})^{2}\bigr]=\mathbb{E}[(\sum_{i}X_{ia})^{2}]\mathbb{E}[(\sum_{j}Y_{jb})^{2}]=n\cdot n=n^{2} .

Combining: 𝔼 ⁡ [ C ~ a ​ b 2 ] \displaystyle\mathbb{E}\left[\widetilde{C}_{ab}^{2}\right] = 1 ( n − 1 ) 2 ​ ( n − 2 n ⋅ n + n 2 n 2 ) = 1 ( n − 1 ) 2 ​ ( n − 2 + 1 ) = 1 n − 1 . \displaystyle=\frac{1}{(n-1)^{2}}\left(n-\frac{2}{n}\cdot n+\frac{n^{2}}{n^{2}}\right)=\frac{1}{(n-1)^{2}}(n-2+1)=\frac{1}{n-1}. (43) Summing over all entries: 𝔼 ⁡ [ ‖ 𝐂 ~ ‖ F 2 ] = ∑ a = 1 d x ∑ b = 1 d y 𝔼 ⁡ [ C ~ a ​ b 2 ] = d x ​ d y n − 1 . \mathbb{E}\left[\|\widetilde{\mathbf{C}}\|_{F}^{2}\right]=\sum_{a=1}^{d_{x}}\sum_{b=1}^{d_{y}}\mathbb{E}[\widetilde{C}_{ab}^{2}]=\frac{d_{x}d_{y}}{n-1}. (44) ∎

##### Interpretation.

The null interaction energy is 𝒪 ⁡ ( d x ​ d y / n ) \mathcal{O}(d_{x}d_{y}/n) . In the common regime d x , d y ≍ n d_{x},d_{y}\asymp n , the null energy is 𝒪 ⁡ ( n ) \mathcal{O}(n) and therefore does not vanish . Since many spectral similarity metrics aggregate singular values ( e.g. , via ‖ 𝐂 ~ ‖ F 2 = ∑ i σ i 2 ​ ( 𝐂 ~ ) \|\widetilde{\mathbf{C}}\|_{F}^{2}=\sum_{i}\sigma_{i}^{2}(\widetilde{\mathbf{C}}) ), this already explains a positive baseline under H 0 H_{0} and its dependence on ( n , d x , d y ) (n,d_{x},d_{y}) .

##### Width inflation persists under genuine signal ( H 1 H_{1} ).

The width confounder is not specific to the null hypothesis. Even when two representations share a fixed, genuine signal, finite-sample CKA is inflated by width, because increasing d d grows the diagonal and off-diagonal Gram entries at different rates and the CKA denominator does not cancel the resulting width-dependent self-similarity.

###### Proposition C.5 (Width inflation under genuine signal) .

Fix n ≥ 2 n\geq 2 and a target alignment ρ ∈ ( 0 , 1 ) \rho\in(0,1) . For each width d d , draw 𝐮 i , 𝐯 i , 𝐰 i ∼ i . i . d . 𝒩 ⁡ ( 𝟎 , 𝐈 d ) \mathbf{u}_{i},\mathbf{v}_{i},\mathbf{w}_{i}\stackrel{{\scriptstyle\mathrm{i.i.d.}}}{{\sim}}\mathcal{N}(\mathbf{0},\mathbf{I}_{d}) independently across i = 1 , … , n i=1,\dots,n , and set 𝐱 i = ρ ​ 𝐮 i + 1 − ρ ​ 𝐯 i , 𝐲 i = ρ ​ 𝐮 i + 1 − ρ ​ 𝐰 i , \mathbf{x}_{i}=\sqrt{\rho}\,\mathbf{u}_{i}+\sqrt{1-\rho}\,\mathbf{v}_{i},\qquad\mathbf{y}_{i}=\sqrt{\rho}\,\mathbf{u}_{i}+\sqrt{1-\rho}\,\mathbf{w}_{i}, (45) so that 𝐱 i \mathbf{x}_{i} and 𝐲 i \mathbf{y}_{i} share the latent signal 𝐮 i \mathbf{u}_{i} . Then the population linear CKA equals ρ 2 < 1 \rho^{2}<1 , whereas for fixed n n the sample centered linear CKA satisfies CKA ⁡ ( 𝐗 , 𝐘 ) → 1 \mathrm{CKA}(\mathbf{X},\mathbf{Y})\to 1 almost surely as d → ∞ d\to\infty . Hence the finite-sample estimate is inflated by width, with CKA ⁡ ( 𝐗 , 𝐘 ) − ρ 2 → 1 − ρ 2 > 0 \mathrm{CKA}(\mathbf{X},\mathbf{Y})-\rho^{2}\to 1-\rho^{2}>0 .

###### Proof.

By independence of 𝐮 i , 𝐯 i , 𝐰 i \mathbf{u}_{i},\mathbf{v}_{i},\mathbf{w}_{i} , the marginal covariances are Σ x = Σ y = 𝐈 d \Sigma_{x}=\Sigma_{y}=\mathbf{I}_{d} and the cross-covariance is Σ x ​ y = Cov ⁡ ( 𝐱 i , 𝐲 i ) = ρ ​ 𝐈 d \Sigma_{xy}=\mathrm{Cov}(\mathbf{x}_{i},\mathbf{y}_{i})=\rho\,\mathbf{I}_{d} . The population linear CKA is therefore CKA pop = ‖ Σ x ​ y ‖ F 2 ‖ Σ x ‖ F ​ ‖ Σ y ‖ F = ρ 2 ​ d d ​ d = ρ 2 . \mathrm{CKA}_{\mathrm{pop}}=\frac{\|\Sigma_{xy}\|_{F}^{2}}{\|\Sigma_{x}\|_{F}\,\|\Sigma_{y}\|_{F}}=\frac{\rho^{2}d}{\sqrt{d}\,\sqrt{d}}=\rho^{2}. (46) For the sample statistic at fixed n n , write the columns of 𝐗 \mathbf{X} as 𝐠 1 , … , 𝐠 d ∈ ℝ n \mathbf{g}_{1},\dots,\mathbf{g}_{d}\in\mathbb{R}^{n} . Each entry of 𝐗 \mathbf{X} is 𝒩 ⁡ ( 0 , 1 ) \mathcal{N}(0,1) (since ρ + ( 1 − ρ ) = 1 \rho+(1-\rho)=1 ), and the columns are i.i.d. across j j with 𝐠 j ∼ 𝒩 ⁡ ( 𝟎 , 𝐈 n ) \mathbf{g}_{j}\sim\mathcal{N}(\mathbf{0},\mathbf{I}_{n}) . By the strong law of large numbers, 1 d ​ 𝐗𝐗 ⊤ = 1 d ​ ∑ j = 1 d 𝐠 j ​ 𝐠 j ⊤ → a . s . 𝔼 ⁡ [ 𝐠 1 ​ 𝐠 1 ⊤ ] = 𝐈 n . \frac{1}{d}\mathbf{X}\mathbf{X}^{\top}=\frac{1}{d}\sum_{j=1}^{d}\mathbf{g}_{j}\mathbf{g}_{j}^{\top}\xrightarrow{\mathrm{a.s.}}\mathbb{E}[\mathbf{g}_{1}\mathbf{g}_{1}^{\top}]=\mathbf{I}_{n}. (47) Since n n is fixed, this convergence also holds in Frobenius norm, so 1 d ​ 𝐇𝐗𝐗 ⊤ ​ 𝐇 → 𝐇 \tfrac{1}{d}\mathbf{H}\mathbf{X}\mathbf{X}^{\top}\mathbf{H}\to\mathbf{H} a.s.; the identical argument gives 1 d ​ 𝐇𝐘𝐘 ⊤ ​ 𝐇 → 𝐇 \tfrac{1}{d}\mathbf{H}\mathbf{Y}\mathbf{Y}^{\top}\mathbf{H}\to\mathbf{H} . By scale invariance of CKA , CKA ⁡ ( 𝐗 , 𝐘 ) = ⟨ 1 d ​ 𝐇𝐗𝐗 ⊤ ​ 𝐇 , 1 d ​ 𝐇𝐘𝐘 ⊤ ​ 𝐇 ⟩ F ‖ 1 d ​ 𝐇𝐗𝐗 ⊤ ​ 𝐇 ‖ F ​ ‖ 1 d ​ 𝐇𝐘𝐘 ⊤ ​ 𝐇 ‖ F → a . s . ⟨ 𝐇 , 𝐇 ⟩ F ‖ 𝐇 ‖ F 2 = 1 . \mathrm{CKA}(\mathbf{X},\mathbf{Y})=\frac{\langle\tfrac{1}{d}\mathbf{H}\mathbf{X}\mathbf{X}^{\top}\mathbf{H},\,\tfrac{1}{d}\mathbf{H}\mathbf{Y}\mathbf{Y}^{\top}\mathbf{H}\rangle_{F}}{\|\tfrac{1}{d}\mathbf{H}\mathbf{X}\mathbf{X}^{\top}\mathbf{H}\|_{F}\,\|\tfrac{1}{d}\mathbf{H}\mathbf{Y}\mathbf{Y}^{\top}\mathbf{H}\|_{F}}\xrightarrow{\mathrm{a.s.}}\frac{\langle\mathbf{H},\mathbf{H}\rangle_{F}}{\|\mathbf{H}\|_{F}^{2}}=1. (48) Subtracting the population value gives CKA ⁡ ( 𝐗 , 𝐘 ) − ρ 2 → 1 − ρ 2 > 0 \mathrm{CKA}(\mathbf{X},\mathbf{Y})-\rho^{2}\to 1-\rho^{2}>0 . ∎

Thus, at any fixed sample size n n , increasing the width drives the estimated CKA toward 1 1 regardless of the true alignment ρ 2 \rho^{2} , inflating it by up to 1 − ρ 2 1-\rho^{2} . This width-driven gap is distinct from the 𝒪 ⁡ ( 1 / n ) \mathcal{O}(1/n) sample-size effect that vanishes as n n grows, and it is exactly what permutation calibration removes. Section E.5 verifies this on real pretrained networks with nonzero true similarity.

##### CCA-based scores.

CCA , SVCCA , and PWCCA fall outside the energy analysis above: their canonical correlations are computed from the whitened cross-covariance, which normalizes away the cross-covariance energy of Proposition 4.1 . They therefore do not follow the 𝒪 ⁡ ( d / n ) \mathcal{O}(d/n) baseline. Their null instead reflects the rank deficiency of the whitening near and beyond d ≈ n d\approx n : mean CCA peaks at d ≈ n d\approx n and decays as 𝒪 ⁡ ( n / d ) \mathcal{O}(n/d) for d > n d>n , PWCCA saturates toward its ceiling once d ≳ n d\gtrsim n , and SVCCA is largely width-insensitive because it first projects onto a fixed low-dimensional subspace ( Section E.7 ). Permutation calibration removes this inflation without closed-form solutions, unlike the energy-based metrics.

##### Why we use permutation rather than closed forms.

Closed-form bulk edges are ensemble- and normalization-specific and are brittle to the preprocessing used in practice ( e.g. , centering, whitening, kernelization). Moreover, finite- n n corrections can be non-negligible. We therefore estimate the relevant right-tail behavior nonparametrically via permutation. This yields a conservative, implementation-faithful estimate of chance fluctuations without relying on fragile analytical formulas.

### C.5 The depth confounder

Here we formalize why selection-based summaries ( e.g. , maximum similarity over layer pairs) inflate with the size of the search space using Extreme Value Theory (EVT) .

Let 𝒮 = { S ℓ , ℓ ′ : 1 ≤ ℓ ≤ L A , 1 ≤ ℓ ′ ≤ L B } \mathcal{S}=\{S_{\ell,\ell^{\prime}}:1\leq\ell\leq L_{A},\,1\leq\ell^{\prime}\leq L_{B}\} denote the collection of null similarity fluctuations under H 0 H_{0} , and let M = L A ​ L B M=L_{A}L_{B} .

###### Assumption C.6 (Uniform sub-Gaussian right tails and integrability) .

There exist μ ∈ ℝ \mu\in\mathbb{R} and σ > 0 \sigma>0 such that for all ( ℓ , ℓ ′ ) (\ell,\ell^{\prime}) and all t ≥ 0 t\geq 0 , ℙ ⁡ ( S ℓ , ℓ ′ − μ ≥ t ) ≤ exp ⁡ ( − t 2 2 ​ σ 2 ) . \mathbb{P}(S_{\ell,\ell^{\prime}}-\mu\geq t)\leq\exp\!\left(-\frac{t^{2}}{2\sigma^{2}}\right). (49) Moreover, each S ℓ , ℓ ′ S_{\ell,\ell^{\prime}} is integrable: 𝔼 ​ | S ℓ , ℓ ′ | < ∞ \mathbb{E}|S_{\ell,\ell^{\prime}}|<\infty for all ( ℓ , ℓ ′ ) (\ell,\ell^{\prime}) .

###### Proposition C.7 (Maximal inequality, no independence required) .

Under Assumption C.6 and for M ≥ 2 M\geq 2 , 𝔼 ⁡ [ max ℓ , ℓ ′ ⁡ S ℓ , ℓ ′ ] ≤ μ + C ​ σ ​ log ⁡ M , \mathbb{E}\Big[\max_{\ell,\ell^{\prime}}S_{\ell,\ell^{\prime}}\Big]\;\leq\;\mu+C\,\sigma\sqrt{\log M}, (50) where C > 0 C>0 is a constant (e.g., one can take C = 3 C=3 ).

###### Proof.

Let Z := max ℓ , ℓ ′ ⁡ S ℓ , ℓ ′ − μ Z:=\max_{\ell,\ell^{\prime}}S_{\ell,\ell^{\prime}}-\mu . Since M < ∞ M<\infty and 𝔼 ​ | S ℓ , ℓ ′ | < ∞ \mathbb{E}|S_{\ell,\ell^{\prime}}|<\infty for all ( ℓ , ℓ ′ ) (\ell,\ell^{\prime}) , we have 𝔼 ​ | Z | ≤ 𝔼 ⁡ [ max ℓ , ℓ ′ ⁡ | S ℓ , ℓ ′ | ] + | μ | ≤ ∑ ℓ , ℓ ′ 𝔼 ​ | S ℓ , ℓ ′ | + | μ | < ∞ , \mathbb{E}|Z|\leq\mathbb{E}\Big[\max_{\ell,\ell^{\prime}}|S_{\ell,\ell^{\prime}}|\Big]+|\mu|\leq\sum_{\ell,\ell^{\prime}}\mathbb{E}|S_{\ell,\ell^{\prime}}|+|\mu|<\infty, (51) so Z Z is integrable, and the tail-integration formula applies. By the union bound and Assumption C.6 , ℙ ⁡ ( Z ≥ t ) ≤ M ​ exp ⁡ ( − t 2 2 ​ σ 2 ) for all ​ t ≥ 0 . \mathbb{P}(Z\geq t)\leq M\exp\!\left(-\frac{t^{2}}{2\sigma^{2}}\right)\qquad\text{for all }t\geq 0. (52) Using the tail-integration formula for an integrable real-valued random variable Z Z , 𝔼 ⁡ [ Z ] = ∫ 0 ∞ ℙ ⁡ ( Z ≥ t ) ​ 𝑑 t − ∫ 0 ∞ ℙ ⁡ ( Z ≤ − t ) ​ 𝑑 t ≤ ∫ 0 ∞ ℙ ⁡ ( Z ≥ t ) ​ 𝑑 t , \mathbb{E}[Z]=\int_{0}^{\infty}\mathbb{P}(Z\geq t)\,dt-\int_{0}^{\infty}\mathbb{P}(Z\leq-t)\,dt\leq\int_{0}^{\infty}\mathbb{P}(Z\geq t)\,dt, (53) and the bound ℙ ⁡ ( Z ≥ t ) ≤ 1 \mathbb{P}(Z\geq t)\leq 1 , we obtain 𝔼 ⁡ [ Z ] ≤ ∫ 0 ∞ min ⁡ { 1 , M ​ exp ⁡ ( − t 2 2 ​ σ 2 ) } ​ 𝑑 t . \mathbb{E}[Z]\;\leq\;\int_{0}^{\infty}\min\!\left\{1,\;M\exp\!\left(-\frac{t^{2}}{2\sigma^{2}}\right)\right\}\,dt. (54) Let t 0 = σ ​ 2 ​ log ⁡ M t_{0}=\sigma\sqrt{2\log M} . This value of t 0 t_{0} is the solution of M exp ( − t 0 2 / 2 σ 2 ) = 1 M\exp\!\left(-t_{0}^{2}/2\sigma^{2}\right)=1 , i.e. , the crossover where the bound min ⁡ { 1 , ⋅ } \min\{1,\cdot\} switches. Splitting the integral at t 0 t_{0} yields 𝔼 ⁡ [ Z ] ≤ t 0 + M ​ ∫ t 0 ∞ exp ⁡ ( − t 2 2 ​ σ 2 ) ​ 𝑑 t . \mathbb{E}[Z]\;\leq\;t_{0}\;+\;M\int_{t_{0}}^{\infty}\exp\!\left(-\frac{t^{2}}{2\sigma^{2}}\right)\,dt. (55) Applying the standard Gaussian tail bound ∫ t 0 ∞ e − t 2 / ( 2 σ 2 ) d t ≤ ( σ 2 / t 0 ) e − t 0 2 / ( 2 σ 2 ) \int_{t_{0}}^{\infty}e^{-t^{2}/(2\sigma^{2})}dt\leq(\sigma^{2}/t_{0})e^{-t_{0}^{2}/(2\sigma^{2})} gives 𝔼 ⁡ [ Z ] ≤ σ ​ 2 ​ log ⁡ M + σ 2 ​ log ⁡ M . \mathbb{E}[Z]\;\leq\;\sigma\sqrt{2\log M}\;+\;\frac{\sigma}{\sqrt{2\log M}}. (56) For M ≥ 2 M\geq 2 , the right-hand side is at most 3 ​ σ ​ log ⁡ M 3\sigma\sqrt{\log M} , proving the claim with C = 3 C=3 . ∎

##### Remark.

When the S ℓ , ℓ ′ S_{\ell,\ell^{\prime}} are i.i.d. (or weakly dependent), classical Extreme Value Theory yields sharper asymptotics. For example, if S ℓ , ℓ ′ ∼ 𝒩 ⁡ ( μ 0 , σ 0 2 ) S_{\ell,\ell^{\prime}}\sim\mathcal{N}(\mu_{0},\sigma_{0}^{2}) i.i.d., the centered maximum converges to a Gumbel distribution and 𝔼 ⁡ [ T max ] ≈ μ 0 + σ 0 ​ ( 2 ​ ln ⁡ M − ln ⁡ ln ⁡ M + ln ⁡ 4 ​ π 2 ​ 2 ​ ln ⁡ M ) , \mathbb{E}[T_{\max}]\approx\mu_{0}+\sigma_{0}\left(\sqrt{2\ln M}-\frac{\ln\ln M+\ln 4\pi}{2\sqrt{2\ln M}}\right), (57) as stated in standard references ( Cramér, 1999 ; Embrechts et al., 2013 ) . Real layer-wise similarities are dependent, so the approximation above should be treated as heuristic; Proposition C.7 provides a dependence-robust upper bound.

### C.6 Null Baselines for Neighborhood Metrics

The preceding analysis focused on the cross-covariance-energy metrics ( CKA and the RV coefficient), whose null baselines scale with d / n d/n . Neighborhood-based metrics such as mutual k k -NN follow a fundamentally different regime, which we now characterize.

###### Definition C.8 (Mutual k k -NN overlap) .

For representations 𝐗 ∈ ℝ n × d x , 𝐘 ∈ ℝ n × d y \mathbf{X}\in\mathbb{R}^{n\times d_{x}},\mathbf{Y}\in\mathbb{R}^{n\times d_{y}} and neighborhood size k < n k<n , let N 𝐗 ​ ( i ) ⊆ { 1 , … , n } ∖ { i } N_{\mathbf{X}}(i)\subseteq\{1,\ldots,n\}\setminus\{i\} denote the indices of the k k nearest neighbors of sample i i in 𝐗 \mathbf{X} ( e.g. , Euclidean or cosine), and similarly for N 𝐘 ​ ( i ) N_{\mathbf{Y}}(i) . The mutual k k -NN overlap is mKNN ⁡ ( 𝐗 , 𝐘 ) = 1 n ​ ∑ i = 1 n | N 𝐗 ​ ( i ) ∩ N 𝐘 ​ ( i ) | k . \mathrm{mKNN}(\mathbf{X},\mathbf{Y})=\frac{1}{n}\sum_{i=1}^{n}\frac{|N_{\mathbf{X}}(i)\cap N_{\mathbf{Y}}(i)|}{k}. (58)

###### Proposition C.9 (Uniformity of k k -NN index sets under i.i.d. sampling) .

Fix an anchor index i ∈ { 1 , … , n } i\in\{1,\dots,n\} . Let 𝐱 1 , … , 𝐱 n ∈ ℝ d \mathbf{x}_{1},\dots,\mathbf{x}_{n}\in\mathbb{R}^{d} be i.i.d. and define the k k -NN set N 𝐗 ​ ( i ) ⊆ { 1 , … , n } ∖ { i } N_{\mathbf{X}}(i)\subseteq\{1,\dots,n\}\setminus\{i\} using a fixed distance dist ⁡ ( ⋅ , ⋅ ) \mathrm{dist}(\cdot,\cdot) . Assume either (i) { dist ⁡ ( 𝐱 i , 𝐱 j ) } j ≠ i \{\mathrm{dist}(\mathbf{x}_{i},\mathbf{x}_{j})\}_{j\neq i} are almost surely distinct, or (ii) ties are broken by selecting a uniformly random k k -subset among the set of minimizers. Then N 𝐗 ​ ( i ) N_{\mathbf{X}}(i) is uniformly distributed over the ( n − 1 k ) \binom{n-1}{k} k k -subsets of { 1 , … , n } ∖ { i } \{1,\dots,n\}\setminus\{i\} .

###### Proof.

Let ℐ := { 1 , … , n } ∖ { i } \mathcal{I}:=\{1,\dots,n\}\setminus\{i\} be the candidate-neighbor index set. For any permutation π \pi of ℐ \mathcal{I} , i.i.d. sampling implies ( 𝐱 j ) j ∈ ℐ = d ( 𝐱 π ⁡ ( j ) ) j ∈ ℐ . (\mathbf{x}_{j})_{j\in\mathcal{I}}\stackrel{{\scriptstyle d}}{{=}}(\mathbf{x}_{\pi(j)})_{j\in\mathcal{I}}. The k k -NN selection rule depends on the candidate points only through their distances to 𝐱 i \mathbf{x}_{i} , so permuting the candidate indices permutes the resulting neighbor set. Under either the no-ties assumption or the stated uniform tie-break rule, for any two k k -subsets S , S ′ ⊆ ℐ S,S^{\prime}\subseteq\mathcal{I} there exists a permutation π \pi with π ⁡ ( S ) = S ′ \pi(S)=S^{\prime} and hence ℙ ⁡ ( N 𝐗 ​ ( i ) = S ) = ℙ ⁡ ( N 𝐗 ​ ( i ) = S ′ ) . \mathbb{P}\!\big(N_{\mathbf{X}}(i)=S\big)=\mathbb{P}\!\big(N_{\mathbf{X}}(i)=S^{\prime}\big). Since the events { N 𝐗 ( i ) = S } \{N_{\mathbf{X}}(i)=S\} over all | S | = k |S|=k partition the sample space, each has probability ( n − 1 k ) − 1 \binom{n-1}{k}^{-1} . ∎

###### Theorem C.10 (Null baseline for mutual k k -NN) .

Let 𝐗 , 𝐘 ∈ ℝ n × d \mathbf{X},\mathbf{Y}\in\mathbb{R}^{n\times d} have i.i.d. rows, with 𝐗 \mathbf{X} independent of 𝐘 \mathbf{Y} . Define N 𝐗 ​ ( i ) N_{\mathbf{X}}(i) and N 𝐘 ​ ( i ) N_{\mathbf{Y}}(i) as in Definition C.8 , using either almost sure absence of distance ties or uniform random tie-breaking. Then 𝔼 H 0 ​ [ mKNN ⁡ ( 𝐗 , 𝐘 ) ] = k n − 1 . \mathbb{E}_{H_{0}}\!\bigg[\mathrm{mKNN}(\mathbf{X},\mathbf{Y})\bigg]\;=\;\frac{k}{n-1}.

###### Proof.

Fix an anchor i i . By Proposition C.9 , N 𝐗 ​ ( i ) N_{\mathbf{X}}(i) and N 𝐘 ​ ( i ) N_{\mathbf{Y}}(i) are each uniform random k k -subsets of the ( n − 1 ) (n-1) -element set { 1 , … , n } ∖ { i } \{1,\dots,n\}\setminus\{i\} . Moreover, since 𝐗 \mathbf{X} and 𝐘 \mathbf{Y} are independent and N 𝐗 ​ ( i ) N_{\mathbf{X}}(i) (resp. N 𝐘 ​ ( i ) N_{\mathbf{Y}}(i) ) is a measurable function of 𝐗 \mathbf{X} (resp. 𝐘 \mathbf{Y} ), the sets N 𝐗 ​ ( i ) N_{\mathbf{X}}(i) and N 𝐘 ​ ( i ) N_{\mathbf{Y}}(i) are independent.

Therefore | N 𝐗 ​ ( i ) ∩ N 𝐘 ​ ( i ) | |N_{\mathbf{X}}(i)\cap N_{\mathbf{Y}}(i)| has a hypergeometric distribution with population size n − 1 n-1 , number of “successes” k k , and draws k k , giving 𝔼 H 0 ​ [ | N 𝐗 ​ ( i ) ∩ N 𝐘 ​ ( i ) | ] = k 2 n − 1 . \mathbb{E}_{H_{0}}\!\bigg[|N_{\mathbf{X}}(i)\cap N_{\mathbf{Y}}(i)|\bigg]=\frac{k^{2}}{n-1}. Substituting into the definition of mKNN \mathrm{mKNN} , 𝔼 H 0 ​ [ mKNN ⁡ ( 𝐗 , 𝐘 ) ] = 1 n ​ ∑ i = 1 n 𝔼 H 0 ​ [ | N 𝐗 ​ ( i ) ∩ N 𝐘 ​ ( i ) | k ] = 1 n ​ ∑ i = 1 n k n − 1 = k n − 1 . \mathbb{E}_{H_{0}}\bigg[\mathrm{mKNN}(\mathbf{X},\mathbf{Y})\bigg]=\frac{1}{n}\sum_{i=1}^{n}\mathbb{E}_{H_{0}}\!\left[\frac{|N_{\mathbf{X}}(i)\cap N_{\mathbf{Y}}(i)|}{k}\right]=\frac{1}{n}\sum_{i=1}^{n}\frac{k}{n-1}=\frac{k}{n-1}. ∎

###### Proposition C.11 (Per-anchor variance and generic bounds for mKNN \mathrm{mKNN} under the null) .

Under the assumptions of Theorem C.10 , for each anchor i i the intersection size H i := | N 𝐗 ​ ( i ) ∩ N 𝐘 ​ ( i ) | H_{i}:=|N_{\mathbf{X}}(i)\cap N_{\mathbf{Y}}(i)| is hypergeometric with mean k 2 / ( n − 1 ) k^{2}/(n-1) and variance Var ⁡ [ H i ] = k 2 ​ ( n − 1 − k ) 2 ( n − 1 ) 2 ​ ( n − 2 ) . \mathrm{Var}[H_{i}]\;=\;\frac{k^{2}(n-1-k)^{2}}{(n-1)^{2}(n-2)}. Moreover, since mKNN ⁡ ( 𝐗 , 𝐘 ) ∈ [ 0 , 1 ] \mathrm{mKNN}(\mathbf{X},\mathbf{Y})\in[0,1] deterministically, we have the fully general bound Var ⁡ [ mKNN ⁡ ( 𝐗 , 𝐘 ) ] ≤ 1 4 . \mathrm{Var}[\mathrm{mKNN}(\mathbf{X},\mathbf{Y})]\leq\frac{1}{4}. If one additionally assumes that the per-anchor terms { | N 𝐗 ​ ( i ) ∩ N 𝐘 ​ ( i ) | / k } i = 1 n \{|N_{\mathbf{X}}(i)\cap N_{\mathbf{Y}}(i)|/k\}_{i=1}^{n} are independent (this is a modeling assumption, not a consequence of H 0 H_{0} ), then Var ⁡ [ mKNN ⁡ ( 𝐗 , 𝐘 ) ] = 𝒪 ⁡ ( 1 / n ) \mathrm{Var}[\mathrm{mKNN}(\mathbf{X},\mathbf{Y})]=\mathcal{O}(1/n) .

###### Proof.

The hypergeometric variance formula gives Var ⁡ [ H i ] = k ⋅ k n − 1 ​ ( 1 − k n − 1 ) ⋅ ( n − 1 ) − k ( n − 1 ) − 1 = k 2 ​ ( n − 1 − k ) 2 ( n − 1 ) 2 ​ ( n − 2 ) . \mathrm{Var}[H_{i}]=k\cdot\frac{k}{n-1}\left(1-\frac{k}{n-1}\right)\cdot\frac{(n-1)-k}{(n-1)-1}=\frac{k^{2}(n-1-k)^{2}}{(n-1)^{2}(n-2)}. The bound Var ⁡ [ mKNN ] ≤ 1 / 4 \mathrm{Var}[\mathrm{mKNN}]\leq 1/4 follows from mKNN ∈ [ 0 , 1 ] \mathrm{mKNN}\in[0,1] . Under the stated additional independence assumption across anchors, Var ⁡ [ mKNN ⁡ ( 𝐗 , 𝐘 ) ] = 1 n ​ Var ​ ( H 1 k ) = 1 n ​ k 2 ​ Var ​ [ H 1 ] , \mathrm{Var}\bigg[\mathrm{mKNN}(\mathbf{X},\mathbf{Y})\bigg]=\frac{1}{n}\,\mathrm{Var}\!\left(\frac{H_{1}}{k}\right)=\frac{1}{nk^{2}}\,\mathrm{Var}[H_{1}], which is 𝒪 ⁡ ( 1 / n ) \mathcal{O}(1/n) for fixed k k . ∎

## Appendix D Implementation

A key advantage of null calibration is its simplicity: the framework can be applied to any similarity metric with minimal code changes. This section provides pseudocode for the two main calibration procedures described in the paper.

##### Scalar null calibration.

Algorithm 1 shows the complete procedure for calibrating a single similarity comparison. The only requirement is a function similarity(X,Y) that computes the raw metric. The algorithm returns both a permutation p p -value and a calibrated score with a principled zero point.

##### Aggregation-aware calibration for layer-wise comparisons.

When comparing models with multiple layers and reporting a summary statistic ( e.g. , maximum similarity across layer pairs), the aggregation step must also be calibrated. Algorithm 2 shows how to extend scalar calibration to this setting. The key insight is that the same sample permutation must be applied consistently across all layers.

##### Computational cost.

Let C sim C_{\mathrm{sim}} denote the cost of a single similarity evaluation on n n samples. Scalar calibration ( Algorithm 1 ) performs K + 1 K+1 evaluations at cost 𝒪 ⁡ ( ( K + 1 ) ​ C sim ) \mathcal{O}\!\left((K{+}1)\,C_{\mathrm{sim}}\right) , and aggregation-aware calibration ( Algorithm 2 ) over an L A × L B L_{A}\times L_{B} layer grid costs 𝒪 ⁡ ( ( K + 1 ) ​ L A ​ L B ​ C sim ) \mathcal{O}\!\left((K{+}1)\,L_{A}L_{B}\,C_{\mathrm{sim}}\right) . The K K null evaluations are independent and run in parallel. The marginal cost per permutation is typically far below C sim C_{\mathrm{sim}} , because permuting the rows of 𝐘 \mathbf{Y} leaves each model’s own representations unchanged. Metrics that are functionals of the n × n n\times n Gram, dissimilarity, or neighbor structures ( CKA , the RV coefficient, RSA , CKNNA) and the neighborhood metrics ( mKNN , cycle- k k NN) build these structures once in 𝒪 ⁡ ( n 2 ​ d ) \mathcal{O}(n^{2}d) and reduce each null draw to a relabeling, at 𝒪 ⁡ ( n 2 ) \mathcal{O}(n^{2}) or 𝒪 ⁡ ( n ​ k ) \mathcal{O}(nk) and independent of the representation width d d . The subspace and shape metrics ( CCA , SVCCA , PWCCA , Procrustes) are the exception: each null draw recomputes an eigendecomposition or SVD of a d d -dependent operator, at up to 𝒪 ⁡ ( n ​ d 2 + d 3 ) \mathcal{O}(nd^{2}+d^{3}) per permutation, which we batch across permutations on the GPU. On a single NVIDIA GTX 1080 Ti with K = 200 K=200 , this overhead is 20 20 ms per layer pair for linear CKA and 52 52 ms for mKNN , so a full layer-wise comparison between two models completes within a few seconds. We use K ∈ { 200 , … , 500 } K\in\{200,\dots,500\} permutations throughout, which we find sufficient for stable thresholds and p p -values ( Section E.6 ).

## Appendix E Additional Experimental Results

This appendix provides additional analyses that support the main text claims.

### E.1 Phase diagrams across different noise distributions

The theoretical analysis in Section 4 assumes Gaussian entries for tractability, but real neural network activations rarely follow Gaussian distributions. Instead, they often exhibit heavy tails, sparsity, or multimodality. A critical question is whether our calibration, which makes no distributional assumptions, remains effective under such deviations.

Figure 8 shows phase diagrams under different noise distributions: Gaussian, Student- t t ( ν = 3 \nu=3 ), Laplace, and Gaussian mixtures. Each panel shows raw scores (left) and calibrated scores (right) across the ( d / n , σ ) (d/n,\sigma) grid, where σ \sigma controls the noise level added to a fixed shared signal. At low σ \sigma , the signal dominates and both raw and calibrated scores correctly indicate high similarity. At high σ \sigma , noise overwhelms the signal, and similarity should approach zero. The key finding is that raw scores remain elevated (around 0.4–0.6) even at high noise levels where no detectable signal remains, while calibrated scores correctly collapse to near-zero. This pattern holds across all noise distributions tested, confirming that permutation-based calibration adapts to the data-generating process without requiring explicit distributional modeling.

### E.2 SNR heatmaps

The experiments of the main paper ( Figure 4 ) demonstrated that calibration eliminates false positives under H 0 H_{0} while preserving sensitivity to fixed signals. This section extends the analysis by characterizing how calibrated similarity varies jointly with signal strength, noise level, and dimensionality ratio, thereby delineating the regimes in which similarity estimation remains reliable.

Figure 9 presents heatmaps of raw scores (top row) and calibrated scores (bottom row) across the (Noise level, Signal strength) grid for three signal ranks ( r ∈ { 1 , 5 , 10 } r\in\{1,5,10\} ). The results reveal a clear phase transition structure. Raw scores (top) show uniformly high values across most of the grid, obscuring the true detection boundary. Calibrated scores (bottom) reveal the underlying signal: high scores concentrate in the low-noise, high-signal corner (bottom-left), while scores correctly collapse to zero as noise increases (moving right) or signal weakens (moving down). The detection boundary shifts rightward (tolerating higher noise) as signal rank increases. This phase structure is meaningful: it delineates when similarity measurements carry information about shared structure versus when they reflect only finite-sample artifacts.

Figure 10 provides a complementary view by collapsing the 2D heatmaps into 1D curves, plotting calibrated score against noise level for different signal strengths s s . As expected, calibrated scores decrease monotonically with noise level: at low noise, scores are high (reflecting the detectable shared signal), while at high noise, scores collapse to zero (reflecting that the signal is buried). Stronger signals (larger s s ) maintain elevated scores across a wider range of noise levels before eventually succumbing. Higher-rank signals ( r = 5 , 10 r=5,10 ) show more gradual decay compared to r = 1 r=1 , consistent with their greater statistical detectability. All curves converge to zero at high noise, confirming that the null floor is correctly calibrated regardless of signal strength or rank.

### E.3 Comparing calibration approaches

A natural question is whether the choice of calibration summary affects the correction. We consider several approaches: (i) gated score , which thresholds at a significance level and rescales ( α ∈ { 0.05 , 0.1 } \alpha\in\{0.05,0.1\} ); (ii) null-centered , subtracting the null mean; (iii) z-score , standardizing by null mean and standard deviation; and (iv) ARI-style , applying the chance-correction formula ( s − 𝔼 ⁡ [ s ] ) / ( s max − 𝔼 ⁡ [ s ] ) (s-\mathbb{E}[s])/(s_{\max}-\mathbb{E}[s]) . Figure 11 evaluates these variants across metrics as d / n d/n increases.

The results demonstrate that the gated score, null-centered, and ARI-style corrections all successfully collapse to appropriate null baselines across all metrics, regardless of whether the raw metric exhibits severe inflation (CKA, approaching 0.8) or mild inflation (RSA and mKNN, below 0.1). The z-score calibration, while correcting the mean, can exhibit artifacts when the null distribution is skewed, as occurs for bounded metrics like CKA at high d / n d/n , making it less suitable as a universal correction.

### E.4 Comparison with analytical debiasing

We validate our empirical null calibration by comparing it to existing analytical bias corrections for CKA . Figure 12 shows the difference between our calibrated CKA and two existing estimators: the debiased CKA of Murphy et al. (2024) and the dep-cols CKA of Chun et al. (2025) .

Our calibrated CKA closely matches the debiased CKA estimator, indicating that our calibration automatically corrects the dominant width-induced bias without requiring a metric-specific derivation. In contrast, dep-cols CKA is designed to correct column dependence, which is not present in our experimental setup (columns are independent by construction), so it does not address the dominant width-induced inflation. Under genuine signal ( H 1 H_{1} ) it stays near its maximal value across all d / n d/n , far above the closely agreeing debiased and calibrated estimates, while under the null ( H 0 H_{0} ) it fluctuates around zero with high variance.

Our calibration targets the same source of finite-sample bias that the unbiased HSIC estimator of Song et al. (2012) subtracts analytically: the self-similarity (diagonal) terms. This is consistent with the close agreement between the two corrections in Figure 12 . Unlike such analytical estimators, our permutation calibration requires no metric-specific derivation and applies to metrics for which no debiasing exists.

### E.5 Width confounder under genuine signal on real networks

We now verify on real pretrained networks that calibration corrects the width confounder when a genuine signal is present, complementing the analytical result of Proposition C.5 . Because the bias scales as 𝒪 ⁡ ( d / n ) \mathcal{O}(d/n) ( Proposition 4.1 ), width and sample size can be separated only by varying one while holding the other fixed, which this experiment does.

We extract last-layer features from the DINOv2 and AugReg ViT families. Within a family the models share training objective, data, and architecture and differ only in width d d ( e.g. , ViT-S/B/L/g for DINOv2), so a within-family pair isolates the effect of width. All pairs use the same n = 1024 n=1024 WIT images as the PRH setting, and for each pair we compute raw and calibrated linear CKA . At fixed n = 1024 n=1024 , the permutation threshold τ \tau (the magnitude of the width correction) increases with the total representation width d X + d Y d_{X}+d_{Y} , with Pearson correlation r = 0.88 r=0.88 ( Figure 13 ). Since n n is held constant, this dependence is attributable to width alone: calibration adapts its correction to representation width rather than applying a fixed offset. Together with Proposition C.5 , this confirms that calibration corrects the width confounder on real networks with genuine similarity.

### E.6 Permutation budget analysis

Permutation-based calibration introduces a computational-statistical tradeoff: more permutations yield more stable threshold estimates but increase runtime. Practitioners need guidance on the minimum budget required for reliable inference.

We analyze the stability of threshold estimates τ α \tau_{\alpha} and calibrated scores as a function of the permutation budget K K across 50 random seeds. Figure 14 shows two panels: the left panel displays threshold estimates, while the right panel shows calibrated scores under H 0 H_{0} . Threshold estimates (left) stabilize rapidly, reaching stable values by approximately K = 50 K=50 for all metrics tested. Calibrated scores (right) exhibit more variability at very low budgets ( K < 50 K<50 ), with occasional spikes due to unstable threshold estimation, but converge to near-zero by K ≈ 100 K\approx 100 – 200 200 .

Based on these results, we recommend K ≥ 200 K\geq 200 . The computational cost scales linearly with K K , so this recommendation represents a favorable tradeoff between precision and efficiency.

### E.7 Full null drift results

The main text presents null drift results for a representative subset of metrics under Gaussian noise. Here, we present additional results across all metrics evaluated in this work, including RSA, the RV coefficient, and Procrustes distance, as well as results under heavy-tailed noise distributions.

Figure 15 presents results under Gaussian noise for all metrics. The severity and shape of the null baseline vary substantially across metric families: among the spectral metrics, CKA variants and the RV coefficient show the strongest monotonic inflation with width, whereas the CCA family follows a distinct rank-deficiency pattern (mean CCA peaks near d ≈ n d\approx n then decays, PWCCA saturates, and SVCCA stays width-insensitive); the neighborhood metrics show the mildest drift. This reflects the structural sensitivity of the metrics to high-dimensional spurious correlations. RSA is the exception: as a self-normalized correlation of within-space dissimilarities, its null stays near zero and shows no width-driven drift. Critically, calibration eliminates drift across all metrics, collapsing scores to zero regardless of the raw bias magnitude.

Figure 16 extends these results to heavy-tailed noise (Student- t t , ν = 3 \nu=3 ). The qualitative pattern is preserved: the confounded metrics exhibit positive drift under the null, and calibration eliminates this drift. The magnitude of raw bias under heavy-tailed noise is comparable to the Gaussian case (marginally lower for the spectral metrics), and calibration adapts automatically without requiring distributional knowledge.

##### Robustness to the generative process.

The experiments above use i.i.d. Gaussian and heavy-tailed noise. To confirm that the width confounder is not tied to these specific generators, we also produce representations as 𝐱 i = f x ​ ( 𝐚 i ) \mathbf{x}_{i}=f_{x}(\mathbf{a}_{i}) and 𝐲 i = f y ​ ( 𝐚 i ) \mathbf{y}_{i}=f_{y}(\mathbf{a}_{i}) , where 𝐚 i \mathbf{a}_{i} is a shared Gaussian input and f x , f y f_{x},f_{y} are independent random linear maps or MLPs, so the two representations share inputs but no systematic structure. Figure 17 shows that raw CKA still inflates with dimensionality d d in every regime, while calibrated CKA stays at zero. Sharing inputs through unrelated networks thus produces width-driven inflation rather than genuine convergence, and calibration removes it regardless of how the representations are generated.

### E.8 Extended PRH alignment results (image–text)

The main text establishes a divergence between local and global similarity metrics when applied to the Platonic Representation Hypothesis (PRH) : neighborhood-based metrics retain significant cross-modal alignment after calibration, while spectral metrics lose their apparent convergence trend. A natural question is whether this finding is robust across model families and metric variants.

Here we present comprehensive results across all five vision model families in the PRH setting (DINOv2, CLIP, ImageNet-21K, MAE, and CLIP-finetuned) and a broad range of metrics spanning the local-to-global spectrum ( Figures 18 , 19 and 20 ).

The results reinforce and extend the main text findings. Neighborhood metrics (mKNN, cycle- k k NN, CKNNA) show a consistent alignment trend across all vision families with a neighborhood size of 10. This pattern holds for both self-supervised (DINOv2, MAE) and supervised (ImageNet-21K) pretraining objectives, as well as for both CLIP-aligned and CLIP-finetuned variants. Spectral metrics (CKA linear, CKA RBF, unbiased CKA, RV coefficient, SVCCA ) show a different pattern: raw scores suggest increasing alignment with model scale, but calibrated scores show no such scaling trend.

##### Trend with model scale, before versus after calibration.

For each metric separately, we measure the Pearson correlation between language-model capability (the model ranking of Huh et al. (2024) ) and the similarity score across all model pairs, before and after calibration ( Table 2 ). Global metrics lose most of their trend with scale after calibration, while local (neighborhood) metrics retain it across neighborhood sizes.

##### Continuous language-performance axis.

The preceding figures place each language model at its performance rank . Because Huh et al. (2024) instead plot cross-modal alignment against a continuous measure of language performance, we reproduce all of the above results on that axis for direct comparison. We quantify language performance by bits-per-byte (BPB) over OpenWebText, as in Huh et al. (2024) , oriented so that larger values, max ⁡ ( BPB ) − BPB \max(\mathrm{BPB})-\mathrm{BPB} , indicate stronger next-token prediction, and place each model at its measured value with a per-encoder least-squares fit ( Figures 21 , 22 and 23 ). The local–global divergence is unchanged on this axis: after calibration, neighborhood metrics retain their alignment trend with language performance while spectral metrics do not, so the finding does not depend on whether capability is expressed as a rank or as a continuous performance value.

##### Statistical significance.

Beyond calibrated scores, we report permutation p p -values to quantify statistical evidence against the null hypothesis of no cross-modal alignment ( Figure 24 ). All 204 vision–language model pairs are significant at p < 0.05 p<0.05 , with most achieving p ≈ 0.002 p\approx 0.002 (the minimum attainable with K = 500 K=500 permutations) for both local and global metrics. This confirms that cross-modal similarity is statistically significant ( i.e. , has some alignment) across all model pairs. The critical distinction between local and global metrics lies not in statistical significance but in the magnitude and trends of calibrated scores. Local metrics show substantial alignment above the null threshold that persists across scales, whereas global metrics, although significant, show no convergence in calibrated effect sizes.

### E.9 Extended video–language alignment results

The main text extends the PRH analysis to video–language alignment following Zhu et al. (2026) . Here, we provide additional results to verify that the local-vs-global pattern observed for image–language alignment extends to the video modality.

We use 1024 samples from the PVD ( Bolya et al., 2025 ; Cho et al., 2025 ) test set. We evaluate video-native models (VideoMAE ( Tong et al., 2022 ) ) and, as a frame-level baseline, image models (DINOv2 and CLIP) applied to the middle frame of each video, comparing all against the same three language model families used in the image–language experiments (BLOOM, OpenLLaMA, LLaMA) at multiple scales. For VideoMAE we include both the fine-tuned scale series (small/base/large/huge, fine-tuned on Kinetics) used in the main text and the corresponding non-fine-tuned checkpoints. Figure 25 shows results for spectral ( CKA RBF) and neighborhood ( mKNN , CKNNA) metrics.

The pattern mirrors the image–language findings. For spectral metrics, raw scores suggest alignment, whereas calibrated scores drop significantly, indicating that much of the apparent alignment is attributable to width and depth confounders. In contrast, neighborhood metrics retain significant alignment after calibration, confirming that video and language representations share local topological structure. This local alignment strengthens with the capability of the video encoder: both fine-tuning on Kinetics and increasing scale raise the calibrated neighborhood alignment, in line with the Aristotelian hypothesis that more capable representations converge more in local structure. Calibration removes the spectral inflation throughout.

### E.10 Characterizing the locality of cross-modal alignment

The main text establishes that local neighborhood metrics retain significant alignment after calibration, while global spectral metrics do not. We next characterize how local this alignment is. Both mKNN and CKA -RBF have hyperparameters that control their sensitivity to local versus global structure. By varying these parameters, we can characterize the scale at which cross-modal alignment emerges.

##### Experimental setup.

We vary two locality parameters: the neighborhood size k k in mKNN , testing k ∈ { 10 , 20 , 50 , 100 } k\in\{10,20,50,100\} where smaller values focus on immediate neighbors and larger values consider broader local structure, and the RBF kernel bandwidth σ \sigma in CKA -RBF, testing σ ∈ { 0.1 , 0.5 , 2.0 , 5.0 } \sigma\in\{0.1,0.5,2.0,5.0\} , which controls the length scale over which the kernel assigns significant weight.

##### RBF bandwidth.

The RBF (radial basis function) kernel is defined as k ( 𝐱 , 𝐲 ) = exp ( − ∥ 𝐱 − 𝐲 ∥ 2 / 2 σ 2 ) k(\mathbf{x},\mathbf{y})=\exp\left(-\|\mathbf{x}-\mathbf{y}\|^{2}/2\sigma^{2}\right) . The bandwidth σ \sigma determines the length scale of similarity. When σ \sigma is small ( e.g. , 0.1 0.1 ), the kernel is sharply peaked: only very close points contribute significantly to the Gram matrix, making the similarity measure sensitive to exact pairwise distances in the immediate neighborhood. When σ \sigma is large ( e.g. , 5.0 5.0 ), the kernel is broad: even moderately distant points contribute, and the similarity measure aggregates information over larger neighborhoods, becoming sensitive to coarser geometric structure.

##### Neighborhood size.

For mKNN , the parameter k k controls how many nearest neighbors are considered when measuring overlap. Small k k ( e.g. , 10 10 ) measures agreement on immediate neighbors, i.e. , the closest points to each sample, capturing fine-grained local topology. Large k k ( e.g. , 100 100 ) measures agreement on a broader neighborhood. With n = 1000 n=1000 samples and k = 100 k=100 , we ask whether the 10 % 10\% closest points agree across representations. Crucially, mKNN is a rank-based metric: it asks which points are neighbors (ordinal information), not how close they are (cardinal information).

##### mKNN across k k values.

Figure 26 shows the PRH alignment results for mKNN with varying k k . A consistent pattern emerges: all k k values show significant alignment after calibration, with calibrated scores remaining well above zero even at k = 100 k=100 . However, the scaling trend is most pronounced at small k k . For k = 10 k=10 , raw scores show a clear upward trend with model capacity that persists after calibration. At large k k , this trend flattens even in raw scores. For k = 100 k=100 , raw scores plateau for larger models, suggesting that broader neighborhood agreement is already saturated across model scales. This pattern indicates that scaling-driven improvement in alignment is concentrated at the finest topological level.

##### CKA-RBF across bandwidth values.

Figure 27 , and the accompanying p p -values in Figure 28 , show results for CKA-RBF with varying bandwidth σ \sigma , revealing a different pattern from mKNN. At σ = 0.1 \sigma=0.1 (very local), there is no significant alignment after calibration: raw scores are near 1.0 1.0 , reflecting the high similarity of any high-dimensional representations under a sharply peaked kernel. However, calibrated scores collapse to approximately zero with p p -values exceeding 0.05 0.05 for most model pairs, indicating that the observed similarity is indistinguishable from chance. At σ = 0.5 \sigma=0.5 , alignment emerges, but with a flattening trend after calibration. Calibrated scores initially rise with model scale, then plateau and slightly decline for the largest models. At σ = 2.0 \sigma=2.0 and σ = 5.0 \sigma=5.0 , significant alignment persists, but the calibrated trend also flattens, resembling the pattern observed for large- k k mKNN: alignment exists, but scaling-driven improvement disappears after calibration.

##### Topological versus metric alignment.

The contrasting behavior of mKNN and small- σ \sigma CKA-RBF reveals a fundamental distinction in what “local alignment” means. On one hand, mKNN measures topological alignment: do the representations agree on which points are neighbors? This captures ordinal information where the ranking of distances matters but not their absolute values. On the other hand, small- σ \sigma CKA-RBF measures metric alignment: do the representations agree on how close neighbors are? This captures cardinal information where exact distance values matter.

The fact that mKNN shows alignment at all k k values while small- σ \sigma CKA-RBF shows no alignment reveals that cross-modal representations agree on neighborhood identity (which points are close) but not on exact local distances (how close they are). This finding is consistent with the observation that different training objectives and architectures induce different distance scales in representation space while preserving the relative ordering of neighbors. The Aristotelian Representation Hypothesis should therefore be understood as convergence to shared topological structure rather than shared metric structure.

### E.11 Sensitivity to significance level α \alpha

The main text uses a significance level of α = 0.05 \alpha=0.05 throughout. To confirm that the PRH conclusions are not sensitive to this choice, we repeat the PRH evaluation from Section 6.3 with α ∈ { 0.01 , 0.05 , 0.10 } \alpha\in\{0.01,0.05,0.10\} for representative global (CKA linear, CKA RBF) and local ( mKNN with k = 10 k=10 ) metrics.

Figures 29 , 30 and 31 show that the conclusions are entirely invariant to the choice of α \alpha . For global metrics, calibrated scores show no convergence trend at any significance level. For local metrics, calibrated scores retain their alignment trend across all three α \alpha values. Stricter thresholds ( α = 0.01 \alpha=0.01 ) produce slightly lower calibrated scores, while more permissive thresholds ( α = 0.10 \alpha=0.10 ) produce slightly higher ones, but the qualitative pattern is unchanged. This confirms that our findings are not an artifact of a particular significance level.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
