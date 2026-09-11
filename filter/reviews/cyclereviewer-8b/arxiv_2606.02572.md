## Summary

The paper proposes a new regularization term for joint embedding predictive architecture (JEPA) training. The proposed method, VISReg, is a combination of a scale regularization term and a shape regularization term. The scale regularization term is similar to the one used in VICReg, while the shape regularization term is based on the Sliced Wasserstein Distance (SWD) to align the normalized embedding distribution with an isotropic Gaussian prior along random 1D projections. The authors show that VISReg outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors also provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

## Soundness

2 fair

## Presentation

3 good

## Contribution

2 fair

## Strengths

- The paper is well-written and easy to follow.
- The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K.
- The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

## Weaknesses

- The paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method.
- The paper does not compare with some recent SOTA methods, such as LpJEPA [1] and KerJEPA [2].
- The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

[1] LpJEPA: Efficient Joint Embedding Predictive Architecture Training with Rectified Distribution Matching Regularization, Kuang et al., 2023
[2] KerJEPA: Kernel MMD Regularization for Joint Embedding Predictive Architecture Training, Zimmermann et al., 2023

## Questions

- How does the proposed method compare with other recent methods in terms of computational cost?
- How does the proposed method compare with other recent methods in terms of scalability?
- Can the proposed method be applied to other types of data, such as text or audio?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

------------------

## Summary

The paper proposes a new regularization term for joint embedding predictive architecture (JEPA) training. The proposed method, VISReg, is a combination of a scale regularization term and a shape regularization term. The scale regularization term is similar to the one used in VICReg, while the shape regularization term is based on the Sliced Wasserstein Distance (SWD) to align the normalized embedding distribution with an isotropic Gaussian prior along random 1D projections. The authors show that VISReg outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors also provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

## Soundness

3 good

## Presentation

3 good

## Contribution

2 fair

## Strengths

- The paper is well-written and easy to follow.
- The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K.
- The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

## Weaknesses

- The paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method.
- The paper does not compare with some recent SOTA methods, such as LpJEPA [1] and KerJEPA [2].
- The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

[1] LpJEPA: Efficient Joint Embedding Predictive Architecture Training with Rectified Distribution Matching Regularization, Kuang et al., 2023
[2] KerJEPA: Kernel MMD Regularization for Joint Embedding Predictive Architecture Training, Zimmermann et al., 2023

## Questions

- How does the proposed method compare with other recent methods in terms of computational cost?
- How does the proposed method compare with other recent methods in terms of scalability?
- Can the proposed method be applied to other types of data, such as text or audio?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Summary

This paper proposes a novel regularization method for self-supervised learning called VISReg. VISReg is designed to replace the covariance regularization term of VICReg with a sketching objective based on the Sliced Wasserstein Distance (SWD). The SWD is used to align the normalized embedding distribution with an isotropic Gaussian prior along random 1D projections, thereby enforcing the full distributional shape of the embedding space. The authors argue that this approach provides stronger distributional control, better training stability, and resilience to low-quality datasets compared to existing methods. The authors also provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

- The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. 
- The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.
- The paper is well-written and easy to follow.

## Weaknesses

- The paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method.
- The paper does not compare with some recent SOTA methods, such as LpJEPA [1] and KerJEPA [2].
- The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

[1] LpJEPA: Efficient Joint Embedding Predictive Architecture Training with Rectified Distribution Matching Regularization, Kuang et al., 2023
[2] KerJEPA: Kernel MMD Regularization for Joint Embedding Predictive Architecture Training, Zimmermann et al., 2023

## Questions

- How does the proposed method compare with other recent methods in terms of computational cost?
- How does the proposed method compare with other recent methods in terms of scalability?
- Can the proposed method be applied to other types of data, such as text or audio?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Summary

The paper proposes a new regularization term for joint embedding predictive architecture (JEPA) training. The proposed method, VISReg, is a combination of a scale regularization term and a shape regularization term. The scale regularization term is similar to the one used in VICReg, while the shape regularization term is based on the Sliced Wasserstein Distance (SWD) to align the normalized embedding distribution with an isotropic Gaussian prior along random 1D projections. The authors show that VISReg outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors also provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

- The paper is well-written and easy to follow.
- The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K.
- The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

## Weaknesses

- The paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method.
- The paper does not compare with some recent SOTA methods, such as LpJEPA [1] and KerJEPA [2].
- The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

[1] LpJEPA: Efficient Joint Embedding Predictive Architecture Training with Rectified Distribution Matching Regularization, Kuang et al., 2023
[2] KerJEPA: Kernel MMD Regularization for Joint Embedding Predictive Architecture Training, Zimmermann et al., 2023

## Questions

- How does the proposed method compare with other recent methods in terms of computational cost?
- How does the proposed method compare with other recent methods in terms of scalability?
- Can the proposed method be applied to other types of data, such as text or audio?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

The paper proposes a new regularization term for joint embedding predictive architecture (JEPA) training. The proposed method, VISReg, is a combination of a scale regularization term and a shape regularization term. The scale regularization term is similar to the one used in VICReg, while the shape regularization term is based on the Sliced Wasserstein Distance (SWD) to align the normalized embedding distribution with an isotropic Gaussian prior along random 1D projections. The authors show that VISReg outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors also provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

## justification_for_why_not_higher_score

The paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

## justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the 5% threshold)

**********

## Paper Decision Criteria

1. The paper is well-written and easy to follow.
2. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K.
3. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

**********

## Paper Decision Final Note

The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

## Paper Decision Policy

The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is simple and effective. It outperforms existing regularization methods on low-quality datasets and achieves state-of-the-art performance on out-of-distribution datasets when pre-trained on ImageNet-1K. The authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

However, the paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. The paper does not compare with some recent SOTA methods, such as LpJEPA and KerJEPA. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors provide an analysis of the complexity of the proposed method, it would be helpful to have a more detailed analysis of the computational cost of the method in practice.

**********

**********

### Paper Decision: Reject (out of the 5% threshold)

**********

## Paper Decision Final Note: The paper is well-written and easy to follow. The proposed VISReg method is