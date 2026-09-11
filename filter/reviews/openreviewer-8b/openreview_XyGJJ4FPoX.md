# Review

## Summary
This paper introduces MetaBFM, a framework that combines elements of meta-reinforcement learning (meta-RL) and behavior foundation models (BFMs) to address the challenge of generalizing to novel reward functions in new environments. The authors identify key limitations in both meta-RL and BFM approaches: meta-RL requires diverse training environments and reward functions, while BFMs rely on large, reward-free datasets. MetaBFM attempts to bridge these gaps by allowing agents to adapt to new objectives at test time, using a hybrid approach that incorporates supervised reward-following, unsupervised reward-free learning, and intrinsic exploration.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The idea of combining BFM and meta-RL is interesting.

## Weaknesses
1. The proposed method is not well-motivated. The authors claim that MetaBFM aims to reduce the need for diverse reward functions during training. However, in the experiments, they use the same reward functions for training as they do for testing. If the goal is to generalize to novel reward functions, the authors should evaluate the method on unseen reward functions during the test phase.
2. The authors claim that MetaBFM can generalize to new environments. However, in the experiments, they only test in-distribution generalization, where the test environments are sampled from the same distribution as the training environments. To demonstrate true generalization to new environments, the authors should evaluate the method on environments with significantly different statistics than those seen during training.
3. The authors claim that MetaBFM combines the best of both worlds. However, the results in Figure 7 show that MetaBFM performs worse than supervised meta-RL on in-distribution tasks. If MetaBFM is truly superior, it should outperform supervised meta-RL on in-distribution tasks.
4. The authors claim that MetaBFM can learn from reward-free trajectories. However, in the experiments, they use reward-labeled tasks during training. To test whether MetaBFM can learn from truly reward-free trajectories, the authors should evaluate the method on environments where no rewards are available during training.
5. The authors do not compare MetaBFM to any baseline methods. To demonstrate the effectiveness of their approach, they should compare to relevant meta-RL and BFM methods.
6. The authors do not provide any theoretical analysis of their method.

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4