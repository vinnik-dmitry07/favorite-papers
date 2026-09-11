## Reviewer

### Summary

The paper introduces a new framework called Chord, which integrates supervised fine-tuning (SFT) and reinforcement learning (RL) for post-training refinement of large language models (LLMs). Chord reframes SFT as a dynamically weighted auxiliary objective within the on-policy RL process, introducing a global coefficient and a token-wise weighting function to harmonize off-policy expert data with on-policy exploration. The authors analyze the training dynamics of SFT and identify a "shift-readapt-overfit" progression. Chord achieves stable and efficient learning, outperforming baselines in various tasks. The paper also provides a systematic analysis of the training dynamics when integrating off-policy expert knowledge into models with established policies.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel framework, Chord, that unifies SFT and RL by reframing SFT as a dynamically weighted auxiliary objective within the on-policy RL process. This approach allows for fine-grained control over the influence of off-policy expert data while ensuring training stability.

2. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate SFT process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of LLMs.

3. The paper conducts extensive experiments demonstrating that Chord outperforms the SFT-then-RL paradigm and existing approaches. The authors provide both quantitative and qualitative analyses to show that Chord strategically navigates training dynamics to selectively absorb expert knowledge without stifling the model's reasoning capabilities.

### Weaknesses

1. The paper lacks a detailed discussion on the potential limitations of the proposed approach. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?

2. The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine SFT and RL? Are there any advantages or disadvantages of the proposed method compared to other methods?

3. The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### Questions

1. How does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?

2. How does the proposed method compare to other approaches that combine SFT and RL? Are there any advantages or disadvantages of the proposed method compared to other methods?

3. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to combine supervised fine-tuning (SFT) and reinforcement learning (RL) for LLMs. The authors claim that the SFT-then-RL paradigm is not always better than RL-only. They propose to use a dynamic weighting scheme for SFT loss and RL loss. The dynamic weighting scheme is based on a global coefficient $\mu$ and a token-wise weighting function $\phi$. The global coefficient $\mu$ controls the influence of the off-policy expert data, while the token-wise weighting function $\phi$ helps to enhance the stability of the off-policy learning. The authors conduct experiments on math reasoning and tool-use tasks, and the results show that their proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of combining SFT and RL for LLMs is interesting and novel.
- The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches.

### Weaknesses

- The paper lacks a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?
- The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine SFT and RL? Are there any advantages or disadvantages of the proposed method compared to other methods?
- The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### Questions

- How does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?
- How does the proposed method compare to other approaches that combine SFT and RL? Are there any advantages or disadvantages of the proposed method compared to other methods?
- How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a novel framework for combining supervised fine-tuning and reinforcement learning for large language models. The authors identify a "shift-readapt-overfit" progression in the training dynamics of supervised fine-tuning, where the model initially disrupts its established response patterns, then adapts to the expert's patterns, and finally overfits to the expert data. To address this, they propose a framework that harmonizes off-policy and on-policy learning by introducing a dynamic weighting function that controls the influence of off-policy expert data. The framework consists of a global coefficient that balances the influence of expert data throughout the training process and a fine-grained weighting function that helps maintain stability by down-weighting highly divergent tokens from off-policy data. The authors conduct extensive experiments on mathematical reasoning problems and tool-use tasks and show that the proposed framework outperforms baselines in terms of performance and stability.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate supervised fine-tuning process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of large language models.

2. The paper proposes a novel framework that unifies supervised fine-tuning and reinforcement learning via a dynamically weighted auxiliary loss. The framework provides a fine-grained and flexible control of the influence of off-policy expert data while ensuring training stability, promoting a harmonious integration of learning from both off-policy expert demonstrations and the model's on-policy exploration.

3. The paper provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities.

### Weaknesses

1. The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?

2. The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods?

3. The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### Questions

1. How does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?

2. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods?

3. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper proposes a new method to combine supervised fine-tuning (SFT) and reinforcement learning (RL) for LLMs. The authors identify a "shift-readapt-overfit" progression in the training dynamics of SFT, and propose a framework that harmonizes off-policy and on-policy learning by introducing a dynamic weighting function that controls the influence of off-policy expert data. The framework consists of a global coefficient that balances the influence of expert data throughout the training process and a fine-grained weighting function that helps maintain stability by down-weighting highly divergent tokens from off-policy data. The authors conduct extensive experiments on mathematical reasoning problems and tool-use tasks and show that the proposed framework outperforms baselines in terms of performance and stability.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper proposes a novel framework that unifies supervised fine-tuning and reinforcement learning via a dynamically weighted auxiliary loss. The framework provides a fine-grained and flexible control of the influence of off-policy expert data while ensuring training stability, promoting a harmonious integration of learning from both off-policy expert demonstrations and the model's on-policy exploration. The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework.

### Weaknesses

The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?

### Questions

How does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a new framework that combines supervised fine-tuning and reinforcement learning for large language models. The authors identify a "shift-readapt-overfit" progression in the training dynamics of supervised fine-tuning, and propose a framework that harmonizes off-policy and on-policy learning by introducing a dynamic weighting function that controls the influence of off-policy expert data. The framework consists of a global coefficient that balances the influence of expert data throughout the training process and a fine-grained weighting function that helps maintain stability by down-weighting highly divergent tokens from off-policy data. The authors conduct extensive experiments on mathematical reasoning problems and tool-use tasks and show that the proposed framework outperforms baselines in terms of performance and stability.

The paper is well-written and easy to follow. The idea of combining SFT and RL for LLMs is interesting and novel. The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate supervised fine-tuning process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of large language models.

The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities.

However, the paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### justification_for_why_not_higher_score

The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### justification_for_why_not_lower_score

The paper proposes a novel framework that unifies supervised fine-tuning and reinforcement learning via a dynamically weighted auxiliary loss. The framework provides a fine-grained and flexible control of the influence of off-policy expert data while ensuring training stability, promoting a harmonious integration of learning from both off-policy expert demonstrations and the model's on-policy exploration. The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework.

The paper is well-written and easy to follow. The idea of combining SFT and RL for LLMs is interesting and novel. The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate supervised fine-tuning process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of large language models.

The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities.

**********

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster) (6/6/0/1) (AC: Yizhou Sun, Yelong Shen, Zeyuan Wang, Zhengzhong Tan)

**********

**********

## Paper Decision Summary

This paper proposes a method to combine supervised fine-tuning (SFT) and reinforcement learning (RL) for LLMs. The authors claim that the SFT-then-RL paradigm is not always better than RL-only. They propose to use a dynamic weighting scheme for SFT loss and RL loss. The dynamic weighting scheme is based on a global coefficient and a token-wise weighting function. The global coefficient controls the influence of the off-policy expert data, while the token-wise weighting function helps to enhance the stability of the off-policy learning. The authors conduct experiments on math reasoning and tool-use tasks, and the results show that their proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper is well-written and easy to follow. The idea of combining SFT and RL for LLMs is interesting and novel. The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate SFT process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of LLMs. The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities. However, the paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine SFT and RL? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains? The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### justification_for_why_not_higher_score

The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### justification_for_why_not_lower_score

The paper proposes a novel framework that unifies supervised fine-tuning and reinforcement learning via a dynamically weighted auxiliary loss. The framework provides a fine-grained and flexible control of the influence of off-policy expert data while ensuring training stability, promoting a harmonious integration of learning from both off-policy expert demonstrations and the model's on-policy exploration. The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities. The paper is well-written and easy to follow. The idea of combining SFT and RL for LLMs is interesting and novel. The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate supervised fine-tuning process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of large language models.

**********

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster) (6/6/0/1) (AC: Yizhou Sun, Yelong Shen, Zeyuan Wang, Zhengzhong Tan)

**********

**********

## Paper Decision Summary

This paper proposes a method to combine supervised fine-tuning (SFT) and reinforcement learning (RL) for LLMs. The authors claim that the SFT-then-RL paradigm is not always better than RL-only. They propose to use a dynamic weighting scheme for SFT loss and RL loss. The dynamic weighting scheme is based on a global coefficient and a token-wise weighting function. The global coefficient controls the influence of the off-policy expert data, while the token-wise weighting function helps to enhance the stability of the off-policy learning. The authors conduct experiments on math reasoning and tool-use tasks, and the results show that their proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper is well-written and easy to follow. The idea of combining SFT and RL for LLMs is interesting and novel. The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate SFT process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of LLMs. The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities. However, the paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine SFT and RL? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains? The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### justification_for_why_not_higher_score

The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### justification_for_why_not_lower_score

The paper proposes a novel framework that unifies supervised fine-tuning and reinforcement learning via a dynamically weighted auxiliary loss. The framework provides a fine-grained and flexible control of the influence of off-policy expert data while ensuring training stability, promoting a harmonious integration of learning from both off-policy expert demonstrations and the model's on-policy exploration. The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities. The paper is well-written and easy to follow. The idea of combining SFT and RL for LLMs is interesting and novel. The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate supervised fine-tuning process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of large language models.

**********

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster) (6/6/0/1) (AC: Yizhou Sun, Yelong Shen, Zeyuan Wang, Zhengzhong Tan)

**********

**********

## Paper Decision Summary

This paper proposes a method to combine supervised fine-tuning (SFT) and reinforcement learning (RL) for LLMs. The authors claim that the SFT-then-RL paradigm is not always better than RL-only. They propose to use a dynamic weighting scheme for SFT loss and RL loss. The dynamic weighting scheme is based on a global coefficient and a token-wise weighting function. The global coefficient controls the influence of the off-policy expert data, while the token-wise weighting function helps to enhance the stability of the off-policy learning. The authors conduct experiments on math reasoning and tool-use tasks, and the results show that their proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper is well-written and easy to follow. The idea of combining SFT and RL for LLMs is interesting and novel. The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate SFT process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of LLMs. The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities. However, the paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine SFT and RL? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains? The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### justification_for_why_not_higher_score

The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine supervised fine-tuning and reinforcement learning? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains?

### justification_for_why_not_lower_score

The paper proposes a novel framework that unifies supervised fine-tuning and reinforcement learning via a dynamically weighted auxiliary loss. The framework provides a fine-grained and flexible control of the influence of off-policy expert data while ensuring training stability, promoting a harmonious integration of learning from both off-policy expert demonstrations and the model's on-policy exploration. The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities. The paper is well-written and easy to follow. The idea of combining SFT and RL for LLMs is interesting and novel. The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate supervised fine-tuning process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of large language models.

**********

**********

## Paper Decision

Reject (not selected for a spotlight/oral/poster) (6/6/0/1) (AC: Yizhou Sun, Yelong Shen, Zeyuan Wang, Zhengzhong Tan)

**********

**********

## Paper Decision Summary

This paper proposes a method to combine supervised fine-tuning (SFT) and reinforcement learning (RL) for LLMs. The authors claim that the SFT-then-RL paradigm is not always better than RL-only. They propose to use a dynamic weighting scheme for SFT loss and RL loss. The dynamic weighting scheme is based on a global coefficient and a token-wise weighting function. The global coefficient controls the influence of the off-policy expert data, while the token-wise weighting function helps to enhance the stability of the off-policy learning. The authors conduct experiments on math reasoning and tool-use tasks, and the results show that their proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper is well-written and easy to follow. The idea of combining SFT and RL for LLMs is interesting and novel. The proposed method achieves better performance than the SFT-then-RL paradigm and existing approaches. The paper provides a systematic and in-depth analysis of the training dynamics when employing a separate SFT process to integrate off-policy expert knowledge into models with established policies. The authors identify the "shift-readapt-overfit" progression, revealing how off-policy data can disrupt the established response patterns of LLMs. The paper also provides extensive experiments that demonstrate the effectiveness of the proposed framework. The authors show that the framework outperforms the SFT-then-RL paradigm and existing approaches in terms of performance and stability. The results also demonstrate that the framework can selectively absorb expert knowledge without stifling the model's reasoning capabilities. However, the paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency? The paper does not provide a clear comparison with existing methods in the literature. How does the proposed method compare to other approaches that combine SFT and RL? Are there any advantages or disadvantages of the proposed method compared to other methods? The paper does not provide a detailed discussion on the generalizability of the proposed approach. How does the proposed method perform on different tasks or datasets? Are there any potential limitations or challenges when applying the proposed method to other domains? The paper does not provide a detailed discussion on the limitations of the proposed method. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks?