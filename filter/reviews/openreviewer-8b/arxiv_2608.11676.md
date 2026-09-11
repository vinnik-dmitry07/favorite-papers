# Review

## Summary
This paper presents a novel approach to enable communication between heterogeneous LLMs, i.e., LLMs with different model families. The authors identify a key challenge in this setting: the entity grounding problem, where the transfer of contextual information from the sender to the receiver may result in the loss of discrete entity identities. To address this issue, the authors propose XBridge, a decode-free communication protocol that consists of two key components: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps the sender's context tokens to the receiver's vocabulary, providing discrete entity anchors. LEB enables the receiver to query the sender's hidden states for contextual enrichment. The authors evaluate XBridge across three model families (Llama, Qwen, and Mistral) and seven benchmarks, demonstrating its superiority over text-based communication methods in terms of performance and latency.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide a clear motivation for the problem and a detailed explanation of the proposed solution.
2. The authors conduct extensive experiments across multiple model families and benchmarks, providing a comprehensive evaluation of the proposed method.
3. The proposed XBridge addresses an important challenge in heterogeneous LLM systems, enabling more efficient and effective communication between models with different architectures.

## Weaknesses
1. The proposed method requires training a new bridge for each model pair, which may limit its scalability and generalizability.
2. The method is only evaluated in an asymmetric setting, where the sender and receiver are of different architectures. It is unclear how well it would perform in a symmetric setting.

## Questions
1. How does the performance of XBridge scale with the size of the sender model? Is there a point of saturation where increasing the sender's capabilities does not further improve the performance of the receiver?
2. How does XBridge handle rare or out-of-vocabulary entities that may not have a direct mapping to the receiver's vocabulary?
3. Can the proposed method be extended to a symmetric setting, where both the sender and receiver are of the same architecture? How does it compare to the asymmetric setting in such a scenario?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4