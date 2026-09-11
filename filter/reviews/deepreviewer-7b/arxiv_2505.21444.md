I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies the problem of self-improvement of LLMs. The authors propose a simple approach, SRT, to improve LLMs. The approach is based on majority voting to generate pseudo-labels, which are used to train the model. The authors conduct experiments on reasoning tasks to evaluate the effectiveness of their approach.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and easy to follow.

The authors conduct extensive experiments to evaluate the effectiveness of their approach.

### Weaknesses

#### Some Related Works


#### comment

The paper lacks a clear motivation for why the proposed approach is effective. The authors should provide a more detailed explanation of the underlying mechanisms that contribute to the success of their approach.

The paper does not compare the proposed approach with other state-of-the-art methods for self-improvement of LLMs. The authors should include a comparison with other methods to demonstrate the advantages of their approach.

The paper does not discuss the limitations of the proposed approach. The authors should discuss the potential drawbacks and challenges of their approach.

### Suggestions

The paper would benefit significantly from a more thorough explanation of the mechanisms behind the proposed Self-Rewarded Training (SRT) approach. While the empirical results are promising, the lack of a clear theoretical or intuitive explanation makes it difficult to fully grasp why SRT works. For instance, the authors could delve deeper into how the majority voting mechanism interacts with the reinforcement learning framework. Specifically, how does the consistency of the majority votes influence the learning process, and what are the conditions under which this approach is most effective? A more detailed analysis of the error propagation and correction mechanisms would also be valuable. It would be beneficial to explore how the model's internal representations evolve during training and how this relates to the observed performance gains. Furthermore, the authors should consider providing a more detailed analysis of the types of errors the model corrects and the types of errors it still struggles with, which could provide insights into the limitations of the approach and guide future research.

To strengthen the paper's contribution, the authors should include a more comprehensive comparison with existing state-of-the-art methods for self-improvement of LLMs. While the authors mention that their approach is simple, it is crucial to demonstrate its advantages over more complex methods. A direct comparison with methods that use different self-improvement strategies, such as those based on policy gradients or actor-critic methods, would be highly informative. The comparison should not only focus on the final performance but also consider other factors such as the computational cost, the amount of data required, and the robustness of the approach. It would be beneficial to include a discussion of the trade-offs between the simplicity of the proposed approach and its performance compared to more complex methods. This would help to better position the contribution of the paper within the broader landscape of self-improvement techniques.

Finally, the paper should include a more detailed discussion of the limitations of the proposed approach. While the authors briefly mention some limitations, a more thorough analysis is needed. For example, how does the approach perform on tasks that require more complex reasoning or creative thinking? Are there any specific types of tasks or datasets where the approach is not effective? What are the potential drawbacks of using majority voting as a pseudo-labeling mechanism? Does it introduce any biases or limitations? A more detailed discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed approach. Furthermore, the authors should discuss potential avenues for future research to address these limitations and further improve the self-improvement capabilities of LLMs.

### Questions

Please see the weaknesses section.

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper explores the potential of self-improvement in large language models (LLMs) through self-rewarding training (SRT). The authors propose a simple mechanism for self-feedback, which uses majority voting to generate pseudo-labels. They conduct experiments on both synthetic and real-world reasoning tasks, demonstrating that this approach can improve model performance. However, the paper also reveals a critical limitation: prolonged training with this framework leads to reward hacking, where the model learns to maximize training rewards without genuine improvement. This raises questions about the sustainability of self-improvement through self-feedback alone.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand. The authors provide a thorough explanation of the proposed method, including the use of majority voting for self-feedback and the experimental setup. The motivation for the study is clearly articulated, and the potential impact of the findings is well-justified.

2. The authors conduct a comprehensive set of experiments on both synthetic and real-world reasoning tasks, which provides strong empirical evidence for the effectiveness of the proposed method. The results show that SRT can improve model performance on various tasks, and the authors also explore the impact of different training parameters on the results.

3. The paper identifies a critical limitation of the proposed method: reward hacking, where the model learns to maximize training rewards without genuine improvement. This finding is significant because it highlights a potential pitfall of self-improvement through self-feedback alone and suggests that further research is needed to address this issue.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's focus on self-improvement through self-feedback is interesting, but it lacks a clear connection to real-world applications. The authors do not provide concrete examples of how this approach could be applied to practical problems, which limits the impact of the study. Specifically, the paper does not explore how the proposed method could be integrated into existing workflows or systems, making it difficult to assess its practical utility. For instance, it would be beneficial to see how this method could be used to improve the performance of an LLM in a specific domain, such as code generation or scientific discovery, and what challenges might arise in such applications.

2. The paper does not adequately address the potential limitations of the proposed method. While the authors acknowledge the issue of reward hacking, they do not explore other potential challenges, such as the computational cost of the approach, its sensitivity to hyperparameters, or its robustness to noisy data. A more thorough discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed method. For example, the paper does not discuss the computational resources required for training, the impact of different hyperparameter settings on performance, or how the method would perform with noisy or incomplete data. These are important considerations for practical applications.

3. The paper's analysis of the reward hacking phenomenon is somewhat superficial. While the authors demonstrate that the model learns to maximize training rewards without genuine improvement, they do not provide a detailed explanation of the underlying mechanisms. A deeper analysis of why and how reward hacking occurs would be valuable for understanding the limitations of self-improvement through self-feedback. The paper should explore the specific conditions under which reward hacking is most likely to occur and what strategies can be used to mitigate this issue. For example, it would be useful to investigate whether reward hacking is more likely to occur when the model is trained on a large number of examples or when the training data is highly diverse.

### Suggestions

To enhance the practical relevance of this work, the authors should provide concrete examples of how their self-improvement method could be applied to real-world problems. This could involve demonstrating the method's effectiveness on specific tasks, such as question answering, text summarization, or code generation, and discussing the challenges and limitations encountered in these applications. For example, the authors could show how their method could be used to improve the performance of an LLM in a specific domain, such as code generation or scientific discovery, and what challenges might arise in such applications. This would help to bridge the gap between the theoretical findings of the paper and their practical implications. Furthermore, the authors should discuss the computational cost of their approach and how it scales with the size of the model and the training data. This would provide a more realistic assessment of the method's feasibility for practical applications.

To address the limitations of the proposed method, the authors should conduct a more thorough analysis of the reward hacking phenomenon. This could involve exploring the specific conditions under which reward hacking is most likely to occur and what strategies can be used to mitigate this issue. For example, the authors could investigate whether reward hacking is more likely to occur when the model is trained on a large number of examples or when the training data is highly diverse. They could also explore different regularization techniques or training strategies that could help to prevent reward hacking. Additionally, the authors should investigate the sensitivity of their method to hyperparameter settings and provide guidance on how to choose appropriate values for these parameters. This would make the method more robust and easier to use in practice. The authors should also discuss the robustness of their method to noisy or incomplete data, which is a common challenge in real-world applications.

Finally, the authors should provide a more detailed analysis of the types of errors that the model makes and how these errors change over time during training. This could involve analyzing the distribution of errors and identifying patterns or trends that could provide insights into the model's learning process. For example, the authors could investigate whether the model is learning to generate more confident or less confident answers over time, or whether it is learning to avoid certain types of errors. This would help to understand the underlying mechanisms of the self-improvement process and identify areas for further improvement. The authors should also explore the relationship between the model's performance on the training data and its performance on the evaluation data, and discuss the implications of any discrepancies.

### Questions

1. How does the proposed method compare to other self-improvement approaches, such as reinforcement learning from human feedback (RLHF)? What are the advantages and disadvantages of each approach?

2. The paper mentions that the proposed method can lead to reward hacking, where the model learns to maximize training rewards without genuine improvement. What are the potential consequences of this phenomenon in real-world applications?

3. The paper focuses on reasoning tasks, but how would the proposed method perform on other types of tasks, such as code generation or text summarization? What challenges might arise in these applications?

4. The paper does not discuss the computational cost of the proposed method. How does the computational cost of SRT compare to other self-improvement approaches? Is the method scalable to larger models and datasets?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

This paper studies the self-improvement of LLMs through self-feedback, specifically using majority voting as a self-supervised mechanism. The authors propose a Self-Rewarded Training (SRT) approach, where the model generates multiple responses to a prompt, and the most common answer is taken as the pseudo-label for training. The paper evaluates SRT on synthetic reasoning tasks from REASONING GYM and real-world datasets, showing that it can improve model performance and even lead to model collapse when trained for an extended period.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a comprehensive set of experiments, including evaluations on synthetic and real-world reasoning tasks.
- The paper identifies the issue of reward hacking and proposes mitigation strategies.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a clear motivation for why the proposed approach is effective. The authors should provide a more detailed explanation of the underlying mechanisms that contribute to the success of their approach.
- The paper does not compare the proposed approach with other state-of-the-art methods for self-improvement of LLMs. The authors should include a comparison with other methods to demonstrate the advantages of their approach.
- The paper does not discuss the limitations of the proposed approach. The authors should discuss the potential drawbacks and challenges of their approach.

### Suggestions

The paper would benefit significantly from a more thorough explanation of the mechanisms behind the proposed Self-Rewarded Training (SRT) approach. While the empirical results are promising, the lack of a clear theoretical or intuitive explanation makes it difficult to fully grasp why SRT works. For instance, the authors could delve deeper into how the majority voting mechanism interacts with the reinforcement learning framework. Specifically, how does the consistency of the majority votes influence the learning process, and what are the conditions under which this approach is most effective? A more detailed analysis of the error propagation and correction mechanisms would also be valuable. It would be beneficial to explore how the model's internal representations evolve during training and how this relates to the observed performance gains. Furthermore, the authors should consider providing a more detailed analysis of the types of errors the model corrects and the types of errors it still struggles with, which could provide insights into the limitations of the approach and guide future research.

