## Reviewer

### Summary

This paper studies the effects of self-distillation on the reasoning ability of LLMs, specifically focusing on the mathematical reasoning tasks. The authors find that self-distillation can reduce response length while degrading performance, and they attribute this degradation to the suppression of epistemic verbalization. They conduct experiments to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. The authors conclude that the effectiveness of self-distillation is closely tied to how information is provided to the model and how the model expresses uncertainty during reasoning.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- This paper studies an important problem of self-distillation and its effects on the reasoning ability of LLMs, which is a timely and important topic.
- The paper is well-written and easy to follow.

### Weaknesses

- The authors only consider the math reasoning tasks, which is a very narrow scope. It is not clear whether the findings can be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on.
- The authors only consider the self-distillation methods, which is not a comprehensive study. It is not clear whether the findings can be generalized to other post-training methods, such as RLHF and so on.
- The authors only consider the Qwen3 and DeepSeek models, which is not a comprehensive study. It is not clear whether the findings can be generalized to other LLMs, such as LLaMA, Falcon, and so on.

### Questions

- In Section 3, the authors claim that the more privileged the information the teacher receives, such as the correct solution, the more its reasoning traces suppress expressions of uncertainty. However, it is not clear how to measure the privileged information. What is the definition of privileged information? Can you provide more details about this?
- In Section 4, the authors claim that training on solution-guided responses leads to substantial degradation across all benchmarks, despite the dataset consisting of correct answers. However, it is not clear why this is the case. What is the reason for this degradation? Can you provide more details about this?
- In Section 5, the authors claim that SDPO with c=s causes a sharp initial drop in both E[L(y)] and score. However, it is not clear why this is the case. What is the reason for this drop? Can you provide more details about this?
- In Section 6, the authors claim that the difference between GRPO and SDPO becomes more pronounced on OOD benchmarks. However, it is not clear why this is the case. What is the reason for this difference? Can you provide more details about this?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper investigates the phenomenon that self-distillation can degrade the reasoning capability of LLMs in mathematical reasoning tasks. The authors claim that the suppression of epistemic verbalization is the main reason for this phenomenon. They conduct experiments to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. They conclude that the effectiveness of self-distillation is closely tied to how information is provided to the model and how the model expresses uncertainty during reasoning.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors conduct extensive experiments to support their claims.

### Weaknesses

- The authors only consider the math reasoning tasks, which is a very narrow scope. It is not clear whether the findings can be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on.
- The authors only consider the self-distillation methods, which is not a comprehensive study. It is not clear whether the findings can be generalized to other post-training methods, such as RLHF and so on.
- The authors only consider the Qwen3 and DeepSeek models, which is not a comprehensive study. It is not clear whether the findings can be generalized to other LLMs, such as LLaMA, Falcon, and so on.
- The authors claim that the suppression of epistemic verbalization is the main reason for the phenomenon that self-distillation can degrade the reasoning capability of LLMs. However, they do not provide any theoretical analysis to support this claim. They only conduct empirical studies to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. However, this does not necessarily mean that the suppression of epistemic verbalization is the main reason for the phenomenon. There could be other reasons that are not considered in the paper.

### Questions

- What is the definition of epistemic verbalization? Why is it important for the reasoning capability of LLMs?
- Why does self-distillation suppress epistemic verbalization? What is the reason for this phenomenon?
- Why does the suppression of epistemic verbalization lead to the degradation of the reasoning capability of LLMs? What is the underlying reason for this phenomenon?
- Can the findings of this paper be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on?
- Can the findings of this paper be generalized to other post-training methods, such as RLHF and so on?
- Can the findings of this paper be generalized to other LLMs, such as LLaMA, Falcon, and so on?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper studies the effect of self-distillation on the reasoning ability of LLMs, particularly on the math reasoning tasks. The authors find that self-distillation can reduce response length while degrading performance, and they attribute this degradation to the suppression of epistemic verbalization. They conduct experiments to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. The authors conclude that the effectiveness of self-distillation is closely tied to how information is provided to the model and how the model expresses uncertainty during reasoning.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments to support their claims.

### Weaknesses

1. The authors only consider the math reasoning tasks, which is a very narrow scope. It is not clear whether the findings can be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on.
2. The authors only consider the self-distillation methods, which is not a comprehensive study. It is not clear whether the findings can be generalized to other post-training methods, such as RLHF and so on.
3. The authors only consider the Qwen3 and DeepSeek models, which is not a comprehensive study. It is not clear whether the findings can be generalized to other LLMs, such as LLaMA, Falcon, and so on.
4. The authors claim that the suppression of epistemic verbalization is the main reason for the phenomenon that self-distillation can degrade the reasoning capability of LLMs. However, they do not provide any theoretical analysis to support this claim. They only conduct empirical studies to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. However, this does not necessarily mean that the suppression of epistemic verbalization is the main reason for the phenomenon. There could be other reasons that are not considered in the paper.

### Questions

