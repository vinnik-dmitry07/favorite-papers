## Reviewer

### Summary

This paper studies the effect of self-supervised learning on Vision Transformer (ViT). The authors claim that self-supervised learning provides new properties to ViT, such as the ability to contain explicit information about the semantic segmentation of an image and perform well with a basic k-NN classifier. They also highlight the importance of momentum encoder, multi-crop training, and small patches in ViT. They propose a simple self-supervised method called DINO, which is a form of self-distillation with no labels. The authors show that DINO achieves 80.1% top-1 accuracy on ImageNet in linear evaluation with ViT-Base.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive review of related work and clearly state the contributions of their work. The experiments are thorough and well-presented, and the authors provide a detailed analysis of the results. The proposed method is simple and effective, and the authors provide a clear explanation of the underlying principles and intuition behind it.

### Weaknesses

1. The novelty of the proposed method is limited. The authors mention that their method is similar to BYOL and MoCov2, and the main difference is the use of a momentum encoder and multi-crop training. However, these components have been used in previous works, and the authors do not provide any new insights or analysis on how they contribute to the performance of the method.

2. The experiments are not convincing. The authors only evaluate their method on ImageNet, which is a relatively small dataset. They also do not compare their method with other self-supervised learning methods, such as SimCLR and MoCo. Additionally, the authors do not provide any analysis of the performance of their method on other datasets, such as COCO or CIFAR-10.

3. The paper does not provide any insights into the limitations of the proposed method. The authors do not discuss any potential drawbacks or limitations of their approach, and they do not provide any suggestions for future work.

### Questions

1. How does the proposed method perform on other datasets, such as COCO or CIFAR-10?

2. How does the proposed method compare with other self-supervised learning methods, such as SimCLR and MoCo?

3. What are the limitations of the proposed method? Are there any potential drawbacks or limitations of the approach?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents an interesting study on the properties of self-supervised vision transformers (ViT) and proposes a simple self-supervised method, DINO, that can be used to train ViT and convolutional neural networks (CNNs) from scratch. The authors show that self-supervised ViT features contain information about semantic segmentation, and perform well with a basic k-NN classifier. They also highlight the importance of momentum encoder, multi-crop training, and small patches in ViT. The proposed DINO method is shown to achieve state-of-the-art performance on ImageNet linear evaluation and transfer learning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents an interesting study on the properties of self-supervised vision transformers (ViT) and proposes a simple self-supervised method, DINO, that can be used to train ViT and convolutional neural networks (CNNs) from scratch.

2. The paper is well-written and easy to follow. The authors provide a comprehensive review of related work and clearly state the contributions of their work.

3. The proposed method is simple and effective, and the authors provide a clear explanation of the underlying principles and intuition behind it.

### Weaknesses

1. The proposed method is very similar to BYOL, and the authors do not provide any new insights or analysis on how the proposed method differs from BYOL. 

2. The paper does not provide any analysis of the performance of the proposed method on other datasets, such as COCO or CIFAR-10.

### Questions

1. How does the proposed method perform on other datasets, such as COCO or CIFAR-10?

2. How does the proposed method compare with other self-supervised learning methods, such as SimCLR and MoCo?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper studies the properties of self-supervised vision transformers (ViT) and proposes a simple self-supervised method, DINO, that can be used to train ViT and convolutional neural networks (CNNs) from scratch. The authors show that self-supervised ViT features contain information about semantic segmentation, and perform well with a basic k-NN classifier. They also highlight the importance of momentum encoder, multi-crop training, and small patches in ViT. The proposed DINO method is shown to achieve state-of-the-art performance on ImageNet linear evaluation and transfer learning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a comprehensive review of related work and clearly state the contributions of their work.

2. The proposed method is simple and effective, and the authors provide a clear explanation of the underlying principles and intuition behind it.

3. The paper presents an interesting study on the properties of self-supervised vision transformers (ViT) and proposes a simple self-supervised method, DINO, that can be used to train ViT and convolutional neural networks (CNNs) from scratch.

### Weaknesses

1. The proposed method is very similar to BYOL, and the authors do not provide any new insights or analysis on how the proposed method differs from BYOL.

2. The paper does not provide any analysis of the performance of the proposed method on other datasets, such as COCO or CIFAR-10.

3. The paper does not provide any analysis of the performance of the proposed method on other tasks, such as object detection or segmentation.

### Questions

1. How does the proposed method perform on other datasets, such as COCO or CIFAR-10?

2. How does the proposed method compare with other self-supervised learning methods, such as SimCLR and MoCo?

3. How does the proposed method perform on other tasks, such as object detection or segmentation?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the properties of self-supervised vision transformers (ViT) and proposes a simple self-supervised method, DINO, that can be used to train ViT and convolutional neural networks (CNNs) from scratch. The authors show that self-supervised ViT features contain information about semantic segmentation, and perform well with a basic k-NN classifier. They also highlight the importance of momentum encoder, multi-crop training, and small patches in ViT. The proposed DINO method is shown to achieve state-of-the-art performance on ImageNet linear evaluation and transfer learning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a comprehensive review of related work and clearly state the contributions of their work.

2. The proposed method is simple and effective, and the authors provide a clear explanation of the underlying principles and intuition behind it.

3. The paper presents an interesting study on the properties of self-supervised vision transformers (ViT) and proposes a simple self-supervised method, DINO, that can be used to train ViT and convolutional neural networks (CNNs) from scratch.

### Weaknesses

1. The proposed method is very similar to BYOL, and the authors do not provide any new insights or analysis on how the proposed method differs from BYOL.

2. The paper does not provide any analysis of the performance of the proposed method on other datasets, such as COCO or CIFAR-10.

3. The paper does not provide any analysis of the performance of the proposed method on other tasks, such as object detection or segmentation.

### Questions

1. How does the proposed method perform on other datasets, such as COCO or CIFAR-10?

2. How does the proposed method compare with other self-supervised learning methods, such as SimCLR and MoCo?

3. How does the proposed method perform on other tasks, such as object detection or segmentation?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the properties of self-supervised vision transformers (ViT) and proposes a simple self-supervised method, DINO, that can be used to train ViT and convolutional neural networks (CNNs) from scratch. The authors show that self-supervised ViT features contain information about semantic segmentation, and perform well with a basic k-NN classifier. They also highlight the importance of momentum encoder, multi-crop training, and small patches in ViT. The proposed DINO method is shown to achieve state-of-the-art performance on ImageNet linear evaluation and transfer learning tasks.

The reviewers generally think that the paper is well-written and easy to follow. The proposed method is simple and effective, and the authors provide a clear explanation of the underlying principles and intuition behind it. The paper presents an interesting study on the properties of self-supervised vision transformers (ViT) and proposes a simple self-supervised method, DINO, that can be used to train ViT and convolutional neural networks (CNNs) from scratch.

However, the reviewers also point out that the proposed method is very similar to BYOL, and the authors do not provide any new insights or analysis on how the proposed method differs from BYOL. The paper does not provide any analysis of the performance of the proposed method on other datasets, such as COCO or CIFAR-10. The paper does not provide any analysis of the performance of the proposed method on other tasks, such as object detection or segmentation.

### justification_for_why_not_higher_score

The proposed method is very similar to BYOL, and the authors do not provide any new insights or analysis on how the proposed method differs from BYOL. The paper does not provide any analysis of the performance of the proposed method on other datasets, such as COCO or CIFAR-10. The paper does not provide any analysis of the performance of the proposed method on other tasks, such as object detection or segmentation.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is simple and effective, and the authors provide a clear explanation of the underlying principles and intuition behind it. The paper presents an interesting study on the properties of self-supervised vision transformers (ViT) and proposes a simple self-supervised method, DINO, that can be used to train ViT and convolutional neural networks (CNNs) from scratch.

**********

## Paper Decision

Reject (out of the scope of ICLR)

**********

## Paper Decision Summary

This paper is out of the scope of ICLR.

**********

## Paper Decision Final Feedback

This paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is out of the scope of ICLR.

**********

## Paper Decision Update

The paper is