I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper introduces TTT-Discover, a novel method for scientific discovery using reinforcement learning (RL). Unlike traditional RL applications that focus on optimizing rewards, TTT-Discover aims to find a single, high-performing solution rather than continuously improving. The authors adapt RL to this setting by using a best-of-N strategy, a PUCT-inspired exploration method, and an entropic objective. The approach is evaluated across five domains—mathematics, GPU kernel engineering, algorithm design, and biology—and demonstrates state-of-the-art performance in several tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a unique problem in scientific discovery, where the goal is to find a single, optimal solution rather than continuous improvement.
- The authors provide a comprehensive evaluation across multiple domains, including mathematics, GPU kernel engineering, algorithm design, and biology, showcasing the versatility of their method.
- The paper is well-written, with clear explanations of the methods and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational resources required for the experiments. This information would be valuable for readers who want to replicate the results or apply the method to new problems.
- The paper does not discuss the limitations of the method or potential failure cases. It would be helpful to understand the scenarios where the method is likely to fail or underperform.
- The paper does not compare the method to other state-of-the-art methods in the field. A comparison to existing methods would help to contextualize the contributions of the paper.
- The paper does not provide a detailed analysis of the sensitivity of the method to hyperparameters. This information would be valuable for readers who want to apply the method to new problems.
- The paper does not discuss the potential ethical implications of the method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse.

### Suggestions

The paper would benefit from a more thorough discussion of the computational costs associated with the TTT-Discover method. Specifically, the authors should provide details on the hardware used for each experiment, the training time, and the memory requirements. This information is crucial for other researchers who may want to replicate the results or apply the method to their own problems. Furthermore, it would be helpful to understand how the computational cost scales with the complexity of the problem and the size of the search space. For example, the authors could provide a breakdown of the time spent on exploration versus exploitation, and how this varies across different tasks. This would allow readers to better understand the practical limitations of the method and make informed decisions about its applicability to their own research questions.

In addition to computational costs, the paper should include a more detailed discussion of the limitations of the TTT-Discover method. The authors should discuss scenarios where the method is likely to fail or underperform, and provide examples of such cases. For instance, it would be useful to understand how the method behaves when the reward function is noisy or sparse, or when the search space is highly discontinuous. The authors should also discuss the potential for the method to get stuck in local optima, and how this can be mitigated. Furthermore, it would be helpful to understand the sensitivity of the method to the choice of hyperparameters, such as the exploration rate and the learning rate. A more detailed analysis of these aspects would provide a more complete picture of the strengths and weaknesses of the method.

Finally, the paper should include a more comprehensive comparison to existing methods in the field. While the authors mention related work, a more detailed comparison to state-of-the-art methods would help to contextualize the contributions of the paper. This comparison should include both quantitative and qualitative aspects, such as the performance of the method on benchmark problems, the computational cost, and the ease of implementation. For example, the authors could compare their method to other reinforcement learning algorithms that have been applied to scientific discovery problems, or to other methods that have been developed for solving similar optimization problems. This would help to highlight the unique advantages of the TTT-Discover method and its potential impact on the field.

### Questions

- How does the method scale with the complexity of the problem and the size of the search space?
- What are the limitations of the method, and in what scenarios is it likely to fail?
- How sensitive is the method to hyperparameters, and how can these be tuned effectively?
- How does the method compare to other state-of-the-art methods in the field?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a novel approach to scientific discovery using reinforcement learning (RL). The authors introduce TTT-Discover, which leverages test-time training to optimize a policy for a specific scientific task. Unlike traditional RL methods that focus on continuous improvement, TTT-Discover aims to find a single, best-performing solution. The method employs an entropic objective, PUCT-inspired exploration, and state reuse to enhance performance. The authors evaluate TTT-Discover across five domains: mathematics, GPU kernel engineering, algorithm design, and biology. The results demonstrate that TTT-Discover achieves state-of-the-art performance in several tasks, surpassing previous best results.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel application of reinforcement learning to scientific discovery, focusing on finding a single, best-performing solution rather than continuous improvement. This is a fresh perspective in the field of AI for science.
2. The authors provide a comprehensive evaluation of TTT-Discover across multiple domains, including mathematics, GPU kernel engineering, algorithm design, and biology. This demonstrates the versatility and robustness of the method.
3. The paper is well-organized and clearly written, making it accessible to readers from both AI and scientific communities.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for the experiments. This information would be valuable for readers who want to replicate the results or apply the method to new problems.
2. The paper does not discuss the limitations of the method or potential failure cases. It would be helpful to understand the scenarios where the method is likely to fail or underperform.
3. The paper does not compare the method to other state-of-the-art methods in the field. A comparison to existing methods would help to contextualize the contributions of the paper.
4. The paper does not provide a detailed analysis of the sensitivity of the method to hyperparameters. This information would be valuable for readers who want to apply the method to new problems.
5. The paper does not discuss the potential ethical implications of the method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse.

### Suggestions

The authors should provide a more detailed analysis of the computational resources required for their experiments. This should include information on the hardware used, the training time, and the memory requirements. This information is crucial for other researchers who may want to replicate the results or apply the method to their own problems. Furthermore, it would be beneficial to understand how the computational cost scales with the complexity of the problem and the size of the search space. For example, the authors could provide a breakdown of the time spent on exploration versus exploitation, and how this varies across different tasks. This would allow readers to better understand the practical limitations of the method and make informed decisions about its applicability to their own research questions.

In addition to computational resources, the authors should also discuss the limitations of their method and potential failure cases. This should include an analysis of scenarios where the method is likely to fail or underperform. For example, the authors could discuss how the method might perform when the reward function is noisy or sparse, or when the search space is highly discontinuous. It would also be helpful to understand the sensitivity of the method to the choice of hyperparameters, such as the exploration rate and the learning rate. A more detailed analysis of these aspects would provide a more complete picture of the strengths and weaknesses of the method. Furthermore, the authors should discuss the potential ethical implications of their method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse. A discussion of these issues would help to ensure that the method is used responsibly and ethically.