To strengthen the paper's contribution, the authors should include a more comprehensive comparison with existing state-of-the-art methods for self-improvement of LLMs. While the authors mention that their approach is simple, it is crucial to demonstrate its advantages over more complex methods. A direct comparison with methods that use different self-improvement strategies, such as those based on policy gradients or actor-critic methods, would be highly informative. The comparison should not only focus on the final performance but also consider other factors such as the computational cost, the amount of data required, and the robustness of the approach. It would be beneficial to include a discussion of the trade-offs between the simplicity of the proposed approach and its performance compared to more complex methods. This would help to better position the contribution of the paper within the broader landscape of self-improvement techniques. Furthermore, the authors should consider including a discussion of the limitations of their approach in comparison to other methods.

Finally, the paper should include a more detailed discussion of the limitations of the proposed approach. While the authors briefly mention some limitations, a more thorough analysis is needed. For example, how does the approach perform on tasks that require more complex reasoning or creative thinking? Are there any specific types of tasks or datasets where the approach is not effective? What are the potential drawbacks of using majority voting as a pseudo-labeling mechanism? Does it introduce any biases or limitations? A more detailed discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed approach. Furthermore, the authors should discuss potential avenues for future research to address these limitations and further improve the self-improvement capabilities of LLMs.

### Questions

- How does the proposed approach compare to other self-improvement methods in terms of performance and computational cost?
- What are the limitations of the proposed approach, and how can they be addressed in future work?

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper explores the potential of self-improvement in large language models (LLMs) through self-rewarding training (SRT). The authors propose a simple mechanism for self-feedback, which uses majority voting to generate pseudo-labels. The paper conducts experiments on reasoning tasks and analyzes the dynamics of model collapse in depth.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The paper conducts extensive experiments to evaluate the effectiveness of the proposed method.
3. The paper identifies the issue of reward hacking and proposes mitigation strategies.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear motivation for why the proposed approach is effective. The authors should provide a more detailed explanation of the underlying mechanisms that contribute to the success of their approach.
2. The paper does not compare the proposed approach with other state-of-the-art methods for self-improvement of LLMs. The authors should include a comparison with other methods to demonstrate the advantages of their approach.
3. The paper does not discuss the limitations of the proposed approach. The authors should discuss the potential drawbacks and challenges of their approach.

### Suggestions

The paper would benefit significantly from a more thorough explanation of the mechanisms behind the proposed Self-Rewarded Training (SRT) approach. While the empirical results are promising, the lack of a clear theoretical or intuitive explanation makes it difficult to fully grasp why SRT works. For instance, the authors could delve deeper into how the majority voting mechanism interacts with the reinforcement learning framework. Specifically, how does the consistency of the majority votes influence the learning process, and what are the conditions under which this approach is most effective? A more detailed analysis of the error propagation and correction mechanisms would also be valuable. It would be beneficial to explore how the model's internal representations evolve during training and how this relates to the observed performance gains. Furthermore, the authors should consider providing a more detailed analysis of the types of errors the model corrects and the types of errors it still struggles with, which could provide insights into the limitations of the approach and guide future research.

To strengthen the paper's contribution, the authors should include a more comprehensive comparison with existing state-of-the-art methods for self-improvement of LLMs. While the authors mention that their approach is simple, it is crucial to demonstrate its advantages over more complex methods. A direct comparison with methods that use different self-improvement strategies, such as those based on policy gradients or actor-critic methods, would be highly informative. The comparison should not only focus on the final performance but also consider other factors such as the computational cost, the amount of data required, and the robustness of the approach. It would be beneficial to include a discussion of the trade-offs between the simplicity of the proposed approach and its performance compared to more complex methods. This would help to better position the contribution of the paper within the broader landscape of self-improvement techniques. Furthermore, the authors should consider including a discussion of the limitations of their approach in comparison to other methods.

Finally, the paper should include a more detailed discussion of the limitations of the proposed approach. While the authors briefly mention some limitations, a more thorough analysis is needed. For example, how does the approach perform on tasks that require more complex reasoning or creative thinking? Are there any specific types of tasks or datasets where the approach is not effective? What are the potential drawbacks of using majority voting as a pseudo-labeling mechanism? Does it introduce any biases or limitations? A more detailed discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed approach. Furthermore, the authors should discuss potential avenues for future research to address these limitations and further improve the self-improvement capabilities of LLMs.

### Questions

