## Reviewer

### Summary

This paper studies the scaling laws of knowledge in language models. It proposes a method to estimate the knowledge bits a model stores and shows that language models can store 2 bits of knowledge per parameter, even when quantized to int8. The paper also explores various factors that affect knowledge storage capacity, including training duration, model architecture, quantization, sparsity, and data signal-to-noise ratio.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper studies an important topic of knowledge storage capacity in language models. The proposed method to estimate knowledge bits is interesting and novel. The paper is well-written and easy to follow.

### Weaknesses

The paper focuses on a synthetic dataset and doesn't study the knowledge storage capacity of real-world language models. The results are not generalizable to real-world models. The paper also doesn't discuss the limitations of the proposed method.

### Questions

- What are the limitations of the proposed method? How can it be improved?
- Can the proposed method be applied to real-world language models?
- What are the implications of the findings for the design of language models?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a framework to study the knowledge storage capacity of language models. The authors define knowledge as (name, attribute, value) tuples, such as (Anya Forger, birthday, 10/2/1996). The authors generate synthetic knowledge-only datasets by uniformly at random generating (name, attribute, value) tuples from a knowledge base and converting them into English descriptions. The authors then train language models (e.g., GPT-2, LLaMA, Mistral) on these texts using a standard auto-regressive objective from random initialization, and “estimate” the learned knowledge. The authors evaluate the knowledge storage capacity of language models by comparing the models’ trainable parameters to the bit complexity lower bounds.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors present a novel framework to study the knowledge storage capacity of language models.

### Weaknesses

- The authors only evaluate the knowledge storage capacity of the GPT-2 architecture. It would be more interesting to evaluate other architectures, such as LLaMA and Mistral.
- The authors only evaluate the knowledge storage capacity of language models on synthetic data. It would be more interesting to evaluate the knowledge storage capacity of language models on real-world data.
- The authors do not discuss the limitations of their framework.

### Questions

- How do the results generalize to other architectures, such as LLaMA and Mistral?
- How do the results generalize to real-world data?
- What are the limitations of the proposed framework?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the scaling laws of knowledge in language models. The authors propose a method to estimate the knowledge bits a model stores and show that language models can store 2 bits of knowledge per parameter, even when quantized to int8. The paper also explores various factors that affect knowledge storage capacity, including training duration, model architecture, quantization, sparsity, and data signal-to-noise ratio.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

This paper is well-written and easy to follow. The authors propose a novel method to estimate the knowledge bits a model stores. The paper also explores various factors that affect knowledge storage capacity, including training duration, model architecture, quantization, sparsity, and data signal-to-noise ratio. The paper also provides a theoretical analysis of the knowledge storage capacity of language models.

### Weaknesses

The paper only studies the knowledge storage capacity of language models on synthetic data. It would be more interesting to evaluate the knowledge storage capacity of language models on real-world data. The paper also does not discuss the limitations of the proposed method.

### Questions

How do the results generalize to real-world data? What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the scaling laws of language models, specifically the relationship between model size and the total bits of knowledge stored. The authors introduce a principled framework to examine highly accurate scaling laws concerning model size versus its knowledge storage capacity. They define a piece of knowledge as a (name, attribute, value) tuple and generate synthetic knowledge-only datasets by uniformly at random generating (name, attribute, value) tuples from a knowledge base and converting them into English descriptions. The authors train language models (e.g., GPT-2, LLaMA, Mistral) on these texts using a standard auto-regressive objective from random initialization, and “estimate” the learned knowledge. By varying the number of knowledge pieces and model sizes, they outline a knowledge capacity scaling law. The authors also explore various factors that affect knowledge storage capacity, including training duration, model architecture, quantization, sparsity, and data signal-to-noise ratio.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper introduces a novel and principled framework to study the scaling laws of language models. The authors provide a theoretical analysis of the knowledge storage capacity of language models and explore various factors that affect knowledge storage capacity. The paper also provides a comprehensive evaluation of the knowledge storage capacity of different language models and architectures. The paper is well-written and easy to follow.

### Weaknesses

The paper only studies the knowledge storage capacity of language models on synthetic data. It would be more interesting to evaluate the knowledge storage capacity of language models on real-world data. The paper also does not discuss the limitations of the proposed method.

### Questions

How do the results generalize to real-world data? What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the scaling laws of knowledge in language models. The authors propose a method to estimate the knowledge bits a model stores and show that language models can store 2 bits of knowledge per parameter, even when quantized to int8. The paper also explores various factors that affect knowledge storage capacity, including training duration, model architecture, quantization, sparsity, and data signal-to-noise ratio.

The reviewers raised several concerns, including the limited scope of the experiments (only GPT-2 architecture) and the lack of discussion on the limitations of the proposed method. The authors addressed some of these concerns in their rebuttal, but the reviewers still have some concerns. The paper is a good start, but it needs to be improved before publication.

### justification_for_why_not_higher_score

The paper is a good start, but it needs to be improved before publication.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR)