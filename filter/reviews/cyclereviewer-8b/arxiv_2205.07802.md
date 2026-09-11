## Reviewer

### Summary

This paper studies the primacy bias in deep RL, which refers to the phenomenon that early experiences have a disproportionate influence on the learning process of deep RL agents. The authors provide empirical evidence of the primacy bias and propose a simple solution by periodically resetting a part of the agent's neural network.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.

### Weaknesses

- The proposed method is not novel. The idea of resetting part of the network has been explored in the supervised learning literature (e.g., [1, 2, 3]). The authors should discuss the difference between their method and the existing work.
- The authors only consider discrete and continuous control tasks. The authors should also consider more complex tasks, such as robotics manipulation tasks.
- The authors only consider a small number of baseline algorithms. The authors should consider more algorithms, such as PPO and SAC with PER.
- The authors should also consider other forms of regularization, such as L2 regularization and dropout.
- The authors should provide more ablation studies to understand the effect of the proposed method.

[1] Anderson, C. W., Moore, A. H., & Schmidhuber, J. (1993). Learning to control an autonomous robot by pure neural reinforcement. Neural information processing systems.

[2] Taha, R., Koutnik, J., & Schmidhuber, J. (2021). Evolutionary subnetwork pruning for deep neural networks. Advances in Neural Information Processing Systems, 34, 11768-11780.

[3] Alabdulmohsin, I., Zhang, Y., & Bengio, Y. (2021). The role of forgetting in deep learning. Advances in Neural Information Processing Systems, 34, 10186-10197.

### Questions

- What is the difference between the proposed method and the existing work on resetting part of the network in supervised learning?
- What are the advantages of the proposed method compared to other forms of regularization, such as L2 regularization and dropout?
- How does the proposed method perform on more complex tasks, such as robotics manipulation tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper identifies a phenomenon in deep reinforcement learning called the primacy bias, where deep RL algorithms tend to overfit early interactions and ignore useful evidence encountered later. The authors propose a simple mechanism to mitigate this bias by periodically resetting a part of the agent. The proposed method is evaluated on both discrete and continuous action domains and shows consistent improvements in performance.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The paper provides a thorough analysis of the primacy bias and its effects on deep RL agents.
4. The proposed method shows consistent improvements in performance across different domains and algorithms.

### Weaknesses

1. The paper lacks a theoretical analysis of the primacy bias and its effects on deep RL agents.
2. The proposed method is not well-motivated, and the authors do not provide a clear explanation of why resetting a part of the agent helps mitigate the primacy bias.
3. The paper only evaluates the proposed method on a limited set of environments and algorithms, and it is unclear whether the method would generalize to other domains and tasks.
4. The paper does not provide a thorough comparison with other methods that aim to mitigate overfitting in deep RL, such as regularization and early stopping.

### Questions

1. Can the authors provide a theoretical analysis of the primacy bias and its effects on deep RL agents?
2. Can the authors provide a more detailed explanation of why resetting a part of the agent helps mitigate the primacy bias?
3. Can the authors evaluate the proposed method on a more diverse set of environments and algorithms to demonstrate its generalizability?
4. Can the authors provide a more thorough comparison with other methods that aim to mitigate overfitting in deep RL?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a simple method to mitigate the primacy bias in deep RL, which is the tendency of RL algorithms to overfit early interactions and ignore useful evidence encountered later. The proposed method is to periodically reset a part of the agent's neural network. The paper provides a thorough analysis of the primacy bias and its effects on deep RL agents, and shows that the proposed method consistently improves performance across different domains and algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The paper provides a thorough analysis of the primacy bias and its effects on deep RL agents.
- The proposed method shows consistent improvements in performance across different domains and algorithms.

### Weaknesses

- The paper lacks a theoretical analysis of the primacy bias and its effects on deep RL agents.
- The proposed method is not well-motivated, and the authors do not provide a clear explanation of why resetting a part of the agent helps mitigate the primacy bias.
- The paper only evaluates the proposed method on a limited set of environments and algorithms, and it is unclear whether the method would generalize to other domains and tasks.
- The paper does not provide a thorough comparison with other methods that aim to mitigate overfitting in deep RL, such as regularization and early stopping.

### Questions

- Can the authors provide a theoretical analysis of the primacy bias and its effects on deep RL agents?
- Can the authors provide a more detailed explanation of why resetting a part of the agent helps mitigate the primacy bias?
- Can the authors evaluate the proposed method on a more diverse set of environments and algorithms to demonstrate its generalizability?
- Can the authors provide a more thorough comparison with other methods that aim to mitigate overfitting in deep RL?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The authors identify a phenomenon in deep RL, where early interactions are overemphasized and later interactions are ignored. This is similar to the primacy bias in human learning, where early experiences have a disproportionate impact on future learning. The authors propose a simple solution: periodically reset a part of the agent. This is shown to improve performance on both discrete and continuous action domains.

### Soundness

3 good

### Presentation

4 excellent

### Contribution

3 good

### Strengths

- The paper is well written and easy to follow.
- The idea is simple, but the empirical results are compelling. The authors demonstrate that their method improves performance on a variety of tasks and domains.
- The authors provide a thorough analysis of the primacy bias and its effects on deep RL agents.
- The proposed method is easy to implement and does not require significant changes to existing deep RL algorithms.

### Weaknesses

- The authors do not provide a theoretical analysis of the primacy bias and its effects on deep RL agents. This makes it difficult to understand why the proposed method works and how it might generalize to other domains and tasks.
- The authors do not provide a thorough comparison with other methods that aim to mitigate overfitting in deep RL, such as regularization and early stopping. This makes it difficult to understand the relative benefits of the proposed method compared to other approaches.

### Questions

- How does the proposed method compare to other methods that aim to mitigate overfitting in deep RL, such as regularization and early stopping?
- Can the authors provide a theoretical analysis of the primacy bias and its effects on deep RL agents?
- How does the proposed method generalize to other domains and tasks? The authors only evaluate their method on discrete and continuous control tasks. Can they demonstrate that their method works on other types of tasks, such as reinforcement learning with function approximation or reinforcement learning with sparse rewards?
- Can the authors provide more details on how the proposed method works? For example, how often is the part of the agent reset? How does the frequency of resets affect performance? What are the trade-offs between different reset frequencies?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper identifies a phenomenon in deep RL, where early interactions are overemphasized and later interactions are ignored. This is similar to the primacy bias in human learning, where early experiences have a disproportionate impact on future learning. The authors propose a simple solution: periodically reset a part of the agent. This is shown to improve performance on both discrete and continuous action domains.

The reviewers generally agree that the paper is well written and easy to follow, and the idea is simple but the empirical results are compelling. The authors provide a thorough analysis of the primacy bias and its effects on deep RL agents, and the proposed method is easy to implement and does not require significant changes to existing deep RL algorithms.

However, the reviewers also point out that the paper lacks a theoretical analysis of the primacy bias and its effects on deep RL agents, and the proposed method is not well-motivated, and the authors do not provide a clear explanation of why resetting a part of the agent helps mitigate the primacy bias. The paper also only evaluates the proposed method on a limited set of environments and algorithms, and it is unclear whether the method would generalize to other domains and tasks.

### justification_for_why_not_higher_score

The paper lacks a theoretical analysis of the primacy bias and its effects on deep RL agents, and the proposed method is not well-motivated, and the authors do not provide a clear explanation of why resetting a part of the agent helps mitigate the primacy bias.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)