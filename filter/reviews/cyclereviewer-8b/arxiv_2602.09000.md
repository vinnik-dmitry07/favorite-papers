## Reviewer

### Summary

The paper introduces iGRPO, an iterative version of GRPO, which is a value-function-free variant of PPO. The authors propose a two-stage approach, where in the first stage, multiple drafts are generated and the best one is selected. In the second stage, the selected draft is appended to the original prompt, and the policy is updated using GRPO. The authors show that iGRPO outperforms GRPO and other self-improvement baselines on several benchmarks.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The authors provide a theoretical analysis of the bootstrapping effect in the proposed method.

### Weaknesses

- The proposed method is a simple extension of GRPO, and the authors do not provide a clear motivation for why the proposed method should work better than GRPO. 
- The authors do not provide a clear analysis of why the proposed method outperforms other self-improvement baselines. 
- The authors do not provide a clear analysis of the computational cost of the proposed method compared to other baselines.
- The authors do not provide a clear analysis of the generalization ability of the proposed method.

### Questions

- What is the motivation for the proposed method? Why do you think the proposed method should work better than GRPO?
- How does the proposed method compare to other self-improvement baselines in terms of computational cost?
- How does the proposed method compare to other self-improvement baselines in terms of generalization ability?
- What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper introduces iGRPO, an iterative version of GRPO, which is a value-function-free variant of PPO. The authors propose a two-stage approach, where in the first stage, multiple drafts are generated and the best one is selected. In the second stage, the selected draft is appended to the original prompt, and the policy is updated using GRPO. The authors show that iGRPO outperforms GRPO and other self-improvement baselines on several benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The authors provide a theoretical analysis of the bootstrapping effect in the proposed method.

### Weaknesses

- The proposed method is a simple extension of GRPO, and the authors do not provide a clear motivation for why the proposed method should work better than GRPO.
- The authors do not provide a clear analysis of why the proposed method outperforms other self-improvement baselines.
- The authors do not provide a clear analysis of the computational cost of the proposed method compared to other baselines.
- The authors do not provide a clear analysis of the generalization ability of the proposed method.

### Questions

- What is the motivation for the proposed method? Why do you think the proposed method should work better than GRPO?
- How does the proposed method compare to other self-improvement baselines in terms of computational cost?
- How does the proposed method compare to other self-improvement baselines in terms of generalization ability?
- What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a two-stage extension of GRPO, which is an efficient, value-function-free alternative to PPO that leverages group-relative reward normalization. In Stage 1, iGRPO samples multiple exploratory drafts and selects the highest-reward draft using the same scalar reward signal used for optimization. In Stage 2, it appends this best draft to the original prompt and applies a GRPO-style update on draft-conditioned refinements, training the policy to improve beyond its strongest prior attempt. Under matched rollout budgets, iGRPO consistently outperforms GRPO across base models, validating its effectiveness on diverse reasoning benchmarks. Moreover, applying iGRPO to OpenReasoning-Nemotron-7B trained on AceReason-Math achieves new state-of-the-art results of 85.62% and 79.64% on AIME24 and AIME25, respectively. Ablations further show that the refinement wrapper generalizes beyond GRPO variants, benefits from a generative judge, and alters learning dynamics by delaying entropy collapse.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The authors provide a theoretical analysis of the bootstrapping effect in the proposed method.

### Weaknesses

- The proposed method is a simple extension of GRPO, and the authors do not provide a clear motivation for why the proposed method should work better than GRPO.
- The authors do not provide a clear analysis of why the proposed method outperforms other self-improvement baselines.
- The authors do not provide a clear analysis of the computational cost of the proposed method compared to other baselines.
- The authors do not provide a clear analysis of the generalization ability of the proposed method.

### Questions

- What is the motivation for the proposed method? Why do you think the proposed method should work better than GRPO?
- How does the proposed method compare to other self-improvement baselines in terms of computational cost?
- How does the proposed method compare to other self-improvement baselines in terms of generalization ability?
- What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper introduces iGRPO, an iterative version of GRPO, which is a value-function-free variant of PPO. The authors propose a two-stage approach, where in the first stage, multiple drafts are generated and the best one is selected. In the second stage, the selected draft is appended to the original prompt, and the policy is updated using GRPO. The authors show that iGRPO outperforms GRPO and other self-improvement baselines on several benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The authors provide a theoretical analysis of the bootstrapping effect in the proposed method.

### Weaknesses

- The proposed method is a simple extension of GRPO, and the authors do not provide a clear motivation for why the proposed method should work better than GRPO.
- The authors do not provide a clear analysis of why the proposed method outperforms other self-improvement baselines.
- The authors do not provide a clear analysis of the computational cost of the proposed method compared to other baselines.
- The authors do not provide a clear analysis of the generalization ability of the proposed method.

### Questions

- What is the motivation for the proposed method? Why do you think the proposed method should work better than GRPO?
- How does the proposed method compare to other self-improvement baselines in terms of computational cost?
- How does the proposed method compare to other self-improvement baselines in terms of generalization ability?
- What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper presents a new method for improving the performance of LLMs on reasoning tasks, called Iterative Group Relative Policy Optimization (iGRPO). The method is an extension of GRPO, which is a value-function-free variant of PPO that leverages group-relative reward normalization. The authors propose a two-stage approach, where in the first stage, multiple drafts are generated and the best one is selected. In the second stage, the selected draft is appended to the original prompt, and the policy is updated using GRPO. The authors show that iGRPO outperforms GRPO and other self-improvement baselines on several benchmarks.

The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The authors provide a theoretical analysis of the bootstrapping effect in the proposed method. However, the proposed method is a simple extension of GRPO, and the authors do not provide a clear motivation for why the proposed method should work better than GRPO. The authors do not provide a clear analysis of why the proposed method outperforms other self-improvement baselines. The authors do not provide a clear analysis of the computational cost of the proposed method compared to other baselines. The authors do not provide a clear analysis of the generalization ability of the proposed method.

### justification_for_why_not_higher_score

The proposed method is a simple extension of GRPO, and the authors do not provide a clear motivation for why the proposed method should work better than GRPO. The authors do not provide a clear analysis of why the proposed method outperforms other self-improvement baselines. The authors do not provide a clear analysis of the computational cost of the proposed method compared to other baselines. The authors do not provide a clear analysis of the generalization ability of the proposed method.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the running for an oral)

**********

# Editor

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

# Editor

**********

## Paper Decision

Reject (out of the running for an oral)

**********

## Paper Decision Summary

Reject (out of the running for an oral)

**********

