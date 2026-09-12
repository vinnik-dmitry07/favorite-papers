##### Report GitHub Issue

Content selection saved. Describe the issue below:

# RIFT: A RubrIc Failure Mode Taxonomy and Automated Diagnostics

###### Abstract

Rubric-based evaluation is widely used in LLM benchmarks and training pipelines for open-ended, less verifiable tasks. While prior work has demonstrated the effectiveness of rubrics using downstream signals such as reinforcement learning outcomes, there remains no principled way to diagnose how a rubric itself fails from such aggregated or downstream signals alone. To address this gap, we introduce RIFT: RubrIc Failure mode Taxonomy , a taxonomy for systematically characterizing failure modes in rubric composition and design. RIFT consists of eight failure modes organized into three high-level categories: Reliability Failures , Content Validity Failures , and Consequential Validity Failures . RIFT is developed using grounded theory by iteratively annotating rubrics drawn from five diverse data sources spanning general instruction following, code generation, creative writing, and expert-level deep research, until no new failure modes are identified. We evaluate the consistency of the taxonomy by measuring agreement among independent human annotators, observing fair agreement overall ( 87% pairwise agreement and 0.64 average Cohen’s kappa ). Finally, to support scalable diagnosis, we propose automated rubric quality metrics and show that they align with human failure-mode annotations, achieving up to 0.925 F1.

## 1 Introduction

Rubrics have become a central component of recent large language model (LLM) benchmarks and training pipelines, providing rich, interpretable, and scalable evaluation signals. They are widely used in evaluating open-ended generation tasks—ranging from general instruction following ( He et al., 2025 ) to research planning ( Goel et al., 2025 ) , as well as professional applications such as healthcare, law, and finance—where fully verifiable ground truth is often unavailable ( Arora et al., 2025 ; Akyürek et al., 2025 ; Shi et al., 2026 ) . By specifying task-specific textual criteria and scoring model outputs with an LLM-as-a-judge, rubric-based evaluation can substantially improve the alignment between automated rewards and human judgments ( Sirdeshmukh et al., 2025 ) .

Despite their growing importance, principled evaluation of rubric quality remains largely unexplored. Considerable effort has been devoted to designing human annotation workflows ( Akyürek et al., 2025 ) and to automatically generating rubrics ( Viswanathan et al., 2025 ; Xie et al., 2025 ; Liu et al., 2026 ; Rezaei et al., 2025 ) , but the quality of the resulting rubrics is rarely assessed. Instead, rubric quality is typically inferred indirectly through downstream performance (e.g., reinforcement learning outcomes) or agreement between rubric-based LLM judges and human preferences. However, such downstream signals conflate rubric quality with other factors, including judge behavior and task formulation, making it difficult to isolate failures caused by the rubric itself. As a result, rubrics produced through heterogeneous pipelines cannot be meaningfully compared, and there is no principled way to characterize how a rubric itself fails .

We introduce RIFT , the RubrIc Failure mode Taxonomy , a taxonomy for diagnosing failures in evaluation rubrics. RIFT is derived through a grounded-theory process ( Glaser and Strauss, 1967b ) based on expert critiques of diverse rubrics drawn from both human-authored and automatically generated sources. Using five representative human-curated and synthetic rubric data sources spanning general instruction following, code generation, creative writing, and expert-level deep research, we identify eight recurring failure modes and organize them into three higher-level dimensions of rubric quality: reliability , content validity , and consequential validity . We also observe systematic differences between human-authored and synthetic rubrics, motivating human-in-the-loop rubric creation that combines broad synthetic coverage with expert refinement. Although the taxonomy is grounded in the rubric collections studied here, the grounded-theory-based construction workflow is general and can be readily applied to new domains and rubric generation procedures.

Beyond defining the taxonomy, we study whether these rubric failures can be identified consistently. We validate RIFT through expert annotation and inter-annotator agreement among three independent human annotators, and further develop automated diagnostics that approximate RIFT labels using a combination of LLM-based classification and agreement- and stability-based signals. These diagnostics enable scalable analysis of rubric quality and make RIFT practical for real-world rubric development and iteration workflows. Our contributions are summarized as follows: • Taxonomy development. We introduce RIFT, a rubric failure-mode taxonomy derived using grounded theory ( Glaser and Strauss, 1967b ) , which identifies eight failure modes organized into three high-level categories: Reliability , Content Validity , and Consequential Validity .

• Systematic empirical grounding. We construct and analyze a dataset of 85 diverse rubrics with 255 expert annotations, drawn from five representative benchmarks and covering both human-authored and automatically generated rubrics.

• Automated diagnostics. We develop scalable automatic signals for detecting RIFT failure modes and achieve high agreement with expert annotations, reaching up to 0.86 F1.

## 2 Related Work

Task-Specific Rubrics as Evaluation. Task-specific rubrics verify LLM performance by using weighted textual criteria, evaluated by an LLM-as-a-judge (LLMaJ) and aggregated into a single reward signal. Rubric-based evaluation improves agreement with human judgments ( Sirdeshmukh et al., 2025 ) and is widely used for benchmarks in unverifiable domains (e.g., healthcare, law, and finance) ( Arora et al., 2025 ; Akyürek et al., 2025 ; Shi et al., 2026 ) and open-ended tasks such as general-purpose instruction following ( He et al., 2025 ) and research planning ( Goel et al., 2025 ) .

Issues With LLM Evaluation Benchmarks. Recent studies show that LLM benchmarks suffer from unreliable outcome verification, including widely used benchmarks such as SWE-bench-Verified and τ \tau -bench ( Chowdhury et al., 2024 ; Yao et al., 2024 ; Zhu et al., 2025b ) . Beyond outcome verification, naive LLM-as-Judge evaluation can introduce systematic bias and overconfident estimates which requires calibrated reporting ( Lee et al., 2026 ) . Prior work also reports substantial evaluation variance ( Madaan et al., 2024 ) and other weaknesses in current benchmarking practices ( Reuel et al., 2024 ; Eriksson et al., 2025 ) , motivating the need for more reliable evaluation design.

Operationalization and Validity in Measurement. RIFT’s three failure categories draw on established measurement-theory concepts. Reliability Failures parallel the problem of operational definitions ( Bridgman, 1927 ; Stevens, 1935 ) : when rubric criteria lack precise operationalizations, different judges interpret them differently, producing inconsistent scores ( Breznau et al., 2022 ; Carpentras, 2024 ) . Content Validity Failures build on the psychometric notion of content validity—whether an instrument adequately represents the construct it measures ( Sireci, 1998 ) —applied here to rubric criteria that miss or misrepresent the evaluation target. Consequential Validity Failures draw on consequential validity ( Iliescu and Greiff, 2021 ) , capturing rubrics whose design enables gaming or low discrimination downstream.

Failure Mode Taxonomy. Constructing failure mode taxonomies via human annotation is a common approach for identifying challenges in LLM-based systems. Zhu et al. (2025a) synthesises human analyses of agent trajectories into a unified failure taxonomy. Ma et al. (2025) and Cemri et al. (2025) further adopt grounded theory ( Glaser and Strauss, 1967a ) to iteratively build failure taxonomies through multi-rater consensus.

Prior work on benchmark reliability has largely focused on verifiable, agentic settings, while rubric-based evaluation in open-ended domains still lacks principled methods for assessing rubric quality in isolation. We therefore focus on evaluating rubric design and composition across datasets, with a particular emphasis on identifying failure modes. To our knowledge, RIFT is the first failure-mode taxonomy specifically designed to uncover structural shortcomings in rubrics themselves.

## 3 The RubrIc Failure mode Taxonomy

We define the RubrIc Failure mode Taxonomy (RIFT) as a generic framework for identifying and classifying failure modes in evaluation rubrics (Tab. 1 ). To avoid imposing a top-down schema, RIFT is developed using grounded theory ( Glaser and Strauss, 1967b ) , in which failure modes are iteratively derived from expert annotations and open-ended feedback. The resulting taxonomy organizes rubric failures into three core categories: Reliability (consistency and reproducibility of judgments; cf. the literature on operational definitions ( Bridgman, 1927 ; Stevens, 1935 ) ), Content Validity (alignment between rubric criteria and the intended evaluation target ( Sireci, 1998 ) ), and Consequential Validity (downstream usefulness and discriminative power of the rubric ( Iliescu and Greiff, 2021 ) ).

Data Sources. To ground the taxonomy in a wide range of settings, we analyze 85 rubrics with 255 expert annotations drawn from five data sources, spanning both human-authored and automatically generated rubrics: • Human-crafted. AdvancedIF ( He et al., 2025 ) provides expert-authored evaluation criteria for complex instruction following in general conversational tasks, and ResearchRubrics ( Sharma et al., 2025 ) focuses on factual grounding and multi-step analytical reasoning for deep research agents.

• Synthetic. WildChecklists ( Viswanathan et al., 2025 ) derives fine-grained rubric requirements from observed failure patterns, OpenRubrics ( Liu et al., 2026 ) constructs rubrics via contrastive analysis of preference pairs, and AutoRubrics ( Xie et al., 2025 ) induces reward-oriented rubrics through symbolic search. Together, these datasets and generation frameworks cover a broad range of domains, including coding and creative writing.

Taxonomy Development with Grounded Theory. We develop RIFT through an iterative process inspired by Grounded Theory, following prior work on failure taxonomies for multi-agent LLM systems ( Cemri et al., 2025 ) and practitioner guide in ( Chun Tie et al., 2019 ) . The process spans four sequential annotation rounds and covers 85 rubrics in total. Ae use purposive sampling to select rubrics from AdvancedIF , ResearchRubrics , WildChecklists , OpenRubrics , and AutoRubrics . These sources were chosen to maximize variation in rubric origin (expert-written or auto-generated), format (checklists, principles, or narrative rubrics), length, and domain. Full details on data composition are provided in Appendix A .

Three experts develop the taxonomy iteratively using standard Grounded Theory practices ( Chun Tie et al., 2019 ) . We use open coding to derive candidate failure modes from open-ended rubric critiques, constant comparative analysis to compare new observations against existing categories, and memoing to record emerging failure modes, boundary cases, and revision decisions. Data collection and analysis proceed concurrently across rounds: each annotation round informs the next revision of the taxonomy. The process continues until saturation condition is reached, which we define as the point at which additional rubrics no longer reveal new failure modes or require substantive taxonomy revisions. We operationalize this process as follows:

1. Bootstrapping (first round only). Experts independently write open-ended rubric critiques for each rubric. These critiques are provided to GPT-5.2 to propose an initial candidate taxonomy.

2. Labeling and feedback. Experts label each rubric using the current taxonomy. They also document failure modes not covered by existing categories and note issues in the taxonomy itself, such as unclear definitions, overlapping categories, or structural inconsistencies.

3. Panel refinement. The three-expert panel reviews all labels, critiques, and feedback, then revises the taxonomy before the next annotation round.

4. Convergence and finalization. The process terminates when experts agree that no new failure modes are emerging and no further rubric-driven taxonomy revisions are needed, yielding the final taxonomy in Tab. 1 .

A full per-source, per-round provenance breakdown is provided in Appendix A .

Validation and Agreement Analysis. We assess theoretical saturation and consistency of RIFT through a final manual annotation round. We observe fair to substantial agreement across identified failure modes, with an average Cohen’s kappa (C- κ \kappa ) of 0.64, Krippendorff’s alpha (K- α \alpha ) of 0.60, and a pairwise agreement rate (PWA) of 87%. A per–failure-mode analysis shows that some categories are more difficult to annotate consistently. In particular, Misaligned or Rigid , which captures cases where a rubric evaluates the wrong objective or imposes overly strict requirements, has the lowest PWA, reflecting variation in annotators’ thresholds for misalignment and strictness. In contrast, annotators show high agreement on the Low Signal category, consistently identifying rubrics that fail to provide sufficient evaluation signal.

Correlation With Human Preferences. Among the five data sources, only OpenRubrics and AutoRubrics provide paired judge-human preference labels, so we restrict this analysis to those two sources. We use judge-human preference agreement as an external validation signal for RIFT and find that rubrics with more RIFT failure mode labels are significantly more likely to exhibit judge–human misalignment (Pearson’s r r = 0.162, p p = 0.0021; average count = 3.66 vs. 3.15, p < p< 1e-4; effective size = 20) failure modes for misaligned vs. aligned cases), providing quantitative evidence that RIFT captures rubric properties relevant to downstream human-aligned evaluation.

Human-Crafted vs Synthetic Comparison. Tab. 2 summarizes the prevalence of RIFT failure modes identified in human-crafted vs. synthetic rubrics. Human-crafted rubrics tend to be more reliable and consequentially valid , but are more often Misaligned or Rigid , reflecting overly strict or incorrect assumptions. Missing Criteria arises in both settings: synthetic rubrics are often encompassing without precision, which can fail to operationalize criteria, while human-crafted rubrics tend to be more specific but can still omit some requirements. These patterns motivate human-in-the-loop rubric creation pipelines that use synthetic generation for broad coverage, then rely on expert review to sharpen and correct misalignments.

## 4 Automated RIFT Evaluators

To enable scalable assessment of rubric quality under RIFT, we develop automated evaluators for each failure mode. We evaluate these signals on an independent test set of 50 rubrics (10 per source, stratified equally across all five data sources) sampled without replacement from rubrics not used during taxonomy development and manually annotated using the RIFT taxonomy. All 50 rubrics are evaluated by every automated signal; for both LLMaJ classifiers (GPT-5.2 and Gemini 3 Pro), each rubric is evaluated by both models. We implement several automated signals and examine how well they align with expert diagnostic labels: • LLM-as-Judge (LLMaJ). A rubric-conditioned failure-mode classifier trained using grounded-theory annotations and the RIFT taxonomy. We report results for two classifiers, GPT-5.2 and Gemini 3 Pro, and provide the taxonomy as part of the prompt (see Appendix C ).

• Majority-Vote LLMaJ (LLMaJ MV). The same rubric-conditioned classifiers run N = 5 N{=}5 times independently per rubric. Per-failure-mode labels are aggregated by strict majority vote: a label is retained only if at least ⌈ N / 2 ⌉ \lceil N/2\rceil runs predict it.

• Inter-rater reliability (IRR). An agreement-based signal computed as pairwise agreement (PWA) over rubric-conditioned preference labels produced by four preference labelers (GPT-5 mini, Claude Haiku 4.5, Gemini 3 Flash, and GPT-5.2.) The preferences are generated over all pairs of responses generated by six models (GPT-5 mini, GPT-5.2, Claude Haiku 4.5, Claude Sonnet 4.5, Gemini 3 Flash, and Gemini 3 Pro.)

