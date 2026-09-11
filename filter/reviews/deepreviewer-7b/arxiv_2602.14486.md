I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper revisits the "Platonic Representation Hypothesis" (Huh et al., 2024), which states that as neural networks scale, their representations converge across different modalities. The authors identify two main biases affecting similarity metrics: a "width confounder" due to increasing dimensionality and a "depth confounder" from the number of layers. To address these, they propose a permutation-based calibration framework that transforms similarity scores into calibrated scores with a principled null reference. Applying this framework, they find that global metric similarities lack significant convergence, while local neighborhood similarities remain consistent, suggesting the "Aristotelian Representation Hypothesis" instead, where local relationships align across models.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective in addressing the identified confounders.

### Weaknesses

#### Some Related Works


#### comment

1. The primary weakness is the limited scope of the evaluation. The study is restricted to a single dataset and a narrow set of models, which raises concerns about the generalizability of the findings. Specifically, the use of only the WIT dataset, which consists of image-text pairs, limits the applicability of the conclusions to other modalities or data types. Furthermore, the selection of only three language model families and five vision model families, without a clear justification for their representativeness, makes it difficult to assess the robustness of the proposed calibration framework across diverse architectures and scales. This narrow evaluation scope weakens the claim that the observed effects are universal and not specific to the chosen models and dataset.
2. The paper lacks a thorough comparison with existing methods for calibrating neural network representations. While the authors introduce a permutation-based calibration, they do not adequately position it within the broader landscape of representation alignment techniques. For instance, methods that use optimal transport or other distance metrics for alignment are not discussed or compared against. This omission makes it challenging to evaluate the novelty and effectiveness of the proposed approach relative to established techniques. A more comprehensive comparison would clarify the advantages and limitations of the permutation-based method.
3. The paper does not sufficiently explore the sensitivity of the calibration framework to different permutation strategies or sample sizes. The choice of permutation method can significantly impact the calibration results, and the paper does not provide a detailed analysis of how different permutation schemes affect the calibrated scores. Similarly, the impact of varying sample sizes on the stability and reliability of the calibration is not thoroughly investigated. This lack of sensitivity analysis raises concerns about the robustness of the calibration framework and its applicability in scenarios with limited data.

### Suggestions

To address the limited scope of the evaluation, the authors should expand their experiments to include a more diverse set of datasets and model architectures. This should include datasets beyond image-text pairs, such as those involving audio, time-series data, or other modalities. Furthermore, the selection of models should be expanded to encompass a wider range of architectures, including transformers of varying sizes and convolutional networks. This would provide a more comprehensive assessment of the proposed calibration framework and its applicability across different domains and model types. It would also be beneficial to include models with different training objectives or pre-training datasets to investigate whether the observed effects are consistent across different learning paradigms. Such an expanded evaluation would significantly strengthen the generalizability of the findings and the claims made in the paper.

To better position the proposed permutation-based calibration method, the authors should include a more thorough comparison with existing techniques for calibrating neural network representations. This should include a discussion of methods that use optimal transport, such as Gromov-Wasserstein distance, for aligning representations. The authors should also compare their method with techniques that use contrastive learning or other self-supervised learning approaches for representation calibration. A detailed comparison should not only highlight the differences in methodology but also analyze the strengths and weaknesses of each approach in terms of computational complexity, calibration accuracy, and robustness to different types of data. This would provide a more comprehensive understanding of the proposed method's novelty and its place within the broader landscape of representation calibration techniques. Furthermore, the authors should discuss the limitations of their permutation-based approach, such as its computational cost for very large datasets, and suggest potential solutions.

Finally, the authors should conduct a more detailed sensitivity analysis of the calibration framework to different permutation strategies and sample sizes. This should include an investigation of how different permutation schemes, such as random permutations versus structured permutations, affect the calibrated scores. The authors should also analyze the impact of varying sample sizes on the stability and reliability of the calibration. This analysis should include a discussion of the trade-offs between computational cost and calibration accuracy when choosing different sample sizes. It would also be beneficial to provide guidelines for selecting appropriate permutation strategies and sample sizes based on the specific characteristics of the dataset and model being used. This would make the proposed calibration framework more practical and applicable in real-world scenarios.

### Questions

1. How does the proposed method perform on other datasets and model architectures? Are there specific types of data or models where the calibration framework is more or less effective?
2. Could the permutation-based calibration be computationally intensive for very large datasets? How does the computational cost scale with the size of the data and model?
3. Are there alternative calibration methods that could be compared with the permutation-based approach? How does the proposed method perform relative to these alternatives in terms of calibration accuracy and computational efficiency?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper addresses the biases introduced by width and depth confounders when measuring representational similarity between neural networks. The authors propose a permutation-based null-calibration framework to correct for these biases, which transforms any representational similarity metric into a calibrated score with a principled null reference. This framework is then applied to revisit the Platonic Representation Hypothesis, finding that global spectral metrics lack significant convergence, while local neighborhood metrics remain consistent across different modalities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough theoretical analysis of the biases introduced by width and depth confounders, which is crucial for understanding the limitations of existing representational similarity metrics.
3. The permutation-based calibration framework is simple yet effective, and the authors demonstrate its applicability across various metrics, including spectral, neighborhood, and geometric measures.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the calibration of representational similarity metrics. However, it does not delve deeply into the specific challenges and nuances of applying these metrics to different types of neural network architectures. For instance, the calibration framework might need adjustments for architectures with skip connections or attention mechanisms, which are not discussed in detail. The paper should explore how the permutation-based calibration interacts with these architectural features, as the presence of skip connections or attention mechanisms can significantly alter the flow of information and the resulting representations. This lack of specificity limits the practical applicability of the framework.
2. While the permutation-based calibration framework is effective, it may not be computationally efficient for very large-scale models or datasets. The computational cost of generating K permutations, especially for high-dimensional representations, could become prohibitive. The paper should provide a more detailed analysis of the computational complexity of the proposed method and discuss potential strategies for mitigating this issue, such as using approximate permutation sampling techniques or parallelization. Furthermore, the paper should explore the trade-off between computational cost and calibration accuracy, as using a large number of permutations might not always be necessary to achieve a reliable calibration.
3. The paper applies the calibration framework to the Platonic Representation Hypothesis, which is a valuable contribution. However, the paper could benefit from a more in-depth discussion of the implications of the calibrated results for understanding the learning dynamics of neural networks. For example, how does the calibrated similarity metric relate to the training process and the generalization performance of the models? The paper should explore whether the calibrated results can provide insights into the mechanisms underlying the observed convergence or divergence of representations. This would strengthen the connection between the calibration framework and the broader understanding of neural network learning.

