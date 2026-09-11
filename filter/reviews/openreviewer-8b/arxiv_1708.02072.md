# Review

## Summary
This paper provides a benchmark for evaluating methods to mitigate catastrophic forgetting in neural networks. The authors evaluate 5 different methods for mitigating catastrophic forgetting on 3 different datasets, and introduce new metrics to evaluate the ability of a model to learn new tasks while retaining performance on previous tasks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The problem of catastrophic forgetting is an important one, and there is currently no good benchmark for evaluating methods to mitigate it
- The authors evaluate a diverse set of methods
- The authors use multiple datasets, including an audio dataset, which is often neglected in these types of studies

## Weaknesses
- The authors do not compare to the simple baseline of training a new model on the new data, without any mitigation method. This baseline should be included, as it is the one option that is guaranteed to perform well (assuming that the model has sufficient capacity)
- The datasets used are all classification tasks, and all have the same general structure (input -> FC -> output). It would be good to include other types of tasks, such as regression, and also some tasks where the input and output are not images. The authors do include an audio dataset, which is a good start, but it is still similar to image data in many ways.
- It would be good to include some more recent methods, such as L2P [1] and REMIND [2]

[1] Kirkpatrick, James, et al. "Overcoming catastrophic forgetting in neural networks." Proceedings of the national academy of sciences 114.13 (2017): 3521-3526.

[2] Hayes, Tyler L., et al. "Remind your neural network to prevent catastrophic forgetting." European conference on computer vision. Springer, Cham, 2018.

## Questions
- Why not include a baseline of training a new model on the new data?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4