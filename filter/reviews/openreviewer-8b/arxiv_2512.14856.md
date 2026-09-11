# Review

## Summary
This paper introduces T5Gemma 2, a new generation of lightweight encoder-decoder models that build upon the T5Gemma family. T5Gemma 2 extends the capabilities of its predecessors by enhancing multilingual, multimodal, and long-context understanding. The model adapts a pretrained decoder-only model into an encoder-decoder architecture using the UL2 objective and leverages the Gemma 3 model as a foundation. To improve efficiency, T5Gemma 2 introduces two strategies: tied word embeddings, which share embeddings across the encoder and decoder, and merged attention, which combines decoder self- and cross-attention into a single module. Experimental results show that T5Gemma 2 achieves comparable or better performance than Gemma 3 during pretraining and significantly improves in post-training scenarios. The pretrained models are released to the research community in various sizes (270M-270M, 1B-1B, and 4B-4B).

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed T5Gemma 2 model is a strong multilingual, multimodal, and long-context encoder-decoder language model.
3. The authors conduct extensive experiments and provide detailed ablation studies to validate their design choices.

## Weaknesses
1. The novelty of this paper is limited. The proposed T5Gemma 2 model is largely based on the previous Gemma 3 model, with modifications such as tied embeddings and merged attention. These changes are incremental and do not represent a significant departure from existing methods.
2. The paper does not provide a clear explanation of the benefits of using an encoder-decoder architecture for long-context tasks. The authors should elaborate on why this specific architecture is advantageous for handling long sequences and provide a comparison with decoder-only models in this regard.
3. The paper lacks a comparison with other long-context models such as LongChat, DeepSeek-Chat, and Qwen2. Including such comparisons would help to better position T5Gemma 2 in the context of existing solutions for long-context understanding.
4. The paper does not provide a detailed analysis of the computational efficiency of T5Gemma 2. Given the importance of efficiency in practical applications, an analysis of training and inference costs would be valuable. This should include metrics such as training time, memory usage, and FLOPs.
5. The paper does not include a detailed analysis of the impact of the tied embeddings and merged attention modifications on the model's performance. While the ablation studies are present, a more in-depth analysis of these specific changes would provide a better understanding of their contributions to the overall model performance.

## Questions
Please refer to the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4