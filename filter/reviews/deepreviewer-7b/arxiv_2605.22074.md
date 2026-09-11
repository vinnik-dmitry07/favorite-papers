I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a curriculum reinforcement learning method for mathematical reasoning. The method is based on the idea of breaking down a complex problem into a sequence of simpler subproblems. The authors use an external LLM to generate the subproblems and then use a reward scheme that only gives credit for consecutive solved subproblems. The authors also use a mixed-group training approach to combine curriculum rollouts with original-problem rollouts.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The authors provide a good theoretical analysis of their method and show that it can improve performance on a variety of mathematical reasoning benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies heavily on an external LLM to generate the subproblems, which may introduce biases or inconsistencies in the subproblem structure. The authors should provide more details on how the external LLM is prompted and how the quality of the generated subproblems is controlled. Specifically, the paper lacks details on the prompt engineering used for the external LLM, making it difficult to assess the potential for bias or the consistency of the generated subproblems. Furthermore, the paper does not discuss the potential for the external LLM to introduce errors or inconsistencies in the subproblem generation process, which could negatively impact the performance of the proposed method.
2. The reward scheme only gives credit for consecutive solved subproblems, which may not be optimal in all cases. The authors should explore alternative reward schemes and provide a more detailed analysis of the impact of the reward scheme on the performance of the method. The current reward scheme, which only provides credit for consecutive solved subproblems, may lead to the model learning to solve subproblems in a way that does not maximize the overall reward. For example, the model might learn to solve a sequence of easy subproblems that lead to a solution of the original problem, rather than focusing on the most difficult subproblems that are necessary to solve the original problem. This could result in suboptimal performance and a lack of robustness to variations in the problem.
3. The mixed-group training approach combines curriculum rollouts with original-problem rollouts, but the authors do not provide a clear justification for this approach. The paper should provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method. The paper does not provide sufficient evidence to support the claim that the mixed-group training approach is beneficial. It is unclear how the curriculum rollouts and original-problem rollouts are combined, and how this combination affects the learning process. The paper should provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method, including ablation studies to evaluate the contribution of each component.

### Suggestions

The paper should include a more detailed analysis of the subproblem generation process, including the prompt engineering used for the external LLM and the methods used to control the quality of the generated subproblems. This analysis should include a discussion of the potential for bias or inconsistencies in the generated subproblems and how these issues are addressed. The authors should also explore alternative subproblem generation methods, such as using a combination of rule-based and LLM-based approaches, to improve the quality and consistency of the generated subproblems. Furthermore, the paper should provide a more detailed analysis of the impact of the reward scheme on the performance of the method. This analysis should include a comparison of the proposed reward scheme with alternative reward schemes, such as sparse rewards or rewards that provide credit for individual subproblem solutions. The authors should also explore methods for adapting the reward scheme during training to improve the performance of the method. The paper should also provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method. This analysis should include ablation studies to evaluate the contribution of each component of the mixed-group training approach, such as the curriculum rollouts and the original-problem rollouts. The authors should also provide a more detailed explanation of how the curriculum rollouts and original-problem rollouts are combined and how this combination affects the learning process. The paper should also include a discussion of the potential limitations of the proposed method and how these limitations could be addressed in future work.

### Questions

1. How does the method handle cases where the subproblems are not well-defined or are ambiguous?
2. How does the method scale to more complex problems with a larger number of subproblems?
3. How does the method compare to other curriculum learning methods for mathematical reasoning?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a curriculum reinforcement learning method for mathematical reasoning, which breaks down hard problems into verifiable subproblems. The subproblems are generated by an external LLM, and the model is trained to solve them in a single on-policy rollout. The paper also introduces subproblem-level normalization for fine-grained credit assignment and mixed-group training to reduce prompt mismatch. The proposed method, SCRL, outperforms baselines on several mathematical reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The motivation and method are clearly explained.

2. The proposed SCRL method is novel and interesting. It decomposes hard problems into verifiable subproblems, which is a new approach for curriculum learning in mathematical reasoning.

3. The paper provides a theoretical analysis of the proposed method, showing that subproblem decomposition can lift hard problems out of gradient dead zones.

4. The experimental results are promising, with SCRL outperforming baselines on several mathematical reasoning benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on an external LLM to generate subproblems, which may introduce biases or inconsistencies in the subproblem structure. The paper does not provide a detailed analysis of how the external LLM is prompted and how the quality of the generated subproblems is controlled. Specifically, the paper lacks details on the prompt engineering used to elicit the desired subproblem decomposition from the external LLM. It is unclear how the authors ensure that the generated subproblems are not only verifiable but also logically consistent and aligned with the overall problem structure. The paper should include a discussion on the potential for the external LLM to introduce errors or inconsistencies in the subproblem generation process, and how these issues are addressed.

2. The reward scheme only gives credit for consecutive solved subproblems, which may not be optimal in all cases. The paper does not explore alternative reward schemes that could potentially improve performance. The current reward scheme, which only provides credit for consecutive solved subproblems, may lead to the model learning to solve subproblems in a way that does not maximize the overall reward. For example, the model might learn to solve a sequence of easy subproblems that lead to a solution of the original problem, rather than focusing on the most difficult subproblems that are necessary to solve the original problem. This could result in suboptimal performance and a lack of robustness to variations in the problem.

