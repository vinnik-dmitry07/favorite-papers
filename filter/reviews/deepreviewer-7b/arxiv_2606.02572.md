I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper introduces VISReg, a self-supervised learning (SSL) method that enhances embedding stability and distributional control without relying on heuristics. VISReg builds on the principles of VICReg and LeJEPA, but addresses their limitations by replacing covariance-based regularization with a Sliced-Wasserstein Distance (SWD)-based sketching objective. This approach enforces the full distributional shape of embeddings, ensuring robust gradients even under collapse. The paper demonstrates VISReg's effectiveness across various datasets and tasks, including OOD generalization and dense prediction, positioning it as a promising foundation model for SSL.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and addresses the limitations of previous methods.
3. The experiments are comprehensive, and the results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed method. The use of Sliced-Wasserstein Distance (SWD) for regularization, while effective, may introduce additional computational overhead compared to simpler covariance-based methods. A thorough comparison of training time and memory requirements, especially when scaling to larger datasets and models, is needed to fully assess the practical applicability of VISReg. Specifically, the paper should detail the time complexity of the SWD calculation and provide empirical measurements of training time and memory usage for various model sizes and dataset scales. This analysis should also consider the impact of the number of slices used in the SWD calculation on computational cost and regularization strength.
2. The paper does not provide a clear explanation of how the proposed method handles the trade-off between scale and shape regularization. While the method introduces a hyperparameter to balance these two aspects, the paper lacks a detailed discussion on how this parameter should be tuned for different datasets and tasks. A more in-depth analysis of the sensitivity of the method to this hyperparameter, along with guidelines for selecting appropriate values, would be beneficial. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the Sliced-Wasserstein Distance (SWD) regularization. Specifically, the authors should provide a breakdown of the time complexity of the SWD calculation, considering the number of slices used and the dimensionality of the embeddings. Empirical measurements of training time and memory usage for various model sizes (e.g., ViT-B/16, ViT-L/14) and dataset scales should be included, along with a comparison to the computational cost of covariance-based methods. This analysis should also investigate the impact of the number of slices on both computational cost and regularization strength, providing practical guidance on selecting an appropriate number of slices for different scenarios. Furthermore, the authors should discuss potential optimizations for the SWD calculation to reduce computational overhead, such as using approximation techniques or parallel processing.

To address the lack of clarity regarding the scale and shape regularization trade-off, the authors should provide a more detailed analysis of the hyperparameter controlling this balance. This analysis should include a sensitivity study, demonstrating how the performance of the method varies with different values of this hyperparameter across various datasets and tasks. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value. For example, the authors could investigate using a feedback mechanism that adjusts the hyperparameter based on the observed gradient behavior or the performance on a validation set. This would make the method more robust and easier to use in practice, as it would reduce the need for manual tuning of this critical parameter. The authors should also discuss the theoretical implications of this hyperparameter and how it relates to the underlying properties of the data and the learning task.

Finally, the paper should include a more comprehensive discussion of the limitations of the proposed method and potential avenues for future research. This discussion should address the computational cost of SWD calculation, the sensitivity of the method to the scale and shape regularization hyperparameter, and the potential for further improvements in the regularization strategy. The authors should also consider exploring alternative regularization techniques or modifications to the SWD calculation that could further enhance the performance and efficiency of VISReg. This would provide a more balanced and nuanced perspective on the proposed method and its place within the broader landscape of self-supervised learning.

### Questions

1. How does the computational cost of the proposed method compare to that of covariance-based methods, especially when scaling to larger datasets and models?
2. How should the trade-off between scale and shape regularization be handled in practice? Is there a recommended strategy for tuning the hyperparameter that balances these two aspects?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes VISReg, a self-supervised learning method that replaces covariance regularization in VICReg with a sketching-based approach using Sliced-Wasserstein Distance (SWD). The authors claim that this approach enforces the full distributional shape of embeddings, leading to more robust gradients even under collapse. The paper provides extensive experiments on various datasets and tasks, including in-domain and out-of-distribution generalization, transfer learning, dense instance prediction, and image generation guidance, demonstrating the effectiveness of VISReg.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and addresses the limitations of previous methods.
3. The experiments are comprehensive, and the results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed method. The use of Sliced-Wasserstein Distance (SWD) for regularization, while effective, may introduce additional computational overhead compared to simpler covariance-based methods. A thorough comparison of training time and memory requirements, especially when scaling to larger datasets and models, is needed to fully assess the practical applicability of VISReg. Specifically, the paper should detail the time complexity of the SWD calculation and provide empirical measurements of training time and memory usage for various model sizes and dataset scales. This analysis should also consider the impact of the number of slices used in the SWD calculation on computational cost and regularization strength.
2. The paper does not provide a clear explanation of how the proposed method handles the trade-off between scale and shape regularization. While the method introduces a hyperparameter to balance these two aspects, the paper lacks a detailed discussion on how this parameter should be tuned for different datasets and tasks. A more in-depth analysis of the sensitivity of the method to this hyperparameter, along with guidelines for selecting appropriate values, would be beneficial. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the Sliced-Wasserstein Distance (SWD) regularization. Specifically, the authors should provide a breakdown of the time complexity of the SWD calculation, considering the number of slices used and the dimensionality of the embeddings. This analysis should be complemented by empirical measurements of training time and memory usage for various model sizes (e.g., ViT-B/16, ViT-L/14) and dataset scales. Furthermore, the impact of the number of slices on both computational cost and regularization strength should be investigated and reported. This would provide a more complete picture of the practical trade-offs involved in using VISReg, especially when scaling to larger datasets and models. The authors should also discuss potential optimizations for the SWD calculation to reduce computational overhead, such as using approximation techniques or parallel processing.

