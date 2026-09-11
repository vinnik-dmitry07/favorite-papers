## Reviewer

### Summary

This paper examines the phenomenon of evaluation awareness in large language models (LLMs) and its relationship with probe-based analysis. Evaluation awareness refers to the ability of LLMs to distinguish between evaluation and deployment contexts. The authors argue that probe-based analysis, which uses linear classifiers to detect evaluation awareness, may not be reliable due to its sensitivity to prompt format rather than the underlying context. The paper introduces a controlled 2x2 dataset design that varies context and format independently, and shows that probes trained on benchmark contrasts fail to generalize to free-form prompts. The authors conclude that probe-based evaluation-awareness diagnostics are highly format-sensitive, limiting their use as structure-invariant safety tools.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The idea of using a controlled 2x2 dataset design to examine the relationship between context and format is interesting and novel.
- The paper highlights an important limitation of probe-based analysis in detecting evaluation awareness.

### Weaknesses

- The paper does not provide a clear definition of evaluation awareness, making it difficult to understand the specific phenomenon being studied.
- The paper does not provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis.
- The paper does not provide a clear discussion of the implications of the findings for the use of probe-based analysis in evaluating LLMs.

### Questions

- Can the authors provide a clear definition of evaluation awareness and explain why it is an important phenomenon to study?
- Can the authors provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis?
- Can the authors discuss the implications of the findings for the use of probe-based analysis in evaluating LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper examines the phenomenon of evaluation awareness in large language models (LLMs) and its relationship with probe-based analysis. Evaluation awareness refers to the ability of LLMs to distinguish between evaluation and deployment contexts. The authors argue that probe-based analysis, which uses linear classifiers to detect evaluation awareness, may not be reliable due to its sensitivity to prompt format rather than the underlying context. The paper introduces a controlled 2x2 dataset design that varies context and format independently, and shows that probes trained on benchmark contrasts fail to generalize to free-form prompts. The authors conclude that probe-based evaluation-awareness diagnostics are highly format-sensitive, limiting their use as structure-invariant safety tools.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of using a controlled 2x2 dataset design to examine the relationship between context and format is interesting and novel.
- The paper highlights an important limitation of probe-based analysis in detecting evaluation awareness.

### Weaknesses

- The paper does not provide a clear definition of evaluation awareness, making it difficult to understand the specific phenomenon being studied.
- The paper does not provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis.
- The paper does not provide a clear discussion of the implications of the findings for the use of probe-based analysis in evaluating LLMs.

### Questions

- Can the authors provide a clear definition of evaluation awareness and explain why it is an important phenomenon to study?
- Can the authors provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis?
- Can the authors discuss the implications of the findings for the use of probe-based analysis in evaluating LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper investigates whether the probe-based evidence of evaluation awareness in large language models is due to the format of the prompt or the evaluation context. The authors argue that the current probe-based evidence does not distinguish between the two. To this end, they construct a 2x2 controlled dataset, where the evaluation context and format are varied independently. They find that the probes trained on the benchmark vs. casual format do not generalize to the other format. They conclude that the probe-based evidence is not due to the evaluation context but rather the format of the prompt.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of using a controlled 2x2 dataset design to examine the relationship between context and format is interesting and novel.
- The paper highlights an important limitation of probe-based analysis in detecting evaluation awareness.

### Weaknesses

- The paper does not provide a clear definition of evaluation awareness, making it difficult to understand the specific phenomenon being studied.
- The paper does not provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis.
- The paper does not provide a clear discussion of the implications of the findings for the use of probe-based analysis in evaluating LLMs.

### Questions

- Can the authors provide a clear definition of evaluation awareness and explain why it is an important phenomenon to study?
- Can the authors provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis?
- Can the authors discuss the implications of the findings for the use of probe-based analysis in evaluating LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper investigates whether probes can distinguish between evaluation and deployment contexts in LLMs. The authors argue that probes are not reliable due to their sensitivity to prompt format rather than the underlying context. They introduce a controlled 2x2 dataset design that varies context and format independently, and show that probes trained on benchmark contrasts fail to generalize to free-form prompts.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using a controlled 2x2 dataset design to examine the relationship between context and format is interesting and novel.
3. The paper highlights an important limitation of probe-based analysis in detecting evaluation awareness.

### Weaknesses

1. The paper does not provide a clear definition of evaluation awareness, making it difficult to understand the specific phenomenon being studied.
2. The paper does not provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis.
3. The paper does not provide a clear discussion of the implications of the findings for the use of probe-based analysis in evaluating LLMs.

### Questions

1. Can the authors provide a clear definition of evaluation awareness and explain why it is an important phenomenon to study?
2. Can the authors provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis?
3. Can the authors discuss the implications of the findings for the use of probe-based analysis in evaluating LLMs?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper investigates the relationship between evaluation awareness in large language models (LLMs) and probe-based analysis. The authors argue that probe-based analysis, which uses linear classifiers to detect evaluation awareness, may not be reliable due to its sensitivity to prompt format rather than the underlying context. The paper introduces a controlled 2x2 dataset design that varies context and format independently, and shows that probes trained on benchmark contrasts fail to generalize to free-form prompts. The authors conclude that probe-based evaluation-awareness diagnostics are highly format-sensitive, limiting their use as structure-invariant safety tools.

The reviewers generally agree that the paper is well-written and easy to follow, and that the idea of using a controlled 2x2 dataset design to examine the relationship between context and format is interesting and novel. They also highlight the importance of the paper in highlighting a limitation of probe-based analysis in detecting evaluation awareness.

However, there are some concerns about the paper's clarity and the definition of evaluation awareness. The reviewers suggest that the paper could benefit from a clearer definition of evaluation awareness and a more detailed explanation of why probes are sensitive to format rather than context. Additionally, the paper could benefit from a more detailed discussion of the implications of the findings for the use of probe-based analysis in evaluating LLMs.

Overall, the paper has some strengths, but also some weaknesses that need to be addressed. The authors are encouraged to revise the paper based on the reviewers' feedback and resubmit it to a future conference.

### justification_for_why_not_higher_score

The paper has some weaknesses that need to be addressed, such as the need for a clearer definition of evaluation awareness and a more detailed explanation of why probes are sensitive to format rather than context.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for spotlight)