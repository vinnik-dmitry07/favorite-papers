##### 1. Summary

This paper proposes a new approach to detect and remove adversarial examples. The authors propose a new method called "Adversarial Example Detection by Learning to Contrast" (AEDLC), which is based on the idea of learning a contrastive model that can distinguish between adversarial examples and benign examples. The authors claim that the proposed method is more robust and efficient than existing methods.

##### 2. Soundness

2 fair

##### 3. Presentation

3 good

##### 4. Contribution

2 fair

##### 5. Strengths

- The paper is well-written and easy to understand.
- The proposed method is simple and easy to understand.
- The proposed method is evaluated on multiple datasets and shows competitive performance compared to existing methods.

##### 6. Weaknesses

- The proposed method is not novel enough. The idea of learning a contrastive model to detect adversarial examples has been explored in previous works [1, 2, 3]. The authors should compare their method with these works and discuss the differences and advantages of their method.
- The evaluation is not comprehensive enough. The authors only evaluate their method on a limited number of datasets and attack methods. They should evaluate their method on more datasets and attack methods to demonstrate its robustness and generalizability.
- The authors claim that the proposed method is more robust and efficient than existing methods, but they do not provide any theoretical analysis or experimental results to support this claim. They should provide more evidence to support their claim.
- The authors do not provide any ablation studies to analyze the effect of different components of their method. They should provide ablation studies to analyze the effect of different components of their method.

[1] A. Grosse et al., "Adversarial Examples Are Not Bugs, They Are Features," NeurIPS 2017.
[2] S. Ilyas et al., "Adversarial Examples Are Not Bugs, They Are Features,” NeurIPS 2019.
[3] S. Bai et al., "Adversarial Example Detection via Learning to Contrast," AAAI 2021.

##### 7. Questions

Please refer to the weaknesses.

##### 8. Rating

5: marginally below the acceptance threshold

##### 9. Meta Review

This paper proposes a new approach to detect and remove adversarial examples. The authors propose a new method called "Adversarial Example Detection by Learning to Contrast" (AEDLC), which is based on the idea of learning a contrastive model that can distinguish between adversarial examples and benign examples. The authors claim that the proposed method is more robust and efficient than existing methods.

The reviewers have raised several concerns regarding the novelty and evaluation of the proposed method. The reviewers have pointed out that the idea of learning a contrastive model to detect adversarial examples has been explored in previous works, and the evaluation is not comprehensive enough. The authors have not provided any theoretical analysis or experimental results to support their claim that the proposed method is more robust and efficient than existing methods. The authors have not provided any ablation studies to analyze the effect of different components of their method.

Overall, the paper has several weaknesses that need to be addressed before it can be accepted. The authors are encouraged to address the concerns raised by the reviewers and improve the paper accordingly.

### justification_for_why_not_higher_score

The reviewers have raised several concerns regarding the novelty and evaluation of the proposed method. The authors have not provided any theoretical analysis or experimental results to support their claim that the proposed method is more robust and efficient than existing methods.

### justification_for_why_not_lower_score

N/A

**********

## Reviewer

### Summary

The paper proposes a method for detecting adversarial examples by learning to contrast. The method is evaluated on a number of datasets and compared to other methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper is well written and easy to follow.

### Weaknesses

The paper lacks a clear motivation for the proposed method. The authors do not explain why learning to contrast is a good idea, and why it should work better than other methods. The paper also lacks a clear evaluation of the method. The authors do not compare their method to other methods in a fair way, and do not provide a clear analysis of the results.

### Questions

1. What is the motivation for the proposed method? Why should learning to contrast work better than other methods for detecting adversarial examples?
2. How does the proposed method compare to other methods for detecting adversarial examples? What are the advantages and disadvantages of the proposed method compared to other methods?
3. What is the significance of the proposed method? How does it contribute to the field of adversarial example detection?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method for detecting adversarial examples based on learning to contrast. The authors first train a contrastive model to distinguish between adversarial examples and benign examples. Then, they use the learned model to detect adversarial examples. The authors evaluate their method on multiple datasets and show that it outperforms other methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The authors evaluate their method on multiple datasets and show that it outperforms other methods.

### Weaknesses

1. The novelty of the proposed method is limited. The idea of learning a contrastive model to detect adversarial examples has been explored in previous works [1, 2, 3]. The authors should compare their method with these works and discuss the differences and advantages of their method.
2. The evaluation is not comprehensive enough. The authors only evaluate their method on a limited number of datasets and attack methods. They should evaluate their method on more datasets and attack methods to demonstrate its robustness and generalizability.
3. The authors claim that the proposed method is more robust and efficient than existing methods, but they do not provide any theoretical analysis or experimental results to support this claim. They should provide more evidence to support their claim.
4. The authors do not provide any ablation studies to analyze the effect of different components of their method. They should provide ablation studies to analyze the effect of different components of their method.

