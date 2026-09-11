# Review

## Summary
This paper revisits three efficient training algorithms for transformer-based language models: layer stacking, layer dropping, selective backpropagation, RHO loss, Lion and Sophia optimizers. The authors evaluate these algorithms under a fixed computation budget using a proposed measure called reference system time (RST) and find that these methods do not improve training, validation, and downstream performance compared to the standard training with a fully decayed learning rate.

## Soundness
2

## Presentation
2

## Contribution
1

## Strengths
- The paper addresses an important problem of evaluating the effectiveness of efficient training algorithms for transformer-based language models.
- The authors evaluate three categories of efficient training algorithms using two model architectures (BERT and T5) and multiple datasets.

## Weaknesses
- The paper does not provide a comprehensive analysis of the reasons why the efficient training algorithms do not work as expected. It would be helpful to have a more in-depth discussion on this aspect.
- The paper could benefit from a more detailed comparison with related work, such as the paper "Don't Take the Hessian for Granite: Neural Network Training with a Noisy Hessian Estimate" which also examines the effectiveness of efficient training algorithms.

## Questions
- Can the authors provide more insights into why the efficient training algorithms do not improve performance? Are there any specific factors or conditions that might be contributing to this?
- How does the proposed measure of reference system time (RST) compare to other measures of computational cost, such as FLOPs or wall-clock time? Are there any limitations or biases associated with RST?
- How do the results of this paper relate to the findings of the paper "Don’t Take the Hessian for Granite: Neural Network Training with a Noisy Hessian Estimate"? Can the authors provide a comparison or discussion of the similarities and differences between the two studies?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4