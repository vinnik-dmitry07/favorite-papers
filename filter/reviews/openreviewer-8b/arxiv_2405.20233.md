# Review

## Summary
This paper proposes a method to accelerate the grokking phenomenon by amplifying the low-frequency components of the gradients. The authors hypothesize that the slow-varying component of the gradients is responsible for generalization and suggest a low-pass filter to amplify these components. The proposed method is evaluated on various tasks and architectures, demonstrating significant acceleration of the grokking phenomenon.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is simple and effective, with a clear theoretical motivation.
- The authors conduct extensive experiments across various tasks and architectures, demonstrating the broad applicability of their method.
- The paper provides valuable insights into the grokking phenomenon by analyzing the training dynamics and parameter trajectories.

## Weaknesses
- The proposed method introduces additional hyperparameters (λ and α) that need to be tuned for different tasks.
- The method is primarily evaluated on tasks that exhibit the delayed generalization characteristic of grokking. It would be interesting to see how it performs on tasks where grokking does not occur.

## Questions
- How does the proposed method affect the generalization performance if the task does not exhibit the grokking phenomenon?
- How does the proposed method compare to other techniques for accelerating convergence, such as larger batch sizes or more frequent evaluations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4