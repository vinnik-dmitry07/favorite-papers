# Review

## Summary
This paper proposes a novel neural network architecture for deep reinforcement learning that decouples the estimation of the state value function V(s) and the state-action value function Q(s,a) into two separate estimators. The authors argue that this decoupling can improve learning efficiency and policy evaluation, particularly in environments with large action spaces or redundant actions. The proposed architecture, called the dueling network, uses a single network with two streams that represent V(s) and A(s,a) respectively. The two streams share a common convolutional feature learning module and are combined through a special aggregating layer to produce the Q(s,a) function. The authors evaluate their approach on a toy environment and on the Atari domain, demonstrating improved performance over single-stream baselines.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a thorough explanation of their proposed architecture.
- The idea of decoupling V(s) and A(s,a) in a single network is novel and well-motivated. The authors provide a clear rationale for why this can improve learning efficiency and policy evaluation.
- The experimental results on the toy environment and the Atari domain are convincing and demonstrate the effectiveness of the proposed approach. The authors also provide a detailed analysis of their results and a discussion of the limitations of their work.

## Weaknesses
- The proposed architecture is only evaluated on discrete action environments. It would be interesting to see how it performs on continuous action environments.
- The performance of the proposed architecture is sensitive to gradient clipping, and it would be helpful to have a more principled approach to determining the clipping threshold.
- The proposed architecture is only evaluated on the Atari domain. It would be interesting to see how it performs on other domains, such as continuous control tasks or robotics.

## Questions
- How does the proposed architecture perform on continuous action environments?
- How does the proposed architecture perform on other domains, such as continuous control tasks or robotics?
- What is the impact of the gradient clipping threshold on the performance of the proposed architecture? Is there a more principled way to determine the optimal threshold?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4