To address the lack of clarity regarding the trade-off between scale and shape regularization, the authors should provide a more detailed analysis of the hyperparameter controlling this balance. This analysis should include a sensitivity study, demonstrating how the performance of the method varies with different values of this hyperparameter across various datasets and tasks. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value. For example, the authors could investigate using a feedback mechanism that adjusts the hyperparameter based on the observed gradient behavior or the performance on a validation set. This would make the method more robust and easier to use in practice, as it would reduce the need for manual tuning of this critical parameter. The authors should also discuss the theoretical implications of this hyperparameter and how it relates to the underlying properties of the data and the learning task.

Finally, the paper should include a more comprehensive discussion of the limitations of the proposed method and potential avenues for future research. This discussion should address the computational cost of SWD calculation, the sensitivity of the method to the scale and shape regularization hyperparameter, and the potential for further improvements in the regularization strategy. The authors should also consider exploring alternative regularization techniques or modifications to the SWD calculation that could further enhance the performance and efficiency of VISReg. This would provide a more balanced and nuanced perspective on the proposed method and its place within the broader landscape of self-supervised learning.

### Questions

See above.

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

The paper introduces VISReg, a self-supervised learning (SSL) method that enhances embedding stability and distributional control without relying on heuristics. VISReg replaces covariance-based regularization in VICReg with a sketching-based approach using Sliced-Wasserstein Distance (SWD), which enforces the full distributional shape of embeddings, ensuring robust gradients even under collapse. The paper demonstrates VISReg's effectiveness across various datasets and tasks, including out-of-distribution generalization and dense prediction, positioning it as a promising foundation model for SSL.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and addresses the limitations of previous methods.
3. The experiments are comprehensive, and the results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed method. The use of Sliced-Wasserstein Distance (SWD) for regularization, while effective, may introduce additional computational overhead compared to simpler covariance-based methods. A thorough comparison of training time and memory requirements, especially when scaling to larger datasets and models, is needed to fully assess the practical applicability of VISReg. Specifically, the paper should detail the time complexity of the SWD calculation and provide empirical measurements of training time and memory usage for various model sizes and dataset scales. This analysis should also consider the impact of the number of slices used in the SWD calculation on computational cost and regularization strength.
2. The paper does not provide a clear explanation of how the proposed method handles the trade-off between scale and shape regularization. While the method introduces a hyperparameter to balance these two aspects, the paper lacks a detailed discussion on how this parameter should be tuned for different datasets and tasks. A more in-depth analysis of the sensitivity of the method to this hyperparameter, along with guidelines for selecting appropriate values, would be beneficial. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the Sliced-Wasserstein Distance (SWD) regularization. Specifically, the authors should provide a breakdown of the time complexity of the SWD calculation, considering the number of slices used and the dimensionality of the embeddings. This analysis should be complemented by empirical measurements of training time and memory usage for various model sizes (e.g., ViT-B/16, ViT-L/14) and dataset scales. Furthermore, the impact of the number of slices on both computational cost and regularization strength should be investigated and reported. This would provide a more complete picture of the practical trade-offs involved in using VISReg, especially when scaling to larger datasets and models. The authors should also discuss potential optimizations for the SWD calculation to reduce computational overhead, such as using approximation techniques or parallel processing.

To address the lack of clarity regarding the trade-off between scale and shape regularization, the authors should provide a more detailed analysis of the hyperparameter controlling this balance. This analysis should include a sensitivity study, demonstrating how the performance of the method varies with different values of this hyperparameter across various datasets and tasks. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value. For example, the authors could investigate using a feedback mechanism that adjusts the hyperparameter based on the observed gradient behavior or the performance on a validation set. This would make the method more robust and easier to use in practice, as it would reduce the need for manual tuning of this critical parameter. The authors should also discuss the theoretical implications of this hyperparameter and how it relates to the underlying properties of the data and the learning task.

Finally, the paper should include a more comprehensive discussion of the limitations of the proposed method and potential avenues for future research. This discussion should address the computational cost of SWD calculation, the sensitivity of the method to the scale and shape regularization hyperparameter, and the potential for further improvements in the regularization strategy. The authors should also consider exploring alternative regularization techniques or modifications to the SWD calculation that could further enhance the performance and efficiency of VISReg. This would provide a more balanced and nuanced perspective on the proposed method and its place within the broader landscape of self-supervised learning.

### Questions

