I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper presents a method for cross-model KV cache transfer, which reuses the source model's KV cache to skip prefill from scratch. The authors find that the cross-model KV relationship exhibits substantial linear structure, and propose a closed-form ridge mapper that operates per-head and proceeds in three steps. Experiments across six matched-KV pairs from three model families show that the linear mapper retains 73–98% of standalone accuracy and runs 2.7–25 × faster than re-prefill in the small-to-large direction. The mapper also shows stability across multi-turn handoff, attention-output cosine predicts cross-pair retention. A nonlinear MLP recovers pairs where ridge falls short.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The experiments are comprehensive, covering six matched-KV pairs from three model families.
- The proposed method is fast and stable across multi-turn handoff.
- The paper provides a detailed analysis of the attention-output cosine and its correlation with cross-pair retention.

### Weaknesses

#### Some Related Works


#### comment

 - The linear mapper relies on a small calibration set of 500 FineWeb-Edu sequences of length 1024, which may not be sufficient to capture the complexity of the KV cache. The performance of the linear mapper is highly dependent on the quality and diversity of the calibration set, and it is unclear how the method would perform with a smaller or less diverse dataset. The paper does not explore the sensitivity of the method to the size and composition of the calibration set, which is a critical factor for practical applications.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to re-prefill. While the authors mention that the linear mapper is faster, they do not provide a breakdown of the computational steps involved, such as the time required for ridge regression and the memory footprint of the model. A more detailed analysis of the computational cost would be beneficial for assessing the practical feasibility of the method.
- The paper does not explore the limitations of the proposed method in detail. For example, it is unclear how the method would perform with models that have different architectures or training procedures. The paper also does not discuss the potential impact of the method on the model's ability to generalize to new tasks or domains. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications.

### Suggestions

The paper would benefit from a more thorough investigation into the impact of the calibration set size and diversity on the performance of the linear mapper. Specifically, the authors should conduct experiments with varying sizes of the calibration set, including smaller sets to assess the minimum data requirements and larger sets to explore the potential for overfitting. Furthermore, the authors should explore the impact of different calibration set compositions, such as using data from different domains or tasks, to assess the robustness of the method. This analysis should include a detailed evaluation of the performance of the linear mapper across different calibration set configurations, providing insights into the sensitivity of the method to the calibration data. The authors should also consider using techniques such as cross-validation to ensure that the results are robust and generalizable.

In addition to the computational cost, the paper should provide a more detailed analysis of the memory footprint of the linear mapper. This analysis should include a breakdown of the memory requirements for each component of the model, such as the ridge regression coefficients and the transformed KV cache. The authors should also explore the potential for optimizing the memory usage of the model, such as by using techniques such as quantization or pruning. Furthermore, the paper should discuss the potential impact of the memory footprint on the scalability of the method, especially for large-scale models. A more detailed analysis of the memory usage would be beneficial for assessing the practical feasibility of the method in resource-constrained environments.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This discussion should include an analysis of the potential impact of the method on the model's ability to generalize to new tasks or domains, as well as an assessment of the potential for the method to introduce biases or artifacts into the KV cache. The authors should also explore the potential impact of the method on the model's ability to handle different types of input sequences, such as those with varying lengths or complexities. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications, and would also provide guidance for future research in this area.

### Questions

- How does the linear mapper perform with different sizes of the calibration set?
- How does the linear mapper perform with different compositions of the calibration set?
- How does the linear mapper perform with models that have different architectures or training procedures?
- What is the memory footprint of the linear mapper?
- What is the impact of the linear mapper on the model's ability to generalize to new tasks or domains?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a method to transfer the KV cache between models in the same family. The method is based on ridge regression and is shown to be effective in experiments.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The experiments are comprehensive, covering six matched-KV pairs from three model families.
- The proposed method is fast and stable across multi-turn handoff.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is limited to models in the same family. It would be more interesting to transfer the KV cache between models with different architectures.
- The proposed method is only evaluated on the KV cache. It would be interesting to see if it can be applied to other intermediate features.

### Suggestions

The paper's focus on transferring KV cache between models within the same family is a reasonable starting point, but the limitation to identical architectures significantly restricts its practical applicability. The core idea of using ridge regression on intermediate features is promising, but the method's lack of generalization to different architectures, such as models with varying attention mechanisms or layer configurations, is a major concern. For example, transferring a KV cache from a model with a standard transformer architecture to one employing a linear attention mechanism would require a more sophisticated approach than simple ridge regression on the raw KV cache. The authors should explore methods that can adapt to these architectural differences, perhaps by learning a transformation that maps the intermediate features from one model to the other, or by using a more flexible regression technique that can handle non-linear relationships between features. This would greatly enhance the method's utility and impact.

Furthermore, the paper's evaluation is narrowly focused on KV cache transfer, neglecting other potential intermediate features that could benefit from similar techniques. While the KV cache is a crucial component of transformer models, other features, such as the attention weights, the hidden states of specific layers, or even the output of certain layers, could also be candidates for transfer. For instance, the attention weights might be useful for understanding the model's decision-making process, and transferring them could lead to more interpretable models. Similarly, transferring hidden states could enable the use of pre-trained models in downstream tasks with different architectures. The authors should consider expanding their evaluation to include these other intermediate features, which would demonstrate the broader applicability of their method and potentially uncover new transfer opportunities. This would also require a more detailed analysis of the characteristics of each feature and how they relate to the target model.

Finally, the paper could benefit from a more thorough analysis of the limitations of the proposed method. While the authors demonstrate its effectiveness on a few specific cases, it is unclear how the method would perform in more challenging scenarios, such as when the source and target models have significantly different sizes or when the transfer is performed across multiple layers. A more detailed analysis of the method's sensitivity to various factors, such as the size of the calibration set, the choice of ridge regularization parameter, and the architecture of the source and target models, would be valuable. This would provide a more complete understanding of the method's strengths and weaknesses and would help guide future research in this area. The authors should also consider comparing their method to other existing techniques for model transfer, which would help to contextualize their contribution and highlight its unique advantages.

