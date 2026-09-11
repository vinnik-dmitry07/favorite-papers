## Summary

The paper proposes a novel approach to mitigate reward hacking in reinforcement learning from human feedback (RLHF) and verifiable rewards (RLVR) by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

2 fair

## Presentation

3 good

## Contribution

2 fair

## Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR.
3. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

1. The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method.
3. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

------------------

## Summary

The paper proposes a novel approach to mitigate reward hacking in reinforcement learning from human feedback (RLHF) and verifiable rewards (RLVR) by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

2 fair

## Presentation

3 good

## Contribution

2 fair

## Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR.
3. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

1. The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method.
3. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Summary

This paper proposes a method to prevent reward hacking in RL post-training of LLMs by biasing policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

2 fair

## Presentation

3 good

## Contribution

2 fair

## Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Summary

This paper studies the problem of reward hacking in RLHF and RLVR, and proposes a novel approach to mitigate this issue by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR.
3. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

1. The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method.
3. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

5: marginally below the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a method to prevent reward hacking in RL post-training of LLMs by biasing policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach. However, the paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## justification_for_why_not_higher_score

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## justification_for_why_not_lower_score

N/A

**********

---Post-rebuttal---

I thank the authors for their response. I have read the reviews and the rebuttal. I have also read the other reviewers' responses. I agree with the reviewers that the paper has some limitations, but I think the authors have addressed most of the concerns. I would recommend the authors to address the remaining concerns and improve the paper before submitting it to another venue.

## Score
6: marginally above the acceptance threshold

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

This paper proposes a novel approach to mitigate reward hacking in RLHF and RLVR by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR.
3. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

1. The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method.
3. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

This paper proposes a method to prevent reward hacking in RL post-training of LLMs. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

This paper proposes a method to prevent reward hacking in RL post-training of LLMs. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Meta Review

This paper proposes a method to prevent reward hacking in RL post-training of LLMs by biasing policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach. However, the paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## justification_for_why_not_higher_score

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## justification_for_why_not_lower_score

N/A

**********

---

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

This paper proposes a novel approach to mitigate reward hacking in RLHF and RLVR by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR.
3. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

1. The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method.
3. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

This paper proposes a method to prevent reward hacking in RL post-training of LLMs. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

This paper proposes a novel approach to mitigate reward hacking in RLHF and RLVR by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

The paper proposes a novel approach to mitigate reward hacking in RLHF and RLVR by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

This paper proposes a novel approach to mitigate reward hacking in RLHF and RLVR by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

This paper proposes a novel approach to mitigate reward hacking in RLHF and RLVR by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster)

**********

## Paper Decision View

Reject (not selected for a spotlight/oral/poster)

**********

---

## Reviewer

## Summary

This paper proposes a novel approach to mitigate reward hacking in RLHF and RLVR by employing gradient regularization (GR) to bias policy updates towards regions with accurate rewards. The authors provide a theoretical connection between reward model accuracy and the flatness of the optimum at convergence, suggesting that GR can maintain reward model accuracy. They empirically demonstrate that GR outperforms a KL penalty across various RL experiments with language models, achieving higher GPT-judged win-rates, avoiding overemphasis on format in rule-based math rewards, and preventing hacking of the judge in LLM-as-a-Judge math tasks.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

The paper is well-written and easy to follow. The proposed method is novel and effective in preventing reward hacking in RLHF and RLVR. The theoretical analysis provides a solid foundation for the proposed approach.

## Weaknesses

The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not discuss the limitations of the proposed method and potential future research directions.

## Questions

1. How does the proposed method compare to other existing methods for preventing reward hacking in RLHF and RLVR?
2. Can the proposed method be applied to other types of reinforcement learning tasks beyond RLHF and RLVR?
3. How does the proposed method scale to larger datasets and more complex tasks?
4. What are the computational costs associated with the proposed method?
5. What are the limitations of the proposed method, and what are some potential future research directions?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of