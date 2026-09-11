## Reviewer

### Summary

The paper studies the effect of spurious rewards in RLHF for improving mathematical reasoning of LLMs. They find that even spurious rewards such as random rewards can lead to significant improvements in performance. They hypothesize that this is because of the clipping bias in the GRPO algorithm and that the model is able to exploit the existing pre-existing behaviors. They conduct experiments on several models and find that the effect is model-dependent and that the model with code reasoning is able to exploit the spurious rewards.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper studies an important problem of spurious rewards in RLHF and its impact on the performance of LLMs.
- The paper is well-written and easy to follow.
- The paper conducts extensive experiments on several models and finds that the effect of spurious rewards is model-dependent.

### Weaknesses

- The paper does not provide a clear explanation for why spurious rewards can lead to improvements in performance. The authors hypothesize that it is due to the clipping bias in GRPO, but this is not clearly explained. It would be helpful if the authors could provide a more detailed explanation of this phenomenon.
- The paper only considers a single type of spurious reward, which is random rewards. It would be helpful if the authors could consider other types of spurious rewards and analyze their effect on performance.
- The paper does not provide a clear conclusion or recommendation for how to handle spurious rewards in RLHF. It would be helpful if the authors could provide some guidance on how to design effective rewards that do not lead to spurious improvements.

### Questions

- How do the results change if the models are not pre-trained on mathematical reasoning tasks?
- How do the results change if the models are not fine-tuned on the same dataset?
- How do the results change if the reward is not binary (0 or 1)?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper investigates the effect of spurious rewards in RLHF for improving mathematical reasoning of LLMs. The authors find that even spurious rewards such as random rewards can lead to significant improvements in performance. They hypothesize that this is because of the clipping bias in the GRPO algorithm and that the model is able to exploit the existing pre-existing behaviors. They conduct experiments on several models and find that the effect is model-dependent and that the model with code reasoning is able to exploit the spurious rewards.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper studies an important problem of spurious rewards in RLHF and its impact on the performance of LLMs.
- The paper is well-written and easy to follow.
- The paper conducts extensive experiments on several models and finds that the effect of spurious rewards is model-dependent.

### Weaknesses

- The paper does not provide a clear explanation for why spurious rewards can lead to improvements in performance. The authors hypothesize that it is due to the clipping bias in GRPO, but this is not clearly explained. It would be helpful if the authors could provide a more detailed explanation of this phenomenon.
- The paper only considers a single type of spurious reward, which is random rewards. It would be helpful if the authors could consider other types of spurious rewards and analyze their effect on performance.
- The paper does not provide a clear conclusion or recommendation for how to handle spurious rewards in RLHF. It would be helpful if the authors could provide some guidance on how to design effective rewards that do not lead to spurious improvements.

### Questions

- How do the results change if the models are not pre-trained on mathematical reasoning tasks?
- How do the results change if the models are not fine-tuned on the same dataset?
- How do the results change if the reward is not binary (0 or 1)?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper investigates the impact of spurious rewards on the performance of reinforcement learning with verifiable rewards (RLVR) in language models. The authors demonstrate that RLVR can significantly improve math reasoning in language models even when using spurious rewards that have little to no correlation with the correct answer. They identify a phenomenon called "code reasoning" in Qwen2.5-Math models, where the model uses code to support mathematical reasoning without executing it. The authors show that the presence of code reasoning is highly model-dependent and that spurious rewards can amplify existing behaviors in the model. They conclude that RLVR outcomes are significantly affected by the base model's pre-training and that spurious rewards can enhance reasoning when they trigger useful existing behaviors. The paper highlights the importance of testing RL methods across diverse models and using multiple baselines when evaluating reinforcement learning techniques.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper presents a novel and interesting finding that RLVR can improve language model performance even with spurious rewards that have little to no correlation with the correct answer.
- The paper provides a detailed analysis of the phenomenon of code reasoning in Qwen2.5-Math models and its impact on RLVR outcomes.
- The paper highlights the importance of testing RL methods across diverse models and using multiple baselines when evaluating reinforcement learning techniques.
- The paper provides a comprehensive analysis of the impact of spurious rewards on RLVR outcomes and identifies the limitations of existing research that relies on a single model family.

### Weaknesses

- The paper does not provide a clear explanation for why spurious rewards can lead to improvements in performance. The authors hypothesize that it is due to the clipping bias in GRPO, but this is not clearly explained. It would be helpful if the authors could provide a more detailed explanation of this phenomenon.
- The paper only considers a single type of spurious reward, which is random rewards. It would be helpful if the authors could consider other types of spurious rewards and analyze their effect on performance.
- The paper does not provide a clear conclusion or recommendation for how to handle spurious rewards in RLHF. It would be helpful if the authors could provide some guidance on how to design effective rewards that do not lead to spurious improvements.

### Questions

- How do the results change if the models are not pre-trained on mathematical reasoning tasks?
- How do the results change if the models are not fine-tuned on the same dataset?
- How do the results change if the reward is not binary (0 or 1)?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the impact of spurious rewards on RLHF for language models. The authors find that spurious rewards, such as random rewards, can lead to significant improvements in performance. They hypothesize that this is due to the clipping bias in the GRPO algorithm and that the model is able to exploit the existing pre-existing behaviors. They conduct experiments on several models and find that the effect is model-dependent and that the model with code reasoning is able to exploit the spurious rewards.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper studies an important problem of spurious rewards in RLHF and its impact on the performance of LLMs.
- The paper is well-written and easy to follow.
- The paper conducts extensive experiments on several models and finds that the effect of spurious rewards is model-dependent.

### Weaknesses

- The paper does not provide a clear explanation for why spurious rewards can lead to improvements in performance. The authors hypothesize that it is due to the clipping bias in GRPO, but this is not clearly explained. It would be helpful if the authors could provide a more detailed explanation of this phenomenon.
- The paper only considers a single type of spurious reward, which is random rewards. It would be helpful if the authors could consider other types of spurious rewards and analyze their effect on performance.
- The paper does not provide a clear conclusion or recommendation for how to handle spurious rewards in RLHF. It would be helpful if the authors could provide some guidance on how to design effective rewards that do not lead to spurious improvements.

### Questions

- How do the results change if the models are not pre-trained on mathematical reasoning tasks?
- How do the results change if the models are not fine-tuned on the same dataset?
- How do the results change if the reward is not binary (0 or 1)?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the effect of spurious rewards in RLHF for improving mathematical reasoning of LLMs. The authors find that even spurious rewards such as random rewards can lead to significant improvements in performance. They hypothesize that this is because of the clipping bias in the GRPO algorithm and that the model is able to exploit the existing pre-existing behaviors. They conduct experiments on several models and find that the effect is model-dependent and that the model with code reasoning is able to exploit the spurious rewards.

The reviewers have raised several questions regarding the clarity of the paper and the novelty of the findings. The authors have provided detailed responses to these questions and have made significant revisions to the paper. The reviewers have acknowledged the authors' responses and have revised their scores accordingly. The paper is borderline and I recommend acceptance.

### justification_for_why_not_higher_score

The paper is borderline.

### justification_for_why_not_lower_score

The paper is borderline.

**********

## Paper Decision

Accept (poster)