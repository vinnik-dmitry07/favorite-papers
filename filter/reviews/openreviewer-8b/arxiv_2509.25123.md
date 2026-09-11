# Review

## Summary
This paper investigates whether LLMs genuinely learn new skills through RL or merely re-weight existing skills. The authors develop a synthetic framework to isolate skill acquisition, defining a skill as the ability to infer the output of a string transformation function. They demonstrate that RL enables LLMs to learn unseen compositions of functions they had already learned before RL training. This compositional ability generalizes to more complex problems and transfers to different tasks, provided the model has acquired the necessary atomic skills beforehand. The study provides evidence that RL fundamentally changes model reasoning behaviors, an effect not observed in standard next-token prediction training.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow.
- The paper addresses a highly relevant and interesting question in the field of LLMs.
- The paper introduces a novel synthetic framework to investigate skill acquisition in LLMs.
- The paper provides evidence that RL can teach LLMs new skills by composing existing ones.

## Weaknesses
- The paper's reliance on synthetic tasks may limit the generalizability of the findings to real-world applications.
- The paper does not provide a clear definition of what constitutes a "new skill" in the context of LLMs.
- The paper does not adequately address the potential for RL to learn new skills in the context of continual learning, where LLMs may need to acquire new skills over time.

## Questions
- How do the authors define a "new skill" in the context of LLMs, and how can we distinguish between the activation of existing skills and the acquisition of new skills?
- How can we ensure that the synthetic tasks used in the study adequately represent the complexity of real-world tasks that LLMs encounter?
- How does the proposed synthetic framework account for the continual learning scenario, where LLMs may need to acquire new skills over time?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4