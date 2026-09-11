## Summary

This paper studies the problem of training a transformer-based language model with masked language modeling on a single GPU in one day. The authors investigate the effects of various modifications to the training pipeline and find that most of the improvements are related to the scaling laws. They also provide a modified pipeline with performance close to BERT.

## Soundness

2 fair

## Presentation

3 good

## Contribution

2 fair

## Strengths

The paper is well-written and easy to follow. The authors investigate the effects of various modifications to the training pipeline and find that most of the improvements are related to the scaling laws. They also provide a modified pipeline with performance close to BERT.

## Weaknesses

1. The novelty of this paper is limited. The authors mainly investigate the effects of various modifications to the training pipeline and find that most of the improvements are related to the scaling laws. This is not a surprising result and has been known in the literature. 

2. The experiments are not convincing. The authors only conduct experiments on a single task, GLUE, and the results are not very convincing. The authors should conduct experiments on more tasks and datasets to demonstrate the effectiveness of the proposed method.

3. The authors only conduct experiments on a single GPU. The authors should conduct experiments on multiple GPUs to demonstrate the effectiveness of the proposed method.

4. The authors only conduct experiments on a single model architecture. The authors should conduct experiments on multiple model architectures to demonstrate the effectiveness of the proposed method.

5. The authors do not provide any theoretical analysis of the proposed method.

## Questions

Please see the weaknesses above.

## Flag For Ethics Review

No ethics review needed.

## Rating

3: reject, not good enough

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

## Summary

The paper investigates the performance of a transformer-based language model trained from scratch with masked language modeling on a single GPU within a day. The authors analyze various components of the pretraining pipeline and propose modifications to improve performance. They find that scaling laws observed in large-compute settings also apply in this constrained setting, making scaling down challenging. The paper categorizes recent improvements to training and architecture and discusses their practical applicability in the context of limited compute. The authors also provide a modified pipeline with performance close to BERT and discuss the implications of their findings for research in this area.

## Soundness

3 good

## Presentation

3 good

## Contribution

2 fair

## Strengths

- The paper is well written and easy to follow.
- The authors provide a thorough analysis of various components of the pretraining pipeline and propose modifications to improve performance in a single GPU within a day.
- The paper provides evidence that scaling laws observed in large-compute settings also apply in this constrained setting, making scaling down challenging.

## Weaknesses

- The paper's novelty is limited, as it primarily investigates the effects of various modifications to the training pipeline and finds that most improvements are related to scaling laws, which is not a new finding.
- The experiments are not convincing, as they are limited to a single task, GLUE, and the results are not very convincing. The authors should conduct experiments on more tasks and datasets to demonstrate the effectiveness of the proposed method.
- The paper does not provide any theoretical analysis of the proposed method.

## Questions

Please see the weaknesses above.

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

## Summary

The paper investigates the performance of a transformer-based language model trained from scratch with masked language modeling on a single GPU within a day. The authors analyze various components of the pretraining pipeline and propose modifications to improve performance. They find that scaling laws observed in large-compute settings also apply in this constrained setting, making scaling down challenging. The paper categorizes recent improvements to training and architecture and discusses their practical applicability in the context of limited compute. The authors also provide a modified pipeline with performance close to BERT and discuss the implications of their findings for research in this area.

## Soundness

3 good

## Presentation

3 good

## Contribution

2 fair

## Strengths

- The paper is well written and easy to follow.
- The authors provide a thorough analysis of various components of the pretraining pipeline and propose modifications to improve performance in a single GPU within a day.
- The paper provides evidence that scaling laws observed in large-compute settings also apply in this constrained setting, making scaling down challenging.

## Weaknesses

- The paper's novelty is limited, as it primarily investigates the effects of various modifications to the training pipeline and finds that most improvements are related to scaling laws, which is not a new finding.
- The experiments are not convincing, as they are limited to a single task, GLUE, and the results are not very convincing. The authors should conduct experiments on more tasks and datasets to demonstrate the effectiveness of the proposed method.
- The paper does not provide any theoretical analysis of the proposed method.

## Questions

Please see the weaknesses above.

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

## Summary

This paper investigates the performance of a transformer-based language model trained from scratch with masked language modeling on a single GPU within a day. The authors analyze various components of the pretraining pipeline and propose modifications to improve performance. They find that scaling laws observed in large-compute settings also apply in this constrained setting, making scaling down challenging. The paper categorizes recent improvements to training and architecture and discusses their practical applicability in the context of limited compute. The authors also provide a modified pipeline with performance close to BERT and discuss the implications of their findings for research in this area.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper is well written and easy to follow.
The authors provide a thorough analysis of various components of the pretraining pipeline and propose modifications to improve performance in a single GPU within a day.
The paper provides evidence that scaling laws observed in large-compute settings also apply in this constrained setting, making scaling down challenging.

## Weaknesses

The paper's novelty is limited, as it primarily investigates the effects of various modifications to the training pipeline and finds that most improvements are related to scaling laws, which is not a new finding.
The experiments are not convincing, as they are limited to a single task, GLUE, and the results are not very convincing. The authors should conduct experiments on more tasks and datasets to demonstrate the effectiveness of the proposed method.
The paper does not provide any theoretical analysis of the proposed method.

## Questions

The paper's novelty is limited, as it primarily investigates the effects of various modifications to the training pipeline and finds that most improvements are related to scaling laws, which is not a new finding.
The experiments are not convincing, as they are limited to a single task, GLUE, and the results are not very convincing. The authors should conduct experiments on more tasks and datasets to demonstrate the effectiveness of the proposed method.
The paper does not provide any theoretical analysis of the proposed method.

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper investigates the performance of a transformer-based language model trained from scratch with masked language modeling on a single GPU within a day. The authors analyze various components of the pretraining pipeline and propose modifications to improve performance. They find that scaling laws observed in large-compute settings also apply in this constrained setting, making scaling down challenging. The paper categorizes recent improvements to training and architecture and discusses their practical applicability in the context of limited compute. The authors also provide a modified pipeline with performance close to BERT and discuss the implications of their findings for research in this area.

The paper is well written and easy to follow. The authors provide a thorough analysis of various components of the pretraining pipeline and propose modifications to improve performance in a single GPU within a day. The paper provides evidence that scaling laws observed in large-compute settings also apply in this constrained setting, making scaling down challenging.

The paper's novelty is limited, as it primarily investigates the effects of various modifications to the training pipeline and finds that most improvements are related to scaling laws, which is not a new finding. The experiments are not convincing, as they are limited to a single task, GLUE, and the results are not very convincing. The authors should conduct experiments on more tasks and datasets to demonstrate the effectiveness of the proposed method. The paper does not provide any theoretical analysis of the proposed method.

## justification_for_why_not_higher_score

The paper's novelty is limited, as it primarily investigates the effects of various modifications to the training pipeline and finds that most improvements are related to scaling laws, which is not a new finding. The experiments are not convincing, as they are limited to a single task, GLUE, and the results are not very convincing. The authors should conduct experiments on more tasks and datasets to demonstrate the effectiveness of the proposed method. The paper does not provide any theoretical analysis of the proposed method.

## justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)

**********

## Paper Decision Policy

The paper was reviewed in its entirety by the reviewers, and a consensus was reached that the paper does not meet the bar for acceptance. The authors did not submit a rebuttal. The paper does not meet the bar for acceptance.

**********

<!-- Added by arXiv -->
<!---->

<!-- The paper is not recommended for publication in its current form. The reviewers and AC agree that the paper is not ready for publication. The authors are encouraged to take the comments and suggestions from the reviewers into account and submit a revised version of the paper to another venue. -->