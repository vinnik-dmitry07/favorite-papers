# Review

## Summary
This paper proposes an online RL framework, Critique-GRPO, which combines numerical and natural language feedback to enhance the reasoning abilities of LLMs. Critique-GRPO addresses the limitations of numerical-only feedback by incorporating natural language critiques, allowing LLMs to refine failed solutions and improve performance. The framework enables simultaneous learning from initial responses and critique-guided refinements, achieving significant performance gains on various reasoning tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper identifies key limitations of RL with numerical feedback and demonstrates how natural language critiques can overcome these limitations.
2. The paper proposes a novel online RL framework that effectively combines numerical and natural language feedback for policy optimization.
3. The paper provides extensive experimental results showing that Critique-GRPO outperforms existing supervised and RL-based fine-tuning methods across multiple reasoning tasks.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational cost of Critique-GRPO compared to other methods.
2. The paper does not extensively discuss the potential biases that may be introduced by the natural language feedback, such as the quality of the critiques.
3. The paper does not provide a thorough error analysis to understand the types of errors that Critique-GRPO is most effective at correcting.

## Questions
1. How does the computational cost of Critique-GRPO compare to other state-of-the-art methods, and what are the trade-offs in terms of performance versus efficiency?
2. How does the quality of the natural language critiques affect the performance of Critique-GRPO, and how can the reliability of the critiques be ensured?
3. Can you provide an error analysis to understand the types of errors that Critique-GRPO is most effective at correcting and which types of errors persist despite the use of natural language feedback?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4