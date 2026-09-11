## Reviewer

### Summary

The authors evaluate a number of methods that aim to speed up training of transformer-based language models. The methods considered are layer stacking, layer dropping, selective backprop, RHO loss, Lion, and Sophia. The authors use a fixed wall-clock time budget for training and compare the final performance of the models trained with these methods to the performance of the baseline models trained with standard methods. The authors find that the methods considered do not improve over the baseline models.

### Soundness

3 good

### Presentation

3 good

### Contribution

1 poor

### Strengths

The paper is well written and easy to follow. The authors use a fixed wall-clock time budget for training and compare the final performance of the models trained with the methods considered to the performance of the baseline models trained with standard methods. This makes the comparison fair.

### Weaknesses

The paper does not provide any significant contribution. The authors evaluate a number of methods that aim to speed up training of transformer-based language models and find that they do not improve over the baseline models. The paper does not propose any new methods for speeding up training of transformer-based language models.

### Questions

N/A

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper revisits the evaluation of efficient training algorithms for transformer-based language models. The authors evaluate three categories of methods: dynamic architectures (layer stacking and layer dropping), batch selection (selective backprop and RHO loss), and efficient optimizers (Lion and Sophia). The authors find that these methods do not provide significant improvements over standard training methods when evaluated under a fixed wall-clock time budget. The authors also propose a new metric, reference system time (RST), to standardize wall-clock time comparisons across different hardware and software configurations.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive evaluation of several efficient training methods for transformer-based language models, and the proposed RST metric is a useful contribution for standardizing wall-clock time comparisons.

### Weaknesses

The paper does not propose any new efficient training methods, but rather evaluates existing methods and finds that they do not provide significant improvements over standard training methods. This makes the paper more of a benchmarking paper, which may not be of interest to a broad audience.

### Questions

N/A

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper evaluates the effectiveness of several efficient training methods for transformer-based language models. The authors find that these methods do not provide significant improvements over standard training methods when evaluated under a fixed wall-clock time budget. The authors also propose a new metric, reference system time (RST), to standardize wall-clock time comparisons across different hardware and software configurations.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive evaluation of several efficient training methods for transformer-based language models, and the proposed RST metric is a useful contribution for standardizing wall-clock time comparisons.

### Weaknesses

The paper does not propose any new efficient training methods, but rather evaluates existing methods and finds that they do not provide significant improvements over standard training methods. This makes the paper more of a benchmarking paper, which may not be of interest to a broad audience.

### Questions

N/A

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper revisits three categories of efficient training algorithms for transformer-based language models: dynamic architectures (layer stacking and layer dropping), batch selection (selective backprop and RHO loss), and efficient optimizers (Lion and Sophia). The authors evaluate these methods under a fixed wall-clock time budget and find that they do not provide significant improvements over standard training methods. The authors also propose a new metric, reference system time (RST), to standardize wall-clock time comparisons across different hardware and software configurations.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive evaluation of several efficient training methods for transformer-based language models, and the proposed RST metric is a useful contribution for standardizing wall-clock time comparisons.

### Weaknesses

The paper does not propose any new efficient training methods, but rather evaluates existing methods and finds that they do not provide significant improvements over standard training methods. This makes the paper more of a benchmarking paper, which may not be of interest to a broad audience.

### Questions

1. How does the RST metric compare to other metrics for standardizing wall-clock time comparisons, such as the FLOPS metric?
2. How does the RST metric account for variations in hardware and software configurations?
3. How do the results of this paper compare to other studies that have evaluated the effectiveness of efficient training methods for transformer-based language models?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper presents a comprehensive evaluation of several efficient training methods for transformer-based language models. The authors find that these methods do not provide significant improvements over standard training methods when evaluated under a fixed wall-clock time budget. The authors also propose a new metric, reference system time (RST), to standardize wall-clock time comparisons across different hardware and software configurations.

The paper received four reviews, all of which rated it as reject. The reviewers raised concerns about the lack of new contributions, as the paper primarily focuses on benchmarking existing methods and finding that they do not provide significant improvements over standard training methods. The reviewers also raised questions about the significance of the RST metric and how it compares to other metrics for standardizing wall-clock time comparisons.

### justification_for_why_not_higher_score

The paper received four reviews, all of which rated it as reject. The reviewers raised concerns about the lack of new contributions, as the paper primarily focuses on benchmarking existing methods and finding that they do not provide significant improvements over standard training methods. The reviewers also raised questions about the significance of the RST metric and how it compares to other metrics for standardizing wall-clock time comparisons.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject

**********

## Paper Decision Overview

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

## Paper Decision Comments

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Type

Reject, not good enough

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

**********

## Paper Decision Comments

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not propose any new efficient training methods, which may not be of interest to a broad audience. The AC recommends rejection.

**********

**********

## Paper Decision Justification

The paper was rejected by all reviewers. There were no discussions or author rebuttals. The paper was not discussed in the AC's discussion meeting. The AC agrees with the reviewers that the paper is more of a benchmarking paper and does not