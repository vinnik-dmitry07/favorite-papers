# Review

## Summary
The paper investigates the phenomenon of choices-only prompts in multiple-choice question answering (MCQA). The authors demonstrate that LLMs can achieve higher accuracy with choices-only prompts compared to majority class baselines. They explore three hypotheses to explain this behavior: memorization, choice dynamics, and abductive question inference (AQI). The paper finds that while AQI contributes to the choices-only performance, it does not fully explain it. The authors advocate for reporting choices-only baselines and designing more robust MCQA datasets to better understand and interpret model capabilities in MCQA evaluations.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The authors conduct a thorough analysis of the choices-only prompt phenomenon, testing three well-defined hypotheses.
- The paper provides valuable insights into LLM decision-making in MCQA and highlights the limitations of current benchmarks.

## Weaknesses
- The authors do not provide concrete recommendations for designing more robust MCQA datasets.
- The study is limited to a black-box analysis, which may not fully capture the internal workings of the models.
- The experiments are conducted with a limited number of MCQA datasets.

## Questions
- How can the findings of this study inform the design of more robust MCQA datasets?
- How might the results differ if the analysis were conducted with a larger number of MCQA datasets?
- Have you considered conducting a sensitivity analysis to understand how the results might vary with different prompt variations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4