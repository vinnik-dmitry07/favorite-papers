## Reviewer

### Summary

This paper studies the Group Relative Policy Optimization (GRPO) algorithm, which is a critic-free variant of PPO for post-training large language models (LLMs). The authors argue that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. This perspective motivates 2-GRPO, a minimal group-size variant that constructs contrastive signals with only two rollouts. The authors provide a rigorous theoretical analysis of 2-GRPO and empirically validate its effectiveness.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors propose a new perspective on GRPO, which is that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. This perspective motivates 2-GRPO, a minimal group-size variant that constructs contrastive signals with only two rollouts.

### Weaknesses

1. The authors only provide a theoretical analysis of 2-GRPO and empirical results on a single dataset. The authors should provide more empirical results on other datasets to validate the effectiveness of 2-GRPO.
2. The authors should provide more details about the implementation of 2-GRPO and the hyperparameters used in the experiments.
3. The authors should provide more discussion on the limitations of 2-GRPO and potential future work.

### Questions

See Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the Group Relative Policy Optimization (GRPO) algorithm, which is a critic-free variant of PPO for post-training large language models (LLMs). The authors argue that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. This perspective motivates 2-GRPO, a minimal group-size variant that constructs contrastive signals with only two rollouts. The authors provide a rigorous theoretical analysis of 2-GRPO and empirically validate its effectiveness.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors propose a new perspective on GRPO, which is that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. This perspective motivates 2-GRPO, a minimal group-size variant that constructs contrastive signals with only two rollouts.

### Weaknesses

1. The authors only provide a theoretical analysis of 2-GRPO and empirical results on a single dataset. The authors should provide more empirical results on other datasets to validate the effectiveness of 2-GRPO.
2. The authors should provide more details about the implementation of 2-GRPO and the hyperparameters used in the experiments.
3. The authors should provide more discussion on the limitations of 2-GRPO and potential future work.

### Questions

See Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the Group Relative Policy Optimization (GRPO) algorithm, which is a critic-free variant of PPO for post-training large language models (LLMs). The authors argue that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. This perspective motivates 2-GRPO, a minimal group-size variant that constructs contrastive signals with only two rollouts. The authors provide a rigorous theoretical analysis of 2-GRPO and empirically validate its effectiveness.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors propose a new perspective on GRPO, which is that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. This perspective motivates 2-GRPO, a minimal group-size variant that constructs contrastive signals with only two rollouts.

### Weaknesses

1. The authors only provide a theoretical analysis of 2-GRPO and empirical results on a single dataset. The authors should provide more empirical results on other datasets to validate the effectiveness of 2-GRPO.
2. The authors should provide more details about the implementation of 2-GRPO and the hyperparameters used in the experiments.
3. The authors should provide more discussion on the limitations of 2-GRPO and potential future work.

### Questions

See Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents a new perspective on the GRPO algorithm, which is a popular method for post-training large language models (LLMs). The authors argue that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. The authors propose a minimal group-size variant, 2-GRPO, that constructs contrastive signals with only two rollouts. They provide a rigorous theoretical analysis of 2-GRPO and empirically validate its effectiveness.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The authors propose a new perspective on GRPO, which is that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. This perspective motivates 2-GRPO, a minimal group-size variant that constructs contrastive signals with only two rollouts.

### Weaknesses

- The authors only provide a theoretical analysis of 2-GRPO and empirical results on a single dataset. The authors should provide more empirical results on other datasets to validate the effectiveness of 2-GRPO.
- The authors should provide more details about the implementation of 2-GRPO and the hyperparameters used in the experiments.
- The authors should provide more discussion on the limitations of 2-GRPO and potential future work.

### Questions

See Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the Group Relative Policy Optimization (GRPO) algorithm, which is a critic-free variant of PPO for post-training large language models (LLMs). The authors argue that the efficacy of GRPO stems from its implicit contrastive objective in the optimization, which helps reduce variance via the control variate method. This makes GRPO structurally related to preference learning methods such as DPO. This perspective motivates 2-GRPO, a minimal group-size variant that constructs contrastive signals with only two rollouts. The authors provide a rigorous theoretical analysis of 2-GRPO and empirically validate its effectiveness.

The paper received 4 reviews, with 3 of them giving a rating of 5 (marginally below the acceptance threshold) and 1 giving a rating of 6 (marginally above the acceptance threshold). The authors provided a detailed response to the reviewers' comments, but unfortunately, the reviewers did not respond to the authors' response. Based on the reviews and the authors' response, the AC recommends rejecting the paper.

### justification_for_why_not_higher_score

The paper received 4 reviews, with 3 of them giving a rating of 5 (marginally below the acceptance threshold) and 1 giving a rating of 6 (marginally above the acceptance threshold). The authors provided a detailed response to the reviewers' comments, but unfortunately, the reviewers did not respond to the authors' response. Based on the reviews and the authors' response, the AC recommends rejecting the paper.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (poster)