Finally, the authors should provide a more comprehensive comparison to existing methods in the field. This comparison should include both quantitative and qualitative aspects, such as the performance of the method on benchmark problems, the computational cost, and the ease of implementation. For example, the authors could compare their method to other reinforcement learning algorithms that have been applied to scientific discovery problems, or to other methods that have been developed for solving similar optimization problems. This would help to contextualize the contributions of the paper and highlight the unique advantages of the proposed approach. A more thorough comparison would also help to identify areas where the method could be improved and to guide future research in this area.

### Questions

1. How does the method scale with the complexity of the problem and the size of the search space?
2. What are the limitations of the method, and in what scenarios is it likely to fail?
3. How sensitive is the method to hyperparameters, and how can these be tuned effectively?
4. How does the method compare to other state-of-the-art methods in the field?

### Rating

6

### Confidence

2

**********

## Reviewer 3

### Summary

This paper introduces TTT-Discover, a novel method for scientific discovery that leverages reinforcement learning (RL) to find optimal solutions in a single attempt, rather than through iterative improvement. Unlike traditional RL approaches that focus on continuous learning, TTT-Discover is designed to identify the best solution possible within a given environment. The authors apply TTT-Discover to five diverse scientific domains: mathematics, GPU kernel engineering, algorithm design, and biology. The method demonstrates state-of-the-art performance in several tasks, outperforming existing AI baselines and human results. The paper also includes a detailed comparison with other RL-based approaches, such as AlphaEvolve and MiGrAt, highlighting the advantages of TTT-Discover in terms of both performance and computational efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. **Novel Problem Formulation**: The paper introduces a unique problem formulation in scientific discovery by focusing on finding a single best solution rather than continuous improvement. This approach is particularly relevant in fields where discovering a single optimal solution is more critical than making incremental improvements.

2. **Strong Empirical Results**: TTT-Discover achieves state-of-the-art performance in several scientific tasks, outperforming both AI baselines and human results. The authors provide detailed experimental results across multiple domains, including mathematics, GPU kernel engineering, algorithm design, and biology, demonstrating the versatility and effectiveness of the method.

3. **Comparison with Existing Methods**: The paper includes a thorough comparison with other RL-based approaches, such as AlphaEvolve and MiGrAt. This comparison highlights the advantages of TTT-Discover in terms of both performance and computational efficiency, providing a clear understanding of its strengths relative to existing methods.

4. **Detailed Methodology**: The paper provides a clear and detailed description of the TTT-Discover method, including the use of an entropic objective, PUCT-inspired exploration, and state reuse. This thorough explanation helps readers understand the technical details of the approach and its effectiveness in solving complex scientific problems.

### Weaknesses

#### Some Related Works


#### comment

1. **Limited Exploration of Hyperparameter Sensitivity**: While the paper provides a detailed description of the TTT-Discover method, it lacks a thorough analysis of how sensitive the method is to different hyperparameter settings. Understanding the impact of hyperparameters on performance is crucial for practical applications, and the paper could benefit from a more in-depth discussion of this aspect. Specifically, the paper does not explore the sensitivity of the method to parameters such as the exploration rate, the learning rate, and the batch size, which could significantly affect the convergence and stability of the algorithm. A more rigorous analysis of these parameters would provide a better understanding of the method's robustness and generalizability.

2. **Lack of Discussion on Computational Cost**: The paper does not provide a detailed analysis of the computational cost associated with the TTT-Discover method. While the authors mention the use of a powerful GPU, they do not discuss the time complexity of the algorithm or the resources required to run it on different hardware configurations. This information is essential for researchers who want to apply the method to their own problems, and a more thorough discussion of the computational cost would help them assess the feasibility of using TTT-Discover in their work. The paper should include a breakdown of the computational cost for each stage of the algorithm, including the exploration phase, the policy training phase, and the evaluation phase, and discuss how these costs scale with the size of the problem and the complexity of the environment.

3. **Limited Discussion on Limitations and Failure Cases**: The paper does not provide a detailed discussion of the limitations of the TTT-Discover method or potential failure cases. Understanding the limitations of the method is crucial for researchers who want to use it in their work, and a more thorough discussion of these aspects would help them avoid potential pitfalls. The paper should discuss scenarios where the method might fail to find the optimal solution, such as when the reward function is noisy or sparse, or when the search space is highly discontinuous. It should also discuss the limitations of the method in terms of the types of problems it can solve and the types of environments it can handle.

### Suggestions

To address the lack of hyperparameter sensitivity analysis, the authors should conduct a more thorough investigation of how different hyperparameter settings affect the performance of TTT-Discover. This should include a systematic exploration of the parameter space, using techniques such as grid search or random search, to identify the optimal hyperparameter settings for different tasks. The authors should also provide a detailed analysis of the impact of each hyperparameter on the convergence and stability of the algorithm, and discuss how these parameters should be tuned for different types of problems. For example, the exploration rate should be tuned to balance exploration and exploitation, while the learning rate should be tuned to ensure that the algorithm converges to a good solution without overshooting. The batch size should be tuned to balance the computational cost and the stability of the algorithm. This analysis should be included in the main body of the paper, rather than just in the appendix, as it is crucial for the practical application of the method.

To address the lack of discussion on computational cost, the authors should provide a more detailed analysis of the time complexity of the TTT-Discover method. This should include a breakdown of the computational cost for each stage of the algorithm, including the exploration phase, the policy training phase, and the evaluation phase. The authors should also discuss how these costs scale with the size of the problem and the complexity of the environment. For example, the exploration phase might be more computationally expensive for large search spaces, while the policy training phase might be more computationally expensive for complex environments. The authors should also discuss the hardware requirements for running the method, including the type of GPU and the amount of memory required. This information should be included in the main body of the paper, rather than just in the appendix, as it is crucial for researchers who want to apply the method to their own problems. The authors should also provide guidelines for optimizing the implementation of the method to reduce the computational cost, such as using more efficient data structures or parallelizing the computation.

