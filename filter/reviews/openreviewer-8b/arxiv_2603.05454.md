# Review

## Summary
This paper proposes the Longest Stable Prefix (LSP) scheduler, a training-free and model-agnostic inference paradigm designed to accelerate Diffusion Language Models (DLMs) by addressing the inefficiencies in current decoding schedulers, which rely on scattered acceptance. LSP identifies and commits the longest contiguous, stable prefix in a single atomic step, maximizing KV cache reuse and ensuring efficient attention computations. This approach reduces the number of repair cycles needed for coherent generation and significantly accelerates inference without compromising output quality. Extensive evaluations on LLaDA-8B and Dream-7B demonstrate LSP's effectiveness across various tasks, including mathematical reasoning, code generation, and creative writing, achieving up to a 3.4x speedup.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed LSP method is simple yet effective, achieving a significant speedup while maintaining performance.
- The ablation study is comprehensive, clearly demonstrating the effectiveness of LSP's core components.

## Weaknesses
- The experiments are conducted on only two models, LLaDA-8B and Dream-7B. It would be beneficial to include more models of varying sizes, such as smaller-scale models like LLaMA-3.1-1B and larger models like LLaMA-3.1-70B, to demonstrate the generalizability of LSP.

## Questions
- In Table 1, why is the performance of LSP on the WritingPrompts dataset not reported? Additionally, it would be helpful to include the speedup results for the WritingPrompts dataset to provide a more comprehensive evaluation of LSP's performance.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4