## Summary

The paper introduces a novel approach to learn a single representation that can be used for multiple downstream tasks. The key idea is to learn a coarse-to-fine representation that can be used for different tasks with varying computational resources. The authors propose a method called Matryoshka Representation Learning (MRL) that encodes information at different granularities and allows a single embedding to adapt to the computational constraints of downstream tasks. The authors show that MRL can achieve up to 14x smaller embedding size for ImageNet-1K classification, up to 14x real-world speed-ups for large-scale retrieval, and up to 2% accuracy improvements for long-tail few-shot classification, while being as robust as the original representations.

## Soundness

1

## Presentation

2

## Contribution

2

## Strengths

- The paper is well-written and easy to follow.
- The idea of learning a single representation that can be used for multiple downstream tasks is interesting and has the potential to be a game-changer in the field of representation learning.
- The experiments are extensive and demonstrate the effectiveness of the proposed method.

## Weaknesses

- The paper lacks a clear motivation for the proposed method. The authors should provide more details on why learning a single representation that can be used for multiple downstream tasks is important and how it can benefit the community.
- The paper lacks a clear explanation of the proposed method. The authors should provide more details on how the proposed method works and how it can be used for different downstream tasks.
- The paper lacks a clear evaluation of the proposed method. The authors should provide more details on how the proposed method compares to existing methods and what are the advantages and disadvantages of the proposed method.

## Questions

- How does the proposed method compare to existing methods for learning a single representation that can be used for multiple downstream tasks?
- How does the proposed method perform on different downstream tasks?
- What are the advantages and disadvantages of the proposed method compared to existing methods?

## Flag For Ethics Review

No ethics review needed.

## Rating

3: reject, not good enough

## Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

------------------

## Summary

This paper proposes Matryoshka Representation Learning (MRL), a method for learning representations that are flexible and can adapt to multiple downstream tasks with varying computational resources. The authors demonstrate that MRL can achieve significant speed-ups and accuracy improvements in large-scale classification and retrieval tasks, while maintaining robustness and accuracy. They also show that MRL can be seamlessly adapted to various modalities and web-scale datasets.

## Soundness

2

## Presentation

2

## Contribution

2

## Strengths

- The paper proposes a novel approach to learn flexible representations that can adapt to multiple downstream tasks with varying computational resources.
- The authors demonstrate that MRL can achieve significant speed-ups and accuracy improvements in large-scale classification and retrieval tasks, while maintaining robustness and accuracy.
- The paper shows that MRL can be seamlessly adapted to various modalities and web-scale datasets.

## Weaknesses

- The paper lacks a clear explanation of the proposed method and how it works.
- The paper lacks a clear evaluation of the proposed method and how it compares to existing methods.
- The paper lacks a clear discussion of the limitations of the proposed method and potential future work.

## Questions

- How does MRL compare to existing methods for learning flexible representations?
- How does MRL perform on different downstream tasks and datasets?
- What are the limitations of MRL and how can they be addressed in future work?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

------------------

## Summary

This paper proposes a novel method called Matryoshka Representation Learning (MRL) for learning flexible representations that can adapt to multiple downstream tasks with varying computational resources. The authors demonstrate that MRL can achieve significant speed-ups and accuracy improvements in large-scale classification and retrieval tasks, while maintaining robustness and accuracy. They also show that MRL can be seamlessly adapted to various modalities and web-scale datasets. The paper also provides a detailed analysis of the proposed method and its applications.

## Soundness

3

## Presentation

3

## Contribution

3

## Strengths

1. The paper proposes a novel approach to learn flexible representations that can adapt to multiple downstream tasks with varying computational resources.
2. The authors demonstrate that MRL can achieve significant speed-ups and accuracy improvements in large-scale classification and retrieval tasks, while maintaining robustness and accuracy.
3. The paper shows that MRL can be seamlessly adapted to various modalities and web-scale datasets.
4. The paper provides a detailed analysis of the proposed method and its applications.

## Weaknesses

1. The paper lacks a clear explanation of the proposed method and how it works.
2. The paper lacks a clear evaluation of the proposed method and how it compares to existing methods.
3. The paper lacks a clear discussion of the limitations of the proposed method and potential future work.

## Questions

1. How does MRL compare to existing methods for learning flexible representations?
2. How does MRL perform on different downstream tasks and datasets?
3. What are the limitations of MRL and how can they be addressed in future work?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

------------------

## Summary

The paper presents a method for learning representations that can be used for multiple downstream tasks. The method is called Matryoshka Representation Learning (MRL), and it learns representations of varying capacities within the same high-dimensional vector through explicit optimization of a subset of lower-dimensional vectors. The authors demonstrate that MRL can achieve significant speed-ups and accuracy improvements in large-scale classification and retrieval tasks, while maintaining robustness and accuracy. They also show that MRL can be seamlessly adapted to various modalities and web-scale datasets. The paper also provides a detailed analysis of the proposed method and its applications.

## Soundness

2

## Presentation

2

## Contribution

2

## Strengths

1. The paper proposes a novel approach to learn representations that can be used for multiple downstream tasks.
2. The authors demonstrate that MRL can achieve significant speed-ups and accuracy improvements in large-scale classification and retrieval tasks, while maintaining robustness and accuracy.
3. The paper shows that MRL can be seamlessly adapted to various modalities and web-scale datasets.
4. The paper provides a detailed analysis of the proposed method and its applications.

## Weaknesses

1. The paper lacks a clear explanation of the proposed method and how it works.
2. The paper lacks a clear evaluation of the proposed method and how it compares to existing methods.
3. The paper lacks a clear discussion of the limitations of the proposed method and potential future work.

## Questions

1. How does MRL compare to existing methods for learning representations that can be used for multiple downstream tasks?
2. How does MRL perform on different downstream tasks and datasets?
3. What are the limitations of MRL and how can they be addressed in future work?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

------------------

## Meta Review

This paper proposes a method for learning a single representation that can be used for multiple downstream tasks. The key idea is to learn a coarse-to-fine representation that can be used for different tasks with varying computational resources. The authors demonstrate that MRL can achieve up to 14x smaller embedding size for ImageNet-1K classification, up to 14x real-world speed-ups for large-scale retrieval, and up to 2% accuracy improvements for long-tail few-shot classification, while being as robust as the original representations. The paper also shows that MRL can be seamlessly adapted to various modalities and web-scale datasets.

The reviewers generally agree that the paper is well-written and easy to follow, and the idea of learning a single representation that can be used for multiple downstream tasks is interesting and has the potential to be a game-changer in the field of representation learning. However, they also raise several concerns about the lack of a clear motivation for the proposed method, the lack of a clear explanation of the proposed method, and the lack of a clear evaluation of the proposed method and how it compares to existing methods. They also raise concerns about the limitations of the proposed method and potential future work.

Overall, while the paper proposes an interesting approach to learning a single representation that can be used for multiple downstream tasks, the reviewers have raised several concerns about the clarity of the paper and the evaluation of the proposed method. Therefore, I recommend rejecting the paper in its current form and encourage the authors to address the concerns raised by the reviewers in a future submission.

### justification_for_why_not_higher_score

The reviewers have raised several concerns about the clarity of the paper and the evaluation of the proposed method.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the running for an oral, but can be accepted as a poster) (poster) (poster) (poster) (poster)