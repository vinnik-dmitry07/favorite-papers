# Review

## Summary
This paper presents LLaDA2.0, a novel approach for scaling up discrete diffusion language models (dLLM) to 100 billion parameters by converting auto-regressive (AR) models. The key innovation lies in a three-phase training scheme (Warmup-Stable-Decay) that progressively adapts AR models to diffusion-based learning, preserving knowledge and efficiency. The resulting models, LLaDA2.0-mini (16B parameters) and LLaDA2.0-flash (100B parameters), are optimized for practical deployment and show superior performance in complex tasks like code generation and mathematical reasoning. The paper also details comprehensive post-training techniques to align the models with human preferences and enhance inference efficiency. Extensive evaluations demonstrate that LLaDA2.0 achieves competitive results with AR models and shows potential advantages in structured domains.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel three-phase training scheme (Warmup-Stable-Decay) that progressively adapts AR models to diffusion-based learning, addressing the challenge of scaling up diffusion language models.
2. The proposed method achieves competitive results with AR models and shows potential advantages in complex, structured domains like code generation and mathematical reasoning.
3. The authors provide a comprehensive recipe for transforming AR models into diffusion models, which includes not only the training scheme but also post-training techniques such as SFT, DPO, and confidence-aware training. This holistic approach is valuable for reproducibility and practical deployment.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational requirements and resource costs associated with the proposed training scheme. Understanding the scalability of the approach and its feasibility on different hardware configurations is crucial for broader adoption.
2. While the paper demonstrates competitive performance on various benchmarks, a more in-depth analysis of the model's capabilities and limitations would be beneficial. For example, exploring the model's performance on a wider range of tasks, including more challenging ones, could provide a more comprehensive understanding of its strengths and weaknesses.

## Questions
1. Can you provide more details about the computational requirements and resource costs of the proposed training scheme? How does the resource consumption compare to training AR models of similar sizes?
2. How does the model perform on more challenging tasks that were not included in the evaluation suite? Are there specific domains where the model struggles compared to AR models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4