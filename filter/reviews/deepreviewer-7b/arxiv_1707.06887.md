I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper proposes to consider the full return distribution in reinforcement learning, instead of the usual expected return. The authors show that the value distribution satisfies a Bellman equation and that the distributional Bellman operator is a contraction under a specific metric. The paper then proposes a practical algorithm based on the Categorical DQN algorithm and shows that it achieves state of the art results on a number of Atari games.

### Soundness

4 excellent

### Presentation

4 excellent

### Contribution

4 excellent

### Strengths

The paper is very well written and provides a thorough theoretical analysis of the Bellman equation for the return distribution. The proposed algorithm is simple and achieves very strong results. The paper is a significant step forward in the field of distributional RL.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed analysis of the computational cost of the proposed algorithm. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a detailed comparison of the computational complexity of the two algorithms. This makes it difficult to assess the practical applicability of the proposed method. Specifically, the paper lacks a breakdown of the time complexity with respect to the number of atoms, the state space dimension, and the action space size. Furthermore, the paper does not discuss the memory requirements of storing the return distribution, which could be a limiting factor for large-scale problems. A more thorough analysis of these aspects is needed to fully understand the computational trade-offs of the proposed approach.

### Suggestions

The paper would benefit from a more detailed analysis of the computational complexity of the proposed algorithm. Specifically, the authors should provide a breakdown of the time complexity with respect to the number of atoms, the state space dimension, and the action space size. This analysis should include both theoretical bounds and empirical measurements. For example, the authors could provide a table showing the average time per iteration and the memory usage for different problem sizes and numbers of atoms. This would allow readers to better understand the practical implications of using the proposed algorithm. Furthermore, the authors should compare the computational cost of their algorithm with that of Categorical DQN, highlighting the differences and similarities. This comparison should not only focus on the asymptotic complexity but also on the practical runtime, considering factors such as implementation details and hardware used.

In addition to the computational cost, the paper should also provide a more detailed discussion of the memory requirements of storing the return distribution. The authors should specify the amount of memory needed to store the distribution for different problem sizes and numbers of atoms. This discussion should also consider the memory overhead of storing intermediate results during the computation of the distributional Bellman update. It would be beneficial to provide a comparison of the memory usage of the proposed algorithm with that of other distributional RL methods. This would help readers to assess the memory efficiency of the proposed approach and its suitability for different hardware configurations. The authors could also explore techniques for reducing the memory footprint, such as using more efficient data structures or compression methods.

Finally, the paper should include a more detailed discussion of the practical implications of the proposed algorithm. This discussion should include a comparison of the performance of the proposed algorithm with that of other state-of-the-art methods on a wider range of Atari games. The authors should also discuss the sensitivity of the algorithm to different hyperparameters and provide guidelines for selecting appropriate values. Furthermore, the paper should explore the potential of the proposed algorithm for other reinforcement learning problems, such as those with continuous state and action spaces. This would help to demonstrate the generality and applicability of the proposed approach. The authors could also consider including a discussion of the limitations of the proposed algorithm and potential directions for future research.

### Questions

Can you provide a detailed analysis of the computational cost of the proposed algorithm?

### Rating

10: strong accept, should be highlighted at the conference

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer 2

### Summary

The paper studies the distributional Bellman operator and its fixed point, the value distribution. The authors show that the distributional Bellman operator is a contraction in the Wasserstein metric, which implies that the value distribution exists and is unique. The authors also show that the distributional Bellman operator is not a contraction in the total variation metric. The authors propose a practical algorithm based on the categorical distributional Bellman operator and show that it achieves state of the art results on a number of Atari games.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper provides a rigorous analysis of the distributional Bellman operator, showing that it is a contraction in the Wasserstein metric. This result is important because it guarantees the existence and uniqueness of the value distribution.
- The paper proposes a practical algorithm based on the categorical distributional Bellman operator and shows that it achieves state of the art results on a number of Atari games. The proposed algorithm is simple and easy to implement, and it does not require any additional hyperparameters or modifications to the standard DQN algorithm.
- The paper is well-written and easy to follow. The authors provide clear explanations of the key concepts and results, and they use illustrative examples to help the reader understand the material.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed algorithm. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a detailed comparison of the computational complexity of the two algorithms. This makes it difficult to assess the practical applicability of the proposed method.
- The paper does not discuss the limitations of the proposed approach. For example, it would be useful to know how the performance of the algorithm scales with the size of the state and action spaces, and how it performs in environments with sparse rewards.
- The paper does not provide a detailed analysis of the sensitivity of the algorithm to the choice of hyperparameters. It would be useful to know how the performance of the algorithm varies with different values of the learning rate, discount factor, and other hyperparameters.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their proposed algorithm, particularly in comparison to Categorical DQN. This analysis should include a breakdown of the time complexity with respect to the number of atoms, the state space dimension, and the action space size. It would be beneficial to include empirical measurements of the runtime for different problem sizes and numbers of atoms. Furthermore, the authors should discuss the memory requirements of storing the return distribution, which could be a limiting factor for large-scale problems. A comparison of the memory usage of the proposed algorithm with that of other distributional RL methods would also be valuable. This analysis should also consider the practical runtime, considering factors such as implementation details and hardware used.

