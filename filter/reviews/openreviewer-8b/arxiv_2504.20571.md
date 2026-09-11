# Review

## Summary
The paper investigates the use of reinforcement learning with verifiable reward using one training example (1-shot RLVR) to enhance the mathematical reasoning capabilities of large language models (LLMs). The authors demonstrate that using a single well-chosen example can significantly improve model performance, achieving results comparable to using a larger dataset. The study identifies a specific example that improves the Qwen2.5-Math-1.5B model's performance on MATH500 from 36.0% to 73.6%, and increases average performance across six mathematical reasoning benchmarks from 17.6% to 35.7%. The paper also discusses the role of data selection, the effectiveness of policy gradient loss, and the importance of promoting exploration in 1-shot RLVR training. The findings suggest that a single example is sufficient to substantially enhance the base model's mathematical performance, and that 1-shot RLVR can improve performance on non-mathematical reasoning tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel approach, 1-shot RLVR, which uses a single example to improve the mathematical reasoning capabilities of LLMs.
2. The study provides empirical evidence that a single example can significantly enhance model performance, achieving results comparable to using a larger dataset.
3. The paper identifies a specific example that improves the Qwen2.5-Math-1.5B model's performance on MATH500 from 36.0% to 73.6%, and increases average performance across six mathematical reasoning benchmarks from 17.6% to 35.7%.
4. The paper discusses the role of data selection, the effectiveness of policy gradient loss, and the importance of promoting exploration in 1-shot RLVR training.
5. The findings suggest that a single example is sufficient to substantially enhance the base model's mathematical performance, and that 1-shot RLVR can improve performance on non-mathematical reasoning tasks.

## Weaknesses
1. The paper does not provide a detailed analysis of the characteristics of the single example used for 1-shot RLVR. It would be beneficial to understand the properties of the example that make it effective in improving model performance.
2. The paper does not discuss the potential for overfitting when using a single example for RLVR. It would be helpful to investigate the model's performance when trained with multiple examples and compare it to the performance with a single example.
3. The paper does not provide a comparison of the computational cost of using 1-shot RLVR compared to using a larger dataset. It would be useful to understand the trade-offs between the two approaches in terms of computational resources.

## Questions
1. What are the characteristics of the single example used for 1-shot RLVR? What properties does it have that make it effective in improving model performance?
2. How does the model perform when trained with multiple examples compared to using a single example for RLVR? Is there a risk of overfitting when using a single example?
3. What is the computational cost of using 1-shot RLVR compared to using a larger dataset? Are there any trade-offs between the two approaches in terms of computational resources?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4