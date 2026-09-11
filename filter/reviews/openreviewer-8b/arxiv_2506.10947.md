# Review

## Summary
This paper investigates the effect of various types of rewards in RLVR. It shows that RLVR can improve model performance even with spurious or random rewards, and that the effectiveness of different rewards varies across model families. The authors hypothesize that the clipping function in GRPO amplifies high-prior behaviors learned during pre-training, and they identify "code reasoning" as a pre-existing behavior in Qwen models that contributes to their success in math reasoning tasks. The paper emphasizes the importance of validating RL methods across diverse models rather than relying on a single model family.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper provides a novel insight into the effectiveness of RLVR with spurious rewards, challenging the assumption that accurate supervision is necessary for effective training.
- The authors conduct a thorough analysis of different reward types and their impact on various model families, providing valuable insights into the relationship between pre-training and RLVR.
- The identification of "code reasoning" as a pre-existing behavior in Qwen models and its contribution to their success is a significant finding.
- The paper emphasizes the importance of validating RL methods across multiple models and families, which is crucial for the field.

## Weaknesses
- The authors only focus on math reasoning tasks, and it is unclear whether the findings would generalize to other types of tasks.
- The paper does not provide a detailed analysis of why certain models are more susceptible to the influence of spurious rewards, which could provide further insights into the underlying mechanisms.

## Questions
- Have you tested whether the findings generalize to other types of reasoning tasks beyond math?
- Can you provide more insights into why certain models are more susceptible to the influence of spurious rewards?
- How do you think the findings in this paper can help future research in RLVR?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4