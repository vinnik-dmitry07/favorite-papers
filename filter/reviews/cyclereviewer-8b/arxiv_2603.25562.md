## Reviewer

### Summary

This paper studies on-policy distillation for LLMs. The authors first theoretically analyze the bias-variance trade-off between token-level and sequence-level on-policy distillation. The authors then empirically study the failure modes of the standard sampled-token on-policy distillation and propose a new objective that uses top-K local support matching. The proposed method is evaluated on math reasoning and multi-task agentic-plus-reasoning training.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a good theoretical analysis of the bias-variance trade-off between token-level and sequence-level on-policy distillation.

### Weaknesses

- The proposed method is not novel. The idea of using top-K local support matching has been studied in the RL community for a long time. See, for example, [1,2]. It is unclear why the authors did not cite these papers.
- The empirical results are not convincing. The proposed method is only evaluated on two small datasets, which are not sufficient to demonstrate its effectiveness. The authors should evaluate the proposed method on more datasets and larger models.

[1] Ghavamzadeh, Mohammad, et al. "A comprehensive survey of transfer value-function reinforcement learning." arXiv preprint arXiv:1908.10259 (2019).

[2] Farahmand, Amir-massoud, Marc Bellemare, and Doina Precup. "Regularized policy iteration." Advances in neural information processing systems 23 (2010).

### Questions

- The authors should cite the existing work on top-K local support matching in the RL community. 
- The authors should evaluate the proposed method on more datasets and larger models.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper studies the on-policy distillation (OPD) for LLMs. The authors first theoretically analyze the bias-variance trade-off between token-level and sequence-level OPD. Then, the authors identify three failure modes of the standard sampled-token OPD: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and tokenizer or special-token mismatch. The authors propose a new method called teacher top-K local support matching to address these issues. The proposed method is evaluated on single-task math reasoning and multi-task agentic-plus-reasoning training.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a good theoretical analysis of the bias-variance trade-off between token-level and sequence-level OPD.
3. The authors identify three failure modes of the standard sampled-token OPD and propose a new method to address them.

### Weaknesses

1. The proposed method is not novel. The idea of using top-K local support matching has been studied in the RL community for a long time. See, for example, [1,2]. It is unclear why the authors did not cite these papers.
2. The empirical results are not convincing. The proposed method is only evaluated on two small datasets, which are not sufficient to demonstrate its effectiveness. The authors should evaluate the proposed method on more datasets and larger models.

[1] Ghavamzadeh, Mohammad, et al. "A comprehensive survey of transfer value-function reinforcement learning." arXiv preprint arXiv:1908.10259 (2019).

[2] Farahmand, Amir-massoud, Marc Bellemare, and Doina Precup. "Regularized policy iteration." Advances in neural information processing systems 23 (2010).

### Questions

1. The proposed method is not novel. The idea of using top-K local support matching has been studied in the RL community for a long time. See, for example, [1,2]. It is unclear why the authors did not cite these papers.
2. The empirical results are not convincing. The proposed method is only evaluated on two small datasets, which are not sufficient to demonstrate its effectiveness. The authors should evaluate the proposed method on more datasets and larger models.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper analyzes the on-policy distillation (OPD) for LLMs. The authors first theoretically analyze the bias-variance trade-off between token-level and sequence-level OPD. Then, the authors identify three failure modes of the standard sampled-token OPD: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and tokenizer or special-token mismatch. The authors propose a new method called teacher top-K local support matching to address these issues. The proposed method is evaluated on single-task math reasoning and multi-task agentic-plus-reasoning training.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a good theoretical analysis of the bias-variance trade-off between token-level and sequence-level OPD.
3. The authors identify three failure modes of the standard sampled-token OPD and propose a new method to address them.

### Weaknesses

1. The proposed method is not novel. The idea of using top-K local support matching has been studied in the RL community for a long time. See, for example, [1,2]. It is unclear why the authors did not cite these papers.
2. The empirical results are not convincing. The proposed method is only evaluated on two small datasets, which are not sufficient to demonstrate its effectiveness. The authors should evaluate the proposed method on more datasets and larger models.

[1] Ghavamzadeh, Mohammad, et al. "A comprehensive survey of transfer value-function reinforcement learning." arXiv preprint arXiv:1908.10259 (2019).

[2] Farahmand, Amir-massoud, Marc Bellemare, and Doina Precup. "Regularized policy iteration." Advances in neural information processing systems 23 (2010).

### Questions

1. The proposed method is not novel. The idea of using top-K local support matching has been studied in the RL community for a long time. See, for example, [1,2]. It is unclear why the authors did not cite these papers.
2. The empirical results are not convincing. The proposed method is only evaluated on two small datasets, which are not sufficient to demonstrate its effectiveness. The authors should evaluate the proposed method on more datasets and larger models.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper revisits on-policy distillation (OPD) for LLMs, focusing on the token-level estimator, which is biased relative to sequence-level reverse-KL but has better worst-case variance scaling. The paper identifies three failure modes of the standard sampled-token OPD: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and tokenizer or special-token mismatch. To address these issues, the paper proposes a new method called teacher top-K local support matching, which compares teacher and student distributions over a teacher-supported token set at each prefix. The proposed method is evaluated on single-task math reasoning and multi-task agentic-plus-reasoning training, showing improved optimization stability and stronger empirical performance compared to the standard sampled-token OPD.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper provides a comprehensive analysis of the failure modes of the standard sampled-token OPD, which is a valuable contribution to the field.
- The proposed method of teacher top-K local support matching is simple yet effective in addressing the identified failure modes.
- The paper presents a thorough evaluation of the proposed method on both single-task math reasoning and multi-task agentic-plus-reasoning training, demonstrating its effectiveness in improving optimization stability and empirical performance.

### Weaknesses

- The paper does not provide a clear comparison with other existing methods for on-policy distillation, such as full-vocabulary distillation or other variants of OPD.
- The paper does not provide a detailed analysis of the computational cost of the proposed method compared to the standard sampled-token OPD.
- The paper does not provide a clear explanation of how the proposed method can be applied to other types of LLMs beyond the specific models used in the experiments.

### Questions

- How does the proposed method compare to other existing methods for on-policy distillation, such as full-vocabulary distillation or other variants of OPD?
- What is the computational cost of the proposed method compared to the standard sampled-token OPD?
- How can the proposed method be applied to other types of LLMs beyond the specific models used in the experiments?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper studies on-policy distillation for LLMs. The authors first theoretically analyze the bias-variance trade-off between token-level and sequence-level OPD. Then, the authors identify three failure modes of the standard sampled-token OPD: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and tokenizer or special-token mismatch. The authors propose a new method called teacher top-K local support matching to address these issues. The proposed method is evaluated on single-task math reasoning and multi-task agentic-plus-reasoning training.

The reviewers generally agree that the paper is well-written and easy to follow. The authors provide a good theoretical analysis of the bias-variance trade-off between token-level and sequence-level OPD. The authors identify three failure modes of the standard sampled-token OPD and propose a new method to address them. However, the reviewers also raised some concerns about the novelty of the proposed method and the empirical results. The authors should address these concerns in the rebuttal.

### justification_for_why_not_higher_score

The reviewers raised some concerns about the novelty of the proposed method and the empirical results. The authors should address these concerns in the rebuttal.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR)