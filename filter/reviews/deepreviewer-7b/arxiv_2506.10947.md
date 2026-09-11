I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies the effect of spurious rewards on RL for reasoning tasks. They show that RL can improve performance on math reasoning tasks even with random rewards. They also show that this effect is model dependent.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well written and easy to follow. The experiments are clearly described and easy to understand.
- The observation that RL can improve reasoning performance even with random rewards is interesting and somewhat surprising.

### Weaknesses

#### Some Related Works


#### comment

 - The observation that RL can improve reasoning performance even with random rewards is interesting and somewhat surprising. However, the paper lacks a deeper analysis of why this happens and what it implies for the field. The paper does not explore the underlying mechanisms that enable RL to extract useful information from random rewards. It remains unclear whether the observed improvements are due to a specific interaction between the RL algorithm and the reward structure, or if it is a more general phenomenon. The paper should delve into the specific properties of the reasoning tasks and the model architecture that make them susceptible to this phenomenon.
- The paper does not provide a clear explanation of the role of the clipping term in GRPO. While the authors mention that the clipping term is crucial for the success of RL with random rewards, they do not provide a detailed analysis of why this is the case. The paper should include a more rigorous analysis of the clipping term, including its effect on the gradient and the convergence properties of the algorithm. It is not clear how the clipping term interacts with the random rewards and why it is necessary for the observed improvements.
- The paper does not provide a clear explanation of the role of the clipping term in GRPO. While the authors mention that the clipping term is crucial for the success of RL with random rewards, they do not provide a detailed analysis of why this is the case. The paper should include a more rigorous analysis of the clipping term, including its effect on the gradient and the convergence properties of the algorithm. It is not clear how the clipping term interacts with the random rewards and why it is necessary for the observed improvements.
- The paper does not provide a clear explanation of the role of the clipping term in GRPO. While the authors mention that the clipping term is crucial for the success of RL with random rewards, they do not provide a detailed analysis of why this is the case. The paper should include a more rigorous analysis of the clipping term, including its effect on the gradient and the convergence properties of the algorithm. It is not clear how the clipping term interacts with the random rewards and why it is necessary for the observed improvements.

### Suggestions

The paper should investigate the specific properties of the reasoning tasks that make them susceptible to the observed phenomenon. For example, are there specific types of reasoning steps or problem structures that are more easily learned from random rewards? The authors could analyze the intermediate representations of the model during RL training to understand how the model is learning from the random rewards. This could involve visualizing the activations of different layers or examining the changes in the model's internal state. Furthermore, the paper should explore the effect of different reward structures. Instead of using completely random rewards, the authors could try using rewards that are correlated with specific reasoning steps or problem features. This could provide insights into the mechanisms that enable RL to extract useful information from the rewards. The paper should also explore the effect of different RL algorithms. The authors should compare the performance of GRPO with other RL algorithms, such as PPO or DQN, to determine if the observed improvements are specific to GRPO or if they are a more general phenomenon. This would help to isolate the effect of the clipping term and the specific properties of GRPO.

The paper should provide a more detailed analysis of the clipping term in GRPO. The authors should investigate how the clipping term affects the gradient of the loss function and how it contributes to the convergence properties of the algorithm. This could involve analyzing the gradient updates under different clipping parameters and comparing the convergence behavior with and without clipping. The paper should also explore the effect of different clipping strategies. For example, the authors could try using adaptive clipping thresholds or different clipping functions. This could provide insights into the optimal way to use the clipping term for RL with random rewards. The paper should also investigate the interaction between the clipping term and the random rewards. The authors should analyze how the clipping term modifies the effect of the random rewards and why this modification is necessary for the observed improvements. This could involve comparing the performance of GRPO with and without clipping, using different types of random rewards, and analyzing the gradient updates under different conditions.

Finally, the paper should provide a more thorough discussion of the limitations of the study. The authors should acknowledge that the observed improvements with random rewards may not generalize to all reasoning tasks or all model architectures. The paper should also discuss the potential ethical implications of using RL with random rewards, especially in safety-critical applications. The authors should also consider the computational cost of RL training and whether the observed improvements justify the additional computational overhead. The paper should also discuss the potential for overfitting to the specific reasoning tasks used in the study and whether the observed improvements would hold for more complex or diverse tasks. The paper should also discuss the potential for the observed improvements to be due to overfitting to the specific model architecture used in the study and whether the observed improvements would hold for other architectures.

### Questions

- Why is the clipping term important for the success of RL with random rewards?
- How does the clipping term interact with the random rewards?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper studies the effectiveness of RL from a verifiable reward (RLVR) in improving language models’ reasoning capabilities. The authors show that even random rewards can improve the performance of Qwen2.5-Math-7B in math reasoning tasks. They also investigate the underlying mechanisms of this phenomenon and find that the clipping function in GRPO amplifies high-prior behaviors learned during pretraining, leading to improvements in reasoning tasks. The authors further analyze the reasoning traces of Qwen2.5-Math-7B and find that it often generates Python code in its reasoning process, which is strongly correlated with correctness. They also show that RL with spurious rewards can upweight pre-existing reasoning strategies, and that prompting or RL-based induction can match or exceed the gains achieved through RL with spurious rewards.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a thorough analysis of the effects of spurious rewards on RLVR, including the impact of different reward functions (weak, spurious, and random rewards), the role of the clipping function in GRPO, and the correlation between code reasoning and math reasoning performance.
- The paper is well-written and easy to follow, with clear explanations of the experimental setup and results.
- The paper provides valuable insights into the mechanisms of RLVR and the importance of considering pretraining biases when evaluating RL methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper only focuses on the Qwen2.5-Math-7B model, and the results may not generalize to other models. The authors should test their findings on a wider range of models to ensure the robustness of their conclusions.
- The paper does not provide a detailed analysis of the computational cost associated with RL training, which could be a limiting factor for practical applications.
- The paper does not explore the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps.