1. What is the definition of epistemic verbalization? Why is it important for the reasoning capability of LLMs?
2. Why does self-distillation suppress epistemic verbalization? What is the reason for this phenomenon?
3. Why does the suppression of epistemic verbalization lead to the degradation of the reasoning capability of LLMs? What is the underlying reason for this phenomenon?
4. Can the findings of this paper be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on?
5. Can the findings of this paper be generalized to other post-training methods, such as RLHF and so on?
6. Can the findings of this paper be generalized to other LLMs, such as LLaMA, Falcon, and so on?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper studies the effect of self-distillation on the reasoning ability of LLMs, particularly on the math reasoning tasks. The authors find that self-distillation can reduce response length while degrading performance, and they attribute this degradation to the suppression of epistemic verbalization. They conduct experiments to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. The authors conclude that the effectiveness of self-distillation is closely tied to how information is provided to the model and how the model expresses uncertainty during reasoning.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments to support their claims.
3. The paper provides a comprehensive analysis of the effect of self-distillation on the reasoning ability of LLMs, particularly on the math reasoning tasks.

### Weaknesses

1. The authors only consider the math reasoning tasks, which is a very narrow scope. It is not clear whether the findings can be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on.
2. The authors only consider the self-distillation methods, which is not a comprehensive study. It is not clear whether the findings can be generalized to other post-training methods, such as RLHF and so on.
3. The authors only consider the Qwen3 and DeepSeek models, which is not a comprehensive study. It is not clear whether the findings can be generalized to other LLMs, such as LLaMA, Falcon, and so on.
4. The authors claim that the suppression of epistemic verbalization is the main reason for the phenomenon that self-distillation can degrade the reasoning capability of LLMs. However, they do not provide any theoretical analysis to support this claim. They only conduct empirical studies to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. However, this does not necessarily mean that the suppression of epistemic verbalization is the main reason for the phenomenon. There could be other reasons that are not considered in the paper.

### Questions

1. What is the definition of epistemic verbalization? Why is it important for the reasoning capability of LLMs?
2. Why does self-distillation suppress epistemic verbalization? What is the reason for this phenomenon?
3. Why does the suppression of epistemic verbalization lead to the degradation of the reasoning capability of LLMs? What is the underlying reason for this phenomenon?
4. Can the findings of this paper be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on?
5. Can the findings of this paper be generalized to other post-training methods, such as RLHF and so on?
6. Can the findings of this paper be generalized to other LLMs, such as LLaMA, Falcon, and so on?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper studies the effects of self-distillation on the reasoning ability of LLMs, specifically focusing on the mathematical reasoning tasks. The authors find that self-distillation can reduce response length while degrading performance, and they attribute this degradation to the suppression of epistemic verbalization. They conduct experiments to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. The authors conclude that the effectiveness of self-distillation is closely tied to how information is provided to the model and how the model expresses uncertainty during reasoning.

The reviewers find that the paper is well-written and easy to follow. The authors conduct extensive experiments to support their claims. However, the reviewers also point out several weaknesses in the paper. For example, the authors only consider the math reasoning tasks, which is a very narrow scope. It is not clear whether the findings can be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on. The authors only consider the self-distillation methods, which is not a comprehensive study. It is not clear whether the findings can be generalized to other post-training methods, such as RLHF and so on. The authors only consider the Qwen3 and DeepSeek models, which is not a comprehensive study. It is not clear whether the findings can be generalized to other LLMs, such as LLaMA, Falcon, and so on. The authors claim that the suppression of epistemic verbalization is the main reason for the phenomenon that self-distillation can degrade the reasoning capability of LLMs. However, they do not provide any theoretical analysis to support this claim. They only conduct empirical studies to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. However, this does not necessarily mean that the suppression of epistemic verbalization is the main reason for the phenomenon. There could be other reasons that are not considered in the paper.

### justification_for_why_not_higher_score

The reviewers find that the paper is well-written and easy to follow. The authors conduct extensive experiments to support their claims. However, the reviewers also point out several weaknesses in the paper. For example, the authors only consider the math reasoning tasks, which is a very narrow scope. It is not clear whether the findings can be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on. The authors only consider the self-distillation methods, which is not a comprehensive study. It is not clear whether the findings can be generalized to other post-training methods, such as RLHF and so on. The authors only consider the Qwen3 and DeepSeek models, which is not a comprehensive study. It is not clear whether the findings can be generalized to other LLMs, such as LLaMA, Falcon, and so on. The authors claim that the suppression of epistemic verbalization is the main reason for the phenomenon that self-distillation can degrade the reasoning capability of LLMs. However, they do not provide any theoretical analysis to support this claim. They only conduct empirical studies to show that the performance of self-distillation is closely related to how information is provided to the model and how the model expresses uncertainty during reasoning. However, this does not necessarily mean that the suppression of epistemic verbalization is the main reason for the phenomenon. There could be other reasons that are not considered in the paper.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for presentation at the conference)