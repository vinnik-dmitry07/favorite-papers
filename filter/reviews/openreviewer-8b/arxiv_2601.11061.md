# Review

## Summary
The paper investigates the phenomenon of spurious rewards in Reinforcement Learning with Verifiable Rewards (RLVR) for Large Language Models (LLMs), specifically focusing on the Qwen2.5 model. The authors identify a paradox where models show improved performance on benchmarks despite training with spurious or incorrect rewards, which should not lead to genuine reasoning improvements. They hypothesize that spurious RLVR activates memorization pathways, bypassing the model's reasoning capabilities. Using mechanistic interpretability tools like Path Patching and Logit Lens, the authors uncover an "Anchor-Adapter" circuit in the model's layers, where middle layers act as a Functional Anchor for memorized answer retrieval and later layers serve as Structural Adapters to transform representations. The paper demonstrates that manipulating specific parts of this circuit can control the model's reliance on memorized solutions, providing a mechanistic understanding of spurious optimization in RLVR.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper provides a detailed mechanistic analysis of how spurious rewards in RLVR lead to memorization in LLMs, offering a deeper understanding of the underlying mechanisms.
2. The identification of the Anchor-Adapter circuit is a significant contribution, as it allows for targeted interventions to mitigate the effects of data contamination.
3. The paper demonstrates the practical applicability of its findings through causal steering experiments, showing the ability to both amplify and suppress memorization effects.

## Weaknesses
1. The paper primarily focuses on the Qwen2.5-Math model and may not be generalizable to other LLMs or tasks, limiting the broader applicability of the findings.
2. While the paper identifies the problem and proposes solutions, it could benefit from more concrete recommendations on how to prevent the activation of memorization pathways in RLVR training.
3. The paper could provide more insight into how the proposed interventions affect the model's performance on tasks that require genuine reasoning, not just on contaminated benchmarks.

## Questions
1. How do the authors suggest preventing the activation of memorization pathways during RLVR training? Are there specific strategies or modifications to the training process that could be implemented to encourage more robust reasoning?
2. Can the findings be generalized to other LLMs or tasks beyond mathematics? How might the Anchor-Adapter circuit behave differently in models used for natural language processing or other reasoning tasks?
3. How do the proposed interventions affect the model's performance on tasks that require genuine reasoning, not just on contaminated benchmarks? Is there a way to preserve the model's problem-solving abilities while mitigating the effects of memorization?
4. The paper mentions the "Perplexity Paradox," where answer-token perplexity decreases while prompt-side coherence degrades. Could the authors elaborate on why this paradox occurs and how it relates to the activation of memorization pathways?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4