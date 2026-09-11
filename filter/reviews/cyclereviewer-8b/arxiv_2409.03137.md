## Reviewer

### Summary

The paper proposes AdEMAMix, a new optimizer that extends Adam by incorporating two EMAs. The first EMA has a relatively small $\beta_1$ value, similar to Adam, while the second EMA has a much larger $\beta_3$ value. The two EMAs are combined with a hyperparameter $\alpha$ that controls the relative weight of the second EMA. The authors show that AdEMAMix can outperform Adam on various tasks, including language modeling and image classification.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed optimizer is simple and easy to implement.
- The experiments show that AdEMAMix can outperform Adam on various tasks.

### Weaknesses

- The paper does not provide a theoretical analysis of the proposed optimizer.
- The paper does not provide a detailed analysis of the hyperparameters, including how they affect the performance and how to choose them in practice.
- The paper does not compare AdEMAMix with other optimizers, such as SGD and AdamW with different hyperparameters.

### Questions

- Can the authors provide a theoretical analysis of the proposed optimizer?
- Can the authors provide a detailed analysis of the hyperparameters and how to choose them in practice?
- Can the authors compare AdEMAMix with other optimizers, such as SGD and AdamW with different hyperparameters?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new variant of the Adam optimizer, AdEMAMix, which leverages a mixture of two EMAs to better take advantage of past gradients. The authors empirically demonstrate the superiority of their method over Adam by training ViT and language models of up to 1.3B parameters. They also show that AdEMAMix forgets the training data slower than Adam. The paper's findings contribute to a deeper understanding of the optimal balance between using historical gradients and adapting to the changing loss landscape.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed AdEMAMix is simple and easy to implement.
- The experiments are extensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

- The novelty of the proposed method is limited. The idea of using a mixture of two EMAs is not new, and the authors do not provide a theoretical analysis of their method.
- The paper lacks a detailed comparison with other state-of-the-art optimizers, such as AdamW and AdamW with different hyperparameters.
- The paper does not discuss the limitations of the proposed method and potential future work.

### Questions

- The authors claim that the proposed method can outperform Adam by a significant margin. However, the paper does not provide a detailed comparison with other state-of-the-art optimizers. Can the authors provide a comparison with AdamW and AdamW with different hyperparameters?
- The paper does not discuss the limitations of the proposed method. What are the potential limitations of AdEMAMix, and how can they be addressed?
- The paper does not discuss potential future work. Can the authors provide some suggestions for future research directions?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new optimizer, AdEMAMix, which is a modification of the Adam optimizer with a mixture of two EMAs to better take advantage of past gradients. The authors empirically demonstrate the superiority of their method over Adam by training ViT and language models of up to 1.3B parameters.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed AdEMAMix is simple and easy to implement.
3. The experiments are extensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

1. The novelty of the proposed method is limited. The idea of using a mixture of two EMAs is not new, and the authors do not provide a theoretical analysis of their method.
2. The paper lacks a detailed comparison with other state-of-the-art optimizers, such as AdamW and AdamW with different hyperparameters.
3. The paper does not discuss the limitations of the proposed method and potential future work.

### Questions

1. The authors claim that the proposed method can outperform Adam by a significant margin. However, the paper does not provide a detailed comparison with other state-of-the-art optimizers. Can the authors provide a comparison with AdamW and AdamW with different hyperparameters?
2. The paper does not discuss the limitations of the proposed method. What are the potential limitations of AdEMAMix, and how can they be addressed?
3. The paper does not discuss potential future work. Can the authors provide some suggestions for future research directions?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces AdEMAMix, an extension of Adam that uses two EMAs to better leverage past gradients. The authors demonstrate that AdEMAMix outperforms Adam on large-scale language modeling and image classification tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The experiments are extensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

1. The paper does not provide a theoretical analysis of the proposed method.
2. The paper does not discuss the limitations of the proposed method and potential future work.
3. The paper does not provide a detailed comparison with other state-of-the-art optimizers.

### Questions

1. Can the authors provide a theoretical analysis of the proposed method?
2. Can the authors discuss the limitations of the proposed method and potential future work?
3. Can the authors provide a detailed comparison with other state-of-the-art optimizers?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a new optimizer, AdEMAMix, which is a modification of the Adam optimizer with a mixture of two EMAs to better take advantage of past gradients. The authors empirically demonstrate the superiority of their method over Adam by training ViT and language models of up to 1.3B parameters.

The paper received four reviews, with all of them recommending rejection. The reviewers raised concerns about the novelty of the proposed method, the lack of theoretical analysis, and the limited comparison with other state-of-the-art optimizers. The authors provided a response to the reviewers, but unfortunately, it did not address the concerns.

### justification_for_why_not_higher_score

All reviewers recommended rejection.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject

**********

## Paper Decision Overview

Reject

**********

## Paper Decision Comments

Thanks for your submission.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at least 5 reviews are received, discuss and reach a consensus based on the review content, score, and self-assessed confidence level.
2. If at least 3 reviews are received, the PC chair reads the reviews, discusses with the reviewers, and makes a decision. If the PC chair is one of the reviewers, another PC member will read the reviews and make the decision.
3. If less than 3 reviews are received, the PC chair (or the PC member if the PC chair is a reviewer) has the final decision power. The chair can still solicit reviews from the community if more reviews are needed.
4. For borderline cases, the PC chair has the final decision power. The AC's recommendation is not binding.
5. For all accepted papers, at least one review should be from the area chair. The area chair is responsible for ensuring the quality of the reviews and the decision.
6. For all rejected papers, at least two reviews are required. The area chair should discuss with the reviewers to ensure the quality of the decision.
7. For papers that are not recommended by the reviewers but the authors would like to respond, the authors can provide a rebuttal. The area chair discusses the rebuttal with the reviewers, and makes a final decision. The AC's decision is based on the following factors:
   - The quality of the paper.
   - The review scores and the review content.
   - The author's rebuttal.
   - The discussion among the AC, authors, and reviewers.
8. The area chair is responsible for ensuring the quality of the reviews and the decision. The AC should discuss with the reviewers to ensure the quality of the decision.
9. The PC chair has the final decision power in case of any disputes.
10. All decisions are final.

**********

**********

**********

## Paper Decision Policies

1. If at