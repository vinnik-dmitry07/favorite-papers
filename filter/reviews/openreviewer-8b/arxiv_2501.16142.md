# Review

## Summary
This paper proposes a new model-free RL algorithm, MR.Q, which leverages model-based representations to achieve the sample efficiency and performance of model-based methods, without the computational overhead. The authors evaluate MR.Q on four widely used RL benchmarks and 118 environments, and achieve competitive performance against state-of-the-art domain-specific and general baselines without algorithmic or hyperparameter changes between environments or benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The idea of using model-based representations for model-free RL is interesting.
3. The experimental results are strong.

## Weaknesses
1. The authors claim that the proposed method can achieve the sample efficiency and performance of model-based methods. However, there is no comparison between MR.Q and any model-based methods in the experiments. It would be better to include such a comparison to support the claim.
2. The authors claim that MR.Q can be used as a general RL algorithm. However, the experiments are only conducted on four benchmarks. It would be better to include more benchmarks to support the claim.
3. The authors claim that MR.Q can achieve competitive performance against state-of-the-art domain-specific and general baselines without algorithmic or hyperparameter changes between environments or benchmarks. However, it is unclear how the hyperparameters are selected for each benchmark. It would be better to provide more details on the hyperparameter selection process and discuss the robustness of MR.Q to different hyperparameters.

## Questions
1. How does MR.Q compare to model-based methods in terms of sample efficiency and performance?
2. How does MR.Q perform on more benchmarks?
3. Can you provide more details on the hyperparameter selection process and discuss the robustness of MR.Q to different hyperparameters?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4