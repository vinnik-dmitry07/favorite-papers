# Review

## Summary
This paper studies why transformers fail to learn multi-digit multiplication. The authors reverse-engineer a model trained with implicit chain-of-thought (ICoT) and find that it has learned to compute the correct long-range dependencies needed for multi-digit multiplication. They also introduce an auxiliary loss that allows a standard fine-tuned model to learn multi-digit multiplication.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The authors provide a detailed analysis of the attention patterns and feature geometry of the ICoT model, revealing how it encodes long-range dependencies using attention trees and Fourier bases.
3. The authors provide a simple fix by introducing an auxiliary loss that allows a standard fine-tuned model to learn multi-digit multiplication.

## Weaknesses
1. The paper focuses on a specific task (multi-digit multiplication) and a specific model (a 2-layer 4-head transformer). It's unclear how well the findings generalize to other tasks and models.
2. The auxiliary loss introduced in Section 6 is task-specific and may not be applicable to other long-range dependency problems.

## Questions
1. The authors mention that scaling does not help for the standard fine-tuned model. Have you tried scaling the auxiliary loss for the fine-tuned model? Will that help?
2. Have you tried applying the auxiliary loss to other long-range dependency tasks beyond multiplication?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4