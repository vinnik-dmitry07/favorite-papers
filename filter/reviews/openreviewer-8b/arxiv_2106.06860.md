# Review

## Summary
This paper proposes a minimalist approach to offline RL by adding a simple behavior cloning term to the policy update of an online RL algorithm, specifically TD3. The resulting algorithm, TD3+BC, matches the performance of state-of-the-art offline RL algorithms while being easier to implement and tune, and reducing computational overhead.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The proposed approach is simple and easy to implement, requiring only a few lines of code change.
2. The algorithm achieves competitive performance compared to state-of-the-art offline RL algorithms on the D4RL benchmark, while being more efficient and easier to tune.
3. The paper provides a thorough analysis of the challenges in offline RL, such as implementation and tuning complexities, extra computation requirement, and instability of trained policies. This highlights the need for a minimalist approach like TD3+BC.

## Weaknesses
1. The proposed approach is quite simple and straightforward, which may be seen as a limitation by some reviewers.
2. The paper does not provide a theoretical analysis or justification for the proposed algorithm, which may limit its understanding and applicability.
3. The paper does not address the instability issue of offline-trained policies, which is a fundamental challenge in offline RL.

## Questions
1. How does the proposed approach perform on other offline RL benchmarks or environments beyond D4RL?
2. How sensitive is the algorithm to the choice of the hyperparameter α?
3. How does the algorithm handle different types of offline datasets, such as those collected by random policies or expert policies?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4