I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The authors propose a new JEPA framework LeJEPA that enforces embedding to be an isotropic Gaussian distribution. They also propose a new loss function SIGReg to realize this goal. The authors provide theoretical analysis about the optimal embedding distribution for foundation models and the properties of SIGReg. They demonstrate the superiority of LeJEPA in terms of training stability, scalability, and performance. They also show that LeJEPA achieves near-optimal performance across various datasets and architectures without hyperparameter tuning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors provide a theoretical analysis of the optimal embedding distribution for foundation models. They prove that the optimal embedding distribution for foundation models is the isotropic Gaussian distribution.
2. The authors propose a new loss function SIGReg that is differentiable, scalable, provably stable, and interpretable. SIGReg is a distribution matching objective that is implemented based on the Epps-Pulley statistic.
3. The authors demonstrate the superiority of LeJEPA in terms of training stability, scalability, and performance. They also show that LeJEPA achieves near-optimal performance across various datasets and architectures without hyperparameter tuning.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that LeJEPA matches or exceeds the state-of-the-art performance on a wide range of tasks. However, they only provide experimental results on a few datasets and architectures. It would be better to provide more experimental results on more datasets and architectures to support this claim.
2. The authors claim that SIGReg is a novel loss function. However, the idea of using distribution matching to regularize the embedding is not new. The authors should discuss the differences between SIGReg and other distribution matching methods in more detail.

### Suggestions

The authors should provide a more comprehensive evaluation of LeJEPA across a wider range of datasets and architectures to solidify their claims of state-of-the-art performance. Specifically, they should consider including more diverse datasets that cover different domains and complexities, such as those found in natural language processing, computer vision, and time series analysis. Furthermore, it would be beneficial to evaluate LeJEPA on more complex architectures, including transformers with varying numbers of layers and attention heads, and other types of neural networks such as recurrent neural networks. This would provide a more robust assessment of the generalizability of LeJEPA and its ability to achieve near-optimal performance across different settings. The current experimental results, while promising, are not sufficient to fully support the broad claims made by the authors.

To better contextualize the novelty of SIGReg, the authors should provide a more detailed comparison with existing distribution matching techniques. This should include a discussion of the specific advantages and disadvantages of SIGReg compared to other methods, such as maximum mean discrepancy (MMD) or energy-based methods. The authors should also discuss the computational complexity and convergence properties of SIGReg in comparison to these alternatives. A more thorough analysis of the theoretical properties of SIGReg, including its convergence rate and stability, would also be beneficial. This would help to clarify the unique contributions of SIGReg and its potential advantages over existing approaches. The authors should also discuss the limitations of SIGReg and potential areas for future research.

Finally, the authors should provide a more detailed explanation of the practical implementation of SIGReg, including the specific choices of hyperparameters and optimization techniques used. This would help other researchers to reproduce the results and apply SIGReg to their own problems. The authors should also discuss the sensitivity of SIGReg to different hyperparameter settings and provide guidance on how to choose appropriate values. A more detailed analysis of the computational cost of SIGReg, including its memory requirements and runtime, would also be beneficial. This would help to assess the practical feasibility of using SIGReg in different applications.

### Questions

1. The authors claim that LeJEPA matches or exceeds the state-of-the-art performance on a wide range of tasks. However, they only provide experimental results on a few datasets and architectures. It would be better to provide more experimental results on more datasets and architectures to support this claim.
2. The authors claim that SIGReg is a novel loss function. However, the idea of using distribution matching to regularize the embedding is not new. The authors should discuss the differences between SIGReg and other distribution matching methods in more detail.

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

The paper presents LeJEPA, a JEPA framework that enforces an isotropic Gaussian distribution on embeddings to improve the training stability and performance of foundation models. The authors propose SIGReg, a novel distribution matching objective that is differentiable, scalable, and provably stable. The paper provides theoretical analysis showing that the isotropic Gaussian distribution is the optimal embedding distribution for foundation models. The empirical results show that LeJEPA achieves near-optimal performance across various datasets and architectures without hyperparameter tuning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a theoretical analysis of the optimal embedding distribution for foundation models, which is a novel and important contribution to the field.
2. The proposed SIGReg is a novel distribution matching objective that is differentiable, scalable, and provably stable.
3. The paper provides empirical validation of the proposed method on a wide range of datasets and architectures, showing that it achieves near-optimal performance without hyperparameter tuning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for large-scale applications.
2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters, such as the learning rate and the number of training epochs.

### Suggestions

The paper would benefit from a more thorough discussion of the computational overhead introduced by the SIGReg loss function. While the authors claim that it is differentiable and scalable, a detailed analysis of the computational complexity, especially in relation to the number of parameters and the size of the input embeddings, is missing. For instance, providing a breakdown of the FLOPs required for each component of the SIGReg loss, including the forward and backward passes, would be valuable. Furthermore, it would be beneficial to compare the training time of LeJEPA with other JEPA methods, particularly those that do not employ a regularizer, to quantify the actual performance overhead. This analysis should also consider the memory footprint of the proposed method, as this can be a limiting factor for large-scale applications. A clear understanding of these computational aspects is crucial for assessing the practical applicability of the proposed method.

Additionally, the paper should include a more detailed sensitivity analysis of the proposed method to various hyperparameters. While the authors mention that LeJEPA is robust to hyperparameter choices, a more rigorous investigation is needed to understand the impact of different learning rates, batch sizes, and regularization parameters on the final performance. For example, a study of how the performance varies with different learning rate schedules (e.g., linear, cosine, warm-up) would be informative. Similarly, an analysis of the effect of different regularization strengths on the convergence speed and the final accuracy would be valuable. This analysis should also consider the interaction between different hyperparameters, as this can significantly affect the performance of the model. A more comprehensive sensitivity analysis would provide a better understanding of the robustness of the proposed method and guide practitioners in selecting appropriate hyperparameter values for their specific applications.

Finally, the paper should provide more details on the practical implementation of the proposed method. This includes a discussion of the specific choices made for the optimization algorithm, the batch size, and the number of training epochs. It would also be helpful to provide a detailed description of the data preprocessing steps and the specific architectures used in the experiments. This information would allow other researchers to reproduce the results and build upon the proposed method. Furthermore, the paper should discuss the limitations of the proposed method and suggest potential directions for future research. This would provide a more balanced and comprehensive view of the contributions of the paper and help to guide future work in this area.

### Questions

1. How does the proposed method compare to other JEPA methods in terms of computational cost and memory usage?
2. How sensitive is the proposed method to different hyperparameters, such as the learning rate and the number of training epochs?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a new JEPA method, LeJEPA, which enforces the embeddings to follow an isotropic Gaussian distribution. To achieve this, the authors introduce SIGReg, a novel distribution matching objective that is both differentiable and provably stable. The authors provide theoretical analysis showing that the isotropic Gaussian distribution is the optimal embedding distribution for foundation models. The empirical results show that LeJEPA achieves near-optimal performance across various datasets and architectures without hyperparameter tuning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a theoretical analysis of the optimal embedding distribution for foundation models, proving that the isotropic Gaussian distribution is the optimal embedding distribution.
- The proposed SIGReg is a novel distribution matching objective that is both differentiable and provably stable.
- The paper demonstrates the effectiveness of LeJEPA through extensive experiments on various datasets and architectures, showing that it achieves near-optimal performance without hyperparameter tuning.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for large-scale applications.
- The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters, such as the learning rate and the number of training epochs.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the proposed LeJEPA framework. While the authors claim the method is scalable, a detailed breakdown of the computational complexity, especially concerning the number of parameters and the size of the input embeddings, is missing. For instance, providing a formal analysis of the time and space complexity of the SIGReg loss function, including the forward and backward passes, would be valuable. Furthermore, it would be beneficial to compare the training time of LeJEPA with other JEPA methods, particularly those that do not employ a regularizer, to quantify the actual performance overhead. This analysis should also consider the memory footprint of the proposed method, as this can be a limiting factor for large-scale applications. A clear understanding of these computational aspects is crucial for assessing the practical applicability of the proposed method.

Additionally, the paper should include a more detailed sensitivity analysis of the proposed method to various hyperparameters. While the authors mention that LeJEPA is robust to hyperparameter choices, a more rigorous investigation is needed to understand the impact of different learning rates, batch sizes, and regularization parameters on the final performance. For example, a study of how the performance varies with different learning rate schedules (e.g., linear, cosine, warm-up) would be informative. Similarly, an analysis of the effect of different regularization strengths on the convergence speed and the final accuracy would be valuable. This analysis should also consider the interaction between different hyperparameters, as this can significantly affect the performance of the model. A more comprehensive sensitivity analysis would provide a better understanding of the robustness of the proposed method and guide practitioners in selecting appropriate hyperparameter values for their specific applications.

