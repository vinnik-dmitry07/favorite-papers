# Review

## Summary
This paper proposes a new on-policy distillation method that distills the teacher’s hidden states into the student’s hidden states. The authors also propose a variant that enables distillation between models with different architectures. The proposed method is evaluated on a math reasoning dataset and shows better performance than the baseline.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The idea of distilling hidden states is novel. The proposed method is well-motivated and supported by theoretical analysis.
2. The writing is clear and easy to follow.

## Weaknesses
1. The experiments are only conducted on a single math reasoning dataset, making it unclear whether the proposed method can generalize to other tasks.
2. The proposed method is only compared with OPD, making it unclear whether it can outperform other distillation methods such as off-policy distillation.

## Questions
1. Can the proposed method generalize to other tasks such as code generation?
2. Can the proposed method outperform other distillation methods such as off-policy distillation?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4