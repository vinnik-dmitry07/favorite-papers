##### Report GitHub Issue

Content selection saved. Describe the issue below:

# From Tokens to Thoughts: How LLMs and Humans Trade Compression for Meaning

###### Abstract

Humans organize knowledge into compact conceptual categories that balance compression with semantic richness. Large Language Models (LLMs) exhibit impressive linguistic abilities, but whether they navigate this same compression-meaning trade-off remains unclear. We apply an Information Bottleneck framework to compare human conceptual structure with embeddings from 40+ LLMs using classic categorization benchmarks ( Rosch, 1973a ; Rosch, 1975 ; McCloskey and Glucksberg, 1978 ) . We find that LLMs broadly agree with human category boundaries, yet fall short on fine-grained semantic distinctions. Unlike humans, who maintain “inefficient” representations that preserve contextual nuance, LLMs aggressively compress, achieving more optimal information-theoretic compression at the cost of semantic richness. Surprisingly, encoder models outperform much larger decoder models in agreement with human categories, suggesting that understanding and generation rely on distinct representational mechanisms. Training-dynamics analysis reveals a two-phase trajectory: rapid initial concept formation followed by architectural reorganization, during which semantic processing migrates from deep to mid-network layers as the model discovers increasingly efficient, sparser encodings. These divergent strategies, where LLMs optimize for compression and humans for adaptive utility, reveal fundamental differences between artificial and natural intelligence. This highlights the need for models that preserve the conceptual “inefficiencies” essential for human-like understanding.

## 1 The Enigma of Meaning in Large Language Models

“The categories defined by constructions in human languages may vary from one language to the next, but they are mapped onto a common conceptual space , which represents a common cognitive heritage, indeed the geography of the human mind.” – Croft (2001) p. 139

Humans excel at organizing knowledge into concepts which are compact categories that achieve remarkable compression while preserving essential meaning ( Murphy, 2004 ) . A single word like “bird” compresses information about thousands of species, yet maintains critical semantic properties (can fly, has feathers, lays eggs). This hierarchical organization (robin → \rightarrow bird → \rightarrow animal; Rosch et al. 1976 ) represents a fundamental cognitive achievement: balancing efficiency with semantic fidelity.

Large Language Models (LLMs) demonstrate striking linguistic capabilities that suggest semantic understanding ( Singh et al., 2024 ; Li et al., 2025 ) . Yet, a critical question remains unanswered: Do LLMs navigate the compression-meaning trade-off similarly to humans, or do they employ fundamentally different representational strategies? This question matters because true understanding, which goes beyond surface-level mimicry, requires representations that balance statistical efficiency with semantic richness ( Tversky, 1977 ; Rosch, 1973c ) .

To address this question, we apply Rate-Distortion Theory ( Shannon, 1948 ) and Information Bottleneck principles ( Tishby et al., 2000 ) to systematically compare LLM and human conceptual structures. We digitize and release seminal cognitive psychology datasets ( Rosch, 1973c ; Rosch, 1975 ; McCloskey and Glucksberg, 1978 ) , which are foundational studies that shaped our understanding of human categorization but were previously unavailable in a machine-readable form. These benchmarks, comprising 1,049 items in 34 categories with membership and typicality ratings, offer unprecedented empirical grounding to evaluate whether LLMs truly understand concepts as humans. It also offers much better quality data than the current crowdsourcing paradigm by relying on experts to design and execute the human experiments.

Analyzing embeddings from 40+ diverse LLMs against these benchmarks, we uncover a fundamental divergence: LLMs and humans employ different strategies when balancing compression with meaning. While LLMs achieve broad categorical agreement with human judgment, they optimize for aggressive statistical compression at the expense of semantic nuance. Humans maintain “inefficient” representations that preserve rich, multidimensional structure essential for flexible reasoning.

This divergence manifests across three dimensions. First, LLMs capture categorical boundaries but miss fine-grained semantic distinctions like item typicality, central to human understanding. Second, our information-theoretic analysis reveals LLMs achieve mathematically “optimal” compression-distortion trade-offs, while human categories appear suboptimal. Third, encoder models surprisingly outperform decoder models in human alignment despite smaller scales, indicating that understanding and generation may require fundamentally different representational strategies.

Through analysis of OLMo-7B across 57 training checkpoints, we further uncover how these strategies emerge during learning: conceptual structure develops via rapid initial formation followed by architectural reorganization, with semantic processing migrating from deep to mid-network layers as models discover increasingly efficient encodings.

These findings challenge the assumption that statistical optimality equals understanding. The apparent “inefficiency” of human concepts may reflect optimization for adaptive flexibility. Our framework and newly-digitized benchmarks provide essential tools for monitoring this critical balance, guiding development toward AI systems that achieve not just compression, but comprehension.

## 2 Research Questions and Scope

Previous work has explored conceptual representations of LLM through multiple lenses: relational knowledge ( Shani et al., 2023 ; Misra et al., 2021 ) , interpretable concept extraction ( Hoang-Xuan et al., 2024 ; Maeda et al., 2024 ) , sparse activation patterns ( Li et al., 2025 ) , similarity preserving architecture Doumbouya et al. (2026) , and embedded geometry, including hierarchical structures ( Park et al., 2025 ) . While insightful, these studies often lack a deep, quantitative comparison of the compression-meaning trade-off using information theory against rich human cognitive benchmarks.

Separately, cognitive science has applied information theory to human concept learning ( Imel and Zaslavsky, 2024 ; Tucker et al., 2025 ; Zaslavsky et al., 2018 ; Sorscher et al., 2022 ) . For example, Zaslavsky et al. (2018) developed an Information Bottleneck framework for color naming efficiency, later extended to animal taxonomies ( Zaslavsky et al., 2020 ) . Yet these cognitive studies typically proceed without connecting to modern LLMs, and tend to focus on a specific domain. One notable example is Wu et al. (2025) , which examined abstraction transfer in humans and LLMs using a behavioral and cognitive modeling level. Our work is different in the sense that it analyzes how information is preserved or distorted inside LLM embedding spaces under controlled clustering transformations.

These two streams, LLM conceptual analysis and cognitive information theory, rarely intersect. We bridge this gap through rigorous comparison of how LLMs and humans navigate the compression-meaning trade-off, grounding our analysis in established cognitive benchmarks. This leads to three research questions:

[RQ1] To what extent do LLM-emergent concepts align with human-defined categories?

[RQ2] Do LLMs exhibit human-like internal structure, particularly item typicality?

[RQ3] How do humans and LLMs differ when balancing compression with semantic fidelity?

Our framework approaches each RQ through a unified lens. [RQ1] examines the categorical alignment, or how information is compressed into discrete groups. [RQ2] probes internal structure, which means how semantic meaning is preserved within categories. [RQ3] employs our ℒ \mathcal{L} objective to evaluate the integrated trade-off. This progression from compression to preservation to their balance mirrors the fundamental challenge both systems face: creating representations that are simultaneously efficient and meaningful.

Figure 1 overviews the data generation and analyses. Human data was collected by asking whether an item i (e.g., chair) is a good example of the category C (furniture). These ratings are aggregated into ranked similarity profiles for each category. Models generate analogous scores using their embeddings. We then compute three metrics: [RQ1] Mutual Information to assess category recoverability, [RQ2] Spearman correlation to measure alignment with human typicality structure, and [RQ3] a rate-distortion objective capturing the trade-off between representation complexity and meaning preservation.

## 3 Benchmarking Against Human Cognition

Investigating LLM-human conceptual alignment requires robust benchmarks and diverse models. This section details both components.

### 3.1 Human Baselines: Empirical Data from Seminal Cognitive Science

We draw on three foundational studies that shaped our understanding of human categorization. Unlike many noisy modern crowdsourced datasets, these classic benchmarks were carefully curated by experts, capturing deep cognitive patterns. We focus on three influential works:

Rosch (1973): This foundational work ( Rosch, 1973a ) explored semantic categories as part of the research program leading to prototype theory ( Rosch, 1973c ) 1 1 1 Prototype theory is only one account of how humans form concepts; exemplar theory offers an alternative based on stored instances. We do not adjudicate between theories, but use this framework because it provides structured data suitable for modeling. Our computational analysis is compatible with alternative accounts. . The theory posits that categories organize around “prototypical” members rather than strict, equally shared features. The dataset includes 48 items in eight common semantic categories (e.g., furniture, bird), with prototypicality rankings (e.g., ‘robin’ as typical bird, ‘bat’ as atypical).

Rosch (1975): Building on prototype theory, Rosch (1975) further detailed how semantic categories are cognitively represented. This work provides typicality ratings for a larger set of 552 items across ten categories (e.g., ‘orange‘ as a prototypical fruit, ‘squash‘ as less so).

McCloskey & Glucksberg (1978): Investigated the ”fuzzy” boundaries of natural categories, showing membership is graded rather than absolute ( McCloskey and Glucksberg, 1978 ) . Covers 449 items in 18 categories with both typicality scores and membership certainty ratings (e.g., ‘dress’ is typical clothing, ‘bandaid’ less so).

While originating from different researchers, these datasets share rigorous experimental designs and provide data on both category assignments and item typicality. We aggregated data from these studies, creating a unified benchmark of 1,049 items across 34 categories. This data, which we have digitized and made publicly available (Appendix C ), offers a high-quality empirical foundation for evaluating the human-likeness of LLMs. 2 2 2 Appendix I shows that polysemy is rare in our data and cannot account for our findings.

### 3.2 Large Language Models Under Study

We analyze 40+ diverse LLMs spanning multiple architectures and scales (300M to 72B parameters) to understand how conceptual representation varies across model design choices. We note that our analysis requires access to LLMs’ embeddings, rather than just output. Thus, we are unable to use any closed-source frontier models such as GPT-5 and Claude.

Model Selection. Our study encompasses three architectural paradigms. Encoder models include the BERT family ( Devlin et al., 2019 ; He et al., 2021 ; Zhuang et al., 2021 ) and CLIP ViT text encoders ( Radford et al., 2021 ) . Decoder models form the majority of our analysis: the Llama family (1B-70B; Touvron et al., 2023a ; Touvron et al., 2023b ; Grattafiori et al., 2024 ), Gemma variants (2B-27B; Team et al., 2024 ; Team et al., 2025 ), Qwen models (0.5B-72B; Bai et al., 2023 ; Yang et al., 2024 ), Phi series ( Javaheripi et al., 2023 ; Abdin et al., 2024 ; Abouelenin et al., 2025 ) , Mistral-7B ( Jiang et al., 2023 ) , GPT-2 ( Radford et al., 2019 ) , and OLMo-7B ( olmo2024 ) . We also include classic static embeddings Word2Vec ( Mikolov et al., 2013a ; Mikolov et al., 2013b ) and GloVe ( Pennington et al., 2014 ) as baselines.

This diverse selection enables us to disentangle effects of architecture (encoder vs. decoder), scale (300M to 72B), and training objectives (understanding vs. generation). Note that encoder-only models are less represented (and are smaller) since recent LLM development has prioritized decoder-only architectures. Complete model specifications appear in Appendix D .

Embedding Extraction. We extract representations at two levels to capture different aspects of conceptual knowledge: (1) static embeddings from input layers (E matrix), capturing context-free lexical knowledge directly comparable to isolated words in human categorization experiments; and (2) contextual embeddings from hidden layers using controlled prompts, revealing how context shapes conceptual structure across network depth.

This dual approach allows us to trace how concepts emerge from basic lexical knowledge to contextualized understanding. Critically, our results prove robust to prompt templates and pooling strategies (Appendix E ). Moreover, despite substantial vocabulary overlap between model families, neither token count nor tokenization patterns correlate with our results (Appendix J ).

## 4 A Framework for Comparing Compression and Meaning

To quantitatively compare how LLMs and humans navigate the fundamental tension between compact representation and semantic richness, we develop a framework that captures both aspects of conceptual organization. Our approach adapts Rate-Distortion Theory ( Shannon, 1948 ) and the Information Bottleneck principle ( Tishby et al., 2000 ) to measure the quality of conceptual systems.

### 4.1 Theoretical Foundations

Human concepts achieve remarkable efficiency: the word “bird” compresses knowledge about thousands of species into a single category, yet preserves critical semantic information (can fly, has feathers, lays eggs). This reflects a fundamental trade-off that any conceptual system must navigate:

• Compression: Grouping diverse items into manageable categories (fewer bits needed)

• Meaning Preservation: Maintaining semantic coherence within groups

Rate-Distortion Theory (RDT; Shannon, 1948 ) formalizes this trade-off for lossy compression. Given data X X and compressed representation X ^ \hat{X} , RDT seeks encodings that minimize: R + λ ​ D = I ⁡ ( X , X ^ ) + λ ​ 𝔼 ​ [ d ⁡ ( X , X ^ ) ] R+\lambda D=I(X;\hat{X})+\lambda\mathbb{E}[d(X,\hat{X})] (1) where R R is the rate (bits required), D D is distortion (information lost), and λ \lambda controls their trade-off.

Information Bottleneck (IB; Tishby et al., 2000 ) extends this by compressing X X into Z Z while preserving information about relevant variable Y Y : min ⁡ I ⁡ ( X , Z ) − β ​ I ​ ( Z , Y ) \min I(X;Z)-\beta I(Z;Y) (2)

Our adaptation: For conceptual representation, we lack an external relevance variable Y Y . Instead, ”relevance” becomes internal semantic coherence, i.e., how well categories preserve within-group similarity. We thus combine RDT’s geometric distortion with IB’s information-theoretic compression, yielding our framework where clustering C C represents items X X by minimizing both the information needed to specify items (compression) and the semantic spread within clusters (distortion).

### 4.2 The ℒ \mathcal{L} Objective: Quantifying the Trade-off

We formalize how clustering C C represents items X X through an objective that combines information-theoretic compression with geometric coherence:

ℒ ( X , C ; β ) = I ⁡ ( X , C ) ⏟ Complexity: bits needed + β ⋅ 1 | X | ​ ∑ c ∈ C ∑ e i ∈ c ‖ e i − e ¯ c ‖ 2 ⏟ Distortion: semantic spread \mathcal{L}(X,C;\beta)=\underbrace{I(X;C)}_{\text{Complexity: bits needed}}+\beta\cdot\underbrace{\frac{1}{|X|}\sum_{c\in C}\sum_{e_{i}\in c}\|e_{i}-\bar{e}_{c}\|^{2}}_{\text{Distortion: semantic spread}} (3)

where β \beta weights the relative importance of compression versus coherence.

#### 4.2.1 The Complexity Term: Measuring Compression

Complexity quantifies how much information the clustering preserves about individual items through mutual information I ⁡ ( X , C ) I(X;C) . Intuitively, if knowing an item’s cluster tells us little about which specific item it is, compression is high (low complexity).

Given | X | |X| items partitioned into clusters of sizes { | C c | } \{|C_{c}|\} : Complexity ​ ( X , C ) = I ⁡ ( X , C ) = log 2 ⁡ | X | − 1 | X | ​ ∑ c ∈ C | C c | ​ log 2 ​ | C c | \text{Complexity}(X,C)=I(X;C)=\log_{2}|X|-\frac{1}{|X|}\sum_{c\in C}|C_{c}|\log_{2}|C_{c}| (4)

This equals the reduction in uncertainty about item identity when told its cluster. Uniform clusters minimize complexity (one | X | |X| cluster; maximum compression), while singleton clusters maximize it (no compression).

#### 4.2.2 The Distortion Term: Measuring Semantic Coherence

Distortion captures how well clusters preserve semantic relationships and meanings by measuring the average squared distance between items and their cluster centroids in embedding space (spread): Distortion ​ ( X , C ) = 1 | X | ​ ∑ c ∈ C | C c | ⋅ σ c 2 \text{Distortion}(X,C)=\frac{1}{|X|}\sum_{c\in C}|C_{c}|\cdot\sigma^{2}_{c} (5)

where σ c 2 = 1 | C c | ​ ∑ e i ∈ c ‖ e i − e ¯ c ‖ 2 \sigma^{2}_{c}=\frac{1}{|C_{c}|}\sum_{e_{i}\in c}\|e_{i}-\bar{e}_{c}\|^{2} is the variance within cluster c c , and e ¯ c \bar{e}_{c} is its centroid.

