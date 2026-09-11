# Review

## Summary
The authors demonstrate that deep learning methods gradually lose plasticity in continual-learning settings. They also show that plasticity can be maintained indefinitely by algorithms that continually inject diversity into the network, such as their proposed continual backpropagation algorithm.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is interesting and backed by empirical evidence.

## Weaknesses
- The paper does not compare with existing methods for maintaining plasticity in continual learning, such as Wise-FT [1], EWC [2], or PackNet [3]. It would be beneficial to see how the proposed method compares to these established approaches.

[1] Mirzadeh, Seyed Iman, et al. "Linear mode connectivity in continual learning." Advances in Neural Information Processing Systems 34 (2021): 10588-10599.

[2] Kirkpatrick, James, et al. "Overcoming catastrophic forgetting in neural networks." Proceedings of the national academy of sciences 114.13 (2017): 3521-3526.

[3] Mallya, Arun, et al. "Packing neural networks for efficient continual learning." Advances in neural information processing systems 31 (2018).

## Questions
- How does the proposed method compare with other methods for maintaining plasticity in continual learning, such as Wise-FT, EWC, or PackNet?
- Have the authors considered using the proposed method in a class-incremental setup? How does it compare with existing methods in that scenario?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4