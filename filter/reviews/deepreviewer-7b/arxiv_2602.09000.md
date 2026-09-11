I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes Iterative Group Relative Policy Optimization (iGRPO), an extension of Group Relative Policy Optimization (GRPO) that incorporates a self-feedback mechanism. While GRPO optimizes large language models (LLMs) through group-based relative rewards, iGRPO adds a two-stage process: the first stage samples multiple responses and selects the highest-scoring one as feedback, and the second stage conditions on this feedback for further refinement. This iterative approach aims to improve LLM performance in complex reasoning tasks, particularly in mathematical problem-solving, by enhancing the model's ability to self-correct and improve upon its initial attempts.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with a clear presentation of the proposed method and its motivation.
2. The authors provide a thorough empirical evaluation of iGRPO across various benchmarks and model sizes, demonstrating consistent improvements over baseline methods. The ablation studies further validate the design choices and the contribution of each component of iGRPO.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by the two-stage process of iGRPO. While the authors mention that the compute cost is comparable to GRPO, a more granular breakdown of the time and resources required for each stage would be beneficial. Specifically, the cost of generating multiple responses in the first stage and the subsequent refinement in the second stage should be quantified, as well as the impact on training time and memory usage. This analysis should also consider the scaling behavior of the method with respect to model size and dataset size.
2. The theoretical analysis is limited to the case of binary rewards, which may not fully capture the complexities of real-world reasoning tasks. The analysis should be extended to more general reward functions, such as those that are continuous or have a more complex structure. Furthermore, the theoretical justification for the bootstrapping effect could be strengthened by providing more insights into the convergence properties of the algorithm and the conditions under which it is guaranteed to improve performance.

### Suggestions

The paper would benefit from a more detailed analysis of the computational costs associated with the two-stage iterative process of iGRPO. While the authors claim that the compute cost is comparable to GRPO, a more granular breakdown of the time and resources required for each stage would be beneficial. Specifically, the cost of generating multiple responses in the first stage and the subsequent refinement in the second stage should be quantified, as well as the impact on training time and memory usage. This analysis should also consider the scaling behavior of the method with respect to model size and dataset size. For example, it would be useful to know how the number of samples needed in each stage scales with the model size and the complexity of the task. Furthermore, the authors should provide a more detailed comparison of the computational cost of iGRPO with other self-improvement methods, such as self-verification or critique-based learning, to better contextualize the efficiency of their approach. This would help readers understand the trade-offs between performance gains and computational overhead.

To strengthen the theoretical analysis, the authors should extend their analysis to more general reward functions beyond the binary case. The current analysis, while providing some insights, is limited by its simplicity and may not fully capture the complexities of real-world reasoning tasks. For example, the reward functions used in practice are often continuous or have a more complex structure, and the theoretical analysis should be extended to these cases. Furthermore, the theoretical justification for the bootstrapping effect could be strengthened by providing more insights into the convergence properties of the algorithm and the conditions under which it is guaranteed to improve performance. It would be beneficial to explore the relationship between the reward function, the policy update rule, and the convergence behavior of the algorithm. This could involve analyzing the properties of the objective function and the gradient updates, and providing theoretical guarantees on the performance improvement.

Finally, the paper could benefit from a more thorough discussion of the limitations of the proposed method. While the empirical results demonstrate improvements on the tested benchmarks, it is important to acknowledge the potential limitations of iGRPO in more complex scenarios. For example, the authors should discuss the potential for the method to get stuck in local optima, or the sensitivity of the method to the choice of hyperparameters. Furthermore, the authors should discuss the potential for the method to amplify biases present in the training data. A more detailed discussion of these limitations would help readers better understand the scope and applicability of the proposed method, and provide directions for future research.

### Questions

1. How does the performance of iGRPO scale with the size of the model and the dataset? Are there any limitations in terms of computational resources or training time?
2. Can the authors provide more insights into the choice of the number of samples in each stage of iGRPO? How does this choice affect the performance and computational cost?
3. The paper focuses on mathematical reasoning tasks. How well does iGRPO generalize to other types of reasoning tasks, such as logical reasoning or commonsense reasoning?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper introduces Iterative Group Relative Policy Optimization (iGRPO), an extension of Group Relative Policy Optimization (GRPO) that incorporates a self-feedback mechanism. iGRPO improves LLMs' mathematical reasoning by iteratively refining drafts through two stages: first, it samples multiple drafts and selects the highest-scoring one; second, it conditions on this best draft and applies GRPO-style updates. Empirical results demonstrate that iGRPO outperforms GRPO and other self-improvement methods across various model sizes and benchmarks, particularly in complex mathematical reasoning tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective, with clear motivation and implementation.
3. The empirical results are comprehensive, covering multiple model sizes and benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by the two-stage process of iGRPO. While the authors mention that the compute cost is comparable to GRPO, a more granular breakdown of the time and resources required for each stage would be beneficial. Specifically, the cost of generating multiple responses in the first stage and the subsequent refinement in the second stage should be quantified, as well as the impact on training time and memory usage. This analysis should also consider the scaling behavior of the method with respect to model size and dataset size.
2. The theoretical analysis is limited to the case of binary rewards, which may not fully capture the complexities of real-world reasoning tasks. The analysis should be extended to more general reward functions, such as those that are continuous or have a more complex structure. Furthermore, the theoretical justification for the bootstrapping effect could be strengthened by providing more insights into the convergence properties of the algorithm and the conditions under which it is guaranteed to improve performance.