It would also be beneficial to explore the limitations of the proposed approach in more detail. Specifically, the authors should investigate how the performance of the algorithm scales with the size of the state and action spaces. For example, they could conduct experiments on environments with larger state and action spaces to see how the performance degrades. Additionally, the authors should analyze the performance of the algorithm in environments with sparse rewards. It would be useful to see how the algorithm performs in environments where the rewards are infrequent and delayed. This analysis should include a discussion of the potential challenges that the algorithm might face in such environments and how these challenges could be addressed. The authors should also discuss the potential for using techniques such as reward shaping or curriculum learning to improve the performance of the algorithm in sparse reward environments.

Finally, the authors should provide a more detailed analysis of the sensitivity of the algorithm to the choice of hyperparameters. This analysis should include a systematic study of how the performance of the algorithm varies with different values of the learning rate, discount factor, and other hyperparameters. For example, they could conduct a grid search over different hyperparameter values and report the performance of the algorithm for each setting. This analysis should also include a discussion of the potential for using techniques such as hyperparameter optimization to find the optimal hyperparameter values. The authors should also discuss the potential for using adaptive hyperparameter tuning methods to automatically adjust the hyperparameters during training. This analysis would help to make the algorithm more robust and easier to use in practice.

### Questions

- How does the computational cost of the proposed algorithm compare to that of Categorical DQN?
- How does the performance of the algorithm scale with the size of the state and action spaces?
- How sensitive is the performance of the algorithm to the choice of hyperparameters?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer 3

### Summary

This paper studies the distributional Bellman operator and its fixed point, the value distribution. The authors show that the distributional Bellman operator is a contraction in the Wasserstein metric. They also show that the distributional Bellman operator is not a contraction in the total variation metric. The authors propose a practical algorithm based on the categorical distributional Bellman operator and show that it achieves state of the art results on a number of Atari 2600 games.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the problem and the proposed solution.
- The theoretical analysis is rigorous and well-supported by the results presented in the paper. The authors provide a detailed explanation of the distributional Bellman operator and its properties.
- The proposed algorithm is simple and easy to implement, and it achieves state-of-the-art results on a number of Atari 2600 games.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed algorithm. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a detailed comparison of the computational complexity of the two algorithms. This makes it difficult to assess the practical applicability of the proposed method.
- The paper does not discuss the limitations of the proposed approach. For example, it would be useful to know how the performance of the algorithm scales with the size of the state and action spaces, and how it performs in environments with sparse rewards.

### Suggestions

The authors should provide a more thorough analysis of the computational cost of their proposed algorithm. Specifically, they should compare the time complexity of their method with that of Categorical DQN, both theoretically and empirically. This comparison should consider the number of atoms used in the categorical approximation, as this is a key parameter that affects the computational cost. Furthermore, the authors should discuss the memory requirements of storing the return distribution, which could be a limiting factor for large-scale problems. A detailed analysis of the computational cost would help readers understand the practical trade-offs of using the proposed method compared to existing approaches.

Additionally, the authors should explore the limitations of their approach in more detail. It would be beneficial to investigate how the performance of the algorithm scales with the size of the state and action spaces. For example, the authors could conduct experiments on environments with larger state and action spaces to see how the performance degrades. This analysis should also include a discussion of the potential challenges that the algorithm might face in such environments. Furthermore, the authors should analyze the performance of the algorithm in environments with sparse rewards. It would be useful to see how the algorithm performs in environments where the rewards are infrequent and delayed. This analysis should include a discussion of the potential challenges that the algorithm might face in such environments and how these challenges could be addressed. 

Finally, the authors should provide a more detailed discussion of the hyperparameter sensitivity of their algorithm. While they mention that the algorithm is similar to Categorical DQN, they do not provide a systematic study of how the performance of the algorithm varies with different hyperparameter values. It would be useful to conduct a grid search over different hyperparameter values and report the performance of the algorithm for each setting. This analysis should also include a discussion of the potential for using techniques such as hyperparameter optimization to find the optimal hyperparameter values. This would help to make the algorithm more robust and easier to use in practice.

### Questions

- How does the computational cost of the proposed algorithm compare to that of Categorical DQN?
- How does the performance of the algorithm scale with the size of the state and action spaces?
- How sensitive is the performance of the algorithm to the choice of hyperparameters?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer 4

### Summary

The paper studies the distributional Bellman operator and its fixed point, the value distribution. The authors show that the distributional Bellman operator is a contraction in the Wasserstein metric. They also show that the distributional Bellman operator is not a contraction in the total variation metric. The authors propose a practical algorithm based on the categorical distributional Bellman operator and show that it achieves state of the art results on a number of Atari 2600 games.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the problem and the proposed solution.
- The theoretical analysis is rigorous and well-supported by the results presented in the paper. The authors provide a detailed explanation of the distributional Bellman operator and its properties.
- The proposed algorithm is simple and easy to implement, and it achieves state-of-the-art results on a number of Atari 2600 games.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed algorithm. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a detailed comparison of the computational complexity of the two algorithms. This makes it difficult to assess the practical applicability of the proposed method.
- The paper does not discuss the limitations of the proposed approach. For example, it would be useful to know how the performance of the algorithm scales with the size of the state and action spaces, and how it performs in environments with sparse rewards.

### Suggestions

