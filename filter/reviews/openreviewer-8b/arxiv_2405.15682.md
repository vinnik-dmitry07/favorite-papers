# Review

## Summary
The paper proposes a new optimization method that is claimed to be schedule-free. The method is a combination of Polyak averaging and Primal averaging. The authors provide some theory for the method and show that it performs well on a variety of tasks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The paper is well-written and the method is clearly presented. The experimental evaluation is extensive and the method performs well on a variety of tasks.

## Weaknesses
The main weakness of the paper is that the method is not really schedule-free. While it does not have a schedule in the sense that it does not have a pre-specified number of iterations, it still has a schedule in the sense that the hyper-parameters $\beta$ and $\gamma$ still need to be tuned. In fact, the authors acknowledge that "For short duration training ($\leq 25$ epochs), larger LR values begin to show the best performance." So, in practice, the user still needs to tune the learning rate and there is no reason to believe that $\beta=0.9$ will be the right choice. 

The theory is also not very convincing. Theorem 1 assumes that the function is non-smooth and convex which is not true for most deep learning problems. Theorem 2 is a very general theorem but it does not show that the method will converge to the optimal point. Theorem 3 is also not very convincing because it assumes that the gradients are bounded which is not true for deep learning problems.

## Questions
1. How do you respond to the criticism that the method is not really schedule-free since the hyper-parameters still need to be tuned?
2. Can you provide some theory for the smooth case?
3. Can you provide some intuition for why the method converges to the optimal point?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4