### Suggestions

The paper would benefit from a more thorough investigation into the computational costs associated with the iterative nature of iGRPO. While the authors claim comparable compute costs to GRPO, a detailed breakdown of the time and resources required for each stage is crucial for practical applications. This should include a quantification of the time spent generating multiple responses in the first stage, as well as the time and memory required for the subsequent refinement stage. Furthermore, the analysis should consider how these costs scale with increasing model size and dataset size. For instance, does the number of samples needed in each stage increase linearly, quadratically, or exponentially with model size? Such an analysis would provide a more complete picture of the practical trade-offs involved in using iGRPO.

To strengthen the theoretical underpinnings of iGRPO, the analysis should be extended beyond the binary reward case. While the current analysis provides some insights, it is limited by its simplicity and may not fully capture the complexities of real-world reasoning tasks. The authors should explore the behavior of iGRPO with more general reward functions, such as those that are continuous or have a more complex structure. This could involve analyzing the convergence properties of the algorithm under different reward structures and identifying the conditions under which it is guaranteed to improve performance. Furthermore, it would be beneficial to investigate the relationship between the reward function, the policy update rule, and the convergence behavior of the algorithm. This would provide a more robust theoretical foundation for the proposed method.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. While the empirical results demonstrate improvements on the tested benchmarks, it is important to acknowledge the potential limitations of iGRPO in more complex scenarios. For example, the authors should discuss the potential for the method to get stuck in local optima, or the sensitivity of the method to the choice of hyperparameters. Furthermore, the authors should discuss the potential for the method to amplify biases present in the training data. A more thorough discussion of these limitations would help readers better understand the scope and applicability of the proposed method, and provide directions for future research.

### Questions

1. How does the performance of iGRPO scale with the size of the model and the dataset? Are there any limitations in terms of computational resources or training time?
2. Can the authors provide more insights into the choice of the number of samples in each stage of iGRPO? How does this choice affect the performance and computational cost?
3. The paper focuses on mathematical reasoning tasks. How well does iGRPO generalize to other types of reasoning tasks, such as logical reasoning or commonsense reasoning?

### Rating

6

### Confidence

4

**********

## Reviewer 3

### Summary

This paper introduces Iterative Group Relative Policy Optimization (iGRPO), a method that extends Group Relative Policy Optimization (GRPO) to improve the performance of large language models (LLMs) in complex reasoning tasks, particularly in mathematical problem-solving. iGRPO is a two-stage process that first selects the highest-scoring draft from multiple generated drafts and then uses this best draft to condition the model for further refinement. This approach allows the model to learn from its own best attempts, leading to improved reasoning capabilities. The authors demonstrate the effectiveness of iGRPO through extensive experiments on various mathematical reasoning benchmarks, showing that it consistently outperforms GRPO and other self-improvement methods across different model sizes.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel and simple extension of GRPO that effectively enhances the performance of LLMs in complex reasoning tasks. The two-stage process of iGRPO, which involves self-conditioning based on the best draft, is straightforward yet powerful, making it easy to implement and integrate into existing training pipelines.
- The paper provides a comprehensive evaluation of iGRPO across multiple benchmarks and model sizes, demonstrating its consistent improvements over baseline methods. The authors also conduct thorough ablation studies to validate the effectiveness of different components of iGRPO, such as the use of a generative judge and the impact of self-feedback on learning dynamics.
- The paper is well-written and organized, with clear explanations of the proposed method and its implementation. The authors also provide a theoretical analysis of the bootstrapping effect of iGRPO, which helps to understand the underlying mechanisms that contribute to its performance improvements.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on mathematical reasoning tasks, and it is unclear how well iGRPO generalizes to other types of reasoning tasks, such as logical reasoning or commonsense reasoning. The authors could provide more insights into the applicability of iGRPO to a broader range of reasoning tasks.
- The paper does not provide a detailed analysis of the computational cost of iGRPO compared to GRPO. While the authors claim that the compute cost is comparable, a more thorough comparison of the training time and resource requirements would be helpful for practitioners who want to adopt this method.
- The paper could benefit from a more in-depth discussion of the limitations of iGRPO and potential areas for future research. For example, the authors could discuss the potential challenges of applying iGRPO to tasks with very large search spaces or the impact of different hyperparameters on the performance of iGRPO.

### Suggestions

The authors should consider expanding their evaluation to include a wider range of reasoning tasks beyond mathematical problem-solving. Specifically, incorporating benchmarks that assess logical reasoning, such as those involving symbolic manipulation or deductive inference, would provide a more comprehensive understanding of iGRPO's capabilities. Furthermore, evaluating iGRPO on tasks that require common-sense reasoning, such as those involving everyday scenarios or implicit knowledge, would help to determine its applicability to real-world problems. This could involve using datasets that test the model's ability to reason about entities, relationships, and events that are not explicitly stated in the training data. Such an analysis would provide a more complete picture of the strengths and weaknesses of the proposed method.

