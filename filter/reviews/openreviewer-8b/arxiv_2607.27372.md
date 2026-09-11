# Review

## Summary
This paper proposes a new paradigm of training generative models, called Explorative Modeling (XM). Instead of factoring the generation process, XM factors the training loop, exploring K candidate matches between model generations and data, and training on the best. The authors demonstrate that this method can be combined with existing generative models and significantly improve their performance. Additionally, XM enables end-to-end training for reconstructive generative modeling.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experiments are comprehensive and demonstrate the effectiveness of the proposed method.

## Weaknesses
1. The proposed method is only applicable to continuous data, which limits its application.
2. The authors claim that exploration is a new pretraining axis, but it is similar to the number of training iterations in the sense that both affect the model's capacity to fit the training data. A larger number of training iterations can also lead to better model performance, so it is unsurprising that exploration would improve performance.
3. The authors claim that exploration can be used for end-to-end training, but only diffusion and flow models were demonstrated. I am curious about whether exploration can be applied to other end-to-end generative models, such as autoregressive models.

## Questions
1. How does the performance of the proposed method compare to the original generative models without exploration when the number of training iterations is the same?
2. Can the proposed method be applied to other end-to-end generative models, such as autoregressive models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4