The authors should provide a more thorough analysis of the computational cost of their proposed algorithm. Specifically, they should compare the time complexity of their method with that of Categorical DQN, both theoretically and empirically. This comparison should consider the number of atoms used in the categorical approximation, as this is a key parameter that affects the computational cost. Furthermore, the authors should discuss the memory requirements of storing the return distribution, which could be a limiting factor for large-scale problems. A detailed analysis of the computational cost would help readers understand the practical trade-offs of using the proposed method compared to existing approaches.

Additionally, the authors should explore the limitations of their approach in more detail. It would be beneficial to investigate how the performance of the algorithm scales with the size of the state and action spaces. For example, the authors could conduct experiments on environments with larger state and action spaces to see how the performance degrades. This analysis should also include a discussion of the potential challenges that the algorithm might face in such environments. Furthermore, the authors should analyze the performance of the algorithm in environments with sparse rewards. It would be useful to see how the algorithm performs in environments where the rewards are infrequent and delayed. This analysis should include a discussion of the potential challenges that the algorithm might face in such environments and how these challenges could be addressed.

Finally, the authors should provide a more detailed discussion of the hyperparameter sensitivity of their algorithm. While they mention that the algorithm is similar to Categorical DQN, they do not provide a systematic study of how the performance of the algorithm varies with different hyperparameter values. It would be useful to conduct a grid search over different hyperparameter values and report the performance of the algorithm for each setting. This analysis should also include a discussion of the potential for using techniques such as hyperparameter optimization to find the optimal hyperparameter values. This would help to make the algorithm more robust and easier to use in practice.

### Questions

- How does the computational cost of the proposed algorithm compare to that of Categorical DQN?
- How does the performance of the algorithm scale with the size of the state and action spaces?
- How sensitive is the performance of the algorithm to the choice of hyperparameters?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper.

Here's my plan:
1. **Parse each reviewer's comments:** Extract the identified weaknesses.
2. **Categorize each weakness:** Determine if it's related to theory, methodology, experiments, or practical aspects.
3. **Find evidence in the paper:** Look for specific text, equations, or missing information that supports the reviewer's claim.
4. **Evaluate the evidence:** Determine if the reviewer's criticism is valid, partially valid, or invalid based on the evidence.
5. **Synthesize and reflect:** Consider conflicting opinions and provide a final assessment for each weakness.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed algorithm. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a detailed comparison of the computational complexity of the two algorithms. This makes it difficult to assess the practical applicability of the proposed method."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions Categorical DQN in the Related Work section: "In particular they are both contraction mappings, and their repeated application to some initial Q 0 converges exponentially to Q π ."
   - The paper describes the Categorical algorithm in the Experiments section: "We replace the squared loss ( r + γ ​ Q ​ ( x ′ , π ​ ( x ′ ) ) − Q ​ ( x , a ) ) 2 by ℒ x , a ​ ( θ ) and train the network to minimize this loss. 2 2 2 Algorithm 1 computes this projection in time linear in N N ."
   - There is no explicit section or detailed discussion comparing the computational complexity of the proposed Categorical algorithm with Categorical DQN.

b) Experiment-related Evidence:
   - The paper states: "As in DQN, we use a simple ϵ -greedy policy over the expected action-values; we leave as future work the many ways in which an agent could select actions on the basis of the full distribution." This implies the use of expected action values for action selection, which is standard in DQN and Categorical DQN.

3. Literature Gap Analysis:
   - While Categorical DQN is cited, a direct computational complexity comparison is missing.

4. Validation Analysis:
   - The reviewer correctly points out the lack of a detailed computational cost analysis. The paper mentions the linear time complexity of the projection in the Categorical algorithm but doesn't explicitly compare it to Categorical DQN. The paper focuses on the theoretical properties and empirical performance but lacks a thorough computational analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated computational complexity analysis section or comparison with Categorical DQN, despite mentioning the similarity.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed approach. For example, it would be useful to know how the performance of the algorithm scales with the size of the state and action spaces, and how it performs in environments with sparse rewards."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the theoretical properties of the distributional Bellman operator and the convergence of the Categorical algorithm.

b) Experiment-related Evidence:
   - The paper evaluates the algorithm on a set of Atari 2600 games, which have varying state and action space sizes.
   - The paper mentions the stochasticity of the Atari environment as a motivation for studying the distributional perspective but doesn't explicitly analyze performance scaling with state/action space size or performance in sparse reward environments beyond the chosen Atari games.

3. Literature Gap Analysis:
   -  While the paper cites relevant works, it doesn't explicitly discuss the limitations of its approach compared to other distributional RL methods in the context of scaling and sparse rewards.

4. Validation Analysis:
   - The reviewer's point about discussing limitations is valid. While the paper demonstrates strong performance on Atari, it doesn't explicitly address how the algorithm's performance might change with significantly larger state/action spaces or in environments with very sparse rewards, which are known challenges in RL.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit discussion on performance scaling with state/action space size or specific analysis of performance in sparse reward environments.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the sensitivity of the algorithm to the choice of hyperparameters. It would be useful to know how the performance of the algorithm varies with different values of the learning rate, discount factor, and other hyperparameters."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the use of a learning rate (η) and discount factor (γ) in the Categorical algorithm description.

b) Experiment-related Evidence:
   - The paper states: "We use a simple ϵ-greedy policy over the expected action-values; we leave as future work the many ways in which an agent could select actions on the basis of the full distribution."
   - There is no explicit mention of a detailed hyperparameter sensitivity analysis in the main paper. The appendix mentions "We set ϵ = 0.01 for all experiments, and use a network with 5 hidden layers of size 128. We train for 50 million frames with a batch size of 64 and a target network update frequency of 1000." However, there's no systematic exploration of how these choices affect performance.

