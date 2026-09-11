# Review

## Summary
This paper studies the value distribution in reinforcement learning, which is defined as the distribution of the random return received by an agent. The authors argue that learning the value distribution is more important than learning the expected value, and demonstrate that the distributional Bellman operator is a contraction in the Wasserstein metric. They also show that the distributional Bellman operator is not a contraction in the control setting. Finally, they propose a new algorithm that models the value distribution using a discrete distribution, and the authors show that the proposed algorithm outperforms the baselines on a suite of games from the Atari environment.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well-written and easy to follow. The authors provide a detailed theoretical analysis of the distributional Bellman operator and demonstrate its effectiveness on a suite of games from the Atari environment. The empirical results are strong and show that the proposed algorithm outperforms the baselines.

## Weaknesses
The paper lacks a detailed discussion of the limitations of the proposed approach. The authors should provide a more detailed discussion of the assumptions and constraints of their method, as well as potential drawbacks or scenarios where it may not perform well. This would provide a more balanced view of the work and help readers understand the context in which it can be applied.

## Questions
1. What is the computational complexity of the proposed algorithm? How does it compare to the baselines in terms of training and inference time?

2. How sensitive is the proposed algorithm to the choice of hyperparameters, such as the number of atoms and the range of the value distribution?

3. Can the proposed algorithm be applied to other reinforcement learning environments beyond the suite of games from the Atari environment?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4