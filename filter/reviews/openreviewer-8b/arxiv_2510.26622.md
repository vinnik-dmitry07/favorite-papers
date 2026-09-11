# Review

## Summary
This paper revisits encoder-decoder LLM (RedLLM) and compares it with decoder-only LLM (DecLLM) from the scaling perspective. The authors adapt recent modeling recipes from DecLLM to enhance RedLLM and pretrain RedLLM with the prefix LM objective. They investigate the scaling properties of RedLLM and DecLLM by comparing their pretraining and finetuning performance on a range of tasks at various model scales, from approximately 150M to 8B parameters. The results show that DecLLM presents unique strengths during pretraining, while RedLLM excels in finetuning scenarios.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a comprehensive comparison between RedLLM and DecLLM, covering a range of tasks and model scales, which adds credibility to the findings.
2. The paper is well-structured and clearly written, making it easy to follow the methodology and results.
3. The paper provides valuable insights into the scaling properties of RedLLM and DecLLM, which can inform future research in LLMs.

## Weaknesses
1. The paper only considers the T5-like structure as the encoder-decoder model, which may not be comprehensive. The encoder-decoder model can be more flexible, such as the mBART model. The paper could benefit from a more detailed discussion on the different types of encoder-decoder models and how they compare to decoder-only models.
2. The paper focuses on the scaling perspective, but it would be interesting to see how RedLLM and DecLLM compare in terms of computational efficiency and resource requirements. This would provide a more complete picture of the trade-offs between the two architectures.
3. The paper could benefit from a more detailed error analysis to understand the types of errors made by both RedLLM and DecLLM and how they differ.

## Questions
1. How do the results compare to other encoder-decoder models like mBART?
2. What are the computational efficiency and resource requirements of RedLLM and DecLLM?
3. Can you provide a more detailed error analysis of RedLLM and DecLLM?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4