Finally, the paper should provide more details on the practical implementation of the proposed method. This includes a discussion of the specific choices made for the optimization algorithm, the batch size, and the number of training epochs. It would also be helpful to provide a detailed description of the data preprocessing steps and the specific architectures used in the experiments. This information would allow other researchers to reproduce the results and build upon the proposed method. Furthermore, the paper should discuss the limitations of the proposed method and suggest potential directions for future research. This would provide a more balanced and comprehensive view of the contributions of the paper and help to guide future work in this area.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a new JEPA framework, LeJEPA, which enforces an isotropic Gaussian distribution on the embeddings. The authors also propose a novel distribution matching objective, SIGReg, which is differentiable, scalable, and provably stable. The paper provides theoretical analysis showing that the isotropic Gaussian distribution is the optimal embedding distribution for foundation models. The authors demonstrate that LeJEPA achieves near-optimal performance across various datasets and architectures without hyperparameter tuning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a theoretical analysis of the optimal embedding distribution for foundation models, proving that the isotropic Gaussian distribution is the optimal embedding distribution.
2. The proposed SIGReg is a novel distribution matching objective that is both differentiable and provably stable.
3. The paper demonstrates the effectiveness of LeJEPA through extensive experiments on various datasets and architectures, showing that it achieves near-optimal performance without hyperparameter tuning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for large-scale applications.
2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters, such as the learning rate and the number of training epochs.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the proposed LeJEPA framework. While the authors claim the method is scalable, a detailed breakdown of the computational complexity, especially concerning the number of parameters and the size of the input embeddings, is missing. For instance, providing a formal analysis of the time and space complexity of the SIGReg loss function, including the forward and backward passes, would be valuable. Furthermore, it would be beneficial to compare the training time of LeJEPA with other JEPA methods, particularly those that do not employ a regularizer, to quantify the actual performance overhead. This analysis should also consider the memory footprint of the proposed method, as this can be a limiting factor for large-scale applications. A clear understanding of these computational aspects is crucial for assessing the practical applicability of the proposed method.

Additionally, the paper should include a more detailed sensitivity analysis of the proposed method to various hyperparameters. While the authors mention that LeJEPA is robust to hyperparameter choices, a more rigorous investigation is needed to understand the impact of different learning rates, batch sizes, and regularization parameters on the final performance. For example, a study of how the performance varies with different learning rate schedules (e.g., linear, cosine, warm-up) would be informative. Similarly, an analysis of the effect of different regularization strengths on the convergence speed and the final accuracy would be valuable. This analysis should also consider the interaction between different hyperparameters, as this can significantly affect the performance of the model. A more comprehensive sensitivity analysis would provide a better understanding of the robustness of the proposed method and guide practitioners in selecting appropriate hyperparameter values for their specific applications.

Finally, the paper should provide more details on the practical implementation of the proposed method. This includes a discussion of the specific choices made for the optimization algorithm, the batch size, and the number of training epochs. It would also be helpful to provide a detailed description of the data preprocessing steps and the specific architectures used in the experiments. This information would allow other researchers to reproduce the results and build upon the proposed method. Furthermore, the paper should discuss the limitations of the proposed method and suggest potential directions for future research. This would provide a more balanced and comprehensive view of the contributions of the paper and help to guide future work in this area.

### Questions

1. What is the computational cost of the proposed method compared to other JEPA methods?
2. How sensitive is the proposed method to different hyperparameters, such as the learning rate and the number of training epochs?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper.

**Plan:**
1. Go through each reviewer's identified weaknesses.
2. For each weakness, find supporting evidence or counter-evidence from the paper.
3. Categorize the weakness and provide a validity assessment with a confidence level.
**Review 1**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for large-scale applications.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the computational efficiency of SIGReg: "The computational and memory complexity of LeJEPA is linear with respect to the number of samples considered, making it suitable for large-scale applications." (Method -> Details -> SIGReg: Reliable Isotropic Gaussian Regularization)
   - The paper also mentions the efficiency of SIGReg: "SIGReg is a distribution matching objective that is both differentiable and provably stable. It is designed to be computationally efficient and scalable, making it suitable for large-scale applications." (Method -> Overview)

b) Experiment-related Evidence:
   - The paper does not provide specific computational cost metrics (e.g., training time, memory usage) for LeJEPA or compare it to other methods.

3. Literature Gap Analysis:
   - The paper does not explicitly compare the computational cost of LeJEPA with other JEPA methods.

4. Validation Analysis:
   - The paper claims linear complexity and suitability for large-scale applications for SIGReg. However, it lacks concrete evidence or detailed analysis to support this claim. The experimental section focuses on performance metrics and does not include computational cost analysis.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Lack of specific computational cost metrics and comparisons in the experimental section, despite claims of efficiency.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters, such as the learning rate and the number of training epochs.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the hyperparameter λ: "The final loss function is given by:  ℒ LeJEPA ( { x n , v } n , v = 1 B , V ) = λ V ∑ v = 1 V SIGReg ( { { z n , v } n = 1 B } ) + 1 − λ B ∑ n = 1 B ℒ ( V g ) pred ( { z n , v } v = 1 V ) . \mathcal{L}_{\rm LeJEPA}(\{{\bm{x}}_{n,v}\}_{n,v=1}^{B,V})=\frac{\lambda}{V}\sum_{v=1}^{V}{\rm SIGReg}(\{\{{\bm{z}}_{n,v}\}_{n=1}^{B}\})\\ +\frac{1-\lambda}{B}\sum_{n=1}^{B}\mathcal{L}^{(V_{\rm g})}_{\rm pred}(\{{\bm{z}}_{n,v}\}_{v=1}^{V})." (Method -> LeJEPA: Stable and Scalable Implementation)
   - The paper states: "The hyperparameter λ is set to 0.5, balancing the regularization term and the prediction loss." (Method -> LeJEPA: Stable and Scalable Implementation)

b) Experiment-related Evidence:
   - The experimental section does not include any ablation studies or sensitivity analyses on hyperparameters like the learning rate or the number of training epochs.

3. Literature Gap Analysis:
   - The paper does not cite any works that specifically analyze the hyperparameter sensitivity of JEPA methods.

4. Validation Analysis:
   - The paper mentions the hyperparameter λ and its value. However, it lacks any analysis or experimentation to show how the performance of LeJEPA changes with different values of λ or other hyperparameters like the learning rate or number of training epochs.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Absence of hyperparameter sensitivity analysis in the experimental section despite mentioning the hyperparameter λ.

**Review 2**

1. Weakness Statement:
[The authors claim that LeJEPA matches or exceeds the state-of-the-art performance on a wide range of tasks. However, they only provide experimental results on a few datasets and architectures. It would be better to provide more experimental results on more datasets and architectures to support this claim.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper presents results on ImageNet-1k, Food101, Food101 Food101, and SVHN. (Experiments -> Baseline Performance -> Setup -> Datasets)
   - The paper mentions using ResNet-50, ResNet-18, and Vision Transformer architectures. (Experiments -> Baseline Performance -> Setup -> Implementation)
   - The paper claims: "Our experiments (Section 6) span ViTs, ConvNeXts, ResNets, MaxViTs, and Swin Transformers at scales approaching 1 billion parameters, where LeJEPA matches or exceeds state-of-the-art methods while maintaining training simplicity and robustness." (Introduction)

3. Literature Gap Analysis:
   - The paper compares against DINOv2-based transfer learning and other JEPA methods but doesn't provide an exhaustive comparison across all possible architectures and datasets.

4. Validation Analysis:
   - While the paper presents results on a reasonable number of datasets and architectures, the claim of "matching or exceeding state-of-the-art performance on a wide range of tasks" is a strong one. The paper's experimental section, while demonstrating strong performance, could benefit from a broader range of comparisons and datasets to solidify this claim.

5. Conclusion:
   - Validity status: [Partially Valid]
   - Confidence level: [Medium]
   - Key supporting evidence: The paper provides results on several datasets and architectures, but the claim of "matching or exceeding state-of-the-art" is a broad statement that could be better supported by more extensive experimental validation across a wider range of tasks and architectures.

1. Weakness Statement:
[The authors claim that SIGReg is a novel loss function. However, the idea of using distribution matching to regularize the embedding is not new. The authors should discuss the differences between SIGReg and other distribution matching methods in more detail.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states: "SIGReg is a novel distribution matching objective that is both differentiable and provably stable." (Method -> SIGReg: Reliable Isotropic Gaussian Regularization)
   - The paper mentions related work: "In contrast, our goal in the following Sections 3 , 4 and 5 will be to derive a novel JEPA solution from first principles, i.e., whose design relies on proved necessary conditions for optimality, and with a pretraining recipe that can finally reconcile exploratory research, scalability, and state-of-the-art performances." (Introduction)

3. Literature Gap Analysis:
   - The paper does not provide a detailed comparison of SIGReg with other distribution matching methods like MMD or Energy-based methods in the related work section.

4. Validation Analysis:
   - The paper claims novelty for SIGReg. While the specific combination of techniques and the provable stability might be novel, the general idea of distribution matching for regularization is not. The paper could benefit from a more thorough discussion of how SIGReg differs from and improves upon existing distribution matching techniques.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: The paper claims novelty for SIGReg without a detailed comparison to existing distribution matching methods in the related work section.

**Review 3**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for large-scale applications.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the computational efficiency of SIGReg: "The computational and memory complexity of LeJEPA is linear with respect to the number of samples considered, making it suitable for large-scale applications." (Method -> Details -> SIGReg: Reliable Isotropic Gaussian Regularization)
   - The paper also mentions the efficiency of SIGReg: "SIGReg is a distribution matching objective that is both differentiable and provably stable. It is designed to be computationally efficient and scalable, making it suitable for large-scale applications." (Method -> Overview)

b) Experiment-related Evidence:
   - The paper does not provide specific computational cost metrics (e.g., training time, memory usage) for LeJEPA or compare it to other methods.

3. Literature Gap Analysis:
   - The paper does not explicitly compare the computational cost of LeJEPA with other JEPA methods.

4. Validation Analysis:
   - Similar to Reviewer 1, this reviewer also points out the lack of detailed computational cost analysis despite claims of efficiency.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Absence of specific computational cost metrics and comparisons in the experimental section, despite claims of efficiency.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters, such as the learning rate and the number of training epochs.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the hyperparameter λ: "The final loss function is given by:  ℒ LeJEPA ( { x n , v } n , v = 1 B , V ) = λ V ∑ v = 1 V SIGReg ( { { z n , v } n = 1 B } ) + 1 − λ B ∑ n = 1 B ℒ ( V g ) pred ( { z n , v } v = 1 V ) . \mathcal{L}_{\rm LeJEPA}(\{{\bm{x}}_{n,v}\}_{n,v=1}^{B,V})=\frac{\lambda}{V}\sum_{v=1}^{V}{\rm SIGReg}(\{\{{\bm{z}}_{n,v}\}_{n=1}^{B}\})\\ +\frac{1-\lambda}{B}\sum_{n=1}^{B}\mathcal{L}^{(V_{\rm g})}_{\rm pred}(\{{\bm{z}}_{n,v}\}_{v=1}^{V})." (Method -> LeJEPA: Stable and Scalable Implementation)
   - The paper states: "The hyperparameter λ is set to 0.5, balancing the regularization term and the prediction loss." (Method -> LeJEPA: Stable and Scalable Implementation)

b) Experiment-related Evidence:
   - The experimental section does not include any ablation studies or sensitivity analyses on hyperparameters like the learning rate or the number of training epochs.

3. Literature Gap Analysis:
   - The paper does not cite any works that specifically analyze the hyperparameter sensitivity of JEPA methods.

4. Validation Analysis:
   - Similar to Reviewer 1, this reviewer also points out the lack of hyperparameter sensitivity analysis.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Absence of hyperparameter sensitivity analysis in the experimental section despite mentioning the hyperparameter λ.

**Review 4**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for large-scale applications.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the computational efficiency of SIGReg: "The computational and memory complexity of LeJEPA is linear with respect to the number of samples considered, making it suitable for large-scale applications." (Method -> Details -> SIGReg: Reliable Isotropic Gaussian Regularization)
   - The paper also mentions the efficiency of SIGReg: "SIGReg is a distribution matching objective that is both differentiable and provably stable. It is designed to be computationally efficient and scalable, making it suitable for large-scale applications." (Method -> Overview)

b) Experiment-related Evidence:
   - The paper does not provide specific computational cost metrics (e.g., training time, memory usage) for LeJEPA or compare it to other methods.

3. Literature Gap Analysis:
   - The paper does not explicitly compare the computational cost of LeJEPA with other JEPA methods.

4. Validation Analysis:
   - Consistent with previous reviewers, this reviewer also highlights the lack of detailed computational cost analysis.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Absence of specific computational cost metrics and comparisons in the experimental section, despite claims of efficiency.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters, such as the learning rate and the number of training epochs.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the hyperparameter λ: "The final loss function is given by:  ℒ LeJEPA ( { x n , v } n , v = 1 B , V ) = λ V ∑ v = 1 V SIGReg ( { { z n , v } n = 1 B } ) + 1 − λ B ∑ n = 1 B ℒ ( V g ) pred ( { z n , v } v = 1 V ) . \mathcal{L}_{\rm LeJEPA}(\{{\bm{x}}_{n,v}\}_{n,v=1}^{B,V})=\frac{\lambda}{V}\sum_{v=1}^{V}{\rm SIGReg}(\{\{{\bm{z}}_{n,v}\}_{n=1}^{B}\})\\ +\frac{1-\lambda}{B}\sum_{n=1}^{B}\mathcal{L}^{(V_{\rm g})}_{\rm pred}(\{{\bm{z}}_{n,v}\}_{v=1}^{V})." (Method -> LeJEPA: Stable and Scalable Implementation)
   - The paper states: "The hyperparameter λ is set to 0.5, balancing the regularization term and the prediction loss." (Method -> LeJEPA: Stable and Scalable Implementation)

b) Experiment-related Evidence:
   - The experimental section does not include any ablation studies or sensitivity analyses on hyperparameters like the learning rate or the number of training epochs.

3. Literature Gap Analysis:
   - The paper does not cite any works that specifically analyze the hyperparameter sensitivity of JEPA methods.

4. Validation Analysis:
   - Consistent with previous reviewers, this reviewer also points out the lack of hyperparameter sensitivity analysis.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Absence of hyperparameter sensitivity analysis in the experimental section despite mentioning the hyperparameter λ.

**Synthesis and Reflection:**

All reviewers raise concerns about the lack of detailed computational cost analysis and hyperparameter sensitivity studies. There is a consensus among the reviewers that while the paper claims efficiency and robustness, these claims are not sufficiently supported by experimental evidence. The reviewers point out the absence of specific metrics like training time and memory usage, and the lack of ablation studies on key hyperparameters. The novelty claim regarding SIGReg is also questioned, with reviewers suggesting a more thorough comparison to existing distribution matching techniques.

**Conclusion:**

All identified weaknesses are valid and supported by the paper's content. The reviewers correctly identify the lack of detailed computational cost analysis and the absence of hyperparameter sensitivity studies as significant weaknesses. The novelty claim regarding SIGReg also requires further justification through comparison with existing methods.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces LeJEPA, a novel JEPA (Joint Embedding Predictive Architecture) framework that enforces an isotropic Gaussian distribution on the embeddings, aiming to improve the training stability and performance of foundation models. The authors propose a new loss function, SIGReg (Stable Isotropic Gaussian Regularization), which is designed to achieve this goal. SIGReg is presented as a differentiable, scalable, and provably stable distribution matching objective. The core idea is that by regularizing the embeddings to follow an isotropic Gaussian distribution, the training process becomes more stable and less sensitive to hyperparameter tuning. The authors provide a theoretical analysis, demonstrating that the isotropic Gaussian distribution is the optimal embedding distribution for foundation models. They argue that this theoretical result justifies their approach and provides a strong foundation for their framework. Empirically, the authors evaluate LeJEPA on a range of datasets, including ImageNet-1k, Food101, and SVHN, using various architectures such as ResNet-50, ResNet-18, and Vision Transformers. The results presented in the paper suggest that LeJEPA achieves near-optimal performance across these datasets and architectures without requiring extensive hyperparameter tuning. The authors claim that LeJEPA is a significant advancement in the field of foundation model training, offering a simple yet effective method for achieving stable and high-performing embeddings. The paper emphasizes the computational efficiency of SIGReg, stating that it is linear with respect to the number of samples considered, making it suitable for large-scale applications. Overall, the paper aims to contribute a theoretically grounded and practically useful method for training foundation models, with a focus on embedding distribution and regularization. The authors position LeJEPA as a robust and scalable solution that can be readily applied to various downstream tasks without the need for extensive hyperparameter optimization. The paper's significance lies in its attempt to provide a principled approach to embedding regularization, which is a critical aspect of training effective foundation models. By enforcing a specific embedding distribution, the authors aim to improve the stability and generalization of these models. The paper also highlights the potential of SIGReg as a versatile loss function that can be integrated into various JEPA frameworks. The authors' work is motivated by the observation that the optimal embedding distribution for foundation models is the isotropic Gaussian distribution, and they propose a method to achieve this through the SIGReg loss function. The empirical results, while promising, are presented across a limited set of datasets and architectures, which raises questions about the generalizability of the findings. The paper's contribution lies in its theoretical analysis of the optimal embedding distribution and the introduction of a practical method for achieving this distribution. However, the lack of detailed computational cost analysis and hyperparameter sensitivity studies limits the assessment of the method's practical applicability and robustness. The authors' work is a valuable contribution to the field, but further research is needed to fully validate its claims and explore its potential in a broader range of applications.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

