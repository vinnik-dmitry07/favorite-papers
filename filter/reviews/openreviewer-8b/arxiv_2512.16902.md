# Review

## Summary
This paper investigates the mechanisms that emerge in transformers trained on in-context algebraic reasoning tasks where tokens serve as variables without fixed meanings. Through a series of targeted experiments, the authors demonstrate that transformers develop and employ symbolic reasoning strategies, including commutative copying, identity element recognition, and closure-based cancellation. The study provides insights into how transformers can learn to reason abstractly when token meanings are context-dependent, challenging previous assumptions about the role of token embeddings in arithmetic tasks.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
- The paper presents a novel approach by removing fixed token embeddings, which forces the model to rely on contextual relationships for reasoning.
- The authors conduct thorough experiments to isolate and verify several mechanisms, such as commutative copying and identity element recognition.
- The paper provides a detailed analysis of how the model’s mechanisms evolve during training, identifying distinct phase transitions.
- The findings contribute to a deeper understanding of in-context learning and how transformers can develop symbolic reasoning without pre-encoded information.

## Weaknesses
- The paper could benefit from a more detailed comparison with existing work on emergent arithmetic reasoning in transformers, particularly regarding the role of attention patterns and the development of Fourier-like representations.
- While the study focuses on algebraic tasks, it would be valuable to explore how these findings might generalize to other abstract reasoning domains.

## Questions
- How do the identified mechanisms in this study compare to the geometric and parametric approaches mentioned in the introduction? Are the proposed mechanisms distinct, or can they be related to or subsumed by the existing approaches?
- The paper mentions that tokens act as placeholders with meaning inferred from context. How does this compare to models that use a mixture of low-rank embeddings and learned tokens, where the meaning is also context-dependent but encoded in low-rank embeddings?
- The authors identify distinct phase transitions during training. How do these transitions relate to known phase transitions in other in-context learning tasks, such as the copying phase transition in induction heads?
- The paper focuses on algebraic tasks. Could the identified mechanisms generalize to other types of abstract reasoning tasks, such as logical reasoning or more complex algebraic structures?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4