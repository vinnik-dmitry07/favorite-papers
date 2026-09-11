## Reviewer

### Summary

This paper studies the trade-off between the two extreme continual learning strategies: joint task learning (JTL) and independent task learning (ITL). The authors propose a new objective, called Average Lifelong Error (ALE), which is the average of the expected loss over the next step. They also propose a new metric, called Transfer Efficiency, which measures the performance gain of JTL over ITL. The authors show that the Transfer Efficiency can be decomposed into two parts: Instability and Transient Error. They also propose a new algorithm, called Window, which interpolates between JTL and ITL.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a thorough theoretical analysis of the trade-off between JTL and ITL. The proposed metric, Transfer Efficiency, is a useful tool for evaluating the performance of continual learning algorithms. The authors also provide a new algorithm, Window, which interpolates between JTL and ITL.

### Weaknesses

The authors do not provide an experimental evaluation of the proposed algorithm, Window. It would be interesting to see how the Window algorithm compares to other continual learning algorithms in terms of Transfer Efficiency.

### Questions

How does the Window algorithm compare to other continual learning algorithms in terms of Transfer Efficiency?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the trade-off between Joint Task Learning (JTL) and Independent Task Learning (ITL) in continual learning. The authors introduce the Average Lifelong Error (ALE) objective, which is the average of the expected loss over the next step. They also introduce the Transfer Efficiency metric, which measures the performance gain of JTL over ITL. The authors show that the Transfer Efficiency can be decomposed into two parts: Instability and Transient Error. They also propose a new algorithm, called Window, which interpolates between JTL and ITL.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a thorough theoretical analysis of the trade-off between JTL and ITL. The proposed metric, Transfer Efficiency, is a useful tool for evaluating the performance of continual learning algorithms. The authors also provide a new algorithm, Window, which interpolates between JTL and ITL.

### Weaknesses

The authors do not provide an experimental evaluation of the proposed algorithm, Window. It would be interesting to see how the Window algorithm compares to other continual learning algorithms in terms of Transfer Efficiency.

### Questions

How does the Window algorithm compare to other continual learning algorithms in terms of Transfer Efficiency?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper challenges the conventional wisdom in continual learning that the goal is to retain all previously acquired knowledge. The authors argue that in non-stationary environments, prioritizing retention can impede real-time adaptation. They introduce Transfer Efficiency as a measure of the tension between Instability (bias from conflicting past experience) and Transient Error (optimization cost of learning new tasks from scratch). They derive a Critical Task Duration beyond which historical knowledge transitions from a warm-start advantage to an optimization liability. The authors also propose Predictive Continual Learning, which optimizes expected future performance under an explicit, dynamically updated model of future tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors provide a thorough theoretical analysis of the trade-off between JTL and ITL.
- The proposed metric, Transfer Efficiency, is a useful tool for evaluating the performance of continual learning algorithms.
- The authors also provide a new algorithm, Window, which interpolates between JTL and ITL.

### Weaknesses

- The authors do not provide an experimental evaluation of the proposed algorithm, Window. It would be interesting to see how the Window algorithm compares to other continual learning algorithms in terms of Transfer Efficiency.
- The authors do not provide an experimental evaluation of the proposed algorithm, Window. It would be interesting to see how the Window algorithm compares to other continual learning algorithms in terms of Transfer Efficiency.

### Questions

- How does the Window algorithm compare to other continual learning algorithms in terms of Transfer Efficiency?
- Can the authors provide an experimental evaluation of the proposed algorithm, Window? It would be interesting to see how the Window algorithm compares to other continual learning algorithms in terms of Transfer Efficiency.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper challenges the conventional wisdom that the goal of continual learning is to retain all previously acquired knowledge. The authors argue that in non-stationary environments, prioritizing retention can impede real-time adaptation. They introduce Transfer Efficiency as a measure of the tension between Instability (bias from conflicting past experience) and Transient Error (optimization cost of learning new tasks from scratch). They derive a Critical Task Duration beyond which historical knowledge transitions from a warm-start advantage to an optimization liability. The authors also propose Predictive Continual Learning, which optimizes expected future performance under an explicit, dynamically updated model of future tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors provide a thorough theoretical analysis of the trade-off between JTL and ITL.
- The proposed metric, Transfer Efficiency, is a useful tool for evaluating the performance of continual learning algorithms.
- The authors also provide a new algorithm, Window, which interpolates between JTL and ITL.

### Weaknesses

- The authors do not provide an experimental evaluation of the proposed algorithm, Window. It would be interesting to see how the Window algorithm compares to other continual learning algorithms in terms of Transfer Efficiency.
- The authors do not provide an experimental evaluation of the proposed algorithm, Window. It would be interesting to see how the Window algorithm compares to other continual learning algorithms in terms of Transfer Efficiency.

### Questions

How does the Window algorithm compare to other continual learning algorithms in terms of Transfer Efficiency?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a novel perspective on continual learning, arguing that the traditional goal of retaining all previously acquired knowledge may not be universally optimal, especially in non-stationary environments. The authors introduce Transfer Efficiency as a measure of the trade-off between Instability (bias from conflicting past experience) and Transient Error (optimization cost of learning new tasks from scratch). They also propose Predictive Continual Learning, which optimizes expected future performance under an explicit, dynamically updated model of future tasks. The paper provides a theoretical analysis of the trade-off between Joint Task Learning (JTL) and Independent Task Learning (ITL) and proposes a new algorithm, Window, which interpolates between JTL and ITL. The paper is well-written and provides a thorough theoretical analysis of the trade-off between JTL and ITL. The proposed metric, Transfer Efficiency, is a useful tool for evaluating the performance of continual learning algorithms. The authors also provide a new algorithm, Window, which interpolates between JTL and ITL.

### justification_for_why_not_higher_score

The paper is well-written and provides a thorough theoretical analysis of the trade-off between JTL and ITL. The proposed metric, Transfer Efficiency, is a useful tool for evaluating the performance of continual learning algorithms. The authors also provide a new algorithm, Window, which interpolates between JTL and ITL.

### justification_for_why_not_lower_score

The paper is well-written and provides a thorough theoretical analysis of the trade-off between JTL and ITL. The proposed metric, Transfer Efficiency, is a useful tool for evaluating the performance of continual learning algorithms. The authors also provide a new algorithm, Window, which interpolates between JTL and ITL.

**********

## Paper Decision

Accept (poster) (poster) **********

*Note:* Please see the paper decision policy for the explanation of the poster acceptance.

**********

# Paper Decision Summary

This paper proposes a novel perspective on continual learning, arguing that the traditional goal of retaining all previously acquired knowledge may not be universally optimal, especially in non-stationary environments. The authors introduce Transfer Efficiency as a measure of the trade-off between Instability (bias from conflicting past experience) and Transient Error (optimization cost of learning new tasks from scratch). They also propose Predictive Continual Learning, which optimizes expected future performance under an explicit, dynamically updated model of future tasks. The paper provides a theoretical analysis of the trade-off between Joint Task Learning (JTL) and Independent Task Learning (ITL) and proposes a new algorithm, Window, which interpolates between JTL and ITL. The paper is well-written and provides a thorough theoretical analysis of the trade-off between JTL and ITL. The proposed metric, Transfer Efficiency, is a useful tool for evaluating the performance of continual learning algorithms. The authors also provide a new algorithm, Window, which interpolates between JTL and ITL.

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
* The paper has a moderate level of technical soundness.
* The paper is of moderate quality and interest.

**********

**********

# Paper Decision Policy

## Accept (poster)

* The paper is of interest to the ICLR community.
