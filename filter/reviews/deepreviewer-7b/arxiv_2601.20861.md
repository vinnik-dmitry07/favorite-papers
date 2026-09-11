I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper compares the performance of evolutionary strategies (ES) and gradient-based algorithms (GRPO) in continual learning settings. The authors find that while ES performs comparably to GRPO in terms of task performance, it suffers significantly more from catastrophic forgetting. The authors analyze the causes of this behavior and show that the updates made using ES are much less sparse and have larger l2 norm compared to GRPO updates, explaining the contrasting forgetting behaviors.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses an important problem in the field of continual learning, specifically the issue of catastrophic forgetting when using evolutionary strategies for fine-tuning large language models.
2. The paper provides a detailed analysis of the differences between ES and GRPO updates, including their sparsity and l2 norm. This analysis provides valuable insights into the behavior of ES in continual learning settings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's comparison of ES and GRPO is limited to a few datasets and model architectures. It is unclear whether the findings generalize to other tasks and models. Specifically, the datasets used, while diverse, may not fully represent the range of complexities encountered in real-world continual learning scenarios. The models used are also relatively small, and it's not clear if the observed differences in forgetting behavior would hold for larger, more complex models such as those with billions of parameters. The paper should include experiments on a wider range of tasks and model sizes to strengthen the generalizability of the conclusions.
2. The paper does not explore the impact of different hyperparameters on the performance of ES and GRPO. It is possible that the observed differences in forgetting behavior are sensitive to the choice of learning rate, population size, and other hyperparameters. A more thorough hyperparameter study is needed to ensure that the results are robust and not specific to a particular set of hyperparameters. For example, the learning rate for ES might need to be significantly smaller than that of GRPO to achieve comparable performance, and this difference could also affect the forgetting behavior.
3. The paper does not provide a clear explanation of why ES updates are less sparse and have larger l2 norms compared to GRPO updates. While the authors show that this difference exists, they do not provide a theoretical explanation for why this is the case. A deeper analysis of the optimization landscape and the properties of the updates would be beneficial. For instance, it would be useful to investigate whether the larger l2 norms are a result of the random perturbations inherent in ES or if there is some other underlying mechanism.

### Suggestions

The paper would benefit significantly from a more comprehensive experimental evaluation. Specifically, the authors should include experiments on a wider range of datasets, including those with more complex tasks and longer sequences. This would help to assess the generalizability of the findings to real-world scenarios. Additionally, the authors should conduct experiments with larger models, such as those with billions of parameters, to determine if the observed differences in forgetting behavior hold for more complex models. It would also be beneficial to explore the impact of different hyperparameters on the performance of ES and GRPO. This could involve systematically varying the learning rate, population size, and other relevant hyperparameters and analyzing their effect on both task performance and forgetting. The authors should also investigate the relationship between the l2 norm of the updates and the forgetting behavior. For example, they could try to reduce the l2 norm of the ES updates and see if this mitigates the forgetting problem. This could involve using different perturbation strategies or regularizing the updates. Finally, the authors should provide a more detailed analysis of the properties of the ES and GRPO updates. This could involve visualizing the updates, analyzing their sparsity patterns, and investigating their effect on the model's loss landscape. This would help to provide a deeper understanding of why ES updates are less sparse and have larger l2 norms compared to GRPO updates.

To address the lack of clarity regarding the differences in forgetting behavior, the authors should conduct a more detailed analysis of the optimization process. This could involve tracking the evolution of the model's parameters during training and visualizing the trajectory of the updates in the loss landscape. The authors could also investigate the effect of different optimization algorithms on the forgetting behavior. For example, they could compare the performance of ES and GRPO with different learning rates, batch sizes, and other hyperparameters. This would help to identify the factors that contribute to the observed differences in forgetting behavior. Furthermore, the authors should explore the relationship between the l2 norm of the updates and the forgetting behavior. For example, they could try to reduce the l2 norm of the ES updates and see if this mitigates the forgetting problem. This could involve using different perturbation strategies or regularizing the updates. Finally, the authors should provide a more detailed analysis of the properties of the ES and GRPO updates. This could involve visualizing the updates, analyzing their sparsity patterns, and investigating their effect on the model's loss landscape. This would help to provide a deeper understanding of why ES updates are less sparse and have larger l2 norms compared to GRPO updates.

### Questions

1. How does the performance of ES and GRPO vary across different tasks and model architectures? Are the findings consistent across a range of datasets and model sizes?
2. How sensitive is the performance of ES to the choice of hyperparameters? Could the observed differences in forgetting behavior be due to suboptimal hyperparameter settings for ES?
3. What is the theoretical explanation for the differences in forgetting behavior between ES and GRPO? Is it possible to modify the ES algorithm to reduce forgetting?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper compares the performance of evolutionary strategies (ES) and gradient-based algorithms (GRPO) in continual learning settings. The authors find that while ES performs comparably to GRPO in terms of task performance, it suffers significantly more from catastrophic forgetting. The authors analyze the causes of this behavior and show that the updates made using ES are much less sparse and have larger l2 norm compared to GRPO updates, explaining the contrasting forgetting behaviors.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses an important problem in the field of continual learning, specifically the issue of catastrophic forgetting when using evolutionary strategies for fine-tuning large language models.
2. The paper provides a detailed analysis of the differences between ES and GRPO updates, including their sparsity and l2 norm. This analysis provides valuable insights into the behavior of ES in continual learning settings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's comparison of ES and GRPO is limited to a few datasets and model architectures. It is unclear whether the findings generalize to other tasks and models. Specifically, the datasets used, while diverse, may not fully represent the range of complexities encountered in real-world continual learning scenarios. The models used are also relatively small, and it's not clear if the observed differences in forgetting behavior would hold for larger, more complex models such as those with billions of parameters. The paper should include experiments on a wider range of tasks and model sizes to strengthen the generalizability of the conclusions.
2. The paper does not explore the impact of different hyperparameters on the performance of ES and GRPO. It is possible that the observed differences in forgetting behavior are sensitive to the choice of learning rate, population size, and other hyperparameters. A more thorough hyperparameter study is needed to ensure that the results are robust and not specific to a particular set of hyperparameters. For example, the learning rate for ES might need to be significantly smaller than that of GRPO to achieve comparable performance, and this difference could also affect the forgetting behavior.
3. The paper does not provide a clear explanation of why ES updates are less sparse and have larger l2 norms compared to GRPO updates. While the authors show that this difference exists, they do not provide a theoretical explanation for why this is the case. A deeper analysis of the optimization landscape and the properties of the updates would be beneficial. For instance, it would be useful to investigate whether the larger l2 norms are a result of the random perturbations inherent in ES or if there is some other underlying mechanism.

### Suggestions

The paper would benefit significantly from a more comprehensive experimental evaluation. Specifically, the authors should include experiments on a wider range of datasets, including those with more complex tasks and longer sequences. This would help to assess the generalizability of the findings to real-world scenarios. Additionally, the authors should conduct experiments with larger models, such as those with billions of parameters, to determine if the observed differences in forgetting behavior hold for more complex models. It would also be beneficial to explore the impact of different hyperparameters on the performance of ES and GRPO. This could involve systematically varying the learning rate, population size, and other relevant hyperparameters and analyzing their effect on both task performance and forgetting. For example, the authors could investigate whether a smaller learning rate for ES is necessary to achieve comparable performance to GRPO and how this affects the forgetting behavior. Furthermore, the authors should provide a more detailed analysis of the properties of the ES and GRPO updates. This could involve visualizing the updates, analyzing their sparsity patterns, and investigating their effect on the model's loss landscape. This would help to provide a deeper understanding of why ES updates are less sparse and have larger l2 norms compared to GRPO updates. For example, the authors could investigate whether the larger l2 norms are a result of the random perturbations inherent in ES or if there is some other underlying mechanism.

To address the lack of clarity regarding the differences in forgetting behavior, the authors should conduct a more detailed analysis of the optimization process. This could involve tracking the evolution of the model's parameters during training and visualizing the trajectory of the updates in the loss landscape. The authors could also investigate the effect of different optimization algorithms on the forgetting behavior. For example, they could compare the performance of ES and GRPO with different learning rates, batch sizes, and other hyperparameters. This would help to identify the factors that contribute to the observed differences in forgetting behavior. Furthermore, the authors should explore the relationship between the l2 norm of the updates and the forgetting behavior. For example, they could try to reduce the l2 norm of the ES updates and see if this mitigates the forgetting problem. This could involve using different perturbation strategies or regularizing the updates. Finally, the authors should provide a more detailed analysis of the properties of the ES and GRPO updates. This could involve visualizing the updates, analyzing their sparsity patterns, and investigating their effect on the model's loss landscape. This would help to provide a deeper understanding of why ES updates are less sparse and have larger l2 norms compared to GRPO updates.

### Questions

1. How does the performance of ES and GRPO vary across different tasks and model architectures? Are the findings consistent across a range of datasets and model sizes?
2. How sensitive is the performance of ES to the choice of hyperparameters? Could the observed differences in forgetting behavior be due to suboptimal hyperparameter settings for ES?
3. What is the theoretical explanation for the differences in forgetting behavior between ES and GRPO? Is it possible to modify the ES algorithm to reduce forgetting?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the use of evolutionary strategies (ES) for continual learning in large language models (LLMs). The authors compare ES with gradient-based methods (GRPO) across several math and reasoning benchmarks, finding that while ES performs competitively on task performance, it suffers significantly more from catastrophic forgetting, where prior abilities degrade with new learning. The authors attribute this to ES updates being less sparse and having larger L2 norms compared to GRPO updates, leading to greater parameter shifts and unintended drifts from previously learned capabilities. The study highlights the memory efficiency of ES but also reveals its limitations in preserving prior knowledge, raising questions about its suitability for continual learning in LLMs without additional mechanisms.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses an important and timely topic in the field of large language models: continual learning and the challenges of catastrophic forgetting.
2. The paper provides a clear and well-structured analysis of the differences between evolutionary strategies (ES) and gradient-based methods (GRPO) in the context of continual learning.
3. The authors provide empirical evidence to support their claims, comparing ES and GRPO across multiple math and reasoning benchmarks.
4. The paper is well-written and easy to follow, with clear explanations of the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper provides a good overview of the differences between ES and GRPO, it does not delve deeply into the theoretical reasons why ES leads to catastrophic forgetting. A more detailed analysis of the underlying mechanisms would strengthen the paper.
2. The paper focuses on a specific set of benchmarks and model architectures. It would be beneficial to explore the generalizability of the findings to other tasks, datasets, and model sizes.
3. The paper does not discuss potential solutions or mitigation strategies for the catastrophic forgetting issue in ES. It would be valuable to explore how techniques like regularization or replay buffers could be adapted for ES to improve its performance in continual learning scenarios.

### Suggestions

The paper would benefit from a more in-depth investigation into the theoretical underpinnings of why evolutionary strategies (ES) lead to catastrophic forgetting in large language models (LLMs). While the empirical results are compelling, a theoretical framework would provide a more robust understanding of the observed phenomena. For instance, the authors could explore the properties of the loss landscape induced by ES updates and how these differ from those induced by gradient-based methods. Specifically, analyzing the Hessian of the loss function and its eigenvalues could provide insights into the curvature of the loss surface and how it affects the model's ability to retain previously learned knowledge. Furthermore, investigating the distribution of the ES updates and their impact on the model's parameter space could reveal why ES updates are less sparse and have larger L2 norms, leading to greater parameter shifts and forgetting. A more detailed analysis of the optimization dynamics, perhaps using tools from dynamical systems theory, could also shed light on the stability and convergence properties of ES in the context of continual learning. This would move beyond empirical observations and provide a more fundamental understanding of the issue.

