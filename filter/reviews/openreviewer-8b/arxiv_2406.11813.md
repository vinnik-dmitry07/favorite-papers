# Review

## Summary
This paper studies how LLMs acquire factual knowledge during pretraining. The authors propose methods, datasets, and metrics to analyze the dynamics of factual knowledge acquisition during LLM pretraining. The authors demonstrate that factual knowledge acquisition in LLM pretraining is achieved through accumulating micro-acquisitions, each of which occurs whenever the model is updated after seeing the factual knowledge. When the model is not presented with factual knowledge, forgetting occurs and the acquisition of the knowledge is gradually diluted. The authors also find that there is a power-law relationship between training steps and forgetting of acquired factual knowledge, in terms of both memorization and generalization. Also, pretraining LLMs with deduplicated data and larger batch sizes enhances the acquisition of factual knowledge, making them more robust against forgetting the learned factual knowledge. The authors provide potential explanations for recently observed, yet underexplored behaviors of LLMs.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide a clear motivation and a detailed explanation of the proposed methods, datasets, and metrics. The authors also provide a clear summary of the experimental results and a detailed discussion of the implications.

2. The paper provides a comprehensive analysis of how LLMs acquire factual knowledge during pretraining. The authors conduct experiments with different model sizes, pretraining stages, and training batch sizes. The authors also investigate different knowledge injection scenarios, including duplication, paraphrase, and once. The authors also provide a detailed analysis of the forgetting phenomenon of acquired factual knowledge.

3. The paper provides potential explanations for recently observed, yet underexplored behaviors of LLMs. The authors propose that the improved performance of LLMs through data scaling results from consistent improvements rather than an emergent ability to acquire factual knowledge more quickly during pretraining. The authors also hypothesize that LLMs struggle to acquire unpopular knowledge because they need sufficient exposure to factual knowledge with intervals shorter than the learnability threshold to increase the probability. Third, the authors' findings suggest that deduplicating the pretraining corpus improves LLM performance by preventing the model from assigning a higher probability to duplicated sequences and helping it retain acquired generalization longer.

## Weaknesses
1. The paper only studies one LLM, OLMo. It would be better to conduct experiments with more LLMs, such as LLAMA, to see if the findings are consistent with OLMo.

2. The paper only studies one pretraining dataset, Dolma v1.5. It would be better to conduct experiments with more pretraining datasets, such as CommonCrawl, to see if the findings are consistent with Dolma v1.5.

3. The paper only studies one evaluation dataset, the Fictional Knowledge dataset. It would be better to conduct experiments with more evaluation datasets, such as Nell-995, to see if the findings are consistent with the Fictional Knowledge dataset.

## Questions
1. Have you conducted experiments with more LLMs, such as LLAMA, to see if the findings are consistent with OLMo?

2. Have you conducted experiments with more pretraining datasets, such as CommonCrawl, to see if the findings are consistent with Dolma v1.5?

3. Have you conducted experiments with more evaluation datasets, such as Nell-995, to see if the findings are consistent with the Fictional Knowledge dataset?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4