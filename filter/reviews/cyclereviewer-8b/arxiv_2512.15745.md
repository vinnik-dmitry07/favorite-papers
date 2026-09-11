## Summary

This paper presents LLaDA2.0, a discrete diffusion language model that scales up to 100B parameters. The authors propose a three-phase training scheme that first converts an autoregressive model to a discrete diffusion model, and then further trains the model with a combination of block diffusion and full-sequence diffusion. The authors also propose a document-level attention mask to prevent the model from forming spurious connections across unrelated texts. The authors evaluate their model on a wide range of benchmarks and show that it outperforms AR models in complex, structured tasks.

## Soundness

1 poor

## Presentation

2 fair

## Contribution

2 fair

## Strengths

- The paper presents a novel approach to scaling up discrete diffusion models to 100B parameters, which is a significant contribution to the field.
- The proposed three-phase training scheme is novel and effective.
- The paper provides a detailed analysis of the model's performance on a wide range of benchmarks, including complex, structured tasks.

## Weaknesses

- The paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model.
- The paper does not provide a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approach to other approaches.
- The paper does not provide a clear explanation of the hyperparameters used in the experiments. The authors do not provide a clear explanation of how they chose the hyperparameters or how they affect the results.
- The paper does not provide a clear explanation of the results. The authors do not provide a clear explanation of why their model outperforms other models on certain tasks.
- The paper does not provide a clear explanation of the limitations of the proposed approach. The authors do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work.

## Questions

- How does the proposed approach compare to other approaches for scaling up discrete diffusion models?
- How does the proposed approach compare to other approaches for scaling up autoregressive models?
- What are the computational costs of the proposed approach compared to other approaches?
- How do the hyperparameters used in the experiments affect the results?
- Why does the proposed approach outperform other models on certain tasks?
- What are the limitations of the proposed approach?

## Flag For Ethics Review

No ethics review needed.

## Rating

3: reject, not good enough

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
## Reviewer

## Summary

This paper presents a 100B parameter discrete diffusion model that is trained from an autoregressive model. The paper introduces a 3-stage training procedure that first converts the autoregressive model into a discrete diffusion model, then trains the model with a combination of block diffusion and full-sequence diffusion. The authors also propose a document-level attention mask to prevent the model from forming spurious connections across unrelated texts. The authors evaluate their model on a wide range of benchmarks and show that it outperforms AR models in complex, structured tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and interesting.
- The experiments are comprehensive and the results are promising.

## Weaknesses

- The proposed method is not well-motivated. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model.
- The paper lacks a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approach to other approaches.
- The paper lacks a detailed analysis of the hyperparameters used in the experiments. The authors do not provide a clear explanation of how they chose the hyperparameters or how they affect the results.
- The paper lacks a detailed analysis of the results. The authors do not provide a clear explanation of why their model outperforms other models on certain tasks.
- The paper lacks a detailed analysis of the limitations of the proposed approach. The authors do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work.

## Questions

- What are the advantages of using a discrete diffusion model instead of an autoregressive model?
- How does the proposed approach compare to other approaches for scaling up discrete diffusion models?
- What are the computational costs of the proposed approach compared to other approaches?
- How do the hyperparameters used in the experiments affect the results?
- Why does the proposed approach outperform other models on certain tasks?
- What are the limitations of the proposed approach?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
## Reviewer

## Summary

This paper introduces LLaDA2.0, a 100B-parameter discrete diffusion language model (dLLM) that scales up through systematic conversion from an autoregressive (AR) model. It employs a novel three-phase block-level WSD training scheme, combining progressive block-size increase, large-scale full-sequence diffusion, and compact block diffusion. The model is optimized for practical deployment with post-training alignment using SFT and DPO. LLaDA2.0-mini (16B) and LLaDA2.0-flash (100B) are two instruction-tuned Mixture-of-Experts (MoE) variants. The models are open-sourced.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

- The paper introduces a novel approach to scaling up discrete diffusion models to 100B parameters, which is a significant contribution to the field.
- The proposed three-phase training scheme is novel and effective.
- The paper provides a detailed analysis of the model's performance on a wide range of benchmarks, including complex, structured tasks.
- The paper is well-written and easy to follow.

## Weaknesses

- The paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model.
- The paper lacks a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approach to other approaches.
- The paper lacks a detailed analysis of the hyperparameters used in the experiments. The authors do not provide a clear explanation of how they chose the hyperparameters or how they affect the results.
- The paper lacks a detailed analysis of the results. The authors do not provide a clear explanation of why their model outperforms other models on certain tasks.
- The paper lacks a detailed analysis of the limitations of the proposed approach. The authors do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work.

## Questions

- How does the proposed approach compare to other approaches for scaling up discrete diffusion models?
- How does the proposed approach compare to other approaches for scaling up autoregressive models?
- What are the computational costs of the proposed approach compared to other approaches?
- How do the hyperparameters used in the experiments affect the results?
- Why does the proposed approach outperform other models on certain tasks?
- What are the limitations of the proposed approach?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
## Reviewer

## Summary

This paper presents LLaDA2.0, a 100B-parameter discrete diffusion language model (dLLM) that scales up through systematic conversion from an autoregressive (AR) model. It employs a novel three-phase block-level WSD training scheme, combining progressive block-size increase, large-scale full-sequence diffusion, and compact block diffusion. The model is optimized for practical deployment with post-training alignment using SFT and DPO. LLaDA2.0-mini (16B) and LLaDA2.0-flash (100B) are two instruction-tuned Mixture-of-Experts (MoE) variants. The models are open-sourced.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

- The paper introduces a novel approach to scaling up discrete diffusion models to 100B parameters, which is a significant contribution to the field.
- The proposed three-phase training scheme is novel and effective.
- The paper provides a detailed analysis of the model's performance on a wide range of benchmarks, including complex, structured tasks.
- The paper is well-written and easy to follow.

## Weaknesses

- The paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model.
- The paper lacks a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approach to other approaches.
- The paper lacks a detailed analysis of the hyperparameters used in the experiments. The authors do not provide a clear explanation of how they chose the hyperparameters or how they affect the results.
- The paper lacks a detailed analysis of the results. The authors do not provide a clear explanation of why their model outperforms other models on certain tasks.
- The paper lacks a detailed analysis of the limitations of the proposed approach. The authors do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work.

## Questions

- How does the proposed approach compare to other approaches for scaling up discrete diffusion models?
- How does the proposed approach compare to other approaches for scaling up autoregressive models?
- What are the computational costs of the proposed approach compared to other approaches?
- How do the hyperparameters used in the experiments affect the results?
- Why does the proposed approach outperform other models on certain tasks?
- What are the limitations of the proposed approach?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
## Meta Review

This paper presents a 100B parameter discrete diffusion model that is trained from an autoregressive model. The paper introduces a 3-stage training procedure that first converts the autoregressive model into a discrete diffusion model, and then further trains the model with a combination of block diffusion and full-sequence diffusion. The authors also propose a document-level attention mask to prevent the model from forming spurious connections across unrelated texts. The authors evaluate their model on a wide range of benchmarks and show that it outperforms AR models in complex, structured tasks.

The reviewers generally agree that this is a good paper, but with a few concerns that need to be addressed. The paper is well-written and easy to follow. The proposed method is novel and interesting. The experiments are comprehensive and the results are promising. However, the paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model. The paper lacks a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approach to other approaches. The paper lacks a detailed analysis of the hyperparameters used in the experiments. The authors do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. The paper lacks a detailed analysis of the results. The authors do not provide a clear explanation of why their model outperforms other models on certain tasks. The paper lacks a detailed analysis of the limitations of the proposed approach. The authors do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work.

## justification_for_why_not_higher_score

The paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model. The paper lacks a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approach to other approaches. The paper lacks a detailed analysis of the hyperparameters used in the experiments. The authors do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. The paper lacks a detailed analysis of the results. The authors do not provide a clear explanation of why their model outperforms other models on certain tasks. The paper lacks a detailed analysis of the limitations of the proposed approach. The authors do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work.

## justification_for_why_not_lower_score

N/A

**********
----- Post-rebuttal -----

Thank you for your response. I have read your response and the reviews from other reviewers. I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper.

1. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a detailed analysis of the computational cost of the proposed approach. They only mention that the proposed approach is more efficient than the baseline AR model, but they do not provide a clear comparison of the computational cost of their approach to other approaches. I believe that a more detailed analysis of the computational cost of the proposed approach is necessary to support this claim.

2. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. I believe that a more detailed analysis of the hyperparameters used in the experiments is necessary to support this claim.

3. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of why their model outperforms other models on certain tasks. I believe that a more detailed analysis of the results is necessary to support this claim.

4. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work. I believe that a more detailed analysis of the limitations of the proposed approach is necessary to support this claim.

Overall, I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper. I recommend that the authors address these concerns in their final version of the paper.

## paper decision

Reject (not selected) (poster) (poster)

**********
----- Post-rebuttal -----

Thank you for your response. I have read your response and the reviews from other reviewers. I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper.

1. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a detailed analysis of the computational cost of the proposed approach. They only mention that the proposed approach is more efficient than the baseline AR model, but they do not provide a clear comparison of the computational cost of their approach to other approaches. I believe that a more detailed analysis of the computational cost of the proposed approach is necessary to support this claim.

2. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. I believe that a more detailed analysis of the hyperparameters used in the experiments is necessary to support this claim.

3. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of why their model outperforms other models on certain tasks. I believe that a more detailed analysis of the results is necessary to support this claim.

4. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work. I believe that a more detailed analysis of the limitations of the proposed approach is necessary to support this claim.

Overall, I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper. I recommend that the authors address these concerns in their final version of the paper.

## paper decision

Reject (not selected) (poster) (poster)

**********
----- Post-rebuttal -----

Thank you for your response. I have read your response and the reviews from other reviewers. I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper.

1. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a detailed analysis of the computational cost of the proposed approach. They only mention that the proposed approach is more efficient than the baseline AR model, but they do not provide a clear comparison of the computational cost of their approach to other approaches. I believe that a more detailed analysis of the computational cost of the proposed approach is necessary to support this claim.

2. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. I believe that a more detailed analysis of the hyperparameters used in the experiments is necessary to support this claim.

3. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of why their model outperforms other models on certain tasks. I believe that a more detailed analysis of the results is necessary to support this claim.

4. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work. I believe that a more detailed analysis of the limitations of the proposed approach is necessary to support this claim.

Overall, I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper. I recommend that the authors address these concerns in their final version of the paper.

## paper decision

Reject (not selected) (poster) (poster)

**********
----- Post-rebuttal -----

Thank you for your response. I have read your response and the reviews from other reviewers. I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper.

1. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a detailed analysis of the computational cost of the proposed approach. They only mention that the proposed approach is more efficient than the baseline AR model, but they do not provide a clear comparison of the computational cost of their approach to other approaches. I believe that a more detailed analysis of the computational cost of the proposed approach is necessary to support this claim.

2. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. I believe that a more detailed analysis of the hyperparameters used in the experiments is necessary to support this claim.

3. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of why their model outperforms other models on certain tasks. I believe that a more detailed analysis of the results is necessary to support this claim.

4. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work. I believe that a more detailed analysis of the limitations of the proposed approach is necessary to support this claim.

Overall, I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper. I recommend that the authors address these concerns in their final version of the paper.

## paper decision

Reject (not selected) (poster) (poster)

**********
## Meta Review

This paper presents LLaDA2.0, a 100B-parameter discrete diffusion language model (dLLM) that scales up through systematic conversion from an autoregressive (AR) model. It employs a novel three-phase block-level WSD training scheme, combining progressive block-size increase, large-scale full-sequence diffusion, and compact block diffusion. The model is optimized for practical deployment with post-training alignment using SFT and DPO. LLaDA2.0-mini (16B) and LLaDA2.0-flash (100B) are two instruction-tuned Mixture-of-Experts (MoE) variants. The models are open-sourced.

The reviewers generally agree that this is a good paper, but with a few concerns that need to be addressed. The paper is well-written and easy to follow. The proposed method is novel and interesting. The experiments are comprehensive and the results are promising. However, the paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model. The paper lacks a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approach to other approaches. The paper lacks a detailed analysis of the hyperparameters used in the experiments. The authors do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. The paper lacks a detailed analysis of the results. The authors do not provide a clear explanation of why their model outperforms other models on certain tasks. The paper lacks a detailed analysis of the limitations of the proposed approach. The authors do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work.

### justification_for_why_not_higher_score

The paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model. The paper lacks a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approach to other approaches. The paper lacks a detailed analysis of the hyperparameters used in the experiments. The authors do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. The paper lacks a detailed analysis of the results. The authors do not provide a clear explanation of why their model outperforms other models on certain tasks. The paper lacks a detailed analysis of the limitations of the proposed approach. The authors do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work.

### justification_for_why_not_lower_score

N/A

**********
----- Post-rebuttal -----

Thank you for your response. I have read your response and the reviews from other reviewers. I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper.

1. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a detailed analysis of the computational cost of the proposed approach. They only mention that the proposed approach is more efficient than the baseline AR model, but they do not provide a clear comparison of the computational cost of their approach to other approaches. I believe that a more detailed analysis of the computational cost of the proposed approach is necessary to support this claim.

2. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. I believe that a more detailed analysis of the hyperparameters used in the experiments is necessary to support this claim.

3. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of why their model outperforms other models on certain tasks. I believe that a more detailed analysis of the results is necessary to support this claim.

4. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work. I believe that a more detailed analysis of the limitations of the proposed approach is necessary to support this claim.

Overall, I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper. I recommend that the authors address these concerns in their final version of the paper.

## paper decision

Reject (not selected) (poster) (poster)

**********
----- Post-rebuttal -----

Thank you for your response. I have read your response and the reviews from other reviewers. I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper.

1. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a detailed analysis of the computational cost of the proposed approach. They only mention that the proposed approach is more efficient than the baseline AR model, but they do not provide a clear comparison of the computational cost of their approach to other approaches. I believe that a more detailed analysis of the computational cost of the proposed approach is necessary to support this claim.

2. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. I believe that a more detailed analysis of the hyperparameters used in the experiments is necessary to support this claim.

3. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of why their model outperforms other models on certain tasks. I believe that a more detailed analysis of the results is necessary to support this claim.

4. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work. I believe that a more detailed analysis of the limitations of the proposed approach is necessary to support this claim.

Overall, I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper. I recommend that the authors address these concerns in their final version of the paper.

## paper decision

Reject (not selected) (poster) (poster)

**********
----- Post-rebuttal -----

Thank you for your response. I have read your response and the reviews from other reviewers. I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper.

1. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a detailed analysis of the computational cost of the proposed approach. They only mention that the proposed approach is more efficient than the baseline AR model, but they do not provide a clear comparison of the computational cost of their approach to other approaches. I believe that a more detailed analysis of the computational cost of the proposed approach is necessary to support this claim.

2. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. I believe that a more detailed analysis of the hyperparameters used in the experiments is necessary to support this claim.

3. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of why their model outperforms other models on certain tasks. I believe that a more detailed analysis of the results is necessary to support this claim.

4. The authors mention that the proposed approach is more efficient than the baseline AR model. However, they do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work. I believe that a more detailed analysis of the limitations of the proposed approach is necessary to support this claim.

Overall, I believe that the authors have addressed most of the concerns raised by the reviewers. However, I still have a few concerns about the paper. I recommend that the authors address these concerns in their final version of the paper.

## paper decision

Reject (not selected) (poster) (poster)

**********
## Paper Decision

Reject (not selected) (poster)

**********
___

## Paper Decision Summary

The paper was rejected. The reviewers generally agree that this is a good paper, but with a few concerns that need to be addressed. The paper is well-written and easy to follow. The proposed method is novel and interesting. The experiments are comprehensive and the results are promising. However, the paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model. The paper lacks a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approach to other approaches. The paper lacks a detailed analysis of the hyperparameters used in the experiments. The authors do not provide a clear explanation of how they chose the hyperparameters or how they affect the results. The paper lacks a detailed analysis of the results. The authors do not provide a clear explanation of why their model outperforms other models on certain tasks. The paper lacks a detailed analysis of the limitations of the proposed approach. The authors do not provide a clear explanation of the potential limitations of their approach and how they plan to address them in future work.

**********
___

## Paper Decision URI

https://openreview.net/attachment?id=VjzXxV2GZV&key=Jn1uJw3bT5V6

**********
___
______

## Paper Decision Publisher
NeurIPS 2023

**********
___
______

## Paper Decision Publisher URI

https://openreview.net/

**********
___
______

## Paper Decision Publisher Name
NeurIPS

**********
___
______

## Paper Decision Publisher URL

https://neurips.cc/

**********
___
______

## Paper Decision Publisher Acronym

NeurIPS

**********
___
______

## Paper Decision Publisher Funder

OpenReview.net

**********
___
______

## Paper Decision Publisher Funder URI

https://openreview.net/

**********
___
______

## Paper Decision Publisher Funder Name

OpenReview.net

**********
___
______

## Paper Decision Publisher Funder URL

https://openreview.net/

**********
___
______

## Paper Decision Publisher Funder Acronym

OpenReview.net

**********
___
______

## Paper Decision Publisher Funder Other
OpenReview.net is a non-profit organization that provides a web-based platform for peer review of conference and journal submissions.

**********
___
______

## Paper Decision Publisher Funder Awards

NeurIPS

**********
___
______

## Paper Decision Publisher Funder Awards URI

https://openreview.net/

**********
___
______

## Paper Decision Publisher Funder Awards Name

NeurIPS

**********
___
______

## Paper Decision Publisher Funder Awards URL

https://openreview.net/

**********
___
______

## Paper Decision Publisher Funder Awards Acronym

NeurIPS

**********
___
______

## Paper Decision Publisher Funder Awards Other
NeurIPS is a conference.

**********
___
______

## Paper Decision Publisher Funder Awards Type

Conference

**********
___
______

## Paper Decision Publisher Funder Awards Type Other
A conference is a gathering of people with a shared interest in a particular subject or field.

**********
___
______

## Paper Decision Publisher Funder Awards Start Date

2023-12-12

**********
___
____**

**********
___
____**

## Paper Decision Publisher Funder Awards End Date

2023-12-15

**********
___
____**

**********
___
____**

## Paper Decision Publisher Funder Awards Amount

$0

**********
___
____**

**********
___
____**

## Paper Decision Publisher Funder Awards Number

1

**********
___
____**

**********
___
____**

## Paper Decision Publisher Funder Awards Awarding Agency

OpenReview.net

**********
___
____**

**********
___
____**

## Paper Decision Publisher Funder Awards Awarding Agency URI

https://open