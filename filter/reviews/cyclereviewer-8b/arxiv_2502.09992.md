## Reviewer

### Summary

This paper introduces LLaDA, a diffusion model trained from scratch under the pre-training and supervised fine-tuning (SFT) paradigm. LLaDA employs a forward data masking process and a reverse generation process, parameterized by a Transformer to predict masked tokens. It provides a principled generative approach for probabilistic inference by optimizing a likelihood lower bound. Across extensive benchmarks on general tasks, math, code, and so on, LLaDA demonstrates strong scalability and performs comparably to our self-constructed ARM baselines. Remarkably, LLaDA 8B is competitive with strong LLMs like LLaMA3 8B in in-context learning and, after SFT, exhibits impressive instruction-following abilities in case studies such as multi-turn dialogue. Moreover, LLaDA addresses the reversal curse, surpassing GPT-4o in a reversal poem completion task. Our findings show the promise of diffusion models for language modeling at scale and challenge the common assumption that core LLM capabilities discussed above inherently depend on ARMs.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper is well-organized and easy to understand.
3. The paper is well-structured and easy to follow.
4. The paper is well-referenced and easy to follow.

### Weaknesses

1. The paper lacks novelty. The proposed method is very similar to MaskGIT. The only difference is the training data and the model size. The authors should compare their method with MaskGIT more comprehensively.
2. The paper lacks experimental results. The authors only provide results on a few datasets. It is hard to evaluate the performance of the proposed method.
3. The paper lacks theoretical analysis. The authors should provide a theoretical analysis of the proposed method.
4. The paper lacks ablation study. The authors should provide an ablation study to evaluate the effect of different components of the proposed method.
5. The paper lacks discussion. The authors should discuss the limitations of the proposed method and potential future work.

### Questions

1. What is the main difference between the proposed method and MaskGIT?
2. What are the advantages of the proposed method compared to MaskGIT?
3. What are the limitations of the proposed method?
4. What are the potential future work?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper presents a diffusion model for language modeling, which is trained from scratch. The model is trained by masking tokens in the input sequence, and the model is trained to predict the masked tokens. The authors show that the model achieves strong performance on various tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a good motivation for their work and explain the method clearly. The results are promising and show that the model achieves strong performance on various tasks.

### Weaknesses

The main weakness of the paper is that it is unclear whether the proposed method is novel. The method is based on the MaskGIT paper, and the authors do not provide any new insights or contributions. The authors should clarify the novelty of their work and provide more details on the differences between their method and MaskGIT.

### Questions

Please see the weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a diffusion-based language model, LLaDA, which is trained from scratch. The authors claim that LLaDA can achieve comparable performance to autoregressive models (ARMs) with the same scale, and it has some unique advantages such as bidirectional modeling and enhanced robustness.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The proposed method achieves comparable performance to ARMs with the same scale.

### Weaknesses

1. The proposed method is not novel enough. The idea of diffusion-based language models has been explored in previous work, such as MaskGIT. The authors should compare their method with MaskGIT more comprehensively.
2. The authors claim that LLaDA has some unique advantages such as bidirectional modeling and enhanced robustness. However, the authors do not provide enough evidence to support this claim.
3. The authors did not perform a comprehensive comparison with other diffusion-based language models, such as MaskGIT and DeepSeek.

### Questions

1. How does LLaDA compare to MaskGIT in terms of performance and computational cost?
2. Can LLaDA handle long-range dependencies like ARMs?
3. How does LLaDA compare to other diffusion-based language models in terms of performance and computational cost?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a novel approach to language modeling by training a diffusion model from scratch. The proposed model is trained to predict masked tokens in a sequence and is shown to achieve comparable performance to autoregressive models on various tasks. The authors also demonstrate the model's ability to perform in-context learning and instruction-following. The paper also shows that the proposed model is able to perform well on reversal tasks, which is a limitation of autoregressive models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper proposes a novel approach to language modeling by training a diffusion model from scratch. The proposed model is trained to predict masked tokens in a sequence and is shown to achieve comparable performance to autoregressive models on various tasks. The authors also demonstrate the model's ability to perform in-context learning and instruction-following. The paper also shows that the proposed model is able to perform well on reversal tasks, which is a limitation of autoregressive models.

### Weaknesses

The paper lacks a detailed analysis of the computational cost of the proposed model. The paper mentions that the model was trained on 0.13 million H800 GPU hours, but it would be helpful to have a more detailed breakdown of the computational cost, including the number of parameters, training time, and inference time.

### Questions

- How does the proposed model compare to other language models in terms of computational cost?
- How does the proposed model perform on long-range dependency tasks?
- How does the proposed model perform on tasks that require reasoning and problem-solving?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces LLaDA, a diffusion model trained from scratch under the pre-training and supervised fine-tuning (SFT) paradigm. LLaDA employs a forward data masking process and a reverse generation process, parameterized by a Transformer to predict masked tokens. It provides a principled generative approach for probabilistic inference by optimizing a likelihood lower bound. Across extensive benchmarks on general tasks, math, code, and so on, LLaDA demonstrates strong scalability and performs comparably to our self-constructed ARM baselines. Remarkably, LLaDA 8B is competitive with strong LLMs like LLaMA3 8B in in-context learning and, after SFT, exhibits impressive instruction-following abilities in case studies such as multi-turn dialogue. Moreover, LLaDA addresses the reversal curse, surpassing GPT-4o in a reversal poem completion task. Our findings show the promise of diffusion models for language modeling at scale and challenge the common assumption that core LLM capabilities discussed above inherently depend on ARMs.

The paper received mixed reviews. The reviewers found the paper well-written and the proposed method simple and effective. However, there were concerns about the novelty of the method and the lack of comprehensive comparisons with other diffusion-based language models. The authors provided a response to the reviewers, but the reviewers remained unconvinced about the novelty of the method and the significance of the results. The AC agrees with the reviewers that the paper lacks novelty and the results are not sufficiently convincing. Therefore, the paper is not recommended for acceptance.

### justification_for_why_not_higher_score

The paper lacks novelty and the results are not sufficiently convincing.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)