# Review

## Summary
The paper presents an extensive empirical study of various design choices in RL training of LLMs, focusing on a 8B model with reasoning tasks. The authors propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow, with clear explanations of the methodology and findings.
- The paper presents a comprehensive empirical study of various design choices in RL training of LLMs, which is a significant contribution to the field.
- The proposed ScaleRL recipe is effective and demonstrates predictable scaling up to 100,000 GPU-hours.

## Weaknesses
- The study focuses on a single model size (8B parameters) and a single task (reasoning), which may limit the generalizability of the findings to other model sizes and tasks.
- The paper does not provide a theoretical analysis of why certain design choices are more effective than others, which could provide deeper insights into the underlying mechanisms.
- The study does not extensively explore the potential trade-offs between different design choices, which could be helpful for practitioners trying to make informed decisions.
- The paper does not provide a clear framework for predicting the performance of new RL algorithms or design choices that are not included in the study.

## Questions
- How do the authors expect the findings to generalize to other model sizes and tasks? Have they conducted any preliminary experiments to investigate this?
- Can the authors provide more theoretical insights into why certain design choices are more effective than others in the RL context?
- What are the potential trade-offs between the design choices discussed in the paper? How do these trade-offs vary depending on the model size and task?
- How do the authors plan to incorporate the proposed framework into existing RL training pipelines? What are the practical implications for RL practitioners?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4