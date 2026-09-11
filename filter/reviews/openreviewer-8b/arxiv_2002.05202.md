# Review

## Summary
This paper proposes to replace the feed-forward network (FFN) in the transformer architecture with different variants of gated linear units (GLU). The variants are obtained by replacing the sigmoid activation function in the first linear transformation with other activation functions such as ReLU, GELU and Swish. The models are trained on a text-to-text task and evaluated on several downstream tasks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well written and easy to follow.
- The authors perform experiments on several downstream tasks and report the standard deviations across multiple runs.

## Weaknesses
- The technical novelty is limited. The authors propose different variants of an architecture that has already been proposed in the past. The novelty seems to be only that they tried these variants in the context of transformers.
- The authors do not provide an explanation as to why some of the variants perform better than others. They only show the empirical results and attribute the success to "divine benevolence".

## Questions
- The authors mention that they use no dropout during pre-training as it produces better results. However, it is known that training without dropout can lead to overfitting. How do the authors explain that training without dropout produces better results in their case?
- The authors fix the hyper-parameters for all models and do not perform any hyper-parameter tuning. How do the authors explain that some of the variants perform better than others when no tuning was performed?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4