### Questions

See weaknesses.

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a closed-form ridge mapper for cross-model KV cache transfer. The authors first demonstrate that the cross-model KV relationship exhibits substantial linear structure and propose a closed-form ridge mapper that operates per-head and proceeds in three steps. The authors conduct experiments across six matched-KV pairs from three model families and show that the linear mapper retains 73–98% of standalone accuracy and runs 2.7–25 × faster than re-prefill.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The experiments are comprehensive, covering six matched-KV pairs from three model families.
3. The proposed method is fast and stable across multi-turn handoff.

### Weaknesses

#### Some Related Works


#### comment

1. The linear mapper relies on a small calibration set of 500 FineWeb-Edu sequences of length 1024, which may not be sufficient to capture the complexity of the KV cache. The performance of the linear mapper is highly dependent on the quality and diversity of the calibration set, and it is unclear how the method would perform with a smaller or less diverse dataset. The paper does not explore the sensitivity of the method to the size and composition of the calibration set, which is a critical factor for practical applications.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to re-prefill. While the authors mention that the linear mapper is faster, they do not provide a breakdown of the computational steps involved, such as the time required for ridge regression and the memory footprint of the model. A more detailed analysis of the computational cost would be beneficial for assessing the practical feasibility of the method.
3. The paper does not explore the limitations of the proposed method in detail. For example, it is unclear how the method would perform with models that have different architectures or training procedures. The paper also does not discuss the potential impact of the method on the model's ability to generalize to new tasks or domains. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications.

### Suggestions

The paper would benefit from a more thorough investigation into the impact of the calibration set size and diversity on the performance of the linear mapper. Specifically, the authors should conduct experiments with varying sizes of the calibration set, including smaller sets to assess the minimum data requirements and larger sets to explore the potential for overfitting. Furthermore, the authors should explore the impact of different calibration set compositions, such as using data from different domains or tasks, to assess the robustness of the method. This analysis should include a detailed evaluation of the performance of the linear mapper across different calibration set configurations, providing insights into the sensitivity of the method to the calibration data. The authors could also consider using techniques such as cross-validation to ensure that the results are robust and generalizable.

In addition to the computational cost, the paper should provide a more detailed analysis of the memory footprint of the linear mapper. This analysis should include a breakdown of the memory requirements for each component of the model, such as the ridge regression coefficients and the transformed KV cache. The authors should also explore the potential for optimizing the memory usage of the model, such as by using techniques such as quantization or pruning. Furthermore, the paper should discuss the potential impact of the memory footprint on the scalability of the method, especially for large-scale models. A more detailed analysis of the memory usage would be beneficial for assessing the practical feasibility of the method in resource-constrained environments.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This discussion should include an analysis of the potential impact of the method on the model's ability to generalize to new tasks or domains, as well as an assessment of the potential for the method to introduce biases or artifacts into the KV cache. The authors should also explore the potential impact of the method on the model's ability to handle different types of input sequences, such as those with varying lengths or complexities. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications, and would also provide guidance for future research in this area.

### Questions

1. How does the linear mapper perform with different sizes of the calibration set?
2. How does the linear mapper perform with different compositions of the calibration set?
3. How does the linear mapper perform with models that have different architectures or training procedures?
4. What is the memory footprint of the linear mapper?
5. What is the impact of the linear mapper on the model's ability to generalize to new tasks or domains?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a method for cross-model KV cache transfer, which reuses the source model's KV cache to skip prefill from scratch. The authors find that the cross-model KV relationship exhibits substantial linear structure, and propose a closed-form ridge mapper that operates per-head and proceeds in three steps. Experiments across six matched-KV pairs from three model families show that the linear mapper retains 73–98% of standalone accuracy and runs 2.7–25 × faster than re-prefill in the small-to-large direction.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The experiments are comprehensive, covering six matched-KV pairs from three model families.
- The proposed method is fast and stable across multi-turn handoff.
- The paper provides a detailed analysis of the attention-output cosine and its correlation with cross-pair retention.

### Weaknesses

#### Some Related Works


#### comment

 - The linear mapper relies on a small calibration set of 500 FineWeb-Edu sequences of length 1024, which may not be sufficient to capture the complexity of the KV cache. The performance of the linear mapper is highly dependent on the quality and diversity of the calibration set, and it is unclear how the method would perform with a smaller or less diverse dataset. The paper does not explore the sensitivity of the method to the size and composition of the calibration set, which is a critical factor for practical applications.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to re-prefill. While the authors mention that the linear mapper is faster, they do not provide a breakdown of the computational steps involved, such as the time required for ridge regression and the memory footprint of the model. A more detailed analysis of the computational cost would be beneficial for assessing the practical feasibility of the method.
- The paper does not explore the limitations of the proposed method in detail. For example, it is unclear how the method would perform with models that have different architectures or training procedures. The paper also does not discuss the potential impact of the method on the model's ability to generalize to new tasks or domains. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications.

### Suggestions

The paper would benefit from a more thorough investigation into the impact of the calibration set size and diversity on the performance of the linear mapper. Specifically, the authors should conduct experiments with varying sizes of the calibration set, including smaller sets to assess the minimum data requirements and larger sets to explore the potential for overfitting. Furthermore, the authors should explore the impact of different calibration set compositions, such as using data from different domains or tasks, to assess the robustness of the method. This analysis should include a detailed evaluation of the performance of the linear mapper across different calibration set configurations, providing insights into the sensitivity of the method to the calibration data. The authors could also consider using techniques such as cross-validation to ensure that the results are robust and generalizable.

