# Review

## Summary
This paper proposes a novel visual generation architecture, Elastic Looped Transformer (ELT), which is a recurrent transformer architecture. The proposed ELT shares the same parameters in each block and applies the same block iteratively to reduce the parameter count. To train the ELT, the authors propose Intra-Loop Self Distillation (ILSD) to distill the knowledge from the teacher configuration (maximum training loops) to the student configuration (intermediate loops). The proposed ELT achieves a competitive FID of 2.0 on class-conditional ImageNet 256 and FVD of 72.8 on class-conditional UCF-101.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed ELT is novel and interesting. The idea of Intra-Loop Self Distillation is also novel. The proposed method can be applied to both MaskGIT and DiT.
2. The paper is well-written and easy to follow.
3. The proposed method achieves a competitive FID of 2.0 on class-conditional ImageNet 256 and FVD of 72.8 on class-conditional UCF-101.

## Weaknesses
1. The authors claim that the proposed method can achieve a competitive FID of 2.0 on class-conditional ImageNet 256 and FVD of 72.8 on class-conditional UCF-101 with 4x fewer parameters. However, it is not clear which baseline method the comparison is made against. The authors should specify this more clearly in the paper.
2. The authors claim that the proposed method can achieve a competitive FID of 2.0 on class-conditional ImageNet 256 and FVD of 72.8 on class-conditional UCF-101 with 4x fewer parameters. However, it is not clear whether the baseline method with 4x fewer parameters can achieve a similar performance. The authors should provide more details on this comparison.
3. The authors should provide more details on the training cost of the proposed method. Specifically, how many GPUs are used, and how many hours per epoch does it take to train the model?

## Questions
1. The authors claim that the proposed method can achieve a competitive FID of 2.0 on class-conditional ImageNet 256 and FVD of 72.8 on class-conditional UCF-101 with 4x fewer parameters. However, it is not clear which baseline method the comparison is made against. The authors should specify this more clearly in the paper.
2. The authors claim that the proposed method can achieve a competitive FID of 2.0 on class-conditional ImageNet 256 and FVD of 72.8 on class-conditional UCF-101 with 4x fewer parameters. However, it is not clear whether the baseline method with 4x fewer parameters can achieve a similar performance. The authors should provide more details on this comparison.
3. The authors should provide more details on the training cost of the proposed method. Specifically, how many GPUs are used, and how many hours per epoch does it take to train the model?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4