### Suggestions

The authors should conduct a more thorough investigation into the generalizability of their findings across different model architectures and sizes. Specifically, they should include models with varying numbers of parameters and different pretraining objectives. For example, testing on models like Llama 3, Mistral, or similar architectures would provide a more comprehensive understanding of whether the observed improvements with random rewards are specific to the Qwen2.5-Math-7B model or a more general phenomenon. Furthermore, it would be beneficial to explore the impact of different pretraining datasets and strategies on the effectiveness of RL with spurious rewards. This could involve comparing models trained on datasets with varying levels of mathematical reasoning complexity or those with different types of reasoning biases. Such an analysis would help to determine whether the observed gains are due to the model's inherent reasoning capabilities or the influence of the pretraining data.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the resources required for their RL training experiments. This should include the number of training steps, the GPU hours, the memory usage, and the overall training time. This information is crucial for practitioners who may want to replicate the results or apply similar techniques to their own models. Furthermore, the authors should explore the trade-offs between the computational cost and the performance gains achieved with spurious rewards. For instance, they could investigate whether there is a point of diminishing returns where increasing the training time or the number of samples does not lead to significant improvements in performance. This analysis would help to determine the practical feasibility of using RL with spurious rewards for large-scale models and datasets. It would also be useful to compare the computational cost of RL with spurious rewards to other methods for improving reasoning capabilities, such as fine-tuning or data augmentation.

Finally, the authors should delve deeper into the potential negative consequences of using spurious rewards. While the paper demonstrates that RL with spurious rewards can improve performance, it does not explore the potential for overfitting to the reward function or generating incorrect reasoning steps. The authors should investigate whether the model is learning to exploit the spurious correlations in the reward function rather than developing a robust understanding of the underlying reasoning process. This could involve analyzing the model's behavior on out-of-distribution examples or testing its ability to generalize to new reasoning tasks. Furthermore, the authors should explore techniques for mitigating the negative consequences of spurious rewards, such as using regularization methods or incorporating human feedback into the training process. This would help to ensure that RL with spurious rewards is used responsibly and does not lead to unintended negative consequences.

### Questions

- How do the results generalize to other models, such as Llama 3, Mistral, or similar architectures?
- What is the computational cost associated with RL training, and how does it scale with model size and dataset size?
- What are the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the impact of various reward functions on the performance of RL for reasoning tasks. The authors find that even random rewards can improve the performance of Qwen2.5-Math-7B in math reasoning tasks, and that this effect is model-dependent. They also analyze the underlying mechanisms of this phenomenon and find that the clipping function in GRPO amplifies high-prior behaviors learned during pretraining, leading to improvements in reasoning tasks. The authors further analyze the reasoning traces of Qwen2.5-Math-7B and find that it often generates Python code in its reasoning process, which is strongly correlated with correctness. They also show that RL with spurious rewards can upweight pre-existing reasoning strategies, and that prompting or RL-based induction can match or exceed the gains achieved through RL with spurious rewards.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The paper provides a thorough analysis of the effects of spurious rewards on RLVR, including the impact of different reward functions (weak, spurious, and random rewards), the role of the clipping function in GRPO, and the correlation between code reasoning and math reasoning performance.
- The paper provides valuable insights into the mechanisms of RLVR and the importance of considering pretraining biases when evaluating RL methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper only focuses on the Qwen2.5-Math-7B model, and the results may not generalize to other models. The authors should test their findings on a wider range of models to ensure the robustness of their conclusions.
- The paper does not provide a detailed analysis of the computational cost associated with RL training, which could be a limiting factor for practical applications.
- The paper does not explore the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps.

### Suggestions

The authors should expand their experimental scope to include a more diverse set of models, particularly those with different architectures and pretraining objectives. This would help to determine whether the observed improvements with random rewards are specific to the Qwen2.5-Math-7B model or a more general phenomenon. For example, testing on models like Llama 3, Mistral, or similar architectures would provide a more comprehensive understanding of the generalizability of their findings. Furthermore, it would be beneficial to investigate the impact of different pretraining datasets and strategies on the effectiveness of RL with spurious rewards. This could involve comparing models trained on datasets with varying levels of mathematical reasoning complexity or those with different types of reasoning biases. Such an analysis would help to determine whether the observed gains are due to the model's inherent reasoning capabilities or the influence of the pretraining data.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the resources required for their RL training experiments. This should include the number of training steps, the GPU hours, the memory usage, and the overall training time. This information is crucial for practitioners who may want to replicate the results or apply similar techniques to their own models. Furthermore, the authors should explore the trade-offs between the computational cost and the performance gains achieved with spurious rewards. For instance, they could investigate whether there is a point of diminishing returns where increasing the training time or the number of samples does not lead to significant improvements in performance. This analysis would help to determine the practical feasibility of using RL with spurious rewards for large-scale models and datasets. It would also be useful to compare the computational cost of RL with spurious rewards to other methods for improving reasoning capabilities, such as fine-tuning or data augmentation.

