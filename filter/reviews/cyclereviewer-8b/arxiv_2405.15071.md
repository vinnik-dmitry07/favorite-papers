## Reviewer

### Summary

The paper studies the ability of transformers to learn to implicitly reason over parametric knowledge. The paper uses two tasks, composition and comparison, and finds that transformers can learn to implicitly reason, but only through grokking, i.e., extended training far beyond overfitting. The paper also analyzes the model's internals and finds that the mechanism behind grokking is the formation of the generalizing circuit and its relation to the relative efficiency of generalizing and memorizing circuits. The paper also finds that the connection between systematicity and the configuration of the generalizing circuit.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The experiments are thorough and the results are interesting.

### Weaknesses

The paper is limited in its scope and does not fully explore the implications of its findings. The paper only studies two tasks, composition and comparison, and does not consider other types of reasoning, such as logical reasoning. The paper also does not consider other types of models, such as recurrent neural networks or graph neural networks, and only studies transformers. The paper also does not provide a comprehensive analysis of the limitations of the transformer architecture and does not consider potential solutions to address these limitations.

### Questions

1. How do the results generalize to other types of reasoning, such as logical reasoning?
2. How do the results generalize to other types of models, such as recurrent neural networks or graph neural networks?
3. What are the limitations of the transformer architecture and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies whether transformers can learn to implicitly reason over parametric knowledge. The authors construct synthetic training and evaluation datasets, train transformers from scratch, and examine their generalization. The authors find that transformers can learn to perform implicit reasoning, but this skill is only robustly acquired through extended training far beyond overfitting. The authors also find that the transformer exhibits different levels of systematicity across reasoning types. The authors conduct mechanistic analysis of the internal mechanisms of the model to understand why this happens. The authors also show that for a challenging reasoning task with a large search space, a fully grokked transformer can achieve near-perfect accuracy, while state-of-the-art LLMs like GPT-4-Turbo and Gemini-1.5-Pro based on non-parametric memory fail badly regardless of prompting styles or retrieval augmentation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper studies an important problem of whether transformers can learn to implicitly reason over parametric knowledge. The authors conduct extensive experiments to show that transformers can learn to perform implicit reasoning, but this skill is only robustly acquired through extended training far beyond overfitting. The authors also conduct mechanistic analysis of the internal mechanisms of the model to understand why this happens.

2. The authors also show that for a challenging reasoning task with a large search space, a fully grokked transformer can achieve near-perfect accuracy, while state-of-the-art LLMs like GPT-4-Turbo and Gemini-1.5-Pro based on non-parametric memory fail badly regardless of prompting styles or retrieval augmentation.

### Weaknesses

1. The authors only study two tasks, composition and comparison, and do not consider other types of reasoning, such as logical reasoning. It is not clear whether the findings of this paper can be generalized to other types of reasoning.

2. The authors only study transformers and do not consider other types of models, such as recurrent neural networks or graph neural networks. It is not clear whether the findings of this paper can be generalized to other types of models.

### Questions

1. Can the authors explain why the authors only study two tasks, composition and comparison, and do not consider other types of reasoning, such as logical reasoning?

2. Can the authors explain why the authors only study transformers and do not consider other types of models, such as recurrent neural networks or graph neural networks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the ability of transformers to learn to implicitly reason over parametric knowledge. The authors study two tasks: composition and comparison. They find that transformers can learn to perform implicit reasoning, but this skill is only robustly acquired through extended training far beyond overfitting. The authors also conduct mechanistic analysis of the internal mechanisms of the model to understand why this happens. The authors also show that for a challenging reasoning task with a large search space, a fully grokked transformer can achieve near-perfect accuracy, while state-of-the-art LLMs like GPT-4-Turbo and Gemini-1.5-Pro based on non-parametric memory fail badly regardless of prompting styles or retrieval augmentation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper studies an important problem of whether transformers can learn to implicitly reason over parametric knowledge. The authors conduct extensive experiments to show that transformers can learn to perform implicit reasoning, but this skill is only robustly acquired through extended training far beyond overfitting. The authors also conduct mechanistic analysis of the internal mechanisms of the model to understand why this happens.

