# Review

## Summary
This paper investigates the dynamics of on-policy distillation (OPD) for large language models, focusing on the conditions that influence its success or failure. The authors identify two key factors: (1) the student and teacher must share compatible thinking patterns, and (2) the teacher must offer new capabilities beyond what the student has learned during training. They validate these findings through controlled experiments and propose practical strategies to recover failing OPD, such as off-policy cold start and teacher-aligned prompt selection. The paper also explores the limitations of OPD, particularly the reward degradation over long trajectories, suggesting that OPD may not be suitable for all reasoning tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a systematic analysis of the conditions necessary for successful on-policy distillation, advancing the understanding of this technique.
2. The proposed practical strategies for recovering failing OPD, such as off-policy cold start and teacher-aligned prompt selection, are valuable insights for practitioners.
3. The investigation into the limitations of OPD, particularly the reward degradation over long trajectories, helps in setting realistic expectations and guides future research directions.

## Weaknesses
1. The experiments are primarily conducted on mathematical reasoning tasks. It would be beneficial to see how the findings generalize to other domains such as natural language understanding and generation.
2. The paper focuses on specific model families (Qwen and DeepSeek). Including more diverse architectures in the analysis could strengthen the claims.
3. The proposed strategies for improving OPD, such as off-policy cold start and teacher-aligned prompt selection, may introduce additional complexity in practical implementations.

## Questions
1. How do the findings generalize to other domains beyond mathematical reasoning? Have you considered conducting experiments in natural language understanding or generation tasks?
2. Your analysis focuses on specific model families (Qwen and DeepSeek). Do you expect the observed phenomena to hold for other architectures as well? Have you conducted any preliminary experiments with different models?
3. The proposed strategies (off-policy cold start and teacher-aligned prompt selection) add complexity to the implementation. How feasible are these strategies in practical settings, and what is their computational cost?
4. The paper identifies the degradation of reward quality with trajectory depth as a limitation of OPD. Have you explored any potential solutions to mitigate this issue, such as adaptive reward weighting or curriculum learning approaches?
5. How do the proposed strategies interact with existing techniques for improving language models, such as supervised fine-tuning or reinforcement learning from human feedback?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4