To enhance the generalizability of the findings, the authors should consider expanding their experimental evaluation to include a wider range of tasks, datasets, and model architectures. While the current benchmarks provide a good starting point, it is crucial to assess the performance of ES and GRPO across different domains and model sizes. For example, the authors could evaluate their approach on tasks such as natural language understanding, text generation, or code generation, using datasets that are more diverse and representative of real-world applications. Additionally, exploring the performance of ES and GRPO on different model architectures, such as transformers with varying numbers of layers and attention heads, would provide a more comprehensive understanding of the impact of model size on the forgetting behavior. Furthermore, it would be valuable to investigate the sensitivity of the results to different hyperparameters of the ES algorithm, such as the population size and the mutation strength. This would help to identify the optimal settings for ES in different scenarios and provide a more robust evaluation of its performance.

Finally, the paper should explore potential solutions or mitigation strategies for the catastrophic forgetting issue in ES. While the paper highlights the limitations of ES in preserving prior knowledge, it does not propose any concrete solutions to address this problem. It would be valuable to investigate how techniques like regularization or replay buffers could be adapted for ES to improve its performance in continual learning scenarios. For example, the authors could explore the use of techniques such as elastic weight consolidation (EWC) or replay-based methods to mitigate the forgetting of previously learned knowledge. Furthermore, it would be interesting to investigate the use of adaptive learning rates or other optimization techniques that could help to stabilize the learning process and reduce the impact of ES updates on the model's parameter space. A more thorough exploration of these potential solutions would significantly enhance the practical value of the paper and provide a more complete picture of the challenges and opportunities of using ES for continual learning in LLMs.

### Questions

1. How does the performance of ES compare to GRPO on tasks beyond math and reasoning benchmarks? Are there specific domains where ES might be more or less suitable for continual learning?
2. Can the authors provide more details on the hyperparameter settings used for both ES and GRPO? How sensitive are the results to these settings?
3. What are the potential implications of the catastrophic forgetting observed in ES for real-world applications of LLMs? How might this impact the deployment of LLMs in dynamic environments?
4. Are there any specific modifications or extensions to the ES algorithm that could potentially mitigate the forgetting issue while maintaining its memory efficiency?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper compares the performance of Evolutionary Strategies (ES) and GRPO in the context of continual learning for LLMs. The authors find that while ES performs comparably to GRPO in terms of task performance, it suffers significantly more from catastrophic forgetting. The authors analyze the causes of this behavior and show that the updates made using ES are much less sparse and have larger l2 norm compared to GRPO updates, explaining the contrasting forgetting behaviors.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses an important problem in the field of continual learning, specifically the issue of catastrophic forgetting when using evolutionary strategies for fine-tuning large language models.
2. The paper provides a detailed analysis of the differences between ES and GRPO updates, including their sparsity and l2 norm. This analysis provides valuable insights into the behavior of ES in continual learning settings.
3. The paper is well-written and easy to follow, with clear explanations of the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's comparison of ES and GRPO is limited to a few datasets and model architectures. It is unclear whether the findings generalize to other tasks and models. Specifically, the datasets used, while diverse, may not fully represent the range of complexities encountered in real-world continual learning scenarios. The models used are also relatively small, and it's not clear if the observed differences in forgetting behavior would hold for larger, more complex models such as those with billions of parameters. The paper should include experiments on a wider range of tasks and model sizes to strengthen the generalizability of the conclusions.
2. The paper does not explore the impact of different hyperparameters on the performance of ES and GRPO. It is possible that the observed differences in forgetting behavior are sensitive to the choice of learning rate, population size, and other hyperparameters. A more thorough hyperparameter study is needed to ensure that the results are robust and not specific to a particular set of hyperparameters. For example, the learning rate for ES might need to be significantly smaller than that of GRPO to achieve comparable performance, and this difference could also affect the forgetting behavior.
3. The paper does not provide a clear explanation of why ES updates are less sparse and have larger l2 norms compared to GRPO updates. While the authors show that this difference exists, they do not provide a theoretical explanation for why this is the case. A deeper analysis of the optimization landscape and the properties of the updates would be beneficial. For instance, it would be useful to investigate whether the larger l2 norms are a result of the random perturbations inherent in ES or if there is some other underlying mechanism.

### Suggestions

The paper would benefit significantly from a more comprehensive experimental evaluation. Specifically, the authors should include experiments on a wider range of datasets, including those with more complex tasks and longer sequences. This would help to assess the generalizability of the findings to real-world scenarios. Additionally, the authors should conduct experiments with larger models, such as those with billions of parameters, to determine if the observed differences in forgetting behavior hold for more complex models. It would also be beneficial to explore the impact of different hyperparameters on the performance of ES and GRPO. This could involve systematically varying the learning rate, population size, and other relevant hyperparameters and analyzing their effect on both task performance and forgetting. For example, the authors could investigate whether a smaller learning rate for ES is necessary to achieve comparable performance to GRPO and how this affects the forgetting behavior. Furthermore, the authors should provide a more detailed analysis of the properties of the ES and GRPO updates. This could involve visualizing the updates, analyzing their sparsity patterns, and investigating their effect on the model's loss landscape. This would help to provide a deeper understanding of why ES updates are less sparse and have larger l2 norms compared to GRPO updates. For example, the authors could investigate whether the larger l2 norms are a result of the random perturbations inherent in ES or if there is some other underlying mechanism.

To address the lack of clarity regarding the differences in forgetting behavior, the authors should conduct a more detailed analysis of the optimization process. This could involve tracking the evolution of the model's parameters during training and visualizing the trajectory of the updates in the loss landscape. The authors could also investigate the effect of different optimization algorithms on the forgetting behavior. For example, they could compare the performance of ES and GRPO with different learning rates, batch sizes, and other hyperparameters. This would help to identify the factors that contribute to the observed differences in forgetting behavior. Furthermore, the authors should explore the relationship between the l2 norm of the updates and the forgetting behavior. For example, they could try to reduce the l2 norm of the ES updates and see if this mitigates the forgetting problem. This could involve using different perturbation strategies or regularizing the updates. Finally, the authors should provide a more detailed analysis of the properties of the ES and GRPO updates. This could involve visualizing the updates, analyzing their sparsity patterns, and investigating their effect on the model's loss landscape. This would help to provide a deeper understanding of why ES updates are less sparse and have larger l2 norms compared to GRPO updates.

