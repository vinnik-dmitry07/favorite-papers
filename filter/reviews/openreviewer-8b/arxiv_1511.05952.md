# Review

## Summary
The paper proposes a new method for prioritizing samples in the replay buffer of a DQN agent. The paper first motivates the need for prioritization with a toy example and then proposes two methods for prioritizing samples. The first method prioritizes transitions with high TD-error, while the second method prioritizes transitions based on rank. Both methods are combined with importance sampling to correct for the bias introduced by prioritization. The paper then evaluates the proposed methods on the Atari benchmark and shows that both methods improve over uniform sampling.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
The paper is well-written and easy to follow. The motivation for the method is clear and the method itself is simple and easy to implement. The experiments are extensive and show a clear improvement over the baseline.

## Weaknesses
The paper does not have many weaknesses. The only one that I could think of is that the method is only evaluated with DQN and not with other RL algorithms that use a replay buffer.

## Questions
- Have you tried prioritization with other RL algorithms? Does it still improve performance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4