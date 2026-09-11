I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes QWM (Q-Learning with World Models), a novel framework that leverages world models for test-time action selection in online reinforcement learning. Unlike previous approaches that use world models for policy or value function optimization, QWM uses the world model solely for generating imagined rollouts during online interaction. These rollouts are then used in a tree search procedure to select the best action for execution in the environment, while the policy and Q-function are trained using standard Q-learning on real transitions. This approach allows QWM to avoid compounding model bias, which is a common issue in model-based RL methods. The authors evaluate QWM on challenging manipulation benchmarks, Robomimic and LIBERO, and demonstrate that it outperforms strong model-free baselines in both sample efficiency and performance. They also show that QWM can be implemented on top of different base algorithms, such as EXPO and RLPD, providing a versatile framework for improving online RL performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a relevant and challenging problem in reinforcement learning, particularly the issue of compounding bias in model-based approaches. The proposed method, QWM, offers a novel and effective way to leverage world models for test-time action selection without compromising the sample efficiency of model-free algorithms.
- The authors provide a thorough evaluation of QWM on challenging manipulation benchmarks, demonstrating its superiority over strong model-free baselines. The results are compelling and show that QWM can achieve better performance with fewer samples.
- The paper is well-written and easy to follow, with clear explanations of the proposed method and its implementation. The authors also provide a detailed ablation study, which helps to understand the importance of different components of QWM.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on manipulation tasks with sparse rewards. It would be beneficial to evaluate QWM on a wider range of tasks with more complex dynamics and reward structures to demonstrate its generalizability.
- The computational overhead of the tree search procedure is not thoroughly analyzed. While the authors mention that the policy and Q-function are trained on real transitions, the search process itself can be computationally expensive, especially for long-horizon tasks or high-dimensional state spaces. A detailed analysis of the computational cost and scalability of QWM would be valuable.
- The paper does not explore the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies on the quality of the imagined rollouts, and it would be important to understand how the method behaves when the world model is imperfect or inaccurate. An analysis of the robustness of QWM to model errors would strengthen the paper.

### Suggestions

The authors should consider expanding their evaluation to include tasks with more complex dynamics and reward structures. While the manipulation tasks used in the paper are challenging, they may not fully represent the diversity of problems where world models are applicable. For example, evaluating QWM on tasks with sparse rewards that require long-term planning, or tasks with high-dimensional state spaces and complex dynamics, would provide a more comprehensive assessment of its capabilities. This could involve incorporating tasks from other domains, such as navigation or robotics, to demonstrate the generalizability of the proposed method. Furthermore, it would be beneficial to explore the performance of QWM in scenarios with partial observability, which is a common challenge in real-world applications. This would help to understand the limitations of the approach and identify potential areas for improvement.

A more detailed analysis of the computational cost and scalability of QWM is also needed. The tree search procedure, while avoiding model bias, can introduce significant computational overhead, especially for tasks with long horizons or high-dimensional state spaces. The authors should provide a breakdown of the computational cost associated with different components of QWM, such as the world model prediction, the tree search, and the policy and Q-function updates. This analysis should also consider the impact of different hyperparameters, such as the tree depth and the number of rollouts, on the computational cost. Furthermore, it would be valuable to explore techniques for reducing the computational overhead of QWM, such as using more efficient search algorithms or pruning strategies. This would make the method more practical for real-world applications with limited computational resources.

Finally, the authors should investigate the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies heavily on the quality of the imagined rollouts, and it is crucial to understand how the method behaves when the world model is imperfect or inaccurate. The authors could explore the impact of different world model architectures and training procedures on the performance of QWM. They could also investigate techniques for improving the robustness of QWM to model errors, such as using ensemble methods or incorporating uncertainty estimates into the search procedure. This would provide a more complete understanding of the limitations of the approach and identify potential areas for future research.

### Questions