Low distortion indicates tight, semantically coherent clusters with similar embeddings. This geometric measure captures the intuition of “meaningful” categories: robins and sparrows cluster tightly as similar birds, while bats would increase distortion on downstream tasks if categorized with them.

### 4.3 Connecting Framework to Research Questions

Our framework provides unified metrics for all three research questions:

[RQ1] Categorical Alignment: How do LLMs and humans partition semantic space? The Complexity term I ⁡ ( X , C ) I(X;C) directly measures this by quantifies how many bits are needed to specify individual items given their clusters. Comparing I ⁡ ( X , C Human ) I(X;C_{\text{Human}}) with I ⁡ ( X , C LLM ) I(X;C_{\text{LLM}}) reveals whether both systems create similarly-sized groupings with comparable compression rates. Higher mutual information means finer-grained categories; lower means broader, more compressed groupings.

[RQ2] Internal Semantic Structure: Do LLMs capture human-like typicality signal? The Distortion term measures how well clusters preserve semantic coherence. We tested whether typical items cluster tightly near centroids while atypical items lie farther away. Low distortion with clear center-periphery structure indicates prototype organization that mirrors human cognitive structure.

[RQ3] Compression-Meaning Trade-off: How do different systems balance efficiency against semantic fidelity? The complete ℒ \mathcal{L} objective reveals fundamental optimization strategies. By varying K K (number of clusters) and computing ℒ \mathcal{L} curves, we uncover system priorities: aggressive compressors rapidly achieve low ℒ \mathcal{L} values by sacrificing nuance, while systems preserving semantic richness maintain higher ℒ \mathcal{L} to retain meaningful distinctions. The shape and level of these curves expose whether a system optimizes for statistical efficiency or cognitive utility.

## 5 An Empirical Investigation of Representational Strategies

Building on our information-theoretic framework (Section 4 ) and established benchmarks (Section 3.1 ), we empirically investigate how LLMs and humans navigate the compression-meaning trade-off. For each analysis, we examine both static embeddings and contextual embeddings (across all hidden layers), revealing how and when context shapes conceptual organization.

### 5.1 [RQ1] The Big Picture: Alignment of Conceptual Categories

We first investigate whether LLMs form conceptual categories aligned with humans , which examines how information is compressed into discrete groups (the complexity term in our framework).

Approach: We tested whether LLMs naturally organize our 1,049 items into categories resembling human conceptual structure. Token embeddings were extracted at two levels: (i) static embeddings from input layers (E matrix), representing context-free lexical knowledge; (ii) contextual embeddings from all hidden layers, measured layer-wise to identify peak conceptual alignment. These were clustered using k-means ( K K matching human category counts) and evaluated against human categories using Adjusted Mutual Information (AMI), Normalized Mutual Information (NMI), and Adjusted Rand Index (ARI) metrics. NMI quantifies how much information is shared between the model-derived clusters and the human-labeled categories; AMI refines this measure by correcting for the amount of overlap that would be expected by chance; and ARI assesses the degree of agreement between the two partitions while explicitly accounting for random assignments, providing a complementary view of clustering accuracy.

Broad Categorical Agreement: All 40+ models achieve significant above-chance alignment (Figure 2 (Left)). Even at baseline, static embeddings show substantial alignment (mean A ​ M ​ I ≈ 0.45 AMI\approx 0.45 ), which contextual processing enhances to peak A ​ M ​ I ≈ 0.55 AMI\approx 0.55 . This confirms that LLMs encode human-like categorical boundaries. Full NMI and ARI results in Appendices K - M .

Architecture Matters More Than Scale: Surprisingly, BERT-large-uncased (340M parameters) achieves A ​ M ​ I = 0.60 AMI=0.60 , matching or exceeding models 100× larger. Classic static Word2Vec and GloVe embeddings, despite predating modern architectures by years, reach AMI scores rivaling contemporary LLMs’ peak performance. This suggests that fundamental semantic structure emerges from relatively simple distributional learning, with encoder architectures particularly effective at capturing human-like categories regardless of scale.

### 5.2 [RQ2] Zooming In: Fidelity to Fine-Grained Semantics

Having established broad categorical alignment, we now examine whether LLMs capture the internal semantic structure of categories. Specifically, we check how meaning is preserved within clusters .

