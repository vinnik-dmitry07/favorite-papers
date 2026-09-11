# Review

## Summary
This paper studies the performance of off-policy and batch RL algorithms in the batch setting. It is shown that these algorithms perform poorly in the batch setting, and a discrete version of BCQ is proposed and shown to outperform the other algorithms.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
The paper is well-written and easy to follow. The experiments are clearly explained.

## Weaknesses
The paper is a bit incremental, and the contribution is a bit limited. The conclusion that off-policy algorithms perform poorly in the batch setting is not new. The proposed discrete BCQ is a straightforward extension of the original BCQ.

## Questions
- The experiments are based on a single seed, and the performance of KL-Control seems very unstable. It would be more convincing if the experiments can be repeated with multiple random seeds and some statistical analysis can be provided.
- The proposed discrete BCQ is very similar to the original BCQ. It would be helpful to provide some analysis on how the performance of the original BCQ and discrete BCQ depends on the perturbation magnitude in the original BCQ.
- The proposed discrete BCQ is only compared with the other algorithms on the Atari benchmark. It would be helpful to evaluate the algorithm on other benchmarks as well.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4