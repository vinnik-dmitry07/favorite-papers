## Reviewer

### Summary

This paper explores the performance of LLMs on multiple-choice question answering (MCQA) tasks when only given the choices. The authors test this on three MCQA datasets and four LLMs and find that the LLMs can perform MCQA with choices-only prompts, often outperforming a majority baseline. The authors then try to explain this performance by testing three hypotheses: (1) memorization, (2) choice dynamics, and (3) abductive question inference. They find that the performance is not due to memorization, and that choice dynamics and abductive question inference are likely contributing factors. The authors conclude by advocating for the use of stronger baselines in MCQA benchmarks and the design of more robust MCQA datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors test their hypotheses on multiple datasets and LLMs, providing a robust evaluation.
- The authors provide a thorough analysis of their results, including qualitative analysis of the LLMs' generated questions.

### Weaknesses

- The paper does not provide a clear conclusion or recommendation for how to improve MCQA benchmarks. The authors state that the LLMs' performance on choices-only prompts is not solely due to memorization, but do not provide a clear explanation of what is causing the performance. The authors also state that abductive question inference is a contributing factor, but do not provide a clear explanation of how the LLMs are able to perform this inference.
- The authors do not provide a clear definition of "artifacts" in the context of MCQA. The authors state that the LLMs' performance on choices-only prompts is due to "artifacts," but do not provide a clear explanation of what these artifacts are or how they are being exploited by the LLMs.
- The authors do not provide a clear explanation of how the LLMs are able to perform abductive question inference. The authors state that the LLMs are able to generate questions that are answerable by the choices, but do not provide a clear explanation of how this is being done.

### Questions

- Can you provide a clear definition of "artifacts" in the context of MCQA? How are the LLMs exploiting these artifacts to perform MCQA with choices-only prompts?
- Can you provide a clear explanation of how the LLMs are able to perform abductive question inference? How are they able to generate questions that are answerable by the choices?
- Can you provide a clear conclusion or recommendation for how to improve MCQA benchmarks? What are the key takeaways from your analysis, and how can they be used to improve the evaluation of LLMs on MCQA tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper investigates the ability of LLMs to answer multiple-choice questions using only the options, without the question. The authors conduct an in-depth analysis of the performance of LLMs on this task, and identify three key factors that contribute to their ability to perform well on this task: memorization, choice dynamics, and abductive question inference. The authors also release a suite of tools for evaluating LLMs on this task.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a thorough analysis of the performance of LLMs on the task of answering multiple-choice questions with only the options.
- The authors release a suite of tools for evaluating LLMs on this task, which can be useful for future research.

### Weaknesses

- The authors do not provide a clear explanation of the limitations of their analysis. For example, it is not clear whether the results would generalize to other LLMs or other tasks. It would be helpful if the authors could provide a more detailed discussion of the limitations of their analysis.
- The authors do not provide a clear explanation of the implications of their findings. For example, it is not clear what the practical implications are of LLMs being able to answer multiple-choice questions with only the options. It would be helpful if the authors could provide a more detailed discussion of the implications of their findings.

### Questions

- Can you provide a clear explanation of the limitations of your analysis? For example, it is not clear whether the results would generalize to other LLMs or other tasks.
- Can you provide a clear explanation of the implications of your findings? For example, it is not clear what the practical implications are of LLMs being able to answer multiple-choice questions with only the options.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper investigates whether LLMs can perform multiple-choice question answering (MCQA) with only the choices. The authors find that LLMs can indeed perform MCQA with only the choices, and that this performance is not solely due to memorization. They also find that LLMs use both individual priors and group dynamics to perform MCQA with only the choices. Furthermore, they find that LLMs can abductively infer the original question from the choices, which can explain some of the performance. The authors release a black-box evaluation suite to facilitate further research on LLMs in MCQA.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

* The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the problem and the proposed approach.
* The authors conduct a thorough analysis of the performance of LLMs on MCQA with only the choices. They investigate three hypotheses to explain the performance and provide evidence to support or refute each hypothesis.
* The authors release a black-box evaluation suite to facilitate further research on LLMs in MCQA.

### Weaknesses

* The paper is somewhat limited in scope. The authors focus on LLMs and MCQA, but do not consider other types of models or other types of question answering tasks. It would be interesting to see how the findings of this paper generalize to other models and tasks.
* The paper does not provide a clear conclusion or recommendation for how to improve MCQA evaluations. The authors suggest that LLMs use both individual priors and group dynamics to perform MCQA with only the choices, but do not provide guidance on how to design evaluations that can detect and mitigate these biases.

### Questions

* How do the findings of this paper generalize to other models and tasks? For example, do other types of models, such as transformer-based models or neural networks, also exhibit similar behavior in MCQA with only the choices?
* How can we design evaluations that can detect and mitigate biases in LLMs? For example, how can we design evaluations that can detect and mitigate individual priors and group dynamics in LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper investigates the ability of LLMs to answer multiple-choice questions using only the choices. The authors test this on three MCQA datasets and four LLMs and find that the LLMs can perform MCQA with choices-only prompts, often outperforming a majority baseline. The authors then try to explain this performance by testing three hypotheses: (1) memorization, (2) choice dynamics, and (3) abductive question inference. They find that the performance is not due to memorization, and that choice dynamics and abductive question inference are likely contributing factors. The authors conclude by advocating for the use of stronger baselines in MCQA benchmarks and the design of more robust MCQA datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow. The authors test their hypotheses on multiple datasets and LLMs, providing a robust evaluation. The authors also provide a thorough analysis of their results, including qualitative analysis of the LLMs' generated questions.
2. The authors release a suite of tools for evaluating LLMs on this task, which can be useful for future research.
3. The authors provide a clear definition of "artifacts" in the context of MCQA, and explain how the LLMs are exploiting these artifacts to perform MCQA with choices-only prompts.

### Weaknesses

1. The authors do not provide a clear explanation of how the LLMs are able to perform abductive question inference. The authors state that the LLMs are able to generate questions that are answerable by the choices, but do not provide a clear explanation of how this is being done.
2. The authors do not provide a clear conclusion or recommendation for how to improve MCQA benchmarks. The authors state that the LLMs' performance on choices-only prompts is not solely due to memorization, but do not provide a clear explanation of what is causing the performance. The authors also state that abductive question inference is a contributing factor, but do not provide a clear explanation of how the LLMs are able to perform this inference.

### Questions

1. Can you provide a clear explanation of how the LLMs are able to perform abductive question inference? How are they able to generate questions that are answerable by the choices?
2. Can you provide a clear conclusion or recommendation for how to improve MCQA benchmarks? What are the key takeaways from your analysis, and how can they be used to improve the evaluation of LLMs on MCQA tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper explores whether LLMs can perform multiple-choice question answering (MCQA) with only the choices. The authors test this on three MCQA datasets and four LLMs and find that the LLMs can perform MCQA with choices-only prompts, often outperforming a majority baseline. The authors then try to explain this performance by testing three hypotheses: (1) memorization, (2) choice dynamics, and (3) abductive question inference. They find that the performance is not due to memorization, and that choice dynamics and abductive question inference are likely contributing factors. The authors conclude by advocating for the use of stronger baselines in MCQA benchmarks and the design of more robust MCQA datasets.

The paper is well-written and easy to follow. The authors test their hypotheses on multiple datasets and LLMs, providing a robust evaluation. The authors also provide a thorough analysis of their results, including qualitative analysis of the LLMs' generated questions. The authors release a suite of tools for evaluating LLMs on this task, which can be useful for future research. However, the authors do not provide a clear explanation of how the LLMs are able to perform abductive question inference. The authors state that the LLMs are able to generate questions that are answerable by the choices, but do not provide a clear explanation of how this is being done. The authors do not provide a clear conclusion or recommendation for how to improve MCQA benchmarks. The authors state that the LLMs' performance on choices-only prompts is not solely due to memorization, but do not provide a clear explanation of what is causing the performance. The authors also state that abductive question inference is a contributing factor, but do not provide a clear explanation of how the LLMs are able to perform this inference. The paper is somewhat limited in scope. The authors focus on LLMs and MCQA, but do not consider other types of models or other types of question answering tasks. It would be interesting to see how the findings of this paper generalize to other models and tasks. The authors do not provide a clear explanation of the limitations of their analysis. For example, it is not clear whether the results would generalize to other LLMs or other tasks. It would be helpful if the authors could provide a more detailed discussion of the limitations of their analysis. The authors do not provide a clear explanation of the implications of their findings. For example, it is not clear what the practical implications are of LLMs being able to answer multiple-choice questions with only the options. It would be helpful if the authors could provide a more detailed discussion of the implications of their findings.

### justification_for_why_not_higher_score

The paper is somewhat limited in scope. The authors focus on LLMs and MCQA, but do not consider other types of models or other types of question answering tasks. It would be interesting to see how the findings of this paper generalize to other models and tasks. The authors do not provide a clear explanation of the limitations of their analysis. For example, it is not clear whether the results would generalize to other LLMs or other tasks. It would be helpful if the authors could provide a more detailed discussion of the limitations of their analysis. The authors do not provide a clear explanation of the implications of their findings. For example, it is not clear what the practical implications are of LLMs being able to answer multiple-choice questions with only the options. It would be helpful if the authors could provide a more detailed discussion of the implications of their findings.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication) (poster) (score 6.25, 5, 5, 6)

**********

**Paper Decision:** Reject (not selected for publication) (poster)

**Reviewers:** 4k6k, Q6Nv, u8Ku, 8T6s

**Score:** 6.25, 5, 5, 6

**Rating:** marginally below the acceptance threshold

**********

*Note:* In the interests of transparency, we would like to note that one of the reviewers was an author on a paper that is cited in the submission. This reviewer did not participate in the discussion or deliberation about this paper.

**********

*If you have any further concerns about the paper, you may want to discuss them with the PC chair, Michael Collins (mcc@cs.nyu.edu)*.