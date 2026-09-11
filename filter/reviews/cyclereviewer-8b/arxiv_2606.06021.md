## OPRD: On-Policy Representation Distillation

### Summary

The paper proposes a new approach to on-policy distillation, which is to distill the model in the hidden-state space. The authors propose a new loss function that minimizes the MSE between the hidden states of the student and the teacher model. They also propose a new method called OPRD-Bridge, which extends the proposed method to cross-architecture setting. The authors evaluate the proposed method on several benchmarks and show that it outperforms the baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper proposes a new approach to on-policy distillation, which is to distill the model in the hidden-state space. This is a novel idea and the proposed method is simple and easy to understand.

The proposed method is evaluated on several benchmarks and shows promising results.

### Weaknesses

The paper proposes a new approach to on-policy distillation, which is to distill the model in the hidden-state space. However, the paper does not provide a thorough analysis of the proposed method. For example, it is not clear how the proposed method compares to other distillation methods, such as knowledge distillation and distillation with reinforcement learning. It would be helpful to provide a more comprehensive comparison with other methods.

The paper also does not provide a thorough analysis of the experimental results. For example, it is not clear how the proposed method performs on different types of tasks, such as language translation and image classification. It would be helpful to provide a more comprehensive analysis of the experimental results.

### Questions

How does the proposed method compare to other distillation methods, such as knowledge distillation and distillation with reinforcement learning?

How does the proposed method perform on different types of tasks, such as language translation and image classification?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new approach to on-policy distillation called OPRD, which aligns student and teacher representations across selected layers on the same on-policy rollouts, providing dense, deterministic, per-layer supervision while bypassing the LM head entirely. The paper also proposes a cross-architecture extension called OPRD-Bridge, which uses a frozen projector pair to align representations across arbitrary depth/width mismatches. The paper provides a theoretical analysis of OPRD and evaluates it on competition mathematics benchmarks, showing that it closes the student-teacher gap where every output-space baseline plateaus, while training 1.44 × faster and using up to 54% less memory.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The theoretical analysis is solid and provides good insights into the proposed method.

### Weaknesses

1. The proposed method is only evaluated on competition mathematics benchmarks, it would be better to evaluate it on other tasks such as QA, summarization, and translation.
2. The ablation study is not sufficient, it would be better to provide more ablation studies on the hyper-parameters of the proposed method.

### Questions

1. How does the proposed method perform on other tasks such as QA, summarization, and translation?
2. How sensitive is the proposed method to the hyper-parameters?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a novel approach to distill on-policy representation, which is a novel idea. The paper is well-written and the proposed method is well-motivated. The experiments show that the proposed method is effective in distilling on-policy representations.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel approach to distill on-policy representation, which is a novel idea. 
2. The paper is well-written and the proposed method is well-motivated. 
3. The experiments show that the proposed method is effective in distilling on-policy representations.

### Weaknesses

1. The proposed method requires the teacher and student to share the same architecture. This is a limitation of the proposed method, as it is not always possible to have the same architecture for the teacher and student models. 
2. The proposed method is only evaluated on competition mathematics benchmarks, it would be better to evaluate it on other tasks such as QA, summarization, and translation.
3. The ablation study is not sufficient, it would be better to provide more ablation studies on the hyper-parameters of the proposed method.

### Questions

1. How does the proposed method perform on other tasks such as QA, summarization, and translation?
2. How sensitive is the proposed method to the hyper-parameters?
3. What is the computational cost of the proposed method compared to other distillation methods?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a new method for on-policy distillation, which is a common practice in training LLMs. The authors argue that the current on-policy distillation methods have two limitations: (1) high variance of the gradient estimator and (2) information bottleneck. To address these limitations, the authors propose a new method called OPRD, which distills the representation of the student and teacher models. The authors also propose a method called OPRD-Bridge, which allows distillation across different architectures. The authors evaluate their method on several benchmarks and show that it outperforms the baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors do a good job of explaining the limitations of current on-policy distillation methods and how their method addresses these limitations. 
2. The proposed method is novel and shows promising results on several benchmarks. 
3. The authors provide a theoretical analysis of their method and show that it has a deterministic per-sample gradient, which removes the token-level estimation variance of OPD's gradient estimator.

### Weaknesses

