## Reviewer

### Summary

This paper proposes to augment the transformer architecture with a non-differentiable memory that stores key-value pairs of recent input tokens. The memory is used as an additional attention layer to retrieve information from the past. The authors demonstrate that this approach improves perplexity on various long-form datasets, including code, math papers, and books. The authors also show that the model can generalize to larger memory sizes than it was trained on.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and effective.
- The paper is well-written and easy to follow.

### Weaknesses

- The paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study on the effect of the memory size, the number of heads, or the number of layers. The authors also do not provide a comparison with other long-range attention methods.
- The paper does not provide a detailed explanation of the experimental setup. For example, the authors do not provide the exact hyperparameters used for each experiment. The authors also do not provide a description of the datasets used in the experiments.
- The paper does not provide a discussion of the limitations of the proposed method. For example, the authors do not discuss the potential trade-offs between memory size and computational cost.

### Questions

- How does the proposed method compare to other long-range attention methods?
- What is the effect of the memory size on the performance of the proposed method?
- What is the effect of the number of heads on the performance of the proposed method?
- What is the effect of the number of layers on the performance of the proposed method?
- How does the proposed method perform on other long-form datasets?
- What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a simple method to increase the context length of language models by using a non-differentiable external memory to store the (key, value) pairs of recent tokens. The method is evaluated on several long-form datasets, including code, math papers, and books, and is shown to improve perplexity over a vanilla transformer baseline.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and effective.
- The paper is well-written and easy to follow.
- The experiments are extensive and show that the proposed method improves perplexity on several long-form datasets.

### Weaknesses

- The paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study on the effect of the memory size, the number of heads, or the number of layers. The authors also do not provide a comparison with other long-range attention methods.
- The paper does not provide a detailed explanation of the experimental setup. For example, the authors do not provide the exact hyperparameters used for each experiment. The authors also do not provide a description of the datasets used in the experiments.
- The paper does not provide a discussion of the limitations of the proposed method. For example, the authors do not discuss the potential trade-offs between memory size and computational cost.

### Questions

- How does the proposed method compare to other long-range attention methods?
- What is the effect of the memory size on the performance of the proposed method?
- What is the effect of the number of heads on the performance of the proposed method?
- What is the effect of the number of layers on the performance of the proposed method?
- How does the proposed method perform on other long-form datasets?
- What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new architecture to extend the context length of the transformer model. The proposed method is to use a non-differentiable external memory to store the (key, value) pairs of recent tokens. The method is evaluated on several long-form datasets, including code, math papers, and books, and is shown to improve perplexity over a vanilla transformer baseline.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and effective.
- The paper is well-written and easy to follow.
- The experiments are extensive and show that the proposed method improves perplexity on several long-form datasets.

### Weaknesses

- The paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study on the effect of the memory size, the number of heads, or the number of layers. The authors also do not provide a comparison with other long-range attention methods.
- The paper does not provide a detailed explanation of the experimental setup. For example, the authors do not provide the exact hyperparameters used for each experiment. The authors also do not provide a description of the datasets used in the experiments.
- The paper does not provide a discussion of the limitations of the proposed method. For example, the authors do not discuss the potential trade-offs between memory size and computational cost.

### Questions

- How does the proposed method compare to other long-range attention methods?
- What is the effect of the memory size on the performance of the proposed method?
- What is the effect of the number of heads on the performance of the proposed method?
- What is the effect of the number of layers on the performance of the proposed method?
- How does the proposed method perform on other long-form datasets?
- What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method for increasing the context length of transformer models by using a non-differentiable external memory to store the (key, value) pairs of recent tokens. The method is evaluated on several long-form datasets, including code, math papers, and books, and is shown to improve perplexity over a vanilla transformer baseline.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and effective.
- The paper is well-written and easy to follow.
- The experiments are extensive and show that the proposed method improves perplexity on several long-form datasets.

### Weaknesses

- The paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study on the effect of the memory size, the number of heads, or the number of layers. The authors also do not provide a comparison with other long-range attention methods.
- The paper does not provide a detailed explanation of the experimental setup. For example, the authors do not provide the exact hyperparameters used for each experiment. The authors also do not provide a description of the datasets used in the experiments.
- The paper does not provide a discussion of the limitations of the proposed method. For example, the authors do not discuss the potential trade-offs between memory size and computational cost.

### Questions