- How does QWM perform on tasks with dense rewards or continuous action spaces?
- What is the computational overhead of the tree search procedure compared to standard Q-learning?
- How sensitive is QWM to the accuracy of the world model? Are there any techniques to mitigate the impact of model inaccuracies?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

The paper introduces a novel framework called QWM (Q-Learning with World Models) that leverages world models for test-time action selection in online reinforcement learning. Unlike previous approaches that use world models for policy or value function optimization, QWM uses the world model solely for generating imagined rollouts during online interaction. These rollouts are then used in a tree search procedure to select the best action for execution in the environment, while the policy and Q-function are trained using standard Q-learning on real transitions. This approach allows QWM to avoid compounding model bias, which is a common issue in model-based RL methods. The authors evaluate QWM on challenging manipulation benchmarks, Robomimic and LIBERO, and demonstrate that it outperforms strong model-free baselines in both sample efficiency and performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation behind QWM and its implementation. The use of a tree search for test-time action selection is innovative and addresses a key limitation of existing model-based RL methods.

2. The authors provide a thorough evaluation of QWM on challenging manipulation benchmarks, Robomimic and LIBERO. The results demonstrate that QWM outperforms strong model-free baselines in both sample efficiency and performance. The ablation study further helps to understand the importance of different components of QWM.

3. The paper also discusses the limitations of QWM and provides insights into future directions. This shows that the authors are aware of the challenges and are actively working to improve their method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on manipulation tasks with sparse rewards. It would be beneficial to evaluate QWM on a wider range of tasks with more complex dynamics and reward structures to demonstrate its generalizability.

2. The computational overhead of the tree search procedure is not thoroughly analyzed. While the authors mention that the policy and Q-function are trained on real transitions, the search process itself can be computationally expensive, especially for long-horizon tasks or high-dimensional state spaces. A detailed analysis of the computational cost and scalability of QWM would be valuable.

3. The paper does not explore the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies on the quality of the imagined rollouts, and it would be important to understand how the method behaves when the world model is imperfect or inaccurate. An analysis of the robustness of QWM to model errors would strengthen the paper.

### Suggestions

The authors should consider expanding their evaluation to include tasks with more complex dynamics and reward structures. While the manipulation tasks used in the paper are challenging, they may not fully represent the diversity of problems where world models are applicable. For example, evaluating QWM on tasks with sparse rewards that require long-term planning, or tasks with high-dimensional state spaces and complex dynamics, would provide a more comprehensive assessment of its capabilities. This could involve incorporating tasks from other domains, such as navigation or robotics, to demonstrate the generalizability of the proposed method. Furthermore, it would be beneficial to explore the performance of QWM in scenarios with partial observability, which is a common challenge in real-world applications. This would help to understand the limitations of the approach and identify potential areas for improvement.

A more detailed analysis of the computational cost and scalability of QWM is also needed. The tree search procedure, while avoiding model bias, can introduce significant computational overhead, especially for tasks with long horizons or high-dimensional state spaces. The authors should provide a breakdown of the computational cost associated with different components of QWM, such as the world model prediction, the tree search, and the policy and Q-function updates. This analysis should also consider the impact of different hyperparameters, such as the tree depth and the number of rollouts, on the computational cost. Furthermore, it would be valuable to explore techniques for reducing the computational overhead of QWM, such as using more efficient search algorithms or pruning strategies. This would make the method more practical for real-world applications with limited computational resources.

Finally, the authors should investigate the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies heavily on the quality of the imagined rollouts, and it is crucial to understand how the method behaves when the world model is imperfect or inaccurate. The authors could explore the impact of different world model architectures and training procedures on the performance of QWM. They could also investigate techniques for improving the robustness of QWM to model errors, such as using ensemble methods or incorporating uncertainty estimates into the search procedure. This would provide a more complete understanding of the limitations of the approach and identify potential areas for future research.

### Questions

1. How does QWM perform on tasks with dense rewards or continuous action spaces?

2. What is the computational overhead of the tree search procedure compared to standard Q-learning?

