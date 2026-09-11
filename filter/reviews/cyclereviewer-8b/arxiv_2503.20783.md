## Reviewer

### Summary

This paper studies the R1-zero-like training, and the authors have identified two issues: 1) the base model already has the ability to answer questions, and 2) the optimization bias in the GRPO algorithm. The authors also propose a new algorithm Dr. GRPO to address the second issue.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The authors have conducted a comprehensive analysis of the R1-zero-like training, and the paper is well-written and easy to follow.

### Weaknesses

1. The paper lacks novelty. The authors have identified two issues in the R1-zero-like training, but the proposed solution is simply removing the normalization terms in the GRPO algorithm, which is a straightforward fix. 
2. The paper lacks experiments. The authors have only conducted experiments on a small number of models and datasets, and the results are not convincing.

### Questions

1. What is the novelty of this paper? The authors have identified two issues in the R1-zero-like training, but the proposed solution is simply removing the normalization terms in the GRPO algorithm, which is a straightforward fix. 
2. What is the significance of this paper? The authors have only conducted experiments on a small number of models and datasets, and the results are not convincing. 
3. The authors have identified that the base model already has the ability to answer questions, and this may lead to the "aha moment" phenomenon. However, the authors did not provide any evidence to support this claim. 
4. The authors have proposed a new algorithm Dr. GRPO to address the optimization bias in the GRPO algorithm. However, the authors did not provide any theoretical analysis to support the effectiveness of this algorithm.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper studies the R1-Zero training, which is a new paradigm for enhancing the reasoning capabilities of LLMs by directly applying RL to base LLMs without relying on supervised fine-tuning. The paper analyzes the two core components of R1-Zero training: base models and RL algorithms. The authors investigate a range of base models, including DeepSeek-V3-Base and Qwen2.5, and find that Qwen2.5 models exhibit strong reasoning capabilities even without prompt templates, suggesting potential pretraining biases. Additionally, the paper identifies an optimization bias in Group Relative Policy Optimization (GRPO), which artificially increases response length (especially for incorrect outputs) during training. To address this, the authors introduce Dr. GRPO, an unbiased optimization method that improves token efficiency while maintaining reasoning performance. Leveraging these insights, the paper presents a minimalist R1-Zero recipe that achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. This paper studies the R1-Zero training, which is a new paradigm for enhancing the reasoning capabilities of LLMs by directly applying RL to base LLMs without relying on supervised fine-tuning. 
2. The authors investigate a range of base models, including DeepSeek-V3-Base and Qwen2.5, and find that Qwen2.5 models exhibit strong reasoning capabilities even without prompt templates, suggesting potential pretraining biases. 
3. The paper identifies an optimization bias in Group Relative Policy Optimization (GRPO), which artificially increases response length (especially for incorrect outputs) during training. To address this, the authors introduce Dr. GRPO, an unbiased optimization method that improves token efficiency while maintaining reasoning performance. 
4. Leveraging these insights, the paper presents a minimalist R1-Zero recipe that achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model.

### Weaknesses

1. The authors have not conducted experiments on more models, such as LLaMA-2 and Vicuna. 
2. The authors have not conducted experiments on more datasets, such as MATH and AMC. 
3. The authors have not conducted experiments on more tasks, such as commonsense reasoning and natural language inference. 
4. The authors have not conducted experiments on more RL algorithms, such as REINFORCE and PPO. 
5. The authors have not conducted experiments on more hyperparameters, such as learning rate and batch size.

### Questions

1. Can you explain why the Qwen2.5 models exhibit strong reasoning capabilities even without prompt templates? 
2. Can you explain why the GRPO introduces an optimization bias? 
3. Can you explain why the Dr. GRPO improves token efficiency while maintaining reasoning performance? 
4. Can you explain why the minimalist R1-Zero recipe achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model? 
5. Can you conduct experiments on more models, such as LLaMA-2 and Vicuna? 
6. Can you conduct experiments on more datasets, such as MATH and AMC? 
7. Can you conduct experiments on more tasks, such as commonsense reasoning and natural language inference? 
8. Can you conduct experiments on more RL algorithms, such as REINFORCE and PPO? 
9. Can you conduct experiments on more hyperparameters, such as learning rate and batch size?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper studies R1-Zero training and its two core components: base models and RL algorithms. The paper analyzes the base model and finds that the Qwen2.5 models already exhibit strong reasoning capabilities. The paper also analyzes the Group Relative Policy Optimization (GRPO) and finds that it introduces an optimization bias that artificially increases response length during training. The paper proposes a new optimization method, Dr. GRPO, that improves token efficiency while maintaining reasoning performance. Finally, the paper presents a minimalist R1-Zero recipe that achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper studies an important topic in LLM research: R1-Zero training. 
2. The paper analyzes the base model and finds that the Qwen2.5 models already exhibit strong reasoning capabilities. 
3. The paper analyzes the Group Relative Policy Optimization (GRPO) and finds that it introduces an optimization bias that artificially increases response length during training. 
4. The paper proposes a new optimization method, Dr. GRPO, that improves token efficiency while maintaining reasoning performance. 
5. The paper presents a minimalist R1-Zero recipe that achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model.

### Weaknesses

1. The paper's contribution is not very clear. The paper analyzes the base model and finds that the Qwen2.5 models already exhibit strong reasoning capabilities. The paper also analyzes the Group Relative Policy Optimization (GRPO) and finds that it introduces an optimization bias that artificially increases response length during training. The paper proposes a new optimization method, Dr. GRPO, that improves token efficiency while maintaining reasoning performance. Finally, the paper presents a minimalist R1-Zero recipe that achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model. However, it is not clear how these contributions are related to each other, and how they contribute to the field of R1-Zero training.
2. The paper's results are not very convincing. The paper presents a minimalist R1-Zero recipe that achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model. However, it is not clear how this result is achieved, and how it compares to other methods. The paper does not provide a thorough comparison with other methods, and it does not provide a detailed analysis of the results.

### Questions

1. What is the contribution of this paper? How do the contributions of the paper relate to each other?
2. How does the proposed method compare to other methods in terms of accuracy and efficiency?
3. What are the limitations of the proposed method? How can they be addressed?
4. What are the potential applications of the proposed method? How can it be used in practice?
5. What are the future directions for this research? How can this research be extended?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the R1-Zero training, which is a new paradigm for enhancing the reasoning capabilities of LLMs by directly applying RL to base LLMs without relying on supervised fine-tuning. The paper analyzes the two core components of R1-Zero training: base models and RL algorithms. The authors investigate a range of base models, including DeepSeek-V3-Base and Qwen2.5, and find that Qwen2.5 models exhibit strong reasoning capabilities even without prompt templates, suggesting potential pretraining biases. Additionally, the paper identifies an optimization bias in Group Relative Policy Optimization (GRPO), which artificially increases response length (especially for incorrect outputs) during training. To address this, the authors introduce Dr. GRPO, an unbiased optimization method that improves token efficiency while maintaining reasoning performance. Leveraging these insights, the paper presents a minimalist R1-Zero recipe that achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper studies the R1-Zero training, which is a new paradigm for enhancing the reasoning capabilities of LLMs by directly applying RL to base LLMs without relying on supervised fine-tuning.
2. The paper analyzes the two core components of R1-Zero training: base models and RL algorithms.
3. The authors investigate a range of base models, including DeepSeek-V3-Base and Qwen2.5, and find that Qwen2.5 models exhibit strong reasoning capabilities even without prompt templates, suggesting potential pretraining biases.
4. The paper identifies an optimization bias in Group Relative Policy Optimization (GRPO), which artificially increases response length (especially for incorrect outputs) during training.
5. To address this, the authors introduce Dr. GRPO, an unbiased optimization method that improves token efficiency while maintaining reasoning performance.
6. Leveraging these insights, the paper presents a minimalist R1-Zero recipe that achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model.

### Weaknesses

1. The paper lacks novelty. The authors have identified two issues in the R1-zero-like training, but the proposed solution is simply removing the normalization terms in the GRPO algorithm, which is a straightforward fix.
2. The paper lacks experiments. The authors have only conducted experiments on a small number of models and datasets, and the results are not convincing.
3. The paper lacks theoretical analysis. The authors have not provided any theoretical analysis to support the effectiveness of the proposed method.

### Questions

1. Can you explain why the Qwen2.5 models exhibit strong reasoning capabilities even without prompt templates?
2. Can you explain why the GRPO introduces an optimization bias?
3. Can you explain why the Dr. GRPO improves token efficiency while maintaining reasoning performance?
4. Can you explain why the minimalist R1-Zero recipe achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model?
5. Can you provide more experiments to support the effectiveness of the proposed method?
6. Can you provide more theoretical analysis to support the effectiveness of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies R1-Zero training, which is a new paradigm for enhancing the reasoning capabilities of LLMs by directly applying RL to base LLMs without relying on supervised fine-tuning. The paper analyzes the two core components of R1-Zero training: base models and RL algorithms. The authors investigate a range of base models, including DeepSeek-V3-Base and Qwen2.5, and find that Qwen2.5 models exhibit strong reasoning capabilities even without prompt templates, suggesting potential pretraining biases. Additionally, the paper identifies an optimization bias in Group Relative Policy Optimization (GRPO), which artificially increases response length (especially for incorrect outputs) during training. To address this, the authors introduce Dr. GRPO, an unbiased optimization method that improves token efficiency while maintaining reasoning performance. Leveraging these insights, the paper presents a minimalist R1-Zero recipe that achieves a new state-of-the-art accuracy on AIME 2024 with a 7B base model.

The paper has received four reviews, all of which have rated it as "marginally below the acceptance threshold". The reviewers have raised several concerns about the novelty, experiments, and theoretical analysis of the paper. The authors have provided a response to the reviews, but the reviewers have not updated their ratings. The AC has carefully read the paper, reviews, and response, and agrees with the reviewers that the paper has several weaknesses. The paper lacks novelty, as the proposed solution is simply removing the normalization terms in the GRPO algorithm, which is a straightforward fix. The paper also lacks experiments, as the authors have only conducted experiments on a small number of models and datasets, and the results are not convincing. The paper also lacks theoretical analysis, as the authors have not provided any theoretical analysis to support the effectiveness of the proposed method. Therefore, the AC recommends rejecting the paper.

### justification_for_why_not_higher_score

The paper lacks novelty, experiments, and theoretical analysis.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)