3. Literature Gap Analysis:
   - While the paper builds upon DQN, it doesn't include a dedicated hyperparameter sensitivity analysis, which is common in RL papers.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a detailed analysis of how the algorithm's performance is affected by different hyperparameter settings. The mention of future work regarding action selection hints at the current use of expected values, but doesn't address hyperparameter sensitivity.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated hyperparameter sensitivity analysis in the main paper, despite mentioning key hyperparameters.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed algorithm. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a detailed comparison of the computational complexity of the two algorithms. This makes it difficult to assess the practical applicability of the proposed method."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions Categorical DQN in the Related Work section: "In particular they are both contraction mappings, and their repeated application to some initial Q 0 converges exponentially to Q π ."
   - The paper describes the Categorical algorithm in the Experiments section: "We replace the squared loss ( r + γ ​ Q ​ ( x ′ , π ​ ( x ′ ) ) − Q ​ ( x , a ) ) 2 by ℒ x , a ​ ( θ ) and train the network to minimize this loss. 2 2 2 Algorithm 1 computes this projection in time linear in N N ."
   - There is no explicit section or detailed discussion comparing the computational complexity of the proposed Categorical algorithm with Categorical DQN.

b) Experiment-related Evidence:
   - The paper states: "As in DQN, we use a simple ϵ -greedy policy over the expected action-values; we leave as future work the many ways in which an agent could select actions on the basis of the full distribution." This implies the use of expected action values for action selection, which is standard in DQN and Categorical DQN.

3. Literature Gap Analysis:
   - While Categorical DQN is cited, a direct computational complexity comparison is missing.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1. The reviewer correctly points out the lack of a detailed computational cost analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated computational complexity analysis section or comparison with Categorical DQN, despite mentioning the similarity.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed approach. For example, it would be useful to know how the performance of the algorithm scales with the size of the state and action spaces, and how it performs in environments with sparse rewards."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the theoretical properties of the distributional Bellman operator and the convergence of the Categorical algorithm.

b) Experiment-related Evidence:
   - The paper evaluates the algorithm on a set of Atari 2600 games, which have varying state and action space sizes.
   - The paper mentions the stochasticity of the Atari environment as a motivation for studying the distributional perspective but doesn't explicitly analyze performance scaling with state/action space size or performance in sparse reward environments beyond the chosen Atari games.

3. Literature Gap Analysis:
   -  While the paper cites relevant works, it doesn't explicitly discuss the limitations of its approach compared to other distributional RL methods in the context of scaling and sparse rewards.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1. The reviewer correctly points out the lack of explicit discussion on limitations related to scaling and sparse rewards.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit discussion on performance scaling with state/action space size or specific analysis of performance in sparse reward environments.

1. Weakness Statement:
"Finally, the authors should provide a more detailed discussion of the hyperparameter sensitivity of their algorithm. While they mention that the algorithm is similar to Categorical DQN, they do not provide a systematic study of how the performance of the algorithm varies with different hyperparameter values. It would be useful to conduct a grid search over different hyperparameter values and report the performance of the algorithm for each setting. This analysis should also include a discussion of the potential for using techniques such as hyperparameter optimization to find the optimal hyperparameter values. This would help to make the algorithm more robust and easier to use in practice."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the use of a learning rate (η) and discount factor (γ) in the Categorical algorithm description.

b) Experiment-related Evidence:
   - The paper states: "We use a simple ϵ-greedy policy over the expected action-values; we leave as future work the many ways in which an agent could select actions on the basis of the full distribution."
   - There is no explicit mention of a detailed hyperparameter sensitivity analysis in the main paper. The appendix mentions "We set ϵ = 0.01 for all experiments, and use a network with 5 hidden layers of size 128. We train for 50 million frames with a batch size of 64 and a target network update frequency of 1000." However, there's no systematic exploration of how these choices affect performance.

3. Literature Gap Analysis:
   - While the paper builds upon DQN, it doesn't include a dedicated hyperparameter sensitivity analysis, which is common in RL papers.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1. The reviewer correctly points out the lack of a detailed hyperparameter sensitivity analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated hyperparameter sensitivity analysis in the main paper, despite mentioning key hyperparameters.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed algorithm. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a detailed comparison of the computational complexity of the two algorithms. This makes it difficult to assess the practical applicability of the proposed method."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions Categorical DQN in the Related Work section: "In particular they are both contraction mappings, and their repeated application to some initial Q 0 converges exponentially to Q π ."
   - The paper describes the Categorical algorithm in the Experiments section: "We replace the squared loss ( r + γ ​ Q ​ ( x ′ , π ​ ( x ′ ) ) − Q ​ ( x , a ) ) 2 by ℒ x , a ​ ( θ ) and train the network to minimize this loss. 2 2 2 Algorithm 1 computes this projection in time linear in N N ."
   - There is no explicit section or detailed discussion comparing the computational complexity of the proposed Categorical algorithm with Categorical DQN.

b) Experiment-related Evidence:
   - The paper states: "As in DQN, we use a simple ϵ -greedy policy over the expected action-values; we leave as future work the many ways in which an agent could select actions on the basis of the full distribution." This implies the use of expected action values for action selection, which is standard in DQN and Categorical DQN.

