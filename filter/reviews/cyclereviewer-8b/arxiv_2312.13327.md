## Reviewer

### Summary

This paper proposes a new method called Headless-AD, which is a variant of Algorithm Distillation (AD) that can generalize to environments with variable action spaces. The main idea is to remove the final linear layer in AD and use a random embedding for each action. The paper also introduces a contrastive loss to train the model. The paper shows that Headless-AD can generalize to new action spaces and outperform AD in some cases.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The paper provides a thorough analysis of the proposed method.

### Weaknesses

- The novelty of the proposed method is limited. The main idea of using random embeddings for actions is not new and has been used in previous work [1]. The contrastive loss is also not new.
- The experiments are not sufficient. The paper only evaluates the proposed method on simple environments such as Bernoulli bandit and Darkroom. More complex environments are needed to show the effectiveness of the proposed method.
- The paper does not compare with other baselines. The paper only compares with AD, but there are other methods that can handle variable action spaces, such as [2,3].

[1] Kirsch, A., Kuhn, D., & Geist, M. (2023). SymLA: Symmetry Learning for Adaptable Transformers. arXiv preprint arXiv:2305.19347.

[2] Ye, C., Zhang, X., & Li, Y. (2023). In-context reinforcement learning with variable action spaces. arXiv preprint arXiv:2306.15465.

[3] Lu, Z., Chen, Y., & Li, L. (2023). Learning to learn with variable action spaces. arXiv preprint arXiv:2307.16194.

### Questions

- What is the novelty of the proposed method compared to existing methods?
- Can you provide more experiments on more complex environments?
- Can you compare with other baselines?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper presents a new approach to address the challenge of adapting reinforcement learning (RL) models to new action spaces. The authors propose a modified version of the Algorithm Distillation (AD) model, called Headless-AD, which is trained to predict action embeddings rather than action probabilities. This modification enables the model to generalize to action spaces of varying sizes and structures without requiring retraining. The paper demonstrates the effectiveness of Headless-AD through experiments in Bernoulli and contextual bandits, as well as in a gridworld environment. The results show that Headless-AD can outperform specialized models trained for specific action spaces, especially in larger action sets.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a clear explanation of the problem and the proposed solution. The experimental results are comprehensive and demonstrate the effectiveness of the proposed approach.

### Weaknesses

The novelty of the proposed approach is limited. The idea of using action embeddings rather than action probabilities is not new. The authors should provide a more detailed discussion of the differences between their approach and existing methods.

The paper does not provide a thorough comparison with existing methods. The authors should compare their approach with other state-of-the-art methods in the field.

The experiments are limited to a small set of environments. The authors should provide more comprehensive experiments in a wider range of environments to demonstrate the generalizability of the proposed approach.

### Questions

See weaknesses

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new architecture for Algorithm Distillation (AD) that is capable of generalizing to environments with variable action spaces. The main idea is to remove the final linear layer in AD and use a random embedding for each action. The paper shows that the proposed method can generalize to new action spaces and outperform AD in some cases.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The paper provides a thorough analysis of the proposed method.

### Weaknesses

- The novelty of the proposed method is limited. The main idea of using random embeddings for actions is not new and has been used in previous work [1]. The contrastive loss is also not new.
- The experiments are not sufficient. The paper only evaluates the proposed method on simple environments such as Bernoulli bandit and Darkroom. More complex environments are needed to show the effectiveness of the proposed method.
- The paper does not compare with other baselines. The paper only compares with AD, but there are other methods that can handle variable action spaces, such as [2,3].

[1] Kirsch, A., Kuhn, D., & Geist, M. (2023). SymLA: Symmetry Learning for Adaptable Transformers. arXiv preprint arXiv:2305.19347.

[2] Ye, C., Zhang, X., & Li, Y. (2023). In-context reinforcement learning with variable action spaces. arXiv preprint arXiv:2306.15465.

[3] Lu, Z., Chen, Y., & Li, L. (2023). Learning to learn with variable action spaces. arXiv preprint arXiv:2307.16194.

### Questions

- What is the novelty of the proposed method compared to existing methods?
- Can you provide more experiments on more complex environments?
- Can you compare with other baselines?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new architecture for Algorithm Distillation (AD) that is capable of generalizing to environments with variable action spaces. The main idea is to remove the final linear layer in AD and use a random embedding for each action. The paper shows that the proposed method can generalize to new action spaces and outperform AD in some cases.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and effective. The paper provides a thorough analysis of the proposed method.

### Weaknesses

The novelty of the proposed method is limited. The main idea of using random embeddings for actions is not new and has been used in previous work [1]. The contrastive loss is also not new.

The experiments are not sufficient. The paper only evaluates the proposed method on simple environments such as Bernoulli bandit and Darkroom. More complex environments are needed to show the effectiveness of the proposed method.

The paper does not compare with other baselines. The paper only compares with AD, but there are other methods that can handle variable action spaces, such as [2,3].

[1] Kirsch, A., Kuhn, D., & Geist, M. (2023). SymLA: Symmetry Learning for Adaptable Transformers. arXiv preprint arXiv:2305.19347.

[2] Ye, C., Zhang, X., & Li, Y. (2023). In-context reinforcement learning with variable action spaces. arXiv preprint arXiv:2306.15465.

[3] Lu, Z., Chen, Y., & Li, L. (2023). Learning to learn with variable action spaces. arXiv preprint arXiv:2307.16194.

### Questions

What is the novelty of the proposed method compared to existing methods?

Can you provide more experiments on more complex environments?

Can you compare with other baselines?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a modification to Algorithm Distillation (AD) for reinforcement learning, called Headless-AD, which can generalize to environments with variable action spaces. The authors propose a modified version of the Algorithm Distillation (AD) model, called Headless-AD, which is trained to predict action embeddings rather than action probabilities. This modification enables the model to generalize to action spaces of varying sizes and structures without requiring retraining. The paper demonstrates the effectiveness of Headless-AD through experiments in Bernoulli and contextual bandits, as well as in a gridworld environment. The results show that Headless-AD can outperform specialized models trained for specific action spaces, especially in larger action sets. However, the reviewers raised several concerns about the novelty of the proposed approach, the limited scope of the experiments, and the lack of comparison with other baselines. The authors did not provide any rebuttal.

### justification_for_why_not_higher_score

The reviewers raised several concerns about the novelty of the proposed approach, the limited scope of the experiments, and the lack of comparison with other baselines.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication for ICLR 2024)