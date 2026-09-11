## Reviewer

### Summary

This paper presents DiffusionGemma, an open-weight language model that uses discrete diffusion to generate text at high speed. Unlike traditional autoregressive models, DiffusionGemma refines blocks of 256 tokens in parallel, bypassing the sequential decoding bottleneck. It's trained by fine-tuning the Gemma 4 model, using a two-stage process that includes supervised fine-tuning and reinforcement learning with sampler distillation. This approach achieves a new balance between generation speed and model capability, outperforming autoregressive models in terms of speed and diffusion models in terms of intelligence. DiffusionGemma also retains the capabilities of its starting model, such as thinking mode and multimodal inputs, and can generate text autoregressively with minimal performance loss. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, and presents a case study on finetuning DiffusionGemma for downstream applications.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages.
2. The proposed method is novel and innovative, combining discrete diffusion with autoregressive generation to achieve high speed and high capability.
3. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results.
4. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

### Weaknesses

1. The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency.
3. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### Questions

1. How does the proposed method compare to existing methods in terms of speed and capability?
2. What is the computational cost of the proposed method, and how does it compare to existing methods?
3. What are the limitations of the proposed method, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a new approach to text generation, called DiffusionGemma, which combines discrete diffusion and autoregressive (AR) generation. DiffusionGemma is an open-weight language model that uses discrete diffusion to generate text at high speed. Unlike traditional AR models, DiffusionGemma refines blocks of 256 tokens in parallel, bypassing the sequential decoding bottleneck. It's trained by fine-tuning the Gemma 4 model, using a two-stage process that includes supervised fine-tuning and reinforcement learning with sampler distillation. This approach achieves a new balance between generation speed and model capability, outperforming AR models in terms of speed and diffusion models in terms of intelligence. DiffusionGemma also retains the capabilities of its starting model, such as thinking mode and multimodal inputs, and can generate text autoregressively with minimal performance loss. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, and presents a case study on finetuning DiffusionGemma for downstream applications.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper presents a new approach to text generation, called DiffusionGemma, which combines discrete diffusion and autoregressive (AR) generation. This approach achieves a new balance between generation speed and model capability, outperforming AR models in terms of speed and diffusion models in terms of intelligence.
2. DiffusionGemma is an open-weight language model that uses discrete diffusion to generate text at high speed. Unlike traditional AR models, DiffusionGemma refines blocks of 256 tokens in parallel, bypassing the sequential decoding bottleneck.
3. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, and presents a case study on finetuning DiffusionGemma for downstream applications.

### Weaknesses

1. The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency.
3. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### Questions

1. How does the proposed method compare to existing methods in terms of speed and capability?
2. What is the computational cost of the proposed method, and how does it compare to existing methods?
3. What are the limitations of the proposed method, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces DiffusionGemma, a text diffusion model that refines blocks of 256 tokens in parallel, achieving exceptional speed and retaining the capabilities of its autoregressive (AR) starting point. It uses a two-stage training pipeline, first fine-tuning the Gemma 4 model and then combining reinforcement learning with sampler distillation to improve generation quality and efficiency. DiffusionGemma is released with open weights, offering a new speed-to-intelligence frontier and potential for hybrid decoding. It outperforms AR models in speed and diffusion models in intelligence, with capabilities like thinking mode and multimodal inputs, and can generate text autoregressively with minimal performance loss.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability.
2. The paper presents a new open-weight language model that uses discrete diffusion to generate text at high speed, refining blocks of 256 tokens in parallel and bypassing the sequential decoding bottleneck.
3. The paper discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.
4. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results.

### Weaknesses

1. The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency.
3. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### Questions

1. How does the proposed method compare to existing methods in terms of speed and capability?
2. What is the computational cost of the proposed method, and how does it compare to existing methods?
3. What are the limitations of the proposed method, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces DiffusionGemma, a text diffusion model that refines blocks of 256 tokens in parallel, achieving exceptional speed and retaining the capabilities of its autoregressive (AR) starting point. It uses a two-stage training pipeline, first fine-tuning the Gemma 4 model and then combining reinforcement learning with sampler distillation to improve generation quality and efficiency. DiffusionGemma is released with open weights, offering a new speed-to-intelligence frontier and potential for hybrid decoding. It outperforms AR models in speed and diffusion models in intelligence, with capabilities like thinking mode and multimodal inputs, and can generate text autoregressively with minimal performance loss.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability.
2. The paper presents a new open-weight language model that uses discrete diffusion to generate text at high speed, refining blocks of 256 tokens in parallel and bypassing the sequential decoding bottleneck.
3. The paper discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.
4. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results.

### Weaknesses

1. The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency.
3. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### Questions

