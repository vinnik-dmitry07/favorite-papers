# Review

## Summary
This paper introduces Dynamic Fine-Tuning (DFT), a method to improve the generalization of Supervised Fine-Tuning (SFT) for Large Language Models (LLMs). The authors identify that standard SFT gradients are limited in generalization due to an implicitly defined, sparse reward structure. DFT addresses this by dynamically rescaling the SFT objective with token probabilities, stabilizing gradients and enhancing generalization. The method shows significant improvements over SFT on challenging benchmarks, including math reasoning and code generation tasks, and demonstrates competitive performance in offline reinforcement learning (RL) settings.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-structured, with a clear presentation of the problem, methodology, and experimental results.
2. The proposed DFT method is theoretically well-motivated, with a clear mathematical connection to RL.
3. The method is simple to implement and requires only a single-line change to the SFT objective.
4. DFT demonstrates consistent improvements over SFT across multiple benchmarks and model types, including math reasoning, code generation, and multi-modal tasks.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational overhead of DFT compared to SFT.
2. The method may be sensitive to the model's initial uncertainty estimates, potentially leading to instability in certain cases.
3. DFT may not be suitable for tasks that require the acquisition of new factual knowledge, as it may reinforce the model's existing beliefs.

## Questions
1. Can you provide more insights into the computational overhead of DFT compared to SFT? How does the dynamic reweighting process affect training time and resource requirements?
2. How does the initial uncertainty estimation affect the performance of DFT? Are there any techniques to mitigate potential instability?
3. Can DFT be combined with other techniques, such as data augmentation or curriculum learning, to further enhance generalization?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4