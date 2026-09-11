# Review

## Summary
The paper proposes a new optimization method, Sharpness-Aware Minimization (SAM), to improve the generalization of deep neural networks. The proposed method is motivated by the loss landscape argument: SAM aims to find a flat minimum with lower loss value. The paper provides a practical algorithm to implement SAM and shows its effectiveness in various settings, including image classification, fine-tuning, and learning with noisy labels. The paper also introduces a new notion of sharpness, called m-sharpness, and shows its correlation with generalization.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. The motivation and the algorithm are clearly explained.
- The proposed method is novel and practical. The paper provides a theoretical justification for SAM and derives a computationally efficient algorithm.
- The empirical results are strong. SAM improves the generalization in various settings, including image classification, fine-tuning, and learning with noisy labels. The paper also shows that SAM can be combined with other techniques, such as data augmentation and dropout.

## Weaknesses
- The paper does not provide a theoretical guarantee that SAM will find a flat minimum or that a flat minimum is indeed good. It would be better to provide some theoretical justification for the proposed algorithm.
- The paper does not provide a comparison with other sharpness-aware optimization methods, such as the one proposed by [1]. It would be better to provide some discussion and empirical comparison with other related methods.
- The paper does not provide an analysis of the computational overhead of SAM. It would be better to report the training time and memory usage of SAM and compare them with other baselines.

[1] Foret, P., Kleiner, A., Mobahi, H., Neyshabur, B., and Srebro, N. Sharpness-aware minimization in the infinite width limit. In International Conference on Machine Learning, pages 3988–3999. PMLR, 2021.

## Questions
- How does SAM compare with other sharpness-aware optimization methods, such as the one proposed by [1]?
- What is the computational overhead of SAM? How does it compare with other baselines?
- How does SAM affect the training dynamics? Does it converge faster or slower than other methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4