## Reviewer

### Summary

The paper introduces a novel framework for evaluating continual learning in large language models (LLMs). The authors argue that the traditional view of continual learning as a context management problem is incomplete and propose a new definition that emphasizes the model's increasing competence as the world changes over time. They evaluate eight methods across four families using a unified protocol and a suite of sequential LLM tasks, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates. The results show that prompt-based methods are insufficient across most regimes, and different learning methods have their strengths depending on how the task and data shift over time. The paper provides a unified perspective on continual learning in LLMs and highlights the need for a more nuanced understanding of the problem.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper provides a unified framework for evaluating continual learning in LLMs, which allows for a fair comparison of different methods.
- The authors evaluate eight methods across four families using a suite of sequential LLM tasks, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates.
- The results show that different learning methods have their strengths depending on how the task and data shift over time, which can guide the design of more capable continual learning systems.

### Weaknesses

- The paper only evaluates eight methods across four families, which may not be representative of all possible approaches to continual learning in LLMs.
- The paper only uses a single model, Qwen3-8B, for all evaluations, which may not generalize to other models or model sizes.
- The paper only considers a limited set of realistic environmental changes, such as domain shifts, agentic sequences, noisy temporal drift, and discrete factual updates. It does not consider more open-ended, changing, and uncertain environments and diverse use cases that may be encountered in real-world applications.

### Questions

- How do the results generalize to other models or model sizes?
- How do the results generalize to more open-ended, changing, and uncertain environments and diverse use cases?
- How can the framework be extended to consider more realistic environmental changes and diverse use cases?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies continual learning for LLMs, and proposes a unified framework to evaluate different continual learning methods. The authors evaluate eight methods across four families, including prompt optimization, supervised weight updates, reinforcement learning, and context compression, using a suite of sequential LLM tasks. The results show that different learning methods have their strengths depending on how the task and data shift over time, and that no single method handles all task regimes well.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- This paper studies an important problem of continual learning for LLMs, which is a timely and relevant topic.
- The authors propose a unified framework for evaluating continual learning in LLMs, which allows for a fair comparison of different methods.
- The authors evaluate eight methods across four families using a suite of sequential LLM tasks, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates.

### Weaknesses

- The authors only evaluate eight methods across four families, which may not be representative of all possible approaches to continual learning in LLMs.
- The authors only use a single model, Qwen3-8B, for all evaluations, which may not generalize to other models or model sizes.
- The authors only consider a limited set of realistic environmental changes, such as domain shifts, agentic sequences, noisy temporal drift, and discrete factual updates. It does not consider more open-ended, changing, and uncertain environments and diverse use cases that may be encountered in real-world applications.

### Questions

- How do the results generalize to other models or model sizes?
- How do the results generalize to more open-ended, changing, and uncertain environments and diverse use cases?
- How can the framework be extended to consider more realistic environmental changes and diverse use cases?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a unified framework to evaluate continual learning in large language models (LLMs). The authors argue that the traditional view of continual learning as a context management problem is incomplete and propose a new definition that emphasizes the model's increasing competence as the world changes over time. They evaluate eight methods across four families using a unified protocol and a suite of sequential LLM tasks, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates. The results show that prompt-based methods are insufficient across most regimes, and different learning methods have their strengths depending on how the task and data shift over time. The paper provides a unified perspective on continual learning in LLMs and highlights the need for a more nuanced understanding of the problem.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a unified framework for evaluating continual learning in LLMs, which allows for a fair comparison of different methods.
- The authors evaluate eight methods across four families using a suite of sequential LLM tasks, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates.
- The results show that different learning methods have their strengths depending on how the task and data shift over time, which can guide the design of more capable continual learning systems.

### Weaknesses

- The paper only evaluates eight methods across four families, which may not be representative of all possible approaches to continual learning in LLMs.
- The paper only uses a single model, Qwen3-8B, for all evaluations, which may not generalize to other models or model sizes.
- The paper only considers a limited set of realistic environmental changes, such as domain shifts, agentic sequences, noisy temporal drift, and discrete factual updates. It does not consider more open-ended, changing, and uncertain environments and diverse use cases that may be encountered in real-world applications.

### Questions

- How do the results generalize to other models or model sizes?
- How do the results generalize to more open-ended, changing, and uncertain environments and diverse use cases?
- How can the framework be extended to consider more realistic environmental changes and diverse use cases?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies continual learning in LLMs and proposes a unified framework to evaluate different continual learning methods. The authors evaluate eight methods across four families using a suite of sequential LLM tasks, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates. The results show that different learning methods have their strengths depending on how the task and data shift over time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper studies an important problem of continual learning in LLMs.
- The authors propose a unified framework for evaluating continual learning in LLMs, which allows for a fair comparison of different methods.
- The authors evaluate eight methods across four families using a suite of sequential LLM tasks, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates.

### Weaknesses

- The paper only evaluates eight methods across four families, which may not be representative of all possible approaches to continual learning in LLMs.
- The paper only uses a single model, Qwen3-8B, for all evaluations, which may not generalize to other models or model sizes.
- The paper only considers a limited set of realistic environmental changes, such as domain shifts, agentic sequences, noisy temporal drift, and discrete factual updates. It does not consider more open-ended, changing, and uncertain environments and diverse use cases that may be encountered in real-world applications.

### Questions

- How do the results generalize to other models or model sizes?
- How do the results generalize to more open-ended, changing, and uncertain environments and diverse use cases?
- How can the framework be extended to consider more realistic environmental changes and diverse use cases?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies continual learning in LLMs and proposes a unified framework to evaluate different continual learning methods. The authors evaluate eight methods across four families using a suite of sequential LLM tasks, including domain adaptation, agentic tasks, financial analysis, and temporally-dependent knowledge updates. The results show that different learning methods have their strengths depending on how the task and data shift over time. All reviewers have raised some concerns about the scope of the paper, and the authors did not provide any rebuttal. Therefore, I recommend rejection.

### justification_for_why_not_higher_score

The paper has some limitations in the scope of the experiment.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (poster)