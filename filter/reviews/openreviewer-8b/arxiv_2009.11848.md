# Review

## Summary
This paper studies the extrapolation ability of neural networks, especially ReLU MLPs and GNNs. The authors show that ReLU MLPs trained by GD converge to linear functions along directions from the origin. They also show that ReLU MLPs can extrapolate well in linear tasks, and provide a hypothesis that a neural network can extrapolate well when appropriate non-linearities are encoded into the architecture and features. This hypothesis is proved for a simplified case and empirical results are provided for more general settings.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The authors provide a detailed analysis of the extrapolation ability of ReLU MLPs and GNNs, which can help to understand the behavior of these models in practical applications.
2. The authors provide a hypothesis on the conditions for a neural network to extrapolate well, and provide both theoretical and empirical evidence to support the hypothesis.

## Weaknesses
1. The theoretical analysis is limited to ReLU MLPs and GNNs, and it is not clear how the results can be generalized to other types of neural networks.
2. The authors only consider the squared loss in their analysis, and it is not clear how the results will be affected by other types of loss functions.
3. The authors do not provide any suggestions or guidelines on how to design neural networks for extrapolation tasks.

## Questions
1. Can the theoretical analysis be generalized to other types of neural networks, such as convolutional neural networks or recurrent neural networks?
2. How will the results be affected by other types of loss functions, such as the cross-entropy loss or the MAE loss?
3. Can you provide some suggestions or guidelines on how to design neural networks for extrapolation tasks, based on the analysis and hypothesis presented in this paper?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4