Approach: We test whether LLMs encode human-like typicality signals, i.e., whether robins are more “birdy” than penguins. For each item, we compute the cosine similarity with its category name using embeddings (e.g., ‘robin’ → ‘bird’; c ​ o ​ s ​ i ​ n ​ e s ​ i ​ m ​ ( E ⁡ ( r ​ o ​ b ​ i ​ n ) , E ⁡ ( b ​ i ​ r ​ d ) CLOSE cosine_{sim}(E(robin),E(bird) ). We compare these similarities with human typicality ratings using Spearman’s correlation coefficient ρ \rho ( Wissler, 1905 ) .

We employed two analysis approaches: (i) static-layer analysis using embeddings directly from the input layer; (ii) peak AMI layer analysis using contextual embeddings from the layer that maximized AMI in RQ1. For the peak AMI approach, we extracted category embeddings by replacing items with category names in the same prompt template, ensuring consistent contextualization (see Appendix F for template and pooling robustness analysis).

Weak Typicality Alignment: Correlations between LLM internal organization of concepts and human typicality are modest at best (Figure 2 (Right); Tables 3 - 4 in Appendix N ). Static embeddings show weak correlations: BERT achieves ρ = 0.38 \rho=0.38 ( p < 0.05 p<0.05 ), while most decoder models fall below ρ = 0.15 \rho=0.15 . Even when statistically significant, these correlations indicate limited correspondence with human judgments. This shows that the internal concept geometries of models differ from those of humans, with representation-focused models aligning more closely.

Architectural Patterns: Several clear patterns emerge in how different architectures capture typicality. Representation-focused models (Word2Vec, GloVe) and most encoder models (both ViT encoders, BERT-large) demonstrate stronger static-layer performance than decoder-only models (Llama, Gemma, Qwen families). Static correlations range from ρ ≈ 0.25 \rho\approx 0.25 - 0.40 0.40 for representation-focused models versus ρ < 0.15 \rho<0.15 for most decoders.

This divergence likely stems from training objectives: models explicitly trained for representation learning appear more effective at capturing semantic category relationships in their embeddings, while modern decoder-only models, which optimized primarily for next-token prediction, show consistently lower static-layer correlations. The pattern holds across model scales, suggesting architectural design matters more than size for capturing fine-grained semantic similarity.

Layer-wise Analysis Reveals a Trade-off: Comparing static and peak AMI layers exposes an architectural limitation. Peak AMI layers, which are optimal for clustering, show systematically weaker typicality correlations than static layers. This pattern holds across model families: layers that best separate categories (RQ1) poorly preserve within-category structure (RQ2). The implication is clear: current architectures encode different aspects of meaning at different depths, forcing applications to choose between broad categorization and semantic nuance.

Interpretation: The divergence between LLMs and humans reflects fundamentally different organizational principles. Humans judge typicality through rich, multidimensional criteria: robins are typical birds due to size, flight ability, song, etc. This creates graded categories with clear prototypes and cognitive structures that optimize flexible reasoning and generalization.

LLMs, in contrast, appear to encode flatter statistical associations between items and category labels. Although sufficient for categorization and fluent text generation, these representations miss the prototype structure that makes categories cognitively useful. This difference suggests that LLMs optimize for different objectives than human cognition, a hypothesis that we test directly in RQ3 by examining how each system balances compression against semantic preservation.

### 5.3 [RQ3] The Efficiency Angle: The Compression-Meaning Trade-off

Having explored categorical alignment (RQ1) and internal semantic structure (RQ2), we now address our central question: How do LLM and human representational strategies compare when balancing compression against meaning preservation?

Approach: We analyzed human-defined categories and LLM-derived clusters using our ℒ \mathcal{L} objective function (Equation 3 , β = 1 \beta=1 ) and mean cluster entropy ( S α S_{\alpha} ). For LLMs, we performed k-means clustering across various K K values to trace the full compression-meaning frontier.

Results: Our analysis reveals three key patterns (Figure 3 ; full results in Appendix Q ):

LLMs Achieve Superior Statistical Efficiency: Both measures reveal stark differences between LLMs and humans (Figure 3 ; full results in Appendix Q ):

Higher human entropy. Human concepts consistently exhibit higher cluster entropy than LLM clusters at comparable K K values, indicating less statistical compactness but greater internal diversity.

Lower LLM ℒ \mathcal{L} scores. LLM-derived clusters achieve significantly lower ℒ \mathcal{L} values than human categories across all tested K K (Figure 3 b). Since lower ℒ \mathcal{L} signifies more optimal compression-distortion balance, LLMs are demonstrably more “efficient” by this information-theoretic measure.

Architectural differences. The Complexity-Distortion plot (Figure 3 a) reveals that encoder models (BERT, ViT, classic static models) achieve superior trade-offs. Their distortion at any given complexity is lower compared to decoder models, across both static and contextual embeddings.

Statistical Optimality Versus Cognitive Utility: This divergence reveals fundamental differences in optimization pressures. LLMs, trained on massive text corpora, develop maximally efficient statistical representations that minimize redundancy and internal variance. Although human conceptual systems may look suboptimal under information-theoretic measures, prior work indicates that they are structured to support goals such as flexible generalization and causal reasoning rather than maximal compression ( Murphy, 2004 ) . Thus, the differing pressures shaping human and LLM representations help explain this apparent suboptimality.

Our analysis reveals that compression efficiency does not predict functional capability. We find no correlation between ℒ \mathcal{L} scores and downstream performance ( r = − 0.20 r=-0.20 , ρ = 0.51 \rho=0.51 on MMLU; Appendix S ). This suggests that apparent human “inefficiency” reflects optimization for cognitive flexibility rather than statistical compression. While LLMs excel at compact representation, they may sacrifice the semantic richness essential for human-like understanding.

The consistent architectural patterns observed raise fundamental questions: Do understanding and generation require distinct computational strategies? The superiority of representation-focused models suggests that current architectures may be conflating two fundamentally different cognitive tasks.

### 5.4 Emergence During Training: How Divergent Strategies Develop

Having established that LLMs and humans employ divergent representational strategies, we investigate how these strategies emerge. Analysis of OLMo-7B across 57 training checkpoints (1K to 557K steps, approximately 4B to 2.5T tokens) reveals how conceptual structure emerges.

Two-Phase Representational Development. Conceptual organization emerges via two phases (Figure 15 ). First, rapid concept formation (1K-100K steps) establishes basic categorical structure, with AMI rising from near zero to approximately 0.45, achieving 80% of final alignment within just 10% of training. Second, architectural reorganization (100K-500K steps) systematically migrates semantic processing from deeper layers toward mid-network while AMI continues to gradually improve. This migration from layer 29 to layer 23 occurs without sacrificing categorical alignment, suggesting the model discovers more efficient internal representations. Moreover, this double-phase dynamics occurs when testing attention sparsity, effective rank, and ℒ \mathcal{L} values. That is, all of these exhibit the same early rapid shift followed by a slower restructuring phase. This convergence across independent metrics indicates that the model is not merely improving categorical alignment, but reorganizing its internal representations toward increasingly efficient structure. See Appendix H .

Architectural Reorganization as Optimization. The upward migration of semantic processing hints that the model discovers increasingly efficient encodings. Early training relies on deep, memorization-heavy representations, but as training progresses, the model shifts to distributed mid-network encoding. This reorganization may explain apparent “emergent” capabilities: they arise not from learning fundamentally new information but from more efficient internal organization of existing knowledge.

Implications. These dynamics demonstrate that the compression-oriented strategy observed in fully trained models develops from the earliest stages of training. The rapid initial alignment followed by efficiency-focused reorganization suggests models are inherently biased toward statistical compression rather than semantic richness. Achieving human-like representations may require not just different final objectives but fundamentally different learning dynamics that actively maintain semantic diversity throughout development.

## 6 Discussion and Conclusion

We investigated how LLMs and humans navigate the compression-meaning trade-off in conceptual representation. Using information-theoretic analysis of 40+ models against classic cognitive benchmarks, we reveal fundamental differences in their representational strategies.

Key Findings. LLMs achieve broad categorical alignment with humans (AMI ≈ \approx 0.55), successfully partitioning semantic space into recognizable categories. However, they fail to capture the internal structure that makes these categories cognitively useful, as typicality correlations remain weak ( ρ < 0.2 \rho<0.2 ) across model families. Most strikingly, when evaluated on the compression-meaning trade-off, LLMs consistently achieve lower (better) ℒ \mathcal{L} scores than human categories, indicating they optimize for statistical efficiency over semantic richness. This pattern holds across architectures, though encoder models surprisingly outperform decoder models in human alignment despite being orders of magnitude smaller. Training dynamics analysis reveals rapid category formation followed by architectural reorganization that shifts semantic processing from deep to mid-network layers, suggesting efficiency optimization continues throughout training.

Implications. These findings challenge the assumption that statistical optimality equals understanding. LLMs excel at their training objective, which is minimizing prediction error, but this drives them toward representations that sacrifice semantic nuances. Encoder models’ superior alignment with human representations questions the current paradigm of unified, scaled decoder models, suggesting that language understanding and generation may require distinct architectures and rely on different processes . Our framework provides quantitative tools for monitoring the compression-meaning balance in future systems.

Conclusions. Our findings reveal an apparent paradox, showing that LLMs are simultaneously better and worse than humans. This occurs because LLMs and humans employ divergent strategies: statistical compression versus semantic richness , likely reflecting different optimization pressures. While LLMs process billions of tokens efficiently, humans enable flexible reasoning and generalization. Progress toward human-like AI may require preserving the apparent “inefficiencies” that support cognitive flexibility. We provide theoretical understanding, practical metrics, and high-quality digital benchmarks to develop more human-aligned representations. We encourage the community to utilize the data and metrics for future research towards making AI more human-like.

## 7 Ethics statement

Our study relies exclusively on publicly available LLMs and digitized datasets from classic cognitive psychology experiments ( Rosch, 1973a ; Rosch, 1975 ; McCloskey and Glucksberg, 1978 ) . No new human subject data was collected, and all benchmark data we release have been properly attributed and curated to preserve research integrity.

We do not foresee privacy, security, or fairness risks arising from our analyses. Our contribution is methodological and theoretical, focusing on representational trade-offs between humans and LLMs. Nevertheless, we acknowledge that insights into model-human divergences could influence how future systems are designed. We caution that optimizing solely for statistical efficiency without considering semantic richness may exacerbate risks of misinterpretation or oversimplification in socially sensitive applications.

We declare no conflicts of interest or external sponsorship that could bias the reported findings.

## 8 Reproducibility statement

We have taken several steps to ensure reproducibility. All digitized human categorization datasets used in our analyses are publicly released in machine-readable form (Appendix B.1). Detailed model specifications, including architectures, scales, and hyperparameters, are provided in Appendix B.2, and we document embedding extraction procedures, pooling strategies, and prompt templates in Appendix B.3-B.4. Full experimental results, including layer-wise analyses, clustering metrics, and training dynamics across checkpoints, are reported in the appendices (B.5-B.14). Our theoretical framework and derivations are described in Section 4, with complete definitions and formulations provided to enable replication. We will release the code for dataset processing, embedding extraction, and evaluation upon acceptance (to preserve anonymity).

## 9 Acknowledgments

We are grateful to our teacher and mentor, the late Prof. Naftali Tishby, for his profound contributions to information theory, as well as for inspiring us with the depth, elegance, and excitement of this field. This work was supported in part by the Koret Foundation grant for Smart Cities and Digital Living.

## References

Abdin et al. (2024) M. Abdin, J. Aneja, H. Awadalla, A. Awadallah, A. A. Awan, N. Bach, A. Bahree, A. Bakhtiari, J. Bao, H. Behl, et al. Phi-3 technical report: a highly capable language model locally on your phone . arXiv preprint arXiv:2404.14219 . Cited by: 4th item , §3.2 .

Abouelenin et al. (2025) A. Abouelenin, A. Ashfaq, A. Atkinson, H. Awadalla, N. Bach, J. Bao, A. Benhaim, M. Cai, V. Chaudhary, C. Chen, et al. Phi-4-mini technical report: compact yet powerful multimodal language models via mixture-of-loras . arXiv preprint arXiv:2503.01743 . Cited by: 4th item , §3.2 .

Bai et al. (2023) J. Bai, S. Bai, Y. Chu, Z. Cui, K. Dang, X. Deng, Y. Fan, W. Ge, Y. Han, F. Huang, et al. Qwen technical report . arXiv preprint arXiv:2309.16609 . Cited by: 2nd item , §3.2 .

Croft (2001) W. Croft Radical construction grammar: syntactic theory in typological perspective . Oxford University Press, USA . Cited by: §1 .

DeepSeek-AI (2025) DeepSeek-AI DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning . External Links: 2501.12948 , Link Cited by: 8th item .

Devlin et al. (2019) J. Devlin, M. Chang, K. Lee, and K. Toutanova BERT: pre-training of deep bidirectional transformers for language understanding . In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) , J. Burstein, C. Doran, and T. Solorio (Eds.) , Minneapolis, Minnesota , pp. 4171–4186 . External Links: Link , Document Cited by: 1st item , §3.2 .

Doumbouya et al. (2026) M. K. B. Doumbouya, D. Jurafsky, and C. D. Manning Tversky neural networks: psychologically plausible deep learning with differentiable tversky similarity . In The Fourteenth International Conference on Learning Representations , Cited by: §2 .

Grattafiori et al. (2024) A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Vaughan, et al. The llama 3 herd of models . In Neural Information Processing Systems , Cited by: 3rd item , §3.2 .

He et al. (2021) P. He, X. Liu, J. Gao, and W. Chen DEBERTA: decoding-enhanced bert with disentangled attention . In International Conference on Learning Representations , Cited by: 1st item , §3.2 .

Hoang-Xuan et al. (2024) N. Hoang-Xuan, M. Vu, and M. T. Thai LLM-assisted concept discovery: automatically identifying and explaining neuron functions . arXiv preprint arXiv:2406.08572 . Cited by: §2 .

Imel and Zaslavsky (2024) N. Imel and N. Zaslavsky Optimal compression in human concept learning . In Proceedings of the Annual Meeting of the Cognitive Science Society , Vol. 46 . Cited by: §2 .

Javaheripi et al. (2023) M. Javaheripi, S. Bubeck, M. Abdin, J. Aneja, S. Bubeck, C. C. T. Mendes, W. Chen, A. Del Giorno, R. Eldan, S. Gopi, et al. Phi-2: the surprising power of small language models . Microsoft Research Blog 1 ( 3 ), pp. 3 . Cited by: 4th item , §3.2 .

Jiang et al. (2023) A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. de las Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier, L. R. Lavaud, M. Lachaux, P. Stock, T. L. Scao, T. Lavril, T. Wang, T. Lacroix, and W. E. Sayed Mistral 7b . External Links: 2310.06825 , Link Cited by: 6th item , §3.2 .

Li et al. (2025) Y. Li, E. J. Michaud, D. D. Baek, J. Engels, X. Sun, and M. Tegmark The geometry of concepts: sparse autoencoder feature structure . Entropy 27 ( 4 ), pp. 344 . Cited by: §1 , §2 .

Maeda et al. (2024) A. Maeda, T. Torii, and S. Hidaka Decomposing co-occurrence matrices into interpretable components as formal concepts . In Findings of the Association for Computational Linguistics ACL 2024 , pp. 4683–4700 . Cited by: §2 .

McCloskey and Glucksberg (1978) M. E. McCloskey and S. Glucksberg Natural categories: well defined or fuzzy sets? . Memory & Cognition 6 ( 4 ), pp. 462–472 . Cited by: Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Figure 27 , Figure 28 , 29(c) , Appendix C , 14(c) , §1 , §3.1 , §7 , Abstract .

Mikolov et al. (2013a) T. Mikolov, K. Chen, G. Corrado, and J. Dean Efficient estimation of word representations in vector space . In Proceedings of Workshop at International Conference on Learning Representations (ICLR) , External Links: Link Cited by: 11st item , §3.2 .

Mikolov et al. (2013b) T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean Distributed representations of words and phrases and their compositionality . In Advances in Neural Information Processing Systems , Vol. 26 , pp. 3111–3119 . Cited by: 11st item , §3.2 .

Misra et al. (2021) K. Misra, A. Ettinger, and J. Rayz Do language models learn typicality judgments from text? . In Proceedings of the Annual Meeting of the Cognitive Science Society , Vol. 43 . Cited by: §2 .

Murphy (2004) G. Murphy The big book of concepts . MIT press . Cited by: §1 , §5.3 .

Park et al. (2025) K. Park, Y. J. Choe, Y. Jiang, and V. Veitch The geometry of categorical and hierarchical concepts in large language models . In The Thirteenth International Conference on Learning Representations , Cited by: §2 .

Pennington et al. (2014) J. Pennington, R. Socher, and C. Manning GloVe: global vectors for word representation . In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) , A. Moschitti, B. Pang, and W. Daelemans (Eds.) , Doha, Qatar , pp. 1532–1543 . External Links: Link , Document Cited by: 11st item , §3.2 .