• Alignment. An accuracy-based signal measuring how often weaker preference labelers (GPT-5 mini, Claude Haiku 4.5, and Gemini 3 Flash) agree with GPT-5.2 on the same rubric-conditioned response pairs.

• Reward variance. A stability-based signal defined as the variance of the aggregate rubric score produced by a rubric-conditioned LLMaJ (GPT-5.2) over four independent responses generated by GPT-5 mini for each test input.

Alignment with Expert Annotations. Results are reported in Tab. 3 . For each evaluator, failure-mode pair, we report F1 at the threshold that maximizes F1 on the test set. The single-run LLMaJs achieves moderate to good alignment on a subset of failure modes, Subjective and Misaligned or Rigid, but exhibits notable misalignment on Non-Atomic and Hackable. Aggregating N = 5 N{=}5 independent LLMaJ runs via majority vote (LLMaJ MV) typically improves performance on the eight failure modes over the single-run LLMaJ and becomes the best evaluator on four. Majority voting degrades Low Signal and Redundant Criteria, where the non-LLMaJ signals and single-run LLMaJ, respectively, remain the strongest evaluators. GPT-5.2 and Gemini 3 Pro have noticeably different strengths: Gemini 3 Pro is substantially better on Ungrounded (0.634 vs. GPT-5.2’s 0.444) and Subjective (0.909 vs. 0.861), but weaker on Missing Criteria (0.452 vs. 0.686) and Low Signal (0.400 vs. 0.667), indicating that different frontier models surface complementary failure modes. The non-LLMaJ-based methods complement the LLMaJ-based evaluators, and we expect further gains from prompt tuning, curating in-context examples, and combining majority voting with these complementary signals.

Grouping failure modes into reliability, content, and consequential categories highlights observed difficulties of automated rubric-quality evaluation. Reliability failures are identified more accurately, likely because they result in inconsistent rubric-based judgments that non-LLMaJ signals measure directly, and because RIFT definitions provide clear scoring guidance for LLMaJs. In contrast, content and consequential failures require detecting substance gaps or inaccuracies in rubric criteria and anticipating downstream effects.

Pairwise Model Agreement. Tab. 4 reports per failure mode and macro-averaged agreement between three frontier majority-vote LLMaJs (Sonnet 4.5, Gemini 3 Pro, GPT-5.2) on the 50-rubric RIFT test set. Overall cross-model agreement rates range from 0.730 0.730 to 0.812 0.812 and Cohen’s κ \kappa from 0.239 0.239 to 0.494 0.494 . Between Gemini 3 Pro and GPT-5.2, per failure mode, Cohen’s κ \kappa ranges from 0.0 0.0 to 0.573 0.573 . This suggests moderate taxonomy interpretation differences between current frontier models and motivates leveraging experts in the loop for RIFT evaluations on failure modes such as Consequential failure modes with low model agreement.

## 5 Conclusions

We introduced RIFT: a taxonomy for rubric failure modes derived from expert annotations of real evaluation rubrics and iterative refinement. A key takeaway from the RIFT development and annotation process is that synthetic rubrics often provide broad but imprecise coverage, while human-crafted rubrics are typically sharper but can be misaligned or overly rigid. Combining generation with targeted expert review can capture coverage while correcting misalignments.

We also implemented automated RIFT evaluators to detect and label failure modes, enabling scalable analysis. In practice, we envision RIFT supporting an iterative rubric improvement workflow, for instance: (1) diagnose : run automated evaluators to flag likely failure modes for a candidate rubric, (2) review : an expert inspects flagged failures using the taxonomy’s decision rules and confirms or dismisses each, (3) revise : apply targeted fixes guided by the failure mode (e.g., anchor subjective terms with concrete criteria, unbundle non-atomic items into separately scored sub-criteria, or add missing requirements), and (4) validate : re-run the automated signals to verify the revision resolved the flagged issues. We expect expert-in-the-loop workflows to remain important for assessing content and consequential validity. Experts can verify coverage, relevance, and missing criteria (with LLM critics to accelerate annotation ( McAleese et al., 2024 ) ), while consequential validity may require methods that directly measure a rubric’s impact in downstream use cases.

## 6 Limitations

RIFT is not intended to be an exhaustive taxonomy of rubric failure modes. The taxonomy is derived from the rubrics, artifacts, and annotation settings examined in this study, and additional failure modes may emerge in other domains, task formats, or stakeholder contexts. As a result, the current taxonomy should be viewed as a useful but incomplete characterization of rubric breakdown.

The generalizability of RIFT remains only partially validated. Our annotations were conducted on a bounded set of tasks and artifacts, and rubric quality may depend heavily on the application setting, evaluation goal, and stakeholder priorities. Future work should test the taxonomy across a broader range of domains, annotator populations, and use cases.

The annotation process itself is expensive and difficult to scale. Although expert annotation provides high-quality supervision, it is still subject to ambiguity and subjectivity, particularly for abstract rubric properties such as completeness or specificity. This limits both the scale of our study and the reliability with which fine-grained failure modes can be distinguished.

Finally, evaluator alignment with expert judgments still has substantial room for improvement. Agreement with expert labels is only an indirect proxy for practical utility, and future work should more directly measure how identifying different failure modes affects downstream outcomes such as rubric revision quality, evaluator robustness, and benchmark reliability.

## 7 Ethical Statement

Rubrics are often used in high-impact evaluation settings, so errors in rubric design can propagate into misleading judgments, poor model selection, or unfair downstream decisions. Our goal in introducing RIFT is to support more transparent and reliable rubric development by making common failure modes easier to identify and analyze. At the same time, we do not view automated rubric diagnosis as a substitute for human oversight, especially in sensitive or high-stakes applications. We believe expert review remains essential for ensuring that evaluation criteria are appropriate, fair, and aligned with the intended use case.

## References

Akyürek et al. (2025) A. F. Akyürek, A. Gosai, C. B. C. Zhang, V. Gupta, J. Jeong, A. Gunjal, T. Rabbani, M. Mazzone, D. Randolph, M. M. Meymand, G. Chattha, P. Rodriguez, D. Mares, P. Singh, M. Liu, S. Chawla, P. Cline, L. Ogaz, E. Hernandez, Z. Wang, P. Bhatter, M. Ayestaran, B. Liu, and Y. He PRBench: large-scale expert rubrics for evaluating high-stakes professional reasoning . External Links: 2511.11562 , Link Cited by: §1 , §1 , §2 .

Arora et al. (2025) R. K. Arora, J. Wei, R. S. Hicks, P. Bowman, J. Quiñonero-Candela, F. Tsimpourlas, M. Sharman, M. Shah, A. Vallone, A. Beutel, J. Heidecke, and K. Singhal HealthBench: evaluating large language models towards improved human health . External Links: 2505.08775 , Link Cited by: §1 , §2 .

Breznau et al. (2022) N. Breznau, E. M. Rinke, A. Wuttke, H. H. V. Nguyen, M. Adem, J. Adriaans, A. Alvarez-Benjumea, H. K. Andersen, D. Auer, F. Azevedo, et al. Observing many researchers using the same data and hypothesis reveals a hidden universe of uncertainty . Proceedings of the National Academy of Sciences 119 ( 44 ), pp. e2203150119 . External Links: Document Cited by: §2 .

