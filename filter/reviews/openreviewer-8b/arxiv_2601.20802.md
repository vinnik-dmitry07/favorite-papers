# Review

## Summary
This paper introduces Reinforcement Learning with Rich Feedback (RLRF), a framework that leverages tokenized feedback for improved credit assignment in reinforcement learning for large language models (LLMs). The authors propose Self-Distillation Policy Optimization (SDPO), which uses the model itself as a self-teacher, incorporating feedback to refine next-token predictions. SDPO is shown to outperform traditional RL methods by enhancing sample efficiency and accuracy across tasks like scientific reasoning and competitive programming. It also accelerates test-time problem-solving, achieving comparable results to best-of-$k$ sampling or multi-turn conversations with fewer attempts. The paper demonstrates SDPO’s effectiveness in environments with rich feedback, offering a promising approach for more efficient LLM training.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is simple and effective, and the results are promising.
- The paper conducts extensive experiments and ablation studies to demonstrate the effectiveness of the proposed method.

## Weaknesses
- The idea of self-distillation is not new, and the proposed method is a direct extension of the RLVR method GRPO. The novelty is somewhat limited.
- The experiments are conducted on only one RLVR baseline, GRPO. It would be better to include more RLVR baselines, such as STaR, which is also a popular method for LLM RL.
- The experiments are conducted on only one LLM family, Qwen. It would be better to include more LLM families, such as LLaMA and Gemma.

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4