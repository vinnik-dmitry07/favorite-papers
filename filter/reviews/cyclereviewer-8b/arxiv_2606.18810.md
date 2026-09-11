## Reviewer

### Summary

This paper proposes a new method for credit assignment in reinforcement learning with verifiable rewards (RLVR). The method is based on the observation that conditioning the model on its own verified trajectories induces a measurable per-token KL divergence between the original and conditioned distributions. The authors propose to use this KL divergence as a multiplicative weight on GRPO gradients. The method is evaluated on five benchmarks spanning math, code, and agentic tasks and is shown to outperform existing methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.

### Weaknesses

- The novelty of the paper is limited. The idea of using KL divergence as a multiplicative weight on gradients is not new and has been explored in other contexts. The novelty of the paper lies in the application of this idea to RLVR and the observation that conditioning the model on its own verified trajectories induces a measurable per-token KL divergence between the original and conditioned distributions.
- The empirical evaluation is limited to a small set of benchmarks and does not include a comprehensive comparison with existing methods.

### Questions

- How does the proposed method compare to other methods for credit assignment in RLVR? 
- How does the proposed method perform on larger models and longer responses?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes SC-GRPO, a method for credit assignment in RL with verifiable rewards. The method uses a self-conditioned teacher to measure the per-token distributional shift between the teacher and the original student. The paper shows that SC-GRPO outperforms existing methods on five benchmarks spanning math, code, and agentic tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The paper provides a comprehensive evaluation of the proposed method on five benchmarks.

### Weaknesses

1. The paper only evaluates the proposed method on a small set of benchmarks. It would be interesting to see how the method performs on a larger set of benchmarks.
2. The paper does not provide a detailed analysis of the computational overhead of the proposed method. It would be interesting to see a more detailed analysis of the computational overhead.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. It would be interesting to see a more detailed analysis of the limitations of the method.

### Questions

1. How does the proposed method compare to other methods for credit assignment in RL with verifiable rewards?
2. How does the proposed method perform on larger models and longer responses?
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

The paper proposes a method for token-level credit assignment in reinforcement learning with verifiable rewards (RLVR). The method is based on self-conditioned GRPO, where the KL divergence between the original and conditioned distributions is used as a multiplicative weight on GRPO gradients. The method is evaluated on five benchmarks and is shown to outperform existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and effective. The paper provides a comprehensive evaluation of the proposed method on five benchmarks. The paper also provides a detailed analysis of the computational overhead of the proposed method.

### Weaknesses

The paper only evaluates the proposed method on a small set of benchmarks. It would be interesting to see how the method performs on a larger set of benchmarks. The paper does not provide a detailed analysis of the limitations of the proposed method. It would be interesting to see a more detailed analysis of the limitations of the method.

### Questions

How does the proposed method compare to other methods for credit assignment in RL with verifiable rewards? How does the proposed method perform on larger models and longer responses?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new method for credit assignment in RL with verifiable rewards (RLVR). The method is based on self-conditioned GRPO, where the KL divergence between the original and conditioned distributions is used as a multiplicative weight on GRPO gradients. The method is evaluated on five benchmarks and is shown to outperform existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and effective. The paper provides a comprehensive evaluation of the proposed method on five benchmarks. The paper also provides a detailed analysis of the computational overhead of the proposed method.

### Weaknesses

The paper only evaluates the proposed method on a small set of benchmarks. It would be interesting to see how the method performs on a larger set of benchmarks. The paper does not provide a detailed analysis of the limitations of the proposed method. It would be interesting to see a more detailed analysis of the limitations of the method.

### Questions

How does the proposed method compare to other methods for credit assignment in RL with verifiable rewards? How does the proposed method perform on larger models and longer responses?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper presents a method for credit assignment in RL with verifiable rewards (RLVR) by using a self-conditioned teacher to measure the per-token distributional shift between the teacher and the original student. The method is evaluated on five benchmarks and shown to outperform existing methods. The paper is well-written and easy to follow, and the proposed method is simple and effective. The paper provides a comprehensive evaluation of the proposed method on five benchmarks and a detailed analysis of the computational overhead of the proposed method. However, the paper only evaluates the proposed method on a small set of benchmarks and does not provide a detailed analysis of the limitations of the proposed method. The paper does not provide a detailed analysis of the limitations of the method.

### justification_for_why_not_higher_score

The paper only evaluates the proposed method on a small set of benchmarks and does not provide a detailed analysis of the limitations of the proposed method.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster) (out of 5: accept spotlight, accept poster, accept paper, reject, very strong reject)

**********

## Paper Decision (public)

Reject

**********

## Paper Decision (machine)

Reject

**********

## Paper Decision (diff)

-1

**********

## Paper Decision (conflict)

0

**********

## Paper Decision (weak_conflict)

0

**********

## Paper Decision (already_accepted_elsewhere)

0

**********

## Paper Decision (not_our_paper)

0

**********

## Paper Decision (not_my_area_of_expertise)

0

**********

## Paper Decision (poster)

0

**********

## Paper Decision (spotlight)

0

**********

## Paper Decision (oral)

0

**********

## Paper Decision (special)

0

**********

## Paper Decision (workshop)

0

**********

## Paper Decision (other)

0

**********

## Paper Decision (accept)

0

**********

## Paper Decision (acceptposter)

0

**********

## Paper Decision (acceptspotlight)

0

**********

## Paper Decision (acceptoral)

0

**********

