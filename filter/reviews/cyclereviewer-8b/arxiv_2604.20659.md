## Reviewer

### Summary

This paper proposes GRPO-VPS, a method that extends the group relative policy optimization (GRPO) framework with a process supervision signal to improve the reasoning performance of large language models (LLMs). The process supervision signal is derived from the model's confidence in the correct answer at each step of the reasoning trajectory. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks.

### Weaknesses

- The proposed method is an extension of GRPO, and the novelty is limited.
- The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score.
- The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks.
- The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

### Questions

- How does the proposed method compare to other methods that use process supervision signals, such as PRMs?
- How does the proposed method perform on other types of reasoning tasks, such as multi-hop question answering?
- How does the proposed method scale to larger models and more complex reasoning tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method for RL-based LLM training that aims to improve the sample efficiency and performance of the training process. The proposed method, GRPO-VPS, enhances Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The authors empirically show that the proposed method outperforms GRPO and other RL-based methods on several reasoning benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks.

### Weaknesses

- The proposed method is an extension of GRPO, and the novelty is limited.
- The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score.
- The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks.
- The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

### Questions

- How does the proposed method compare to other methods that use process supervision signals, such as PRMs?
- How does the proposed method perform on other types of reasoning tasks, such as multi-hop question answering?
- How does the proposed method scale to larger models and more complex reasoning tasks?
- Can the proposed method be applied to other types of LLMs, such as GPT-3.5-turbo?
- How does the proposed method compare to other RL-based methods that use different reward functions, such as the reward function proposed in [1]?

[1] Shao et al. Reinforcement Learning with Verifiable Rewards. arXiv preprint arXiv:2304.11455 (2023).

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes GRPO-VPS, a method that extends the group relative policy optimization (GRPO) framework with a process supervision signal to improve the reasoning performance of large language models (LLMs). The process supervision signal is derived from the model's confidence in the correct answer at each step of the reasoning trajectory. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks.
- The paper is well-written and easy to follow.

### Weaknesses

- The proposed method is an extension of GRPO, and the novelty is limited.
- The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score.
- The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks.
- The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

### Questions

- How does the proposed method compare to other methods that use process supervision signals, such as PRMs?
- How does the proposed method perform on other types of reasoning tasks, such as multi-hop question answering?
- How does the proposed method scale to larger models and more complex reasoning tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to enhance Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and easy to implement.
- The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks.
- The paper is well-written and easy to follow.

### Weaknesses

- The proposed method is an extension of GRPO, and the novelty is limited.
- The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score.
- The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks.
- The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

### Questions

- How does the proposed method compare to other methods that use process supervision signals, such as PRMs?
- How does the proposed method perform on other types of reasoning tasks, such as multi-hop question answering?
- How does the proposed method scale to larger models and more complex reasoning tasks?
- Can the proposed method be applied to other types of LLMs, such as GPT-3.5-turbo?
- How does the proposed method compare to other RL-based methods that use different reward functions, such as the reward function proposed in [1]?

[1] Shao et al. Reinforcement Learning with Verifiable Rewards. arXiv preprint arXiv:2304.11455 (2023).

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces a method to enhance Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length.

The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks.

However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

### justification_for_why_not_higher_score

The proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Summary

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

### justification_for_why_not_higher_score

The proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

### justification_for_why_not_lower_score

N/A

**********

<!--paper_reviewer_2K3o->

<!--paper_reviewer_9eQ5->

<!--paper_reviewer_9pRv->

<!--paper_reviewer_uYQk->

<!--paper_author_response_9eQ5->

<!--paper_author_response_9pRv->

<!--paper_author_response_uYQk->

<!--paper_author_response_2K3o->

**********

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Summary

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (GRPO) with verifiable process supervision derived from the annotated final answer. The proposed method is evaluated on both math and general reasoning benchmarks and outperforms the baseline methods in terms of accuracy and reasoning length. The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The proposed method achieves consistent improvements over the baseline methods on both math and general reasoning benchmarks. However, the proposed method is an extension of GRPO, and the novelty is limited. The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. The proposed method is only evaluated on math and general reasoning benchmarks, and it is not clear if it can be applied to other types of reasoning tasks. The proposed method requires a large number of rollouts to compute the process supervision signal, which may be computationally expensive.

**********

## Paper Decision (Rebuttal)

Reject (out of the borderline range for acceptance)

**********

## Paper Decision Final Feedback

The paper introduces GRPO-VPS, a method that extends Group Relative Policy Optimization (