# Review

## Summary
This paper introduces a curriculum learning approach for training LLMs to improve their reasoning abilities. The authors propose a method called E2H Reasoner, which gradually schedules tasks from easy to hard to help LLMs build reasoning skills progressively. The paper provides both empirical results and theoretical analysis to demonstrate the effectiveness of the proposed method.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive theoretical analysis of their method, including convergence guarantees and finite-sample complexity bounds.
3. The empirical results show that the E2H Reasoner outperforms several baselines on multiple reasoning tasks.

## Weaknesses
1. The paper does not compare with some important baselines, such as the one that uses a fixed curriculum learning schedule (e.g., always start with easy tasks and switch to hard tasks after a fixed number of iterations).
2. The E2H Reasoner requires careful tuning of hyperparameters (e.g., the hyperparameters for the Gaussian scheduler).
3. The E2H Reasoner relies on accurate difficulty estimation for the tasks, which may not always be available.

## Questions
1. How does the E2H Reasoner compare to other adaptive curriculum learning methods, such as the one proposed by [1]?
2. How robust is the E2H Reasoner to the choice of hyperparameters, especially for the Gaussian scheduler? How do you choose the hyperparameters in practice?
3. How does the E2H Reasoner perform when the difficulty estimation is noisy or inaccurate?
4. How does the E2H Reasoner compare to other state-of-the-art methods for improving LLM reasoning, such as [2]?

[1] Chen, Xinyue, et al. "Self-evolve: Adaptive curriculum learning for large language model reasoning." Advances in Neural Information Processing Systems 37 (2024).

[2] Zeng, Andy, et al. "Beyond human data: Scaling self-imitation with model-guided curriculum for language model reasoning." arXiv preprint arXiv:2407.02485 (2024).

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4