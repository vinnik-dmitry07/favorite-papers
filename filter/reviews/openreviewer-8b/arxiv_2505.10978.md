# Review

## Summary
This paper proposes a new method for training LLMs in multi-turn environments. The method extends group-based RL methods to multi-turn environments by introducing a mechanism to assign credit to individual steps within a trajectory. The method is evaluated on ALFWorld, WebShop, and search-augmented QA tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well written and easy to understand
- The method is novel and addresses an important problem in RL for LLMs
- The experimental evaluation is thorough and the method is compared to a number of relevant baselines

## Weaknesses
- The paper should discuss the computational overhead of the method. While the paper claims that the method incurs little to no additional time cost, it is important to provide a detailed analysis of the computational overhead of the method compared to the baselines. This would help readers understand the trade-offs between performance and computational cost.
- The paper should discuss the sensitivity of the method to hyperparameters. It would be useful to know how sensitive the method is to the choice of hyperparameters, such as the weighting coefficient w. A sensitivity analysis would help readers understand how easy/hard it is to tune the method for new tasks.
- The paper should discuss the limitations of the method. It would be useful to provide a detailed discussion of the limitations of the method, such as the assumptions it makes and potential failure modes. This would help readers understand the contexts in which the method is suitable and where it may struggle.

## Questions
- How does the computational overhead of GiGPO compare to the baselines?
- How sensitive is GiGPO to the choice of hyperparameters, such as the weighting coefficient w?
- What are the limitations of GiGPO, and in which types of environments does it tend to struggle?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4