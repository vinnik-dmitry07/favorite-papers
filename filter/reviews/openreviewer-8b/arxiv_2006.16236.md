# Review

## Summary
This paper proposes a linear attention mechanism that achieves linear complexity by using a kernel-based formulation of self-attention. The proposed method is up to 4000x faster on autoregressive prediction of very long sequences while achieving similar performance to vanilla transformers.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experiments are convincing.

## Weaknesses
1. The idea of linear attention is not new. It has been explored in previous works such as [1, 2, 3]. The authors should discuss these works in the paper.
2. The proposed method is not as good as the baselines on some tasks. For example, in the speech recognition task, although the proposed method is much faster than the baselines, it achieves a much higher WER (word error rate) than the vanilla transformer. 

[1] Linear Complexity Randomized Self-attention Mechanism for Long-Range Sequence Modeling. 2021.
[2] Fast Transformers with Clustered Attention. 2020.
[3] Nystromformer: A Nyström-Based Algorithm for Approximating Self-Attention. 2020.

## Questions
1. Can the proposed method be applied to bidirectional tasks such as language modeling?
2. How does the proposed method perform on machine translation tasks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4