3. How sensitive is QWM to the accuracy of the world model? Are there any techniques to mitigate the impact of model inaccuracies?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a novel method, QWM, which leverages world models to improve Q-learning in online RL. QWM uses the world model to generate imagined rollouts for test-time action selection, avoiding the compounding bias of optimizing the policy or value function directly with the world model. The authors evaluate QWM on challenging manipulation benchmarks, Robomimic and LIBERO, and demonstrate its superior performance compared to strong model-free baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a key limitation of model-based RL by using world models for test-time action selection rather than for policy optimization. This approach avoids the compounding bias that often plagues model-based methods.
- The authors provide a thorough evaluation of QWM on challenging manipulation benchmarks, Robomimic and LIBERO, demonstrating its superior performance compared to strong model-free baselines.
- The paper is well-written and easy to follow, with clear explanations of the proposed method and its implementation.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on manipulation tasks with sparse rewards. It would be beneficial to evaluate QWM on a wider range of tasks with more complex dynamics and reward structures to demonstrate its generalizability.
- The computational overhead of the tree search procedure is not thoroughly analyzed. While the authors mention that the policy and Q-function are trained on real transitions, the search process itself can be computationally expensive, especially for long-horizon tasks or high-dimensional state spaces. A detailed analysis of the computational cost and scalability of QWM would be valuable.
- The paper does not explore the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies on the quality of the imagined rollouts, and it would be important to understand how the method behaves when the world model is imperfect or inaccurate. An analysis of the robustness of QWM to model errors would strengthen the paper.

### Suggestions

The authors should consider expanding their evaluation to include tasks with more complex dynamics and reward structures. While the manipulation tasks used in the paper are challenging, they may not fully represent the diversity of problems where world models are applicable. For example, evaluating QWM on tasks with sparse rewards that require long-term planning, or tasks with high-dimensional state spaces and complex dynamics, would provide a more comprehensive assessment of its capabilities. This could involve incorporating tasks from other domains, such as navigation or robotics, to demonstrate the generalizability of the proposed method. Furthermore, it would be beneficial to explore the performance of QWM in scenarios with partial observability, which is a common challenge in real-world applications. This would help to understand the limitations of the approach and identify potential areas for improvement.

A more detailed analysis of the computational cost and scalability of QWM is also needed. The tree search procedure, while avoiding model bias, can introduce significant computational overhead, especially for tasks with long horizons or high-dimensional state spaces. The authors should provide a breakdown of the computational cost associated with different components of QWM, such as the world model prediction, the tree search, and the policy and Q-function updates. This analysis should also consider the impact of different hyperparameters, such as the tree depth and the number of rollouts, on the computational cost. Furthermore, it would be valuable to explore techniques for reducing the computational overhead of QWM, such as using more efficient search algorithms or pruning strategies. This would make the method more practical for real-world applications with limited computational resources.

Finally, the authors should investigate the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies heavily on the quality of the imagined rollouts, and it is crucial to understand how the method behaves when the world model is imperfect or inaccurate. The authors could explore the impact of different world model architectures and training procedures on the performance of QWM. They could also investigate techniques for improving the robustness of QWM to model errors, such as using ensemble methods or incorporating uncertainty estimates into the search procedure. This would provide a more complete understanding of the limitations of the approach and identify potential areas for future research.

### Questions

