# Review

## Summary
This paper proposes a soft actor-critic algorithm, which combines the off-policy update with a stable stochastic actor-critic formulation. The proposed method achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy methods. The authors also demonstrate that the proposed method is very stable, achieving very similar performance across different random seeds.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is technically sound.
3. The empirical results show that the proposed method achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy methods.

## Weaknesses
1. The novelty of the proposed method is limited. The proposed method is very similar to the existing soft Q-learning method [1], which also aims to maximize the expected reward while also maximizing entropy. The difference is that the proposed method uses a separate actor network to maximize the entropy of the actor, while the soft Q-learning method uses a sampling network trained to draw samples from the optimal policy. The authors should discuss the similarity and difference between the proposed method and the soft Q-learning method, and explain why using a separate actor network is better.
2. The proposed method is not evaluated on the D4RL benchmark, which is a standard benchmark for evaluating RL algorithms. The authors should evaluate the proposed method on the D4RL benchmark to compare with more baselines and to demonstrate the generalization ability of the proposed method.
3. The proposed method is not evaluated on high-dimensional tasks, such as the Humanoid task. The authors should evaluate the proposed method on the Humanoid task to demonstrate its effectiveness on high-dimensional tasks.

[1] Haarnoja, Tuomas, et al. "Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor." arXiv preprint arXiv:1801.01290 (2018).

## Questions
1. What is the difference between the proposed method and the soft Q-learning method?
2. Can the proposed method be applied to discrete action spaces?
3. How does the proposed method perform on the D4RL benchmark?
4. How does the proposed method perform on the Humanoid task?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4