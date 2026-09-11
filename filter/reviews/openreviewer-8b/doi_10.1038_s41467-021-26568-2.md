# Review

## Summary
The paper establishes a correspondence between the dynamics of a single neural network parameterized by $x$ trained via gradient descent and a "neuroevolution" process in which the network parameters are stochastically mutated and accepted or rejected according to a Metropolis-Hastings criterion.  The paper shows that in the limit of small mutations, the neuroevolution process is equivalent to gradient descent on the loss function.  The paper derives this result analytically and then demonstrates it numerically for shallow and deep networks trained on simple regression tasks.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
The paper is well-written and easy to follow.  The theoretical result is interesting and nontrivial, and the numerical experiments provide convincing evidence that the theoretical result is relevant to practice.  The theoretical approach is similar to that of Haqq-Mishra et al. (2013), but the result itself is new and, to my knowledge, has not previously been demonstrated empirically.

## Weaknesses
The paper considers only very simple regression tasks and very simple network architectures.  It would be interesting to see if the correspondence holds for more complex tasks and architectures.

## Questions
None.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4