# Review

## Summary
This paper studies scaling laws for language models. It shows that the scaling laws are sensitive to the complexity of the training data. The paper proposes to use gzip compressibility as a measure of the complexity of the training data. The paper presents experiments with synthetic data generated from PCFGs, and with natural language and code.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well written and easy to follow. The experiments are well-motivated and well-executed. The topic is timely and interesting.

## Weaknesses
The paper presents an interesting idea, but the empirical evidence is not strong enough to support the claims. The experiments are done on synthetic data, and the results on natural language and code are very limited.

## Questions
* The experiments are done on synthetic data generated from PCFGs. This is a very restricted setting. I understand that this is done to have more control over the data, but it would be good to see experiments with real data. For example, you could use the PCFGs to generate data for pre-training, and train LMs on the pre-training data, and then fine-tune LMs on the fine-tuning data, and compare the scaling laws.
* The results on natural language and code are very limited. It would be good to have more extensive experiments on real data. You could use different pre-training datasets, and compare the scaling laws. There are many pre-training datasets available, for example, you could use the datasets from the Big-Bench benchmark.
* It would be good to see results with larger models. 1.4B is not a very large model these days. It would be good to see results with larger models, for example, 7B, 70B, etc.
* It would be good to see results with more training tokens. 100M tokens is not a lot these days. It would be good to see results with more tokens, for example, 1T tokens.
* It would be good to see results with different optimizers, different learning rates, different training schedules, different architectures, etc.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4