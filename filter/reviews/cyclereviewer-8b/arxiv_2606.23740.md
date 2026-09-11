## Reviewer

### Summary

This paper presents an analysis of the weight-space geometry of different offline RL methods for reasoning distillation. The authors train six methods (SFT, RFT, DFT, RIFT, Offline GRPO, DPO) on identical math rollouts from a single base model (Qwen3-4B) with attention-only LoRA and analyze the resulting deltas via cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. The results show that SFT, RFT, and RIFT have nearly colinear weight deltas, while DFT diverges further in direction than any reward-weighted method. Offline GRPO adds a substantial component orthogonal to the SFT direction, and DPO sits in a near-orthogonal subspace with higher effective rank, a sharp linear-mode barrier, and reaches the highest accuracy in the protocol on both GSM8K and AIME26.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper presents an interesting analysis of the weight-space geometry of different offline RL methods for reasoning distillation. 
2. The results show that DPO sits in a near-orthogonal subspace with higher effective rank, a sharp linear-mode barrier, and reaches the highest accuracy in the protocol on both GSM8K and AIME26.

### Weaknesses

1. The paper only considers a single domain and checkpoint, which may limit the generalizability of the findings. 
2. The analysis is limited to attention-only LoRA, which may not be representative of the full range of LoRA configurations. 
3. The paper does not consider other contrastive methods such as IPO, KTO, SimPO, which may provide additional insights into the weight-space geometry of different offline RL methods. 
4. The paper does not provide a clear explanation for the observed differences in weight-space geometry among the different offline RL methods. 
5. The paper does not discuss the implications of the findings for the design of offline RL methods for reasoning distillation.

### Questions

1. How do the findings generalize to other domains and checkpoints?
2. How do different LoRA configurations affect the weight-space geometry of the offline RL methods?
3. How do other contrastive methods such as IPO, KTO, SimPO affect the weight-space geometry of the offline RL methods?
4. What are the implications of the findings for the design of offline RL methods for reasoning distillation?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper compares several offline RL methods for reasoning distillation (SFT, RFT, DFT, RIFT, Offline GRPO, DPO) on a single base model (Qwen3-4B) with attention-only LoRA. The paper analyzes the weight-space geometry of the resulting deltas using several metrics (cosine similarity, principal-angle subspace analysis, linear mode connectivity, CKA). The results show that SFT, RFT, and RIFT have similar weight-space geometry, while DFT diverges further in direction, Offline GRPO adds a substantial component orthogonal to the SFT direction, and DPO sits in a near-orthogonal subspace with higher effective rank.

### Soundness

3 good

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper analyzes the weight-space geometry of different offline RL methods for reasoning distillation.
- The paper shows that SFT, RFT, and RIFT have similar weight-space geometry, while DFT diverges further in direction, Offline GRPO adds a substantial component orthogonal to the SFT direction, and DPO sits in a near-orthogonal subspace with higher effective rank.

### Weaknesses

- The paper only considers a single base model (Qwen3-4B) and a single LoRA configuration (attention-only LoRA), which may limit the generalizability of the findings.
- The paper does not provide a clear explanation for the observed differences in weight-space geometry among the different offline RL methods.
- The paper does not discuss the implications of the findings for the design of offline RL methods for reasoning distillation.

### Questions

- How do the findings generalize to other base models and LoRA configurations?
- What are the implications of the findings for the design of offline RL methods for reasoning distillation?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the weight-space geometry of several offline RL methods for reasoning distillation. The authors analyze the weight-space geometry of the resulting deltas using several metrics (cosine similarity, principal-angle subspace analysis, linear mode connectivity, CKA). The results show that SFT, RFT, and RIFT have similar weight-space geometry, while DFT diverges further in direction, Offline GRPO adds a substantial component orthogonal to the SFT direction, and DPO sits in a near-orthogonal subspace with higher effective rank.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper analyzes the weight-space geometry of different offline RL methods for reasoning distillation.
- The paper shows that SFT, RFT, and RIFT have similar weight-space geometry, while DFT diverges further in direction, Offline GRPO adds a substantial component orthogonal to the SFT direction, and DPO sits in a near-orthogonal subspace with higher effective rank.

### Weaknesses

