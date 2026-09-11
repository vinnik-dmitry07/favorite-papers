# Review

## Summary
This paper proves that LeJEPA (alignment plus Gaussian regularization) learns a linearly identifiable representation if and only if the latent variables are Gaussian. This result is both surprising and interesting. The authors also provide an approximate identifiability result and validate the theory with experiments ranging from 2D examples to 1024-dimensional latents, including distributional ablations and pixel-based robotic control.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The paper provides a theoretical analysis of the LeJEPA method, which is interesting and important for the community.
- The paper conducts comprehensive experiments to validate the theory.

## Weaknesses
- The paper assumes that the dimension of the latent variable is known, which is often not the case in practice.
- The paper only considers a limited class of nonlinear mixing functions in the experiments. It would be interesting to see how the method performs with more complex mixing functions, such as those used in [1].
- The paper does not provide any experiments on real-world datasets.

[1] van de Ven, Gido M., et al. "Deep variational information bottleneck." ICLR 2017

## Questions
- How does the performance of LeJEPA compare to other methods, such as VICReg and InfoNCE, when the latent variables are non-Gaussian?
- Can the results be extended to the case where the dimension of the latent variable is unknown?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4