# Review

## Summary
This paper conducts a comparative study on offline reasoning training methods, including SFT, RFT, DFT, RIFT, Offline GRPO, and DPO, by analyzing the weight-space geometry of their training updates. The authors examine the cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA to compare the methods. The results show that reward-weighted methods (SFT, RFT, RIFT) converge in a similar direction, while DPO sits in a near-orthogonal subspace, and Offline GRPO adds a substantial orthogonal component while staying within the SFT loss basin. Notably, DPO achieves the highest accuracy on benchmarks like GSM8K and AIME26.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper provides a novel perspective on comparing offline reasoning training methods by analyzing their weight-space geometry. This approach goes beyond traditional accuracy metrics and offers insights into the mechanisms behind these methods.
- The authors conduct a comprehensive analysis using multiple techniques, including cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. This multi-faceted approach ensures a thorough evaluation of the methods' weight-space properties.
- The study reveals that reward-weighted methods (SFT, RFT, RIFT) converge in a similar direction, indicating that the core mechanisms behind these methods are similar. This finding helps in understanding the effectiveness of these methods and how they can be potentially unified.
- The paper identifies that DPO sits in a near-orthogonal subspace, which suggests that it introduces a fundamentally different mechanism compared to reward-weighted methods. This orthogonality is supported by the highest accuracy achieved by DPO on benchmarks like GSM8K and AIME26, indicating that its distinct weight-space geometry contributes to its superior performance.
- The study also shows that Offline GRPO adds a substantial orthogonal component while staying within the SFT loss basin. This finding suggests that Offline GRPO leverages additional information not captured by reward-weighted methods, which could be a valuable insight for future research.

## Weaknesses
- The study is limited to a single domain and a specific model architecture (Qwen3-4B). This may restrict the generalizability of the findings to other domains and model architectures. It would be beneficial to include experiments across different domains and model sizes to validate the robustness of the results.
- The paper only considers attention-only LoRA for the analysis. It would be valuable to extend the analysis to include other types of parameter-efficient fine-tuning methods (e.g., LoRA with MLP) to see if similar patterns emerge.
- The paper does not explore the impact of different hyperparameters on the weight-space geometry. Conducting sensitivity analyses on hyperparameters could provide insights into how they affect the convergence behavior and weight-space properties of the methods.
- The paper does not provide a clear interpretation of the implications of the weight-space geometry on the learning dynamics and generalization capabilities of the methods. While the analysis provides insights into the similarity or differences between methods, it would be helpful to discuss how these geometric properties influence the learning process and the ability of the models to generalize to new tasks.

## Questions
- How do the findings generalize to other domains and model architectures? Have you considered conducting experiments in different domains to validate the robustness of your results?
- How do other types of parameter-efficient fine-tuning methods (e.g., LoRA with MLP) compare in terms of weight-space geometry? Have you considered including them in your analysis?
- How do different hyperparameters affect the weight-space geometry and learning dynamics of the methods? Have you conducted sensitivity analyses on hyperparameters to investigate their impact?
- What are the practical implications of the weight-space geometry on the generalization capabilities of the methods? How do the geometric properties influence the learning process and the ability of the models to acquire new knowledge?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4