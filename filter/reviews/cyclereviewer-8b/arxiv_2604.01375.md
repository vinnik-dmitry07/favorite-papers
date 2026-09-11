## Reviewer

### Summary

This paper introduces RIFT, a taxonomy of rubric failure modes, which is designed to help diagnose issues in evaluation rubrics. The taxonomy is based on expert critiques of rubrics from various sources and is organized into three categories: reliability, content validity, and consequential validity. The paper also presents automated diagnostics for rubric quality and evaluates them against human annotations, achieving high F1 scores.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper addresses an important problem in the field of LLMs, which is the lack of a principled way to diagnose failures in evaluation rubrics. The proposed taxonomy is comprehensive and well-organized, and the automated diagnostics are shown to align well with human annotations.

### Weaknesses

1. The paper focuses on the evaluation of rubrics, but does not discuss how to construct good rubrics. This is an important limitation, as the quality of the rubric is critical to the effectiveness of the evaluation. The paper should discuss how to construct good rubrics and how to evaluate their quality.

2. The paper does not provide a clear definition of the failure modes in the taxonomy. It would be helpful to provide a clear definition of each failure mode and how it is measured.

3. The paper does not discuss the limitations of the proposed taxonomy and diagnostics. For example, how well does the taxonomy generalize to other domains and tasks? How robust are the automated diagnostics to different LLMs and evaluation settings?

### Questions

See weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a rubric failure mode taxonomy, RIFT, which consists of eight failure modes organized into three high-level categories: reliability failures, content validity failures, and consequential validity failures. The taxonomy is developed using grounded theory and is validated through expert annotation and inter-annotator agreement. The paper also proposes automated diagnostics for rubric quality based on LLM-based classification and agreement- and stability-based signals, which achieve high agreement with expert annotations.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper addresses an important problem in the field of LLMs, which is the lack of a principled way to diagnose failures in evaluation rubrics.
- The proposed taxonomy is comprehensive and well-organized, and the automated diagnostics are shown to align well with human annotations.
- The paper is well-written and easy to follow.

### Weaknesses

- The paper focuses on the evaluation of rubrics, but does not discuss how to construct good rubrics. This is an important limitation, as the quality of the rubric is critical to the effectiveness of the evaluation.
- The paper does not provide a clear definition of the failure modes in the taxonomy. It would be helpful to provide a clear definition of each failure mode and how it is measured.
- The paper does not discuss the limitations of the proposed taxonomy and diagnostics. For example, how well does the taxonomy generalize to other domains and tasks? How robust are the automated diagnostics to different LLMs and evaluation settings?

### Questions

- Could you provide a clear definition of each failure mode in the taxonomy and how it is measured?
- How does the taxonomy generalize to other domains and tasks?
- How robust are the automated diagnostics to different LLMs and evaluation settings?
- How does the quality of the rubric affect the effectiveness of the evaluation?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a taxonomy of rubric failures, and a method for automated rubric quality metrics. The taxonomy is developed through a grounded theory approach, with a set of expert annotators. The automated metrics are based on LLM-based classification and agreement- and stability-based signals. The authors show that the automated metrics align with expert annotations.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper addresses an important problem in the field of LLMs, which is the lack of a principled way to diagnose failures in evaluation rubrics.
- The proposed taxonomy is comprehensive and well-organized, and the automated diagnostics are shown to align well with human annotations.

### Weaknesses

- The paper focuses on the evaluation of rubrics, but does not discuss how to construct good rubrics. This is an important limitation, as the quality of the rubric is critical to the effectiveness of the evaluation.
- The paper does not provide a clear definition of the failure modes in the taxonomy. It would be helpful to provide a clear definition of each failure mode and how it is measured.
- The paper does not discuss the limitations of the proposed taxonomy and diagnostics. For example, how well does the taxonomy generalize to other domains and tasks? How robust are the automated diagnostics to different LLMs and evaluation settings?

### Questions

- How does the taxonomy generalize to other domains and tasks?
- How robust are the automated diagnostics to different LLMs and evaluation settings?
- How does the quality of the rubric affect the effectiveness of the evaluation?
- How do the authors see this work being used in practice?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a taxonomy of rubric failures, which is developed through a grounded theory approach. The taxonomy is organized into three categories: reliability failures, content validity failures, and consequential validity failures. The paper also proposes automated diagnostics for rubric quality based on LLM-based classification and agreement- and stability-based signals, which achieve high agreement with expert annotations.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper addresses an important problem in the field of LLMs, which is the lack of a principled way to diagnose failures in evaluation rubrics.
- The proposed taxonomy is comprehensive and well-organized, and the automated diagnostics are shown to align well with human annotations.
- The paper is well-written and easy to follow.

### Weaknesses

- The paper does not provide a clear definition of the failure modes in the taxonomy. It would be helpful to provide a clear definition of each failure mode and how it is measured.
- The paper does not discuss the limitations of the proposed taxonomy and diagnostics. For example, how well does the taxonomy generalize to other domains and tasks? How robust are the automated diagnostics to different LLMs and evaluation settings?
- The paper focuses on the evaluation of rubrics, but does not discuss how to construct good rubrics. This is an important limitation, as the quality of the rubric is critical to the effectiveness of the evaluation.
- The paper does not discuss how the proposed taxonomy and diagnostics can be used in practice. For example, how can the taxonomy be used to identify and address failures in rubrics? How can the automated diagnostics be used to improve the quality of rubrics?

### Questions

- How does the taxonomy generalize to other domains and tasks?
- How robust are the automated diagnostics to different LLMs and evaluation settings?
- How does the quality of the rubric affect the effectiveness of the evaluation?
- How can the taxonomy be used to identify and address failures in rubrics?
- How can the automated diagnostics be used to improve the quality of rubrics?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces RIFT, a taxonomy of rubric failure modes, which is designed to help diagnose issues in evaluation rubrics. The taxonomy is based on expert critiques of rubrics from various sources and is organized into three categories: reliability, content validity, and consequential validity. The paper also presents automated diagnostics for rubric quality and evaluates them against human annotations, achieving high F1 scores.

The reviewers raised several concerns regarding the paper. Firstly, the paper focuses on the evaluation of rubrics, but does not discuss how to construct good rubrics. This is an important limitation, as the quality of the rubric is critical to the effectiveness of the evaluation. Secondly, the paper does not provide a clear definition of the failure modes in the taxonomy. It would be helpful to provide a clear definition of each failure mode and how it is measured. Thirdly, the paper does not discuss the limitations of the proposed taxonomy and diagnostics. For example, how well does the taxonomy generalize to other domains and tasks? How robust are the automated diagnostics to different LLMs and evaluation settings? Finally, the paper does not discuss how the proposed taxonomy and diagnostics can be used in practice. For example, how can the taxonomy be used to identify and address failures in rubrics? How can the automated diagnostics be used to improve the quality of rubrics?

### justification_for_why_not_higher_score

The reviewers raised several concerns regarding the paper. Firstly, the paper focuses on the evaluation of rubrics, but does not discuss how to construct good rubrics. This is an important limitation, as the quality of the rubric is critical to the effectiveness of the evaluation. Secondly, the paper does not provide a clear definition of the failure modes in the taxonomy. It would be helpful to provide a clear definition of each failure mode and how it is measured. Thirdly, the paper does not discuss the limitations of the proposed taxonomy and diagnostics. For example, how well does the taxonomy generalize to other domains and tasks? How robust are the automated diagnostics to different LLMs and evaluation settings? Finally, the paper does not discuss how the proposed taxonomy and diagnostics can be used in practice. For example, how can the taxonomy be used to identify and address failures in rubrics? How can the automated diagnostics be used to improve the quality of rubrics?

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)