Finally, the authors should delve deeper into the potential negative consequences of using spurious rewards. While the paper demonstrates that RL with spurious rewards can improve performance, it does not explore the potential for overfitting to the reward function or generating incorrect reasoning steps. The authors should investigate whether the model is learning to exploit the spurious correlations in the reward function rather than developing a robust understanding of the underlying reasoning process. This could involve analyzing the model's behavior on out-of-distribution examples or testing its ability to generalize to new reasoning tasks. Furthermore, the authors should explore techniques for mitigating the negative consequences of spurious rewards, such as using regularization methods or incorporating human feedback into the training process. This would help to ensure that RL with spurious rewards is used responsibly and does not lead to unintended negative consequences.

### Questions

- How do the results generalize to other models, such as Llama 3, Mistral, or similar architectures?
- What is the computational cost associated with RL training, and how does it scale with model size and dataset size?
- What are the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper investigates the effectiveness of reinforcement learning with verifiable rewards (RLVR) in enhancing language models' reasoning abilities. The authors challenge the prevailing assumption that RLVR requires high-quality, task-specific rewards and demonstrate that even random or spurious rewards can improve model performance. They analyze the impact of various reward functions, including majority vote rewards, format rewards, and random rewards, on the reasoning capabilities of Qwen2.5-Math-7B. The study reveals that the clipping function in GRPO amplifies high-prior behaviors learned during pretraining, leading to performance gains. The authors also show that code reasoning, a distinct pre-existing capability of the Qwen2.5-Math-7B model, is strongly correlated with reasoning accuracy. They propose a case study on code reasoning as a representative pre-existing behavior and examine how RLVR can upweight these behaviors. The findings highlight the importance of considering pretraining biases when evaluating RL methods and suggest that RLVR, at least with random rewards, may not be a reliable method for developing new reasoning capabilities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a thorough analysis of the effects of spurious rewards on RLVR, including the impact of different reward functions (weak, spurious, and random rewards), the role of the clipping function in GRPO, and the correlation between code reasoning and math reasoning performance.
- The paper is well-written and easy to follow, with clear explanations of the experimental setup and results.
- The paper provides valuable insights into the mechanisms of RLVR and the importance of considering pretraining biases when evaluating RL methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper only focuses on the Qwen2.5-Math-7B model, and the results may not generalize to other models. The authors should test their findings on a wider range of models to ensure the robustness of their conclusions.
- The paper does not provide a detailed analysis of the computational cost associated with RL training, which could be a limiting factor for practical applications.
- The paper does not explore the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps.

### Suggestions

The authors should expand their experimental scope to include a more diverse set of models, particularly those with different architectures and pretraining objectives. This would help to determine whether the observed improvements with random rewards are specific to the Qwen2.5-Math-7B model or a more general phenomenon. For example, testing on models like Llama 3, Mistral, or similar architectures would provide a more comprehensive understanding of the generalizability of their findings. Furthermore, it would be beneficial to investigate the impact of different pretraining datasets and strategies on the effectiveness of RL with spurious rewards. This could involve comparing models trained on datasets with varying levels of mathematical reasoning complexity or those with different types of reasoning biases. Such an analysis would help to determine whether the observed gains are due to the model's inherent reasoning capabilities or the influence of the pretraining data.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the resources required for their RL training experiments. This should include the number of training steps, the GPU hours, the memory usage, and the overall training time. This information is crucial for practitioners who may want to replicate the results or apply similar techniques to their own models. Furthermore, the authors should explore the trade-offs between the computational cost and the performance gains achieved with spurious rewards. For instance, they could investigate whether there is a point of diminishing returns where increasing the training time or the number of samples does not lead to significant improvements in performance. This analysis would help to determine the practical feasibility of using RL with spurious rewards for large-scale models and datasets. It would also be useful to compare the computational cost of RL with spurious rewards to other methods for improving reasoning capabilities, such as fine-tuning or data augmentation.

Finally, the authors should delve deeper into the potential negative consequences of using spurious rewards. While the paper demonstrates that RL with spurious rewards can improve performance, it does not explore the potential for overfitting to the reward function or generating incorrect reasoning steps. The authors should investigate whether the model is learning to exploit the spurious correlations in the reward function rather than developing a robust understanding of the underlying reasoning process. This could involve analyzing the model's behavior on out-of-distribution examples or testing its ability to generalize to new reasoning tasks. Furthermore, the authors should explore techniques for mitigating the negative consequences of spurious rewards, such as using regularization methods or incorporating human feedback into the training process. This would help to ensure that RL with spurious rewards is used responsibly and does not lead to unintended negative consequences.

### Questions