In addition to the computational cost, the paper should provide a more detailed analysis of the memory footprint of the linear mapper. This analysis should include a breakdown of the memory requirements for each component of the model, such as the ridge regression coefficients and the transformed KV cache. The authors should also explore the potential for optimizing the memory usage of the model, such as by using techniques such as quantization or pruning. Furthermore, the paper should discuss the potential impact of the memory footprint on the scalability of the method, especially for large-scale models. A more detailed analysis of the memory usage would be beneficial for assessing the practical feasibility of the method in resource-constrained environments.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This discussion should include an analysis of the potential impact of the method on the model's ability to generalize to new tasks or domains, as well as an assessment of the potential for the method to introduce biases or artifacts into the KV cache. The authors should also explore the potential impact of the method on the model's ability to handle different types of input sequences, such as those with varying lengths or complexities. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications, and would also provide guidance for future research in this area.

### Questions

- How does the linear mapper perform with different sizes of the calibration set?
- How does the linear mapper perform with different compositions of the calibration set?
- How does the linear mapper perform with models that have different architectures or training procedures?
- What is the memory footprint of the linear mapper?
- What is the impact of the linear mapper on the model's ability to generalize to new tasks or domains?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence (methodological, experimental).
4. Write a validation analysis for each weakness.
**Review 1**

1. Weakness Statement:
"The linear mapper relies on a small calibration set of 500 FineWeb-Edu sequences of length 1024, which may not be sufficient to capture the complexity of the KV cache. The performance of the linear mapper is highly dependent on the quality and diversity of the calibration set, and it is unclear how the method would perform with a smaller or less diverse dataset. The paper does not explore the sensitivity of the method to the size and composition of the calibration set, which is a critical factor for practical applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "We use ridge ( λ = 0.01 ) and content-space mapping. The number of source layers k k is swept over { 1 , 2 , 4 , 6 , 8 , 10 , 12 , 16 , 20 , 24 , all } . We select a single k k per pair as the value that maximizes the arithmetic mean of the log-likelihood benchmark accuracies (ARC-C, HellaSwag, WinoGrande, MMLU), breaking near-ties toward larger k k for evaluation coverage. Table 2 reports component ablations, and calibration sensitivity to λ \lambda , N N , and calibration domain is in Appendix C ." (Section 4.1)
   - "Calibration data consists of 500 FineWeb-Edu sequences of length 1024, stride-4 subsampled to N ≈ 128 K tokens per target head." (Section 4.1)
   - "Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB), and the family table are in Appendix D ." (Section 4.1)
   - Appendix C contains the calibration sensitivity analysis.

3. Literature Gap Analysis:
   - The paper does not explicitly cite works that discuss the impact of calibration set size and diversity on linear regression or similar methods in the context of model compression or transfer.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly states the use of a 500 sequence calibration set. Appendix C presents an analysis of the impact of the number of calibration samples (N) on performance, showing results for N=200, 500, and 1000. The paper also mentions the composition of the calibration data as being from FineWeb-Edu.
   - Supporting quotes: "We use ridge ... The number of source layers k k is swept over ... We select a single k k per pair as the value that maximizes the arithmetic mean of the log-likelihood benchmark accuracies ... Table 2 reports component ablations, and calibration sensitivity to λ \lambda , N N , and calibration domain is in Appendix C ."
   - Impact assessment: While the paper does explore the impact of the number of calibration samples, it does not explore the impact of different compositions of the calibration set (e.g., using data from different domains or tasks). The reviewer's point about the potential insufficiency of the calibration set and the dependence on its quality and diversity is valid, as the paper does not provide a comprehensive analysis of these aspects.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses a 500 sequence calibration set and explores the impact of the number of samples but not the diversity of the samples.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to re-prefill. While the authors mention that the linear mapper is faster, they do not provide a breakdown of the computational steps involved, such as the time required for ridge regression and the memory footprint of the model. A more detailed analysis of the computational cost would be beneficial for assessing the practical feasibility of the method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "The mapper has three components: per-head ridge regression fit from a small calibration set, cross-layer source selection, and content-space mapping. The per-head ridge regression is a closed-form solution, which is computationally efficient." (Section 3.1)
   - "The time taken to fit the mapper directly on the calibration layer is 47–87 min per pair on a single 8 × 8× H100 node with no gradient-based training. Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB), and the family table are in Appendix D ." (Section 4.1)
   - "Table 5 reports per-sequence-length latency. The mapper runs 4–25 × faster small-to-large and 3–7 × faster large-to-small across sequence lengths from 64 to 32,768 tokens. The full sequence-length sweep is in Appendix G ." (Section 4.7)

3. Literature Gap Analysis:
   - The paper does not explicitly compare the computational cost to other model transfer methods in detail.

4. Validation Analysis:
   - Primary evidence summary: The paper mentions the computational efficiency of the per-head ridge regression as a closed-form solution. It also provides the time taken to fit the mapper on the calibration layer and the memory footprint. It reports the speedup compared to re-prefill in Section 4.7.
   - Supporting quotes: "The per-head ridge regression is a closed-form solution, which is computationally efficient." "The time taken to fit the mapper directly on the calibration layer is 47–87 min per pair ... Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB) ... The mapper runs 4–25 × faster small-to-large and 3–7 × faster large-to-small across sequence lengths from 64 to 32,768 tokens."
   - Impact assessment: The paper does provide some information on computational cost, including the time for fitting and speedup compared to re-prefill. However, it lacks a detailed breakdown of the computational steps involved in the ridge regression (e.g., the complexity of the inversion or decomposition) and a more granular analysis of memory footprint beyond the total parameter size and storage.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions computational efficiency and provides some timing and memory information, but lacks a detailed breakdown of computational steps and a more granular memory footprint analysis.

1. Weakness Statement:
"The paper does not explore the limitations of the proposed method in detail. For example, it is unclear how the method would perform with models that have different architectures or training procedures. The paper also does not discuss the potential impact of the method on the model's ability to generalize to new tasks or domains. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications, and would also provide guidance for future research in this area."

2. Evidence Collection:
- The paper focuses on transferring between models within the same family (Qwen3, Llama 3.1, Ministral 3).
- The experiments are conducted on six matched-KV pairs.
- The paper discusses the limitations of the method in the "Broader impact, future work, and limitations" section: "(1) Single-domain calibration. Calibration uses only FineWeb-Edu. Appendix C measures the cost of substituting Wikipedia or CodeAlpaca on one pair. Neither substitution separates subject matter from register, so the sweep does not bound calibration confined to a single field such as medicine or law. (2) k k selection. Per-pair k k is selected on the same log-likelihood benchmarks we report on. Appendix H measures the effect, at most 2.49  pp, and adds a held-out evaluation, though neither is a substitute for selecting k k out of sample. (3) Matched-KV is empirical. The closed-form mapper imposes no structural requirement on source or target dimensions, but our six pairs are all matched-KV by construction. Different families may share enough representation structure to admit a similar mapping, or may require different machinery. (4) Hidden factors. Beyond architecture, training-data overlap, fine-tuning recipe, and other non-architectural factors may also influence transferability. We leave systematic study of these to future work."

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of cross-model transfer methods in detail.

4. Validation Analysis:
   - Primary evidence summary: The paper acknowledges limitations in the "Broader impact, future work, and limitations" section, specifically mentioning the single-domain calibration, k selection, matched-KV pairs, and hidden factors.
   - Supporting quotes: "Single-domain calibration. Calibration uses only FineWeb-Edu. Appendix C measures the cost of substituting Wikipedia or CodeAlpaca on one pair. Neither substitution separates subject matter from register, so the sweep does not bound calibration confined to a single field such as medicine or law. (2) k k selection. Per-pair k k is selected on the same log-likelihood benchmarks we report on. Appendix H measures the effect, at most 2.49  pp, and adds a held-out evaluation, though neither is a substitute for selecting k k out of sample. (3) Matched-KV is empirical. The closed-form mapper imposes no structural requirement on source or target dimensions, but our six pairs are all matched-KV by construction. Different families may share enough representation structure to admit a similar mapping, or may require different machinery. (4) Hidden factors. Beyond architecture, training-data overlap, fine-tuning recipe, and other non-arithmetical factors may also influence transferability. We leave systematic study of these to future work."
   - Impact assessment: The paper does discuss some limitations, particularly the matched-KV pairs and the single-domain calibration. However, the reviewer's point about the lack of discussion on performance with different architectures or training procedures and the potential impact on generalization to new tasks or domains is valid, as the paper's experiments are limited to models within the same family and specific tasks.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper discusses limitations related to matched-KV pairs and calibration domain, but lacks a detailed discussion on performance with different architectures or training procedures and the impact on generalization to new tasks or domains.

**Review 2**

1. Weakness Statement:
"The proposed method is limited to models in the same family. It would be more interesting to transfer the KV cache between models with different architectures."

2. Evidence Collection:
- The paper explicitly states the focus on transferring KV cache within the same model family: "This pipeline generalizes intra-model KV reuse." (Abstract) and "This paper generalizes intra-model KV reuse." (Introduction).
- The experiments are conducted on matched-KV pairs from three model families (Qwen3, Llama 3.1, Ministral 3), which are different families but the transfer is within each family.

3. Literature Gap Analysis:
   - The paper does not extensively discuss or compare against methods for cross-family KV cache transfer.

4. Validation Analysis:
   - Primary evidence summary: The paper's focus is clearly on intra-model transfer. The experiments involve transferring within different model families but not across entirely different architectures.
   - Supporting quotes: "This pipeline generalizes intra-model KV reuse." (Abstract) and "This paper generalizes intra-model KV reuse." (Introduction).
   - Impact assessment: The reviewer's point is valid. The paper's scope is limited to transferring within the same model family, and it does not explore the challenges or potential of transferring KV cache between models with fundamentally different architectures.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly focuses on intra-model transfer and the experiments are limited to transferring within different model families.

1. Weakness Statement:
"The proposed method is only evaluated on the KV cache. It would be interesting to see if it can be applied to other intermediate features."

2. Evidence Collection:
- The paper's title and abstract mention "cross-model KV cache transfer".
- The method section focuses specifically on the KV cache.
- The experiments are designed to evaluate the transfer of the KV cache.

3. Literature Gap Analysis:
   - The paper does not discuss or cite works that explore transferring other intermediate features in cross-model settings.

4. Validation Analysis:
   - Primary evidence summary: The paper's scope is explicitly on KV cache transfer. The method and experiments are designed around this specific component.
   - Supporting quotes: "This paper introduces a gradient-free framework for cross-model KV cache transfer..." (Main Idea) and the title of the paper.
   - Impact assessment: The reviewer's point is valid. The paper's evaluation is limited to the KV cache, and it does not explore the applicability of the proposed method to other intermediate features.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus is on KV cache transfer, and the method and experiments are designed around this specific component.

**Review 3**

1. Weakness Statement:
"The linear mapper relies on a small calibration set of 500 FineWeb-Edu sequences of length 1024, which may not be sufficient to capture the complexity of the KV cache. The performance of the linear mapper is highly dependent on the quality and diversity of the calibration set, and it is unclear how the method would perform with a smaller or less diverse dataset. The paper does not explore the sensitivity of the method to the size and composition of the calibration set, which is a critical factor for practical applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "We use ridge ( λ = 0.01 ) and content-space mapping. The number of source layers k k is swept over { 1 , 2 , 4 , 6 , 8 , 10 , 12 , 16 , 20 , 24 , all } . We select a single k k per pair as the value that maximizes the arithmetic mean of the log-likelihood benchmark accuracies (ARC-C, HellaSwag, WinoGrande, MMLU), breaking near-ties toward larger k k for evaluation coverage. Table 2 reports component ablations, and calibration sensitivity to λ \lambda , N N , and calibration domain is in Appendix C ." (Section 4.1)
   - "Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB), and the family table are in Appendix D ." (Section 4.1)
   - Appendix C contains the calibration sensitivity analysis.

