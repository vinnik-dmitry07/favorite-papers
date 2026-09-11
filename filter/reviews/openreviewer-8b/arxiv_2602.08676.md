# Review

## Summary
This paper introduces LLaDA2.1, a discrete diffusion language model that incorporates token-to-token (T2T) editing to improve decoding speed while maintaining generation quality. The model features a configurable threshold decoding scheme with two modes: Speedy Mode (S Mode) for faster generation with reduced quality checks, and Quality Mode (Q Mode) for higher quality at the cost of slower decoding. LLaDA2.1 also employs a Reinforcement Learning (RL) framework for stable gradient estimation and enhanced performance. The model is available in 16B and 100B parameter variants, demonstrating strong performance across various benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The introduction of T2T editing to discrete diffusion models is novel and addresses the challenge of balancing decoding speed and quality.
2. The dual-mode decoding scheme provides flexibility, allowing users to adjust the trade-off between speed and accuracy based on their needs.
3. The implementation of an RL framework for dLLMs is innovative, particularly the use of ELBO-based Block-level Policy Optimization (EBPO) for stable gradient estimation.
4. The model achieves impressive decoding speeds, particularly in code-related tasks, with the 100B parameter model reaching up to 663 TPS on LiveCodeBench.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational cost associated with the RL training stage. Understanding the resources required for this step is crucial for assessing the practicality of adopting this approach.
2. While the paper mentions the use of block-wise causal masked attention for accelerating long-context inference, it lacks a comprehensive discussion on how this approach scales with increasing context lengths and the potential impact on model performance.
3. The performance of LLaDA2.1 in S Mode shows a significant drop in some benchmarks, particularly in general chat scenarios. This raises concerns about the robustness of the model when operating at high speeds.

## Questions
1. Can you provide more details on the computational requirements and time consumption for the RL training stage of LLaDA2.1? How does the cost compare to traditional SFT approaches?
2. How does the performance of LLaDA2.1 in S Mode vary with increasing context length? Are there any benchmarks where the model's performance degrades significantly as the context size grows?
3. The paper mentions the use of block-wise causal masked attention for long-context inference. How does this approach scale with context length, and what are the theoretical limits before performance degrades significantly?
4. How sensitive is the model's performance to the choice of the two threshold parameters, and is there a way to automatically tune these parameters based on the input data?
5. Can you provide more details on the Multi-Turn Forward (MTF) data augmentation technique mentioned in Section 3.1? How does it enhance the model's editing capabilities?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4