Bridgman (1927) P. W. Bridgman The logic of modern physics . Macmillan , New York . External Links: Link Cited by: §2 , §3 .

Carpentras (2024) D. Carpentras We urgently need a culture of multi-operationalization in psychological research . Communications Psychology 2 ( 1 ), pp. 32 . External Links: Document Cited by: §2 .

Cemri et al. (2025) M. Cemri, M. Z. Pan, S. Yang, L. A. Agrawal, B. Chopra, R. Tiwari, K. Keutzer, A. Parameswaran, D. Klein, K. Ramchandran, M. Zaharia, J. E. Gonzalez, and I. Stoica Why do multi-agent llm systems fail? . External Links: 2503.13657 , Link Cited by: §2 , §3 .

Chowdhury et al. (2024) N. Chowdhury, J. Aung, C. J. Shern, O. Jaffe, D. Sherburn, G. Starace, E. Mays, R. Dias, M. Aljubeh, M. Glaese, C. E. Jimenez, J. Yang, L. Ho, T. Patwardhan, K. Liu, and A. Madry Introducing swe-bench verified . External Links: Link Cited by: §2 .

Chun Tie et al. (2019) Y. Chun Tie, M. Birks, and K. Francis Grounded theory research: a design framework for novice researchers . Open Medicine 7 , pp. 1–8 . External Links: Document Cited by: §3 , §3 .

Eriksson et al. (2025) M. Eriksson, E. Purificato, A. Noroozian, J. Vinagre, G. Chaslot, E. Gomez, and D. Fernandez-Llorca Can we trust ai benchmarks? an interdisciplinary review of current issues in ai evaluation . External Links: 2502.06559 , Link Cited by: §2 .

Glaser and Strauss (1967a) B. G. Glaser and A. L. Strauss The discovery of grounded theory: strategies for qualitative research . Aldine Publishing Company , Chicago . Cited by: §2 .

Glaser and Strauss (1967b) B. G. Glaser and A. L. Strauss The discovery of grounded theory: strategies for qualitative research . Aldine Publishing Company . Cited by: 1st item , §1 , §3 .

Goel et al. (2025) S. Goel, R. Hazra, D. Jayalath, T. Willi, P. Jain, W. F. Shen, I. Leontiadis, F. Barbieri, Y. Bachrach, J. Geiping, and C. Whitehouse Training ai co-scientists using rubric rewards . External Links: 2512.23707 , Link Cited by: §1 , §2 .

He et al. (2025) Y. He, W. Li, H. Zhang, S. Li, K. Mandyam, S. Khosla, Y. Xiong, N. Wang, X. Peng, B. Li, S. Bi, S. G. Patil, Q. Qi, S. Feng, J. Katz-Samuels, R. Y. Pang, S. Gonugondla, H. Lang, Y. Yu, Y. Qian, M. Fazel-Zarandi, L. Yu, A. Benhalloum, H. Awadalla, and M. Faruqui AdvancedIF: rubric-based benchmarking and reinforcement learning for advancing llm instruction following . External Links: 2511.10507 , Link Cited by: §1 , §2 , 1st item .

Iliescu and Greiff (2021) D. Iliescu and S. Greiff On consequential validity . European Journal of Psychological Assessment 37 ( 3 ), pp. 163–166 . External Links: Document Cited by: §2 , §3 .

Lee et al. (2026) C. Lee, T. Zeng, J. Jeong, J. Sohn, and K. Lee How to correctly report llm-as-a-judge evaluations . External Links: 2511.21140 , Link Cited by: §2 .

Liu et al. (2026) T. Liu, R. Xu, T. Yu, I. Hong, C. Yang, T. Zhao, and H. Wang OpenRubrics: towards scalable synthetic rubric generation for reward modeling and llm alignment . External Links: 2510.07743 , Link Cited by: §1 , 2nd item .

Ma et al. (2025) X. Ma, X. Xie, Y. Wang, J. Wang, B. Wu, M. Li, and Q. Wang Diagnosing failure root causes in platform-orchestrated agentic systems: dataset, taxonomy, and benchmark . External Links: 2509.23735 , Link Cited by: §2 .

Madaan et al. (2024) L. Madaan, A. K. Singh, R. Schaeffer, A. Poulton, S. Koyejo, P. Stenetorp, S. Narang, and D. Hupkes Quantifying variance in evaluation benchmarks . External Links: 2406.10229 , Link Cited by: §2 .

McAleese et al. (2024) N. McAleese, R. M. Pokorny, J. F. C. Uribe, E. Nitishinskaya, M. Trebacz, and J. Leike LLM critics help catch LLM bugs . External Links: Link Cited by: §5 .

Reuel et al. (2024) A. Reuel, A. Hardy, C. Smith, M. Lamparth, M. Hardy, and M. J. Kochenderfer BetterBench: assessing ai benchmarks, uncovering issues, and establishing best practices . In Advances in Neural Information Processing Systems , A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang (Eds.) , Vol. 37 , pp. 21763–21813 . External Links: Document , Link Cited by: §2 .

Rezaei et al. (2025) M. Rezaei, R. Vacareanu, Z. Wang, C. Wang, B. Liu, Y. He, and A. F. Akyürek Online rubrics elicitation from pairwise comparisons . External Links: 2510.07284 , Link Cited by: §1 .

Sharma et al. (2025) M. Sharma, C. B. C. Zhang, C. Bandi, C. Wang, A. Aich, H. Nghiem, T. Rabbani, Y. Htet, B. Jang, S. Basu, A. Balwani, D. Peskoff, M. Ayestaran, S. M. Hendryx, B. Kenstler, and B. Liu ResearchRubrics: a benchmark of prompts and rubrics for evaluating deep research agents . External Links: 2511.07685 , Link Cited by: 1st item .

Shi et al. (2026) Y. Shi, H. Liu, Y. Hu, G. Song, X. Xu, Y. Ma, T. Tang, L. Zhang, Q. Chen, D. Feng, W. Lv, W. Wu, K. Yang, S. Yang, W. Wang, R. Shi, Y. Qiu, Y. Qi, J. Zhang, X. Sui, Y. Chen, Y. Zhang, A. Yang, B. Yu, D. Liu, J. Lin, W. Shen, B. Zhao, C. L. A. Clarke, and H. Wei PLawBench: a rubric-based benchmark for evaluating llms in real-world legal practice . External Links: 2601.16669 , Link Cited by: §1 , §2 .

Sirdeshmukh et al. (2025) V. Sirdeshmukh, K. Deshpande, J. Mols, L. Jin, E. Cardona, D. Lee, J. Kritz, W. Primack, S. Yue, and C. Xing MultiChallenge: a realistic multi-turn conversation evaluation benchmark challenging to frontier llms . External Links: 2501.17399 , Link Cited by: §1 , §2 .

Sireci (1998) S. G. Sireci The construct of content validity . Social Indicators Research 45 ( 1 ), pp. 83–117 . External Links: Document Cited by: §2 , §3 .

Stevens (1935) S. S. Stevens The operational definition of psychological concepts . Psychological Review 42 ( 6 ), pp. 517–527 . External Links: Document Cited by: §2 , §3 .

Viswanathan et al. (2025) V. Viswanathan, Y. Sun, S. Ma, X. Kong, M. Cao, G. Neubig, and T. Wu Checklists are better than reward models for aligning language models . External Links: 2507.18624 , Link Cited by: §1 , 2nd item .

Xie et al. (2025) L. Xie, S. Huang, Z. Zhang, A. Zou, Y. Zhai, D. Ren, K. Zhang, H. Hu, B. Liu, H. Chen, Z. Liu, and B. Ding Auto-rubric: learning to extract generalizable criteria for reward modeling . External Links: 2510.17314 , Link Cited by: §1 , 2nd item .

Yao et al. (2024) S. Yao, N. Shinn, P. Razavi, and K. Narasimhan τ \tau -Bench: a benchmark for tool-agent-user interaction in real-world domains . External Links: 2406.12045 , Link Cited by: §2 .

Zhu et al. (2025a) K. Zhu, Z. Liu, B. Li, M. Tian, Y. Yang, J. Zhang, P. Han, Q. Xie, F. Cui, W. Zhang, X. Ma, X. Yu, G. Ramesh, J. Wu, Z. Liu, P. Lu, J. Zou, and J. You Where llm agents fail and how they can learn from failures . External Links: 2509.25370 , Link Cited by: §2 .

Zhu et al. (2025b) Y. Zhu, T. Jin, Y. Pruksachatkun, A. Zhang, S. Liu, S. Cui, S. Kapoor, S. Longpre, K. Meng, R. Weiss, F. Barez, R. Gupta, J. Dhamala, J. Merizian, M. Giulianelli, H. Coppock, C. Ududec, J. Sekhon, J. Steinhardt, A. Kellermann, S. Schwettmann, M. Zaharia, I. Stoica, P. Liang, and D. Kang Establishing best practices for building rigorous agentic benchmarks . External Links: 2507.02825 , Link Cited by: §2 .

## Appendix A Data Source and Sampling Provenance

This appendix summarizes the data sources and sampling procedure used for taxonomy development (Section 3 ) and automated evaluator experiments (Section 4).

### A.1 Data source distribution.

We sample rubrics from five datasets selected to cover variation in rubric origin, format, length, and task domain. Tab. 5 summarizes each source.

### A.2 Sampling.

Rubrics are drawn by stratified uniform random sampling with equal counts per source, without replacement across rounds, and with a fixed random seed per round for reproducibility. The taxonomy development sample contains 85 rubrics across four rounds: Round 1 collects open-ended critiques for bootstrapping, while Rounds 2–4 use the evolving taxonomy for labeling. Each rubric is independently annotated by at least three experts. The test set is drawn independently with the same stratified procedure, contains 50 rubrics with no overlap with the taxonomy development sample, and is evaluated by all automated signals in Section 4. For the LLM-as-Judge classifiers, both GPT-5.2 and Gemini 3 Pro evaluate every test rubric. Tab. 6 summarizes both samples.

## Appendix B Additional Experiment Details

This appendix provides additional analyses for the automated RIFT evaluators. First, we test whether the Alignment and Reward Variance signals are sensitive to the choice of judge model by replacing GPT-5.2 with Gemini 3 Pro Preview. Second, we report threshold-free ROC-AUC for the non-LLMaJ evaluators to complement best-threshold F1 and better account for class imbalance in the failure-mode labels.

### B.1 Alignment and Reward Variance Judge Model Ablation

The main paper reports two automated signals whose “judge” role is instantiated with GPT-5.2. Alignment measures how often weaker preference labelers (GPT-5 mini, Claude Haiku 4.5, and Gemini 3 Flash) agree with a strong reference labeler (GPT-5.2) on the same rubric-conditioned response pairs. We ablate by swapping the reference labeler to Gemini 3 Pro Preview, holding the three weaker labelers and the response pairs fixed. Reward variance measures stability of the aggregate rubric score under a rubric-conditioned LLM-as-Judge (LLMaJ) that scores four independent responses from GPT-5 mini per test input; we ablate by swapping that judge from GPT-5.2 to Gemini 3 Pro Preview, holding the response generator and evaluation protocol fixed. As shown in Tab. 7 , both signals are largely judge-model robust on Subjective and Non-Atomic, with the largest swings on consequential failure modes (notably Hackable and Low Signal). We hypothesize that is caused by label imbalance in the evaluation dataset.

### B.2 Additional Analysis for non-LLMaJ RIFT Evaluators

We additionally report threshold-free ROC-AUC results for automated failure-mode detection to address the concern that F1 at the best threshold on the same evaluation set may overstate performance due to in-sample threshold tuning. In particular, some failure modes are highly imbalanced (e.g., only 4 positives for Hackable ), making threshold-dependent F1 especially unstable. We therefore compute direction-agnostic ROC-AUC as max ⁡ ( AUC , 1 − AUC ) \max(\mathrm{AUC},1-\mathrm{AUC}) , matching the direction-agnostic threshold sweep used for F1.

We evaluate all evaluators except LLMaJ , including IRR , Alignment , Reward variance . Across the 48 joined rubrics, IRR has mean 0.712 (std. 0.149), Alignment has mean 0.704 (std. 0.166), and Reward Variance has mean 0.025 (std. 0.053).

Tables 8 and 9 show that threshold-free AUC is generally more conservative than best-threshold F1. The clearest example is Subjective , where F1 reaches 0.854 but best AUC is only 0.640, suggesting that much of the F1 comes from class prevalence rather than strong ranking ability. In contrast, Hackable has the strongest AUC (0.807 with Alignment) despite a modest best F1 of 0.400, indicating unstable signals under severe class imbalance. The strongest diagnostic also differs by failure mode, i.e., Alignment works best for Hackable , Misaligned or Rigid , and Missing Criteria ; IRR works best for Non-Atomic ; and Reward Variance works best for Ungrounded , Low Signal , and Redundant Criteria , suggesting that the three signals provide complementary information. Finally, correlations with the total number of failure modes are weak ( r = 0.247 r=0.247 for IRR, r = 0.222 r=0.222 for Alignment, and r = 0.052 r=0.052 for Reward Variance), so these signals are more informative about which failure mode is present than how many are present overall.

## Appendix C Prompts

This section provides the prompt templates used in the RIFT pipeline. Template variables are denoted with double curly braces (e.g., {{variable}} ).

### C.1 LLM-as-a-Judge Annotation Prompt

The following prompt template is used by the automated LLM-as-a-Judge (LLMaJ) evaluator described in Section 4. For each rubric under evaluation, the prompt is populated with the complete RIFT taxonomy—including all failure mode descriptions and pass/fail examples—alongside the rubric’s input context and rubric text. The LLMaJ returns structured output: for each identified failure mode, the model provides the failure mode label, a justification for why the failure mode applies, and a direct quote from the rubric exhibiting the issue.

You are an expert at evaluating rubric quality. Analyze the following rubric against the failure mode taxonomy and identify any issues. The rubric is designed to evaluate the quality of an AI model’s response to a given prompt. ## Failure Mode Taxonomy [For each failure mode in the taxonomy:] ### {{failure_mode.label}} Description: {{failure_mode.description}} **Pass Examples** (rubric does NOT exhibit this failure mode): [For each pass example:] - Input: {{example.input_context[:150]}}... Rubric: {{example.rubric[:200]}}... **Fail Examples** (rubric DOES exhibit this failure mode): [For each fail example:] - Input: {{example.input_context[:150]}}... Rubric: {{example.rubric[:200]}}... [End of taxonomy loop. If no failure modes are defined:] No failure modes defined yet - suggest any issues you observe. ## Input Context {{input_context}} ## Rubric to Evaluate {{rubric}} ## Task Identify which failure modes from the taxonomy apply to this rubric (if any).

