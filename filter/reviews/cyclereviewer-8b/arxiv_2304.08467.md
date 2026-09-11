## Reviewer

### Summary

The paper proposes a method called "gisting" to compress prompts into a smaller set of tokens, which can be cached and reused for compute efficiency. The method involves training an LM to predict the gist tokens given the prompt, and then using these gist tokens to generate the output. The authors evaluate their method on decoder-only (LLaMA-7B) and encoder-decoder (FLAN-T5-XXL) LMs and show that it enables up to 26x compression of prompts, resulting in up to 40% FLOPs reductions, 4.2% wall time speedups, and storage savings, all with minimal loss in output quality.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper addresses an important problem of prompt compression in LMs, which can lead to significant compute and memory savings.
- The proposed method is simple and effective, and can be applied to various LM architectures.
- The evaluation is thorough and shows promising results.

### Weaknesses

- The paper lacks a clear motivation for the proposed method. The authors mention that the goal is to compress prompts into a smaller set of tokens, but it is not clear why this is necessary or what the benefits of doing so are.
- The evaluation is limited to a single dataset and a single LM architecture. It would be helpful to see how the method performs on other datasets and architectures.
- The paper does not provide a clear comparison to other methods for prompt compression. It would be helpful to see how the proposed method compares to other methods in terms of performance and efficiency.

### Questions

- Can you provide more details on the motivation for the proposed method? What are the benefits of compressing prompts into a smaller set of tokens?
- Can you provide more details on the evaluation? How does the method perform on other datasets and architectures?
- Can you provide a comparison to other methods for prompt compression? How does the proposed method compare in terms of performance and efficiency?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a method called gisting to compress prompts into a smaller set of tokens, which can be cached and reused for compute efficiency. The method involves training an LM to predict the gist tokens given the prompt, and then using these gist tokens to generate the output. The authors evaluate their method on decoder-only (LLaMA-7B) and encoder-decoder (FLAN-T5-XXL) LMs and show that it enables up to 26x compression of prompts, resulting in up to 40% FLOPs reductions, 4.2% wall time speedups, and storage savings, all with minimal loss in output quality.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The idea of compressing prompts into a smaller set of tokens is interesting and can lead to significant compute and memory savings.
2. The proposed method is simple and effective, and can be applied to various LM architectures.
3. The evaluation is thorough and shows promising results.

### Weaknesses

1. The paper lacks a clear motivation for the proposed method. The authors mention that the goal is to compress prompts into a smaller set of tokens, but it is not clear why this is necessary or what the benefits of doing so are.
2. The evaluation is limited to a single dataset and a single LM architecture. It would be helpful to see how the method performs on other datasets and architectures.
3. The paper does not provide a clear comparison to other methods for prompt compression. It would be helpful to see how the proposed method compares to other methods in terms of performance and efficiency.

### Questions

1. Can you provide more details on the motivation for the proposed method? What are the benefits of compressing prompts into a smaller set of tokens?
2. Can you provide more details on the evaluation? How does the method perform on other datasets and architectures?
3. Can you provide a comparison to other methods for prompt compression? How does the proposed method compare in terms of performance and efficiency?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to compress prompts into a smaller set of tokens, which can be cached and reused for compute efficiency. The method involves training an LM to predict the gist tokens given the prompt, and then using these gist tokens to generate the output. The authors evaluate their method on decoder-only (LLaMA-7B) and encoder-decoder (FLAN-T5-XXL) LMs and show that it enables up to 26x compression of prompts, resulting in up to 40% FLOPs reductions, 4.2% wall time speedups, and storage savings, all with minimal loss in output quality.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The idea of compressing prompts into a smaller set of tokens is interesting and can lead to significant compute and memory savings.
2. The proposed method is simple and effective, and can be applied to various LM architectures.
3. The evaluation is thorough and shows promising results.

### Weaknesses

1. The paper lacks a clear motivation for the proposed method. The authors mention that the goal is to compress prompts into a smaller set of tokens, but it is not clear why this is necessary or what the benefits of doing so are.
2. The evaluation is limited to a single dataset and a single LM architecture. It would be helpful to see how the method performs on other datasets and architectures.
3. The paper does not provide a clear comparison to other methods for prompt compression. It would be helpful to see how the proposed method compares to other methods in terms of performance and efficiency.

### Questions

1. Can you provide more details on the motivation for the proposed method? What are the benefits of compressing prompts into a smaller set of tokens?
2. Can you provide more details on the evaluation? How does the method perform on other datasets and architectures?
3. Can you provide a comparison to other methods for prompt compression? How does the proposed method compare in terms of performance and efficiency?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to compress prompts into a smaller set of tokens, which can be cached and reused for compute efficiency. The method involves training an LM to predict the gist tokens given the prompt, and then using these gist tokens to generate the output. The authors evaluate their method on decoder-only (LLaMA-7B) and encoder-decoder (FLAN-T5-XXL) LMs and show that it enables up to 26x compression of prompts, resulting in up to 40% FLOPs reductions, 4.2% wall time speedups, and storage savings, all with minimal loss in output quality.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The idea of compressing prompts into a smaller set of tokens is interesting and can lead to significant compute and memory savings.
2. The proposed method is simple and effective, and can be applied to various LM architectures.
3. The evaluation is thorough and shows promising results.

### Weaknesses

1. The paper lacks a clear motivation for the proposed method. The authors mention that the goal is to compress prompts into a smaller set of tokens, but it is not clear why this is necessary or what the benefits of doing so are.
2. The evaluation is limited to a single dataset and a single LM architecture. It would be helpful to see how the method performs on other datasets and architectures.
3. The paper does not provide a clear comparison to other methods for prompt compression. It would be helpful to see how the proposed method compares to other methods in terms of performance and efficiency.

### Questions

1. Can you provide more details on the motivation for the proposed method? What are the benefits of compressing prompts into a smaller set of tokens?
2. Can you provide more details on the evaluation? How does the method perform on other datasets and architectures?
3. Can you provide a comparison to other methods for prompt compression? How does the proposed method compare in terms of performance and efficiency?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a method to compress prompts into a smaller set of tokens, which can be cached and reused for compute efficiency. The method involves training an LM to predict the gist tokens given the prompt, and then using these gist tokens to generate the output. The authors evaluate their method on decoder-only (LLaMA-7B) and encoder-decoder (FLAN-T5-XXL) LMs and show that it enables up to 26x compression of prompts, resulting in up to 40% FLOPs reductions, 4.2% wall time speedups, and storage savings, all with minimal loss in output quality.

### justification_for_why_not_higher_score

This paper received four reviews with scores of 5, 5, 5, and 5. The reviewers raised several concerns, including the lack of motivation for the proposed method, limited evaluation, and lack of comparison to other methods. The authors did not provide a response to the reviews.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject

**********

## Paper Decision Overview

Reject

**********

## Paper Decision Comments

The paper received four reviews with scores of 5, 5, 5, and 5. The reviewers raised several concerns, including the lack of motivation for the proposed method, limited evaluation, and lack of comparison to other methods. The authors did not provide a response to the reviews. Therefore, the paper is rejected.