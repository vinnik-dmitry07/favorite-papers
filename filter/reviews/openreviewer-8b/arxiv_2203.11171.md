# Review

## Summary
The paper proposes a new decoding strategy called self-consistency for LLMs. The idea is to sample multiple reasoning paths and then select the most consistent answer by marginalizing over the sampled reasoning paths. The paper shows that self-consistency can improve the performance of chain-of-thought prompting on a range of arithmetic and commonsense reasoning tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The idea of self-consistency is simple and intuitive. It is also very easy to implement and does not require any training.
- The paper shows that self-consistency can significantly improve the performance of chain-of-thought prompting on a wide range of reasoning tasks and LLMs.
- The paper also shows that self-consistency can improve robustness to imperfect prompts and is compatible with beam search.

## Weaknesses
- The paper does not provide any analysis on the sampled reasoning paths. It would be interesting to see what the common patterns are for the sampled reasoning paths that lead to correct/incorrect answers. This could provide more insights into the reasoning process of LLMs and how to further improve their reasoning abilities.
- The paper does not provide any analysis on the computational cost of self-consistency. It would be helpful to know how the performance changes as the number of sampled reasoning paths increases.

## Questions
- How does the performance of self-consistency change as the number of sampled reasoning paths increases? Is there a point of saturation?
- What are the common patterns for the sampled reasoning paths that lead to correct/incorrect answers?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4