### Questions

1. How does the performance of ES and GRPO vary across different tasks and model architectures? Are the findings consistent across a range of datasets and model sizes?
2. How sensitive is the performance of ES to the choice of hyperparameters? Could the observed differences in forgetting behavior be due to suboptimal hyperparameter settings for ES?
3. What is the theoretical explanation for the differences in forgetting behavior between ES and GRPO? Is it possible to modify the ES algorithm to reduce forgetting?

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
2. For each comment, identify the type of weakness (methodological, experimental, etc.).
3. Find specific evidence in the paper (quotes, numbers, missing information) to support the reviewer's claim.
4. If the reviewer asks a question, check if the answer is present in the paper.
5. Summarize the evidence and conclude if the weakness is valid, partially valid, or invalid.
**Review 1**

1. Weakness Statement:
"The paper's comparison of ES and GRPO is limited to a few datasets and model architectures. It is unclear whether the findings generalize to other tasks and models. Specifically, the datasets used, while diverse, may not fully represent the range of complexities encountered in real-world continual learning scenarios. The models used are also relatively small, and it's not clear if the observed differences in forgetting behavior would hold for larger, more complex models such as those with billions of parameters. The paper should include experiments on a wider range of tasks and model sizes to strengthen the generalizability of the conclusions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: The paper explicitly states the datasets used: "HellaSwag, MATH, OlympiadBench, and Countdown." (Experiments Section, Setup, Datasets)
   - Model architectures: The paper mentions the models used: "Qwen2.5-1.5B-Instruct and Llama-3.2-1B-Instruct." (Experiments Section, Setup, Models)
   - The paper does not include experiments with models having billions of parameters.

3. Literature Gap Analysis:
   - While the paper cites relevant works in continual learning and evolutionary strategies, it doesn't explicitly justify the choice of these specific datasets and model sizes in terms of their representativeness of real-world continual learning scenarios or scalability.

4. Validation Analysis:
   - Primary evidence summary: The paper uses four datasets and two relatively small models. It lacks experiments on larger models.
   - Supporting quotes: "HellaSwag, MATH, OlympiadBench, and Countdown." and "Qwen2.5-1.5B-Instruct and Llama-3.2-1B-Instruct."
   - Impact assessment: The limited number of datasets and model sizes raises concerns about the generalizability of the findings to more complex real-world scenarios and larger models.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly lists the datasets and model architectures used, which are limited in scope.

1. Weakness Statement:
"The paper does not explore the impact of different hyperparameters on the performance of ES and GRPO. It is possible that the observed differences in forgetting behavior are sensitive to the choice of learning rate, population size, and other hyperparameters. A more thorough hyperparameter study is needed to ensure that the results are robust and not specific to a particular set of hyperparameters. For example, the learning rate for ES might need to be significantly smaller than that of GRPO to achieve comparable performance, and this difference could also affect the forgetting behavior."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Implementation Details: The paper mentions the hyperparameters used for both ES and GRPO: "The experiments were conducted using a batch size of 32, a learning rate of 1e-3 for both ES and GRPO, and a population size of 30 for ES." (Experiments Section, ES vs GRPO Comparison, Setup, Implementation Details)
   - The paper does not present any experiments varying these hyperparameters.

3. Literature Gap Analysis:
   - While the paper cites the GRPO algorithm, it doesn't discuss the sensitivity of these algorithms to hyperparameter choices in the context of continual learning.

4. Validation Analysis:
   - Primary evidence summary: The paper uses fixed hyperparameters and doesn't explore the impact of varying them.
   - Supporting quotes: "The experiments were conducted using a batch size of 32, a learning rate of 1e-3 for both ES and GRPO, and a population size of 30 for ES."
   - Impact assessment: The lack of hyperparameter exploration leaves open the possibility that the observed results are specific to the chosen settings and might not hold under different configurations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the fixed hyperparameters used in the experiments.

1. Weakness Statement:
"The paper does not provide a clear explanation of why ES updates are less sparse and have larger l2 norms compared to GRPO updates. While the authors show that this difference exists, they do not provide a theoretical explanation for why this is the case. A deeper analysis of the optimization landscape and the properties of the updates would be beneficial. For instance, it would be useful to investigate whether the larger l2 norms are a result of the random perturbations inherent in ES or if there is some other underlying mechanism."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the ES update rule: "ES updates are generated by applying a random perturbation to the current model parameters, followed by a selection process to retain the best performing updates." (Method Section, Details, Evolutionary Strategies (ES))
   - The paper describes the GRPO update rule: "GRPO, on the other hand, uses a trust region method to ensure that the updates are within a certain range of the current parameters, which helps to maintain performance on previously learned tasks." (Method Section, Details, Gradient-based Parameter Optimization (GRPO))
   - The paper presents empirical results showing the sparsity and L2 norm differences (Figure 4).
b) Experiment-related Evidence:
   - Figure 4 shows the sparsity and L2 norm of the updates.
   - The paper offers an interpretation: "The lack of sparsity and large update norms in ES drifts the fine-tuned model further away from the base model, potentially leading to the catastrophic forgetting of prior capabilities." (Experiments Section, ES and Catastrophic Forgetting, Analysis)
   - However, this explanation is descriptive rather than a deep theoretical analysis.

3. Literature Gap Analysis:
   - The paper cites the original ES and GRPO papers, but doesn't delve into the theoretical underpinnings of why ES might produce less sparse and larger norm updates in the context of continual learning.

4. Validation Analysis:
   - Primary evidence summary: The paper shows the difference in sparsity and L2 norms but lacks a deep theoretical explanation for this phenomenon.
   - Supporting quotes: (Figure 4 results) and the analysis in the "ES and Catastrophic Forgetting" section.
   - Impact assessment: The lack of a theoretical explanation weakens the understanding of the underlying mechanisms causing the observed forgetting behavior.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper presents the empirical results but lacks a detailed theoretical analysis of the reasons behind the observed differences in update properties.

