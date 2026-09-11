## Reviewer

### Summary

This paper proposes a new pre-training objective, reinforcement pre-training (RPT), which frames next-token prediction as a reasoning task trained with reinforcement learning. The authors claim that RPT offers a scalable and general-purpose approach to RL pre-training, minimizing reward hacking through rule-based rewards and promoting generalization by encouraging next-token reasoning patterns over rote memorization.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.

### Weaknesses

1. The authors claim that RPT offers a scalable and general-purpose approach to RL pre-training, but the authors only conduct experiments on a small-scale model (14B) and a specific dataset (mathematical documents). The authors should conduct experiments on large-scale models (e.g., 70B, 130B) and general-domain text.
2. The authors claim that RPT minimizes reward hacking through rule-based rewards, but the authors do not provide any evidence to support this claim. The authors should provide a comparison with other RL pre-training methods to demonstrate the effectiveness of RPT in minimizing reward hacking.
3. The authors claim that RPT promotes generalization by encouraging next-token reasoning patterns over rote memorization, but the authors do not provide any evidence to support this claim. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in promoting generalization.
4. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in improving next-token prediction accuracy.
5. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in providing a stronger pre-trained foundation for subsequent reinforcement fine-tuning.

### Questions

Please refer to the weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new pre-training approach called reinforcement pre-training (RPT) to improve the next-token prediction accuracy of LLMs. The authors propose to train LLMs to perform next-token reasoning via on-policy reinforcement learning. The reward is based on the correctness of the prediction. The authors show that RPT improves the next-token prediction accuracy and reasoning abilities of LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple and easy to understand.
2. The authors show that RPT improves the next-token prediction accuracy and reasoning abilities of LLMs.
3. The authors show that RPT provides a stronger pre-trained foundation for subsequent reinforcement fine-tuning.

### Weaknesses

1. The authors only conduct experiments on a small-scale model (14B) and a specific dataset (mathematical documents). The authors should conduct experiments on large-scale models (e.g., 70B, 130B) and general-domain text.
2. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in improving next-token prediction accuracy.
3. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in providing a stronger pre-trained foundation for subsequent reinforcement fine-tuning.

### Questions

1. The authors only conduct experiments on a small-scale model (14B) and a specific dataset (mathematical documents). The authors should conduct experiments on large-scale models (e.g., 70B, 130B) and general-domain text.
2. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in improving next-token prediction accuracy.
3. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in providing a stronger pre-trained foundation for subsequent reinforcement fine-tuning.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new pre-training method for LLMs, which is called Reinforcement Pre-Training (RPT). The authors propose to reframe next-token prediction as a reasoning task trained using RL, where the model receives verifiable rewards for correctly predicting the next token for a given context. The paper claims that RPT offers a scalable method to leverage vast amounts of text data for general-purpose RL, rather than relying on domain-specific annotated answers. The paper also claims that RPT provides a strong pre-trained foundation for further reinforcement fine-tuning. The paper also shows that RPT significantly improves the language modeling accuracy of predicting the next tokens.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper proposes a novel pre-training method for LLMs, which is called Reinforcement Pre-Training (RPT). The paper claims that RPT offers a scalable method to leverage vast amounts of text data for general-purpose RL, rather than relying on domain-specific annotated answers. The paper also claims that RPT provides a strong pre-trained foundation for further reinforcement fine-tuning. The paper also shows that RPT significantly improves the language modeling accuracy of predicting the next tokens.

2. The paper is well-written and easy to follow.

### Weaknesses

1. The paper claims that RPT offers a scalable method to leverage vast amounts of text data for general-purpose RL, rather than relying on domain-specific annotated answers. However, the paper only evaluates RPT on a single dataset, which is OmniMATH. The paper should evaluate RPT on more datasets to demonstrate its generalizability.

2. The paper claims that RPT provides a strong pre-trained foundation for further reinforcement fine-tuning. However, the paper only evaluates RPT on a single downstream task, which is SuperGPQA. The paper should evaluate RPT on more downstream tasks to demonstrate its effectiveness.

3. The paper claims that RPT significantly improves the language modeling accuracy of predicting the next tokens. However, the paper only evaluates RPT on a single metric, which is next-token prediction accuracy. The paper should evaluate RPT on more metrics to demonstrate its effectiveness.

4. The paper claims that RPT offers a scalable method to leverage vast amounts of text data for general-purpose RL. However, the paper only evaluates RPT on a single scale, which is 14B parameters. The paper should evaluate RPT on more scales to demonstrate its scalability.

### Questions

1. The paper claims that RPT offers a scalable method to leverage vast amounts of text data for general-purpose RL. However, the paper only evaluates RPT on a single scale, which is 14B parameters. The paper should evaluate RPT on more scales to demonstrate its scalability.

2. The paper claims that RPT provides a strong pre-trained foundation for further reinforcement fine-tuning. However, the paper only evaluates RPT on a single downstream task, which is SuperGPQA. The paper should evaluate RPT on more downstream tasks to demonstrate its effectiveness.

3. The paper claims that RPT significantly improves the language modeling accuracy of predicting the next tokens. However, the paper only evaluates RPT on a single metric, which is next-token prediction accuracy. The paper should evaluate RPT on more metrics to demonstrate its effectiveness.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new pre-training method, reinforcement pre-training (RPT), which frames next-token prediction as a reasoning task trained with reinforcement learning. The authors claim that RPT offers a scalable and general-purpose approach to RL pre-training, minimizing reward hacking through rule-based rewards and promoting generalization by encouraging next-token reasoning patterns over rote memorization. The paper presents experiments demonstrating that RPT improves next-token prediction accuracy and reasoning abilities of LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The paper presents experiments demonstrating that RPT improves next-token prediction accuracy and reasoning abilities of LLMs.

### Weaknesses

1. The authors only conduct experiments on a small-scale model (14B) and a specific dataset (mathematical documents). The authors should conduct experiments on large-scale models (e.g., 70B, 130B) and general-domain text.
2. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in improving next-token prediction accuracy.
3. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in providing a stronger pre-trained foundation for subsequent reinforcement fine-tuning.

### Questions

1. The authors only conduct experiments on a small-scale model (14B) and a specific dataset (mathematical documents). The authors should conduct experiments on large-scale models (e.g., 70B, 130B) and general-domain text.
2. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in improving next-token prediction accuracy.
3. The authors should provide a comparison with other pre-training methods to demonstrate the effectiveness of RPT in providing a stronger pre-trained foundation for subsequent reinforcement fine-tuning.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a new pre-training approach called reinforcement pre-training (RPT) to improve the next-token prediction accuracy of LLMs. The authors propose to train LLMs to perform next-token reasoning via on-policy reinforcement learning. The reward is based on the correctness of the prediction. The authors show that RPT improves the next-token prediction accuracy and reasoning abilities of LLMs.

The paper is well-written and easy to follow. The proposed method is simple and easy to understand. However, the paper only conducts experiments on a small-scale model (14B) and a specific dataset (mathematical documents). The authors should conduct experiments on large-scale models (e.g., 70B, 130B) and general-domain text.

### justification_for_why_not_higher_score

The paper only conducts experiments on a small-scale model (14B) and a specific dataset (mathematical documents). The authors should conduct experiments on large-scale models (e.g., 70B, 130B) and general-domain text.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)