- How do the results generalize to other models, such as Llama 3, Mistral, or similar architectures?
- What is the computational cost associated with RL training, and how does it scale with model size and dataset size?
- What are the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find supporting evidence from the paper.
3. Categorize the evidence as method-related or experiment-related.
4. If the weakness is about missing information, explicitly state what is missing.
5. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper only focuses on the Qwen2.5-Math-7B model, and the results may not generalize to other models. The authors should test their findings on a wider range of models to ensure the robustness of their conclusions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "EXPERIMENTS" section explicitly states: "We train on deepScaleR data ( Luo et al., 2025 ) with our rewards; all other experimental details are kept constant." This implies a consistent experimental setup across all reward types for the Qwen2.5-Math-7B model.
   - The "EXPERIMENTS" section also mentions: "We evaluate performance as pass@1 and average@8 accuracy on two standard math reasoning benchmarks: MATH-500 ( Hendrycks et al., 2021 ) and AMC ( Li et al., 2024 ) , respectively. See Appendix D for additional results on AIME 2024 and AIME 2025." This confirms the use of MATH-500 and AMC for evaluation.
   - The "INTRODUCTION" states: "We show that reinforcement learning with verifiable rewards (RLVR) can yield substantial performance improvements on math reasoning even under a family of spurious rewards that carry little, no, or outright task-relevant signal and that this effect depends critically on the base model." This framing suggests a focus on the Qwen2.5-Math-7B model.
   - The "CONCLUSION" states: "Our findings not only open new questions but also have practical implications. We should generally be more aware that reasoning patterns instilled during pretraining heavily impact the behavior of downstream RLVR training. Qwen models, with open weights and high performance on reasoning tasks, have become the de facto choice for RLVR research in the open-source community—a range of recent methods on RLVR for reasoning draw their conclusions primarily or exclusively from gains shown on Qwen models ( Lambert et al., 2024 ) . However, we show that it is easy to get significant performance improvements on Qwen models even with completely spurious reward signals. Our results highlight the importance of (1) testing across multiple models with differing pretraining distributions, and (2) testing across multiple different baselines, such as format and random rewards, when evaluating reinforcement learning techniques." This explicitly acknowledges the focus on Qwen models and the need for generalization.

3. Literature Gap Analysis:
   - The paper does not cite specific works that demonstrate the generalizability of RLVR with spurious rewards across different model architectures.

4. Validation Analysis:
   - The paper's experimental setup and conclusions are heavily centered around the Qwen2.5-Math-7B model. The authors themselves acknowledge the need to test across multiple models with differing pretraining distributions to ensure the robustness of their findings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states its focus on the Qwen2.5-Math-7B model and acknowledges the need for generalization to other models.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost associated with RL training, which could be a limiting factor for practical applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "EXPERIMENTS" section describes the setup but does not include any information about the computational resources used (e.g., GPU hours, training time).
   - There is no mention of the number of training steps or the scale of the RL training process.

3. Literature Gap Analysis:
   - While the paper cites the GRPO algorithm ( Guo et al., 2023 ), it does not discuss the typical computational costs associated with implementing and training RL agents using this or similar algorithms.

4. Validation Analysis:
   - The paper lacks any discussion or data regarding the computational resources required for the RL training experiments. This is a standard piece of information for evaluating the practicality of a method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "EXPERIMENTS" section lacks any details about computational costs or resources.

1. Weakness Statement:
"The paper does not explore the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper primarily focuses on the positive outcomes of using spurious rewards, demonstrating performance improvements on math reasoning tasks.
   - The "INTRODUCTION" mentions the possibility of spurious rewards leading to "non-robust solutions."
   - The "DISCUSSION" section acknowledges the importance of validating RL methods across diverse models and reward types but does not explicitly discuss the potential for negative consequences like overfitting or incorrect reasoning steps.
   - The "CONCLUSION" reiterates the importance of testing across multiple models but does not delve into the potential downsides of spurious rewards.

3. Literature Gap Analysis:
   - While the paper cites works on RLVR, it doesn't specifically engage with literature discussing the potential pitfalls of using spurious rewards, such as those focusing on overfitting or negative transfer.

4. Validation Analysis:
   - The paper's focus is on demonstrating the effectiveness of spurious rewards. While it acknowledges the possibility of non-robust solutions, it doesn't provide a detailed analysis or empirical evidence of negative consequences like overfitting or generating incorrect reasoning steps.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's emphasis is on positive results, and there's a lack of specific experiments or discussion on negative consequences.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The observation that RL can improve reasoning performance even with random rewards is interesting and somewhat surprising. However, the paper lacks a deeper analysis of why this happens and what it implies for the field. The paper does not explore the underlying mechanisms that enable RL to extract useful information from random rewards. It remains unclear whether the observed improvements are due to a specific interaction between the RL algorithm and the reward structure, or if it is a more general phenomenon. The paper should delve into the specific properties of the reasoning tasks and the model architecture that make them susceptible to this phenomenon."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the GRPO algorithm in the "2 SPURIOUS REWARDS YIELD SIGNIFICANT RLVR GAINS" section and explains the clipping term's role in mitigating exploration.
   - The paper states: "No training signal from random rewards, even though the reward is not a task-relevant signal, still produce a 21.4% performance boost. We observe similar trends in AMC, where training on format, incorrect, or random rewards yields a gain of 13.8 % 13.8\% , 24.1 % 24.1\% , or 21.4 % 21.4\% , respectively, approaching the ∼ 27 % – 29 % improvement gained from training on majority voted and ground truth labels." This highlights the empirical finding.
   - The paper analyzes the impact of the clipping term in GRPO in the "4 UNDERSTANDING TRAINING SIGNALS FROM RANDOM REWARDS IN GRPO" section, concluding: "We analyze the effect of clipping in GRPO under random rewards, with the full derivation provided in Appendix B. At a high level, clipping introduces a bias in the gradient update that depends on how the current policy’s token probabilities deviate from those of the behavior policy. Factoring out reward-independent scalar terms, the expected gradient induced by random rewards can be written (up to a positive constant) as 𝔼[∇θJ̃] ∝ 𝔼[x, y] [∇θ log πθ,x(y), 1 − ϵc, 0, |Rθ < 1 − ϵc, 1 + ϵc] A.2 2 2 We illustrate this effect with the following example: In Appendix B, we show that this effect persists across different random reward distributions, indicating its stability. Our findings echo the intuition of Yu et al. (2025) , who show that clipping bias reduces exploration and increases exploitation in RLVR with ground-truth labels."
