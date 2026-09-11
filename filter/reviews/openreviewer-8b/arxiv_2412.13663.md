# Review

## Summary
This paper presents ModernBERT, an encoder-only transformer model that incorporates modern model optimizations to achieve state-of-the-art performance on various NLP tasks while being efficient and designed for inference on common GPUs. The authors demonstrate that ModernBERT outperforms older BERT models and other encoder-only models on a wide range of tasks, including classification and retrieval, while also being more speed and memory efficient.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The authors conduct a comprehensive set of experiments to evaluate ModernBERT across a wide range of tasks, including classification and retrieval, and provide detailed comparisons with other models.
3. The authors provide detailed information on the training process, including data, hyperparameters, and optimization techniques, which could be useful for reproducibility and further research.

## Weaknesses
1. The paper focuses on encoder-only models, but it would be beneficial to compare ModernBERT with decoder-only models as well. After all, decoder-only models have become the mainstream in recent years, and many of them have open-source versions with similar parameter counts to ModernBERT (e.g., LLaMA-3 8B, Qwen-2 7B, Mistral 7B). Such comparisons could provide a more comprehensive understanding of where encoder-only models stand in comparison to the current trends.
2. The paper does not provide a detailed analysis of the individual contributions of each architectural choice on the performance of ModernBERT. For example, it would be interesting to see how much impact the use of RoPE, GeGLU, pre-normalization, and unpadding has on the model's performance. Such an ablation study could help readers understand which techniques are most effective and why.
3. The paper does not provide a detailed analysis of the interpretability of ModernBERT. For example, it would be interesting to see how the model makes decisions on a sample of data and whether there are any patterns or biases in its attention distribution. Such an analysis could help readers understand how the model works and potentially identify areas for improvement.

## Questions
1. How does ModernBERT compare to decoder-only models with similar parameter counts?
2. What is the impact of each architectural choice on the performance of ModernBERT?
3. How does ModernBERT make decisions and what are the patterns or biases in its attention distribution?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4