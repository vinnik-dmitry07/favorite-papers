I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper examines the use of Centered Kernel Alignment (CKA) as a metric for comparing activations in artificial and biological neural networks. The authors highlight that standard (biased) CKA can produce misleadingly high similarity scores, especially when comparing neural networks with different feature dimensions. They propose using debiased CKA as a more reliable alternative.

### Soundness

1

### Presentation

1

### Contribution

1

### Strengths

The paper addresses an important issue in the field of comparing artificial and biological neural networks. By highlighting the limitations of biased CKA, the authors provide valuable insights that can improve the reliability of comparisons between these two types of neural networks.

### Weaknesses

#### Some Related Works


#### comment

The paper's presentation and structure could be improved to enhance clarity and readability. For example, the abstract could be more concise and clearly state the main contributions of the paper. Additionally, the introduction could provide a more detailed overview of the problem being addressed and the significance of the proposed solution. The authors should consider adding a section that explicitly discusses the limitations of biased CKA and how debiased CKA addresses these limitations. The current presentation lacks a clear explanation of why debiased CKA is superior to biased CKA in the context of comparing neural networks. The paper would benefit from a more detailed explanation of the mathematical formulation of both biased and debiased CKA, including the specific equations and the rationale behind each step. Furthermore, the experimental section could be strengthened by including a more diverse set of neural network architectures and datasets. The current experiments are limited to a specific set of models and data, which may not generalize to other scenarios. The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA. The paper would also benefit from a more detailed discussion of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks.

### Suggestions

To improve the paper, the authors should begin by significantly streamlining the abstract to clearly articulate the problem, the proposed solution (debiased CKA), and the key findings. The current abstract is too verbose and does not effectively communicate the core contributions. The introduction should be expanded to provide a more thorough background on the challenges of comparing neural networks, particularly the issues arising from different feature dimensions. The authors should also clearly explain why biased CKA is problematic in this context, perhaps by providing a concrete example of how it can lead to misleading conclusions. The introduction should also motivate the need for a more robust metric like debiased CKA, highlighting its advantages over biased CKA. The authors should then provide a detailed mathematical formulation of both biased and debiased CKA, including the specific equations and the rationale behind each step. This section should clearly explain the differences between the two methods and why debiased CKA is more appropriate for comparing neural networks with different feature dimensions. The experimental section should be significantly expanded to include a more diverse set of neural network architectures and datasets. This should include a variety of network architectures, such as convolutional neural networks, recurrent neural networks, and transformers, as well as different types of datasets, such as image, text, and time-series data. This would help to demonstrate the generalizability of the proposed approach. The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA. This should include reporting confidence intervals and p-values to support the claims made in the paper. The paper should also include a more detailed discussion of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks. This should include a comparison of the time and memory requirements of each method, as well as a discussion of any potential optimizations that could be used to reduce the computational cost of debiased CKA. Finally, the authors should consider adding a section that discusses the limitations of their approach and potential avenues for future research. This could include discussing the limitations of the specific datasets and network architectures used in the experiments, as well as potential ways to further improve the robustness and generalizability of the proposed method.

### Questions

Could the authors provide more details on the specific types of neural data used in their experiments? How do these data differ in terms of structure and dimensionality compared to the data used in previous studies? What are the key characteristics of the neural networks used, and how do they vary in terms of architecture and size?

How does the computational cost of debiased CKA compare to biased CKA, especially for large-scale neural networks? Are there any potential optimizations or trade-offs to consider when choosing between the two methods?

### Rating

1

### Confidence

3

**********

## Reviewer 2

### Summary

The authors highlight that biased CKA can produce misleadingly high similarity scores, especially when comparing neural networks with different feature dimensions. They propose using debiased CKA as a more reliable alternative.

### Soundness

1

### Presentation

1

### Contribution

1

### Strengths

The paper addresses an important issue in the field of comparing artificial and biological neural networks. By highlighting the limitations of biased CKA, the authors provide valuable insights that can improve the reliability of comparisons between these two types of neural networks.

### Weaknesses

#### Some Related Works


#### comment

The paper's presentation and structure could be improved to enhance clarity and readability. For example, the abstract could be more concise and clearly state the main contributions of the paper. Additionally, the introduction could provide a more detailed overview of the problem being addressed and the significance of the proposed solution. The authors should consider adding a section that explicitly discusses the limitations of biased CKA and how debiased CKA addresses these limitations. The current presentation lacks a clear explanation of why debiased CKA is superior to biased CKA in the context of comparing neural networks. The paper would benefit from a more detailed explanation of the mathematical formulation of both biased and debiased CKA, including the specific equations and the rationale behind each step. Furthermore, the experimental section could be strengthened by including a more diverse set of neural network architectures and datasets. The current experiments are limited to a specific set of models and data, which may not generalize to other scenarios. The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA. The paper would also benefit from a more detailed discussion of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks.

### Suggestions

To improve the paper, the authors should begin by significantly streamlining the abstract to clearly articulate the problem, the proposed solution (debiased CKA), and the key findings. The current abstract is too verbose and does not effectively communicate the core contributions. The introduction should be expanded to provide a more thorough background on the challenges of comparing neural networks, particularly the issues arising from different feature dimensions. The authors should also clearly explain why biased CKA is problematic in this context, perhaps by providing a concrete example of how it can lead to misleading conclusions. The introduction should also motivate the need for a more robust metric like debiased CKA, highlighting its advantages over biased CKA. The authors should then provide a detailed mathematical formulation of both biased and debiased CKA, including the specific equations and the rationale behind each step. This section should clearly explain the differences between the two methods and why debiased CKA is more appropriate for comparing neural networks with different feature dimensions. The experimental section should be significantly expanded to include a more diverse set of neural network architectures and datasets. This should include a variety of network architectures, such as convolutional neural networks, recurrent neural networks, and transformers, as well as different types of datasets, such as image, text, and time-series data. This would help to demonstrate the generalizability of the proposed approach. The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA. This should include reporting confidence intervals and p-values to support the claims made in the paper. The paper should also include a more detailed discussion of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks. This should include a comparison of the time and memory requirements of each method, as well as a discussion of any potential optimizations that could be used to reduce the computational cost of debiased CKA. Finally, the authors should consider adding a section that discusses the limitations of their approach and potential avenues for future research. This could include discussing the limitations of the specific datasets and network architectures used in the experiments, as well as potential ways to further improve the robustness and generalizability of the proposed method.

### Questions

See above.

### Rating

3

### Confidence

4

**********

## Reviewer 3

### Summary

This paper examines the use of Centered Kernel Alignment (CKA) as a metric for comparing activations in artificial and biological neural networks. The authors highlight that standard (biased) CKA can produce misleadingly high similarity scores, especially when comparing neural networks with different feature dimensions. They propose using debiased CKA as a more reliable alternative.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper addresses an important issue in the field of comparing artificial and biological neural networks. By highlighting the limitations of biased CKA, the authors provide valuable insights that can improve the reliability of comparisons between these two types of neural networks.

### Weaknesses

#### Some Related Works


#### comment

The paper's presentation and structure could be improved to enhance clarity and readability. For example, the abstract could be more concise and clearly state the main contributions of the paper. Additionally, the introduction could provide a more detailed overview of the problem being addressed and the significance of the proposed solution. The authors should consider adding a section that explicitly discusses the limitations of biased CKA and how debiased CKA addresses these limitations. The current presentation lacks a clear explanation of why debiased CKA is superior to biased CKA in the context of comparing neural networks. The paper would benefit from a more detailed explanation of the mathematical formulation of both biased and debiased CKA, including the specific equations and the rationale behind each step. Furthermore, the experimental section could be strengthened by including a more diverse set of neural network architectures and datasets. The current experiments are limited to a specific set of models and data, which may not generalize to other scenarios. The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA. The paper would also benefit from a more detailed discussion of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks.

### Suggestions

To improve the paper, the authors should begin by significantly streamlining the abstract to clearly articulate the problem, the proposed solution (debiased CKA), and the key findings. The current abstract is too verbose and does not effectively communicate the core contributions. The introduction should be expanded to provide a more thorough background on the challenges of comparing neural networks, particularly the issues arising from different feature dimensions. The authors should also clearly explain why biased CKA is problematic in this context, perhaps by providing a concrete example of how it can lead to misleading conclusions. The introduction should also motivate the need for a more robust metric like debiased CKA, highlighting its advantages over biased CKA. The authors should then provide a detailed mathematical formulation of both biased and debiased CKA, including the specific equations and the rationale behind each step. This section should clearly explain the differences between the two methods and why debiased CKA is more appropriate for comparing neural networks with different feature dimensions. The experimental section should be significantly expanded to include a more diverse set of neural network architectures and datasets. This should include a variety of network architectures, such as convolutional neural networks, recurrent neural networks, and transformers, as well as different types of datasets, such as image, text, and time-series data. This would help to demonstrate the generalizability of the proposed approach. The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA. This should include reporting confidence intervals and p-values to support the claims made in the paper. The paper should also include a more detailed discussion of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks. This should include a comparison of the time and memory requirements of each method, as well as a discussion of any potential optimizations that could be used to reduce the computational cost of debiased CKA. Finally, the authors should consider adding a section that discusses the limitations of their approach and potential avenues for future research. This could include discussing the limitations of the specific datasets and network architectures used in the experiments, as well as potential ways to further improve the robustness and generalizability of the proposed method.

### Questions

See above.

### Rating

5

### Confidence

4

**********

## Reviewer 4

### Summary

The paper highlights the limitations of Centered Kernel Alignment (CKA) when comparing activations between artificial and biological neural networks, especially in low-data high-dimension settings. The authors demonstrate that biased CKA can produce artificially inflated similarity scores due to the mismatch in feature-sample ratios, leading to spurious correlations. To address this, they propose using debiased CKA, which corrects for these biases, providing a more reliable measure of similarity. The authors show that while biased CKA can be sensitive to changes in feature dimensions, debiased CKA remains robust, allowing for accurate comparisons across different network architectures and datasets. They also demonstrate that biased CKA is sensitive to shuffled data, indicating that it may be picking up on non-stimulus-driven responses. Overall, the paper provides a valuable contribution to the field by highlighting the importance of using appropriate metrics for comparing neural networks and by proposing a more reliable alternative to biased CKA.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written and clearly explains the problem of biased CKA and the proposed solution of debiased CKA. The authors provide a thorough analysis of the limitations of biased CKA, including its sensitivity to feature-sample ratios and its sensitivity to shuffled data. They also provide a clear explanation of how debiased CKA works and why it is more robust. The paper is well-organized and easy to follow, with clear figures and tables that illustrate the key findings. The authors also provide a detailed discussion of the implications of their findings for the field of neural network comparison, highlighting the importance of using appropriate metrics for comparing neural networks. Overall, the paper makes a significant contribution to the field by providing a more reliable alternative to biased CKA and by demonstrating the importance of using appropriate metrics for comparing neural networks.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed analysis of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks. This could be important for researchers who want to use debiased CKA in their own work. The paper also does not discuss the limitations of debiased CKA, such as its sensitivity to specific types of data or network architectures. It would be useful to explore these limitations and provide guidance on when debiased CKA is most appropriate. The paper also does not provide a comparison of debiased CKA to other similarity metrics, such as RV2 or other correlation-based measures. It would be useful to see how debiased CKA compares to these other metrics in terms of sensitivity to feature-sample ratios and robustness to shuffled data. Finally, the paper could benefit from a more detailed discussion of the practical implications of using debiased CKA in real-world applications, such as in the development of brain-like AI systems.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of debiased CKA, including a comparison to biased CKA for different network sizes and data dimensions. This analysis should include both theoretical estimates and empirical measurements. It would be beneficial to provide guidelines for researchers who want to use debiased CKA in their own work, including recommendations for the size of the networks and datasets they can handle. The authors should also explore the limitations of debiased CKA, such as its sensitivity to specific types of data or network architectures. For example, it would be useful to investigate whether debiased CKA is more sensitive to certain types of noise or artifacts in the data, or whether it is more robust to certain types of network architectures. This analysis should include a discussion of the assumptions underlying debiased CKA and how these assumptions might be violated in practice. Furthermore, the authors should provide a more detailed comparison of debiased CKA to other similarity metrics, such as RV2 and other correlation-based measures. This comparison should include an analysis of the sensitivity of each metric to feature-sample ratios and its robustness to shuffled data. It would be useful to explore the trade-offs between these different metrics and provide guidance on when each metric is most appropriate. Finally, the authors should provide a more detailed discussion of the practical implications of using debiased CKA in real-world applications, such as in the development of brain-like AI systems. This discussion should include examples of how debiased CKA can be used to address specific challenges in these applications, as well as potential limitations and ethical considerations.

### Questions

Could the authors provide more details on the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks? How does the computational cost scale with the size of the networks and the dimensionality of the data?

How sensitive is debiased CKA to specific types of data or network architectures? Are there any limitations to its applicability?

Could the authors provide a more detailed comparison of debiased CKA to other similarity metrics, such as RV2 or other correlation-based measures? How does debiased CKA compare in terms of sensitivity to feature-sample ratios and robustness to shuffled data?

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
1. **State the weakness.**
2. **Collect evidence from the paper.** This will involve looking for specific quotes, descriptions of methods or experiments, and missing information.
3. **Analyze literature gaps.** Check if the paper misses citations for claimed limitations or alternative methods.
4. **Provide a validation analysis.** Summarize the evidence and assess the impact of the weakness.
5. **Conclude on the validity of the weakness.**

Let's start with Reviewer 1.
**Review 1 Weakness Analysis:**

1. Weakness Statement:
"The paper's presentation and structure could be improved to enhance clarity and readability. For example, the abstract could be more concise and clearly state the main contributions of the paper."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: Not applicable.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The abstract is indeed quite long and contains multiple points. While it mentions the problem of biased CKA and the proposed solution of debiased CKA, it doesn't explicitly state the main contributions in a concise manner. For example, the abstract could more clearly highlight the specific scenarios where biased CKA fails and how debiased CKA addresses these issues.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The abstract is lengthy and could be more focused on the core contributions.

1. Weakness Statement:
"Additionally, the introduction could provide a more detailed overview of the problem being addressed and the significance of the proposed solution."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: Not applicable.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The introduction does provide context about the use of CKA in comparing biological and artificial neural networks and mentions the limitations of biased CKA. However, it could be more detailed in explaining the specific challenges posed by the low-data high-dimensionality regime and the significance of addressing these challenges for the field. The introduction could also more explicitly state the proposed solution (debiased CKA) and its potential impact.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: While the introduction touches upon the problem and solution, it could be more detailed in explaining the significance and the specific challenges.

1. Weakness Statement:
"The authors should consider adding a section that explicitly discusses the limitations of biased CKA and how debiased CKA addresses these limitations."

2. Evidence Collection:
a) Method-related Evidence: The paper does discuss the limitations of biased CKA in the "Introduction" and "Covariates" sections, particularly in the context of low-data high-dimensionality. The "Covariates" section explicitly compares biased and debiased CKA and shows the sensitivity of biased CKA to feature-sample ratios.
b) Experiment-related Evidence: The experiments in Section 5 directly demonstrate the limitations of biased CKA by showing its inflated similarity scores in various scenarios.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The paper does address the limitations of biased CKA and how debiased CKA addresses them, particularly in the "Covariates" section. The experiments also provide empirical evidence for this.

5. Conclusion:
Validity status: Invalid
Confidence level: High
Key supporting evidence: The "Covariates" section and the experimental results in Section 5 directly address the limitations of biased CKA.

1. Weakness Statement:
"The current presentation lacks a clear explanation of why debiased CKA is superior to biased CKA in the context of comparing neural networks."

2. Evidence Collection:
a) Method-related Evidence: The "Introduction" and "Covariates" sections explain the theoretical reasons for debiased CKA's superiority. The "Covariates" section provides a mathematical explanation of how biased CKA is sensitive to feature-sample ratios and how debiased CKA corrects for this.
b) Experiment-related Evidence: The experiments in Section 5, particularly Figure 2, demonstrate the superior performance of debiased CKA in detecting true stimulus-driven responses compared to biased CKA.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The paper provides explanations for why debiased CKA is superior, both theoretically and empirically. The "Covariates" section offers a detailed mathematical explanation.

5. Conclusion:
Validity status: Invalid
Confidence level: High
Key supporting evidence: The "Covariates" section provides a mathematical explanation, and the experiments in Section 5 demonstrate the practical superiority of debiased CKA.

1. Weakness Statement:
"The paper would benefit from a more detailed explanation of the mathematical formulation of both biased and debiased CKA, including the specific equations and the rationale behind each step."

2. Evidence Collection:
a) Method-related Evidence: The paper provides the formulas for biased and debiased CKA in the "Covariates" section:
   - Biased CKA:  `RV2 = HSIC(A, B) / (HSIC(A, A) * HSIC(B, B))^0.5`
   - Debiased CKA: `RV2_debiased = HSIC(A, B) / (HSIC(A, A) * HSIC(B, B))^0.5` (with the note that HSIC is the Hilbert-Schmidt Independence Criterion, which is the squared centered kernel alignment)
   The rationale behind debiasing is explained as correcting for the bias introduced by the feature-sample ratio.
b) Experiment-related Evidence: Not applicable.

3. Literature Gap Analysis: The paper cites the original papers for HSIC and CKA.

4. Validation Analysis:
The paper does provide the mathematical formulations for both biased and debiased CKA. While the explanation of the rationale behind debiasing could be more detailed, the core formulas are present.

5. Conclusion:
Validity status: Partially Valid
Confidence level: Medium
Key supporting evidence: The formulas are present, but the explanation of the rationale behind debiasing could be more detailed.

1. Weakness Statement:
"Furthermore, the experimental section could be strengthened by including a more diverse set of neural network architectures and datasets."

2. Evidence Collection:
a) Method-related Evidence: The paper uses ResNet18 and CORnet-S.
b) Experiment-related Evidence: The paper uses the THINGS dataset.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The paper uses two common CNN architectures and one dataset. While this is a reasonable starting point, including more diverse architectures and datasets would indeed strengthen the generalizability of the findings.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The experiments are limited to two specific architectures and one dataset.

1. Weakness Statement:
"The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The paper presents numerical results in tables and figures but does not explicitly discuss statistical significance (e.g., p-values, confidence intervals).

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The paper lacks a discussion of statistical significance. While the trends are clear, the absence of statistical analysis makes it difficult to assess the reliability of the observed differences.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper does not include statistical significance analysis.

1. Weakness Statement:
"The paper would also benefit from a more detailed discussion of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks."

2. Evidence Collection:
a) Method-related Evidence: The paper mentions that debiased CKA is more computationally expensive than biased CKA.
b) Experiment-related Evidence: Not applicable.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
While the paper acknowledges the increased computational cost of debiased CKA, it does not provide a detailed analysis or empirical measurements of this cost, especially for large-scale networks.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks a detailed discussion and empirical analysis of the computational cost.

1. Weakness Statement:
"Finally, the authors should consider adding a section that discusses the limitations of their approach and potential avenues for future research."

2. Evidence Collection:
a) Method-related Evidence: The paper discusses the limitations of biased CKA.
b) Experiment-related Evidence: Not applicable.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The paper focuses on the limitations of biased CKA and the advantages of debiased CKA. While it implicitly suggests future research by highlighting the need for reliable metrics, a dedicated section discussing the limitations of debiased CKA and potential future research directions would be beneficial.

5. Conclusion:
Validity status: Partially Valid
Confidence level: Medium
Key supporting evidence: While the paper addresses limitations, a dedicated section on debiased CKA's limitations and future directions is missing.

**Review 2 Weakness Analysis:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks."

2. Evidence Collection:
a) Method-related Evidence: The paper states that debiased CKA is more computationally expensive.
b) Experiment-related Evidence: Not applicable.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
As noted in the analysis of Reviewer 1, the paper acknowledges the increased cost but lacks a detailed analysis.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks a detailed computational cost analysis.

1. Weakness Statement:
"The paper also does not discuss the limitations of debiased CKA, such as its sensitivity to specific types of data or network architectures."

2. Evidence Collection:
a) Method-related Evidence: The paper shows sensitivity to shuffled data in the "Covariates" section.
b) Experiment-related Evidence: The experiments use specific architectures and datasets.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The paper demonstrates sensitivity to shuffled data, which can be seen as a limitation. However, it doesn't explicitly discuss other potential limitations related to specific data types or architectures beyond what's shown in the experiments.

5. Conclusion:
Validity status: Partially Valid
Confidence level: Medium
Key supporting evidence: Sensitivity to shuffled data is shown, but a broader discussion of limitations is missing.

1. Weakness Statement:
"It would be useful to explore these limitations and provide guidance on when debiased CKA is most appropriate."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The experiments show debiased CKA's effectiveness in the intended scenarios.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The paper demonstrates debiased CKA's effectiveness in the tested scenarios but doesn't provide extensive guidance on when it might be inappropriate or less suitable.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks detailed guidance on the appropriateness of debiased CKA.

1. Weakness Statement:
"The paper also does not provide a comparison of debiased CKA to other similarity metrics, such as RV2 or other correlation-based measures."

2. Evidence Collection:
a) Method-related Evidence: The paper focuses on comparing biased and debiased CKA.
b) Experiment-related Evidence: The experiments only compare biased and debiased CKA.

3. Literature Gap Analysis: The paper cites the RV2 paper.

4. Validation Analysis:
The paper's focus is on CKA. While it cites the RV2 paper, it doesn't empirically compare debiased CKA to RV2 or other correlation-based measures.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks a comparison to other similarity metrics.

1. Weakness Statement:
"Finally, the paper could benefit from a more detailed discussion of the practical implications of using debiased CKA in real-world applications, such as in the development of brain-like AI systems."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The experiments are on a specific dataset.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
The paper focuses on the technical aspects of debiased CKA. It doesn't delve deeply into the practical implications in real-world applications like brain-like AI.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks a detailed discussion of practical implications.

**Review 3 Weakness Analysis:**

1. Weakness Statement:
"The paper's presentation and structure could be improved to enhance clarity and readability. For example, the abstract could be more concise and clearly state the main contributions of the paper."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: Not applicable.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
This is the same point raised by Reviewer 1 and is valid.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The abstract is lengthy and could be more focused on the core contributions.

1. Weakness Statement:
"Additionally, the introduction could provide a more detailed overview of the problem being addressed and the significance of the proposed solution."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: Not applicable.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
This is the same point raised by Reviewer 1 and is valid.

5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The introduction could be more detailed in explaining the significance and the specific challenges.

1. Weakness Statement:
"The authors should consider adding a section that explicitly discusses the limitations of biased CKA and how debiased CKA addresses these limitations."

2. Evidence Collection:
a) Method-related Evidence: This point was addressed in the analysis of Reviewer 1. The paper does discuss this in the "Covariates" section.

5. Conclusion:
Validity status: Invalid
Confidence level: High
Key supporting evidence: The "Covariates" section and the experimental results in Section 5 directly address the limitations of biased CKA.

1. Weakness Statement:
"The current presentation lacks a clear explanation of why debiased CKA is superior to biased CKA in the context of comparing neural networks."

2. Evidence Collection:
a) Method-related Evidence: This point was addressed in the analysis of Reviewer 1. The "Covariates" section provides a mathematical explanation.
5. Conclusion:
Validity status: Invalid
Confidence level: High
Key supporting evidence: The "Covariates" section provides a mathematical explanation, and the experiments in Section 5 demonstrate the practical superiority of debiased CKA.

1. Weakness Statement:
"The paper would benefit from a more detailed explanation of the mathematical formulation of both biased and debiased CKA, including the specific equations and the rationale behind each step."

2. Evidence Collection:
a) Method-related Evidence: This point was addressed in the analysis of Reviewer 1. The formulas are present, but the explanation of the rationale behind debiasing could be more detailed.
5. Conclusion:
Validity status: Partially Valid
Confidence level: Medium
Key supporting evidence: The formulas are present, but the explanation of the rationale behind debiasing could be more detailed.

1. Weakness Statement:
"Furthermore, the experimental section could be strengthened by including a more diverse set of neural network architectures and datasets."

2. Evidence Collection:
a) Method-related Evidence: The paper uses ResNet18 and CORnet-S.
b) Experiment-related Evidence: The paper uses the THINGS dataset.
5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The experiments are limited to two specific architectures and one dataset.

1. Weakness Statement:
"The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The paper presents numerical results but lacks statistical significance analysis.
5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper does not include statistical significance analysis.

1. Weakness Statement:
"The paper would also benefit from a more detailed discussion of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks."

2. Evidence Collection:
a) Method-related Evidence: The paper acknowledges the increased cost.
b) Experiment-related Evidence: Not applicable.
5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks a detailed computational cost analysis.

1. Weakness Statement:
"Finally, the authors should consider adding a section that discusses the limitations of their approach and potential avenues for future research."

2. Evidence Collection:
a) Method-related Evidence: The paper discusses the limitations of biased CKA.
b) Experiment-related Evidence: Not applicable.
5. Conclusion:
Validity status: Partially Valid
Confidence level: Medium
Key supporting evidence: While the paper addresses limitations, a dedicated section on debiased CKA's limitations and future directions is missing.

**Review 4 Weakness Analysis:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks."

2. Evidence Collection:
a) Method-related Evidence: The paper states that debiased CKA is more computationally expensive.
b) Experiment-related Evidence: Not applicable.
5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks a detailed computational cost analysis.

1. Weakness Statement:
"The paper also does not discuss the limitations of debiased CKA, such as its sensitivity to specific types of data or network architectures."

2. Evidence Collection:
a) Method-related Evidence: The paper shows sensitivity to shuffled data.
b) Experiment-related Evidence: The experiments use specific architectures and datasets.
5. Conclusion:
Validity status: Partially Valid
Confidence level: Medium
Key supporting evidence: Sensitivity to shuffled data is shown, but a broader discussion of limitations is missing.

1. Weakness Statement:
"It would be useful to explore these limitations and provide guidance on when debiased CKA is most appropriate."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The experiments show debiased CKA's effectiveness in the tested scenarios.
5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks detailed guidance on the appropriateness of debiased CKA.

1. Weakness Statement:
"The paper also does not provide a comparison of debiased CKA to other similarity metrics, such as RV2 or other correlation-based measures."

2. Evidence Collection:
a) Method-related Evidence: The paper focuses on comparing biased and debiased CKA.
b) Experiment-related Evidence: The experiments only compare biased and debiased CKA.
5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks a comparison to other similarity metrics.

1. Weakness Statement:
"Finally, the paper could benefit from a more detailed discussion of the practical implications of using debiased CKA in real-world applications, such as in the development of brain-like AI systems."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The experiments are on a specific dataset.
5. Conclusion:
Validity status: Valid
Confidence level: High
Key supporting evidence: The paper lacks a detailed discussion of practical implications.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper tackles a critical issue in the field of comparing neural networks: the limitations of using biased Centered Kernel Alignment (CKA) for comparing activations, particularly when dealing with datasets that have a low number of samples but a high number of features. The authors convincingly demonstrate that biased CKA can produce misleadingly high similarity scores even when comparing unrelated networks or data splits, a problem that arises from the mismatch between the feature and sample dimensions. To address this, they propose using debiased CKA, which corrects for these biases, providing a more reliable measure of similarity. The core argument is that while biased CKA can be sensitive to subtle changes in feature dimensions, this sensitivity makes it unsuitable for comparing networks with different architectures or datasets. The authors support their claims with a series of experiments using the THINGS dataset, comparing the performance of biased and debiased CKA with different neural network architectures, including ResNet18 and CORnet-S. They show that biased CKA is highly sensitive to changes in feature dimensions and can be easily inflated by shuffling data, while debiased CKA provides a more robust and reliable measure of similarity. The paper's findings are significant because they highlight a critical flaw in a widely used metric and provide a more reliable alternative for comparing neural networks, which is essential for advancing our understanding of both artificial and biological neural systems. The authors also show that debiased CKA is able to detect true stimulus-driven responses in the THINGS dataset, while biased CKA fails to do so. This further underscores the importance of using debiased CKA for comparing neural networks with different feature dimensions. Overall, the paper makes a valuable contribution by identifying a key limitation of biased CKA and proposing a more reliable alternative, which is crucial for the field of neural network comparison.