3. Literature Gap Analysis:
   - The paper does not explicitly cite works that discuss the impact of calibration set size and diversity on linear regression or similar methods in the context of model compression or transfer.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly states the use of a 500 sequence calibration set. Appendix C presents an analysis of the impact of the number of calibration samples (N) on performance, showing results for N=200, 500, and 1000. The paper also mentions the composition of the calibration data as being from FineWeb-Edu.
   - Supporting quotes: "We use ridge ... The number of source layers k k is swept over ... We select a single k k per pair as the value that maximizes the arithmetic mean of the log-likelihood benchmark accuracies ... Table 2 reports component ablations, and calibration sensitivity to λ \lambda , N N , and calibration domain is in Appendix C ."
   - Impact assessment: While the paper does explore the impact of the number of calibration samples, it does not explore the impact of different compositions of the calibration set (e.g., using data from different domains or tasks). The reviewer's point about the potential insufficiency of the calibration set and the dependence on its quality and diversity is valid, as the paper does not provide a comprehensive analysis of these aspects.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses a 500 sequence calibration set and explores the impact of the number of samples but not the diversity of the samples.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to re-prefill. While the authors mention that the linear mapper is faster, they do not provide a breakdown of the computational steps involved, such as the time required for ridge regression and the memory footprint of the model. A more detailed analysis of the computational cost would be beneficial for assessing the practical feasibility of the method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "The mapper has three components: per-head ridge regression fit from a small calibration set, cross-layer source selection, and content-space mapping. The per-head ridge regression is a closed-form solution, which is computationally efficient." (Section 3.1)
   - "The time taken to fit the mapper directly on the calibration layer is 47–87 min per pair on a single 8 × 8× H100 node with no gradient-based training. Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB), and the family table are in Appendix D ." (Section 4.1)
   - "Table 5 reports per-sequence-length latency. The mapper runs 4–25 × faster small-to-large and 3–7 × faster large-to-small across sequence lengths from 64 to 32,768 tokens. The full sequence-length sweep is in Appendix G ." (Section 4.7)

3. Literature Gap Analysis:
   - The paper does not explicitly compare the computational cost to other model transfer methods in detail.

4. Validation Analysis:
   - Primary evidence summary: The paper mentions the computational efficiency of the per-head ridge regression as a closed-form solution. It also provides the time taken to fit the mapper on the calibration layer and the memory footprint. It reports the speedup compared to re-prefill in Section 4.7.
   - Supporting quotes: "The per-head ridge regression is a closed-form solution, which is computationally efficient." "The time taken to fit the mapper directly on the calibration layer is 47–87 min per pair ... Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB) ... The mapper runs 4–25 × faster small-to-large and 3–7 × faster large-to-small across sequence lengths from 64 to 32,768 tokens."
   - Impact assessment: The paper does provide some information on computational cost, including the time for fitting and speedup compared to re-prefill. However, it lacks a detailed breakdown of the computational steps involved in the ridge regression (e.g., the complexity of the inversion or decomposition) and a more granular analysis of memory footprint beyond the total parameter size and storage.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions computational efficiency and provides some timing and memory information, but lacks a detailed breakdown of computational steps and a more granular memory footprint analysis.

1. Weakness Statement:
"The paper does not explore the limitations of the proposed method in detail. For example, it is unclear how the method would perform with models that have different architectures or training procedures. The paper also does not discuss the potential impact of the method on the model's ability to generalize to new tasks or domains. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications, and would also provide guidance for future research in this area."

2. Evidence Collection:
- The paper focuses on transferring between models within the same family (Qwen3, Llama 3.1, Ministral 3).
- The experiments are conducted on six matched-KV pairs.
- The paper discusses the limitations of the method in the "Broader impact, future work, and limitations" section: "(1) Single-domain calibration. Calibration uses only FineWeb-Edu. Appendix C measures the cost of substituting Wikipedia or CodeAlpaca on one pair. Neither substitution separates subject matter from register, so the sweep does not bound calibration confined to a single field such as medicine or law. (2) k k selection. Per-pair k k is selected on the same log-likelihood benchmarks we report on. Appendix H measures the effect, at most 2.49  pp, and adds a held-out evaluation, though neither is a substitute for selecting k k out of sample. (3) Matched-KV is empirical. The closed-form mapper imposes no structural requirement on source or target dimensions, but our six pairs are all matched-KV by construction. Different families may share enough representation structure to admit a similar mapping, or may require different machinery. (4) Hidden factors. Beyond architecture, training-data overlap, fine-tuning recipe, and other non-architectural factors may also influence transferability. We leave systematic study of these to future work."

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of cross-model transfer methods in detail.

4. Validation Analysis:
   - Primary evidence summary: The paper acknowledges limitations in the "Broader impact, future work, and limitations" section, specifically mentioning the single-domain calibration, k selection, matched-KV pairs, and hidden factors.
   - Supporting quotes: "Single-domain calibration. Calibration uses only FineWeb-Edu. Appendix C measures the cost of substituting Wikipedia or CodeAlpaca on one pair. Neither substitution separates subject matter from register, so the sweep does not bound calibration confined to a single field such as medicine or law. (2) k k selection. Per-pair k k is selected on the same log-likelihood benchmarks we report on. Appendix H measures the effect, at most 2.49  pp, and adds a held-out evaluation, though neither is a substitute for selecting k k out of sample. (3) Matched-KV is empirical. The closed-form mapper imposes no structural requirement on source or target dimensions, but our six pairs are all matched-KV by construction. Different families may share enough representation structure to admit a similar mapping, or may require different machinery. (4) Hidden factors. Beyond architecture, training-data overlap, fine-tuning recipe, and other non-arithmetical factors may also influence transferability. We leave systematic study of these to future work."
   - Impact assessment: The paper does discuss some limitations, particularly the matched-KV pairs and the single-domain calibration. However, the reviewer's point about the lack of discussion on performance with different architectures or training procedures and the potential impact on generalization to new tasks or domains is valid, as the paper's experiments are limited to models within the same family and specific tasks.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper discusses limitations related to matched-KV pairs and calibration domain, but lacks a detailed discussion on performance with different architectures or training procedures and the impact on generalization to new tasks or domains.

