##### Report GitHub Issue

Content selection saved. Describe the issue below:

# LiveMathematicianBench : A Live Benchmark for Mathematician-Level Reasoning with Proof Sketches

###### Abstract

Mathematical reasoning is widely regarded as a hallmark of human intelligence, and determining whether large language models (LLMs) can meaningfully perform it remains a central question in artificial intelligence and cognitive science. As LLMs are increasingly integrated into scientific workflows, rigorous evaluation of their mathematical capabilities becomes a practical necessity. Existing mathematical reasoning benchmarks, however, are often limited by synthetic problem settings and growing contamination from widely circulated datasets.

We present LiveMathematicianBench , a dynamic multiple-choice benchmark for evaluating research-level mathematical reasoning using recent arXiv papers published after model training cutoffs. By grounding evaluation in newly published theorem statements, the benchmark provides a more realistic testbed for assessing whether models can reason about natural mathematical claims beyond memorized benchmark patterns. LiveMathematicianBench introduces a taxonomy of thirteen problem categories based on the logical form of theorem statements, enabling fine-grained evaluation across reasoning types such as implication, equivalence, existence, and uniqueness. It further introduces a proof-sketch-guided distractor generation pipeline, in which proof sketches are used to construct plausible but invalid answer choices that reflect misleading proof directions. This design makes the benchmark more sensitive to genuine mathematical understanding rather than surface-level answer matching. We additionally introduce a substitution-resistant evaluation mechanism designed to distinguish answer recognition from substantive mathematical reasoning.

Evaluation of frontier models shows that the benchmark is far from saturated: the best-performing model, Gemini-3.1-pro-preview, achieves only 43.5% accuracy in the standard setting. Under substitution-resistant evaluation, accuracy drops sharply across all models: GPT-5.4 achieves the highest score at 30.6%, while Gemini-3.1-pro-preview falls to 17.6%, below the 20% random baseline. A dual-mode protocol comparing performance with and without proof-sketch access reveals that sketches yield consistent gains (e.g., +13.6 pp for Gemini-3.1-pro-preview), suggesting that models can leverage high-level proof strategies to improve reasoning.

Overall, LiveMathematicianBench offers a scalable and contamination-resistant testbed for studying research-level mathematical reasoning in large language models.

## 1 Introduction

As large language models (LLMs) become increasingly integrated into scientific workflows, evaluating their reasoning ability has become a central challenge. Mathematics is a natural domain for this evaluation because it combines precise logical structure with verifiable ground truth. Yet existing benchmarks, including GSM8K ( Cobbe et al., 2021 ) , MATH ( Hendrycks et al., 2021 ) , AIME, MathVista ( Lu et al., 2023 ) , Omni-Math ( Gao et al., 2024 ) , and OlympiadBench ( He et al., 2024 ) , are largely synthetic, competition-based, or historically sourced, and are increasingly susceptible to contamination. These limitations reduce their value for assessing research-level mathematical reasoning in frontier models.

The core limitation lies in the fundamental mismatch between “Olympiad-style” competition mathematics and authentic mathematical research. Existing benchmarks predominantly feature calculation-heavy problems that reward heuristic pattern matching and the use of specialized tricks to obtain a closed-form answer. Although challenging, such tasks do not reflect the true nature of mathematics research.

By research-level mathematics , we mean open-ended, non-routine mathematical reasoning that is characterized by abstraction, sensitivity to technical hypotheses, and the lack of a pre-specified solution strategy. Such work often requires one to reason through layers of definitions, infer subtle logical dependencies, and identify the right conceptual framework in which a problem can even be meaningfully posed. A central difficulty of research lies not only in proving statements, but also in determining what the right question is to ask and what potential statement might be true in the first place. Unlike competition problems, naturally arising research questions do not come with a contrived setup, an intended solution path, or even a clear indication of which tools are relevant. Progress therefore often requires exploration under substantial uncertainty, familiarity with prior literature, and occasional conceptual innovations, which are sometimes sparked by ideas from seemingly unrelated fields of mathematics.

This gap is visible even at the level of theorem comprehension. A model that can solve routine calculus or algebra problems may still fail to track the precise hypotheses of a modularity lifting theorem, a stability result in geometric invariant theory, or a compactness theorem in nonlinear PDE, where small changes in local conditions, regularity assumptions, or finiteness hypotheses can fundamentally alter the statement. Therefore, to truly assess an LLM’s potential as a scientific research assistant, evaluation must shift from measuring the ability to ”solve exams” toward measuring the ability to comprehend, interpret, and reason about mathematical hypotheses and statements.

This conceptual mismatch is compounded by a second problem: data contamination. State-of-the-Art (SOTA) models have reached saturation on standard benchmarks, often exceeding 90% accuracy, yet this performance is brittle. Studies suggest that many problems have leaked into pre-training corpora, allowing models to memorize solution templates rather than derive answers from first principles ( Glazer et al., 2024 ) . Consequently, performance drops precipitously when questions are rephrased or numerical values altered. This reliance on static, potentially contaminated datasets necessitates a shift toward continuous and refreshable evaluations grounded in authentic research artifacts.

Notably, Zhang et al. (2025) introduced RealMath, a benchmark derived directly from arXiv papers to reduce contamination risk. While RealMath reduces contamination risk and demonstrates that LLMs can engage with research-derived material, its construction prioritizes theorem types that admit straightforward automated verification. As a result, it covers only a limited subset of research-level mathematical reasoning, with less support for tasks involving inequalities, asymptotic relations, or non-constructive arguments, excluding common research tasks such as establishing asymptotic bounds in analysis, deriving classification results in algebraic geometry, or determining modes of convergence in probability. These limitations suggest that the central challenge is not only to control contamination risk in benchmarks, but to do so without collapsing research mathematics into a narrowly verifiable subset of problems of limited width and depth.

To address these limitations, we introduce LiveMathematicianBench , a benchmark framework that expands evaluation along two dimensions: the diversity of mathematical reasoning it captures and the use of high-level proof strategies, enabling evaluation beyond statement-level recognition to strategy-level mathematical reasoning.

For the first dimension, we introduce a taxonomy of thirteen distinct problem types defined by the underlying logical forms and tailor question design to each type. Unlike RealMath, whose questions are restricted to settings with a single uniquely verifiable answer, this framework enables evaluation of mathematical skills that are central to research practice but often considered too ambiguous for automated metrics. These include Logical Structure (distinguishing necessary vs. sufficient conditions via Equivalence and Implication), Qualitative Analysis (establishing Inequalities and Asymptotic bounds), and Generalization (validating Universal quantifiers and structural Bijections).

For the second dimension, we incorporate proof sketches into the benchmark. A proof sketch is a high-level outline of the main ideas and strategic steps of a proof, omitting most technical details. Access to this proof structure makes question construction more targeted and more diagnostic: instead of merely testing whether a model can retrieve a theorem statement, it allows us to design questions about the same result that probe deeper structural understanding. Without such proof-aware design, questions are more likely to be too easy or to reward memorization and surface-level pattern matching. Proof sketches also enable a dual-mode evaluation protocol, where models are assessed both with and without access to high-level proof guidance. This makes it possible to measure whether strategic hints improve mathematical reasoning, and how effectively current models can use them.

Building on these two design principles, we introduce the LiveMathematicianBench , a dynamic benchmark designed to assess LLMs on research-level mathematical reasoning. Each item is presented as a multiple-choice question ( MCQ ) with five answer options, exactly one of which is correct. Our contributions fall into three categories: benchmark construction, methodological novelty, and scientific questions enabled by the benchmark.

Our contributions are threefold. 1) We present a contamination-resistant benchmark for research-level mathematical reasoning, built from dynamically sourced post-cutoff arXiv theorems, organized by a logic-based taxonomy, and augmented with curated proof sketches. 2) We introduce a proof-aware benchmark construction methodology, including category-specific question design, sketch-adversarial distractor generation, and dual-mode evaluation with and without sketch access. 3) We establish a new testbed for studying higher-level mathematical reasoning in LLMs, including logical-form-specific failure modes, the use of proof-level guidance, and progress beyond theorem recognition toward proof planning.

## 2 Methods

Our benchmark construction pipeline transforms raw arXiv papers into calibrated research-level multiple-choice questions (MCQs). The pipeline contains seven stages: (1) paper retrieval, (2) L a T e X source extraction, (3) theorem extraction and classification, (4) MCQ generation, (5) stem-only triviality filtering, (6) hardness calibration, and (7) model evaluation. Each stage is designed to preserve mathematical fidelity while increasing question discriminativeness and benchmark difficulty. Human validation is performed at every stage to ensure quality control (see Appendix B for details).

Stage 1: Paper Retrieval. We query the arXiv API for papers submitted within a target month under the math.* category. The retrieval window is incrementally widened until a configurable maximum number of papers is collected. For each paper, we record its arXiv identifier, submission link, source link, and title. By restricting retrieval to papers published strictly after a model’s training cutoff, we ensure that the resulting benchmark is contamination-free by construction.

Stage 2: L a T e X Source Extraction. For each retrieved paper, we download its e-print source archive and extract the constituent .tex files. The extractor resolves \input and \include directives to reconstruct the complete document in its logical order, strips L a T e X comments and comment environments, and concatenates the result into a single full-text representation. This produces a clean, self-contained L a T e X corpus suitable for downstream parsing.

Stage 3: Theorem Extraction and Classification.

Stage 3a: Hybrid Agentic Extraction. Extracting well-formed theorem statements from raw L a T e X is nontrivial due to the heterogeneity of document styles, custom macros, and cross-referencing conventions. We adopt a hybrid agentic extraction architecture that balances throughput with robustness:

1. Rule-based fast path. A rule-based extractor restricts its search to the Introduction section, exploiting the convention that a paper’s main theorem is formally stated there. Within the introduction, it identifies all theorem-like environments declared via \newtheorem in the preamble (excluding remark -type environments) and applies a priority ranking : the standard theorem environment is selected first; only if no theorem block is found does the extractor fall back to custom environments. This design ensures that auxiliary results such as lemmas, propositions, or corollaries, which may appear elsewhere in the introduction, are not mistakenly extracted in place of the main theorem.

2. Agentic fallback. When the rule-based path fails (e.g., due to an absent Introduction heading or unconventional formatting), an LLM-based agentic extractor is invoked over a larger document window. The extraction prompt explicitly instructs the model to return at most one primary theorem-level claim and to prefer theorem environments over lemma , proposition , or corollary when multiple candidates appear, maintaining the same main-theorem priority as the rule-based path.

3. L a T e X normalization. Custom commands ( \newcommand , \def ) are expanded in-line so that downstream modules receive standard mathematical notation.

4. Reference resolution. Internal cross-references ( \ref , \eqref ) are resolved by collecting all labeled environments and substituting their content, producing an Expanded Theorem that is semantically self-contained.

5. Context recovery. A two-layer retrieval mechanism assembles the notational and definitional context needed to make the theorem self-contained. First , within the Introduction, paragraph blocks preceding the theorem are scored by (i) token overlap with the theorem statement, (ii) the presence of definitional cues (e.g., “let,” “denote,” “suppose”), (iii) mathematical content density, and (iv) positional proximity, with the two blocks immediately before the theorem always retained. The top-scoring blocks are selected and concatenated in their original order. Second , a full-paper pass extracts high-value anchor terms from the theorem and scans the entire document for blocks containing definitions, setup, or preliminaries, scoring them by anchor-term hits, section-heading relevance (e.g., Setup , Preliminary ), and distance to the theorem. Finally, any content referenced via \ref or \eqref within the selected blocks is resolved and appended, and the combined context is trimmed to a character budget.

Stage 3b: Proof-sketch summarization. A large language model extracts a concise proof sketch for each theorem, capturing the high-level strategy without full formal detail. These sketches serve a dual purpose: they inform adversarial distractor generation (Stage 4) and enable sketch-aware evaluation (Stage 7).

Stage 3c: Logical Taxonomy of Theorems. Each extracted theorem is classified into one of thirteen logical categories, listed in Table 1 . Classification is performed by a specialized LLM-based classifier. This taxonomy enables fine-grained diagnosis of model reasoning failures across distinct logical forms.

Stage 4: Question–Answer Pair Generation. Stage 4 synthesizes adversarial MCQs via a two-stage generative protocol , each informed by the theorem’s logical category and the proof sketch.

Stage 4a: Question Stem and Correct Choice. A key design principle is that every question should read as a genuine research-type question about a specific mathematical object or property, rather than a generic request such as “which is the correct result below.” To this end, the generator selects one of thirteen category-specific system prompts , one for each logical type in Table 1 , each prescribing a tailored stem formulation that exercises the distinguishing logical feature of the category. For example, an equivalence-type theorem is transformed into a question that presents one side of the biconditional and asks “which statement is equivalent to A A ?”; an implication-type theorem embeds all hypotheses in the stem and asks “which is the strongest conclusion about … that holds under these assumptions?”, etc. With the strongest quantifier, we ensure there is a unique answer for questions of all logical types.

Each prompt further instructs the model to (i) isolate a single decisive mathematical feature of the conclusion, such as quantifier scope, sharp bound, exact dependence, existence versus uniqueness, or asymptotic regime, rather than restating the theorem verbatim, and (ii) define any paper-specific objects or notation inline so that the question is self-contained. Red-flag checks automatically reject stems containing trivializing phrases (e.g., “which of the following is the strongest result”) or correct options that bundle multiple theorem clauses, triggering a regeneration pass. Finally, a repair pass re-examines the draft stem and, operating in theorem_only_repair mode, injects any missing definitions or notation from the recovered paper context (Stage 3, Step 5) to guarantee self-containedness without leaking answer-relevant information.

