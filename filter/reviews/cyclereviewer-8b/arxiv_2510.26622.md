## Reviewer

### Summary

This paper compares encoder-decoder and decoder-only models on pretraining and finetuning tasks. The authors compare the two models with different sizes and compute budgets, and also compare the two models on zero/few-shot learning and context length extrapolation. The authors find that while the decoder-only model is better at zero/few-shot learning, the encoder-decoder model is better at finetuning and context length extrapolation. The authors also find that the encoder-decoder model is more computationally efficient than the decoder-only model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive comparison of encoder-decoder and decoder-only models, including both pretraining and finetuning. The authors also provide a detailed analysis of the models' performance on zero/few-shot learning and context length extrapolation.

### Weaknesses

1. The authors only compare the performance of the encoder-decoder and decoder-only models on a single pretraining dataset (RedPajama V1). It would be interesting to see how the models perform on other pretraining datasets, such as the Common Crawl dataset used by LLaMA.

2. The authors only compare the performance of the encoder-decoder and decoder-only models on a single finetuning dataset (FLAN). It would be interesting to see how the models perform on other finetuning datasets, such as the OpenAI GPT-3 finetuning dataset.

3. The authors do not compare the performance of the encoder-decoder and decoder-only models on a wide range of tasks. It would be interesting to see how the models perform on tasks such as machine translation, question answering, and text summarization.

4. The authors do not compare the performance of the encoder-decoder and decoder-only models on a wide range of model sizes. It would be interesting to see how the models perform on smaller and larger models.

5. The authors do not compare the performance of the encoder-decoder and decoder-only models on a wide range of compute budgets. It would be interesting to see how the models perform on different compute budgets.

### Questions

1. How do the encoder-decoder and decoder-only models perform on other pretraining datasets, such as the Common Crawl dataset used by LLaMA?

2. How do the encoder-decoder and decoder-only models perform on other finetuning datasets, such as the OpenAI GPT-3 finetuning dataset?

3. How do the encoder-decoder and decoder-only models perform on a wide range of tasks, such as machine translation, question answering, and text summarization?

4. How do the encoder-decoder and decoder-only models perform on a wide range of model sizes, such as smaller and larger models?

5. How do the encoder-decoder and decoder-only models perform on a wide range of compute budgets, such as different compute budgets?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper compares encoder-decoder and decoder-only models in terms of their scaling behavior. The authors find that the two models have similar scaling exponents and that the decoder-only model is more computationally efficient. However, the encoder-decoder model performs better on certain tasks after instruction tuning. The authors also find that the encoder-decoder model has a better context-length extrapolation capability.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive comparison of encoder-decoder and decoder-only models, including both pretraining and finetuning. The authors also provide a detailed analysis of the models' performance on zero/few-shot learning and context length extrapolation.

### Weaknesses

The authors should consider including more model architectures in their comparison, such as the encoder-decoder model with a single decoder layer. This would provide a more comprehensive understanding of the scaling behavior of different model architectures.

### Questions

How do the results change if the encoder-decoder model has a single decoder layer?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper compares encoder-decoder and decoder-only LLMs on a range of tasks, including pretraining and finetuning. The authors find that while the decoder-only model performs better on zero-shot and few-shot tasks, the encoder-decoder model performs better on finetuning and context length extrapolation. The authors also find that the encoder-decoder model is more computationally efficient than the decoder-only model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive comparison of encoder-decoder and decoder-only models, including both pretraining and finetuning. The authors also provide a detailed analysis of the models' performance on zero/few-shot learning and context length extrapolation.

### Weaknesses

The paper would benefit from a more thorough analysis of the results. For example, the authors could provide more details on the specific tasks and datasets used in the experiments, as well as the specific metrics used to evaluate the models. Additionally, the authors could provide more discussion on the implications of the results for the development of future LLMs.

### Questions

How do the results change if the encoder-decoder model has a single decoder layer?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper conducts a comprehensive comparison of encoder-decoder LLMs and decoder-only LLMs in terms of pretraining and finetuning performance. The authors compare the two models with different sizes and compute budgets, and also compare the two models on zero/few-shot learning and context length extrapolation. The authors find that while the decoder-only model is better at zero/few-shot learning, the encoder-decoder model is better at finetuning and context length extrapolation. The authors also find that the encoder-decoder model is more computationally efficient than the decoder-only model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The authors provide a comprehensive comparison of encoder-decoder and decoder-only models, including both pretraining and finetuning. The authors also provide a detailed analysis of the models' performance on zero/few-shot learning and context length extrapolation.
3. The authors also find that the encoder-decoder model is more computationally efficient than the decoder-only model.

### Weaknesses

1. The authors only compare the performance of the encoder-decoder and decoder-only models on a single pretraining dataset (RedPajama V1). It would be interesting to see how the models perform on other pretraining datasets, such as the Common Crawl dataset used by LLaMA.
2. The authors only compare the performance of the encoder-decoder and decoder-only models on a single finetuning dataset (FLAN). It would be interesting to see how the models perform on other finetuning datasets, such as the OpenAI GPT-3 finetuning dataset.
3. The authors do not compare the performance of the encoder-decoder and decoder-only models on a wide range of tasks. It would be interesting to see how the models perform on tasks such as machine translation, question answering, and text summarization.
4. The authors do not compare the performance of the encoder-decoder and decoder-only models on a wide range of model sizes. It would be interesting to see how the models perform on smaller and larger models.
5. The authors do not compare the performance of the encoder-decoder and decoder-only models on a wide range of compute budgets. It would be interesting to see how the models perform on different compute budgets.

### Questions

1. How do the encoder-decoder and decoder-only models perform on other pretraining datasets, such as the Common Crawl dataset used by LLaMA?
2. How do the encoder-decoder and decoder-only models perform on other finetuning datasets, such as the OpenAI GPT-3 finetuning dataset?
3. How do the encoder-decoder and decoder-only models perform on a wide range of tasks, such as machine translation, question answering, and text summarization?
4. How do the encoder-decoder and decoder-only models perform on a wide range of model sizes, such as smaller and larger models?
5. How do the encoder-decoder and decoder-only models perform on a wide range of compute budgets, such as different compute budgets?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper compares encoder-decoder and decoder-only LLMs on a range of tasks, including pretraining and finetuning. The authors find that while the decoder-only model performs better on zero-shot and few-shot tasks, the encoder-decoder model performs better on finetuning and context length extrapolation. The authors also find that the encoder-decoder model is more computationally efficient than the decoder-only model. The paper is well-written and easy to follow. The authors provide a comprehensive comparison of encoder-decoder and decoder-only models, including both pretraining and finetuning. The authors also provide a detailed analysis of the models' performance on zero/few-shot learning and context length extrapolation. The paper is recommended for acceptance.

### justification_for_why_not_higher_score

N/A

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a comprehensive comparison of encoder-decoder and decoder-only models, including both pretraining and finetuning. The authors also provide a detailed analysis of the models' performance on zero/few-shot learning and context length extrapolation.

**********

## Paper Decision

Accept (poster)