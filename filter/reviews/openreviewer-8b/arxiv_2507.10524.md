# Review

## Summary
This paper introduces Mixture-of-Recursions (MoR), a novel framework that combines parameter sharing and adaptive computation in a single Recursive Transformer model. MoR achieves parameter efficiency by reusing a shared stack of layers across recursion steps and enhances memory and computation efficiency by dynamically assigning different recursion depths to individual tokens. This approach reduces the quadratic attention computation to focus only on active tokens at each recursion depth and selectively caches key-value pairs to minimize memory usage. MoR forms a new performance frontier across various model scales, demonstrating lower validation perplexity and improved few-shot accuracy compared to existing recursive and vanilla baselines, while also achieving higher throughput.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. MoR combines parameter sharing and adaptive computation in a single framework, addressing both efficiency aspects simultaneously.
2. The dynamic token-level recursion in MoR allows for efficient allocation of computational resources, focusing on tokens that require deeper processing.
3. The selective KV caching strategy reduces memory traffic, leading to improved throughput without post-hoc modifications.
4. MoR demonstrates superior performance across various model scales, outperforming both vanilla and recursive baselines in terms of validation perplexity and few-shot accuracy.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational overhead introduced by the routing mechanism, especially for large-scale models.
2. While the paper claims improved memory efficiency, it lacks a comprehensive analysis of the routing mechanism's impact on memory usage across different model scales.
3. The scalability of MoR to even larger models and datasets is not thoroughly explored in the paper.

## Questions
1. How does the routing mechanism scale with increasing model size and complexity?
2. What are the specific contributions of each component (parameter sharing, adaptive recursion, KV caching) to the overall performance improvements?
3. How does MoR handle the trade-off between computation and memory efficiency, especially at scale?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4