Stage 4b: Sketch-Adversarial Distractor Generation. The model receives the theorem, proof sketch, question stem, and correct choice, and generates four distractors (Options B–E). The proof sketch plays a critical role: by exposing the “load-bearing” logical steps of the argument (e.g., the dependence of constants on hidden parameters, a critical case split, or a uniformity condition that distinguishes effective from non-effective bounds), the generator is guided to engineer distractors that exploit specific mathematical constraints or misconceptions. Each distractor is constructed by one of four general perturbation strategies:

• Controlled perturbation. A small surface-level modification to the theorem’s conclusion, such as an altered constant, exponent, inequality direction, or parameter range.

• Semantic weakening. A statement that is plausible but strictly weaker than the theorem’s conclusion, e.g., dropping a uniformity requirement or restricting the domain.

• Semantic strengthening. A statement that overstates the conclusion beyond what is proven, e.g., adding uniqueness, higher regularity, or optimality not asserted by the theorem.

• Property confusion. A statement concerning a closely related but non-equivalent mathematical object or property, e.g., swapping an L 2 L^{2} norm for an L ∞ L^{\infty} norm, or confusing pointwise convergence with uniform convergence.

The concrete realization of each strategy is category-dependent : the distractor prompt is tailored to the theorem’s logical type (Table 1 ). For instance, for an equivalence-type theorem the controlled perturbation modifies a quantifier within one side of the biconditional, whereas for a bound-type theorem it alters the exponent or direction of the inequality; for an existence-type theorem the semantic strengthening adds uniqueness not stated in the theorem, whereas for a classification-type theorem it replaces the bijection with a mere surjection. This category-aware design ensures that distractors probe the decisive logical feature specific to each theorem type, rather than relying on generic, one-size-fits-all perturbations. An adversarial revision pass subsequently re-examines the generated distractors, auditing them for surface-level distinguishability from the correct option and rewriting any that can be rejected without genuine mathematical inspection.

Substitution-Resistant Option Design. A common shortcut exploited by strong models is option substitution : systematically plugging each candidate answer back into the question stem and verifying consistency, rather than deriving the answer through genuine mathematical reasoning. Process-of-elimination strategies similarly bypass comprehension by narrowing choices through superficial cues. To counteract both shortcuts, we introduce a substitution-resistant mechanism: for a configurable fraction of generated items, the correct option is replaced with the meta-option “One of the remaining options is correct, but a stronger result can be proven.” Answering correctly now requires the model to (i) identify the valid option among the distractors and (ii) independently determine whether a strictly stronger result holds, a task that demands substantive mathematical reasoning about the relative strength of claims and cannot be resolved by mechanical substitution or elimination alone.

Quality Rubric. Each generated MCQ undergoes a quality evaluation scored on a 0 0 – 8 8 rubric comprising four dimensions: • Answer Leakage Score (ALS, 0–2): Measures whether the correct answer is inadvertently revealed by the question stem or distractor phrasing.

• Tautology Avoidance Score (TAS, 0–2): Assesses whether the correct option is trivially true or self-evident without mathematical knowledge.

• Generative Pressure Score (GPS, 0–2): Evaluates whether distractors exert sufficient “pressure” to discriminate genuine understanding from guessing.

• Distractor Quality Score (DQS, 0–2): Rates the mathematical plausibility, precision, and diversity of the distractors.

MCQs that do not meet a minimum aggregate threshold (5) are discarded.

Stage 5: Rote-Recall Prevented Triviality Filter. Stage 5 ensures that the remaining questions are not trivially solvable from the question stem alone, without reference to the answer choices. A judge model receives only the question stem (with all options withheld) and generates a free-form response. A second judge then determines whether this response matches the correct answer (Option A). Questions for which the stem alone reveals the answer are classified as stem-trivial and excluded from the final candidate pool. This filter prevents the benchmark from rewarding rote recall and ensures that genuine option-level reasoning is required.

Stage 6: Hardness Calibration. Stage 6 ensures that the final benchmark is genuinely difficult for state-of-the-art models through a three-step calibration pipeline:

Step 1: Overgenerate Hard Pool. For each stem-nontrivial item, we retain both the original distractor set and one regenerated alternative set, thereby doubling the candidate pool per source theorem. This overgeneration increases the likelihood of retaining at least one maximally challenging variant.

Step 2: First-Pass Accuracy Test. A frontier model is evaluated on the entire candidate pool at moderate reasoning effort. Items that the model answers correctly are flagged as potentially too easy.

Step 3: Source-Level Hardest Selection. For each source theorem, the pipeline compares all surviving candidate variants and selects the hardest , defined as the variant the calibration model answered incorrectly while achieving the highest quality rubric score. Source groups in which all candidates were solved are dropped entirely. This procedure yields the final benchmark subset.

Stage 7: Evaluation Protocol. We propose a dual-mode evaluation protocol: Mode 1: Selection. The model receives the question stem and all five options, then selects the answer that it judges to be the correct theorem statement. This mode evaluates the model’s baseline mathematical comprehension. Mode 2: Sketch-Aware Selection. The model additionally receives the proof sketch as a hint alongside the stem and options. By comparing performance across modes, we isolate the model’s ability to synthesize and apply high-level proof strategies, a proxy for mathematical intuition .

To ensure a fair rendering of notations, all questions undergo L a T e X validation via compilation and, when necessary, automated L a T e X repair before presentation to the model.

## 3 Benchmark

We summarize the logical-form composition of the hard benchmark split in Figure 3 . The hard split contains 177 theorems in total, and a single theorem may belong to multiple logical categories. The benchmark therefore covers a broad range of theorem structures rather than concentrating on a single template: implication and universal statements are the most common categories, followed by existence and inequality/bound problems. The month-level breakdown further shows that benchmark composition changes over time while preserving category diversity, with all slices drawn from papers released after the evaluated models’ knowledge cutoffs. Examples can be found in the Appendix C .

## 4 Evaluation Results

#### Even frontier models suffer.

Figure 1 shows overall accuracy on LiveMathematicianBench . The strongest performance is achieved by Gemini-3.1-pro-preview at 43.5% overall, followed by GPT-5.4 (high) at 41.8%. Even the strongest systems remain far from saturation.

#### Category-wise pattern and monthly trajectories.