b) Experiment-related Evidence:
   - The paper presents performance improvements on MATH-500 and AMC benchmarks with random rewards.
   - The "5 CASE STUDY: CODE REASONING AS A REPRESENTATIVE PRE-EXISTING BEHAVIOR" section analyzes the prevalence of code reasoning with random rewards and its correlation with accuracy.

3. Literature Gap Analysis:
   - The paper cites Yu et al. (2025) regarding the effect of clipping bias, suggesting some engagement with the underlying mechanisms.

4. Validation Analysis:
   - While the paper demonstrates the phenomenon and analyzes the clipping term, it doesn't deeply explore the specific properties of the reasoning tasks or model architecture that make them susceptible. The analysis of clipping is focused on its effect on the gradient, but a more in-depth investigation into the interplay between the reward structure and the model's pre-existing capabilities is missing.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper shows the phenomenon and analyzes clipping, but lacks a deeper dive into the task and model properties.

1. Weakness Statement:
"The paper does not provide a clear explanation of the role of the clipping term in GRPO. While the authors mention that the clipping term is crucial for the success of RL with random rewards, they do not provide a detailed analysis of why this is the case. The paper should include a more rigorous analysis of the clipping term, including its effect on the gradient and the convergence properties of the algorithm. It is not clear how the clipping term interacts with the random rewards and why it is necessary for the observed improvements."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the GRPO algorithm and the clipping term in the "2 SPURIOUS REWARDS YIELD SIGNIFICANT RLVR GAINS" section.
   - The paper states: "To demonstrate this, we consider three separate no-clipping variants of GRPO: disabling clipping in the implementation, increasing the mini-batch size to match the rollout size, or reducing the rollout size so that only a single gradient update is performed per rollout. 3 3 3 The latter two variants enforce πθ = πold ∇θJ̃ ≡ zero, yielding no meaningful learning signal. We analyze the effect of clipping in GRPO under random rewards, with the full derivation provided in Appendix B. At a high level, clipping introduces a bias in the gradient update that depends on how the current policy’s token probabilities deviate from those of the behavior policy."
b) Experiment-related Evidence:
   - The "4 UNDERSTANDING TRAINING SIGNALS FROM RANDOM REWARDS IN GRPO" section presents Figure 4, which shows the performance of GRPO with and without clipping.

3. Literature Gap Analysis:
   - The paper cites Yu et al. (2025), which also discusses clipping bias in RLVR.

4. Validation Analysis:
   - The paper explains that the clipping term introduces a bias in the gradient update, preventing excessive exploration. However, it doesn't provide a rigorous mathematical analysis of the clipping term's effect on the convergence properties of GRPO with random rewards. The explanation is more conceptual than deeply analytical.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper explains the effect of clipping but lacks a rigorous mathematical analysis of its impact on convergence.

1. Weakness Statement:
"The paper does not provide a clear explanation of the role of the clipping term in GRPO. While the authors mention that the clipping term is crucial for the success of RL with random rewards, they do not provide a detailed analysis of why this is the case. The paper should include a more rigorous analysis of the clipping term, including its effect on the gradient and the convergence properties of the algorithm. It is not clear how the clipping term interacts with the random rewards and why it is necessary for the observed improvements."

2. Evidence Collection:
   - This is a repetition of the previous weakness.

3. Literature Gap Analysis:
   - Same as above.

4. Validation Analysis:
   - Same as above.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Same as above.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper only focuses on the Qwen2.5-Math-7B model, and the results may not generalize to other models. The authors should test their findings on a wider range of models to ensure the robustness of their conclusions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "EXPERIMENTS" section explicitly states: "We train on deepScaleR data ( Luo et al., 2025 ) with our rewards; all other experimental details are kept constant."
   - The "EXPERIMENTS" section also mentions: "We evaluate performance as pass@1 and average@8 accuracy on two standard math reasoning benchmarks: MATH-500 ( Hendrycks et al., 2021 ) and AMC ( Li et al., 2024 ) , respectively. See Appendix D for additional results on AIME 2024 and AIME 2025." This confirms the use of MATH-500 and AMC for evaluation.
   - The "INTRODUCTION" states: "We show that reinforcement learning with verifiable rewards (RLVR) can yield substantial performance improvements on math reasoning even under a family of spurious rewards that carry little, no, or outright task-relevant signal and that this effect depends critically on the base model." This framing suggests a focus on the Qwen2.5-Math-7B model.
   - The "CONCLUSION" states: "Our findings not only open new questions but also have practical implications. We should generally be more aware that reasoning patterns instilled during pretraining heavily impact the behavior of downstream RLVR training. Qwen models, with open weights and high performance on reasoning tasks, have become the de facto choice for RLVR research in the open-source community—a range of recent methods on RLVR for reasoning draw their conclusions primarily or exclusively from gains shown on Qwen models ( Lambert et al., 2024 ) . However, we show that it is easy to get significant performance improvements on Qwen models even with completely spurious reward signals. Our results highlight the importance of (1) testing across multiple models with differing pretraining distributions, and (2) testing across multiple different baselines, such as format and random rewards, when evaluating reinforcement learning techniques." This explicitly acknowledges the focus on Qwen models and the need for generalization.

