# Review

## Summary
This paper proposes Sophia, a scalable second-order optimizer that uses a light-weight estimate of the diagonal Hessian as the pre-conditioner. The update is the moving average of the gradients divided by the moving average of the estimated Hessian, followed by element-wise clipping. The clipping controls the worst-case update size and tames the negative impact of non-convexity and rapid change of Hessian along the trajectory. The authors show that Sophia achieves a 2x speed-up compared to Adam in the number of steps, total compute, and wall-clock time, achieving the same perplexity with 50 \% fewer steps, less total compute, and reduced wall-clock time.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective. 
3. The experiments are solid.

## Weaknesses
1. The idea of using the diagonal of the Hessian as a pre-conditioner is not new, and the authors did not cite the following paper:
Jahani, Y., Chen, C., Zhang, S., Li, Y., Lin, Q., Huang, Y., ... & Li, Y. (2021). A diagonal quasi-Newton update for deep learning. Advances in Neural Information Processing Systems, 34, 11287-11299.
2. The theoretical analysis is not very relevant to the main contribution of this paper. The diagonal Hessian method is not new and the convex setting is not the main setting of deep learning.

## Questions
1. In Figure 2, why does the Newton's method quickly converge to a saddle point instead of a local minimum?
2. What is the performance of the proposed method on vision tasks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4