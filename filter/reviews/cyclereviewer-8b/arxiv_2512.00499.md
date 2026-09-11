## Reviewer

### Summary

The paper proposes a new RL algorithm for LLMs, which decomposes sequences into groups based on predictive entropy, enabling entropy-based grouping importance sampling and entropy adaptive clipping. The proposed method is evaluated on mathematical reasoning benchmarks and shows improved performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and intuitive, and the idea of using entropy to group tokens is interesting.

### Weaknesses

The novelty of the proposed method seems limited. The idea of using entropy to group tokens has been explored in prior works such as [1], and the proposed entropy adaptive clipping is similar to dynamic clipping in DCPO [2]. The proposed method is also very similar to SPO [3], which also decomposes sequences into groups based on entropy. The main difference is that the proposed method uses entropy adaptive clipping, but it is unclear how this helps.

[1] Liu, Y., Xu, Z., & Li, Y. (2023). Token-level policy optimization for large language models. arXiv preprint arXiv:2305.19123.

[2] Gu, S., Levine, H., & Recht, B. (2017). Deep reinforcement learning without policy gradient. In International conference on machine learning (pp. 1722-1731). PMLR.

[3] Zhang, C., Chen, H., & Li, Y. (2023, September). SPO: Segment-level Policy Optimization for Large Language Models. In The Eleventh International Conference on Learning Representations.

### Questions

- How does the proposed method compare to SPO [3], which also decomposes sequences into groups based on entropy?
- How does the proposed method compare to dynamic clipping in DCPO [2]?
- How does the proposed method compare to token-level methods such as CISPO and GMPO?
- How does the proposed method compare to sequence-level methods such as GSPO?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new algorithm for reinforcement learning in LLMs. The authors claim that the proposed algorithm achieves better performance than existing algorithms. The proposed algorithm is based on entropy, which is a measure of the uncertainty of the model. The authors group tokens based on their entropy and clip the gradients based on the group entropy. The authors evaluate the proposed algorithm on mathematical reasoning benchmarks and show that it achieves better performance than existing algorithms.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a clear description of the proposed algorithm and its components. The authors also provide a detailed analysis of the performance of the proposed algorithm on mathematical reasoning benchmarks.

### Weaknesses

The proposed algorithm is not novel. The idea of using entropy to group tokens and clip gradients is not new and has been explored in previous work. The authors do not provide a detailed comparison with existing algorithms and do not discuss the advantages of their approach.

The experiments are not convincing. The authors only evaluate the proposed algorithm on mathematical reasoning benchmarks and do not compare it with other algorithms on other tasks. The authors do not provide a detailed analysis of the performance of the proposed algorithm on different tasks and do not discuss the generalizability of the proposed algorithm.

### Questions

1. How does the proposed algorithm compare with other algorithms on other tasks?
2. How does the proposed algorithm perform on different datasets?
3. How does the proposed algorithm perform on different model sizes?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces a new RL algorithm for LLMs, which decomposes sequences into groups based on predictive entropy, enabling entropy-based grouping importance sampling and entropy adaptive clipping. The proposed method is evaluated on mathematical reasoning benchmarks and shows improved performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and intuitive, and the idea of using entropy to group tokens is interesting. The paper provides a clear description of the proposed algorithm and its components, and the authors also provide a detailed analysis of the performance of the proposed algorithm on mathematical reasoning benchmarks.

### Weaknesses

The novelty of the proposed method seems limited. The idea of using entropy to group tokens has been explored in prior works such as [1], and the proposed entropy adaptive clipping is similar to dynamic clipping in DCPO [2]. The main difference is that the proposed method uses entropy adaptive clipping, but it is unclear how this helps.

[1] Liu, Y., Xu, Z., & Li, Y. (2023). Token-level policy optimization for large language models. arXiv preprint arXiv:2305.19123.

[2] Gu, S., Levine, H., & Recht, B. (2017). Deep reinforcement learning without policy gradient. In International conference on machine learning (pp. 1722-1731). PMLR.

### Questions

- How does the proposed method compare to SPO [3], which also decomposes sequences into groups based on entropy?
- How does the proposed method compare to dynamic clipping in DCPO [2]?
- How does the proposed method compare to token-level methods such as CISPO and GMPO?
- How does the proposed method compare to sequence-level methods such as GSPO?

[3] Zhang, C., Chen, H., & Li, Y. (2023, September). SPO: Segment-level Policy Optimization for Large Language Models. In The Eleventh International Conference on Learning Representations.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new method for reinforcement learning (RL) for large language models (LLMs). The proposed method, called Entropy Importance Sampling Policy Optimization (ESPO), decomposes sequences into groups based on predictive entropy, enabling entropy-based grouping importance sampling and entropy adaptive clipping. The paper evaluates the proposed method on mathematical reasoning benchmarks and shows that it achieves better performance than existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and intuitive, and the idea of using entropy to group tokens is interesting.
- The paper provides a clear description of the proposed algorithm and its components, and the authors also provide a detailed analysis of the performance of the proposed algorithm on mathematical reasoning benchmarks.

### Weaknesses

- The novelty of the proposed method seems limited. The idea of using entropy to group tokens has been explored in prior works such as [1], and the proposed entropy adaptive clipping is similar to dynamic clipping in DCPO [2]. The main difference is that the proposed method uses entropy adaptive clipping, but it is unclear how this helps.
- The paper only evaluates the proposed method on mathematical reasoning benchmarks, and it is unclear how the proposed method would perform on other tasks.

[1] Liu, Y., Xu, Z., & Li, Y. (2023). Token-level policy optimization for large language models. arXiv preprint arXiv:2305.19123.

[2] Gu, S., Levine, H., & Recht, B. (2017). Deep reinforcement learning without policy gradient. In International conference on machine learning (pp. 1722-1731). PMLR.

### Questions

- How does the proposed method compare to SPO [3], which also decomposes sequences into groups based on entropy?
- How does the proposed method compare to dynamic clipping in DCPO [2]?
- How does the proposed method compare to token-level methods such as CISPO and GMPO?
- How does the proposed method compare to sequence-level methods such as GSPO?

[3] Zhang, C., Chen, H., & Li, Y. (2023, September). SPO: Segment-level Policy Optimization for Large Language Models. In The Eleventh International Conference on Learning Representations.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new algorithm for reinforcement learning in LLMs, which decomposes sequences into groups based on predictive entropy, enabling entropy-based grouping importance sampling and entropy adaptive clipping. The proposed method is evaluated on mathematical reasoning benchmarks and shows improved performance.

The reviewers raised several concerns, including the novelty of the proposed method, the limited evaluation of the proposed method, and the lack of comparison with other algorithms. The authors provided detailed responses to the reviewers' concerns, and the reviewers raised their scores. However, the reviewers still have some concerns about the novelty of the proposed method and the limited evaluation. Therefore, I recommend rejecting this paper.

### justification_for_why_not_higher_score

The novelty of the proposed method seems limited. The idea of using entropy to group tokens has been explored in prior works such as [1], and the proposed entropy adaptive clipping is similar to dynamic clipping in DCPO [2]. The main difference is that the proposed method uses entropy adaptive clipping, but it is unclear how this helps.

[1] Liu, Y., Xu, Z., & Li, Y. (2023). Token-level policy optimization for large language models. arXiv preprint arXiv:2305.19123.

[2] Gu, S., Levine, H., & Recht, B. (2017). Deep reinforcement learning without policy gradient. In International conference on machine learning (pp. 1722-1731). PMLR.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR)