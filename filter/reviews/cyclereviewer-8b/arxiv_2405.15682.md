## Reviewer

### Summary

This paper proposes a new method for optimizing convex functions. The proposed method is based on a new online-to-batch conversion theorem that unifies several existing online-to-batch theorems. The method does not require the stopping time T to be known or set in advance and closely tracks the Pareto frontier of loss versus training time during a single training run. The method is evaluated on 28 problems, ranging from logistic regression to large-scale deep learning problems, and shows strong performance, matching or out-performing heavily-tuned cosine schedules.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper is well written and easy to follow.
- The proposed method is simple and easy to implement.
- The method does not require the stopping time T to be known or set in advance and closely tracks the Pareto frontier of loss versus training time during a single training run.
- The method is evaluated on 28 problems, ranging from logistic regression to large-scale deep learning problems, and shows strong performance, matching or out-performing heavily-tuned cosine schedules.

### Weaknesses

- The paper only considers convex problems and does not provide any theoretical results for non-convex problems.
- The method requires the stopping time T to be known or set in advance, which may not always be possible in practice.
- The method requires the use of a new hyperparameter $\beta$ which may require additional tuning.
- The method does not provide any convergence guarantees for non-convex problems.

### Questions

- The paper only considers convex problems and does not provide any theoretical results for non-convex problems. Can the method be extended to non-convex problems?
- The method requires the stopping time T to be known or set in advance, which may not always be possible in practice. How does the method perform when T is unknown or set in advance?
- The method requires the use of a new hyperparameter $\beta$ which may require additional tuning. How does the method perform with different values of $\beta$?
- The method does not provide any convergence guarantees for non-convex problems. Can the method be extended to provide convergence guarantees for non-convex problems?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new approach to learning rate scheduling that does not require the specification of the stopping time $T$. The authors propose an approach that avoids the need for this stopping time by eschewing the use of schedules entirely, while exhibiting state-of-the-art performance compared to schedules across a wide family of problems ranging from convex problems to large-scale deep learning problems. The authors provide a theoretical analysis of the proposed method and show that it has a similar convergence rate as the Polyak-Ruppert averaging method. The authors also provide experimental results on a variety of deep learning tasks and show that the proposed method outperforms other optimization algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The authors provide a theoretical analysis of the proposed method and show that it has a similar convergence rate as the Polyak-Ruppert averaging method. The authors also provide experimental results on a variety of deep learning tasks and show that the proposed method outperforms other optimization algorithms.

### Weaknesses

The paper only considers convex problems and does not provide any theoretical results for non-convex problems. The method requires the stopping time $T$ to be known or set in advance, which may not always be possible in practice. The method requires the use of a new hyperparameter $\beta$ which may require additional tuning. The method does not provide any convergence guarantees for non-convex problems.

### Questions

1. The paper only considers convex problems and does not provide any theoretical results for non-convex problems. Can the method be extended to non-convex problems?
2. The method requires the stopping time $T$ to be known or set in advance, which may not always be possible in practice. How does the method perform when $T$ is unknown or set in advance?
3. The method requires the use of a new hyperparameter $\beta$ which may require additional tuning. How does the method perform with different values of $\beta$?
4. The method does not provide any convergence guarantees for non-convex problems. Can the method be extended to provide convergence guarantees for non-convex problems?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a new method for optimizing convex functions. The method does not require the stopping time $T$ to be known or set in advance and closely tracks the Pareto frontier of loss versus training time during a single training run. The method is evaluated on 28 problems, ranging from logistic regression to large-scale deep learning problems, and shows strong performance, matching or out-performing heavily-tuned cosine schedules.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The method does not require the stopping time $T$ to be known or set in advance and closely tracks the Pareto frontier of loss versus training time during a single training run. The method is evaluated on 28 problems, ranging from logistic regression to large-scale deep learning problems, and shows strong performance, matching or out-performing heavily-tuned cosine schedules.

### Weaknesses

The paper only considers convex problems and does not provide any theoretical results for non-convex problems. The method requires the stopping time $T$ to be known or set in advance, which may not always be possible in practice. The method requires the use of a new hyperparameter $\beta$ which may require additional tuning. The method does not provide any convergence guarantees for non-convex problems.

### Questions

1. The paper only considers convex problems and does not provide any theoretical results for non-convex problems. Can the method be extended to non-convex problems?
2. The method requires the stopping time $T$ to be known or set in advance, which may not always be possible in practice. How does the method perform when $T$ is unknown or set in advance?
3. The method requires the use of a new hyperparameter $\beta$ which may require additional tuning. How does the method perform with different values of $\beta$?
4. The method does not provide any convergence guarantees for non-convex problems. Can the method be extended to provide convergence guarantees for non-convex problems?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The authors propose a new method for learning rate scheduling that does not require the specification of the stopping time $T$. The proposed method is based on a new online-to-batch conversion theorem that unifies several existing online-to-batch theorems. The method does not require the stopping time $T$ to be known or set in advance and closely tracks the Pareto frontier of loss versus training time during a single training run. The method is evaluated on 28 problems, ranging from logistic regression to large-scale deep learning problems, and shows strong performance, matching or out-performing heavily-tuned cosine schedules.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and easy to implement. The method does not require the stopping time $T$ to be known or set in advance and closely tracks the Pareto frontier of loss versus training time during a single training run. The method is evaluated on 28 problems, ranging from logistic regression to large-scale deep learning problems, and shows strong performance, matching or out-performing heavily-tuned cosine schedules.

### Weaknesses

The paper only considers convex problems and does not provide any theoretical results for non-convex problems. The method requires the stopping time $T$ to be known or set in advance, which may not always be possible in practice. The method requires the use of a new hyperparameter $\beta$ which may require additional tuning. The method does not provide any convergence guarantees for non-convex problems.

### Questions

1. The paper only considers convex problems and does not provide any theoretical results for non-convex problems. Can the method be extended to non-convex problems?
2. The method requires the stopping time $T$ to be known or set in advance, which may not always be possible in practice. How does the method perform when $T$ is unknown or set in advance?
3. The method requires the use of a new hyperparameter $\beta$ which may require additional tuning. How does the method perform with different values of $\beta$?
4. The method does not provide any convergence guarantees for non-convex problems. Can the method be extended to provide convergence guarantees for non-convex problems?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

The paper presents a novel approach to learning rate scheduling that eliminates the need to specify the stopping time $T$. The method is based on a new online-to-batch conversion theorem that unifies existing online-to-batch theorems. The method is evaluated on 28 problems, ranging from logistic regression to large-scale deep learning problems, and shows strong performance, matching or out-performing heavily-tuned cosine schedules.

The reviewers raised several concerns regarding the paper's limitations, including its focus on convex problems, the requirement for the stopping time $T$ to be known or set in advance, and the need for additional tuning of the hyperparameter $\beta$. The authors did not provide a response to these concerns.

### justification_for_why_not_higher_score

The reviewers raised several concerns regarding the paper's limitations, including its focus on convex problems, the requirement for the stopping time $T$ to be known or set in advance, and the need for additional tuning of the hyperparameter $\beta$. The authors did not provide a response to these concerns.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)