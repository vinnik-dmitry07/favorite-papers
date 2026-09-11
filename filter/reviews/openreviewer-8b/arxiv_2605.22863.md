# Review

## Summary
This paper introduces Latent Cache Flow (LCF), a novel method for enabling efficient, non-text-based communication between large language models (LLMs). LCF aims to address the limitations of existing methods like Cache-to-Cache (C2C), which requires large, specialized adapters for cross-model communication and is constrained to shared contexts. LCF achieves a 115x reduction in adapter size and supports communication across different contexts by jointly compressing and translating the key-value (KV) cache states of LLMs into a shared latent space. This latent cache is a compact summary of the sharer’s context, which the receiver can condition on, allowing efficient and flexible communication without the need for text generation. The authors demonstrate that LCF outperforms C2C in both accuracy and efficiency, with a 13 MB LCF adapter achieving better performance than C2C’s 956 MB adapter in shared-context settings. They also introduce LCF-X, an extension that supports cross-context communication by summarizing the sharer’s full KV cache into a fixed-size tensor, which the receiver can condition on. LCF-X significantly reduces communication latency and improves accuracy in cross-context scenarios, outperforming text-based communication methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel approach to inter-model communication, moving beyond text-based and position-aligned methods. This is a meaningful contribution to the field of LLM integration.
2. LCF achieves a significant reduction in adapter size (up to 115x) compared to existing methods like C2C. This makes it more practical for real-world applications where memory and computational resources are limited.
3. The paper provides a thorough empirical evaluation, demonstrating that LCF outperforms C2C in both accuracy and efficiency. The results are presented in a clear and compelling manner.

## Weaknesses
1. The paper only evaluates LCF on a single model pair (Qwen2.5-0.5B-Instruct to Qwen3-0.6B). It would be beneficial to see how LCF performs across different model architectures and sizes, especially larger models.
2. While the paper demonstrates the effectiveness of LCF in controlled settings, the evaluation could be strengthened by testing in more diverse and complex scenarios, such as multi-turn conversations or agentic workflows.
3. The paper could benefit from a more detailed discussion on the selection of the latent dimension size and its impact on performance across different models and tasks.
4. The paper does not provide sufficient details on the computational overhead of LCF compared to C2C in terms of training time, inference speed, and memory usage. A more comprehensive analysis of the efficiency trade-offs would be valuable.

## Questions
1. How does the performance of LCF scale with larger models and different model architectures? Have you tested it on other pairs of models?
2. Can you provide more details on the selection of the latent dimension size? How does it affect the performance across different models and tasks?
3. How does LCF perform in more complex scenarios, such as multi-turn conversations or agentic workflows with longer contexts?
4. Can you provide a more detailed analysis of the computational overhead of LCF compared to C2C, including training time, inference speed, and memory usage?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4