1. How does the proposed method compare to existing methods in terms of speed and capability?
2. What is the computational cost of the proposed method, and how does it compare to existing methods?
3. What are the limitations of the proposed method, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper presents an open-weight language model that uses discrete diffusion to generate text at high speed. The model refines blocks of 256 tokens in parallel, bypassing the sequential decoding bottleneck. The paper presents a two-stage training pipeline, first fine-tuning the Gemma 4 model and then combining reinforcement learning with sampler distillation to improve generation quality and efficiency. DiffusionGemma is released with open weights, offering a new speed-to-intelligence frontier and potential for hybrid decoding. It outperforms AR models in speed and diffusion models in intelligence, with capabilities like thinking mode and multimodal inputs, and can generate text autoregressively with minimal performance loss. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, and presents a case study on finetuning DiffusionGemma for downstream applications.

The reviewers acknowledge that the paper is well-written and easy to follow. They also appreciate the novelty and effectiveness of the proposed method. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. However, the reviewers also point out that the paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. They also suggest that the paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. Finally, the reviewers suggest that the paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

### Paper Decision Policy

* Strong reject: As a clear reject, there is no need for a discussion with authors.
* Weak reject: Unlikely to get to the bar at ICLR. Authors are encouraged to discuss with the reviewers, and use the feedback to improve the paper.
* Marginally below the acceptance threshold: Could get to the bar at ICLR, but not this year. Authors are encouraged to discuss with the reviewers, and use the feedback to improve the paper for the next submission.
* Marginally above the acceptance threshold: Could get rejected at ICLR. Authors are encouraged to discuss with the reviewers, and use the feedback to improve the paper.
* Accept: At the bar or above. Authors may choose to decline if they think the paper is not ready.
* Excellent paper: Well written and very interesting. Well above the acceptance threshold.
* Spotlight: Accept and highlight the paper with a spotlight.
* Oral: Accept, highlight the paper with an oral.
* Camera-Ready: There are errors in the paper that need to be corrected before publication. Please correct the errors and resubmit a new version.
* ResubmitForReview: The paper is not yet at the acceptance threshold, but has a high potential. Authors are encouraged to revisit the major concerns of the reviewers, and game changers are encouraged to resubmit.
* Reject: Not at the acceptance threshold. Can be revised and resubmitted.
* Weak reject with revision: Very unlikely to get to the bar at ICLR. Authors are encouraged to take a major revision, and resubmit another round.
* Double reject: As a clear reject, there is no need for a discussion with authors.
* Not applicable: Not an oral, spotlight, or regular paper.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision Policy

* Strong reject: As a clear reject, there is no need for a discussion with authors.
* Weak reject: Unlikely to get to the bar at ICLR. Authors are encouraged to discuss with the reviewers, and use the feedback to improve the paper.
* Marginally below the acceptance threshold: Could get to the bar at ICLR, but not this year. Authors are encouraged to discuss with the reviewers, and use the feedback to improve the paper for the next submission.
* Marginally above the acceptance threshold: Could get rejected at ICLR. Authors are encouraged to discuss with the reviewers, and use the feedback to improve the paper.
* Accept: At the bar or above. Authors may choose to decline if they think the paper is not ready.
* Excellent paper: Well written and very interesting. Well above the acceptance threshold.
* Spotlight: Accept and highlight the paper with a spotlight.
* Oral: Accept, highlight the paper with an oral.
* Camera-Ready: There are errors in the paper that need to be corrected before publication. Please correct the errors and resubmit a new version.
* ResubmitForReview: The paper is not yet at the acceptance threshold, but has a high potential. Authors are encouraged to revisit the major concerns of the reviewers, and game changers are encouraged to resubmit.
* Reject: Not at the acceptance threshold. Can be revised and resubmitted.
* Weak reject with revision: Very unlikely to get to the bar at ICLR. Authors are encouraged to take a major revision, and resubmit another round.
* Double reject: As a clear reject, there is no need for a discussion with authors.
* Not applicable: Not an oral, spotlight, or regular paper.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. The paper does not provide a detailed discussion of the limitations of the proposed method, making it difficult to assess its potential applications and limitations.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors provide a detailed explanation of their method and its advantages. The paper presents a novel approach to text generation, combining discrete diffusion with autoregressive generation, which achieves a new balance between generation speed and model capability. The paper provides a comprehensive evaluation of the proposed method, including both quantitative and qualitative results. The paper also discusses the practical advantages of text diffusion, including bidirectional reasoning and self-correction, which are not typically found in autoregressive models.

**********

**********

## Paper Decision: Reject (out of the scope of ICLR)

**********

**********

### justification_for_why_not_higher_score

The paper does not provide a detailed comparison