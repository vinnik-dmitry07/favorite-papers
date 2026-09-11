# Review

## Summary
This paper proposes a new training and inference method for diffusion language models (dLMs) to improve the parallel decoding efficiency. Specifically, the authors propose to combine the strengths of masked and uniform dLMs, and propose On-Policy Uniform Training (OPUT) to train a model that can recover clean tokens from both masked and uniform noisy inputs. During inference, the authors propose Soft Parallel Decoding (SPD) to represent each intermediate decoding state as a weighted sum of the embedding of the predicted token and the mask token, which enables iterative self-revising in the embedding space. Experiments show that the proposed method can significantly improve the tokens per forward (TPF) while maintaining the model accuracy.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The idea of combining the strengths of masked and uniform dLMs is novel and interesting. The proposed method can improve the parallel decoding efficiency of dLMs without sacrificing the model accuracy.
2. The experimental results are strong. The proposed method can significantly improve the TPF of dLMs on math and code tasks.

## Weaknesses
1. The proposed method is only evaluated on LLaDA-2.0-mini, which is a relatively small dLM with 345M parameters. It is unclear whether the method can scale up to larger dLMs, e.g., LLaDA-2.0 with 1B parameters.
2. The proposed method is only evaluated on math and code tasks. It is unclear whether the method can generalize to other tasks, e.g., natural language inference.
3. The proposed method is only compared with a few baselines. It is unclear whether the method can outperform stronger baselines, e.g., hierarchical decoding [1].

[1] Accelerating Parallel Decoding of Diffusion Language Models via Hierarchical Generation

## Questions
1. Can the proposed method scale up to larger dLMs, e.g., LLaDA-2.0 with 1B parameters?
2. Can the proposed method generalize to other tasks, e.g., natural language inference?
3. Can the proposed method outperform stronger baselines, e.g., hierarchical decoding?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4