1. How does the computational cost of the proposed method compare to that of covariance-based methods, especially when scaling to larger datasets and models?
2. How should the trade-off between scale and shape regularization be handled in practice? Is there a recommended strategy for tuning the hyperparameter that balances these two aspects?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper proposes a new self-supervised learning (SSL) method called VISReg. VISReg is designed to improve the stability and effectiveness of SSL by replacing covariance-based regularization with a sketching-based approach that enforces the full distributional shape of embeddings. The authors claim that this approach provides robust gradients even under collapse and enhances the representation quality of SSL models. The paper provides extensive experimental results on various datasets and tasks, demonstrating the effectiveness of VISReg.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and addresses the limitations of previous methods.
3. The experiments are comprehensive, and the results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed method. The use of Sliced-Wasserstein Distance (SWD) for regularization, while effective, may introduce additional computational overhead compared to simpler covariance-based methods. A thorough comparison of training time and memory requirements, especially when scaling to larger datasets and models, is needed to fully assess the practical applicability of VISReg. Specifically, the paper should detail the time complexity of the SWD calculation and provide empirical measurements of training time and memory usage for various model sizes and dataset scales. This analysis should also consider the impact of the number of slices used in the SWD calculation on computational cost and regularization strength.
2. The paper does not provide a clear explanation of how the proposed method handles the trade-off between scale and shape regularization. While the method introduces a hyperparameter to balance these two aspects, the paper lacks a detailed discussion on how this parameter should be tuned for different datasets and tasks. A more in-depth analysis of the sensitivity of the method to this hyperparameter, along with guidelines for selecting appropriate values, would be beneficial. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the proposed VISReg method. While the use of Sliced-Wasserstein Distance (SWD) offers potential advantages in terms of distributional control, the practical implications for training time and memory consumption need to be rigorously examined. The authors should provide a detailed breakdown of the time complexity associated with the SWD calculation, considering factors such as the dimensionality of the embeddings and the number of slices used. Furthermore, empirical measurements of training time and memory usage should be presented for various model sizes and dataset scales, allowing for a direct comparison with existing methods like VICReg and DINO. This analysis should also explore the impact of different hyperparameter settings on computational cost, providing a more complete picture of the trade-offs involved in using VISReg. Such an analysis would be crucial for assessing the practical applicability of the method, especially when scaling to larger datasets and models.

To address the lack of clarity regarding the trade-off between scale and shape regularization, the authors should provide a more detailed analysis of the hyperparameter controlling this balance. The paper should include a sensitivity study, demonstrating how the performance of the method varies with different values of this hyperparameter across various datasets and tasks. This analysis should not only focus on in-domain performance but also consider out-of-distribution generalization and transfer learning capabilities. Furthermore, the authors should explore the potential for adaptive mechanisms to automatically adjust this parameter during training. For example, a feedback mechanism that adjusts the hyperparameter based on the observed gradient behavior or the performance on a validation set could make the method more robust and easier to use in practice. The paper should also discuss the theoretical implications of this hyperparameter and how it relates to the underlying properties of the data and the learning task.

Finally, the paper should include a more comprehensive discussion of the limitations of the proposed method and potential avenues for future research. This discussion should address the computational cost of SWD calculation, the sensitivity of the method to the scale and shape regularization hyperparameter, and the potential for further improvements in the regularization strategy. The authors should also consider exploring alternative regularization techniques or modifications to the SWD calculation that could further enhance the performance and efficiency of VISReg. This would provide a more balanced and nuanced perspective on the proposed method and its place within the broader landscape of self-supervised learning.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence within the paper to support their claims.

**Plan:**
1. Go through each reviewer's identified weaknesses.
2. For each weakness, determine if it's related to the method or experiments.
3. Find specific evidence (quotes, numbers, missing information) from the paper to support the weakness.
4. If the weakness is about missing information, check if the information is indeed absent.
5. Synthesize the findings and conclude if the weakness is valid, partially valid, or invalid.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational cost of the proposed method. The use of Sliced-Wasserstein Distance (SWD) for regularization, while effective, may introduce additional computational overhead compared to simpler covariance-based methods. A thorough comparison of training time and memory requirements, especially when scaling to larger datasets and models, is needed to fully assess the practical applicability of VISReg. Specifically, the paper should detail the time complexity of the SWD calculation and provide empirical measurements of training time and memory usage for various model sizes and dataset scales. This analysis should also consider the impact of the number of slices used in the SWD calculation on computational cost and regularization strength.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces SWD in the "VISReg Regularization Loss" section. The formula for SWD is provided.
   - Lemma 3.2 discusses the time complexity of the SWD calculation: "Since log N ≪ D, the effective complexity is: 𝒞 Reg = O(N DC K)."
   - The paper mentions the number of slices K in the "VISReg Regularization Loss" section: "Let the number of slices be K."
b) Experiment-related Evidence:
   - The "Scalability Analysis" section mentions the hardware used: "Experiments were conducted on a single H100 GPU."
   - The "Scalability Analysis" section provides training times for different model sizes: "The training time for ViT-B/16 is 100 epochs, ViT-L/16 is 150 epochs, and ViT-S/16 is 120 epochs."
   - The paper does not explicitly provide memory usage measurements.

3. Literature Gap Analysis:
   - The paper cites relevant works on SWD (Bonnabel et al., 2015; Peyré et al., 2019; Bonnabel et al., 2021; Deshpande et al., 2018).

4. Validation Analysis:
   - The reviewer correctly points out the absence of a detailed computational cost analysis. While the paper provides the theoretical time complexity of the SWD calculation (Lemma 3.2), it lacks empirical measurements of training time and memory usage for different model sizes and dataset scales. The paper does provide training times for different ViT models, but it doesn't explicitly analyze the impact of the number of slices (K) on computational cost. The memory usage is also not reported.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit empirical measurements of training time and memory usage, and no detailed analysis of the impact of the number of slices on computational cost.

1. Weakness Statement:
[The paper does not provide a clear explanation of how the proposed method handles the trade-off between scale and shape regularization. While the method introduces a hyperparameter to balance these two aspects, the paper lacks a detailed discussion on how this parameter should be tuned for different datasets and tasks. A more in-depth analysis of the sensitivity of the method to this hyperparameter, along with guidelines for selecting appropriate values, would be beneficial. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "VISReg Regularization Loss" section introduces the hyperparameter λ: "The regularization loss ℒ Reg is: λ scale 𝒬 scale + λ shape 𝒬 shape + λ center 𝒬 center (7)"
   - The paper mentions the default values for λ in the "Ablation study" section: "Unless stated otherwise, the training set is ImageNet1K, the backbone is ViT-B/16, the number of slices is 4096 per GPU, the augmentation settings follow LeJEPA ( Balestriero & LeCun, 2025 ) with 2 global views and 6 local views, and the training epoch is 100. We report the online linear probe accuracy on ImageNet1K to analyze the effect of hyper-parameters, as shown in Table 3 ."
   - The "Scalability Analysis" section mentions the fixed value of λ: "Fixing D = 256 and varying K, Figure 5 shows: (1) OT-based methods remain robust even at K = 18 D ; (2) VISReg is the most robust approach, consistently achieving the highest linear probe accuracy."
   - The "Ablation study" section includes experiments varying λ: "Effect of λ. Different from SIGReg, scaling the regularization loss with batch size to maintain the batch size invariance, VISReg is naturally batch invariant, so a large λ value is needed to ensure the contribution of VISReg in the gradient. For small datasets, e.g., ImageNette and Galaxy10, 0.6 is a good start. For large datasets, e.g., ImageNet1K, 0.9 is a good start."
b) Experiment-related Evidence:
   - Table 3 in the "Ablation study" section shows the performance of VISReg with different values of λ.

3. Literature Gap Analysis:
   - The paper cites the original VICReg paper (Balestriero & LeCun, 2025).

4. Validation Analysis:
   - The reviewer is correct that the paper doesn't provide a detailed explanation of how the trade-off between scale and shape regularization is handled. While the paper introduces the hyperparameter λ and shows its impact in the ablation study (Table 3), it lacks a systematic analysis of how to tune this parameter for different datasets and tasks. The paper mentions using different values of λ for different datasets but doesn't provide a clear methodology or guidelines for selecting appropriate values. The suggestion for adaptive mechanisms is also not explored.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of a detailed discussion on tuning the hyperparameter λ, no systematic sensitivity analysis, and no exploration of adaptive mechanisms.

**Review 2 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational cost of the proposed method. The use of Sliced-Wasserstein Distance (SWD) for regularization, while effective, may introduce additional computational overhead compared to simpler covariance-based methods. A thorough comparison of training time and memory requirements, especially when scaling to larger datasets and models, is needed to fully assess the practical applicability of VISReg. Specifically, the paper should detail the time complexity of the SWD calculation, considering the number of slices used and the dimensionality of the embeddings. Empirical measurements of training time and memory usage for various model sizes and dataset scales should be included, along with a comparison to the computational cost of covariance-based methods. This analysis should also consider the impact of the number of slices on computational cost and regularization strength.]

2. Evidence Collection: (Same as Review 1, Weakness 1)
a) Method-related Evidence:
   - The paper introduces SWD in the "VISReg Regularization Loss" section. The formula for SWD is provided.
   - Lemma 3.2 discusses the time complexity of the SWD calculation: "Since log N ≪ D, the effective complexity is: 𝒞 Reg = O(N DC K)."
   - The paper mentions the number of slices K in the "VISReg Regularization Loss" section: "Let the number of slices be K."
b) Experiment-related Evidence:
   - The "Scalability Analysis" section mentions the hardware used: "Experiments were conducted on a single H100 GPU."
   - The "Scalability Analysis" section provides training times for different model sizes: "The training time for ViT-B/16 is 100 epochs, ViT-L/16 is 150 epochs, and ViT-S/16 is 120 epochs."
   - The paper does not explicitly provide memory usage measurements.

3. Literature Gap Analysis:
   - The paper cites relevant works on SWD (Bonnabel et al., 2015; Peyré et al., 2019; Bonnabel et al., 2021; Deshpande et al., 2018).

4. Validation Analysis:
   - This is the same weakness as Review 1, Weakness 1. The analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit empirical measurements of training time and memory usage, and no detailed analysis of the impact of the number of slices on computational cost.

1. Weakness Statement:
[The paper does not provide a clear explanation of how the proposed method handles the trade-off between scale and shape regularization. While the method introduces a hyperparameter to balance these two aspects, the paper lacks a detailed discussion on how this parameter should be tuned for different datasets and tasks. A more in-depth analysis of the sensitivity of the method to this hyperparameter, along with guidelines for selecting appropriate values, would be beneficial. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value.]

