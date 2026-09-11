# Review

## Summary
This paper proposes a new architecture for language models that can scale test-time computation by reasoning in latent space through recurrent iterations. The model iteratively processes hidden states and embedded input data, requiring no specialized training data and enabling reasoning that verbalization. The authors scale a proof-of-concept model to 3.5 billion parameters and 800 billion tokens. The model demonstrates significant performance improvements on reasoning benchmarks and supports features like per-token adaptive compute and KV-cache sharing at inference time. The paper also visualizes the computation patterns in latent space, showing behaviors like "orbiting" for numerical computations.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The idea of scaling test-time compute by reasoning in latent space is novel and interesting.
3. The paper provides a detailed description of the model architecture, training process, and benchmark results.

## Weaknesses
1. The model's performance on standard benchmarks is not as strong as the latest open-source models, and it is not compared with the latest models (e.g., OLMo-2).
2. The paper does not provide a detailed analysis of the computational efficiency and resource requirements of the proposed model, which is important for practical applications.
3. The paper does not provide a detailed analysis of the potential limitations or failure modes of the proposed model.

## Questions
1. How does the model's performance compare to the latest open-source models, and what are the reasons for any performance differences?
2. What are the computational efficiency and resource requirements of the proposed model, and how do they compare to existing models?
3. What are the potential limitations or failure modes of the proposed model, and how can they be addressed in future work?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4