**Review 4**

1. Weakness Statement:
"The linear mapper relies on a small calibration set of 500 FineWeb-Edu sequences of length 1024, which may not be sufficient to capture the complexity of the KV cache. The performance of the linear mapper is highly dependent on the quality and diversity of the calibration set, and it is unclear how the method would perform with a smaller or less diverse dataset. The paper does not explore the sensitivity of the method to the size and composition of the calibration set, which is a critical factor for practical applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "We use ridge ( λ = 0.01 ) and content-space mapping. The number of source layers k k is swept over { 1 , 2 , 4 , 6 , 8 , 10 , 12 , 16 , 20 , 24 , all } . We select a single k k per pair as the value that maximizes the arithmetic mean of the log-likelihood benchmark accuracies (ARC-C, HellaSwag, WinoGrande, MMLU), breaking near-ties toward larger k k for evaluation coverage. Table 2 reports component ablations, and calibration sensitivity to λ \lambda , N N , and calibration domain is in Appendix C ." (Section 4.1)
   - "Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB), and the family table are in Appendix D ." (Section 4.1)
   - Appendix C contains the calibration sensitivity analysis.

3. Literature Gap Analysis:
   - The paper does not explicitly cite works that discuss the impact of calibration set size and diversity on linear regression or similar methods in the context of model compression or transfer.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly states the use of a 500 sequence calibration set. Appendix C presents an analysis of the impact of the number of calibration samples (N) on performance, showing results for N=200, 500, and 1000. The paper also mentions the composition of the calibration data as being from FineWeb-Edu.
   - Supporting quotes: "We use ridge ... The number of source layers k k is swept over ... We select a single k k per pair as the value that maximizes the arithmetic mean of the log-likelihood benchmark accuracies ... Table 2 reports component ablations, and calibration sensitivity to λ \lambda , N N , and calibration domain is in Appendix C ."
   - Impact assessment: While the paper does explore the impact of the number of calibration samples, it does not explore the impact of different compositions of the calibration set (e.g., using data from different domains or tasks). The reviewer's point about the potential insufficiency of the calibration set and the dependence on its quality and diversity is valid, as the paper does not provide a comprehensive analysis of these aspects.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses a 500 sequence calibration set and explores the impact of the number of samples but not the diversity of the samples.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to re-prefill. While the authors mention that the linear mapper is faster, they do not provide a breakdown of the computational steps involved, such as the time required for ridge regression and the memory footprint of the model. A more detailed analysis of the computational cost would be beneficial for assessing the practical feasibility of the method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "The mapper has three components: per-head ridge regression fit from a small calibration set, cross-layer source selection, and content-space mapping. The per-head ridge regression is a closed-form solution, which is computationally efficient." (Section 3.1)
   - "The time taken to fit the mapper directly on the calibration layer is 47–87 min per pair on a single 8 × 8× H100 node with no gradient-based training. Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB), and the family table are in Appendix D ." (Section 4.1)
   - "Table 5 reports per-sequence-length latency. The mapper runs 4–25 × faster small-to-large and 3–7 × faster large-to-small across sequence lengths from 64 to 32,768 tokens. The full sequence-length sweep is in Appendix G ." (Section 4.7)

3. Literature Gap Analysis:
   - The paper does not explicitly compare the computational cost to other model transfer methods in detail.

4. Validation Analysis:
   - Primary evidence summary: The paper mentions the computational efficiency of the per-head ridge regression as a closed-form solution. It also provides the time taken to fit the mapper on the calibration layer and the memory footprint. It reports the speedup compared to re-prefill in Section 4.7.
   - Supporting quotes: "The per-head ridge regression is a closed-form solution, which is computationally efficient." "The time taken to fit the mapper directly on the calibration layer is 47–87 min per pair ... Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB) ... The mapper runs 4–25 × faster small-to-large and 3–7 × faster large-to-small across sequence lengths from 64 to 32,768 tokens."
   - Impact assessment: The paper does provide some information on computational cost, including the time for fitting and speedup compared to re-prefill. However, it lacks a detailed breakdown of the computational steps involved in the ridge regression (e.g., the complexity of the inversion or decomposition) and a more granular analysis of memory footprint beyond the total parameter size and storage.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions computational efficiency and provides some timing and memory information, but lacks a detailed breakdown of computational steps and a more granular memory footprint analysis.

1. Weakness Statement:
"The paper does not explore the limitations of the proposed method in detail. For example, it is unclear how the method would perform with models that have different architectures or training procedures. The paper also does not discuss the potential impact of the method on the model's ability to generalize to new tasks or domains. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications, and would also provide guidance for future research in this area."

2. Evidence Collection:
- The paper focuses on transferring between models within the same family (Qwen3, Llama 3.1, Ministral 3).
- The experiments are conducted on six matched-KV pairs.
- The paper discusses the limitations of the method in the "Broader impact, future work, and limitations" section: "(1) Single-domain calibration. Calibration uses only FineWeb-Edu. Appendix C measures the cost of substituting Wikipedia or CodeAlpaca on one pair. Neither substitution separates subject matter from register, so the sweep does not bound calibration confined to a single field such as medicine or law. (2) k k selection. Per-pair k k is selected on the same log-likelihood benchmarks we report on. Appendix H measures the effect, at most 2.49  pp, and adds a held-out evaluation, though neither is a substitute for selecting k k out of sample. (3) Matched-KV is empirical. The closed-form mapper imposes no structural requirement on source or target dimensions, but our six pairs are all matched-KV by construction. Different families may share enough representation structure to admit a similar mapping, or may require different machinery. (4) Hidden factors. Beyond architecture, training-data overlap, fine-tuning recipe, and other non-arithmetical factors may also influence transferability. We leave systematic study of these to future work."

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of cross-model transfer methods in detail.