Radford et al. (2021) A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. Learning transferable visual models from natural language supervision . In International conference on machine learning , pp. 8748–8763 . Cited by: 10th item , §3.2 .

Radford et al. (2019) A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever, et al. Language models are unsupervised multitask learners . OpenAI blog 1 ( 8 ), pp. 9 . Cited by: 7th item , §3.2 .

Rosch (1973a) E. Rosch On the internal structure of perceptual and semantic categories . Cognitive development and the acquisition of language/New York: Academic Press . Cited by: Figure 27 , Figure 28 , 29(a) , Appendix C , 14(a) , §3.1 , §7 , Abstract .

Rosch (1973b) E. H. Rosch Natural categories . Cognitive psychology 4 ( 3 ), pp. 328–350 . Cited by: Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 .

Rosch et al. (1976) E. Rosch, C. Simpson, and R. S. Miller Structural bases of typicality effects. . Journal of Experimental Psychology: Human perception and performance 2 ( 4 ), pp. 491 . Cited by: §1 .

Rosch (1973c) E. Rosch Prototype theory . Cognitive development and the acquisition of language , pp. 111–144 . Cited by: §1 , §1 , §3.1 .

Rosch (1975) E. Rosch Cognitive representations of semantic categories. . Journal of experimental psychology: General 104 ( 3 ), pp. 192 . Cited by: Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Table 2 , Figure 27 , Figure 28 , 29(b) , Appendix C , 14(b) , §1 , §3.1 , Figure 3 , §7 , Abstract .

Shani et al. (2023) C. Shani, J. Vreeken, and D. Shahaf Towards concept-aware large language models . In Findings of the Association for Computational Linguistics: EMNLP 2023 , pp. 13158–13170 . Cited by: §2 .

Shannon (1948) C. E. Shannon A mathematical theory of communication . The Bell system technical journal 27 ( 3 ), pp. 379–423 . Cited by: §1 , §4.1 , §4 .

Singh et al. (2024) C. Singh, J. P. Inala, M. Galley, R. Caruana, and J. Gao Rethinking interpretability in the era of large language models . arXiv preprint arXiv:2402.01761 . Cited by: §1 .

Sorscher et al. (2022) B. Sorscher, S. Ganguli, and H. Sompolinsky Neural representational geometry underlies few-shot concept learning . Proceedings of the National Academy of Sciences 119 ( 43 ), pp. e2200800119 . Cited by: §2 .

Team et al. (2025) G. Team, A. Kamath, J. Ferret, S. Pathak, N. Vieillard, R. Merhej, S. Perrin, T. Matejovicova, A. Ramé, M. Rivière, et al. Gemma 3 technical report . arXiv preprint arXiv:2503.19786 . Cited by: 5th item , §3.2 .

