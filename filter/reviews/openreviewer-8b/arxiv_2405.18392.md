# Review

## Summary
The paper explores alternatives to the cosine learning rate schedule for training large language models (LLMs). The authors argue that the cosine schedule, while widely used, has limitations, particularly in the need to pre-determine the training duration to match the cycle length, which can restrict flexibility and lead to suboptimal performance. The authors propose an alternative schedule of constant learning rate with cooldown as a more flexible alternative. This approach allows models to be evaluated at any point during training, making it easier to perform continual learning and scaling studies without retraining from scratch. The authors also investigate stochastic weight averaging and schedule-free optimizers as potential alternatives to learning rate schedules. They demonstrate that these methods can provide strong performance at any point during training, but may not match the optimal performance of the cosine schedule or constant + cooldown. The paper provides experimental results across various model sizes and training durations, showing that the proposed methods can match or outperform the cosine schedule in terms of validation loss and downstream performance. The authors highlight the computational savings of their approach, which can reduce the need for multiple full training runs when studying scaling laws.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a simple but effective alternative to the cosine learning rate schedule, which is widely used in training LLMs. The proposed constant + cooldown schedule provides more flexibility, allowing models to be evaluated at any point during training and facilitating continual learning without retraining from scratch. This approach can potentially simplify the training process and reduce computational costs.

2. The paper provides extensive experimental results across various model sizes and training durations. The authors demonstrate that the proposed methods can match or outperform the cosine schedule in terms of validation loss and downstream performance. This thorough evaluation helps establish the efficacy of the proposed approach.

3. The paper highlights the computational savings of the proposed approach, which can reduce the need for multiple full training runs when studying scaling laws. This is particularly relevant for researchers with limited computational resources, as it can enable more frequent computation of scaling laws for data mixtures or novel architectures.

## Weaknesses
1. The paper does not provide a comprehensive theoretical analysis of the proposed learning rate schedule or its advantages. While the experimental results are promising, a deeper understanding of why this schedule works well would strengthen the paper.

2. The experiments are conducted on a specific subset of tasks and datasets. It is unclear how well the proposed methods would generalize to other tasks or datasets. Additional experiments in diverse settings would help establish the robustness of the approach.

3. The paper does not extensively compare the proposed methods with other recent advancements in learning rate scheduling. While it discusses some related work, a more thorough comparison with alternative approaches would provide a clearer picture of the advantages and limitations of the proposed methods.

## Questions
1. Can you provide more theoretical insights into why the constant + cooldown learning rate schedule works well? Are there any theoretical guarantees or analysis that support its performance?

2. How well do the proposed methods generalize to other tasks or datasets beyond those used in the experiments? Have you tested them on different types of problems to assess their robustness?

3. How does the proposed approach compare with other recent advancements in learning rate scheduling? Can you provide a more detailed comparison with alternative methods to highlight the advantages and limitations of your approach?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4