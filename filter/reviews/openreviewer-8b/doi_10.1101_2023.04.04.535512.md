# Review

## Summary
The authors propose that belief states may not be necessary for optimal learning in partially observable environments. Instead, they show that recurrent neural networks (RNNs) can learn to estimate value directly from observations, generating reward prediction errors similar to those seen in experiments. The authors demonstrate that the RNN's learned representation encodes belief information only when its capacity is sufficient. This finding suggests that animals may not need to explicitly estimate beliefs to perform well in such tasks, offering a more computationally efficient approach for systems with limited capacity.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The paper is well-written and easy to follow. The authors provide a thorough analysis of the RNN's learned representations, showing that they can capture belief information. The paper also includes a detailed examination of the RNN's activity patterns, belief-like dynamics, and the impact of network capacity on the quality of the learned representations.

## Weaknesses
The paper's main weakness is its lack of novelty. The idea that RNNs can learn to estimate value directly from observations in partially observable environments has been explored in previous work. The authors do not provide any new insights or advancements in this area. Additionally, the paper does not offer any new theoretical insights or contributions to the field.

## Questions
1. How does the proposed approach differ from previous work on RNNs in partially observable environments? What novel contributions does this paper make to the field?
2. Can the authors provide more theoretical insights into why the RNN's learned representations encode belief information only when its capacity is sufficient? What are the underlying mechanisms at play?
3. How does the proposed approach scale to more complex tasks with higher-dimensional state spaces? What are the limitations of the current approach in terms of scalability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4