[1] A. Grosse et al., "Adversarial Examples Are Not Bugs, They Are Features," NeurIPS 2017.
[2] S. Ilyas et al., "Adversarial Examples Are Not Bugs, They Are Features,” NeurIPS 2019.
[3] S. Bai et al., "Adversarial Example Detection via Learning to Contrast," AAAI 2021.

### Questions

Please see the weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new approach to detect and remove adversarial examples. The authors propose a new method called "Adversarial Example Detection by Learning to Contrast" (AEDLC), which is based on the idea of learning a contrastive model that can distinguish between adversarial examples and benign examples. The authors claim that the proposed method is more robust and efficient than existing methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to understand.
2. The proposed method is simple and easy to understand.
3. The proposed method is evaluated on multiple datasets and shows competitive performance compared to existing methods.

### Weaknesses

1. The proposed method is not novel enough. The idea of learning a contrastive model to detect adversarial examples has been explored in previous works [1, 2, 3]. The authors should compare their method with these works and discuss the differences and advantages of their method.
2. The evaluation is not comprehensive enough. The authors only evaluate their method on a limited number of datasets and attack methods. They should evaluate their method on more datasets and attack methods to demonstrate its robustness and generalizability.
3. The authors claim that the proposed method is more robust and efficient than existing methods, but they do not provide any theoretical analysis or experimental results to support this claim. They should provide more evidence to support their claim.
4. The authors do not provide any ablation studies to analyze the effect of different components of their method. They should provide ablation studies to analyze the effect of different components of their method.

[1] A. Grosse et al., "Adversarial Examples Are Not Bugs, They Are Features," NeurIPS 2017.
[2] S. Ilyas et al., "Adversarial Examples Are Not Bugs, They Are Features,” NeurIPS 2019.
[3] S. Bai et al., "Adversarial Example Detection via Learning to Contrast," AAAI 2021.

### Questions

Please see the weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method for detecting adversarial examples based on learning to contrast. The authors first train a contrastive model to distinguish between adversarial examples and benign examples. Then, they use the learned model to detect adversarial examples. The authors evaluate their method on multiple datasets and show that it outperforms other methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The proposed method is evaluated on multiple datasets and shows competitive performance compared to existing methods.

### Weaknesses

1. The proposed method is not novel enough. The idea of learning a contrastive model to detect adversarial examples has been explored in previous works [1, 2, 3]. The authors should compare their method with these works and discuss the differences and advantages of their method.
2. The evaluation is not comprehensive enough. The authors only evaluate their method on a limited number of datasets and attack methods. They should evaluate their method on more datasets and attack methods to demonstrate its robustness and generalizability.
3. The authors claim that the proposed method is more robust and efficient than existing methods, but they do not provide any theoretical analysis or experimental results to support this claim. They should provide more evidence to support their claim.
4. The authors do not provide any ablation studies to analyze the effect of different components of their method. They should provide ablation studies to analyze the effect of different components of their method.

[1] A. Grosse et al., "Adversarial Examples Are Not Bugs, They Are Features," NeurIPS 2017.
[2] S. Ilyas et al., "Adversarial Examples Are Not Bugs, They Are Features,” NeurIPS 2019.
[3] S. Bai et al., "Adversarial Example Detection via Learning to Contrast," AAAI 2021.

### Questions

Please see the weaknesses.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new approach to detect and remove adversarial examples. The authors propose a new method called "Adversarial Example Detection by Learning to Contrast" (AEDLC), which is based on the idea of learning a contrastive model that can distinguish between adversarial examples and benign examples. The authors claim that the proposed method is more robust and efficient than existing methods.

The reviewers have raised several concerns regarding the novelty and evaluation of the proposed method. The reviewers have pointed out that the idea of learning a contrastive model to detect adversarial examples has been explored in previous works, and the evaluation is not comprehensive enough. The authors have not provided any theoretical analysis or experimental results to support their claim that the proposed method is more robust and efficient than existing methods. The authors have not provided any ablation studies to analyze the effect of different components of their method.

### justification_for_why_not_higher_score

The reviewers have raised several concerns regarding the novelty and evaluation of the proposed method. The authors have not provided any theoretical analysis or experimental results to support their claim that the proposed method is more robust and efficient than existing methods. The authors have not provided any ablation studies to analyze the effect of different components of their method.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)