I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new method called On-Policy Self-Distillation (OPSD) to improve the reasoning capabilities of large language models (LLMs). The authors claim that OPSD can match or exceed the performance of reinforcement learning methods and supervised fine-tuning while being more sample efficient. The paper evaluates OPSD on three competition-level mathematical reasoning benchmarks and shows that it outperforms existing methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The authors provide a clear motivation for their work and explain the technical details of OPSD in a clear and concise manner. The experimental setup is well-described, and the results are presented in a clear and organized way. The authors also provide a detailed analysis of the experimental results, including ablation studies and comparisons with existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison with existing self-distillation methods. While the authors mention that OPSD is inspired by self-distillation, they do not provide a thorough comparison with other self-distillation techniques, such as those used in knowledge distillation or model compression. This makes it difficult to understand the novelty and advantages of OPSD over existing methods.
2. The paper does not provide a clear explanation of how OPSD addresses the limitations of existing methods. While the authors claim that OPSD is more sample efficient than reinforcement learning methods, they do not provide a detailed analysis of why this is the case. It is not clear how the on-policy approach reduces the need for large amounts of data or how the self-distillation mechanism avoids the issues of sparse rewards and limited exploration in reinforcement learning.
3. The paper does not provide a detailed analysis of the computational cost of OPSD. While the authors claim that OPSD is more sample efficient, they do not provide a detailed analysis of the computational resources required for training and inference. This makes it difficult to assess the practical applicability of OPSD, especially for large-scale models and datasets.
4. The paper does not provide a clear explanation of the choice of hyperparameters. The authors do not provide a detailed analysis of how the hyperparameters were chosen or how they affect the performance of OPSD. This makes it difficult to reproduce the results and to understand the robustness of OPSD to different hyperparameter settings.

### Suggestions

The paper would benefit from a more detailed comparison with existing self-distillation methods. The authors should clearly articulate how OPSD differs from other self-distillation techniques, particularly those used in knowledge distillation and model compression. A thorough analysis should include a discussion of the specific mechanisms used for knowledge transfer, the types of distillation losses employed, and the ways in which these methods handle the challenges of learning from a teacher model. Furthermore, the authors should provide a quantitative comparison of OPSD with these methods, demonstrating the specific advantages of OPSD in terms of performance, sample efficiency, and computational cost. This would help to establish the novelty and significance of the proposed approach.

To address the lack of clarity regarding the limitations of existing methods, the authors should provide a more detailed explanation of how OPSD overcomes the challenges of sparse rewards and limited exploration in reinforcement learning. This should include a discussion of how the on-policy approach reduces the need for large amounts of data and how the self-distillation mechanism avoids the issues of reward sparsity. The authors should also provide a more detailed analysis of the training dynamics of OPSD, including the convergence behavior and the stability of the training process. This would help to demonstrate the effectiveness of OPSD in addressing the limitations of existing methods and provide a more solid foundation for the claims made in the paper. Specifically, the authors should analyze the impact of the on-policy sampling strategy on the learning process, and how it helps to avoid the pitfalls of reinforcement learning.

Finally, the paper needs a more detailed analysis of the computational cost of OPSD. The authors should provide a breakdown of the computational resources required for training and inference, including the memory usage, the training time, and the inference time. This analysis should also include a comparison with existing methods, demonstrating the computational efficiency of OPSD. Furthermore, the authors should provide a detailed explanation of the choice of hyperparameters, including the rationale behind the selection of each hyperparameter and its impact on the performance of OPSD. This should include a sensitivity analysis of the hyperparameters, demonstrating the robustness of OPSD to different hyperparameter settings. The authors should also discuss the potential limitations of OPSD in terms of computational cost and scalability, and suggest potential solutions to address these limitations.

### Questions

1. How does OPSD compare to other self-distillation methods in terms of performance, sample efficiency, and computational cost?
2. How does OPSD address the limitations of existing methods, such as sparse rewards and limited exploration in reinforcement learning?
3. What is the computational cost of OPSD compared to existing methods?
4. How were the hyperparameters chosen, and how do they affect the performance of OPSD?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

The paper introduces On-Policy Self-Distillation (OPSD), a method that enables a single large language model (LLM) to act as both teacher and student, using its own capabilities to improve its reasoning abilities. OPSD leverages ground-truth solutions to provide dense, token-level supervision, addressing limitations of traditional distillation methods that rely on sparse, sequence-level feedback. The authors demonstrate OPSD’s effectiveness on mathematical reasoning benchmarks, achieving superior performance with fewer training samples compared to reinforcement learning methods like GRPO.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective, and the experimental results are convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with OPSD, especially in comparison to other distillation methods. Specifically, the paper does not provide a breakdown of the time and memory requirements for both training and inference, making it difficult to assess the practical applicability of the method, particularly for large-scale models and datasets. A comparison of training time, GPU memory usage, and inference speed against methods like supervised fine-tuning and reinforcement learning would be beneficial.
2. The paper does not explore the sensitivity of OPSD to different hyperparameter settings, such as the weighting of the KL divergence loss or the choice of the privileged information used for distillation. The paper should include a more thorough analysis of how these hyperparameters affect the performance of OPSD, including a discussion of the optimal ranges and the potential for overfitting or underfitting. It is unclear how the method would perform with different choices of privileged information, such as different types of reasoning traces or different levels of ground-truth detail.
3. The paper does not discuss the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The paper should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios.

