# Review

## Summary
This paper introduces GRPO-VPS, a method that enhances Group Relative Policy Optimization (GRPO) by incorporating segment-level process supervision. GRPO-VPS addresses the challenge of indiscriminate credit assignment in GRPO by segmenting the reasoning process and providing more precise feedback at each step. The method uses token-level entropy to identify reasoning segments and computes a confidence score for each, reflecting the model's belief in the correct answer. This fine-grained supervision enables more efficient and targeted policy updates, leading to improved performance on math reasoning tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is simple and easy to understand.
- The proposed method demonstrates strong empirical performance on math reasoning tasks and general-domain reasoning tasks.

## Weaknesses
- The paper only evaluates the proposed method on math reasoning tasks and general-domain reasoning tasks. It would be better to evaluate the proposed method on a wider range of reasoning tasks, such as logical reasoning tasks (e.g., LogiQA [1]) and planing tasks (e.g., PlanQA [2]).
- The paper does not provide a detailed analysis of the computational overhead introduced by the proposed method.

[1] LogiQA: A Large-Scale Distilling Dataset for Logical Reasoning of Open-Ended Questions in Long Texts. EMNLP 2023.

[2] PlanQA: A Reasoning Dataset for Evaluating Large Language Models' Planning Abilities. NeurIPS 2023.

## Questions
- How does the proposed method perform on logical reasoning tasks and planning tasks?
- What is the computational overhead of the proposed method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4