3. Literature Gap Analysis:
   - The paper does not cite specific works that demonstrate the generalizability of RLVR with spurious rewards across different model architectures.

4. Validation Analysis:
   - The paper's experimental setup and conclusions are heavily centered around the Qwen2.5-Math-7B model. The authors themselves acknowledge the need to test across multiple models with differing pretraining distributions to ensure the robustness of their findings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states its focus on the Qwen2.5-Math-7B model and acknowledges the need for generalization.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost associated with RL training, which could be a limiting factor for practical applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "EXPERIMENTS" section describes the setup but does not include any information about the computational resources used (e.g., GPU hours, training time).
   - There is no mention of the number of training steps or the scale of the RL training process.

3. Literature Gap Analysis:
   - While the paper cites the GRPO algorithm ( Guo et al., 2023 ), it does not discuss the typical computational costs associated with implementing and training RL agents using this or similar algorithms.

4. Validation Analysis:
   - The paper lacks any discussion or data regarding the computational resources required for the RL training experiments. This is a standard piece of information for evaluating the practicality of a method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "EXPERIMENTS" section lacks any details about computational costs or resources.

1. Weakness Statement:
"The paper does not explore the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper primarily focuses on the positive outcomes of using spurious rewards, demonstrating performance improvements on math reasoning tasks.
   - The "INTRODUCTION" mentions the possibility of spurious rewards leading to "non-robust solutions."
   - The "DISCUSSION" section acknowledges the importance of validating RL methods across diverse models and reward types but does not explicitly discuss the potential downsides of spurious rewards.
   - The "CONCLUSION" reiterates the importance of testing across multiple models but does not delve into the potential negative consequences of spurious rewards.

3. Literature Gap Analysis:
   - While the paper cites works on RLVR, it doesn't specifically engage with literature discussing the potential pitfalls of using spurious rewards, such as those focusing on overfitting or negative transfer.

4. Validation Analysis:
   - The paper's focus is on demonstrating the effectiveness of spurious rewards. While it acknowledges the possibility of non-robust solutions, it doesn't provide a detailed analysis or empirical evidence of negative consequences like overfitting or generating incorrect reasoning steps.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's emphasis is on positive results, and there's a lack of specific experiments or discussion on negative consequences.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper only focuses on the Qwen2.5-Math-7B model, and the results may not generalize to other models. The authors should test their findings on a wider range of models to ensure the robustness of their conclusions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "EXPERIMENTS" section explicitly states: "We train on deepScaleR data ( Luo et al., 2025 ) with our rewards; all other experimental details are kept constant."
   - The "EXPERIMENTS" section also mentions: "We evaluate performance as pass@1 and average@8 accuracy on two standard math reasoning benchmarks: MATH-500 ( Hendrycks et al., 2021 ) and AMC ( Li et al., 2024 ) , respectively. See Appendix D for additional results on AIME 2024 and AIME 2025." This confirms the use of MATH-500 and AMC for evaluation.
   - The "INTRODUCTION" states: "We show that reinforcement learning with verifiable rewards (RLVR) can yield substantial performance improvements on math reasoning even under a family of spurious rewards that carry little, no, or outright task-relevant signal and that this effect depends critically on the base model." This framing suggests a focus on the Qwen2.5-Math-7B model.
   - The "CONCLUSION" states: "Our findings not only open new questions but also have practical implications. We should generally be more aware that reasoning patterns instilled during pretraining heavily impact the behavior of downstream RLVR training. Qwen models, with open weights and high performance on reasoning tasks, have become the de facto choice for RLVR research in the open-source community—a range of recent methods on RLVR for reasoning draw their conclusions primarily or exclusively from gains shown on Qwen models ( Lambert et al., 2024 ) . However, we show that it is easy to get significant performance improvements on Qwen models even with completely spurious reward signals. Our results highlight the importance of (1) testing across multiple models with differing pretraining distributions, and (2) testing across multiple different baselines, such as format and random rewards, when evaluating reinforcement learning techniques." This explicitly acknowledges the focus on Qwen models and the need for generalization.

3. Literature Gap Analysis:
   - The paper does not cite specific works that demonstrate the generalizability of RLVR with spurious rewards across different model architectures.

4. Validation Analysis:
   - The paper's experimental setup and conclusions are heavily centered around the Qwen2.5-Math-7B model. The authors themselves acknowledge the need to test across multiple models with differing pretraining distributions to ensure the robustness of their findings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states its focus on the Qwen2.5-Math-7B model and acknowledges the need for generalization.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost associated with RL training, which could be a limiting factor for practical applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "EXPERIMENTS" section describes the setup but does not include any information about the computational resources used (e.g., GPU hours, training time).
   - There is no mention of the number of training steps or the scale of the RL training process.

3. Literature Gap Analysis:
   - While the paper cites the GRPO algorithm ( Guo et al., 2023 ), it does not discuss the typical computational costs associated with implementing and training RL agents using this or similar algorithms.

4. Validation Analysis:
   - The paper lacks any discussion or data regarding the computational resources required for the RL training experiments. This is a standard piece of information for evaluating the practicality of a method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "EXPERIMENTS" section lacks any details about computational costs or resources.

