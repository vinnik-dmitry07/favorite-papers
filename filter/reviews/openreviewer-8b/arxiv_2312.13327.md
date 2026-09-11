# Review

## Summary
This paper proposes a new method, Headless-AD, which extends the existing ICL method AD to be able to handle variable action spaces. The authors show that AD struggles to generalize to new action spaces, and demonstrate that Headless-AD can handle new action spaces without re-training.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The method is simple and intuitive.
- The experiments are well-designed to demonstrate the effectiveness of the method.

## Weaknesses
- The method is only evaluated on toy environments. It would be great to see if this method works on more complex environments, such as Atari games, which have discrete action spaces.
- The authors only test their method on AD. It would be great to see if this method can be applied to other ICL methods as well.

## Questions
- How does the performance of Headless-AD compare to other ICL methods, such as Decision Transformer [1] or DrQ [2]?

[1] Chen, Lili, et al. "Decision transformer: Reinforcement learning via sequence modeling." Advances in neural information processing systems 34 (2021): 15084-15097.

[2] Hafner, Danijar, et al. "Mastering diverse domains through world models." arXiv preprint arXiv:2301.04104 (2023).

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4