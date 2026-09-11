## Reviewer

### Summary

The paper presents a novel approach to improve the performance of Large Language Models (LLMs) by selectively removing higher-order components from their weight matrices. The authors propose a method called LAyer-SElective Rank reduction (LASER) that can be applied after training, without requiring additional parameters or data. The paper demonstrates the generality of this approach across various language models and datasets, providing insights into when and how LASER is effective. The authors also analyze the relationship between the model's training data and the samples that benefit from LASER, suggesting that it offers a denoising procedure that makes weakly learned facts accessible. Additionally, the paper explores the robustness of LASER to paraphrases and the storage of high-order components in weight matrices.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper presents a novel approach to improving LLMs by selectively removing higher-order components from their weight matrices, which is a simple yet effective intervention.
2. The paper demonstrates the generality of this approach across various language models and datasets, providing insights into when and how LASER is effective.
3. The paper analyzes the relationship between the model's training data and the samples that benefit from LASER, suggesting that it offers a denoising procedure that makes weakly learned facts accessible.

### Weaknesses

1. The paper lacks a clear explanation of the underlying mechanism of LASER and how it improves the performance of LLMs. While the paper provides some insights into the relationship between the model's training data and the samples that benefit from LASER, it does not provide a comprehensive explanation of how LASER works.
2. The paper does not provide a thorough evaluation of the robustness of LASER to different types of noise and perturbations. While the paper shows that LASER is robust to paraphrases, it does not provide a comprehensive evaluation of its robustness to other types of noise and perturbations.
3. The paper does not provide a clear comparison of LASER with other methods for improving LLMs. While the paper shows that LASER can improve the performance of LLMs, it does not provide a comparison with other methods that can also improve LLMs.

### Questions

1. Can you provide a more comprehensive explanation of the underlying mechanism of LASER and how it improves the performance of LLMs?
2. Can you provide a more thorough evaluation of the robustness of LASER to different types of noise and perturbations?
3. Can you provide a clear comparison of LASER with other methods for improving LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper introduces a method called LASER that reduces the rank of weight matrices in a transformer to improve performance on reasoning tasks. The authors show that this method can be applied to various models and datasets, and that it can improve performance even when 99% of the weight matrix is removed. The authors also analyze the relationship between the training data and the samples that benefit from LASER, and find that LASER improves performance on information that is less common in the training data.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents a novel method for improving the performance of large language models on reasoning tasks by selectively removing higher-order components of their weight matrices. This approach is simple, effective, and can be applied to various models and datasets.

2. The paper provides a thorough analysis of the relationship between the model's training data and the samples that benefit from LASER. The authors find that LASER improves performance on information that is less common in the training data, which suggests that it acts as a denoising technique that makes weakly learned facts accessible.

3. The paper evaluates the generality of LASER across multiple language models and datasets, and finds that it consistently improves performance on reasoning tasks.

### Weaknesses

1. The paper does not provide a detailed explanation of the underlying mechanism of LASER and how it improves the performance of LLMs. While the paper provides some insights into the relationship between the model's training data and the samples that benefit from LASER, it does not provide a comprehensive explanation of how LASER works.

2. The paper does not provide a thorough comparison of LASER with other methods for improving LLMs. While the paper shows that LASER can improve the performance of LLMs, it does not provide a comparison with other methods that can also improve LLMs.

3. The paper does not provide a clear explanation of how LASER can be applied to other types of models beyond large language models. While the paper evaluates LASER on multiple language models, it does not provide a clear explanation of how LASER can be applied to other types of models, such as computer vision models or reinforcement learning models.

### Questions

1. Can you provide a more detailed explanation of the underlying mechanism of LASER and how it improves the performance of LLMs?

2. Can you provide a more thorough comparison of LASER with other methods for improving LLMs?

3. Can you provide a clear explanation of how LASER can be applied to other types of models beyond large language models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a method to improve the performance of LLMs by selectively reducing the rank of weight matrices in the model. The authors show that this method can be applied to various models and datasets, and that it can improve performance even when 99% of the weight matrix is removed. The authors also analyze the relationship between the training data and the samples that benefit from this method, and find that it improves performance on information that is less common in the training data.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper presents a novel method for improving the performance of large language models on reasoning tasks by selectively removing higher-order components of their weight matrices. This approach is simple, effective, and can be applied to various models and datasets.

The paper provides a thorough analysis of the relationship between the model's training data and the samples that benefit from this method. The authors find that this method improves performance on information that is less common in the training data, which suggests that it acts as a denoising technique that makes weakly learned facts accessible.

The paper evaluates the generality of this method across multiple language models and datasets, and finds that it consistently improves performance on reasoning tasks.

### Weaknesses

The paper does not provide a detailed explanation of the underlying mechanism of this method and how it improves the performance of LLMs. While the paper provides some insights into the relationship between the model's training data and the samples that benefit from this method, it does not provide a comprehensive explanation of how it works.

The paper does not provide a thorough comparison of this method with other methods for improving LLMs. While the paper shows that this method can improve the performance of LLMs, it does not provide a comparison with other methods that can also improve LLMs.

The paper does not provide a clear explanation of how this method can be applied to other types of models beyond large language models. While the paper evaluates this method on multiple language models, it does not provide a clear explanation of how it can be applied to other types of models, such as computer vision models or reinforcement learning models.

### Questions

1. Can you provide a more detailed explanation of the underlying mechanism of this method and how it improves the performance of LLMs?

2. Can you provide a more thorough comparison of this method with other methods for improving LLMs?

3. Can you provide a clear explanation of how this method can be applied to other types of models beyond large language models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to improve the performance of LLMs by selectively reducing the rank of weight matrices in the model. The authors show that this method can be applied to various models and datasets, and that it can improve performance even when 99% of the weight matrix is removed. The authors also analyze the relationship between the training data and the samples that benefit from this method, and find that it improves performance on information that is less common in the training data.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper presents a novel method for improving the performance of large language models on reasoning tasks by selectively removing higher-order components of their weight matrices. This approach is simple, effective, and can be applied to various models and datasets.

The paper provides a thorough analysis of the relationship between the model's training data and the samples that benefit from this method. The authors find that this method improves performance on information that is less common in the training data, which suggests that it acts as a denoising technique that makes weakly learned facts accessible.

The paper evaluates the generality of this method across multiple language models and datasets, and finds that it consistently improves performance on reasoning tasks.

### Weaknesses

The paper does not provide a detailed explanation of the underlying mechanism of this method and how it improves the performance of LLMs. While the paper provides some insights into the relationship between the model's training data and the samples that benefit from this method, it does not provide a comprehensive explanation of how it works.

The paper does not provide a thorough comparison of this method with other methods for improving LLMs. While the paper shows that this method can improve the performance of LLMs, it does not provide a comparison with other methods that can also improve LLMs.

The paper does not provide a clear explanation of how this method can be applied to other types of models beyond large language models. While the paper evaluates this method on multiple language models, it does not provide a clear explanation of how it can be applied to other types of models, such as computer vision models or reinforcement learning models.

### Questions

1. Can you provide a more detailed explanation of the underlying mechanism of this method and how it improves the performance of LLMs?

2. Can you provide a more thorough comparison of this method with other methods for improving LLMs?

3. Can you provide a clear explanation of how this method can be applied to other types of models beyond large language models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a method called LASER that reduces the rank of weight matrices in a transformer to improve performance on reasoning tasks. The authors show that this method can be applied to various models and datasets, and that it can improve performance even when 99% of the weight matrix is removed. The authors also analyze the relationship between the training data and the samples that benefit from LASER, and find that LASER improves performance on information that is less common in the training data.

The paper is well written and easy to follow. The proposed method is simple and effective. The paper also provides a thorough analysis of the relationship between the model's training data and the samples that benefit from LASER. The authors find that LASER improves performance on information that is less common in the training data, which suggests that it acts as a denoising technique that makes weakly learned facts accessible.

However, the paper does not provide a detailed explanation of the underlying mechanism of LASER and how it improves the performance of LLMs. While the paper provides some insights into the relationship between the model's training data and the samples that benefit from LASER, it does not provide a comprehensive explanation of how LASER works.

### justification_for_why_not_higher_score

The paper does not provide a detailed explanation of the underlying mechanism of LASER and how it improves the performance of LLMs.

### justification_for_why_not_lower_score

The paper is well written and easy to follow. The proposed method is simple and effective. The paper also provides a thorough analysis of the relationship between the model's training data and the samples that benefit from LASER. The authors find that LASER improves performance on information that is less common in the training data, which suggests that it acts as a denoising technique that makes weakly learned facts accessible.

**********

## Paper Decision

Accept (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster)