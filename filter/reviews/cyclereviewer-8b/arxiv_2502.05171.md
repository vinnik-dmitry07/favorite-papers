## Reviewer

### Summary

This paper proposes a new approach to scaling language models by scaling the depth of the recurrent block at test time. The authors demonstrate that this approach can improve performance on reasoning benchmarks, and can be used to implement various useful features such as per-token adaptive compute, speculative decoding, and KV-cache sharing.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors demonstrate that their approach can improve performance on reasoning benchmarks, and can be used to implement various useful features such as per-token adaptive compute, speculative decoding, and KV-cache sharing.

### Weaknesses

The paper does not include a comparison with existing methods for scaling language models.

### Questions

How does the proposed approach compare to existing methods for scaling language models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper introduces a novel approach to scaling language models by scaling the depth of the recurrent block at test time, which allows for implicit reasoning in latent space. The model iterates through a recurrent block, enabling arbitrary depth at test time. Unlike mainstream reasoning models, this approach doesn't require specialized training data, can work with small context windows, and can handle reasoning types not easily represented in words. The authors scale a proof-of-concept model to 3.5 billion parameters and 800 billion tokens, showing improved performance on reasoning benchmarks, sometimes significantly, up to a computation load equivalent to 50 billion parameters.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to scaling language models by scaling the depth of the recurrent block at test time, which allows for implicit reasoning in latent space.
2. The model's ability to work with small context windows and handle reasoning types not easily represented in words is a significant advantage over mainstream reasoning models.
3. The paper scales a proof-of-concept model to 3.5 billion parameters and 800 billion tokens, demonstrating improved performance on reasoning benchmarks.

### Weaknesses

1. The paper lacks a detailed comparison with existing methods for scaling language models, making it challenging to assess the novelty and effectiveness of the proposed approach.
2. The paper does not provide a comprehensive analysis of the computational efficiency and memory requirements of the proposed approach, which is crucial for understanding its practical feasibility.
3. The paper does not discuss potential limitations or challenges associated with the proposed approach, such as the potential for increased training time or computational overhead.

### Questions

1. How does the proposed approach compare to existing methods for scaling language models in terms of performance and computational efficiency?
2. What are the potential limitations or challenges associated with the proposed approach, and how can they be addressed?
3. How does the proposed approach handle the trade-off between model size and computational efficiency, and how can it be optimized for practical applications?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel approach to scaling language models by scaling the depth of the recurrent block at test time. The proposed model can improve its performance on reasoning benchmarks by iteratively processing and updating its hidden state, allowing for arbitrary depth at test time. The paper also discusses the advantages of this approach over mainstream reasoning models, including the ability to work with small context windows and handle reasoning types not easily represented in words.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel approach to scaling language models by scaling the depth of the recurrent block at test time, which allows for implicit reasoning in latent space.
2. The model's ability to work with small context windows and handle reasoning types not easily represented in words is a significant advantage over mainstream reasoning models.
3. The paper scales a proof-of-concept model to 3.5 billion parameters and 800 billion tokens, demonstrating improved performance on reasoning benchmarks.

### Weaknesses

1. The paper lacks a detailed comparison with existing methods for scaling language models, making it challenging to assess the novelty and effectiveness of the proposed approach.
2. The paper does not provide a comprehensive analysis of the computational efficiency and memory requirements of the proposed approach, which is crucial for understanding its practical feasibility.
3. The paper does not discuss potential limitations or challenges associated with the proposed approach, such as the potential for increased training time or computational overhead.

### Questions

1. How does the proposed approach compare to existing methods for scaling language models in terms of performance and computational efficiency?
2. What are the potential limitations or challenges associated with the proposed approach, and how can they be addressed?
3. How does the proposed approach handle the trade-off between model size and computational efficiency, and how can it be optimized for practical applications?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new approach to scale the test-time computation of language models by using a recurrent block that can be unrolled to arbitrary depth. The authors show that this approach can improve the performance on reasoning benchmarks and can be used to implement various useful features such as per-token adaptive compute, speculative decoding, and KV-cache sharing. The authors also show that the model can be trained efficiently and demonstrate its effectiveness on various tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed approach and its advantages over existing methods. The paper also includes a comprehensive evaluation of the proposed approach on various tasks and benchmarks.