1. Weakness Statement:
"The paper does not explore the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper primarily focuses on the positive outcomes of using spurious rewards, demonstrating performance improvements on math reasoning tasks.
   - The "INTRODUCTION" mentions the possibility of spurious rewards leading to "non-robust solutions."
   - The "DISCUSSION" section acknowledges the importance of validating RL methods across diverse models and reward types but does not explicitly discuss the potential downsides of spurious rewards.
   - The "CONCLUSION" reiterates the importance of testing across multiple models but does not delve into the potential negative consequences of spurious rewards.

3. Literature Gap Analysis:
   - While the paper cites works on RLVR, it doesn't specifically engage with literature discussing the potential pitfalls of using spurious rewards, such as those focusing on overfitting or negative transfer.

4. Validation Analysis:
   - The paper's focus is on demonstrating the effectiveness of spurious rewards. While it acknowledges the possibility of non-robust solutions, it doesn't provide a detailed analysis or empirical evidence of negative consequences like overfitting or generating incorrect reasoning steps.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's emphasis is on positive results, and there's a lack of specific experiments or discussion on negative consequences.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a compelling investigation into the efficacy of reinforcement learning with verifiable rewards (RLVR) for enhancing reasoning capabilities in language models, particularly when using random or spurious rewards. The authors challenge the conventional assumption that RLVR requires high-quality, task-relevant rewards, demonstrating that even random or semantically meaningless rewards can significantly improve model performance on math reasoning tasks. The study primarily focuses on the Qwen2.5-Math-7B model, showing that it can improve performance on math reasoning tasks even with random rewards in math reasoning-7B or Qwen2.5-7B-SFT. The authors also analyze the underlying mechanisms of this phenomenon, finding that the clipping function in GRPO amplifies high-prior behaviors learned during pretraining, leading to performance gains. Furthermore, the paper highlights a strong correlation between code reasoning and math reasoning performance in the Qwen2.5-Math-7B model, and shows that RL with spurious rewards can upweight pre-existing reasoning strategies. The authors conduct a case study on code reasoning as a representative pre-existing behavior, examining how RL with spurious rewards can upweight these behaviors. They also show that prompting or RL-based induction can match or exceed the gains achieved through RL with spurious rewards. The paper's core contribution lies in its empirical demonstration that even random rewards can improve reasoning performance through RL, and that this effect is model-dependent. This finding has significant implications for the evaluation and design of RL methods, suggesting that current benchmarks may not be sufficient to assess RL methods' true capabilities. The authors also emphasize the importance of considering pretraining biases when evaluating RL methods, and advocate for testing across multiple models with differing pretraining distributions. Overall, this work provides valuable insights into the mechanisms of RLVR and the role of pretraining biases, while also highlighting the need for more robust evaluation methodologies.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

This paper makes several notable contributions to the field of reinforcement learning for language models. First, the authors provide a thorough analysis of the effects of spurious rewards on RLVR, including the impact of different reward functions (weak, spurious, and random rewards), the role of the clipping function in GRPO, and the correlation between code reasoning and math reasoning performance. This comprehensive analysis is a significant strength, as it provides a detailed understanding of the mechanisms at play. The paper's finding that even random rewards can improve performance on math reasoning tasks is particularly surprising and intriguing. This result challenges the conventional wisdom that RLVR requires high-quality, task-relevant rewards, and opens up new avenues for research. The authors also demonstrate that the performance gains are model-dependent, which is a crucial insight for the field. The case study on code reasoning as a representative pre-existing behavior is another strength. The authors show that RL with spurious rewards can upweight pre-existing reasoning strategies, and that prompting or RL-based induction can match or exceed the gains achieved through RL with spurious rewards. This highlights the importance of considering pretraining biases when evaluating RL methods. The paper is also well-written and easy to follow, with clear explanations of the experimental setup and results. The authors provide a thorough analysis of the results, and the paper is well-organized and easy to understand. The authors also acknowledge the limitations of their study and suggest directions for future research, which is a sign of good scientific practice. Overall, the paper's strengths lie in its novel findings, thorough analysis, and clear presentation, making it a valuable contribution to the field.


## Weaknesses:

