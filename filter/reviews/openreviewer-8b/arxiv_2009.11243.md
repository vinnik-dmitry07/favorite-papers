# Review

## Summary
This paper proposes a learned optimization algorithm that is trained to minimize validation loss on a diverse set of tasks. The authors propose to use evolutionary strategies to optimize their learned optimizer, which allows them to train for many more iterations and therefore achieve better performance. The authors demonstrate that their learned optimizer outperforms hand-designed optimizers when the hyperparameters are either not tuned at all or tuned with a simple random search. The authors also demonstrate that their learned optimizer has some ability to generalize to different architectures and datasets than it was trained on, and can even train itself.

## Soundness
3

## Presentation
4

## Contribution
4

## Strengths
- The paper is well-written and easy to follow. The authors do a good job of explaining the challenges of training learned optimizers and how they address each of these challenges.
- The paper presents a large set of experiments that demonstrate the effectiveness of the proposed method. The authors compare to hand-designed optimizers in the limit of no hyperparameter tuning, minimal hyperparameter tuning, and full hyperparameter tuning. The authors also include experiments that demonstrate that the learned optimizer has some ability to generalize to different architectures and datasets than it was trained on, and can even train itself.
- The authors demonstrate that their learned optimizer outperforms hand-designed optimizers on average when the hyperparameters are not tuned at all or when they are tuned with a simple random search. This is a significant result and suggests that learned optimizers could be a promising direction for future research.

## Weaknesses
- The proposed learned optimizer requires significantly more memory than hand-designed optimizers, as the authors note.
- The authors do not demonstrate that the proposed learned optimizer outperforms hand-designed optimizers when the hand-designed optimizers have their hyperparameters fully tuned. The authors acknowledge this limitation and suggest that a more thorough comparison of learned and hand-designed optimizers is a subject for future work. However, it is difficult to assess the significance of the current work without knowing how it compares to the best possible performance of hand-designed optimizers.
- The authors do not provide a detailed analysis of the computational cost of training the learned optimizer. They note that it takes significant compute expenditure to train the learned optimizer at the scale they consider, resulting in a nontrivial carbon footprint. However, they do not provide a detailed breakdown of the computational cost or an estimate of the carbon emissions.

## Questions
- How does the performance of the learned optimizer compare to the best possible performance of hand-designed optimizers?
- What is the detailed breakdown of the computational cost of training the learned optimizer?
- How does the performance of the learned optimizer compare to hand-designed optimizers when the hand-designed optimizers are trained with more sophisticated hyperparameter tuning methods, such as Bayesian optimization or hyperband?
- How does the performance of the learned optimizer compare to hand-designed optimizers on a wider variety of tasks and architectures, such as reinforcement learning tasks, natural language processing tasks, and graph neural network training?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4