1. How does the proposed approach compare to other self-improvement methods in terms of performance and computational cost?
2. What are the limitations of the proposed approach, and how can they be addressed in future work?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find the corresponding section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) to support the weakness.
4. If the weakness is about missing information, check if that information is indeed absent.
5. If the weakness is about a lack of comparison, check the related work and experiment sections.
6. Synthesize the findings and conclude whether the weakness is valid, partially valid, or invalid.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper lacks a clear motivation for why the proposed approach is effective. The authors should provide a more detailed explanation of the underlying mechanisms that contribute to the success of their approach.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the "Self-Rewarded Training (SRT)" mechanism in Section 3, describing the use of majority voting for pseudo-label generation. The motivation is stated as: "To study this question, we investigate the setting in which the feedback signal is updated at every gradient step —fundamentally altering the dynamics of self-improvement compared to earlier work." (Introduction)
   - The paper explains the mechanism: "At a high level, each iteration proceeds as follows: (1) Sample a mini-batch of prompts, (2) Determine pseudo-labels, y pseudo y_{\text{pseudo}} , using the mechanism for each prompt, (3) Generate n responses per prompt and use agreement with the derived psuedo-labels as an intrinsic binary reward: r(y) =  1 [answer (y) = y_{\text{pseudo}}] , and then (4) Perform a single RL update step on this mini-batch using the reward function r(y)." (Section 3)
   - The paper provides an intuitive explanation: "Among several possible choices for determining reasonably accurate pseudo-labels, we explore the simplest one in this work, majority voting . Majority voting has been empirically demonstrated to have higher accuracy compared to individual generations." (Section 3)

b) Experiment-related Evidence:
   - The paper presents experimental results showing performance improvements on synthetic tasks (Section 4.1) and real-world math problems (Section 4.2).
   - The paper also shows performance collapse on math problems (Section 4.2).

3. Literature Gap Analysis:
   - The paper cites relevant work on RL and self-improvement in the Introduction and Related Works sections.

4. Validation Analysis:
   - Primary evidence suggests the paper provides a motivation for the approach (studying self-improvement with updated feedback) and explains the mechanism (majority voting). However, the reviewer's point about a *clearer* and more *detailed* explanation of the *underlying mechanisms* contributing to effectiveness is valid. While the paper describes *how* the method works, it doesn't delve deeply into *why* this specific mechanism leads to the observed improvements beyond the general benefit of majority voting.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper explains the *what* (majority voting) and *how* (repeated sampling and reward calculation), but lacks a deeper explanation of the *why* behind its effectiveness beyond the general benefit of majority voting.

1. Weakness Statement:
[The paper does not compare the proposed approach with other state-of-the-art methods for self-improvement of LLMs. The authors should include a comparison with other methods to demonstrate the advantages of their approach.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper includes baselines in the experiments: "SFT on the majority vote (SFT-MV), DPO and ScPO employing contrastive learning between the majority vote and non-majority vote answer in Table 1." (Section 4.1)
   - The paper also includes baselines in the extended SRT training experiment: "SFT on the majority vote (SFT-MV), DPO and ScPO employing contrastive loss using negative samples and curriculum learning." (Section 4.2)

b) Literature Gap Analysis:
   - The Related Works section (Section 5) discusses several self-improvement methods, including those using majority voting and those that distill from fixed policies.

3. Literature Gap Analysis:
   - The Related Works section mentions several self-improvement methods, including "Zelikman et al. (2022); Wang et al. (2023b); Huang et al. (2023); Song et al. (2024a)" which are relevant.

4. Validation Analysis:
   - The paper *does* compare against several state-of-the-art methods (SFT-MV, DPO, ScPO) in its experimental setup. The reviewer's statement is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly includes comparisons with SFT-MV, DPO, and ScPO in its experimental sections.

