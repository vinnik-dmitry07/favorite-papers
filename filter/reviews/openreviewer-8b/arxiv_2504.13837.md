# Review

## Summary
This paper investigates the impact of Reinforcement Learning with Verifiable Rewards (RLVR) on the reasoning capabilities of large language models (LLMs). The study focuses on whether RLVR enables LLMs to develop new reasoning abilities or simply leverage existing reasoning patterns in the base model. Using the pass@k metric, which measures the proportion of problems a model can solve within k trials, the authors compare the performance of base models with their RLVR-trained counterparts across various benchmarks, including mathematics, code generation, and visual reasoning.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper provides a thorough evaluation across multiple benchmarks and model sizes, revealing consistent trends in the performance of RLVR models.
2. The use of the pass@k metric allows for a more robust assessment of the models' reasoning boundaries, offering insights into the limitations of RLVR.
3. The authors conduct detailed analyses, including accuracy distribution, solvable-problem coverage, and perplexity, to understand the effects of RLVR training.

## Weaknesses
1. The paper does not explore the impact of different RL algorithms on the performance of LLMs, which could provide insights into the effectiveness of various approaches.
2. The study does not investigate the potential of RLVR to improve reasoning capabilities over longer chains of reasoning, which is critical for complex problem-solving.
3. The paper does not consider the role of RLVR in developing general-purpose models versus task-specific models, which could affect the generalizability of the findings.

## Questions
1. How does the choice of the RL algorithm impact the reasoning capabilities of LLMs in the context of RLVR?
2. Can RLVR improve the reasoning abilities of LLMs over longer chains of reasoning, and if so, how does this compare to the base model?
3. How do RLVR-trained models compare to models trained with other advanced techniques, such as distillation or few-shot learning, in terms of reasoning capabilities?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4