### Suggestions

The paper would significantly benefit from a more detailed exploration of how the proposed permutation-based calibration framework interacts with different neural network architectures. Specifically, the authors should investigate the impact of skip connections and attention mechanisms on the calibration process. For skip connections, it would be valuable to analyze whether the permutation-based calibration needs to be adjusted to account for the direct connections between layers. For attention mechanisms, the authors should discuss how the permutation of tokens or channels affects the calibration and whether any specific strategies are needed to ensure accurate calibration. This analysis should include both theoretical considerations and empirical evaluations on models with these architectural features. Furthermore, the authors should provide guidelines for practitioners on how to apply the calibration framework to different architectures, including those with complex combinations of skip connections and attention mechanisms. This would greatly enhance the practical applicability of the proposed method.

To address the computational concerns, the authors should provide a more thorough analysis of the computational complexity of the proposed permutation-based calibration framework. This analysis should include a breakdown of the time and memory requirements for each step of the algorithm, such as the permutation generation and the similarity metric calculation. The authors should also explore and discuss potential strategies for reducing the computational cost, such as using approximate permutation sampling techniques, parallelization, or other optimization methods. Furthermore, the paper should include a detailed discussion of the trade-off between computational cost and calibration accuracy. This discussion should provide practical guidance on how to choose the number of permutations based on the available computational resources and the desired level of accuracy. The authors should also consider providing an implementation of the calibration framework to facilitate its adoption by the research community.

Finally, the paper should delve deeper into the implications of the calibrated results for understanding the learning dynamics of neural networks. The authors should explore whether the calibrated similarity metric can provide insights into the mechanisms underlying the observed convergence or divergence of representations. For example, can the calibrated metric reveal how representations evolve during training, or whether it correlates with the generalization performance of the models? The authors should also discuss the potential limitations of the calibrated metric and whether it can be used to identify specific properties of the learned representations. This discussion should include both theoretical considerations and empirical evaluations, and it should provide a more comprehensive understanding of the relationship between the calibration framework and the broader understanding of neural network learning.

### Questions

1. How does the permutation-based calibration framework handle architectures with skip connections or attention mechanisms?
2. What is the computational complexity of the proposed calibration framework, and how does it scale with the size of the models and datasets?
3. How does the calibrated similarity metric relate to the training process and the generalization performance of the models?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper revisits the Platonic Representation Hypothesis (Huh et al., 2024), which posits that as neural networks scale, their representations converge to a shared structure across modalities. The authors identify two confounding factors that distort the interpretation of representational similarity metrics: (1) the width confounder, where increasing model dimensionality introduces a systematic bias, and (2) the depth confounder, where the number of layers in the model can inflate similarity scores. To address these issues, the authors propose a permutation-based calibration framework that transforms any representational similarity metric into a calibrated score with a principled null reference. Applying this framework to the Platonic Representation Hypothesis reveals that global spectral metrics lack significant convergence, while local neighborhood metrics remain consistent, suggesting a refined "Aristotelian Representation Hypothesis" where local relationships align across models, rather than global geometry.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written, and the problem is well-motivated. The authors clearly identify two key confounding factors—width and depth—that can bias representational similarity metrics, and they propose a permutation-based calibration framework to address these issues. The framework is general and can be applied to any similarity metric, making it a valuable tool for the community. The authors apply their framework to the Platonic Representation Hypothesis, a timely and important problem in the field of neural network representation learning. The results are insightful and suggest a refined "Aristotelian Representation Hypothesis" where local relationships align across models, rather than global geometry. The paper is well-organized and easy to follow, with clear explanations of the methods and results.

### Weaknesses

#### Some Related Works


#### comment

While the paper is well-written and the problem is well-motivated, the authors could further elaborate on the limitations of their approach. For example, the permutation-based calibration framework may be computationally expensive for very large models or datasets, and the authors could discuss potential strategies for mitigating this issue. Additionally, the authors could provide more details on the choice of permutation strategy and its impact on the calibration results. Finally, while the authors apply their framework to the Platonic Representation Hypothesis, it would be interesting to see how it performs on other tasks or datasets.

### Suggestions

The authors should delve deeper into the computational cost associated with their permutation-based calibration framework. Specifically, they should analyze the time complexity of generating the permutations and how this scales with the number of samples, model parameters, and the dimensionality of the representations. It would be beneficial to explore and discuss potential approximations or optimizations that could reduce the computational burden without significantly compromising the accuracy of the calibration. For instance, instead of generating all possible permutations, they could consider using a subset of permutations or employing more efficient sampling techniques. Furthermore, the authors should provide a more detailed analysis of the impact of different permutation strategies on the calibration results. For example, they could compare the performance of random permutations with other strategies, such as those based on specific data augmentations or structural properties of the data. This analysis would help to understand the sensitivity of the calibration framework to the choice of permutation strategy and provide guidance on selecting the most appropriate strategy for different scenarios.

To further strengthen the paper, the authors should provide a more comprehensive evaluation of their calibration framework on a wider range of tasks and datasets. While the application to the Platonic Representation Hypothesis is insightful, it would be valuable to demonstrate the generalizability of the framework by applying it to other problems in representation learning. For example, they could consider tasks such as image classification, object detection, or natural language processing. This would help to establish the robustness and versatility of the framework and provide a more complete picture of its capabilities. Additionally, the authors should explore the sensitivity of their framework to different choices of similarity metrics. While they mention that the framework is general and can be applied to any similarity metric, it would be useful to provide a more detailed analysis of how the choice of metric affects the calibration results. This analysis could include a comparison of different similarity metrics, such as cosine similarity, Euclidean distance, or correlation coefficients, and their impact on the calibrated scores.