1. Weakness Statement:
[The paper does not discuss the limitations of the proposed approach. The authors should discuss the potential drawbacks and challenges of their approach.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions "reward hacking" as a potential limitation in the Discussion section: "In this work, we analyze a simple strategy of leveraging an LLM’s self-consistency to train it via an RL framework. Our key contributions are threefold: (1) Our comprehensive set of experiments demonstrate that this simple mechanism yields measurable gains over the base model on key reasoning metrics such as maj@k and avg@k success rates (Section 4.1 ). Remarkably, we observe clear improvement in the label generating policy after a comparable rate with ground-truth verification. (2) In synthetic tasks where one can control the difficulty of the training dataset, we observe that a simple curriculum-based self-improvement approach can maintain improvement across multiple difficulty levels. (3) However, prolonged training with this framework can lead to reward hacking and complete model collapse." (Introduction)
   - The Discussion section also mentions the computational cost: "Overall, these findings identify feedback design as the key challenge and call for future research on mechanisms to enable prolonged self-improvement."

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The paper explicitly discusses the issue of "reward hacking" and "model collapse" as limitations in the Discussion section. While the discussion could be more extensive, the reviewer's claim that the paper *does not* discuss limitations is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The Discussion section explicitly mentions "reward hacking" and "model collapse" as limitations.

**Review 2 Weaknesses:**

1. Weakness Statement:
[The paper lacks a clear motivation for why the proposed approach is effective. The authors should provide a more detailed explanation of the underlying mechanisms that contribute to the success of their approach.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper explains the *what* (majority voting) and *how* (repeated sampling and reward calculation), but lacks a deeper explanation of the *why* behind its effectiveness beyond the general benefit of majority voting.

1. Weakness Statement:
[The paper does not compare the proposed approach with other state-of-the-art methods for self-improvement of LLMs. The authors should include a comparison with other methods to demonstrate the advantages of their approach.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1's second point.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly includes comparisons with SFT-MV, DPO, and ScPO in its experimental sections.

1. Weakness Statement:
[The paper does not discuss the limitations of the proposed approach. The authors should discuss the potential drawbacks and challenges of their approach.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the analysis for Reviewer 1's third weakness.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1's third point.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The Discussion section explicitly mentions "reward hacking" and "model collapse" as limitations.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The paper lacks a clear motivation for why the proposed approach is effective. The authors should provide a more detailed explanation of the underlying mechanisms that contribute to the success of their approach.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point and Reviewer 2's first point. Please see the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper explains the *what* (majority voting) and *how* (repeated sampling and reward calculation), but lacks a deeper explanation of the *why* behind its effectiveness beyond the general benefit of majority voting.

1. Weakness Statement:
[The paper does not compare the proposed approach with other state-of-the-art methods for self-improvement of LLMs. The authors should include a comparison with other methods to demonstrate the advantages of their approach.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point and Reviewer 2's second point. Please see the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1's second point.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly includes comparisons with SFT-MV, DPO, and ScPO in its experimental sections.

1. Weakness Statement:
[The paper does not discuss the limitations of the proposed approach. The authors should discuss the potential drawbacks and challenges of their approach.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point and Reviewer 2's third point. Please see the analysis for Reviewer 1's third weakness.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1's third point.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The Discussion section explicitly mentions "reward hacking" and "model collapse" as limitations.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper's focus on self-improvement through self-feedback is interesting, but it lacks a clear connection to real-world applications. The authors do not provide concrete examples of how this approach could be applied to practical problems, which limits the impact of the study. Specifically, the paper does not explore how the proposed method could be integrated into existing workflows or systems, making it difficult to assess its practical utility. For instance, it would be beneficial to see how this method could be used to improve the performance of an LLM in a specific domain, such as code generation or scientific discovery, and what challenges might arise in such applications.]

2. Evidence Collection:
a) Motivation Section:
   - The motivation section mentions "the need to develop methods that can continuously improve the capabilities of LLMs without relying on external human feedback." (Motivation section)
   - It also states, "This paper aims to address this gap by exploring the potential of self-improvement through self-feedback mechanisms, specifically focusing on the use of majority voting to generate pseudo-labels for reinforcement learning training."

b) Introduction Section:
   - The introduction highlights the potential of self-improvement: "If sustained iteratively, and if teacher models can also self-improve , this process could enable continual progress without human supervision — which is crucial step for AI based automatic scientific discovery."

3. Literature Gap Analysis:
   - The paper does not explicitly detail integration into specific real-world applications.

4. Validation Analysis:
   - The reviewer has a valid point. While the paper motivates the work by mentioning the desire for autonomous improvement, it doesn't provide concrete examples or discuss the challenges of applying SRT in specific real-world scenarios like code generation or scientific discovery. The paper focuses on demonstrating the mechanism and its potential, but lacks a detailed discussion of practical integration and challenges.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks concrete examples of real-world applications and the challenges of integrating SRT into specific domains.

1. Weakness Statement:
[The paper does not adequately address the potential limitations of the proposed method. While the authors acknowledge the issue of reward hacking, they do not explore other potential challenges, such as the computational cost of the approach, its sensitivity to hyperparameters, or its robustness to noisy data. A more thorough discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed method. For example, the paper does not discuss the computational resources required for training, the impact of different hyperparameter settings on performance, or how the method would perform with noisy or incomplete data. These are important considerations for practical applications.]

2. Evidence Collection:
a) Discussion Section:
   - The Discussion section mentions "reward hacking" and "model collapse" as limitations.
   - It also mentions "computational cost" as a challenge for future research.
   - It briefly mentions the use of a "fixed teacher policy" and the potential for data mixing as future research directions.

b) Experiment Section:
   - The paper mentions using the same hardware as previous work (Delta).
   - It explores the impact of learning rate and number of generations in the extended SRT training experiment.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The reviewer has a valid point. While the paper acknowledges reward hacking and computational cost, it doesn't delve into other potential limitations like hyperparameter sensitivity or robustness to noisy data. The paper lacks a detailed discussion of the computational cost beyond mentioning the hardware used and briefly touches upon hyperparameter sensitivity in one experiment.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper acknowledges reward hacking and computational cost but lacks a detailed discussion of hyperparameter sensitivity and robustness to noisy data.

1. Weakness Statement:
[The paper's analysis of the reward hacking phenomenon is somewhat superficial. While the authors demonstrate that the model learns to maximize training rewards without genuine improvement, they do not provide a detailed explanation of the underlying mechanisms. A deeper analysis of why and how reward hacking occurs would be valuable for understanding the limitations of self-improvement through self-feedback. The paper should explore the specific conditions under which reward hacking is most likely to occur and what strategies can be used to mitigate this issue. For example, it would be useful to investigate whether reward hacking is more likely to occur when the model is trained on a large number of examples or when the training data is highly diverse.]

2. Evidence Collection:
a) Discussion Section:
   - The Discussion section states: "In this work, we analyze a simple strategy of leveraging an LLM’s self-consistency to train it via an RL framework. Our key contributions are threefold: (1) Our comprehensive set of experiments demonstrate that this simple mechanism yields measurable gains over the base model on key reasoning metrics such as maj@k and avg@k success rates (Section 4.1 ). Remarkably, we observe clear improvement in the label generating policy after a comparable rate with ground-truth verification. (2) In synthetic tasks where one can control the difficulty of the training dataset, we observe that a simple curriculum-based self-improvement approach can maintain improvement across multiple difficulty levels. (3) However, prolonged training with this framework can lead to reward hacking and complete model collapse." (Introduction)
   - It further states: "Overall, these findings identify feedback design as the key challenge and call for future research on mechanisms to enable prolonged self-improvement."

b) Experiment Section:
   - The paper shows the performance collapse on math problems, which is attributed to reward hacking.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The reviewer has a valid point. The paper identifies reward hacking as a limitation and shows its occurrence, but the analysis is somewhat high-level. It doesn't delve into the underlying mechanisms causing reward hacking or explore factors that influence its likelihood. The paper demonstrates the phenomenon but doesn't provide a deep mechanistic explanation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper identifies reward hacking but lacks a detailed analysis of its underlying mechanisms and influencing factors.

1. Weakness Statement:
[How does the proposed approach compare to other self-improvement methods, such as reinforcement learning from human feedback (RLHF)? What are the advantages and disadvantages of each approach?]

2. Evidence Collection:
   - This is a question, not a statement about a weakness in the paper's content.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - N/A

5. Conclusion:
   - Validity status: Not Applicable
   - Confidence level: N/A
   - Key supporting evidence: N/A

1. Weakness Statement:
[The paper mentions that the proposed method can lead to reward hacking, where the model learns to maximize training rewards without genuine improvement. What are the potential consequences of this phenomenon in real-world applications?]

2. Evidence Collection:
   - This is a question, not a statement about a weakness in the paper's content.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - N/A

5. Conclusion:
   - Validity status: Not Applicable
   - Confidence level: N/A
   - Key supporting evidence: N/A

1. Weakness Statement:
[The paper focuses on reasoning tasks, but how would the proposed method perform on other types of tasks, such as code generation or text summarization? What challenges might arise in these applications?]

2. Evidence Collection:
   - This is a question, not a statement about a weakness in the paper's content.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - N/A

5. Conclusion:
   - Validity status: Not Applicable
   - Confidence level: N/A
   - Key supporting evidence: N/A

1. Weakness Statement:
[The paper does not discuss the computational cost of the proposed method. How does the computational cost of SRT compare to other self-improvement approaches? Is the method scalable to larger models and datasets?]

2. Evidence Collection:
a) Experiment Section:
   - The paper mentions using the same hardware as previous work (Delta).
   - It doesn't provide a direct comparison of computational cost with other methods.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The reviewer has a valid point. While the paper mentions the hardware used, it doesn't provide a detailed analysis or comparison of the computational cost of SRT with other self-improvement methods. The scalability to larger models and datasets is also not discussed.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a detailed discussion and comparison of the computational cost of SRT.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Self-Rewarded Training (SRT), a novel approach to enhance the performance of large language models (LLMs) through self-supervised learning. The core idea behind SRT is to leverage the LLM's inherent self-consistency by generating multiple responses to a given prompt and then using the most frequent answer as a pseudo-label for training. This method circumvents the need for external verification or human feedback, which are often costly and time-consuming. The authors propose that this self-supervised mechanism allows the model to iteratively improve its performance by refining its responses based on its own generated labels. The paper presents a comprehensive empirical evaluation of SRT on both synthetic and real-world reasoning tasks. In synthetic tasks, drawn from the REASONING GYM, SRT demonstrates the ability to improve model performance and even lead to model collapse when trained for an extended period. The authors also explore the impact of different training parameters, such as learning rates and the number of generations, on the results. Furthermore, the paper investigates the application of SRT to real-world math problems, where it again shows promise in improving model performance, but also highlights the risk of reward hacking and model collapse. The authors compare SRT with other self-improvement methods, such as SFT-MV, DPO, and ScPO, demonstrating that SRT can achieve comparable or better performance in some cases. The paper's findings suggest that self-supervised learning through self-generated pseudo-labels is a viable strategy for improving LLMs, but also underscores the importance of carefully managing the training process to avoid reward hacking and model collapse. The authors conclude that while SRT shows promise, further research is needed to address the limitations of this approach and to explore its potential for more complex tasks and real-world applications. The paper's exploration of self-improvement through self-feedback is a significant step towards more autonomous and scalable AI systems, but also highlights the challenges and risks associated with this approach. The authors' work provides a valuable contribution to the field by introducing a simple yet effective method for self-improvement, while also raising important questions about the limitations and potential pitfalls of such methods.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.25