- How does QWM perform on tasks with dense rewards or continuous action spaces?
- What is the computational overhead of the tree search procedure compared to standard Q-learning?
- How sensitive is QWM to the accuracy of the world model? Are there any techniques to mitigate the impact of model inaccuracies?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper proposes QWM, a framework that leverages world models for test-time action selection in online reinforcement learning. The key idea is to use the world model to generate imagined rollouts for action selection, while the policy and Q-function are trained using standard Q-learning on real transitions. This approach avoids the compounding bias of model-based RL methods. The authors evaluate QWM on challenging manipulation benchmarks, Robomimic and LIBERO, and demonstrate that it outperforms strong model-free baselines in both sample efficiency and performance. The paper also includes an ablation study to analyze the impact of different components of QWM.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a relevant and challenging problem in reinforcement learning, particularly the issue of compounding bias in model-based approaches. The proposed method, QWM, offers a novel and effective way to leverage world models for test-time action selection without compromising the sample efficiency of model-free algorithms.
- The authors provide a thorough evaluation of QWM on challenging manipulation benchmarks, Robomimic and LIBERO. The results are compelling and show that QWM can achieve better performance with fewer samples.
- The paper is well-written and easy to follow, with clear explanations of the proposed method and its implementation. The authors also provide a detailed ablation study, which helps to understand the importance of different components of QWM.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on manipulation tasks with sparse rewards. It would be beneficial to evaluate QWM on a wider range of tasks with more complex dynamics and reward structures to demonstrate its generalizability.
- The computational overhead of the tree search procedure is not thoroughly analyzed. While the authors mention that the policy and Q-function are trained on real transitions, the search process itself can be computationally expensive, especially for long-horizon tasks or high-dimensional state spaces. A detailed analysis of the computational cost and scalability of QWM would be valuable.
- The paper does not explore the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies on the quality of the imagined rollouts, and it would be important to understand how the method behaves when the world model is imperfect or inaccurate. An analysis of the robustness of QWM to model errors would strengthen the paper.

### Suggestions

The authors should consider expanding their evaluation to include tasks with more complex dynamics and reward structures. While the manipulation tasks used in the paper are challenging, they may not fully represent the diversity of problems where world models are applicable. For example, evaluating QWM on tasks with sparse rewards that require long-term planning, or tasks with high-dimensional state spaces and complex dynamics, would provide a more comprehensive assessment of its capabilities. This could involve incorporating tasks from other domains, such as navigation or robotics, to demonstrate the generalizability of the proposed method. Furthermore, it would be beneficial to explore the performance of QWM in scenarios with partial observability, which is a common challenge in real-world applications. This would help to understand the limitations of the approach and identify potential areas for improvement.

A more detailed analysis of the computational cost and scalability of QWM is also needed. The tree search procedure, while avoiding model bias, can introduce significant computational overhead, especially for tasks with long horizons or high-dimensional state spaces. The authors should provide a breakdown of the computational cost associated with different components of QWM, such as the world model prediction, the tree search, and the policy and Q-function updates. This analysis should also consider the impact of different hyperparameters, such as the tree depth and the number of rollouts, on the computational cost. Furthermore, it would be valuable to explore techniques for reducing the computational overhead of QWM, such as using more efficient search algorithms or pruning strategies. This would make the method more practical for real-world applications with limited computational resources.

Finally, the authors should investigate the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies heavily on the quality of the imagined rollouts, and it is crucial to understand how the method behaves when the world model is imperfect or inaccurate. The authors could explore the impact of different world model architectures and training procedures on the performance of QWM. They could also investigate techniques for improving the robustness of QWM to model errors, such as using ensemble methods or incorporating uncertainty estimates into the search procedure. This would provide a more complete understanding of the limitations of the approach and identify potential areas for future research.

### Questions

- How does QWM perform on tasks with dense rewards or continuous action spaces?
- What is the computational overhead of the tree search procedure compared to standard Q-learning?
- How sensitive is QWM to the accuracy of the world model? Are there any techniques to mitigate the impact of model inaccuracies?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer has identified three weaknesses: limited task diversity, lack of computational overhead analysis, and sensitivity to world model accuracy. I need to examine the paper to see if these criticisms are valid and supported by evidence.

**Plan:**
1. **Categorize Weaknesses:** Mark each weakness as Valid, Partially Valid, or Invalid, and state the confidence level.
2. **Evidence Collection:** Find specific evidence from the paper (quotes, experimental details, missing citations) to support the validation of each weakness.
3. **Synthesis and Reflection:** Summarize the evidence and explain the reasoning behind the validity assessment.
**Review 1 Weakness Analysis**

