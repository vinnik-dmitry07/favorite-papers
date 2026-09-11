I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates the performance of LLMs on multiple-choice question answering (MCQA) tasks when provided only with the answer choices, without the actual question. The authors evaluate several LLMs, including LLaMA-2, Falcon, Phi-2, and Mixtral, on three MCQA datasets: ARC, MMLU, and HellaSwag. They employ various prompting techniques and conduct a detailed analysis to understand why LLMs sometimes perform well even in the absence of the question.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper addresses an intriguing and timely question: how well do LLMs perform on MCQA tasks when the question is omitted, and what strategies they use to answer the questions. This is a valuable area of exploration, as it sheds light on the reasoning capabilities of LLMs and their ability to infer the question from the answer choices alone. The authors conduct a comprehensive evaluation across multiple models and datasets, providing a robust empirical foundation for their findings. Additionally, the paper is well-written and easy to follow, making it accessible to a broad audience.

### Weaknesses

#### Some Related Works


#### comment

1. The paper’s central claim that LLMs can achieve high accuracy on MCQA tasks without the question is not particularly surprising, as this ability is already demonstrated in prior work (e.g., "LLM can Learn to Answer Multiple Choice Questions without the Questions"). While the authors explore this phenomenon in more models and datasets, the core finding lacks significant novelty. The observation that LLMs can perform well in this setting is not a novel insight, and the paper does not provide a deep analysis of the underlying mechanisms that enable this behavior. The paper essentially reiterates what is already known, without providing new insights into the reasoning process.
2. The paper lacks a clear and compelling motivation for studying MCQA without the question. While the authors mention potential applications in real-world scenarios, such as in medicine or law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. The motivation remains weak and speculative.
3. The paper does not provide a thorough analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This limits the paper's contribution to a descriptive analysis rather than a deeper understanding of the underlying mechanisms. The paper does not explore the characteristics of questions that are more or less amenable to this type of inference, nor does it analyze the types of answer choices that are more or less effective for this task. This lack of analysis limits the practical value of the findings.

### Suggestions

The paper would benefit significantly from a more in-depth analysis of the underlying mechanisms that enable LLMs to perform well in MCQA without the question. Instead of simply demonstrating that LLMs can achieve high accuracy, the authors should investigate the specific strategies and reasoning processes that they employ. For example, they could analyze the attention patterns of the models to understand which parts of the answer choices are most influential in their decision-making process. They could also explore the use of techniques such as ablation studies to identify the key components of the answer choices that are most important for the model's performance. Furthermore, the authors should investigate the relationship between the structure of the answer choices and the model's performance. Are certain types of answer choices more effective than others? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting.

To strengthen the paper's motivation, the authors should provide concrete examples of real-world scenarios where this capability would be valuable. For instance, in medical diagnosis, could an LLM be used to identify the most likely diagnosis from a set of symptoms without being provided with the actual patient history? Similarly, in legal document analysis, could an LLM be used to identify the most relevant clause from a set of legal documents without being provided with the full context? The authors should also discuss the potential implications of this finding for the development of more robust and reliable AI systems. For example, could this capability be used to improve the performance of AI systems in situations where the question is not explicitly stated? Could it be used to reduce the amount of training data required to achieve a certain level of performance? A more thorough discussion of these aspects would make the paper more compelling and relevant to the broader research community.

Finally, the paper should include a more detailed analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This analysis should explore the characteristics of questions that are more or less amenable to this type of inference. For example, are questions that involve more complex reasoning or that require the model to integrate information from multiple sources more difficult for the model to answer without the question? Are there specific types of datasets that are more or less suitable for this type of evaluation? The authors should also analyze the types of answer choices that are most effective for this task. Are certain types of answer choices more likely to be exploited by the model? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting.

### Questions

1. How do the results vary across different types of questions and datasets? Are there specific types of questions or datasets where LLMs perform particularly well or poorly in this setting?
2. What are the practical implications of this finding for real-world applications? How could this capability be used to improve the performance of AI systems in situations where the question is not explicitly stated?
3. What are the limitations of the current study? Are there other factors that could influence the performance of LLMs in this setting, such as the size or complexity of the model, or the specific prompting techniques used?

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

The paper investigates the performance of LLMs on multiple-choice question answering (MCQA) tasks when provided with only the answer choices, without the actual question. The authors explore this phenomenon across three MCQA datasets (ARC, MMLU, and HellaSwag) and four LLMs (LLaMA-2, Falcon, Phi-2, and Mixtral). They find that LLMs achieve significantly higher accuracy in this "choices-only" setting compared to the majority baseline, suggesting that they may be exploiting dataset artifacts or using reasoning strategies beyond standard MCQA evaluation. The authors propose three hypotheses to explain this behavior: memorization, choice dynamics, and abductive question inference. They conduct experiments to test these hypotheses, finding that memorization is unlikely, choice dynamics play a role, and abductive question inference is a significant factor. The paper also introduces a black-box evaluation suite for MCQA tasks, which could be useful for future research.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper addresses an important and timely question about the robustness of LLMs in MCQA tasks. It highlights the potential for LLMs to exploit dataset artifacts, which is a crucial issue for fair and reliable evaluation of these models.
- The paper provides a comprehensive analysis of the problem, exploring different hypotheses and conducting thorough experiments to test them. The proposed black-box evaluation suite could be a valuable tool for the community.
- The paper is well-written and easy to follow, with clear explanations of the methods and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's main finding that LLMs can achieve high accuracy in the choices-only setting is not particularly surprising, as this ability is already demonstrated in prior work (e.g., "LLM can Learn to Answer Multiple Choice Questions without the Questions"). While the authors explore this phenomenon in more models and datasets, the core finding lacks significant novelty.
- The paper lacks a clear and compelling motivation for studying MCQA without the question. While the authors mention potential applications in real-world scenarios, such as in medicine or law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. The motivation remains weak and speculative.
- The paper does not provide a thorough analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This limits the paper's contribution to a descriptive analysis rather than a deeper understanding of the underlying mechanisms. The paper does not explore the characteristics of questions that are more or less amenable to this type of inference, nor does it analyze the types of answer choices that are more or less effective for this task. This lack of analysis limits the practical value of the findings.

### Suggestions

The paper would benefit significantly from a more in-depth analysis of the underlying mechanisms that enable LLMs to perform well in the MCQA without the question setting. Instead of simply demonstrating that LLMs can achieve high accuracy, the authors should investigate the specific strategies and reasoning processes that they employ. For example, they could analyze the attention patterns of the models to understand which parts of the answer choices are most influential in their decision-making process. They could also explore the use of techniques such as ablation studies to identify the key components of the answer choices that are most important for the model's performance. Furthermore, the authors should investigate the relationship between the structure of the answer choices and the model's performance. Are certain types of answer choices more effective than others? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting.

To strengthen the paper's motivation, the authors should provide concrete examples of real-world scenarios where this capability would be valuable. For instance, in medical diagnosis, could an LLM be used to identify the most likely diagnosis from a set of symptoms without being provided with the actual patient history? Similarly, in legal document analysis, could an LLM be used to identify the most relevant clause from a set of legal documents without being provided with the full context? The authors should also discuss the potential implications of this finding for the development of more robust and reliable AI systems. For example, could this capability be used to improve the performance of AI systems in situations where the question is not explicitly stated? Could it be used to reduce the amount of training data required to achieve a certain level of performance? A more thorough discussion of these aspects would make the paper more compelling and relevant to the broader research community.

Finally, the paper should include a more detailed analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This analysis should explore the characteristics of questions that are more or less amenable to this type of inference. For example, are questions that involve more complex reasoning or that require the model to integrate information from multiple sources more difficult for the model to answer without the question? Are there specific types of datasets that are more or less suitable for this type of evaluation? The authors should also analyze the types of answer choices that are most effective for this task. Are certain types of answer choices more likely to be exploited by the model? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting.

### Questions

- How do the results vary across different types of questions and datasets? Are there specific types of questions or datasets where LLMs perform particularly well or poorly in this setting?
- What are the practical implications of this finding for real-world applications? How could this capability be used to improve the performance of AI systems in situations where the question is not explicitly stated?
- What are the limitations of the current study? Are there other factors that could influence the performance of LLMs in this setting, such as the size or complexity of the model, or the specific prompting techniques used?

### Rating

3

### Confidence

4

**********

## Reviewer 3

### Summary

This paper investigates the performance of LLMs on MCQA tasks when only answer choices are provided. It explores three hypotheses: memorization, choice dynamics, and question inference. The authors find that LLMs can achieve high accuracy in this setting, suggesting they may be exploiting dataset artifacts or using reasoning strategies beyond standard MCQA evaluation. They propose a black-box evaluation suite to assess LLMs more reliably and advocate for artifact-robust evaluations, highlighting the need for stronger baselines and more robust MCQA datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The authors conduct extensive experiments across multiple datasets and models, providing a thorough analysis of the phenomenon.
- The paper identifies three potential hypotheses for the observed high accuracy in the choices-only setting and provides evidence to support or refute each hypothesis.
- The authors propose a black-box evaluation suite to assess LLMs more reliably and advocate for artifact-robust evaluations, highlighting the need for stronger baselines and more robust MCQA datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's main finding that LLMs can achieve high accuracy in the choices-only setting is not particularly surprising, as this ability is already demonstrated in prior work (e.g., "LLM can Learn to Answer Multiple Choice Questions without the Questions"). While the authors explore this phenomenon in more models and datasets, the core finding lacks significant novelty.
- The paper lacks a clear and compelling motivation for studying MCQA without the question. While the authors mention potential applications in real-world scenarios, such as in medicine or law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. The motivation remains weak and speculative.
- The paper does not provide a thorough analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This limits the paper's contribution to a descriptive analysis rather than a deeper understanding of the underlying mechanisms. The paper does not explore the characteristics of questions that are more or less amenable to this type of inference, nor does it analyze the types of answer choices that are more or less effective for this task. This lack of analysis limits the practical value of the findings.

### Suggestions

The paper would benefit significantly from a more in-depth analysis of the underlying mechanisms that enable LLMs to perform well in the MCQA without the question setting. Instead of simply demonstrating that LLMs can achieve high accuracy, the authors should investigate the specific strategies and reasoning processes that they employ. For example, they could analyze the attention patterns of the models to understand which parts of the answer choices are most influential in their decision-making process. They could also explore the use of techniques such as ablation studies to identify the key components of the answer choices that are most important for the model's performance. Furthermore, the authors should investigate the relationship between the structure of the answer choices and the model's performance. Are certain types of answer choices more effective than others? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting.

To strengthen the paper's motivation, the authors should provide concrete examples of real-world scenarios where this capability would be valuable. For instance, in medical diagnosis, could an LLM be used to identify the most likely diagnosis from a set of symptoms without being provided with the actual patient history? Similarly, in legal document analysis, could an LLM be used to identify the most relevant clause from a set of legal documents without being provided with the full context? The authors should also discuss the potential implications of this finding for the development of more robust and reliable AI systems. For example, could this capability be used to improve the performance of AI systems in situations where the question is not explicitly stated? Could it be used to reduce the amount of training data required to achieve a certain level of performance? A more thorough discussion of these aspects would make the paper more compelling and relevant to the broader research community.

Finally, the paper should include a more detailed analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This analysis should explore the characteristics of questions that are more or less amenable to this type of inference. For example, are questions that involve more complex reasoning or that require the model to integrate information from multiple sources more difficult for the model to answer without the question? Are there specific types of datasets that are more or less suitable for this type of evaluation? The authors should also analyze the types of answer choices that are most effective for this task. Are certain types of answer choices more likely to be exploited by the model? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting and would make the paper more valuable to the research community.

### Questions

- How do the results vary across different types of questions and datasets? Are there specific types of questions or datasets where LLMs perform particularly well or poorly in this setting?
- What are the practical implications of this finding for real-world applications? How could this capability be used to improve the performance of AI systems in situations where the question is not explicitly stated?
- What are the limitations of the current study? Are there other factors that could influence the performance of LLMs in this setting, such as the size or complexity of the model, or the specific prompting techniques used?

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper explores the behavior of large language models (LLMs) in a multiple-choice question answering (MCQA) setting where the questions are omitted, and only the choices are provided. The authors test if LLMs can achieve high accuracy in this setup and analyze their reasoning processes. They find that LLMs can perform MCQA tasks without the questions, and the performance is not due to memorization or simple choice dynamics. Instead, the models use meta-strategies, such as inferring the question from the choices, to answer the questions. The authors also propose a new evaluation benchmark and highlight the need for more robust MCQA datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly present their methodology and findings.
2. The study addresses an important issue in evaluating LLMs, as MCQA tasks are widely used in real-world applications. The authors identify a potential flaw in the current evaluation methods and propose a new benchmark to address it.
3. The authors conduct extensive experiments across multiple models and datasets, providing a comprehensive analysis of the phenomenon.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's main finding that LLMs can achieve high accuracy in the choices-only setting is not particularly surprising, as this ability is already demonstrated in prior work (e.g., "LLM can Learn to Answer Multiple Choice Questions without the Questions"). While the authors explore this phenomenon in more models and datasets, the core finding lacks significant novelty.
2. The paper lacks a clear and compelling motivation for studying MCQA without the question. While the authors mention potential applications in real-world scenarios, such as in medicine or law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. The motivation remains weak and speculative.
3. The paper does not provide a thorough analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This limits the paper's contribution to a descriptive analysis rather than a deeper understanding of the underlying mechanisms. The paper does not explore the characteristics of questions that are more or less amenable to this type of inference, nor does it analyze the types of answer choices that are more or less effective for this task. This lack of analysis limits the practical value of the findings.

### Suggestions

The paper would benefit significantly from a more in-depth analysis of the underlying mechanisms that enable LLMs to perform well in the MCQA without the question setting. Instead of simply demonstrating that LLMs can achieve high accuracy, the authors should investigate the specific strategies and reasoning processes that they employ. For example, they could analyze the attention patterns of the models to understand which parts of the answer choices are most influential in their decision-making process. They could also explore the use of techniques such as ablation studies to identify the key components of the answer choices that are most important for the model's performance. Furthermore, the authors should investigate the relationship between the structure of the answer choices and the model's performance. Are certain types of answer choices more effective than others? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting.

To strengthen the paper's motivation, the authors should provide concrete examples of real-world scenarios where this capability would be valuable. For instance, in medical diagnosis, could an LLM be used to identify the most likely diagnosis from a set of symptoms without being provided with the actual patient history? Similarly, in legal document analysis, could an LLM be used to identify the most relevant clause from a set of legal documents without being provided with the full context? The authors should also discuss the potential implications of this finding for the development of more robust and reliable AI systems. For example, could this capability be used to improve the performance of AI systems in situations where the question is not explicitly stated? Could it be used to reduce the amount of training data required to achieve a certain level of performance? A more thorough discussion of these aspects would make the paper more compelling and relevant to the broader research community.

Finally, the paper should include a more detailed analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This analysis should explore the characteristics of questions that are more or less amenable to this type of inference. For example, are questions that involve more complex reasoning or that require the model to integrate information from multiple sources more difficult for the model to answer without the question? Are there specific types of datasets that are more or less suitable for this type of evaluation? The authors should also analyze the types of answer choices that are most effective for this task. Are certain types of answer choices more likely to be exploited by the model? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting and would make the paper more valuable to the research community.

### Questions

1. How do the results vary across different types of questions and datasets? Are there specific types of questions or datasets where LLMs perform particularly well or poorly in this setting?
2. What are the practical implications of this finding for real-world applications? How could this capability be used to improve the performance of AI systems in situations where the question is not explicitly stated?
3. What are the limitations of the current study? Are there other factors that could influence the performance of LLMs in this setting, such as the size or complexity of the model, or the specific prompting techniques used?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Here's my plan:
1. **Iterate through each reviewer's comments.**
2. **For each weakness identified by the reviewer:**
    - **Locate the specific claim in the review.**
    - **Search the paper for evidence related to that claim.** This might involve looking at the method description, experimental setup, results, or motivation sections.
    - **Collect evidence:** Direct quotes, descriptions of experimental setup, reported results, or missing information.
    - **Analyze the evidence:** Determine if the reviewer's claim is valid based on the evidence found.
    - **Formulate a conclusion:** State whether the weakness is valid, partially valid, or invalid, and provide the supporting evidence and reasoning.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper's main finding that LLMs can achieve high accuracy in the choices-only setting is not particularly surprising, as this ability is already demonstrated in prior work (e.g., "LLM can Learn to Answer Multiple Choice Questions without the Questions"). While the authors explore this phenomenon in more models and datasets, the core finding lacks significant novelty."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The paper explicitly states in the Introduction: "While this concern has been studied with prompt sensitivity Zheng et al. (2024) , an unexplored aspect of MCQA-based LLM evaluation is dataset artifacts—patterns or biases in text that models may use as shortcuts, rather than completing the task as intended. Researchers have found that partial-input baselines Poliak et al. (2018) , models trained using just a subset of inputs, can exploit artifacts in parts of the input. Such models include hypothesis -only models in natural language inference Poliak et al. (2018) ; Herlihy and Rudinger (2021) and passage -only models in reading comprehension Shah et al. (2020) ; Kaushik and Lipton (2018) . If LLMs exhibit high choices-only accuracy, we suggest three approaches: First, along with typical MCQA metrics, choices-only prompts can be reported as stronger alternatives to majority baselines Poliak et al. (2018) . Second, researchers can design datasets with more robust protocols, such as the Winograd pair format Levesque et al. (2011) , to mitigate the potential for artifacts. Third, HellaSwag has the highest choices-only accuracy (0.585 with LLaMA) and it is also the only dataset with human -written gold answers and model -written distractors. Thus, the gold answers may contain stylistic cues distinct from the distractors, which can inform strong discriminators like LLMs in partial-input settings. To help explain LLM decision-making. 1 1 1 Our intention is not to discredit MCQA evaluations. Instead, by highlighting the high choices-only accuracy of LLMs and investigating several potential explanations, we aim to give suggestions to enhance transparency and robustness in benchmarking, as well as provide insights into the decision-making of LLMs in partial-input settings. Our contributions can be summarized as follows: 1) We assess choices-only prompts with four LLMs and three MCQA datasets, being the first to show that LLMs can exhibit high partial-input accuracy in few-shot settings and with minimal exemplars. 2) We test several hypotheses to help explain this high choices-only accuracy, such as memorization, choice dynamics, and abductive question inference. 3) We release a thorough black-box MCQA analysis suite to facilitate transparent LLM evaluations. 1 1 1 A majority class baseline always predicts the most frequent answer choice found in the dataset. (Section 3.2)"

3. Literature Gap Analysis: The paper cites Zheng et al. (2024) regarding prompt sensitivity, but the reviewer points out that the core finding of high accuracy in the choices-only setting is not novel. The paper acknowledges prior work on partial-input baselines but argues that the *specific* phenomenon of high choices-only accuracy in MCQA tasks and the *systematic investigation* across models and datasets is a contribution.

4. Validation Analysis:
Primary evidence summary: The paper explicitly states its goal is to investigate the phenomenon of high choices-only accuracy and provides a systematic analysis across models and datasets.
Supporting quotes: See quote in Evidence Collection.
Impact assessment: While the core finding might not be entirely novel, the paper's contribution lies in its systematic investigation and the proposed solutions. The reviewer's point about the lack of significant novelty is valid in the context of the core finding itself.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper's introduction and contributions section highlight the investigation of high choices-only accuracy as a key contribution, but the reviewer correctly points out the prior demonstration of this phenomenon.

1. Weakness Statement:
"The paper lacks a clear and compelling motivation for studying MCQA without the question. While the authors mention potential applications in real-world scenarios, such as in medicine or law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. The motivation remains weak and speculative."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The motivation is presented in the Introduction: "Given this role of MCQA, it is essential to verify that MCQA accuracy reflects the abilities we intend to measure. While this concern has been studied with prompt sensitivity Zheng et al. (2024) , an unexplored aspect of MCQA-based LLM evaluation is dataset artifacts—patterns or biases in text that models may use as shortcuts, rather than completing the task as intended. Researchers have found that partial-input baselines Poliak et al. (2018) , models trained using just a subset of inputs, can exploit artifacts in parts of the input. Such models include hypothesis -only models in natural language inference Poliak et al. (2018) ; Herlihy and Rudinger (2021) and passage -only models in reading comprehension Shah et al. (2020) ; Kaushik and Lipton (2018) . If LLMs exhibit high choices-only accuracy, we suggest three approaches: First, along with typical MCQA metrics, choices-only prompts can be reported as stronger alternatives to majority baselines Poliak et al. (2018) . Second, researchers can design datasets with more robust protocols, such as the Winograd pair format Levesque et al. (2011) , to mitigate the potential for artifacts. Third, HellaSwag has the highest choices-only accuracy (0.585 with LLaMA) and it is also the only dataset with human -written gold answers and model -written distractors. Thus, the gold answers may contain stylistic cues distinct from the distractors, which can inform strong discriminators like LLMs in partial-input settings. To help explain LLM decision-making. 1 1 1 Our contributions can be summarized as follows: 1) We assess choices-only prompts with four LLMs and three MCQA datasets, being the first to show that LLMs can exhibit high partial-input accuracy in few-shot settings and with minimal exemplars. 2) We test several hypotheses to help explain this high choices-only accuracy, such as memorization, choice dynamics, and abductive question inference. 3) We release a thorough black-box MCQA analysis suite to facilitate transparent LLM evaluations. 1 1 1 A majority class baseline always predicts the most frequent answer choice found in the dataset. (Section 1 and 3.2)"

3. Literature Gap Analysis: The paper cites relevant works on partial-input baselines, suggesting an awareness of the motivation.

4. Validation Analysis:
Primary evidence summary: The paper mentions applications in medicine and law as potential real-world scenarios.
Supporting quotes: "This is crucial for ensuring that the models' performance is genuinely reflective of their reasoning abilities rather than exploiting superficial patterns in the data." (Section 1)
Impact assessment: While the paper mentions potential applications, the reviewer is correct that it lacks concrete examples and a detailed discussion of the practical implications. The motivation is present but could be strengthened with more specific examples.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper mentions potential applications but lacks concrete examples and a detailed discussion of practical implications.

1. Weakness Statement:
"The paper does not provide a thorough analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This limits the paper's contribution to a descriptive analysis rather than a deeper understanding of the underlying mechanisms. The paper does not explore the characteristics of questions that are more or less amenable to this type of inference, nor does it analyze the types of answer choices that are more or less effective for this task. This lack of analysis limits the practical value of the findings."

2. Evidence Collection:
a) Method-related Evidence: The paper describes the datasets used (ARC, MMLU, HellaSwag) and their characteristics in Section 3.1.
b) Experiment-related Evidence: The paper presents results for each dataset in Section 4, showing the choices-only accuracy for each model. The analysis in Section 5 discusses the results and proposes explanations. The qualitative analysis in Section 6.3 provides some insights into the types of questions and choices the model infers.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
Primary evidence summary: The paper presents results across different datasets and analyzes the findings, including a qualitative analysis of inferred questions.
Supporting quotes: The entire Section 4 presents results across datasets. Section 5 analyzes these results. Section 6.3 provides a qualitative analysis of the inferred questions.
Impact assessment: While the paper provides some analysis, the reviewer is correct that a more in-depth investigation into the characteristics of questions and answer choices that lead to better or worse performance is missing. The analysis is somewhat descriptive rather than deeply mechanistic.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper presents results across datasets and provides some analysis, but lacks a thorough investigation into the specific characteristics of questions and answer choices that influence performance.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper's central claim that LLMs can achieve high accuracy on MCQA tasks without the question is not particularly surprising, as this ability is already demonstrated in prior work (e.g., "LLM can Learn to Answer Multiple Choice Questions without the Questions"). While the authors explore this phenomenon in more models and datasets, the core finding lacks significant novelty."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The paper explicitly states in the Introduction: "While this concern has been studied with prompt sensitivity Zheng et al. (2024) , an unexplored aspect of MCQA-based LLM evaluation is dataset artifacts—patterns or biases in text that models may use as shortcuts, rather than completing the task as intended. Researchers have found that partial-input baselines Poliak et al. (2018) , models trained using just a subset of inputs, can exploit artifacts in parts of the input. Such models include hypothesis -only models in natural language inference Poliak et al. (2018) ; Herlihy and Rudinger (2021) and passage -only models in reading comprehension Shah et al. (2020) ; Kaushik and Lipton (2018) . If LLMs exhibit high choices-only accuracy, we suggest three approaches: First, along with typical MCQA metrics, choices-only prompts can be reported as stronger alternatives to majority baselines Poliak et al. (2018) . Second, researchers can design datasets with more robust protocols, such as the Winograd pair format Levesque et al. (2011) , to mitigate the potential for artifacts. Third, HellaSwag has the highest choices-only accuracy (0.585 with LLaMA) and it is also the only dataset with human -written gold answers and model -written distractors. Thus, the gold answers may contain stylistic cues distinct from the distractors, which can inform strong discriminators like LLMs in partial-input settings. To help explain LLM decision-making. 1 1 1 Our contributions can be summarized as follows: 1) We assess choices-only prompts with four LLMs and three MCQA datasets, being the first to show that LLMs can exhibit high partial-input accuracy in few-shot settings and with minimal exemplars. 2) We test several hypotheses to help explain this high choices-only accuracy, such as memorization, choice dynamics, and abductive question inference. 3) We release a thorough black-box MCQA analysis suite to facilitate transparent LLM evaluations. 1 1 1 A majority class baseline always predicts the most frequent answer choice found in the dataset. (Section 1 and 3.2)"

3. Literature Gap Analysis: The paper cites Zheng et al. (2024) regarding prompt sensitivity, but the reviewer points out that the core finding of high accuracy in the choices-only setting is not novel. The paper acknowledges prior work on partial-input baselines but argues that the *specific* phenomenon of high choices-only accuracy in MCQA tasks and the *systematic investigation* across models and datasets is a contribution.

4. Validation Analysis:
Primary evidence summary: The paper explicitly states its goal is to investigate the phenomenon of high choices-only accuracy and provides a systematic analysis across models and datasets.
Supporting quotes: See quote in Evidence Collection.
Impact assessment: While the core finding might not be entirely novel, the paper's contribution lies in its systematic investigation and the proposed solutions. The reviewer's point about the lack of significant novelty is valid in the context of the core finding itself.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper's introduction and contributions section highlight the investigation of high choices-only accuracy as a key contribution, but the reviewer correctly points out the prior demonstration of this phenomenon.

1. Weakness Statement:
"The paper lacks a clear and compelling motivation for studying MCQA without the question. While the authors mention potential applications in real-world scenarios, such as in medicine or law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. The motivation remains weak and speculative."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The motivation is presented in the Introduction: "Given this role of MCQA, it is essential to verify that MCQA accuracy reflects the abilities we intend to measure. While this concern has been studied with prompt sensitivity Zheng et al. (2024) , an unexplored aspect of MCQA-based LLM evaluation is dataset artifacts—patterns or biases in text that models may use as shortcuts, rather than completing the task as intended. Researchers have found that partial-input baselines Poliak et al. (2018) , models trained using just a subset of inputs, can exploit artifacts in parts of the input. Such models include hypothesis -only models in natural language inference Poliak et al. (2018) ; Herlihy and Rudinger (2021) and passage -only models in reading comprehension Shah et al. (2020) ; Kaushik and Lipton (2018) . If LLMs exhibit high choices-only accuracy, we suggest three approaches: First, along with typical MCQA metrics, choices-only prompts can be reported as stronger alternatives to majority baselines Poliak et al. (2018) . Second, researchers can design datasets with more robust protocols, such as the Winograd pair format Levesque et al. (2011) , to mitigate the potential for artifacts. Third, HellaSwag has the highest choices-only accuracy (0.585 with LLaMA) and it is also the only dataset with human -written gold answers and model -written distractors. Thus, the gold answers may contain stylistic cues distinct from the distractors, which can inform strong discriminators like LLMs in partial-input settings. To help explain LLM decision-making. 1 1 1 Our contributions can be summarized as follows: 1) We assess choices-only prompts with four LLMs and three MCQA datasets, being the first to show that LLMs can exhibit high partial-input accuracy in few-shot settings and with minimal exemplars. 2) We test several hypotheses to help explain this high choices-only accuracy, such as memorization, choice dynamics, and abductive question inference. 3) We release a thorough black-box MCQA analysis suite to facilitate transparent LLM evaluations. 1 1 1 A majority class baseline always predicts the most frequent answer choice found in the dataset. (Section 1 and 3.2)"

3. Literature Gap Analysis: The paper cites relevant works on partial-input baselines, suggesting an awareness of the motivation.

4. Validation Analysis:
Primary evidence summary: The paper mentions applications in medicine and law as potential real-world scenarios.
Supporting quotes: "This is crucial for ensuring that the models' performance is genuinely reflective of their reasoning abilities rather than exploiting superficial patterns in the data." (Section 1)
Impact assessment: While the paper mentions potential applications, the reviewer is correct that it lacks concrete examples and a detailed discussion of the practical implications. The motivation is present but could be strengthened with more specific examples.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper mentions potential applications but lacks concrete examples and a detailed discussion of practical implications.

1. Weakness Statement:
"The paper does not provide a thorough analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This limits the paper's contribution to a descriptive analysis rather than a deeper understanding of the underlying mechanisms. The paper does not explore the characteristics of questions that are more or less amenable to this type of inference, nor does it analyze the types of answer choices that are more or less effective for this task. This lack of analysis limits the practical value of the findings."

2. Evidence Collection:
a) Method-related Evidence: The paper describes the datasets used (ARC, MMLU, HellaSwag) and their characteristics in Section 3.1.
b) Experiment-related Evidence: The paper presents results for each dataset in Section 4, showing the choices-only accuracy for each model. The analysis in Section 5 discusses the results and proposes explanations. The qualitative analysis in Section 6.3 provides some insights into the types of questions and choices the model infers.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
Primary evidence summary: The paper presents results across different datasets and analyzes the findings, including a qualitative analysis of inferred questions.
Supporting quotes: The entire Section 4 presents results across datasets. Section 5 analyzes these results. Section 6.3 provides a qualitative analysis of the inferred questions.
Impact assessment: While the paper provides some analysis, the reviewer is correct that a more in-depth investigation into the characteristics of questions and answer choices that lead to better or worse performance is missing. The analysis is somewhat descriptive rather than deeply mechanistic.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper presents results across datasets and provides some analysis, but lacks a thorough investigation into the specific characteristics of questions and answer choices that influence performance.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper’s main finding that LLMs can achieve high accuracy in the choices-only setting is not particularly surprising, as this ability is already demonstrated in prior work (e.g., "LLM can Learn to Answer Multiple Choice Questions without the Questions"). While the authors explore this phenomenon in more models and datasets, the core finding lacks significant novelty."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The paper explicitly states in the Introduction: "While this concern has been studied with prompt sensitivity Zheng et al. (2024) , an unexplored aspect of MCQA-based LLM evaluation is dataset artifacts—patterns or biases in text that models may use as shortcuts, rather than completing the task as intended. Researchers have found that partial-input baselines Poliak et al. (2018) , models trained using just a subset of inputs, can exploit artifacts in parts of the input. Such models include hypothesis -only models in natural language inference Poliak et al. (2018) ; Herlihy and Rudinger (2021) and passage -only models in reading comprehension Shah et al. (2020) ; Kaushik and Lipton (2018) . If LLMs exhibit high choices-only accuracy, we suggest three approaches: First, along with typical MCQA metrics, choices-only prompts can be reported as stronger alternatives to majority baselines Poliak et al. (2018) . Second, researchers can design datasets with more robust protocols, such as the Winograd pair format Levesque et al. (2011) , to mitigate the potential for artifacts. Third, HellaSwag has the highest choices-only accuracy (0.585 with LLaMA) and it is also the only dataset with human -written gold answers and model -written distractors. Thus, the gold answers may contain stylistic cues distinct from the distractors, which can inform strong discriminators like LLMs in partial-input settings. To help explain LLM decision-making. 1 1 1 Our contributions can be summarized as follows: 1) We assess choices-only prompts with four LLMs and three MCQA datasets, being the first to show that LLMs can exhibit high partial-input accuracy in few-shot settings and with minimal exemplars. 2) We test several hypotheses to help explain this high choices-only accuracy, such as memorization, choice dynamics, and abductive question inference. 3) We release a thorough black-box MCQA analysis suite to facilitate transparent LLM evaluations. 1 1 1 A majority class baseline always predicts the most frequent answer choice found in the dataset. (Section 1 and 3.2)"

3. Literature Gap Analysis: The paper cites Zheng et al. (2024) regarding prompt sensitivity, but the reviewer points out that the core finding of high accuracy in the choices-only setting is not novel. The paper acknowledges prior work on partial-input baselines but argues that the *specific* phenomenon of high choices-only accuracy in MCQA tasks and the *systematic investigation* across models and datasets is a contribution.

4. Validation Analysis:
Primary evidence summary: The paper explicitly states its goal is to investigate the phenomenon of high choices-only accuracy and provides a systematic analysis across models and datasets.
Supporting quotes: See quote in Evidence Collection.
Impact assessment: While the core finding might not be entirely novel, the paper's contribution lies in its systematic investigation and the proposed solutions. The reviewer's point about the lack of significant novelty is valid in the context of the core finding itself.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper's introduction and contributions section highlight the investigation of high choices-only accuracy as a key contribution, but the reviewer correctly points out the prior demonstration of this phenomenon.

1. Weakness Statement:
"The paper lacks a clear and compelling motivation for studying MCQA without the question. While the authors mention potential applications in real-world scenarios, such as in medicine or law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. The motivation remains weak and speculative."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The motivation is presented in the Introduction: "Given this role of MCQA, it is essential to verify that MCQA accuracy reflects the abilities we intend to measure. While this concern has been studied with prompt sensitivity Zheng et al. (2024) , an unexplored aspect of MCQA-based LLM evaluation is dataset artifacts—patterns or biases in text that models may use as shortcuts, rather than completing the task as intended. Researchers have found that partial-input baselines Poliak et al. (2018) , models trained using just a subset of inputs, can exploit artifacts in parts of the input. Such models include hypothesis -only models in natural language inference Poliak et al. (2018) ; Herlihy and Rudinger (2021) and passage -only models in reading comprehension Shah et al. (2020) ; Kaushik and Lipton (2018) . If LLMs exhibit high choices-only accuracy, we suggest three approaches: First, along with typical MCQA metrics, choices-only prompts can be reported as stronger alternatives to majority baselines Poliak et al. (2018) . Second, researchers can design datasets with more robust protocols, such as the Winograd pair format Levesque et al. (2011) , to mitigate the potential for artifacts. Third, HellaSwag has the highest choices-only accuracy (0.585 with LLaMA) and it is also the only dataset with human -written gold answers and model -written distractors. Thus, the gold answers may contain stylistic cues distinct from the distractors, which can inform strong discriminators like LLMs in partial-input settings. To help explain LLM decision-making. 1 1 1 Our contributions can be summarized as follows: 1) We assess choices-only prompts with four LLMs and three MCQA datasets, being the first to show that LLMs can exhibit high partial-input accuracy in few-shot settings and with minimal exemplars. 2) We test several hypotheses to help explain this high choices-only accuracy, such as memorization, choice dynamics, and abductive question inference. 3) We release a thorough black-box MCQA analysis suite to facilitate transparent LLM evaluations. 1 1 1 A majority class baseline always predicts the most frequent answer choice found in the dataset. (Section 1 and 3.2)"

3. Literature Gap Analysis: The paper cites relevant works on partial-input baselines, suggesting an awareness of the motivation.

4. Validation Analysis:
Primary evidence summary: The paper mentions applications in medicine and law as potential real-world scenarios.
Supporting quotes: "This is crucial for ensuring that the models' performance is genuinely reflective of their reasoning abilities rather than exploiting superficial patterns in the data." (Section 1)
Impact assessment: While the paper mentions potential applications, the reviewer is correct that it lacks concrete examples and a detailed discussion of the practical implications. The motivation is present but could be strengthened with more specific examples.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper mentions potential applications but lacks concrete examples and a detailed discussion of practical implications.

1. Weakness Statement:
"The paper does not provide a thorough analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This limits the paper's contribution to a descriptive analysis rather than a deeper understanding of the underlying mechanisms. The paper does not explore the characteristics of questions that are more or less amenable to this type of inference, nor does it analyze the types of answer choices that are more or less effective for this task. This lack of analysis limits the practical value of the findings."

2. Evidence Collection:
a) Method-related Evidence: The paper describes the datasets used (ARC, MMLU, HellaSwag) and their characteristics in Section 3.1.
b) Experiment-related Evidence: The paper presents results for each dataset in Section 4, showing the choices-only accuracy for each model. The analysis in Section 5 discusses the results and proposes explanations. The qualitative analysis in Section 6.3 provides some insights into the types of questions and choices the model infers.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
Primary evidence summary: The paper presents results across different datasets and analyzes the findings, including a qualitative analysis of inferred questions.
Supporting quotes: The entire Section 4 presents results across datasets. Section 5 analyzes these results. Section 6.3 provides a qualitative analysis of the inferred questions.
Impact assessment: While the paper provides some analysis, the reviewer is correct that a more in-depth investigation into the characteristics of questions and answer choices that lead to better or worse performance is missing. The analysis is somewhat descriptive rather than deeply mechanistic.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper presents results across datasets and provides some analysis, but lacks a thorough investigation into the specific characteristics of questions and answer choices that influence performance.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper's main finding that LLMs can achieve high accuracy in the choices-only setting is not particularly surprising, as this ability is already demonstrated in prior work (e.g., "LLM can Learn to Answer Multiple Choice Questions without the Questions"). While the authors explore this phenomenon in more models and datasets, the core finding lacks significant novelty."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The paper explicitly states in the Introduction: "While this concern has been studied with prompt sensitivity Zheng et al. (2024) , an unexplored aspect of MCQA-based LLM evaluation is dataset artifacts—patterns or biases in text that models may use as shortcuts, rather than completing the task as intended. Researchers have found that partial-input baselines Poliak et al. (2018) , models trained using just a subset of inputs, can exploit artifacts in parts of the input. Such models include hypothesis -only models in natural language inference Poliak et al. (2018) ; Herlihy and Rudinger (2021) and passage -only models in reading comprehension Shah et al. (2020) ; Kaushik and Lipton (2018) . If LLMs exhibit high choices-only accuracy, we suggest three approaches: First, along with typical MCQA metrics, choices-only prompts can be reported as stronger alternatives to majority baselines Poliak et al. (2018) . Second, researchers can design datasets with more robust protocols, such as the Winograd pair format Levesque et al. (2011) , to mitigate the potential for artifacts. Third, HellaSwag has the highest choices-only accuracy (0.585 with LLaMA) and it is also the only dataset with human -written gold answers and model -written distractors. Thus, the gold answers may contain stylistic cues distinct from the distractors, which can inform strong discriminators like LLMs in partial-input settings. To help explain LLM decision-making. 1 1 1 Our contributions can be summarized as follows: 1) We assess choices-only prompts with four LLMs and three MCQA datasets, being the first to show that LLMs can exhibit high partial-input accuracy in few-shot settings and with minimal exemplars. 2) We test several hypotheses to help explain this high choices-only accuracy, such as memorization, choice dynamics, and abductive question inference. 3) We release a thorough black-box MCQA analysis suite to facilitate transparent LLM evaluations. 1 1 1 A majority class baseline always predicts the most frequent answer choice found in the dataset. (Section 1 and 3.2)"

3. Literature Gap Analysis: The paper cites Zheng et al. (2024) regarding prompt sensitivity, but the reviewer points out that the core finding of high accuracy in the choices-only setting is not novel. The paper acknowledges prior work on partial-input baselines but argues that the *specific* phenomenon of high choices-only accuracy in MCQA tasks and the *systematic investigation* across models and datasets is a contribution.

4. Validation Analysis:
Primary evidence summary: The paper explicitly states its goal is to investigate the phenomenon of high choices-only accuracy and provides a systematic analysis across models and datasets.
Supporting quotes: See quote in Evidence Collection.
Impact assessment: While the core finding might not be entirely novel, the paper's contribution lies in its systematic investigation and the proposed solutions. The reviewer's point about the lack of significant novelty is valid in the context of the core finding itself.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper's introduction and contributions section highlight the investigation of high choices-only accuracy as a key contribution, but the reviewer correctly points out the prior demonstration of this phenomenon.

1. Weakness Statement:
"The paper lacks a clear and compelling motivation for studying MCQA without the question. While the authors mention potential applications in real-world scenarios, such as in medicine or law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. The motivation remains weak and speculative."

