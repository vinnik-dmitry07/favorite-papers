## Reviewer

### Summary

This paper proposes a new method to combine the strengths of two existing methods for post-hoc training of LLMs: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). The proposed method, Sample-Routed Policy Optimization (SRPO), routes correct samples to GRPO and failed samples to SDPO. Furthermore, SRPO incorporates an entropy-aware dynamic weighting mechanism to suppress high-entropy, unreliable distillation targets while emphasizing confident ones. The authors show that SRPO achieves both the rapid early improvement of SDPO and the long-horizon stability of GRPO and outperforms both baselines on five benchmarks and two model scales.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is well motivated and the paper provides a clear explanation of the motivation and the design of the method.
- The proposed method is simple and easy to implement.
- The experimental results show that SRPO achieves both the rapid early improvement of SDPO and the long-horizon stability of GRPO and outperforms both baselines on five benchmarks and two model scales.

### Weaknesses

- The paper only compares SRPO with GRPO and SDPO. It would be interesting to see how SRPO compares to other methods for post-hoc training of LLMs, such as RLHF.
- The paper only evaluates SRPO on five benchmarks and two model scales. It would be interesting to see how SRPO performs on a wider range of benchmarks and model scales.
- The paper does not provide any analysis of the limitations of SRPO.

### Questions

- How does SRPO compare to other methods for post-hoc training of LLMs, such as RLHF?
- How does SRPO perform on a wider range of benchmarks and model scales?
- What are the limitations of SRPO?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a new method for post-training LLMs with verifiable rewards. The authors propose a new method called Sample-Routed Policy Optimization (SRPO) that combines the strengths of two existing methods: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). SRPO routes correct samples to GRPO and failed samples to SDPO, and incorporates an entropy-aware dynamic weighting mechanism to suppress high-entropy, unreliable distillation targets while emphasizing confident ones. The authors evaluate SRPO on five benchmarks and two model scales, and show that it outperforms both GRPO and SDPO in terms of peak performance, response length, and per-step compute time.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is well motivated and the paper provides a clear explanation of the motivation and the design of the method.
- The experimental results are thorough and convincing.

### Weaknesses

- The paper does not provide a detailed analysis of the limitations of the proposed method.
- The paper does not provide a detailed analysis of the computational cost of the proposed method.

### Questions

- How does the proposed method compare to other methods for post-training LLMs with verifiable rewards?
- How does the proposed method scale to larger models and more complex tasks?
- How does the proposed method perform on tasks that require more complex reasoning and problem-solving skills?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method called Sample-Routed Policy Optimization (SRPO) that combines the strengths of two existing methods: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). SRPO routes correct samples to GRPO and failed samples to SDPO, and incorporates an entropy-aware dynamic weighting mechanism to suppress high-entropy, unreliable distillation targets while emphasizing confident ones. The authors evaluate SRPO on five benchmarks and two model scales, and show that it outperforms both GRPO and SDPO in terms of peak performance, response length, and per-step compute time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is well motivated and the paper provides a clear explanation of the motivation and the design of the method. The experimental results are thorough and convincing.

### Weaknesses

The paper does not provide a detailed analysis of the limitations of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method.

### Questions

How does the proposed method compare to other methods for post-training LLMs with verifiable rewards? How does the proposed method scale to larger models and more complex tasks? How does the proposed method perform on tasks that require more complex reasoning and problem-solving skills?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method called Sample-Routed Policy Optimization (SRPO) that combines the strengths of two existing methods: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). SRPO routes correct samples to GRPO and failed samples to SDPO, and incorporates an entropy-aware dynamic weighting mechanism to suppress high-entropy, unreliable distillation targets while emphasizing confident ones. The authors evaluate SRPO on five benchmarks and two model scales, and show that it outperforms both GRPO and SDPO in terms of peak performance, response length, and per-step compute time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is well motivated and the paper provides a clear explanation of the motivation and the design of the method. The experimental results are thorough and convincing.

### Weaknesses

The paper does not provide a detailed analysis of the limitations of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method.

### Questions

How does the proposed method compare to other methods for post-training LLMs with verifiable rewards? How does the proposed method scale to larger models and more complex tasks? How does the proposed method perform on tasks that require more complex reasoning and problem-solving skills?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new method for post-training LLMs with verifiable rewards. The authors propose a new method called Sample-Routed Policy Optimization (SRPO) that combines the strengths of two existing methods: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). SRPO routes correct samples to GRPO and failed samples to SDPO, and incorporates an entropy-aware dynamic weighting mechanism to suppress high-entropy, unreliable distillation targets while emphasizing confident ones. The authors evaluate SRPO on five benchmarks and two model scales, and show that it outperforms both GRPO and SDPO in terms of peak performance, response length, and per-step compute time.

All reviewers agree that the paper is well-written and easy to follow. The proposed method is well motivated and the paper provides a clear explanation of the motivation and the design of the method. The experimental results are thorough and convincing. The paper is recommended for acceptance.

### justification_for_why_not_higher_score

This paper proposes a new method for post-training LLMs with verifiable rewards. The authors propose a new method called Sample-Routed Policy Optimization (SRPO) that combines the strengths of two existing methods: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). SRPO routes correct samples to GRPO and failed samples to SDPO, and incorporates an entropy-aware dynamic weighting mechanism to suppress high-entropy, unreliable distillation targets while emphasizing confident ones. The authors evaluate SRPO on five benchmarks and two model scales, and show that it outperforms both GRPO and SDPO in terms of peak performance, response length, and per-step compute time.

All reviewers agree that the paper is well-written and easy to follow. The proposed method is well motivated and the paper provides a clear explanation of the motivation and the design of the method. The experimental results are thorough and convincing. The paper is recommended for acceptance.

### justification_for_why_not_lower_score

This paper proposes a new method for post-training LLMs with verifiable rewards. The authors propose a new method called Sample-Routed Policy Optimization (SRPO) that combines the strengths of two existing methods: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). SRPO routes correct samples to GRPO and failed samples to SDPO, and incorporates an entropy-aware dynamic weighting mechanism to suppress high-entropy, unreliable distillation targets while emphasizing confident ones. The authors evaluate SRPO on five benchmarks and two model scales, and show that it outperforms both GRPO and SDPO in terms of peak performance, response length, and per-step compute time.

All reviewers agree that the paper is well-written and easy to follow. The proposed method is well motivated and the paper provides a clear explanation of the motivation and the design of the method. The experimental results are thorough and convincing. The paper is recommended for acceptance.

**********

## Paper Decision

Accept (poster)