2. The authors also show that for a challenging reasoning task with a large search space, a fully grokked transformer can achieve near-perfect accuracy, while state-of-the-art LLMs like GPT-4-Turbo and Gemini-1.5-Pro based on non-parametric memory fail badly regardless of prompting styles or retrieval augmentation.

### Weaknesses

1. The authors only study two tasks, composition and comparison, and do not consider other types of reasoning, such as logical reasoning. It is not clear whether the findings of this paper can be generalized to other types of reasoning.

2. The authors only study transformers and do not consider other types of models, such as recurrent neural networks or graph neural networks. It is not clear whether the findings of this paper can be generalized to other types of models.

### Questions

1. Can the authors explain why the authors only study two tasks, composition and comparison, and do not consider other types of reasoning, such as logical reasoning?

2. Can the authors explain why the authors only study transformers and do not consider other types of models, such as recurrent neural networks or graph neural networks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper investigates the ability of transformers to learn to reason implicitly over parametric knowledge. The authors create synthetic training and evaluation datasets, train transformers from scratch, and examine their generalization. The authors find that transformers can learn to perform implicit reasoning, but this skill is only robustly acquired through extended training far beyond overfitting. The authors also find that the transformer exhibits different levels of systematicity across reasoning types. The authors conduct mechanistic analysis of the internal mechanisms of the model to understand why this happens. The authors also show that for a challenging reasoning task with a large search space, a fully grokked transformer can achieve near-perfect accuracy, while state-of-the-art LLMs like GPT-4-Turbo and Gemini-1.5-Pro based on non-parametric memory fail badly regardless of prompting styles or retrieval augmentation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper studies an important problem of whether transformers can learn to implicitly reason over parametric knowledge. The authors conduct extensive experiments to show that transformers can learn to perform implicit reasoning, but this skill is only robustly acquired through extended training far beyond overfitting. The authors also conduct mechanistic analysis of the internal mechanisms of the model to understand why this happens.

2. The authors also show that for a challenging reasoning task with a large search space, a fully grokked transformer can achieve near-perfect accuracy, while state-of-the-art LLMs like GPT-4-Turbo and Gemini-1.5-Pro based on non-parametric memory fail badly regardless of prompting styles or retrieval augmentation.

### Weaknesses

1. The authors only study two tasks, composition and comparison, and do not consider other types of reasoning, such as logical reasoning. It is not clear whether the findings of this paper can be generalized to other types of reasoning.

2. The authors only study transformers and do not consider other types of models, such as recurrent neural networks or graph neural networks. It is not clear whether the findings of this paper can be generalized to other types of models.

### Questions

1. Can the authors explain why the authors only study two tasks, composition and comparison, and do not consider other types of reasoning, such as logical reasoning?

2. Can the authors explain why the authors only study transformers and do not consider other types of models, such as recurrent neural networks or graph neural networks?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the ability of transformers to learn to implicitly reason over parametric knowledge. The authors study two tasks, composition and comparison, and find that transformers can learn to perform implicit reasoning, but this skill is only robustly acquired through extended training far beyond overfitting. The authors also conduct mechanistic analysis of the internal mechanisms of the model to understand why this happens. The authors also show that for a challenging reasoning task with a large search space, a fully grokked transformer can achieve near-perfect accuracy, while state-of-the-art LLMs like GPT-4-Turbo and Gemini-1.5-Pro based on non-parametric memory fail badly regardless of prompting styles or retrieval augmentation. The reviewers agree that this paper studies an important problem, and the experiments are thorough and the results are interesting. The authors have addressed the concerns of the reviewers. I recommend acceptance.

### justification_for_why_not_higher_score

N/A

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Accept (poster)