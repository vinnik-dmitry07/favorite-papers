I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes On-Policy Representation Distillation (OPRD), a novel approach to distilling large language models (LLMs) that addresses the limitations of existing on-policy distillation methods. The authors identify two primary issues with current on-policy distillation: the high variance of the gradient estimators and the loss of structural information by focusing solely on output-space projections. To overcome these challenges, OPPD introduces a method that leverages hidden-state supervision across selected layers and positions, providing a deterministic and low-variance gradient with respect to the student model's parameters. This approach exposes the structural information that the language model's hidden states contain, which is often lost in output-space distillation. The authors demonstrate that OPPD can achieve state-of-the-art performance on competition-level mathematical reasoning benchmarks, where it narrows the student-teacher gap on tasks like AIME 2024, AIME 2025, and AIMO, while simultaneously training 1.44x faster and using 54% less memory.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors clearly identify the limitations of existing on-policy distillation methods and provide a strong rationale for their proposed approach. The paper is well-structured, with clear explanations of the problems with current methods and the benefits of OPPD.
2. The empirical results are compelling, demonstrating that OPPD achieves state-of-the-art performance on challenging mathematical reasoning benchmarks. The authors also show that OPPD is more efficient in terms of training time and memory usage, which is a significant practical advantage.
3. The paper introduces the OPRD-Bridge method, which extends OPPD to cross-architecture settings, allowing for representation distillation across arbitrary architectures. This is a novel contribution that addresses a critical limitation of existing distillation methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of OPPD, such as potential challenges in applying it to different types of tasks or models. Specifically, the paper lacks a discussion on how the performance of OPPD might be affected by the choice of layers for hidden state supervision. It would be beneficial to understand if certain layers are more critical than others, and if there is an optimal strategy for selecting these layers. Furthermore, the paper does not explore the sensitivity of OPPD to the choice of hidden state dimensions, which could impact the amount of information retained during distillation.
2. The paper could provide more details on the computational cost of OPPD, especially in comparison to existing methods. While the authors mention that OPPD is more efficient in terms of training time and memory usage, a more detailed analysis of the computational complexity of the proposed method would be beneficial. This should include a breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself. A comparison with the computational cost of other on-policy distillation methods would also be valuable.

### Suggestions

The authors should consider expanding on the discussion of the limitations of OPPD by exploring the impact of layer selection on the performance of the method. Specifically, they could investigate whether certain layers are more critical for knowledge transfer than others, and if there is an optimal strategy for selecting these layers. This could involve conducting experiments where different sets of layers are used for hidden state supervision, and analyzing the resulting performance. Furthermore, the authors should explore the sensitivity of OPPD to the choice of hidden state dimensions. This could involve varying the dimensionality of the hidden states used for distillation and analyzing the impact on performance. Such an analysis would provide a more comprehensive understanding of the method's robustness and limitations.

To provide a more complete picture of the computational cost of OPPD, the authors should include a detailed analysis of the computational complexity of the proposed method. This analysis should include a breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself. A comparison with the computational cost of other on-policy distillation methods would also be valuable. This analysis should also consider the impact of different factors, such as the size of the models and the length of the input sequences, on the computational cost of OPPD. This would allow readers to better understand the practical implications of using OPPD in different scenarios.

Finally, the authors should consider including a more detailed discussion of the potential challenges in applying OPPD to different types of tasks and models. This discussion should include an analysis of the types of tasks and models for which OPPD is most suitable, as well as the potential limitations of the method in other scenarios. For example, the authors could discuss whether OPPD is equally effective for tasks that require different types of reasoning or for models with different architectural designs. This would provide a more balanced and comprehensive view of the applicability of OPPD.

### Questions

