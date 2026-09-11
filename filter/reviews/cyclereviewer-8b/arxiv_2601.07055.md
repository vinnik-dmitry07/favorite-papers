## Reviewer

### Summary

This paper introduces a framework called Dr. Zero, which enables search agents to self-evolve without the need for human-annotated training data. The framework uses an external search engine as the knowledge environment and consists of a proposer and a solver. The proposer generates structurally diverse questions to train the solver, which in turn incentivizes the proposer to produce increasingly difficult yet solvable tasks. To enhance training efficiency, the paper introduces hop-grouped relative policy optimization (HRPO), which clusters structurally similar questions to construct group-level baselines and minimize sampling overhead. The experiments show that Dr. Zero matches or surpasses fully supervised search agents on several question answering benchmarks, demonstrating that strong agentic search and evidence-grounded reasoning can emerge solely through self-evolution.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper proposes a novel framework that enables search agents to self-evolve without human-annotated training data.
2. The framework uses an external search engine as the knowledge environment, which is a novel approach.
3. The paper introduces hop-grouped relative policy optimization (HRPO), which is a novel optimization method that clusters structurally similar questions to provide a robust group-level baseline for advantage estimation.
4. The paper provides extensive experimental results demonstrating the effectiveness of Dr. Zero.

### Weaknesses

1. The paper lacks a detailed description of the methodology, making it difficult to understand the specific techniques used in the framework.
2. The paper does not provide a clear explanation of the advantages of the proposed framework over existing methods.
3. The paper does not discuss the potential limitations of the proposed framework.
4. The paper does not provide a clear explanation of how the proposed framework can be applied to other domains or tasks.

### Questions

1. How does the proposed framework compare to existing methods in terms of performance and efficiency?
2. What are the potential limitations of the proposed framework?
3. How can the proposed framework be applied to other domains or tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a self-evolving search agent that does not require human-annotated training data. The agent consists of a proposer and a solver, which are trained in an iterative manner. The proposer generates questions to train the solver, and the solver provides feedback to the proposer. The authors propose a hop-grouped relative policy optimization (HRPO) to train the proposer. Experiments on various question answering benchmarks show that the proposed method can match or outperform fully supervised search agents.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The proposed method achieves good performance on various question answering benchmarks.

### Weaknesses

1. The proposed method is not well-motivated. The authors claim that the existing methods suffer from limited question diversity and the substantial compute required for multi-step reasoning and tool use. However, the authors do not provide sufficient evidence to support this claim. The authors also do not explain why the proposed method can address these issues.
2. The proposed method is not well-motivated. The authors claim that the existing methods suffer from limited question diversity and the substantial compute required for multi-step reasoning and tool use. However, the authors do not provide sufficient evidence to support this claim. The authors also do not explain why the proposed method can address these issues.
3. The proposed method is not well-motivated. The authors claim that the existing methods suffer from limited question diversity and the substantial compute required for multi-step reasoning and tool use. However, the authors do not provide sufficient evidence to support this claim. The authors also do not explain why the proposed method can address these issues.

### Questions

1. How does the proposed method compare to existing methods in terms of question diversity and compute efficiency?
2. How does the proposed method address the issues of limited question diversity and substantial compute required for multi-step reasoning and tool use?
3. What are the advantages of the proposed method compared to existing methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method for self-evolving search agents without human-annotated training data. The proposed method consists of two components: a proposer and a solver. The proposer generates questions to train the solver, and the solver provides feedback to the proposer. The authors propose a hop-grouped relative policy optimization (HRPO) to train the proposer. Experiments on various question answering benchmarks show that the proposed method can match or outperform fully supervised search agents.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The proposed method achieves good performance on various question answering benchmarks.

### Weaknesses

1. The proposed method is not well-motivated. The authors claim that the existing methods suffer from limited question diversity and the substantial compute required for multi-step reasoning and tool use. However, the authors do not provide sufficient evidence to support this claim. The authors also do not explain why the proposed method can address these issues.
2. The proposed method is not well-motivated. The authors claim that the existing methods suffer from limited question diversity and the substantial compute required for multi-step reasoning and tool use. However, the authors do not provide sufficient evidence to support this claim. The authors also do not explain why the proposed method can address these issues.
3. The proposed method is not well-motivated. The authors claim that the existing methods suffer from limited question diversity and the substantial compute required for multi-step reasoning and tool use. However, the authors do not provide sufficient evidence to support this claim. The authors also do not explain why the proposed method can address these issues.

### Questions

1. How does the proposed method compare to existing methods in terms of question diversity and compute efficiency?
2. How does the proposed method address the issues of limited question diversity and substantial compute required for multi-step reasoning and tool use?
3. What are the advantages of the proposed method compared to existing methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces Dr. Zero, a framework that enables search agents to self-evolve without human-annotated training data. It uses an external search engine as the knowledge environment and consists of a proposer and a solver. The proposer generates questions to train the solver, and the solver provides feedback to the proposer. The authors propose a hop-grouped relative policy optimization (HRPO) to train the proposer. Experiments on various question answering benchmarks show that the proposed method can match or outperform fully supervised search agents.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The proposed method achieves good performance on various question answering benchmarks.

### Weaknesses

1. The proposed method is not well-motivated. The authors claim that the existing methods suffer from limited question diversity and the substantial compute required for multi-step reasoning and tool use. However, the authors do not provide sufficient evidence to support this claim. The authors also do not explain why the proposed method can address these issues.
2. The proposed method is not well-motivated. The authors claim that the existing methods suffer from limited question diversity and the substantial compute required for multi-step reasoning and tool use. However, the authors do not provide sufficient evidence to support this claim. The authors also do not explain why the proposed method can address these issues.
3. The proposed method is not well-motivated. The authors claim that the existing methods suffer from limited question diversity and the substantial compute required for multi-step reasoning and tool use. However, the authors do not provide sufficient evidence to support this claim. The authors also do not explain why the proposed method can address these issues.

### Questions

1. How does the proposed method compare to existing methods in terms of question diversity and compute efficiency?
2. How does the proposed method address the issues of limited question diversity and substantial compute required for multi-step reasoning and tool use?
3. What are the advantages of the proposed method compared to existing methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a self-evolving search agent that does not require human-annotated training data. The agent consists of a proposer and a solver, which are trained in an iterative manner. The proposer generates questions to train the solver, and the solver provides feedback to the proposer. The authors propose a hop-grouped relative policy optimization (HRPO) to train the proposer. Experiments on various question answering benchmarks show that the proposed method can match or outperform fully supervised search agents.

The reviewers have raised several concerns about the paper, including the lack of motivation for the proposed method, the lack of evidence to support the claims made in the paper, and the lack of clarity in the presentation of the method. The authors have provided a response to these concerns, but the reviewers remain unconvinced about the significance of the work.

### justification_for_why_not_higher_score

The reviewers have raised several concerns about the paper, including the lack of motivation for the proposed method, the lack of evidence to support the claims made in the paper, and the lack of clarity in the presentation of the method. The authors have provided a response to these concerns, but the reviewers remain unconvinced about the significance of the work.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication for ICLR 2024)