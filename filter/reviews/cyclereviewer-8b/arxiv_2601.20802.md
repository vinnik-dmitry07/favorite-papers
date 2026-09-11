## Reviewer

### Summary

The paper proposes a new method called Self-Distillation Policy Optimization (SDPO) for reinforcement learning with rich feedback. The method is based on the idea of using the current policy as a self-teacher, which is prompted with the question and the rich feedback, and then distilling the feedback-informed next-token predictions back into the policy. The paper evaluates SDPO on three online RL settings: learning without rich feedback, learning with rich feedback, and discovering novel solutions to hard tasks at test-time. The results show that SDPO outperforms baselines in terms of sample efficiency and final accuracy.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper proposes a novel method called Self-Distillation Policy Optimization (SDPO) for reinforcement learning with rich feedback.
2. The paper evaluates SDPO on three online RL settings: learning without rich feedback, learning with rich feedback, and discovering novel solutions to hard tasks at test-time.
3. The results show that SDPO outperforms baselines in terms of sample efficiency and final accuracy.

### Weaknesses

1. The paper does not provide a clear motivation for the proposed method. The paper states that the key limitation is not RL per se, but the information bottleneck imposed by scalar outcome rewards. However, it is not clear why this is the case or how the proposed method addresses this limitation.
2. The paper does not provide a clear explanation of the proposed method. The paper states that the method uses the current policy as a self-teacher, which is prompted with the question and the rich feedback, and then distills the feedback-informed next-token predictions back into the policy. However, it is not clear how this is done or what the specific steps are.
3. The paper does not provide a clear evaluation of the proposed method. The paper states that the method is evaluated on three online RL settings: learning without rich feedback, learning with rich feedback, and discovering novel solutions to hard tasks at test-time. However, it is not clear what the specific metrics are or how they are calculated.
4. The paper does not provide a clear comparison to existing methods. The paper states that the method is compared to baselines, but it is not clear what the specific baselines are or how they are compared.
5. The paper does not provide a clear discussion of the limitations of the proposed method. The paper states that the method has limitations, but it is not clear what they are or how they can be addressed.

### Questions

1. Can you provide a clear motivation for the proposed method?
2. Can you provide a clear explanation of the proposed method?
3. Can you provide a clear evaluation of the proposed method?
4. Can you provide a clear comparison to existing methods?
5. Can you provide a clear discussion of the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces Self-Distillation Policy Optimization (SDPO), a reinforcement learning method that utilizes the model's ability to learn from context for dense credit assignment. The authors demonstrate that SDPO can be implemented as a minimal, drop-in modification to standard RLVR pipelines. Empirical results show that SDPO achieves superior sample efficiency and wall-clock convergence compared to GRPO on reasoning tasks, even when training in standard RLVR environments without rich feedback.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using self-distillation for credit assignment is novel and interesting.
3. The empirical results demonstrate the effectiveness of SDPO in improving sample efficiency and wall-clock convergence compared to GRPO.

### Weaknesses

1. The paper lacks a clear discussion on the limitations of the proposed method. It would be beneficial to include a section on limitations and potential future work to provide a more comprehensive understanding of the method's scope and potential applications.
2. The paper could benefit from a more detailed explanation of the experimental setup, including the specific datasets used, the evaluation metrics employed, and the hyperparameter choices made for the baselines and the proposed method. Providing more details on these aspects would enhance the reproducibility of the results and allow for a more thorough understanding of the experimental design.
3. The paper could be improved by including more discussion on the potential applications of the proposed method. While the paper demonstrates the effectiveness of SDPO on reasoning tasks, it would be beneficial to explore other potential domains where the method could be applied and how it could be adapted to suit different use cases.

### Questions

1. How does the proposed method compare to other reinforcement learning algorithms in terms of sample efficiency and wall-clock convergence?
2. Can the proposed method be applied to other domains beyond reasoning tasks?
3. How does the proposed method handle the credit assignment bottleneck in reinforcement learning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces a novel approach to reinforcement learning with language models, focusing on the use of rich feedback from the environment. The authors propose Self-Distillation Policy Optimization (SDPO), which leverages the model's ability to learn from context and distills feedback-informed next-token predictions back into the policy. This approach addresses the credit-assignment bottleneck in RL with verifiable rewards and demonstrates improved sample efficiency and final accuracy in scientific reasoning, tool use, and competitive programming tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to reinforcement learning with language models, focusing on the use of rich feedback from the environment. This approach addresses the credit-assignment bottleneck in RL with verifiable rewards and demonstrates improved sample efficiency and final accuracy in scientific reasoning, tool use, and competitive programming tasks.

2. The paper is well-written and easy to follow, with a clear presentation of the proposed method and its evaluation.

3. The experimental results demonstrate the effectiveness of SDPO in improving sample efficiency and wall-clock convergence compared to GRPO.

### Weaknesses

1. The paper could benefit from a more detailed discussion on the limitations of the proposed method. It would be beneficial to include a section on limitations and potential future work to provide a more comprehensive understanding of the method's scope and potential applications.

2. The paper could be improved by including more discussion on the potential applications of the proposed method. While the paper demonstrates the effectiveness of SDPO on reasoning tasks, it would be beneficial to explore other potential domains where the method could be applied and how it could be adapted to suit different use cases.

### Questions

1. How does the proposed method compare to other reinforcement learning algorithms in terms of sample efficiency and wall-clock convergence?
2. Can the proposed method be applied to other domains beyond reasoning tasks?
3. How does the proposed method handle the credit assignment bottleneck in reinforcement learning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new algorithm, Self-Distillation Policy Optimization (SDPO), for reinforcement learning with rich feedback. The authors show that SDPO is a policy gradient algorithm whose advantages are estimated using the self-teacher. They evaluate SDPO in three online RL settings: learning without rich feedback, learning with rich feedback, and discovering novel solutions to hard tasks at test-time. The results show that SDPO outperforms baselines in terms of sample efficiency and final accuracy.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well written and easy to follow.
2. The proposed method is novel and interesting.
3. The experimental results are convincing.

### Weaknesses

1. The authors should provide more details about the implementation of the proposed method.
2. The authors should provide more details about the experimental settings.

### Questions

1. How does the proposed method compare to other reinforcement learning algorithms in terms of sample efficiency and final accuracy?
2. Can the proposed method be applied to other domains beyond reasoning tasks?
3. How does the proposed method handle the credit assignment bottleneck in reinforcement learning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces a new method for reinforcement learning with rich feedback, called Self-Distillation Policy Optimization (SDPO). The method uses the current policy as a self-teacher, which is prompted with the question and the rich feedback, and then distills the feedback-informed next-token predictions back into the policy. The paper evaluates SDPO on three online RL settings: learning without rich feedback, learning with rich feedback, and discovering novel solutions to hard tasks at test-time. The results show that SDPO outperforms baselines in terms of sample efficiency and final accuracy.

The paper is well-written and easy to follow. The proposed method is novel and interesting. The experimental results are convincing. However, the paper lacks a clear discussion on the limitations of the proposed method. It would be beneficial to include a section on limitations and potential future work to provide a more comprehensive understanding of the method's scope and potential applications.

### justification_for_why_not_higher_score

The paper lacks a clear discussion on the limitations of the proposed method. It would be beneficial to include a section on limitations and potential future work to provide a more comprehensive understanding of the method's scope and potential applications.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is novel and interesting. The experimental results are convincing.

**********

## Paper Decision

Reject (not selected for spotlight/oral/in oral) (poster)