## Soundness:

1.75


## Presentation:

1.75


## Contribution:

1.75


## Strengths:

I found several strengths in this paper that contribute to its overall impact and significance. First and foremost, the paper directly addresses a crucial problem in the field of comparing neural networks. The authors identify a significant flaw in the widely used biased CKA metric, demonstrating its limitations when applied to low-data high-dimensionality datasets, a common scenario in many neural network applications. This is a valuable contribution because it highlights a potential pitfall that could lead to misinterpretations of neural network behavior. The paper's core argument is well-supported by the experimental results. The authors clearly show that biased CKA is sensitive to changes in feature dimensions and can be easily inflated by shuffling data, which is a critical flaw for a metric intended to compare neural networks. The use of debiased CKA as a solution is also a strength, as it provides a more reliable measure of similarity, as demonstrated in the experiments. The paper's focus on the low-data high-dimensionality regime is particularly relevant, as this is a common scenario in many neural network applications. The authors also provide a clear explanation of the mathematical formulation of both biased and debiased CKA, which is essential for understanding the underlying mechanisms of the proposed solution. The experimental results are compelling, showing that debiased CKA is able to detect true stimulus-driven responses in the THINGS dataset, while biased CKA fails to do so. This further underscores the importance of using debiased CKA for comparing neural networks with different feature dimensions. The paper is also well-written and clearly explains the problem, the proposed solution, and the experimental results. The authors provide a thorough analysis of the limitations of biased CKA and the advantages of debiased CKA, which makes the paper easy to follow and understand. The paper also provides a clear explanation of how debiased CKA works and why it is more appropriate for comparing neural networks with different feature dimensions. The authors also provide a clear explanation of how debiased CKA works and why it is more appropriate for comparing neural networks with different feature dimensions. The paper also provides a clear explanation of how debiased CKA works and why it is more appropriate for comparing neural networks with different feature dimensions.


## Weaknesses:

While the paper presents a compelling argument for the use of debiased CKA, I have identified several weaknesses that warrant further discussion. First, the paper's presentation, while generally clear, could benefit from more concise language and a more focused introduction. The abstract, in particular, is quite lengthy and could be more succinctly written to clearly state the main contributions of the paper. While the abstract does mention the problem of biased CKA and the proposed solution of debiased CKA, it doesn't explicitly state the main contributions in a concise manner. The introduction, while providing context, could also be more detailed in explaining the specific challenges posed by the low-data high-dimensionality regime and the significance of addressing these challenges for the field. While the introduction touches upon the problem and solution, it could be more detailed in explaining the significance and the specific challenges. Second, while the paper does discuss the limitations of biased CKA and how debiased CKA addresses these limitations, particularly in the 'Covariates' section, a dedicated section explicitly discussing the limitations of debiased CKA and potential avenues for future research is missing. While the paper implicitly suggests future research by highlighting the need for reliable metrics, a dedicated section discussing the limitations of debiased CKA and potential future research directions would be beneficial. The paper also lacks a detailed explanation of the computational cost of debiased CKA compared to biased CKA, especially for large-scale neural networks. While the paper acknowledges that debiased CKA is more computationally expensive, it does not provide a detailed analysis or empirical measurements of this cost, which is crucial for researchers who want to use debiased CKA in their own work. The paper also does not discuss the limitations of debiased CKA, such as its sensitivity to specific types of data or network architectures beyond what's shown in the experiments. While the paper demonstrates sensitivity to shuffled data, which can be seen as a limitation, it doesn't explicitly discuss other potential limitations related to specific data types or architectures beyond what's shown in the experiments. The paper also does not provide a comparison of debiased CKA to other similarity metrics, such as RV2 or other correlation-based measures. The paper's focus is on CKA, and while it cites the RV2 paper, it doesn't empirically compare debiased CKA to RV2 or other correlation-based measures. Finally, the paper could benefit from a more detailed discussion of the practical implications of using debiased CKA in real-world applications, such as in the development of brain-like AI systems. The paper focuses on the technical aspects of debiased CKA. It doesn't delve deeply into the practical implications in real-world applications like brain-like AI. The experimental section, while demonstrating the effectiveness of debiased CKA, could be strengthened by including a more diverse set of neural network architectures and datasets. The current experiments are limited to a specific set of models and data, which may not generalize to other scenarios. The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA. The paper presents numerical results but does not explicitly discuss statistical significance (e.g., p-values, confidence intervals). The paper also lacks a detailed discussion of the practical implications of using debiased CKA in real-world applications, such as in the development of brain-like AI systems. The paper focuses on the technical aspects of debiased CKA. It doesn't delve deeply into the practical implications in real-world applications like brain-like AI.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should revise the abstract to be more concise and clearly state the main contributions of the paper. The abstract should explicitly highlight the specific scenarios where biased CKA fails and how debiased CKA addresses these issues. The introduction should be expanded to provide a more thorough background on the challenges of comparing neural networks, particularly the issues arising from different feature dimensions. The authors should also clearly explain why biased CKA is problematic in this context, perhaps by providing a concrete example of how it can lead to misleading conclusions. The introduction should also motivate the need for a more robust metric like debiased CKA, highlighting its advantages over biased CKA. Second, the authors should add a dedicated section that explicitly discusses the limitations of debiased CKA and potential avenues for future research. This section could include a discussion of the assumptions underlying debiased CKA and how these assumptions might be violated in practice. For example, it would be useful to investigate whether debiased CKA is more sensitive to certain types of noise or artifacts in the data, or whether it is more robust to certain types of network architectures. This analysis should include a discussion of the assumptions underlying debiased CKA and how these assumptions might be violated in practice. Furthermore, the authors should provide guidance on when debiased CKA is most appropriate. Third, the authors should provide a more detailed analysis of the computational cost of debiased CKA, including a comparison to biased CKA for different network sizes and data dimensions. This analysis should include both theoretical estimates and empirical measurements. It would be beneficial to provide guidelines for researchers who want to use debiased CKA in their own work, including recommendations for the size of the networks and datasets they can handle. The authors should also explore the limitations of debiased CKA, such as its sensitivity to specific types of data or network architectures. For example, it would be useful to investigate whether debiased CKA is more sensitive to certain types of noise or artifacts in the data, or whether it is more robust to certain types of network architectures. This analysis should include a discussion of the assumptions underlying debiased CKA and how these assumptions might be violated in practice. Furthermore, the authors should provide guidance on when debiased CKA is most appropriate. Fourth, the authors should provide a more detailed comparison of debiased CKA to other similarity metrics, such as RV2 and other correlation-based measures. This comparison should include an analysis of the sensitivity of each metric to feature-sample ratios and its robustness to shuffled data. It would be useful to explore the trade-offs between these different metrics and provide guidance on when each metric is most appropriate. Fifth, the authors should provide a more detailed discussion of the practical implications of using debiased CKA in real-world applications, such as in the development of brain-like AI systems. This discussion should include examples of how debiased CKA can be used to address specific challenges in these applications, as well as potential limitations and ethical considerations. Finally, the authors should strengthen the experimental section by including a more diverse set of neural network architectures and datasets. This should include a variety of network architectures, such as convolutional neural networks, recurrent neural networks, and transformers, as well as different types of datasets, such as image, text, and time-series data. This would help to demonstrate the generalizability of the proposed approach. The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the observed differences between biased and debiased CKA. This should include reporting confidence intervals and p-values to support the claims made in the paper. The paper should also include a more detailed discussion of the computational cost of debiased CKA, including a comparison to biased CKA for different network sizes and data dimensions. This analysis should include both theoretical estimates and empirical measurements. It would be beneficial to provide guidelines for researchers who want to use debiased CKA in their own work, including recommendations for the size of the networks and datasets they can handle.


## Questions:

I have several questions that arise from my analysis of the paper. First, could the authors provide more details on the specific types of neural data used in their experiments? How do these data differ in terms of structure and dimensionality compared to the data used in previous studies? What are the key characteristics of the neural networks used, and how do they vary in terms of architecture and size? Second, how does the computational cost of debiased CKA compare to biased CKA, especially for large-scale neural networks? Are there any potential optimizations or trade-offs to consider when choosing between the two methods? Third, how sensitive is debiased CKA to specific types of data or network architectures? Are there any limitations to its applicability? Fourth, could the authors provide a more detailed comparison of debiased CKA to other similarity metrics, such as RV2 or other correlation-based measures? How does debiased CKA compare in terms of sensitivity to feature-sample ratios and robustness to shuffled data? Fifth, what are the practical implications of using debiased CKA in real-world applications, such as in the development of brain-like AI systems? Are there any specific scenarios where debiased CKA is most appropriate? Finally, could the authors provide more details on the statistical significance of the observed differences between biased and debiased CKA? What are the confidence intervals and p-values for the results presented in the paper?


## Rating:

4.25


## Confidence:

3.5


## Decision:

Reject
}