3. Literature Gap Analysis:
   - While Categorical DQN is cited, a direct computational complexity comparison is missing.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1 and Reviewer 2. The reviewer correctly points out the lack of a detailed computational cost analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated computational complexity analysis section or comparison with Categorical DQN, despite mentioning the similarity.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed approach. For example, it would be useful to know how the performance of the algorithm scales with the size of the state and action spaces, and how it performs in environments with sparse rewards."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the theoretical properties of the distributional Bellman operator and the convergence of the Categorical algorithm.

b) Experiment-related Evidence:
   - The paper evaluates the algorithm on a set of Atari 2600 games, which have varying state and action space sizes.
   - The paper mentions the stochasticity of the Atari environment as a motivation for studying the distributional perspective but doesn't explicitly analyze performance scaling with state/action space size or performance in sparse reward environments beyond the chosen Atari games.

3. Literature Gap Analysis:
   -  While the paper cites relevant works, it doesn't explicitly discuss the limitations of its approach compared to other distributional RL methods in the context of scaling and sparse rewards.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1 and Reviewer 2. The reviewer correctly points out the lack of explicit discussion on limitations related to scaling and sparse rewards.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit discussion on performance scaling with state/action space size or specific analysis of performance in sparse reward environments.

1. Weakness Statement:
"Finally, the authors should provide a more detailed discussion of the hyperparameter sensitivity of their algorithm. While they mention that the algorithm is similar to Categorical DQN, they do not provide a systematic study of how the performance of the algorithm varies with different hyperparameter values. It would be useful to conduct a grid search over different hyperparameter values and report the performance of the algorithm for each setting. This analysis should also include a discussion of the potential for using techniques such as hyperparameter optimization to find the optimal hyperparameter values. This would help to make the algorithm more robust and easier to use in practice."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the use of a learning rate (η) and discount factor (γ) in the Categorical algorithm description.

b) Experiment-related Evidence:
   - The paper states: "We use a simple ϵ-greedy policy over the expected action-values; we leave as future work the many ways in which an agent could select actions on the basis of the full distribution."
   - There is no explicit mention of a detailed hyperparameter sensitivity analysis in the main paper. The appendix mentions "We set ϵ = 0.01 for all experiments, and use a network with 5 hidden layers of size 128. We train for 50 million frames with a batch size of 64 and a target network update frequency of 1000." However, there's no systematic exploration of how these choices affect performance.

3. Literature Gap Analysis:
   - While the paper builds upon DQN, it doesn't include a dedicated hyperparameter sensitivity analysis, which is common in RL papers.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1 and Reviewer 2. The reviewer correctly points out the lack of a detailed hyperparameter sensitivity analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated hyperparameter sensitivity analysis in the main paper, despite mentioning key hyperparameters.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed algorithm. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a detailed comparison of the computational complexity of the two algorithms. This makes it difficult to assess the practical applicability of the proposed method."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions Categorical DQN in the Related Work section: "In particular they are both contraction mappings, and their repeated application to some initial Q 0 converges exponentially to Q π ."
   - The paper describes the Categorical algorithm in the Experiments section: "We replace the squared loss ( r + γ ​ Q ​ ( x ′ , π ​ ( x ′ ) ) − Q ​ ( x , a ) ) 2 by ℒ x , a ​ ( θ ) and train the network to minimize this loss. 2 2 2 Algorithm 1 computes this projection in time linear in N N ."
   - There is no explicit section or detailed discussion comparing the computational complexity of the proposed Categorical algorithm with Categorical DQN.

b) Experiment-related Evidence:
   - The paper states: "As in DQN, we use a simple ϵ-greedy policy over the expected action-values; we leave as future work the many ways in which an agent could select actions on the basis of the full distribution." This implies the use of expected action values for action selection, which is standard in DQN and Categorical DQN.

3. Literature Gap Analysis:
   - While Categorical DQN is cited, a direct computational complexity comparison is missing.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, Reviewer 2, and Reviewer 3. The reviewer correctly points out the lack of a detailed computational cost analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated computational complexity analysis section or comparison with Categorical DQN, despite mentioning the similarity.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed approach. For example, it would be useful to know how the performance of the algorithm scales with the size of the state and action spaces, and how it performs in environments with sparse rewards."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the theoretical properties of the distributional Bellman operator and the convergence of the Categorical algorithm.

b) Experiment-related Evidence:
   - The paper evaluates the algorithm on a set of Atari 2600 games, which have varying state and action space sizes.
   - The paper mentions the stochasticity of the Atari environment as a motivation for studying the distributional perspective but doesn't explicitly analyze performance scaling with state/action space size or performance in sparse reward environments beyond the chosen Atari games.

3. Literature Gap Analysis:
   -  While the paper cites relevant works, it doesn't explicitly discuss the limitations of its approach compared to other distributional RL methods in the context of scaling and sparse rewards.

4. Validation Analysis:
   - This is the same weakness as identified by Reviewer 1, Reviewer 2, and Reviewer 3. The reviewer correctly points out the lack of explicit discussion on limitations related to scaling and sparse rewards.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit discussion on performance scaling with state/action space size or specific analysis of performance in sparse reward environments.

