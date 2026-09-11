## Reviewer

### Summary

This paper proposes a new approach to visual generation using recurrent transformers called Elastic Looped Transformers (ELT). The authors introduce Intra-Loop Self Distillation (ILSD), which trains a single model to be performant across a variable number of iterations. This allows for Any-Time inference, where the practitioner can dynamically balance image quality and computational cost. The paper shows that ELT achieves strong empirical performance with fewer parameters and identifies fundamental scaling properties of looped transformers.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and has the potential to improve the efficiency of visual generation models.
3. The paper provides extensive experiments on both image and video generation tasks.

### Weaknesses

1. The novelty of this paper is limited. The idea of using a recurrent transformer architecture for visual generation is not new. The proposed method is a combination of existing techniques, such as looping and distillation.
2. The experiments are not convincing. The authors only compare their method with MaskGIT and MAGVIT, which are not the state-of-the-art methods in visual generation. The authors should compare their method with more recent and stronger baselines.
3. The paper lacks an ablation study on the proposed ILSD method. It is unclear how important ILSD is for the performance of ELT. The authors should provide more ablation studies to demonstrate the effectiveness of ILSD.

### Questions

1. How does the proposed method compare with other state-of-the-art visual generation methods, such as [1] and [2]?
2. Can the proposed method be applied to other types of generative models, such as diffusion models?
3. How does the proposed method scale to larger datasets, such as ImageNet-21k?

[1] Zhang, Haoran, et al. "A style-based diffusion model for generative image synthesis." arXiv preprint arXiv:2106.10842 (2021).

[2] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new approach to visual generation using recurrent transformers called Elastic Looped Transformers (ELT). The authors introduce Intra-Loop Self Distillation (ILSD), which trains a single model to be performant across a variable number of iterations. This allows for Any-Time inference, where the practitioner can dynamically balance image quality and computational cost. The paper shows that ELT achieves strong empirical performance with fewer parameters and identifies fundamental scaling properties of looped transformers.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and has the potential to improve the efficiency of visual generation models.
3. The paper provides extensive experiments on both image and video generation tasks.

### Weaknesses

1. The novelty of this paper is limited. The idea of using a recurrent transformer architecture for visual generation is not new. The proposed method is a combination of existing techniques, such as looping and distillation.
2. The experiments are not convincing. The authors only compare their method with MaskGIT and MAGVIT, which are not the state-of-the-art methods in visual generation. The authors should compare their method with more recent and stronger baselines.
3. The paper lacks an ablation study on the proposed ILSD method. It is unclear how important ILSD is for the performance of ELT. The authors should provide more ablation studies to demonstrate the effectiveness of ILSD.

### Questions

1. How does the proposed method compare with other state-of-the-art visual generation methods, such as [1] and [2]?
2. Can the proposed method be applied to other types of generative models, such as diffusion models?
3. How does the proposed method scale to larger datasets, such as ImageNet-21k?

[1] Zhang, Haoran, et al. "A style-based diffusion model for generative image synthesis." arXiv preprint arXiv:2106.10842 (2021).

[2] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces a novel approach to visual generation using a recurrent transformer architecture, called Elastic Looped Transformers (ELT). This approach employs iterative, weight-shared transformer blocks to reduce parameter counts while maintaining high synthesis quality. The authors propose Intra-Loop Self Distillation (ILSD), which trains a single model to be performant across a variable number of iterations. This allows for Any-Time inference, where the practitioner can dynamically balance image quality and computational cost. The paper shows that ELT achieves strong empirical performance with fewer parameters and identifies fundamental scaling properties of looped transformers.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper introduces a novel approach to visual generation using a recurrent transformer architecture, called Elastic Looped Transformers (ELT). This approach employs iterative, weight-shared transformer blocks to reduce parameter counts while maintaining high synthesis quality.
2. The authors propose Intra-Loop Self Distillation (ILSD), which trains a single model to be performant across a variable number of iterations. This allows for Any-Time inference, where the practitioner can dynamically balance image quality and computational cost.
3. The paper shows that ELT achieves strong empirical performance with fewer parameters and identifies fundamental scaling properties of looped transformers.

### Weaknesses

