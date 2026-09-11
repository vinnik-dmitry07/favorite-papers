# Review

## Summary
This paper proposes a method to extend the context length of any pre-trained encoder-decoder transformer model to be effectively unbounded by using a kNN index. The authors show that their method can be applied to any pre-trained model and can improve the performance of the base model on long-context tasks without any additional training. They also show that further training with their method can lead to even more improvements. The authors evaluate their method on two long-document summarization datasets and a book summarization dataset, where they show consistent improvements over the base models and other baselines.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The proposed method is simple and can be applied to any pre-trained encoder-decoder transformer model.
- The proposed method can be used at test time on long inputs without any additional training, and with training, the performance can be further improved.
- The proposed method leads to consistent improvements over the base model and other baselines on long-context summarization tasks.

## Weaknesses
- The proposed method is only evaluated on summarization tasks. It would be interesting to see how it performs on other tasks that require long contexts, such as long-document question-answering or narrative QA.
- The proposed method is only evaluated on a few datasets. It would be interesting to see how it performs on other long-context datasets, such as the SCROLLS benchmark (Shaham et al., 2022).
- The proposed method is only evaluated on a few base models. It would be interesting to see how it performs on other encoder-decoder models, such as T5 or T5-XL.

## Questions
- How does the proposed method perform on other tasks that require long contexts, such as long-document question-answering or narrative QA?
- How does the proposed method perform on other long-context datasets, such as the SCROLLS benchmark (Shaham et al., 2022)?
- How does the proposed method perform on other encoder-decoder models, such as T5 or T5-XL?
- How does the proposed method compare to other methods for handling long contexts, such as streaming attention or Sliding Window Attention (Kini et al., 2021)?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4