1. The authors only evaluate their method on a single benchmark, which is the DAPO-Math-17K dataset. It would be good to evaluate the method on other benchmarks, such as AIME 2024 and AIME 2025. 
2. The authors do not provide a comparison with other on-policy distillation methods, such as OPD with top-k sampling. It would be good to compare the proposed method with these methods. 
3. The authors do not provide a comparison with other distillation methods, such as knowledge distillation and distillation with reinforcement learning. It would be good to compare the proposed method with these methods. 
4. The authors do not provide a comparison with other methods that address the information bottleneck problem, such as using a different loss function or a different architecture. It would be good to compare the proposed method with these methods. 
5. The authors do not provide a comparison with other methods that address the high variance of the gradient estimator problem, such as using a different optimizer or a different learning rate schedule. It would be good to compare the proposed method with these methods.

### Questions

1. How does the proposed method compare to other on-policy distillation methods, such as OPD with top-k sampling?
2. How does the proposed method compare to other distillation methods, such as knowledge distillation and distillation with reinforcement learning?
3. How does the proposed method compare to other methods that address the information bottleneck problem, such as using a different loss function or a different architecture?
4. How does the proposed method compare to other methods that address the high variance of the gradient estimator problem, such as using a different optimizer or a different learning rate schedule?
5. How does the proposed method compare to other methods that address the information bottleneck problem, such as using a different loss function or a different architecture?
6. How does the proposed method compare to other methods that address the high variance of the gradient estimator problem, such as using a different optimizer or a different learning rate schedule?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents a novel approach to on-policy distillation, which is a common practice in training LLMs. The authors argue that the current on-policy distillation methods have two limitations: (1) high variance of the gradient estimator and (2) information bottleneck. To address these limitations, the authors propose a new method called OPRD, which distills the representation of the student and teacher models. The authors also propose a method called OPRD-Bridge, which allows distillation across different architectures. The authors evaluate their method on several benchmarks and show that it outperforms the baselines.

The paper is well-written and easy to follow. The authors do a good job of explaining the limitations of current on-policy distillation methods and how their method addresses these limitations. The proposed method is novel and shows promising results on several benchmarks. The authors provide a theoretical analysis of their method and show that it has a deterministic per-sample gradient, which removes the token-level estimation variance of OPD's gradient estimator.

However, the paper only evaluates their method on a single benchmark, which is the DAPO-Math-17K dataset. It would be good to evaluate the method on other benchmarks, such as AIME 2024 and AIME 2025. The authors do not provide a comparison with other on-policy distillation methods, such as OPD with top-k sampling. It would be good to compare the proposed method with these methods. The authors do not provide a comparison with other distillation methods, such as knowledge distillation and distillation with reinforcement learning. It would be good to compare the proposed method with these methods.

### justification_for_why_not_higher_score

The paper only evaluates their method on a single benchmark, which is the DAPO-Math-17K dataset. It would be good to evaluate the method on other benchmarks, such as AIME 2024 and AIME 2025. The authors do not provide a comparison with other on-policy distillation methods, such as OPD with top-k sampling. It would be good to compare the proposed method with these methods. The authors do not provide a comparison with other distillation methods, such as knowledge distillation and distillation with reinforcement learning. It would be good to compare the proposed method with these methods.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Summary

The paper proposes a novel approach to on-policy distillation, which is to distill the model in the hidden-state space. The paper is well-written and the proposed method is simple and easy to understand. The proposed method is evaluated on several benchmarks and shows promising results. However, the paper does not provide a thorough analysis of the proposed method, and the experiments are limited to a single benchmark. The authors do not provide a comparison with other distillation methods, such as knowledge distillation and distillation with reinforcement learning. It would be good to compare the proposed method with these methods. The authors do not provide a comparison with other methods that address the information bottleneck problem, such as using a different loss function or a different architecture. It would be good to compare the proposed method with these methods. The authors do not provide a comparison with other methods that address the high variance of the gradient estimator problem, such as using a different optimizer or a different learning rate schedule. It would be good to compare the proposed method with these methods.

**********

## Paper Decision Policy

See [this document](https://openreview.net/pdf?id=GhMfZr9xgj) for the ICLR 2024 paper decision policy.

1. **Accept** (accept, good paper): The paper is technically sound and presents an important, interesting, or valuable result. It has been well tested on a wide range of problems and situations and performed well. The paper is well written and clear to read. Results are properly validated and well presented.
2. **Accept (poster)** (accept, poster): The paper is good but not of very broad interest. The paper is technically sound but lacks the breadth of applicability and interest needed for an oral presentation. It presents a novel, interesting idea or result, but it is not thoroughly tested or validated. The paper is well written and clear to read.
3. **Reject (not selected for publication)** (reject, not selected for publication): The paper does not meet the bar for an ICLR paper, either because it is not novel, not technically sound, not well written, or not properly validated.
4. **Reject (not selected for oral/poster)** (reject, not selected for oral/poster): The paper does not meet the bar for an oral or poster presentation at ICLR, but it may be suitable for publication at another venue. This is often used for papers that are technically sound and interesting, but not of broad interest to the ICLR community.
5. **Withdrawn by authors** (withdrawn by authors): The authors have withdrawn the paper from consideration for publication.
6. **Under review at another conference** (under review at another conference): The paper is under review at another conference and has not been rejected. In this case, it is not acceptable for publication at ICLR and the authors should not resubmit a similar paper to ICLR.
7. **Resubmit elsewhere (not good enough for discussion at ICLR)** (resubmit elsewhere, not good enough for discussion at ICLR): The paper is not good enough to be discussed at ICLR. It may be suitable for publication at a different venue, but it is not suitable for publication at ICLR. In this case, the authors should resubmit the paper to another venue.
8. **Resubmit elsewhere (not good enough for publication at ICLR)** (resubmit elsewhere, not good enough for publication at ICLR): The paper is not good enough for publication at ICLR. It may be suitable for publication at a different venue, but it is not suitable for publication at ICLR. In this case, the authors should resubmit the paper to another venue.
9. **Spam/Privacy Violation/Malicious/Not a Paper** (spam/privacy violation/malicious/not a paper): The paper is spam, violates privacy, is malicious, or is not a paper. In this case, the paper should be rejected and the authors may be banned from submitting to ICLR in the future.
10. **Student Abstract/Poster Slam/Challenge/Workshop** (student abstract/poster slam/challenge/workshop): The paper is a submission for the student abstracts, poster slam, challenge, or workshop. In this case, the paper should be evaluated by the relevant program chairs and reviewers for the student abstracts, poster slam, challenge, or workshop.
11. **Need Author Stated Reviewer Category** (need author stated reviewer category): The paper needs to be categorized by the authors as a poster or oral. Please use the author response period to specify the category.
12. **Need AC Reviewer Discussion** (need ac reviewer discussion): The paper requires further discussion among the reviewers and the area chair. Please use the author response period to resolve the issues.
13. **Posters For Site (accept, poster)** (posters for site, accept, poster): The paper is accepted as a poster and will be presented at the conference. It may not be suitable for publication at ICLR, but it is good enough to be presented at the conference. In this case, the paper should be properly formatted according to the ICLR style guide and submitted to OpenReview with the poster track selected.
14. **Orals For Site (accept, oral)** (orals for site, accept, oral): The paper is accepted as an oral and will be presented at the conference. It is a top paper and should be presented to a wide audience. In this case, the paper should be properly formatted according to the ICLR style guide and submitted to OpenReview with the oral track selected.
15. **Spotlight For Site (accept, spotlight)** (spotlight for site, accept, spotlight): The paper is accepted as a spotlight and will be presented at the conference. It is a good paper, but not good enough for an oral. In this case, the paper should be properly formatted according to the ICLR style guide and submitted to OpenReview with the spotlight track selected.
16. **Accept (poster, because the authors requested poster)** (accept, poster, because the authors requested poster): The paper is accepted as a poster and will be presented at the conference. The authors requested that the paper be presented as a poster. In this case, the paper should be properly formatted according to the ICLR style guide and submitted to OpenReview with the poster track selected.
17. **Accept (oral, because the authors requested oral)** (accept, oral, because the authors requested oral): The paper is accepted as an oral and will be presented at the conference. The authors requested that the paper be presented as an oral. In this case, the paper should be properly formatted according to the ICLR style guide and submitted to OpenReview with the oral track selected.
18. **Accept (spotlight, because the authors requested spotlight)** (accept, spotlight, because the authors requested spotlight): The paper is accepted as a spotlight and will be presented at the conference. The authors requested that the paper be presented as a spotlight. In this case, the paper should be properly formatted according to the ICLR style guide and submitted to OpenReview with the spotlight track selected.
19. **Withdrawn (withdrawn)** (withdrawn, withdrawn): The authors have withdrawn the paper from consideration for publication.
20. **Resubmit as a Tool/Repository/Dataset (resubmit as a tool/repository/dataset)** (resubmit as a tool/repository/dataset, resubmit as a tool/repository/dataset): The paper is not a research paper, but a tool, repository, or dataset. In this case, the paper should be resubmitted as a tool, repository, or dataset.
21. **Resubmit as a Workshop Paper (resubmit as a workshop paper)** (resubmit as a workshop paper, resubmit as a workshop paper): The paper is not a full conference paper, but a workshop paper. In this case, the paper should be resubmitted as a workshop paper.
22. **Resubmit as a Student Abstract (resubmit as a student abstract)** (resubmit as a student abstract, resubmit as a student abstract): The paper is a student abstract. In this case, the paper should be resubmitted as a student abstract.
23. **Resubmit as a Poster Slam/Challenge/Workshop (resubmit as a poster slam/challenge/workshop)** (resubmit as a poster slam/challenge/workshop, resubmit as a poster slam/challenge/workshop): The paper is a poster slam, challenge, or workshop submission. In this case, the paper should be resubmitted as a poster slam, challenge, or workshop.
24. **Resubmit Elsewhere (resubmit elsewhere)** (resubmit elsewhere, resubmit elsewhere): The paper is not good enough for publication at ICLR. It may be suitable for publication at a different venue, but it is not suitable for publication at ICLR. In this case, the authors should resubmit the paper to another venue.
25. **No Review (no review)** (no review, no review): The paper received no reviews. In this case, the paper should be properly formatted according to the ICLR style guide and submitted to OpenReview with the relevant track selected.
26. **Under Review (under review)** (under review, under review): The paper is under review at another conference and has not been rejected. In this case, it is not acceptable for publication at ICLR and the authors should not resubmit a similar paper to ICLR.
27. **Not Applicable (not applicable)** (not applicable, not applicable): The paper is not applicable to ICLR. In this case, the paper should not be submitted to ICLR.
28. **Spam/Privacy Violation/Malicious/Not a Paper (spam/privacy violation/malicious/not a paper)** (spam/privacy violation/malicious/not a paper, spam/privacy violation/malicious/not a paper): The paper is spam, violates privacy, is malicious, or is not a paper. In this case, the paper should be rejected and the authors may be banned from submitting to ICLR in the future.
29. **Need Author Response (need author response)** (need author response, need author response): The paper needs an author response. Please use the author response period to address the reviewer comments.
30. **Need AC Reviewer Discussion (need ac reviewer discussion)** (need ac reviewer discussion, need ac reviewer discussion): The paper requires further discussion among the reviewers and the area chair. Please use the author response period to resolve the issues.
31. **Need AC Reviewer Re-review (need ac reviewer re-review)** (need ac reviewer re-review, need ac reviewer re-review): The paper requires further review by the reviewers. Please use the author response period to resolve the issues.
32. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
33. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
34. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
35. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
36. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
37. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
38. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
39. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
40. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
41. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
42. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
43. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
44. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
45. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
46. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
47. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
48. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
49. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
50. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
51. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
52. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
53. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
54. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
55. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
56. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
57. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
58. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
59. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
60. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
61. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
62. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
63. **Need AC Reviewer Re-review Post-rebuttal (need ac reviewer re-review post-rebuttal)** (need ac reviewer re-review post-rebuttal, need ac reviewer re-review post-rebuttal): The paper requires further review by the reviewers after the author response period. Please use the rebuttal period to resolve the issues.
64. **Need AC Reviewer Discussion Post-rebuttal (need ac reviewer discussion post-rebuttal)** (need ac reviewer discussion post-rebuttal, need ac reviewer discussion post-rebuttal): The paper requires further discussion among the reviewers and the area chair after the author response period. Please use the rebuttal period to resolve the issues.
65. **Need AC Reviewer Re-review Post-rebuttal