1. How does the choice of layers for hidden state supervision affect the performance of OPPD? Are there any guidelines for selecting the optimal layers for a given task or model?
2. How does the computational cost of OPPD compare to existing on-policy distillation methods? Can the authors provide a more detailed analysis of the computational complexity of the proposed method?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper introduces On-Policy Representation Distillation (OPRD), a novel approach to distillation that lifts on-policy distillation from the output space into the hidden state space. This method addresses two key limitations of existing on-policy distillation: the high-variance gradient estimators and the loss of structural information by only using the output-space. The authors propose a low-rank projection bridge to align the hidden states between different model architectures, enabling representation distillation across architectures. The effectiveness of OPRD is demonstrated through experiments on mathematical reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper identifies the limitations of existing on-policy distillation methods and proposes a novel approach to address these limitations.
2. The authors provide a thorough theoretical analysis of OPRD, including proofs of zero-variance gradients and the loss of information in output-space distillation.
3. The paper introduces OPRD-Bridge, which extends OPRD to cross-architecture distillation by using a low-rank projection bridge to align hidden states between different architectures.
4. The authors conduct extensive experiments on mathematical reasoning benchmarks, demonstrating the effectiveness of OPRD in narrowing the student-teacher gap and achieving state-of-the-art results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of OPRD compared to existing on-policy distillation methods. While the authors claim that OPRD is more efficient, they do not provide specific metrics such as training time, memory usage, or the number of parameters. A more thorough analysis of the computational cost would be beneficial to understand the practical implications of using OPRD.
2. The paper does not provide a detailed analysis of the sensitivity of OPRD to different hyperparameters, such as the rank of the projection bridge and the number of layers used for distillation. A sensitivity analysis would help to understand the robustness of OPRD and provide guidance on how to choose the optimal hyperparameters for different tasks and architectures.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational overhead introduced by OPRD. While the authors claim efficiency gains, a detailed breakdown of the computational cost is necessary to fully assess the practical implications. Specifically, the authors should provide a comparison of training time, memory consumption, and the number of parameters for OPRD versus existing on-policy distillation methods. This analysis should be conducted across different model sizes and datasets to understand how the computational cost scales with model complexity. Furthermore, it would be helpful to include a discussion of the trade-offs between computational cost and performance, allowing readers to make informed decisions about when to use OPRD. For example, providing a table showing the training time in hours, GPU memory usage in GB, and the number of trainable parameters for each method on different datasets would be very informative.

In addition to the computational cost, a more thorough sensitivity analysis of the hyperparameters is needed. The authors should investigate the impact of the rank of the projection bridge on the performance of OPRD. A lower rank might lead to faster training but could also result in a loss of information, while a higher rank might improve performance but increase computational cost. The authors should provide empirical evidence to support their choice of rank and discuss the trade-offs involved. Similarly, the number of layers used for distillation should be analyzed. The authors should investigate how the performance of OPRD changes when using different numbers of layers and provide guidelines for selecting the optimal number of layers for different tasks and architectures. This analysis should include a discussion of the potential impact of the number of layers on the convergence rate and the final performance of the distilled model. For example, a plot showing the performance of OPRD as a function of the number of layers would be very useful.

Finally, the authors should provide a more detailed discussion of the limitations of OPRD. While the paper demonstrates the effectiveness of OPRD on mathematical reasoning benchmarks, it is important to acknowledge the potential limitations of the method. For example, the authors should discuss the potential challenges of applying OPRD to other types of tasks, such as natural language processing or computer vision. They should also discuss the potential impact of the choice of teacher and student models on the performance of OPRD. A more thorough discussion of the limitations would help to provide a more balanced and realistic assessment of the method.

### Questions

1. How does the computational cost of OPRD compare to existing on-policy distillation methods? Can the authors provide a more detailed analysis of the training time, memory usage, and the number of parameters for OPRD versus existing methods?
2. What is the sensitivity of OPRD to different hyperparameters, such as the rank of the projection bridge and the number of layers used for distillation? Can the authors provide empirical evidence to support their choice of hyperparameters and discuss the trade-offs involved?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces On-Policy Representation Distillation (OPRD), a novel distillation method that lifts on-policy distillation from the output space into the hidden state space. The authors identify two key limitations of existing on-policy distillation methods: (1) high-variance gradient estimators, and (2) the loss of structural information by only using the output-space. To overcome these limitations, OPRD aligns student and teacher representations across selected layers and positions via a low-rank projection bridge. The paper provides theoretical analysis showing that OPRD has a deterministic per-sample gradient and exposes structural information that is otherwise lost. Empirical results demonstrate that OPRD narrows the student-teacher gap on competition-level mathematical reasoning benchmarks while training 1.44× faster and using 54% less memory.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to on-policy distillation by lifting it to the hidden state space, addressing the limitations of existing methods in terms of gradient variance and information loss.
2. The authors provide a thorough theoretical analysis of OPRD, demonstrating its deterministic per-sample gradient and the exposure of structural information through the low-rank projection bridge.
3. The empirical results show that OPRD achieves state-of-the-art performance on competition-level mathematical reasoning benchmarks, narrowing the student-teacher gap while significantly reducing training time and memory usage.
4. The paper introduces OPRD-Bridge, a method to extend OPRD to cross-architecture distillation by aligning representations across different architectures using a low-rank projection bridge.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of OPRD, such as potential challenges in applying it to different types of tasks or models. Specifically, the paper lacks a discussion on how the performance of OPRD might be affected by the choice of layers for hidden state supervision. It would be beneficial to understand if certain layers are more critical than others, and if there is an optimal strategy for selecting these layers. Furthermore, the paper does not explore the sensitivity of OPRD to the choice of hidden state dimensions, which could impact the amount of information retained during distillation.
2. The paper could provide more details on the computational cost of OPRD, especially in comparison to existing methods. While the authors mention that OPRD is more efficient in terms of training time and memory usage, a more detailed analysis of the computational complexity of the proposed method would be beneficial. This should include a breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself. A comparison with the computational cost of other on-policy distillation methods would also be valuable.

### Suggestions

The authors should provide a more in-depth analysis of the impact of layer selection on the performance of OPRD. Specifically, they should investigate whether certain layers are more critical for knowledge transfer than others, and if there is an optimal strategy for selecting these layers. This could involve conducting experiments where different sets of layers are used for hidden state supervision, and analyzing the resulting performance. Furthermore, the authors should explore the sensitivity of OPRD to the choice of hidden state dimensions. This could involve varying the dimensionality of the hidden states used for distillation and analyzing the impact on performance. Such an analysis would provide a more comprehensive understanding of the method's robustness and limitations.

To provide a more complete picture of the computational cost of OPRD, the authors should include a detailed breakdown of the computational complexity of the proposed method. This should include a breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself. A comparison with the computational cost of other on-policy distillation methods would also be valuable. This analysis should consider the impact of different factors, such as the size of the models and the length of the input sequences, on the computational cost of OPRD. This would allow readers to better understand the practical implications of using OPRD in different scenarios.

Finally, the authors should discuss the potential challenges of applying OPRD to different types of tasks and models. This discussion should include an analysis of the types of tasks and models for which OPRD is most suitable, as well as the potential limitations of the method in other scenarios. For example, the authors could discuss whether OPRD is equally effective for tasks that require different types of reasoning or for models with different architectural designs. This would provide a more balanced and comprehensive view of the applicability of OPRD.

### Questions

1. How does the choice of layers for hidden state supervision affect the performance of OPRD? Are there any guidelines for selecting the optimal layers for a given task or model?
2. How does the computational cost of OPRD compare to existing on-policy distillation methods? Can the authors provide a more detailed analysis of the computational complexity of the proposed method?

### Rating

8

### Confidence

4

**********

## Reviewer 4

### Summary

This paper proposes a new distillation objective called On-Policy Representation Distillation (OPRD), which leverages the hidden states of the student and teacher models to distill knowledge. The authors identify two limitations of existing on-policy distillation methods: the high variance of the gradient estimator and the loss of structural information by only using the output space. To address these limitations, they propose a new distillation objective that aligns the student's hidden states with the teacher's across selected layers and positions. They also introduce OPRD-Bridge, a method to extend OPRD to cross-architecture distillation by using a low-rank projection bridge to align representations across different architectures. The authors demonstrate that OPRD achieves state-of-the-art performance on competition-level mathematical reasoning benchmarks while training 1.44× faster and using 54% less memory.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a detailed explanation of their proposed method.
2. The authors provide a thorough theoretical analysis of the proposed method, including proofs of the zero-variance gradient and the loss of structural information in existing on-policy distillation methods.
3. The authors conduct extensive experiments on competition-level mathematical reasoning benchmarks, demonstrating that OPRD achieves state-of-the-art performance while training 1.44× faster and using 54% less memory.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of OPRD compared to existing on-policy distillation methods. While the authors claim that OPRD is more efficient, they do not provide specific metrics such as training time, memory usage, or the number of parameters. A more thorough analysis of the computational cost would be beneficial to understand the practical implications of using OPRD.
2. The paper does not provide a detailed analysis of the sensitivity of OPRD to different hyperparameters, such as the rank of the projection bridge and the number of layers used for distillation. A sensitivity analysis would help to understand the robustness of OPRD and provide guidance on how to choose the optimal hyperparameters for different tasks and architectures.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of OPRD compared to existing on-policy distillation methods. This analysis should include specific metrics such as training time, memory usage, and the number of parameters. For example, the authors could provide a table comparing the training time and memory usage of OPRD with existing methods on different datasets and model sizes. This would allow readers to better understand the practical implications of using OPRD and make informed decisions about when to use it. Furthermore, the authors should discuss the computational overhead introduced by the low-rank projection bridge and how it affects the overall efficiency of the method. It would be beneficial to see a breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself.

In addition to the computational cost, the authors should also provide a more detailed analysis of the sensitivity of OPRD to different hyperparameters. This analysis should include a discussion of how the rank of the projection bridge and the number of layers used for distillation affect the performance of the method. For example, the authors could provide a plot showing the performance of OPRD as a function of the rank of the projection bridge and the number of layers. This would help to understand the robustness of OPRD and provide guidance on how to choose the optimal hyperparameters for different tasks and architectures. The authors should also discuss the impact of these hyperparameters on the convergence rate and the final performance of the distilled model. It would be useful to see a sensitivity analysis of the hyperparameters on different datasets and model sizes.

Finally, the authors should discuss the limitations of OPRD and potential directions for future research. For example, the authors could discuss the potential challenges of applying OPRD to other types of tasks or models. They could also discuss the potential for further improvements to the method, such as the use of adaptive projection bridges or the incorporation of other techniques for improving the efficiency of distillation. A discussion of the limitations and future directions would help to provide a more complete picture of the method and its potential impact.

### Questions

1. How does the computational cost of OPRD compare to existing on-policy distillation methods? Can the authors provide a more detailed analysis of the training time, memory usage, and the number of parameters for OPRD versus existing methods?
2. What is the sensitivity of OPRD to different hyperparameters, such as the rank of the projection bridge and the number of layers used for distillation? Can the authors provide empirical evidence to support their choice of hyperparameters and discuss the trade-offs involved?

### Rating

8

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper provided.

Here's my plan:
1. **Iterate through each reviewer's comments.**
2. **For each weakness identified by the reviewer:**
    - **Locate the specific claim in the paper.**
    - **Find evidence (quotes, descriptions, data) to support or refute the weakness.**
    - **Consider if the reviewer misunderstood something.**
    - **Formulate a conclusion about the validity of the weakness.**
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper could benefit from a more detailed discussion of the limitations of OPRD, such as potential challenges in applying it to different types of tasks or models. Specifically, the paper lacks a discussion on how the performance of OPRD might be affected by the choice of layers for hidden state supervision. It would be beneficial to understand if certain layers are more critical than others, and if there is an optimal strategy for selecting these layers. Furthermore, the paper does not explore the sensitivity of OPRD to the choice of hidden state dimensions, which could impact the amount of information retained during distillation.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the low-rank projection bridge but doesn't explicitly discuss the criteria for selecting layers for supervision.
   - The method section describes the OPRD objective and the OPRD-Bridge method but lacks a detailed discussion on layer selection or hidden state dimensionality.
b) Experiment-related Evidence:
   - The experiments section focuses on mathematical reasoning tasks and compares OPRD variants but doesn't include experiments varying the layers or hidden state dimensions used for supervision.

3. Literature Gap Analysis:
   - The paper cites works on representation distillation and on-policy distillation but doesn't cite specific literature discussing the impact of layer selection in representation distillation or the sensitivity to hidden state dimensionality in this context.

4. Validation Analysis:
   - The reviewer correctly points out the lack of a detailed discussion on the limitations of OPRD, particularly regarding layer selection and hidden state dimensionality. The paper focuses on the mechanics of OPRD and OPRD-Bridge but doesn't delve into the nuances of these choices and their potential impact on performance and applicability. The experiments also don't explore these aspects.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method and experiment sections lack discussion and experiments on layer selection and hidden state dimensionality.

1. Weakness Statement:
[The paper could provide more details on the computational cost of OPRD, especially in comparison to existing methods. While the authors mention that OPRD is more efficient in terms of training time and memory usage, a more detailed analysis of the computational complexity of the proposed method would be beneficial. This should include a breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself. A comparison with the computational cost of other on-policy distillation methods would also be valuable.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method section describes the OPRD objective and OPRD-Bridge but doesn't provide a formal analysis of the computational complexity.
b) Experiment-related Evidence:
   - The experiment section mentions the efficiency gains ("OPRD reduces wall-clock time by 30% and GPU memory usage by 20% compared to the original on-policy distillation method") but lacks a detailed breakdown of the computational cost of each step or a comparison with other methods.

3. Literature Gap Analysis:
   - While the paper compares performance, it doesn't provide a computational complexity analysis against other methods.

4. Validation Analysis:
   - The reviewer is correct. While the paper claims efficiency, it lacks a detailed computational cost analysis. The provided information is high-level and doesn't break down the complexity of each step in the OPRD and OPRD-Bridge methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method and experiment sections lack a detailed computational cost analysis.

**Review 2 Weaknesses:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of OPRD compared to existing on-policy distillation methods. While the authors claim that OPRD is more efficient, they do not provide specific metrics such as training time, memory usage, or the number of parameters. A more thorough analysis of the computational cost would be beneficial to understand the practical implications of using OPRD.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method section describes the OPRD objective and OPRD-Bridge but doesn't provide a formal analysis of the computational complexity.
b) Experiment-related Evidence:
   - The experiment section mentions the efficiency gains ("OPRD reduces wall-clock time by 30% and GPU memory usage by 20% compared to the original on-policy distillation method") but lacks a detailed breakdown of the computational cost of each step or a comparison with other methods.

3. Literature Gap Analysis:
   - While the paper compares performance, it doesn't provide a computational complexity analysis against other methods.

4. Validation Analysis:
   - This is the same weakness as Reviewer 1's second point. The reviewer is correct. The paper lacks a detailed computational cost analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method and experiment sections lack a detailed computational cost analysis.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the sensitivity of OPRD to different hyperparameters, such as the rank of the projection bridge and the number of layers used for distillation. A sensitivity analysis would help to understand the robustness of OPRD and provide guidance on how to choose the optimal hyperparameters for different tasks and architectures.]

2. Evidence Collection:
a) Method-related Evidence:
   - The OPRD-Bridge method introduces the rank 'r' of the projection bridge as a hyperparameter, but the paper doesn't include an analysis of how different values of 'r' affect performance.
   - The paper mentions selecting a subset of layers for OPRD but doesn't provide a sensitivity analysis of this choice.
b) Experiment-related Evidence:
   - The experiments use specific values for the rank of the projection bridge and the number of layers but don't explore the impact of varying these parameters.

3. Literature Gap Analysis:
   - The paper doesn't cite literature on hyperparameter sensitivity analysis in the context of representation distillation.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a sensitivity analysis for key hyperparameters like the rank of the projection bridge and the number of layers used for distillation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method and experiment sections lack a sensitivity analysis for key hyperparameters.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of OPRD compared to existing on-policy distillation methods. While the authors claim that OPRD is more efficient, they do not provide specific metrics such as training time, memory usage, or the number of parameters. A more thorough analysis of the computational cost would be beneficial to understand the practical implications of using OPRD.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1 and 2's first point. The reviewer is correct. The paper lacks a detailed computational cost analysis.

3. Literature Gap Analysis:
   - The paper doesn't provide a computational complexity analysis against other methods.

4. Validation Analysis:
   - Valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method and experiment sections lack a detailed computational cost analysis.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the sensitivity of OPRD to different hyperparameters, such as the rank of the projection bridge and the number of layers used for distillation. A sensitivity analysis would help to understand the robustness of OPRD and provide guidance on how to choose the optimal hyperparameters for different tasks and architectures.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 2's second point. The reviewer is correct. The paper lacks a sensitivity analysis for key hyperparameters.

3. Literature Gap Analysis:
   - The paper doesn't cite literature on hyperparameter sensitivity analysis in the context of representation distillation.

4. Validation Analysis:
   - Valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method and experiment sections lack a sensitivity analysis for key hyperparameters.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper could benefit from a more detailed discussion of the limitations of OPRD, such as potential challenges in applying it to different types of tasks or models. Specifically, the paper lacks a discussion on how the performance of OPRD might be affected by the choice of layers for hidden state supervision. It would be beneficial to understand if certain layers are more critical than others, and if there is an optimal strategy for selecting these layers. Furthermore, the paper does not explore the sensitivity of OPRD to the choice of hidden state dimensions, which could impact the amount of information retained during distillation.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. The reviewer is correct. The paper lacks a detailed discussion and analysis of the limitations regarding layer selection and hidden state dimensionality.

3. Literature Gap Analysis:
   - The paper doesn't cite literature on the impact of layer selection in representation distillation or sensitivity to hidden state dimensionality in this context.

4. Validation Analysis:
   - Valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method and experiment sections lack a detailed discussion and analysis of these limitations.

1. Weakness Statement:
[The paper could provide more details on the computational cost of OPRD, especially in comparison to existing methods. While the authors mention that OPRD is more efficient in terms of training time and memory usage, a more detailed analysis of the computational complexity of the proposed method would be beneficial. This should include a breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself. A comparison with the computational cost of other on-policy distillation methods would also be valuable.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 2 and 3's first point. The reviewer is correct. The paper lacks a detailed computational cost analysis.

3. Literature Gap Analysis:
   - The paper doesn't provide a computational complexity analysis against other methods.

4. Validation Analysis:
   - Valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method and experiment sections lack a detailed computational cost analysis.

**Synthesis and Reflection:**

All reviewers raise similar concerns regarding the paper's lack of detailed analysis on computational cost and hyperparameter sensitivity. There's a consensus that while the paper claims efficiency and provides some high-level comparisons, it lacks the granular detail needed to fully assess the practical implications and robustness of OPRD. The reviewers correctly point out the absence of a detailed discussion on the limitations, particularly concerning the selection of layers for hidden state supervision and the sensitivity to hidden state dimensions. There are no conflicting opinions among the reviewers regarding the identified weaknesses. The weaknesses are consistently identified across multiple reviews, strengthening their validity.

**Final Conclusion:**

All identified weaknesses are valid. The paper would benefit from a more thorough analysis of the computational cost, including a breakdown of the complexity of each step and a comparison with existing methods. Additionally, a sensitivity analysis of key hyperparameters like the rank of the projection bridge and the number of layers used for distillation is necessary to understand the robustness and practical applicability of OPRD. A more detailed discussion of the limitations, especially regarding layer selection and hidden state dimensionality, would also strengthen the paper.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces On-Policy Representation Distillation (OPRD), a novel approach to distilling knowledge from a teacher model to a student model, specifically targeting the limitations of existing on-policy distillation methods. The authors identify two key issues with current on-policy distillation techniques: the high variance of the gradient estimators and the loss of structural information by focusing solely on the output space. To address these challenges, OPRD leverages hidden-state supervision across selected layers and positions, providing a deterministic and low-variance gradient with respect to the student model's parameters. This is achieved by aligning the student's hidden states with the teacher's across selected layers and positions, effectively exposing the structural information that is lost in output-space distillation. The authors also introduce OPRD-Bridge, a method to extend OPRD to cross-architecture distillation by using a low-rank projection bridge to align representations across different architectures. The core idea is to use a shared, low-dimensional representation space to bridge the gap between models with different architectures. The paper presents a thorough theoretical analysis of OPRD, demonstrating its deterministic per-sample gradient and the exposure of structural information through the low-rank projection bridge. Empirically, the authors demonstrate that OPRD achieves state-of-the-art performance on competition-level mathematical reasoning benchmarks, narrowing the student-teacher gap while significantly reducing training time and memory usage. Specifically, they show that OPRD reduces wall-clock time by 30% and GPU memory usage by 20% compared to the original on-policy distillation method. The authors also show that OPRD-Bridge can be used to distill across architectures, allowing for representation distillation across arbitrary architectures. Overall, the paper presents a significant contribution to the field of on-policy distillation by introducing a method that addresses key limitations of existing approaches and achieves state-of-the-art performance on challenging benchmarks. The theoretical analysis and empirical results provide strong evidence for the effectiveness of OPRD and OPRD-Bridge, and the paper is well-written and easy to follow.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I found several aspects of this paper to be particularly strong. First, the authors clearly identify the limitations of existing on-policy distillation methods, specifically the high variance of gradient estimators and the loss of structural information. This provides a strong rationale for their proposed approach. The introduction of OPRD, which leverages hidden-state supervision and aligns student and teacher representations across selected layers and positions, is a novel and technically sound contribution. The theoretical analysis, which demonstrates the deterministic per-sample gradient and the exposure of structural information through the low-rank projection bridge, provides a solid foundation for the method. The authors also introduce OPRD-Bridge, which extends OPRD to cross-architecture distillation, which is a significant contribution that addresses a critical limitation of existing distillation methods. The empirical results are compelling, demonstrating that OPRD achieves state-of-the-art performance on competition-level mathematical reasoning benchmarks while significantly reducing training time and memory usage. The authors show that OPRD narrows the student-teacher gap on tasks like AIME 2024, AIME 2025, and AIMO, while training 1.44× faster and using 54% less memory. This is a significant achievement that has practical implications for the deployment of distillation methods. The paper is also well-written and easy to follow, with clear explanations of the problem, the proposed method, and the experimental results. The authors provide a thorough theoretical analysis of OPRD, including proofs of the zero-variance gradient and the loss of structural information in existing on-policy distillation methods. The empirical results are compelling, demonstrating that OPRD achieves state-of-the-art performance on competition-level mathematical reasoning benchmarks while significantly reducing training time and memory usage. The authors also provide a clear motivation for their work and a detailed explanation of their proposed method. The paper is well-structured, with clear sections for the introduction, related work, methodology, experiments, and conclusion. The authors also provide a detailed description of the OPRD-Bridge method, which is a novel contribution that addresses a critical limitation of existing distillation methods. Overall, the paper presents a significant contribution to the field of on-policy distillation by introducing a method that addresses key limitations of existing approaches and achieves state-of-the-art performance on challenging benchmarks.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper lacks a detailed analysis of the computational cost of OPRD compared to existing on-policy distillation methods. While the authors claim that OPRD is more efficient, they do not provide specific metrics such as training time, memory usage, or the number of parameters. The paper mentions that OPRD reduces wall-clock time by 30% and GPU memory usage by 20% compared to the original on-policy distillation method, but this is a high-level comparison that does not provide a detailed breakdown of the computational cost of each step of the algorithm. A more thorough analysis of the computational complexity of OPRD, including a breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself, is needed to fully assess the practical implications of using OPRD. This lack of detailed analysis makes it difficult to understand the practical trade-offs between computational cost and performance. The paper also lacks a detailed analysis of the sensitivity of OPRD to different hyperparameters, such as the rank of the projection bridge and the number of layers used for distillation. The authors introduce the rank 'r' of the projection bridge as a hyperparameter, but they do not include an analysis of how different values of 'r' affect performance. Similarly, the paper mentions selecting a subset of layers for OPRD but does not provide a sensitivity analysis of this choice. The experiments use specific values for these hyperparameters but do not explore the impact of varying them. This lack of sensitivity analysis makes it difficult to understand the robustness of OPRD and provide guidance on how to choose the optimal hyperparameters for different tasks and architectures. The paper also lacks a detailed discussion of the limitations of OPRD, particularly regarding the selection of layers for hidden state supervision and the sensitivity to hidden state dimensions. The paper focuses on the mechanics of OPRD and OPRD-Bridge but does not delve into the nuances of these choices and their potential impact on performance and applicability. The experiments also do not explore these aspects. The paper does not discuss whether certain layers are more critical than others, or if there is an optimal strategy for selecting these layers. Furthermore, the paper does not explore the sensitivity of OPRD to the choice of hidden state dimensions, which could impact the amount of information retained during distillation. This lack of discussion limits the understanding of the method's robustness and limitations. Finally, while the paper demonstrates the effectiveness of OPRD on mathematical reasoning benchmarks, it does not provide a detailed discussion of the types of tasks and models for which OPRD is most suitable, as well as the potential limitations of the method in other scenarios. For example, the authors do not discuss whether OPRD is equally effective for tasks that require different types of reasoning or for models with different architectural designs. This lack of discussion limits the understanding of the applicability of OPRD. These weaknesses, while not invalidating the contributions of the paper, do limit the practical understanding and applicability of OPRD.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed analysis of the computational cost of OPRD compared to existing on-policy distillation methods. This analysis should include specific metrics such as training time, memory usage, and the number of parameters. A breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself, would be very beneficial. A comparison with the computational cost of other on-policy distillation methods would also be valuable. This analysis should also consider the impact of different factors, such as the size of the models and the length of the input sequences, on the computational cost of OPRD. This would allow readers to better understand the practical implications of using OPRD and make informed decisions about when to use it. Second, the authors should also provide a more detailed analysis of the sensitivity of OPRD to different hyperparameters. This analysis should include a discussion of how the rank of the projection bridge and the number of layers used for distillation affect the performance of the method. For example, the authors could provide a plot showing the performance of OPRD as a function of the rank of the projection bridge and the number of layers. This would help to understand the robustness of OPRD and provide guidance on how to choose the optimal hyperparameters for different tasks and architectures. The authors should also discuss the impact of these hyperparameters on the convergence rate and the final performance of the distilled model. Third, the authors should provide a more in-depth analysis of the impact of layer selection on the performance of OPRD. Specifically, they should investigate whether certain layers are more critical for knowledge transfer than others, and if there is an optimal strategy for selecting these layers. This could involve conducting experiments where different sets of layers are used for hidden state supervision, and analyzing the resulting performance. Furthermore, the authors should explore the sensitivity of OPRD to the choice of hidden state dimensions. This could involve varying the dimensionality of the hidden states used for distillation and analyzing the impact on performance. Such an analysis would provide a more comprehensive understanding of the method's robustness and limitations. Fourth, the authors should discuss the potential challenges of applying OPRD to different types of tasks and models. This discussion should include an analysis of the types of tasks and models for which OPRD is most suitable, as well as the potential limitations of the method in other scenarios. For example, the authors could discuss whether OPRD is equally effective for tasks that require different types of reasoning or for models with different architectural designs. This would provide a more balanced and comprehensive view of the applicability of OPRD. Finally, the authors should consider including a more detailed discussion of the potential challenges in applying OPRD to different types of tasks and models. This discussion should include an analysis of the types of tasks and models for which OPRD is most suitable, as well as the potential limitations of the method in other scenarios. For example, the authors could discuss whether OPRD is equally effective for tasks that require different types of reasoning or for models with different architectural designs. This would provide a more balanced and comprehensive view of the applicability of OPRD. These suggestions, if implemented, would significantly strengthen the paper and provide a more complete understanding of the OPRD method.


## Questions:

Based on my analysis, I have several questions that I believe would be beneficial to address. First, how does the computational cost of OPRD compare to existing on-policy distillation methods, and can the authors provide a more detailed analysis of the computational complexity of the proposed method? Specifically, I would like to see a breakdown of the computational cost associated with each step of the algorithm, such as the calculation of hidden state gradients and the distillation process itself. I am also interested in understanding the impact of different factors, such as the size of the models and the length of the input sequences, on the computational cost of OPRD. Second, what is the sensitivity of OPRD to different hyperparameters, such as the rank of the projection bridge and the number of layers used for distillation? Can the authors provide empirical evidence to support their choice of hyperparameters and discuss the trade-offs involved? I am particularly interested in understanding how the rank of the projection bridge affects the performance of OPRD and whether there is an optimal strategy for selecting this hyperparameter. I would also like to see a sensitivity analysis of the number of layers used for distillation. Third, how does the choice of layers for hidden state supervision affect the performance of OPRD? Are there any guidelines for selecting the optimal layers for a given task or model? I am interested in understanding if certain layers are more critical than others and if there is an optimal strategy for selecting these layers. Fourth, how does the computational cost of OPRD compare to existing on-policy distillation methods? Can the authors provide a more detailed analysis of the computational complexity of the proposed method? I am interested in understanding the impact of different factors, such as the size of the models and the length of the input sequences, on the computational cost of OPRD. Finally, how does the performance of OPRD vary when using different numbers of layers for distillation? I would like to see a plot showing the performance of OPRD as a function of the number of layers, which would be very useful. These questions target key uncertainties in the methodology and seek clarification of critical assumptions, aiming to provide a more complete understanding of the OPRD method.


## Rating:

6.75


## Confidence:

3.5


## Decision:

Accept
}