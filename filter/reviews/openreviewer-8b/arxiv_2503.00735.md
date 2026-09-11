# Review

## Summary
This paper proposes LADDER, a framework that enables large language models to improve their problem-solving abilities through recursive problem decomposition. LADDER generates progressively simpler variants of complex problems, allowing the model to learn from easier examples first and build up to harder ones. The authors demonstrate LADDER's effectiveness on mathematical integration tasks, showing significant improvements. They also introduce TTRL, which further boosts performance by applying reinforcement learning to problem variants at inference time.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper presents a novel framework for autonomous model improvement through recursive problem decomposition and self-guided learning.
- The authors demonstrate significant empirical improvements on mathematical reasoning tasks, achieving state-of-the-art performance on the MIT Integration Bee with a 7B parameter model.
- The paper introduces Test-Time Reinforcement Learning (TTRL), which further boosts performance by applying reinforcement learning to problem variants at inference time.

## Weaknesses
- The method is only tested on mathematical integration tasks, and it's unclear how well it would generalize to other domains.
- The variant generation process is manually designed and requires significant engineering effort to get right.
- The method relies on a numerical verification method, which may not be 100% accurate and could lead to incorrect learning signals.

## Questions
- How well do you expect the method to generalize to other domains beyond mathematical integration? What are the key challenges in adapting LADDER to other types of problems?
- How sensitive is the method to the quality of the variant generation process? What happens if the generated variants are of poor quality or the wrong difficulty level?
- How does the computational cost of LADDER compare to other approaches like data augmentation or curriculum learning? Is it more expensive to generate variants recursively?
- How do you determine the optimal number of variants to generate for each problem? Is there a way to predict when to stop the recursion?
- How does the performance of LADDER compare to other self-improvement methods like self-play or self-questioning? What are the key advantages of recursive problem decomposition?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4