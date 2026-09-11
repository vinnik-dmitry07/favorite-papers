## Reviewer

### Summary

The paper proposes a novel approach to credit assignment in RL for LLMs. The authors first identify that the training process of LLMs on reasoning tasks can be decomposed into two phases: (1) learning low-level skills and (2) learning high-level planning. The authors then propose a method to focus the learning signal on high-level planning tokens. The authors validate their approach on various reasoning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and intuitive. The authors provide a thorough analysis of the training dynamics of LLMs on reasoning tasks.

### Weaknesses

1. The paper assumes that the reasoning process can be decomposed into high-level planning and low-level execution. This assumption is not always valid. For example, in the case of mathematical problem-solving, the high-level plan and low-level execution are often intertwined. The authors should provide more evidence to support their assumption.

2. The authors use a heuristic to identify high-level planning tokens. The heuristic is based on the frequency of n-grams. However, this may not always be accurate. For example, a low-frequency n-gram may still be a high-level planning token. The authors should provide more evidence to support their heuristic.

3. The authors only evaluate their method on mathematical problem-solving tasks. The authors should evaluate their method on other types of reasoning tasks, such as logical reasoning and commonsense reasoning.

### Questions

1. How do you handle the case where the high-level plan and low-level execution are intertwined?

2. How do you handle the case where a low-frequency n-gram is a high-level planning token?

3. How do you evaluate your method on other types of reasoning tasks, such as logical reasoning and commonsense reasoning?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new RL algorithm for LLMs that focuses on the high-level planning tokens in the reasoning process. The authors first analyze the training dynamics of LLMs on reasoning tasks and find that the training process can be decomposed into two phases: (1) learning low-level skills and (2) learning high-level planning. The authors then propose a method to focus the learning signal on high-level planning tokens. The authors validate their approach on various reasoning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a thorough analysis of the training dynamics of LLMs on reasoning tasks.
- The proposed method is simple and intuitive.

### Weaknesses

- The authors only evaluate their method on mathematical problem-solving tasks. The authors should evaluate their method on other types of reasoning tasks, such as logical reasoning and commonsense reasoning.
- The authors use a heuristic to identify high-level planning tokens. The heuristic is based on the frequency of n-grams. However, this may not always be accurate. For example, a low-frequency n-gram may still be a high-level planning token. The authors should provide more evidence to support their heuristic.
- The authors only evaluate their method on a small number of models. The authors should evaluate their method on more models to see if the results are generalizable.

### Questions

- How do you handle the case where the high-level plan and low-level execution are intertwined?
- How do you handle the case where a low-frequency n-gram is a high-level planning token?
- How do you evaluate your method on other types of reasoning tasks, such as logical reasoning and commonsense reasoning?
- How do you evaluate your method on more models to see if the results are generalizable?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new method to improve the reasoning ability of LLMs via RL. The authors first analyze the RL training dynamics of LLMs and find that there are two phases: (1) learning low-level skills and (2) learning high-level planning. The authors then propose a method to focus the learning signal on high-level planning tokens. The authors validate their approach on various reasoning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a thorough analysis of the training dynamics of LLMs on reasoning tasks.
- The proposed method is simple and intuitive.
- The authors validate their approach on various reasoning tasks.

### Weaknesses

- The authors only evaluate their method on mathematical problem-solving tasks. The authors should evaluate their method on other types of reasoning tasks, such as logical reasoning and commonsense reasoning.
- The authors use a heuristic to identify high-level planning tokens. The heuristic is based on the frequency of n-grams. However, this may not always be accurate. For example, a low-frequency n-gram may still be a high-level planning token. The authors should provide more evidence to support their heuristic.
- The authors only evaluate their method on a small number of models. The authors should evaluate their method on more models to see if the results are generalizable.

### Questions

- How do you handle the case where the high-level plan and low-level execution are intertwined?
- How do you handle the case where a low-frequency n-gram is a high-level planning token?
- How do you evaluate your method on other types of reasoning tasks, such as logical reasoning and commonsense reasoning?
- How do you evaluate your method on more models to see if the results are generalizable?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new method to improve the reasoning ability of LLMs via RL. The authors first analyze the RL training dynamics of LLMs and find that there are two phases: (1) learning low-level skills and (2) learning high-level planning. The authors then propose a method to focus the learning signal on high-level planning tokens. The authors validate their approach on various reasoning tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the training dynamics of LLMs on reasoning tasks.
3. The proposed method is simple and intuitive.
4. The authors validate their approach on various reasoning tasks.

### Weaknesses

1. The authors only evaluate their method on mathematical problem-solving tasks. The authors should evaluate their method on other types of reasoning tasks, such as logical reasoning and commonsense reasoning.
2. The authors use a heuristic to identify high-level planning tokens. The heuristic is based on the frequency of n-grams. However, this may not always be accurate. For example, a low-frequency n-gram may still be a high-level planning token. The authors should provide more evidence to support their heuristic.
3. The authors only evaluate their method on a small number of models. The authors should evaluate their method on more models to see if the results are generalizable.

### Questions

1. How do you handle the case where the high-level plan and low-level execution are intertwined?
2. How do you handle the case where a low-frequency n-gram is a high-level planning token?
3. How do you evaluate your method on other types of reasoning tasks, such as logical reasoning and commonsense reasoning?
4. How do you evaluate your method on more models to see if the results are generalizable?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new RL algorithm for LLMs that focuses on the high-level planning tokens in the reasoning process. The authors first analyze the training dynamics of LLMs on reasoning tasks and find that the training process can be decomposed into two phases: (1) learning low-level skills and (2) learning high-level planning. The authors then propose a method to focus the learning signal on high-level planning tokens. The authors validate their approach on various reasoning tasks.

The reviewers raised several concerns regarding the evaluation, generalization, and the assumption of the proposed method. The authors provided a detailed response to the reviewers' concerns. However, the reviewers still maintain their initial ratings. The AC also carefully read the paper, the reviews, and the authors' responses. The AC agrees with the reviewers that the paper still needs further improvement before publication. The AC encourages the authors to carefully consider the reviewers' comments and improve the paper accordingly.

### justification_for_why_not_higher_score

The reviewers raised several concerns regarding the evaluation, generalization, and the assumption of the proposed method. The authors provided a detailed response to the reviewers' concerns. However, the reviewers still maintain their initial ratings. The AC also carefully read the paper, the reviews, and the authors' responses. The AC agrees with the reviewers that the paper still needs further improvement before publication. The AC encourages the authors to carefully consider the reviewers' comments and improve the paper accordingly.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (Reject, not acceptable)