- The paper only considers a single base model (Qwen3-4B) and a single LoRA configuration (attention-only LoRA), which may limit the generalizability of the findings.
- The paper does not provide a clear explanation for the observed differences in weight-space geometry among the different offline RL methods.
- The paper does not discuss the implications of the findings for the design of offline RL methods for reasoning distillation.

### Questions

- How do the findings generalize to other base models and LoRA configurations?
- What are the implications of the findings for the design of offline RL methods for reasoning distillation?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the weight-space geometry of different offline RL methods for reasoning distillation. The authors train six methods (SFT, RFT, DFT, RIFT, Offline GRPO, DPO) on identical math rollouts from a single base model (Qwen3-4B) with attention-only LoRA and analyze the resulting deltas via cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. The results show that SFT, RFT, and RIFT have nearly colinear weight deltas, while DFT diverges further in direction than any reward-weighted method. Offline GRPO adds a substantial component orthogonal to the SFT direction, and DPO sits in a near-orthogonal subspace with higher effective rank, a sharp linear-mode barrier, and reaches the highest accuracy in the protocol on both GSM8K and AIME26.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper presents an interesting analysis of the weight-space geometry of different offline RL methods for reasoning distillation.
2. The results show that DPO sits in a near-orthogonal subspace with higher effective rank, a sharp linear-mode barrier, and reaches the highest accuracy in the protocol on both GSM8K and AIME26.

### Weaknesses

1. The paper only considers a single domain and checkpoint, which may limit the generalizability of the findings. 
2. The analysis is limited to attention-only LoRA, which may not be representative of the full range of LoRA configurations. 
3. The paper does not consider other contrastive methods such as IPO, KTO, SimPO, which may provide additional insights into the weight-space geometry of different offline RL methods. 
4. The paper does not provide a clear explanation for the observed differences in weight-space geometry among the different offline RL methods. 
5. The paper does not discuss the implications of the findings for the design of offline RL methods for reasoning distillation.

### Questions

1. How do the findings generalize to other domains and checkpoints?
2. How do different LoRA configurations affect the weight-space geometry of the offline RL methods?
3. How do other contrastive methods such as IPO, KTO, SimPO affect the weight-space geometry of the offline RL methods?
4. What are the implications of the findings for the design of offline RL methods for reasoning distillation?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents an analysis of the weight-space geometry of different offline RL methods for reasoning distillation. The authors train six methods (SFT, RFT, DFT, RIFT, Offline GRPO, DPO) on identical math rollouts from a single base model (Qwen3-4B) with attention-only LoRA and analyze the resulting deltas via cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. The results show that SFT, RFT, and RIFT have nearly colinear weight deltas, while DFT diverges further in direction than any reward-weighted method. Offline GRPO adds a substantial component orthogonal to the SFT direction, and DPO sits in a near-orthogonal subspace with higher effective rank, a sharp linear-mode barrier, and reaches the highest accuracy in the protocol on both GSM8K and AIME26.

However, the reviewers raised several concerns about the generalizability of the findings, the limited analysis of LoRA configurations, and the lack of consideration of other contrastive methods. The authors did not provide a clear explanation for the observed differences in weight-space geometry among the different offline RL methods. The paper did not discuss the implications of the findings for the design of offline RL methods for reasoning distillation. Therefore, this paper is not ready for publication.

### justification_for_why_not_higher_score

The paper only considers a single base model (Qwen3-4B) and a single LoRA configuration (attention-only LoRA), which may limit the generalizability of the findings.

### justification_for_why_not_lower_score

N/A

**********

**********

## Paper Decision

Reject (not good enough)

**********

## Paper Decision Summary

This paper is not good enough to be accepted at ICLR.

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Justification

This paper is not good enough to be accepted at ICLR.

**********

**********

## justification_for_why_not_higher_score

This paper is not good enough to be accepted at ICLR.

**********

## justification_for_why_not_lower_score

N/A

**********

## justification_for_why_not_published

This paper is not good enough to be accepted at ICLR.

**********

**********

## Paper Decision Metadata

- **Paper Decision:** Reject (not good enough)
- **Conference:** ICLR 2024

**********

## Paper Decision Comments

This paper is not good enough to be accepted at ICLR.

**********

