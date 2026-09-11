# Review

## Summary
This paper presents the performance of OpenAI's o1, o1-ioi, and o3 models on competitive programming tasks. The key findings are that (1) o1-ioi, with hand-crafted test-time strategies, achieved a gold medal at IOI 2024, and (2) o3 achieves a gold medal without these strategies. The authors also demonstrate that increasing RL training compute and test-time compute improves performance, and that o3 outperforms o1 and o1-ioi on the Codeforces and SWE-bench/verified benchmarks.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
- The paper presents strong empirical results, showing that o1-ioi achieved a gold medal at IOI 2024 and that o3 achieves a gold medal without hand-crafted strategies.
- The paper demonstrates that increasing RL training compute and test-time compute improves performance.
- The paper shows that o3 outperforms o1 and o1-ioi on the Codeforces and SWE-bench/verified benchmarks.
- The paper provides a detailed analysis of the test-time strategies employed by o1-ioi and o3, including the clustering and reranking approach used by o1-ioi and the brute-force solutions written by o3.
- The paper provides a detailed analysis of the performance of o1, o1-ioi, and o3 on different types of problems, including algorithmic problems, data structures problems, and object-oriented programming problems.

## Weaknesses
- The paper does not provide a detailed analysis of the limitations of the models or potential areas for improvement.
- The paper does not provide a detailed analysis of the computational resources required to achieve these results, such as the number of GPU hours used for RL training or the number of API calls made during test-time compute. This makes it difficult to reproduce the results or estimate the cost of achieving these results.
- The paper does not provide a detailed analysis of the impact of different hyperparameters or training settings on the performance of the models.
- The paper does not provide a detailed analysis of the interpretability of the models' solutions or the reasoning behind their decisions.

## Questions
- What are the limitations of the models, and what are potential areas for improvement?
- What are the computational resources required to achieve these results, such as the number of GPU hours used for RL training or the number of API calls made during test-time compute?
- How do different hyperparameters or training settings impact the performance of the models?
- Can you provide more insight into the interpretability of the models' solutions and the reasoning behind their decisions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4