# Review

## Summary
This paper proposes LASER, a method for improving the performance of LLMs by selectively reducing the rank of specific weight matrices in the model. The authors demonstrate that, by using SVD to reduce the rank of MLP layers in transformers, it is possible to improve the performance of LLMs on several tasks. The authors show that the performance improvements come from the model's ability to better handle information that is infrequently present in the training data. The authors also show that the higher-order components of the weight matrices encode high-frequency words or alternate answers, which can be removed to improve the model's performance.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and well-organized, with clear explanations of the proposed method and the experimental results.
2. The paper presents a novel method for improving the performance of LLMs by selectively reducing the rank of specific weight matrices.
3. The paper provides a thorough analysis of the proposed method, including experiments on several datasets and models, as well as a detailed discussion of the results.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a potential limitation for its practical application.
2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters, such as the rank reduction factor and the number of layers to intervene.
3. The paper does not provide a detailed analysis of the impact of the proposed method on the model's ability to generalize to new data, which is an important consideration for practical applications.

## Questions
1. How does the computational cost of the proposed method compare to other methods for improving the performance of LLMs, such as fine-tuning or transfer learning?
2. How sensitive is the proposed method to the choice of hyperparameters, such as the rank reduction factor and the number of layers to intervene? How did you choose these hyperparameters for your experiments?
3. How does the proposed method impact the model's ability to generalize to new data? Have you evaluated the proposed method on any out-of-distribution datasets?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4