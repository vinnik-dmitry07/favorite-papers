# Review

## Summary
The paper introduces DiffusionGemma, a novel open-weight language model that employs discrete diffusion for high-speed text generation. DiffusionGemma refines blocks of 256 tokens in parallel, bypassing the sequential bottleneck of traditional autoregressive models. Fine-tuned from the Gemma 4 model, it achieves exceptional speed, generating up to 1,500 tokens per second on a single NVIDIA H100 GPU. It also retains strong multimodal capabilities and supports hybrid AR decoding with minimal performance loss, offering a promising approach for balancing speed and intelligence in language modeling.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is novel, and the results are solid.
- The released model is open-sourced, which will be useful for the community.

## Weaknesses
- The paper lacks a comparison with some existing diffusion LLMs, such as LLaDA 2.1 Flash and Nemotron Diffusion.
- The paper does not include a comparison of the generation quality with the original Gemma-4. It would be better to provide the AR performance of DiffusionGemma and compare it with the original Gemma-4.
- The paper does not include a comparison of the reasoning capabilities with existing diffusion LLMs, such as LLaDA 2.1 Flash and Nemotron Diffusion.
- The paper does not include a comparison of the code generation capabilities with existing diffusion LLMs, such as LLaDA 2.1 Flash and Nemotron Diffusion.
- The paper does not include a comparison of the general knowledge QA capabilities with existing diffusion LLMs, such as LLaDA 2.1 Flash and Nemotron Diffusion.

## Questions
- The paper mentions that the model can generate 1,500 tokens per second on a single NVIDIA H100 GPU. How many tokens can it generate per second on a single A100 GPU?
- How does the model perform on long-context tasks, such as 128K, 256K, or 512K contexts?
- How does the model perform on the following tasks: (1) mathematical reasoning, (2) code generation, and (3) general knowledge QA?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4