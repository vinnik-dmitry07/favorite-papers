## Reviewer

### Summary

This paper presents a new self-supervised learning method, which is called SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper proposes a novel method for self-supervised learning that learns visual features by contrasting cluster assignments. This approach is online, memory efficient, and can be trained with large and small batches.
- The paper proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions. This approach is simple and effective, and can be applied to many self-supervised methods.
- The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining.

### Weaknesses

- The proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach.
- The paper does not provide a thorough analysis of the proposed method. For example, it would be helpful to see how the method performs on different datasets and with different architectures. Additionally, it would be helpful to see how the method compares to other self-supervised learning methods, such as SimCLR and MoCo.
- The paper does not provide a clear explanation of the proposed method. For example, it is not clear how the cluster assignments are learned online, and how the multi-crop strategy is implemented.

### Questions

- What are the advantages of the proposed method compared to other self-supervised learning methods?
- How does the proposed method perform on different datasets and with different architectures?
- How does the proposed method compare to other self-supervised learning methods, such as SimCLR and MoCo?
- Can you provide a clear explanation of the proposed method?
- How is the cluster assignments learned online?
- How is the multi-crop strategy implemented?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes an online algorithm, SwAV, that takes advantage of contrastive methods without requiring to compute pairwise comparisons. The method simultaneously clusters the data while enforcing consistency between cluster assignments produced for different augmentations (or “views”) of the same image, instead of comparing features directly as in contrastive learning. The method can be trained with large and small batches and can scale to unlimited amounts of data. Compared to previous contrastive methods, the method is more memory efficient since it does not require a large memory bank or a special momentum network. The authors also propose a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The authors validate their findings by achieving 75.3% top-1 accuracy on ImageNet with ResNet-50, as well as surpassing supervised pretraining on all the considered transfer tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and easy to understand.
- The proposed method is able to achieve SOTA performance on ImageNet.
- The proposed method is able to scale to large datasets.

### Weaknesses

- The proposed method is a variant of DeepCluster [1], which is a clustering-based method. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.
- The proposed method is not compared with other clustering-based methods, such as SeLa [2] and DeepCluster [1]. It is unclear how the proposed method compares to these methods in terms of performance and efficiency.
- The proposed method is not compared with other contrastive methods, such as MoCo [3] and SimCLR [4]. It is unclear how the proposed method compares to these methods in terms of performance and efficiency.
- The proposed method is not compared with other self-supervised methods, such as BYOL [5] and DINO [6]. It is unclear how the proposed method compares to these methods in terms of performance and efficiency.

[1] Caron, Matias, et al. "Deep clustering for unsupervised learning of visual features." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2018.

[2] Asano, Yutaka, et al. "A simple framework for contrastive learning of visual representations." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2020.

[3] He, Kaiming, et al. "Momentum contrast for unsupervised visual representation learning." Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XIX 16. Springer International Publishing, 2020.

[4] Chen, Xinyu, et al. "A simple framework for contrastive learning of visual representations." Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XIX 16. Springer International Publishing, 2020.

[5] Bojanowski, Marc, et al. "Improved bootstrap your own latent (by moving deformer to image-space)." arXiv preprint arXiv:2104.13882 (2021).

[6] Caron, Matias, et al. "Emerging properties in self-supervised vision transformers." arXiv preprint arXiv:2104.14240 (2021).

### Questions

See Weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new self-supervised learning method, SwAV, which is an online algorithm that takes advantage of contrastive methods without requiring pairwise comparisons. SwAV simultaneously clusters the data while enforcing consistency between cluster assignments produced for different augmentations (or “views”) of the same image. The method can be trained with large and small batches and can scale to unlimited amounts of data. Compared to previous contrastive methods, the method is more memory efficient since it does not require a large memory bank or a special momentum network. The authors also propose a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The authors validate their findings by achieving 75.3% top-1 accuracy on ImageNet with ResNet-50, as well as surpassing supervised pretraining on all the considered transfer tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements.

### Weaknesses

The paper does not provide a thorough analysis of the proposed method. For example, it would be helpful to see how the method performs on different datasets and with different architectures. Additionally, it would be helpful to see how the method compares to other self-supervised learning methods, such as SimCLR and MoCo. The paper also does not provide a clear explanation of the proposed method. For example, it is not clear how the cluster assignments are learned online, and how the multi-crop strategy is implemented.

### Questions

1. The paper does not provide a thorough analysis of the proposed method. For example, it would be helpful to see how the method performs on different datasets and with different architectures. Additionally, it would be helpful to see how the method compares to other self-supervised learning methods, such as SimCLR and MoCo. 
2. The paper also does not provide a clear explanation of the proposed method. For example, it is not clear how the cluster assignments are learned online, and how the multi-crop strategy is implemented.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes an unsupervised learning method for visual features, which is based on contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The authors also propose a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The authors validate their findings by achieving 75.3% top-1 accuracy on ImageNet with ResNet-50, as well as surpassing supervised pretraining on all the considered transfer tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple and easy to understand.
2. The proposed method is able to achieve SOTA performance on ImageNet.
3. The proposed method is able to scale to large datasets.

### Weaknesses

1. The proposed method is not novel, as it is a variant of DeepCluster.
2. The paper does not provide a thorough analysis of the proposed method. For example, it would be helpful to see how the method performs on different datasets and with different architectures. Additionally, it would be helpful to see how the method compares to other self-supervised learning methods, such as SimCLR and MoCo.
3. The paper also does not provide a clear explanation of the proposed method. For example, it is not clear how the cluster assignments are learned online, and how the multi-crop strategy is implemented.

### Questions

1. The proposed method is not novel, as it is a variant of DeepCluster.
2. The paper does not provide a thorough analysis of the proposed method. For example, it would be helpful to see how the method performs on different datasets and with different architectures. Additionally, it would be helpful to see how the method compares to other self-supervised learning methods, such as SimCLR and MoCo.
3. The paper also does not provide a clear explanation of the proposed method. For example, it is not clear how the cluster assignments are learned online, and how the multi-crop strategy is implemented.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining.

The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements.

However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

### justification_for_why_not_higher_score

The proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

### justification_for_why_not_higher_score

The proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper proposes a new self-supervised learning method, SwAV, that learns visual features by contrasting cluster assignments. The proposed method is online, memory efficient, and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. The paper evaluates the method on ImageNet and several transfer tasks, showing that it outperforms previous contrastive methods and supervised pretraining. The paper is well-written and easy to follow. The proposed method is simple and effective, and the results show that it outperforms previous contrastive methods and supervised pretraining on ImageNet and several transfer tasks. The method is also scalable to large datasets and can be trained with large and small batches. The paper also proposes a new data augmentation strategy, multi-crop, that uses a mix of views with different resolutions in place of two full-resolution views, without increasing the memory or compute requirements. However, the proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. Therefore, I think the proposed method is not novel enough.

**********

## Paper Decision Final Feedback

Reject (not selected for publication)

**********

---

## Paper Decision Summary

The paper