Finally, the authors should provide more details on the practical implementation of their framework. This includes specifying the software libraries and tools used, as well as the computational resources required for different experiments. They should also discuss any specific considerations or challenges that arise when applying the framework to different types of data or models. This would make it easier for other researchers to reproduce their results and apply the framework to their own work. Furthermore, the authors should consider providing a software package or toolbox that implements their framework, which would further facilitate its adoption by the community. This package should include clear documentation and examples to help users understand how to use the framework effectively.

### Questions

- Could you provide more details on the computational cost of your permutation-based calibration framework? How does it scale with the size of the models or datasets?
- How sensitive is the framework to the choice of permutation strategy? Have you explored different strategies, and if so, what were the results?
- Have you considered applying your framework to other tasks or datasets beyond the Platonic Representation Hypothesis? If so, what were the results?
- Could you elaborate on the practical implementation of your framework? Specifically, what software libraries or tools are required, and what computational resources are needed?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper addresses the issue of biases in representational similarity metrics, specifically the "width" and "depth" confounders, which distort the interpretation of these metrics. The authors propose a permutation-based calibration framework that transforms any similarity metric into a calibrated score with a principled null reference. This framework is then applied to revisit the Platonic Representation Hypothesis, revealing that global spectral metrics lack significant convergence, while local neighborhood metrics remain consistent across modalities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors clearly identify two key confounding factors—width and depth—that can bias representational similarity metrics.
3. The proposed permutation-based calibration framework is general and can be applied to any similarity metric, making it a valuable tool for the community.
4. The application of the framework to the Platonic Representation Hypothesis provides valuable insights into the nature of neural network representations.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the calibration of representational similarity metrics. However, it does not delve deeply into the specific challenges and nuances of applying these metrics to different types of neural network architectures. For instance, the calibration framework might need adjustments for architectures with skip connections or attention mechanisms, which are not discussed in detail. The paper should explore how the permutation-based calibration interacts with these architectural features, as the presence of skip connections or attention mechanisms can significantly alter the flow of information and the resulting representations. This lack of specificity limits the practical applicability of the framework.
2. While the permutation-based calibration framework is effective, it may not be computationally efficient for very large-scale models or datasets. The computational cost of generating K permutations, especially for high-dimensional representations, could become prohibitive. The paper should provide a more detailed analysis of the computational complexity of the proposed method and discuss potential strategies for mitigating this issue, such as using approximate permutation sampling techniques or parallelization. Furthermore, the paper should explore the trade-off between computational cost and calibration accuracy, as using a large number of permutations might not always be necessary to achieve a reliable calibration.
3. The paper applies the calibration framework to the Platonic Representation Hypothesis, which is a valuable contribution. However, the paper could benefit from a more in-depth discussion of the implications of the calibrated results for understanding the learning dynamics of neural networks. For example, how does the calibrated similarity metric relate to the training process and the generalization performance of the models? The paper should explore whether the calibrated results can provide insights into the mechanisms underlying the observed convergence or divergence of representations. This would strengthen the connection between the calibration framework and the broader understanding of neural network learning.

### Suggestions

The authors should provide a more detailed analysis of how their permutation-based calibration framework interacts with different neural network architectures, particularly those incorporating skip connections and attention mechanisms. For skip connections, it would be beneficial to investigate whether the permutation process needs to be adjusted to account for the direct connections between layers. For attention mechanisms, the authors should discuss how the permutation of tokens or channels affects the calibration and whether any specific strategies are needed to ensure accurate calibration. This analysis should include both theoretical considerations and empirical evaluations on models with these architectural features. Furthermore, the authors should provide clear guidelines for practitioners on how to apply the calibration framework to different architectures, including those with complex combinations of skip connections and attention mechanisms. This would greatly enhance the practical applicability of the proposed method.

To address the computational concerns, the authors should provide a more thorough analysis of the computational complexity of their permutation-based calibration framework. This analysis should include a breakdown of the time and memory requirements for each step of the algorithm, such as the permutation generation and the similarity metric calculation. The authors should also explore and discuss potential strategies for reducing the computational cost, such as using approximate permutation sampling techniques, parallelization, or other optimization methods. Furthermore, the paper should include a detailed discussion of the trade-off between computational cost and calibration accuracy. This discussion should provide practical guidance on how to choose the number of permutations based on the available computational resources and the desired level of accuracy. The authors could also consider providing an implementation of the calibration framework to facilitate its adoption by the research community.

Finally, the authors should expand on the implications of their calibrated results for understanding the learning dynamics of neural networks. This should include a discussion of how the calibrated similarity metric relates to the training process and the generalization performance of the models. For example, the authors could investigate whether the calibrated results can reveal how representations evolve during training or whether they correlate with the generalization performance of the models. This analysis should also explore whether the calibrated results can provide insights into the mechanisms underlying the observed convergence or divergence of representations. This would strengthen the connection between the calibration framework and the broader understanding of neural network learning. The authors should also consider exploring the relationship between the calibrated similarity metric and other measures of representation similarity, such as those based on optimal transport or kernel methods.

### Questions

1. How does the permutation-based calibration framework handle architectures with skip connections or attention mechanisms?
2. What is the computational complexity of the proposed calibration framework, and how does it scale with the size of the models and datasets?
3. How does the calibrated similarity metric relate to the training process and the generalization performance of the models?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper provided.

For each weakness, I will:
1. **State the weakness** as quoted from the reviewer.
2. **Collect evidence** from the paper to support or refute the weakness. This will involve looking at the method description, experimental setup, results, and related work.
3. **Analyze literature gaps** by checking if the paper misses relevant citations or comparisons.
4. **Provide a validation analysis** summarizing the evidence and its impact.
5. **Conclude** whether the weakness is valid, partially valid, or invalid, and state my confidence level.

Let's start with Reviewer 1.
**Review 1 Weakness Analysis:**

1. Weakness Statement:
"The paper primarily focuses on the calibration of representational similarity metrics. However, it does not delve deeply into the specific challenges and nuances of applying these metrics to different types of neural network architectures. For instance, the calibration framework might need adjustments for architectures with skip connections or attention mechanisms, which are not discussed in detail. The paper should explore how the permutation-based calibration interacts with these architectural features, as the presence of skip connections or attention mechanisms can significantly alter the flow of information and the resulting representations. This lack of specificity limits the practical applicability of the framework."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the permutation-based calibration framework in Section 4, focusing on general principles and mathematical formulations. There is no specific discussion about how skip connections or attention mechanisms might affect the calibration.
   - The examples provided in the "method" section (e.g., CKA calculation) are general and do not involve specific architectural details.
b) Experiment-related Evidence:
   - The "experiments" section (Section 6) describes the datasets and models used, but there is no mention of models with skip connections or attention mechanisms like Transformers. The models used are primarily language models and ViTs.

3. Literature Gap Analysis:
   - The paper cites works related to representational similarity metrics and calibration, but it doesn't specifically engage with literature discussing the interaction of these metrics with different architectural features like skip connections or attention mechanisms.

4. Validation Analysis:
   - The reviewer correctly points out that the paper's focus is primarily on the calibration framework itself, and it doesn't delve into the nuances of applying these metrics to architectures with specific features like skip connections or attention. The method description and experiments are general and do not address these architectural complexities. The reviewer's concern about the potential need for adjustments in the calibration framework for these architectures is valid, as the paper doesn't provide any such analysis.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The method section focuses on general principles, and the experiments do not include models with skip connections or attention mechanisms.

---

1. Weakness Statement:
"While the permutation-based calibration framework is effective, it may not be computationally efficient for very large-scale models or datasets. The computational cost of generating K permutations, especially for high-dimensional representations, could become prohibitive. The paper should provide a more detailed analysis of the computational complexity of the proposed method and discuss potential strategies for mitigating this issue, such as using approximate permutation sampling techniques or parallelization. Furthermore, the paper should explore the trade-off between computational cost and calibration accuracy, as using a large number of permutations might not always be necessary to achieve a reliable calibration."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Calibration Framework" component in the "method/details" section mentions generating "K permutations" of the samples. The computational cost of this step is not explicitly analyzed.
   - The "Calibrated Score" component describes the calculation involving the K-th order statistic, which depends on K.
b) Experiment-related Evidence:
   - The "Null-calibration removes width confounder" experiment mentions "K=200 permutations" but doesn't discuss the computational cost associated with this choice.
   - The "Revisiting the Platonic Representation Hypothesis" experiment also mentions "K=200 permutations" without a detailed computational analysis.

3. Literature Gap Analysis:
   - While the paper cites works on permutation tests, it doesn't discuss the computational challenges associated with large-scale permutation testing or alternative methods for efficiency.

4. Validation Analysis:
   - The reviewer's concern about the computational cost is valid. Generating K permutations, especially for high-dimensional data and large models, can be computationally expensive. The paper does not provide a detailed analysis of this complexity or discuss strategies for mitigation. The trade-off between computational cost and accuracy is also not explored.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The method description involves generating K permutations, and the experimental sections mention the value of K without computational analysis.

---

1. Weakness Statement:
"The paper applies the calibration framework to the Platonic Representation Hypothesis, which is a valuable contribution. However, the paper could benefit from a more in-depth discussion of the implications of the calibrated results for understanding the learning dynamics of neural networks. For example, how does the calibrated similarity metric relate to the training process and the generalization performance of the models? The paper should explore whether the calibrated results can provide insights into the mechanisms underlying the observed convergence or divergence of representations. This would strengthen the connection between the calibration framework and the broader understanding of neural network learning."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Calibration Framework" section focuses on the mathematical formulation of the calibration process.
b) Experiment-related Evidence:
   - The "Null-calibration removes width confounder" experiment shows the effect of calibration on the CKA score, indicating the presence of the width confounder.
   - The "Revisiting the Platonic Representation Hypothesis" experiment shows the calibrated CKA scores, indicating the lack of global convergence and presence of local convergence.
   - The paper does not explicitly discuss the relationship between the calibrated similarity metric and the training process or generalization performance.

3. Literature Gap Analysis:
   - The paper cites works related to the Platonic Representation Hypothesis, but it doesn't connect its calibration framework to the broader literature on understanding learning dynamics and generalization.

4. Validation Analysis:
   - The reviewer's point is valid. While the paper demonstrates the effectiveness of the calibration framework in addressing the width and depth confounders, it lacks a discussion on how these calibrated metrics relate to the training process and generalization capabilities of the models. Exploring these connections would provide a deeper understanding of the implications of the calibrated results.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper focuses on calibration and the Platonic Representation Hypothesis but lacks discussion on the relationship with training dynamics and generalization.

**Review 2 Weakness Analysis:**

1. Weakness Statement:
"The primary weakness is the limited scope of the evaluation. The study is restricted to a single dataset and a narrow set of models, which raises concerns about the generalizability of the findings. Specifically, the use of only the WIT dataset, which consists of image-text pairs, limits the applicability of the conclusions to other modalities or data types. Furthermore, the selection of only three language model families and five vision model families, without a clear justification for their representativeness, makes it difficult to assess the robustness of the proposed calibration framework across diverse architectures and scales. This narrow evaluation scope weakens the claim that the observed effects are universal and not specific to the chosen models and dataset."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "Null-calibration removes width confounder" experiment uses the WIT dataset.
   - The "Calibration framework on neural network similarity" experiment uses the same WIT dataset.
   - The "Revisiting the Platonic Representation Hypothesis" experiment uses the WIT dataset.
   - The models used are primarily language models (BLOOM, OpenLLaMA, LLaMA) and Vision Models (ImageNet-21K, MAE, DINOv2, CLIP, CLIP-finetuned).
   - The paper does not explicitly justify the selection of these specific models.

3. Literature Gap Analysis:
   - While the paper cites relevant works, it doesn't discuss the limitations of its dataset and model choices in the context of the broader literature on representational similarity analysis.

4. Validation Analysis:
   - The reviewer's criticism regarding the limited scope of evaluation is valid. The experiments are primarily conducted on the WIT dataset, which consists of image-text pairs. While the paper includes a reasonable number of models, the justification for their representativeness is missing. This narrow scope does raise concerns about the generalizability of the findings to other modalities and data types.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The experiments are primarily conducted on the WIT dataset, and the justification for the model selection is absent.

