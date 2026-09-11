## Reviewer

### Summary

This paper proposes Latent Consistency Models (LCMs) for fast, high-resolution image generation. LCMs employ consistency models in the image latent space, enabling fast few-step or even one-step high-fidelity sampling on pre-trained latent diffusion models (e.g., Stable Diffusion (SD)). The authors provide a simple and efficient one-stage guided consistency distillation method to distill SD for few-step (2 ~ 4) or even 1-step sampling. They also introduce a new fine-tuning method for LCMs, named Latent Consistency Fine-tuning, enabling efficient adaptation of a pre-trained LCM to customized datasets while preserving the ability of fast inference.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The idea of distilling the consistency model from pre-trained diffusion models is interesting and promising.
- The proposed method achieves SOTA performance on LAION-5B-Aesthetics dataset.

### Weaknesses

- The proposed method is a direct extension of the consistency model to latent space. The novelty is limited.
- The proposed method is not compared with the latest diffusion models, such as [1-3]. 
- The proposed method is not compared with the latest consistency models, such as [4, 5].
- The proposed method is only evaluated on LAION-5B-Aesthetics dataset. It is not clear how the proposed method performs on other datasets, such as FFHQ, CelebA-HQ, and COCO.
- The proposed method is not compared with other distillation methods, such as [6, 7].

[1] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." arXiv preprint arXiv:2205.02351 (2022).

[2] Saharia, Kfir, et al. "Imagen: Text-to-image generation and editing with diffusion models." arXiv preprint arXiv:2205.14148 (2022).

[3] Ramesh, Amit, et al. "Dall-e 2: Learning tips from language to image generation." arXiv preprint arXiv:2211.10802 (2022).

[4] Zhang, Yifan, et al. "Consistency models are diffusion models." arXiv preprint arXiv:2305.01991 (2023).

[5] Zhang, Yifan, et al. "Consistency models are diffusion models." arXiv preprint arXiv:2305.01991 (2023).

[6] Salimans, Tim, and Jonathan Ho. "Progressive distillation for fast sampling of diffusion models." arXiv preprint arXiv:2203.16859 (2022).

[7] Meng, Xiang, et al. "Guided distillation for fast sampling of diffusion models." arXiv preprint arXiv:2302.02658 (2023).

### Questions

Please refer to the weakness.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a method to distill a pre-trained diffusion model into a consistency model, which can be used for fast generation. The proposed method is based on the idea of latent space distillation, where the consistency model is distilled from a pre-trained diffusion model in the latent space, instead of the pixel space. The authors also propose a one-stage guided distillation method to distill a pre-trained guided diffusion model into a latent consistency model by solving an augmented PF-ODE. Furthermore, the authors propose Latent Consistency Fine-tuning, a novel method that is tailored for fine-tuning LCMs on customized image datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and effective. The proposed method is based on the idea of latent space distillation, which is a novel idea. The proposed method is effective in distilling a pre-trained diffusion model into a consistency model, which can be used for fast generation.

### Weaknesses

The paper lacks some ablation studies. For example, the paper does not provide any ablation studies on the effect of the number of steps in the distillation process. The paper does not provide any ablation studies on the effect of the number of iterations in the distillation process. The paper does not provide any ablation studies on the effect of the batch size in the distillation process. The paper does not provide any ablation studies on the effect of the learning rate in the distillation process.

### Questions

1. What is the effect of the number of steps in the distillation process? 
2. What is the effect of the number of iterations in the distillation process? 
3. What is the effect of the batch size in the distillation process? 
4. What is the effect of the learning rate in the distillation process?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes Latent Consistency Models (LCMs) for fast, high-resolution image generation. LCMs employ consistency models in the image latent space, enabling fast few-step or even one-step high-fidelity sampling on pre-trained latent diffusion models (e.g., Stable Diffusion (SD)). The authors provide a simple and efficient one-stage guided consistency distillation method to distill SD for few-step (2 ~ 4) or even 1-step sampling. They also introduce a new fine-tuning method for LCMs, named Latent Consistency Fine-tuning, enabling efficient adaptation of a pre-trained LCM to customized datasets while preserving the ability of fast inference.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The proposed method is simple and effective. 
2. The proposed method is based on the idea of latent space distillation, which is a novel idea. The proposed method is effective in distilling a pre-trained diffusion model into a consistency model, which can be used for fast generation.
3. The proposed method is effective in distilling a pre-trained diffusion model into a consistency model, which can be used for fast generation.

### Weaknesses

1. The proposed method is a direct extension of the consistency model to latent space. The novelty is limited.
2. The proposed method is not compared with the latest diffusion models, such as [1, 2, 3]. 
3. The proposed method is not compared with the latest consistency models, such as [4, 5].
4. The proposed method is only evaluated on LAION-5B-Aesthetics dataset. It is not clear how the proposed method performs on other datasets, such as FFHQ, CelebA-HQ, and COCO.
5. The proposed method is not compared with other distillation methods, such as [6, 7].

[1] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." arXiv preprint arXiv:2205.02351 (2022).

[2] Saharia, Kfir, et al. "Imagen: Text-to-image generation and editing with diffusion models." arXiv preprint arXiv:2205.14148 (2022).