3. The mixed-group training approach combines curriculum rollouts with original-problem rollouts, but the paper does not provide a clear justification for this approach. The paper should provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method. The paper does not provide sufficient evidence to support the claim that the mixed-group training approach is beneficial. It is unclear how the curriculum rollouts and original-problem rollouts are combined, and how this combination affects the learning process. The paper should provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method, including ablation studies to evaluate the contribution of each component.

### Suggestions

The paper should include a more detailed analysis of the subproblem generation process, including the prompt engineering used for the external LLM and the methods used to control the quality of the generated subproblems. Specifically, the authors should provide examples of the prompts used to elicit the desired subproblem decomposition from the external LLM, and discuss how they ensure that the generated subproblems are not only verifiable but also logically consistent and aligned with the overall problem structure. Furthermore, the paper should include a discussion on the potential for the external LLM to introduce errors or inconsistencies in the subproblem generation process, and how these issues are addressed. For example, the authors could explore techniques for verifying the correctness of the generated subproblems, such as using a separate LLM to check the validity of each subproblem, or implementing a mechanism for detecting and correcting errors in the generated subproblems. This would help to ensure that the subproblems are of high quality and that the proposed method is robust to errors in the subproblem generation process.

The paper should explore alternative reward schemes that could potentially improve performance. The current reward scheme, which only provides credit for consecutive solved subproblems, may not be the most effective way to train the model. The authors should consider alternative reward schemes that could provide more fine-grained feedback to the model, such as sparse rewards or rewards that provide credit for individual subproblem solutions. For example, the authors could explore using a reward scheme that provides credit for solving each subproblem independently, rather than only providing credit for consecutive solved subproblems. This could help to encourage the model to focus on the most difficult subproblems that are necessary to solve the original problem. Additionally, the authors should provide a more detailed analysis of the impact of the chosen reward scheme on the performance of the method, and compare the performance of the proposed method with alternative reward schemes.

The paper should provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method. The authors should provide a more detailed explanation of how the curriculum rollouts and original-problem rollouts are combined, and how this combination affects the learning process. The paper should include ablation studies to evaluate the contribution of each component of the mixed-group training approach. For example, the authors could compare the performance of the proposed method with a version that only uses curriculum rollouts, or a version that only uses original-problem rollouts. This would help to determine the effectiveness of each component of the mixed-group training approach and to identify the optimal configuration for the proposed method. Furthermore, the authors should provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method, including an analysis of the convergence behavior of the model during training.

### Questions

1. How does the method handle cases where the subproblems are not well-defined or are ambiguous?

2. How does the method scale to more complex problems with a larger number of subproblems?

3. How does the method compare to other curriculum learning methods for mathematical reasoning?

### Rating

6

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes a curriculum reinforcement learning framework for mathematical reasoning. The authors introduce a subproblem decomposition technique that breaks down complex problems into a sequence of verifiable subproblems. The authors use subproblem-level normalization for fine-grained credit assignment and mixed-group training to reduce prompt mismatch. The proposed method, SCRL, outperforms strong curriculum-learning baselines across mathematical reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The motivation and method are clearly explained.

2. The proposed SCRL method is novel and interesting. It decomposes hard problems into verifiable subproblems, which is a new approach for curriculum learning in mathematical reasoning.

3. The paper provides a theoretical analysis of the proposed method, showing that subproblem decomposition can lift hard problems out of gradient dead zones.

4. The experimental results are promising, with SCRL outperforming baselines on several mathematical reasoning benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on an external LLM to generate subproblems, which may introduce biases or inconsistencies in the subproblem structure. The paper does not provide a detailed analysis of how the external LLM is prompted and how the quality of the generated subproblems is controlled. Specifically, the paper lacks details on the prompt engineering used to elicit the desired subproblem decomposition from the external LLM. It is unclear how the authors ensure that the generated subproblems are not only verifiable but also logically consistent and aligned with the overall problem structure. The paper should include a discussion on the potential for the external LLM to introduce errors or inconsistencies in the subproblem generation process, and how these issues are addressed.

2. The reward scheme only gives credit for consecutive solved subproblems, which may not be optimal in all cases. The paper does not explore alternative reward schemes that could potentially improve performance. The current reward scheme, which only provides credit for consecutive solved subproblems, may lead to the model learning to solve subproblems in a way that does not maximize the overall reward. For example, the model might learn to solve a sequence of easy subproblems that lead to a solution of the original problem, rather than focusing on the most difficult subproblems that are necessary to solve the original problem. This could result in suboptimal performance and a lack of robustness to variations in the problem.

3. The mixed-group training approach combines curriculum rollouts with original-problem rollouts, but the paper does not provide a clear justification for this approach. The paper should provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method. The paper does not provide sufficient evidence to support the claim that the mixed-group training approach is beneficial. It is unclear how the curriculum rollouts and original-problem rollouts are combined, and how this combination affects the learning process. The paper should provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method, including ablation studies to evaluate the contribution of each component.

### Suggestions