While this paper presents several interesting findings, there are several weaknesses that warrant careful consideration. First, the paper's primary focus on the Qwen2.5-Math-7B model limits the generalizability of its conclusions. As noted by multiple reviewers, the results may not hold for other models, such as Llama 3, Mistral, or similar architectures. The authors themselves acknowledge this limitation in the conclusion, stating that they should generally be more aware that reasoning patterns instilled during pretraining heavily impact the behavior of downstream RLVR training. The paper's experimental setup and conclusions are heavily centered around the Qwen2.5-Math-7B model, and the need for testing across multiple models with differing pretraining distributions to ensure the robustness of their findings is a valid concern. This lack of generalizability is a significant limitation, as it restricts the applicability of the findings to a specific model family. Second, the paper lacks a detailed analysis of the computational cost associated with RL training. The authors do not provide any information about the number of training steps, the GPU hours, the memory usage, or the overall training time. This information is crucial for practitioners who may want to replicate the results or apply similar techniques to their own models. The absence of this information makes it difficult to assess the practical feasibility of using RL with spurious rewards for large-scale models and datasets. Furthermore, the paper does not explore the trade-offs between the computational cost and the performance gains achieved with spurious rewards. For instance, it is unclear whether there is a point of diminishing returns where increasing the training time or the number of samples does not lead to significant improvements in performance. This lack of analysis limits the practical utility of the paper's findings. Third, the paper does not delve deeply into the potential negative consequences of using spurious rewards. While the paper demonstrates that RL with spurious rewards can improve performance, it does not explore the potential for overfitting to the reward function or generating incorrect reasoning steps. The authors do not investigate whether the model is learning to exploit the spurious correlations in the reward function rather than developing a robust understanding of the underlying reasoning process. This lack of analysis is a significant oversight, as it is important to understand the limitations of using spurious rewards in RL with language models. The paper's focus is primarily on the positive outcomes of using spurious rewards, and it does not provide a detailed analysis of the potential downsides. Finally, while the paper provides a high-level explanation of the clipping term in GRPO, it lacks a rigorous mathematical analysis of its effect on the convergence properties of the algorithm. The paper states that the clipping term introduces a bias in the gradient update, but it does not provide a detailed analysis of how this bias affects the convergence of the algorithm. This lack of analysis makes it difficult to fully understand the mechanisms that enable RL to extract useful information from random rewards. The paper's explanation of the clipping term is more conceptual than deeply analytical, and it does not provide a clear understanding of why the clipping term is necessary for the observed improvements. These limitations, taken together, significantly impact the overall strength of the paper's conclusions and highlight areas for future research.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should expand their experimental scope to include a more diverse set of models. Specifically, they should include models with varying numbers of parameters and different pretraining objectives, such as Llama 3, Mistral, or similar architectures. This would provide a more comprehensive understanding of whether the observed improvements with random rewards are specific to the Qwen2.5-Math-7B model or a more general phenomenon. Furthermore, it would be beneficial to investigate the impact of different pretraining datasets and strategies on the effectiveness of RL with spurious rewards. This could involve comparing models trained on datasets with varying levels of mathematical reasoning complexity or those with different types of reasoning biases. Such an analysis would help to determine whether the observed gains are due to the model's inherent reasoning capabilities or the influence of the pretraining data. Second, the authors should provide a detailed breakdown of the resources required for their RL training experiments. This should include the number of training steps, the GPU hours, the memory usage, and the overall training time. This information is crucial for practitioners who may want to replicate the results or apply similar techniques to their own models. Furthermore, the authors should explore the trade-offs between the computational cost and the performance gains achieved with spurious rewards. For instance, they could investigate whether there is a point of diminishing returns where increasing the training time or the number of samples does not lead to significant improvements in performance. This analysis would help to determine the practical feasibility of using RL with spurious rewards for large-scale models and datasets. It would also be useful to compare the computational cost of RL with spurious rewards to other methods for improving reasoning capabilities, such as fine-tuning or data augmentation. Third, the authors should delve deeper into the potential negative consequences of using spurious rewards. While the paper demonstrates that RL with spurious rewards can improve performance, it does not explore the potential for overfitting to the reward function or generating incorrect reasoning steps. The authors should investigate whether the model is learning to exploit the spurious correlations in the reward function rather than developing a robust understanding of the underlying reasoning process. This could involve analyzing the model's behavior on out-of-distribution examples or testing its ability to generalize to new reasoning tasks. Furthermore, the authors should explore techniques for mitigating the negative consequences of spurious rewards, such as using regularization methods or incorporating human feedback into the training process. This would help to ensure that RL with spurious rewards is used responsibly and does not lead to unintended negative consequences. Finally, the authors should provide a more detailed analysis of the clipping term in GRPO. The paper should include a more rigorous mathematical analysis of the clipping term's effect on the gradient and the convergence properties of the algorithm. This could involve analyzing the gradient updates under different clipping parameters and comparing the convergence behavior with and without clipping. The paper should also explore the effect of different clipping strategies. For example, the authors could try using adaptive clipping thresholds or different clipping functions. This could provide insights into the optimal way to use the clipping term for RL with random rewards. By addressing these weaknesses, the authors can significantly strengthen their paper and make it more impactful for the research community.


## Questions:

Several questions arise from my analysis of this paper. First, how do the results generalize to other models, such as Llama 3, Mistral, or similar architectures? The paper's focus on the Qwen2.5-Math-7B model limits the generalizability of its conclusions, and it would be beneficial to understand whether the observed improvements with random rewards are specific to this model or a more general phenomenon. Second, what is the computational cost associated with RL training, and how does it scale with model size and dataset size? The paper does not provide any information about the number of training steps, the GPU hours, the memory usage, or the overall training time, which makes it difficult to assess the practical feasibility of using RL with spurious rewards for large-scale models and datasets. Third, what are the potential negative consequences of using spurious rewards, such as overfitting to the reward function or generating incorrect reasoning steps? The paper primarily focuses on the positive outcomes of using spurious rewards, and it would be beneficial to understand the potential risks associated with this approach. Fourth, how does the clipping term in GRPO interact with the random rewards, and why is it necessary for the observed improvements? The paper provides a high-level explanation of the clipping term, but it lacks a rigorous mathematical analysis of its effect on the convergence properties of the algorithm. Finally, how do the results generalize to other reasoning tasks or datasets? The paper's experiments are limited to math reasoning tasks, and it would be beneficial to understand whether the observed improvements with random rewards are specific to this task or a more general phenomenon. Addressing these questions would provide a more comprehensive understanding of the mechanisms of RLVR and the role of pretraining biases, and would help to guide future research in this area.


## Rating:

6.25


## Confidence:

3.0


## Decision:

Accept
}