[3] Ramesh, Amit, et al. "Dall-e 2: Learning tips from language to image generation." arXiv preprint arXiv:2211.10802 (2022).

[4] Zhang, Yifan, et al. "Consistency models are diffusion models." arXiv preprint arXiv:2305.01991 (2023).

[5] Zhang, Yifan, et al. "Consistency models are diffusion models." arXiv preprint arXiv:2305.01991 (2023).

[6] Salimans, Tim, and Jonathan Ho. "Progressive distillation for fast sampling of diffusion models." arXiv preprint arXiv:2203.16859 (2022).

[7] Meng, Xiang, et al. "Guided distillation for fast sampling of diffusion models." arXiv preprint arXiv:2302.02658 (2023).

### Questions

Please refer to the weakness.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes Latent Consistency Models (LCMs), which is a fast, high-resolution image generation method. LCMs employ consistency models in the image latent space, enabling fast few-step or even one-step high-fidelity sampling on pre-trained latent diffusion models (e.g., Stable Diffusion (SD)). The authors provide a simple and efficient one-stage guided consistency distillation method to distill SD for few-step (2 ~ 4) or even 1-step sampling. They also introduce a new fine-tuning method for LCMs, named Latent Consistency Fine-tuning, enabling efficient adaptation of a pre-trained LCM to customized datasets while preserving the ability of fast inference.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The proposed method is simple and effective.
2. The proposed method is effective in distilling a pre-trained diffusion model into a consistency model, which can be used for fast generation.
3. The proposed method is effective in distilling a pre-trained diffusion model into a consistency model, which can be used for fast generation.

### Weaknesses

1. The proposed method is a direct extension of the consistency model to latent space. The novelty is limited.
2. The proposed method is not compared with the latest diffusion models, such as [1, 2, 3]. 
3. The proposed method is not compared with the latest consistency models, such as [4, 5].
4. The proposed method is only evaluated on LAION-5B-Aesthetics dataset. It is not clear how the proposed method performs on other datasets, such as FFHQ, CelebA-HQ, and COCO.
5. The proposed method is not compared with other distillation methods, such as [6, 7].

[1] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." arXiv preprint arXiv:2205.02351 (2022).

[2] Saharia, Kfir, et al. "Imagen: Text-to-image generation and editing with diffusion models." arXiv preprint arXiv:2205.14148 (2022).

[3] Ramesh, Amit, et al. "Dall-e 2: Learning tips from language to image generation." arXiv preprint arXiv:2211.10802 (2022).

[4] Zhang, Yifan, et al. "Consistency models are diffusion models." arXiv preprint arXiv:2305.01991 (2023).

[5] Zhang, Yifan, et al. "Consistency models are diffusion models." arXiv preprint arXiv:2305.01991 (2023).

[6] Salimans, Tim, and Jonathan Ho. "Progressive distillation for fast sampling of diffusion models." arXiv preprint arXiv:2203.16859 (2022).

[7] Meng, Xiang, et al. "Guided distillation for fast sampling of diffusion models." arXiv preprint arXiv:2302.02658 (2023).

### Questions

Please refer to the weakness.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper proposes Latent Consistency Models (LCMs), which is a fast, high-resolution image generation method. LCMs employ consistency models in the image latent space, enabling fast few-step or even one-step high-fidelity sampling on pre-trained latent diffusion models (e.g., Stable Diffusion (SD)). The authors provide a simple and efficient one-stage guided consistency distillation method to distill SD for few-step (2 ~ 4) or even 1-step sampling. They also introduce a new fine-tuning method for LCMs, named Latent Consistency Fine-tuning, enabling efficient adaptation of a pre-trained LCM to customized datasets while preserving the ability of fast inference.

The paper is well-written and easy to follow. The proposed method is simple and effective. The proposed method is effective in distilling a pre-trained diffusion model into a consistency model, which can be used for fast generation. However, the proposed method is a direct extension of the consistency model to latent space. The novelty is limited. The proposed method is not compared with the latest diffusion models, such as [1, 2, 3]. The proposed method is not compared with the latest consistency models, such as [4, 5]. The proposed method is only evaluated on LAION-5B-Aesthetics dataset. It is not clear how the proposed method performs on other datasets, such as FFHQ, CelebA-HQ, and COCO. The proposed method is not compared with other distillation methods, such as [6, 7].

### justification_for_why_not_higher_score

The proposed method is a direct extension of the consistency model to latent space. The novelty is limited. The proposed method is not compared with the latest diffusion models, such as [1, 2, 3]. The proposed method is not compared with the latest consistency models, such as [4, 5]. The proposed method is only evaluated on LAION-5B-Aesthetics dataset. It is not clear how the proposed method performs on other datasets, such as FFHQ, CelebA-HQ, and COCO. The proposed method is not compared with other distillation methods, such as [6, 7].

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation. After the rebuttal, the authors did not address the concerns of the reviewers. The AC decided to reject the paper.

**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

<!---
Please follow the format: https://openreview.net/paper/kygYfuEpwv
--->
<!----


**********

## Paper Decision URI

https://openreview.net/pdf/1sC7Jd6tjw

**********

## Paper Decision Summary

The paper received two weak accept and two reject ratings. The reviewers raised some concerns about the novelty and the experimental evaluation