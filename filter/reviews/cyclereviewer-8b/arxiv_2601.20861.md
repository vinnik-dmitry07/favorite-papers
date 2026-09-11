## Reviewer

### Summary

The paper investigates the catastrophic forgetting of LLMs when using evolutionary strategies (ES) for continual learning. The authors show that ES is able to reach comparable performance to gradient-based optimization (GRPO) on several math and reasoning benchmarks, but at the cost of significant model degradation and forgetting of existing abilities. The authors also analyze the characteristics of ES updates that lead to catastrophic forgetting, including large norm and low sparsity levels.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The experiments are well-designed and the results are convincing.
- The analysis of ES updates is thorough and insightful.

### Weaknesses

- The paper only evaluates ES on a limited set of tasks and models, which may not be representative of the broader LLM landscape.
- The paper only considers a single type of ES implementation, which may not be representative of all ES variants.
- The paper does not provide any insights into how to mitigate catastrophic forgetting in ES.

### Questions

- How do the results generalize to other types of LLMs, such as those with different sizes or architectures?
- How do the results generalize to other types of ES implementations, such as those with different population sizes or mutation rates?
- Are there any potential solutions to mitigate catastrophic forgetting in ES?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper compares the performance of evolutionary strategies and gradient-based optimization for continual learning in LLMs. The authors show that while ES can match the performance of GRPO on some tasks, it suffers from catastrophic forgetting, and this is due to the large norm and low sparsity of the updates.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The authors conduct a comprehensive empirical study of ES and GRPO on multiple tasks and models.
- The analysis of the norm and sparsity of the updates is insightful and provides a good explanation of the forgetting behavior of ES.

### Weaknesses

- The paper only evaluates ES and GRPO on a limited set of tasks and models. It would be interesting to see how these methods perform on a broader set of tasks and models.
- The paper does not provide any insights into how to mitigate catastrophic forgetting in ES. It would be interesting to see if there are any techniques that can be used to improve the forgetting behavior of ES.
- The paper does not compare ES to other continual learning methods, such as online learning or episodic memory methods. It would be interesting to see how ES compares to these methods in terms of forgetting.

### Questions

- How do the results generalize to other types of LLMs, such as those with different sizes or architectures?
- How do the results generalize to other types of ES implementations, such as those with different population sizes or mutation rates?
- Are there any potential solutions to mitigate catastrophic forgetting in ES?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper investigates the catastrophic forgetting of LLMs when using evolutionary strategies (ES) for continual learning. The authors show that ES is able to reach comparable performance to gradient-based optimization (GRPO) on several math and reasoning benchmarks, but at the cost of significant model degradation and forgetting of existing abilities. The authors also analyze the characteristics of ES updates that lead to catastrophic forgetting, including large norm and low sparsity levels.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The experiments are well-designed and the results are convincing. The analysis of ES updates is thorough and insightful. The paper also provides a comprehensive comparison of ES and GRPO on multiple tasks and models, which helps to understand the performance of ES in continual learning.

### Weaknesses

The paper only evaluates ES and GRPO on a limited set of tasks and models. It would be interesting to see how these methods perform on a broader set of tasks and models. The paper does not provide any insights into how to mitigate catastrophic forgetting in ES. It would be interesting to see if there are any techniques that can be used to improve the forgetting behavior of ES.

### Questions

How do the results generalize to other types of LLMs, such as those with different sizes or architectures? How do the results generalize to other types of ES implementations, such as those with different population sizes or mutation rates? Are there any potential solutions to mitigate catastrophic forgetting in ES?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper studies the catastrophic forgetting problem of LLMs when using evolutionary strategies (ES) for continual learning. The authors show that ES is able to reach comparable performance to gradient-based optimization (GRPO) on several math and reasoning benchmarks, but at the cost of significant model degradation and forgetting of existing abilities. The authors also analyze the characteristics of ES updates that lead to catastrophic forgetting, including large norm and low sparsity levels.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

This paper is well-written and easy to follow. The experiments are well-designed and the results are convincing. The analysis of ES updates is thorough and insightful. The paper also provides a comprehensive comparison of ES and GRPO on multiple tasks and models, which helps to understand the performance of ES in continual learning.

### Weaknesses

The paper only evaluates ES and GRPO on a limited set of tasks and models. It would be interesting to see how these methods perform on a broader set of tasks and models. The paper does not provide any insights into how to mitigate catastrophic forgetting in ES. It would be interesting to see if there are any techniques that can be used to improve the forgetting behavior of ES.

### Questions

How do the results generalize to other types of LLMs, such as those with different sizes or architectures? How do the results generalize to other types of ES implementations, such as those with different population sizes or mutation rates? Are there any potential solutions to mitigate catastrophic forgetting in ES?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper investigates the catastrophic forgetting of LLMs when using evolutionary strategies (ES) for continual learning. The authors show that ES is able to reach comparable performance to gradient-based optimization (GRPO) on several math and reasoning benchmarks, but at the cost of significant model degradation and forgetting of existing abilities. The authors also analyze the characteristics of ES updates that lead to catastrophic forgetting, including large norm and low sparsity levels.

The paper is well-written and easy to follow. The experiments are well-designed and the results are convincing. The analysis of ES updates is thorough and insightful. The paper also provides a comprehensive comparison of ES and GRPO on multiple tasks and models, which helps to understand the performance of ES in continual learning.

### justification_for_why_not_higher_score

The paper only evaluates ES and GRPO on a limited set of tasks and models. It would be interesting to see how these methods perform on a broader set of tasks and models. The paper does not provide any insights into how to mitigate catastrophic forgetting in ES. It would be interesting to see if there are any techniques that can be used to improve the forgetting behavior of ES.

### justification_for_why_not_lower_score

This paper is well-written and easy to follow. The experiments are well-designed and the results are convincing. The analysis of ES updates is thorough and insightful. The paper also provides a comprehensive comparison of ES and GRPO on multiple tasks and models, which helps to understand the performance of ES in continual learning.

**********

## Paper Decision

Accept (poster)