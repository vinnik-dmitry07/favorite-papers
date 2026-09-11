# Review

## Summary
This paper proposes a phenomenon called super-convergence which is an order of magnitude faster than typical neural network training. The key elements of super-convergence include training with one learning rate cycle and a large maximum learning rate. The authors also derive a simplification of the Hessian Free optimization method to compute an estimate of the optimal learning rate. Experiments demonstrate super-convergence for CIFAR-10/100, MNIST, and ImageNet datasets, and ResNet, Wide-ResNet, DenseNet, and Inception architectures.

## Soundness
2

## Presentation
1

## Contribution
2

## Strengths
The paper proposes a new phenomenon called super-convergence which can train neural networks much faster than typical training methods. The authors demonstrate the existence of super-convergence for several datasets and architectures, and show that it can provide a greater boost in performance when the amount of labeled training data is limited.

## Weaknesses
The paper is poorly written and hard to follow. The authors should improve the organization and clarity of the paper. The figures are also not well-organized and hard to understand. The authors should improve the presentation of the figures. The paper lacks a comparison with other state-of-the-art methods. The authors should compare their method with other fast training methods to demonstrate its superiority. The paper lacks an ablation study. The authors should conduct an ablation study to analyze the impact of different components of their method.

## Questions
1. The paper is poorly written and hard to follow. The authors should improve the organization and clarity of the paper.
2. The figures are not well-organized and hard to understand. The authors should improve the presentation of the figures.
3. The paper lacks a comparison with other state-of-the-art methods. The authors should compare their method with other fast training methods to demonstrate its superiority.
4. The paper lacks an ablation study. The authors should conduct an ablation study to analyze the impact of different components of their method.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4