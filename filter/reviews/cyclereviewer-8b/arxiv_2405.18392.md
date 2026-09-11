## Reviewer

### Summary

This paper proposes a constant learning rate schedule with a cooldown period as an alternative to the cosine learning rate schedule, which is commonly used for training large language models. The authors argue that this alternative schedule can provide similar performance to the cosine schedule while being more flexible and reducing the need for multiple training runs with different lengths. They also investigate the use of stochastic weight averaging as a replacement for the cooldown period and find that it can provide strong performance at any point during training. The authors demonstrate the effectiveness of their approach through experiments on a range of model sizes and training datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed approach is simple and easy to implement.
3. The experiments are comprehensive and well-designed.

### Weaknesses

1. The paper does not provide a thorough theoretical analysis of the proposed approach. It would be helpful to understand the underlying reasons for the effectiveness of the constant learning rate schedule with a cooldown period.
2. The paper does not provide a detailed comparison with other learning rate schedules, such as the inverse square root schedule, which is commonly used for training large language models.
3. The paper does not provide a detailed analysis of the computational costs of the proposed approach, particularly in terms of memory usage and training time.

### Questions

1. How does the proposed approach compare to other learning rate schedules, such as the inverse square root schedule?
2. Can you provide a detailed analysis of the computational costs of the proposed approach?
3. How does the proposed approach perform on other tasks, such as classification and generation?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper studies the scaling laws and compute-optimal training of LLMs. The authors argue that the cosine schedule is not necessary for LLM training and propose a constant learning rate with cooldown schedule as an alternative. They show that the proposed schedule can achieve similar performance as the cosine schedule and can be used for scaling law research.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed schedule is simple and easy to implement.
2. The proposed schedule can achieve similar performance as the cosine schedule.
3. The proposed schedule can be used for scaling law research.

### Weaknesses

1. The proposed schedule is not always better than the cosine schedule. For example, in Figure 8, the cosine schedule achieves better performance than the proposed schedule on some benchmarks.
2. The proposed schedule is not always better than the cosine schedule in terms of training loss. For example, in Figure 3, the cosine schedule achieves lower training loss than the proposed schedule.
3. The proposed schedule is not always better than the cosine schedule in terms of scaling law. For example, in Figure 12, the cosine schedule achieves better scaling law than the proposed schedule.

### Questions

1. Why does the cosine schedule perform better than the proposed schedule in some cases?
2. Why does the cosine schedule achieve lower training loss than the proposed schedule in some cases?
3. Why does the cosine schedule achieve better scaling law than the proposed schedule in some cases?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper studies the scaling laws and compute-optimal training of LLMs. The authors argue that the cosine schedule is not necessary for LLM training and propose a constant learning rate with cooldown schedule as an alternative. They show that the proposed schedule can achieve similar performance as the cosine schedule and can be used for scaling law research.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed schedule is simple and easy to implement.
2. The proposed schedule can achieve similar performance as the cosine schedule.
3. The proposed schedule can be used for scaling law research.

### Weaknesses

1. The proposed schedule is not always better than the cosine schedule. For example, in Figure 8, the cosine schedule achieves better performance than the proposed schedule on some benchmarks.
2. The proposed schedule is not always better than the cosine schedule in terms of training loss. For example, in Figure 3, the cosine schedule achieves lower training loss than the proposed schedule.
3. The proposed schedule is not always better than the cosine schedule in terms of scaling law. For example, in Figure 12, the cosine schedule achieves better scaling law than the proposed schedule.

### Questions

1. Why does the cosine schedule perform better than the proposed schedule in some cases?
2. Why does the cosine schedule achieve lower training loss than the proposed schedule in some cases?
3. Why does the cosine schedule achieve better scaling law than the proposed schedule in some cases?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper argues that the cosine schedule is not necessary for LLM training and proposes a constant learning rate with cooldown schedule as an alternative. They show that the proposed schedule can achieve similar performance as the cosine schedule and can be used for scaling law research.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed schedule is simple and easy to implement.
2. The proposed schedule can achieve similar performance as the cosine schedule.
3. The proposed schedule can be used for scaling law research.

### Weaknesses

1. The proposed schedule is not always better than the cosine schedule. For example, in Figure 8, the cosine schedule achieves better performance than the proposed schedule on some benchmarks.
2. The proposed schedule is not always better than the cosine schedule in terms of training loss. For example, in Figure 3, the cosine schedule achieves lower training loss than the proposed schedule.
3. The proposed schedule is not always better than the cosine schedule in terms of scaling law. For example, in Figure 12, the cosine schedule achieves better scaling law than the proposed schedule.

### Questions

1. Why does the cosine schedule perform better than the proposed schedule in some cases?
2. Why does the cosine schedule achieve lower training loss than the proposed schedule in some cases?
3. Why does the cosine schedule achieve better scaling law than the proposed schedule in some cases?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

The paper proposes a constant learning rate with a cooldown schedule as an alternative to the cosine learning rate schedule, which is commonly used for training large language models. The authors argue that this alternative schedule can provide similar performance to the cosine schedule while being more flexible and reducing the need for multiple training runs with different lengths. They also investigate the use of stochastic weight averaging as a replacement for the cooldown period and find that it can provide strong performance at any point during training. The authors demonstrate the effectiveness of their approach through experiments on a range of model sizes and training datasets.

The reviewers raised several concerns about the paper, including the lack of a thorough theoretical analysis, the lack of comparison with other learning rate schedules, and the lack of detailed analysis of computational costs. The authors provided additional experiments and analysis in the rebuttal, but the reviewers still have concerns about the paper's contributions and the robustness of the results.

### justification_for_why_not_higher_score

The reviewers raised several concerns about the paper, including the lack of a thorough theoretical analysis, the lack of comparison with other learning rate schedules, and the lack of detailed analysis of computational costs. The authors provided additional experiments and analysis in the rebuttal, but the reviewers still have concerns about the paper's contributions and the robustness of the results.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication for ICLR 2024)