Figure 4 -(a) shows that no single model dominates every reasoning type. Gemini-3.1-pro-preview achieves the strongest overall profile and is particularly competitive on biconditional/equivalence and classification/bijection problems, whereas GPT-5.4 variants are stronger on implication, universal, and inequality/bound items. These categories combined constitute a substantial portion of the benchmark (Figure 3 ). This heterogeneity suggests that research-level mathematical reasoning is not a one-dimensional capability: models with similar aggregate performance can still exhibit sharp weaknesses on particular logical forms. The monthly trajectories in Figure 4 -(b) further show that performance is unstable across benchmark slices. Several models do best on the 2026/01 subset but perform worse again on the 2026/02 subset.

#### Substitution-resistant options sharply reduce accuracy.

Figure 5 -(a) compares model accuracy on the original-choice subset and the substitution-resistant subset, where the correct answer is replaced by a stronger meta-option intended to frustrate shortcut strategies such as direct substitution and surface-level elimination. Across all evaluated systems, the substitution-resistant setting is substantially harder than the original-choice setting. The strongest original-choice performance is achieved by Gemini-3.1-pro-preview at 67.4%, but its accuracy drops to only 17.6% on substitution-resistant items, below the 20% random-guess baseline. GPT-5.4 provides a useful contrast: although it ranks second overall, it reaches 52.2% on original items under both medium and high reasoning effort and still retains 29.4%–30.6% on the substitution-resistant subset. GPT-5.4 is therefore more stable under the harder choice design, remaining above the random-guess baseline even when the benchmark removes the direct theorem statement as an option, whereas most other evaluated models fall to chance level or below. More broadly, the remaining difficulty in LiveMathematicianBench lies not only in understanding the theorem itself, but also in reasoning among nearby mathematical claims once surface matching and answer substitution become ineffective.

#### Proof sketches yields a consistent improvement.

As shown in Figure 5 -(b), GPT-5.4 (high) improves from 41.8% to 53.7% overall, a gain of 11.9% points, while Gemini-3.1-pro-preview (high) rises from 43.5% to 57.1%, a gain of 13.6% points. This pattern suggests that proof sketches are not merely redundant restatements of the theorem. Instead, they provide useful strategic information that helps models disambiguate closely related answer choices and identify the load-bearing structure of the argument.

## 5 Endnote and Discussion

From aggregate accuracy alone, Gemini-3.1-pro-preview (high) achieves the highest score, with GPT-5.4 variants close behind by less than 3%. However, a category-level analysis in Section 4 (Fig. 4 (a)) reveals additional structure that supports the first central design choice of LiveMathematicianBench : organizing problems by logical type. Performance varies meaningfully across logical forms in ways that are not visible from aggregate scores alone. This suggests that logical structure may be an important axis along which current models differ, and it raises a broader interpretability question: why are some models systematically stronger on certain forms of reasoning than others? If such patterns persist at scale, they may also have practical implications for mathematical workflows, since different models may prove more useful for different kinds of reasoning tasks. In this sense, a logic-based taxonomy complements traditional field-based categorization by capturing structural similarities that cut across mathematical areas. More broadly, this suggests that LiveMathematicianBench can serve not only as a leaderboard benchmark, but also as a diagnostic testbed for studying structure-specific strengths and weaknesses in mathematical reasoning. This diagnostic value is especially relevant because the benchmark is constructed from recent post-cutoff arXiv papers, making it less vulnerable to rapid saturation and contamination than static mathematics benchmarks. In this sense, LiveMathematicianBench contributes not only a new dataset, but also a more durable evaluation setting for tracking progress in research-level mathematical reasoning.

Substitution-resistant options (Stage 4b) are designed to test whether a model can recognize that the semantically weakened option is true while also inferring that a strictly stronger statement follows from the hypotheses. Success on such questions therefore requires an additional deductive step. In this sense, substitution-resistant questions provide a useful probe of whether a model can move beyond recognition toward a limited form of mathematical conjecturing. This is precisely the kind of ability mathematicians hope AI systems may leverage on when facilitating research, as illustrated by the work of Georgiev et al. (2025) using AlphaEvolve for mathematical exploration and discovery. As highlighted in Section 4 , all tested models perform substantially worse with substitution-resistant options (Fig. 5 (a)). This gap suggests that current models rely heavily on option substitution in standard multiple-choice settings. More importantly, it underscores the importance of adversarial option design for isolating genuine reasoning ability. At its core, it shows that benchmark design can materially affect the capabilities we appear to measure. From considerations of both overall benchmark performance and performance under substitution-resistant evaluation, GPT-5.4 (high) and Gemini-3.1-pro-preview (high) emerge as the two strongest models on LiveMathematicianBench .

Finally, we have observed earlier that providing proof sketches at inference time induces significant performance improvements in the two highest-scoring models (Fig. 5 (b)). Since proof sketches are extracted from the source papers and typically summarize the central ideas of the proof at a high level, this result suggests that models can often use strategic mathematical guidance without full derivational detail, demonstrating some similarities to how expert researchers work. These findings further support the second design philosophy of LiveMathematicianBench : incorporating proof strategy into evaluation rather than restricting assessment to statement-level recognition alone. More broadly, they indicate that the benchmark can distinguish not only whether a model reaches the correct answer, but also how its performance changes when supplied with information closer to the level of mathematical strategy used by human researchers. Collectively, these features make LiveMathematicianBench useful not only for comparing current models, but also for future work on proof-guided reasoning, tool use, and interactive mathematical exploration.

## References

Abouzaid et al. (2026) M. Abouzaid, A. J. Blumberg, M. Hairer, J. Kileel, T. G. Kolda, P. D. Nelson, D. Spielman, N. Srivastava, R. Ward, S. Weinberger, and L. Williams First proof . External Links: 2602.05192 , Link Cited by: Appendix A .

Bi and Zhou (2025) Y. Bi and J. Zhou Quantitative stability of the clifford torus as a willmore minimizer . External Links: 2511.19681 , Link Cited by: Appendix C .

Cobbe et al. (2021) K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman Training verifiers to solve math word problems . arXiv preprint arXiv:2110.14168 . Cited by: Appendix A , §1 .

Frieder (2023) S. Frieder Mathematical capabilities of chatgpt . arXiv preprint arXiv:2301.13867 . Cited by: Appendix A .

Gao et al. (2024) B. Gao, F. Song, Z. Yang, Z. Cai, Y. Miao, Q. Dong, L. Li, C. Ma, L. Chen, R. Xu, et al. Omni-math: a universal olympiad level mathematic benchmark for large language models . arXiv preprint arXiv:2410.07985 . Cited by: Appendix A , §1 .

Georgiev et al. (2025) B. Georgiev, J. Gómez-Serrano, T. Tao, and A. Z. Wagner Mathematical exploration and discovery at scale . External Links: 2511.02864 , Link Cited by: §5 .

Giesler (2026) J. Giesler Jacobian rings and the infinitesimal torelli theorem . External Links: 2601.17765 , Link Cited by: Appendix C .

Glazer et al. (2024) E. Glazer, E. Erdil, T. Besiroglu, D. Chicharro, E. Chen, A. Gunning, C. F. Olsson, J. Denain, A. Ho, E. d. O. Santos, et al. Frontiermath: a benchmark for evaluating advanced mathematical reasoning in ai . arXiv preprint arXiv:2411.04872 . Cited by: Appendix A , §1 .

Grabbel et al. (2026) T. Grabbel, G. Martin, G. Mezzedimi, M. R. von Frentz, and P. J. Schmidt On symmetries of hyperbolic lattices of large rank . External Links: 2602.05652 , Link Cited by: Appendix C .

Gulati et al. (2025) A. Gulati, B. Miranda, E. Chen, E. Xia, K. Fronsdal, B. Dumont, E. Obbad, and S. Koyejo Putnam-axiom: a functional and static benchmark for measuring higher level mathematical reasoning in llms . arXiv preprint arXiv:2508.08292 . Cited by: Appendix A .

He et al. (2024) C. He, R. Luo, Y. Bai, S. Hu, Z. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, et al. Olympiadbench: a challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 3828–3850 . Cited by: Appendix A , §1 .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt Measuring mathematical problem solving with the math dataset . arXiv preprint arXiv:2103.03874 . Cited by: Appendix A , §1 .

Kala and Prakash (2026) V. Kala and O. Prakash There are consecutive cubic fields with large class numbers, when ordered by discriminant . External Links: 2601.03984 , Link Cited by: Appendix C .

Kaplan (2025a) E. Kaplan A note on the ketonen order and lipschitz reducibility between ultrafilters . External Links: 2512.12835 , Link Cited by: Appendix C .

Kaplan (2025b) E. Kaplan The number of normal measures, revisited . arXiv preprint arXiv:2507.20466 . Cited by: Appendix C .

Lu et al. (2023) P. Lu, H. Bansal, T. Xia, J. Liu, C. Li, H. Hajishirzi, H. Cheng, K. Chang, M. Galley, and J. Gao Mathvista: evaluating mathematical reasoning of foundation models in visual contexts . arXiv preprint arXiv:2310.02255 . Cited by: §1 .

Marques and Trojovsky (2025) D. Marques and P. Trojovsky Geometric progressions meet zeckendorf representations . External Links: 2512.19586 , Link Cited by: Appendix C .

Mejía et al. (2025) J. F. A. Mejía, I. Chifan, D. Osin, and B. Sun McDuff superrigidity for group ii 1 {}_{1} factors . External Links: 2511.23123 , Link Cited by: Appendix C .

Mendonça et al. (2025) W. Mendonça, M. Miralaei, and G. O. Mota Graphs with asymmetric ramsey properties . External Links: 2511.02963 , Link Cited by: Appendix C .

Moraga and Zúñiga (2026) J. Moraga and J. P. Zúñiga Degenerations of cluster type varieties . External Links: 2511.14959 , Link Cited by: Appendix C .

Mu and Wang (2025) Y. Mu and D. Wang Global existence for the relativistic vlasov-poisson system in a two-dimensional bounded domain . External Links: 2511.06595 , Link Cited by: Appendix C .

Ozawa (2026) M. Ozawa Crossing numbers of knots on closed surfaces . External Links: 2602.21659 , Link Cited by: Appendix C .

Sawada et al. (2023) T. Sawada, D. Paleka, A. Havrilla, P. Tadepalli, P. Vidas, A. Kranias, J. J. Nay, K. Gupta, and A. Komatsuzaki Arb: advanced reasoning benchmark for large language models . arXiv preprint arXiv:2307.13692 . Cited by: Appendix A .

Tang and Zhang (2025) Q. Tang and S. Zhang Harmonic lcm patterns and sunflower-free capacity . External Links: 2512.20055 , Link Cited by: Appendix C .

Tsoukalas et al. (2024) G. Tsoukalas, J. Lee, J. Jennings, J. Xin, M. Ding, M. Jennings, A. Thakur, and S. Chaudhuri Putnambench: a multilingual competition-mathematics benchmark for formal theorem-proving . In AI for Math Workshop@ ICML 2024 , Cited by: Appendix A .

Wang (2025) J. Wang Non-negative scalar curvature on spin surgeries and novikov conjecture . External Links: 2512.16535 , Link Cited by: Appendix C .

XTX Markets (2024) XTX Markets The ai mathematical olympiad (aimo) prize . Note: Accessed: 2024-05-01 External Links: Link Cited by: Appendix A .

Zhang et al. (2025) J. Zhang, C. Petrui, K. Nikolić, and F. Tramèr RealMath: a continuous benchmark for evaluating language models on research-level mathematics . arXiv preprint arXiv:2505.12575 . Cited by: §1 .

Zheng et al. (2021) K. Zheng, J. M. Han, and S. Polu Minif2f: a cross-system benchmark for formal olympiad-level mathematics . arXiv preprint arXiv:2109.00110 . Cited by: Appendix A .

## Appendix A Related Work

#### Standard and Advanced Mathematical Benchmarks

The evaluation of mathematical reasoning in large language models has traditionally relied on static datasets spanning elementary to undergraduate-level problems. Early benchmarks such as GSM8K ( Cobbe et al., 2021 ) and MATH ( Hendrycks et al., 2021 ) helped establish common evaluation standards for quantitative and symbolic reasoning. As model performance has improved, however, these benchmarks have become less discriminative for frontier systems.

Subsequent work has therefore shifted toward more challenging settings. The Advanced Reasoning Benchmark (ARB) ( Sawada et al., 2023 ) and GHOSTS ( Frieder, 2023 ) extend evaluation toward graduate-level mathematics, with GHOSTS further emphasizing natural language interaction and expert assessment. Other efforts focus on competition-level mathematics, including OlympiadBench ( He et al., 2024 ) , PutnamBench ( Tsoukalas et al., 2024 ) , and Omni-Math ( Gao et al., 2024 ) . These benchmarks substantially increase difficulty, but because they are derived from historical competition archives, they may be more susceptible to contamination from pretraining data and benchmark-specific memorization.

#### Contamination Mitigation, Formal Mathematics, and Frontier-Level Evaluation

Several recent benchmarks attempt to mitigate contamination more directly. Putnam-AXIOM ( Gulati et al., 2025 ) perturbs existing problems through programmatic modifications such as renaming variables or altering constants. While this strategy can reduce exact overlap with known solutions, it preserves much of the original problem structure. The AI Mathematical Olympiad (AIMO) ( XTX Markets, 2024 ) instead introduces newly created olympiad-style problems, and MiniF2F ( Zheng et al., 2021 ) focuses on formally verified mathematics across theorem proving systems such as Lean and Isabelle. These directions address important aspects of evaluation reliability, but they remain centered on competition-style or formalized problem settings.

