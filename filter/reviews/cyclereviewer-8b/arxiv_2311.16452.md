## Reviewer

### Summary

This paper presents a novel approach to improving the performance of generalist foundation models on medical challenge problems. The authors employ a systematic exploration of prompt engineering to boost performance, introducing Medprompt, a composition of several prompting strategies. Medprompt enhances GPT-4's performance, achieving state-of-the-art results on multiple medical benchmark datasets, including the MultiMedQA suite. The method outperforms specialist models like Med-PaLM 2 with significantly fewer model calls, demonstrating its efficiency and effectiveness. The paper also discusses the limitations and risks associated with the approach, emphasizing the need for further research on real-world performance and addressing potential biases and hallucinations.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method, Medprompt, is a novel and effective approach to improving the performance of generalist foundation models on medical challenge problems.
- The method outperforms specialist models like Med-PaLM 2 with significantly fewer model calls, demonstrating its efficiency and effectiveness.
- The paper also discusses the limitations and risks associated with the approach, emphasizing the need for further research on real-world performance and addressing potential biases and hallucinations.

### Weaknesses

- The paper lacks a comprehensive evaluation of the proposed method, particularly in real-world scenarios.
- The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed approach.
- The paper does not discuss potential risks and limitations of the proposed method, such as bias and hallucinations.

### Questions

- How does the proposed method perform in real-world scenarios, and what are the potential risks and limitations of using this approach in practical applications?
- How does the proposed method compare with existing approaches, and what are the advantages and disadvantages of this approach?
- What are the potential biases and hallucinations associated with the proposed method, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a new prompting strategy for GPT-4 to solve medical QA tasks. The proposed method is based on three components: 1) dynamic few-shot selection, 2) self-generated chain of thought, and 3) choice shuffle ensembling. The proposed method is evaluated on 9 benchmarks from the MultiMedQA benchmark suite. The proposed method outperforms the previous SOTA method Med-PaLM2 by a large margin with an order of magnitude fewer calls to the model. The authors also conducted ablation studies to investigate the contribution of each component.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method outperforms the previous SOTA method Med-PaLM2 by a large margin with an order of magnitude fewer calls to the model.
2. The authors conducted ablation studies to investigate the contribution of each component.
3. The proposed method is general-purpose and can be applied to other domains.

### Weaknesses

1. The proposed method is based on three components: 1) dynamic few-shot selection, 2) self-generated chain of thought, and 3) choice shuffle ensembling. However, the novelty of these components is limited. The dynamic few-shot selection is based on the kNN algorithm, which is a common approach in few-shot learning. The self-generated chain of thought is based on the previous work [1]. The choice shuffle ensembling is based on the self-consistency method [2].
2. The proposed method is only evaluated on 9 benchmarks from the MultiMedQA benchmark suite. It would be better to evaluate the proposed method on more benchmarks to demonstrate the generalization ability of the proposed method.
3. The proposed method is only evaluated on GPT-4. It would be better to evaluate the proposed method on other LLMs to demonstrate the generalization ability of the proposed method.

[1] Wang et al., "AutoPrompt: Eliciting Knowledge from Language Models with Automatically Invented Prompts", 2022

[2] Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models", 2022

### Questions

1. How does the proposed method perform on other LLMs?
2. How does the proposed method perform on other benchmarks?
3. How does the proposed method perform with different k in kNN algorithm?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper presents a study on the capabilities of GPT-4 on medical challenge benchmarks. The authors use a systematic exploration of prompt engineering to boost performance. They introduce Medprompt, a composition of several prompting strategies that greatly enhances GPT-4's performance and achieves state-of-the-art results on all nine benchmark datasets in the MultiMedQA suite. The method outperforms specialist models like Med-PaLM 2 with significantly fewer model calls, demonstrating its efficiency and effectiveness. The paper also discusses the limitations and risks associated with the approach, emphasizing the need for further research on real-world performance and addressing potential biases and hallucinations.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method, Medprompt, is a novel and effective approach to improving the performance of generalist foundation models on medical challenge problems.
- The method outperforms specialist models like Med-PaLM 2 with significantly fewer model calls, demonstrating its efficiency and effectiveness.
- The paper also discusses the limitations and risks associated with the approach, emphasizing the need for further research on real-world performance and addressing potential biases and hallucinations.

### Weaknesses

