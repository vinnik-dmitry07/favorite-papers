# Review

## Summary
The paper presents rStar-Math, a self-evolutionary approach for enhancing small language models' (SLMs) mathematical reasoning capabilities to rival or surpass larger models like OpenAI o1. rStar-Math uses a combination of Monte Carlo Tree Search (MCTS) and a self-improving framework to iteratively refine both the policy model and a process preference model (PPM). The approach introduces a novel code-augmented method for generating high-quality training data and a new training method for the PPM. After four rounds of self-evolution, rStar-Math achieves state-of-the-art performance on multiple math benchmarks, including the MATH dataset and the USA Math Olympiad (AIME) problems.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The paper introduces a novel self-evolution framework that leverages smaller language models (SLMs) to generate high-quality training data through Monte Carlo Tree Search (MCTS).
3. The paper presents a new method for training process preference models (PPMs) without requiring precise step-level reward annotations.
4. The paper demonstrates that rStar-Math achieves state-of-the-art performance on multiple math reasoning tasks, including the MATH dataset and the USA Math Olympiad (AIME) problems, using SLMs as small as 1.5B parameters.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational resources required for the self-evolution process, including the number of GPUs used, the number of hours per round, and the total cost.
2. The paper does not provide a detailed analysis of the limitations of the proposed approach, such as the potential for overfitting to the training data or the sensitivity to the hyperparameters of the MCTS algorithm.

## Questions
1. Can you provide more details on the computational resources required for each round of self-evolution? How many GPUs were used, for how many hours per round, and what was the total cost for each round?
2. How do you ensure that the generated training data is diverse and representative of the target math reasoning tasks?
3. How do you handle cases where the generated solutions are incorrect or of poor quality? Is there a mechanism for detecting and filtering out such cases?
4. How do you determine the optimal number of rounds for the self-evolution process? Is there a risk of overfitting after a certain number of rounds?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4