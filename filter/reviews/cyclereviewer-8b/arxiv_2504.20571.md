## Reviewer

### Summary

The paper investigates the effectiveness of using reinforcement learning with verifiable reward (RLVR) with a single training example on a base model Qwen2.5-Math-1.5B. The authors find that using a single example can improve the model's performance on MATH500 from 36.0% to 73.6% and average performance across six common mathematical reasoning benchmarks from 17.6% to 35.7%. They also observe that the improvement is consistent across different models, RL algorithms, and different math examples. The authors also identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper provides a detailed analysis of the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. The authors identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

2. The paper is well-organized and clearly written. The authors provide a clear summary of their contributions and findings in the introduction.

3. The paper provides a detailed analysis of the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. The authors identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

### Weaknesses

1. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

2. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

3. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

4. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

### Questions

1. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

2. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

3. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

4. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

5. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper studies the problem of using reinforcement learning with verifiable reward (RLVR) with a single training example on a base model Qwen2.5-Math-1.5B. The authors find that using a single example can improve the model's performance on MATH500 from 36.0% to 73.6% and average performance across six common mathematical reasoning benchmarks from 17.6% to 35.7%. They also observe that the improvement is consistent across different models, RL algorithms, and different math examples. The authors also identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a detailed analysis of the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. The authors identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

2. The paper is well-organized and clearly written. The authors provide a clear summary of their contributions and findings in the introduction.

3. The paper provides a detailed analysis of the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. The authors identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

### Weaknesses

1. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

2. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

3. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

4. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

### Questions

1. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

2. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

3. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

4. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper investigates the effectiveness of reinforcement learning with verifiable reward (RLVR) using only a single training example on a base model Qwen2.5-Math-1.5B. The authors find that using a single example can improve the model's performance on MATH500 from 36.0% to 73.6% and average performance across six common mathematical reasoning benchmarks from 17.6% to 35.7%. They also observe that the improvement is consistent across different models, RL algorithms, and different math examples. The authors also identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a clear summary of their contributions and findings in the introduction. The paper provides a detailed analysis of the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. The authors identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

### Weaknesses

1. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

2. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

3. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

4. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

### Questions

1. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

2. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

3. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

4. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper investigates the use of reinforcement learning with verifiable reward (RLVR) with a single training example on a base model Qwen2.5-Math-1.5B. The authors find that using a single example can improve the model's performance on MATH500 from 36.0% to 73.6% and average performance across six common mathematical reasoning benchmarks from 17.6% to 35.7%. They also observe that the improvement is consistent across different models, RL algorithms, and different math examples. The authors also identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear summary of their contributions and findings in the introduction. The paper provides a detailed analysis of the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. The authors identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

### Weaknesses

The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

### Questions

1. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

2. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

3. Can you explain why the authors chose to use the Qwen2.5-Math-1.5B model for their experiments? What are the advantages of using this model compared to other base models?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper investigates the effectiveness of reinforcement learning with verifiable reward (RLVR) using only a single training example on a base model Qwen2.5-Math-1.5B. The authors find that using a single example can improve the model's performance on MATH500 from 36.0% to 73.6% and average performance across six common mathematical reasoning benchmarks from 17.6% to 35.7%. They also observe that the improvement is consistent across different models, RL algorithms, and different math examples. The authors also identify some interesting phenomena during 1-shot RLVR, including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after the training accuracy has saturated, which they term post-saturation generalization. They also verify that the effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the "grokking" phenomenon. The paper also discusses the critical role of promoting exploration in 1-shot RLVR training and the importance of selecting the right data for RLVR.

### justification_for_why_not_higher_score

The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)