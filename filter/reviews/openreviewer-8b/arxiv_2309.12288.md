# Review

## Summary
This paper shows that LLMs trained on sentences of the form "A is B" fail to generalize to the reverse direction "B is A". The authors provide evidence for the Reversal Curse by finetuning GPT-3 and Llama-1 on fictitious statements and evaluating their ability to answer questions in the reverse direction. The Reversal Curse is robust across model sizes and model families and is not alleviated by data augmentation. The authors also evaluate ChatGPT on questions about real-world celebrities and find that it correctly answers questions in the forward direction 79% of the time, but only 33% of the time in the reverse direction. The authors argue that this demonstrates a basic failure of logical deduction in the LLM's training process and a failure of meta-learning. They suggest that the Reversal Curse is a consequence of the myopic nature of the gradient update when training on "A is B", which may not take into account the need to predict "B is A" in the future.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper identifies a fundamental limitation of LLMs in generalizing from sentences of the form "A is B" to their reverse direction "B is A", which has important implications for the capabilities of these models.
2. The authors provide evidence for the Reversal Curse through a series of experiments on both synthetic and real-world data, using different model sizes and families. The robustness of the results across different settings strengthens the validity of the findings.
3. The paper is well-written and clearly explains the concept of the Reversal Curse, the experimental setup, and the results. The authors also provide a discussion of the potential reasons behind the Reversal Curse and propose future research directions.

## Weaknesses
1. The paper only considers sentences of the form "A is B" and their reverse direction "B is A". It would be interesting to see if the Reversal Curse generalizes to other types of sentences with different grammatical structures and logical relationships.
2. The authors only consider LLMs such as GPT-3 and Llama-1. It would be valuable to investigate if the Reversal Curse exists in other types of language models or if it is a specific failure mode of auto-regressive models.
3. The paper does not provide a comprehensive explanation for the Reversal Curse. While the authors propose some hypotheses, a more in-depth analysis of the underlying mechanisms causing this phenomenon would be beneficial.

## Questions
1. Have you tried any other types of sentences beyond "A is B" and "B is A"? Do you expect the Reversal Curse to generalize to other sentence structures?
2. Have you tried any other types of language models beyond GPT-3 and Llama-1? Do you expect the Reversal Curse to exist in other models?
3. Can you provide any insights into the underlying mechanisms causing the Reversal Curse? Why do you think LLMs fail to generalize in this way?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4