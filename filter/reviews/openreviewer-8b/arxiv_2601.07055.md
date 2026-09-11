# Review

## Summary
This paper introduces Dr. Zero, a framework for self-evolving search agents that enhances the reasoning and search capabilities of language models without the need for curated QA training data. By utilizing an iterative proposer-solver training paradigm, Dr. Zero autonomously generates diverse and increasingly challenging short-form, verifiable open-domain questions without human-written questions or annotated answers. The framework employs a multi-turn tool-use pipeline and a difficulty-guided reward mechanism to produce complex, multi-hop questions and incentivize the proposer to utilize an external search engine and generate challenging yet verifiable queries. Experimental results demonstrate that Dr. Zero is competitive with supervised search agents and surpasses them on several question answering benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide clear explanations of the proposed framework, the self-evolution process, and the experimental setup. The inclusion of figures and tables also helps to illustrate the concepts and results.
2. The paper introduces a novel approach to enhancing the capabilities of search agents without the need for curated training data. The self-evolution framework and the use of an external search engine as the knowledge environment are innovative contributions to the field.
3. The paper provides a thorough evaluation of the proposed framework on multiple open-domain question answering benchmarks. The results demonstrate the effectiveness of Dr. Zero in matching or surpassing fully supervised search agents, which is a significant achievement.

## Weaknesses
1. The paper does not provide a detailed analysis of the limitations of the proposed framework. It would be beneficial to discuss any potential drawbacks or challenges that the authors encountered during the implementation or evaluation of Dr. Zero.
2. The paper does not provide a detailed analysis of the computational resources required to implement the proposed framework. It would be beneficial to discuss the computational cost of the self-evolution process and the use of the external search engine.
3. The paper does not provide a detailed analysis of the sensitivity of the proposed framework to the choice of hyperparameters. It would be beneficial to discuss how the performance of Dr. Zero is affected by different hyperparameter settings.

## Questions
1. How does the performance of Dr. Zero compare to other state-of-the-art methods for improving search agents, such as those based on supervised learning or reinforcement learning?
2. How does the proposed framework handle ambiguous or underspecified queries, and what is the impact on the performance of Dr. Zero?
3. How does the proposed framework handle queries that require specialized knowledge or domain-specific expertise, and what is the impact on the performance of Dr. Zero?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4