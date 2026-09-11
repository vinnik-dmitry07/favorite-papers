# Review

## Summary
This paper proposes a method for solving scientific discovery problems using LLMs. The method, Test-Time Training to Discover (TTT-Discover), combines reinforcement learning (RL) with evolutionary search to improve LLM performance on individual test problems. TTT-Discover trains the LLM on the specific test problem, using experience gathered during test-time search to refine its responses. The approach is evaluated across diverse tasks, including mathematics, kernel engineering, algorithm design, and biology, where it reportedly achieves state-of-the-art results.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper presents a novel approach to test-time training by integrating RL with LLMs for scientific discovery, focusing on individual problem-solving rather than generalization.
- The method is thoroughly evaluated across multiple domains, demonstrating its versatility and effectiveness.
- The paper is well-structured, with clear explanations and detailed descriptions of the methodology and results.

## Weaknesses
- The method is limited to problems with continuous rewards, which restricts its applicability to a narrower range of tasks.
- The approach is computationally expensive, requiring significant resources for training and evaluation.
- The paper lacks a detailed comparison with other state-of-the-art methods, particularly in terms of computational efficiency and practical applicability.

## Questions
- How does TTT-Discover compare to other recent approaches in terms of computational efficiency and cost-effectiveness?
- Could the method be adapted for tasks with sparse or binary rewards, which are common in many scientific discovery problems?
- What specific challenges were encountered in applying TTT-Discover to different domains, and how were they addressed?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4