- How does the proposed method compare to other long-range attention methods?
- What is the effect of the memory size on the performance of the proposed method?
- What is the effect of the number of heads on the performance of the proposed method?
- What is the effect of the number of layers on the performance of the proposed method?
- How does the proposed method perform on other long-form datasets?
- What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a simple method to increase the context length of transformer models by using a non-differentiable external memory to store the (key, value) pairs of recent tokens. The method is evaluated on several long-form datasets, including code, math papers, and books, and is shown to improve perplexity over a vanilla transformer baseline.

The reviewers generally agree that the paper presents a simple and effective method. The paper is well-written and easy to follow. The experiments are extensive and show that the proposed method improves perplexity on several long-form datasets. However, the paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study on the effect of the memory size, the number of heads, or the number of layers. The authors also do not provide a comparison with other long-range attention methods. The paper does not provide a detailed explanation of the experimental setup. For example, the authors do not provide the exact hyperparameters used for each experiment. The authors also do not provide a description of the datasets used in the experiments. The paper does not provide a discussion of the limitations of the proposed method. For example, the authors do not discuss the potential trade-offs between memory size and computational cost.

### justification_for_why_not_higher_score

The paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study on the effect of the memory size, the number of heads, or the number of layers. The authors also do not provide a comparison with other long-range attention methods. The paper does not provide a detailed explanation of the experimental setup. For example, the authors do not provide the exact hyperparameters used for each experiment. The authors also do not provide a description of the datasets used in the experiments. The paper does not provide a discussion of the limitations of the proposed method. For example, the authors do not discuss the potential trade-offs between memory size and computational cost.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision Summary

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision Comment

The paper proposes a simple method to increase the context length of transformer models by using a non-differentiable external memory to store the (key, value) pairs of recent tokens. The method is evaluated on several long-form datasets, including code, math papers, and books, and is shown to improve perplexity over a vanilla transformer baseline.

The reviewers generally agree that the paper presents a simple and effective method. The paper is well-written and easy to follow. The experiments are extensive and show that the proposed method improves perplexity on several long-form datasets. However, the paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study on the effect of the memory size, the number of heads, or the number of layers. The authors also do not provide a comparison with other long-range attention methods. The paper does not provide a detailed explanation of the experimental setup. For example, the authors do not provide the exact hyperparameters used for each experiment. The authors also do not provide a description of the datasets used in the experiments. The paper does not provide a discussion of the limitations of the proposed method. For example, the authors do not discuss the potential trade-offs between memory size and computational cost.

**********

**********

## Paper Decision Policy

1. If at least 3 reviewers score 6 or higher, it is an accept (either spotlight/oral or poster depending on the score and the category).
2. If at least 2 reviewers score 6 or higher and no one scores lower than 5, it is an accept (either spotlight/oral or poster depending on the score and the category).
3. If at least 5 reviewers score 6 or higher, it is an accept (either spotlight/oral or poster depending on the score and the category).
4. If no more than one reviewer scores 6 or higher, or if more than 50% of the reviewers score 5 or lower, it is a reject.
5. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate)

1. If at least 3 reviewers score 8 or higher, it is an oral accept.
2. If at least 3 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
5. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 2)

1. If at least 3 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 6 or higher, it is an accept (poster).
4. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
5. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 3)

1. If at least 3 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is a poster accept.
3. If at least 5 reviewers score 6 or higher, it is an accept (poster).
4. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
5. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 4)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
6. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 5)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
7. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 6)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
8. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 7)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
9. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 8)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
10. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 9)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 10)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 11)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 12)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 13)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 14)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 15)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 16)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 17)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 18)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If at least 5 reviewers score 6 or higher, it is an accept (poster).
5. If at least 3 reviewers score 8 or higher, it is an accept (poster).
6. If at least 3 reviewers score 7 or higher, it is an accept (spotlight).
7. If at least 3 reviewers score 6 or higher, it is an accept (poster).
8. If at least 3 reviewers score 5 or higher, it is an accept (poster).
9. If at least 1 reviewer scores 9 or higher, it is an oral accept.
10. If no more than one reviewer scores 8 or higher, if more than 50% of the reviewers score 4 or lower, or if the score is 6 or higher and no one scores 7 or higher, it is a reject.
11. In all other cases, the PC members discuss the paper until a consensus is reached.

**********

**********

## Paper Decision Policy (Alternate 19)

1. If at least 5 reviewers score 8 or higher, it is an oral accept.
2. If at least 5 reviewers score 8 or higher, it is an accept (spotlight).
3. If at least 5 reviewers score 7 or higher, it is an accept (spotlight).
4. If