Team et al. (2024) G. Team, T. Mesnard, C. Hardin, R. Dadashi, S. Bhupatiraju, S. Pathak, L. Sifre, M. Rivière, M. S. Kale, J. Love, et al. Gemma: open models based on gemini research and technology . arXiv preprint arXiv:2403.08295 . Cited by: 5th item , §3.2 .

Tishby et al. (2000) N. Tishby, F. C. Pereira, and W. Bialek The information bottleneck method . arXiv preprint physics/0004057 . Cited by: §1 , §4.1 , §4 .

Touvron et al. (2023a) H. Touvron, T. Lavril, G. Izacard, X. Martinet, M. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al. Llama: open and efficient foundation language models . arXiv preprint arXiv:2302.13971 . Cited by: 3rd item , §3.2 .

Touvron et al. (2023b) H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale, et al. Llama 2: open foundation and fine-tuned chat models . arXiv preprint arXiv:2307.09288 . Cited by: 3rd item , §3.2 .

Tucker et al. (2025) M. Tucker, J. Shah, R. Levy, and N. Zaslavsky Towards human-like emergent communication via utility, informativeness, and complexity . Open Mind 9 , pp. 418–451 . Cited by: §2 .

Tversky (1977) A. Tversky Features of similarity. . Psychological review 84 ( 4 ), pp. 327 . Cited by: §1 .

Wissler (1905) C. Wissler The spearman correlation formula . Science 22 ( 558 ), pp. 309–311 . Cited by: §5.2 .

Wu et al. (2025) S. Wu, M. Thalmann, P. Dayan, Z. Akata, and E. Schulz Building, reusing, and generalizing abstract representations from concrete sequences . In Thirteenth International Conference on Learning Representations (ICLR 2025) , Cited by: §2 .

Yang et al. (2024) A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, H. Wei, et al. Qwen2. 5 technical report . arXiv preprint arXiv:2412.15115 . Cited by: 2nd item , §3.2 .

Zaslavsky et al. (2018) N. Zaslavsky, C. Kemp, T. Regier, and N. Tishby Efficient compression in color naming and its evolution . Proceedings of the National Academy of Sciences 115 ( 31 ), pp. 7937–7942 . Cited by: §2 .

Zaslavsky et al. (2020) N. Zaslavsky, T. Regier, N. Tishby, and C. Kemp Semantic categories of artifacts and animals reflect efficient coding . In Proceedings of the Society for Computation in Linguistics 2020 , pp. 80–81 . Cited by: §2 .

Zhuang et al. (2021) L. Zhuang, L. Wayne, S. Ya, and Z. Jun A robustly optimized BERT pre-training approach with post-training . In Proceedings of the 20th Chinese National Conference on Computational Linguistics , S. Li, M. Sun, Y. Liu, H. Wu, K. Liu, W. Che, S. He, and G. Rao (Eds.) , Huhhot, China , pp. 1218–1227 ( eng ). External Links: Link Cited by: 1st item , §3.2 .

## Appendix A Cognitive Intuition

### A.1 A Cognitive Intuition of the compression-meaning tradeoff

The compression-meaning tradeoff refers to the cognitive tension between representing concepts with maximal efficiency (i.e., minimal information) and preserving the semantic richness needed for flexible generalization, inference, and communication. For instance, upon hearing the sentence “There was a large brown Labrador barking loudly near the playground,” a person will often encode a simplified memory, such as “big scary dog near kids.” This is not to suggest that humans cannot recall the full sentence, but rather that we typically retain the most meaningful elements to enable efficient reasoning and generalization; without such abstraction and simplification, leveraging past experience for learning and prediction would be more difficult.

We acknowledge that our metrics, while capturing the information-compression trade-off and geometric efficiency in embedding space, do not directly measure all aspects of human-style conceptual abstraction or reasoning. Our aim is not to claim full equivalence with human cognition (nor do we think anyone can or should make such claims), but rather to provide a quantitative, interpretable proxy that highlights where LLMs and humans converge or diverge in how they compress and organize semantic information. We view these metrics as one lens among many, and we are careful in the paper to frame our findings as providing insights into human-like patterns rather than definitive evidence of human-style conceptual processing.

### A.2 Cognitively-Inspired Inductive Biases

Future models could more closely align with human conceptual structure by incorporating cognitively motivated inductive biases and representational mechanisms. Hierarchical and compositional structure could enable models to capture nested relationships between categories, reflecting the way humans organize knowledge from superordinate to basic-level concepts (e.g., animal → mammal → dog → Labrador). Feature- and relation-based biases could help models focus on meaningful perceptual or functional attributes and relational patterns, rather than relying solely on statistical co-occurrence.

Additionally, theory- or causally grounded priors that draw on humans’ intuitive understanding of how objects interact or behave, could constrain learning in complex domains and support more flexible generalization. Incorporating a hybrid exemplar-rule approach, combining memory of specific examples with abstracted rules, would further approximate human category learning. Modular architectures, in which specialized sub-networks handle different aspects of conceptual representation, could enhance generalization and reduce interference between unrelated features. Finally, meta-learned priors distilled from symbolic or program-based representations offer a way to embed structured, human-like concept hypotheses directly into neural models, allowing them to generalize more like humans across novel situations.

Together, these inductive biases offer a path for models that not only compress information efficiently but also organize knowledge in a manner that mirrors human conceptual richness, capturing graded typicality, family resemblance, and hierarchical relationships. While integrating these biases may trade some compression for fidelity, they provide an exciting opportunity to reduce meaning distortion and bridge the gap between statistical efficiency and human-like conceptual understanding.

## Appendix B Limitations

While this study offers valuable insights, several limitations should be considered. • Our analysis primarily focuses on English; generalizability across languages with different structures is an open question.

• Human categorization data as a benchmark may not fully capture cognitive complexity and could introduce biases.

• Our IB-RDT objective is applied to specific LLMs; other models or representations might behave differently.

• Our analysis is limited to textual input and does not explore image-based representations.

Future work could address these by expanding to other languages, exploring alternative cognitive models, and testing these principles on different architectures or in real-world applications.

## Appendix C Dataset Access Details

The aggregated and digitized human categorization datasets from Rosch (1973a) ; Rosch (1975) ; McCloskey and Glucksberg (1978) are made available in CSV format at: https://huggingface.co/datasets/CShani/human-concepts .

## Appendix D LLM Details

• BERT family: deberta-large, bert-large-uncased, roberta-large ( Devlin et al., 2019 ; He et al., 2021 ; Zhuang et al., 2021 ) .

• QWEN family: qwen2-0.5b, qwen2.5-0.5b, qwen1.5-0.5b, qwen2.5-1.5b, qwen2-1.5b, qwen1.5-1.5b, qwen1.5-4b, qwen2.5-4b, qwen2-7b, qwen1.5-14b, qwen1.5-32b, qwen1.5-72b, qwen2.5-72b ( Bai et al., 2023 ; Yang et al., 2024 ) .

• Llama family: llama-3.2-1b, llama-3.1-8b, llama-3-8b, llama-3-70b, llama-3.1-70b ( Touvron et al., 2023a ; Touvron et al., 2023b ; Grattafiori et al., 2024 ) .

• Phi family: phi-1.5, phi-1, phi-2, phi-4 ( Javaheripi et al., 2023 ; Abdin et al., 2024 ; Abouelenin et al., 2025 ) .

• Gemma family: gemma-2b, gemma-2-2b, gemma-7b, gemma-2-9b ( Team et al., 2024 ; Team et al., 2025 ) .

• Mistral family: mistral-7b-v0.3 ( Jiang et al., 2023 ) .

• GPT family: gpt2, gpt2-medium ( Radford et al., 2019 ) .

• DeepSeek family: DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B, DeepSeek-R1-Distill-Qwen-32B, DeepSeek-R1-Distill-Llama-8B ( DeepSeek-AI, 2025 ) .

• OLMo family: Olmo-7b ( olmo2024 ) .

• ViT family: Clip ViT-B/32, Clip ViT-B/16 ( Radford et al., 2021 ) .

• Classic static embeddings: GloVe, Word2Vec ( Pennington et al., 2014 ; Mikolov et al., 2013a ; Mikolov et al., 2013b ) .

## Appendix E Contextual Prompts and Pooling Strategies

