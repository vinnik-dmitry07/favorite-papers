# Review

## Summary
This paper proposes using the stable rank of the final layer hidden states as a proxy for response quality in LLMs. The authors demonstrate that the stable rank can effectively distinguish between good and bad responses, and can be used as a reward signal in RLHF to improve the model's performance on STEM and mathematical reasoning tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The idea of using the stable rank of the final layer hidden states as a proxy for response quality is novel and interesting.
- The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.

## Weaknesses
- The correlation analysis in Section 5 is not very convincing. The authors use a sample-level Pearson correlation to show that stable rank is correlated with various text metrics. However, since the stable rank is computed based on the final layer hidden states, it is likely that the text metrics that are based on the final generated text (e.g., lexical diversity) are correlated with the stable rank. It would be more convincing if the authors could show that the hidden states of the model that generate more diverse texts also have a higher stable rank.
- The authors only use the stable rank of the final layer hidden states as a proxy for response quality. However, it is possible that the stable rank of the hidden states of earlier layers can also provide quality signals. It would be interesting to investigate this and see if using the stable rank of multiple layers can further improve the performance.
- The authors only use the stable rank as a proxy for response quality. It would be interesting to explore whether the stable rank can also be used as a reward during the decoding process, similar to how the perplexity is used in many RLHF methods.

## Questions
- Can you provide more details on how the baseline methods are implemented? For example, what prompts are used for pointwise scoring and pairwise comparison? How are the "Yes" and "No" tokens selected for IPO?
- Have you tried using the stable rank of earlier layers as a proxy for response quality? Does it perform worse than using the final layer?
- Have you tried using the stable rank as a reward during the decoding process?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4