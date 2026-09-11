## Reviewer

### Summary

This paper studies the on-policy distillation (OPD) of large language models. The authors identify two conditions for successful OPD: (i) the student and teacher should share compatible thinking patterns; (ii) the teacher should offer new capabilities beyond what the student has seen. The authors validate these findings through weak-to-strong reverse distillation and show that successful OPD is characterized by progressive alignment on high-probability tokens at student-visited states. They also propose two practical strategies to recover failing OPD: off-policy cold start and teacher-aligned prompt selection. Finally, they show that OPD's dense token-level reward comes at a cost, raising questions about its scalability to long-horizon distillation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper provides a systematic investigation of OPD dynamics and mechanisms, identifying two key conditions for successful OPD. The authors validate their findings through experiments and propose practical strategies to recover failing OPD. The paper also highlights the limitations of OPD for long-horizon distillation, which is an important area for future research.

### Weaknesses

1. The paper focuses on mathematical benchmarks, which may not be representative of other domains such as code and open-ended settings. It would be interesting to see if the same conditions and token-level mechanisms govern OPD in these other domains.

2. The paper does not isolate the impact of pre-training on OPD. It would be helpful to understand how differences in pre-training corpora affect OPD.

3. The paper does not explore the dynamics of self-distillation, where a single model serves as its own teacher given privileged information. It would be interesting to extend the insights to this regime.

### Questions

Please refer to the weakness part.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper investigates the dynamics and mechanisms of on-policy distillation (OPD) in large language models. The authors identify two conditions for successful OPD: (i) the student and teacher should share compatible thinking patterns, and (ii) the teacher should offer new capabilities beyond what the student has seen. They validate these findings through weak-to-strong reverse distillation and show that successful OPD is characterized by progressive alignment on high-probability tokens at student-visited states. The authors also propose two practical strategies to recover failing OPD: off-policy cold start and teacher-aligned prompt selection. Finally, they show that OPD's dense token-level reward comes at a cost, raising questions about its scalability to long-horizon distillation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- This paper provides a systematic investigation of OPD dynamics and mechanisms, identifying two key conditions for successful OPD.
- The authors validate their findings through experiments and propose practical strategies to recover failing OPD.
- The paper also highlights the limitations of OPD for long-horizon distillation, which is an important area for future research.

### Weaknesses

- The paper focuses on mathematical benchmarks, which may not be representative of other domains such as code and open-ended settings. It would be interesting to see if the same conditions and token-level mechanisms govern OPD in these other domains.
- The paper does not isolate the impact of pre-training on OPD. It would be helpful to understand how differences in pre-training corpora affect OPD.
- The paper does not explore the dynamics of self-distillation, where a single model serves as its own teacher given privileged information. It would be interesting to extend the insights to this regime.

### Questions

Please refer to the weakness part.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a systematic analysis of on-policy distillation (OPD) for large language models. The authors identify two key conditions for successful OPD: (i) the student and teacher should share compatible thinking patterns, and (ii) the teacher should offer new capabilities beyond what the student has seen. They validate these findings through weak-to-strong reverse distillation and show that successful OPD is characterized by progressive alignment on high-probability tokens at student-visited states. The authors also propose two practical strategies to recover failing OPD: off-policy cold start and teacher-aligned prompt selection. Finally, they show that OPD's dense token-level reward comes at a cost, raising questions about its scalability to long-horizon distillation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- This paper provides a systematic investigation of OPD dynamics and mechanisms, identifying two key conditions for successful OPD.
- The authors validate their findings through experiments and propose practical strategies to recover failing OPD.
- The paper also highlights the limitations of OPD for long-horizon distillation, which is an important area for future research.

### Weaknesses

- The paper focuses on mathematical benchmarks, which may not be representative of other domains such as code and open-ended settings. It would be interesting to see if the same conditions and token-level mechanisms govern OPD in these other domains.
- The paper does not isolate the impact of pre-training on OPD. It would be helpful to understand how differences in pre-training corpora affect OPD.
- The paper does not explore the dynamics of self-distillation, where a single model serves as its own teacher given privileged information. It would be interesting to extend the insights to this regime.

### Questions

Please refer to the weakness part.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the on-policy distillation (OPD) of large language models. The authors identify two conditions for successful OPD: (i) the student and teacher should share compatible thinking patterns; (ii) the teacher should offer new capabilities beyond what the student has seen. The authors validate these findings through weak-to-strong reverse distillation and show that successful OPD is characterized by progressive alignment on high-probability tokens at student-visited states. The authors also propose two practical strategies to recover failing OPD: off-policy cold start and teacher-aligned prompt selection. Finally, they show that OPD's dense token-level reward comes at a cost, raising questions about its scalability to long-horizon distillation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper provides a systematic investigation of OPD dynamics and mechanisms, identifying two key conditions for successful OPD.
2. The authors validate their findings through experiments and propose practical strategies to recover failing OPD.
3. The paper also highlights the limitations of OPD for long-horizon distillation, which is an important area for future research.

### Weaknesses

1. The paper focuses on mathematical benchmarks, which may not be representative of other domains such as code and open-ended settings. It would be interesting to see if the same conditions and token-level mechanisms govern OPD in these other domains.
2. The paper does not isolate the impact of pre-training on OPD. It would be helpful to understand how differences in pre-training corpora affect OPD.
3. The paper does not explore the dynamics of self-distillation, where a single model serves as its own teacher given privileged information. It would be interesting to extend the insights to this regime.

### Questions

Please refer to the weakness part.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies on-policy distillation (OPD) for large language models. The authors identify two conditions for successful OPD: (i) the student and teacher should share compatible thinking patterns; (ii) the teacher should offer new capabilities beyond what the student has seen. They validate these findings through weak-to-strong reverse distillation and show that successful OPD is characterized by progressive alignment on high-probability tokens at student-visited states. The authors also propose two practical strategies to recover failing OPD: off-policy cold start and teacher-aligned prompt selection. Finally, they show that OPD's dense token-level reward comes at a cost, raising questions about its scalability to long-horizon distillation.

This paper received four reviews with scores 6, 6, 6, 6. The reviewers are all positive about the paper and recommend acceptance. The authors have responded to all the questions raised by the reviewers. The AC has read the paper, the reviews, and the authors' responses. The AC agrees with the reviewers that this paper is a solid work and should be accepted.

### justification_for_why_not_higher_score

This paper is a solid work. However, it is not a groundbreaking work.

### justification_for_why_not_lower_score

This paper is a solid work. It is well-written and easy to follow. The authors have done a good job on the experiments.

**********

## Paper Decision

Accept (poster)