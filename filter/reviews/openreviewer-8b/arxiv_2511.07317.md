# Review

## Summary
The paper introduces Reinforcement Learning with Adaptive Verifiable Environments (RLVE), a method that enhances LM training by using dynamically adjustable environments. RLVE creates a suite of 400 environments, called RLVE-Gym, where problems adapt to the model’s performance, avoiding the learning stall caused by static environments that are either too easy or too difficult. The authors demonstrate that RLVE improves generalization across reasoning benchmarks, outperforming traditional static approaches by 3.37%, while using only one-third of the compute resources.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The authors introduce a novel method, RLVE, which enhances LM training by using dynamically adjustable environments. 
3. The authors conduct extensive experiments to validate the effectiveness of RLVE.

## Weaknesses
1. The authors only conduct experiments on small LLMs (1.5B). It is unclear whether the proposed method can be scaled to larger models (e.g., 7B, 13B, 30B).
2. The authors only conduct experiments on reasoning tasks. It is unclear whether the proposed method can be applied to other tasks (e.g., RLAIF, code generation).
3. The authors do not provide a detailed analysis of the computational cost of the proposed method.

## Questions
1. Can the proposed method be scaled to larger models?
2. Can the proposed method be applied to other tasks (e.g., RLAIF, code generation)?
3. What is the computational cost of the proposed method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4