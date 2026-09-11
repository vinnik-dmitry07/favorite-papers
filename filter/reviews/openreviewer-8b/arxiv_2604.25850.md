# Review

## Summary
This paper introduces a method for automated harness engineering for coding agents. The authors propose a three-step pipeline that first collects traces from the agent, then analyzes the traces to identify failure patterns and root causes, and finally applies edits to the harness based on the root causes. The authors conduct experiments on Terminal-Bench2 and SWE-bench-verified, and demonstrate that their method outperforms human-designed harnesses and other automated baselines.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is simple and intuitive.
- The authors conduct comprehensive experiments and ablation studies to show the effectiveness of their method.

## Weaknesses
- The proposed method is only evaluated on two benchmarks, and the improvement on one of the benchmarks is not very significant.
- The proposed method requires a lot of steps and tokens to evolve the harness, and it is not clear if it is worth the cost.
- The proposed method is only evaluated on coding tasks. It is not clear if the method can be applied to other types of tasks.

## Questions
- How does the proposed method compare to other methods in terms of the number of steps and tokens required?
- Can the proposed method be applied to non-coding tasks?
- How does the proposed method compare to other methods in terms of the robustness to the choice of initial harness?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4