Contextual embeddings of LLMs require feeding words into the model through a prompt. Because tokenizers often split a word into multiple tokens, and since some items in our datasets consist of two or more words, we face a design choice regarding how to aggregate token representations. In our methodology, we adopt average pooling over the actual tokens, ensuring that all subword pieces contribute equally. Figures 4 and 5 reveal that the average pooling strategy achieves consistent performance and demonstrates the tightest distribution, making it the most reliable choice for our research.

For prompts, we selected a neutral template, "This is a {word}. " (with a trailing space), designed to minimize any additional semantic bias on the target item. Figures 6 and 7 show this prompt to balance performance and consistency, making it ideal for baseline comparisons.

In this section, we explore alternative pooling strategies and evaluate a diverse set of prompt templates across multiple models.

##### Pooling Strategies.

We compare four common approaches: • Avg - mean over all tokens representing the word

• First - representation of the first token

• Last - representation of the last token

• Sentence Avg - mean over the full sentence embedding

##### Prompt Templates.

To test robustness, we design eight templates spanning different linguistic framings:

• "This is a {word}."

• "This is a {word}. " (with trailing space)

• "The concept of {word} is"

• "When we think of {word}, we consider"

• "A typical {word} would be"

• "Examples of {word} include"

• "The category {word} contains"

• "One kind of {word} is"

##### Models.

We evaluate eight representative LLMs covering major architectures: • bert-large-uncased (BERT family)

• deberta-large (DeBERTa family)

• gemma-2-2b (Gemma family)

• Llama-3.2-1B (Llama family)

• Mistral-7B-v0.3 (Mistral family)

• phi-2 (Phi family)

• Qwen2.5-1.5B (Qwen family)

• roberta-large (RoBERTa family)

## Appendix F Static vs. Contextual AMI Exploration

To understand how LLMs develop conceptual alignment with human categories, we examine the progression from static to contextual embeddings. Figure 8 presents three complementary views of this progression across different model scales and architectures.

The left subplot shows Static AMI scores, which represent the conceptual alignment achieved by models’ input embeddings before any contextual processing (i.e., the E matrix embeddings of the target word). These scores reveal that even at the most basic level, LLMs encode semantic information that supports human-like categorical grouping. Remarkably, static models like Word2Vec and GloVe achieve static AMI scores that rival the peak contextual performance of modern LLMs, suggesting that fundamental conceptual structure is captured early in the learning process.

The middle subplot displays Average AMI across all layers, providing a measure of overall semantic representation quality throughout the network. This metric shows the typical performance a model achieves across its entire depth, offering insight into how consistently different layers maintain conceptual alignment. The improvement from static to average AMI demonstrates that contextual processing generally enhances rather than diminishes semantic understanding.

The right subplot reveals Peak AMI , representing the optimal conceptual alignment achieved by any single layer. This metric identifies where in the network conceptual understanding is maximized, typically occurring in middle-to-late layers before declining in the final layers. The progression from static to peak AMI shows that contextual processing not only preserves but significantly enhances the conceptual alignment present in static embeddings.

Several key insights emerge from this multi-metric analysis. First, all models demonstrate above-chance alignment even in their static embeddings, confirming that basic semantic structure is a fundamental property of learned representations. Second, the consistent improvement from static to peak AMI across all model types suggests that contextual processing universally enhances conceptual understanding rather than creating it de novo. Third, encoder architectures of different types (BERT, ViT encoders, and static models) achieve comparable or superior performance to much larger decoder models, highlighting that architectural factors and pre-training objectives significantly influence conceptual alignment quality beyond mere model scale.

This analysis complements the main text findings by showing that LLMs do not simply achieve above-chance alignment with human categories but rather so through a systematic progression from basic to sophisticated conceptual representations, with contextual processing serving as an amplifier rather than a generator of semantic understanding.

We also tested the robustness of our results to different clustering seeds (Figure 9 ). We found AMI to be highly stable across seeds, with negligible variation in the peak values and layer-wise profiles, indicating that our conclusions are not sensitive to the choice of clustering initialization.

Lastly, we plot the peak AMI against the number of FLOPS per token and find no systematic correlation, suggesting that computational cost alone does not predict human-aligned conceptual representations (Figure 10 .)

## Appendix G Multilingual Analysis

To further explore conceptual understanding across languages, we translated our dataset into Spanish, German, Italian, and Russian using Google Translate’s API and repeated our analyses with the same LLMs and methods. In RQ1, a clear scale effect emerges for all non-English languages, while English shows no such trend (Figures 11 , 12 ). We interpret this as a consequence of limited non-English training data: larger models are more likely to have been exposed to sufficient multilingual data, improving their conceptual alignment. In RQ2, all models struggle to preserve the internal geometry of human concepts across languages (Figure 13 ). RQ3 shows that non-English languages exhibit greater compression (Figure 14 ), consistent with our explanation for RQ1: smaller exposure to non-English data leads to more compressed representations, reducing flexibility and interpretability.

## Appendix H Training Dynamics

The OLMo analysis examines how semantic structure develops during training by analyzing 57 intermediate checkpoints from the OLMo-7B model, representing evenly spaced sampling (every 10K training steps) spanning from 1K to 557K steps (covering approximately 4B to 2.5T tokens).

The analysis employs two complementary sampling strategies: representative sampling (6 checkpoints) captures major developmental phases at 1K, 101K, 201K, 301K, 401K, and 501K steps, while high-resolution sampling (57 checkpoints) reveals the inherent noise and fluctuations in training. Despite significant training noise, the overall semantic development follows a stable, predictable pattern captured by the representative sampling, as shown in Figure 16 . The complete training trajectory with all 57 checkpoints is presented in Figure 17 .

Moreover, this double-phase dynamics occurs when testing attention sparsity, effective rank, and ℒ \mathcal{L} values (Figures 18 , 19 ). Meaning, all of which exhibit the same early rapid shift followed by a slower restructuring phase. This convergence across independent metrics indicates that the model is not merely improving categorical alignment, but reorganizing its internal representations toward increasingly efficient structure.

## Appendix I Datasets Polysemy

Scope. We quantify lexical ambiguity in our psycholinguistic stimuli by counting the distinct WordNet synsets associated with each lemma. This polysemy score lets us estimate how many alternative senses a model must implicitly conflate when it produces a single embedding for a word.

Why it matters. Consider bat , which can denote either a flying mammal or a piece of sports equipment. The same vector must account for both senses. Aggregating semantically distant senses can blur the representation and thus confound model-human comparisons, especially in tasks that rely on fine-grained semantic similarity. Explicitly tracking polysemy allows us to verify that any performance effects we observe are not artefacts of lexical ambiguity.

Results Figure 20 shows the distribution of polysemy scores. The majority of items are unambiguous (1-2 senses), but a heavy-tailed minority (e.g. Running (52 senses), Saw (28), Block (28)) is highly polysemous. This suggests that our findings are due to real differences between the models rather than polysemy-related artifacts. An additional 141 lemmas that are not in WordNet were omitted.

][t]

## Appendix J Tokenizer Analysis

Rational. The tokenizer of a model has a significant influence over the representations: segmentation rules (WordPiece vs. BPE), vocabulary size and special control tokens can inflate sequence length, skew frequency statistics, and shape error patterns. To ensure fair cross-model comparisons, we therefore (i) cluster checkpoints by the tokenizer they use and (ii) quantify how much those tokenizers overlap when applied to our datasets.

