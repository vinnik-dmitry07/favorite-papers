# Review

## Summary
This paper proposes Cache-to-Cache (C2C), a new paradigm for direct semantic communication between LLMs. C2C uses a neural network to project and fuse the source model’s KV-cache with that of the target model to enable direct semantic transfer. A learnable gating mechanism selects the target layers that benefit from cache communication. Compared with text communication, C2C utilizes the deep, specialized semantics from both models, while avoiding explicit intermediate text generation. Experiments show that C2C achieves 6.4-14.2% higher average accuracy than individual models. It further outperforms the text communication paradigm by approximately 3.1-5.4%, while delivering an average 2.5× speedup in latency.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed method is novel and interesting. It leverages the KV-Cache as a medium for semantic transfer between LLMs. It supports sharing across different model families and varying model sizes.
2. The paper is well-written and easy to follow.
3. The experiments are comprehensive and the results are impressive.

## Weaknesses
1. The proposed method requires training, which may limit its application scenarios. 
2. The proposed method may be difficult to scale up for multiple LLMs.

## Questions
1. How to extend the proposed method to multiple LLMs?
2. What is the training cost of the proposed method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4