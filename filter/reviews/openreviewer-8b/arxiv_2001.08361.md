# Review

## Summary
This paper studies scaling laws for language models. The authors train a series of language models with different sizes, compute budgets, and dataset sizes, and fit the test cross-entropy loss with power-law functions. They observe that the test cross-entropy loss follows power-law functions with respect to model size, dataset size, and compute budget. They also observe that the test cross-entropy loss is correlated with the validation loss. Based on these observations, they provide some guidelines for training language models.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- This paper studies an important topic, and the results may be useful for future research on language models.
- The authors conduct extensive experiments to verify their observations.

## Weaknesses
- The authors only study one type of language models, i.e., autoregressive language models with the Transformer architecture. It is not clear whether the observations in this paper apply to other types of language models, such as BERT-like language models.
- The authors only use the cross-entropy loss as the performance metric. It is not clear whether the observations in this paper apply to other performance metrics, such as perplexity and accuracy.
- The authors only conduct experiments on one dataset, i.e., WebText2. It is not clear whether the observations in this paper apply to other datasets.
- The authors do not provide the code, so it is not clear whether their experiments can be reproduced.

## Questions
- Do the observations in this paper apply to other types of language models, such as BERT-like language models?
- Do the observations in this paper apply to other performance metrics, such as perplexity and accuracy?
- Do the observations in this paper apply to other datasets?
- Can their experiments be reproduced?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4