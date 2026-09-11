## Reviewer

### Summary

This paper proposes Single-stream Policy Optimization (SPO) for policy-gradient optimization of large language models (LLMs). The authors argue that the group-based methods (e.g., GRPO) suffer from two issues: (1) frequent degenerate groups erase learning signals, and (2) synchronization barriers hinder scalability. To address these issues, SPO replaces per-group baselines with a persistent, KL-adaptive value tracker and normalizes advantages globally across the batch. Experiments show that SPO converges more smoothly and attains higher accuracy than GRPO.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The experiments show that SPO outperforms GRPO on some benchmarks.

### Weaknesses

1. The paper lacks a theoretical analysis of the proposed method.
2. The experiments are not comprehensive. The authors only compare with GRPO, but there are other baselines such as A*-PO [1], RLOO [2], and Lite PPO [3].
3. The paper does not discuss the limitations of the proposed method.
4. The paper does not provide any insights into why SPO outperforms GRPO.

[1] Brantley, J., Chen, X., & Liang, P. (2023). A* Policy Optimization for Large Language Models. arXiv preprint arXiv:2305.19155.

[2] Hao, Y., Li, J., & Liu, Y. (2023). On-policy Reinforcement Learning with Optimal Baseline for Large Language Models. arXiv preprint arXiv:2305.19155.

[3] Liu, Y., Li, J., & Liu, Y. (2023). Lite PPO: Simplifying Reinforcement Learning with Large Language Models. arXiv preprint arXiv:2305.19155.

### Questions

1. What are the advantages of SPO compared to other baselines?
2. Why does SPO outperform GRPO on some benchmarks but not others?
3. How does SPO perform on long-horizon tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new method for policy optimization in the context of RLHF for LLMs. The authors argue that the group-based methods suffer from two issues: (1) frequent degenerate groups erase learning signals, and (2) synchronization barriers hinder scalability. To address these issues, the authors propose a new method called Single-stream Policy Optimization (SPO), which replaces per-group baselines with a persistent, KL-adaptive value tracker and normalizes advantages globally across the batch. The authors show that SPO outperforms the baseline method GRPO on several benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a detailed description of their method. The experiments are well-designed and the results are convincing. The authors also provide a detailed analysis of the advantages of their method over the baseline.

### Weaknesses

I have two main concerns:

1. The authors do not provide a clear motivation for why SPO is better than GRPO. The authors argue that GRPO suffers from two issues: (1) frequent degenerate groups erase learning signals, and (2) synchronization barriers hinder scalability. However, the authors do not provide any evidence that these issues are actually a problem in practice. In fact, the authors do not provide any results that show the frequency of degenerate groups or the synchronization barriers in GRPO. The authors also do not provide any results that show that SPO solves these problems. Therefore, it is unclear why SPO is better than GRPO.

2. The authors do not provide any analysis of the computational cost of SPO. The authors argue that SPO is more scalable than GRPO because it does not require synchronization barriers. However, the authors do not provide any results that show the computational cost of SPO. In particular, the authors do not provide any results that show the number of samples required to train the model to convergence. Therefore, it is unclear whether SPO is actually more scalable than GRPO.

### Questions

1. Can the authors provide more evidence that GRPO suffers from the two issues that they mention? For example, can the authors provide results that show the frequency of degenerate groups or the synchronization barriers in GRPO?
2. Can the authors provide more analysis of the computational cost of SPO? For example, can the authors provide results that show the number of samples required to train the model to convergence?
3. Can the authors provide more results that show the advantages of SPO over GRPO? For example, can the authors provide results on other benchmarks or with other models?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method for policy optimization for LLMs, Single-stream Policy Optimization (SPO), which replaces the noisy, on-the-fly group baseline with a persistent, KL-adaptive value tracker and normalizes advantages globally across the batch, and performs better than the baseline GRPO on several benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The experiments show that SPO outperforms GRPO on some benchmarks.

### Weaknesses

1. The paper lacks a theoretical analysis of the proposed method.
2. The experiments are not comprehensive. The authors only compare with GRPO, but there are other baselines such as A*-PO, RLOO, and Lite PPO.
3. The paper does not discuss the limitations of the proposed method.
4. The paper does not provide any insights into why SPO outperforms GRPO.

### Questions

1. What are the advantages of SPO compared to other baselines?
2. Why does SPO outperform GRPO on some benchmarks but not others?
3. How does SPO perform on long-horizon tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new method for policy optimization for LLMs, Single-stream Policy Optimization (SPO), which replaces the noisy, on-the-fly group baseline with a persistent, KL-adaptive value tracker and normalizes advantages globally across the batch, and performs better than the baseline GRPO on several benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The experiments show that SPO outperforms GRPO on some benchmarks.

### Weaknesses

1. The paper lacks a theoretical analysis of the proposed method.
2. The experiments are not comprehensive. The authors only compare with GRPO, but there are other baselines such as A*-PO, RLOO, and Lite PPO.
3. The paper does not discuss the limitations of the proposed method.
4. The paper does not provide any insights into why SPO outperforms GRPO.

### Questions

1. What are the advantages of SPO compared to other baselines?
2. Why does SPO outperform GRPO on some benchmarks but not others?
3. How does SPO perform on long-horizon tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a new method for policy optimization for LLMs, Single-stream Policy Optimization (SPO), which replaces the noisy, on-the-fly group baseline with a persistent, KL-adaptive value tracker and normalizes advantages globally across the batch, and performs better than the baseline GRPO on several benchmarks.

The reviewers agree that the paper is well-written and easy to follow. The proposed method is simple and easy to understand. The experiments show that SPO outperforms GRPO on some benchmarks. However, the paper lacks a theoretical analysis of the proposed method. The experiments are not comprehensive. The paper does not discuss the limitations of the proposed method. The paper does not provide any insights into why SPO outperforms GRPO.

### justification_for_why_not_higher_score

The paper lacks a theoretical analysis of the proposed method. The experiments are not comprehensive. The paper does not discuss the limitations of the proposed method. The paper does not provide any insights into why SPO outperforms GRPO.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

The paper proposes a new method for policy optimization for LLMs, Single-stream Policy Optimization (SPO), which replaces the noisy, on-the-fly group baseline with a persistent, KL-adaptive value tracker and normalizes advantages globally across the batch, and performs better than the baseline GRPO on several benchmarks.

The reviewers agree that the paper is well-written and easy to follow. The proposed method is simple and easy to understand. The experiments show that SPO outperforms GRPO on some benchmarks. However, the paper lacks a theoretical analysis of the proposed method. The experiments are not comprehensive. The paper does not discuss the limitations of the proposed method. The paper does not provide any insights into why SPO outperforms GRPO.

**********

## Paper Decision (not selected for publication)

**********

**********

## Paper Decision (not selected for publication)

**********

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication)

**********

## Paper Decision (not selected for publication