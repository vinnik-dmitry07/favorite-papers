## Reviewer

### Summary

This paper proposes Meta-Harness, an outer-loop system that searches over harness code for LLM applications. The proposed method uses an agentic proposer that accesses the source code, scores, and execution traces of all prior candidates through a filesystem. Experimental results show that the proposed method outperforms state-of-the-art context management systems.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is intuitive and reasonable.

### Weaknesses

- The proposed method is limited to the LLM-based coding agent. It is not clear whether the proposed method can be generalized to other types of agents.
- The proposed method requires a large amount of memory to store the source code, scores, and execution traces of all prior candidates. It is not clear whether the proposed method can be applied to resource-constrained environments.
- The proposed method requires a large amount of computational resources to train the LLM-based coding agent. It is not clear whether the proposed method can be applied to resource-constrained environments.

### Questions

- The proposed method requires a large amount of memory to store the source code, scores, and execution traces of all prior candidates. It is not clear whether the proposed method can be applied to resource-constrained environments.
- The proposed method requires a large amount of computational resources to train the LLM-based coding agent. It is not clear whether the proposed method can be applied to resource-constrained environments.
- The proposed method is limited to the LLM-based coding agent. It is not clear whether the proposed method can be applied to other types of agents.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a method for optimizing LLM-based systems by searching over their harnesses. The authors propose a method that uses a coding agent to search over the space of possible harnesses. The search agent is able to access the source code, scores, and execution traces of all prior candidates through a filesystem. The authors evaluate their method on three different tasks: online text classification, math reasoning, and agentic coding. The results show that the proposed method outperforms state-of-the-art methods on these tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is intuitive and reasonable.

### Weaknesses

The paper is not clear about the limitations of the proposed method. The authors do not discuss the limitations of the method and how they can be addressed. The authors also do not discuss the potential risks of using the proposed method.

### Questions

How does the proposed method compare to other methods for optimizing LLM-based systems?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents Meta-Harness, a method for optimizing large language model (LLM) systems by searching over their harnesses. The authors propose a coding agent that accesses the source code, scores, and execution traces of all prior candidates through a filesystem. They evaluate Meta-Harness on three tasks: online text classification, math reasoning, and agentic coding. The results show that Meta-Harness outperforms state-of-the-art context management systems and hand-engineered baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is intuitive and reasonable.
3. The authors provide a detailed description of the method and its implementation.
4. The evaluation is comprehensive and includes three different tasks.

### Weaknesses

1. The paper does not provide a clear description of the limitations of the proposed method.
2. The paper does not discuss the potential risks of using the proposed method.
3. The paper does not provide a comparison of the proposed method with other methods for optimizing LLM-based systems.

### Questions

1. How does the proposed method compare to other methods for optimizing LLM-based systems?
2. What are the potential risks of using the proposed method?
3. What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to search for the best LLM harness. The authors propose a search algorithm that uses a coding agent to search for the best LLM harness. The coding agent is a LLM that can modify code. The search algorithm uses a population of candidate harnesses and evaluates each one on a search set. The candidate harnesses are modified based on the evaluation results. The search algorithm is evaluated on three tasks: online text classification, math reasoning, and agentic coding. The results show that the proposed method can find better harnesses than hand-engineered ones.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is intuitive and reasonable.
3. The evaluation is comprehensive and includes three different tasks.

### Weaknesses

1. The paper does not provide a clear description of the limitations of the proposed method.
2. The paper does not discuss the potential risks of using the proposed method.
3. The paper does not provide a comparison of the proposed method with other methods for optimizing LLM-based systems.

### Questions

1. How does the proposed method compare to other methods for optimizing LLM-based systems?
2. What are the potential risks of using the proposed method?
3. What are the limitations of the proposed method?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a method for optimizing LLM-based systems by searching over their harnesses. The authors propose a method that uses a coding agent to search over the space of possible harnesses. The search agent is able to access the source code, scores, and execution traces of all prior candidates through a filesystem. The authors evaluate their method on three different tasks: online text classification, math reasoning, and agentic coding. The results show that the proposed method outperforms state-of-the-art methods on these tasks.

The reviewers generally agree that the paper is well-written and easy to follow. The proposed method is intuitive and reasonable. The evaluation is comprehensive and includes three different tasks.

However, the reviewers also raised several concerns about the limitations of the proposed method. The authors did not provide a clear description of the limitations of the proposed method. The authors did not discuss the potential risks of using the proposed method. The authors did not provide a comparison of the proposed method with other methods for optimizing LLM-based systems.

### justification_for_why_not_higher_score

The reviewers raised several concerns about the limitations of the proposed method. The authors did not provide a clear description of the limitations of the proposed method. The authors did not discuss the potential risks of using the proposed method. The authors did not provide a comparison of the proposed method with other methods for optimizing LLM-based systems.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for spotlight) -> Not good enough

**********

## Paper Decision Summary

This paper proposes a method for optimizing LLM-based systems by searching over their harnesses. The authors propose a method that uses a coding agent to search over the space of possible harnesses. The search agent is able to access the source code, scores, and execution traces of all prior candidates through a filesystem. The authors evaluate their method on three different tasks: online text classification, math reasoning, and agentic coding. The results show that the proposed method outperforms state-of-the-art methods on these tasks.

The reviewers generally agree that the paper is well-written and easy to follow. The proposed method is intuitive and reasonable. The evaluation is comprehensive and includes three different tasks.

However, the reviewers also raised several concerns about the limitations of the proposed method. The authors did not provide a clear description of the limitations of the proposed method. The authors did not discuss the potential risks of using the proposed method. The authors did not provide a comparison of the proposed method with other methods for optimizing LLM-based systems.

### justification_for_why_not_higher_score

The reviewers raised several concerns about the limitations of the proposed method. The authors did not provide a clear description of the limitations of the proposed method. The authors did not discuss the potential risks of using the proposed method. The authors did not provide a comparison of the proposed method with other methods for optimizing LLM-based systems.

### justification_for_why_not_lower_score

N/A

**********

<!-- Paper Decision: Reject (not selected for spotlight) -->