The LLMaJ is configured to return a structured JSON response conforming to the following schema:

{ "suggested_labels": [ { "label": "<failure mode label from taxonomy>", "justification": "<why this failure mode applies>", "quote": "<specific rubric quote exhibiting the issue>" }, ... ] }

### C.2 Taxonomy Refinement Prompt

The following prompt template drives the iterative taxonomy refinement process described in Section 3 (Tab. 1 ). During each iteration of the grounded theory pipeline, expert annotator feedback—comprising open-ended rubric critiques and taxonomy critiques—is batched and provided to GPT-5.2 alongside the current taxonomy state. The model proposes refinements (merges, additions, clarifications, splits, removals, or renames), which are then reviewed and finalized by the expert panel.

You are an expert at analyzing rubric quality feedback and refining failure mode taxonomies. Your task is to output a complete refined failure mode taxonomy. ## Original Failure Mode Taxonomy This is the original taxonomy before any refinements in this session: [For each failure mode: label and description. If none defined: “No failure modes have been defined yet.”] ## Current Running Refinement This is the taxonomy as refined so far in this session (may be identical to original if this is the first batch): [For each failure mode: label, description, rationale, and counts of pass/fail examples. If none refined: “No refinements have been made yet.”] ## Annotator Feedback to Analyze Below are annotations with two types of critiques: - Rubric Critique: Issues the annotator observed in the rubric that were NOT captured by the original taxonomy labels (may suggest new failure modes) - Taxonomy Critique: Critique of the ORIGINAL taxonomy (unclear definitions, overlapping categories, missing categories, etc.). Note: these critiques were written against the original taxonomy, not the running refinement. [For each annotation in the batch:] Annotation {{loop.index}} Input Context: {{item.input_context}} Rubric: {{item.rubric}} Rubric Critique: (issues not captured by original taxonomy) {{item.rubric_critique or "None provided"}} Taxonomy Critique: (critique of the original taxonomy) {{item.failure_mode_critique or "None provided"}} [End of annotation loop]

The prompt further specifies a detailed taxonomy philosophy and refinement guidelines that constrain the model’s proposed changes:

## Taxonomy Philosophy CRITICAL: This taxonomy will be used by human annotators. The primary goal is to create a taxonomy that is: • Compact : Aim for 7–10 total failure modes. Fewer distinct categories is ALWAYS better than many granular ones.

• Easily distinguishable : A human should be able to distinguish between any two failure modes in under 30 seconds. If two categories require careful reading to tell apart, they should be merged or their distinction should be clarified by refining the label names and or the description.

• Actionable : Each category must be clearly applicable without ambiguity.

Consolidation over proliferation: When in doubt, MERGE rather than add. Two failure modes that are 80% similar should become one category, not two. The cost of a slightly imperfect merge is far lower than the cost of a bloated, hard-to-use taxonomy.

## Guidelines

• Clear descriptions : Each failure mode description must be clear, specific, and actionable. The description should explicitly specify HOW to determine if a rubric exhibits this failure mode. An annotator should be able to read the description and confidently apply it to any rubric.

• No overlapping failure modes : The taxonomy should not contain failure modes with overlapping meanings. If two labels capture the same concept, merge them or refine them to make them distinct. Do NOT add a new failure mode if its meaning already exists under a different label.

• Self-contained rationales : Each rationale must be a self-contained justification that will be used for manual review. It should explain WHY this failure mode exists, what evidence from critiques supports it, and how it differs from other failure modes. A reviewer should understand the rationale without needing to see the original critiques.

• Cumulative applicability : The refined taxonomy must be applicable to ALL critiques that have been seen in this session (including previous batches), not just the current batch. Do not remove or change failure modes in ways that would make them inapplicable to earlier critiques that supported them.

## Task

Analyze BOTH the rubric critiques and taxonomy critiques above. Before adding any new failure modes, first consider whether existing categories should be merged.

FIRST: Consider merging existing failure modes when:

• Two or more categories have similar descriptions or capture closely related issues

• Categories are difficult to distinguish without careful reading

• A broader category could capture multiple narrower ones without losing important distinctions

• The taxonomy has grown beyond 12 failure modes

PREFERRED action - merge: Combine overlapping, redundant, or closely related labels into one. This is the most important refinement action. If you’re unsure whether two categories are distinct enough, merge them.

Add new failure modes ONLY when ALL of the following are true:

• The issue is clearly NOT capturable by ANY existing failure mode (even with minor rewording)

• The issue appears in MULTIPLE critiques (not just one annotation)

• The new category is easily distinguishable from ALL existing categories

• Adding it would NOT push the taxonomy beyond 12 failure modes

Other refinement actions:

• clarify: Make a label’s description clearer, more specific, or more actionable (especially clarifying HOW to identify the failure mode)

• split: Divide an overly broad label into more specific ones (use sparingly---only when a category is genuinely too broad to apply consistently)

• remove: Eliminate labels that are not useful, are duplicates, or are too similar to other categories

• rename: Change a label name to be more descriptive

Output: 1. failure_modes: The complete list of failure modes after applying changes. Each failure mode should have:

• label: concise identifier (e.g., contradictory_criteria, missing_edge_cases)

• description: clear, specific, and actionable description that explains HOW to determine if a rubric has this failure mode (what to look for, what conditions must be met)

• rationale: a self-contained justification for this failure mode that can be understood without seeing the original critiques. Explain why it exists, what patterns it captures, and how it differs from related failure modes. If this is a NEW category, explicitly explain why it cannot be captured by any existing category.

• examples: REQUIRED: 3-5 pass_examples AND 3-5 fail_examples for each failure mode. Multiple diverse examples are essential for annotator training. You may use real examples from the annotations or synthesize clear illustrative examples. Each example should illustrate a distinct scenario or nuance.

2. changes_summary: A list of strings describing what changes you made (e.g., "Added ‘contradictory_criteria’ based on rubric critiques", "Clarified description of ‘ambiguous_criterion’", "Merged ‘x’ and ‘y’ into ‘z’")

If no changes are needed based on these critiques, return the current running refinement unchanged with an empty changes_summary.

## Appendix D RIFT: RubrIc Failure Mode Taxonomy

This section provides the complete descriptions of each failure mode in the RIFT taxonomy (Tab. 1 ), including detailed decision rules for annotation. Each failure mode includes: (1) when to apply the label, (2) how to determine whether a rubric exhibits the failure mode, and (3) boundary conditions specifying when not to apply the label and which alternative label to consider instead. For each failure mode, we also provide illustrative pass examples (rubrics that do not exhibit the failure mode) and fail examples (rubrics that do exhibit the failure mode). Note: in the “Do NOT apply” cross-references below, CSV-internal label identifiers have been replaced with the display names used in Tab. 1 .

### D.1 Reliability Failures

Reliability failures lead to inconsistent grading across annotators or evaluation runs, reducing the reproducibility and trustworthiness of rubric-based evaluation.

