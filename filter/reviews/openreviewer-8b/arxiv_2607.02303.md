# Review

## Summary
The paper proposes HOLA, a method to add a bounded, exact KV cache to linear attention models. The cache is built by keeping the top-$w$ keys and values with the largest residual error, and the read is done by a decoupled RMSNorm cache path. The resulting model shows lower perplexity and better long-context retrieval abilities.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. The method is well-motivated and the presentation is clear.
- The method is simple and effective. The authors did a good job explaining the motivation behind the design choices.
- The experiments are comprehensive and well-designed, covering language modeling, commonsense, retrieval, and long-context benchmarks. The results are strong, showing lower perplexity and better long-context retrieval abilities.

## Weaknesses
- The proposed method is only evaluated on a single model size (340M), making it unclear if the improvements would generalize to other model sizes.
- The paper does not provide a detailed analysis of the cache eviction dynamics, such as the distribution of the cached KV pairs and how the cache grows and shrinks over time.
- The paper does not compare against other methods that use a bounded cache, such as the related work mentioned in the paper (LTE).

## Questions
- How does the eviction rule perform at different model scales? Would the same cache size (w=64) be sufficient for larger models?
- How does the cache eviction dynamics evolve over time? How does it affect the model's performance?
- How does HOLA compare to other bounded cache approaches, such as LTE?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4