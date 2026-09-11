# Review

## Summary
This paper introduces ASI-Arch, a system designed to autonomously discover novel neural architectures. It proposes a three-module framework: Researcher, Engineer, and Analyst, to implement an automated architecture discovery pipeline. The system conducts 1,773 experiments over 20,000 GPU hours, resulting in the discovery of 106 innovative architectures.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The automated architecture discovery pipeline is interesting.

## Weaknesses
1. The paper lacks a comparison with other neural architecture search methods, such as [1, 2], and does not provide evidence that the discovered architectures outperform those found by other methods.
2. The paper does not provide sufficient details about the architecture of the LLM used, the training data for the LLM, or the hyperparameters of the LLM.
3. The paper does not provide details on the hyperparameters used for training the discovered architectures.
4. The paper does not provide details on the hardware used to conduct the experiments.

[1] Zoph, Barret, et al. "Neural architecture search with reinforcement learning." *International conference on machine learning*. PMLR, 2018.

[2] Liu, Hanxiao, Karen Simonyan, and Yiming Yang. "Darts: Differentiable architecture search." *International conference on learning representations*. 2018.

## Questions
1. What are the architectures of the LLM used in the Researcher, Engineer, and Analyst modules?
2. What are the training data for the LLM used in the Researcher, Engineer, and Analyst modules?
3. What are the hyperparameters of the LLM used in the Researcher, Engineer, and Analyst modules?
4. What are the hyperparameters used for training the discovered architectures?
5. What are the hardware specifications used for the experiments?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4