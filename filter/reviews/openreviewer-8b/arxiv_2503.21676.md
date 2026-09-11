# Review

## Summary
The paper investigates the learning dynamics of language models using a synthetic factual recall task. The authors find that language models learn in three phases: first, they learn overall distribution statistics, then enter a plateau phase, and finally, acquire individual-specific knowledge. The plateau phase is hypothesized to be due to the formation of attention-based circuits, which can be demonstrated through an attention patching technique. The paper also explores how data distribution properties affect learning dynamics, finding that imbalanced distributions can both accelerate learning but lead to overfitting. The authors propose data scheduling strategies to exploit this phenomenon while mitigating overfitting. Finally, the paper examines the challenges of incorporating new knowledge into a pretrained model, finding that hallucinations emerge alongside knowledge acquisition, and fine-tuning often corrupts existing parametric memories.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
- The paper is well-written and easy to follow. The problem is well-motivated, and the methodology is clearly explained. The figures are informative and complement the text well.
- The paper addresses a crucial question in the field of language modeling: understanding how language models learn factual knowledge. The findings have important implications for the design of language models and their training strategies.
- The authors provide a novel explanation for the learning dynamics of language models, focusing on the formation of attention-based circuits and the impact of data distribution properties on learning. The attention patching technique is a creative method for analyzing the learning process.
- The paper provides empirical evidence for its claims through well-designed experiments and analyses. The results are presented clearly and support the conclusions drawn.

## Weaknesses
- The paper focuses on a synthetic factual recall task, which may not fully capture the complexity of real-world language learning. The authors acknowledge this limitation, but it would be helpful to discuss potential implications of the findings for natural language learning.
- The paper could benefit from a more detailed comparison with existing theories and models of language learning. While some connections to previous work are discussed, a comprehensive comparison would strengthen the paper's contribution.
- The paper primarily focuses on a specific model architecture and size. It would be valuable to explore how the findings generalize to other models, especially larger-scale models used in practical applications.

## Questions
- How do the findings generalize to natural language learning? Are there any implications for theories of language acquisition in the field of linguistics?
- How do the findings compare to other theories and models of language learning? Are there any contradictions or complementary aspects?
- Have you considered the potential impact of the findings on the design of language models in practical applications? How could the proposed data scheduling strategies be implemented in real-world scenarios?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4