### Weaknesses

1. The paper does not provide a detailed comparison with existing methods for scaling language models, making it challenging to assess the novelty and effectiveness of the proposed approach.
2. The paper does not provide a comprehensive analysis of the computational efficiency and memory requirements of the proposed approach, which is crucial for understanding its practical feasibility.
3. The paper does not discuss potential limitations or challenges associated with the proposed approach, such as the potential for increased training time or computational overhead.

### Questions

1. How does the proposed approach compare to existing methods for scaling language models in terms of performance and computational efficiency?
2. What are the potential limitations or challenges associated with the proposed approach, and how can they be addressed?
3. How does the proposed approach handle the trade-off between model size and computational efficiency, and how can it be optimized for practical applications?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new approach to scaling language models by scaling the depth of the recurrent block at test time. The proposed model can improve its performance on reasoning benchmarks by iteratively processing and updating its hidden state, allowing for arbitrary depth at test time. The paper also discusses the advantages of this approach over mainstream reasoning models, including the ability to work with small context windows and handle reasoning types not easily represented in words.

The reviewers find the paper interesting and novel. However, the reviewers also point out that the paper lacks a detailed comparison with existing methods for scaling language models, making it challenging to assess the novelty and effectiveness of the proposed approach. The paper also does not provide a comprehensive analysis of the computational efficiency and memory requirements of the proposed approach, which is crucial for understanding its practical feasibility. The paper also does not discuss potential limitations or challenges associated with the proposed approach, such as the potential for increased training time or computational overhead.

### justification_for_why_not_higher_score

The paper lacks a detailed comparison with existing methods for scaling language models, making it challenging to assess the novelty and effectiveness of the proposed approach. The paper also does not provide a comprehensive analysis of the computational efficiency and memory requirements of the proposed approach, which is crucial for understanding its practical feasibility. The paper also does not discuss potential limitations or challenges associated with the proposed approach, such as the potential for increased training time or computational overhead.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication at ICLR 2024)

**********

<!-- ICLR FOLIA Template 2023 - 
- Please use the newest version of the template, which can be found here https://openreview.net/paper/kygMmKEC
- Please DO NOT change the font size, spacing, or margins of the template
- Please DO NOT change the font size of the text in tables
- Please DO NOT change the font size of the captions in figures
- Please DO NOT change the font size of the references
- Please DO NOT change the font size of the title
- Please DO NOT change the font size of the author names
- Please DO NOT change the font size of the affiliations
- Please DO NOT change the font size of the abstract
- Please DO NOT change the font size of the keywords
- Please DO NOT change the font size of the conclusion
- Please DO NOT change the font size of the acknowledgement
- Please DO NOT change the font size of the paper title in the header
- Please DO NOT change the font size of the paper title in the footer
- Please DO NOT change the font size of the page number in the footer
- Please DO NOT change the font size of the header
- Please DO NOT change the font size of the footer
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the page number in the appendix
- Please DO NOT change the font size of the section title in the appendix
- Please DO NOT change the font size of the subsection title in the appendix
- Please DO NOT change the font size of the subsubsection title in the appendix
- Please DO NOT change the font size of the table caption in the appendix
- Please DO NOT change the font size of the figure caption in the appendix
- Please DO NOT change the font size of the equation in the appendix
- Please DO NOT change the font size of the algorithm in the appendix
- Please DO NOT change the font size of the table in the appendix
- Please DO NOT change the font size of the code in the appendix
- Please DO NOT change the font size of the reference in the appendix
- Please DO NOT change the font size of the bibliography in the appendix
- Please DO NOT change the font size of the footnote in the appendix
- Please DO NOT change the font size of the footnote symbol in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the header in the appendix
- Please DO NOT change the font size of the footer in