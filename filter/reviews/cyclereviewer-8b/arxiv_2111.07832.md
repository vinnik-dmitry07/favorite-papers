## Reviewer

### Summary

This paper proposes a new pre-training framework for vision transformers based on masked image modeling (MIM) with a self-distillation objective. The authors argue that the key to the success of masked language modeling (MLM) is the use of a semantically meaningful tokenizer, and propose to use a similar approach for vision transformers. The proposed method, iBOT, uses a self-distillation objective to learn a tokenizer that can be jointly trained with the MIM objective. The authors show that iBOT achieves state-of-the-art results on various downstream tasks, including classification, object detection, and semantic segmentation.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The proposed method is simple and effective, and achieves state-of-the-art results on various downstream tasks.
2. The authors provide a thorough analysis of the proposed method, including an ablation study and visualization of the learned features.

### Weaknesses

1. The novelty of the proposed method is limited. The idea of using self-distillation for pre-training has been explored in previous works, such as DINO.
2. The paper lacks a clear motivation for the proposed method. The authors do not provide a clear explanation of why masked image modeling with a self-distillation objective is a good approach for pre-training vision transformers.
3. The paper does not provide a clear comparison with previous works. The authors do not provide a detailed comparison of their method with previous works, and do not discuss the advantages and disadvantages of their method compared to other approaches.

### Questions

1. How does the proposed method compare to other pre-training methods for vision transformers, such as BEiT and DINO?
2. Can the proposed method be applied to other pre-training tasks, such as image generation or image-to-image translation?
3. How does the proposed method scale to larger models and datasets?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a self-supervised framework iBOT that can perform masked prediction with an online tokenizer. Specifically, they perform self-distillation on masked patch tokens and take the teacher network as the online tokenizer, along with self-distillation on the class token to acquire visual semantics. The online tokenizer is jointly learnable with the MIM objective and dispenses with a multi-stage training pipeline where the tokenizer needs to be pre-trained beforehand. They show the prominence of iBOT by achieving an 82.3% linear probing accuracy and an 87.8% fine-tuning accuracy evaluated on ImageNet-1K. Beyond the state-of-the-art image classification results, they underline emerging local semantic patterns, which helps the models to obtain strong robustness against common corruptions and achieve leading results on dense downstream tasks, e.g., object detection, instance segmentation, and semantic segmentation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, which achieves state-of-the-art performance on various downstream tasks.
3. The authors provide a thorough analysis of the proposed method, including an ablation study and visualization of the learned features.

### Weaknesses

1. The novelty of the proposed method is limited. The idea of using self-distillation for pre-training has been explored in previous works, such as DINO.
2. The paper lacks a clear motivation for the proposed method. The authors do not provide a clear explanation of why masked image modeling with a self-distillation objective is a good approach for pre-training vision transformers.

### Questions

1. How does the proposed method compare to other pre-training methods for vision transformers, such as BEiT and DINO?
2. Can the proposed method be applied to other pre-training tasks, such as image generation or image-to-image translation?
3. How does the proposed method scale to larger models and datasets?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a self-supervised framework iBOT that can perform masked prediction with an online tokenizer. Specifically, they perform self-distillation on masked patch tokens and take the teacher network as the online tokenizer, along with self-distillation on the class token to acquire visual semantics. The online tokenizer is jointly learnable with the MIM objective and dispenses with a multi-stage training pipeline where the tokenizer needs to be pre-trained beforehand. They show the prominence of iBOT by achieving an 82.3% linear probing accuracy and an 87.8% fine-tuning accuracy evaluated on ImageNet-1K. Beyond the state-of-the-art image classification results, they underline emerging local semantic patterns, which helps the models to obtain strong robustness against common corruptions and achieve leading results on dense downstream tasks, e.g., object detection, instance segmentation, and semantic segmentation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The proposed method is simple and effective, which achieves state-of-the-art performance on various downstream tasks.

### Weaknesses

The novelty of the proposed method is limited. The idea of using self-distillation for pre-training has been explored in previous works, such as DINO.

### Questions

1. The authors claim that the online tokenizer is jointly learnable with the MIM objective and dispenses with a multi-stage training pipeline where the tokenizer needs to be pre-trained beforehand. However, the proposed method still needs to pre-train the tokenizer, which is the same as BEiT. Can the authors clarify this point?

2. The authors claim that the proposed method can perform masked prediction with an online tokenizer. However, the tokenizer is still pre-trained before the masked prediction. Can the authors clarify this point?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a self-supervised framework iBOT that performs masked image modeling via self-distillation with an online tokenizer. The online tokenizer is jointly learnable with the MIM objective and dispenses with a multi-stage training pipeline where the tokenizer needs to be pre-trained beforehand. The proposed method achieves state-of-the-art results on various downstream tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple and effective, which achieves state-of-the-art performance on various downstream tasks.
2. The authors provide a thorough analysis of the proposed method, including an ablation study and visualization of the learned features.

### Weaknesses

1. The novelty of the proposed method is limited. The idea of using self-distillation for pre-training has been explored in previous works, such as DINO.

### Questions

1. How does the proposed method compare to other pre-training methods for vision transformers, such as BEiT and DINO?
2. Can the proposed method be applied to other pre-training tasks, such as image generation or image-to-image translation?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a self-supervised framework iBOT that can perform masked prediction with an online tokenizer. Specifically, they perform self-distillation on masked patch tokens and take the teacher network as the online tokenizer, along with self-distillation on the class token to acquire visual semantics. The online tokenizer is jointly learnable with the MIM objective and dispenses with a multi-stage training pipeline where the tokenizer needs to be pre-trained beforehand. They show the prominence of iBOT by achieving an 82.3% linear probing accuracy and an 87.8% fine-tuning accuracy evaluated on ImageNet-1K. Beyond the state-of-the-art image classification results, they underline emerging local semantic patterns, which helps the models to obtain strong robustness against common corruptions and achieve leading results on dense downstream tasks, e.g., object detection, instance segmentation, and semantic segmentation.

The paper received four reviews with scores of 5, 5, 6, 6. The reviewers raised some concerns about the novelty of the proposed method and the motivation of the proposed method. The authors provided a rebuttal, but the reviewers did not change their scores. The AC checked the paper and the rebuttal, and decided to reject the paper.

### justification_for_why_not_higher_score

The novelty of the proposed method is limited. The idea of using self-distillation for pre-training has been explored in previous works, such as DINO.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not good enough) -> Not good enough for ICLR

**********

<!-- Added "not good enough for ICLR" to the end of the decision, as per the new ICLR policy. -->