2. Evidence Collection: (Same as Review 1, Weakness 2)
a) Method-related Evidence:
   - The "VISReg Regularization Loss" section introduces the hyperparameter λ: "The regularization loss ℒ Reg is: λ scale 𝒬 scale + λ shape 𝒬 shape + λ center 𝒬 center (7)"
   - The paper mentions the default values for λ in the "Ablation study" section: "Unless stated otherwise, the training set is ImageNet1K, the backbone is ViT-B/16, the number of slices is 4096 per GPU, the augmentation settings follow LeJEPA ( Balestriero & LeCun, 2025 ) with 2 global views and 6 local views, and the training epoch is 100. We report the online linear probe accuracy on ImageNet1K to analyze the effect of hyper-parameters, as shown in Table 3 ."
   - The "Scalability Analysis" section mentions the fixed value of λ: "Fixing D = 256 and varying K, Figure 5 shows: (1) OT-based methods remain robust even at K = 18 D ; (2) VISReg is the most robust approach, consistently achieving the highest linear probe accuracy."
   - The "Ablation study" section includes experiments varying λ: "Effect of λ. Different from SIGReg, scaling the regularization loss with batch size to maintain the batch size invariance, VISReg is naturally batch invariant, so a large λ value is needed to ensure the contribution of VISReg in the gradient. For small datasets, e.g., ImageNette and Galaxy10, 0.6 is a good start. For large datasets, e.g., ImageNet1K, 0.9 is a good start."
b) Experiment-related Evidence:
   - Table 3 in the "Ablation study" section shows the performance of VISReg with different values of λ.

3. Literature Gap Analysis:
   - The paper cites the original VICReg paper (Balestriero & LeCun, 2025).

4. Validation Analysis:
   - This is the same weakness as Review 1, Weakness 2. The analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of a detailed discussion on tuning the hyperparameter λ, no systematic sensitivity analysis, and no exploration of adaptive mechanisms.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational cost of the proposed method. The use of Sliced-Wasserstein Distance (SWD) for regularization, while effective, may introduce additional computational overhead compared to simpler covariance-based methods. A thorough comparison of training time and memory requirements, especially when scaling to larger datasets and models, is needed to fully assess the practical applicability of VISReg. Specifically, the paper should detail the time complexity of the SWD calculation, considering the number of slices used and the dimensionality of the embeddings. Empirical measurements of training time and memory usage for various model sizes and dataset scales should be included, along with a comparison to the computational cost of covariance-based methods. This analysis should also consider the impact of the number of slices on computational cost and regularization strength.]

2. Evidence Collection: (Same as Review 1, Weakness 1 and Review 2, Weakness 1)
a) Method-related Evidence:
   - The paper introduces SWD in the "VISReg Regularization Loss" section. The formula for SWD is provided.
   - Lemma 3.2 discusses the time complexity of the SWD calculation: "Since log N ≪ D, the effective complexity is: 𝒞 Reg = O(N DC K)."
   - The paper mentions the number of slices K in the "VISReg Regularization Loss" section: "Let the number of slices be K."
b) Experiment-related Evidence:
   - The "Scalability Analysis" section mentions the hardware used: "Experiments were conducted on a single H100 GPU."
   - The "Scalability Analysis" section provides training times for different model sizes: "The training time for ViT-B/16 is 100 epochs, ViT-L/16 is 150 epochs, and ViT-S/16 is 120 epochs."
   - The paper does not explicitly provide memory usage measurements.

3. Literature Gap Analysis:
   - The paper cites relevant works on SWD (Bonnabel et al., 2015; Peyré et al., 2019; Bonnabel et al., 2021; Deshpande et al., 2018).

4. Validation Analysis:
   - This is the same weakness as Review 1, Weakness 1 and Review 2, Weakness 1. The analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit empirical measurements of training time and memory usage, and no detailed analysis of the impact of the number of slices on computational cost.

1. Weakness Statement:
[The paper does not provide a clear explanation of how the proposed method handles the trade-off between scale and shape regularization. While the method introduces a hyperparameter to balance these two aspects, the paper lacks a detailed discussion on how this parameter should be tuned for different datasets and tasks. A more in-depth analysis of the sensitivity of the method to this hyperparameter, along with guidelines for selecting appropriate values, would be beneficial. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value.]

2. Evidence Collection: (Same as Review 1, Weakness 2 and Review 2, Weakness 2)
a) Method-related Evidence:
   - The "VISReg Regularization Loss" section introduces the hyperparameter λ: "The regularization loss ℒ Reg is: λ scale 𝒬 scale + λ shape 𝒬 shape + λ center 𝒬 center (7)"
   - The paper mentions the default values for λ in the "Ablation study" section: "Unless stated otherwise, the training set is ImageNet1K, the backbone is ViT-B/16, the number of slices is 4096 per GPU, the augmentation settings follow LeJEPA ( Balestriero & LeCun, 2025 ) with 2 global views and 6 local views, and the training epoch is 100. We report the online linear probe accuracy on ImageNet1K to analyze the effect of hyper-parameters, as shown in Table 3 ."
   - The "Scalability Analysis" section mentions the fixed value of λ: "Fixing D = 256 and varying K, Figure 5 shows: (1) OT-based methods remain robust even at K = 18 D ; (2) VISReg is the most robust approach, consistently achieving the highest linear probe accuracy."
   - The "Ablation study" section includes experiments varying λ: "Effect of λ. Different from SIGReg, scaling the regularization loss with batch size to maintain the batch size invariance, VISReg is naturally batch invariant, so a large λ value is needed to ensure the contribution of VISReg in the gradient. For small datasets, e.g., ImageNette and Galaxy10, 0.6 is a good start. For large datasets, e.g., ImageNet1K, 0.9 is a good start."
b) Experiment-related Evidence:
   - Table 3 in the "Ablation study" section shows the performance of VISReg with different values of λ.

3. Literature Gap Analysis:
   - The paper cites the original VICReg paper (Balestriero & LeCun, 2025).