#### Subjective.

Apply when the rubric uses inherently subjective evaluative terms (e.g., “clear,” “appropriate,” “credible,” “comprehensive,” “professional,” “engaging,” “well-written,” “good sources”) and does NOT sufficiently anchor them with objective expectations.

How to determine: • Identify criteria dominated by inherently subjective terms.

• Check whether the rubric provides ANY anchoring attempt such as: – concrete checklists (“includes X/Y/Z”),

– measurable thresholds (word count, required sections, required elements),

– examples/anti-examples of what qualifies vs does not qualify, or

– explicit decision rules (“count as clear if it defines the term and gives one example”).

• If the rubric relies primarily on grader judgment and provides no meaningful anchors, apply.

Important clarification: • Do NOT apply if the rubric gives examples or non-trivial decision rules that explain what the subjective term means (even if the term is still somewhat subjective).

Do NOT apply if: • The core issue is missing expected answers/tolerances or a bounded verification procedure for a groundable requirement (use Ungrounded ).

• The requirement is entirely absent (use Missing Criteria ).

Illustrative examples:

Input Context Rubric Pass Write a professional email declining a meeting. 2 pts: Includes a decline + proposes an alternative time. 2 pts: Uses a greeting and sign-off. 1 pt: No negative or insulting language. Fail Summarize the study. 10 pts: The summary is clear and sufficiently detailed.

#### Non-Atomic.

Apply when the rubric does not provide a parseable, consistently scorable structure OR uses bundled (non-atomic) criteria that prevent consistent partial credit.

Triggers (any sufficient):

Non-atomic (bundled) criteria • One scored item bundles multiple independently scorable requirements with no partial-credit rule or separable sub-scores (e.g., “clear, comprehensive, accurate, and well-cited” as a single 10-pt item).

Do NOT apply when: • Subparts are separately scored or the rubric provides explicit level anchors (e.g., “1 point each for A/B/C” or a 0–2 scale per dimension with definitions).

• The rubric is scorable but uses subjective language (use Subjective ) or is missing requirements (use Missing Criteria ).

Illustrative examples:

Input Context Rubric Pass Write a short answer with two supporting reasons. 2 pts: Answers the question. 1 pt: Reason #1 supports the answer. 1 pt: Reason #2 supports the answer. 1 pt: Total length <=150 words. Fail Summarize the article. 10 pts: Summary is clear, accurate, comprehensive, concise, and engaging.

#### Ungrounded.

Apply when the rubric requires verification that is plausibly groundable/boundable, but the rubric does not provide the necessary grounding (answer keys/acceptable variants/tolerances/decision rules) OR does not bound the verification procedure (what to check, how much to check, and how to judge conflicts).

How to determine (any sufficient): (A) Groundable determinate tasks lack grading anchors. The task has a knowable target output given fixed inputs (e.g., extraction, classification, translation, math, SQL result, code output), but the rubric provides no expected answers, acceptable variants, label mappings, tolerances, or decision rules. The criterion may be clearly worded (e.g., “totals are correct”), yet graders still lack what they need to check correctness.

(B) Open-world requirements lack bounded audit procedure. The rubric demands broad verification (e.g., “all facts are true,” “restaurants are open right now,” “fully original/no plagiarism,” “links work”) without bounding: what to check (scope/sample size), which sources/tools are allowed, how to resolve conflicting evidence, and the pass/fail threshold.

(C) Measurement standard is unspecified but could be made checkable. The rubric requires a measurement that depends on an unspecified standard (e.g., “exactly 20 pages”) without defining the rendering/formatting standard or offering a workable proxy.

Do NOT apply if: • The requirement is simply missing from the rubric (use Missing Criteria ).

• The main issue is subjective wording without anchors (use Subjective ). The rubric provides a representative list of examples to demonstrate expected content.

Illustrative examples:

Input Context Rubric Pass Extract all email addresses from the text. 1 pt per correct email address; accepted forms include plus-addressing. Gold list of emails: a@x.com, b.y@z.org, … Deduct 1 pt per missing email. Fail Compute the correct totals for these 30 invoices. 10 pts: Totals are correct.

### D.2 Content Validity Failures

Content validity failures arise when rubric criteria are misaligned with the intended evaluation target, either by grading the wrong objective or by failing to cover essential requirements.

#### Misaligned or Rigid.

Apply when the rubric (a) grades the wrong objective for the prompt or embeds incorrect assumptions, OR (b) imposes unnecessarily strict/narrow requirements not asked for by the prompt or reasonably inferred from the prompt, predictably penalizing prompt-faithful high-quality answers.

How to determine (any applies): • Wrong task / shifted objective: makes non-requested deliverables mandatory for points.

• Incorrect embedded assumptions: assumes a context not in the prompt (jurisdiction, audience, tools, constraints) and scores accordingly.

• Penalizes good practice: scores down reasonable caveats/uncertainty/safety practices when the prompt does not forbid them.

• Arbitrary brittleness/over-constraint: mandates a specific tool/library/method/structure/formatting or false precision when multiple reasonable alternatives would satisfy the prompt.

Do NOT apply when: • The prompt itself imposes the strictness at any point (e.g., exact JSON keys, or a direct instruction from the user earlier in a chat conversation).

• The requirement is missing entirely (use Missing Criteria ).

• The main problem is internal contradiction (use Self-Contradictory ).

• The main problem is rubric-level proxy gaming (use Hackable ).

Illustrative examples:

Input Context Rubric Pass Write Python code to parse CSV. 5 pts: Correct parsing. 3 pts: Handles quoted commas. 2 pts: Includes brief usage example. (Does not mandate pandas vs csv module.) Fail Write a haiku about winter. 5 pts: Includes at least 5 academic citations. 5 pts: Uses APA format reference list.

#### Missing Criteria.

Apply when the prompt implies at least one checkable must-have requirement, but the rubric provides no criterion that allows a grader to evaluate that requirement at all.

How to determine: 1. List the prompt’s core requirements: • required deliverables/components,

• must/must-not constraints,

• required format/ordering/sections,

• and genre-critical qualities the prompt clearly expects (e.g., functional correctness for code; “two sentences”; “valid JSON”; “include 10 items”; “chronological order”).

2. For each requirement, check whether ANY rubric criterion covers it.

3. If one or more requirements have no corresponding criterion, apply.

Do NOT apply if: • The rubric mentions the requirement but is vague or subjective (use Subjective ).

• The rubric mentions the requirement but it cannot be graded consistently due to missing keys/tolerances/bounded audit steps (use Ungrounded ).

• The rubric grades a different task or adds arbitrary constraints (use Misaligned or Rigid ).

Illustrative examples:

Input Context Rubric Pass Return ONLY valid JSON with keys: name (string) and age (integer). 3 pts: Output parses as JSON. 2 pts: Contains exactly keys name and age. 2 pts: name is a string; age is an integer. 1 pt: No surrounding commentary. Fail Write a 200-word email and include a subject line. 10 pts: Tone is professional. 5 pts: Grammar and spelling are correct.

### D.3 Consequential Validity Failures

Consequential validity failures reduce the downstream usefulness and discriminative power of rubric-based evaluation, even when individual criteria may be well-defined.

#### Hackable.

