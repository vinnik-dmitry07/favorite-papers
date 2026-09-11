# Review

## Summary
The paper proposes a meta-learning approach to continual learning. The idea is to train a model that can learn tasks sequentially and keep learning new tasks without forgetting previous ones. The authors propose to use a self-referential weight matrix (SRWM) to modify the weights of the model as it learns new tasks. The SRWM is a weight matrix that updates itself as it learns new tasks. The authors also propose a new loss function that encourages the model to learn new tasks while retaining performance on previous tasks. The authors evaluate their approach on the Split-MNIST benchmark and show that their approach outperforms existing methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper proposes a novel approach to continual learning that uses meta-learning and self-referential weight matrices.
- The paper is well-written and easy to follow.
- The paper provides a thorough review of the literature and compares the proposed approach to existing methods.

## Weaknesses
- The paper only evaluates the proposed approach on the Split-MNIST benchmark. It would be interesting to see how the approach performs on other benchmarks, such as the Split-CIFAR100 or the 5-datasets benchmark.
- The paper does not provide any analysis of the learned models. It would be interesting to see how the self-referential weight matrices change as the model learns new tasks.

## Questions
- Can you provide more details on the self-referential weight matrices? How do they work and how do they help the model learn new tasks without forgetting previous ones?
- Can you provide more details on the loss function? How does it encourage the model to learn new tasks while retaining performance on previous tasks?
- Can you provide more details on the evaluation protocol? How many epochs are the models trained for and how are the tasks ordered?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4