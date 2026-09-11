# Review

## Summary
This paper investigates the application of Evolutionary Strategies (ES) for fine-tuning large language models (LLMs) and its impact on continual learning. The authors compare ES with the Gradient-based Policy Optimization (GRPO) algorithm, evaluating their performance, forgetting behavior, and parameter update characteristics. The study shows that while ES achieves comparable results to GRPO on several math and reasoning benchmarks, it suffers from significant catastrophic forgetting—indicating that ES may not be a viable alternative to traditional gradient-based methods for continual learning in LLMs.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
- **Comprehensive Evaluation**: The paper provides a thorough comparison between ES and GRPO across multiple benchmarks, including GSM8K, MATH, and OlympiadBench, offering a well-rounded analysis of their performance.
- **Detailed Analysis of Updates**: The study examines the characteristics of parameter updates, specifically the norm and sparsity of updates, providing insights into why ES may lead to catastrophic forgetting.

## Weaknesses
- **Limited Novelty**: The paper primarily builds on the findings of Qiu et al. (2025), with its main contribution being the addition of a catastrophic forgetting analysis. This limits the originality of the research.
- **Lack of Baseline Comparisons**: The study does not include comparisons with other relevant gradient-free optimization methods, such as CMA-ES or natural ES, which would provide a more comprehensive view of ES’s performance relative to the state-of-the-art.
- **Insufficient Analysis of Hyperparameter Sensitivity**: The paper does not explore how sensitive ES is to hyperparameter choices, such as mutation rates and population sizes, which could significantly impact its performance and forgetting behavior.
- **Narrow Focus on Continual Learning**: The study’s focus on continual learning and catastrophic forgetting is interesting, but ES has shown success in other areas, such as robustness and sample efficiency. Expanding the analysis to these aspects could provide a more balanced view of ES’s capabilities.

## Questions
1. Why did you choose to focus solely on ES and GRPO for your comparison? Including other gradient-free methods like CMA-ES or natural ES could provide a more comprehensive evaluation of ES’s performance.
2. How does the performance of ES change with different hyperparameters, such as mutation rates and population sizes? A sensitivity analysis could offer insights into the robustness of ES and its impact on catastrophic forgetting.
3. ES has been shown to be effective in areas beyond continual learning. Have you considered evaluating its performance in tasks like robustness or sample efficiency? This could help balance the focus on ES’s limitations in continual learning.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4