---

1. Weakness Statement:
"The paper lacks a thorough comparison with existing methods for calibrating neural network representations. While the authors introduce a permutation-based calibration, they do not adequately position it within the broader landscape of representation alignment techniques. For instance, methods that use optimal transport or other distance metrics for alignment are not discussed or compared against. This omission makes it challenging to evaluate the novelty and effectiveness of the proposed approach relative to established techniques. A more comprehensive comparison would clarify the advantages and limitations of the permutation-based method."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Related work" section (Section 2) discusses representational similarity metrics and the Platonic Representation Hypothesis but does not include a detailed comparison with methods for calibrating neural network representations using optimal transport or other alignment techniques.
b) Experiment-related Evidence:
   - The experiments focus on comparing the calibrated metrics with and without calibration, not against other calibration methods.

3. Literature Gap Analysis:
   - The "Related work" section mentions "representational similarity metrics" and "replicability of representational similarity metrics" but lacks a discussion of calibration methods using optimal transport or other alignment techniques.

4. Validation Analysis:
   - The reviewer's criticism is valid. The paper introduces a novel calibration framework but does not adequately compare it with existing methods for calibrating neural network representations, particularly those based on optimal transport. This lack of comparison makes it difficult to assess the novelty and advantages of the proposed method.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The "Related work" section does not discuss or compare the proposed method with calibration techniques using optimal transport.

---

1. Weakness Statement:
"The paper does not sufficiently explore the sensitivity of the calibration framework to different permutation strategies or sample sizes. The choice of permutation method can significantly impact the calibration results, and the paper does not provide a detailed analysis of how different permutation schemes affect the calibrated scores. Similarly, the impact of varying sample sizes on the stability and reliability of the calibration is not thoroughly investigated. This lack of sensitivity analysis raises concerns about the robustness of the calibration framework and its applicability in scenarios with limited data."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Calibration Framework" section describes the use of random permutations but doesn't explore alternative strategies.
   - The "Calibrated Score" component mentions the K-th order statistic, which is influenced by the sample size N.
b) Experiment-related Evidence:
   - The experiments use a fixed number of permutations (K=200) and don't explore the impact of varying K or sample sizes.

3. Literature Gap Analysis:
   - The paper cites works on permutation tests but doesn't delve into the sensitivity of permutation-based methods to different choices of permutations or sample sizes.

4. Validation Analysis:
   - The reviewer's concern about the lack of sensitivity analysis is valid. The paper does not explore the impact of different permutation strategies or varying sample sizes on the calibration results. This lack of analysis raises concerns about the robustness and generalizability of the calibration framework.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The method description focuses on random permutations, and the experiments use a fixed number of permutations without exploring alternatives.

**Review 3 Weakness Analysis:**

1. Weakness Statement:
"While the paper is well-written and the problem is well-motivated, the authors could further elaborate on the limitations of their approach. For example, the permutation-based calibration framework may be computationally expensive for very large models or datasets, and the authors could discuss potential strategies for mitigating this issue. Additionally, the authors could provide more details on the choice of permutation strategy and its impact on the calibration results. Finally, while the authors apply their framework to the Platonic Representation Hypothesis, it would be interesting to see how it performs on other tasks or datasets."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Calibration Framework" section describes the use of random permutations but doesn't discuss alternative strategies.
b) Experiment-related Evidence:
   - The experiments use a fixed number of permutations (K=200) without exploring alternatives or discussing computational costs.
   - The experiments focus on the Platonic Representation Hypothesis.

3. Literature Gap Analysis:
   - The paper cites works on permutation tests but doesn't discuss the limitations of permutation-based methods in terms of computational cost or alternative strategies.

4. Validation Analysis:
   - The reviewer's points are valid. The paper could benefit from a more detailed discussion of the limitations of the permutation-based calibration framework, particularly regarding computational cost. Furthermore, exploring the impact of different permutation strategies and applying the framework to other tasks or datasets would strengthen the paper.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks a detailed discussion on the limitations of the permutation-based approach and doesn't explore other tasks or datasets.

---

1. Weakness Statement:
"The authors should delve deeper into the computational cost associated with their permutation-based calibration framework. Specifically, they should analyze the time complexity of generating the permutations and how this scales with the number of samples, model parameters, and the dimension of the data. The authors should also explore and discuss potential approximations or optimizations that could reduce the computational burden without significantly compromising the accuracy of the calibration. Furthermore, the paper should include a detailed discussion of the trade-off between computational cost and calibration accuracy, as using a large number of permutations might not always be necessary to achieve a reliable calibration."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Calibration Framework" section describes the generation of K permutations but does not analyze the computational complexity.
b) Experiment-related Evidence:
   - The experiments use a fixed number of permutations (K=200) without discussing the computational cost or the trade-off between K and accuracy.

3. Literature Gap Analysis:
   - The paper cites works on permutation tests but doesn't discuss the computational challenges or optimization strategies for large-scale permutation testing.

4. Validation Analysis:
   - This is a more detailed reiteration of the computational cost concern raised by Reviewer 1 and is valid for the same reasons.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The method section describes permutation generation without computational analysis, and the experiments use a fixed number of permutations without discussing the trade-off.

---

1. Weakness Statement:
"Finally, the authors should provide more details on the practical implementation of their framework. This includes specifying the software libraries and tools used, as well as the computational resources required for different experiments. They should also discuss any specific considerations or challenges that arise when applying the framework to different types of data or models. This would make it easier for other researchers to reproduce their results and apply the framework to their own work. Furthermore, the authors should consider providing an implementation of the framework to facilitate its adoption by the research community. This package should include clear documentation and examples to help users understand how to use the framework effectively."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Method" section provides a mathematical description of the framework but lacks details on implementation specifics.
b) Experiment-related Evidence:
   - The "Experiments" section describes the setup and results but doesn't provide details on the software libraries, computational resources, or specific implementation challenges.

3. Literature Gap Analysis:
   - The paper focuses on the theoretical framework and doesn't discuss practical implementation details or provide code.

4. Validation Analysis:
   - The reviewer's point about the lack of practical implementation details is valid. The paper focuses on the theoretical aspects and doesn't provide sufficient information for others to easily reproduce the results or implement the framework.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks details on software libraries, computational resources, and implementation challenges.

**Review 4 Weakness Analysis:**

1. Weakness Statement:
"The paper primarily focuses on the calibration of representational similarity metrics. However, it does not delve deeply into the specific challenges and nuances of applying these metrics to different types of neural network architectures. For instance, the calibration framework might need adjustments for architectures with skip connections or attention mechanisms, which are not discussed in detail. The paper should explore how the permutation-based calibration interacts with these architectural features, as the presence of skip connections or attention mechanisms can significantly alter the flow of information and the resulting representations. This lack of specificity limits the practical applicability of the framework."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1 and is valid for the same reasons.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1.

---

1. Weakness Statement:
"While the permutation-based calibration framework is effective, it may not be computationally efficient for very large-scale models or datasets. The computational cost of generating K permutations, especially for high-dimensional representations, could become prohibitive. The paper should provide a more detailed analysis of the computational complexity of the proposed method and discuss potential strategies for mitigating this issue, such as using approximate permutation sampling techniques or parallelization. Furthermore, the paper should explore the trade-off between computational cost and calibration accuracy, as using a large number of permutations might not always be necessary to achieve a reliable calibration."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1 and Reviewer 3 and is valid for the same reasons.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and Reviewer 3.

4. Validation Analysis:
   - Same as Reviewer 1 and Reviewer 3.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1 and Reviewer 3.

---

1. Weakness Statement:
"The paper applies the calibration framework to the Platonic Representation Hypothesis, which is a valuable contribution. However, the paper could benefit from a more in-depth discussion of the implications of the calibrated results for understanding the learning dynamics of neural networks. For example, how does the calibrated similarity metric relate to the training process and the generalization performance of the models? The paper should explore whether the calibrated results can provide insights into the mechanisms underlying the observed convergence or divergence of representations. This would strengthen the connection between the calibration framework and the broader understanding of neural network learning."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1 and is valid for the same reasons.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1.

---

1. Weakness Statement:
"The primary weakness is the limited scope of the evaluation. The study is restricted to a single dataset and a narrow set of models, which raises concerns about the generalizability of the findings. Specifically, the use of only the WIT dataset, which consists of image-text pairs, limits the applicability of the conclusions to other modalities or data types. Furthermore, the selection of only three language model families and five vision model families, without a clear justification for their representativeness, makes it difficult to assess the robustness of the proposed calibration framework across diverse architectures and scales. This narrow evaluation scope weakens the claim that the observed effects are universal and not specific to the chosen models and dataset."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 2 and is valid for the same reasons.

3. Literature Gap Analysis:
   - Same as Reviewer 2.

4. Validation Analysis:
   - Same as Reviewer 2.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 2.

---

1. Weakness Statement:
"The paper lacks a thorough comparison with existing methods for calibrating neural network representations. While the authors introduce a permutation-based calibration, they do not adequately position it within the broader landscape of representation alignment techniques. For instance, methods that use optimal transport or other distance metrics for alignment are not discussed or compared against. This omission makes it challenging to evaluate the novelty and effectiveness of the proposed approach relative to established techniques. A more comprehensive comparison would clarify the advantages and limitations of the permutation-based method."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 2 and is valid for the same reasons.

3. Literature Gap Analysis:
   - Same as Reviewer 2.

4. Validation Analysis:
   - Same as Reviewer 2.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 2.

---

1. Weakness Statement:
"The paper does not sufficiently explore the sensitivity of the calibration framework to different permutation strategies or sample sizes. The choice of permutation method can significantly impact the calibration results, and the paper does not provide a detailed analysis of how different permutation schemes affect the calibrated scores. Similarly, the impact of varying sample sizes on the stability and reliability of the calibration is not thoroughly investigated. This lack of sensitivity analysis raises concerns about the robustness of the calibration framework and its applicability in scenarios with limited data."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 2 and Reviewer 3 and is valid for the same reasons.

3. Literature Gap Analysis:
   - Same as Reviewer 2 and Reviewer 3.

4. Validation Analysis:
   - Same as Reviewer 2 and Reviewer 3.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 2 and Reviewer 3.

---

1. Weakness Statement:
"While the paper is well-written and the problem is well-motivated, the authors could further elaborate on the limitations of their approach. For example, the permutation-based calibration framework may be computationally expensive for very large models or datasets, and the authors could discuss potential strategies for mitigating this issue. Additionally, the authors could provide more details on the choice of permutation strategy and its impact on the calibration results. Finally, while the authors apply their framework to the Platonic Representation Hypothesis, it would be interesting to see how it performs on other tasks or datasets."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 3 and is valid for the same reasons.

3. Literature Gap Analysis:
   - Same as Reviewer 3.

4. Validation Analysis:
   - Same as Reviewer 3.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 3.

---

1. Weakness Statement:
"The authors should delve deeper into the computational cost associated with their permutation-based calibration framework. Specifically, they should analyze the time complexity of generating the permutations and how this scales with the number of samples, model parameters, and the dimension of the data. The authors should also explore and discuss potential approximations or optimizations that could reduce the computational burden without significantly compromising the accuracy of the calibration. Furthermore, the paper should include a detailed discussion of the trade-off between computational cost and calibration accuracy, as using a large number of permutations might not always be necessary to achieve a reliable calibration."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1, Reviewer 3, and Reviewer 4 and is valid for the same reasons.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Reviewer 3, and Reviewer 4.

4. Validation Analysis:
   - Same as Reviewer 1, Reviewer 3, and Reviewer 4.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Reviewer 3, and Reviewer 4.

---

1. Weakness Statement:
"Finally, the authors should provide more details on the practical implementation of their framework. This includes specifying the software libraries and tools used, as well as the computational resources required for different experiments. They should also discuss any specific considerations or challenges that arise when applying the framework to different types of data or models. This would make it easier for other researchers to reproduce their results and apply the framework to their own work. Furthermore, the authors should consider providing an implementation of the framework to facilitate its adoption by the research community. This package should include clear documentation and examples to help users understand how to use the framework effectively."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 3 and is valid for the same reasons.

