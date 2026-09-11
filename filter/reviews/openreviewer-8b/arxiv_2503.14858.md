# Review

## Summary
The paper explores the impact of increasing network depth in self-supervised reinforcement learning (RL) and finds that scaling depth can significantly improve performance, particularly in goal-conditioned tasks. The authors demonstrate that increasing the depth of networks up to 1024 layers can lead to substantial gains in success rates and the development of qualitatively new behaviors in simulated locomotion and manipulation tasks. The study highlights the importance of depth scaling as a key factor in achieving emergent capabilities in RL, offering insights into how deeper networks can capture richer representations and improve exploration.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper presents a novel finding that increasing network depth can significantly improve performance in self-supervised RL, which is counter to the prevailing focus on width scaling in prior works.
2. The paper is well-written and easy to follow. The figures are clear and informative. 
3. The experiments are comprehensive and well-designed, covering a wide range of tasks and providing detailed analyses of the effects of depth scaling.

## Weaknesses
1. The paper does not provide a theoretical explanation for why depth scaling is more effective than width scaling in this context. 
2. The paper does not explore the potential benefits of combining depth scaling with other scaling techniques, such as increasing the diversity of the tasks in the training data or using more complex reward structures.

## Questions
1. How does the performance of depth scaling compare to other advanced techniques like model-based RL or multi-task RL?
2. Are there any specific types of tasks or environments where depth scaling might be less effective or even detrimental to performance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4