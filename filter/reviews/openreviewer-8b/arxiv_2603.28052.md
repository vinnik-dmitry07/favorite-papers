# Review

## Summary
The paper introduces Meta-Harness, a system for optimizing the "harness" code that surrounds and influences the behavior of large language models (LLMs). The authors argue that the performance of LLMs is not solely dependent on model weights, but also on the code that determines what information to retrieve, store, and present to the model. Meta-Harness uses a coding agent that has access to the file system, allowing it to inspect and learn from prior code and execution traces. The system is evaluated on three tasks: online text classification, retrieval-augmented math reasoning, and agentic coding. The results show that Meta-Harness outperforms existing methods and even surpasses hand-engineered baselines.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper presents a novel approach to optimizing the code that influences LLM behavior, going beyond traditional model optimization.
2. The use of a coding agent with access to the file system allows for a more nuanced and effective learning process.
3. The system is evaluated on three different tasks, demonstrating its versatility and effectiveness.

## Weaknesses
1. The paper could benefit from a more detailed comparison with existing methods, particularly in terms of computational efficiency.
2. The reliance on a coding agent with access to the file system may not be feasible or practical in all settings.
3. The evaluation could be more comprehensive, especially in terms of comparing the proposed method with other state-of-the-art approaches.

## Questions
1. How does Meta-Harness compare to other state-of-the-art methods for optimizing LLMs in terms of computational efficiency and resource requirements?
2. Can the approach be adapted to work with LLMs that do not have a coding agent available or that have limited file system access?
3. How generalizable is the approach across different types of tasks and domains, and what are the limitations of its applicability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4