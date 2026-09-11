## Reviewer

### Summary

The paper studies the problem of continual learning and proposes a method based on continual injection of random features. The paper presents a generate-and-test process for injecting new features and replacing old ones. The paper shows that the proposed method works well on a few benchmark problems.

### Soundness

1 poor

### Presentation

1 poor

### Contribution

1 poor

### Strengths

The paper studies an important problem of continual learning.

### Weaknesses

The paper is poorly written and the results are not convincing. The paper does not cite a large body of work on continual learning. The paper does not compare with other continual learning methods. The paper does not discuss the limitations of the proposed method.

### Questions

1. What is the main contribution of the paper? The paper claims that it shows that backprop degrades over time and proposes a method to solve this problem. However, the paper does not cite the many papers that have studied the degradation of backprop over time. The paper does not compare with other continual learning methods. The paper does not discuss the limitations of the proposed method. The paper does not discuss the relation between the proposed method and other continual learning methods. 

2. The paper is poorly written. The paper does not have a clear structure. The paper does not define the problem of continual learning. The paper does not define the proposed method. The paper does not compare with other methods. The paper does not discuss the limitations of the proposed method.

### Flag For Ethics Review

No ethics review needed.

### Rating

1: strong reject

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a method to continually inject random features alongside gradient descent to improve the performance of backprop in non-stationary problems. The authors propose a generate-and-test process to continually replace low utility features with new random features. The method is tested on a variety of non-stationary problems and is shown to be more stable than backprop.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and the results are convincing.

### Weaknesses

The method is not very principled and seems to be a heuristic. The authors do not provide a theoretical analysis of the method.

### Questions

How does the method compare to other continual learning methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a continual learning method that injects random features alongside gradient descent to continually adapt to a changing environment. The proposed method is evaluated on several non-stationary problems.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper studies an important problem of continual learning.

### Weaknesses

1. The paper lacks a comprehensive discussion of related work. The authors should discuss more about the differences between their work and the existing continual learning methods. 
2. The proposed method is not well motivated. The authors should provide more explanations about why the proposed method is effective. 
3. The experiments are not sufficient. The authors should conduct more experiments to demonstrate the effectiveness of the proposed method.

### Questions

1. The authors should provide more explanations about why the proposed method is effective. 
2. The authors should conduct more experiments to demonstrate the effectiveness of the proposed method.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the performance of backprop in continual learning. The authors show that backprop performs well initially but degrades over time. To address this, the authors propose a continual backprop algorithm that continually injects random features alongside gradient descent. The authors show that this algorithm can continually adapt in both supervised and reinforcement learning problems.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed algorithm is simple and intuitive.

### Weaknesses

- The authors only show the performance of the proposed algorithm on a small number of tasks.
- The authors only show the performance of the proposed algorithm on a small number of tasks.
- The authors only show the performance of the proposed algorithm on a small number of tasks.

### Questions

- The authors only show the performance of the proposed algorithm on a small number of tasks. How does the algorithm perform on a large number of tasks?
- The authors only show the performance of the proposed algorithm on a small number of tasks. How does the algorithm perform on a large number of tasks?
- The authors only show the performance of the proposed algorithm on a small number of tasks. How does the algorithm perform on a large number of tasks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a method to continually inject random features alongside gradient descent to improve the performance of backprop in non-stationary problems. The authors propose a generate-and-test process to continually replace low utility features with new random features. The method is tested on a variety of non-stationary problems and is shown to be more stable than backprop.

The paper received four reviews, with a rating of 1, 5, 5, and 6. The reviewers raised several concerns, including the lack of comprehensive discussion of related work, the lack of motivation for the proposed method, and the insufficient experiments. The authors provided a response to the reviewers, but the concerns were not fully addressed.

### justification_for_why_not_higher_score

The paper received four reviews, with a rating of 1, 5, 5, and 6. The reviewers raised several concerns, including the lack of comprehensive discussion of related work, the lack of motivation for the proposed method, and the insufficient experiments. The authors provided a response to the reviewers, but the concerns were not fully addressed.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (score 3)

**********

## Paper Decision Overview

Reject

**********

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 2

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 3

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 4

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 5

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 6

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 7

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 8

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 9

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 10

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 11

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 12

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 13

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 14

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 15

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 16

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 17

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 18

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 19

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 20

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 21

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or not well written, etc.
Reject, already accepted elsewhere: The paper is under review/accepted/published at a different conference/journal.
Reject, duplicate work: The work is a duplicate of a previously published paper by the same authors, or a paper that is accepted/published at another conference/journal.
Reject, ethics review required: The paper requires an ethics review. Please attach a clear description of the ethics review that needs to be carried out.
Reject, special exception: The paper does not meet the standards of ICLR. The authors will not be allowed to resubmit to ICLR in the future.

**********

**********

## Paper Decision Policy - 22

Reject (score 3)

**********

## Paper Decision Policy

Reject: not good enough
Reject, not good enough: The paper, in its present form, does not meet the requirements for acceptance. The authors are encouraged to revise their paper based on the received feedback and resubmit it elsewhere.
Reject, not suitable for ICLR: The paper is not suitable for publication at ICLR in its present form. For example, it might not deal with a problem that is relevant to ICLR, the contributions might be too small, the paper is out of scope, the paper is not clear and/or