1. The paper lacks an ablation study on the proposed ILSD method. It is unclear how important ILSD is for the performance of ELT. The authors should provide more ablation studies to demonstrate the effectiveness of ILSD.
2. The paper does not provide a clear explanation of how the proposed method compares to other state-of-the-art visual generation methods, such as diffusion models.
3. The paper does not provide a clear explanation of how the proposed method scales to larger datasets, such as ImageNet-21k.

### Questions

1. How does the proposed method compare with other state-of-the-art visual generation methods, such as diffusion models?
2. Can the proposed method be applied to other types of generative models, such as diffusion models?
3. How does the proposed method scale to larger datasets, such as ImageNet-21k?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a novel approach to visual generation using a recurrent transformer architecture, called Elastic Looped Transformers (ELT). This approach employs iterative, weight-shared transformer blocks to reduce parameter counts while maintaining high synthesis quality. The authors propose Intra-Loop Self Distillation (ILSD), which trains a single model to be performant across a variable number of iterations. This allows for Any-Time inference, where the practitioner can dynamically balance image quality and computational cost. The paper shows that ELT achieves strong empirical performance with fewer parameters and identifies fundamental scaling properties of looped transformers.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and has the potential to improve the efficiency of visual generation models.
3. The paper provides extensive experiments on both image and video generation tasks.

### Weaknesses

1. The novelty of this paper is limited. The idea of using a recurrent transformer architecture for visual generation is not new. The proposed method is a combination of existing techniques, such as looping and distillation.
2. The experiments are not convincing. The authors only compare their method with MaskGIT and MAGVIT, which are not the state-of-the-art methods in visual generation. The authors should compare their method with more recent and stronger baselines.
3. The paper lacks an ablation study on the proposed ILSD method. It is unclear how important ILSD is for the performance of ELT. The authors should provide more ablation studies to demonstrate the effectiveness of ILSD.

### Questions

1. How does the proposed method compare with other state-of-the-art visual generation methods, such as [1] and [2]?
2. Can the proposed method be applied to other types of generative models, such as diffusion models?
3. How does the proposed method scale to larger datasets, such as ImageNet-21k?

[1] Zhang, Haoran, et al. "A style-based diffusion model for generative image synthesis." arXiv preprint arXiv:2106.10842 (2021).

[2] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper proposes a novel approach to visual generation using a recurrent transformer architecture, called Elastic Looped Transformers (ELT). This approach employs iterative, weight-shared transformer blocks to reduce parameter counts while maintaining high synthesis quality. The authors propose Intra-Loop Self Distillation (ILSD), which trains a single model to be performant across a variable number of iterations. This allows for Any-Time inference, where the practitioner can dynamically balance image quality and computational cost. The paper shows that ELT achieves strong empirical performance with fewer parameters and identifies fundamental scaling properties of looped transformers.

The reviewers generally agree that the paper is well-written and easy to follow, and the proposed method is novel and has the potential to improve the efficiency of visual generation models. However, the novelty of this paper is limited. The idea of using a recurrent transformer architecture for visual generation is not new. The proposed method is a combination of existing techniques, such as looping and distillation. The experiments are not convincing. The authors only compare their method with MaskGIT and MAGVIT, which are not the state-of-the-art methods in visual generation. The authors should compare their method with more recent and stronger baselines. The paper lacks an ablation study on the proposed ILSD method. It is unclear how important ILSD is for the performance of ELT. The authors should provide more ablation studies to demonstrate the effectiveness of ILSD.

### justification_for_why_not_higher_score

The novelty of this paper is limited. The idea of using a recurrent transformer architecture for visual generation is not new. The proposed method is a combination of existing techniques, such as looping and distillation. The experiments are not convincing. The authors only compare their method with MaskGIT and MAGVIT, which are not the state-of-the-art methods in visual generation. The authors should compare their method with more recent and stronger baselines. The paper lacks an ablation study on the proposed ILSD method. It is unclear how important ILSD is for the performance of ELT. The authors should provide more ablation studies to demonstrate the effectiveness of ILSD.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the 7 papers selected for discussion, 5 reviewers gave scores of 5 or lower, and 2 gave scores of 3)

**********

## Paper Decision

Reject (out of the 7 papers selected for discussion, 5 reviewers gave scores of 5 or lower, and 2 gave scores of 3)

**********

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!-- Added by arXiv -->
<!---->

<!--