### Suggestions

To address the lack of computational cost analysis, the authors should include a detailed breakdown of the time and memory requirements for both training and inference of OPSD. This should include a comparison against other distillation methods, such as supervised fine-tuning and reinforcement learning, to provide a clear understanding of the trade-offs involved. The analysis should also consider the impact of different model sizes and dataset sizes on the computational cost of OPSD. Furthermore, the authors should investigate the scalability of OPSD to larger models and datasets, and discuss any potential bottlenecks or limitations that might arise. This analysis should be presented in a clear and concise manner, with tables and figures that allow for easy comparison of the computational costs of different methods.

To address the sensitivity to hyperparameters, the authors should conduct a more thorough analysis of the impact of different hyperparameter settings on the performance of OPSD. This should include a systematic exploration of the optimal ranges for the weighting of the KL divergence loss and the choice of privileged information used for distillation. The authors should also investigate the potential for overfitting or underfitting with different hyperparameter settings, and provide guidelines for selecting appropriate values. This analysis should include a discussion of the trade-offs between different hyperparameter settings, and how these trade-offs might affect the performance of OPSD. The authors should also explore the use of techniques such as grid search or Bayesian optimization to identify the optimal hyperparameter settings for OPSD.

To address the limitations of OPSD in handling more complex reasoning tasks, the authors should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference. This should include a discussion of the modifications that would be necessary to adapt the method to these scenarios, and the potential challenges that might arise. The authors should also explore the use of techniques such as knowledge graphs or external knowledge bases to provide OPSD with the necessary external knowledge. Furthermore, the authors should consider evaluating OPSD on more complex reasoning benchmarks that require multi-step inference or external knowledge, to provide a more comprehensive assessment of its capabilities.

### Questions

See the weaknesses.

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces On-Policy Self-Distillation (OPSD), a novel framework for improving the reasoning capabilities of large language models (LLMs) through self-distillation. The key innovation is enabling a single LLM to act as both teacher and student, using its own reasoning abilities and ground-truth solutions to provide dense, token-level supervision. OPSD employs a per-token pointwise KL clipping mechanism to stabilize training and achieves superior performance on mathematical reasoning benchmarks compared to reinforcement learning methods, with improved token efficiency and reduced training time.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective, and the experimental results are convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with OPSD, especially in comparison to other distillation methods. Specifically, the paper does not provide a breakdown of the time and memory requirements for both training and inference, making it difficult to assess the practical applicability of the method, particularly for large-scale models and datasets. A comparison of training time, GPU memory usage, and inference speed against methods like supervised fine-tuning and reinforcement learning would be beneficial.
2. The paper does not explore the sensitivity of OPSD to different hyperparameter settings, such as the weighting of the KL divergence loss or the choice of the privileged information used for distillation. The paper should include a more thorough analysis of how these hyperparameters affect the performance of OPSD, including a discussion of the optimal ranges and the potential for overfitting or underfitting. It is unclear how the method would perform with different choices of privileged information, such as different types of reasoning traces or different levels of ground-truth detail.
3. The paper does not discuss the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The paper should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios.

### Suggestions

To strengthen the paper, the authors should provide a more detailed analysis of the computational cost of OPSD. This should include a breakdown of the time and memory requirements for both training and inference, comparing OPSD against other distillation methods, such as supervised fine-tuning and reinforcement learning. The analysis should consider the impact of different model sizes and dataset sizes on the computational cost of OPSD. Furthermore, the authors should investigate the scalability of OPSD to larger models and datasets, and discuss any potential bottlenecks or limitations that might arise. This would provide a more comprehensive understanding of the practical applicability of the method.

Additionally, the authors should conduct a more thorough analysis of the sensitivity of OPSD to different hyperparameter settings. This should include a systematic exploration of the optimal ranges for the weighting of the KL divergence loss and the choice of privileged information used for distillation. The authors should also investigate the potential for overfitting or underfitting with different hyperparameter settings, and provide guidelines for selecting appropriate values. This analysis should include a discussion of the trade-offs between different hyperparameter settings, and how these trade-offs might affect the performance of OPSD. The authors should also explore the use of techniques such as grid search or Bayesian optimization to identify the optimal hyperparameter settings for OPSD.

Finally, the authors should discuss the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The authors should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios. For example, the authors could explore the use of knowledge graphs or external knowledge bases to provide OPSD with the necessary external knowledge. Furthermore, the authors should consider evaluating OPSD on more complex reasoning benchmarks that require multi-step inference or external knowledge, to provide a more comprehensive assessment of its capabilities.

### Questions

See the weaknesses.

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces On-Policy Self-Distillation (OPSD), a novel framework that enables a single large language model to act as both teacher and student, leveraging ground-truth solutions to provide dense, token-level supervision. OPSD addresses the limitations of existing distillation methods by using on-policy sampling and a per-token pointwise KL clipping mechanism, achieving superior performance on mathematical reasoning benchmarks compared to reinforcement learning methods while requiring fewer training samples.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective, and the experimental results are convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with OPSD, especially in comparison to other distillation methods. Specifically, the paper does not provide a breakdown of the time and memory requirements for both training and inference, making it difficult to assess the practical applicability of the method, particularly for large-scale models and datasets. A comparison of training time, GPU memory usage, and inference speed against methods like supervised fine-tuning and reinforcement learning would be beneficial.
2. The paper does not explore the sensitivity of OPSD to different hyperparameter settings, such as the weighting of the KL divergence loss or the choice of the privileged information used for distillation. The paper should include a more thorough analysis of how these hyperparameters affect the performance of OPSD, including a discussion of the optimal ranges and the potential for overfitting or underfitting. It is unclear how the method would perform with different choices of privileged information, such as different types of reasoning traces or different levels of ground-truth detail.
3. The paper does not discuss the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The paper should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with OPSD. Specifically, the authors should provide a detailed breakdown of the time and memory requirements for both training and inference, comparing OPSD against other distillation methods such as supervised fine-tuning and reinforcement learning. This analysis should consider the impact of different model sizes and dataset sizes on the computational cost of OPSD. For example, the authors could include a table or graph showing the training time, GPU memory usage, and inference speed for OPSD and other methods as a function of model size and dataset size. This would provide a clearer understanding of the practical applicability of OPSD, especially for large-scale models and datasets. Furthermore, the authors should discuss any potential bottlenecks or limitations that might arise when scaling OPSD to larger models and datasets.

In addition to the computational cost, the paper should also explore the sensitivity of OPSD to different hyperparameter settings. The authors should include a more thorough analysis of how the weighting of the KL divergence loss and the choice of privileged information used for distillation affect the performance of OPSD. This analysis should include a discussion of the optimal ranges for these hyperparameters and the potential for overfitting or underfitting. For example, the authors could conduct a grid search or use Bayesian optimization to identify the optimal hyperparameter settings for OPSD. Furthermore, the authors should discuss how the method would perform with different choices of privileged information, such as different types of reasoning traces or different levels of ground-truth detail. This would provide a more complete understanding of the robustness and generalizability of OPSD.

Finally, the paper should address the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The authors should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios. For example, the authors could explore the use of knowledge graphs or external knowledge bases to provide OPSD with the necessary external knowledge. Furthermore, the authors should consider evaluating OPSD on more complex reasoning benchmarks that require multi-step inference or external knowledge, to provide a more comprehensive assessment of its capabilities. This would help to identify the limitations of OPSD and guide future research in this area.

### Questions

See the weaknesses.

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's identified weaknesses.
2. For each weakness, check if it's related to the method or experiments.
3. Find specific evidence in the paper (quotes, numbers, missing information) to support the weakness.
4. If the weakness is about missing information, check if the information is indeed absent.
5. If there are conflicting opinions, note them.
6. Finally, conclude if the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational cost associated with OPSD, especially in comparison to other distillation methods. Specifically, the paper does not provide a breakdown of the time and memory requirements for both training and inference, making it difficult to assess the practical applicability of the method, particularly for large-scale models and datasets. A comparison of training time, GPU memory usage, and inference speed against methods like supervised fine-tuning and reinforcement learning would be beneficial.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hardware used for experiments: "Experiments were conducted on A100 or H100 GPUs with LoRA." (Section 4.1)
   - There is no explicit mention of training time, GPU memory usage, or inference speed for OPSD or the baseline methods.

3. Literature Gap Analysis:
   - While the paper compares performance metrics (accuracy, F1 score), it does not include a computational cost comparison with other methods.

4. Validation Analysis:
   - The reviewer correctly points out the absence of a detailed computational cost analysis. The paper focuses on performance metrics but omits information on training time, memory usage, and inference speed, making it difficult to assess the practical applicability of OPSD, especially in resource-constrained environments.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Lack of explicit mention of training time, GPU memory usage, and inference speed in the experimental setup and results sections.

