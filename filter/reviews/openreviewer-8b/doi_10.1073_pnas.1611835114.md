# Review

## Summary
The paper proposes a method to avoid catastrophic forgetting in neural networks by penalizing the change of parameters that are important for previously learned tasks. The method is validated on a set of classification tasks based on the MNIST dataset and on several Atari 2600 games.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well written and the method is well motivated. The method is evaluated on a wide range of tasks and compared to a reasonable baseline (dropout). The method seems to be effective at avoiding catastrophic forgetting.

## Weaknesses
The method is not compared to other methods that have been proposed to avoid catastrophic forgetting. It would be interesting to see how it compares to e.g. PackNet (https://arxiv.org/abs/1609.06490) or more recent methods.

The method is only evaluated on a set of relatively simple tasks. It would be interesting to see how it performs on more complex tasks, such as ImageNet ILSVRC-2012 (https://www.image.net/).

## Questions
How does the method compare to other methods that have been proposed to avoid catastrophic forgetting?

How does the method perform on more complex tasks, such as ImageNet ILSVRC-2012?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4