- The paper lacks a comprehensive evaluation of the proposed method, particularly in real-world scenarios.
- The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed approach.
- The paper does not discuss potential risks and limitations of the proposed method, such as bias and hallucinations.

### Questions

- How does the proposed method perform in real-world scenarios, and what are the potential risks and limitations of using this approach in practical applications?
- How does the proposed method compare with existing approaches, and what are the advantages and disadvantages of this approach?
- What are the potential biases and hallucinations associated with the proposed method, and how can they be addressed?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a novel prompting approach for GPT-4 to solve medical QA tasks. The proposed method is based on three components: 1) dynamic few-shot selection, 2) self-generated chain of thought, and 3) choice shuffle ensembling. The proposed method is evaluated on 9 benchmarks from the MultiMedQA benchmark suite. The proposed method outperforms the previous SOTA method Med-PaLM2 by a large margin with an order of magnitude fewer calls to the model. The authors also conducted ablation studies to investigate the contribution of each component.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method outperforms the previous SOTA method Med-PaLM2 by a large margin with an order of magnitude fewer calls to the model.
2. The authors conducted ablation studies to investigate the contribution of each component.
3. The proposed method is general-purpose and can be applied to other domains.

### Weaknesses

1. The proposed method is based on three components: 1) dynamic few-shot selection, 2) self-generated chain of thought, and 3) choice shuffle ensembling. However, the novelty of these components is limited. The dynamic few-shot selection is based on the kNN algorithm, which is a common approach in few-shot learning. The self-generated chain of thought is based on the previous work [1]. The choice shuffle ensembling is based on the self-consistency method [2].
2. The proposed method is only evaluated on 9 benchmarks from the MultiMedQA benchmark suite. It would be better to evaluate the proposed method on more benchmarks to demonstrate the generalization ability of the proposed method.
3. The proposed method is only evaluated on GPT-4. It would be better to evaluate the proposed method on other LLMs to demonstrate the generalization ability of the proposed method.

[1] Wang et al., "AutoPrompt: Eliciting Knowledge from Language Models with Automatically Invented Prompts", 2022

[2] Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models", 2022

### Questions

1. How does the proposed method perform on other LLMs?
2. How does the proposed method perform on other benchmarks?
3. How does the proposed method perform with different k in kNN algorithm?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents a novel approach to improving the performance of generalist foundation models on medical challenge problems. The authors employ a systematic exploration of prompt engineering to boost performance, introducing Medprompt, a composition of several prompting strategies. Medprompt enhances GPT-4's performance, achieving state-of-the-art results on multiple medical benchmark datasets, including the MultiMedQA suite. The method outperforms specialist models like Med-PaLM 2 with significantly fewer model calls, demonstrating its efficiency and effectiveness. The paper also discusses the limitations and risks associated with the approach, emphasizing the need for further research on real-world performance and addressing potential biases and hallucinations. 

The paper received mixed reviews, with two reviewers recommending acceptance and two recommending rejection. The reviewers raised concerns about the lack of a comprehensive evaluation of the proposed method, particularly in real-world scenarios, and the limited novelty of the proposed method. The authors provided a detailed response to the reviewers' concerns, addressing the issues raised and providing additional information about the proposed method. The reviewers acknowledged the authors' response and provided updated ratings. 

After careful consideration of the reviewers' comments and the authors' response, I recommend accepting the paper. The paper presents a novel approach to improving the performance of generalist foundation models on medical challenge problems, and the authors' response addresses the concerns raised by the reviewers. The paper has the potential to contribute to the field of medical AI and improve the performance of generalist foundation models on medical challenge problems.

### justification_for_why_not_higher_score

N/A

### justification_for_why_not_lower_score

The paper presents a novel approach to improving the performance of generalist foundation models on medical challenge problems. The authors employ a systematic exploration of prompt engineering to boost performance, introducing Medprompt, a composition of several prompting strategies. Medprompt enhances GPT-4's performance, achieving state-of-the-art results on multiple medical benchmark datasets, including the MultiMedQA suite. The method outperforms specialist models like Med-PaLM 2 with significantly fewer model calls, demonstrating its efficiency and effectiveness. The paper also discusses the limitations and risks associated with the approach, emphasizing the need for further research on real-world performance and addressing potential biases and hallucinations.

**********

## Paper Decision

Accept (poster) (poster) (AC: Jindřich Černota)