**Review 2**

1. Weakness Statement:
"The paper's comparison of ES and GRPO is limited to a few datasets and model architectures. It is unclear whether the findings generalize to other tasks and models. Specifically, the datasets used, while diverse, may not fully represent the range of complexities encountered in real-world continual learning scenarios. The models used are also relatively small, and it's not clear if the observed differences in forgetting behavior would hold for larger, more complex models such as those with billions of parameters. The paper should include experiments on a wider range of tasks and model sizes to strengthen the generalizability of the conclusions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: "HellaSwag, MATH, OlympiadBench, and Countdown." (Experiments Section, Setup, Datasets)
   - Model architectures: "Qwen2.5-1.5B-Instruct and Llama-3.2-1B-Instruct." (Experiments Section, Setup, Models)
   - The paper does not include experiments with models having billions of parameters.

3. Literature Gap Analysis:
   - While the paper cites relevant works in continual learning and evolutionary strategies, it doesn't explicitly justify the choice of these specific datasets and model sizes in terms of their representativeness of real-world continual learning scenarios or scalability.

4. Validation Analysis:
   - Primary evidence summary: The paper uses four datasets and two relatively small models. It lacks experiments on larger models.
   - Supporting quotes: "HellaSwag, MATH, OlympiadBench, and Countdown." and "Qwen2.5-1.5B-Instruct and Llama-3.2-1B-Instruct."
   - Impact assessment: The limited number of datasets and model sizes raises concerns about the generalizability of the findings to more complex real-world scenarios and larger models.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly lists the datasets and model architectures used, which are limited in scope.

1. Weakness Statement:
"The paper does not explore the impact of different hyperparameters on the performance of ES and GRPO. It is possible that the observed differences in forgetting behavior are sensitive to the choice of learning rate, population size, and other hyperparameters. A more thorough hyperparameter study is needed to ensure that the results are robust and not specific to a particular set of hyperparameters. For example, the learning rate for ES might need to be significantly smaller than that of GRPO to achieve comparable performance, and this difference could also affect the forgetting behavior."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Implementation Details: The paper mentions the hyperparameters used for both ES and GRPO: "The experiments were conducted using a batch size of 32, a learning rate of 1e-3 for both ES and GRPO, and a population size of 30 for ES." (Experiments Section, ES vs GRPO Comparison, Setup, Implementation Details)
   - The paper does not present any experiments varying these hyperparameters.

3. Literature Gap Analysis:
   - While the paper cites the GRPO algorithm, it doesn't discuss the sensitivity of these algorithms to hyperparameter choices in the context of continual learning.

4. Validation Analysis:
   - Primary evidence summary: The paper uses fixed hyperparameters and doesn't explore the impact of varying them.
   - Supporting quotes: "The experiments were conducted using a batch size of 32, a learning rate of 1e-3 for both ES and GRPO, and a population size of 30 for ES."
   - Impact assessment: The lack of hyperparameter exploration leaves open the possibility that the observed results are specific to the chosen settings and might not hold under different configurations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the fixed hyperparameters used in the experiments.

1. Weakness Statement:
"The paper does not provide a clear explanation of why ES updates are less sparse and have larger l2 norms compared to GRPO updates. While the authors show that this difference exists, they do not provide a theoretical explanation for why this is the case. A deeper analysis of the optimization landscape and the properties of the updates would be beneficial. For instance, it would be useful to investigate whether the larger l2 norms are a result of the random perturbations inherent in ES or if there is some other underlying mechanism."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the ES update rule: "ES updates are generated by applying a random perturbation to the current model parameters, followed by a selection process to retain the best performing updates." (Method Section, Details, Evolutionary Strategies (ES))
   - The paper describes the GRPO update rule: "GRPO, on the other hand, uses a trust region method to ensure that the updates are within a certain range of the current parameters, which helps to maintain performance on previously learned tasks." (Method Section, Details, Gradient-based Parameter Optimization (GRPO))
   - The paper presents empirical results showing the sparsity and L2 norm differences (Figure 4).
   - The paper offers an interpretation: "The lack of sparsity and large update norms in ES drifts the fine-tuned model further away from the base model, potentially leading to the catastrophic forgetting of prior capabilities." (Experiments Section, ES and Catastrophic Forgetting, Analysis)
   - However, this explanation is descriptive rather than a deep theoretical analysis.

3. Literature Gap Analysis:
   - The paper cites the original ES and GRPO papers, but doesn't delve into the theoretical underpinnings of why ES might produce less sparse and larger norm updates in the context of continual learning.

4. Validation Analysis:
   - Primary evidence summary: The paper shows the difference in sparsity and L2 norms but lacks a deep theoretical explanation for this phenomenon.
   - Supporting quotes: (Figure 4 results) and the analysis in the "ES and Catastrophic Forgetting" section.
   - Impact assessment: The lack of a theoretical explanation weakens the understanding of the underlying mechanisms causing the observed forgetting behavior.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper presents the empirical results but lacks a detailed theoretical analysis of the reasons behind the observed differences in update properties.

**Review 3**

1. Weakness Statement:
"While the paper provides a good overview of the differences between ES and GRPO, it does not delve deeply into the theoretical reasons why ES leads to catastrophic forgetting. A more detailed analysis of the underlying mechanisms would strengthen the paper."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the ES and GRPO update rules (Method Section).
   - The paper provides an intuitive explanation based on the properties of the updates (Experiments Section, ES and Catastrophic Forgetting).
   - However, it lacks a formal theoretical analysis of the optimization landscape or the properties of the updates that lead to forgetting.

3. Literature Gap Analysis:
   - While the paper cites relevant works, it doesn't engage deeply with the theoretical literature on the convergence and stability of ES and GRPO in the context of continual learning.

4. Validation Analysis:
   - Primary evidence summary: The paper explains the difference in forgetting but lacks a deep theoretical analysis of the underlying mechanisms.
   - Supporting quotes: (Method and Experiments sections).
   - Impact assessment: The lack of a theoretical analysis limits the understanding of why ES is more prone to catastrophic forgetting in this context.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper focuses on empirical observations and intuitive explanations rather than a formal theoretical analysis.

1. Weakness Statement:
"The paper focuses on a specific set of benchmarks and model architectures. It would be beneficial to explore the generalizability of the findings to other tasks, datasets, and model sizes."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: "HellaSwag, MATH, OlympiadBench, and Countdown." (Experiments Section, ES vs GRPO Comparison, Setup, Datasets)
   - Model architectures: "Qwen2.5-1.5B-Instruct and Llama-3.2-1B-Instruct." (Experiments Section, ES vs GRPO Comparison, Setup, Models)
   - The paper does not include experiments on a wider range of tasks, datasets, or model sizes.

3. Literature Gap Analysis:
   - The paper doesn't explicitly justify the choice of these specific benchmarks and model architectures in terms of their representativeness of the broader continual learning problem.

4. Validation Analysis:
   - Primary evidence summary: The paper uses a limited set of benchmarks and model architectures.
   - Supporting quotes: "HellaSwag, MATH, OlympiadBench, and Countdown." and "Qwen2.5-1.5B-Instruct and Llama-3.2-1B-Instruct."
   - Impact assessment: The limited scope of the experiments raises questions about the generalizability of the conclusions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly lists the datasets and model architectures used, which are limited in scope.

1. Weakness Statement:
"The paper does not discuss potential solutions or mitigation strategies for the catastrophic forgetting issue in ES. It would be valuable to explore how techniques like regularization or replay buffers could be adapted for ES to improve its performance in continual learning scenarios."

2. Evidence Collection:
   - The paper focuses on comparing ES and GRPO and analyzing the reasons for catastrophic forgetting (Introduction, Main Idea, Method, Experiments, Conclusion).
   - There is no discussion of potential solutions or adaptation of techniques like regularization or replay buffers for ES.

3. Literature Gap Analysis:
   - While the paper cites relevant works, it doesn't explore the literature on mitigating catastrophic forgetting in the context of evolutionary strategies.

4. Validation Analysis:
   - Primary evidence summary: The paper focuses on analysis and doesn't discuss solutions.
   - Impact assessment: The lack of discussion on potential solutions limits the practical implications of the findings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus is on analyzing the problem rather than proposing solutions.

**Review 4**

1. Weakness Statement:
"The paper's comparison of ES and GRPO is limited to a few datasets and model architectures. It is unclear whether the findings generalize to other tasks and models. Specifically, the datasets used, while diverse, may not fully represent the range of complexities encountered in real-world continual learning scenarios. The models used are also relatively small, and it's not clear if the observed differences in forgetting behavior would hold for larger, more complex models such as those with billions of parameters. The paper should include experiments on a wider range of tasks and model sizes to strengthen the generalizability of the conclusions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: "HellaSwag, MATH, OlympiadBench, and Countdown." (Experiments Section, ES vs GRPO Comparison, Setup, Datasets)
   - Model architectures: "Qwen2.5-1.5B-Instruct and Llama-3.2-1B-Instruct." (Experiments Section, ES vs GRPO Comparison, Setup, Models)
   - The paper does not include experiments on a wider range of tasks, datasets, or model sizes.

3. Literature Gap Analysis:
   - The paper doesn't explicitly justify the choice of these specific datasets and model sizes in terms of their representativeness of real-world continual learning scenarios or scalability.

4. Validation Analysis:
   - Primary evidence summary: The paper uses a limited set of datasets and model architectures.
   - Supporting quotes: "HellaSwag, MATH, OlympiadBench, and Countdown." and "Qwen2.5-1.5B-Instruct and Llama-3.2-1B-Instruct."
   - Impact assessment: The limited scope of the experiments raises questions about the generalizability of the conclusions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly lists the datasets and model architectures used, which are limited in scope.

1. Weakness Statement:
"The paper does not explore the impact of different hyperparameters on the performance of ES and GRPO. It is possible that the observed differences in forgetting behavior are sensitive to the choice of learning rate, population size, and other hyperparameters. A more thorough hyperparameter study is needed to ensure that the results are robust and not specific to a particular set of hyperparameters. For example, the learning rate for ES might need to be significantly smaller than that of GRPO to achieve comparable performance, and this difference could also affect the forgetting behavior."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Implementation Details: The paper mentions the hyperparameters used for both ES and GRPO: "The experiments were conducted using a batch size of 32, a learning rate of 1e-3 for both ES and GRPO, and a population size of 30 for ES." (Experiments Section, ES vs GRPO Comparison, Setup, Implementation Details)
   - The paper does not present any experiments varying these hyperparameters.

3. Literature Gap Analysis:
   - While the paper cites the GRPO algorithm, it doesn't discuss the sensitivity of these algorithms to hyperparameter choices in the context of continual learning.

4. Validation Analysis:
   - Primary evidence summary: The paper uses fixed hyperparameters and doesn't explore the impact of varying them.
   - Supporting quotes: "The experiments were conducted using a batch size of 32, a learning rate of 1e-3 for both ES and GRPO, and a population size of 30 for ES."
   - Impact assessment: The lack of hyperparameter exploration leaves open the possibility that the observed results are specific to the chosen settings and might not hold under different configurations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the fixed hyperparameters used in the experiments.

1. Weakness Statement:
"The paper does not provide a clear explanation of why ES updates are less sparse and have larger l2 norms compared to GRPO updates. While the authors show that this difference exists, they do not provide a theoretical explanation for why this is the case. A deeper analysis of the optimization landscape and the properties of the updates would be beneficial. For instance, it would be useful to investigate whether the larger l2 norms are a result of the random perturbations inherent in ES or if there is some other underlying mechanism."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the ES and GRPO update rules (Method Section).
   - The paper presents empirical results showing the sparsity and L2 norm differences (Figure 4).
   - The paper offers an interpretation: "The lack of sparsity and large update norms in ES drifts the fine-tuned model further away from the base model, potentially leading to the catastrophic forgetting of prior capabilities." (Experiments Section, ES and Catastrophic Forgetting, Analysis)
   - However, this explanation is descriptive rather than a deep theoretical analysis.

3. Literature Gap Analysis:
   - The paper cites the original ES and GRPO papers, but doesn't delve into the theoretical underpinnings of why ES might produce less sparse and larger norm updates in the context of continual learning.

4. Validation Analysis:
   - Primary evidence summary: The paper shows the difference in sparsity and L2 norms but lacks a deep theoretical explanation for this phenomenon.
   - Supporting quotes: (Figure 4 results) and the analysis in the "ES and Catastrophic Forgetting" section.
   - Impact assessment: The lack of a theoretical explanation weakens the understanding of the underlying mechanisms causing the observed forgetting behavior.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper presents the empirical results but lacks a detailed theoretical analysis of the reasons behind the observed differences in update properties.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper investigates the performance of Evolutionary Strategies (ES) in the context of continual learning for large language models, comparing it against gradient-based methods like Gradient-Based Parameter Optimization (GRPO). The authors' core contribution lies in their empirical analysis, which reveals that while ES performs comparably to GRPO in terms of task performance, it suffers significantly more from catastrophic forgetting when learning new tasks sequentially. This finding is significant because it highlights a critical limitation of ES in continual learning scenarios, despite its memory efficiency. The paper's methodology involves fine-tuning language models on a variety of mathematical and reasoning benchmarks, including HellaSwag, MATH, OlympiadBench, and Countdown, using both ES and GRPO. The authors meticulously compare the performance of these methods, focusing not only on task accuracy but also on the model's ability to retain knowledge from previously learned tasks. A key aspect of their analysis is the examination of the update properties of ES and GRPO. They find that ES updates are less sparse and have larger L2 norms compared to GRPO updates. This difference in update properties is presented as a potential explanation for the catastrophic forgetting observed with ES. The authors argue that the larger L2 norms and less sparse updates of ES push the model parameters further away from the pre-trained state, leading to a degradation of performance on prior tasks. The paper's findings are significant because they provide empirical evidence that challenges the potential of ES as a memory-efficient alternative to gradient-based methods for continual learning in large language models. The authors also explore the underlying reasons for the differences in forgetting behavior between ES and GRPO, suggesting that the update properties of ES are a key factor. This work is important because it provides a deeper understanding of the trade-offs between different optimization methods in the context of continual learning, and it highlights the need for further research into mitigation strategies for catastrophic forgetting in ES. The paper's focus on memory efficiency is particularly relevant given the increasing size and complexity of language models, making the study of memory-efficient continual learning methods crucial. The authors' analysis of the update properties of ES and GRPO provides a valuable starting point for future research in this area, and their findings have important implications for the practical application of ES in real-world scenarios.


## Soundness:

2.75


## Presentation:

2.75


## Contribution:

2.25


## Strengths:

This paper presents several notable strengths, primarily in its empirical investigation and clear presentation of results. The most significant strength is the paper's focus on a critical and timely problem: the application of Evolutionary Strategies (ES) to continual learning in large language models. The authors have identified a crucial gap in the literature by directly comparing ES with a gradient-based method, GRPO, in the context of continual learning. This direct comparison is valuable because it allows for a clear understanding of the trade-offs between these two approaches. The paper's empirical approach is another significant strength. The authors have conducted a thorough analysis of the performance of ES and GRPO across multiple mathematical and reasoning benchmarks, providing a robust foundation for their conclusions. The use of diverse datasets, including HellaSwag, MATH, OlympiadBench, and Countdown, ensures that the findings are not limited to a specific task or domain. The paper's analysis of the update properties of ES and GRPO is also a significant contribution. The authors have shown that ES updates are less sparse and have larger L2 norms compared to GRPO updates. This observation is crucial because it provides a potential explanation for the catastrophic forgetting observed with ES. The authors' analysis of the optimization landscape and the properties of the updates is a valuable step towards understanding the underlying mechanisms causing the observed forgetting behavior. The paper is also well-written and easy to follow, with clear explanations of the methodology and results. The authors have provided a detailed description of the experimental setup, including the models used, the datasets, and the hyperparameters. The results are presented in a clear and concise manner, with appropriate use of figures and tables. The paper's focus on memory efficiency is also a strength, as it addresses a critical challenge in the deployment of large language models in real-world scenarios. The authors have highlighted the potential of ES as a memory-efficient alternative to gradient-based methods, and their findings have important implications for the practical application of ES in continual learning settings. Finally, the paper's identification of the lack of sparsity and large L2 norms in ES updates as a potential cause of catastrophic forgetting is a valuable insight that can guide future research in this area. The paper's clear articulation of the problem, the methodology, and the results makes it a valuable contribution to the field of continual learning.


## Weaknesses:

Despite its strengths, this paper has several notable weaknesses that limit the generalizability and depth of its conclusions. The most significant weakness is the limited scope of the experimental evaluation. The authors have used only four datasets (HellaSwag, MATH, OlympiadBench, and Countdown) and two relatively small language models (Qwen2.5-1.5B-Instruct and Llama-3.2-1B-Instruct) for their experiments. This narrow selection of datasets and models raises concerns about whether the observed differences between ES and GRPO would hold for a wider range of tasks and model sizes. Specifically, the datasets used, while diverse, may not fully represent the range of complexities encountered in real-world continual learning scenarios. The models used are also relatively small, and it is not clear if the observed differences in forgetting behavior would hold for larger, more complex models such as those with billions of parameters. This limitation is significant because the performance of ES and GRPO might vary significantly with different model architectures and sizes, and the paper's conclusions may not generalize to larger models. The authors do not provide any justification for the choice of these specific datasets and models, and this lack of justification further weakens the generalizability of the findings. My confidence in this weakness is high, as the paper explicitly lists the datasets and model architectures used, and these are indeed a limited set. Another significant weakness is the lack of exploration of the impact of different hyperparameters on the performance of ES and GRPO. The authors used fixed hyperparameters for both ES and GRPO, with a batch size of 32, a learning rate of 1e-3, and a population size of 30 for ES. However, it is possible that the observed differences in forgetting behavior are sensitive to the choice of these hyperparameters. For example, the learning rate for ES might need to be significantly smaller than that of GRPO to achieve comparable performance, and this difference could also affect the forgetting behavior. The authors do not present any experiments varying these hyperparameters, and this lack of exploration leaves open the possibility that the results are specific to the chosen settings and might not hold under different configurations. This is a critical limitation because it raises questions about the robustness of the findings and the practical applicability of ES in different scenarios. My confidence in this weakness is high, as the paper explicitly states the fixed hyperparameters used in the experiments. Furthermore, the paper does not provide a clear explanation of why ES updates are less sparse and have larger L2 norms compared to GRPO updates. While the authors show that this difference exists, they do not provide a theoretical explanation for why this is the case. The paper offers an intuitive explanation based on the properties of the updates, but this explanation is descriptive rather than a deep theoretical analysis. The authors state that the lack of sparsity and large update norms in ES drifts the fine-tuned model further away from the base model, potentially leading to catastrophic forgetting. However, this explanation is not sufficient to fully understand the underlying mechanisms causing the observed differences in update properties. The lack of a theoretical explanation weakens the understanding of the underlying mechanisms causing the observed forgetting behavior. My confidence in this weakness is high, as the paper presents the empirical results but lacks a detailed theoretical analysis of the reasons behind the observed differences in update properties. Finally, the paper does not explore potential solutions or mitigation strategies for the catastrophic forgetting issue in ES. While the paper highlights the limitations of ES in preserving prior knowledge, it does not propose any concrete solutions to address this problem. The authors do not discuss how techniques like regularization or replay buffers could be adapted for ES to improve its performance in continual learning scenarios. This lack of discussion on potential solutions limits the practical implications of the findings and leaves open the question of how to effectively use ES in real-world continual learning applications. My confidence in this weakness is high, as the paper's focus is on analyzing the problem rather than proposing solutions.


## Suggestions:

To address the identified weaknesses and strengthen the paper, I recommend several concrete improvements. First, the authors should significantly expand their experimental evaluation to include a wider range of datasets and model architectures. This would involve incorporating datasets with more complex tasks and longer sequences, such as those found in natural language understanding, text generation, or code generation. This would help to assess the generalizability of the findings to real-world scenarios. Additionally, the authors should conduct experiments with larger models, such as those with billions of parameters, to determine if the observed differences in forgetting behavior hold for more complex models. It would also be beneficial to explore the impact of different hyperparameters on the performance of ES and GRPO. This could involve systematically varying the learning rate, population size, and other relevant hyperparameters and analyzing their effect on both task performance and forgetting. For example, the authors could investigate whether a smaller learning rate for ES is necessary to achieve comparable performance to GRPO and how this affects the forgetting behavior. This would help to identify the factors that contribute to the observed differences in forgetting behavior and ensure that the results are robust and not specific to a particular set of hyperparameters. Furthermore, the authors should provide a more detailed analysis of the properties of the ES and GRPO updates. This could involve visualizing the updates, analyzing their sparsity patterns, and investigating their effect on the model's loss landscape. This would help to provide a deeper understanding of why ES updates are less sparse and have larger L2 norms compared to GRPO updates. For example, the authors could try to reduce the L2 norm of the ES updates and see if this mitigates the forgetting problem. This could involve using different perturbation strategies or regularizing the updates. Finally, the authors should explore potential solutions or mitigation strategies for the catastrophic forgetting issue in ES. This could involve investigating how techniques like regularization or replay buffers could be adapted for ES to improve its performance in continual learning scenarios. For example, the authors could explore the use of techniques such as elastic weight consolidation (EWC) or replay-based methods to mitigate the forgetting of previously learned knowledge. Furthermore, it would be interesting to investigate the use of adaptive learning rates or other optimization techniques that could help to stabilize the learning process and reduce the impact of ES updates on the model's parameter space. A more thorough exploration of these potential solutions would significantly enhance the practical value of the paper and provide a more complete picture of the challenges and opportunities of using ES for continual learning in LLMs. In summary, these suggestions aim to address the limitations of the paper by expanding the experimental evaluation, exploring the impact of different hyperparameters, providing a deeper analysis of the update properties, and exploring potential solutions to the catastrophic forgetting issue in ES.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for a deeper understanding of the paper's findings and their implications. First, how does the performance of ES and GRPO vary across different tasks and model architectures? Are the findings consistent across a range of datasets and model sizes, or are there specific domains where ES might be more or less suitable for continual learning? This question is important because it directly addresses the generalizability of the findings, which is a key limitation of the current study. Second, how sensitive is the performance of ES to the choice of hyperparameters? Could the observed differences in forgetting behavior be due to suboptimal hyperparameter settings for ES? This question is crucial because it addresses the robustness of the findings and the practical applicability of ES in different scenarios. Third, what is the theoretical explanation for the differences in update properties between ES and GRPO? Is it possible to modify the ES algorithm to reduce the forgetting issue while maintaining its memory efficiency? This question is important because it addresses the underlying mechanisms causing the observed forgetting behavior and seeks potential solutions to mitigate this issue. Fourth, how does the performance of ES compare to GRPO on tasks beyond math and reasoning benchmarks? Are there specific domains where ES might be more or less suitable for continual learning? This question is important because it addresses the applicability of ES in real-world scenarios and seeks to identify potential limitations of the method. Finally, what are the potential implications of the catastrophic forgetting observed in ES for real-world applications of LLMs? How might this impact the deployment of LLMs in dynamic environments? This question is important because it addresses the practical relevance of the findings and seeks to understand the potential impact of the observed limitations on real-world applications. These questions are designed to target the core methodological choices and assumptions of the paper, and I believe that addressing them would significantly enhance the understanding and impact of this work.


## Rating:

5.5


## Confidence:

3.0


## Decision:

Reject
}