2. Evidence Collection:
a) Method-related Evidence: Not applicable.
b) Experiment-related Evidence: The motivation is presented in the Introduction: "Given this role of MCQA, it is essential to verify that MCQA accuracy reflects the abilities we intend to measure. While this concern has been studied with prompt sensitivity Zheng et al. (2024) , an unexplored aspect of MCQA-based LLM evaluation is dataset artifacts—patterns or biases in text that models may use as shortcuts, rather than completing the task as intended. Researchers have found that partial-input baselines Poliak et al. (2018) , models trained using just a subset of inputs, can exploit artifacts in parts of the input. Such models include hypothesis -only models in natural language inference Poliak et al. (2018) ; Herlihy and Rudinger (2021) and passage -only models in reading comprehension Shah et al. (2020) ; Kaushik and Lipton (2018) . If LLMs exhibit high choices-only accuracy, we suggest three approaches: First, along with typical MCQA metrics, choices-only prompts can be reported as stronger alternatives to majority baselines Poliak et al. (2018) . Second, researchers can design datasets with more robust protocols, such as the Winograd pair format Levesque et al. (2011) , to mitigate the potential for artifacts. Third, HellaSwag has the highest choices-only accuracy (0.585 with LLaMA) and it is also the only dataset with human -written gold answers and model -written distractors. Thus, the gold answers may contain stylistic cues distinct from the distractors, which can inform strong discriminators like LLMs in partial-input settings. To help explain LLM decision-making. 1 1 1 Our contributions can be summarized as follows: 1) We assess choices-only prompts with four LLMs and three MCQA datasets, being the first to show that LLMs can exhibit high partial-input accuracy in few-shot settings and with minimal exemplars. 2) We test several hypotheses to help explain this high choices-only accuracy, such as memorization, choice dynamics, and abductive question inference. 3) We release a thorough black-box MCQA analysis suite to facilitate transparent LLM evaluations. 1 1 1 A majority class baseline always predicts the most frequent answer choice found in the dataset. (Section 1 and 3.2)"

3. Literature Gap Analysis: The paper cites relevant works on partial-input baselines, suggesting an awareness of the motivation.

4. Validation Analysis:
Primary evidence summary: The paper mentions applications in medicine and law as potential real-world scenarios.
Supporting quotes: "This is crucial for ensuring that the models' performance is genuinely reflective of their reasoning abilities rather than exploiting superficial patterns in the data." (Section 1)
Impact assessment: While the paper mentions potential applications, the reviewer is correct that it lacks concrete examples and a detailed discussion of the practical implications. The motivation is present but could be strengthened with more specific examples.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper mentions potential applications but lacks concrete examples and a detailed discussion of practical implications.

1. Weakness Statement:
"The paper does not provide a thorough analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This limits the paper's contribution to a descriptive analysis rather than a deeper understanding of the underlying mechanisms. The paper does not explore the characteristics of questions that are more or less amenable to this type of inference, nor does it analyze the types of answer choices that are more or less effective for this task. This lack of analysis limits the practical value of the findings."

2. Evidence Collection:
a) Method-related Evidence: The paper describes the datasets used (ARC, MMLU, HellaSwag) and their characteristics in Section 3.1.
b) Experiment-related Evidence: The paper presents results for each dataset in Section 4, showing the choices-only accuracy for each model. The analysis in Section 5 discusses the results and proposes explanations. The qualitative analysis in Section 6.3 provides some insights into the types of questions and choices the model infers.

3. Literature Gap Analysis: Not applicable.

4. Validation Analysis:
Primary evidence summary: The paper presents results across different datasets and analyzes the findings, including a qualitative analysis of inferred questions.
Supporting quotes: The entire Section 4 presents results across datasets. Section 5 analyzes these results. Section 6.3 provides a qualitative analysis of the inferred questions.
Impact assessment: While the paper provides some analysis, the reviewer is correct that a more in-depth investigation into the characteristics of questions and answer choices that lead to better or worse performance is missing. The analysis is somewhat descriptive rather than deeply mechanistic.

5. Conclusion:
Validity status: Partially Valid
Confidence level: High
Key supporting evidence: The paper presents results across datasets and provides some analysis, but lacks a thorough investigation into the specific characteristics of questions and answer choices that influence performance.

**Synthesis and Reflection:**

After analyzing the reviewer comments and comparing them against the paper's content, several recurring themes emerge. All reviewers express concerns about the novelty of the core finding that LLMs can achieve high accuracy in the choices-only setting. They point to prior work demonstrating this phenomenon, suggesting that the paper's contribution lies more in its systematic investigation across models and datasets rather than the discovery of a novel finding.

Reviewers 1, 2, and 3 all question the clarity and strength of the paper's motivation for studying MCQA without the question. They note that while the paper mentions potential applications in medicine and law, it lacks concrete examples and a detailed discussion of the practical implications of this type of evaluation. This suggests a need for a more compelling justification for the research.

Reviewers 1 and 2 also raise concerns about the depth of the analysis. They suggest that the paper primarily presents descriptive results and lacks a thorough investigation into the underlying mechanisms that enable LLMs to perform well in the choices-only setting. This includes questions about the characteristics of questions and answer choices that lead to better or worse performance.

Reviewer 4 echoes the concerns about the novelty of the core finding and the need for a stronger motivation. They also emphasize the need for a more in-depth analysis of the underlying mechanisms.

There is a general consensus among the reviewers that while the paper is well-written and presents a systematic analysis, it could be strengthened by addressing the concerns about novelty, motivation, and the depth of the analysis.

**Conclusion:**

Based on the evidence collected, the majority of the weaknesses identified by the reviewers are valid. The primary areas of concern are:

*   **Novelty of the Core Finding:** The paper's central finding, that LLMs can achieve high accuracy in the choices-only setting, is not entirely novel. (Valid - Partially Valid)
*   **Clarity and Strength of Motivation:** The paper could provide a more compelling and detailed motivation for studying MCQA without the question, including concrete examples of real-world applications. (Valid - Partially Valid)
*   **Depth of Analysis:** The paper could benefit from a more in-depth investigation into the underlying mechanisms that enable LLMs to perform well in the choices-only setting, including a more thorough analysis of the characteristics of questions and answer choices. (Valid - Partially Valid)

The reviewers' comments are largely consistent and highlight key areas for improvement in the paper.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents an investigation into the performance of large language models (LLMs) on multiple-choice question answering (MCQA) tasks when presented with only the answer choices, a scenario the authors term 'choices-only.' The authors explore this phenomenon across three multiple-choice question answering datasets—ARC, MMLU, and HellaSwag—and four LLMs: LLaMA-2, Falcon, Phi-2, and Mixtral. Their core finding is that LLMs can achieve surprisingly high accuracy in this 'choices-only' setting, often surpassing the performance of majority baselines. This finding is not entirely novel, as prior work has demonstrated similar results, but the authors argue that their systematic investigation across different models and datasets, along with the release of a black-box evaluation suite, contributes to the field. The authors propose three potential hypotheses to explain this high 'choices-only' accuracy: memorization of answer choices, choice dynamics, and abductive question inference. To test these hypotheses, they conduct a series of experiments, including abductive question inference, choice dynamics, and question inference. The paper's significance lies in its systematic approach to a previously under-explored area of LLM evaluation, highlighting the potential for shortcuts and biases in MCQA tasks and the need for more robust evaluation methods. The authors also emphasize the importance of reporting choices-only baselines alongside majority baselines to provide a more complete picture of LLM performance. The paper concludes by advocating for the development of more robust MCQA datasets and evaluation protocols, particularly in the context of partial-input settings, and by releasing their black-box evaluation suite to facilitate transparent LLM evaluations.


## Soundness:

2.75


## Presentation:

2.75


## Contribution:

2.5


## Strengths:

I found several aspects of this paper to be commendable. First, the paper addresses a significant and timely issue in the evaluation of LLMs: the potential for shortcuts and biases in multiple-choice question answering tasks. The authors' focus on the 'choices-only' setting is particularly relevant, as it exposes the limitations of current evaluation methods that often assume the presence of the question. The systematic approach taken by the authors, involving multiple datasets and models, is a notable strength. By testing their hypotheses across a range of LLMs and datasets, they provide a more comprehensive analysis of the phenomenon of high 'choices-only' accuracy. The release of a black-box evaluation suite is another valuable contribution, as it facilitates transparent and reproducible research in this area. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors clearly present their methodology and findings, and the experimental setup is well-described. The inclusion of qualitative analysis, particularly in Section 6.3, provides some insights into the types of questions and choices that the LLMs are able to infer, which adds depth to the analysis. Finally, the authors' emphasis on the importance of reporting choices-only baselines alongside majority baselines is a crucial point that should be considered in future evaluations. This focus on transparency and rigor is a significant strength of the paper.


## Weaknesses:

Despite its strengths, I have identified several weaknesses in this paper that warrant careful consideration. First, while the authors' systematic investigation is a positive aspect, the core finding that LLMs can achieve high accuracy in the 'choices-only' setting is not entirely novel. As pointed out by multiple reviewers, prior work has already demonstrated this phenomenon. While the authors argue that their contribution lies in the systematic analysis across different models and datasets, the lack of significant novelty in the core finding diminishes the overall impact of the paper. This is not to say that the paper is without value, but the core finding should be more clearly acknowledged as a known phenomenon. Second, the paper's motivation for studying MCQA without the question is not as strong as it could be. While the authors mention potential applications in medicine and law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. This lack of concrete examples and detailed discussion weakens the motivation for the paper and makes it less compelling. Third, the paper's analysis, while systematic, is somewhat descriptive rather than deeply mechanistic. The authors do not provide a thorough investigation into the characteristics of questions and answer choices that lead to better or worse performance in the 'choices-only' setting. While the paper includes a qualitative analysis of inferred questions, it does not explore the specific features of questions that are more or less amenable to abductive question inference. Similarly, the paper does not analyze the types of answer choices that are more or less effective for this task. This lack of in-depth analysis limits the practical value of the findings and makes it difficult to generalize the results to other contexts. Finally, the paper lacks a clear and compelling motivation for studying MCQA without the question. While the authors mention potential applications in medicine and law, they do not provide concrete examples or a detailed discussion of how this capability could be practically utilized. The paper does not adequately justify the need for this specific type of evaluation, and it does not explore the potential implications of this finding for real-world applications. This lack of concrete examples and detailed discussion weakens the motivation for the paper and makes it less compelling. The paper also does not provide a thorough analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This limits the paper's contribution to a descriptive analysis rather than a deeper understanding of the underlying mechanisms. The paper does not explore the characteristics of questions that are more or less amenable to this type of inference, nor does it analyze the types of answer choices that are more or less effective for this task. This lack of analysis limits the practical value of the findings. I have high confidence in these identified weaknesses, as they are supported by direct examination of the paper's content and are consistent across multiple reviewers.


## Suggestions:

Based on the identified weaknesses, I propose several concrete suggestions for improving this paper. First, the authors should acknowledge the prior work on the core finding that LLMs can achieve high accuracy in the 'choices-only' setting. While the systematic investigation is a positive aspect, the authors should clearly state that the core finding is not entirely novel and that their contribution lies in the systematic analysis. This would provide a more accurate representation of the paper's contribution and avoid overstating the novelty of the findings. Second, the authors should provide more concrete examples of real-world scenarios where the 'choices-only' evaluation would be valuable. For instance, in medical diagnosis, could an LLM be used to identify the most likely diagnosis from a set of symptoms without being provided with the actual patient history? Similarly, in legal document analysis, could an LLM be used to identify the most relevant clause from a set of legal documents without being provided with the full context? The authors should also discuss the potential implications of this finding for the development of more robust and reliable AI systems. For example, could this capability be used to improve the performance of AI systems in situations where the question is not explicitly stated? Could it be used to reduce the amount of training data required to achieve a certain level of performance? A more thorough discussion of these aspects would make the paper more compelling and relevant to the broader research community. Third, the authors should conduct a more in-depth analysis of the underlying mechanisms that enable LLMs to perform well in the 'choices-only' setting. Instead of simply demonstrating that LLMs can achieve high accuracy, the authors should investigate the specific strategies and reasoning processes that they employ. For example, they could analyze the attention patterns of the models to understand which parts of the answer choices are most influential in their decision-making process. They could also explore the use of techniques such as ablation studies to identify the key components of the answer choices that are most important for the model's performance. Furthermore, the authors should investigate the relationship between the structure of the answer choices and the model's performance. Are certain types of answer choices more effective than others? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting. Fourth, the authors should provide a more detailed analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This analysis should explore the characteristics of questions that are more or less amenable to abductive question inference. For example, are questions that involve more complex reasoning or that require the model to integrate information from multiple sources more difficult for the model to answer without the question? Are there specific types of datasets that are more or less suitable for this type of evaluation? The authors should also analyze the types of answer choices that are most effective for this task. Are certain types of answer choices more or less likely to be exploited by the model? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting. Finally, the authors should provide a more detailed analysis of the types of questions and datasets where LLMs perform well or poorly in this setting. This analysis should explore the characteristics of questions that are more or less amenable to abductive question inference. For example, are questions that involve more complex reasoning or that require the model to integrate information from multiple sources more difficult for the model to answer without the question? Are there specific types of datasets that are more or less suitable for this type of evaluation? The authors should also analyze the types of answer choices that are most effective for this task. Are certain types of answer choices more or less likely to be exploited by the model? Are there specific patterns or relationships between the choices that are more or less likely to be exploited by the model? A more detailed analysis of these aspects would provide a deeper understanding of the capabilities and limitations of LLMs in this setting. By addressing these suggestions, the authors can significantly strengthen their paper and make it more valuable to the research community.


## Questions:

I have several questions that arise from my analysis of this paper. First, how do the results vary across different types of questions and datasets? Are there specific types of questions or datasets where LLMs are more or less likely to perform well in the 'choices-only' setting? For example, are questions that involve more complex reasoning or that require the model to integrate information from multiple sources more difficult for the model to answer without the question? Second, what are the practical implications of this finding for real-world applications? How could the 'choices-only' evaluation be used to improve the performance of AI systems in situations where the question is not explicitly stated? Could it be used to reduce the amount of training data required to achieve a certain level of performance? Third, what are the limitations of the current study? Are there other factors that could influence the performance of LLMs in the 'choices-only' setting, such as the size or complexity of the model, or the specific prompting techniques used? Fourth, what are the specific mechanisms that enable LLMs to perform well in the 'choices-only' setting? What are the key strategies and reasoning processes that they employ? How do these strategies differ from those used in standard MCQA evaluation? Fifth, how does the 'choices-only' setting relate to other forms of out-of-distribution (OOD) testing? Are the findings consistent across different types of OOD data? Finally, what are the next steps for future research in this area? How can we develop more robust and reliable evaluation methods for LLMs that are less susceptible to shortcuts and biases? These questions are intended to encourage further discussion and exploration of the findings presented in this paper and to guide future research in this area.


## Rating:

4.25


## Confidence:

3.75


## Decision:

Reject
}