# Review

## Summary
The paper addresses the problem of overestimation of the Q values in deep reinforcement learning. The authors show that the problem is still present in Deep Q Networks (DQN) and propose a solution based on Double Q-learning, an algorithm that was previously proposed in the tabular setting. The authors show that the Double Q-learning idea can be easily extended to the deep reinforcement learning and that it can be implemented with a minimal change to the DQN algorithm. The authors show that the proposed algorithm, called Double DQN, outperforms DQN on the Atari 2600 domain.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well written and easy to follow.
- The proposed algorithm is simple and effective.
- The experimental results are convincing.

## Weaknesses
- The novelty of the paper is limited. The main idea of the paper is based on the Double Q-learning algorithm, which was proposed in 2010. The main contribution of the paper is the extension of this algorithm to the deep reinforcement learning setting, which is relatively straightforward.
- The experimental evaluation is limited to the Atari 2600 domain. It would be interesting to see how the proposed algorithm performs on other domains, such as MuJoCo.

## Questions
- How does the proposed algorithm perform on other domains, such as MuJoCo?
- How does the proposed algorithm perform in the presence of function approximation errors due to the expressivity limitations of the neural networks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4