1. Weakness Statement:
"The paper primarily focuses on manipulation tasks with sparse rewards. It would be beneficial to evaluate QWM on a wider range of tasks with more complex dynamics and reward structures to demonstrate its generalizability."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper explicitly states the datasets used: "For Robomimic, we consider four tasks: Lift, Can, Square, and Tool Hang. For LIBERO, we evaluate on five tasks following the experimental protocol of prior work ( Dong et al., 2026d )." (Section 5)
   - These tasks are all manipulation tasks, and the paper doesn't mention experiments on tasks with dense rewards or different dynamics.

3. Literature Gap Analysis:
   - While the paper cites Robomimic and LIBERO, it doesn't discuss the diversity of tasks within these benchmarks or justify the exclusion of other types of tasks.

4. Validation Analysis:
   - Primary evidence summary: The paper's experimental section clearly focuses on manipulation tasks with sparse rewards.
   - Supporting quotes: "For Robomimic, we consider four tasks: Lift, Can, Square, and Tool Hang. For LIBERO, we evaluate on five tasks following the experimental protocol of prior work ( Dong et al., 2026d )."
   - Impact assessment: The reviewer's point about limited task diversity is valid as the paper's evaluation is confined to manipulation tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The explicit listing of manipulation tasks used in the experiments.

1. Weakness Statement:
"The computational overhead of the tree search procedure is not thoroughly analyzed. While the authors mention that the policy and Q-function are trained on real transitions, the search process itself can be computationally expensive, especially for long-horizon tasks or high-dimensional state spaces. A detailed analysis of the computational cost and scalability of QWM is also needed."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the tree search procedure in detail in Section 4.3.
   - There is no explicit mention of the computational cost or time complexity of the tree search.
b) Experiment-related Evidence:
   - The paper mentions the hardware used for experiments: "Experiments were conducted on a high-performance computing cluster with NVIDIA V100 GPUs." (Section 5.1)
   - There is no information on the actual runtime or computational resources required for the tree search compared to standard Q-learning.

3. Literature Gap Analysis:
   - The paper doesn't cite works that specifically analyze the computational cost of similar tree-based search methods in RL.

4. Validation Analysis:
   - Primary evidence summary: The paper details the tree search algorithm but lacks a quantitative analysis of its computational cost.
   - Supporting quotes: The entire Section 4.3 describes the algorithm without any computational analysis.
   - Impact assessment: The reviewer's concern about the computational overhead is valid as the paper doesn't provide a detailed analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The absence of computational cost analysis in the method and experimental sections.

1. Weakness Statement:
"The paper does not explore the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies on the quality of the imagined rollouts, and it would be important to understand how the method behaves when the world model is imperfect or inaccurate. An analysis of the robustness of QWM to model errors would strengthen the paper."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the world model training in Section 4.1, mentioning the use of a deterministic residual dynamics model for low-dimensional state observations and an action-conditioned video world model for pixel observations.
   - There is no discussion on how the performance of QWM changes with varying levels of world model accuracy.
b) Experiment-related Evidence:
   - The paper doesn't include experiments that systematically vary the accuracy of the world model or analyze the impact on QWM's performance.

3. Literature Gap Analysis:
   - The paper doesn't cite works that specifically investigate the robustness of model-based RL methods to imperfect world models.

