## Reviewer

### Summary

This paper proposes a second-order optimization algorithm for language model pre-training. The proposed method, named Sophia, is a stochastic second-order optimizer that uses a light-weight estimate of the diagonal Hessian as the pre-conditioner. The update is the moving average of the gradients divided by the moving average of the estimated Hessian, followed by element-wise clipping. The clipping controls the worst-case update size and tames the negative impact of non-convexity and rapid change of Hessian along the trajectory. Sophia only estimates the diagonal Hessian every handful of iterations, which has negligible average per-step time and memory overhead. On language modeling with GPT models of sizes ranging from 125M to 1.5B, Sophia achieves a 2x speed-up compared to Adam in the number of steps, total compute, and wall-clock time, achieving the same perplexity with 50% fewer steps, less total compute, and reduced wall-clock time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and intuitive.
- The experimental results are promising.

### Weaknesses

- The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs.
- The proposed method is not compared with other second-order methods.

### Questions

- The proposed method is not compared with other second-order methods.
- The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new optimizer, Sophia, which is a second-order optimizer that uses a light-weight estimate of the diagonal Hessian as the pre-conditioner. The update is the moving average of the gradients divided by the moving average of the estimated Hessian, followed by element-wise clipping. The clipping controls the worst-case update size and tames the negative impact of non-convexity and rapid change of Hessian along the trajectory. Sophia only estimates the diagonal Hessian every handful of iterations, which has negligible average per-step time and memory overhead. On language modeling with GPT models of sizes ranging from 125M to 1.5B, Sophia achieves a 2x speed-up compared to Adam in the number of steps, total compute, and wall-clock time, achieving the same perplexity with 50% fewer steps, less total compute, and reduced wall-clock time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and intuitive. The experimental results are promising.

### Weaknesses

The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs.

### Questions

1. The proposed method is not compared with other second-order methods.
2. The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs.
3. The proposed method is not compared with other second-order methods.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes Sophia, a second-order optimizer for language model pre-training. Sophia uses a light-weight estimate of the diagonal Hessian as the pre-conditioner. The update is the moving average of the gradients divided by the moving average of the estimated Hessian, followed by element-wise clipping. The clipping controls the worst-case update size and tames the negative impact of non-convexity and rapid change of Hessian along the trajectory. Sophia only estimates the diagonal Hessian every handful of iterations, which has negligible average per-step time and memory overhead. Theoretical analysis is provided to show the advantage of Sophia in adapting to heterogeneous curvatures across parameter dimensions.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and intuitive.
- The experimental results are promising.

### Weaknesses

- The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs.
- The proposed method is not compared with other second-order methods.

### Questions

- The proposed method is not compared with other second-order methods.
- The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a second-order optimizer for training large language models. The proposed optimizer, Sophia, is a stochastic second-order optimizer that uses a light-weight estimate of the diagonal Hessian as the pre-conditioner. The update is the moving average of the gradients divided by the moving average of the estimated Hessian, followed by element-wise clipping. The clipping controls the worst-case update size and tames the negative impact of non-convexity and rapid change of Hessian along the trajectory. Sophia only estimates the diagonal Hessian every handful of iterations, which has negligible average per-step time and memory overhead. On language modeling with GPT models of sizes ranging from 125M to 1.5B, Sophia achieves a 2x speed-up compared to Adam in the number of steps, total compute, and wall-clock time, achieving the same perplexity with 50% fewer steps, less total compute, and reduced wall-clock time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and intuitive.
3. The experimental results are promising.

### Weaknesses

1. The proposed method is not compared with other second-order methods.
2. The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs.

### Questions

1. The proposed method is not compared with other second-order methods.
2. The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a second-order optimizer for training large language models. The proposed optimizer, Sophia, is a stochastic second-order optimizer that uses a light-weight estimate of the diagonal Hessian as the pre-conditioner. The update is the moving average of the gradients divided by the moving average of the estimated Hessian, followed by element-wise clipping. The clipping controls the worst-case update size and tames the negative impact of non-convexity and rapid change of Hessian along the trajectory. Sophia only estimates the diagonal Hessian every handful of iterations, which has negligible average per-step time and memory overhead. On language modeling with GPT models of sizes ranging from 125M to 1.5B, Sophia achieves a 2x speed-up compared to Adam in the number of steps, total compute, and wall-clock time, achieving the same perplexity with 50% fewer steps, less total compute, and reduced wall-clock time.

The paper received 4 reviews with scores 5, 5, 5, 5. The authors provided detailed responses to the reviewers, but the reviewers did not update their scores. The AC checked the paper and the reviews, and agrees with the reviewers that the paper is not ready for publication at ICLR.

### justification_for_why_not_higher_score

The paper received 4 reviews with scores 5, 5, 5, 5. The authors provided detailed responses to the reviewers, but the reviewers did not update their scores. The AC checked the paper and the reviews, and agrees with the reviewers that the paper is not ready for publication at ICLR.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (poster) (poster) **********

*Note: If authors want to resubmit the paper to a future conference, I would recommend to add more experiments to show that the proposed method works well for non-convex functions, and to compare with more baselines. Also, the theoretical analysis should be improved.*