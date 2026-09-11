# Review

## Summary
This paper proposes a new self-supervised learning method called VICReg, which adds two regularization terms to the loss function to prevent representation collapse. The two terms are variance term and covariance term. The variance term maintains the standard deviation of each variable of the embedding above a given threshold. The covariance term attracts the covariances between every pair of (centered) embedding variables towards zero. The proposed method is evaluated on several downstream tasks including image classification, object detection, instance segmentation, and image-text retrieval.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The proposed method is simple and easy to understand.
2. The proposed method does not require a memory bank, nor contrastive samples, nor a large batch size.

## Weaknesses
1. The proposed method is very similar to Barlow Twins, the difference is that the proposed method explicitly prevents collapse by adding two regularization terms to the loss function. However, the experimental results show that the proposed method is worse than Barlow Twins on some downstream tasks (Table 1 and Table 3).
2. The proposed method is not evaluated on the most important downstream task - image classification on the full ImageNet dataset.
3. The proposed method is not evaluated on object detection and instance segmentation on the COCO dataset.
4. The proposed method is not compared with recent self-supervised learning methods, e.g., SwAV, BYOL, and DINO.
5. The writing of the paper needs to be improved. For example, the first sentence of the abstract is not proper.

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4