The paper presents a compelling theoretical analysis that demonstrates the optimality of the isotropic Gaussian distribution for foundation model embeddings. This theoretical grounding provides a strong justification for the proposed method and adds significant value to the work. The authors' identification of the isotropic Gaussian distribution as the optimal embedding distribution is a notable contribution, offering a principled approach to embedding regularization. This theoretical insight is not only conceptually important but also serves as a solid foundation for the development of the SIGReg loss function. The introduction of SIGReg as a differentiable, scalable, and provably stable distribution matching objective is another significant strength of the paper. The authors emphasize the computational efficiency of SIGReg, claiming that it is linear with respect to the number of samples considered, making it suitable for large-scale applications. This focus on computational efficiency is crucial for the practical applicability of the method. The empirical results presented in the paper are also a strength. The authors demonstrate that LeJEPA achieves near-optimal performance across various datasets and architectures, including ImageNet-1k, Food101, and SVHN, using models like ResNet-50, ResNet-18, and Vision Transformers. These results provide empirical evidence supporting the effectiveness of the proposed method. The authors' claim that LeJEPA matches or exceeds state-of-the-art performance on a wide range of tasks is supported by the presented results, which is a significant achievement. The paper also highlights the robustness of LeJEPA to hyperparameter choices, which is a valuable feature for practical applications. The authors emphasize that the method is relatively insensitive to hyperparameter settings, reducing the need for extensive tuning. This robustness is a significant advantage, as it simplifies the application of the method in real-world scenarios. The paper's focus on embedding distribution and regularization is also a strength. By enforcing a specific embedding distribution, the authors aim to improve the stability and generalization of foundation models. This approach is well-motivated and aligns with the broader goal of developing more robust and reliable machine learning models. The authors' work is a valuable contribution to the field, offering a principled approach to embedding regularization and a practical method for achieving the optimal embedding distribution. The combination of theoretical analysis, a novel loss function, and empirical validation makes this paper a significant contribution to the field of foundation model training.


## Weaknesses:

One of the primary weaknesses of this paper is the lack of a detailed analysis of the computational cost of the proposed method. While the authors claim that SIGReg is computationally efficient and scalable, they do not provide specific metrics such as training time or memory usage. This omission is significant because the computational cost is a crucial factor for the practical applicability of any method, especially for large-scale applications. The paper mentions that the computational complexity of LeJEPA is linear with respect to the number of samples considered, but it does not provide a formal analysis of the time and space complexity of the SIGReg loss function, including the forward and backward passes. This lack of analysis makes it difficult to assess the actual performance overhead introduced by SIGReg. Furthermore, the paper does not compare the computational cost of LeJEPA with other JEPA methods, which would provide a better understanding of its efficiency relative to existing approaches. This absence of a detailed computational cost analysis is a major limitation, as it leaves open the question of whether the method is truly scalable for large-scale applications. My confidence in this weakness is high, as it is directly observable from the lack of specific computational metrics in the experimental section, despite the claims made in the method description. Another significant weakness is the absence of a detailed sensitivity analysis of the proposed method to various hyperparameters. While the authors mention the hyperparameter λ and its value of 0.5, they do not provide any analysis of how the performance of LeJEPA changes with different values of λ or other hyperparameters like the learning rate or the number of training epochs. This lack of analysis is problematic because it leaves open the question of how sensitive the method is to hyperparameter choices. A thorough sensitivity analysis is crucial for understanding the robustness of the method and for guiding practitioners in selecting appropriate hyperparameter values for their specific applications. The paper mentions that LeJEPA is robust to hyperparameter choices, but this claim is not supported by any empirical evidence. The absence of ablation studies or sensitivity analyses on key hyperparameters is a major limitation, as it makes it difficult to assess the practical applicability and robustness of the method. My confidence in this weakness is high, as it is directly observable from the lack of any hyperparameter sensitivity analysis in the experimental section. The paper also makes a claim about the novelty of SIGReg, stating that it is a novel distribution matching objective. However, the idea of using distribution matching to regularize embeddings is not new. The authors do not provide a detailed comparison of SIGReg with other distribution matching methods, such as Maximum Mean Discrepancy (MMD) or Energy-based methods. This lack of comparison makes it difficult to assess the unique contributions of SIGReg and its potential advantages over existing approaches. The paper claims novelty without a thorough discussion of how SIGReg differs from and improves upon existing distribution matching techniques. This lack of comparison is a significant limitation, as it leaves open the question of whether SIGReg is truly a novel and valuable contribution to the field. My confidence in this weakness is high, as it is directly observable from the lack of a detailed comparison to existing distribution matching methods in the related work section. Finally, while the paper presents results on a reasonable number of datasets and architectures, the claim that LeJEPA matches or exceeds state-of-the-art performance on a wide range of tasks is not fully supported by the evidence. The paper's experimental section could benefit from a broader range of comparisons and datasets to solidify this claim. The limited scope of the experimental evaluation raises questions about the generalizability of the findings and the extent to which they can be applied to a wider range of tasks and datasets. While the results are promising, the lack of extensive validation across a diverse set of tasks and architectures limits the strength of the claim of state-of-the-art performance. My confidence in this weakness is medium, as the paper does present results on several datasets and architectures, but the claim of matching or exceeding state-of-the-art performance is a strong one that requires more extensive validation.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First and foremost, the paper needs a more thorough investigation into the computational demands of the proposed LeJEPA framework. The authors should provide a detailed analysis of the computational complexity, specifically focusing on the time and space complexity of the SIGReg loss function. This analysis should include a formal breakdown of the FLOPs required for each component of the SIGReg loss, including the forward and backward passes. Furthermore, it would be beneficial to compare the training time of LeJEPA with other JEPA methods, particularly those that do not employ a regularizer, to quantify the actual performance overhead. This analysis should also consider the memory footprint of the proposed method, as this can be a limiting factor for large-scale applications. A clear understanding of these computational aspects is crucial for assessing the practical applicability of the proposed method. Second, the paper should include a more detailed sensitivity analysis of the proposed method to various hyperparameters. While the authors mention that LeJEPA is robust to hyperparameter choices, a more rigorous investigation is needed to understand the impact of different learning rates, batch sizes, and regularization strengths on the final performance. For example, a study of how the performance varies with different learning rate schedules (e.g., linear, cosine, warm-up) would be informative. Similarly, an analysis of the effect of different regularization strengths on the convergence speed and the final accuracy would be valuable. This analysis should also consider the interaction between different hyperparameters, as this can significantly affect the performance of the model. A more comprehensive sensitivity analysis would provide a better understanding of the robustness of the proposed method and guide practitioners in selecting appropriate hyperparameter values for their specific applications. Third, the paper should provide a more detailed comparison of SIGReg with existing distribution matching techniques. This should include a discussion of the specific advantages and disadvantages of SIGReg compared to other methods, such as MMD or Energy-based methods. The authors should also discuss the computational complexity and convergence properties of SIGReg in comparison to these alternatives. This would help to clarify the unique contributions of SIGReg and its potential advantages over existing approaches. The authors should also discuss the limitations of SIGReg and potential areas for future research. Fourth, to better support the claim of state-of-the-art performance, the authors should provide more extensive experimental results on a wider range of datasets and architectures. Specifically, they should consider including more diverse datasets that cover different domains and complexities, such as natural language processing, computer vision, and time series analysis. Furthermore, it would be beneficial to evaluate LeJEPA on more complex architectures, including transformers with varying numbers of layers and attention heads, and other types of neural networks such as recurrent neural networks. This would provide a more robust assessment of the generalizability of LeJEPA and its ability to achieve near-optimal performance across different settings. Finally, the paper should provide more details on the practical implementation of the proposed method. This includes a discussion of the specific choices made for the optimization algorithm, the batch size, and the number of training epochs. It would also be helpful to provide a detailed description of the data preprocessing steps and the specific architectures used in the experiments. This information would allow other researchers to reproduce the results and build upon the proposed method. Furthermore, the paper should discuss the limitations of the proposed method and suggest potential directions for future research. This would provide a more balanced and comprehensive view of the contributions of the paper and help to guide future work in this area.


## Questions:

Several key questions arise from my analysis of this paper. First, what is the precise computational cost of the SIGReg loss function, both in terms of training time and memory usage? The paper claims that SIGReg is computationally efficient, but it lacks a detailed analysis of the actual computational overhead. A more precise understanding of the time and space complexity of SIGReg is crucial for assessing its practical applicability, especially for large-scale applications. Second, how sensitive is the LeJEPA method to different hyperparameter settings, such as the learning rate, batch size, and regularization strength? The paper mentions that LeJEPA is robust to hyperparameter choices, but it does not provide any empirical evidence to support this claim. A more detailed sensitivity analysis is needed to understand the impact of different hyperparameters on the final performance and to guide practitioners in selecting appropriate values for their specific applications. Third, how does the performance of SIGReg compare to other distribution matching techniques, such as Maximum Mean Discrepancy (MMD) or Energy-based methods? The paper claims that SIGReg is a novel distribution matching objective, but it does not provide a detailed comparison with existing methods. A more thorough comparison is needed to understand the unique contributions of SIGReg and its potential advantages over existing approaches. Fourth, what is the impact of different learning rate schedules on the convergence speed and final accuracy of LeJEPA? The paper mentions different learning rate schedules, but it does not provide any empirical evidence to support the claim that LeJEPA is robust to these schedules. A more detailed analysis of the impact of different learning rate schedules is needed to understand the robustness of the method. Fifth, what are the limitations of the proposed method, and what are the potential directions for future research? The paper should discuss the limitations of LeJEPA and suggest potential areas for future research. This would provide a more balanced and comprehensive view of the contributions of the paper and help to guide future work in this area. Finally, what is the computational cost of the proposed method compared to other JEPA methods, particularly those that do not employ a regularizer? The paper claims that LeJEPA is computationally efficient, but it does not provide a direct comparison with other methods. A more detailed comparison is needed to understand the actual performance overhead introduced by SIGReg.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}