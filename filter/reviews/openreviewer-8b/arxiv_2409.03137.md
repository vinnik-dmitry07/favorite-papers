# Review

## Summary
The paper introduces AdEMAMix, a new optimizer that improves upon Adam by incorporating a mixture of two Exponential Moving Averages (EMAs) to better utilize past gradients. Traditional optimizers like Adam use a single EMA to smooth out gradients, assuming that recent gradients are more relevant. However, the authors argue that this approach is sub-optimal because it cannot simultaneously emphasize both recent and older gradients. AdEMAMix addresses this by introducing a second EMA with a larger decay rate, allowing the model to leverage older gradients without sacrificing the benefits of recent gradient information. This approach aims to improve convergence speed and stability, particularly in training large models like language models and vision transformers.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide a clear motivation for their work and effectively communicate their ideas.

2. The paper introduces a novel approach to improving the Adam optimizer by incorporating a mixture of two Exponential Moving Averages (EMAs) to better leverage past gradients. This is a unique contribution to the field and addresses a potential limitation in traditional optimization methods.

3. The authors conduct extensive experiments on language models and vision transformers, demonstrating the effectiveness of AdEMAMix. The results show that AdEMAMix can outperform Adam in terms of convergence speed and accuracy, which is a strong empirical contribution.

## Weaknesses
1. The paper introduces several new hyperparameters, such as $\beta_3$ and $\alpha$, which require careful tuning. This adds complexity to the already complex process of hyperparameter optimization in machine learning.

2. While the paper shows that AdEMAMix outperforms Adam, it would be beneficial to see how it compares to other state-of-the-art optimizers. This would provide a more comprehensive understanding of its relative performance.

3. The paper does not provide a theoretical analysis of AdEMAMix. Developing a theoretical framework to explain the observed empirical results would strengthen the paper's contributions and provide insights into why the proposed method works.

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4