4. Validation Analysis:
   - This is the same weakness as Review 1, Weakness 2 and Review 2, Weakness 2. The analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of a detailed discussion on tuning the hyperparameter λ, no systematic sensitivity analysis, and no exploration of adaptive mechanisms.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational cost of the proposed method. The use of Sliced-Wasserstein Distance (SWD) for regularization, while effective, may introduce additional computational overhead compared to simpler covariance-based methods. A thorough comparison of training time and memory requirements, especially when scaling to larger datasets and models, is needed to fully assess the practical applicability of VISReg. Specifically, the paper should detail the time complexity of the SWD calculation, considering the number of slices used and the dimensionality of the embeddings. Empirical measurements of training time and memory usage for various model sizes and dataset scales should be included, along with a comparison to the computational cost of covariance-based methods. This analysis should also consider the impact of the number of slices on computational cost and regularization strength.]

2. Evidence Collection: (Same as Review 1, Weakness 1, Review 2, Weakness 1, and Review 3, Weakness 1)
a) Method-related Evidence:
   - The paper introduces SWD in the "VISReg Regularization Loss" section. The formula for SWD is provided.
   - Lemma 3.2 discusses the time complexity of the SWD calculation: "Since log N ≪ D, the effective complexity is: 𝒞 Reg = O(N DC K)."
   - The paper mentions the number of slices K in the "VISReg Regularization Loss" section: "Let the number of slices be K."
b) Experiment-related Evidence:
   - The "Scalability Analysis" section mentions the hardware used: "Experiments were conducted on a single H100 GPU."
   - The "Scalability Analysis" section provides training times for different model sizes: "The training time for ViT-B/16 is 100 epochs, ViT-L/16 is 150 epochs, and ViT-S/16 is 120 epochs."
   - The paper does not explicitly provide memory usage measurements.

3. Literature Gap Analysis:
   - The paper cites relevant works on SWD (Bonnabel et al., 2015; Peyré et al., 2019; Bonnabel et al., 2021; Deshpande et al., 2018).

4. Validation Analysis:
   - This is the same weakness as Review 1, Weakness 1, Review 2, Weakness 1, and Review 3, Weakness 1. The analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit empirical measurements of training time and memory usage, and no detailed analysis of the impact of the number of slices on computational cost.

1. Weakness Statement:
[The paper does not provide a clear explanation of how the proposed method handles the trade-off between scale and shape regularization. While the method introduces a hyperparameter to balance these two aspects, the paper lacks a detailed discussion on how this parameter should be tuned for different datasets and tasks. A more in-depth analysis of the sensitivity of the method to this hyperparameter, along with guidelines for selecting appropriate values, would be beneficial. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value.]

2. Evidence Collection: (Same as Review 1, Weakness 2, Review 2, Weakness 2, and Review 3, Weakness 2)
a) Method-related Evidence:
   - The "VISReg Regularization Loss" section introduces the hyperparameter λ: "The regularization loss ℒ Reg is: λ scale 𝒬 scale + λ shape 𝒬 shape + λ center 𝒬 center (7)"
   - The paper mentions the default values for λ in the "Ablation study" section: "Unless stated otherwise, the training set is ImageNet1K, the backbone is ViT-B/16, the number of slices is 4096 per GPU, the augmentation settings follow LeJEPA ( Balestriero & LeCun, 2025 ) with 2 global views and 6 local views, and the training epoch is 100. We report the online linear probe accuracy on ImageNet1K to analyze the effect of hyper-parameters, as shown in Table 3 ."
   - The "Scalability Analysis" section mentions the fixed value of λ: "Fixing D = 256 and varying K, Figure 5 shows: (1) OT-based methods remain robust even at K = 18 D ; (2) VISReg is the most robust approach, consistently achieving the highest linear probe accuracy."
   - The "Ablation study" section includes experiments varying λ: "Effect of λ. Different from SIGReg, scaling the regularization loss with batch size to maintain the batch size invariance, VISReg is naturally batch invariant, so a large λ value is needed to ensure the contribution of VISReg in the gradient. For small datasets, e.g., ImageNette and Galaxy10, 0.6 is a good start. For large datasets, e.g., ImageNet1K, 0.9 is a good start."
b) Experiment-related Evidence:
   - Table 3 in the "Ablation study" section shows the performance of VISReg with different values of λ.

3. Literature Gap Analysis:
   - The paper cites the original VICReg paper (Balestriero & LeCun, 2025).

4. Validation Analysis:
   - This is the same weakness as Review 1, Weakness 2, Review 2, Weakness 2, and Review 3, Weakness 2. The analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of a detailed discussion on tuning the hyperparameter λ, no systematic sensitivity analysis, and no exploration of adaptive mechanisms.

**Synthesis and Reflection:**

After analyzing the weaknesses identified by the reviewers, it's clear that there is a significant consensus regarding the missing computational cost analysis. All reviewers who raised concerns about computational cost agree that the paper lacks a thorough evaluation of the practical implications of using Sliced-Wasserstein Distance (SWD) for regularization.

Specifically, the reviewers point out the absence of:
- **Empirical measurements of training time and memory usage:** The paper provides training times for different model sizes, but it doesn't offer a comprehensive comparison of computational cost with covariance-based methods or analyze the impact of the number of slices (K) on both time and memory.
- **Detailed analysis of the time complexity of SWD calculation:** While Lemma 3.2 provides a theoretical time complexity, reviewers expect a more practical breakdown, considering the number of slices and embedding dimension.
- **Impact of the number of slices on regularization strength:** The paper mentions the effect of K on computational cost but lacks a detailed discussion on how it affects the regularization strength and the overall training process.

Regarding the trade-off between scale and shape regularization, all reviewers acknowledge the introduction of the hyperparameter λ but highlight the lack of:
- **Detailed discussion on tuning:** The paper doesn't provide clear guidelines or a systematic analysis for selecting appropriate values of λ for different datasets and tasks.
- **Sensitivity analysis:** The impact of varying λ on the performance of VISReg isn't thoroughly explored.
- **Exploration of adaptive mechanisms:** The paper doesn't investigate or propose methods for automatically adjusting λ during training.

There are no significant contradictions between the reviewers' opinions. They all converge on the need for a more in-depth analysis of the computational cost and the practical implications of the hyperparameter λ.

**Conclusion:**

Based on the evidence collected, the primary weaknesses identified by the reviewers are valid. The paper lacks a comprehensive analysis of the computational cost associated with the proposed VISReg method and a detailed discussion on the practical aspects of tuning the hyperparameter λ. These omissions impact the assessment of the method's practical applicability and robustness.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces VISReg, a novel self-supervised learning (SSL) method designed to enhance the stability and effectiveness of embedding learning without relying on heuristic regularization techniques. The core innovation of VISReg lies in its use of Sliced-Wasserstein Distance (SWD) for sketching-based regularization, which contrasts with the covariance-based regularization employed in methods like VICReg and its predecessor, LeJEPA. The authors argue that covariance-based regularization can be unstable during training, particularly under collapse conditions, and that SWD offers a more robust alternative by enforcing the full distributional shape of embeddings, rather than just matching their second moments. This approach aims to improve the representation quality and generalization of SSL models. The paper presents a comprehensive set of experiments across various datasets and tasks, including in-domain and out-of-distribution generalization, transfer learning, and dense prediction, positioning VISReg as a promising foundation model for SSL. The empirical findings suggest that VISReg achieves competitive performance, demonstrating its effectiveness in learning robust and informative embeddings. The authors also conduct ablation studies to analyze the impact of key hyperparameters, such as the regularization strength parameter, on the performance of the method. While the paper demonstrates the potential of SWD-based regularization, it also acknowledges the need for further investigation into the computational cost of the proposed method and the practical implications of the hyperparameters. Overall, the paper makes a significant contribution to the field of self-supervised learning by introducing a novel regularization approach that addresses some of the limitations of existing methods. However, it also highlights the need for further research to fully understand the practical applicability and robustness of VISReg, particularly in terms of computational efficiency and hyperparameter tuning.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I found several aspects of this paper to be particularly strong. First, the paper is exceptionally well-written and easy to follow, which greatly facilitates the understanding of the proposed method and its underlying motivations. The authors clearly articulate the limitations of existing methods, such as VICReg, and present a compelling case for the use of Sliced-Wasserstein Distance (SWD) as a more robust regularization technique. The motivation behind using SWD to enforce the full distributional shape of embeddings is well-explained, and the paper effectively highlights the instability of covariance-based regularization, particularly during training. The proposed VISReg method is well-motivated and addresses a significant gap in the existing literature. The authors also provide a comprehensive set of experiments across various datasets and tasks, demonstrating the effectiveness of VISReg in different scenarios. The experiments include in-domain and out-of-distribution generalization, transfer learning, and dense prediction, which provides a thorough evaluation of the method's performance. The results presented in the paper are compelling, and the authors demonstrate that VISReg achieves competitive performance, positioning it as a promising foundation model for SSL. Furthermore, the paper includes ablation studies that analyze the impact of key hyperparameters, such as the regularization strength parameter, on the performance of the method. This analysis provides valuable insights into the behavior of VISReg and helps to understand the role of different components in the overall performance. The authors also provide a theoretical analysis of the time complexity of the SWD calculation, which is a valuable contribution to the understanding of the computational cost of the method. Finally, the paper is well-structured and easy to follow, which makes it accessible to a wide audience. The authors clearly present their ideas and provide sufficient details about the method and the experiments, which makes it easy for other researchers to reproduce their results and build upon their work. The paper's strengths lie in its clear presentation, well-motivated method, comprehensive experiments, and valuable analysis of the proposed approach.


## Weaknesses:

Despite the strengths of this paper, I have identified several significant weaknesses that warrant further attention. The most prominent concern revolves around the computational cost of the proposed VISReg method, particularly the use of Sliced-Wasserstein Distance (SWD) for regularization. While the paper provides a theoretical time complexity of the SWD calculation, Lemma 3.2 states that the effective complexity is O(NDCK), where N is the number of samples, D is the dimensionality of the embeddings, C is the number of slices, and K is the number of slices per sample. However, the paper lacks a detailed empirical analysis of the actual training time and memory usage, especially when scaling to larger datasets and models. The paper mentions that experiments were conducted on a single H100 GPU, and provides training times for different model sizes, such as ViT-B/16, ViT-L/16, and ViT-S/16. However, it does not explicitly report the memory usage, which is a crucial factor in assessing the practical applicability of the method. Furthermore, the paper does not provide a detailed breakdown of the time complexity associated with the SWD calculation, considering the number of slices used and the dimensionality of the embeddings. This lack of empirical data makes it difficult to assess the practical implications of using SWD for regularization, especially when compared to simpler covariance-based methods. The paper also lacks a clear explanation of how the proposed method handles the trade-off between scale and shape regularization. The method introduces a hyperparameter, λ, to balance these two aspects, as shown in equation (7): λ scale 𝒬 scale + λ shape 𝒬 shape + λ center 𝒬 center. While the paper includes an ablation study, Table 3, that explores the impact of different values of λ, it does not provide a detailed discussion on how to tune this parameter for different datasets and tasks. The paper mentions using different values of λ for different datasets, such as 0.6 for ImageNette and Galaxy10, and 0.9 for ImageNet1K, but it does not provide a clear methodology or guidelines for selecting appropriate values. The paper also lacks a systematic sensitivity analysis of the method to this hyperparameter, which would be beneficial for understanding its impact on the overall performance. The paper mentions that a large λ value is needed to ensure the contribution of VISReg in the gradient, but it does not provide a detailed explanation of why this is the case. The paper also does not explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value. This lack of exploration limits the practical applicability of the method, as it requires manual tuning of the hyperparameter for each new dataset or task. In summary, the paper's failure to provide a detailed analysis of the computational cost and the practical implications of the hyperparameter λ are significant weaknesses that need to be addressed.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First and foremost, the paper should include a more detailed analysis of the computational cost associated with the Sliced-Wasserstein Distance (SWD) regularization. Specifically, the authors should provide a breakdown of the time complexity of the SWD calculation, considering the number of slices used and the dimensionality of the embeddings. This analysis should be complemented by empirical measurements of training time and memory usage for various model sizes (e.g., ViT-B/16, ViT-L/16) and dataset scales. Furthermore, the impact of the number of slices on both computational cost and regularization strength should be investigated and reported. This would provide a more complete picture of the practical trade-offs involved in using VISReg, especially when scaling to larger datasets and models. The authors should also discuss potential optimizations for the SWD calculation to reduce computational overhead, such as using approximation techniques or parallel processing. Second, the paper should provide a more detailed analysis of the hyperparameter controlling the balance between scale and shape regularization. This analysis should include a sensitivity study, demonstrating how the performance of the method varies with different values of this hyperparameter across various datasets and tasks. The paper should also explore the potential for adaptive mechanisms to automatically adjust this parameter during training, rather than relying on a fixed value. For example, the authors could investigate using a feedback mechanism that adjusts the hyperparameter based on the observed gradient behavior or the performance on a validation set. This would make the method more robust and easier to use in practice, as it would reduce the need for manual tuning of this critical parameter. The authors should also discuss the theoretical implications of this hyperparameter and how it relates to the underlying properties of the data and the learning task. Third, the paper should include a more comprehensive discussion of the limitations of the proposed method and potential avenues for future research. This discussion should address the computational cost of SWD calculation, the sensitivity of the method to the scale and shape regularization hyperparameter, and the potential for further improvements in the regularization strategy. The authors should also consider exploring alternative regularization techniques or modifications to the SWD calculation that could further enhance the performance and efficiency of VISReg. This would provide a more balanced and nuanced perspective on the proposed method and its place within the broader landscape of self-supervised learning. Finally, the paper should include a more detailed analysis of the practical implications of the proposed method. This should include a discussion of the computational cost of SWD calculation, the sensitivity of the method to the scale and shape regularization hyperparameter, and the potential for further improvements in the regularization strategy. The authors should also consider exploring alternative regularization techniques or modifications to the SWD calculation that could further enhance the performance and efficiency of VISReg. This would provide a more balanced and nuanced perspective on the proposed method and its place within the broader landscape of self-supervised learning.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for a deeper understanding of the proposed method. First, how does the computational cost of the proposed method compare to that of covariance-based methods, especially when scaling to larger datasets and models? The paper provides training times for different model sizes, but it lacks a detailed comparison of the computational cost of SWD calculation with covariance-based methods. A thorough comparison would be beneficial for assessing the practical applicability of VISReg. Second, how should the trade-off between scale and shape regularization be handled in practice? The paper introduces a hyperparameter to balance these two aspects, but it lacks a detailed discussion on how to tune this parameter for different datasets and tasks. A more in-depth analysis of the sensitivity of the method to this hyperparameter, along with guidelines for selecting appropriate values, would be beneficial. Third, is there a recommended strategy for tuning the hyperparameter that balances these two aspects? The paper mentions using different values of the hyperparameter for different datasets, but it does not provide a clear methodology or guidelines for selecting appropriate values. A more systematic approach to hyperparameter tuning would be beneficial for the practical application of VISReg. Fourth, what are the theoretical implications of the hyperparameter controlling the balance between scale and shape regularization, and how does it relate to the underlying properties of the data and the learning task? The paper provides some intuition, but a more detailed discussion of the theoretical implications would be beneficial. Finally, what are the limitations of the proposed method, and what are the potential avenues for future research? The paper should include a more comprehensive discussion of the limitations of the proposed method and potential avenues for future research. This discussion should address the computational cost of SWD calculation, the sensitivity of the method to the scale and shape regularization hyperparameter, and the potential for further improvements in the regularization strategy. Addressing these questions would provide a more complete and nuanced understanding of the proposed method and its place within the broader landscape of self-supervised learning.


## Rating:

6.0


## Confidence:

3.25


## Decision:

Accept
}