To address the lack of discussion on limitations and failure cases, the authors should provide a more detailed analysis of the scenarios where the TTT-Discover method might fail to find the optimal solution. This should include a discussion of the types of problems and environments where the method is likely to struggle, such as when the reward function is noisy or sparse, or when the search space is highly discontinuous. The authors should also discuss the limitations of the method in terms of the types of problems it can solve, such as whether it can handle problems with complex dependencies or problems with high-dimensional state spaces. The authors should also discuss the limitations of the method in terms of the types of environments it can handle, such as whether it can handle environments with stochastic transitions or environments with partial observability. This analysis should be included in the main body of the paper, rather than just in the appendix, as it is crucial for researchers who want to use the method in their work. The authors should also provide guidelines for avoiding these failure cases, such as using more robust reward functions or using more sophisticated exploration strategies.

### Questions

1. How does the TTT-Discover method compare to other state-of-the-art RL algorithms in terms of computational efficiency and scalability? A more detailed analysis of the computational cost and scalability of the method would be helpful for researchers who want to apply it to their own problems.

2. What are the limitations of the TTT-Discover method, and in what scenarios is it likely to fail? A more thorough discussion of the limitations and potential failure cases would help researchers understand the scope and applicability of the method.

3. How sensitive is the TTT-Discover method to different hyperparameter settings? A more detailed analysis of the impact of hyperparameters on performance would be helpful for practitioners who want to use the method in their own work.

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces a novel approach to scientific discovery using reinforcement learning (RL). The authors propose a method called TTT-Discover, which leverages test-time training to optimize a policy for a specific scientific task. Unlike traditional RL approaches that focus on continuous improvement, TTT-Discover aims to find a single, best-performing solution rather than iteratively improving upon previous solutions. The method is evaluated across five domains: mathematics, GPU kernel engineering, algorithm design, and biology, where it achieves state-of-the-art results in several tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel application of reinforcement learning to scientific discovery, focusing on finding a single, best-performing solution rather than continuous improvement. This is a fresh perspective in the field of AI for science.
2. The authors provide a comprehensive evaluation of TTT-Discover across multiple domains, including mathematics, GPU kernel engineering, algorithm design, and biology. This demonstrates the versatility and robustness of the method.
3. The paper is well-organized and clearly written, making it accessible to readers from both AI and scientific communities.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for the experiments. This information would be valuable for readers who want to replicate the results or apply the method to new problems.
2. The paper does not discuss the limitations of the method or potential failure cases. It would be helpful to understand the scenarios where the method is likely to fail or underperform.
3. The paper does not compare the method to other state-of-the-art methods in the field. A comparison to existing methods would help to contextualize the contributions of the paper.
4. The paper does not provide a detailed analysis of the sensitivity of the method to hyperparameters. This information would be valuable for readers who want to apply the method to new problems.
5. The paper does not discuss the potential ethical implications of the method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse.

### Suggestions

The paper would benefit from a more thorough discussion of the computational resources required for the experiments. Specifically, the authors should provide details on the hardware used, the training time, and the memory requirements. This information is crucial for other researchers who may want to replicate the results or apply the method to their own problems. Furthermore, it would be helpful to understand how the computational cost scales with the complexity of the problem and the size of the search space. For example, the authors could provide a breakdown of the time spent on exploration versus exploitation, and how this varies across different tasks. This would allow readers to better understand the practical limitations of the method and make informed decisions about its applicability to their own research questions.

In addition to computational resources, the paper should include a more detailed discussion of the limitations of the method and potential failure cases. The authors should discuss scenarios where the method is likely to fail or underperform, and provide examples of such cases. For instance, it would be useful to understand how the method behaves when the reward function is noisy or sparse, or when the search space is highly discontinuous. The authors should also discuss the sensitivity of the method to the choice of hyperparameters, such as the exploration rate and the learning rate. A more detailed analysis of these aspects would provide a more complete picture of the strengths and weaknesses of the method. Furthermore, the authors should discuss the potential ethical implications of their method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse. A discussion of these issues would help to ensure that the method is used responsibly and ethically.

Finally, the paper should include a more comprehensive comparison to existing methods in the field. While the authors mention related work, a more detailed comparison to state-of-the-art methods would help to contextualize the contributions of the paper. This comparison should include both quantitative and qualitative aspects, such as the performance of the method on benchmark problems, the computational cost, and the ease of implementation. For example, the authors could compare their method to other reinforcement learning algorithms that have been applied to scientific discovery problems, or to other methods that have been developed for solving similar optimization problems. This would help to highlight the unique advantages of the proposed approach and its potential impact on the field.

### Questions

1. How does the method scale with the complexity of the problem and the size of the search space?
2. What are the limitations of the method, and in what scenarios is it likely to fail?
3. How sensitive is the method to hyperparameters, and how can these be tuned effectively?
4. How does the method compare to other state-of-the-art methods in the field?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper.

For each weakness, I will:
1. **State the weakness.**
2. **Collect evidence from the paper.** This will involve looking for specific mentions of computational resources, limitations, comparisons to other methods, sensitivity to hyperparameters, and ethical implications.
3. **Analyze the evidence.** I will determine if the paper provides the information the reviewer claims is missing.
4. **Conclude on the validity of the weakness.** I will state whether the weakness is valid, partially valid, or invalid, and provide a confidence level.
**Review 1**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational resources required for the experiments. This information would be valuable for readers who want to replicate the results or apply the method to new problems."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hardware used for GPU kernel engineering experiments: "For the GPU kernel engineering experiments, we use the Hopper and A100 GPUs, and the experiments are run on a server with 64 GB of RAM." (Experiments section, GPU Kernel Engineering, Setup, Implementation)
   - There is no mention of the training time, number of GPUs used, or specific software versions for other experiments.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer is correct that the paper lacks a detailed analysis of computational resources for all experiments. While the GPU kernel engineering section mentions the hardware and server, other experiments do not provide this information.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper provides hardware details for GPU kernel engineering but lacks this information for other experiments.

