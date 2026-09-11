# Review

## Summary
The paper proposes to use parameter resetting to increase the update-to-data ratio in experience replay. The authors show that resetting the parameters of SAC and SPR allows them to significantly increase the UTD ratio, while maintaining or improving performance. The authors also study the effect of various design choices, such as the role of online samples and target networks.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. The authors motivate the problem well and the experiments are well-designed to address the research questions.
- The paper shows that parameter resetting allows to significantly increase the UTD ratio for two popular algorithms, SAC and SPR, and achieves strong performance on standard benchmarks.
- The authors perform a careful study of the design choices required for replay ratio scaling, such as the role of online samples and target networks.

## Weaknesses
- The paper does not introduce a new method, but simply applies parameter resetting to SAC and SPR. While the results are interesting, the novelty is limited.
- The paper does not provide any theoretical analysis or insights into why parameter resetting allows for better replay ratio scaling.

## Questions
- Have you tried resetting only part of the parameters, as done by Nikishin et al.? What is the effect of resetting only the last layers of the network?
- What is the effect of the reset interval in terms of environment steps, rather than number of updates? This would be more relevant for practical purposes.
- Have you tried using a larger replay buffer size? This would allow for more samples per update, and perhaps reduce the need for frequent resets.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4