## Reviewer

### Summary

The paper investigates the effectiveness of perplexity-based data pruning for large language models (LLMs). The authors demonstrate that a small language model can effectively prune the pretraining dataset of a larger model, leading to significant gains in downstream performance. They also show that the optimal pruning techniques vary depending on the dataset composition and that perplexity-based data pruning can still lead to gains in non-standard training regimes, such as over-training and data-constrained settings. Additionally, the authors highlight that test set perplexity may not always be a reliable metric for evaluating data pruning techniques, and instead suggest evaluating based on downstream performance.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper provides a comprehensive evaluation of perplexity-based data pruning for LLMs, considering various aspects such as dataset composition, training regimes, and evaluation metrics. The authors also provide a detailed analysis of the effects of perplexity-based pruning on the distribution of perplexities and domain composition of the dataset.

### Weaknesses

The paper's main contribution is an empirical investigation of perplexity-based data pruning for LLMs. While the results are promising, the paper lacks a theoretical foundation or a clear explanation of the underlying mechanisms driving the observed effects. The authors acknowledge this limitation and suggest that future work should investigate the predictive theory for how pruning parameters should be selected for different datasets. However, this leaves the paper without a clear takeaway message or practical guidance for practitioners.

### Questions

- The paper mentions that the optimal pruning techniques vary depending on the dataset composition. Can the authors provide more insights into what factors contribute to this variation and how practitioners can determine the optimal pruning strategy for a specific dataset?

- The paper highlights that test set perplexity may not always be a reliable metric for evaluating data pruning techniques. Can the authors provide more guidance on how to evaluate the effectiveness of data pruning techniques in practice?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents an empirical study on perplexity-based data pruning for LLMs. The authors investigate whether small language models can be used to prune large-scale datasets and improve the performance of larger language models. They demonstrate that perplexity-based pruning can improve downstream task performance and reduce pretraining steps. They also show that the effectiveness of perplexity-based pruning varies depending on the dataset composition and training regime. Additionally, they find that test set perplexity may not be a reliable metric for evaluating data pruning techniques.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors conduct a comprehensive empirical study on perplexity-based data pruning for LLMs, considering various aspects such as dataset composition, training regimes, and evaluation metrics.
- The paper highlights the limitations of relying solely on test set perplexity as a metric for evaluating data pruning techniques, emphasizing the importance of considering downstream performance.

### Weaknesses

- The paper's contributions are mostly empirical, and it lacks a theoretical foundation or a clear explanation of the underlying mechanisms driving the observed effects.
- The paper does not provide a predictive theory for how pruning parameters should be selected for different datasets, which could be a valuable contribution for practitioners.
- The paper does not provide a clear takeaway message or practical guidance for practitioners on how to apply perplexity-based data pruning in their own work.

### Questions

- How do the authors suggest practitioners select the optimal pruning parameters for their specific dataset?
- What are the key factors that contribute to the variation in the effectiveness of perplexity-based pruning across different dataset compositions?
- How can the authors' findings on the limitations of test set perplexity inform the development of more effective evaluation metrics for data pruning techniques?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper investigates the effectiveness of perplexity-based data pruning for large language models (LLMs). The authors demonstrate that a small language model can effectively prune the pretraining dataset of a larger model, leading to significant gains in downstream performance. They also show that the optimal pruning techniques vary depending on the dataset composition and that perplexity-based data pruning can still lead to gains in non-standard training regimes, such as over-training and data-constrained settings. Additionally, the authors highlight that test set perplexity may not always be a reliable metric for evaluating data pruning techniques, and instead suggest evaluating based on downstream performance.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper provides a comprehensive evaluation of perplexity-based data pruning for LLMs, considering various aspects such as dataset composition, training regimes, and evaluation metrics. The authors also provide a detailed analysis of the effects of perplexity-based pruning on the distribution of perplexities and domain composition of the dataset.

### Weaknesses

The paper's main contribution is an empirical investigation of perplexity-based data pruning for LLMs. While the results are promising, the paper lacks a theoretical foundation or a clear explanation of the underlying mechanisms driving the observed effects. The authors acknowledge this limitation and suggest that future work should investigate the predictive theory for how pruning parameters should be selected for different datasets. However, this leaves the paper without a clear takeaway message or practical guidance for practitioners.

### Questions

- The paper mentions that the optimal pruning techniques vary depending on the dataset composition. Can the authors provide more insights into what factors contribute to this variation and how practitioners can determine the optimal pruning strategy for a specific dataset?
- The paper highlights that test set perplexity may not always be a reliable metric for evaluating data pruning techniques. Can the authors provide more guidance on how to evaluate the effectiveness of data pruning techniques in practice?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper investigates the effectiveness of perplexity-based data pruning for large language models (LLMs). The authors demonstrate that a small language model can effectively prune the pretraining dataset of a larger model, leading to significant gains in downstream performance. They also show that the optimal pruning techniques vary depending on the dataset composition and that perplexity-based data pruning can still lead to gains in non-standard training regimes, such as over-training and data-constrained settings. Additionally, the authors highlight that test set perplexity may not always be a reliable metric for evaluating data pruning techniques, and instead suggest evaluating based on downstream performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper provides a comprehensive evaluation of perplexity-based data pruning for LLMs, considering various aspects such as dataset composition, training regimes, and evaluation metrics. The authors also provide a detailed analysis of the effects of perplexity-based pruning on the distribution of perplexities and domain composition of the dataset.

### Weaknesses

The paper's main contribution is an empirical investigation of perplexity-based data pruning for LLMs. While the results are promising, the paper lacks a theoretical foundation or a clear explanation of the underlying mechanisms driving the observed effects. The authors acknowledge this limitation and suggest that future work should investigate the predictive theory for how pruning parameters should be selected for different datasets. However, this leaves the paper without a clear takeaway message or practical guidance for practitioners.

### Questions

- The paper mentions that the optimal pruning techniques vary depending on the dataset composition. Can the authors provide more insights into what factors contribute to this variation and how practitioners can determine the optimal pruning strategy for a specific dataset?
- The paper highlights that test set perplexity may not always be a reliable metric for evaluating data pruning techniques. Can the authors provide more guidance on how to evaluate the effectiveness of data pruning techniques in practice?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

The paper investigates the effectiveness of perplexity-based data pruning for large language models (LLMs). The authors demonstrate that a small language model can effectively prune the pretraining dataset of a larger model, leading to significant gains in downstream performance. They also show that the optimal pruning techniques vary depending on the dataset composition and that perplexity-based data pruning can still lead to gains in non-standard training regimes, such as over-training and data-constrained settings. Additionally, the authors highlight that test set perplexity may not always be a reliable metric for evaluating data pruning techniques, and instead suggest evaluating based on downstream performance.

The paper received four reviews, all of which rated it as marginally below the acceptance threshold. The reviewers raised concerns about the lack of theoretical foundation, the limited practical guidance for practitioners, and the lack of a clear takeaway message. The authors provided a rebuttal, but it did not address the reviewers' concerns. Therefore, the paper is not recommended for acceptance.

### justification_for_why_not_higher_score

The paper received four reviews, all of which rated it as marginally below the acceptance threshold. The reviewers raised concerns about the lack of theoretical foundation, the limited practical guidance for practitioners, and the lack of a clear takeaway message. The authors provided a rebuttal, but it did not address the reviewers' concerns. Therefore, the paper is not recommended for acceptance.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)