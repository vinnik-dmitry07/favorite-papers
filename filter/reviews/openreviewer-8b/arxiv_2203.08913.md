# Review

## Summary
This paper proposes a new attention mechanism that combines the standard attention with kNN attention over an external memory. The external memory is constructed by simply appending the (key, value) pairs from the current training batch. The authors demonstrate that the proposed attention mechanism can improve the language modeling performance on several datasets, including arXiv math, Github, Isabelle, C4, and PG-19. The authors also show that the performance can be further improved by scaling up the model size and the external memory size.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The proposed attention mechanism is simple and effective. It can be easily applied to existing models.
- The authors conducted extensive experiments to demonstrate the effectiveness of the proposed method. The results show that the proposed method can consistently improve the performance on various datasets.
- The authors also show that the proposed method can be applied to large-scale models and the performance can be further improved by scaling up the model size and the external memory size.

## Weaknesses
- The proposed method is very similar to the kNN-LLM method proposed in [1]. The only difference is that the proposed method uses a non-differentiable external memory while kNN-LLM uses a differentiable memory. The authors should discuss the pros and cons of using a non-differentiable external memory.
- The authors should also compare the proposed method with the kNN-LLM method to demonstrate the effectiveness of using a non-differentiable external memory.
- The authors should also compare the proposed method with other long-range attention methods, such as the methods mentioned in the related work section.
- The authors should also compare the proposed method with the Transformer-XL method on the PG-19 dataset, which is a standard benchmark for long-range language modeling.

[1] Zhang et al. kNN-LTM: Towards Efficient and Effective Long-Range Language Modeling via Large Memory. ACL 2022.

## Questions
- The authors should discuss the pros and cons of using a non-differentiable external memory.
- The authors should compare the proposed method with the kNN-LLM method.
- The authors should compare the proposed method with other long-range attention methods.
- The authors should compare the proposed method with the Transformer-XL method on the PG-19 dataset.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4