# Review

## Summary
This paper introduces a new attention mechanism, Infini-attention, for Transformer language models that enables them to handle extremely long sequences with limited memory and computational resources. The key innovation is incorporating a compressive memory into the standard attention mechanism, allowing the model to reuse and retain key, value, and query states from previous segments rather than discarding them. The authors demonstrate the effectiveness of Infini-attention on long-context language modeling, passkey retrieval, and book summarization tasks, showing improvements over existing methods while using significantly less memory.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and its benefits.
2. The paper addresses a significant challenge in the field of natural language processing: handling long sequences with limited resources. The proposed Infini-attention mechanism offers a promising solution to this problem.
3. The authors provide a thorough evaluation of their method on multiple benchmarks, including long-context language modeling, passkey retrieval, and book summarization tasks. The results demonstrate the effectiveness of Infini-attention in handling long sequences while maintaining good performance.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational complexity of Infini-attention compared to other methods for handling long sequences. While the authors claim that their method is more efficient, a formal analysis would strengthen this claim.
2. The paper could benefit from a more detailed comparison with other methods for handling long sequences, such as those based on sparse attention or hierarchical attention. While the authors compare their method to Transformer-XL and Memorizing Transformers, a broader comparison would provide a better understanding of the landscape of methods for handling long sequences.
3. The paper does not provide a detailed analysis of the sensitivity of the method to various hyperparameters, such as the segment length and the number of heads. Understanding how these hyperparameters affect the performance of the method is important for practical implementation.

## Questions
1. Can you provide a more detailed analysis of the computational complexity of Infini-attention compared to other methods for handling long sequences?
2. How does Infini-attention compare to other methods such as sparse attention or hierarchical attention in terms of handling long sequences?
3. Can you provide a more detailed analysis of the sensitivity of the method to various hyperparameters, such as the segment length and the number of heads?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4