## Reviewer

### Summary

This paper proposes a new method for RLHF that decomposes reasoning into upstream and downstream phases, and uses a skip connection to concatenate the upstream segment with the original problem. The upstream phase receives dense rewards from downstream Monte Carlo sampling with single-stream optimization, while the downstream phase maintains group-relative optimization. The authors demonstrate the effectiveness of their method on mathematical benchmarks and out-of-domain tasks including general reasoning and code generation.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and shows good performance on various benchmarks.

### Weaknesses

- The proposed method is very similar to the existing method, DAPO (Yu et al., 2025b). The main difference is that DAPO uses a self-critic, while the proposed method uses a separate upstream and downstream phase. I think the authors should discuss more about the difference between the proposed method and DAPO. 
- The proposed method is not very efficient. It requires generating two separate segments, which is more computationally expensive than other methods that only generate one segment. 
- The authors should compare the proposed method with other methods that also use a separate upstream and downstream phase, such as Critique-GRPO (Zhang et al., 2025b).

### Questions

- How does the proposed method compare to other methods that use a separate upstream and downstream phase, such as Critique-GRPO (Zhang et al., 2025b)?
- How does the proposed method compare to other methods that use a self-critic, such as DAPO (Yu et al., 2025b)?
- What is the computational cost of the proposed method compared to other methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new approach for RLHF for LLMs. The key idea is to decompose reasoning into two phases: an upstream phase and a downstream phase. In the upstream phase, the model generates an early-stopped reasoning segment and receives Monte Carlo rewards aggregated from downstream continuations. In the downstream phase, the model maintains group-relative optimization with a skip connection that concatenates both the upstream segment and the original problem. The proposed method is evaluated on several benchmarks and shows improvements over the baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and shows good performance on various benchmarks.
- The ablation study is comprehensive and helps to understand the effectiveness of each component of the proposed method.

### Weaknesses

- The motivation of the proposed method is not clear. The authors claim that "fine-grained Monte Carlo rewards fail under practical budgets: high-variance advantages whose signs frequently flip, underperforming outcome-only GRPO." However, the authors do not provide a clear explanation of why this is the case. It is not clear why the proposed method is able to address this issue.
- The proposed method is not well-motivated. The authors claim that "we instantiate Monte Carlo trajectory sampling at a single intermediate position through an upstream-downstream architecture." However, it is not clear why this is the best approach. It is not clear why the authors chose to use a single intermediate position, and why this is better than other approaches.
- The proposed method is not well-motivated. The authors claim that "we employ an asymmetric optimization strategy using different algorithms for each phase." However, it is not clear why this is necessary. It is not clear why the authors chose to use different algorithms for each phase, and why this is better than using the same algorithm for both phases.

### Questions

- What is the motivation of the proposed method? Why does the proposed method address the issue of high-variance advantages?
- Why did the authors choose to use a single intermediate position for Monte Carlo trajectory sampling? Why is this better than other approaches?
- Why did the authors choose to use different algorithms for each phase of the proposed method? Why is this better than using the same algorithm for both phases?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel RLHF method called SKPO. The method decomposes reasoning into upstream and downstream phases. The upstream phase generates early-stopped reasoning segments and receives Monte Carlo rewards aggregated from downstream continuations. The downstream phase maintains group-relative optimization with a skip connection that concatenates both the upstream segment and the original problem. Experiments on several benchmarks show that the proposed method outperforms several baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and effective.
2. The paper is well-written and easy to follow.

### Weaknesses

1. The proposed method seems to be a combination of several existing methods. It would be better to provide a more detailed comparison with related works.
2. The experiments are not sufficient. It would be better to conduct experiments on more benchmarks and more models.

### Questions

1. Could you provide more details on how the proposed method differs from existing methods?
2. Could you provide more experiments on more benchmarks and more models?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel method for RLHF, which decomposes reasoning into upstream and downstream phases. The upstream phase generates early-stopped reasoning segments and receives Monte Carlo rewards aggregated from downstream continuations. The downstream phase maintains group-relative optimization with a skip connection that concatenates both the upstream segment and the original problem. The proposed method is evaluated on several benchmarks and shows improvements over the baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective.
3. The proposed method is evaluated on several benchmarks and shows improvements over the baselines.

### Weaknesses

1. The proposed method seems to be a combination of several existing methods. It would be better to provide a more detailed comparison with related works.
2. The experiments are not sufficient. It would be better to conduct experiments on more benchmarks and more models.
3. The proposed method is not very efficient. It requires generating two separate segments, which is more computationally expensive than other methods that only generate one segment.

### Questions

1. Could you provide more details on how the proposed method differs from existing methods?
2. Could you provide more experiments on more benchmarks and more models?
3. Could you provide more details on the computational cost of the proposed method compared to other methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new approach for RLHF for LLMs. The key idea is to decompose reasoning into two phases: an upstream phase and a downstream phase. In the upstream phase, the model generates an early-stopped reasoning segment and receives Monte Carlo rewards aggregated from downstream continuations. In the downstream phase, the model maintains group-relative optimization with a skip connection that concatenates both the upstream segment and the original problem. The proposed method is evaluated on several benchmarks and shows improvements over the baselines.

The reviewers have raised several concerns about the paper, including the motivation of the proposed method, the efficiency of the proposed method, the comparison with related works, and the experiments. The authors have responded to these concerns in their rebuttal. However, the reviewers still have some concerns about the paper. For example, Reviewer 7T5a has raised concerns about the motivation of the proposed method, and Reviewer 5uX4 has raised concerns about the efficiency of the proposed method. 

The AC has read the paper, the reviews, and the authors' responses. The AC agrees with the reviewers that the paper has some limitations and could be improved. However, the AC also thinks that the paper has some strengths, such as the proposed method is novel and shows good performance on various benchmarks. Considering the pros and cons, the AC recommends rejecting the paper.

### justification_for_why_not_higher_score

The paper has some limitations and could be improved.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)