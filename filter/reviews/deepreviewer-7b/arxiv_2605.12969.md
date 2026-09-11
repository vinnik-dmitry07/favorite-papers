I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper addresses the limitations of GRPO, an RL method for post-training LLMs on reasoning tasks. The authors identify two key issues with GRPO: (1) GRPO’s surrogate score is not aligned with sequence likelihoods, and (2) GRPO’s credit assignment is insensitive to the score gap between positive and negative rollouts. To address these issues, they propose a contrastive reformulation of GRPO, which uses InfoNCE-style objectives and length-normalized sequence log-probabilities as rollout scores. They also introduce a curriculum-scheduled margin to enhance separation pressure. Experiments across diverse settings validate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper is well-organized and easy to follow.
2. The proposed method is well-motivated, and the authors provide a thorough theoretical analysis of the limitations of GRPO.
3. The proposed method is simple and effective, and the experiments are comprehensive.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by the contrastive reformulation of GRPO. The InfoNCE-style objective, while effective, involves a pairwise comparison between positive and negative samples, which could significantly increase the computational cost, especially with large batch sizes or sequence lengths. A thorough analysis of the time and memory complexity is needed to understand the practical implications of the proposed method.
2. The paper does not provide a clear explanation of how the margin is determined and how it affects the training dynamics. The scheduled margin is introduced to enhance separation pressure, but the specific form of the margin function (e.g., cosine annealing) and its parameters are not well justified. A more detailed discussion on the sensitivity of the method to different margin schedules and the theoretical basis for the chosen function is necessary.

### Suggestions

The authors should provide a more detailed analysis of the computational complexity of their proposed method, specifically focusing on the time and memory requirements of the InfoNCE-style objective. This analysis should include a breakdown of the computational cost associated with calculating the contrastive loss for different batch sizes and sequence lengths. It would be beneficial to compare the computational overhead of the proposed method with that of the original GRPO, providing a clear understanding of the trade-offs involved. Furthermore, the authors should investigate techniques to mitigate the computational cost, such as using a smaller number of negative samples or employing approximation methods for the contrastive loss. This would make the proposed method more practical for large-scale applications.

To address the lack of clarity regarding the margin schedule, the authors should provide a more detailed explanation of the rationale behind their choice of a cosine annealing schedule. They should discuss the specific parameters of the cosine function and how they are determined. A sensitivity analysis of the method to different margin schedules would be valuable, demonstrating how the performance of the method varies with different choices of the margin function and its parameters. This analysis should include a discussion of the theoretical basis for the chosen margin schedule and how it relates to the convergence properties of the training process. It would also be helpful to provide a visualization of the margin schedule during training to illustrate how it evolves over time.

Finally, the authors should consider providing a more in-depth discussion of the limitations of their proposed method. While the paper demonstrates the effectiveness of the method on several reasoning tasks, it would be beneficial to discuss the potential challenges and limitations of the method in other contexts. For example, how does the method perform on tasks with different characteristics, such as tasks that require more complex reasoning or tasks that involve different types of feedback? A thorough discussion of the limitations would provide a more balanced perspective on the proposed method and help guide future research in this area.

### Questions

1. Could the authors provide a more detailed analysis of the computational overhead introduced by the contrastive reformulation of GRPO?
2. How does the margin schedule affect the training dynamics, and what is the rationale behind the chosen margin schedule?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a contrastive learning method for RL in LLMs, which is based on GRPO. The authors first show that GRPO has two limitations: (1) the surrogate score is not aligned with the sequence likelihood; (2) the credit assignment is insensitive to the score gap between positive and negative rollouts. To address these limitations, they propose a contrastive reformulation of GRPO that uses length-normalized sequence log-probabilities as rollout scores and a curriculum-scheduled margin to maintain separation pressure. Experiments show that the proposed method outperforms strong baselines on challenging reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper is well-written and easy to follow.
2. The proposed method is novel and well-motivated.
3. The authors conduct extensive experiments to show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the contrastive reformulation of GRPO, such as the specific form of the contrastive loss and the choice of negative samples. The current description lacks sufficient detail to fully understand the implementation. For example, it is unclear how the negative samples are selected, whether they are randomly sampled or if there is a specific strategy, and how the contrastive loss is formulated given the specific choice of positive and negative samples. A more precise definition of the contrastive loss function, including the exact mathematical expression and the parameters involved, is needed.
2. The authors should provide more details about the curriculum-scheduled margin, such as how the margin is determined and how it affects the training dynamics. The paper does not specify the exact function used to schedule the margin, nor does it explain how the margin is adapted during training. It is unclear how the margin is initialized, how it is updated, and what the impact of different margin schedules is on the convergence and performance of the model. A more detailed explanation of the margin scheduling strategy, including the mathematical formulation and the rationale behind the chosen approach, is necessary.
3. The authors should discuss the limitations of the proposed method, such as the computational cost and the sensitivity to hyperparameters. The paper does not address the computational overhead of the contrastive learning approach, which could be significant, especially for large language models. Furthermore, the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters, is not discussed. It is important to understand how these hyperparameters affect the performance and stability of the training process.

### Suggestions

The paper would benefit from a more detailed explanation of the contrastive reformulation of GRPO. Specifically, the authors should provide the exact mathematical formulation of the contrastive loss function, including all parameters and variables involved. They should also clarify the method used to select negative samples, whether it is random or based on some criteria, and how this choice impacts the training process. For example, if the negative samples are selected based on the similarity of the trajectories, the authors should provide details on the similarity metric used. Furthermore, the authors should provide a more detailed explanation of the margin scheduling strategy, including the mathematical formulation of the margin function and the rationale behind the chosen approach. The authors should also discuss the impact of different margin schedules on the convergence and performance of the model. For instance, they could explore different types of margin schedules, such as linear or exponential decay, and analyze their effects on the training dynamics. This would provide a more comprehensive understanding of the proposed method and its sensitivity to different design choices.

To address the computational cost, the authors should provide a detailed analysis of the time and memory complexity of their proposed method. They should compare the computational cost of their method with that of the baselines, and discuss the factors that contribute to the computational overhead. For example, they could analyze the number of forward and backward passes required for each training step, and compare it with the computational cost of the baselines. Furthermore, the authors should discuss the sensitivity of their method to hyperparameters, such as the margin schedule and the contrastive loss parameters. They should provide a detailed analysis of how these hyperparameters affect the performance and stability of the training process. For example, they could conduct a sensitivity analysis by varying these hyperparameters and observing their impact on the final performance. This would provide a more robust evaluation of the proposed method and its practical applicability.

Finally, the authors should provide a more comprehensive discussion of the limitations of their proposed method. They should discuss the potential challenges and limitations of applying their method to different types of tasks and datasets. For example, they could discuss how their method performs on tasks with different levels of complexity or different types of feedback. They should also discuss the potential limitations of their method in terms of scalability and robustness. For instance, they could analyze the performance of their method on larger models or with more complex datasets. This would provide a more balanced perspective on the proposed method and its potential for future research.

### Questions

1. How does the proposed method compare to other contrastive learning methods for RL in LLMs?
2. How does the proposed method perform on tasks with different levels of complexity or different types of feedback?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces a new method called ConSPO, which is a contrastive reformulation of GRPO. The authors identify two limitations of GRPO: likelihood-misaligned surrogate scores and score-insensitive credit assignment. ConSPO addresses these limitations by using length-normalized sequence log-probabilities as rollout scores and a curriculum-scheduled margin to maintain separation pressure. Experiments show that ConSPO outperforms strong baselines on challenging reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and well-motivated.
3. The authors conduct extensive experiments to show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the contrastive reformulation of GRPO, such as the specific form of the contrastive loss and the choice of negative samples. The current description lacks sufficient detail to fully understand the implementation. For example, it is unclear how the negative samples are selected, whether they are randomly sampled or if there is a specific strategy, and how the contrastive loss is formulated given the specific choice of positive and negative samples. A more precise definition of the contrastive loss function, including the exact mathematical expression and the parameters involved, is needed.
2. The authors should provide more details about the curriculum-scheduled margin, such as how the margin is determined and how it affects the training dynamics. The paper does not specify the exact function used to schedule the margin, nor does it explain how the margin is adapted during training. It is unclear how the margin is initialized, how it is updated, and what the impact of different margin schedules is on the convergence and performance of the model. A more detailed explanation of the margin scheduling strategy, including the mathematical formulation and the rationale behind the chosen approach, is necessary.
3. The authors should discuss the limitations of the proposed method, such as the computational cost and the sensitivity to hyperparameters. The paper does not address the computational overhead of the contrastive learning approach, which could be significant, especially for large language models. Furthermore, the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters, is not discussed. It is important to understand how these hyperparameters affect the performance and stability of the training process.

### Suggestions

The paper would benefit from a more detailed explanation of the contrastive reformulation of GRPO. Specifically, the authors should provide the exact mathematical formulation of the contrastive loss function, including all parameters and variables involved. This should include a clear definition of how the negative samples are selected, whether it is through random sampling or a more sophisticated strategy, and how this choice impacts the training dynamics. For instance, if the negative samples are selected based on the similarity of the trajectories, the authors should provide details on the similarity metric used. Furthermore, the authors should clarify how the contrastive loss is formulated given the specific choice of positive and negative samples. A more precise definition of the contrastive loss function, including the exact mathematical expression and the parameters involved, is needed to fully understand the implementation. This would allow for a more rigorous evaluation of the proposed method and facilitate reproducibility.

Regarding the curriculum-scheduled margin, the authors should provide a more detailed explanation of how the margin is determined and how it affects the training dynamics. The paper should specify the exact function used to schedule the margin, including the mathematical formulation and the rationale behind the chosen approach. It is crucial to understand how the margin is initialized, how it is updated during training, and what the impact of different margin schedules is on the convergence and performance of the model. For example, the authors could explore different types of margin schedules, such as linear or exponential decay, and analyze their effects on the training dynamics. This would provide a more comprehensive understanding of the proposed method and its sensitivity to different design choices. Furthermore, the authors should discuss the potential limitations of the chosen margin schedule and how it might affect the overall performance of the model.

Finally, the authors should address the computational cost and sensitivity to hyperparameters of the proposed method. The paper should include a detailed analysis of the computational overhead of the contrastive learning approach, especially in comparison to the original GRPO method. This analysis should consider the number of forward and backward passes required for each training step, as well as the memory requirements for storing the contrastive loss. Furthermore, the authors should discuss the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters. It is important to understand how these hyperparameters affect the performance and stability of the training process. The authors should provide a sensitivity analysis by varying these hyperparameters and observing their impact on the final performance. This would provide a more robust evaluation of the proposed method and its practical applicability.

### Questions

1. How does the proposed method compare to other contrastive learning methods for RL in LLMs?
2. How does the proposed method perform on tasks with different levels of complexity or different types of feedback?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a new method called ConSPO, which is a contrastive reformulation of GRPO. The authors identify two limitations of GRPO: likelihood-misaligned surrogate scores and score-insensitive credit assignment. ConSPO addresses these limitations by using length-normalized sequence log-probabilities as rollout scores and a curriculum-scheduled margin to maintain separation pressure. Experiments show that ConSPO outperforms strong baselines on challenging reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and well-motivated.
3. The authors conduct extensive experiments to show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the contrastive reformulation of GRPO, such as the specific form of the contrastive loss and the choice of negative samples. The current description lacks sufficient detail to fully understand the implementation. For example, it is unclear how the negative samples are selected, whether they are randomly sampled or if there is a specific strategy, and how the contrastive loss is formulated given the specific choice of positive and negative samples. A more precise definition of the contrastive loss function, including the exact mathematical expression and the parameters involved, is needed.
2. The authors should provide more details about the curriculum-scheduled margin, such as how the margin is determined and how it affects the training dynamics. The paper does not specify the exact function used to schedule the margin, nor does it explain how the margin is adapted during training. It is unclear how the margin is initialized, how it is updated, and what the impact of different margin schedules is on the convergence and performance of the model. A more detailed explanation of the margin scheduling strategy, including the mathematical formulation and the rationale behind the chosen approach, is necessary.
3. The authors should discuss the limitations of the proposed method, such as the computational cost and the sensitivity to hyperparameters. The paper does not address the computational overhead of the contrastive learning approach, which could be significant, especially for large language models. Furthermore, the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters, is not discussed. It is important to understand how these hyperparameters affect the performance and stability of the training process.

### Suggestions

The paper would benefit from a more detailed explanation of the contrastive reformulation of GRPO. Specifically, the authors should provide the exact mathematical formulation of the contrastive loss function, including all parameters and variables involved. This should include a clear definition of how the negative samples are selected, whether it is through random sampling or a more sophisticated strategy, and how this choice impacts the training dynamics. For instance, if the negative samples are selected based on the similarity of the trajectories, the authors should provide details on the similarity metric used. Furthermore, the authors should clarify how the contrastive loss is formulated given the specific choice of positive and negative samples. A more precise definition of the contrastive loss function, including the exact mathematical expression and the parameters involved, is needed to fully understand the implementation. This would allow for a more rigorous evaluation of the proposed method and facilitate reproducibility.

Regarding the curriculum-scheduled margin, the authors should provide a more detailed explanation of how the margin is determined and how it affects the training dynamics. The paper should specify the exact function used to schedule the margin, including the mathematical formulation and the rationale behind the chosen approach. It is crucial to understand how the margin is initialized, how it is updated during training, and what the impact of different margin schedules is on the convergence and performance of the model. For example, the authors could explore different types of margin schedules, such as linear or exponential decay, and analyze their effects on the training dynamics. This would provide a more comprehensive understanding of the proposed method and its sensitivity to different design choices. Furthermore, the authors should discuss the potential limitations of the chosen margin schedule and how it might affect the overall performance of the model.

Finally, the authors should address the computational cost and sensitivity to hyperparameters of the proposed method. The paper should include a detailed analysis of the computational overhead of the contrastive learning approach, especially in comparison to the original GRPO method. This analysis should consider the number of forward and backward passes required for each training step, as well as the memory requirements for storing the contrastive loss. Furthermore, the authors should discuss the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters. It is important to understand how these hyperparameters affect the performance and stability of the training process. A sensitivity analysis by varying these hyperparameters and observing their impact on the final performance would provide a more robust evaluation of the proposed method and its practical applicability.

### Questions

1. How does the proposed method compare to other contrastive learning methods for RL in LLMs?
2. How does the proposed method perform on tasks with different levels of complexity or different types of feedback?

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
2. **Collect evidence from the paper.** This will involve looking for specific mentions of the method, experiments, or missing information.
3. **Analyze literature gaps.** Check if the paper misses citations for relevant concepts or baselines.
4. **Validate the weakness.** Based on the evidence, I will determine if the weakness is valid, partially valid, or invalid.
5. **State my confidence level.**

Let's start with Reviewer 1.
**Review 1 Weaknesses:**

1. **Weakness Statement:** The authors should provide more details about the contrastive reformulation of GRPO, such as the specific form of the contrastive loss and the choice of negative samples. The current description lacks sufficient detail to fully understand the implementation. For example, it is unclear how the negative samples are selected, whether they are randomly sampled or if there is a specific strategy, and how the contrastive loss is formulated given the specific choice of positive and negative samples. A more precise definition of the contrastive loss function, including the exact mathematical expression and the parameters involved, is needed.

2. **Evidence Collection:**
a) Method-related Evidence:
   - The paper introduces the InfoNCE-style objective in Equation (10):
     ```
     \mathcal{J} ^ N C A P ​ = 1 N + ​ ∑ i = 1 N + τ \displaystyle\sum_{i = 1}^{N + } \tau (8) log ⁡ exp ⁡ ( ( s θ ​ ( o i + , q ) − m t ) / τ ) exp ⁡ ( ( s θ ​ ( o i + , q ) − m t ) / τ ) + ∑ j = 1 N − exp ⁡ ( s θ ​ ( o j − , q ) / τ )
     ```
   - The paper mentions "length-normalized log-probabilities" as rollout scores in the "Contrastive Reformulation of GRPO" section.
   - The "Scheduled Margin as a Separation Curriculum" section describes the margin `m_t` and its components, but doesn't explicitly detail how negative samples are chosen or the exact formulation of the contrastive loss given the chosen positive and negative samples.

3. **Literature Gap Analysis:**
   - The paper cites (24) for the InfoNCE loss, which provides the general form. However, the specific application to the RLVR setting with the defined positive and negative samples could benefit from more explicit referencing or derivation.

4. **Validation Analysis:**
   - The reviewer is correct that while the InfoNCE loss is presented, the specific selection of negative samples and the exact formulation of the loss with those samples could be more explicit. The paper states the scores are length-normalized log-probabilities, but the process of pairing them to form the positive and negative pairs for the InfoNCE loss isn't fully elaborated. The margin scheduling is explained, but the connection between the margin and the InfoNCE loss formulation isn't explicitly detailed.

5. **Conclusion:**
   - Validity status: **Partially Valid**
   - Confidence level: **High**
   - Key supporting evidence: While the InfoNCE loss is presented, the specifics of negative sample selection and its direct integration into the loss function's formulation could be clearer.

1. **Weakness Statement:** The authors should provide more details about the curriculum-scheduled margin, such as how the margin is determined and how it affects the training dynamics. The paper does not specify the exact function used to schedule the margin, nor does it explain how the margin is adapted during training. It is unclear how the margin is initialized, how it is updated, and what the impact of different margin schedules is on the convergence and performance of the model. A more detailed explanation of the margin scheduling strategy, including the mathematical formulation and the rationale behind the chosen approach, is necessary.

2. **Evidence Collection:**
a) Method-related Evidence:
   - The "Scheduled Margin as a Separation Curriculum" section provides the mathematical formulation for the margin `m_t`:
     ```
     m t = M 2 ​ ( 1 − cos ⁡ ( π ρ t ) ) . \rho t = min ⁡ ( λ t α , 1 ) , m t = M 2 ​ ( 1 − cos ⁡ ( π ρ t ) ) .
     ```
   - It also explains how `ρ_t` and `λ_t` are calculated.
   - The rationale behind the cosine annealing schedule is mentioned: "The margin starts from zero, allowing early training to focus on coarse positive-negative ordering, and gradually increases to enforce stronger separation as optimization progresses."

3. **Literature Gap Analysis:**
   - The paper doesn't explicitly cite literature justifying the specific cosine annealing schedule used for the margin.

4. **Validation Analysis:**
   - The reviewer's initial statement is partially inaccurate as the paper *does* specify the exact function used to schedule the margin and explains how it's adapted during training. The mathematical formulation is provided, and the rationale for the cosine annealing is given. However, the reviewer's point about exploring different margin schedules is valid, as the paper doesn't include experiments or discussion on alternative schedules.

5. **Conclusion:**
   - Validity status: **Partially Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper provides the mathematical formulation and rationale for the cosine annealing margin schedule, but lacks exploration of alternative schedules.

1. **Weakness Statement:** The authors should discuss the limitations of the proposed method, such as the computational cost and the sensitivity to hyperparameters. The paper does not address the computational overhead of the contrastive learning approach, which could be significant, especially for large language models. Furthermore, the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters, is not discussed. It is important to understand how these hyperparameters affect the performance and stability of the training process.

2. **Evidence Collection:**
a) Method-related Evidence:
   - The paper doesn't explicitly discuss the computational cost of ConSPO compared to GRPO.
b) Experiment-related Evidence:
   - The "Implementation details" section mentions the hardware used but doesn't provide a detailed analysis of training time or computational resources.
   - The "Ablation Study" section explores the impact of removing the InfoNCE objective and the margin, but doesn't systematically vary hyperparameters like the margin schedule parameters or the temperature `τ`.

3. **Literature Gap Analysis:**
   - While the paper compares against several baselines, it doesn't include a discussion of the computational complexity of these methods or a comparison to ConSPO.

4. **Validation Analysis:**
   - The reviewer is correct. The paper lacks a discussion on the computational cost of ConSPO. While the ablation study touches upon the importance of the InfoNCE objective and margin, it doesn't systematically explore the sensitivity to other hyperparameters, such as the margin schedule parameters or the temperature `τ`.

5. **Conclusion:**
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks a dedicated discussion on the computational cost and a systematic analysis of hyperparameter sensitivity.

**Review 2 Weaknesses:**

1. **Weakness Statement:** The paper lacks a detailed analysis of the computational overhead introduced by the contrastive reformulation of GRPO. The InfoNCE-style objective, while effective, involves a pairwise comparison between positive and negative samples, which could significantly increase the computational cost, especially with large batch sizes or sequence lengths. A thorough analysis of the time and memory complexity is needed to understand the practical implications of the proposed method.

2. **Evidence Collection:**
a) Method-related Evidence:
   - The InfoNCE objective involves calculating the exponential of scores for both positive and negative pairs.
b) Experiment-related Evidence:
   - The paper doesn't provide a detailed analysis of training time, memory usage, or scalability with batch size or sequence length.

3. **Literature Gap Analysis:**
   -  While InfoNCE is a known efficient loss function, the specific overhead in the RLVR context with variable sequence lengths isn't analyzed.

4. **Validation Analysis:**
   - The reviewer's point is valid. The paper doesn't provide a detailed analysis of the computational overhead introduced by the InfoNCE objective in the context of RLVR, especially considering the variable sequence lengths and potential for large batch sizes.

5. **Conclusion:**
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks a detailed computational cost analysis specific to the InfoNCE objective in the RLVR setting.

1. **Weakness Statement:** The paper does not provide a clear explanation of how the margin is determined and how it affects the training dynamics. The scheduled margin is introduced to enhance separation pressure, but the specific form of the margin function (e.g., cosine annealing) and its parameters are not well justified. A more detailed discussion on the sensitivity of the method to different margin schedules and the theoretical basis for the chosen function is necessary.

2. **Evidence Collection:**
a) Method-related Evidence:
   - The paper provides the formula for the scheduled margin and explains the cosine annealing.
   - The rationale for cosine annealing is given: "The margin starts from zero, allowing early training to focus on coarse positive-negative ordering, and gradually increases to enforce stronger separation as optimization progresses."
b) Experiment-related Evidence:
   - The ablation study shows the impact of removing the margin, but doesn't explore different margin schedules.

3. **Literature Gap Analysis:**
   - The paper doesn't cite literature justifying the specific cosine annealing schedule.

4. **Validation Analysis:**
   - The reviewer is partially correct. The paper *does* specify the margin function and its rationale. However, it lacks a detailed discussion on the sensitivity to different margin schedules and a strong theoretical basis for the chosen cosine annealing schedule beyond the high-level explanation.

5. **Conclusion:**
   - Validity status: **Partially Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper provides the margin function and rationale, but lacks a detailed sensitivity analysis and strong theoretical justification for the specific cosine annealing schedule.

1. **Weakness Statement:** The authors should provide a more in-depth discussion of the limitations of their proposed method. While the paper demonstrates the effectiveness of the method on several reasoning tasks, it would be beneficial to discuss the potential challenges and limitations of the method in other contexts. For example, how does the method perform on tasks with different levels of complexity or different types of feedback? A thorough discussion of the limitations would provide a more balanced perspective on the proposed method and help guide future research in this area.

2. **Evidence Collection:**
a) Method-related Evidence:
   - The paper focuses on the limitations identified within the GRPO framework.
b) Experiment-related Evidence:
   - The experiments are conducted on mathematical reasoning benchmarks.

3. **Literature Gap Analysis:**
   - The paper doesn't discuss limitations in other RL domains or with different types of feedback.

4. **Validation Analysis:**
   - The reviewer is correct. The paper primarily focuses on the strengths and effectiveness within the defined RLVR context. A broader discussion of potential limitations in other RL scenarios or with different feedback mechanisms is missing.

5. **Conclusion:**
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks a broader discussion of the method's limitations beyond the specific context of GRPO and mathematical reasoning.

**Review 3 Weaknesses:**

1. **Weakness Statement:** The authors should provide more details about the contrastive reformulation of GRPO, such as the specific form of the contrastive loss and the choice of negative samples. The current description lacks sufficient detail to fully understand the implementation. For example, it is unclear how the negative samples are selected, whether they are randomly sampled or if there is a specific strategy, and how the contrastive loss is formulated given the specific choice of positive and negative samples. A more precise definition of the contrastive loss function, including the exact mathematical expression and the parameters involved, is needed.

2. **Evidence Collection:**
   - This is the same weakness as Reviewer 1's first point. Please see the analysis for Reviewer 1's first weakness.

3. **Conclusion:**
   - Validity status: **Partially Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper provides the InfoNCE loss but lacks explicit details on negative sample selection and its integration into the loss function.

1. **Weakness Statement:** The authors should provide more details about the curriculum-scheduled margin, such as how the margin is determined and how it affects the training dynamics. The paper does not specify the exact function used to schedule the margin, nor does it explain how the margin is adapted during training. It is unclear how the margin is initialized, how it is updated, and what the impact of different margin schedules is on the convergence and performance of the model. A more detailed explanation of the margin scheduling strategy, including the mathematical formulation and the rationale behind the chosen approach, is necessary.

2. **Evidence Collection:**
   - This is the same weakness as Reviewer 1's second point. Please see the analysis for Reviewer 1's second weakness.

3. **Conclusion:**
   - Validity status: **Partially Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper provides the margin function and rationale but lacks a detailed sensitivity analysis.

1. **Weakness Statement:** The authors should discuss the limitations of the proposed method, such as the computational cost and the sensitivity to hyperparameters. The paper does not address the computational overhead of the contrastive learning approach, which could be significant, especially for large language models. Furthermore, the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters, is not discussed. It is important to understand how these hyperparameters affect the performance and stability of the training process.

2. **Evidence Collection:**
   - This is the same weakness as Reviewer 1's third point. Please see the analysis for Reviewer 1's third weakness.

3. **Conclusion:**
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks a detailed discussion on computational cost and hyperparameter sensitivity.

**Review 4 Weaknesses:**

1. **Weakness Statement:** The authors should provide more details about the contrastive reformulation of GRPO, such as the specific form of the contrastive loss and the choice of negative samples. The current description lacks sufficient detail to fully understand the implementation. For example, it is unclear how the negative samples are selected, whether they are randomly sampled or if there is a specific strategy, and how the contrastive loss is formulated given the specific choice of positive and negative samples. A more precise definition of the contrastive loss function, including all parameters and variables involved, is needed.

2. **Evidence Collection:**
   - This is the same weakness as Reviewer 1's first point and Reviewer 3's first point. Please see the analysis for Reviewer 1's first weakness.

3. **Conclusion:**
   - Validity status: **Partially Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper provides the InfoNCE loss but lacks explicit details on negative sample selection and its integration into the loss function.

1. **Weakness Statement:** The authors should provide more details about the curriculum-scheduled margin, such as how the margin is determined and how it affects the training dynamics. The paper does not specify the exact function used to schedule the margin, nor does it explain how the margin is adapted during training. It is unclear how the margin is initialized, how it is updated, and what the impact of different margin schedules is on the convergence and performance of the model. A more detailed explanation of the margin scheduling strategy, including the mathematical formulation and the rationale behind the chosen approach, is necessary.

2. **Evidence Collection:**
   - This is the same weakness as Reviewer 1's second point and Reviewer 3's second point. Please see the analysis for Reviewer 1's second weakness.

3. **Conclusion:**
   - Validity status: **Partially Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper provides the margin function and rationale but lacks a detailed sensitivity analysis.

1. **Weakness Statement:** The authors should discuss the limitations of the proposed method, such as the computational cost and the sensitivity to hyperparameters. The paper does not address the computational overhead of the contrastive learning approach, which could be significant, especially for large language models. Furthermore, the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters, is not discussed. It is important to understand how these hyperparameters affect the performance and stability of the training process.

2. **Evidence Collection:**
   - This is the same weakness as Reviewer 1's third point and Reviewer 3's third point. Please see the analysis for Reviewer 1's third weakness.

3. **Conclusion:**
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks a detailed discussion on computational cost and hyperparameter sensitivity.

1. **Weakness Statement:** How does the proposed method compare to other contrastive learning methods for RL in LLMs?

2. **Evidence Collection:**
a) Experiment-related Evidence:
   - The "Baselines" section lists several RLVR methods, including some that use contrastive learning principles (e.g., DisCO).
   - The experimental results show comparisons against these baselines.

3. **Literature Gap Analysis:**
   - The paper does compare against some contrastive learning methods.

4. **Validation Analysis:**
   - The reviewer's question is addressed by the experimental comparisons. The paper does compare against other contrastive learning methods.

5. **Conclusion:**
   - Validity status: **Invalid**
   - Confidence level: **High**
   - Key supporting evidence: The paper includes comparisons against several RLVR methods, some of which are contrastive learning approaches.

1. **Weakness Statement:** How does the proposed method perform on tasks with different levels of complexity or different types of feedback?

2. **Evidence Collection:**
a) Experiment-related Evidence:
   - The experiments are conducted on mathematical reasoning benchmarks (AIME, AMC, etc.), which vary in complexity.
   - The paper doesn't explicitly test with different types of feedback (e.g., different reward structures or environments).

3. **Literature Gap Analysis:**
   - The paper focuses on the specific RLVR setting.

4. **Validation Analysis:**
   - The reviewer's question is partially addressed by the experiments on varying complexity tasks. However, the paper doesn't explore different types of feedback.

5. **Conclusion:**
   - Validity status: **Partially Valid**
   - Confidence level: **Medium**
   - Key supporting evidence: The paper tests on tasks with varying complexity but doesn't explore different feedback types.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces ConSPO, a novel reinforcement learning from human feedback (RLHF) method designed to address perceived limitations in the Grouped Policy Optimization (GRPO) algorithm. The authors identify two primary issues with GRPO: its use of surrogate scores that do not align with sequence likelihoods, and its credit assignment mechanism that is insensitive to the score gap between positive and negative rollouts. To overcome these challenges, ConSPO reformulates GRPO into a contrastive learning framework, leveraging length-normalized sequence log-probabilities as rollout scores. This approach aims to align the surrogate scores more closely with the actual likelihoods of the generated sequences. Furthermore, ConSPO incorporates a curriculum-scheduled margin to enhance separation pressure, ensuring that the model learns to distinguish between high-quality and low-quality rollouts more effectively. The authors provide a theoretical analysis of the limitations of GRPO, demonstrating how the surrogate scores and credit assignment mechanism contribute to its shortcomings. They then present empirical results across diverse mathematical reasoning benchmarks, showing that ConSPO outperforms strong baselines, including GRPO, on challenging tasks. The core idea is to move beyond the simple surrogate scores used in GRPO and instead use a more principled approach based on sequence likelihoods. The contrastive learning framework allows the model to learn from both positive and negative examples, which helps to improve the quality of the learned policy. The curriculum-scheduled margin is a key component of ConSPO, as it helps to ensure that the model learns to differentiate between high-quality and low-quality rollouts. The authors also provide an ablation study to demonstrate the importance of both the contrastive objective and the margin schedule. The paper's main contribution is the reformulation of GRPO into a contrastive learning framework, which addresses the identified limitations of the original algorithm. The empirical results demonstrate the effectiveness of the proposed method, showing that it outperforms strong baselines on a variety of mathematical reasoning tasks. Overall, the paper presents a well-motivated and well-executed approach to RLHF, with a clear theoretical foundation and strong empirical support. The use of length-normalized sequence log-probabilities as rollout scores and the curriculum-scheduled margin are both novel and effective, and the paper provides a valuable contribution to the field of reinforcement learning from human feedback.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I find several aspects of this paper to be particularly strong. First, the paper is exceptionally well-written and easy to follow, which greatly enhances its accessibility. The authors clearly articulate the problem with GRPO, the limitations of its surrogate scores and credit assignment, and the motivation for their proposed solution. The theoretical analysis of GRPO's limitations is also a significant strength. The authors provide a clear and rigorous explanation of why GRPO's surrogate scores are not aligned with sequence likelihoods and why its credit assignment mechanism is insensitive to the score gap between positive and negative rollouts. This theoretical grounding provides a solid foundation for the proposed method, ConSPO. Furthermore, the proposed method itself is well-motivated and technically sound. The reformulation of GRPO into a contrastive learning framework is a novel and effective approach. By using length-normalized sequence log-probabilities as rollout scores, the authors address the issue of surrogate scores not aligning with sequence likelihoods. The curriculum-scheduled margin is another key strength of the method. This mechanism enhances separation pressure, ensuring that the model learns to distinguish between high-quality and low-quality rollouts more effectively. The empirical results presented in the paper are also compelling. The authors conduct extensive experiments across diverse mathematical reasoning benchmarks, and the results consistently show that ConSPO outperforms strong baselines, including GRPO. This provides strong evidence for the effectiveness of the proposed method. The ablation study, which demonstrates the importance of both the contrastive objective and the margin schedule, further strengthens the paper's claims. The authors also provide a clear explanation of the InfoNCE-style objective and its connection to the contrastive learning framework. Overall, the paper's strengths lie in its clear presentation, strong theoretical motivation, novel methodological approach, and compelling empirical results. The combination of these factors makes this a valuable contribution to the field of reinforcement learning from human feedback.


## Weaknesses:

Despite its strengths, I have identified several weaknesses in this paper that warrant further discussion. First, while the paper introduces the InfoNCE-style objective, it lacks sufficient detail regarding the specific formulation of the contrastive loss and the selection of negative samples. Although the authors provide the mathematical expression for the InfoNCE loss, they do not explicitly explain how the negative samples are selected. It is unclear whether the negative samples are randomly selected or if there is a specific strategy, such as selecting them based on the similarity of the trajectories. This lack of clarity makes it difficult to fully understand the implementation and reproduce the results. Furthermore, the paper does not provide a precise definition of the contrastive loss function, including all parameters and variables involved. This lack of detail hinders a complete understanding of the implementation. My confidence in this weakness is high, as the paper's description of the contrastive loss lacks the necessary specifics. Second, while the paper provides the mathematical formulation for the curriculum-scheduled margin, it lacks a detailed discussion on the sensitivity of the method to different margin schedules. The authors specify the exact function used to schedule the margin, including the mathematical formulation and the rationale behind the chosen approach. However, they do not explore the impact of different margin schedules on the convergence and performance of the model. For example, the paper does not include experiments or discussion on alternative margin schedules, such as linear or exponential decay. This lack of exploration limits the robustness of the method and its practical applicability. My confidence in this weakness is high, as the paper does not include a sensitivity analysis of the margin schedule. Third, the paper does not adequately address the computational cost and sensitivity to hyperparameters of the proposed method. The InfoNCE-style objective involves a pairwise comparison between positive and negative samples, which could significantly increase the computational cost, especially with large batch sizes or sequence lengths. The paper does not provide a detailed analysis of the time and memory complexity of the proposed method. Furthermore, the paper does not discuss the sensitivity of the method to hyperparameters, such as the margin schedule parameters and the temperature `τ`. It is important to understand how these hyperparameters affect the performance and stability of the training process. The lack of a detailed analysis of the computational cost and hyperparameter sensitivity limits the practical applicability of the method. My confidence in this weakness is high, as the paper lacks a dedicated discussion on these important aspects. Finally, while the paper demonstrates the effectiveness of the proposed method on several reasoning tasks, it lacks a broader discussion of the method's limitations in other contexts. The paper focuses on the limitations identified within the GRPO framework and the specific RLVR context. However, it does not discuss how the method performs on tasks with different levels of complexity or different types of feedback. This lack of a broader discussion limits the generalizability of the method and its potential for future research. My confidence in this weakness is high, as the paper's discussion of limitations is primarily focused on the specific context of the paper.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed explanation of the contrastive reformulation of GRPO. Specifically, they should provide the exact mathematical formulation of the contrastive loss function, including all parameters and variables involved. They should also clarify the method used to select negative samples, whether it is random or based on some criteria, and how this choice impacts the training dynamics. For instance, if the negative samples are selected based on the similarity of the trajectories, the authors should provide details on the similarity metric used. Furthermore, the authors should clarify how the contrastive loss is formulated given the specific choice of positive and negative samples. A more precise definition of the contrastive loss function, including the exact mathematical expression and the parameters involved, is needed to fully understand the implementation. This would allow for a more rigorous evaluation of the proposed method and facilitate reproducibility. Second, regarding the curriculum-scheduled margin, the authors should provide a more detailed explanation of how the margin is determined and how it affects the training dynamics. The paper should specify the exact function used to schedule the margin, including the mathematical formulation and the rationale behind the chosen approach. It is crucial to understand how the margin is initialized, how it is updated during training, and what the impact of different margin schedules is on the convergence and performance of the model. For example, the authors could explore different types of margin schedules, such as linear or exponential decay, and analyze their effects on the training dynamics. This would provide a more comprehensive understanding of the proposed method and its sensitivity to different design choices. Furthermore, the authors should discuss the potential limitations of the chosen margin schedule and how it might affect the overall performance of the model. Third, the authors should address the computational cost and sensitivity to hyperparameters of the proposed method. The paper should include a detailed analysis of the computational overhead of the contrastive learning approach, especially in comparison to the original GRPO method. This analysis should consider the number of forward and backward passes required for each training step, as well as the memory requirements for storing the contrastive loss. Furthermore, the authors should discuss the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters. It is important to understand how these hyperparameters affect the performance and stability of the training process. The authors should provide a sensitivity analysis by varying these hyperparameters and observing their impact on the final performance. This would provide a more robust evaluation of the proposed method and its practical applicability. Fourth, the authors should provide a more in-depth discussion of the limitations of their proposed method. While the paper demonstrates the effectiveness of the method on several reasoning tasks, it would be beneficial to discuss the potential challenges and limitations of the method in other contexts. For example, how does the method perform on tasks with different levels of complexity or different types of feedback? A thorough discussion of the limitations would provide a more balanced perspective on the proposed method and help guide future research in this area. Finally, the authors should consider including a discussion of the limitations of their proposed method, such as the computational cost and the sensitivity to hyperparameters. The paper does not address the computational overhead of the contrastive learning approach, which could be significant, especially for large language models. Furthermore, the sensitivity of the method to hyperparameters, such as the margin schedule and the contrastive loss parameters, is not discussed. It is important to understand how these hyperparameters affect the performance and stability of the training process. A sensitivity analysis by varying these hyperparameters and observing their impact on the final performance would provide a more robust evaluation of the proposed method and its practical applicability.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the proposed method, ConSPO, compare to other contrastive learning methods for RL in LLMs? While the paper includes comparisons against several RLVR methods, some of which use contrastive learning principles, a more direct comparison with other contrastive learning methods would be beneficial. This would help to clarify the unique contributions of ConSPO and its advantages over existing approaches. Second, how does the proposed method perform on tasks with different levels of complexity or different types of feedback? The paper demonstrates the effectiveness of ConSPO on mathematical reasoning benchmarks, which vary in complexity. However, it does not explore the method's performance on tasks with different types of feedback, such as different reward structures or environments. Understanding how ConSPO performs in these different contexts would provide a more comprehensive evaluation of its generalizability. Third, could the authors provide a more detailed analysis of the computational overhead introduced by the contrastive reformulation of GRPO? The InfoNCE-style objective involves a pairwise comparison between positive and negative samples, which could significantly increase the computational cost, especially with large batch sizes or sequence lengths. A detailed analysis of the time and memory complexity of the proposed method would be valuable. Fourth, how does the margin schedule affect the training dynamics, and what is the rationale behind the chosen cosine annealing schedule? The paper provides the mathematical formulation for the margin schedule and explains the cosine annealing. However, it lacks a detailed discussion on the sensitivity of the method to different margin schedules and a strong theoretical basis for the chosen function. A more detailed explanation of the margin scheduling strategy, including the mathematical formulation and the rationale behind the chosen approach, is necessary. Finally, what are the limitations of the proposed method, and how can these limitations be addressed in future research? The paper primarily focuses on the strengths and effectiveness within the defined RLVR context. A broader discussion of potential limitations in other RL scenarios or with different feedback mechanisms is missing. Understanding these limitations would provide a more balanced perspective on the proposed method and help guide future research in this area.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}