4. Validation Analysis:
   - Primary evidence summary: The paper describes the world model but lacks an analysis of its impact on QWM's performance.
   - Supporting quotes: The method section details the world model architecture but doesn't discuss its limitations or the sensitivity of QWM to its quality.
   - Impact assessment: The reviewer's point about the lack of sensitivity analysis to the world model's accuracy is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The absence of experiments or discussion on the impact of world model accuracy on QWM's performance.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces QWM (Q-Learning with World Models), a novel framework that leverages world models for test-time action selection in online reinforcement learning. Unlike previous approaches that use world models for policy or value function optimization, QWM employs the world model solely for generating imagined rollouts during online interaction. These rollouts are then used in a tree search procedure to select the best action for execution in the environment, while the policy and Q-function are trained using standard Q-learning on real transitions. This approach aims to avoid the compounding model bias that often plagues model-based RL methods. The authors evaluate QWM on challenging manipulation benchmarks, Robomimic and LIBERO, and demonstrate that it outperforms strong model-free baselines in both sample efficiency and performance. The paper is well-written and easy to follow, with clear explanations of the proposed method and its implementation. The authors also provide a thorough evaluation of QWM on challenging manipulation benchmarks, Robomimic and LIBERO, demonstrating its superior performance compared to strong model-free baselines. The ablation study further helps to understand the importance of different components of QWM. However, the paper primarily focuses on manipulation tasks with sparse rewards, and it would be beneficial to evaluate QWM on a wider range of tasks with more complex dynamics and reward structures to demonstrate its generalizability. Additionally, the computational overhead of the tree search procedure is not thoroughly analyzed, and the paper does not explore the sensitivity of QWM to the accuracy of the world model. These limitations, while not diminishing the paper's contributions, highlight areas for further research and improvement.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I found several strengths in this paper. First, the core idea of using world models for test-time action selection, rather than for policy or value function optimization, is a novel and effective approach. This allows QWM to avoid the compounding model bias that often plagues model-based RL methods. The authors clearly articulate this motivation and provide a compelling rationale for their design choice. Second, the empirical results are quite strong. The paper demonstrates that QWM outperforms strong model-free baselines on challenging manipulation benchmarks, Robomimic and LIBERO, in both sample efficiency and performance. This is a significant achievement, as it shows that the proposed method is not only theoretically sound but also practically effective. The authors also provide a detailed ablation study, which helps to understand the importance of different components of QWM. This is valuable for the community, as it provides insights into the design choices and allows for further improvements. Finally, the paper is well-written and easy to follow. The authors clearly explain the proposed method and its implementation, making it accessible to a wide audience. The use of clear language and well-organized sections makes the paper easy to understand and follow. The authors also provide a thorough evaluation of QWM on challenging manipulation benchmarks, Robomimic and LIBERO, demonstrating its superior performance compared to strong model-free baselines. The ablation study further helps to understand the importance of different components of QWM.


## Weaknesses:

Despite the strengths, I have identified several weaknesses that warrant further attention. First, the paper primarily focuses on manipulation tasks with sparse rewards, which limits the generalizability of the findings. The authors evaluate QWM on four tasks from Robomimic (Lift, Can, Square, and Tool Hang) and five tasks from LIBERO. While these tasks are challenging, they are all within the domain of manipulation and have sparse reward structures. The paper does not include experiments on tasks with dense rewards or different dynamics, which makes it difficult to assess the robustness of QWM in more general settings. This is a significant limitation, as real-world applications often involve tasks with more complex dynamics and reward structures. My confidence in this weakness is high, as the experimental section clearly lists the manipulation tasks used, and there is no evidence of experiments on other types of tasks. Second, the computational overhead of the tree search procedure is not thoroughly analyzed. The authors describe the tree search algorithm in detail in Section 4.3, but they do not provide any quantitative analysis of its computational cost. While the authors mention that the policy and Q-function are trained on real transitions, the search process itself can be computationally expensive, especially for long-horizon tasks or high-dimensional state spaces. The paper does not include a breakdown of the computational cost associated with different components of QWM, such as the world model prediction, the tree search, and the policy and Q-function updates. Furthermore, the paper does not explore techniques for reducing the computational overhead of QWM, such as using more efficient search algorithms or pruning strategies. This lack of analysis makes it difficult to assess the practical applicability of QWM in real-world scenarios with limited computational resources. My confidence in this weakness is high, as the method section describes the algorithm without any computational analysis, and the experimental section does not provide any information on the runtime or computational resources required for the tree search. Finally, the paper does not explore the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies heavily on the quality of the imagined rollouts, and it is crucial to understand how the method behaves when the world model is imperfect or inaccurate. The authors describe the world model training in Section 4.1, but they do not discuss how the performance of QWM changes with varying levels of world model accuracy. The paper does not include experiments that systematically vary the accuracy of the world model or analyze the impact on QWM's performance. This is a significant limitation, as real-world world models are often imperfect, and understanding the robustness of QWM to model errors is essential for its practical application. My confidence in this weakness is high, as the method section details the world model architecture but doesn't discuss its limitations or the sensitivity of QWM to its quality, and the experimental section does not include any experiments that systematically vary the accuracy of the world model.


## Suggestions:

Based on the identified weaknesses, I have several suggestions for improving the paper. First, the authors should expand their evaluation to include tasks with more complex dynamics and reward structures. While the manipulation tasks used in the paper are challenging, they may not fully represent the diversity of problems where world models are applicable. For example, evaluating QWM on tasks with sparse rewards that require long-term planning, or tasks with high-dimensional state spaces and complex dynamics, would provide a more comprehensive assessment of its capabilities. This could involve incorporating tasks from other domains, such as navigation or robotics, to demonstrate the generalizability of the proposed method. Furthermore, it would be beneficial to explore the performance of QWM in scenarios with partial observability, which is a common challenge in real-world applications. This would help to understand the limitations of the approach and identify potential areas for improvement. Second, a more detailed analysis of the computational cost and scalability of QWM is needed. The tree search procedure, while avoiding model bias, can introduce significant computational overhead, especially for tasks with long horizons or high-dimensional state spaces. The authors should provide a breakdown of the computational cost associated with different components of QWM, such as the world model prediction, the tree search, and the policy and Q-function updates. This analysis should also consider the impact of different hyperparameters, such as the tree depth and the number of rollouts, on the computational cost. Furthermore, it would be valuable to explore techniques for reducing the computational overhead of QWM, such as using more efficient search algorithms or pruning strategies. This would make the method more practical for real-world applications with limited computational resources. Finally, the authors should investigate the sensitivity of QWM to the accuracy of the world model. The performance of QWM relies heavily on the quality of the imagined rollouts, and it is crucial to understand how the method behaves when the world model is imperfect or inaccurate. The authors could explore the impact of different world model architectures and training procedures on the performance of QWM. They could also investigate techniques for improving the robustness of QWM to model errors, such as using ensemble methods or incorporating uncertainty estimates into the search procedure. This would provide a more complete understanding of the limitations of the approach and identify potential areas for future research.


## Questions:

I have several questions regarding the paper's methodology and findings. First, how does QWM perform on tasks with dense rewards or continuous action spaces? The paper primarily focuses on manipulation tasks with sparse rewards, and it would be valuable to understand how QWM performs in settings with dense rewards or continuous action spaces. This would help to assess the generalizability of the method to a wider range of tasks. Second, what is the computational overhead of the tree search procedure compared to standard Q-learning? The paper does not provide a detailed analysis of the computational cost of the tree search, and it would be helpful to understand how much more computationally expensive QWM is compared to standard Q-learning. This would help to assess the practical applicability of QWM in real-world scenarios with limited computational resources. Third, how sensitive is QWM to the accuracy of the world model? The paper does not explore the sensitivity of QWM to the accuracy of the world model, and it would be valuable to understand how the method behaves when the world model is imperfect or inaccurate. This would help to assess the robustness of QWM to model errors and identify potential areas for improvement. Finally, how does the performance of QWM compare to other model-based RL methods that also use tree search for planning? The paper compares QWM to model-free baselines, but it would be valuable to compare it to other model-based RL methods that also use tree search for planning. This would help to assess the relative strengths and weaknesses of QWM compared to other approaches in the field.


## Rating:

6.5


## Confidence:

3.25


## Decision:

Accept
}