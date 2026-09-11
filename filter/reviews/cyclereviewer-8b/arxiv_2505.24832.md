## Reviewer

### Summary

This paper proposes a new definition of memorization based on Kolmogorov complexity and uses it to measure the capacity of language models. The paper also proposes a scaling law for membership inference attacks based on model capacity and dataset size.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The proposed definition of memorization is novel and interesting. The paper also proposes a scaling law for membership inference attacks based on model capacity and dataset size.

### Weaknesses

The paper's main contribution is the proposed definition of memorization based on Kolmogorov complexity. However, this definition is not very practical, as it is difficult to estimate Kolmogorov complexity in practice. The paper also does not provide a clear comparison with existing definitions of memorization, such as those based on perplexity or likelihood.

The paper's experiments are limited to small-scale models and datasets. It is not clear how the proposed definition of memorization would scale to larger models and datasets.

The paper does not provide a clear discussion of the limitations of the proposed definition of memorization.

### Questions

1. How does the proposed definition of memorization compare to existing definitions of memorization, such as those based on perplexity or likelihood?
2. How does the proposed definition of memorization scale to larger models and datasets?
3. What are the limitations of the proposed definition of memorization?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new definition of memorization based on Kolmogorov complexity and uses it to measure the capacity of language models. The paper also proposes a scaling law for membership inference attacks based on model capacity and dataset size.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed definition of memorization is novel and interesting. The paper also proposes a scaling law for membership inference attacks based on model capacity and dataset size.

### Weaknesses

The paper's main contribution is the proposed definition of memorization based on Kolmogorov complexity. However, this definition is not very practical, as it is difficult to estimate Kolmogorov complexity in practice. The paper also does not provide a clear comparison with existing definitions of memorization, such as those based on perplexity or likelihood.

The paper's experiments are limited to small-scale models and datasets. It is not clear how the proposed definition of memorization would scale to larger models and datasets.

The paper does not provide a clear discussion of the limitations of the proposed definition of memorization.

### Questions

1. How does the proposed definition of memorization compare to existing definitions of memorization, such as those based on perplexity or likelihood?
2. How does the proposed definition of memorization scale to larger models and datasets?
3. What are the limitations of the proposed definition of memorization?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method for estimating how much a model “knows” about a datapoint and use it to measure the capacity of modern language models. The authors propose a definition of memorization that quantifies the extent to which a model retains information about a specific datapoint. Their approach leverages the concept of compression rate in bits: a model is considered to have memorized an input if the input can be compressed into a shorter encoding when the model is available. The authors train language models on datasets of increasing size and observe that models memorize until their capacity fills, at which point “grokking” begins, and unintended memorization decreases as models begin to generalize.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed definition of memorization is novel and interesting. The paper also proposes a scaling law for membership inference attacks based on model capacity and dataset size.

### Weaknesses

The paper's main contribution is the proposed definition of memorization based on Kolmogorov complexity. However, this definition is not very practical, as it is difficult to estimate Kolmogorov complexity in practice. The paper also does not provide a clear comparison with existing definitions of memorization, such as those based on perplexity or likelihood.

The paper's experiments are limited to small-scale models and datasets. It is not clear how the proposed definition of memorization would scale to larger models and datasets.

The paper does not provide a clear discussion of the limitations of the proposed definition of memorization.

### Questions

1. How does the proposed definition of memorization compare to existing definitions of memorization, such as those based on perplexity or likelihood?
2. How does the proposed definition of memorization scale to larger models and datasets?
3. What are the limitations of the proposed definition of memorization?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the capacity of language models and how it scales with the size of the training data. The authors propose a new definition of memorization based on Kolmogorov complexity and use it to measure the capacity of language models. They find that the capacity of language models increases with the size of the training data, but eventually plateaus as the data size exceeds the model capacity. They also propose a scaling law for membership inference attacks based on model capacity and dataset size.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel definition of memorization based on Kolmogorov complexity and uses it to measure the capacity of language models. This is a new and interesting approach that could potentially lead to a better understanding of how language models work.

2. The paper provides a thorough analysis of the capacity of language models and how it scales with the size of the training data. This is a valuable contribution to the field of natural language processing.

3. The paper proposes a scaling law for membership inference attacks based on model capacity and dataset size. This could potentially be useful for practitioners who want to understand the risks associated with using language models in certain applications.

### Weaknesses

1. The paper assumes that the training data is randomly sampled from a uniform distribution, which may not be a realistic assumption in practice.

2. The paper does not consider the impact of hyperparameters on the capacity of language models. For example, the authors do not investigate how the capacity of language models changes when the number of layers, the hidden dimension, or the learning rate is varied.

3. The paper does not provide a clear comparison with existing definitions of memorization, such as those based on perplexity or likelihood.

### Questions

1. How does the proposed definition of memorization compare to existing definitions of memorization, such as those based on perplexity or likelihood?

2. How does the proposed definition of memorization scale to larger models and datasets?

3. What are the limitations of the proposed definition of memorization?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new definition of memorization based on Kolmogorov complexity and uses it to measure the capacity of language models. The paper also proposes a scaling law for membership inference attacks based on model capacity and dataset size. The reviewers agree that the paper is well-written and easy to follow. The proposed definition of memorization is novel and interesting. However, the reviewers also raised several concerns, including the practicality of the proposed definition, the lack of comparison with existing definitions of memorization, and the limited experiments on small-scale models and datasets. The authors did not provide a clear response to these concerns during the rebuttal period. Therefore, I recommend rejecting the paper.

### justification_for_why_not_higher_score

The reviewers raised several concerns, including the practicality of the proposed definition, the lack of comparison with existing definitions of memorization, and the limited experiments on small-scale models and datasets. The authors did not provide a clear response to these concerns during the rebuttal period.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)