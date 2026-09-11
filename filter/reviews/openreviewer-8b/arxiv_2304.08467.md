# Review

## Summary
This paper proposes a method to compress prompts into gist tokens, which can be cached and reused for compute efficiency. The method is very simple and straightforward. It simply inserts several gist tokens between the prompt and the input, and masks the attention so that the gist tokens can capture the information of the prompt while the input cannot. The number of gist tokens is a hyperparameter, and the experiments show that a single gist token is enough to capture the information of the prompt. The experiments also show that the method can generalize to unseen prompts.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The method is simple and straightforward. It does not need additional training cost.
2. The method can generalize to unseen prompts to some degree.
3. The method can save the storage cost of the KV cache.

## Weaknesses
1. The method can be viewed as a special case of prompt tuning. Therefore, it is not surprising that the model can learn to compress the prompt into the gist tokens. The novelty of the method is limited.
2. The experiments only use a single gist token, which is not enough to verify that the model can learn to compress the prompt effectively. More experiments with more gist tokens are needed.
3. The experiments only use ROUGE-L and ChatGPT to evaluate the quality of the generation. More evaluation metrics should be used, such as BLEU, Distinct1, Distinct2, and human evaluation.
4. The method can fail if the prompt contains details that are important for the generation. This is a fundamental limitation of the method.

## Questions
1. Can you provide more experimental results with more gist tokens?
2. Can you provide more evaluation results with more evaluation metrics?
3. Can you provide the results of the experiment where the prompt contains details that are important for the generation?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4