To address the lack of detailed computational analysis, the authors should provide a more granular breakdown of the training time and resource requirements for iGRPO compared to GRPO. This should include a comparison of the number of forward passes, the memory usage, and the overall training time for different model sizes. It would be beneficial to present this information in a table or graph, allowing readers to easily compare the computational cost of the two methods. Additionally, the authors should discuss the scalability of iGRPO to larger models and datasets, and identify any potential bottlenecks that might arise when applying the method to more complex tasks. This analysis should also consider the impact of different hardware configurations on the performance of iGRPO.

Finally, the authors should include a more thorough discussion of the limitations of iGRPO and potential avenues for future research. This could include exploring the impact of different hyperparameters on the performance of iGRPO, such as the number of drafts sampled in each stage and the learning rate. It would also be valuable to investigate the sensitivity of iGRPO to the quality of the initial model and the potential for the method to get stuck in local optima. Furthermore, the authors could discuss the potential for extending iGRPO to other optimization algorithms beyond GRPO, and explore the possibility of using different types of conditioning in the second stage of the method. This discussion should also consider the potential for combining iGRPO with other techniques for improving the reasoning capabilities of LLMs, such as reinforcement learning or adversarial training.

### Questions

- How does iGRPO perform on tasks that require multi-step reasoning or planning? Are there any specific challenges or limitations in applying iGRPO to such tasks?
- How sensitive is iGRPO to the quality of the initial model? Would using a pre-trained model with a lower performance on the target task still yield improvements with iGRPO?
- What are the potential limitations of iGRPO in terms of scalability to larger models or datasets? Are there any specific challenges in applying iGRPO to more complex tasks?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces Iterative Group Relative Policy Optimization (iGRPO), a novel approach to enhance the reasoning capabilities of large language models (LLMs) by incorporating a self-feedback mechanism. The core idea of iGRPO is to iteratively improve the model's performance through two stages: first, the model samples multiple drafts and selects the highest-scoring one as feedback, and then it conditions on this best draft for further refinement. This iterative process allows the model to learn from its own best attempts, leading to improved reasoning abilities. The authors demonstrate the effectiveness of iGRPO through extensive experiments on various mathematical reasoning benchmarks, showing consistent improvements over baseline methods across different model sizes. Additionally, the paper provides a theoretical analysis of the bootstrapping effect, explaining how iGRPO improves the model's performance over time.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel and effective method, iGRPO, which leverages self-feedback to enhance the reasoning capabilities of LLMs. This approach is simple yet powerful, requiring only minor changes to existing training pipelines.
- The authors provide a thorough empirical evaluation of iGRPO across multiple benchmarks and model sizes, demonstrating consistent improvements over baseline methods. The results are well-supported by extensive experiments and ablation studies.
- The paper also includes a theoretical analysis of the bootstrapping effect, which provides a deeper understanding of the underlying mechanisms that contribute to the performance improvements.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on mathematical reasoning tasks, and it is unclear how well iGRPO generalizes to other types of reasoning tasks, such as logical reasoning or commonsense reasoning. The authors could provide more insights into the applicability of iGRPO to a broader range of reasoning tasks.
- The paper does not provide a detailed analysis of the computational cost of iGRPO compared to GRPO. While the authors claim that the compute cost is comparable, a more thorough comparison of the training time and resource requirements would be helpful for practitioners who want to adopt this method.
- The paper could benefit from a more in-depth discussion of the limitations of iGRPO and potential areas for future research. For example, the authors could discuss the potential challenges of applying iGRPO to tasks with very large search spaces or the impact of different hyperparameters on the performance of iGRPO.

### Suggestions

The authors should consider expanding their evaluation to include a wider range of reasoning tasks beyond mathematical problem-solving. Specifically, incorporating benchmarks that assess logical reasoning, such as those involving symbolic manipulation or deductive inference, would provide a more comprehensive understanding of iGRPO's capabilities. Furthermore, evaluating iGRPO on tasks that require common-sense reasoning, such as those involving everyday scenarios or implicit knowledge, would help to determine its applicability to real-world problems. This could involve using datasets that test the model's ability to reason about entities, relationships, and events that are not explicitly stated in the training data. Such an analysis would provide a more complete picture of the strengths and weaknesses of the proposed method.

To address the lack of detailed computational analysis, the authors should provide a more granular breakdown of the training time and resource requirements for iGRPO compared to GRPO. This should include a comparison of the number of forward passes, the memory usage, and the overall training time for different model sizes. It would be beneficial to present this information in a table or graph, allowing readers to easily compare the computational cost of the two methods. Additionally, the authors should discuss the scalability of iGRPO to larger models and datasets, and identify any potential bottlenecks that might arise when applying the method to more complex tasks. This analysis should also consider the impact of different hardware configurations on the performance of iGRPO.

Finally, the authors should include a more thorough discussion of the limitations of iGRPO and potential avenues for future research. This could include exploring the impact of different hyperparameters on the performance of iGRPO, such as the number of drafts sampled in each stage and the learning rate. It would also be valuable to investigate the sensitivity of iGRPO to the quality of the initial model and the potential for the method to get stuck in local optima. Furthermore, the authors could discuss the potential for extending iGRPO to other optimization algorithms beyond GRPO, and explore the possibility of using different types of conditioning in the second stage of the method. This discussion should also consider the potential for combining iGRPO with other techniques for improving the reasoning capabilities of LLMs, such as reinforcement learning or adversarial training.

