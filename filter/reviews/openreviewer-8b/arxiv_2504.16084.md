# Review

## Summary
This paper introduces Test-Time Reinforcement Learning (TTRL), a novel framework for training large language models (LLMs) using reinforcement learning (RL) on test data without access to ground-truth labels. The key innovation is a majority voting-based reward function that enables RL training even when only unlabeled data is available. The authors demonstrate that TTRL leads to significant performance improvements across multiple reasoning benchmarks and model types. The paper also explores the conditions under which TTRL works best and provides preliminary insights into its limitations.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel approach to RL training for LLMs on unlabeled test data, addressing a significant challenge in the field.
2. The experimental results are comprehensive and impressive, showing consistent performance improvements across different models and benchmarks.
3. The paper provides a detailed analysis of the conditions under which TTRL works, including important considerations for hyperparameters and prior knowledge.
4. The authors demonstrate that TTRL can be integrated with different RL algorithms, increasing its potential impact and versatility.

## Weaknesses
1. The paper could benefit from a more detailed comparison with existing self-supervised and semi-supervised learning approaches for reasoning tasks.
2. While the paper provides some analysis of hyperparameters and their impact, a more systematic study could be valuable.
3. The paper could explore the potential of TTRL in more complex, multi-step reasoning tasks.
4. The paper could provide more details on the computational requirements and efficiency of TTRL, especially compared to traditional RL approaches.

## Questions
1. How does TTRL compare to other self-supervised and semi-supervised learning approaches for reasoning tasks?
2. What are the key hyperparameters that affect TTRL performance, and how sensitive is the method to these choices?
3. Can TTRL be extended to more complex, multi-step reasoning tasks such as agentic workflows or scientific discovery?
4. What are the computational requirements for implementing TTRL, and how does it scale with model size and dataset size?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4