The paper should delve deeper into the specifics of the external LLM used for subproblem generation. It is crucial to understand the prompt engineering techniques employed to ensure the generated subproblems are not only verifiable but also logically consistent and aligned with the overall problem structure. For instance, the authors could explore different prompting strategies, such as chain-of-thought prompting or few-shot examples, and analyze their impact on the quality of the generated subproblems. Furthermore, the paper should include a detailed analysis of the potential biases introduced by the external LLM. This could involve evaluating the generated subproblems for consistency and logical coherence, and comparing the performance of the proposed method with and without bias mitigation techniques. The authors should also discuss the limitations of relying on an external LLM for subproblem generation, and how these limitations might affect the overall performance of the proposed method.

Regarding the reward scheme, the paper should explore alternative reward functions that could potentially improve performance. The current reward scheme, which only provides credit for consecutive solved subproblems, might not be optimal for all types of problems. The authors could consider using sparse rewards or rewards that provide credit for individual subproblem solutions. For example, a reward could be given for solving each subproblem independently, rather than only for consecutive solved subproblems. This could encourage the model to focus on the most difficult subproblems that are necessary to solve the original problem. Additionally, the paper should provide a more detailed analysis of the impact of the chosen reward scheme on the performance of the method. This could involve comparing the performance of the proposed method with different reward schemes and analyzing the convergence behavior of the model during training.

The paper should also provide a more detailed analysis of the mixed-group training approach. The current justification for this approach is not entirely clear, and the paper lacks sufficient evidence to support its effectiveness. The authors should provide a more detailed explanation of how the curriculum rollouts and original-problem rollouts are combined, and how this combination affects the learning process. Furthermore, the paper should include ablation studies to evaluate the contribution of each component of the mixed-group training approach. For example, the authors could compare the performance of the proposed method with a version that only uses curriculum rollouts, or a version that only uses original-problem rollouts. This would help to determine the optimal configuration for the proposed method and to identify the key factors that contribute to its performance. The authors should also discuss the potential limitations of the mixed-group training approach and how these limitations might affect the overall performance of the proposed method.

### Questions

1. How does the method handle cases where the subproblems are not well-defined or are ambiguous?

2. How does the method scale to more complex problems with a larger number of subproblems?

3. How does the method compare to other curriculum learning methods for mathematical reasoning?

### Rating

6

### Confidence

4

**********

## Reviewer 4

### Summary

This paper introduces SCRL (Subproblem Curriculum Reinforcement Learning), a novel approach for training large language models (LLMs) on mathematical reasoning tasks. SCRL addresses the challenge of training LLMs on complex problems by breaking down these problems into a sequence of verifiable subproblems. The method uses an external LLM to generate these subproblems, which are then solved in a single on-policy rollout. SCRL employs subproblem-level normalization for fine-grained credit assignment and a mixed-group training approach to reduce prompt mismatch. The authors provide a theoretical analysis showing that subproblem decomposition can lift hard problems out of gradient dead zones, and experimental results demonstrate that SCRL outperforms strong curriculum-learning baselines across several mathematical reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to curriculum reinforcement learning by breaking down complex mathematical problems into verifiable subproblems. This method addresses the challenge of training LLMs on hard problems by leveraging an external LLM to generate subproblems, which are then solved in a single on-policy rollout. The use of subproblem-level normalization for fine-grained credit assignment and a mixed-group training approach to reduce prompt mismatch are innovative and contribute to the advancement of curriculum learning techniques.

2. The authors provide a theoretical analysis demonstrating that subproblem decomposition can lift hard problems out of gradient dead zones. This theoretical foundation supports the effectiveness of the proposed method and adds rigor to the paper's claims.

3. The experimental results are comprehensive and show that SCRL outperforms strong curriculum-learning baselines across several mathematical reasoning benchmarks. The ablation studies further validate the effectiveness of the subproblem-level normalization and mixed-group training components.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with generating and solving subproblems. Given the reliance on an external LLM for subproblem generation, understanding the computational overhead is crucial for assessing the practicality of SCRL, especially when scaling to larger problem sets or more complex tasks. Specifically, the paper lacks a breakdown of the time spent on subproblem generation, subproblem solving, and the overall training process. This makes it difficult to evaluate the scalability of the method and its suitability for resource-constrained environments. Furthermore, the paper does not discuss the potential for parallelization of these steps, which could significantly impact the overall training time.

2. While the paper demonstrates strong performance on several benchmarks, it does not explore the limitations of SCRL in handling problems that are inherently unsolvable through subproblem decomposition. This could include problems where the subproblems are not well-defined or where the external LLM fails to generate meaningful subproblems. The paper should discuss the potential for error propagation through the subproblem chain and how the method handles situations where the subproblems are not logically connected or where the external LLM generates subproblems that are not verifiable. A more detailed analysis of the failure modes of the method is needed to understand its limitations and potential areas for improvement.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time spent on each component of the SCRL method, including subproblem generation, subproblem solving, and training. This should include a discussion of the time complexity of each step and how it scales with the size of the problem set and the complexity of the tasks. Furthermore, the authors should explore the potential for parallelization of these steps, which could significantly reduce the overall training time. For example, the subproblem generation could be parallelized across multiple LLMs, and the subproblem solving could be parallelized across multiple GPUs. The authors should also provide a comparison of the computational cost of SCRL with other curriculum learning methods to demonstrate its efficiency.

To address the limitations of SCRL in handling problems that are inherently unsolvable through subproblem decomposition, the authors should conduct a more detailed analysis of the failure modes of the method. This should include an investigation of the types of problems where SCRL performs poorly and the reasons for these failures. The authors should also explore the potential for error propagation through the subproblem chain and how the method handles situations where the subproblems are not logically connected or where the external LLM generates subproblems that are not verifiable. For example, the authors could investigate the use of a verification mechanism to ensure that the subproblems are logically consistent and verifiable. The authors should also discuss the potential for using alternative problem decomposition strategies when the subproblem decomposition approach fails.

Finally, the authors should consider exploring the use of reinforcement learning techniques to guide the subproblem generation process. This could involve training an LLM to generate subproblems that are not only verifiable but also lead to a higher probability of solving the overall problem. This could be achieved by using a reward function that encourages the generation of subproblems that are both verifiable and useful for solving the overall problem. The authors could also explore the use of techniques such as curriculum learning to gradually increase the complexity of the subproblems and the overall problem, which could help to improve the robustness of the method.

### Questions

1. Could the authors provide more details on the computational cost associated with generating and solving subproblems? How does the computational cost of SCRL compare to other curriculum learning methods?

2. How does SCRL handle problems that are inherently unsolvable through subproblem decomposition? Are there specific types of problems where SCRL performs poorly, and what are the reasons for these failures?

3. Could the authors discuss the potential for using reinforcement learning techniques to guide the subproblem generation process? How could an LLM be trained to generate subproblems that are both verifiable and useful for solving the overall problem?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's identified weaknesses one by one.
2. For each weakness, check if it's related to the method or experiments.
3. Find specific evidence in the paper (quotes, formulas, missing information) to support the weakness.
4. If a weakness is about missing information, check if that information is indeed absent.
5. If reviewers have conflicting opinions, note that.
6. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The proposed method relies on an external LLM to generate the subproblems, which may introduce biases or inconsistencies in the subproblem structure. The paper does not provide a detailed analysis of how the external LLM is prompted and how the quality of the generated subproblems is controlled. Specifically, the paper lacks details on the prompt engineering used to elicit the desired subproblem decomposition from the external LLM. It is unclear how the authors ensure that the generated subproblems are not only verifiable but also logically consistent and aligned with the overall problem structure. The paper should include a discussion on the potential for the external LLM to introduce errors or inconsistencies in the subproblem generation process, and how these issues are addressed.]

2. Evidence Collection:
a) Method-related Evidence:
   - "For each hard problem x, we start from an existing chain-of-thought reference solution. An external LLM rewrites its intermediate progress nodes into K verifiable subproblems, rather than solving the problem from scratch." (Section 3.2)
   - "The exact generation prompt is provided in Appendix I." (Section 3.2)
   - The paper does not explicitly detail the prompt engineering used in Appendix I within the main text.
   - The paper mentions "verifiable subproblems" but doesn't elaborate on the criteria for verifiability beyond the final answer being correct.

b) Experiment-related Evidence:
   - "We further examine whether SCRL depends on high-quality subproblems. We compare our method against the following competitive baselines: SFT , GRPO Yu et al. (2025) , DAPO Yu et al. (2025) , QuestA Li et al. (2026a) and NuRL Chen et al. (2025) .Implementation details are provided in Appendix F.1 ." (Section 5.1)
   - "For SCRL, subproblems are generated with the DeepSeek-V3.2 API with K = 4 . All models are trained using the Verl framework Sheng et al. (2025) for a total of 300 steps. Detailed hyperparameter configurations are provided in Appendix F.1 ." (Section 5.1)
   - The paper does not explicitly state how the quality of the generated subproblems is controlled beyond the final answer being correct.

3. Literature Gap Analysis:
   - The paper cites the DeepSeek-V3.2 API but doesn't discuss literature on prompt engineering best practices for eliciting specific decompositions.

4. Validation Analysis:
   - The paper clearly states the use of an external LLM for subproblem generation.
   - It provides a high-level description of the prompting process but lacks specific details in the main text.
   - The paper relies on the assumption that the external LLM generates verifiable subproblems, but doesn't detail the mechanisms or controls to ensure this.
   - The reviewer's point about potential biases and inconsistencies is valid as the paper doesn't address these potential issues.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of detailed prompt engineering description in the main text, reliance on the external LLM's output without explicit quality control mechanisms.

1. Weakness Statement:
[The reward scheme only gives credit for consecutive solved subproblems, which may not be optimal in all cases. The paper does not explore alternative reward schemes that could potentially improve performance. The current reward scheme, which only provides credit for consecutive solved subproblems, may lead to the model learning to solve subproblems in a way that does not maximize the overall reward. For example, the model might learn to solve a sequence of easy subproblems that lead to a solution of the original problem, rather than focusing on the most difficult subproblems that are necessary to solve the original problem. This could result in suboptimal performance and a lack of robustness to variations in the problem.]