Moving beyond competition settings, First Proof ( Abouzaid et al. (2026) ) curates a collection of ten original, research-level problems drawn directly from the authors’ active work. While this approach effectively guarantees the absence of data contamination, the extremely small sample size limits its utility as a comprehensive evaluation benchmark.

FrontierMath ( Glazer et al., 2024 ) is more closely related to our setting in that it targets highly difficult mathematics under reduced contamination risk through a larger set of expert-authored problems. However, similar to First Proof, tailored problem authoring requires substantial dedicated human effort, which inherently limits scalability.

LiveMathematicianBench differs in both construction and evaluation emphasis. Rather than relying on manually authored problems, it draws from a continuously growing stream of recent arXiv papers, enabling a scalable and refreshable benchmark construction pipeline. In addition, whereas prior benchmarks largely emphasize answer derivation, our framework explicitly evaluates structural comprehension through theorem-level logical categories and proof-sketch-guided distractors that probe sensitivity to plausible but invalid reasoning directions.

## Appendix B Human Validation Protocol

All prompts used in theorem extraction, classification, question generation, and filtering were authored by a research-level mathematician. For quality control, the final released set of 177 benchmark items was reviewed for theorem fidelity, self-containedness, answer uniqueness, and distractor quality. To audit upstream pipeline quality, we additionally performed stratified reviews of intermediate outputs, sampling approximately 10 cases per logical category for theorem extraction, category assignment, proof-sketch quality, and MCQ generation. Given the unusual breadth and depth of the mathematical content covered by the pipeline, these reviews were intended as benchmark quality control, assessing whether outputs were mathematically sound, internally consistent, and benchmark-ready, rather than as full peer-review-level sense of independent verification of every source-paper claim.

We now provide an example demonstrating how the combination of prompt design and human validation ensures that all distractors are demonstrably false, thereby guaranteeing the overall validity of the MCQs.

In Appendix C , Example C is generated from an Existential-Universal type theorem, and the correct option generated from the theorem is replaced by the correct substitution-resistant option. When generating distractors, the system prompt (see Appendix G , Stage 4b) forces the LLM to include a meta description for each distractor indicating the type of perturbation strategies used in its construction. For Example C , the meta description reads:

"meta": { "weaker_true_label": "C", "false_labels": [ "B", "D", "E" ], "wildcard_false_label": "B" }, "sketch_usage_meta": [ { "label": "B", "sketch_hook_type": "counting_estimate", "tampered_component": "counts signed cubic discriminants instead of cubic fields", "template_used": "wildcard" }, { "label": "C", "sketch_hook_type": "finiteness", "tampered_component": "dropped the lower bound guaranteeing at least k/2 cubic fields in the interval", "template_used": "weaker_true" }, { "label": "D", "sketch_hook_type": "counting_estimate", "tampered_component": "threshold k/2 replaced by (k+1)/2", "template_used": "stronger_trap" }, { "label": "E", "sketch_hook_type": "regularity", "tampered_component": "removed the epsilon-loss in the exponent", "template_used": "stronger_trap" } ]

We first notice that option C is the ”weaker_true_label”, meaning that it is strictly weaker than the theorem’s assertion (which is always true if we assume the theorem itself is true). However, since the question asks for the ’strongest’ true statement, option C is not correct.

Option B is the ”wildcard_false_label”, meaning that it is designed to be false but with a question specific tempering. It counts the number of integers within that range that are determinants of cubic fields. This is clearly not the same as counting the number of cubic fields, as multiple non-isomorphic fields can share the same discriminant. Therefore, it is not realistic for a smaller set to have the same lower bound. This reasoning aligns with the ”tempered_component” field provided in the meta description. Moreover, this option critically uses the proof sketch.

Option D and E are false labels tempered with ”stronger_trap”, meaning that they are strengthened versions of the theorem statement in different ways. Option D increases the lower bound of the set being counted, making the statement stronger. However, the lower bound is obtained by explicit construction and a bigger lower bound cannot be achieved. Option E modifies the count for the specific integers d d by removing the epsilon factor in the exponent. The epsilon-dependence in the original theorem comes from deep conjectures in the subject of counting number fields, which cannot be removed.

To conclude, taking the original theorem as the ground truth, we can see from a combination of meta description and human expertise that the distractors are false and the MCQ is valid. In particular, this example demonstrates that our prompt design alone has guaranteed the mathematical falsity of the distractors to a great extent.

## Appendix C Detailed Logical Taxonomy of Theorem Categories

This appendix provides extended descriptions of the thirteen logical theorem categories listed in Table 1 . The taxonomy focuses exclusively on the logical form of a theorem statement, independent of its mathematical topic or context. Each category is accompanied by its canonical logical form and a representative example.

#### 1. Algorithmic / Constructive.

Canonical form: There exists an algorithm A A that computes f ⁡ ( x ) f(x) , or “object X X can be explicitly constructed.” This category covers theorems providing an explicit or computable method to obtain an object. Example: “There exists a polynomial-time algorithm that computes a maximum matching in any bipartite graph.”

#### 2. Asymptotic / Limit.

Canonical form: As n → ∞ n\to\infty (or another limiting regime), a quantity behaves as described. This category covers theorems describing limiting or asymptotic behavior, including exact limits, asymptotic equivalences ( ∼ \sim ), and big- O O /little- o o estimates. Example: “The number of primes less than x x satisfies π ⁡ ( x ) ∼ x / ln ⁡ x \pi(x)\sim x/\ln x as x → ∞ x\to\infty .”

#### 3. Biconditional / Equivalence.

Canonical form: A ⇔ B A\iff B , or “the following are equivalent.” This category covers theorems asserting that two (or more) conditions are logically equivalent. The theorem may present the equivalence as a single biconditional or as a list of mutually equivalent statements. Example: “A ring R R is Noetherian if and only if every ideal of R R is finitely generated.”

#### 4. Classification / Bijection.

Canonical form: There is a bijection between X X and Y Y , or “objects of type A A are completely classified by objects of type B B .” This category covers theorems establishing a one-to-one correspondence or a complete classification between two classes of mathematical objects. Example: “Finite simple groups are classified into cyclic groups of prime order, alternating groups, groups of Lie type, and 26 26 sporadic groups.”

