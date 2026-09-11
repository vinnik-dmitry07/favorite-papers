## Reviewer

### Summary

This paper proposes a new decoding algorithm for dLLMs, which combines mask-to-token and token-to-token decoding to improve the decoding efficiency. The proposed decoding algorithm is trained with a mixture of mask-to-token and token-to-token objectives. The proposed model is evaluated on various benchmarks, and the results show that the proposed model can achieve better decoding efficiency while maintaining the performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The proposed decoding algorithm is simple and effective. The proposed model can achieve better decoding efficiency while maintaining the performance.

### Weaknesses

1. The proposed decoding algorithm is not new. There have been many previous works that use a mixture of mask-to-token and token-to-token decoding to improve the decoding efficiency. For example, [1] also uses a mixture of mask-to-token and token-to-token decoding to improve the decoding efficiency. The main difference between the proposed method and [1] is that the proposed method uses a mixture of mask-to-token and token-to-token objectives during training. However, the training objective is not new, and it is also used in [1]. 

2. The proposed method is not evaluated on any general language generation tasks. The proposed method is only evaluated on coding tasks. It is unclear how the proposed method performs on general language generation tasks.

3. The proposed method is not evaluated on any long-form generation tasks. The proposed method is only evaluated on short-form generation tasks. It is unclear how the proposed method performs on long-form generation tasks.

4. The proposed method is not evaluated on any real-world applications. The proposed method is only evaluated on benchmark tasks. It is unclear how the proposed method performs on real-world applications.

5. The proposed method is not compared with any other decoding algorithms. The proposed method is only compared with LLaDA2.0. It is unclear how the proposed method compares with other decoding algorithms.

[1] Song et al. 2023. Token-to-Token Diffusion Language Models. https://arxiv.org/abs/2305.14494

### Questions

Please see the weaknesses above.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper introduces a new decoding algorithm for dLLMs, which combines mask-to-token and token-to-token decoding to improve decoding efficiency. The proposed decoding algorithm is trained with a mixture of mask-to-token and token-to-token objectives. The proposed model is evaluated on various benchmarks, and the results show that the proposed model can achieve better decoding efficiency while maintaining the performance.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method can achieve better decoding efficiency while maintaining the performance.

### Weaknesses

- The novelty of this paper is limited. The proposed method is similar to the previous work [1], which also uses a mixture of mask-to-token and token-to-token decoding to improve decoding efficiency.
- The proposed method is only evaluated on coding tasks, and it is unclear how the proposed method performs on general language generation tasks.
- The proposed method is not compared with other decoding algorithms.
- The proposed method is not evaluated on long-form generation tasks.
- The proposed method is not evaluated on real-world applications.

[1] Song et al. 2023. Token-to-Token Diffusion Language Models. https://arxiv.org/abs/2305.14494

### Questions

- How does the proposed method compare with other decoding algorithms?
- How does the proposed method perform on general language generation tasks?
- How does the proposed method perform on long-form generation tasks?
- How does the proposed method perform on real-world applications?
- Why is the proposed method only evaluated on coding tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new decoding algorithm for dLLMs, which combines mask-to-token and token-to-token decoding to improve decoding efficiency. The proposed decoding algorithm is trained with a mixture of mask-to-token and token-to-token objectives. The proposed model is evaluated on various benchmarks, and the results show that the proposed model can achieve better decoding efficiency while maintaining the performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method can achieve better decoding efficiency while maintaining the performance.
- The paper is well-written and easy to follow.

### Weaknesses

- The proposed method is only evaluated on coding tasks, and it is unclear how the proposed method performs on general language generation tasks.
- The proposed method is not compared with other decoding algorithms.
- The proposed method is not evaluated on long-form generation tasks.
- The proposed method is not evaluated on real-world applications.

### Questions

- How does the proposed method compare with other decoding algorithms?
- How does the proposed method perform on general language generation tasks?
- How does the proposed method perform on long-form generation tasks?
- How does the proposed method perform on real-world applications?
- Why is the proposed method only evaluated on coding tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a new decoding algorithm for dLLMs, which combines mask-to-token and token-to-token decoding to improve decoding efficiency. The proposed decoding algorithm is trained with a mixture of mask-to-token and token-to-token objectives. The proposed model is evaluated on various benchmarks, and the results show that the proposed model can achieve better decoding efficiency while maintaining the performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method can achieve better decoding efficiency while maintaining the performance.
- The paper is well-written and easy to follow.

### Weaknesses

- The proposed method is only evaluated on coding tasks, and it is unclear how the proposed method performs on general language generation tasks.
- The proposed method is not compared with other decoding algorithms.
- The proposed method is not evaluated on long-form generation tasks.
- The proposed method is not evaluated on real-world applications.

### Questions

- How does the proposed method compare with other decoding algorithms?
- How does the proposed method perform on general language generation tasks?
- How does the proposed method perform on long-form generation tasks?
- How does the proposed method perform on real-world applications?
- Why is the proposed method only evaluated on coding tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper proposes a new decoding algorithm for dLLMs, which combines mask-to-token and token-to-token decoding to improve decoding efficiency. The proposed decoding algorithm is trained with a mixture of mask-to-token and token-to-token objectives. The proposed model is evaluated on various benchmarks, and the results show that the proposed model can achieve better decoding efficiency while maintaining the performance.

The reviewers have raised several concerns about the novelty of the proposed method, the evaluation of the proposed method on general language generation tasks, long-form generation tasks, and real-world applications. The authors did not provide a response to these concerns. Therefore, the paper is not recommended for acceptance.

### justification_for_why_not_higher_score

The reviewers have raised several concerns about the novelty of the proposed method, the evaluation of the proposed method on general language generation tasks, long-form generation tasks, and real-world applications. The authors did not provide a response to these concerns.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR)