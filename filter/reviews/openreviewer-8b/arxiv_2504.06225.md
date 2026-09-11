# Review

## Summary
This paper explores adapting pretrained decoder-only LLMs to encoder-decoder models to achieve a better quality-efficiency trade-off. The authors propose a straightforward adaptation method, initializing the encoder from the decoder in a decoder-only model and fine-tuning all parameters. They conduct experiments using Gemma-2 2B and 9B models, as well as a suite of mT5-sized models, demonstrating that encoder-decoder LLMs achieve comparable or better performance than decoder-only models under similar inference budgets. Encoder-decoder LLMs also show better performance on SuperGLUE. The authors plan to release their checkpoints to facilitate future research.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed adaptation method is simple and effective.
- The experiments are comprehensive, covering a range of model sizes and tasks.

## Weaknesses
- The paper only considers adapting a specific type of decoder-only model (Gemma-2), and it is unclear whether the proposed method generalizes to other decoder-only models.
- The paper does not provide a detailed analysis of the learned representations or any insight into why the adaptation method works.
- The paper does not compare the proposed method with other methods for improving inference efficiency, such as quantization, KV cache optimization, or the use of smaller models.

## Questions
- How does the proposed method perform when adapting other types of decoder-only models, such as LLaMA or QWen?
- Can you provide more insight into why the adaptation method works? For example, have you analyzed the learned representations or the attention patterns of the encoder-decoder model compared to the decoder-only model?
- How does the proposed method compare to other methods for improving inference efficiency, such as quantization, KV cache optimization, or the use of smaller models? A table comparing the performance and inference efficiency of the proposed method with these approaches would be helpful.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4