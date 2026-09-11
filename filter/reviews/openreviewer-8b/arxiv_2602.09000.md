# Review

## Summary
This paper proposes Iterative Group Relative Policy Optimization (iGRPO), a two-stage RL training framework that enhances LLM reasoning by incorporating self-feedback. iGRPO first samples multiple drafts and selects the highest-rewarding one to condition the LLM, then applies a GRPO-style update on refinements. This approach improves performance on math reasoning tasks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The idea of using the highest-rewarding draft as a condition is interesting.
2. The paper is well-written and easy to follow.

## Weaknesses
1. The improvement over the baselines is marginal, especially for the 14B models.
2. The evaluation is limited to math reasoning tasks. It would be better to include other reasoning tasks such as logical reasoning and code generation.

## Questions
1. What is the performance of DeepSeek-R1-Distill-Qwen-14B and OpenMath-Nemotron-14B on the math reasoning tasks?
2. How does iGRPO compare to other RL training frameworks, such as PPO, on math reasoning tasks?
3. How does iGRPO perform on other reasoning tasks, such as logical reasoning and code generation?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4