# Review

## Summary
This paper proposes a new attention-free architecture called Hyena, which is a subquadratic drop-in replacement for attention. It is constructed by interleaving implicitly parameterized long convolutions and data-controlled gating. The authors demonstrate the effectiveness of the proposed Hyena architecture on WikiText-103 and The Pile datasets, and show that it can match the performance of Transformer with a 20% reduction in training compute. They also show that Hyena operators are twice as fast as highly optimized attention at sequence length 8K and 100x faster at sequence length 64K.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The authors provide a clear and concise explanation of the proposed Hyena architecture, and the figures help to illustrate the concept.
3. The authors provide a thorough analysis of the proposed method, including its computational properties and efficiency. They also provide a detailed comparison with other attention-free architectures.

## Weaknesses
1. The experiments are only conducted on WikiText-103 and The Pile datasets. It would be beneficial to evaluate the proposed method on a wider range of datasets to assess its generalizability.
2. The paper does not provide a detailed analysis of the limitations of the proposed method. It would be beneficial to discuss any potential drawbacks or challenges of using Hyena in different scenarios or tasks.
3. The paper does not provide a detailed analysis of the interpretability of the proposed method. It would be beneficial to explain how the Hyena architecture makes decisions and how it can be interpreted.

## Questions
1. Can you provide more details on the experimental setup and hyperparameters used in the experiments?
2. Can you provide more details on the potential limitations of the proposed method and how it can be improved in future work?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4