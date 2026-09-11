# Review

## Summary
The paper introduces a novel framework called Compute as Teacher (CaT) that leverages inference compute to generate parallel rollouts, which are then used to create pseudo-reference responses for training without human labels. This approach is applicable to both verifiable and non-verifiable domains. For non-verifiable domains, the authors propose a method to generate self-proposed rubrics from the pseudo-reference, which are then used to derive rewards. The framework is evaluated on two datasets: HealthBench and MATH-500, demonstrating its effectiveness in improving model performance while significantly reducing inference-time compute requirements.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel framework that leverages inference compute to generate parallel rollouts, which are then used to create pseudo-reference responses for training without human labels. This approach is applicable to both verifiable and non-verifiable domains.
2. The paper is well-structured and clearly written, with a logical flow that makes it easy to follow the authors' reasoning and methodology.
3. The authors conduct a thorough empirical evaluation of their proposed framework on two datasets: HealthBench and MATH-500. The results demonstrate the effectiveness of the approach in improving model performance while significantly reducing inference-time compute requirements.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational overhead introduced by the CaT framework. While it claims to reduce inference-time compute requirements, it is important to quantify the additional compute needed for tasks such as rubric generation and synthesis. A more comprehensive analysis of the computational trade-offs would strengthen the paper.
2. The paper lacks a thorough comparison with existing methods that use synthetic data generation for training. The authors should include a more detailed discussion of how their approach compares to other synthetic data generation techniques in terms of quality, diversity, and computational efficiency.
3. The paper does not provide a detailed analysis of the diversity of the generated rollouts. The quality of the pseudo-reference response may depend on the diversity of the generated rollouts. The authors should include a more detailed analysis of how the diversity of the rollouts affects the quality of the pseudo-reference response and the overall performance of the framework.

## Questions
1. Can you provide a more detailed analysis of the computational overhead introduced by the CaT framework? How does the computational cost of tasks like rubric generation and synthesis compare to the inference-time compute savings?
2. How does the CaT framework compare to other synthetic data generation methods in terms of quality, diversity, and computational efficiency? Can you provide a more detailed comparison with existing approaches?
3. Can you provide a more detailed analysis of the diversity of the generated rollouts? How does the diversity of the rollouts affect the quality of the pseudo-reference response and the overall performance of the framework?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4