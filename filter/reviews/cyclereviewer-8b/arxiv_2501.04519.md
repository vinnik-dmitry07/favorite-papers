## Reviewer

### Summary

This paper proposes rStar-Math, a self-evolved System 2-style reasoning approach that achieves the state-of-the-art math reasoning, rivaling and sometimes even surpassing OpenAI o1 on challenging math competition benchmarks with a model size as small as 7 billion. rStar-Math leverages smaller language models (SLMs) with Monte Carlo Tree Search (MCTS) to establish a self-evolutionary process, iteratively generating higher-quality training data. To achieve self-evolution, rStar-Math introduces three key innovations: 1) a novel code-augmented CoT data synthesis method, 2) a novel process reward model training method, 3) a self-evolution recipe.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is interesting and novel. 
- The paper is well-written and easy to follow. 
- The proposed method achieves SOTA performance on math reasoning benchmarks.

### Weaknesses

- The proposed method requires a large amount of compute resources to train the models. 
- The proposed method is not generalizable to other tasks. 

I am willing to increase my score if the authors can address the above two concerns.

### Questions

- The proposed method requires a large amount of compute resources to train the models. It is unclear how much compute resources are required to train the proposed method. 
- The proposed method is not generalizable to other tasks. It is unclear how the proposed method can be applied to other tasks. 

I am willing to increase my score if the authors can address the above two concerns.

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper introduces rStar-Math, a novel approach that leverages smaller language models (SLMs) and Monte Carlo Tree Search (MCTS) to enhance math reasoning capabilities. rStar-Math is designed to rival or surpass the math reasoning abilities of OpenAI's o1 model without relying on distillation from larger models. The approach involves three key innovations: a code-augmented data synthesis method, a novel process reward model training method, and a self-evolution recipe. rStar-Math demonstrates state-of-the-art performance on math reasoning benchmarks, outperforming o1 in some cases and achieving results comparable to it in others.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper presents a novel approach to math reasoning that leverages smaller language models and Monte Carlo Tree Search, which is both innovative and effective.
- The paper is well-structured and easy to follow, with clear explanations of the methodology and results.
- The results are promising, with rStar-Math demonstrating state-of-the-art performance on math reasoning benchmarks.

### Weaknesses

- The paper does not provide a clear explanation of the computational resources required for the proposed approach, which may limit its practical applicability.
- The paper does not provide a clear explanation of the limitations of the proposed approach, which may limit its generalizability to other tasks or domains.

### Questions

- How does the proposed approach compare to other approaches in terms of computational resources and efficiency?
- How does the proposed approach generalize to other tasks or domains beyond math reasoning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper introduces a novel approach to math reasoning using smaller language models (SLMs) and Monte Carlo Tree Search (MCTS). The authors propose three key innovations: a code-augmented data synthesis method, a novel process reward model training method, and a self-evolution recipe. The paper presents a well-structured and easy-to-follow narrative, with clear explanations of the methodology and results. The results are promising, with rStar-Math demonstrating state-of-the-art performance on math reasoning benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper presents a novel approach to math reasoning that leverages smaller language models and Monte Carlo Tree Search, which is both innovative and effective.
- The paper is well-structured and easy to follow, with clear explanations of the methodology and results.
- The results are promising, with rStar-Math demonstrating state-of-the-art performance on math reasoning benchmarks.

### Weaknesses

- The paper does not provide a clear explanation of the computational resources required for the proposed approach, which may limit its practical applicability.
- The paper does not provide a clear explanation of the limitations of the proposed approach, which may limit its generalizability to other tasks or domains.

### Questions

- How does the proposed approach compare to other approaches in terms of computational resources and efficiency?
- How does the proposed approach generalize to other tasks or domains beyond math reasoning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method to improve the math reasoning capability of small language models. The method is based on Monte Carlo Tree Search (MCTS) and consists of three main components: 1) a code-augmented CoT data synthesis method, 2) a novel process reward model training method, and 3) a self-evolution recipe. The proposed method is evaluated on several math benchmarks, and the results show that the proposed method can improve the math reasoning capability of small language models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and effective. The method is based on MCTS, which is a well-known method in the field of AI. The code-augmented CoT data synthesis method is also novel and effective. The process reward model training method is also novel and effective.
2. The proposed method is evaluated on several math benchmarks, and the results show that the proposed method can improve the math reasoning capability of small language models.
3. The paper is well-written and easy to follow.

### Weaknesses

1. The proposed method requires a large amount of compute resources to train the models.
2. The proposed method is not generalizable to other tasks.

### Questions

1. How does the proposed method compare to other methods in terms of computational resources and efficiency?
2. How does the proposed method generalize to other tasks or domains beyond math reasoning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents a novel approach to math reasoning using smaller language models (SLMs) and Monte Carlo Tree Search (MCTS). The authors propose three key innovations: a code-augmented data synthesis method, a novel process reward model training method, and a self-evolution recipe. The paper presents a well-structured and easy-to-follow narrative, with clear explanations of the methodology and results. The results are promising, with rStar-Math demonstrating state-of-the-art performance on math reasoning benchmarks.

### justification_for_why_not_higher_score

The paper is not generalizable to other tasks or domains beyond math reasoning.

### justification_for_why_not_lower_score

The paper presents a novel approach to math reasoning that leverages smaller language models and Monte Carlo Tree Search, which is both innovative and effective. The paper is well-structured and easy to follow, with clear explanations of the methodology and results. The results are promising, with rStar-Math demonstrating state-of-the-art performance on math reasoning benchmarks.

**********

## Paper Decision

Accept (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (