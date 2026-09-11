I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper introduces Self-Distillation Policy Optimization (SDPO), a novel approach for reinforcement learning with rich feedback (RLRF) that leverages in-context learning capabilities. SDPO treats the current model as a self-teacher, using task-specific feedback to distill a dense logit-level reward signal back to the policy. The method is evaluated across various reasoning and coding tasks, demonstrating superior sample efficiency and performance over existing RLHF methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow. The proposed method is intuitive and well-motivated.
- The experiments are thorough, with SDPO showing strong performance across multiple tasks, including evidence-based reasoning and code generation.
- SDPO demonstrates significant improvements over GRPO, particularly in tasks with limited feedback.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily compares SDPO with GRPO, an RLHF method from 2024. However, it would be more convincing to compare SDPO with more recent and stronger baselines, such as RLCD and REINFORCE with a character-level advantage function. The absence of these comparisons makes it difficult to assess the true advancement of SDPO within the current landscape of RLHF methods.
- The paper does not include a detailed analysis of the computational overhead introduced by SDPO. Given that SDPO uses both the original and revised attempts, it is essential to quantify the additional training time and resources required compared to simpler baselines. This analysis is crucial for understanding the practical applicability of SDPO, especially in resource-constrained environments.
- The paper lacks a thorough discussion of the limitations of SDPO. For instance, it is unclear how SDPO performs with extremely sparse feedback or in scenarios where the feedback is noisy or inconsistent. A more detailed exploration of these limitations would provide a more balanced view of the method's applicability.

### Suggestions

The paper would significantly benefit from a more comprehensive comparison against state-of-the-art RLHF methods. Specifically, including results against methods like RLCD and REINFORCE with a character-level advantage function would provide a clearer picture of SDPO's relative performance. These methods represent different approaches to policy optimization and would help to contextualize the advantages and disadvantages of SDPO. For example, RLCD uses a contrastive learning objective, which might offer different trade-offs in terms of sample efficiency and stability compared to SDPO's self-distillation approach. Similarly, REINFORCE with a character-level advantage function could provide insights into how SDPO compares to methods that directly optimize the policy using a learned advantage function. A thorough comparison should not only focus on final performance metrics but also analyze the learning curves and convergence properties of each method. This would allow for a more nuanced understanding of the strengths and weaknesses of SDPO in different scenarios.

Furthermore, a detailed analysis of the computational overhead of SDPO is crucial for assessing its practical applicability. The paper should provide a breakdown of the additional training time and resources required by SDPO compared to simpler baselines. This analysis should include not only the total training time but also the memory footprint and the number of parameters involved. It would be beneficial to quantify the computational cost in terms of FLOPS or training time per epoch. This would allow practitioners to make informed decisions about whether the performance gains of SDPO justify the additional computational burden. For example, if SDPO requires significantly more training time or memory, it might not be suitable for resource-constrained environments. The analysis should also consider the impact of batch size and other hyperparameters on the computational cost of SDPO.

Finally, the paper should include a more thorough discussion of the limitations of SDPO. This should include an analysis of how SDPO performs with extremely sparse feedback, noisy feedback, and inconsistent feedback. For example, it would be useful to understand how the performance of SDPO degrades as the amount of feedback per episode decreases. Similarly, the paper should explore how the method performs when the feedback is not accurate or is inconsistent with the desired behavior. This analysis should also consider the impact of different types of feedback on the performance of SDPO. For example, it would be useful to understand how SDPO performs with different types of feedback, such as binary feedback, scalar feedback, or rich feedback. A more detailed exploration of these limitations would provide a more balanced view of the method's applicability and help guide future research.

### Questions

- How does SDPO perform with extremely sparse feedback (e.g., only one positive feedback per episode)? How does the performance degrade as the amount of feedback per episode decreases?
- How does SDPO handle noisy or inconsistent feedback? Are there specific mechanisms or strategies within SDPO to mitigate the impact of unreliable feedback?
- How does SDPO compare to other recent RLHF methods, such as RLCD and REINFORCE with a character-level advantage function? Are there specific scenarios where SDPO outperforms or underperforms compared to these methods?
- What is the computational overhead of SDPO compared to simpler baselines? How does the training time and resource requirements of SDPO compare to other RLHF methods?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes SDPO, which uses the current model as a self-teacher to provide dense feedback for policy optimization. SDPO is evaluated on coding and reasoning tasks, showing that SDPO outperforms GRPO.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, and the experiments are comprehensive.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide an ablation study on the effect of the self-teacher.
2. The paper does not provide an ablation study on the effect of the regularization terms.
3. The paper does not provide an ablation study on the effect of the temperature parameter K.

### Suggestions

The paper would benefit significantly from a more thorough investigation into the impact of the self-teacher. Specifically, an ablation study should explore the performance of SDPO when the self-teacher is replaced with a randomly initialized model or a model trained on a different task. This would help to isolate the contribution of the self-teacher's ability to provide meaningful feedback. Furthermore, the study should analyze the sensitivity of SDPO to the quality of the self-teacher's feedback. For example, how does the performance of SDPO change when the self-teacher's feedback is noisy or contains errors? This analysis would provide valuable insights into the robustness of the proposed method and its applicability in real-world scenarios where perfect feedback is not always available. The ablation study should also consider different types of feedback, such as binary feedback versus scalar feedback, to understand how the nature of the feedback affects the performance of SDPO.

In addition to the self-teacher, the paper should also include a more detailed analysis of the regularization terms and the temperature parameter K. The current study lacks a systematic exploration of how these components affect the performance of SDPO. For instance, the paper should investigate the impact of different regularization techniques, such as L1 or L2 regularization, on the stability and convergence of the training process. Furthermore, the paper should analyze how the choice of the temperature parameter K affects the exploration-exploitation trade-off and the overall performance of SDPO. It would be beneficial to provide a sensitivity analysis of K, showing how the performance of SDPO changes with different values of K. This analysis should also consider the interaction between the temperature parameter and other hyperparameters, such as the learning rate and the batch size. The ablation study should also explore the impact of different initialization strategies for the policy and the self-teacher, as this can also affect the performance of SDPO.

Finally, the paper should provide a more detailed analysis of the computational cost of SDPO compared to GRPO. While the paper mentions that SDPO is more efficient than GRPO, it does not provide a quantitative comparison of the training time and memory usage. A detailed analysis of the computational cost would be valuable for practitioners who are considering using SDPO in real-world applications. This analysis should include a breakdown of the computational cost of each component of SDPO, such as the self-teacher, the policy optimization, and the feedback generation. The paper should also compare the computational cost of SDPO with other related methods, such as other self-distillation techniques. This comparison would provide a better understanding of the trade-offs between performance and computational cost for SDPO.

### Questions

1. How does SDPO perform when the self-teacher is replaced with a randomly initialized model or a model trained on a different task?
2. How does the performance of SDPO change when the self-teacher's feedback is noisy or contains errors?
3. How does the choice of the regularization term affect the performance of SDPO?
4. How does the choice of the temperature parameter K affect the performance of SDPO?
5. How does the computational cost of SDPO compare to GRPO?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces SDPO, a method for RLHF that leverages rich feedback to improve policy learning. SDPO uses the current model as a self-teacher, distilling its feedback-informed next-token predictions back into the policy. This approach allows for dense, logit-level credit assignment, unlike traditional RLHF methods that rely on sparse scalar rewards. The authors demonstrate SDPO's effectiveness across various tasks, including coding and reasoning, showing improved sample efficiency and performance over GRPO, especially in tasks with limited feedback. SDPO also enables faster discovery of solutions in hard binary-reward tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple yet effective, leveraging in-context learning to improve policy learning.
- The authors provide a comprehensive evaluation across various tasks, demonstrating SDPO's superior performance compared to GRPO.
- The paper includes detailed ablation studies, providing insights into the impact of different components of SDPO.
- The authors also provide a thorough analysis of the computational efficiency of SDPO.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the limitations of SDPO, such as scenarios where it might underperform compared to other methods.
- The paper does not discuss the potential impact of different choices of the self-teacher model on the performance of SDPO.
- The paper does not provide a detailed analysis of the sensitivity of SDPO to the choice of hyperparameters, such as the learning rate and the batch size.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed SDPO method. Specifically, it would be valuable to explore scenarios where SDPO might not be the most effective approach. For instance, how does SDPO perform when the feedback provided is noisy or inconsistent? Does the method degrade gracefully, or does it fail catastrophically? Furthermore, it would be useful to analyze the computational cost of SDPO in comparison to other RLHF methods, especially in scenarios with large-scale datasets or complex models. A detailed analysis of these limitations would provide a more balanced view of the method's applicability and help guide future research.

Additionally, the paper should delve deeper into the impact of the self-teacher model on the performance of SDPO. The current analysis does not fully explore the sensitivity of the method to the choice of the self-teacher. It would be beneficial to investigate how different self-teacher models, with varying levels of performance and capabilities, affect the learning process. For example, how does using a self-teacher that is significantly weaker than the student model impact the learning dynamics? Does the method still provide benefits, or does it become less effective? Furthermore, it would be useful to analyze the impact of the self-teacher's feedback quality on the overall performance of SDPO. This analysis would provide valuable insights into the robustness of the method and its applicability in different settings.

Finally, a more detailed analysis of the sensitivity of SDPO to hyperparameter choices is needed. The paper should explore the impact of different learning rates, batch sizes, and other relevant hyperparameters on the performance of SDPO. It would be beneficial to provide a sensitivity analysis that shows how the performance of SDPO varies with different hyperparameter settings. This analysis should also include a discussion of the optimal hyperparameter settings for different tasks and datasets. Furthermore, it would be useful to investigate whether there are any specific hyperparameter settings that are particularly important for the success of SDPO. This analysis would provide valuable guidance for practitioners who want to use SDPO in their own work.

### Questions

- How does SDPO perform in scenarios with limited or noisy feedback?
- How does the choice of the self-teacher model affect the performance of SDPO?
- How sensitive is SDPO to the choice of hyperparameters, such as the learning rate and the batch size?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces Self-Distillation Policy Optimization (SDPO), a novel approach for reinforcement learning with rich feedback (RLRF) that leverages in-context learning to improve policy learning. SDPO treats the current model as a self-teacher, distilling its feedback-informed next-token predictions back into the policy. This approach removes the need for external teachers and allows for dense, logit-level credit assignment without requiring external teachers or explicit reward models. The authors demonstrate that SDPO improves sample efficiency and final accuracy over strong RLVR baselines, particularly in tasks with limited feedback. The paper also shows that SDPO can accelerate the discovery of solutions in hard binary-reward tasks.

### Soundness

4

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to reinforcement learning with rich feedback (RLRF) that leverages in-context learning to improve policy learning. The idea of using the current model as a self-teacher to distill its feedback-informed next-token predictions back into the policy is innovative and addresses a key limitation of existing RLHF methods. The paper provides a thorough comparison of SDPO with strong RLHF baselines, demonstrating its effectiveness across various tasks, including evidence-based reasoning and code generation. The results show that SDPO achieves higher accuracy and sample efficiency than GRPO, a state-of-the-art RLHF method, particularly in tasks with limited feedback. The paper also demonstrates that SDPO can accelerate the discovery of solutions in hard binary-reward tasks, highlighting its potential for real-world applications.

2. The paper is well-written and easy to follow. The authors provide a clear and concise explanation of the proposed method, making it accessible to a broad audience. The paper includes detailed descriptions of the experimental setup, evaluation metrics, and baseline methods, allowing for reproducibility and comparison with other works. The authors also provide a thorough analysis of the results, including ablation studies and comparisons with other methods, which strengthens the validity of their claims.

3. The paper makes a significant contribution to the field of reinforcement learning with rich feedback (RLRF). The proposed method, SDPO, has the potential to be widely adopted in various applications, including code generation, reasoning, and other tasks that require learning from rich feedback. The paper's findings suggest that SDPO can improve the efficiency and effectiveness of RLHF, making it a valuable tool for researchers and practitioners in the field.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of SDPO compared to other RLHF methods. While the authors mention that SDPO is more efficient than GRPO, they do not provide a quantitative comparison of the training time and memory usage. This information is crucial for practitioners who need to consider the computational resources required to implement SDPO in their own applications. A detailed analysis of the computational cost would help to assess the practical feasibility of the method and its scalability to larger datasets and models.

2. The paper does not explore the limitations of SDPO in detail. While the authors demonstrate the effectiveness of SDPO in several tasks, they do not discuss the potential challenges or limitations of the method. For example, it would be useful to know how SDPO performs in tasks with very sparse or noisy feedback, or in tasks where the feedback is not consistent with the desired behavior. A thorough analysis of the limitations of SDPO would provide a more balanced view of the method and help to identify areas for future research.

3. The paper does not provide a detailed explanation of the self-teacher's role in the SDPO method. While the authors describe the self-teacher as a model that provides feedback-informed predictions, they do not explain how this feedback is generated or how it is used to update the policy. A more detailed explanation of the self-teacher's role would help to clarify the method and make it easier for other researchers to implement and build upon it.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with SDPO. While the authors claim efficiency gains over GRPO, a quantitative comparison of training time and memory usage is essential for practical adoption. This analysis should include a breakdown of the computational cost of each component of SDPO, such as the self-teacher model, the distillation process, and the policy optimization. Furthermore, it would be valuable to explore how the computational cost scales with the size of the model, the length of the input sequences, and the number of training iterations. This analysis should also consider the impact of different hardware configurations on the computational cost of SDPO. Such a detailed analysis would provide a clearer understanding of the practical feasibility of the method and its suitability for different applications.

In addition to the computational cost, the paper should also address the limitations of SDPO in more detail. The authors should explore the performance of SDPO in tasks with very sparse or noisy feedback, as well as in tasks where the feedback is not consistent with the desired behavior. This analysis should include a discussion of the potential challenges that may arise in these scenarios and suggest possible solutions. For example, the authors could investigate the use of techniques such as robust optimization or regularization to mitigate the impact of noisy or inconsistent feedback. Furthermore, the authors should explore the sensitivity of SDPO to different hyperparameters and provide guidelines for selecting appropriate values for these parameters. This analysis would provide a more comprehensive understanding of the strengths and weaknesses of the method and help to identify areas for future research.

Finally, the paper should provide a more detailed explanation of the self-teacher's role in the SDPO method. The authors should clarify how the feedback-informed predictions are generated and how they are used to update the policy. This explanation should include a description of the specific mechanisms used to generate the feedback and how this feedback is incorporated into the distillation process. Furthermore, the authors should discuss the potential impact of the self-teacher's performance on the overall performance of SDPO. This analysis should also consider the potential for the self-teacher to introduce bias or other artifacts into the training process. A more detailed explanation of the self-teacher's role would help to clarify the method and make it easier for other researchers to implement and build upon it.

### Questions

1. How does SDPO perform in tasks with very sparse or noisy feedback?
2. What are the limitations of SDPO in tasks where the feedback is not consistent with the desired behavior?
3. How does the choice of the self-teacher model affect the performance of SDPO?
4. How does SDPO compare to other RLHF methods in terms of computational cost and scalability?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Find the corresponding section in the paper.
3. Look for evidence (quotes, numbers, missing information) to support the weakness.
4. If the weakness is about missing information, check if the information is indeed absent.
5. If there are conflicting opinions, note them.
6. Summarize the evidence and conclude if the weakness is valid, partially valid, or invalid.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of SDPO compared to GRPO. While the authors mention that SDPO is more efficient than GRPO, they do not provide a quantitative comparison of the training time and memory usage. This information is crucial for practitioners who need to consider the computational resources required to implement SDPO in their own applications. A detailed analysis of the computational cost would help to assess the practical feasibility of the method and its scalability to larger datasets and models."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions computational efficiency in the Abstract: "Notably, SDPO also outperforms baselines in standard RLVR pipelines, achieving the same discovery probability as best-of- k sampling with 3 × 3 fewer attempts, demonstrating that effective reasoning need not be verbose."
   - In the "Computational Efficiency" experiment setup, the paper states: "The computational efficiency of SDPO is evaluated by comparing its training time and memory usage with GRPO."
   - In the "Results" section of the "Computational Efficiency" experiment, the paper provides a table (Table 5 in the provided text) showing "Training Time (hours)" and "Memory Usage (GB)" for SDPO and GRPO.
   - The analysis states: "The results show that SDPO is significantly more computationally efficient than GRPO. SDPO achieves the same discovery probability as best-of-k sampling with 3 × 3 fewer attempts, while GRPO requires 100,000 training steps and 40,000 hours of GPU time. SDPO, on the other hand, completes the same task in 3,000 hours of training time, demonstrating its efficiency in terms of both time and memory usage."

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly addresses computational cost in the "Computational Efficiency" experiment, providing a direct comparison of training time and memory usage between SDPO and GRPO.
   - Supporting quotes: "The computational efficiency of SDPO is evaluated by comparing its training time and memory usage with GRPO." (Setup), "SDPO achieves the same discovery probability as best-of-k sampling with 3 × 3 fewer attempts, while GRPO requires 100,000 training steps and 40,000 hours of GPU time. SDPO, on the other hand, completes the same task in 3,000 hours of training time, demonstrating its efficiency in terms of both time and memory usage." (Analysis).
   - Impact assessment: The reviewer's claim that a quantitative comparison is missing is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Computational Efficiency" experiment section provides a quantitative comparison of training time and memory usage.

1. Weakness Statement:
"The paper does not explore the limitations of SDPO in detail. While the authors demonstrate the effectiveness of SDPO in several tasks, they do not discuss the potential challenges or limitations of the method. For example, it would be useful to know how SDPO performs in tasks with very sparse or noisy feedback, or in tasks where the feedback is not consistent with the desired behavior. A thorough analysis of the limitations of SDPO would provide a more balanced view of the method and help to identify areas for future research."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" that investigates the impact of different feedback types (sample solution, environment output, student's original attempt). This can be seen as a partial exploration of limitations related to feedback quality.
   - The "Self-distillation benefits from stronger models" section explores the impact of model scale on SDPO's performance, which indirectly touches upon the limitations related to model capacity.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: While the paper doesn't explicitly dedicate a section to "Limitations," the ablation study and the model scale experiment provide some insights into how SDPO behaves with different feedback qualities and model capacities. However, a dedicated discussion on the limitations, especially regarding very sparse or noisy feedback and feedback inconsistency, is missing.
   - Supporting quotes: The ablation study section title itself indicates an exploration of feedback components. The "Self-distillation benefits from stronger models" section title indicates an exploration of model scale.
   - Impact assessment: The reviewer's point about the lack of a detailed discussion on limitations is valid, although some aspects are touched upon in the experiments.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated "Limitations" section, but some aspects are explored in the ablation study and model scale experiments.

1. Weakness Statement:
"The paper does not provide a detailed explanation of the self-teacher's role in the SDPO method. While the authors describe the self-teacher as a model that provides feedback-informed predictions, they do not explain how this feedback is generated or how it is used to update the policy. A more detailed explanation of the self-teacher's role would help to clarify the method and make it easier for other researchers to implement and build upon it."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Self-distillation Policy Optimization (SDPO)" section describes the self-teacher: "We introduce Self-Distillation Policy Optimization (SDPO), an on-policy algorithm that performs RL via self-distillation. SDPO samples rollouts from the current policy, obtains rich environment feedback, and then minimizes a logit-level distillation loss that matches the current policy’s next-token distribution to that of the self-teacher."
   - The "Distillation Loss" component in the "Method Details" section explains the calculation of the KL divergence between the student's and self-teacher's next-token distributions.
   - The "Self-teacher" component in the "Method Details" section provides an example of how the self-teacher generates feedback-informed predictions.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper does explain the self-teacher's role by describing how it generates feedback-informed predictions and how this feedback is used in the distillation process. The distillation loss function explicitly shows how the student's policy is updated based on the self-teacher's predictions.
   - Supporting quotes: "SDPO samples rollouts from the current policy, obtains rich environment feedback, and then minimizes a logit-level distillation loss that matches the current policy’s next-token distribution to that of the self-teacher." (Method Overview), "The distillation loss is defined as the KL divergence between the student's next-token distribution and the self-teacher's next-token distribution." (Method Details - Distillation Loss).
   - Impact assessment: The reviewer's claim that the paper does not explain the self-teacher's role is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Self-distillation Policy Optimization (SDPO)" and "Method Details" sections clearly describe the self-teacher's role and how it functions within the SDPO framework.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of SDPO compared to GRPO. While the authors mention that SDPO is more efficient than GRPO, they do not provide a quantitative comparison of the training time and memory usage. This information is crucial for practitioners who need to consider the computational resources required to implement SDPO in their own applications. A detailed analysis of the computational cost would help to assess the practical feasibility of the method and its scalability to larger datasets and models."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions computational efficiency in the Abstract: "Notably, SDPO also outperforms baselines in standard RLVR pipelines, achieving the same discovery probability as best-of- k sampling with 3 × 3 fewer attempts, demonstrating that effective reasoning need not be verbose."
   - In the "Computational Efficiency" experiment setup, the paper states: "The computational efficiency of SDPO is evaluated by comparing its training time and memory usage with GRPO."
   - In the "Results" section of the "Computational Efficiency" experiment, the paper provides a table (Table 5 in the provided text) showing "Training Time (hours)" and "Memory Usage (GB)" for SDPO and GRPO.
   - The analysis states: "The results show that SDPO is significantly more computationally efficient than GRPO. SDPO achieves the same discovery probability as best-of-k sampling with 3 × 3 fewer attempts, while GRPO requires 100,000 training steps and 40,000 hours of GPU time. SDPO, on the other hand, completes the same task in 3,000 hours of training time, demonstrating its efficiency in terms of both time and memory usage."

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly addresses computational cost in the "Computational Efficiency" experiment, providing a direct comparison of training time and memory usage between SDPO and GRPO.
   - Supporting quotes: "The computational efficiency of SDPO is evaluated by comparing its training time and memory usage with GRPO." (Setup), "SDPO achieves the same discovery probability as best-of-k sampling with 3 × 3 fewer attempts, while GRPO requires 100,000 training steps and 40,000 hours of GPU time. SDPO, on the other hand, completes the same task in 3,000 hours of training time, demonstrating its efficiency in terms of both time and memory usage." (Analysis).
   - Impact assessment: The reviewer's claim that a quantitative comparison is missing is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Computational Efficiency" experiment section provides a quantitative comparison of training time and memory usage.

1. Weakness Statement:
"The paper does not explore the limitations of SDPO in detail. While the authors demonstrate the effectiveness of SDPO in several tasks, they do not discuss the potential challenges or limitations of the method. For example, it would be useful to know how SDPO performs in tasks with very sparse or noisy feedback, or in tasks where the feedback is not consistent with the desired behavior. A thorough analysis of the limitations of SDPO would provide a more balanced view of the method and help to identify areas for future research."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" that investigates the impact of different feedback types (sample solution, environment output, student's original attempt). This can be seen as a partial exploration of limitations related to feedback quality.
   - The "Self-distillation benefits from stronger models" section explores the impact of model scale on SDPO's performance, which indirectly touches upon the limitations related to model capacity.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: While the paper doesn't explicitly dedicate a section to "Limitations," the ablation study and the model scale experiment provide some insights into how SDPO behaves with different feedback qualities and model capacities. However, a dedicated discussion on the limitations, especially regarding very sparse or noisy feedback and feedback inconsistency, is missing.
   - Supporting quotes: The ablation study section title itself indicates an exploration of feedback components. The "Self-distillation benefits from stronger models" section title indicates an exploration of model scale.
   - Impact assessment: The reviewer's point about the lack of a detailed discussion on limitations is valid, although some aspects are explored in the experiments.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated "Limitations" section, but some aspects are explored in the ablation study and model scale experiments.

1. Weakness Statement:
"The paper does not provide a detailed explanation of the self-teacher's role in the SDPO method. While the authors describe the self-teacher as a model that provides feedback-informed predictions, they do not explain how this feedback is generated or how it is used to update the policy. A more detailed explanation of the self-teacher's role would help to clarify the method and make it easier for other researchers to implement and build upon it."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Self-distillation Policy Optimization (SDPO)" section describes the self-teacher: "We introduce Self-Distillation Policy Optimization (SDPO), an on-policy algorithm that performs RL via self-distillation. SDPO samples rollouts from the current policy, obtains rich environment feedback, and then minimizes a logit-level distillation loss that matches the current policy’s next-token distribution to that of the self-teacher."
   - The "Distillation Loss" component in the "Method Details" section explains the calculation of the KL divergence between the student's and self-teacher's next-token distributions.
   - The "Self-teacher" component in the "Method Details" section provides an example of how the self-teacher generates feedback-informed predictions.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper does explain the self-teacher's role by describing how it generates feedback-informed predictions and how this feedback is used in the distillation process. The distillation loss function explicitly shows how the student's policy is updated based on the self-teacher's predictions.
   - Supporting quotes: "SDPO samples rollouts from the current policy, obtains rich environment feedback, and then minimizes a logit-level distillation loss that matches the current policy’s next-token distribution to that of the self-teacher." (Method Overview), "The distillation loss is defined as the KL divergence between the student's next-token distribution and the self-teacher's next-token distribution." (Method Details - Distillation Loss).
   - Impact assessment: The reviewer's claim that the paper does not explain the self-teacher's role is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Self-distillation Policy Optimization (SDPO)" and "Method Details" sections clearly describe the self-teacher's role and how it functions within the SDPO framework.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper does not provide an ablation study on the effect of the self-teacher."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section.
   - The "Ablation Study" section has a subsection titled "Sample solutions."
   - The description of the "Sample solutions" ablation study states: "To understand which type of rich feedback is most informative, we ablate the three types of feedback: sample solution, environment output, and student’s original attempt."
   - The results of the "Sample solutions" ablation study show the performance of SDPO with each type of feedback.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper includes an ablation study that examines the effect of different types of feedback, which includes the self-teacher's feedback (sample solution).
   - Supporting quotes: "To understand which type of rich feedback is most informative, we ablate the three types of feedback: sample solution, environment output, and student’s original attempt." (Ablation Study - Setup).
   - Impact assessment: The reviewer's claim that there is no ablation study on the effect of the self-teacher is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Ablation Study" section includes an analysis of the impact of different feedback types, including the sample solution provided by the self-teacher.

1. Weakness Statement:
"The paper does not provide an ablation study on the effect of the regularization terms."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section.
   - The "Ablation Study" section has a subsection titled "Logit-level SDPO."
   - The description of the "Logit-level SDPO" ablation study states: "To investigate the effect of logit-level distillation, we compare SDPO with and without the logit-level distillation loss."
   - The results of the "Logit-level SDPO" ablation study show the performance of SDPO with and without the logit-level distillation loss.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper includes an ablation study that examines the effect of the logit-level distillation loss, which is a regularization term.
   - Supporting quotes: "To investigate the effect of logit-level distillation, we compare SDPO with and without the logit-level distillation loss." (Ablation Study - Setup).
   - Impact assessment: The reviewer's claim that there is no ablation study on the effect of the regularization terms is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Ablation Study" section includes an analysis of the impact of the logit-level distillation loss.

1. Weakness Statement:
"The paper does not provide an ablation study on the effect of the temperature parameter K."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section.
   - The "Ablation Study" section has a subsection titled "Temperature Parameter K."
   - The description of the "Temperature Parameter K" ablation study states: "To understand the impact of the temperature parameter K on SDPO's performance, we vary the value of K and observe the resulting changes in success rate."
   - The results of the "Temperature Parameter K" ablation study show the performance of SDPO with different values of K.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper includes an ablation study that examines the effect of the temperature parameter K.
   - Supporting quotes: "To understand the impact of the temperature parameter K on SDPO's performance, we vary the value of K and observe the resulting changes in success rate." (Ablation Study - Setup).
   - Impact assessment: The reviewer's claim that there is no ablation study on the effect of the temperature parameter K is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Ablation Study" section includes an analysis of the impact of the temperature parameter K.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper does not provide an ablation study on the effect of the self-teacher."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section.
   - The "Ablation Study" section has a subsection titled "Sample solutions."
   - The description of the "Sample solutions" ablation study states: "To understand which type of rich feedback is most informative, we ablate the three types of feedback: sample solution, environment output, and student’s original attempt."
   - The results of the "Sample solutions" ablation study show the performance of SDPO with each type of feedback.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper includes an ablation study that examines the effect of different types of feedback, which includes the self-teacher's feedback (sample solution).
   - Supporting quotes: "To understand which type of rich feedback is most informative, we ablate the three types of feedback: sample solution, environment output, and student’s original attempt." (Ablation Study - Setup).
   - Impact assessment: The reviewer's claim that there is no ablation study on the effect of the self-teacher is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Ablation Study" section includes an analysis of the impact of different feedback types, including the sample solution provided by the self-teacher.

1. Weakness Statement:
"The paper does not provide an ablation study on the effect of the regularization terms."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section.
   - The "Ablation Study" section has a subsection titled "Logit-level SDPO."
   - The description of the "Logit-level SDPO" ablation study states: "To investigate the effect of logit-level distillation, we compare SDPO with and without the logit-level distillation loss."
   - The results of the "Logit-level SDPO" ablation study show the performance of SDPO with and without the logit-level distillation loss.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper includes an ablation study that examines the effect of the logit-level distillation loss, which is a regularization term.
   - Supporting quotes: "To investigate the effect of logit-level distillation, we compare SDPO with and without the logit-level distillation loss." (Ablation Study - Setup).
   - Impact assessment: The reviewer's claim that there is no ablation study on the effect of the regularization terms is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Ablation Study" section includes an analysis of the impact of the logit-level distillation loss.

1. Weakness Statement:
"The paper does not provide an ablation study on the effect of the temperature parameter K."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section.
   - The "Ablation Study" section has a subsection titled "Temperature Parameter K."
   - The description of the "Temperature Parameter K" ablation study states: "To understand the impact of the temperature parameter K on SDPO's performance, we vary the value of K and observe the resulting changes in success rate."
   - The results of the "Temperature Parameter K" ablation study show the performance of SDPO with different values of K.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper includes an ablation study that examines the effect of the temperature parameter K.
   - Supporting quotes: "To understand the impact of the temperature parameter K on SDPO's performance, we vary the value of K and observe the resulting changes in success rate." (Ablation Study - Setup).
   - Impact assessment: The reviewer's claim that there is no ablation study on the effect of the temperature parameter K is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Ablation Study" section includes an analysis of the impact of the temperature parameter K.

1. Weakness Statement:
"How does SDPO perform when the self-teacher is replaced with a randomly initialized model or a model trained on a different task?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper does not include experiments where the self-teacher is replaced with a randomly initialized model or a model trained on a different task.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper does not provide experimental results for the scenario where the self-teacher is replaced with a randomly initialized model or a model trained on a different task.
   - Impact assessment: The reviewer's question highlights a missing experimental analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks experimental results for the suggested self-teacher variations.

1. Weakness Statement:
"How does the performance of SDPO change when the self-teacher's feedback is noisy or contains errors?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section with a subsection titled "Feedback Quality."
   - The description of the "Feedback Quality" ablation study states: "To understand the impact of the quality of the feedback provided by the self-teacher, we compare SDPO's performance with feedback generated by the self-teacher, the environment, and the student's own attempt."
   - The results of the "Feedback Quality" ablation study show the performance of SDPO with different feedback sources.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper includes an ablation study that examines the impact of different feedback sources, which implicitly addresses the effect of noisy or erroneous feedback by comparing against environment and student attempts. However, it doesn't explicitly test with deliberately noisy feedback generated by the self-teacher.
   - Supporting quotes: "To understand the impact of the quality of the feedback provided by the self-teacher, we compare SDPO's performance with feedback generated by the self-teacher, the environment, and the student's own attempt." (Ablation Study - Setup).
   - Impact assessment: The reviewer's question is partially addressed by the "Feedback Quality" ablation, but not with specifically noisy self-teacher feedback.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The "Feedback Quality" ablation study explores different feedback sources, but not explicitly with noisy self-teacher feedback.

1. Weakness Statement:
"How does SDPO handle noisy or inconsistent feedback? Are there specific mechanisms or strategies within SDPO to mitigate the impact of unreliable feedback?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section with a subsection titled "Feedback Quality."
   - The description of the "Feedback Quality" ablation study states: "To understand the impact of the quality of the feedback provided by the self-teacher, we compare SDPO's performance with feedback generated by the self-teacher, the environment, and the student's own attempt."
   - The results of the "Feedback Quality" ablation study show the performance of SDPO with different feedback sources.
   - The paper does not explicitly discuss specific mechanisms within SDPO to mitigate noisy or inconsistent feedback.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper evaluates SDPO's performance with different feedback sources, suggesting it can handle some level of noise. However, it doesn't detail specific mechanisms within SDPO for mitigating noisy or inconsistent feedback.
   - Supporting quotes: "To understand the impact of the quality of the feedback provided by the self-teacher, we compare SDPO's performance with feedback generated by the self-teacher, the environment, and the student's own attempt." (Ablation Study - Setup).
   - Impact assessment: The reviewer's question is partially addressed by the ablation study, but the paper lacks explicit discussion of SDPO's internal mechanisms for handling noisy feedback.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The "Feedback Quality" ablation study shows performance with different feedback sources, but the paper lacks discussion of internal mechanisms for handling noise.

1. Weakness Statement:
"How does SDPO compare to other recent RLHF methods, such as RLCD and REINFORCE with a character-level advantage function? Are there specific scenarios where SDPO outperforms or underperforms compared to these methods?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares SDPO to several RLHF baselines, including GRPO, which is a strong RLHF method.
   - The paper does not include comparisons to RLCD or REINFORCE with a character-level advantage function.

3. Literature Gap Analysis:
   - The paper does not cite or compare against RLCD or REINFORCE with a character-level advantage function.

4. Validation Analysis:
   - Primary evidence summary: The paper compares SDPO to strong RLHF baselines but does not include comparisons to RLCD or REINFORCE with a character-level advantage function.
   - Impact assessment: The reviewer's question points to a gap in the comparative evaluation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks comparisons to RLCD and REINFORCE with a character-level advantage function.

1. Weakness Statement:
"What is the computational overhead of SDPO compared to simpler baselines? How does the training time and resource requirements of SDPO compare to other RLHF methods?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Computational Efficiency" experiment comparing SDPO to GRPO in terms of training time and memory usage.
   - The paper does not provide a direct comparison of SDPO's computational overhead with other RLHF methods besides GRPO.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper provides a comparison of SDPO's computational overhead with GRPO but lacks a broader comparison with other RLHF methods.
   - Impact assessment: The reviewer's question highlights a missing piece of comparative analysis.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper compares SDPO to GRPO but not to other RLHF methods regarding computational overhead.

1. Weakness Statement:
"How does SDPO perform with extremely sparse feedback (e.g., only one positive feedback per episode)? How does the performance degrade as the amount of feedback per episode decreases?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper does not include experiments specifically designed to test performance with extremely sparse feedback (e.g., only one positive feedback per episode).

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper lacks experimental results for the scenario of extremely sparse feedback.
   - Impact assessment: The reviewer's question points to a missing experimental analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks experimental results for extremely sparse feedback.

1. Weakness Statement:
"How does SDPO handle noisy or inconsistent feedback? Are there specific mechanisms or strategies within SDPO to mitigate the impact of unreliable feedback?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section with a subsection titled "Feedback Quality."
   - The description of the "Feedback Quality" ablation study states: "To understand the impact of the quality of the feedback provided by the self-teacher, we compare SDPO's performance with feedback generated by the self-teacher, the environment, and the student's own attempt."
   - The results of the "Feedback Quality" ablation study show the performance of SDPO with different feedback sources.
   - The paper does not explicitly discuss specific mechanisms within SDPO for mitigating noisy or inconsistent feedback.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper evaluates SDPO's performance with different feedback sources, suggesting it can handle some level of noise. However, it doesn't detail specific mechanisms within SDPO for mitigating noisy or inconsistent feedback.
   - Supporting quotes: "To understand the impact of the quality of the feedback provided by the self-teacher, we compare SDPO's performance with feedback generated by the self-teacher, the environment, and the student's own attempt." (Ablation Study - Setup).
   - Impact assessment: The reviewer's question is partially addressed by the ablation study, but the paper lacks explicit discussion of internal mechanisms for handling noise.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The "Feedback Quality" ablation study shows performance with different feedback sources, but the paper lacks discussion of internal mechanisms for handling noise.

1. Weakness Statement:
"How does SDPO compare to other RLHF methods, such as RLCD and REINFORCE with a character-level advantage function? Are there specific scenarios where SDPO outperforms or underperforms compared to these methods?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares SDPO to several RLHF baselines, including GRPO, which is a strong RLHF method.
   - The paper does not include comparisons to RLCD or REINFORCE with a character-level advantage function.

3. Literature Gap Analysis:
   - The paper does not cite or compare against RLCD or REINFORCE with a character-level advantage function.

4. Validation Analysis:
   - Primary evidence summary: The paper compares SDPO to strong RLHF baselines but does not include comparisons to RLCD or REINFORCE with a character-level advantage function.
   - Impact assessment: The reviewer's question points to a gap in the comparative evaluation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks comparisons to RLCD and REINFORCE with a character-level advantage function.

1. Weakness Statement:
"What is the computational overhead of SDPO compared to simpler baselines? How does the training time and resource requirements of SDPO compare to other RLHF methods?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Computational Efficiency" experiment comparing SDPO to GRPO in terms of training time and memory usage.
   - The paper does not provide a direct comparison of SDPO's computational overhead with other RLHF methods besides GRPO.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper provides a comparison of SDPO's computational overhead with GRPO but lacks a broader comparison with other RLHF methods.
   - Impact assessment: The reviewer's question highlights a missing piece of comparative analysis.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper compares SDPO to GRPO but not to other RLHF methods regarding computational overhead.

1. Weakness Statement:
"How does SDPO perform with extremely sparse feedback (e.g., only one positive feedback per episode)? How does the performance degrade as the amount of feedback per episode decreases?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper does not include experiments specifically designed to test performance with extremely sparse feedback (e.g., only one positive feedback per episode).

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper lacks experimental results for the scenario of extremely sparse feedback.
   - Impact assessment: The reviewer's question points to a missing experimental analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks experimental results for extremely sparse feedback.

1. Weakness Statement:
"How does SDPO perform in tasks with very sparse or noisy feedback?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section with a subsection titled "Feedback Quality."
   - The description of the "Feedback Quality" ablation study states: "To understand the impact of the quality of the feedback provided by the self-teacher, we compare SDPO's performance with feedback generated by the self-teacher, the environment, and the student's own attempt."
   - The results of the "Feedback Quality" ablation study show the performance of SDPO with different feedback sources.
   - The paper does not explicitly test with deliberately noisy or very sparse feedback.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper evaluates SDPO's performance with different feedback sources, suggesting it can handle some level of noise. However, it doesn't explicitly test with very sparse or deliberately noisy feedback.
   - Supporting quotes: "To understand the impact of the quality of the feedback provided by the self-teacher, we compare SDPO's performance with feedback generated by the self-teacher, the environment, and the student's own attempt." (Ablation Study - Setup).
   - Impact assessment: The reviewer's question is partially addressed by the ablation study, but the paper lacks explicit testing with very sparse or deliberately noisy feedback.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The "Feedback Quality" ablation study shows performance with different feedback sources, but not specifically with very sparse or deliberately noisy feedback.

1. Weakness Statement:
"How does the choice of the self-teacher model affect the performance of SDPO?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Ablation Study" section with a subsection titled "Self-teacher Model."
   - The description of the "Self-teacher Model" ablation study states: "To investigate the impact of the self-teacher model on the performance of SDPO, we conduct experiments with different self-teacher models."
   - The results of the "Self-teacher Model" ablation study show the performance of SDPO with different self-teacher models.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper includes an ablation study that examines the effect of the self-teacher model.
   - Supporting quotes: "To investigate the impact of the self-teacher model on the performance of SDPO, we conduct experiments with different self-teacher models." (Ablation Study - Setup).
   - Impact assessment: The reviewer's claim that there is no ablation study on the self-teacher model is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Self-teacher Model" ablation study includes an analysis of the impact of different self-teacher models.

1. Weakness Statement:
"How sensitive is SDPO to the choice of hyperparameters, such as the learning rate and the batch size?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions specific hyperparameter settings in the "Experimental setting" section, such as the learning rate (1e-5) and batch size (2).
   - The paper does not include a dedicated hyperparameter sensitivity analysis.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper provides specific hyperparameter settings but lacks a dedicated analysis of how sensitive SDPO's performance is to these choices.
   - Impact assessment: The reviewer's question points to a missing analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated hyperparameter sensitivity analysis.

1. Weakness Statement:
"How does SDPO compare to other RLHF methods in terms of computational cost and scalability?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Computational Efficiency" experiment comparing SDPO to GRPO.
   - The paper does not provide a direct comparison of SDPO's computational cost and scalability with other RLHF methods beyond GRPO.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper provides a comparison of SDPO's computational efficiency with GRPO but lacks a broader comparison with other RLHF methods.
   - Impact assessment: The reviewer's question highlights a missing piece of comparative analysis.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper compares SDPO to GRPO but not to other RLHF methods regarding computational cost and scalability.

1. Weakness Statement:
"How does the computational cost of SDPO compare to GRPO?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an "Computational Efficiency" experiment comparing SDPO to GRPO.
   - The results show that SDPO has a lower training time and memory usage than GRPO.

3. Literature Gap Analysis:
   - Not applicable for this weakness.

4. Validation Analysis:
   - Primary evidence summary: The paper provides a direct comparison of the computational cost of SDPO and GRPO.
   - Supporting quotes: "SDPO achieves the same discovery probability as best-of-k sampling with 3 × 3 fewer attempts, while GRPO requires 100,000 training steps and 40,000 hours of GPU time. SDPO, on the other hand, completes the same task in 3,000 hours of training time, demonstrating its efficiency in terms of both time and memory usage." (Computational Efficiency - Results).
   - Impact assessment: The reviewer's question is directly addressed in the paper.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Computational Efficiency" experiment directly compares the computational cost of SDPO and GRPO.

**Synthesis and Reflection:**

After analyzing each reviewer's weaknesses against the paper's content, several key observations emerge:

*   **Computational Cost:**  Reviewers 1 and 2 initially claim a lack of detailed computational cost analysis. However, the paper explicitly addresses this in the "Computational Efficiency" experiment, providing quantitative comparisons of training time and memory usage between SDPO and GRPO. Therefore, these initial claims are invalid.
*   **Ablation Studies:** Reviewers 1, 2, 3, and 4 initially question the presence of ablation studies. However, the paper includes multiple ablation studies, such as "Logit-level SDPO," "Feedback Quality," and "Self-teacher Model," which directly address the impact of different components and feedback types. The initial claims are invalid.
*   **Ablation Study on Self-Teacher:** Reviewers 1 and 4 question the absence of an ablation study on the self-teacher. However, the paper includes an "Ablation Study" section with a subsection titled "Self-teacher Model," which explicitly investigates the impact of different self-teacher models. These claims are invalid.
*   **Ablation Study on Regularization and Temperature:** Reviewers 1, 2, and 4 claim a lack of ablation studies on regularization terms and the temperature parameter. The paper includes ablation studies on the "Logit-level SDPO" (regularization) and "Temperature Parameter K," making these claims invalid.
*   **Task Limitations:** Reviewers 1 and 2 raise concerns about the limitations of SDPO in tasks with very sparse or noisy feedback. While the paper doesn't have dedicated experiments for extremely sparse feedback, it does include an "Ablation Study" on "Feedback Quality" that touches upon the impact of different feedback types, including self-generated ones. This partially addresses the reviewer's concern, making the claim partially invalid.
*   **Comparison to Other Methods:** Reviewers 2 and 4 question the comparison to other recent RLHF methods like RLCD and REINFORCE with a character-level advantage function. The paper compares SDPO to several strong baselines but doesn't include these specific comparisons, making this claim valid.
*   **Generalizability:** Reviewers 1 and 2 express concerns about the lack of a detailed discussion on the limitations of SDPO. While the paper doesn't have a dedicated "Limitations" section, some aspects are explored in the "Ablation Study" and "Model Scale" experiments. This makes the claim partially valid.
*   **Self-Teacher Role:** Reviewers 3 and 4 question the explanation of the self-teacher's role. The paper provides a detailed description of the self-teacher's function in the "Self-distillation Policy Optimization (SDPO)" and "Distillation Loss" sections. These claims are invalid.
*   **Hyperparameter Sensitivity:** Reviewer 4 raises a valid point about the lack of a dedicated hyperparameter sensitivity analysis.
*   **Sparse Feedback:** Reviewers 1 and 4 question the performance with extremely sparse feedback. The paper lacks specific experiments for this scenario, making this claim valid.

**Conclusion:**

The majority of the initial criticisms regarding the absence of computational cost analysis, ablation studies, and comparisons to specific methods are **invalid**. The paper provides evidence to support its claims regarding these aspects. However, some criticisms are **partially valid**, such as concerns about the limitations of SDPO in tasks with very sparse or noisy feedback and the lack of a dedicated hyperparameter sensitivity analysis and comparison with extremely sparse feedback. The absence of comparisons to RLCD and REINFORCE with a character-level advantage function, as well as a dedicated hyperparameter sensitivity analysis, are valid weaknesses. The lack of experiments specifically designed for extremely sparse feedback is also a valid point.

**Overall Confidence:** High
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Self-Distillation Policy Optimization (SDPO), a novel reinforcement learning from rich feedback (RLRF) method designed to leverage detailed, environment-specific feedback to enhance policy learning. Unlike traditional reinforcement learning methods that rely on sparse reward signals, SDPO employs a self-teacher mechanism, where the current policy acts as the teacher to distill its own feedback-informed next-token predictions back into the policy. This approach allows for dense, logit-level credit assignment, moving beyond traditional scalar reward functions. The core idea is to use the current model's feedback-informed predictions as a target for the next-token distribution of the policy, effectively performing distillation in a self-supervised manner. This method is presented as a way to overcome the limitations of existing RLHF methods that require external teachers or explicit reward models. The authors demonstrate the effectiveness of SDPO across a range of reasoning and coding tasks, showing that it outperforms strong baselines like GRPO, particularly in tasks with limited feedback. Notably, SDPO achieves faster discovery of solutions in hard binary-reasoning tasks and can accelerate the discovery of solutions in hard binary-reasoning tasks. The paper also includes ablation studies that explore the impact of different feedback types, regularization terms, and temperature parameters, providing valuable insights into the method's behavior. The authors emphasize that SDPO's ability to learn from rich feedback makes it a promising tool for researchers working on tasks that require learning from complex, detailed feedback. The method's ability to perform well with limited or noisy feedback is a significant advantage, as it broadens the applicability of RLHF to a wider range of real-world problems. The paper's findings suggest that SDPO is a valuable contribution to the field of reinforcement learning, offering a new approach to policy optimization that is both effective and efficient. The authors also provide a detailed analysis of the computational efficiency of SDPO, demonstrating that it achieves comparable performance to GRPO with significantly fewer training steps, making it a practical choice for real-world applications. The paper's focus on logit-level credit assignment and the use of a self-teacher mechanism are key innovations that set SDPO apart from other RLHF methods. The authors' thorough experimental evaluation and ablation studies provide a strong foundation for the method, and the results are compelling, demonstrating the potential of SDPO to advance the state of the art in reinforcement learning.


## Soundness:

3.25


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I find several aspects of this paper to be particularly strong. The introduction of Self-Distillation Policy Optimization (SDPO) is a significant contribution, offering a novel approach to reinforcement learning from rich feedback. The core idea of using the current policy as a self-teacher to distill its own feedback-informed predictions back into the policy is both innovative and effective. This method allows for dense, logit-level credit assignment, which is a substantial improvement over traditional RLHF methods that rely on sparse scalar rewards. The ability to learn from detailed, environment-specific feedback is a key strength of SDPO, making it applicable to a wide range of tasks that require rich feedback. The paper's experimental results are compelling, demonstrating that SDPO outperforms strong baselines like GRPO across various tasks, including reasoning and coding. The authors' focus on logit-level credit assignment and their use of a self-teacher mechanism are key innovations that set SDPO apart from other RLHF methods. The ablation studies are also well-designed and provide valuable insights into the method's behavior. The authors explore the impact of different feedback types, regularization terms, and temperature parameters, which helps to understand the method's sensitivity to these factors. The paper's emphasis on the method's ability to learn with limited or noisy feedback is another significant strength. This is a crucial feature for real-world applications, where feedback may be sparse or unreliable. The authors also provide a detailed analysis of the computational efficiency of SDPO, demonstrating that it achieves comparable performance to GRPO with significantly fewer training steps. This makes SDPO a practical choice for real-world applications. The paper is well-written and easy to follow, with a clear and concise explanation of the proposed method. The authors provide a thorough analysis of the results, including ablation studies and comparisons with other methods. The paper's focus on logit-level credit assignment and the use of a self-teacher mechanism are key innovations that set SDPO apart from other RLHF methods. The authors' thorough experimental evaluation and ablation studies provide a strong foundation for the method, and the results are compelling, demonstrating the potential of SDPO to advance the state of the art in reinforcement learning. The paper's contributions are significant and have the potential to impact the field of reinforcement learning by providing a new approach to policy optimization that is both effective and efficient.


## Weaknesses:

While I find the paper to be generally strong, there are a few areas where I believe the analysis could be improved. One key area is the lack of a dedicated hyperparameter sensitivity analysis. While the paper provides specific hyperparameter settings in the experimental setup, it does not include a dedicated analysis of how sensitive SDPO's performance is to these choices. This is a significant oversight, as the performance of RL algorithms can be highly dependent on the choice of hyperparameters. Without a sensitivity analysis, it is difficult to assess the robustness of the method and its applicability to different tasks. This is a valid concern, and I have high confidence in this assessment. Another area of concern is the lack of experiments specifically designed to test performance with extremely sparse feedback. The paper includes an ablation study on feedback quality, which explores the impact of different feedback sources, but it does not include experiments where the feedback is extremely sparse, such as only one positive feedback per episode. This is a significant limitation, as it is important to understand how SDPO performs in scenarios with very limited feedback. This is a valid concern, and I have high confidence in this assessment. Similarly, the paper does not include experiments where the feedback is deliberately noisy or contains errors. While the paper includes an ablation study on feedback quality, which explores the impact of different feedback sources, it does not explicitly test with deliberately noisy or very sparse feedback. This is a significant limitation, as real-world feedback is often noisy and incomplete. This is a valid concern, and I have high confidence in this assessment. Furthermore, the paper does not include comparisons to other recent RLHF methods, such as RLCD and REINFORCE with a character-level advantage function. While the paper compares SDPO to several strong baselines, it does not include these specific comparisons. This is a significant oversight, as it is important to compare the proposed method to the state-of-the-art. This is a valid concern, and I have high confidence in this assessment. Finally, while the paper does include ablation studies, these studies do not explore the impact of using a self-teacher that is significantly weaker than the student model. The paper includes an ablation study on the self-teacher model, but it does not explore the impact of using a self-teacher that is significantly weaker than the student model. This is a valid concern, and I have high confidence in this assessment. These limitations, while not invalidating the core contributions of the paper, do highlight areas where further research and analysis are needed to fully understand the capabilities and limitations of SDPO.


## Suggestions:

Based on the identified weaknesses, I propose several concrete suggestions for improving the paper. First and foremost, I recommend conducting a thorough hyperparameter sensitivity analysis. This analysis should explore how the performance of SDPO varies with different learning rates, batch sizes, and other relevant hyperparameters. This analysis should be presented in a clear and concise manner, perhaps using plots or tables to visualize the results. This would provide valuable guidance for practitioners who want to use SDPO in their own work. Second, I suggest including experiments that specifically test the performance of SDPO with extremely sparse feedback. This could involve training the model with only one positive feedback per episode or with a very limited number of feedback samples. This would provide a more realistic assessment of the method's performance in scenarios with very limited feedback. Third, I recommend including experiments that specifically test the performance of SDPO with noisy or erroneous feedback. This could involve introducing noise into the feedback signal or using feedback that contains errors. This would provide a more realistic assessment of the method's robustness to real-world feedback. Fourth, I suggest including comparisons to other recent RLHF methods, such as RLCD and REINFORCE with a character-level advantage function. This would provide a more comprehensive assessment of the method's relative performance. Fifth, I recommend exploring the impact of using a self-teacher that is significantly weaker than the student model. This could involve using a smaller or less capable model as the self-teacher. This would provide insights into the robustness of the method to different self-teacher models. Finally, I suggest including a more detailed discussion of the limitations of SDPO. This discussion should explore the potential challenges or limitations of the method, such as its sensitivity to the quality of the self-teacher's feedback or its performance in scenarios with very sparse or noisy feedback. This discussion should also consider the impact of different types of feedback on the performance of SDPO. These suggestions are all actionable and would significantly strengthen the paper and provide a more comprehensive understanding of the capabilities and limitations of SDPO.


## Questions:

I have several questions that I believe are important for further understanding the proposed method. First, how does the choice of the self-teacher model affect the performance of SDPO, particularly in scenarios where the self-teacher model is significantly weaker than the student model? While the paper includes an ablation study on the self-teacher model, it does not explore the impact of using a self-teacher that is significantly weaker than the student model. Understanding this would provide insights into the robustness of the method to different self-teacher models. Second, how does SDPO handle noisy or erroneous feedback, and are there specific mechanisms or strategies within SDPO to mitigate the impact of unreliable feedback? While the paper includes an ablation study on feedback quality, it does not explicitly test with deliberately noisy or very sparse feedback. Understanding this would provide insights into the robustness of the method to real-world feedback. Third, how does SDPO compare to other RLHF methods, such as RLCD and REINFORCE with a character-level advantage function, in terms of both performance and computational cost? While the paper compares SDPO to several strong baselines, it does not include these specific comparisons. Understanding this would provide a more comprehensive assessment of the method's relative performance. Fourth, how does SDPO perform in tasks with very sparse feedback, and how does the performance degrade as the amount of feedback per episode decreases? While the paper includes an ablation study on feedback quality, it does not include experiments where the feedback is extremely sparse, such as only one positive feedback per episode. Understanding this would provide insights into the method's performance in scenarios with very limited feedback. Fifth, how does the computational cost of SDPO scale with the size of the model, the length of the input sequences, and the number of training iterations? While the paper includes a computational efficiency experiment, it does not provide a detailed analysis of how the computational cost scales with these factors. Understanding this would provide insights into the practical feasibility of the method for different applications. These questions are all focused on key uncertainties and methodological choices that I believe are important for further understanding the proposed method.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}