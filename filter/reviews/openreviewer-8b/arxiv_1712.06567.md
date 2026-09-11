# Review

## Summary
This paper presents a study of the performance of a simple genetic algorithm for training deep neural networks for reinforcement learning. The authors compare the performance of the genetic algorithm with that of contemporary algorithms applied to deep RL, such as DQN, A3C, and ES. The authors show that the genetic algorithm performs competitively with these methods, and in some cases even outperforms them. The paper also introduces a novel method for encoding large neural network parameter vectors compactly, which enables efficient distributed training.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper presents a novel approach to training deep neural networks for reinforcement learning using a simple genetic algorithm. This approach is different from the more common gradient-based methods, and it is interesting to see that it performs competitively with these methods.

The paper is well-written and easy to follow. The authors do a good job of explaining the genetic algorithm and the experimental setup. The results are presented in a clear and concise manner.

The paper presents a novel method for encoding large neural network parameter vectors compactly, which enables efficient distributed training. This is a significant contribution, as it allows for more flexible and scalable training of deep neural networks.

The authors show that the genetic algorithm performs competitively with contemporary algorithms applied to deep RL, such as DQN, A3C, and ES. In some cases, the genetic algorithm even outperforms these methods.

## Weaknesses
The paper only considers a simple genetic algorithm without any additional enhancements. It would be interesting to see how more advanced genetic algorithms, such as those with crossover operations, perform in comparison to the simple genetic algorithm.

The paper does not provide a theoretical analysis of the genetic algorithm or a comparison of its convergence properties to other methods. A better understanding of the underlying principles of the genetic algorithm and its behavior would be beneficial.

The paper only considers a limited number of environments. It would be interesting to see how the genetic algorithm performs on a wider range of tasks, including more complex ones.

## Questions
How does the performance of the genetic algorithm compare to more advanced genetic algorithms with crossover operations?

What are the convergence properties of the genetic algorithm, and how do they compare to other methods?

How does the genetic algorithm perform on a wider range of tasks, including more complex ones?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4