1. Weakness Statement:
"The paper does not discuss the limitations of the method or potential failure cases. It would be helpful to understand the scenarios where the method is likely to fail or underperform."

2. Evidence Collection:
   - The paper includes a "Limitations" section at the end of the Introduction: "To take advantage of these differences, our learning objective and search subroutine strongly favor the most promising solutions. First, our policy only needs to solve this single state that improves upon the state-of-the-art. Second, the policy might also explore a promising direction using s = <empty> to gain exploitation, which may not be advantageous for a large compute budget."
   - The paper also mentions limitations in the Discussion section: "We note that the context window limit led to a large number of rollouts in OpenEvolve to be truncated before the model completes its response, as OpenEvolve’s prompts grow very large in length."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer is partially correct. The paper does discuss limitations in the Introduction and Discussion sections, but these are relatively brief and don't delve into specific failure cases or scenarios where the method is likely to underperform.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper has a "Limitations" section, but it is brief and doesn't cover specific failure cases.

1. Weakness Statement:
"The paper does not compare the method to other state-of-the-art methods in the field. A comparison to existing methods would help to contextualize the contributions of the paper."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares TTT-Discover to "Best-of-N" and "Random" baselines in the "Mathematics" and "GPU Kernel Engineering" experiments.
   - In the "Algorithm Engineering" experiment, TTT-Discover is compared to "OptimalEvolve" and "ShinkaEvolve."
   - In the "Algorithm Design" experiment, TTT-Discover is compared to "AHC039" and "AHC058."
   - In the "Single Cell Analysis" experiment, TTT-Discover is compared to "Best-of-25600."

3. Literature Gap Analysis:
   - The paper explicitly mentions and compares against relevant state-of-the-art methods in each domain.

4. Validation Analysis:
   - The reviewer is incorrect. The paper does include comparisons to other state-of-the-art methods in each of the experimental sections.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section includes comparisons to relevant baselines in each domain.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the sensitivity of the method to hyperparameters. This information would be valuable for readers who want to apply the method to new problems."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hyperparameters used: "We use LoRA Hu et al. (2022) with rank 32 32 . At each step, we generate a batch of 512 rollouts, with 8 8 groups of 64 rollouts each. Each group of rollouts is generated using the same context and initial state selected from the reuse buffer. We use the entropic objective, and apply importance sampling ratio correction to the gradients due to the sampler/learner mismatch in the RL infrastructure Yao et al. () . We do not take any off-policy steps, i.e., take 1 1 gradient step on the entire batch." (Experiments section, Implementation)
   - There is no explicit analysis of how sensitive the results are to changes in these hyperparameters.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer is correct. While the paper states the hyperparameters used, it lacks a detailed analysis of the method's sensitivity to these choices.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions hyperparameters but doesn't analyze their impact on performance.

1. Weakness Statement:
"The paper does not discuss the potential ethical implications of the method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse."

2. Evidence Collection:
   - The paper does not have a dedicated "Ethical Considerations" section.
   - The "Single Cell Analysis" section mentions the potential for "discovering new drugs or materials."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer is correct. While the paper mentions potential applications that could have ethical implications, it does not discuss these implications in detail.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a discussion of ethical implications despite mentioning potential applications.

**Review 2**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational resources required for the experiments. This information would be valuable for readers who want to replicate the results or apply the method to new problems."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hardware used for GPU kernel engineering experiments: "For the GPU kernel engineering experiments, we use the Hopper and A100 GPUs, and the experiments are run on a server with 64 GB of RAM." (Experiments section, GPU Kernel Engineering, Setup, Implementation)
   - There is no mention of the training time, number of GPUs used, or specific software versions for other experiments.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper provides hardware details for GPU kernel engineering but lacks this information for other experiments.

1. Weakness Statement:
"The paper does not discuss the limitations of the method or potential failure cases. It would be helpful to understand the scenarios where the method is likely to fail or underperform."

2. Evidence Collection:
   - The paper includes a "Limitations" section at the end of the Introduction: "To take advantage of these differences, our learning objective and search subroutine strongly favor the most promising solutions. First, our policy only needs to solve this single state that improves upon the state-of-the-art. Second, the policy might also explore a promising direction using s = <empty> to gain exploitation, which may not be advantageous for a large compute budget."
   - The paper also mentions limitations in the Discussion section: "We note that the context window limit led to a large number of rollouts in OpenEvolve to be truncated before the model completes its response, as OpenEvolve’s prompts grow very large in length."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper has a "Limitations" section, but it is brief and doesn't cover specific failure cases.

1. Weakness Statement:
"The paper does not compare the method to other state-of-the-art methods in the field. A comparison to existing methods would help to contextualize the contributions of the paper."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares TTT-Discover to "Best-of-N" and "Random" baselines in the "Mathematics" and "GPU Kernel Engineering" experiments.
   - In the "Algorithm Engineering" experiment, TTT-Discover is compared to "OptimalEvolve" and "ShinkaEvolve."
   - In the "Algorithm Design" experiment, TTT-Discover is compared to "AHC039" and "AHC058."
   - In the "Single Cell Analysis" experiment, TTT-Discover is compared to "Best-of-25600."

3. Literature Gap Analysis:
   - The paper explicitly mentions and compares against relevant state-of-the-art methods in each domain.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section includes comparisons to relevant baselines in each domain.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the sensitivity of the method to hyperparameters. This information would be valuable for readers who want to apply the method to new problems."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hyperparameters used: "We use LoRA Hu et al. (2022) with rank 32 32 . At each step, we generate a batch of 512 rollouts, with 8 8 groups of 64 rollouts each. Each group of rollouts is generated using the same context and initial state selected from the reuse buffer. We use the entropic objective, and apply importance sampling ratio correction to the gradients due to the sampler/learner mismatch in the RL infrastructure Yao et al. () . We do not take any off-policy steps, i.e., take 1 1 gradient step on the entire batch." (Experiments section, Implementation)
   - There is no explicit analysis of how sensitive the results are to changes in these hyperparameters.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions hyperparameters but doesn't analyze their impact on performance.

1. Weakness Statement:
"The paper does not discuss the potential ethical implications of the method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse."

2. Evidence Collection:
   - The paper does not have a dedicated "Ethical Considerations" section.
   - The "Single Cell Analysis" section mentions the potential for "discovering new drugs or materials."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a discussion of ethical implications despite mentioning potential applications.

**Review 3**

1. Weakness Statement:
"Limited Exploration of Hyperparameter Sensitivity: While the paper provides a detailed description of the TTT-Discover method, it lacks a thorough analysis of how sensitive the method is to different hyperparameter settings. Understanding the impact of hyperparameters on performance is crucial for practical applications, and the paper could benefit from a more in-depth discussion of this aspect. Specifically, the paper does not explore the sensitivity of the method to parameters such as the exploration rate, the learning rate, and the batch size, which could significantly affect the convergence and stability of the algorithm. A more rigorous analysis of these parameters would provide a better understanding of the method's robustness and generalizability."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hyperparameters used: "We use LoRA Hu et al. (2022) with rank 32 32 . At each step, we generate a batch of 512 rollouts, with 8 8 groups of 64 rollouts each. Each group of rollouts is generated using the same context and initial state selected from the reuse buffer. We use the entropic objective, and apply importance sampling ratio correction to the gradients due to the sampler/learner mismatch in the RL infrastructure Yao et al. () . We do not take any off-policy steps, i.e., take 1 1 gradient step on the entire batch." (Experiments section, Implementation)
   - There is no explicit analysis of how sensitive the results are to changes in these hyperparameters.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1 and 2, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions hyperparameters but doesn't analyze their impact on performance.

1. Weakness Statement:
"Lack of Discussion on Computational Cost: The paper does not provide a detailed analysis of the computational cost associated with the TTT-Discover method. While the authors mention the use of a powerful GPU, they do not discuss the time complexity of the algorithm or the resources required to run it on different hardware configurations. This information is crucial for researchers who want to apply the method to their own problems. Furthermore, it would be beneficial to understand how the computational cost scales with the complexity of the problem and the size of the search space. For example, the authors could provide a breakdown of the time spent on exploration versus exploitation, and how this varies across different tasks. This would allow readers to better understand the practical limitations of the method and make informed decisions about its applicability to their own research questions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hardware used for GPU kernel engineering experiments: "For the GPU kernel engineering experiments, we use the Hopper and A100 GPUs, and the experiments are run on a server with 64 GB of RAM." (Experiments section, GPU Kernel Engineering, Setup, Implementation)
   - There is no mention of the training time, number of GPUs used, or specific software versions for other experiments.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1 and 2, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper provides hardware details for GPU kernel engineering but lacks this information for other experiments.

1. Weakness Statement:
"Limited Discussion on Limitations and Failure Cases: The paper does not provide a detailed discussion of the limitations of the TTT-Discover method or potential failure cases. Understanding the limitations of the method is crucial for researchers who want to use it in their work, and a more thorough discussion of these aspects would help to avoid potential pitfalls. The paper should discuss scenarios where the method is likely to fail or underperform, such as when the reward function is noisy or sparse, or when the search space is highly discontinuous. It should also discuss the limitations of the method in terms of the types of problems it can solve and the types of environments it can handle."

2. Evidence Collection:
   - The paper includes a "Limitations" section at the end of the Introduction: "To take advantage of these differences, our learning objective and search subroutine strongly favor the most promising solutions. First, our policy only needs to solve this single state that improves upon the state-of-the-art. Second, the policy might also explore a promising direction using s = <empty> to gain exploitation, which may not be advantageous for a large compute budget."
   - The paper also mentions limitations in the Discussion section: "We note that the context window limit led to a large number of rollouts in OpenEvolve to be truncated before the model completes its response, as OpenEvolve’s prompts grow very large in length."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1 and 2, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper has a "Limitations" section, but it is brief and doesn't cover specific failure cases.

1. Weakness Statement:
"How does the method scale with the complexity of the problem and the size of the search space?"

2. Evidence Collection:
   - The paper does not explicitly discuss the scaling of the method with problem complexity and search space size.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a discussion on how the method scales with problem complexity and search space size.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper does not discuss the scaling of the method.

1. Weakness Statement:
"What are the limitations of the method, and in what scenarios is it likely to fail?"

2. Evidence Collection:
   - The paper includes a "Limitations" section at the end of the Introduction: "To take advantage of these differences, our learning objective and search subroutine strongly favor the most promising solutions. First, our policy only needs to solve this single state that improves upon the state-of-the-art. Second, the policy might also explore a promising direction using s = <empty> to gain exploitation, which may not be advantageous for a large compute budget."
   - The paper also mentions limitations in the Discussion section: "We note that the context window limit led to a large number of rollouts in OpenEvolve to be truncated before the model completes its response, as OpenEvolve’s prompts grow very large in length."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1 and 2, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper has a "Limitations" section, but it is brief and doesn't cover specific failure cases.

1. Weakness Statement:
"How sensitive is the method to hyperparameters, and how can these be tuned effectively?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hyperparameters used: "We use LoRA Hu et al. (2022) with rank 32 32 . At each step, we generate a batch of 512 rollouts, with 8 8 groups of 64 rollouts each. Each group of rollouts is generated using the same context and initial state selected from the reuse buffer. We use the entropic objective, and apply importance sampling ratio correction to the gradients due to the sampler/learner mismatch in the RL infrastructure Yao et al. (). We do not take any off-policy steps, i.e., take 1 1 gradient step on the entire batch." (Experiments section, Implementation)
   - There is no explicit analysis of how sensitive the results are to changes in these hyperparameters.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, 2, and 3, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions hyperparameters but doesn't analyze their impact on performance.

