# Review

## Summary
This paper provides a comprehensive study of the stages of inference in recurrent LLMs. The authors show that the attention patterns in recurrent LLMs converge across recurrences. The authors also show that the stages of inference in recurrent LLMs occur within each recurrent block, and that these stages are similar to those in feedforward LLMs. Finally, the authors show that recurrent LLMs that converge to a fixed point exhibit stable stages of inference for any number of recurrences, while those that do not exhibit unstable stages of inference.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
* The paper is very well written and easy to follow. The authors do a great job at introducing the necessary background and related work. The figures are also very well made.
* The experiments are very thorough and well-motivated. The authors provide experiments on a variety of recurrent LLMs, including Ouro, Huggin-0125, and retrofitted Llama. The authors also provide experiments on randomly initialized models to show that the results are not just an artifact of the training procedure.
* The results are very interesting. The finding that the stages of inference occur within each recurrent block is surprising to me. The finding that recurrent LLMs mirror the stages of inference of feedforward LLMs is also very interesting.

## Weaknesses
* The paper could benefit from a more detailed discussion of the implications of the findings. For example, the authors show that recurrent LLMs that converge to a fixed point exhibit stable stages of inference for any number of recurrences, while those that do not exhibit unstable stages of inference. The authors should discuss the implications of this finding for recurrent LLM design.
* The paper could benefit from a more detailed discussion of the limitations of the analysis. For example, the authors focus on cyclic recurrence, but do not extend to sequential recurrence with multiple separate recurrent blocks. The authors should discuss the limitations of their analysis and how they might be addressed in future work.

## Questions
* Do the authors have any hypotheses for why Ouro does not exhibit stable limiting behavior?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4