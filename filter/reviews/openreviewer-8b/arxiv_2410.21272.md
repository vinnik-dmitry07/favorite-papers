# Review

## Summary
The paper investigates how LLMs perform arithmetic operations, questioning whether they learn robust algorithms or merely memorize training data. Through circuit analysis, the authors identify a subset of model components crucial for arithmetic tasks and examine their behavior at the neuron level. They find that a small subset of neurons implements a set of simple heuristics that, when combined, enable the model to produce correct answers. The study shows that this heuristic-based mechanism is the primary means by which LLMs perform arithmetic, even in early training stages, suggesting that memorization and algorithmic understanding lie somewhere in between these heuristics.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper provides a novel and detailed view into the inner workings of LLMs for arithmetic tasks, focusing on heuristic-based computation rather than traditional algorithmic or memorization models. The methodology is rigorous, using causal analysis and neuron-level examination to identify and validate the heuristic types within the model. This work has implications for the broader understanding of LLM capabilities and limitations, especially in arithmetic tasks, and suggests directions for improving model training and architecture.

## Weaknesses
The analysis is focused on specific LLMs and arithmetic tasks, which may limit the generalizability of the findings. The heuristic types identified may be human-imposed abstractions, potentially limiting the understanding of true model mechanisms. Additionally, the study does not explore in depth how these heuristics interact with other model components or how they might be influenced by external factors like input representation or context.

## Questions
1. How do the identified heuristics interact with other model components outside the identified circuit?
2. Could the authors elaborate on how the findings might generalize to other types of reasoning tasks beyond arithmetic?
3. What impact might the tokenization approach have on the identified heuristics, and would different tokenization strategies lead to different conclusions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4