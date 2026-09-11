# Review

## Summary
This paper investigates the phenomenon of "grokking" in small transformers trained on modular addition tasks. The authors reverse engineer the algorithm learned by these networks, which uses discrete Fourier transforms and trigonometric identities to convert addition to rotation about a circle. They define progress measures that allow us to study the dynamics of training and split training into three continuous phases: memorization, circuit formation, and cleanup.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a detailed analysis of the algorithm learned by small transformers on modular addition tasks, using various techniques such as Fourier transforms and trigonometric identities.
2. The paper identifies three continuous phases of training: memorization, circuit formation, and cleanup, which contribute to the understanding of the training dynamics.
3. The paper proposes progress measures that allow for a more nuanced understanding of the training process and the emergence of grokking behavior.

## Weaknesses
1. The analysis is focused on a specific task (modular addition) and a specific architecture (one-layer transformer), which may limit the generalizability of the findings.
2. The paper lacks a detailed comparison with other approaches to understanding emergence in neural networks, such as the slingshot mechanism proposed by Thilak et al. (2022).
3. The paper does not provide a clear explanation for why the sudden transition to perfect test accuracy occurs during the cleanup phase, and more work is needed to understand this aspect of the phenomenon.

## Questions
1. Can the findings of this paper be generalized to other tasks and architectures beyond modular addition and one-layer transformers?
2. How does the proposed approach to understanding emergence in neural networks compare to other existing approaches, such as the slingshot mechanism?
3. What is the significance of the sudden transition to perfect test accuracy during the cleanup phase, and what mechanisms drive this phenomenon?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4