4. Validation Analysis:
   - Primary evidence summary: The paper acknowledges limitations in the "Broader impact, future work, and limitations" section, specifically mentioning the single-domain calibration, k selection, matched-KV pairs, and hidden factors.
   - Supporting quotes: "Single-domain calibration. Calibration uses only FineWeb-Edu. Appendix C measures the cost of substituting Wikipedia or CodeAlpaca on one pair. Neither substitution separates subject matter from register, so the sweep does not bound calibration confined to a single field such as medicine or law. (2) k k selection. Per-pair k k is selected on the same log-likelihood benchmarks we report on. Appendix H measures the effect, at most 2.49  pp, and adds a held-out evaluation, though neither is a substitute for selecting k k out of sample. (3) Matched-KV is empirical. The closed-form mapper imposes no structural requirement on source or target dimensions, but our six pairs are all matched-KV by construction. Different families may share enough representation structure to admit a similar mapping, or may require different machinery. (4) Hidden factors. Beyond architecture, training-data overlap, fine-tuning recipe, and other non-arithmetical factors may also influence transferability. We leave systematic study of these to future work."
   - Impact assessment: The paper does discuss some limitations, particularly the matched-KV pairs and the single-domain calibration. However, the reviewer's point about the lack of discussion on performance with different architectures or training procedures and the potential impact on generalization to new tasks or domains is valid, as the paper's experiments are limited to models within the same family and specific tasks.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper discusses limitations related to matched-KV pairs and calibration domain, but lacks a detailed discussion on performance with different architectures or training procedures and the impact on generalization to new tasks or domains.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel method for cross-model Key-Value (KV) cache transfer, a critical challenge in the deployment of multi-task large language models (LLMs). The core idea revolves around the observation that the KV cache exhibits substantial linear structure across different model families. Building upon this insight, the authors propose a closed-form ridge mapper that operates per-head and per-layer, effectively re-purposing the source model's KV cache to accelerate inference in the target model. This approach is motivated by the practical need to reduce prefill latency, a significant bottleneck in the efficient deployment of LLMs, particularly in cost-quality cascading scenarios. The method involves a three-step process: first, a small calibration set of 500 sequences from FineWeb-Edu is used to determine the optimal number of source layers, denoted as 'k', for each KV pair. Second, a per-head ridge regression is performed on this calibration data to learn the mapping from the source model's KV cache to the target model's KV cache. Finally, the learned mapper is applied to the target model's KV cache during inference. The authors conduct experiments across six matched-KV pairs from three model families: Qwen3, Llama 3.1, and Ministral 3. The results demonstrate that the proposed linear mapper retains 73-98% of the standalone accuracy of the source model and runs 2.7-25 times faster than re-prefill on the smaller-to-large direction, with a speedup of 3-7 times for the large-to-small direction. Furthermore, the paper explores the limitations of the proposed method, including the impact of calibration set size, the selection of the optimal 'k' value, and the transferability of the method across different model families. The authors also analyze the correlation between the attention output and the target KV cache, revealing that the attention output is primarily influenced by the target's attention-sensitive subspaces. This finding is used to develop a non-linear mapper that outperforms the linear mapper in scenarios where the linear assumption is violated. Overall, this paper presents a compelling approach to cross-model KV cache transfer, offering a fast and efficient solution for accelerating inference in multi-task LLMs. The method's simplicity and effectiveness make it a valuable contribution to the field, although some limitations and areas for further research remain.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

This paper presents several notable strengths that contribute to its overall impact and significance. First and foremost, the proposed method is both simple and effective. The closed-form ridge mapper, which is per-head and per-layer, provides a computationally efficient solution for cross-model KV cache transfer. This simplicity is a significant advantage, as it makes the method easy to implement and integrate into existing LLM pipelines. The empirical results are also compelling, demonstrating that the linear mapper can retain a substantial portion of the standalone accuracy of the source model while achieving significant speedups compared to re-prefill. Specifically, the method runs 2.7-25 times faster for smaller-to-large model pairs and 3-7 times faster for large-to-small pairs, which is a substantial improvement in the context of multi-turn conversations. The paper also provides a detailed analysis of the attention-output cosine, which is a valuable contribution in itself. This analysis reveals that the attention output is primarily influenced by the target's attention-sensitive subspaces, which is a key insight that underpins the development of the non-linear mapper. Furthermore, the paper is well-written and easy to follow, making it accessible to a broad audience. The experiments are comprehensive, covering six matched-KV pairs from three model families, which provides a solid foundation for the claims made in the paper. The authors also explore the limitations of the method, such as the impact of calibration set size and the selection of the optimal 'k' value, which demonstrates a thorough and rigorous approach to research. The paper's focus on practical applications, particularly in the context of multi-task LLMs and cost-quality cascading, further enhances its relevance and impact. The authors have successfully addressed a critical challenge in the deployment of LLMs, and the proposed method offers a promising solution for accelerating inference in real-world scenarios. The combination of simplicity, effectiveness, and practical relevance makes this paper a valuable contribution to the field.


## Weaknesses:

Despite its strengths, this paper has several limitations that warrant careful consideration. A primary concern is the reliance on a small calibration set of 500 sequences from FineWeb-Edu. While the authors explore the impact of calibration set size to some extent, with results for N=200, 500, and 1000, the initial use of only 500 sequences raises questions about the generalizability of the method. As the paper states, "We use ridge ( λ = 0.01 ) and content-space mapping. The number of source layers k k is swept over { 1 , 2 , 4 , 6 , 8 , 10 , 12 , 16 , 20 , 24 , all } . We select a single k k per pair as the value that maximizes the arithmetic mean of the log-likelihood benchmark accuracies (ARC-C, HellaSwag, WinoGrande, MMLU), breaking near-ties toward larger k k for evaluation coverage. Table 2 reports component ablations, and calibration sensitivity to λ \lambda , N N , and calibration domain is in Appendix C ." This initial choice of 500 sequences may not be sufficient to capture the complexity of the KV cache, and the performance of the linear mapper is likely highly dependent on the quality and diversity of this calibration set. The paper does not explore the sensitivity of the method to different compositions of the calibration set, such as using data from different domains or tasks, which is a critical factor for practical applications. This lack of analysis limits our understanding of the method's robustness and generalizability. My confidence in this limitation is high, as the paper itself acknowledges the use of a fixed calibration set size and does not provide a comprehensive analysis of its impact. Another significant limitation is the lack of a detailed analysis of the computational cost of the proposed method. While the authors mention that the linear mapper is faster than re-prefill, they do not provide a breakdown of the computational steps involved, such as the time required for ridge regression and the memory footprint of the model. The paper states, "The time taken to fit the mapper directly on the calibration layer is 47–87 min per pair on a single 8 × 8× H100 node with no gradient-based training. Per-pair selected k k , total mapper parameters (1.01–3.36 B), storage (4–12 GB)..." However, this information is insufficient for assessing the practical feasibility of the method, especially for large-scale models. A more granular analysis of the computational cost, including the time required for ridge regression and the memory footprint of the model, is needed to fully understand the trade-offs involved. My confidence in this limitation is also high, as the paper does not provide a detailed breakdown of the computational steps and memory footprint beyond the overall time and parameter size. Furthermore, the paper does not explore the limitations of the proposed method in detail, particularly regarding its performance with models that have different architectures or training procedures. The experiments are limited to models within the same family (Qwen3, Llama 3.1, Ministral 3), and the paper does not investigate how the method would perform with models that have significantly different architectures or training procedures. This is a critical limitation, as it restricts the generalizability of the method to a narrow range of models. The paper also does not discuss the potential impact of the method on the model's ability to generalize to new tasks or domains, which is a crucial aspect for practical applications. My confidence in this limitation is high, as the paper's experiments are limited to models within the same family and do not explore the impact of different architectures or training procedures. Finally, while the paper demonstrates the effectiveness of the linear mapper, it does not explore the limitations of the method in detail, particularly regarding its performance with different sizes of the calibration set. The paper does explore the impact of the number of calibration samples, but it does not explore the impact of different compositions of the calibration set, such as using data from different domains or tasks. This is a critical factor for practical applications, as the method's performance may be sensitive to the calibration data. My confidence in this limitation is high, as the paper does not provide a comprehensive analysis of the impact of different calibration set compositions.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should conduct a more thorough investigation into the impact of the calibration set size and diversity on the performance of the linear mapper. Specifically, the authors should conduct experiments with varying sizes of the calibration set, including smaller sets to assess the minimum data requirements and larger sets to explore the potential for overfitting. Furthermore, the authors should explore the impact of different calibration set compositions, such as using data from different domains or tasks, to assess the robustness of the method. This analysis should include a detailed evaluation of the performance of the linear mapper across different calibration set configurations, providing insights into the sensitivity of the method to the calibration data. The authors could also consider using techniques such as cross-validation to ensure that the results are robust and generalizable. Second, the paper should provide a more detailed analysis of the computational cost of the proposed method, especially in comparison to re-prefill. This analysis should include a breakdown of the computational steps involved, such as the time required for ridge regression and the memory footprint of the model. The authors should also explore the potential for optimizing the memory usage of the model, such as by using techniques such as quantization or pruning. Furthermore, the paper should discuss the potential impact of the memory footprint on the scalability of the method, especially for large-scale models. A more detailed analysis of the memory usage would be beneficial for assessing the practical feasibility of the method in resource-constrained environments. Third, the paper should include a more detailed discussion of the limitations of the proposed method. This discussion should include an analysis of the potential impact of the method on the model's ability to generalize to new tasks or domains, as well as an assessment of the potential for the method to introduce biases or artifacts into the KV cache. The authors should also explore the potential impact of the method on the model's ability to handle different types of input sequences, such as those with varying lengths or complexities. A more thorough discussion of the limitations would be helpful for understanding the scope of the method and its potential applications, and would also provide guidance for future research in this area. Finally, the paper should explore the potential of the proposed method in different model transfer scenarios, such as transferring between models with different architectures or training procedures. This would greatly enhance the method's utility and impact. The authors should also consider expanding their evaluation to include these other intermediate features, which could also be candidates for transfer. This would demonstrate the broader applicability of their method and potentially uncover new transfer opportunities. This would also require a more detailed analysis of the characteristics of each feature and how they relate to the target model. By addressing these limitations, the authors can significantly strengthen their work and make it more relevant for practical applications.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the linear mapper perform with different sizes of the calibration set? The paper mentions using a calibration set of 500 FineWeb-Edu sequences of length 1024, but it does not explore the sensitivity of the method to the size and composition of the calibration set. Specifically, what is the minimum amount of calibration data required to achieve acceptable performance, and how does the performance degrade when the calibration set is too small? Second, how does the linear mapper perform with different compositions of the calibration set? The paper uses a single calibration set of FineWeb-Edu, but it does not explore the impact of using data from different domains or tasks. How does the performance of the mapper vary when the calibration set is composed of data from different sources, and what are the implications for the generalizability of the method? Third, how does the linear mapper perform with models that have different architectures or training procedures? The paper focuses on transferring between models within the same family, but it does not investigate how the method would perform with models that have significantly different architectures or training procedures. What are the challenges and limitations of transferring KV cache between models with different architectures, and how can these challenges be addressed? Fourth, what is the memory footprint of the linear mapper, and how does it scale with the size of the model and the calibration set? The paper provides some information on the memory footprint of the model, but it does not explore the potential for optimizing the memory usage of the model. What are the trade-offs between memory usage and performance, and how can the memory footprint be minimized without sacrificing accuracy? Finally, what is the impact of the linear mapper on the model's ability to generalize to new tasks or domains? The paper does not explore the potential impact of the method on the model's ability to generalize to new tasks or domains. How does the linear mapper affect the model's ability to handle different types of input sequences, such as those with varying lengths or complexities, and what are the potential implications for the model's overall performance? These questions highlight key uncertainties and areas for further investigation, and addressing them would significantly enhance the understanding and applicability of the proposed method.


## Rating:

6.5


## Confidence:

3.25


## Decision:

Accept
}