## Paper Decision (acceptspecial)

0

**********

## Paper Decision (acceptworkshop)

0

**********

## Paper Decision (acceptother)

0

**********

## Paper Decision (rejectrebuttal)

0

**********

## Paper Decision (notmyday)

0

**********

## Paper Decision (accept)

0

**********

## Paper Decision (reject)

1

**********

## Paper Decision (withdrawn)

-1

**********

## Paper Decision (unsubmitted)

-1

**********

## Paper Decision (unrefereed)

-1

**********

## Paper Decision (do_not_referee)

-1

**********

## Paper Decision (already_rejected)

-1

**********

## Paper Decision (not submitted yet)

-1

**********

## Paper Decision (underpeerreview)

-1

**********

## Paper Decision (undereditorreview)

-1

**********

## Paper Decision (awaitingauthor)

-1

**********

## Paper Decision (awaitingreferees)

-1

**********

## Paper Decision (inreviewer)

-1

**********

## Paper Decision (ineditor)

-1

**********

## Paper Decision (abandoned)

-1

**********

## Paper Decision (unpublished)

-1

**********

## Paper Decision (published)

1

**********

## Paper Decision (deleted)

-1

**********

## Paper Decision (requiremajorrevision)

0

**********

## Paper Decision (requireminorrevision)

0

**********

## Paper Decision (accept)

0

**********

## Paper Decision (notacceptable)

-1

**********

## Paper Decision (toanotherconference)

-1

**********

## Paper Decision (electtoaccept)

1

**********

## Paper Decision (electtoreject)

-1

**********

## Paper Decision (endorsetoreject)

-1

**********

## Paper Decision (endorsetoaccept)

1

**********

## Paper Decision (reviewer)

-1

**********

## Paper Decision (pc)

0

**********

## Paper Decision (admin)

1

**********

**********

**********

## Paper Decision (elect)

0

**********

## Paper Decision (conf)

0

**********

## Paper Decision (ac)

0

**********

## Paper Decision (sm)

0

**********

## Paper Decision (chair)

0

**********

## Paper Decision (localchair)

0

**********

## Paper Decision (final)

0

**********

## Paper Decision (other1)

0

**********

## Paper Decision (other2)

0

**********

## Paper Decision (other3)

0

**********

## Paper Decision (other4)

0

**********

## Paper Decision (other5)

0

**********

## justification_for_why_not_higher_score

N/A

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_poster

N/A

**********

## justification_for_why_not_spotlight

N/A

**********

## justification_for_why_not_oral

N/A

**********

## justification_for_why_not_accept

N/A

**********

## justification_for_why_not_acceptposter

N/A

**********

## justification_for_why_not_acceptspotlight

N/A

**********

## justification_for_why_not_acceptoral

N/A

**********

## justification_for_why_not_acceptspecial

N/A

**********

## justification_for_why_not_acceptworkshop

N/A

**********

## justification_for_why_not_acceptother

N/A

**********

## justification_for_why_not_reject

N/A

**********

## justification_for_why_not_unsubmitted

N/A

**********

## justification_for_why_not_unrefereed

N/A

**********

## justification_for_why_not_do_not_referee

N/A

**********

## justification_for_why_not_already_rejected

N/A

**********

## justification_for_why_not_inreviewer

N/A

**********

## justification_for_why_not_ineditor

N/A

**********

## justification_for_why_not_abandoned

N/A

**********

## justification_for_why_not_unpublished

N/A

**********

## justification_for_why_not_published

N/A

**********

## justification_for_why_not_deleted

N/A

**********

## justification_for_why_not_requiremajorrevision

N/A

**********

## justification_for_why_not_requireminorrevision

N/A

**********

## justification_for_why_not_accept

N/A

**********

## justification_for_why_not_notacceptable

N/A

**********

## justification_for_why_not_toanotherconference

N/A

**********

## justification_for_why_not_electtoaccept

N/A

**********

## justification_for_why_not_electtoreject

N/A

**********

## justification_for_why_not_endorsetoreject

N/A

**********

## justification_for_why_not_endorsetoaccept

N/A

**********

## justification_for_why_not_reviewer

N/A

**********

## justification_for_why_not_pc

N/A

**********

## justification_for_why_not_admin

N/A

**********

## justification_for_why_not_elect

N/A

**********

## justification_for_why_not_conf

N/A

**********

## justification_for_why_not_ac

N/A

**********

## justification_for_why_not_sm

N/A

**********

## justification_for_why_not_chair

N/A

**********

## justification_for_why_not_localchair

N/A

**********

## justification_for_why_not_final

N/A

**********

## justification_for_why_not_other1

N/A

**********

## justification_for_why_not_other2

N/A

**********

## justification_for_why_not_other3

N/A

**********

## justification_for_why_not_other4

N/A

**********

## justification_for_why_not_other5

N/A

**********

**********

## Paper Decision (conf)

0

**********

## Paper Decision (ac)

0

**********

## Paper Decision (sm)

0

**********

## Paper Decision (chair)

0

**********

## Paper Decision (localchair)

0

**********

## Paper Decision (final)

0

**********

## Paper Decision (other1)

0

**********

## Paper Decision (other2)

0

**********

## Paper Decision (other3)

0

**********

## Paper Decision (other4)

0

**********

## Paper Decision (other5)

0

**********

## Paper Decision (other)

0

**********

## Paper Decision (rejectrebuttal)

0

**********

## Paper Decision (notmyday)

0

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

********