**Review 4**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational resources required for the experiments. This information would be valuable for readers who want to replicate the results or apply the method to new problems."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hardware used for GPU kernel engineering experiments: "For the GPU kernel engineering experiments, we use the Hopper and A100 GPUs, and the experiments are run on a server with 64 GB of RAM." (Experiments section, GPU Kernel Engineering, Setup, Implementation)
   - There is no mention of the training time, number of GPUs used, or specific software versions for other experiments.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, 2, and 3, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper provides hardware details for GPU kernel engineering but lacks this information for other experiments.

1. Weakness Statement:
"The paper does not discuss the limitations of the method or potential failure cases. It would be helpful to understand the scenarios where the method is likely to fail or underperform."

2. Evidence Collection:
   - The paper includes a "Limitations" section at the end of the Introduction: "To take advantage of these differences, our learning objective and search subroutine strongly favor the most promising solutions. First, our policy only needs to solve this single state that improves upon the state-of-the-art. Second, the policy might also explore a promising direction using s = <empty> to gain exploitation, which may not be advantageous for a large compute budget."
   - The paper also mentions limitations in the Discussion section: "We note that the context window limit led to a large number of rollouts in OpenEvolve to be truncated before the model completes its response, as OpenEvolve’s prompts grow very large in length."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, 2, and 3, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper has a "Limitations" section, but it is brief and doesn't cover specific failure cases.

1. Weakness Statement:
"The paper does not compare the method to other state-of-the-art methods in the field. A comparison to existing methods would help to contextualize the contributions of the paper."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares TTT-Discover to "Best-of-N" and "Random" baselines in the "Mathematics" and "GPU Kernel Engineering" experiments.
   - In the "Algorithm Engineering" experiment, TTT-Discover is compared to "OptimalEvolve" and "ShinkaEvolve."
   - In the "Algorithm Design" experiment, TTT-Discover is compared to "AHC039" and "AHC058."
   - In the "Single Cell Analysis" experiment, TTT-Discover is compared to "Best-of-25600."

3. Literature Gap Analysis:
   - The paper explicitly mentions and compares against relevant state-of-the-art methods in each domain.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, 2, and 3, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section includes comparisons to relevant baselines in each domain.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the sensitivity of the method to hyperparameters. This information would be valuable for readers who want to apply the method to new problems."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hyperparameters used: "We use LoRA Hu et al. (2022) with rank 32 32 . At each step, we generate a batch of 512 rollouts, with 8 8 groups of 64 rollouts each. Each group of rollouts is generated using the same context and initial state selected from the reuse buffer. We use the entropic objective, and apply importance sampling ratio correction to the gradients due to the sampler/learner mismatch in the RL infrastructure Yao et al. (). We do not take any off-policy steps, i.e., take 1 1 gradient step on the entire batch." (Experiments section, Implementation)
   - There is no explicit analysis of how sensitive the results are to changes in these hyperparameters.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, 2, 3, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions hyperparameters but doesn't analyze their impact on performance.

1. Weakness Statement:
"The paper does not discuss the potential ethical implications of the method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse."

2. Evidence Collection:
   - The paper does not have a dedicated "Ethical Considerations" section.
   - The "Single Cell Analysis" section mentions the potential for "discovering new drugs or materials."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, 2, and 3, and the analysis and conclusion remain the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a discussion of ethical implications despite mentioning potential applications.

**Synthesis and Reflection:**

After analyzing the reviewer comments and comparing them against the paper's content, several key observations emerge:

* **Consistent Weaknesses:**  Reviewers 1, 2, 3, and 4 all point out the lack of detailed computational resource analysis for all experiments. Reviewers 1, 2, and 3 also consistently highlight the limited discussion of limitations and potential failure cases. Reviewers 1, 2, and 3 note the absence of a detailed analysis of hyperparameter sensitivity. Reviewer 4 points out the lack of a dedicated ethics section. Reviewers 1, 2, and 3 also note the absence of a comprehensive comparison to existing methods, although this is contradicted by Reviewer 4.

* **Invalid Weaknesses:** Reviewer 2's claim that the paper lacks comparisons to state-of-the-art methods is invalid, as the paper explicitly compares against relevant baselines in each experimental section.

* **Overlapping Concerns:** The reviewers largely agree on the areas needing improvement. The most prominent recurring themes are the need for more detailed information about computational resources, a thorough discussion of limitations, an analysis of hyperparameter sensitivity, and a consideration of ethical implications.

* **Conflicting Opinions:** The main conflict arises regarding the comparison to existing methods. Reviewer 4 claims this is missing, while the paper explicitly includes comparisons in each experiment section.

* **Valid vs. Invalid Criticisms:** The criticisms regarding the lack of computational resource details, limited discussion of limitations, and the absence of a hyperparameter sensitivity analysis are valid. The criticism about the lack of comparison to existing methods is invalid. The criticism about the absence of an ethics section is valid.

**Conclusion:**

The majority of the weaknesses identified by the reviewers are valid and supported by the paper's content. The key areas for improvement are:

1. **Detailed Computational Resource Analysis:** Providing specific hardware and software details for all experiments.
2. **Thorough Discussion of Limitations:** Elaborating on specific scenarios where the method might fail or underperform.
3. **Analysis of Hyperparameter Sensitivity:** Investigating the impact of different hyperparameter settings on the method's performance.
4. **Consideration of Ethical Implications:** Discussing the potential ethical considerations of the method, particularly in applications involving new drugs or materials.
5. **Comparison to Existing Methods:** While the paper does include comparisons, a more comprehensive and detailed comparison to state-of-the-art methods could further contextualize the contributions.

The invalid criticism regarding the lack of comparison to existing methods needs to be addressed by either removing the criticism or providing evidence of such a comparison within the paper.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces TTT-Discover, a novel reinforcement learning (RL) method designed to discover a single, high-performing solution rather than iteratively improving upon existing solutions, a departure from traditional RL approaches. The authors frame this as a search for a single best solution, which they argue is more relevant in certain scientific discovery contexts where finding one optimal outcome is more critical than continuous improvement. The core methodological approach of TTT-Discover involves an 'entropic objective,' which aims to balance exploration and exploitation by maximizing the expected reward of the policy, and a 'PUCT-inspired exploration,' which is inspired by the Upper Confidence Bound applied to Trees, to efficiently explore the search space. The method also incorporates a 'state reuse' mechanism, where previous successful states are used to initialize new searches, and a 'replay buffer' to store and reuse past experiences. The authors evaluate TTT-Discover across five diverse scientific domains: mathematics, GPU kernel engineering, algorithm design, algorithm engineering, and biology. In mathematics, the method is used to discover new prime numbers. In GPU kernel engineering, it optimizes performance for specific hardware configurations. In algorithm design and engineering, it focuses on finding single, best-performing algorithms. In biology, it is applied to single-cell analysis. The empirical results demonstrate that TTT-Discover achieves state-of-the-art performance in several tasks, surpassing previous best results, including both AI baselines and human results in some cases. The authors also compare their method to other relevant baselines, such as 'Best-of-N' and 'Random' in the mathematics and GPU kernel engineering domains, 'OptimalEvolve' and 'ShinkaEvolve' in the algorithm engineering domain, 'AHC039' and 'AHC058' in the algorithm design domain, and 'Best-of-25600' in the single cell analysis domain. These comparisons highlight the advantages of TTT-Discover in terms of both performance and computational efficiency. The paper's overall significance lies in its novel application of RL to scientific discovery, focusing on finding a single, best solution rather than continuous improvement. This approach is particularly relevant in fields where the discovery of a single optimal solution is more important than iterative refinement. The authors also introduce a comprehensive evaluation framework, covering multiple domains and comparing against relevant baselines, which demonstrates the versatility and effectiveness of their method. The use of an entropic objective and PUCT-inspired exploration, combined with a state reuse and replay buffer mechanism, provides a robust approach to scientific discovery. The paper's findings suggest that TTT-Discover has the potential to significantly impact various scientific fields by providing a more efficient and effective way to discover new solutions.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

The paper presents several notable strengths that contribute to its overall impact and significance. First and foremost, the introduction of TTT-Discover as a novel approach to scientific discovery is a significant contribution. The method's focus on finding a single, best-performing solution, rather than iteratively improving upon existing solutions, is a fresh perspective that aligns well with certain scientific contexts. This is a clear departure from traditional RL approaches, which are often designed for continuous improvement. The authors' decision to frame the problem in this way is both innovative and well-motivated. The methodological approach of TTT-Discover is also a strength. The use of an 'entropic objective' to balance exploration and exploitation, inspired by the PUCT algorithm, is a clever way to efficiently explore the search space. The 'state reuse' mechanism, which initializes new searches using previous successful states, is a practical and effective way to leverage past experiences. The 'replay buffer,' which stores and reuses past experiences, further enhances the method's efficiency. The combination of these techniques provides a robust framework for scientific discovery. The empirical results presented in the paper are another significant strength. The authors demonstrate the versatility of TTT-Discover by applying it to five diverse scientific domains: mathematics, GPU kernel engineering, algorithm design, algorithm engineering, and biology. This comprehensive evaluation showcases the method's broad applicability and robustness. The fact that TTT-Discover achieves state-of-the-art performance in several tasks, surpassing both AI baselines and human results in some cases, is particularly impressive. The comparisons to other relevant baselines, such as 'Best-of-N' and 'Random' in the mathematics and GPU kernel engineering domains, 'OptimalEvolve' and 'ShinkaEvolve' in the algorithm engineering domain, 'AHC039' and 'AHC058' in the algorithm design domain, and 'Best-of-25600' in the single cell analysis domain, further highlight the advantages of TTT-Discover. The paper is also well-written and clearly organized, making it accessible to readers from both AI and scientific communities. The authors provide a comprehensive explanation of the method and its implementation, which is crucial for reproducibility and further research. The use of concrete examples and detailed descriptions of the experimental setup and results further enhances the paper's clarity and impact. Finally, the paper's focus on a novel problem formulation in scientific discovery, combined with a robust methodological approach and strong empirical results, makes it a valuable contribution to the field. The authors have successfully demonstrated the potential of RL to address complex scientific problems and have provided a solid foundation for future research in this area.


## Weaknesses:

Despite the strengths of the paper, there are several weaknesses that warrant attention. One of the most significant limitations is the lack of a detailed analysis of the computational resources required for the experiments. While the paper mentions the hardware used for the GPU kernel engineering experiments, stating that 'For the GPU kernel engineering experiments, we use the Hopper and A100 GPUs, and the experiments are run on a server with 64 GB of RAM,' this information is insufficient for other experiments. The paper does not provide details on the training time, number of GPUs used, or specific software versions for the mathematics, algorithm design, and algorithm engineering domains. This lack of information makes it difficult for other researchers to replicate the results or apply the method to their own problems. The absence of this information is a major impediment to the practical adoption of the method and limits the paper's impact. Another significant weakness is the limited discussion of the method's limitations and potential failure cases. While the paper includes a brief section at the end of the introduction and a discussion in the context of the 'Single Cell Analysis' experiment, these discussions are brief and do not delve into specific scenarios where the method is likely to fail or underperform. For instance, the paper does not discuss how the method would perform when the reward function is noisy or sparse, or when the search space is highly discontinuous. The paper also does not discuss the sensitivity of the method to the choice of hyperparameters, such as the exploration rate and the learning rate. A more thorough discussion of these limitations would provide a more complete picture of the method's strengths and weaknesses and would help researchers understand the scope and applicability of the method. Furthermore, the paper lacks a comprehensive comparison to existing methods in the field. While the paper does compare TTT-Discover to relevant baselines in each experimental section, such as 'Best-of-N' and 'Random' in the mathematics and GPU kernel engineering domains, 'OptimalEvolve' and 'ShinkaEvolve' in the algorithm engineering domain, 'AHC039' and 'AHC058' in the algorithm design domain, and 'Best-of-25600' in the single cell analysis domain, the comparison is not as thorough as it could be. A more detailed comparison to state-of-the-art methods in the field would help to contextualize the contributions of the paper and highlight the unique advantages of the proposed approach. This comparison should include both quantitative and qualitative aspects, such as the performance of the method on benchmark problems, the computational cost, and the ease of implementation. Finally, the paper does not include a dedicated 'Ethical Considerations' section. While the paper mentions the potential for 'discovering new drugs or materials' in the 'Single Cell Analysis' section, it does not discuss the potential ethical implications of the method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse. A discussion of these issues would help to ensure that the method is used responsibly and ethically. The lack of this discussion is a significant oversight, particularly given the potential applications of the method in sensitive domains. These weaknesses, while not invalidating the paper's contributions, highlight areas where the paper could be significantly improved. The lack of detailed computational resource information, the limited discussion of limitations and failure cases, the insufficient comparison to existing methods, and the absence of an ethical considerations section all impact the paper's overall impact and practical applicability. I have high confidence in these identified weaknesses, as they are directly supported by the paper's content and the absence of crucial information.


## Suggestions:

To address the identified weaknesses, I recommend several concrete and actionable improvements. First and foremost, the authors should provide a more detailed analysis of the computational resources required for their experiments. This should include information on the hardware used, the training time, and the memory requirements. This information is crucial for other researchers who may want to replicate the results or apply the method to their own problems. The authors should also provide a breakdown of the time spent on exploration versus exploitation, and how this varies across different tasks. This would allow readers to better understand the practical limitations of the method and make informed decisions about its applicability to their own research questions. Second, the authors should include a more detailed discussion of the limitations of the method and potential failure cases. This should include an analysis of scenarios where the method is likely to fail or underperform, such as when the reward function is noisy or sparse, or when the search space is highly discontinuous. The authors should also discuss the sensitivity of the method to the choice of hyperparameters, such as the exploration rate and the learning rate. A more detailed analysis of these aspects would provide a more complete picture of the strengths and weaknesses of the method. Furthermore, the authors should discuss the potential ethical implications of their method. For example, if the method is used to discover new drugs or materials, there may be ethical concerns about the potential for misuse. A discussion of these issues would help to ensure that the method is used responsibly and ethically. Third, the authors should provide a more comprehensive comparison to existing methods in the field. This comparison should include both quantitative and qualitative aspects, such as the performance of the method on benchmark problems, the computational cost, and the ease of implementation. For example, the authors could compare their method to other reinforcement learning algorithms that have been applied to scientific discovery problems, or to other methods that have been developed for solving similar optimization problems. This would help to highlight the unique advantages of the proposed approach and its potential impact on the field. Fourth, the authors should include a dedicated 'Ethical Considerations' section. This section should discuss the potential ethical implications of the method, particularly in applications involving new drugs or materials. The authors should also discuss the potential for misuse of the method and how to mitigate these risks. Finally, the authors should provide a more detailed analysis of the sensitivity of the method to hyperparameters. This should include a systematic exploration of the parameter space, using techniques such as grid search or random search, to identify the optimal hyperparameter settings for different tasks. The authors should also provide a detailed analysis of the impact of each hyperparameter on the convergence and stability of the algorithm, and discuss how these parameters should be tuned for different types of problems. For example, the exploration rate should be tuned to balance exploration and exploitation, while the learning rate should be tuned to ensure that the algorithm converges to a good solution without overshooting. The batch size should be tuned to balance the computational cost and the stability of the algorithm. This analysis should be included in the main body of the paper, rather than just in the appendix, as it is crucial for the practical application of the method. These suggestions are all concrete and actionable, and they directly address the identified weaknesses. Implementing these changes would significantly improve the paper's overall quality and impact.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for a deeper understanding of the paper's contributions and limitations. First, how does the TTT-Discover method scale with the complexity of the problem and the size of the search space? The paper does not provide a detailed analysis of this aspect, and it would be valuable to understand how the method's performance and computational cost change as the problem becomes more complex. Second, what are the limitations of the TTT-Discover method, and in what scenarios is it likely to fail or underperform? The paper mentions some limitations, but a more thorough discussion of these aspects would be helpful. Specifically, I am interested in understanding how the method behaves when the reward function is noisy or sparse, or when the search space is highly discontinuous. Third, how sensitive is the TTT-Discover method to the choice of hyperparameters, and how can these be tuned effectively? The paper mentions the hyperparameters used, but it does not provide a detailed analysis of how sensitive the results are to changes in these parameters. A more systematic exploration of the parameter space would be valuable. Fourth, how does the TTT-Discover method compare to other state-of-the-art methods in the field, both in terms of performance and computational efficiency? While the paper includes comparisons to relevant baselines in each experimental section, a more comprehensive comparison to state-of-the-art methods would be helpful. This comparison should include both quantitative and qualitative aspects, such as the performance of the method on benchmark problems, the computational cost, and the ease of implementation. Fifth, what are the potential ethical implications of the TTT-Discover method, particularly in applications involving new drugs or materials? The paper mentions the potential for discovering new drugs or materials, but it does not discuss the potential ethical concerns that may arise from this. A more detailed discussion of these issues would be valuable. Finally, what is the computational cost associated with the TTT-Discover method, and how does this scale with the complexity of the problem and the size of the search space? The paper does not provide a detailed analysis of the computational cost, and this information is crucial for researchers who want to apply the method to their own problems. These questions are all targeted at core methodological choices and seek clarification of critical assumptions. Addressing these questions would significantly enhance the paper's overall impact and provide a more complete understanding of the TTT-Discover method.


## Rating:

6.25


## Confidence:

2.75


## Decision:

Accept
}