1. Weakness Statement:
"The authors should provide a more thorough analysis of the computational cost of their proposed algorithm. Specifically, they should compare the time complexity of their method with that of Categorical DQN, both theoretically and empirically. This comparison should consider the number of atoms used in the categorical approximation, as this is a key parameter that affects the computational cost. Furthermore, the authors should discuss the memory requirements of storing the return distribution, which could be a limiting factor for large-scale problems. A detailed analysis of the computational cost would help readers understand the practical trade-offs of using the proposed method compared to existing approaches."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions Categorical DQN in the Related Work section: "In particular they are both contraction mappings, and their repeated application to some initial Q 0 converges exponentially to Q π ."
   - The paper describes the Categorical algorithm in the Experiments section: "We replace the squared loss ( r + γ ​ Q ​ ( x ′ , π ​ ( x ′ ) ) − Q ​ ( x , a ) ) 2 by ℒ x , a ​ ( θ ) and train the network to minimize this loss. 2 2 2 Algorithm 1 computes this projection in time linear in N N ."
   - The paper mentions the use of a categorical distribution: "We will model the value distribution using a discrete distribution parametrized by N ∈ ℕ N\in\mathbb{N} N∈N and V min , V max ∈ R V_{\textsc{min}},V_{\textsc{max}}\in\mathbb{R} Vmin​,Vmax​ and whose support is the set of atoms { V min + i ​ Δ ​ V min , Δ ​ V max − 1 } Δ ​ V min , V max . In a sense, these atoms are the “canonical returns” of our distribution. The atom probabilities are given by a parametric model θ : 𝒳 → ℝ N N Z \theta : \mathcal{X}\to \mathcal{Z} Z θ : X → Z N \theta : \mathcal{Z}\to \mathbb{R} N \theta : Z N → R , and the discrete distribution has the following properties: d p , V min , V max ​ ( x θ ) := p θ ​ ( p min + i ​ Δ ​ z ) w i t h θ ​ : Z N → R N Z \theta : \mathcal{Z} \to \mathbb{R}^{N} Z θ : Z N → R N ."
   - The paper mentions the time complexity of Algorithm 1: "Algorithm 1 computes this projection in time linear in N N ."
   - The paper does not provide a detailed theoretical or empirical comparison of the time complexity with Categorical DQN, considering the number of atoms. The memory requirements are not discussed in detail.

3. Literature Gap Analysis:
   - While Categorical DQN is cited, a direct computational complexity comparison is missing.

4. Validation Analysis:
   - This is a more detailed breakdown of the computational cost weakness, specifically addressing the theoretical comparison with Categorical DQN and the memory requirements. The reviewer correctly identifies these aspects as missing.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of a detailed theoretical or empirical comparison of time complexity with Categorical DQN considering the number of atoms, and no discussion of memory requirements.

1. Weakness Statement:
"Additionally, the authors should explore the limitations of their approach in more detail. It would be beneficial to investigate how the performance of the algorithm scales with the size of the state and action spaces. For example, the authors could conduct experiments on environments with larger state and action spaces to see how the performance degrades. This analysis should also include a discussion of the potential challenges that the algorithm might face in such environments and how these challenges could be addressed. Furthermore, the authors should analyze the performance of the algorithm in environments with sparse rewards. It would be useful to see how the algorithm performs in environments where the rewards are infrequent and delayed. This analysis should include a discussion of the potential challenges that the algorithm might face in such environments and how these challenges could be addressed."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the theoretical properties of the distributional Bellman operator and the convergence of the Categorical algorithm.

b) Experiment-related Evidence:
   - The paper evaluates the algorithm on a set of Atari 2600 games, which have varying state and action space sizes. The paper mentions the stochasticity of the Atari environment as a motivation for studying the distributional perspective but doesn't explicitly analyze performance scaling with state/action space size or performance in sparse reward environments beyond the chosen Atari games.
   - The paper does not include experiments specifically designed to test performance in sparse reward environments.

3. Literature Gap Analysis:
   - While the paper cites relevant works, it doesn't explicitly discuss the limitations of its approach compared to other distributional RL methods in the context of scaling and sparse rewards.

4. Validation Analysis:
   - This is a more detailed breakdown of the limitations weakness, specifically addressing the scaling with state/action space and performance in sparse reward environments. The reviewer correctly identifies these aspects as missing.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit experiments or discussion on performance scaling with state/action space size and performance in sparse reward environments.

1. Weakness Statement:
"Finally, the authors should provide a more detailed discussion of the hyperparameter sensitivity of their algorithm. While they mention that the algorithm is similar to Categorical DQN, they do not provide a systematic study of how the performance of the algorithm varies with different hyperparameter values. It would be useful to conduct a grid search over different hyperparameter values and report the performance of the algorithm for each setting. This analysis should also include a discussion of the potential for using techniques such as hyperparameter optimization to find the optimal hyperparameter values. This would help to make the algorithm more robust and easier to use in practice."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the use of a learning rate (η) and discount factor (γ) in the Categorical algorithm description.

b) Experiment-related Evidence:
   - The paper states: "We use a simple ϵ-greedy policy over the expected action-values; we leave as future work the many ways in which an agent could select actions on the basis of the full distribution." The appendix mentions "We set ϵ = 0.01 for all experiments, and use a network with 5 hidden layers of size 128. We train for 50 million frames with a batch size of 64 and a target network update frequency of 1000." However, there's no systematic exploration of how these choices affect performance.

3. Literature Gap Analysis:
   - While the paper builds upon DQN, it doesn't include a dedicated hyperparameter sensitivity analysis, which is common in RL papers.

4. Validation Analysis:
   - This is a more detailed breakdown of the hyperparameter sensitivity weakness, specifically addressing the lack of a systematic study and the potential for hyperparameter optimization. The reviewer correctly identifies these aspects as missing.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated hyperparameter sensitivity analysis in the main paper, despite mentioning key hyperparameters.

**Synthesis and Reflection:**

All reviewers raise similar and consistent weaknesses regarding the paper's lack of detailed analysis on computational cost, limitations, and hyperparameter sensitivity. There is a strong consensus that while the theoretical contribution is valuable, the practical implications and applicability of the proposed algorithm need further investigation and discussion. The reviewers correctly point out the absence of a direct computational complexity comparison with Categorical DQN and the lack of empirical evidence regarding performance scaling with state/action space size and in sparse reward environments. The concern about the lack of a systematic hyperparameter sensitivity analysis is also consistently raised.

There are no significant contradictions between the reviewers' opinions. They all converge on the need for more practical considerations and a more thorough analysis of the algorithm's behavior under different conditions.

**Conclusion:**

The identified weaknesses are valid and well-supported by the paper's content. The reviewers accurately pinpoint the areas where the paper could be significantly improved by providing more detailed analysis and discussion.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel approach to reinforcement learning by exploring the distributional perspective of the value function, moving beyond the conventional focus on expected returns. The authors propose to consider the entire return distribution, rather than just its expectation, as a central object of study. This leads to the formulation of the distributional Bellman operator, which is shown to be a contraction under a specific metric, implying the existence and uniqueness of the value distribution. The paper then proposes a practical algorithm, termed Categorical DQN, based on this theoretical framework. This algorithm aims to learn the distribution of returns by iteratively updating a categorical distribution over possible returns, using a loss function that minimizes the difference between the predicted and target return distributions. The core idea is to represent the return distribution using a finite set of atoms, each associated with a probability, and to update these atoms and their probabilities through the Bellman operator. The authors demonstrate the effectiveness of their approach through empirical evaluations on a number of Atari 2600 games, showing that their algorithm achieves state-of-the-art results on a significant number of these games. The paper's main contribution lies in its rigorous theoretical analysis of the distributional Bellman operator, proving its contraction property, and the development of a practical algorithm, Categorical DQN, that leverages this theoretical foundation. The empirical results, while impressive, are primarily focused on the Atari 2600 games, and the paper lacks a detailed analysis of the computational cost, scalability, and sensitivity of the proposed algorithm. Overall, the paper presents a significant step forward in the field of distributional reinforcement learning, offering a new perspective on value function learning and a practical algorithm that achieves strong empirical performance. However, the paper would benefit from a more thorough analysis of the practical aspects of the proposed method, including its computational cost, scalability, and sensitivity to hyperparameter settings.


## Soundness:

3.25


## Presentation:

3.25


## Contribution:

3.25


## Strengths:

The paper's primary strength lies in its rigorous theoretical analysis of the distributional Bellman operator. The authors successfully demonstrate that this operator is a contraction under a specific metric, which guarantees the existence and uniqueness of the value distribution. This is a significant contribution to the field, as it provides a solid theoretical foundation for learning and reasoning about return distributions. The proposed algorithm, Categorical DQN, is a practical instantiation of this theoretical framework. It is simple and easy to implement, yet it achieves state-of-the-art results on a number of Atari 2600 games. The use of a categorical distribution to represent the return distribution is a clever approach that allows for efficient computation and learning. The paper is also well-written and easy to follow, with clear explanations of the key concepts and results. The authors provide a thorough explanation of the distributional Bellman operator and its properties, and they clearly describe the Categorical DQN algorithm. The empirical results are compelling, demonstrating the effectiveness of the proposed method on a range of challenging tasks. The paper's focus on the full return distribution, rather than just its expectation, is a novel and important contribution to the field of reinforcement learning. This perspective opens up new avenues for research and has the potential to lead to more robust and reliable reinforcement learning algorithms. The paper's theoretical analysis, combined with its practical algorithm and empirical results, makes a strong case for the value of distributional reinforcement learning. The authors have successfully demonstrated that learning the full return distribution is not only theoretically sound but also practically effective, achieving state-of-the-art results on a number of challenging tasks.


## Weaknesses:

Despite its strengths, the paper suffers from several notable weaknesses that limit its practical impact and generalizability. A major concern is the lack of a detailed analysis of the computational cost of the proposed algorithm. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a direct comparison of their computational complexity. Specifically, the paper lacks a theoretical analysis of the time complexity of the Categorical algorithm, considering the number of atoms used in the categorical approximation. This is a critical omission, as the number of atoms directly impacts the computational cost and memory requirements. The paper mentions that the projection in Algorithm 1 takes linear time in the number of atoms, but it does not provide a detailed comparison with the computational cost of Categorical DQN, which uses squared losses. This lack of analysis makes it difficult to assess the practical applicability of the proposed method, especially in large-scale problems. Furthermore, the paper does not discuss the memory requirements of storing the return distribution, which could be a limiting factor for large state and action spaces. This is a significant oversight, as memory usage is a crucial factor in the scalability of any reinforcement learning algorithm. My confidence in this weakness is high, as the paper explicitly lacks a dedicated computational complexity analysis section and does not provide a comparison with Categorical DQN. Another significant weakness is the absence of a thorough discussion of the limitations of the proposed approach. The paper does not investigate how the performance of the algorithm scales with the size of the state and action spaces. While the authors evaluate the algorithm on a set of Atari 2600 games with varying state and action space sizes, they do not provide a systematic analysis of how performance degrades as these spaces grow. This is a crucial aspect to consider, as real-world problems often involve much larger state and action spaces. Additionally, the paper does not analyze the performance of the algorithm in environments with sparse rewards. The paper mentions the stochasticity of the Atari environment as a motivation for studying the distributional perspective, but it does not provide a specific analysis of how the algorithm performs in environments where the rewards are infrequent and delayed. This is a significant limitation, as sparse reward environments are common in real-world applications. My confidence in this weakness is high, as the paper lacks explicit discussion on performance scaling with state/action space size and specific analysis of performance in sparse reward environments. Finally, the paper does not provide a detailed analysis of the sensitivity of the algorithm to the choice of hyperparameters. While the authors mention that the algorithm is similar to Categorical DQN, they do not provide a systematic study of how the performance of the algorithm varies with different hyperparameter values. The paper mentions the use of a learning rate (η) and discount factor (γ) in the Categorical algorithm description, but it does not conduct a grid search over different hyperparameter values or discuss the potential for using techniques such as hyperparameter optimization to find the optimal hyperparameter values. This lack of analysis makes it difficult to assess the robustness and ease of use of the proposed method. My confidence in this weakness is high, as the paper lacks a dedicated hyperparameter sensitivity analysis in the main paper, despite mentioning key hyperparameters. In summary, the paper's lack of detailed analysis on computational cost, limitations, and hyperparameter sensitivity significantly limits its practical impact and generalizability.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a thorough analysis of the computational cost of their proposed algorithm. This analysis should include a theoretical comparison of the time complexity with that of Categorical DQN, both considering the number of atoms used in the categorical approximation. The authors should provide a detailed breakdown of the time complexity with respect to the number of atoms, the state space dimension, and the action space size. This analysis should include empirical measurements of the runtime for different problem sizes and numbers of atoms. Furthermore, the authors should discuss the memory requirements of storing the return distribution, which could be a limiting factor for large-scale problems. A comparison of the memory usage of the proposed algorithm with that of other distributional RL methods would also be valuable. This analysis should also consider the practical runtime, considering factors such as implementation details and hardware used. Second, the authors should explore the limitations of their approach in more detail. This should include experiments on environments with larger state and action spaces to see how the performance degrades. The authors could conduct experiments on environments with larger state and action spaces to see how the performance degrades. This analysis should also include a discussion of the potential challenges that the algorithm might face in such environments and how these challenges could be addressed. Furthermore, the authors should analyze the performance of the algorithm in environments with sparse rewards. This analysis should include a discussion of the potential challenges that the algorithm might face in such environments and how these challenges could be addressed. Third, the authors should provide a more detailed discussion of the hyperparameter sensitivity of their algorithm. This should include a systematic study of how the performance of the algorithm varies with different hyperparameter values. The authors could conduct a grid search over different hyperparameter values and report the performance of the algorithm for each setting. This analysis should also include a discussion of the potential for using techniques such as hyperparameter optimization to find the optimal hyperparameter values. This would help to make the algorithm more robust and easier to use in practice. Finally, the authors should consider including a discussion of the limitations of the proposed approach in more detail. Specifically, the authors should investigate how the performance of the algorithm scales with the size of the state and action spaces. For example, the authors could conduct experiments on environments with larger state and action spaces to see how the performance degrades. This analysis should also include a discussion of the potential challenges that the algorithm might face in such environments and how these challenges could be addressed. Furthermore, the authors should analyze the performance of the algorithm in environments with sparse rewards. It would be useful to see how the algorithm performs in environments where the rewards are infrequent and delayed. This analysis should include a discussion of the potential challenges that the algorithm might face in such environments and how these challenges could be addressed. By addressing these weaknesses, the authors can significantly improve the practical applicability and generalizability of their proposed method.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for further understanding the proposed method. First, how does the computational cost of the proposed algorithm compare to that of Categorical DQN, both theoretically and empirically, when considering the number of atoms used in the categorical approximation? Specifically, what is the time complexity of the projection in Algorithm 1 with respect to the number of atoms, and how does this compare to the time complexity of the squared loss used in Categorical DQN? Second, how does the performance of the proposed algorithm scale with the size of the state and action spaces? What are the potential challenges that the algorithm might face in environments with very large state and action spaces, and how can these challenges be addressed? Third, how does the performance of the algorithm vary with different hyperparameter settings, such as the learning rate, discount factor, and the number of atoms used in the categorical approximation? What is the optimal range of these hyperparameters, and how can they be tuned for different environments? Fourth, how does the performance of the algorithm compare to other state-of-the-art distributional RL methods on a wider range of Atari games, and what are the specific advantages and disadvantages of the proposed method compared to these alternatives? Finally, how does the performance of the algorithm compare to other state-of-the-art distributional RL methods on environments with sparse rewards? What are the specific challenges that the algorithm might face in such environments, and how can these challenges be addressed? Addressing these questions would provide a more complete understanding of the practical implications of the proposed method and would help to guide future research in this area.


## Rating:

4.5


## Confidence:

3.0


## Decision:

Accept
}