3. Literature Gap Analysis:
   - Same as Reviewer 3.

4. Validation Analysis:
   - Same as Reviewer 3.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 3.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper tackles a critical issue in the field of neural network representation learning: the biases introduced by current similarity metrics when comparing representations across different model scales. The authors identify two primary sources of these biases: the 'width confounder,' stemming from the increasing dimensionality of representations as models grow, and the 'depth confounder,' arising from the number of layers in the model. To address these biases, they propose a permutation-based calibration framework that transforms any representational similarity metric into a calibrated score with a principled null reference. This framework is designed to provide a more accurate assessment of representational similarity by accounting for these confounding factors. The core methodological approach involves generating random permutations of the sample data and computing the similarity metric on these permuted samples. The calibrated score is then derived from the distribution of these permuted similarity values, effectively establishing a null reference point. This approach is presented as a general and flexible method applicable to various similarity metrics, including spectral, neighborhood, and geometric measures. The authors apply their calibration framework to the Platonic Representation Hypothesis (PRH), a recent conjecture suggesting that as neural networks scale, their representations converge across modalities. Through a series of experiments, they demonstrate that while global spectral metrics appear to lack significant convergence due to the width confounder, local neighborhood metrics, when calibrated, reveal a consistent convergence of representations across different modalities. This finding suggests a refined version of the PRH, which they term the 'Aristotelian Representation Hypothesis,' emphasizing the convergence of local relationships rather than global geometry. The empirical findings highlight the importance of calibrating representational similarity metrics to accurately interpret the behavior of neural networks as they scale. The paper's significance lies in its rigorous approach to addressing biases in similarity metrics, providing a more reliable tool for understanding the evolution of neural network representations. By demonstrating the effectiveness of their framework on the PRH, the authors offer valuable insights into the nature of neural network learning and the convergence of representations across modalities. The paper's contribution is not only in identifying the biases but also in providing a practical and generalizable method to mitigate them, thus advancing the field of neural network representation analysis. The authors' work underscores the need for careful consideration of confounding factors when interpreting representational similarity metrics and offers a compelling alternative to the original PRH, highlighting the importance of focusing on local relationships rather than global geometry.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

The paper's primary strength lies in its identification and rigorous treatment of biases inherent in representational similarity metrics, specifically the 'width' and 'depth' confounders. This is a crucial contribution, as it highlights a potential pitfall in interpreting representational similarity across different model scales. The authors' analysis of these biases is both insightful and well-supported by theoretical arguments and empirical evidence. The proposed permutation-based calibration framework is another significant strength. This framework is not only effective in mitigating the identified biases but also remarkably general, capable of being applied to a wide range of similarity metrics. This flexibility enhances its utility for the broader research community. The authors' decision to apply their framework to the Platonic Representation Hypothesis (PRH) is commendable. This application demonstrates the practical relevance of their work and provides valuable insights into the behavior of neural networks as they scale. The finding that global spectral metrics lack significant convergence, while local neighborhood metrics show consistent convergence, is a novel and important contribution. This result challenges the original PRH and suggests a more nuanced understanding of neural network representation learning. The paper is also well-written and easy to follow. The authors clearly explain the problem, the proposed solution, and the implications of their findings. The use of clear examples and well-structured arguments makes the paper accessible to a wide audience. The theoretical analysis of the biases introduced by width and depth confounders is crucial for understanding the limitations of existing representational similarity metrics. The authors provide a thorough explanation of how these biases arise and why they pose a challenge to the interpretation of representational similarity. The permutation-based calibration framework is a simple yet effective solution to these biases. The authors demonstrate its applicability across various metrics, including spectral, neighborhood, and geometric measures, highlighting its versatility. The application of the calibration framework to the Platonic Representation Hypothesis is a valuable contribution. By applying their method to this recent hypothesis, the authors provide empirical evidence that challenges the original formulation and suggests a refined version, the Aristotelian Representation Hypothesis. This not only demonstrates the practical utility of their framework but also advances our understanding of neural network representation learning.


## Weaknesses:

