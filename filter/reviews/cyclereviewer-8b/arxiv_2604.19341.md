## Reviewer

### Summary

The paper proposes a framework for scaling AI-driven discovery by structuring how evaluator queries are allocated and how evaluated histories are grown, filtered, and reused. The framework is applied to 28 open-ended problems across five domains and achieves state-of-the-art results.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed framework is well-motivated and the results are impressive.

### Weaknesses

I have the following concerns:

1. The paper does not clearly explain how the proposal constructor $\Phi$ is implemented. The authors mention that it is a graph-based variant of the PUCT rule, but they do not provide any details. It would be helpful to include a more detailed description of how $\Phi$ is implemented.

2. The paper does not provide any analysis of the computational efficiency of the proposed framework. How does the computational cost of the framework compare to other methods? How does the computational cost scale with the number of trajectories and the number of refinement steps?

3. The paper does not provide any analysis of the generalizability of the proposed framework. How well does the framework perform on new, unseen problems? How does the performance of the framework compare to other methods on new problems?

### Questions

See above.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a framework for scaling AI-driven scientific discovery by structuring the discovery loop. The framework is evaluated on 28 open-ended problems across five domains and achieves state-of-the-art results.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. 
- The proposed framework is well-motivated and the results are impressive.
- The framework is evaluated on a wide range of problems across five domains.

### Weaknesses

- The paper does not clearly explain how the proposal constructor $\Phi$ is implemented. 
- The paper does not provide any analysis of the computational efficiency of the proposed framework. 
- The paper does not provide any analysis of the generalizability of the proposed framework. 
- The paper does not provide any analysis of the robustness of the proposed framework to different hyperparameters.

### Questions

- How does the computational cost of the framework compare to other methods? 
- How does the computational cost scale with the number of trajectories and the number of refinement steps? 
- How well does the framework perform on new, unseen problems? 
- How does the performance of the framework compare to other methods on new problems? 
- How robust is the framework to different hyperparameters?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces SimpleTES, a framework for scaling AI-driven scientific discovery. SimpleTES is a test-time framework that structures the discovery loop by allocating evaluator queries and growing, filtering, and reusing evaluated histories. It achieves state-of-the-art results on 28 open-ended problems across five domains.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed framework is well-motivated and the results are impressive. The framework is evaluated on a wide range of problems across five domains. The paper also provides a comprehensive analysis of the computational efficiency and generalizability of the proposed framework.

### Weaknesses

The paper does not clearly explain how the proposal constructor $\Phi$ is implemented. The paper does not provide any analysis of the robustness of the proposed framework to different hyperparameters.

### Questions

How does the computational cost of the framework compare to other methods? How does the computational cost scale with the number of trajectories and the number of refinement steps? How well does the framework perform on new, unseen problems? How does the performance of the framework compare to other methods on new problems? How robust is the framework to different hyperparameters?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes SimpleTES, a framework for scaling AI-driven scientific discovery. SimpleTES is a test-time framework that structures the discovery loop by allocating evaluator queries and growing, filtering, and reusing evaluated histories. It achieves state-of-the-art results on 28 open-ended problems across five domains.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed framework is well-motivated and the results are impressive. The framework is evaluated on a wide range of problems across five domains. The paper also provides a comprehensive analysis of the computational efficiency and generalizability of the proposed framework.

### Weaknesses

The paper does not clearly explain how the proposal constructor $\Phi$ is implemented. The paper does not provide any analysis of the robustness of the proposed framework to different hyperparameters.

### Questions

How does the computational cost of the framework compare to other methods? How does the computational cost scale with the number of trajectories and the number of refinement steps? How well does the framework perform on new, unseen problems? How does the performance of the framework compare to other methods on new problems? How robust is the framework to different hyperparameters?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper introduces SimpleTES, a framework for scaling AI-driven scientific discovery. SimpleTES is a test-time framework that structures the discovery loop by allocating evaluator queries and growing, filtering, and reusing evaluated histories. It achieves state-of-the-art results on 28 open-ended problems across five domains.

The reviewers have raised several concerns regarding the paper. The main concerns are the lack of clarity in the implementation of the proposal constructor Φ, the lack of analysis of the computational efficiency and robustness of the proposed framework, and the lack of analysis of the generalizability of the proposed framework. The authors have provided responses to these concerns, but the reviewers have not found them to be satisfactory. Therefore, I recommend rejecting the paper.

### justification_for_why_not_higher_score

The reviewers have raised several concerns regarding the paper. The main concerns are the lack of clarity in the implementation of the proposal constructor Φ, the lack of analysis of the computational efficiency and robustness of the proposed framework, and the lack of analysis of the generalizability of the proposed framework. The authors have provided responses to these concerns, but the reviewers have not found them to be satisfactory. Therefore, I recommend rejecting the paper.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (poster)