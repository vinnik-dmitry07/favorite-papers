# Review

## Summary
This paper investigates the effectiveness of perplexity-based data pruning for large language model (LLM) pretraining, specifically examining whether a smaller model can be used to prune data for a larger model. The authors demonstrate that a 125 million parameter model can effectively prune datasets for 1 billion and 3 billion parameter models, leading to improvements in downstream performance and training efficiency. They also explore perplexity-based pruning in over-trained and data-constrained regimes and find that it can still yield gains. The paper highlights the importance of considering dataset composition when applying perplexity-based pruning and shows that test set perplexity is not always a reliable metric for evaluating data pruning techniques, as downstream performance can be improved even when test set perplexity increases. The findings suggest that perplexity-based pruning is a valuable technique for improving LLM performance and training efficiency, with potential applications in various training scenarios.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. This paper is well-written and easy to follow.
2. This paper investigates an interesting research question: Can a small model be used to prune data for a larger model?
3. This paper conducts extensive experiments to verify the effectiveness of the proposed method.

## Weaknesses
1. The novelty of this paper is limited. The method proposed in this paper is the same as the method in [1]. The only difference is that this paper evaluates the pruned model on downstream tasks. However, evaluating the pruned model on downstream tasks is a common practice in the field of data pruning for LLMs.

2. The experimental results are not convincing. First, the authors only report the average performance across all downstream tasks. However, the performance of LLMs on downstream tasks is usually highly imbalanced. Therefore, it is necessary to report the performance of LLMs on each downstream task. Second, the authors only report the average normalized accuracy, which is an uncommon metric. It would be more convincing to report more common metrics, such as the pass@1 and pass@5. Third, the authors only compare the proposed method with the baseline model. It would be more convincing to compare the proposed method with other advanced data pruning methods for LLMs.

3. The motivation for this paper is unclear. The authors do not explain why a small model can be used to prune data for a larger model. The authors only conduct experiments to verify this idea, but do not provide any theoretical analysis or intuitive explanation.

[1] Marion, J., et al. "Data pruning via model proxies." arXiv preprint arXiv:2306.08751 (2023).

## Questions
1. What is the novelty of this paper?
2. Why can a small model be used to prune data for a larger model?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
2

## Confidence
4