Despite its strengths, the paper suffers from several notable weaknesses that limit its overall impact and generalizability. One significant concern is the limited scope of the evaluation. The authors primarily focus on the WIT dataset, which consists of image-text pairs. This narrow focus raises concerns about the generalizability of their findings to other modalities, such as audio, time-series data, or other forms of structured data. The use of only three language model families and five vision model families, without a clear justification for their representativeness, further weakens the claim that the observed effects are universal and not specific to the chosen models and dataset. This narrow evaluation scope weakens the claim that the observed effects are universal and not specific to the chosen models and dataset. The paper's focus is primarily on the calibration of representational similarity metrics. While this is a valuable contribution, it does not delve deeply into the specific challenges and nuances of applying these metrics to different types of neural network architectures. For instance, the calibration framework might need adjustments for architectures with skip connections or attention mechanisms, which are not discussed in detail. The absence of such discussion limits the practical applicability of the framework, as it is unclear how it would perform with these common architectural features. The permutation-based calibration framework, while effective, may not be computationally efficient for very large-scale models or datasets. The computational cost of generating K permutations, especially for high-dimensional representations, could become prohibitive. The paper does not provide a detailed analysis of this complexity or discuss strategies for mitigating this issue, such as using approximate permutation sampling techniques or parallelization. Furthermore, the trade-off between computational cost and calibration accuracy is not explored, raising concerns about the practical applicability of the framework in scenarios with limited computational resources. The paper does not sufficiently explore the sensitivity of the calibration framework to different permutation strategies or sample sizes. The choice of permutation method can significantly impact the calibration results, and the paper does not provide a detailed analysis of how different permutation schemes affect the calibrated scores. Similarly, the impact of varying sample sizes on the stability and reliability of the calibration is not thoroughly investigated. This lack of sensitivity analysis raises concerns about the robustness of the calibration framework and its applicability in scenarios with limited data. The paper's discussion of related work is also limited. While the authors cite relevant works, they do not adequately position their permutation-based calibration method within the broader landscape of representation alignment techniques. For instance, methods that use optimal transport or other distance metrics for alignment are not discussed or compared against. This omission makes it challenging to evaluate the novelty and effectiveness of the proposed approach relative to established techniques. The paper also lacks a thorough discussion of the limitations of the permutation-based calibration framework. While the authors mention that the framework might be computationally expensive for very large models or datasets, they do not provide a detailed analysis of these limitations or discuss potential strategies for mitigating them. The paper also does not explore the specific considerations or challenges that arise when applying the framework to different types of data or models. Finally, the paper lacks practical implementation details. The authors do not specify the software libraries and tools used, nor do they discuss the computational resources required for different experiments. This lack of information makes it difficult for other researchers to reproduce their results and apply the framework to their own work. The absence of an implementation package further hinders the adoption of the proposed method by the research community. These weaknesses, particularly the limited evaluation scope, the lack of computational analysis, and the absence of practical implementation details, significantly impact the paper's overall contribution and limit its potential for widespread adoption. The confidence level in these identified issues is high, as they are directly supported by the paper's content and the absence of certain analyses or discussions.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should significantly expand the scope of their evaluation. This should include experiments on a more diverse set of datasets, encompassing different modalities such as audio, time-series data, or other forms of structured data. This would provide a more comprehensive assessment of the proposed calibration framework and its applicability across different domains and model types. Furthermore, the selection of models should be expanded to encompass a wider range of architectures, including transformers of varying sizes and convolutional networks. This would provide a more comprehensive assessment of the proposed calibration framework and its applicability across different domains and model types. It would also be beneficial to include models with different training objectives or pre-training datasets to investigate whether the observed effects are consistent across different learning paradigms. Such an expanded evaluation would significantly strengthen the generalizability of the findings and the claims made in the paper. Second, the authors should delve deeper into the computational cost associated with their permutation-based calibration framework. This analysis should include a breakdown of the time and memory requirements for each step of the algorithm, such as the permutation generation and the similarity metric calculation. The authors should also explore and discuss potential approximations or optimizations that could reduce the computational burden without significantly compromising the accuracy of the calibration. For instance, instead of generating all possible permutations, they could consider using a subset of permutations or employing more efficient sampling techniques. Furthermore, the paper should include a detailed discussion of the trade-off between computational cost and calibration accuracy. This discussion should provide practical guidance on how to choose the number of permutations based on the available computational resources and the desired level of accuracy. The authors could also consider providing an implementation of the calibration framework to facilitate its adoption by the research community. Third, the authors should conduct a more thorough analysis of the sensitivity of the calibration framework to different permutation strategies and sample sizes. This analysis should include an investigation of how different permutation schemes, such as random permutations versus structured permutations, affect the calibrated scores. The authors should also analyze the impact of varying sample sizes on the stability and reliability of the calibration. This analysis should include a discussion of the trade-offs between computational cost and calibration accuracy when choosing different sample sizes. It would also be beneficial to provide guidelines for selecting appropriate permutation strategies and sample sizes based on the specific characteristics of the dataset and model being used. Fourth, the authors should include a more thorough comparison with existing techniques for calibrating neural network representations. This should include a discussion of methods that use optimal transport, such as Gromov-Wasserstein distance, for aligning representations. The authors should also compare their method with techniques that use contrastive learning or other self-supervised learning approaches for representation calibration. A detailed comparison should not only highlight the differences in methodology but also analyze the strengths and weaknesses of each approach in terms of computational complexity, calibration accuracy, and robustness to different types of data. This would provide a more comprehensive understanding of the proposed method's novelty and its place within the broader landscape of representation calibration techniques. Furthermore, the authors should discuss the limitations of their permutation-based approach, such as its computational cost for very large datasets, and suggest potential solutions. Fifth, the authors should provide more details on the practical implementation of their framework. This includes specifying the software libraries and tools used, as well as the computational resources required for different experiments. They should also discuss any specific considerations or challenges that arise when applying the framework to different types of data or models. This would make it easier for other researchers to reproduce their results and apply the framework to their own work. Furthermore, the authors should consider providing an implementation of the framework to facilitate its adoption by the research community. This package should include clear documentation and examples to help users understand how to use the framework effectively. Finally, the authors should expand on the implications of their calibrated results for understanding the learning dynamics of neural networks. This should include a discussion of how the calibrated similarity metric relates to the training process and the generalization performance of the models. For example, the authors could investigate whether the calibrated results can reveal how representations evolve during training or whether they correlate with the generalization performance of the models. This analysis should also explore whether the calibrated results can provide insights into the mechanisms underlying the observed convergence or divergence of representations. This would strengthen the connection between the calibration framework and the broader understanding of neural network learning.


## Questions:

Given the computational cost associated with generating K permutations, what is the optimal strategy for choosing K to balance computational efficiency and calibration accuracy? How does the choice of K impact the stability and reliability of the calibration, especially in scenarios with limited data? How does the permutation-based calibration framework handle architectures with skip connections or attention mechanisms? Are there specific adjustments or considerations needed to ensure accurate calibration in these cases? What is the computational complexity of the proposed calibration framework, and how does it scale with the size of the models and datasets? Can the authors provide a detailed analysis of the time and memory requirements for each step of the algorithm? How sensitive is the calibration framework to different permutation strategies? Does the choice of permutation method significantly impact the calibrated scores, and if so, what are the best practices for selecting an appropriate permutation strategy? How does the calibrated similarity metric relate to the training process and the generalization performance of the models? Can the calibrated results provide insights into the mechanisms underlying the observed convergence or divergence of representations, and how can this information be used to improve the training of neural networks? What are the limitations of the permutation-based calibration framework, and what are the potential strategies for mitigating these limitations, particularly for very large-scale models or datasets? How does the calibrated similarity metric compare to other alignment or distance metrics, such as those based on optimal transport or kernel methods, in terms of calibration accuracy and computational efficiency? What are the trade-offs between using different alignment metrics, and how do these trade-offs impact the interpretation of neural network representations?


## Rating:

6.25


## Confidence:

3.0


## Decision:

Reject
}