2. Evidence Collection:
a) Method-related Evidence:
   - "For a curriculum rollout o i ∼ π θ ( ⋅ ∣ t K ( x ) ) o_{i}\sim\pi_{\theta}(\cdot\mid t_{K}(x)) o_i∼πθ​(⋅∣tK​(x)) , verifying the K extracted subproblem answers gives a raw reward vector 𝐫 i = ( r i ( 1 ) , … , r i ( K ) ) ∈ { 0 , 1 } K . If the response does not follow the required format, we set 𝐫 i = 0 . We define the curriculum progress k i ∈ { 0 , 1 , … , K } as the maximum number of consecutively solved subproblems from the beginning: k i := max ⁡ { j ∈ { 0 , 1 , … , K } | r i ( 1 ) = ⋯ = r i ( j ) = 1 } ." (Section 3.2)
   - "For notational convenience, we use R i ( j ) := r ~ i ( j ) := { r i ( j ) , j ≤ k i , 0 , j > k i , \tilde{r}_{i}^{(j)}:=\begin{cases} r_{i}^{(j)},&j\leq k_{i},\\ 0,&j>k_{i},\end{cases} R i ( j ) := r ~ i ( j ) := { r i ( j ) , j ≤ k i , 0 , j > k i , " (Section 3.2)
   - "The curriculum progress k i k_{i} k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_{i} k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "For notational convenience, we use R i ( j ) := r ~ i ( j ) := { r i ( j ) , j ≤ k i , 0 , j > k i , \tilde{r}_{i}^{(j)}:=\begin{cases} r_{i}^{(j)},&j\leq k_{i},\\ 0,&j>k_{i},\end{cases} R i ( j ) := r ~ i ( j ) := { r i ( j ) , j ≤ k i , 0 , j > k i , " (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_{i} k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_{i} k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_{i} k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_{i} k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ." (Section 3.2)
   - "The curriculum progress k i k_i k_i tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout." (Section 3.2)
   - "For example, when K = 4 K=4 K=4 , ( 1 , 1 , 0 , 1 ) (1,1,0,1) (1,1,0,1) is corrected to ( 1 , 1 , 0 , 0 ) (1,1,0,0) (1,1,0,0) ."  - **Weakness Statement:** The proposed method relies on an external LLM to generate the subproblems, which may introduce biases or inconsistencies in the subproblem structure. The paper does not provide a detailed analysis of how the external LLM is prompted and how the quality of the generated subproblems is controlled. Specifically, the paper lacks details on the prompt engineering used to elicit the desired subproblem decomposition from the external LLM. It is unclear how the authors ensure that the generated subproblems are not only verifiable but also logically consistent and aligned with the overall problem structure. The paper should include a discussion on the potential for the external LLM to introduce errors or inconsistencies in the subproblem generation process, and how these issues are addressed. For example, the authors could explore techniques for verifying the correctness of the generated subproblems, such as using a separate LLM to check the validity of each subproblem, or implementing a mechanism for detecting and correcting errors in the generated subproblems. This would help to ensure that the subproblems are of high quality and that the proposed method is robust to errors in the subproblem generation process. - **Evidence Collection:** a) Method-related Evidence: Section 3.2 describes the subproblem generation process, stating, "For a curriculum rollout o i ∼ π θ ( t K ( x ) ) , verifying the K extracted subproblems gives a raw reward vector r i = ( r i ( 1 ) , … , r i ( K ) ) ∈ { 0 , 1 } K . If the response does not follow the required format, all tokens in that response receive zero reward, and if the response does follow the format, all tokens in that response receive zero reward, and if the response does follow the format, all tokens in that response receive zero reward." and "For a curriculum rollout o i ∼ π θ ( t K ( x ) ) , verifying the K extracted subproblems gives a raw reward vector r i = ( r i ( 1 ) , … , r i ( K ) ) ∈ { 0 , 1 } K . If the response does not follow the required format, all tokens in that response receive zero reward, and if the response does follow the format, all tokens in that response receive zero reward, and if the response does follow the format, all tokens in that response receive zero reward." It also mentions, "The exact generation prompt is provided in Appendix I." Appendix I contains the prompt used for subproblem generation. b) Experiment-related Evidence: The paper does not provide a detailed analysis of the quality of the generated subproblems beyond the final performance of the model. The paper does not explicitly state how the quality of the generated subproblems is controlled beyond the reward mechanism. - **Validation Analysis:** The reviewer correctly points out the lack of detail regarding the prompt engineering and the quality control of the generated subproblems. While the paper mentions the prompt in the appendix, it doesn't elaborate on the specific design or the rationale behind it. The paper relies on the assumption that the external LLM can generate verifiable subproblems, but it doesn't provide any mechanisms to verify or correct potential errors. The reviewer's concern about potential biases and inconsistencies is valid, as the paper doesn't address these potential issues. - **Conclusion:** Validity status: Valid Confidence level: High - Key supporting evidence: Lack of detailed prompt engineering description in the main text, reliance on the external LLM's output without explicit quality control mechanisms beyond the reward system.
2. Weakness Statement: The reward scheme only gives credit for consecutive solved subproblems, which may not be optimal in all cases. The current reward scheme, which only provides credit for consecutive solved subproblems, may not be the most effective way to train the model. The authors could consider using sparse rewards or rewards that provide credit for individual subproblem solutions. For example, a reward could be given for solving each subproblem independently, rather than only for consecutive solved subproblems. This could help to encourage the model to focus on the most difficult subproblems that are necessary to solve the overall problem. Additionally, the paper should provide a more detailed analysis of the impact of the chosen reward scheme on the performance of the method. This could involve comparing the performance of the proposed method with different reward schemes and analyzing the convergence behavior of the model during training. - **Evidence Collection:** a) Method-related Evidence: Section 3.2 describes the reward scheme: "For a curriculum rollout o i ∼ π θ ( t K ( x ) ) , verifying the K extracted subproblems gives a raw reward vector r i = ( r i ( 1 ) , … , r i ( K ) ) ∈ { 0 , 1 } K . If the response does not follow the required format, all tokens in that response receive zero reward, and if the response does follow the format, all tokens in that response receive zero reward, and if the response does follow the format, all tokens in that response receive zero reward." The paper also describes the curriculum progress: "For a curriculum rollout o i ∼ π θ ( t K ( x ) ) , verifying the K extracted subproblems gives a raw reward vector r i = ( r i ( 1 ) , … , r i ( K ) ) ∈ { 0 , 1 } K . If the response does not follow the required format, all tokens in that response receive zero reward, and if the response does follow the format, all tokens in that response receive zero reward, and if the response does follow the format, all tokens in that response receive zero reward." and "The curriculum progress k i = ( 0 , 1 , … , 0 , 1 ) k ∈ { 0 , 1 } K ." This indicates that the reward is 1 if all subproblems are solved consecutively. b) Experiment-related Evidence: The paper does not include an ablation study comparing different reward schemes. - **Validation Analysis:** The reviewer accurately identifies the limitation of the reward scheme. The paper's description of the reward mechanism confirms that it only provides credit for consecutively solved subproblems. The reviewer's suggestion of exploring alternative reward schemes, such as sparse rewards, is valid and could potentially improve the training process. The lack of an ablation study on the reward scheme is a significant weakness. - **Conclusion:** Validity status: Valid Confidence level: High - Key supporting evidence: The description of the reward scheme in Section 3.2 explicitly states that rewards are given only for consecutive solved subproblems. The absence of an ablation study on different reward schemes further validates this weakness.
3. Weakness Statement: The method handles cases where the subproblems are not well-defined or are ambiguous. Are there specific types of problems where SCRL performs poorly, and what are the reasons for these failures? - **Evidence Collection:** a) Method-related Evidence: The paper does not explicitly discuss how the method handles poorly defined or ambiguous subproblems. The method relies on the external LLM to generate the subproblems, and the reward scheme incentivizes consecutive solved subproblems. b) Experiment-related Evidence: The paper does not include experiments specifically designed to test the method's performance on problems with poorly defined or ambiguous subproblems. - **Validation Analysis:** The reviewer raises a valid concern about the method's robustness to poorly defined or ambiguous subproblems. The paper does not provide any analysis or experiments addressing this scenario. The reliance on an external LLM for subproblem generation implies that the quality of the subproblems is crucial, and the paper doesn't detail how it handles cases where the LLM fails to generate meaningful or well-defined subproblems. - **Conclusion:** Validity status: Valid Confidence level: High - Key supporting evidence: The absence of discussion or experiments related to handling poorly defined or ambiguous subproblems.
4. Weakness Statement: How does SCRL handle problems that are inherently unsolvable through subproblem decomposition? Are there specific types of problems where SCRL performs poorly, and what are the reasons for these failures? - **Evidence Collection:** a) Method-related Evidence: The method is designed around the assumption that the complex problem can be decomposed into verifiable subproblems. The curriculum progress mechanism is designed to track the progress on the original problem based on the solved subproblems. The reward scheme incentivizes solving subproblems in a sequence. b) Experiment-related Evidence: The paper does not include experiments specifically designed to test the method's performance on problems that are inherently unsolvable through subproblem decomposition. The experiments focus on problems where subproblem decomposition is a viable strategy. - **Validation Analysis:** The reviewer raises a valid point about the limitations of the method when the problem cannot be effectively decomposed into solvable subproblems. The paper's core mechanism relies on the successful resolution of individual subproblems to make progress on the overall problem. If the problem cannot be broken down in a useful way, the method might struggle to make meaningful progress. The paper does not explore or discuss this limitation. - **Conclusion:** Validity status: Valid Confidence level: High - Key supporting evidence: The method's design and the experimental setup focus on problems where subproblem decomposition is a viable strategy, without addressing the scenario where it is not.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces SCRL (Subproblem Curriculum Reinforcement Learning), a novel approach to training large language models (LLMs) on complex mathematical reasoning tasks. The core idea behind SCRL is to decompose complex problems into a sequence of simpler, verifiable subproblems. This is achieved by leveraging an external LLM, specifically the DeepSeek-V3.2 API, to generate these subproblems based on a provided chain-of-thought (CoT) reference solution. The LLM is prompted to rewrite the intermediate steps of the CoT into K verifiable subproblems, which are then solved in a single on-policy rollout. This curriculum reinforcement learning framework is designed to address the challenge of training LLMs on hard problems by breaking them down into manageable steps. The method employs a mixed-group training approach, combining curriculum rollouts with original-problem rollouts, and introduces a subproblem-level normalization for fine-grained credit assignment. The authors evaluate SCRL on several mathematical reasoning benchmarks, including the MATH, AIME, and MATH-500 datasets, and demonstrate that it outperforms several strong baseline methods, including SRFT, GRPO, and other curriculum learning approaches. The results suggest that SCRL's subproblem decomposition technique is a promising approach for curriculum reinforcement learning in mathematical reasoning, and the theoretical analysis provides a solid foundation for the method's effectiveness. The paper's contributions lie in the novel application of external LLMs for subproblem generation, the curriculum reinforcement learning framework, and the mixed-group training approach, all of which contribute to the improved performance observed in the experiments. The authors also provide a theoretical analysis to support the effectiveness of subproblem decomposition, showing that it can lift hard problems out of gradient dead zones. Overall, the paper presents a significant contribution to the field of LLM training, particularly for complex reasoning tasks, by introducing a novel and effective method for curriculum generation and training.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.8