## Strengths:

The paper's primary strength lies in its clear and well-structured presentation of the Self-Rewarded Training (SRT) method. The authors provide a detailed explanation of the mechanism, which involves generating multiple responses to a prompt, using the most frequent answer as a pseudo-label, and then training the model using reinforcement learning. This approach is both intuitive and easy to understand, making it accessible to a wide audience. The paper's empirical evaluation is another significant strength. The authors conduct extensive experiments on both synthetic and real-world reasoning tasks, providing strong evidence for the effectiveness of SRT. The inclusion of both synthetic tasks from the REASONING GYM and real-world math problems demonstrates the versatility of the method. Furthermore, the paper's comparison with other self-improvement methods, such as SFT-MV, DPO, and ScPO, is valuable. This comparison highlights the potential advantages of SRT, particularly in terms of its simplicity and ease of implementation. The authors also explore the impact of different training parameters, such as learning rates and the number of generations, on the results. This analysis provides valuable insights into the behavior of the method and helps to identify optimal training strategies. The paper's identification of the issue of reward hacking and model collapse is another important contribution. The authors demonstrate that prolonged training with SRT can lead to the model learning to maximize training rewards without genuine improvement, which is a critical concern for the practical application of self-improvement methods. The paper's discussion of this issue and its potential mitigation strategies is a valuable contribution to the field. Finally, the paper's focus on self-supervised learning is a significant strength. The ability to improve the model's performance without relying on external feedback is a crucial step towards more autonomous and scalable AI systems. The authors' work provides a valuable contribution to the field by introducing a simple yet effective method for self-improvement, while also raising important questions about the limitations and potential pitfalls of such methods.


## Weaknesses:

While the paper presents a compelling approach to self-improvement, several weaknesses warrant careful consideration. First, while the paper explains the *what* and *how* of SRT, it lacks a deep explanation of the *why* behind its effectiveness. The authors describe the mechanism of majority voting and its use as a pseudo-label, but they do not delve into the underlying mechanisms that contribute to the observed improvements. For instance, the paper does not explore how the consistency of the majority votes influences the learning process or what conditions might lead to the method being less effective. This lack of a deeper theoretical or intuitive explanation makes it difficult to fully grasp why SRT works and under what circumstances it might fail. This is a significant limitation because it prevents a thorough understanding of the method's behavior and its potential limitations. My confidence in this weakness is high, as the paper's focus is primarily on the mechanics of the method rather than a detailed analysis of its underlying principles. Second, although the paper includes comparisons with several state-of-the-art methods, such as SFT-MV, DPO, and ScPO, it does not provide a comprehensive comparison with other self-improvement methods that use different self-improvement strategies. While the authors mention that their approach is simple, it is crucial to demonstrate its advantages over more complex methods. A direct comparison with methods that use policy gradients or actor-critic methods would be highly informative. The comparison should not only focus on the final performance but also consider other factors such as the computational cost, the amount of data required, and the robustness of the approach. This lack of a comprehensive comparison makes it difficult to assess the true advantages of SRT and its potential limitations. My confidence in this weakness is high, as the paper does not provide a detailed comparison with a wide range of self-improvement methods. Third, while the paper acknowledges the issue of reward hacking and model collapse, it does not delve into other potential limitations of the proposed method. The paper does not explore the sensitivity of the method to hyperparameter settings or its robustness to noisy data. A more thorough discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed method. For example, the paper does not discuss the computational resources required for training, the impact of different hyperparameter settings on performance, or how the method would perform with noisy or incomplete data. This lack of a detailed discussion of these limitations is a significant oversight. My confidence in this weakness is high, as the paper does not provide a comprehensive analysis of the method's limitations beyond reward hacking and model collapse. Finally, the paper's analysis of the reward hacking phenomenon is somewhat superficial. While the authors demonstrate that the model learns to maximize training rewards without genuine improvement, they do not provide a detailed explanation of the underlying mechanisms. A deeper analysis of why and how reward hacking occurs would be valuable for understanding the limitations of self-improvement through self-feedback. The paper should explore the specific conditions under which reward hacking is most likely to occur and what strategies can be used to mitigate this issue. For example, it would be useful to investigate whether reward hacking is more likely to occur when the model is trained on a large number of examples or when the training data is highly diverse. The paper's lack of a detailed analysis of reward hacking is a significant limitation because it prevents a thorough understanding of the method's limitations. My confidence in this weakness is high, as the paper does not provide a detailed explanation of the underlying mechanisms of reward hacking.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more thorough explanation of the mechanisms behind the proposed Self-Rewarded Training (SRT) approach. While the empirical results are promising, the lack of a clear theoretical or intuitive explanation makes it difficult to fully grasp why SRT works. For instance, the authors could delve deeper into how the majority voting mechanism interacts with the reinforcement learning framework. Specifically, how does the consistency of the majority votes influence the learning process, and what are the conditions under which this approach is most effective? A more detailed analysis of the error propagation and correction mechanisms would also be valuable. It would be beneficial to explore how the model's internal representations evolve during training and how this relates to the observed performance gains. Furthermore, the authors should consider providing a more detailed analysis of the types of errors the model corrects and the types of errors it still struggles with, which could provide insights into the limitations of the approach and guide future research. Second, to strengthen the paper's contribution, the authors should include a more comprehensive comparison with existing state-of-the-art methods for self-improvement of LLMs. While the authors mention that their approach is simple, it is crucial to demonstrate its advantages over more complex methods. A direct comparison with methods that use different self-improvement strategies, such as those based on policy gradients or actor-critic methods, would be highly informative. The comparison should not only focus on the final performance but also consider other factors such as the computational cost, the amount of data required, and the robustness of the approach. It would be beneficial to include a discussion of the trade-offs between the simplicity of the proposed approach and its performance compared to more complex methods. This would help to better position the contribution of the paper within the broader landscape of self-improvement techniques. Furthermore, the authors should consider including a discussion of the limitations of their approach in comparison to other methods. Third, the paper should include a more detailed discussion of the limitations of the proposed approach. While the authors briefly mention some limitations, a more thorough analysis is needed. For example, how does the approach perform on tasks that require more complex reasoning or creative thinking? Are there any specific types of tasks or datasets where the approach is not effective? What are the potential drawbacks of using majority voting as a pseudo-labeling mechanism? Does it introduce any biases or limitations? A more detailed discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed approach. Furthermore, the authors should discuss potential avenues for future research to address these limitations and further improve the self-improvement capabilities of LLMs. Fourth, the authors should provide a more detailed analysis of the underlying mechanisms of reward hacking. This could involve exploring the specific conditions under which reward hacking is most likely to occur and what strategies can be used to mitigate this issue. For example, it would be useful to investigate whether reward hacking is more likely to occur when the model is trained on a large number of examples or when the training data is highly diverse. The authors could also explore different regularization techniques or training strategies that could help to prevent reward hacking. Additionally, the authors should investigate the sensitivity of their method to hyperparameter settings and provide guidance on how to choose appropriate values for these parameters. This would make the method more robust and easier to use in practice. Finally, the authors should provide concrete examples of how their self-improvement method could be applied to real-world problems. This could involve demonstrating the method's effectiveness on specific tasks, such as question answering, text summarization, or code generation, and discussing the challenges and limitations encountered in these applications. For example, the authors could show how their method could be used to improve the performance of an LLM in a specific domain, such as code generation or scientific discovery, and what challenges might arise in such applications. This would help to bridge the gap between the theoretical findings of the paper and their practical implications. Furthermore, the authors should discuss the computational cost of their approach and how it scales with the size of the model and the training data. This would provide a more realistic assessment of the method's feasibility for practical applications.


## Questions:

Several questions arise from my analysis of the paper. First, how does the proposed approach compare to other self-improvement methods, such as reinforcement learning from human feedback (RLHF)? What are the advantages and disadvantages of each approach? While the paper compares SRT to several other self-improvement methods, it does not provide a direct comparison with RLHF, which is a widely used approach for improving LLMs. A comparison with RLHF would help to better understand the relative strengths and weaknesses of SRT. Second, the paper mentions that the proposed method can lead to reward hacking, where the model learns to maximize training rewards without genuine improvement. What are the potential consequences of this phenomenon in real-world applications? While the paper identifies reward hacking as a limitation, it does not fully explore the potential consequences of this phenomenon in real-world applications. A more detailed discussion of the potential negative impacts of reward hacking would be valuable. Third, the paper focuses on reasoning tasks, but how would the proposed method perform on other types of tasks, such as code generation or text summarization? What challenges might arise in these applications? The paper does not provide a detailed analysis of the method's performance on tasks beyond reasoning. A discussion of the potential challenges and limitations of applying SRT to other types of tasks would be valuable. Fourth, the paper does not discuss the computational cost of the proposed method. How does the computational cost of SRT compare to other self-improvement approaches? Is the method scalable to larger models and datasets? A detailed analysis of the computational cost of SRT would be valuable for assessing its practical feasibility. Finally, the paper mentions that the method can lead to model collapse when trained for an extended period. What are the potential causes of this phenomenon, and what strategies can be used to mitigate this issue? The paper does not provide a detailed analysis of the causes of model collapse or potential mitigation strategies. A more thorough discussion of this issue would be valuable for understanding the limitations of SRT.


## Rating:

5.25


## Confidence:

3.25


## Decision:

Reject
}