Apply when the rubric is gameable at the rubric level: a responder could easily achieve a top score by inflating proxy metrics (length, number of bullets/sections/items/citations/examples/brands, repeated keywords) without materially improving correctness, relevance, or fulfillment of the prompt—and the rubric lacks strong quality gates that tie points to substantive, prompt-aligned success.

Core question (required): • Could I easily achieve full marks on this rubric while still not satisfying the prompt requirements or producing a low-quality response?

How to determine (any sufficient): • Most points come from “more” ( ≥ \geq N tips/citations/examples/pros/cons/sections) while relevance, non-duplication, correctness, and prompt-specific success conditions are weakly specified or absent.

• Rewards merely asserting attributes (“quiet,” “fast Wi-Fi,” “no fees”) without requiring evidence, linkage to the task, or checks against duplication.

• Counting proxies dominate while key prompt requirements have only weak gates (e.g., no requirement that citations support specific claims; no requirement that items be distinct and on-topic).

Do NOT apply when: • Quantity minimums are paired with robust quality controls that make padding ineffective (e.g., each item must be non-duplicative, tied to a specific claim or user need, and verifiably grounded/bounded).

• The main issue is that the rubric is generic and doesn’t discriminate at all (use Low Signal ).

• The main issue is a specific criterion that shifts the task or overconstrains acceptable answers (use Misaligned or Rigid ).

Illustrative examples:

Input Context Rubric Pass Provide 5 study tips. 1 pt each for 5 tips that are (a) non-duplicative and (b) each includes a concrete example of how to apply it. Fail Provide a recommendation. 5 pts: At least 10 pros. 5 pts: At least 10 cons. (No check for relevance or duplication.)

#### Low Signal.

Apply when the rubric as a whole does not discriminate candidate responses well for this prompt—i.e., it would give similar (often high) scores to many substantively different-quality responses—because the criteria are all generic, conditionally irrelevant, or too easy.

How to determine (rubric-level discrimination test): • Imagine 3–5 candidate responses ranging from weak to excellent.

• Ask: Would the rubric’s criteria/weights produce nearly equivalent different scores across them based on prompt-relevant success?

• If the rubric would likely award similar scores because most criteria are low-signal (e.g., “helpful,” “nice formatting,” “completed the task”) and there are few/no strong quality gates tied to the prompt’s real success conditions, apply.

Common signals: • Most points are allocated to generic writing quality/tone/formatting that is not central for this prompt.

• Criteria are trivially satisfied by any minimally on-task response (e.g., “schedule exists”).

• The rubric could be pasted into many unrelated tasks with little or no change.

Do NOT apply when: • The rubric is instead missing prompt-imposed must-haves (use Missing Criteria ).

• The rubric imposes the wrong constraints/assumptions (use Misaligned or Rigid ).

• The rubric is gameable specifically via quantity/proxies (use Hackable ).

Illustrative examples:

Input Context Rubric Pass Return JSON only with required keys. 6 pts: Valid JSON with required keys. 4 pts: No extra text outside JSON. Fail Return only a SQL query. 5 pts: Response is helpful. 5 pts: Uses appropriate tone.

#### Redundant Criteria.

Apply when two or more rubric criteria substantially evaluate the same underlying requirement such that the same behavior is rewarded/penalized multiple times.

How to determine: • Additional-signal test (primary): If these criteria are separate, do you get genuinely different evaluation signal, or are you just re-awarding the same property?

• Remove-one test: If removing a criterion would not meaningfully change what is evaluated (only point allocation), it is redundant.

• Includes near-duplicates and cases where one criterion fully subsumes another.

Important clarification (do NOT apply for mere dependencies): • Do NOT apply just because criteria are related or one tends to enable another.

• If Criterion B is a prerequisite/necessary condition for Criterion A (or vice versa) but still measures a distinct dimension (e.g., “valid JSON” and “has required keys”; “code compiles” and “passes tests”), that is NOT redundancy.

Do NOT apply when criteria are related but clearly distinct checks (e.g., factual accuracy vs clarity; format compliance vs correctness; presence of citations vs whether citations support claims).

Illustrative examples:

Input Context Rubric Pass Write a research summary with citations. 3 pts: Claims are supported by citations. 2 pts: Writing is well-organized. 2 pts: Includes limitations of the evidence. Fail Essay rubric. 5 pts: Clear writing. 5 pts: Clarity of prose. 5 pts: Writing is easy to understand.

## Appendix E Qualitative Analysis of Failure of LLMaJ in Detecting Failure Modes

To understand where the automated annotator disagrees with humans, we examine two difficult failure modes for LLM judges: Hackable or Proxy-Based Scoring and Ungrounded Verification . On the evaluation subset, these categories have F1 scores of 0.444 and 0.545, respectively. Both require reasoning beyond surface-level rubric critique: Hackable asks whether a responder could exploit the rubric, while Ungrounded asks whether a grader could actually verify the rubric.

#### Hackable : rewarding presentation instead of task success.

A representative false negative comes from a JSON-to-SQLite coding task, where the user asks how to save contacts from a JSON file into SQLite. Humans label the rubric as Hackable , but the automated annotator does not.

The rubric rewards presentation features such as step-by-step guidance, contextual explanation, and beginner-friendly writing. However, it does not require working code or any check that the JSON is actually parsed and saved into SQLite. A response could therefore look polished and detailed while still containing broken or incomplete code. The automated annotator catches nearby issues such as subjectivity and missing criteria, but misses the core problem: the rubric can be optimized by sounding competent rather than solving the task.

To test whether this is a capability issue or a prompting issue, we re-prompted the model on the same example. Under the standard annotation prompt with explicit rejection reasoning, the model still rejected Hackable :

This shows that the model interprets Hackable too narrowly. It looks for explicit numeric proxies, such as the number of bullets or citations, and misses softer proxies such as verbosity, structure, and tutorial-style explanation.

We then used a focused adversarial prompt that asked the model to imagine a responder trying to game the rubric. With this prompt, the model reversed its verdict:

This result suggests that the model can detect quality-proxy gameability when explicitly prompted to reason adversarially. The standard prompt does not reliably trigger that reasoning. In this case, the model treats hackability as a surface pattern to match, rather than asking whether the rubric can actually be exploited.

#### Ungrounded : clear requirement, missing verification procedure.

A representative false negative for Ungrounded Verification comes from a C# deadlock task. The model sees that the rubric is weak, but misses that the main requirement is not verifiable from the rubric alone.

The central criterion—“avoids the deadlock issue”—is clear at a high level, but the rubric does not say how to verify it. It gives no test case, expected behavior, execution setup, or pass/fail rule. A grader would need outside knowledge of C# async behavior and would have to decide independently whether the proposed solution works. This is an Ungrounded Verification problem: the criterion exists, but the rubric does not provide enough information to check it consistently.

Under the standard annotation prompt, the model focuses on general rubric weakness instead:

This explains why the model assigns nearby labels such as Subjective , Non-Atomic , and Trivial . However, it misses the main issue: the model never asks what evidence a grader would need to verify that the solution avoids deadlock. It does not check whether the rubric provides a test case, expected behavior, execution condition, or decision rule.

This is the main failure pattern for Ungrounded Verification : the model notices that the rubric is weak, but maps the problem to surface-level labels instead of the missing verification procedure. A better annotator needs to explicitly ask, for each factual or technical criterion, what the grader should check, how they should check it, and what counts as passing.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
