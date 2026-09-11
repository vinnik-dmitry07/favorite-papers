# Review

## Summary
This paper proposes a framework called Propose, Solve, Verify (PSV) for training LLMs in code generation through self-play, leveraging formal verification to improve the training process. The framework consists of a proposer that generates programming problems, a solver that attempts to solve these problems, and a verifier that checks the correctness of the solutions. The authors demonstrate the effectiveness of PSV by training PSV-Verus, which outperforms existing methods on three benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel approach to LLM training in code generation by utilizing formal verification to enhance the self-play framework. This is a significant contribution as it addresses the challenge of obtaining a reliable reward signal in self-play, which is a critical issue in the field.
2. The paper is well-written and easy to follow. The authors provide clear explanations of the PSV framework, the experimental setup, and the results. The figures and tables are also well-designed and help to illustrate the key points.
3. The authors conduct extensive experiments to evaluate the performance of PSV-Verus. The results show that PSV-Verus outperforms existing methods on three benchmarks, demonstrating the effectiveness of the proposed framework.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational cost of the PSV framework. It would be helpful to compare the computational resources required for PSV-Verus with those required for other methods.
2. The paper does not provide a detailed analysis of the limitations of the PSV framework. It would be helpful to discuss any potential limitations or challenges that the authors encountered during the implementation and evaluation of PSV-Verus.
3. The paper does not provide a detailed analysis of the generalizability of the PSV framework to other programming languages or domains. It would be helpful to discuss any potential challenges or modifications needed to apply PSV to other contexts.

## Questions
1. How does the computational cost of PSV-Verus compare to other methods?
2. What are the limitations of the PSV framework, and how might they be addressed in future work?
3. Can the PSV framework be generalized to other programming languages or domains, and if so, what modifications would be required?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4