### Questions

- How does iGRPO perform on tasks that require multi-step reasoning or planning? Are there any specific challenges or limitations in applying iGRPO to such tasks?
- How sensitive is iGRPO to the quality of the initial model? Would using a pre-trained model with a lower performance on the target task still yield improvements with iGRPO?
- What are the potential limitations of iGRPO in terms of scalability to larger models or datasets? Are there any specific challenges in applying iGRPO to more complex tasks?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find corresponding evidence in the paper.
3. Categorize the weakness and provide specific quotes or references to support the validation.
4. If a weakness is not supported by the paper, explain why.
5. Pay attention to potential misunderstandings or conflicting opinions between reviewers.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational overhead introduced by the two-stage process of iGRPO. While the authors mention that the compute cost is comparable to GRPO, a more granular breakdown of the time and resources required for each stage would be beneficial. Specifically, the cost of generating multiple responses in the first stage and the subsequent refinement in the second stage should be quantified, as well as the impact on training time and memory usage. This analysis should also consider the scaling behavior of the method with respect to model size and dataset size.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the two stages of iGRPO in Section 3.2.1 and 3.2.2.
   - The paper states in Section 4.1: "To ensure a fair compute comparison, we keep the total sampling budget fixed at eight completions per prompt for every method; iGRPO redistributes this budget across Stage 1 and Stage 2 rather than increasing them. As a result, differences in Table 1 reflect the effect of conditioning on the best draft rather than the effect of more sampling."
   - The paper mentions in Section 4.1: "For all experiments, the completion length is capped at 4,096 tokens across all datasets. For all benchmarks we report Pass@1 accuracy. However, for AIME24/AIME25 the reported value is averaged over 64 runs to ensure robustness. For other benchmarks, an average of 8 runs are reported. For evaluations, we use NeMo-Skills framework 1 1× GPU-Skills with decoding parameters such as a temperature of 0.6, top-p of 0.95, and generation length of 65,000. Additional training and evaluation details are provided in the supplementary materials."
   - The paper does not provide a detailed breakdown of the time taken for each stage or the memory usage.

b) Experiment-related Evidence:
   - Table 1 shows the performance of iGRPO and GRPO with a fixed sampling budget.
   - The paper does not provide data on the time taken for each stage or the memory usage.

3. Literature Gap Analysis:
   - The paper cites the GRPO paper (Shao et al., 2024), which likely contains some information about the computational cost of GRPO. However, the paper does not explicitly compare the time and memory usage of each stage of iGRPO with GRPO.

4. Validation Analysis:
   - The reviewer correctly points out the lack of a detailed computational overhead analysis. While the paper mentions a fixed sampling budget and reports performance, it does not provide a granular breakdown of the time and resources required for each stage of iGRPO. The claim of comparable compute cost is based on maintaining the same total sampling budget, but the overhead of the two-stage process is not quantified.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks specific data on the time taken for each stage and memory usage, relying on a fixed sampling budget for performance comparison.

1. Weakness Statement:
[The theoretical analysis is limited to the case of binary rewards, which may not fully capture the complexities of real-world reasoning tasks. The analysis should be extended to more general reward functions, such as those that are continuous or have a more complex structure. Furthermore, the theoretical justification for the bootstrapping effect could be strengthened by providing more insights into the convergence properties of the algorithm and the conditions under which it is guaranteed to improve performance.]

2. Evidence Collection:
a) Method-related Evidence:
   - Section 3.2.4 presents the mathematical formulation of the iGRPO objective.
   - The reward function is defined in Equation 6 as a binary indicator:  `R ϕ ( o ) = 𝟙 [ extract ( o ) = a ]`.
   - The theoretical analysis in Section 3.2.4 focuses on this binary reward setting.

b) Experiment-related Evidence:
   - The experiments use a binary reward function (pass/fail).

3. Literature Gap Analysis:
   - The paper does not cite theoretical works that analyze policy optimization with more general reward functions in the context of iterative refinement.

4. Validation Analysis:
   - The reviewer is correct. The theoretical analysis in the paper is indeed limited to the binary reward setting. The paper does not provide a theoretical justification for the bootstrapping effect or convergence properties with more complex reward functions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The theoretical analysis in Section 3.2.4 explicitly uses a binary reward function, and there is no discussion of more general reward functions or convergence properties.

**Review 2 Weaknesses:**

1. Weakness Statement:
[- The paper primarily focuses on mathematical reasoning tasks, and it is unclear how well iGRPO generalizes to other types of reasoning tasks, such as logical reasoning or commonsense reasoning. The authors could provide more insights into the applicability of iGRPO to a broader range of reasoning tasks.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method description in Section 3.2 is general and does not inherently restrict its application to mathematical reasoning.

b) Experiment-related Evidence:
   - The experiments in Section 4 focus on mathematical benchmarks: AIME24, AIME25, MATH500, AMC23, GSM8K, Minerva Math, and GPQA.
   - The paper mentions in Section 4.1: "For models with 7B and 14B parameters, we use a learning rate of 1 × 10 − 6 with a cosine schedule, generating eight completions per prompt (halved in each stage for iGRPO). The maximum prompt length is 1,024 tokens across all datasets. For all benchmarks we report Pass@1 accuracy. However, for AIME24/AIME25 the reported value is averaged over 64 runs to ensure robustness. For other benchmarks, an average of 8 runs are reported."
   - There are no experiments on logical or commonsense reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not cite or compare against methods specifically designed for logical or commonsense reasoning.

4. Validation Analysis:
   - The reviewer's point is valid. The experimental evaluation is limited to mathematical reasoning tasks. The paper does not provide evidence or discussion on the generalizability of iGRPO to other types of reasoning.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experiments section only includes mathematical reasoning benchmarks.

1. Weakness Statement:
[- The paper does not provide a detailed analysis of the computational cost of iGRPO compared to GRPO. While the authors claim that the compute cost is comparable, a more thorough comparison of the training time and resource requirements would be helpful for practitioners who want to adopt this method.]

2. Evidence Collection:
a) Method-related Evidence:
   - Section 4.1 states: "To ensure a fair compute comparison, we keep the total sampling budget fixed at eight completions per prompt for every method; iGRPO redistributes this budget across Stage 1 and Stage 2 rather than increasing them. As a result, differences in Table 1 reflect the effect of conditioning on the best draft rather than the effect of more sampling."

b) Experiment-related Evidence:
   - Table 1 shows the performance of iGRPO and GRPO with a fixed sampling budget.
   - The paper does not provide data on the time taken for training or inference.

3. Literature Gap Analysis:
   - The paper relies on the GRPO paper for some computational details, but it doesn't provide a direct comparison within the context of iGRPO.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1. The paper claims comparable compute cost based on a fixed sampling budget but lacks a detailed analysis of training time and resource requirements.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks specific data on training time and resource requirements, relying on a fixed sampling budget for performance comparison.

1. Weakness Statement:
[- The paper could benefit from a more in-depth discussion of the limitations of iGRPO and potential areas for future research. For example, the authors could discuss the potential for the method to get stuck in local optima, or the sensitivity of the method to the choice of hyperparameters. Furthermore, the authors could discuss the potential for the method to amplify biases present in the training data.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper does not explicitly discuss the potential for getting stuck in local optima or the sensitivity to hyperparameters.

b) Experiment-related Evidence:
   - The paper mentions the hardware used for training but does not discuss the sensitivity to hyperparameters in detail.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of iterative refinement methods or the impact of hyperparameter choices.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a detailed discussion of the limitations of iGRPO, such as the potential for getting stuck in local optima, sensitivity to hyperparameters, and the amplification of biases.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper does not include a dedicated section or detailed discussion on the limitations of the proposed method.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The paper primarily focuses on mathematical reasoning tasks, and it is unclear how well iGRPO generalizes to other types of reasoning tasks, such as logical reasoning or commonsense reasoning. The authors could provide more insights into the applicability of iGRPO to a broader range of reasoning tasks.]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 2. The experimental evaluation is limited to mathematical reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not cite or compare against methods specifically designed for logical or commonsense reasoning.

4. Validation Analysis:
   - Valid. The paper's experimental scope is limited to mathematical reasoning.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experiments section only includes mathematical reasoning benchmarks.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of iGRPO compared to GRPO. While the authors claim that the compute cost is comparable, a more thorough comparison of the training time and resource requirements would be helpful for practitioners who want to adopt this method.]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1 and 2. The paper lacks a detailed analysis of training time and resource requirements.

3. Literature Gap Analysis:
   - The paper relies on the GRPO paper for some computational details but doesn't provide a direct comparison.

4. Validation Analysis:
   - Valid. The paper lacks a detailed computational cost analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks specific data on training time and resource requirements.

1. Weakness Statement:
[The paper could benefit from a more in-depth discussion of the limitations of iGRPO and potential areas for future research. For example, the authors could discuss the potential for the method to get stuck in local optima, or the sensitivity of iGRPO to the choice of hyperparameters. Furthermore, the authors could discuss the potential for the method to amplify biases present in the training data.]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 2. The paper lacks a detailed discussion of limitations.

3. Literature Gap Analysis:
   - The paper does not cite works discussing the limitations of iterative refinement or hyperparameter sensitivity.

4. Validation Analysis:
   - Valid. The paper lacks a thorough discussion of limitations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper does not include a dedicated section or detailed discussion on limitations.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational overhead introduced by the two-stage process of iGRPO. While the authors mention that the compute cost is comparable to GRPO, a more granular breakdown of the time and resources required for each stage would be beneficial. Specifically, the cost of generating multiple responses in the first stage and the subsequent refinement in the second stage should be quantified, as well as the impact on training time and memory usage. This analysis should also consider the scaling behavior of the method with respect to model size and dataset size.]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, 2, and 3. The paper lacks a detailed computational overhead analysis.

3. Literature Gap Analysis:
   - The paper relies on the GRPO paper for some computational details but doesn't provide a direct comparison.

4. Validation Analysis:
   - Valid. The paper lacks a detailed computational overhead analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks specific data on the time taken for each stage and memory usage.

1. Weakness Statement:
[The theoretical analysis is limited to the case of binary rewards, which may not fully capture the complexities of real-world reasoning tasks. The analysis should be extended to more general reward functions, such as those that are continuous or have a more complex structure. Furthermore, the theoretical justification for the bootstrapping effect could be strengthened by providing more insights into the convergence properties of the algorithm and the conditions under which it is guaranteed to improve performance.]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1. The theoretical analysis is limited to binary rewards.

3. Literature Gap Analysis:
   - The paper does not cite theoretical works analyzing policy optimization with more general reward functions in the context of iterative refinement.

4. Validation Analysis:
   - Valid. The theoretical analysis is limited to binary rewards.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The theoretical analysis in Section 3.2.4 explicitly uses a binary reward function.

1. Weakness Statement:
[How does iGRPO perform on tasks that require multi-step reasoning or planning? Are there any specific challenges or limitations in applying iGRPO to such tasks?]

2. Evidence Collection:
a) Method-related Evidence:
   - The method description in Section 3.2 is general and does not inherently restrict its application to single-step reasoning tasks.

b) Experiment-related Evidence:
   - The experiments in Section 4 focus on tasks that can be evaluated with a single pass or a binary outcome (pass/fail). There are no experiments on tasks requiring multi-step reasoning or planning.

3. Literature Gap Analysis:
   - The paper does not cite or compare against methods specifically designed for multi-step reasoning.

4. Validation Analysis:
   - The reviewer raises a valid point. The paper does not provide evidence on the performance of iGRPO on tasks requiring multi-step reasoning or planning. The current experiments focus on tasks with relatively clear single-step solutions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experiments section does not include tasks requiring multi-step reasoning or planning.

1. Weakness Statement:
[How sensitive is iGRPO to the quality of the initial model? Would using a pre-trained model with a lower performance on the target task still yield improvements with iGRPO?]

2. Evidence Collection:
a) Method-related Evidence:
   - The method description in Section 3.2 is independent of the initial model's quality.

b) Experiment-related Evidence:
   - The paper uses pre-trained models (DeepSeek-R1-Distill, DeepSeek-R1, DeepSeek-R2, DeepSeek-R1-Distill-8K, OpenMath-Nem, OpenMath-Nem-Distill, OpenReasoning-Nem).
   - The paper does not systematically evaluate the sensitivity of iGRPO to the initial model's performance.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the sensitivity of iterative refinement methods to the initial model's quality.

4. Validation Analysis:
   - The reviewer's question is valid. The paper does not provide a systematic analysis of how the initial model's quality affects the performance of iGRPO.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks experiments or analysis on the sensitivity of iGRPO to the initial model's performance.

1. Weakness Statement:
[What are the potential limitations of iGRPO in terms of scalability to larger models or datasets? Are there any specific challenges in applying iGRPO to more complex tasks?]

2. Evidence Collection:
a) Method-related Evidence:
   - The method description in Section 3.2 is general and does not inherently restrict its scalability.

b) Experiment-related Evidence:
   - The paper presents results for models up to 14B parameters.
   - The paper does not provide a detailed analysis of the challenges of scaling iGRPO to much larger models or more complex tasks.

3. Literature Gap Analysis:
   - The paper does not cite works discussing the scalability limitations of iterative refinement methods.

