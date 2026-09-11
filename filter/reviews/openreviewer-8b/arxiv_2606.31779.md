# Review

## Summary
This paper proposes a new method for training a language model to perform latent chain-of-thought (CoT) reasoning. The method, called LOTUS, uses a looped padded Transformer architecture to encode the CoT steps in parallel and a cross-entropy loss to align the latent representations with the ground truth CoT steps. The authors demonstrate that LOTUS can match the performance of explicit CoT at the 3B parameter scale and reduce the latency of the reasoning phase by 2.5-6.9 times. The paper also includes an analysis of the learned latent representations, showing that they are interpretable and aligned with the ground truth CoT steps.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the proposed method, including ablation studies and an analysis of the learned latent representations.
3. The proposed method, LOTUS, shows promising results in terms of both accuracy and latency.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational requirements of the proposed method, such as the number of training steps and the resources needed for training.
2. The proposed method is only evaluated on math reasoning tasks, and it is unclear how well it would perform on other types of tasks that require CoT reasoning.
3. The paper does not provide a detailed comparison with other methods that use looped Transformers, such as LPTs.

## Questions
1. How does the computational cost of LOTUS compare to other methods that use explicit CoT, such as the cost of encoding and decoding the CoT tokens?
2. How well does LOTUS perform on other types of tasks that require CoT reasoning, such as logical reasoning or commonsense reasoning?
3. How does LOTUS compare to other methods that use looped Transformers, such as LPTs? For example, how does the performance of LOTUS compare to LPTs on the same tasks and datasets?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4