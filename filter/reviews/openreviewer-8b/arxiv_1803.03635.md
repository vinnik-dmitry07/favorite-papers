# Review

## Summary
The paper proposes the Lottery Ticket Hypothesis (LTH), which states that large neural networks contain smaller subnetworks that can match the performance of the original network when trained in isolation. The authors provide empirical evidence for LTH by pruning a large network and showing that the pruned network can be trained as fast and to the same accuracy as the original network. The authors also show that if the pruned network is reinitialized, it cannot match the performance of the original network, indicating the importance of the initial weights of the subnetwork. The authors conduct experiments on MNIST and CIFAR10 using fully-connected and convolutional architectures. They find that the winning tickets are 10-20% of the size of the original network and can learn faster and reach higher test accuracy than the original network. The authors also discuss the implications of LTH for improving training performance, designing better networks, and improving theoretical understanding of neural networks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper proposes a novel and interesting hypothesis that challenges the conventional view of neural network compression. The paper is well-written and easy to follow. The authors provide a clear definition of LTH and provide empirical evidence to support the hypothesis.
- The authors conduct extensive experiments on different architectures and datasets to support LTH. The authors also explore the implications of LTH for improving training performance, designing better networks, and improving theoretical understanding of neural networks.
- The paper has the potential to inspire further research on LTH and its applications. The paper can also lead to the development of new network compression techniques that can find winning tickets more efficiently.

## Weaknesses
- The paper only considers vision-centric classification tasks on smaller datasets (MNIST, CIFAR10). It would be interesting to see if LTH holds for larger datasets and other tasks such as object detection or segmentation.
- The paper only considers sparse pruning as a way to find winning tickets. It would be interesting to see if other pruning techniques such as structured pruning or non-magnitude pruning can also find winning tickets.
- The paper does not provide a clear explanation of why LTH holds. It would be interesting to see if the authors can provide some theoretical analysis or insights on why LTH holds.

## Questions
- Have you tried other pruning techniques such as structured pruning or non-magnitude pruning to find winning tickets? If so, what were the results?
- Have you tried to train the winning tickets found by sparse pruning on larger datasets or other tasks such as object detection or segmentation? What were the results?
- Can you provide some theoretical analysis or insights on why LTH holds? For example, is it related to the overparameterization of neural networks or the optimization algorithm used?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4