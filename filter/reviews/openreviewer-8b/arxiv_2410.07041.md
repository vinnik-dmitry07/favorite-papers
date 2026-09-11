# Review

## Summary
This paper studies the effect of repeating training examples in transformer models. The authors show that for a fixed training budget, models trained on a small data budget (but with high repetition) outperform models trained on a large data budget without repetition. They also introduce a two-set training approach, where a subset of the training examples are repeated more often than others. This approach leads to faster learning and better performance, as long as the repeated examples are mixed with the non-repeated ones in the same mini-batches. The authors conduct experiments on three algorithmically generated datasets: greatest common divisor, modular multiplication, and matrix eigenvalues.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The authors provide a thorough analysis of the effect of repetition in transformer models, challenging the common belief that more diverse data is always better.
- The two-set training approach is innovative and shows promising results in terms of learning speed and performance.

## Weaknesses
- The experiments are conducted on algorithmically generated datasets, which may not fully represent the characteristics of natural language data. It would be interesting to see how the findings translate to more complex tasks or real-world datasets.
- The paper could benefit from a more detailed analysis of the model's memorization of repeated examples. For instance, it would be interesting to see if the model can recall previous occurrences of the repeated examples and how it integrates this information during training.

## Questions
- Have you considered the potential impact of the ordering of the examples in the training set? How might the performance be affected if the repeated examples are spread throughout the training set rather than clustered together?
- How do you explain the fact that the model can still learn even when the training set is composed of a large number of unique examples that are each seen only once or a small number of times?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4