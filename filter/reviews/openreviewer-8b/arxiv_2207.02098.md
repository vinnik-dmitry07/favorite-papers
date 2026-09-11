# Review

## Summary
This paper presents an empirical study of the ability of different neural network architectures to learn different formal languages, in particular focusing on the Chomsky hierarchy. The authors consider several architectures (RNN, LSTM, Transformer, Stack-RNN, Tape-RNN) and tasks (15 language transduction tasks, ranging from regular to context-sensitive languages). The authors find that the different architectures match the theoretical computational power of the corresponding models they are based on, with some caveats.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
The paper is very well written and clear, and the experiments are well described. The experiments are very thorough, and the code is open source. The results are interesting and insightful, and validate the theoretical analysis of the different models.

## Weaknesses
The paper is missing some references to related work. In particular, the authors should consider citing:
- "On the Recognition of Formal Languages by Recurrent Neural Networks" by Hahn, Korsky, and Zwick, which shows that RNNs can recognize any regular language that can be recognized by a finite-state automaton with n states, where n is the number of hidden units in the RNN.
- "What Can Transformers Learn? A Case Study of Counter Languages" by Weiss, which shows that Transformers can recognize some counter languages, but cannot recognize simple periodic finite-state languages.
- "A Strongly-Turing-Complete Neural Network Architecture" by Korsky and Berwick, which shows that RNNs augmented with a single attention head can recognize any regular language.

## Questions
- The authors should consider adding the missing references mentioned above.
- The authors should clarify that the tasks are language transduction tasks, not language recognition tasks. This is an important distinction, since for recognition, negative examples are usually also needed, which is not the case in transduction.
- The authors should clarify that the architectures considered are not Turing complete, and that the tasks considered are not computable in general. This is important to avoid confusion with the results of Siegelmann and Sontag, which show that RNNs can be Turing complete if they are unrolled over an unbounded domain.
- The authors should clarify that the results are empirical, and do not rule out the possibility that some architecture could solve a task higher in the Chomsky hierarchy, or that some architecture could solve a task lower or on the same level in the Chomsky hierarchy that is not considered here.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
5