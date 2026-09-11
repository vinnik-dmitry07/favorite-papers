# Review

## Summary
This paper addresses the issue of insufficient exploration in Reinforcement Learning with Verifiable Rewards (RLVR) for Large Language Models (LLMs). It introduces Curiosity-Driven Exploration (CDE), a framework that leverages intrinsic curiosity signals from both the actor and the critic to guide exploration. For the actor, curiosity is measured by the perplexity of generated responses, while for the critic, it is assessed via the variance of value estimates from a multi-head architecture. The paper provides theoretical analysis demonstrating that the actor-based bonus promotes diversity among correct responses and penalizes overconfident errors, while the critic-based bonus is equivalent to count-based bonuses in linear MDPs. Empirical results show that CDE achieves approximately a +3 point improvement over standard RLVR on AIME benchmarks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow, with clear explanations of the proposed methods and thorough descriptions of the experimental setups.
- The paper provides a theoretical analysis that connects the actor-based perplexity bonus to the critic-based bonus, establishing a relationship to count-based bonuses in linear MDPs.
- The empirical results demonstrate that CDE achieves consistent performance gains across multiple benchmarks, with a notable improvement of approximately +3 points on the AIME benchmark.

## Weaknesses
- The paper does not compare the proposed method with other exploration techniques, such as intrinsic motivation or curiosity-based approaches, which would provide a more comprehensive evaluation of its effectiveness.
- The paper does not provide a detailed analysis of the computational cost associated with the multi-head architecture and the calculation of the curiosity bonuses, which could be a potential drawback in resource-constrained environments.
- The paper does not discuss the sensitivity of the method to the choice of hyperparameters, such as the bonus weights and the number of heads in the critic, which could affect the reproducibility and generalizability of the results.

## Questions
- How does the computational cost of CDE compare to other exploration techniques, and is the trade-off between performance improvement and computational efficiency justified?
- How sensitive is the performance of CDE to the choice of hyperparameters, such as the bonus weights and the number of heads in the critic, and how can practitioners effectively tune these parameters?
- How does CDE compare to other intrinsic motivation or curiosity-based exploration techniques in the context of LLMs, and what are the key advantages of the proposed method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4