“yields a both computational and much explicit perspective.” Under the assumptions of the main theorem, one “easily deduce[s] ker ⁡ ( d ​ 𝒫 B , f k ) = ker ⁡ ( d ​ 𝒫 B , f 1 ) , k ≥ 1 \ker(d\mathcal{P}_{B,f}^{k})=\ker(d\mathcal{P}_{B,f}^{1}),\quad k\geq 1 We record the precise statement as follows. Corollary . Under the assumption of theorem we have ker ⁡ ( d ​ ϕ f ) = ker ⁡ ( d ​ ϕ f 1 ) . \ker(d\phi_{f})=\ker(d\phi_{f}^{1}). For an element g = g Γ ​ ( f ) ⋅ x w ∈ ker ⁡ ( d ​ 𝒫 f 1 ) g=g_{\Gamma}(f)\cdot x^{w}\in\ker(d\mathcal{P}_{f}^{1}) one obtains the distinction ⟨ w , n Γ ⟩ = { 0 ⇔ g ≡ 0 , − 1 ⇔ g ∈ ker ⁡ ( κ f ) , ≤ − 2 exceptional cases, \langle w,n_{\Gamma}\rangle=\begin{cases}0&\Leftrightarrow\ g\equiv 0,\\ -1&\Leftrightarrow\ g\in\ker(\kappa_{f}),\\ \leq-2&\text{exceptional cases,}\end{cases} and also “ ⟨ w , n Γ ′ ⟩ ≥ 0 \langle w,n_{\Gamma^{\prime}}\rangle\geq 0 for Γ ′ ≠ Γ \Gamma^{\prime}\neq\Gamma by the main theorem.” The “last case” ⟨ w , n Γ ⟩ ≤ − 2 \langle w,n_{\Gamma}\rangle\leq-2 “causes Φ f | Im ⁡ κ f \Phi_{f|{\operatorname{Im}\,\kappa_{f}}} to be not injective, which implies in particular that the infinitesimal Torelli theorem (ITT) fails.” For n = 3 n=3 , to rule out the exceptional case and conclude injectivity, the text sketches: “we construct a 3 3 -dimensional empty polytope Q Q with 6 6 vertices,” namely “the convex span of an empty triangle with vertex ( 0 , 0 , 0 ) (0,0,0) and this triangle dilated by w w ,” and then “use a theorem of White on empty 3 3 -simplices to deduce | Q ∩ M | ≥ 7 |Q\cap M|\geq 7 under the assumption ⟨ w , n Γ ⟩ ≤ − 2 \langle w,n_{\Gamma}\rangle\leq-2 , contradiction.”

#### 5. Existence.

Canonical form: ∃ x \exists\,x such that P ⁡ ( x ) P(x) . This category covers theorems guaranteeing that at least one object with a given property exists, without claiming uniqueness. Example: “There exists a continuous, nowhere-differentiable function on [ 0 , 1 ] [0,1] .”

#### 6. Existential–Universal.

Canonical form: ∃ x ​ ∀ y , P ⁡ ( x , y ) \exists\,x\;\forall\,y,\;P(x,y) . This category covers theorems asserting the existence of an object (often a constant, function, or parameter) that “works” uniformly for all elements of a given class. The existential quantifier precedes the universal one. Example: “There exists a constant C > 0 C>0 such that for all f ∈ L 2 ​ ( ℝ ) f\in L^{2}(\mathbb{R}) , ‖ f ‖ ∞ ≤ C ​ ‖ f ‖ H 1 \|f\|_{\infty}\leq C\,\|f\|_{H^{1}} .”

#### 7. Implication.

Canonical form: A ⟹ B A\implies B , or “if P P holds, then Q Q holds.” This category covers theorems in which a set of hypotheses implies a specific conclusion, without asserting the converse. Example: “If f f is a continuous function on a closed interval [ a , b ] [a,b] , then f f is uniformly continuous on [ a , b ] [a,b] .”

#### 8. Independence / Consistency.

Canonical form: T ⊬ P T\not\vdash P and T ⊬ ¬ P T\not\vdash\neg P , or “statement P P is independent of axiom system T T .” This category covers theorems expressing a meta-mathematical statement that a proposition cannot be proved or refuted from given axioms. Example: “The Continuum Hypothesis is independent of ZFC.”

#### 9. Inequality / Bound.

Canonical form: f ⁡ ( x ) ≤ g ⁡ ( x ) f(x)\leq g(x) (or ≥ \geq , < < , > > ), holding universally. This category covers theorems providing a quantitative estimate, such as a uniform bound, norm inequality, or comparison between quantities. Example: “For all f ∈ L 1 ​ ( ℝ ) ∩ L 2 ​ ( ℝ ) f\in L^{1}(\mathbb{R})\cap L^{2}(\mathbb{R}) , ‖ f ^ ‖ 2 = ‖ f ‖ 2 \|\hat{f}\|_{2}=\|f\|_{2} .”

#### 10. Nonexistence.

Canonical form: ∄ x \not\exists\,x such that P ⁡ ( x ) P(x) (or equivalently, ∀ x , ¬ P ⁡ ( x ) \forall\,x,\;\neg P(x) ). This category covers theorems asserting that no object satisfies a given property. Example: “There does not exist a rational number whose square is 2 2 .”

#### 11. Uniqueness.

Canonical form: ∃ ! x \exists!\,x such that P ⁡ ( x ) P(x) . This category covers theorems asserting both existence and uniqueness of an object satisfying a given property. Example: “For every positive definite matrix A A , there exists a unique positive definite matrix B B such that B 2 = A B^{2}=A .”

#### 12. Universal.

Canonical form: ∀ x , P ⁡ ( x ) \forall\,x,\;P(x) . This category covers theorems asserting that a property holds for every object in a specified class. Example: “Every finite-dimensional real vector space admits an inner product.”

#### 13. Universal–Existential.

Canonical form: ∀ x ​ ∃ y , P ⁡ ( x , y ) \forall\,x\;\exists\,y,\;P(x,y) . This category covers theorems asserting that for every object in a class, there exists an associated object satisfying a property. The existential witness may depend on the universally quantified variable. Example: “For every ε > 0 \varepsilon>0 , there exists δ > 0 \delta>0 such that | f ⁡ ( x ) − f ⁡ ( a ) | < ε |f(x)-f(a)|<\varepsilon whenever | x − a | < δ |x-a|<\delta .”

## Appendix D Benchmark Composition Across Construction Stages

Figure 6 summarizes how the benchmark size changes across the main construction stages for each month. Full denotes the complete post-generation candidate pool, Quality Rubric > 5 >5 denotes the subset retained after the rubric-based quality filter, and Hard denotes the final released split after stem-nontrivial filtering and hardness calibration. The figure shows that the pipeline consistently reduces the candidate pool in a structured way rather than through ad hoc pruning: each month begins from a substantially larger generated set, is narrowed by quality control, and is then further distilled into a compact hard benchmark.

## Appendix E Evaluation Implementation Details

This section documents the released evaluation implementation in LiveMathematicianBench/eval/ . The current repository provides three backend-specific entry points: eval.py for Azure OpenAI models, eval_claude.py for Claude models accessed through the Anthropic API, and eval_vllm.py for models served through an OpenAI-compatible vLLM endpoint. Despite backend-specific client code and usage accounting, the three scripts share the same hard-set loader, prompt template, deterministic choice shuffling, answer parser, correctness rule, and output JSON structure.

#### Benchmark file format.

For each evaluation month, the scripts load the hard benchmark split from data/<month>/hard/qaEval_<month>_ge5_hard.json . Each JSON item contains a unique identifier and an mcq object with a question stem, one correct_choice , four distractors in choices , and auxiliary metadata such as mcq.meta.score . During evaluation, the released scripts consume the finalized mcq fields only; source theorem context, sketches, and other record-level annotations remain in the benchmark file but are not inserted into the released prompts.

#### Prompt construction.

Evaluation is implemented as a five-way multiple-choice selection task. For each item, the scripts combine the stored correct choice with the four distractors, then apply a deterministic shuffle using a per-item seed equal to the global seed plus the item’s dataset index. The shuffled options are relabeled as A – E . The model then receives a fixed system prompt instructing it to act as an expert mathematician, reason step by step, and place its final answer inside \boxed{} . The user prompt contains only two blocks: 1. the question stem from mcq.question ; and

2. the five relabeled answer choices.

The choices are formatted as “ (A) ... ”, “ (B) ... ”, and so on, separated by blank lines. All models were evaluated in the without-sketch setting. Due to budget constraints, we additionally ran sketch-aware evaluation only for the few models that performed best in the without-sketch setting.

#### Answer extraction and scoring.

After generation, the scripts recover the model’s predicted label by first searching for the last occurrence of \boxed{A} through \boxed{E} . If no boxed answer is found, the parser falls back to either a one-character response in A – E or, failing that, the last standalone capital letter in A – E . In the Azure and vLLM evaluators, answer extraction is applied directly to the returned response text. In the Claude evaluator, the Anthropic response is split into text and thinking blocks; the final prediction is extracted from the text block, while the thinking block is recorded separately. An item is marked correct iff the extracted label matches the post-shuffle label of the ground-truth option. Monthly accuracy is then computed as correct/total over the evaluated hard split.

#### Execution details.

All evaluators parallelize item-level inference with a ThreadPoolExecutor controlled by --concurrency . They also support repeated sampling through --n ; in that case each question is answered multiple times, a full per-sample list is stored under samples , and the top-level prediction fields intentionally mirror the first sample for backward compatibility. For every sample, the scripts record elapsed time, prompt tokens, completion tokens, total tokens, and reasoning-token counts whenever the backend exposes them.

The backend-specific command-line options differ as follows. The Azure evaluator requires --endpoint and --api-key , accepts --api-version , exposes both a client-wide --timeout and a per-sample --request-timeout , and optionally switches from chat completions to the Responses API through --use-responses-api ; this switch is also enabled automatically when the model name contains gpt-5.4 . The Claude evaluator requires --base-url , accepts --api-key , supports --thinking-budget to request extended thinking, and exposes --debug , --timeout , and --request-timeout . The vLLM evaluator requires --base-url , accepts an optional --api-key , exposes --temperature , --top-p , --debug , --timeout , and --request-timeout , and also supports optional --use-responses-api with automatic activation for model names containing gpt-5.4 .

Token accounting is normalized across backends. Azure records usage directly from the provider response. Claude and vLLM additionally normalize completion_tokens so that, when reasoning-token metadata is available, the reported completion count includes both visible output tokens and reasoning tokens, matching the OpenAI-style accounting used elsewhere in the benchmark.

#### Resuming and result serialization.

All scripts support fault-tolerant resumption through --resume . If an output file already exists, the evaluator loads the previous JSON, skips items whose prior record has a non- None model_answer and no recorded error, and re-runs unanswered or failed items only. Results are written to results/<month>/accuracy_test_<model>_<month>_<effort>.json , where model names are sanitized for filesystem safety and <effort> defaults to default when no reasoning level is specified. Each output file contains (i) test_info metadata such as model name, month, seed, maximum token budget, number of samples, and timestamps; (ii) duplicated aggregate accuracy summaries under summary.all and overall ; and (iii) detailed_results records containing the item identifier, extracted model_answer , shuffled correct_answer , raw_response , correctness flag, latency, token usage, reasoning_tokens , reasoning effort, n_samples , optional per-sample samples , auxiliary mcq.meta.score , and any backend error message. For Claude runs, each record additionally stores raw_thinking extracted from the Anthropic thinking block.

## Appendix F Additional Evaluation Results

### F.1 Sketch-Aware Accuracy with Substitution-Resistant Settings

Built upon the sketch-aware evaluation results in Figure , we further analyze how the presence of proof sketches interacts with and without substitution-resistant question formulations. We break down sketch-aware gains, separating standard multiple-choice questions from substitution-resistant items. Figure 7 shows that proof sketches improve performance in both settings, but the magnitude of the gain depends on the model and the choice style. GPT-5.4 benefits more strongly on the original-choice subset, whereas Gemini-3.1-pro-preview shows especially large gains on the substitution-resistant subset. This suggests that proof-level guidance can help models not only identify the correct theorem statement, but also reason through adversarial answer formulations designed to resist shortcut strategies.

### F.2 Cost Analysis

Accuracy alone does not capture how practical a model is for benchmark-scale evaluation. Figure 8 shows that the accuracy-cost frontier is led by GPT-5.4 rather than by the highest-token models. Gemini-3.1-pro-preview achieves the top accuracy at 43.5%, but it requires about 15.3k average completion tokens. By contrast, GPT-5.4 (high) reaches a similar 41.8% accuracy with only about 7.0k tokens, and GPT-5.4 (medium) remains close at 41.2% with about 3.8k tokens. In other words, GPT-5.4 combines high accuracy with materially lower token cost, while several other long-generation models, such as Qwen and Kimi, use far more tokens without matching GPT-5.4 or Gemini in accuracy.

At the same time, several open-weight or alternative frontier systems occupy distinct efficiency niches. Qwen3.5-397B-A17B and Kimi-K2.5 achieve mid-tier accuracy at higher token budgets, while GPT-oss-120b generates even more tokens without matching the top closed-model accuracy band. This pattern suggests that improvements in research-level mathematical reasoning cannot be reduced to simply allocating more inference budget: architectural and training differences still materially affect how efficiently models convert tokens into correct mathematical judgments.

## Appendix G Prompt Details

We provide below some examples of system prompts used in our construction pipeline. We will focus on prompts used in Stage 4 (Question-Answer Pair Generation) as it best demonstrates the methodological novelty of LiveMathematicianBench .

To show case our category-specific system prompts, we include prompts from two categories: biconditional/equivalence and implication as they are representative of our central design philosophy.

#### Stage 4a: Question Stem and Correct Choice Generation.

#### Stage 4b: Sketch-Adversarial Distractor Generation.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
