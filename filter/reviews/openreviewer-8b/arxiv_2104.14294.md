# Review

## Summary
This paper proposes a self-supervised learning method for vision transformers. The method is based on knowledge distillation, where the student tries to match the output of an EMA teacher. The authors show that the method is effective for vision transformers and leads to features that are useful for kNN classification, retrieval, transfer learning, etc.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well written and easy to follow
- The method is simple and effective
- The authors show that the method leads to features that are useful for various tasks (kNN classification, retrieval, transfer learning, copy detection, etc.)
- The authors conduct a thorough ablation study

## Weaknesses
- The proposed method is very similar to BYOL and the differences are not clear

## Questions
What are the differences between the proposed method and BYOL? The teacher in BYOL can also be seen as an EMA of the student. The only difference is that in BYOL the teacher is fixed after a certain epoch and in the proposed method the teacher is always an EMA of the student. But even this small difference is not critical as shown in Figure 6 (right). So what are the main differences between the two methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4