## Reviewer

### Summary

This paper studies the distributional Bellman equation, and proposes a new algorithm based on the distributional Bellman optimality operator. The authors show that the distributional Bellman operator is a contraction in Wasserstein distance, and propose a new algorithm based on this operator. The authors evaluate the proposed algorithm on the Atari 2600 games, and show that the proposed algorithm outperforms the state-of-the-art algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The proposed algorithm is simple and easy to understand. The empirical results are promising.

### Weaknesses

1. The theoretical results are not very surprising. The distributional Bellman operator is a contraction in Wasserstein distance, which has been shown in previous work. The authors only show that the distributional Bellman operator is a contraction in Wasserstein distance, but do not show that the proposed algorithm converges to the optimal solution. 

2. The proposed algorithm is a simple extension of the standard Q-learning algorithm. The authors do not provide a theoretical analysis of the convergence of the proposed algorithm.

### Questions

1. Can the authors provide a theoretical analysis of the convergence of the proposed algorithm?

2. Can the authors provide a theoretical analysis of the convergence of the proposed algorithm in the finite-horizon setting?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a new perspective on reinforcement learning by focusing on the distribution of the return rather than the expectation. The authors argue that the distribution of returns is more fundamental than the expected return, which is a common approach in reinforcement learning. They provide theoretical results in both policy evaluation and control settings, demonstrating the importance of the distributional perspective. They also propose a new algorithm based on the distributional Bellman equation, which applies Bellman's equation to the learning of approximate value distributions. The algorithm is evaluated on the Arcade Learning Environment, and the results demonstrate the effectiveness of the distributional perspective in reinforcement learning.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the distributional perspective on reinforcement learning and its importance. The theoretical results are well-presented and easy to understand. The proposed algorithm is well-described and evaluated on a range of games from the Arcade Learning Environment. The results demonstrate the effectiveness of the distributional perspective in reinforcement learning.

### Weaknesses

The paper does not provide a detailed discussion of the limitations of the proposed algorithm. While the algorithm is evaluated on a range of games from the Arcade Learning Environment, it is not clear how well it would perform on more complex tasks. Additionally, the paper does not discuss potential applications of the distributional perspective in reinforcement learning beyond the specific algorithm proposed in this paper.

### Questions

1. How does the proposed algorithm perform on more complex tasks beyond the Arcade Learning Environment?
2. What are the potential applications of the distributional perspective in reinforcement learning beyond the specific algorithm proposed in this paper?
3. How does the proposed algorithm compare to other algorithms that focus on the distribution of returns, such as those mentioned in the related work section?
4. How does the proposed algorithm handle the case where the reward function is not stationary, as in the case of partial observability?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the distributional perspective of reinforcement learning. The authors first show that the distributional Bellman operator is a contraction in Wasserstein distance, then they propose a new algorithm based on this operator. The algorithm is evaluated on the Atari 2600 games and shows better performance than the state-of-the-art algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The proposed algorithm is simple and easy to understand. The empirical results are promising.

### Weaknesses

1. The theoretical results are not very surprising. The distributional Bellman operator is a contraction in Wasserstein distance, which has been shown in previous work. The authors only show that the distributional Bellman operator is a contraction in Wasserstein distance, but do not show that the proposed algorithm converges to the optimal solution. 

2. The proposed algorithm is a simple extension of the standard Q-learning algorithm. The authors do not provide a theoretical analysis of the convergence of the proposed algorithm.

### Questions

1. Can the authors provide a theoretical analysis of the convergence of the proposed algorithm?

2. Can the authors provide a theoretical analysis of the convergence of the proposed algorithm in the finite-horizon setting?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents a new approach to reinforcement learning (RL) that focuses on the distribution of returns rather than the expected return. The authors argue that this perspective is more fundamental to RL and propose a new algorithm based on the distributional Bellman equation. They demonstrate the effectiveness of this approach by evaluating it on the Arcade Learning Environment (ALE) and showing significant improvements over existing algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper introduces a novel approach to RL by considering the distribution of returns, which is a fresh perspective in the field. The authors provide a comprehensive theoretical analysis of the distributional Bellman operator, demonstrating its properties and behavior. The proposed algorithm, C51, is evaluated on the ALE, a well-established benchmark, and shows significant improvements over existing methods. The paper is well-written and easy to follow, with clear explanations and visualizations of the results.

### Weaknesses

The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. While the authors mention that the distributional perspective is more fundamental to RL, they do not provide a clear explanation of why this perspective is more important or how it addresses specific challenges in RL. Additionally, the paper does not discuss potential applications of the distributional perspective beyond the specific algorithm proposed. The authors could also provide more details on the computational complexity of the proposed algorithm and its scalability to larger and more complex environments.

### Questions

1. Can the authors provide a more detailed discussion of the limitations of the proposed approach and how it addresses specific challenges in RL?
2. How does the distributional perspective relate to other approaches in RL, such as policy gradient methods or model-based RL?
3. Can the authors provide more details on the computational complexity of the proposed algorithm and its scalability to larger and more complex environments?
4. How does the proposed algorithm compare to other distributional RL methods, such as quantile regression?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the distributional perspective of reinforcement learning. The authors first show that the distributional Bellman operator is a contraction in Wasserstein distance, then they propose a new algorithm based on this operator. The algorithm is evaluated on the Atari 2600 games and shows better performance than the state-of-the-art algorithms.

The authors have addressed the concerns of the reviewers in the rebuttal. However, the reviewers still have some concerns on the novelty of the theoretical results and the comparison with other distributional RL methods. The authors are encouraged to address these concerns in the camera-ready version.

### justification_for_why_not_higher_score

The reviewers still have some concerns on the novelty of the theoretical results and the comparison with other distributional RL methods.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the top 10% of submissions, but not good enough for spotlight/oral)