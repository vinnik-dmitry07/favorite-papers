# Review

## Summary
This paper analyzes the effect of RL fine-tuning on LLMs for reasoning tasks. They show that the effect of RL is concentrated on a small number of tokens in the generation trajectory, specifically at points where the model is uncertain (high entropy). They further show that it is possible to achieve similar performance to RL fine-tuning by only fine-tuning a small adapter module on these positions.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
- The paper is well written and easy to follow
- The analysis is quite thorough and supports the paper's claims
- The proposed method is efficient and effective

## Weaknesses
- The paper focuses on reasoning tasks, so it is not clear how well the results generalize to other tasks
- The paper does not have a discussion of the limitations of the proposed method

## Questions
- How well does the proposed method generalize to other tasks? For example, what about tasks that are not so "linear" in the sense that the correct solution might not be among the top 5 tokens?
- What are the limitations of the proposed method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4