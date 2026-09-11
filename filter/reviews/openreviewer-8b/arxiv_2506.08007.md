# Review

## Summary
This paper introduces Reinforcement Pre-Training (RPT), a new pre-training paradigm for large language models that reframes next-token prediction as a reasoning task using reinforcement learning (RL). Unlike traditional next-token prediction, RPT incorporates a chain-of-thought process before predicting the next token, using intrinsic rewards based on prediction accuracy. Experiments show that RPT improves next-token prediction accuracy, enhances performance on reasoning benchmarks, and provides a strong foundation for subsequent RL fine-tuning.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written, with clear explanations of the RPT method, experimental setup, and results.
2. The paper introduces a novel pre-training paradigm, RPT, which reframes next-token prediction as a reasoning task using RL, offering a fresh perspective on pre-training large language models.
3. The paper provides a detailed analysis of the reasoning patterns developed by the RPT model, highlighting its potential to improve reasoning capabilities.

## Weaknesses
1. The experiments are primarily conducted on a 14B parameter model and mathematical datasets. Broader testing on various domains and larger scales would strengthen the generalizability of the findings.
2. The paper lacks a direct comparison with other pre-training methods, such as standard next-token prediction or other RL-based approaches, to contextualize the benefits of RPT.
3. The paper does not provide a detailed analysis of the computational cost of the RPT method compared to standard pre-training approaches.
4. The paper could benefit from a more detailed discussion on the potential drawbacks or failure cases of the RPT method.

## Questions
1. How does the computational cost of RPT compare to standard next-token prediction pre-training methods?
2. Have you considered testing RPT on non-mathematical datasets? What challenges do you anticipate in such domains?
3. How does RPT compare to other RL-based pre-training methods, if any exist, or to standard next-token prediction in terms of performance and efficiency?
4. Are there any specific limitations or failure cases of the RPT method that you have observed?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4