4. Validation Analysis:
   - The reviewer raises a valid concern. While the paper shows results for a 14B parameter model, it does not delve into the potential challenges and limitations of scaling iGRPO to even larger models or more complex tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a detailed discussion on the scalability limitations of iGRPO.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Iterative Group Relative Policy Optimization (iGRPO), an extension of the Group Relative Policy Optimization (GRPO) method, designed to enhance the reasoning capabilities of large language models (LLMs). While GRPO optimizes language models through group-based relative rewards, iGRPO adds a self-feedback mechanism by iteratively refining drafts through a two-stage process. The first stage samples multiple responses and selects the highest-scoring one, which then serves as feedback for the second stage, where the model conditions on this best draft and applies further refinement. This iterative approach aims to improve the model's performance in complex reasoning tasks, particularly in mathematical problem-solving. The authors provide a comprehensive empirical evaluation of iGRPO across various benchmarks and model sizes, demonstrating consistent improvements over baseline methods. Additionally, the paper includes a theoretical analysis of the bootstrapping effect, which explains how iGRPO improves the model's performance over time. The core contribution of this work lies in its simple yet effective extension of GRPO, which leverages self-feedback to enhance the model's ability to self-correct and improve its reasoning capabilities. The authors demonstrate the effectiveness of iGRPO through extensive experiments on mathematical reasoning benchmarks, showing that it consistently outperforms GRPO and other self-improvement methods. The paper also includes ablation studies to validate the design choices and the impact of different components of iGRPO. The authors also explore the use of a generative judge and analyze the learning dynamics of the algorithm. Overall, this paper presents a valuable contribution to the field of LLM optimization, providing a simple yet effective method for improving the reasoning capabilities of these models. However, as I will discuss in the following sections, there are several limitations that warrant further investigation.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I found several aspects of this paper to be particularly strong. First, the core idea of iGRPO, which involves iteratively refining drafts using a self-feedback mechanism, is both simple and elegant. The method is easy to implement and integrate into existing training pipelines, making it a practical approach for improving the reasoning capabilities of LLMs. The two-stage process, where the model first selects the best draft and then conditions on it for further refinement, is a clever way to leverage the model's own output to guide the learning process. This approach is particularly effective in tasks that require iterative refinement, such as mathematical reasoning. Second, the empirical evaluation of iGRPO is comprehensive and convincing. The authors conduct extensive experiments across multiple benchmarks and model sizes, demonstrating consistent improvements over baseline methods. The results are well-supported by ablation studies, which validate the effectiveness of different components of iGRPO, such as the use of a generative judge and the impact of self-feedback on learning dynamics. The authors also provide a detailed comparison of iGRPO with other self-improvement methods, further highlighting the advantages of their approach. The inclusion of a theoretical analysis of the bootstrapping effect is another strength of the paper. This analysis provides a deeper understanding of the underlying mechanisms that contribute to the performance improvements of iGRPO, explaining how the iterative conditioning on the best draft leads to enhanced reasoning capabilities. The authors also provide a clear and well-organized presentation of their method and results, making it easy for readers to understand and follow their work. Finally, the paper is well-written and organized, with clear explanations of the proposed method and its implementation. The authors also provide a thorough discussion of the related work, placing their contribution in the context of existing research. Overall, I believe that this paper makes a significant contribution to the field of LLM optimization, providing a valuable method for improving the reasoning capabilities of these models.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper lacks a detailed analysis of the computational overhead introduced by the two-stage process of iGRPO. While the authors claim that the compute cost is comparable to GRPO, a more granular breakdown of the time and resources required for each stage would be beneficial. Specifically, the cost of generating multiple responses in the first stage and the subsequent refinement in the second stage should be quantified, as well as the impact on training time and memory usage. This analysis should also consider the scaling behavior of the method with respect to model size and dataset size. The authors state in Section 4.1 that they keep the total sampling budget fixed at eight completions per prompt for every method, and that iGRPO redistributes this budget across Stage 1 and Stage 2 rather than increasing them. While this ensures a fair compute comparison, it does not provide a detailed breakdown of the time taken for each stage or the memory usage. This lack of detailed analysis makes it difficult to assess the practical trade-offs involved in using iGRPO. My confidence in this weakness is high, as the paper does not provide any data on the time taken for each stage or memory usage, relying on a fixed sampling budget for performance comparison. Second, the theoretical analysis is limited to the case of binary rewards, which may not fully capture the complexities of real-world reasoning tasks. The analysis in Section 3.2.4 focuses on a binary reward function, where the reward is 1 if the generated solution is correct and 0 otherwise. This analysis does not fully capture the complexities of real-world reasoning tasks, which often involve continuous or more complex reward structures. Furthermore, the theoretical justification for the bootstrapping effect could be strengthened by providing more insights into the convergence properties of the algorithm and the conditions under which it is guaranteed to improve performance. The paper does not cite theoretical works that analyze policy optimization with more general reward functions in the context of iterative refinement. My confidence in this weakness is high, as the theoretical analysis in Section 3.2.4 explicitly uses a binary reward function, and there is no discussion of more general reward functions or convergence properties. Third, the paper primarily focuses on mathematical reasoning tasks, and it is unclear how well iGRPO generalizes to other types of reasoning tasks, such as logical reasoning or commonsense reasoning. The authors do not provide any evidence or discussion on the applicability of iGRPO to a broader range of reasoning tasks. The experiments in Section 4 focus on mathematical benchmarks: AIME24, AIME25, MATH500, AMC23, GSM8K, Minerva Math, and GPQA. There are no experiments on logical or commonsense reasoning tasks. My confidence in this weakness is high, as the experiments section only includes mathematical reasoning benchmarks. Fourth, the paper does not provide a detailed analysis of the computational cost of iGRPO compared to GRPO. While the authors claim that the compute cost is comparable, a more thorough comparison of the training time and resource requirements would be helpful for practitioners who want to adopt this method. This lack of detailed computational analysis makes it difficult to assess the practical trade-offs involved in using iGRPO. My confidence in this weakness is high, as the paper lacks specific data on training time and resource requirements, relying on a fixed sampling budget for performance comparison. Fifth, the paper could benefit from a more in-depth discussion of the limitations of iGRPO and potential areas for future research. For example, the authors could discuss the potential for the method to get stuck in local optima, or the sensitivity of the method to the choice of hyperparameters. Furthermore, the authors could discuss the potential for the method to amplify biases present in the training data. The paper does not include a dedicated section or detailed discussion on the limitations of the proposed method. My confidence in this weakness is high, as the paper does not include a dedicated section or detailed discussion on the limitations of the proposed method. Sixth, the paper does not provide evidence on the performance of iGRPO on tasks requiring multi-step reasoning or planning. The current experiments focus on tasks with relatively clear single-step solutions. The paper does not include any experiments on tasks that require multi-step reasoning or planning. My confidence in this weakness is high, as the experiments section does not include tasks requiring multi-step reasoning or planning. Seventh, the paper does not provide a systematic analysis of how the initial model's quality affects the performance of iGRPO. The paper uses pre-trained models, but it does not systematically evaluate the sensitivity of iGRPO to the initial model's performance. My confidence in this weakness is high, as the paper lacks experiments or analysis on the sensitivity of iGRPO to the initial model's performance. Finally, the paper lacks a detailed discussion on the scalability limitations of iGRPO. While the paper shows results for a 14B parameter model, it does not delve into the potential challenges and limitations of scaling iGRPO to much larger models or more complex tasks. My confidence in this weakness is high, as the paper lacks a detailed discussion on the scalability limitations of iGRPO.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a more detailed analysis of the computational costs associated with the two-stage process of iGRPO. This analysis should include a quantification of the time and resources required for each stage, as well as the impact on training time and memory usage. This analysis should also consider the scaling behavior of the method with respect to model size and dataset size. For example, it would be useful to know how the number of samples needed in each stage scales with the model size and the complexity of the task. Furthermore, the authors should provide a more detailed comparison of the computational cost of iGRPO with GRPO, including a comparison of the number of forward passes, the memory usage, and the overall training time. This analysis should also consider the impact of different hardware configurations on the performance of iGRPO. Second, to strengthen the theoretical underpinnings of iGRPO, the authors should extend their analysis to more general reward functions beyond the binary case. This could involve analyzing the convergence properties of the algorithm under different reward structures and identifying the conditions under which it is guaranteed to improve performance. Furthermore, it would be beneficial to investigate the relationship between the reward function, the policy update rule, and the convergence behavior of the algorithm. This could involve analyzing the properties of the objective function and the gradient updates, and providing theoretical guarantees on the performance improvement. Third, the authors should expand their evaluation to include a wider range of reasoning tasks beyond mathematical problem-solving. Specifically, incorporating benchmarks that assess logical reasoning, such as those involving symbolic manipulation or deductive inference, would provide a more comprehensive understanding of iGRPO's capabilities. Furthermore, evaluating iGRPO on tasks that require common-sense reasoning, such as those involving everyday scenarios or implicit knowledge, would help to determine its applicability to real-world problems. This could involve using datasets that test the model's ability to reason about entities, relationships, and events that are not explicitly stated in the training data. Such an analysis would provide a more complete picture of the strengths and weaknesses of the proposed method. Fourth, the authors should include a more granular breakdown of the training time and resource requirements for iGRPO compared to GRPO. This should include a comparison of the number of forward passes, the memory usage, and the overall training time for different model sizes. It would be beneficial to present this information in a table or graph, allowing readers to easily compare the computational cost of the two methods. Additionally, the authors should discuss the scalability of iGRPO to larger models and datasets, and identify any potential bottlenecks that might arise when applying the method to more complex tasks. Fifth, the authors should include a more thorough discussion of the limitations of iGRPO and potential avenues for future research. This could include exploring the impact of different hyperparameters on the performance of iGRPO, such as the number of drafts sampled in each stage and the learning rate. It would also be valuable to investigate the sensitivity of iGRPO to the quality of the initial model and the potential for the method to get stuck in local optima. Furthermore, the authors could discuss the potential for extending iGRPO to other optimization algorithms beyond GRPO, and explore the possibility of using different types of conditioning in the second stage of the method. Sixth, the authors should evaluate iGRPO on tasks that require multi-step reasoning or planning. This would provide a more comprehensive understanding of the method's capabilities and limitations. Seventh, the authors should conduct a systematic analysis of how the initial model's quality affects the performance of iGRPO. This could involve using pre-trained models with varying performance on the target task and evaluating the performance of iGRPO on these models. Finally, the authors should include a more detailed discussion of the scalability limitations of iGRPO and potential challenges in applying it to much larger models or more complex tasks. This could involve analyzing the computational cost of iGRPO as the model size and dataset size increase, and identifying any potential bottlenecks that might arise when applying the method to more complex tasks.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the performance of iGRPO scale with the size of the model and the dataset? Are there any limitations in terms of computational resources or training time? The paper presents results for models up to 14B parameters, but it would be valuable to understand how iGRPO performs with even larger models and on larger datasets. Second, can the authors provide more insights into the choice of the number of samples in each stage of iGRPO? How does this choice affect the performance and computational cost? The paper claims that the compute cost is comparable to GRPO, but it does not provide a detailed analysis of how the number of samples in each stage affects the performance and computational cost. Third, the paper focuses on mathematical reasoning tasks. How well does iGRPO generalize to other types of reasoning tasks, such as logical reasoning or commonsense reasoning? The paper does not provide any evidence or discussion on the applicability of iGRPO to a broader range of reasoning tasks. Fourth, how sensitive is iGRPO to the quality of the initial model? Would using a pre-trained model with a lower performance on the target task still yield improvements with iGRPO? The paper does not systematically evaluate the sensitivity of iGRPO to the initial model's performance. Fifth, what are the potential limitations of iGRPO in terms of scalability to larger models or datasets? Are there any specific challenges in applying iGRPO to more complex tasks? The paper lacks a detailed discussion on the scalability limitations of iGRPO. Sixth, how does iGRPO perform on tasks that require multi-step reasoning or planning? The current experiments focus on tasks with relatively clear single-step solutions. Seventh, how does the performance of iGRPO compare to other self-improvement methods, such as self-verification or critique-based learning, on tasks that require multi-step reasoning? The paper focuses on mathematical reasoning tasks, and it would be valuable to understand how iGRPO compares to other self-improvement methods on more complex tasks. Finally, what are the potential limitations of iGRPO in terms of amplifying biases present in the training data? The paper does not discuss the potential for iGRPO to amplify biases present in the training data.


## Rating:

6.5


## Confidence:

3.25


## Decision:

Accept
}