1. Weakness Statement:
[The paper does not explore the sensitivity of OPSD to different hyperparameter settings, such as the weighting of the KL divergence loss or the choice of the privileged information used for distillation. The paper should include a more thorough analysis of how these hyperparameters affect the performance of OPSD, including a discussion of the optimal ranges and the potential for overfitting or underfitting. It is unclear how the method would perform with different choices of privileged information, such as different types of reasoning traces or different levels of ground-truth detail.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the use of a "full-vocabulary logit distillation" objective (Section 3.2) but does not explicitly discuss the weighting of the KL divergence loss.
   - The paper states: "We instantiate a full-vocabulary divergence objective that matches the teacher and student next-token distributions at each position." (Section 3.2) and later mentions "a reverse-KL signal on sampled actions" (Section 3.2). The weighting of this reverse-KL signal is not explicitly discussed or varied in the experiments.
   - The paper uses the teacher policy (with privileged information) to guide the student's generation (Section 3.2). The choice of privileged information (TM-off student, TM-on teacher) is explored in ablation studies (Section 4.3.1).

3. Literature Gap Analysis:
   - While the paper cites relevant works on distillation, it doesn't delve into the sensitivity analysis of hyperparameters specific to its method.

4. Validation Analysis:
   - The reviewer is partially correct. The paper does explore the choice of privileged information (TM-off student, TM-on teacher). However, it does not explicitly discuss or experiment with the weighting of the KL divergence loss or the impact of different types of privileged information beyond the two mentioned.

5. Conclusion:
   - Validity status: [Partially Valid]
   - Confidence level: [High]
   - Key supporting evidence: The paper explores different privileged information settings but lacks a discussion or experimentation on the weighting of the KL divergence loss.

1. Weakness Statement:
[The paper does not discuss the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The paper should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper evaluates OPSD on AIME 2024, AIME 2025, HMMT 2025, and AIME 2025 (Section 4.2). These are mathematical reasoning benchmarks.
   - The "Motivation" section mentions "reasoning datasets" but doesn't specify the complexity beyond the evaluated benchmarks.

3. Literature Gap Analysis:
   - The paper doesn't discuss the limitations of OPSD in the context of tasks requiring external knowledge or multi-step inference.

4. Validation Analysis:
   - The reviewer is correct. The paper's evaluation is limited to mathematical reasoning benchmarks. There is no discussion about the potential limitations of OPSD for more complex reasoning tasks requiring external knowledge or multi-step inference.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: The experimental evaluation is limited to mathematical reasoning datasets, and there is no discussion of limitations for more complex reasoning tasks.

**Review 2 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed comparison with existing self-distillation methods. While the authors mention that OPSD is inspired by self-distillation, they do not provide a thorough comparison with other self-distillation techniques, such as those used in knowledge distillation or model compression. This makes it difficult to understand the novelty and advantages of OPSD over existing methods.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions "On-Policy Self-Distillation (OPSD), a novel framework that enables a single large language model (LLM) to act as both teacher and student, leveraging ground-truth solutions to provide dense, token-level supervision." (Main Idea)
   - The "Introduction" mentions "On-policy distillation ( Agarwal et al., 2024 ; Lu and Lab, 2025 ; Xu et al., 2024a ) addresses this by training the student on its own generated trajectories while a teacher policy provides dense, token-level supervision."
   - The paper cites Agarwal et al. (2024) and Lu and Lab (2025) as examples of on-policy distillation.
   - The paper distinguishes OPSD by stating: "We propose On-Policy Self-Distillation (OPSD) , a framework in which a single model plays both teacher and student roles." (Section 3.2) and "In summary, our contributions are as follows: • We introduce On-Policy Self-Distillation (OPSD), a novel framework that enables a single model to act as both teacher and student with different contexts." (Introduction)

3. Literature Gap Analysis:
   - While the paper mentions on-policy distillation and highlights the difference in teacher-student roles, it doesn't provide a detailed comparison with other self-distillation methods used in knowledge distillation or model compression.

4. Validation Analysis:
   - The reviewer is correct. While the paper mentions on-policy distillation, it lacks a detailed comparison with other self-distillation techniques, making it harder to understand the specific novelty and advantages of OPSD.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: The paper mentions on-policy distillation but lacks a detailed comparison with other self-distillation methods.

1. Weakness Statement:
[The paper does not provide a clear explanation of how OPSD addresses the limitations of existing methods. While the authors claim that OPSD is more sample efficient than reinforcement learning methods, they do not provide a detailed analysis of why this is the case. It is not clear how the on-policy approach reduces the need for large amounts of data or how the self-distillation mechanism avoids the issues of sparse rewards and limited exploration in reinforcement learning.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Motivation" section states: "However, reinforcement learning (RL) methods, while effective, suffer from inefficiencies, including sample sparsity, limited exploration, and the need for extensive reward signal generation."
   - The "Main Idea" section states: "The key innovation is the use of ground-truth solutions to provide dense, token-level supervision, which addresses the distribution mismatch between training and inference in off-policy methods."
   - The "Introduction" states: "On-policy distillation ( Agarwal et al., 2024 ; Lu and Lab, 2025 ; Xu et al., 2024a ) addresses this by training the student on its own generated trajectories while a teacher policy provides dense, token-level supervision."
   - The paper explains the on-policy sampling in Section 3.1.

3. Literature Gap Analysis:
   - The paper cites relevant works on on-policy distillation, which implicitly explains how it addresses sample inefficiency.

4. Validation Analysis:
   - The reviewer is partially correct. The paper does explain the mechanism of on-policy distillation (using the student's own generated trajectories) and how it addresses sample inefficiency compared to off-policy methods. However, it could provide a more explicit and detailed analysis of how OPSD specifically avoids the issues of sparse rewards and limited exploration inherent in reinforcement learning.

5. Conclusion:
   - Validity status: [Partially Valid]
   - Confidence level: [Medium]
   - Key supporting evidence: The paper mentions on-policy distillation and its benefits but could elaborate more on how OPSD avoids RL's specific limitations.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of OPSD. While the authors claim that OPSD is more sample efficient, they do not provide a detailed analysis of the computational resources required for training and inference. This makes it difficult to assess the practical applicability of OPSD, especially for large-scale models and datasets.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hardware used for experiments: "Experiments were conducted on A100 or H100 GPUs with LoRA." (Section 4.1)
   - There is no explicit mention of training time, GPU memory usage, or inference speed for OPSD or the baseline methods.

3. Literature Gap Analysis:
   - While the paper compares performance metrics (accuracy, F1 score), it does not include a computational cost comparison with other methods.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1, and the validation remains the same. The reviewer is correct that the paper lacks a detailed analysis of the computational cost.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Lack of explicit mention of training time, GPU memory usage, and inference speed in the experimental setup and results sections.

1. Weakness Statement:
[The paper does not provide a clear explanation of the choice of hyperparameters. The authors do not provide a detailed analysis of how the hyperparameters were chosen or how they affect the performance of OPSD. This makes it difficult to reproduce the results and to understand the robustness of OPSD to different hyperparameter settings.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions using LoRA for fine-tuning: "We fix the teacher policy to be the initial policy, rather than the currently updating learning policy, as we find this helps stabilize training and implicitly acts as regularization to prevent excessive deviation from the initial policy. We use full-vocabulary logit distillation in our experiments. All experiments are conducted on A100 or H100 GPUs with LoRA ( Hu et al., 2022 ). More experimental details are in Appendix B ." (Section 4.1)
   - The paper mentions the learning rate: "All experiments are conducted on A100 or H100 GPUs with LoRA ( Hu et al., 2022 ). More experimental details are in Appendix B ." (Section 4.1)
   - The paper mentions the number of sampled tokens: "All experiments are conducted on A100 or H100 GPUs with LoRA ( Hu et al., 2022 ). More experimental details are in Appendix B ." (Section 4.1)
   - The paper mentions the generation length: "All experiments are conducted on A100 or H100 GPUs with LoRA ( Hu et al., 2022 ). More experimental details are in Appendix B ." (Section 4.1)
   - The paper mentions the teacher policy: "We fix the teacher policy to be the initial policy..." (Section 4.1)
   - The paper mentions the student policy: "We use full-vocabulary logit distillation in our experiments." (Section 4.1)
   - The paper mentions the token efficiency: "We also observe consistent performance degradation under SFT across tasks and model scales when trained on the same dataset, which we attribute to the concise reasoning style of the ground truth solutions which has reduced reasoning lengths at test time." (Section 4.2)
   - The paper mentions the token clipping: "To address this, we apply pointwise clipping to the vocabulary-level divergence contributions. Let D f (p T ∥ p S ) D(p T ∥ p S ) denote an f -divergence. At each token position n n and vocabulary entry v v , define: ℓ n , v ( f ) = p T ( v ∣ ⋅ ) f ( p S ( v ∣ ⋅ ) p T ( v ∣ ⋅ ) ) ." (Section 3.2)

4. Validation Analysis:
   - The reviewer is correct. While the paper mentions some hyperparameters like LoRA, learning rate, number of sampled tokens, generation length, and the choice of teacher and student policies, it lacks a detailed explanation of how these were chosen and their impact on performance. There is no sensitivity analysis or justification for the specific values used.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: The paper mentions some hyperparameters but lacks a detailed explanation of their selection and impact.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational cost associated with OPSD, especially in comparison to other distillation methods. Specifically, the paper does not provide a breakdown of the time and memory requirements for both training and inference, making it difficult to assess the practical applicability of the method, particularly for large-scale models and datasets. A comparison of training time, GPU memory usage, and inference speed against methods like supervised fine-tuning and reinforcement learning would be beneficial.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hardware used for experiments: "Experiments were conducted on A100 or H100 GPUs with LoRA." (Section 4.1)
   - There is no explicit mention of training time, GPU memory usage, or inference speed for OPSD or the baseline methods.

3. Literature Gap Analysis:
   - While the paper compares performance metrics (accuracy, F1 score), it does not include a computational cost comparison with other methods.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1 and Reviewer 2, and the validation remains the same. The reviewer is correct that the paper lacks a detailed analysis of the computational cost.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Lack of explicit mention of training time, GPU memory usage, and inference speed in the experimental setup and results sections.

1. Weakness Statement:
[The paper does not explore the sensitivity of OPSD to different hyperparameter settings, such as the weighting of the KL divergence loss or the choice of the privileged information used for distillation. The paper should include a more thorough analysis of how these hyperparameters affect the performance of OPSD, including a discussion of the optimal ranges and the potential for overfitting or underfitting. It is unclear how the method would perform with different choices of privileged information, such as different types of reasoning traces or different levels of ground-truth detail.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the use of a "full-vocabulary logit distillation" objective (Section 3.2) but does not explicitly discuss the weighting of the KL divergence loss.
   - The paper states: "We instantiate a full-vocabulary divergence objective that matches the teacher and student next-token distributions at each position." (Section 3.2) and later mentions "a reverse-KL signal on sampled actions" (Section 3.2). The weighting of this reverse-KL signal is not explicitly discussed or varied in the experiments.
   - The paper states: "We use full-vocabulary logit distillation in our experiments." (Section 4.1)
   - The paper explores the choice of privileged information (TM-off student, TM-on teacher) in ablation studies (Section 4.3.1).

4. Validation Analysis:
   - The reviewer is partially correct. The paper explores the choice of privileged information (TM-off student, TM-on teacher). However, it does not explicitly discuss or experiment with the weighting of the KL divergence loss or the impact of different types of privileged information beyond the two mentioned.

5. Conclusion:
   - Validity status: [Partially Valid]
   - Confidence level: [High]
   - Key supporting evidence: The paper explores different privileged information settings but lacks a discussion or experimentation on the weighting of the KL divergence loss.

1. Weakness Statement:
[The paper does not discuss the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The paper should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper evaluates OPSD on AIME 2024, AIME 2025, HMMT 2025, and AIME 2025 (Section 4.2). These are mathematical reasoning benchmarks.
   - The "Motivation" section mentions "reasoning datasets" but doesn't specify the complexity beyond the evaluated benchmarks.

3. Literature Gap Analysis:
   - The paper doesn't discuss the limitations of OPSD in the context of tasks requiring external knowledge or multi-step inference.

4. Validation Analysis:
   - The reviewer is correct. The paper's evaluation is limited to mathematical reasoning benchmarks. There is no discussion about the potential limitations of OPSD for more complex reasoning tasks requiring external knowledge or multi-step inference.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: The experimental evaluation is limited to mathematical reasoning datasets, and there is no discussion of limitations for more complex reasoning tasks.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational cost associated with OPSD, especially in comparison to other distillation methods. Specifically, the paper does not provide a breakdown of the time and memory requirements for both training and inference, making it difficult to assess the practical applicability of the method, particularly for large-scale models and datasets. A comparison of training time, GPU memory usage, and inference speed against methods like supervised fine-tuning and reinforcement learning would be beneficial.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hardware used for experiments: "Experiments were conducted on A100 or H100 GPUs with LoRA." (Section 4.1)
   - There is no explicit mention of training time, GPU memory usage, or inference speed for OPSD or the baseline methods.

3. Literature Gap Analysis:
   - While the paper compares performance metrics (accuracy, F1 score), it does not include a computational cost comparison with other methods.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1, Reviewer 2, and Reviewer 3, and the validation remains the same. The reviewer is correct that the paper lacks a detailed analysis of the computational cost.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: Lack of explicit mention of training time, GPU memory usage, and inference speed in the experimental setup and results sections.

1. Weakness Statement:
[The paper does not explore the sensitivity of OPSD to different hyperparameter settings, such as the weighting of the KL divergence loss or the choice of the privileged information used for distillation. The paper should include a more thorough analysis of how these hyperparameters affect the performance of OPSD, including a discussion of the optimal ranges and the potential for overfitting or underfitting. It is unclear how the method would perform with different choices of privileged information, such as different types of reasoning traces or different levels of ground-truth detail.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the use of a "full-vocabulary logit distillation" objective (Section 3.2) but does not explicitly discuss the weighting of the KL divergence loss.
   - The paper states: "We instantiate a full-vocabulary divergence objective that matches the teacher and student next-token distributions at each position." (Section 3.2) and later mentions "a reverse-KL signal on sampled actions" (Section 3.2). The weighting of this reverse-KL signal is not explicitly discussed or varied in the experiments.
   - The paper states: "We use full-vocabulary logit distillation in our experiments." (Section 4.1)
   - The paper explores the choice of privileged information (TM-off student, TM-on teacher) in ablation studies (Section 4.3.1).

4. Validation Analysis:
   - The reviewer is partially correct. The paper explores the choice of privileged information (TM-off student, TM-on teacher). However, it does not explicitly discuss or experiment with the weighting of the KL divergence loss or the impact of different types of privileged information beyond the two mentioned.

5. Conclusion:
   - Validity status: [Partially Valid]
   - Confidence level: [High]
   - Key supporting evidence: The paper explores different privileged information settings but lacks a discussion or experimentation on the weighting of the KL divergence loss.

1. Weakness Statement:
[The paper does not discuss the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The paper should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper evaluates OPSD on AIME 2024, AIME 2025, HMMT 2025, and AIME 2025 (Section 4.2). These are mathematical reasoning benchmarks.
   - The "Motivation" section mentions "reasoning datasets" but doesn't specify the complexity beyond the evaluated benchmarks.

3. Literature Gap Analysis:
   - The paper doesn't discuss the limitations of OPSD in the context of tasks requiring external knowledge or multi-step inference.

4. Validation Analysis:
   - The reviewer is correct. The paper's evaluation is limited to mathematical reasoning benchmarks. There is no discussion about the potential limitations of OPSD for more complex reasoning tasks requiring external knowledge or multi-step inference.

5. Conclusion:
   - Validity status: [Valid]
   - Confidence level: [High]
   - Key supporting evidence: The experimental evaluation is limited to mathematical reasoning datasets, and there is no discussion of limitations for more complex reasoning tasks.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces On-Policy Self-Distillation (OPSD), a novel framework designed to enhance the reasoning capabilities of large language models (LLMs). The core idea behind OPSD is to enable a single LLM to simultaneously act as both the teacher and the student, leveraging its own reasoning abilities and ground-truth solutions to provide dense, token-level supervision. This approach contrasts with traditional distillation methods that often rely on sparse, sequence-level feedback. OPSD employs a per-token pointwise KL clipping mechanism to stabilize training and achieve superior performance with fewer training samples compared to reinforcement learning (RL) methods. The method is evaluated on mathematical reasoning benchmarks, where it demonstrates competitive performance with fewer training samples and reduced training time. The authors frame OPSD as an on-policy distillation technique, where the student model is trained on its own generated trajectories, guided by a teacher policy that has access to the ground truth. This is in contrast to off-policy distillation methods that use a separate, fixed teacher policy. The paper's main contribution lies in its innovative approach to self-distillation, which allows a single model to learn from itself in a more efficient and effective manner. The experimental results show that OPSD achieves comparable performance to RL methods, while requiring significantly fewer training samples and less training time. The authors also conduct ablation studies to analyze the impact of different privileged information settings and the effectiveness of the KL divergence objective. The paper is well-written and easy to follow, making the technical details accessible to a broad audience. The authors provide a clear motivation for their work, highlighting the limitations of existing distillation methods and the need for more efficient and effective approaches. The experimental results are convincing, demonstrating the potential of OPSD as a viable alternative to RL-based methods for improving the reasoning capabilities of LLMs. The paper's focus on mathematical reasoning benchmarks is a strength, as it allows for a clear and quantitative evaluation of the method's performance. However, the paper also has some limitations, particularly in its lack of detailed analysis of computational costs and its limited discussion of the method's applicability to more complex reasoning tasks. Despite these limitations, the paper makes a significant contribution to the field of LLM distillation and provides a promising direction for future research.


## Soundness:

2.75


## Presentation:

2.75


## Contribution:

2.75


## Strengths:

I found several aspects of this paper to be particularly strong. First, the core idea of On-Policy Self-Distillation (OPSD) is both innovative and well-motivated. The authors effectively frame the problem of improving LLM reasoning as a self-distillation challenge, where a single model acts as both teacher and student. This approach is particularly appealing because it eliminates the need for separate, often expensive, teacher models. The use of ground-truth solutions to provide dense, token-level supervision is a key strength, addressing the limitations of traditional distillation methods that rely on sparse, sequence-level feedback. The per-token pointwise KL clipping mechanism is another notable technical innovation, which helps stabilize training and contributes to the method's overall effectiveness. The experimental results are also compelling, demonstrating that OPSD achieves competitive performance with fewer training samples and less training time compared to reinforcement learning methods. The authors provide a clear and concise explanation of their method, making it easy to understand and reproduce. The paper is well-written and organized, which greatly enhances its readability. The authors also conduct ablation studies to analyze the impact of different privileged information settings and the effectiveness of the KL divergence objective, which further strengthens the paper's findings. The paper's focus on mathematical reasoning benchmarks is also a strength, as it allows for a clear and quantitative evaluation of the method's performance. The authors effectively demonstrate the potential of OPSD as a viable alternative to RL-based methods for improving the reasoning capabilities of LLMs. The paper's motivation is clear, and the authors effectively highlight the limitations of existing distillation methods and the need for more efficient and effective approaches. The experimental results are convincing, demonstrating the potential of OPSD as a viable alternative to RL-based methods for improving the reasoning capabilities of LLMs. The paper's focus on mathematical reasoning benchmarks is a strength, as it allows for a clear and quantitative evaluation of the method's performance. The authors also provide a clear and concise explanation of their method, making it easy to understand and reproduce. The paper is well-written and organized, which greatly enhances its readability.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. A primary concern is the lack of a detailed analysis of the computational cost associated with OPSD. While the paper mentions the hardware used for experiments (A100 or H100 GPUs with LoRA), it fails to provide a breakdown of the time and memory requirements for both training and inference. This omission makes it difficult to assess the practical applicability of OPSD, particularly for large-scale models and datasets. The paper does not include a comparison of training time, GPU memory usage, or inference speed against other distillation methods, such as supervised fine-tuning or reinforcement learning. This lack of computational analysis is a significant limitation, as it prevents a comprehensive understanding of the trade-offs involved in using OPSD. My confidence in this weakness is high, as the absence of this information is clearly evident in the experimental setup and results sections. Furthermore, the paper does not explore the sensitivity of OPSD to different hyperparameter settings. While the paper mentions the use of a full-vocabulary logit distillation objective and the application of pointwise KL divergence clipping, it does not provide a thorough analysis of how these hyperparameters affect the performance of OPSD. The paper does not explicitly discuss or experiment with the weighting of the KL divergence loss, which is a crucial hyperparameter that can significantly impact the training process. The paper also does not explore the impact of different types of privileged information, such as different types of reasoning traces or different levels of ground-truth detail. Although the paper explores the choice of privileged information (TM-off student, TM-on teacher) in ablation studies, it does not investigate the potential for overfitting or underfitting with different hyperparameter settings. This lack of sensitivity analysis makes it difficult to reproduce the results and to understand the robustness of OPSD to different hyperparameter settings. My confidence in this weakness is high, as the paper lacks a discussion or experimentation on the weighting of the KL divergence loss and the impact of different types of privileged information beyond the two mentioned. Another significant weakness is the limited discussion of the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The paper does not include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios. This lack of discussion limits the generalizability of the findings and raises questions about the applicability of OPSD to more complex reasoning tasks. My confidence in this weakness is high, as the experimental evaluation is limited to mathematical reasoning datasets, and there is no discussion of limitations for more complex reasoning tasks. Additionally, the paper lacks a detailed comparison with existing self-distillation methods. While the authors mention that OPSD is inspired by self-distillation, they do not provide a thorough comparison with other self-distillation techniques, such as those used in knowledge distillation or model compression. This makes it difficult to understand the novelty and advantages of OPSD over existing methods. The paper should clearly articulate how OPSD differs from other self-distillation techniques, particularly those used in knowledge distillation and model compression. My confidence in this weakness is high, as the paper mentions on-policy distillation but lacks a detailed comparison with other self-distillation methods. Finally, while the paper claims that OPSD is more sample efficient than reinforcement learning methods, it does not provide a detailed analysis of why this is the case. The paper mentions on-policy distillation and its benefits, but it could provide a more explicit and detailed analysis of how OPSD specifically avoids the issues of sparse rewards and limited exploration inherent in reinforcement learning. My confidence in this weakness is medium, as the paper mentions on-policy distillation but could elaborate more on how OPSD avoids RL's specific limitations. These weaknesses, taken together, highlight the need for further investigation and analysis to fully understand the potential and limitations of OPSD.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a more detailed analysis of the computational cost associated with OPSD. This analysis should include a breakdown of the time and memory requirements for both training and inference, comparing OPSD against other distillation methods, such as supervised fine-tuning and reinforcement learning. The analysis should consider the impact of different model sizes and dataset sizes on the computational cost of OPSD. Furthermore, the authors should investigate the scalability of OPSD to larger models and datasets, and discuss any potential bottlenecks or limitations that might arise. This analysis should be presented in a clear and concise manner, with tables and figures that allow for easy comparison of the computational costs of different methods. Second, the authors should conduct a more thorough analysis of the sensitivity of OPSD to different hyperparameter settings. This analysis should include a systematic exploration of the optimal ranges for the weighting of the KL divergence loss and the choice of privileged information used for distillation. The authors should also investigate the potential for overfitting or underfitting with different hyperparameter settings, and provide guidelines for selecting appropriate values. This analysis should include a discussion of the trade-offs between different hyperparameter settings, and how these trade-offs might affect the performance of OPSD. The authors should also explore the use of techniques such as grid search or Bayesian optimization to identify the optimal hyperparameter settings for OPSD. Third, the authors should discuss the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge. The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. The authors should include a discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference, and what modifications would be necessary to adapt the method to these scenarios. For example, the authors could explore the use of knowledge graphs or external knowledge bases to provide OPSD with the necessary external knowledge. Furthermore, the authors should consider evaluating OPSD on more complex reasoning benchmarks that require multi-step inference or external knowledge, to provide a more comprehensive assessment of its capabilities. Fourth, the authors should provide a more detailed comparison with existing self-distillation methods. The authors should clearly articulate how OPSD differs from other self-distillation techniques, particularly those used in knowledge distillation and model compression. A thorough analysis should include a discussion of the specific mechanisms used for knowledge transfer, the types of distillation losses employed, and the ways in which these methods handle the challenges of learning from a teacher model. Furthermore, the authors should provide a quantitative comparison of OPSD with these methods, demonstrating the specific advantages of OPSD in terms of performance, sample efficiency, and computational cost. This would help to establish the novelty and significance of the proposed approach. Finally, the authors should provide a more detailed analysis of why OPSD is more sample efficient than reinforcement learning methods. This analysis should include a discussion of how the on-policy approach reduces the need for large amounts of data and how the self-distillation mechanism avoids the issues of sparse rewards and limited exploration inherent in reinforcement learning. By addressing these weaknesses, the authors can significantly strengthen the paper and provide a more comprehensive understanding of the potential and limitations of OPSD.


## Questions:

Based on my analysis, I have several questions that I believe are important for further clarification. First, how does OPSD compare to other self-distillation methods in terms of performance, sample efficiency, and computational cost? The paper mentions that OPSD is inspired by self-distillation, but it does not provide a detailed comparison with other self-distillation techniques. A thorough analysis should clarify the specific advantages of OPSD over existing methods. Second, how does OPSD address the limitations of existing methods, such as sparse rewards and limited exploration in reinforcement learning? While the paper claims that OPSD is more sample efficient than reinforcement learning methods, it does not provide a detailed analysis of why this is the case. A more explicit and detailed analysis of how OPSD specifically avoids the issues of sparse rewards and limited exploration inherent in reinforcement learning would be beneficial. Third, what is the computational cost of OPSD compared to existing methods? The paper lacks a detailed analysis of the computational cost associated with OPSD, particularly in comparison to other distillation methods. A comparison of training time, GPU memory usage, and inference speed against methods like supervised fine-tuning and reinforcement learning would be beneficial. Fourth, what is the sensitivity of OPSD to different hyperparameter settings? The paper does not explore the sensitivity of OPSD to different hyperparameter settings, such as the weighting of the KL divergence loss or the choice of privileged information used for distillation. A more thorough analysis of how these hyperparameters affect the performance of OPSD would be beneficial. Fifth, what are the potential limitations of OPSD in handling more complex reasoning tasks that require multi-step inference or external knowledge? The current evaluation focuses on mathematical reasoning benchmarks, which may not fully capture the challenges of more complex reasoning scenarios. A discussion of how OPSD might be extended to handle tasks that require external knowledge or multi-step inference would be beneficial. Finally, how does OPSD compare to other self-distillation methods in terms of performance, sample efficiency, and computational cost? The paper should provide a quantitative comparison of OPSD with these methods, demonstrating the specific advantages of OPSD in terms of performance, sample efficiency, and computational cost. Addressing these questions would provide a more comprehensive understanding of the potential and limitations of OPSD and would help to guide future research in this area.


## Rating:

6.25


## Confidence:

3.0


## Decision:

Reject
}