Procedure. Before computing overlap, we normalize the vocabulary, stripping tokenizer-specific characters; SentencePiece prefixes (_), GPT-style BPE space prefixes ( Ġ/ġ ) and newline markers ( Ċ ), WordPiece continuations markers (##), and related block characters. After this cleanup, tokens differing only by such prefixes collapse to a shared canonical form (e.g. _house , Ġhouse , and ##house all become house ). We then compute pair-wise Jaccard similarity on these cleaned vocabularies.

Table 1 summarizes the core statistics and information regarding the tokenizer types, while Figure 21 visualizes the resulting pairwise vocabulary overlap.

Findings. We find that most tokenizer families share substantial lexical overlap, often exceeding 60 % \,60\% , suggesting a de-facto common token inventory across recent open-source models. First-generation BERT WordPiece (bert-large-uncased and bert-base-uncased) are an outlier, sharing under 16 % 16\% of tokens with any other group.

##### Model Clustering By Tokenizer Family

• Llama: Llama-3.2-1B (representative), Llama-3.1-8B, Meta-Llama-3-8B, Llama-3.1-70B, Meta-Llama-3-70B

• Gemma: gemma-2-9b (representative), gemma-7b, gemma-2b, gemma-2-2b

• Mistral: Mistral-7B-v0.3 (unique)

• Phi: phi-2 (representative), phi-1, phi-1.5

• RoBERTa: roberta-large (unique)

• DeBERTa: deberta-large (unique)

• GPT : gpt2-medium (representative), gpt2

• BERT: bert-large-uncased (representative), bert-base-uncased

• Qwen: Qwen1.5-0.5B (representative), Qwen1.5-1.8B, Qwen1.5-14B, Qwen2-0.5B, Qwen2-7B, Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-32B, Qwen1.5-32B, phi-4 3 3 3 phi-4 has a different tokenizer than the rest of Phi family. The results of its tokenizer match the tokenizer of the Qwen family.

## Appendix K Additional Clustering Metrics

To further validate our cluster alignment findings (Section 5.1 ), in addition to Adjusted Mutual Information (AMI) and the Normalized Mutual Information (NMI), we also computed the Adjusted Rand Index (ARI) for the k-means clusters derived from LLM embeddings against human-defined categories. ARI measures the similarity between two data clusterings, correcting for chance. Like AMI, a score of 1 indicates perfect agreement and 0 indicates chance agreement.

Across all tested LLMs, the ARI and NMI scores largely mirrored the trends observed with AMI, showing significantly above-chance alignment with human categories and similar relative model performances. Silhouette scores, while more variable, generally indicated reasonable cluster cohesion for both LLM-derived and human categories. Detailed tables of these scores are provided below.

These supplementary metrics reinforce the conclusion that LLMs capture broad human-like conceptual groupings.

## Appendix L Mini-Controlled Experiment (Matched Training Data)

To evaluate the extent to which dataset differences might account for the architectural patterns we report, we conducted matched-family analyses involving the only model families that can be aligned in both training data: GPT, Pythia, Cerebras, and T5. While these comparisons cannot rule out all confounds, they substantially reduce the influence of dataset variation. Across all matched settings, encoder models continue to outperform decoder models, yielding higher AMI and lower ℒ \mathcal{L} . This indicates that the architectural effects observed throughout the paper cannot be explained by differences in training data alone.

## Appendix M Detailed AMI Scores per Model and Dataset

Table 2 provides a more granular view of the static AMI scores for each LLM across the three individual psychological datasets.

## Appendix N Correlation between Human Typicality Judgments and LLM Internal Cluster Geometry

The following tables present the Spearman correlation coefficients ( ρ \rho ) between human typicality judgments and LLM internal representations across different analysis approaches:

Table 3 : Static analysis correlations using embeddings from the E matrix. This approach captures the baseline semantic relationships between items and categories without contextual processing.

Table 4 : Peak AMI layer analysis correlations using contextual embeddings from the layer that maximized AMI scores (as identified in RQ1). This approach leverages the optimal layer for semantic clustering to assess fine-grained semantic fidelity.

Both tables present correlations across three cognitive science datasets: Rosch (1973), Rosch (1975), and McCloskey (1978), with asterisks (*) indicating statistically significant correlations ( p < 0.05 p<0.05 ). The modest correlation values across most models suggest limited alignment between LLM internal representations and human-perceived semantic nuances.

## Appendix O Typicality and Cosine Similarity [RQ2]

Figure 25 shows representative scatter plots illustrating the relationship between human typicality scores (or psychological distances) and the LLM-derived item-centroid cosine similarities for selected categories and models. These plots visually demonstrate the often modest correlations discussed in Section 5.2 .

Figure 26 shows the aggregated Spearman correlation across model families and datasets. These correlations are very weak and mostly non-significant.

## Appendix P Theoretical Extreme Case Exploration for ℒ \mathcal{L}

In the case where | C | = | X | |C|=|X| (each data point is a cluster of size 1 1 , so | C c | = 1 ​ ∀ c ∈ C |C_{c}|=1\ \forall c\in C ), then H ⁡ ( X | C ) = 1 | X | ​ ∑ c ∈ C 1 ⋅ log 2 ⁡ 1 = 0 H(X|C)=\frac{1}{|X|}\sum_{c\in C}1\cdot\log_{2}1=0 . The distortion term σ c 2 = 0 \sigma_{c}^{2}=0 for each cluster as the item is its own centroid. Thus, ℒ = I ⁡ ( X , C ) + β ⋅ 0 = H ⁡ ( X ) − H ⁡ ( X | C ) = H ⁡ ( X ) = log 2 ⁡ | X | \mathcal{L}=I(X;C)+\beta\cdot 0=H(X)-H(X|C)=H(X)=\log_{2}|X| . This represents the cost of encoding each item perfectly without any compression via clustering, and zero distortion.

In the case where | C | = 1 |C|=1 (one cluster C X C_{X} contains all | X | |X| data points, so | C C X | = | X | |C_{C_{X}}|=|X| ), then H ⁡ ( X | C ) = 1 | X | ​ | X | ​ log 2 | X | = log 2 ⁡ | X | H(X|C)=\frac{1}{|X|}|X|\log_{2}|X|=\log_{2}|X| . Thus, I ⁡ ( X , C ) = H ⁡ ( X ) − H ⁡ ( X | C ) = log 2 ⁡ | X | − log 2 | X | = 0 I(X;C)=H(X)-H(X|C)=\log_{2}|X|-\log_{2}|X|=0 . This represents maximum compression (all items are treated as one). The distortion term becomes β ⋅ 1 | X | ​ | X | ⋅ σ X 2 = β ⋅ σ X 2 \beta\cdot\frac{1}{|X|}|X|\cdot\sigma_{X}^{2}=\beta\cdot\sigma_{X}^{2} , where σ X 2 \sigma_{X}^{2} is the variance of all items X X with respect to the global centroid of X X . So, ℒ = 0 + β ⋅ σ X 2 = β ⋅ σ X 2 \mathcal{L}=0+\beta\cdot\sigma_{X}^{2}=\beta\cdot\sigma_{X}^{2} . This represents the scenario of maximum compression where the cost is purely the distortion incurred by representing all items by a single prototype.

## Appendix Q Compression Figures

Figure 28 depicts the IB-RDT objective ( ℒ \mathcal{L} ) vs. K K . Lower ℒ \mathcal{L} indicates a more optimal balance between compression ( I ⁡ ( X , C ) I(X;C) ) and semantic fidelity (distortion). Human categories (fixed K K ) show higher ℒ \mathcal{L} values.

## Appendix R Complexity-Distortion Ratio (on the importance of β \beta )

Figure 29 provides an additional sensitivity analysis in which we examine the ratio between the distortion and complexity components of ℒ \mathcal{L} as β \beta varies. Across all three datasets, encoder models maintain flat profiles, indicating stable conceptual structure under compression, whereas decoder models exhibit stronger shifts, reflecting greater reallocation of representational capacity.

## Appendix S ℒ \mathcal{L} objective vs. downstream task performance

Analysis of 13 instruction-tuned models across 5 families (Qwen, Llama, Gemma, Phi, Mistral; see Table 5 for results) indicates no statistical significance ( r = − 0.202 r=-0.202 , p = 0.508 p=0.508 ). This finding suggests that while the ℒ \mathcal{L} objective successfully identifies models that compress semantic categories more effectively, this compression ability does not directly translate to improved performance on standard NLP benchmarks. The lack of correlation implies that concept compression and benchmark accuracy represent distinct aspects of model capability, with the former capturing semantic organization efficiency and the latter measuring general knowledge and reasoning abilities. We specifically chose instruction-tuned models to ensure fair comparison on MMLU, as base models would likely perform poorly on this instruction-following benchmark. While our analysis covers a diverse range of model families and sizes, this represents a subset of available models due to the limited availability of instruction-tuned variants.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