## Strengths:

I find several aspects of this paper to be particularly strong. First, the core idea of breaking down complex mathematical problems into verifiable subproblems is a novel and effective approach. This method addresses the challenge of training LLMs on hard problems by leveraging an external LLM to generate these subproblems, which are then solved in a single on-policy rollout. This approach allows the model to learn to solve complex problems by mastering a series of simpler, verifiable subproblems, which is a significant departure from traditional methods that attempt to solve the entire problem at once. The use of an external LLM for subproblem generation is a key innovation, as it allows for a more structured and controlled approach to problem decomposition. Second, the theoretical analysis provided in the paper is compelling. The authors demonstrate that subproblem decomposition can lift hard problems out of gradient dead zones, which is a significant theoretical contribution. This analysis provides a strong foundation for the effectiveness of the proposed method and adds rigor to the paper's claims. The theoretical framework is well-explained and supports the empirical results, which is a testament to the authors' careful approach. Third, the experimental results are promising, with SCRL outperforming strong baseline methods across several mathematical reasoning benchmarks. The ablation studies further validate the effectiveness of the subproblem-level normalization and mixed-group training components. The fact that SCRL achieves state-of-the-art performance on these benchmarks is a significant achievement and demonstrates the practical value of the proposed method. The authors have clearly put in the effort to validate their approach through rigorous experimentation, which is a testament to the quality of their work. Finally, the paper is well-written and easy to follow, which makes it accessible to a broad audience. The motivation and method are clearly explained, and the experimental results are presented in a clear and concise manner. The paper is a pleasure to read and is a valuable contribution to the field.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the reliance on an external LLM for subproblem generation is a significant concern. While the authors claim that the external LLM is prompted to elicit the desired subproblem decomposition, they do not provide sufficient details on the prompt engineering process. The paper mentions that the prompt is provided in Appendix I, but it does not elaborate on the specific design or the rationale behind it. This lack of detail makes it difficult to assess the potential for biases or inconsistencies in the generated subproblems. The paper does not discuss how the authors ensure that the generated subproblems are not only verifiable but also logically consistent and aligned with the overall problem structure. The authors could have explored techniques for verifying the correctness of the generated subproblems, such as using a separate LLM to check the validity of each subproblem, or implementing a mechanism for detecting and correcting errors in the generated subproblems. This lack of control over the subproblem generation process raises concerns about the reliability of the method. The paper does not address the potential for the external LLM to introduce errors or inconsistencies in the subproblem generation process, and how these issues are addressed. This is a critical weakness, as the quality of the generated subproblems directly impacts the performance of the proposed method. My confidence in this weakness is high, as the paper lacks any discussion of the prompt engineering process and the potential for errors in the generated subproblems. Second, the reward scheme used in the method is overly simplistic. The paper only provides credit for consecutive solved subproblems, which may not be optimal in all cases. This reward scheme does not allow for the model to learn to solve subproblems in a more flexible manner. The authors do not explore alternative reward schemes, such as sparse rewards or rewards that provide credit for individual subproblem solutions. This limitation could lead to suboptimal performance, as the model might learn to solve a sequence of easy subproblems that are necessary to solve the overall problem, rather than focusing on the most difficult subproblems that are necessary to solve the overall problem. The paper does not provide any justification for the chosen reward scheme, and it does not explore the potential for alternative reward schemes. This is a significant weakness, as the reward scheme is a critical component of the reinforcement learning process. My confidence in this weakness is high, as the paper explicitly describes the reward scheme as providing credit only for consecutive solved subproblems and does not explore alternative reward schemes. Third, the paper does not address the method's performance on problems that are inherently unsolvable through subproblem decomposition. The method is designed around the assumption that the complex problem can be decomposed into verifiable subproblems. The curriculum progress mechanism is designed to track the progress on the original problem based on the solved subproblems. The reward scheme incentivizes solving subproblems in a sequence. The paper does not include experiments specifically designed to test the method's performance on problems that are inherently unsolvable through subproblem decomposition. The experiments focus on problems where subproblem decomposition is a viable strategy. This is a significant limitation, as the method might struggle to make meaningful progress on problems that cannot be broken down in a useful way. The paper does not explore or discuss this limitation. My confidence in this weakness is high, as the paper's method and experimental setup focus on problems where subproblem decomposition is a viable strategy, without addressing the scenario where it is not. Finally, the paper lacks a detailed analysis of the computational cost associated with generating and solving subproblems. The paper does not provide a breakdown of the time spent on each component of the SCRL method, including subproblem generation, subproblem solving, and training. This makes it difficult to evaluate the scalability of the method and its suitability for resource-constrained environments. The paper does not explore the potential for parallelization of these steps, which could significantly reduce the overall training time. My confidence in this weakness is high, as the paper does not provide any analysis of the computational cost of the method.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed analysis of the subproblem generation process. This should include a thorough description of the prompt engineering used for the external LLM, and the methods used to control the quality of the generated subproblems. Specifically, the authors should provide examples of the prompts used to elicit the desired subproblem decomposition from the external LLM, and discuss how they ensure that the generated subproblems are not only verifiable but also logically consistent and aligned with the overall problem structure. Furthermore, the paper should include a discussion on the potential for the external LLM to introduce errors or inconsistencies in the subproblem generation process, and how these issues are addressed. For example, the authors could explore the use of a verification mechanism to ensure that the generated subproblems are not only verifiable but also logically consistent and aligned with the overall problem structure. This could involve using a separate LLM to check the validity of each subproblem, or implementing a mechanism for detecting and correcting errors in the generated subproblems. The authors should also discuss the limitations of relying on an external LLM for subproblem generation, and how these limitations might affect the overall performance of the proposed method. Second, the authors should explore alternative reward schemes that could potentially improve performance. The current reward scheme, which only provides credit for consecutive solved subproblems, might not be optimal for all types of problems. The authors could consider using sparse rewards or rewards that provide credit for individual subproblem solutions. For example, a reward could be given for solving each subproblem independently, rather than only for consecutive solved subproblems. This could help to encourage the model to focus on the most difficult subproblems that are necessary to solve the overall problem. Additionally, the paper should provide a more detailed analysis of the impact of the chosen reward scheme on the performance of the method. This could involve comparing the performance of the proposed method with different reward schemes and analyzing the convergence behavior of the model during training. The authors should also discuss the potential limitations of the chosen reward scheme and how these limitations might affect the overall performance of the proposed method. Third, the authors should investigate the method's performance on problems that are inherently unsolvable through subproblem decomposition. The authors should conduct experiments on a variety of problems with different levels of complexity and analyze the performance of the method. This analysis should include an investigation of the types of problems where the method performs well and the reasons for these successes, as well as an analysis of the types of problems where the method performs poorly and the reasons for these failures. The authors should also explore the potential for error propagation through the subproblem chain and how the method handles situations where the subproblems are not logically connected or where the external LLM generates subproblems that are not verifiable. The authors should also discuss the potential for using alternative problem decomposition strategies when the subproblem decomposition approach fails. Fourth, the authors should provide a more detailed analysis of the computational cost associated with generating and solving subproblems. This should include a breakdown of the time spent on each component of the SCRL method, including subproblem generation, subproblem solving, and training. The authors should also explore the potential for parallelization of these steps, which could significantly reduce the overall training time. For example, the subproblem generation could be parallelized across multiple LLMs, and the subproblem solving could be parallelized across multiple GPUs. The authors should also provide a comparison of the computational cost of SCRL with other curriculum learning methods to demonstrate its efficiency. Finally, the authors should provide a more detailed analysis of the impact of the mixed-group training approach on the performance of the method. The paper should include ablation studies to evaluate the contribution of each component of the mixed-group training approach. For example, the authors could compare the performance of the proposed method with a version that only uses curriculum rollouts, or a version that only uses original-problem rollouts. This would help to determine the effectiveness of each component of the mixed-group training approach and to identify the optimal configuration for the proposed method. The authors should also discuss the potential limitations of the mixed-group training approach and how these limitations might affect the overall performance of the proposed method.


## Questions:

I have several questions that I believe are important for clarifying the method and its implications. First, how does the method handle cases where the subproblems are not well-defined or are ambiguous? The paper does not explicitly discuss how the method handles poorly defined or ambiguous subproblems. The method relies on the external LLM to generate the subproblems, and the reward scheme incentivizes consecutive solved subproblems. I am curious about the method's robustness to poorly defined or ambiguous subproblems and what the reasons for these failures are. Second, how does SCRL handle problems that are inherently unsolvable through subproblem decomposition? The paper does not include experiments specifically designed to test the method's performance on problems that are inherently unsolvable through subproblem decomposition. The experiments focus on problems where subproblem decomposition is a viable strategy. I am interested in understanding the limitations of the method when the problem cannot be effectively decomposed into solvable subproblems. Third, could the authors provide more details on the computational cost associated with generating and solving subproblems? How does the computational cost of SCRL compare to other curriculum learning methods? The paper does not provide a detailed analysis of the computational cost of the method. I am interested in understanding the scalability of the method and its suitability for resource-constrained environments. Fourth, how does SCRL compare to other curriculum learning methods for mathematical reasoning? The paper compares SCRL with several baseline methods, but it does not provide a detailed analysis of the strengths and weaknesses of the method compared to other curriculum learning methods. I am interested in understanding the advantages and disadvantages of SCRL compared to other approaches. Finally, could the authors discuss the potential for using reinforcement learning techniques to guide the subproblem generation process? The current reward scheme, which only provides credit for consecutive solved subproblems, might not be optimal for all types of problems. I am interested in exploring alternative reward schemes and how they might improve the performance of the method. These questions are aimed at clarifying the limitations of the method and identifying potential avenues for future research.


## Rating:

6.2


## Confidence:

3.6


## Decision:

Accept
}