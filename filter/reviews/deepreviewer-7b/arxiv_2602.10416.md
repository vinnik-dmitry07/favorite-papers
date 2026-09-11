I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates the performance of frontier LLMs on integer addition. The authors find that accuracy decreases as the number of digits increases, and that most errors are due to misalignment or close carry errors. The authors also find that tokenization can influence the occurrence of misalignment errors.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The experiments are comprehensive and well-designed.
- The authors provide a detailed analysis of the types of errors made by frontier LLMs on integer addition.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide any insights into how to improve the performance of LLMs on integer addition.
- The paper does not compare the performance of LLMs with other types of models, such as neural networks or symbolic solvers.

### Suggestions

The paper would be significantly strengthened by exploring potential avenues for improving the performance of LLMs on integer addition. While the authors identify the types of errors made by these models, they do not delve into strategies for mitigating these errors. For instance, the authors could investigate the impact of different training techniques, such as fine-tuning on a dataset of integer addition problems, or exploring the use of specialized architectures designed for numerical reasoning. Furthermore, they could examine the effect of different prompting strategies, such as chain-of-thought prompting, on the accuracy of LLMs. Without exploring these aspects, the paper remains primarily an observational study, lacking practical implications for the field.

Additionally, the paper would benefit from a more comprehensive comparison of LLMs with other types of models for integer addition. While the authors focus on the performance of LLMs, they do not contextualize their findings within the broader landscape of numerical reasoning. For example, comparing the performance of LLMs with that of neural networks trained on the same task would provide valuable insights into the strengths and weaknesses of each approach. Furthermore, the authors could explore the use of symbolic solvers, such as those based on computer algebra systems, as a benchmark for the performance of LLMs. This would help to determine whether LLMs are capable of achieving similar levels of accuracy and reliability as more traditional approaches. Such comparisons would not only enhance the paper's contribution but also provide a more complete understanding of the current state of the art in integer addition.

Finally, the paper could benefit from a more detailed analysis of the types of errors made by LLMs, particularly the close carry errors. While the authors categorize these errors, they do not provide a detailed explanation of why these errors occur. For example, the authors could investigate whether these errors are due to limitations in the model's ability to handle carries, or whether they are related to the tokenization process. A deeper understanding of the underlying causes of these errors would be valuable for developing more effective strategies for improving the performance of LLMs on integer addition. This could involve analyzing the internal representations of the model, or conducting experiments with different tokenization schemes. By providing a more detailed analysis of the error patterns, the paper could offer more concrete guidance for future research in this area.

### Questions

- How does the performance of LLMs on integer addition compare to that of other types of models, such as neural networks or symbolic solvers?
- What are the potential reasons for the close carry errors observed in the paper?
- What are the implications of the findings in the paper for the development of more robust and reliable AI systems?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

The paper studies the performance of frontier LLMs on integer addition and analyzes the types of errors made by these models. The authors find that all frontier models suffer significantly degraded accuracy for integer addition as the number of digits increases. The authors also show that most errors are due to either misalignment or close carry errors. The authors also find that tokenization can influence the occurrence of misalignment errors.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The experiments are comprehensive and well-designed. The authors provide a detailed analysis of the types of errors made by frontier LLMs on integer addition.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide any insights into how to improve the performance of LLMs on integer addition.

The paper does not compare the performance of LLMs with other types of models, such as neural networks or symbolic solvers.

### Suggestions

The paper would be significantly strengthened by exploring potential avenues for improving the performance of LLMs on integer addition. While the authors identify the types of errors made by these models, they do not delve into strategies for mitigating these errors. For instance, the authors could investigate the impact of different training techniques, such as fine-tuning on a dataset of integer addition problems, or exploring the use of specialized architectures designed for numerical reasoning. Furthermore, they could examine the effect of different prompting strategies, such as chain-of-thought prompting, on the accuracy of LLMs. Without exploring these aspects, the paper remains primarily an observational study, lacking practical implications for the field.

Additionally, the paper would benefit from a more comprehensive comparison of LLMs with other types of models for integer addition. While the authors focus on the performance of LLMs, they do not contextualize their findings within the broader landscape of numerical reasoning. For example, comparing the performance of LLMs with that of neural networks trained on the same task would provide valuable insights into the strengths and weaknesses of each approach. Furthermore, the authors could explore the use of symbolic solvers, such as those based on computer algebra systems, as a benchmark for the performance of LLMs. This would help to determine whether LLMs are capable of achieving similar levels of accuracy and reliability as more traditional approaches. Such comparisons would not only enhance the paper's contribution but also provide a more complete understanding of the current state of the art in integer addition.

Finally, the paper could benefit from a more detailed analysis of the types of errors made by LLMs, particularly the close carry errors. While the authors categorize these errors, they do not provide a detailed explanation of why these errors occur. For example, the authors could investigate whether these errors are due to limitations in the model's ability to handle carries, or whether they are related to the tokenization process. A deeper understanding of the underlying causes of these errors would be valuable for developing more effective strategies for improving the performance of LLMs on integer addition. This could involve analyzing the internal representations of the model, or conducting experiments with different tokenization schemes. By providing a more detailed analysis of the error patterns, the paper could offer more concrete guidance for future research in this area.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the performance of frontier LLMs on integer addition. The authors find that: 1) all frontier models suffer significantly degraded accuracy as the number of digits increases; 2) most errors are due to either misalignment or close carry errors; 3) tokenization can influence the occurrence of misalignment errors.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. This paper is well-written and easy to follow.
2. The experiments are comprehensive and well-designed.
3. The authors provide a detailed analysis of the types of errors made by frontier LLMs on integer addition.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide any insights into how to improve the performance of LLMs on integer addition.
2. The paper does not compare the performance of LLMs with other types of models, such as neural networks or symbolic solvers.

### Suggestions

The paper would be significantly strengthened by exploring potential avenues for improving the performance of LLMs on integer addition. While the authors identify the types of errors made by these models, they do not delve into strategies for mitigating these errors. For instance, the authors could investigate the impact of different training techniques, such as fine-tuning on a dataset of integer addition problems, or exploring the use of specialized architectures designed for numerical reasoning. Furthermore, they could examine the effect of different prompting strategies, such as chain-of-thought prompting, on the accuracy of LLMs. Without exploring these aspects, the paper remains primarily an observational study, lacking practical implications for the field.

Additionally, the paper would benefit from a more comprehensive comparison of LLMs with other types of models for integer addition. While the authors focus on the performance of LLMs, they do not contextualize their findings within the broader landscape of numerical reasoning. For example, comparing the performance of LLMs with that of neural networks trained on the same task would provide valuable insights into the strengths and weaknesses of each approach. Furthermore, the authors could explore the use of symbolic solvers, such as those based on computer algebra systems, as a benchmark for the performance of LLMs. This would help to determine whether LLMs are capable of achieving similar levels of accuracy and reliability as more traditional approaches. Such comparisons would not only enhance the paper's contribution but also provide a more complete understanding of the current state of the art in integer addition.

Finally, the paper could benefit from a more detailed analysis of the types of errors made by LLMs, particularly the close carry errors. While the authors categorize these errors, they do not provide a detailed explanation of why these errors occur. For example, the authors could investigate whether these errors are due to limitations in the model's ability to handle carries, or whether they are related to the tokenization process. A deeper understanding of the underlying causes of these errors would be valuable for developing more effective strategies for improving the performance of LLMs on integer addition. This could involve analyzing the internal representations of the model, or conducting experiments with different tokenization schemes. By providing a more detailed analysis of the error patterns, the paper could offer more concrete guidance for future research in this area.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper investigates the performance of frontier LLMs on integer addition and analyzes the types of errors made by these models. The authors find that all frontier models suffer significantly degraded accuracy for integer addition as the number of digits increases. The authors also show that most errors are due to either misalignment or close carry errors. The authors also find that tokenization can influence the occurrence of misalignment errors.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The experiments are comprehensive and well-designed.
3. The authors provide a detailed analysis of the types of errors made by frontier LLMs on integer addition.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide any insights into how to improve the performance of LLMs on integer addition.
2. The paper does not compare the performance of LLMs with other types of models, such as neural networks or symbolic solvers.

### Suggestions

The paper would be significantly strengthened by exploring potential avenues for improving the performance of LLMs on integer addition. While the authors identify the types of errors made by these models, they do not delve into strategies for mitigating these errors. For instance, the authors could investigate the impact of different training techniques, such as fine-tuning on a dataset of integer addition problems, or exploring the use of specialized architectures designed for numerical reasoning. Furthermore, they could examine the effect of different prompting strategies, such as chain-of-thought prompting, on the accuracy of LLMs. Without exploring these aspects, the paper remains primarily an observational study, lacking practical implications for the field.

Additionally, the paper would benefit from a more comprehensive comparison of LLMs with other types of models for integer addition. While the authors focus on the performance of LLMs, they do not contextualize their findings within the broader landscape of numerical reasoning. For example, comparing the performance of LLMs with that of neural networks trained on the same task would provide valuable insights into the strengths and weaknesses of each approach. Furthermore, the authors could explore the use of symbolic solvers, such as those based on computer algebra systems, as a benchmark for the performance of LLMs. This would help to determine whether LLMs are capable of achieving similar levels of accuracy and reliability as more traditional approaches. Such comparisons would not only enhance the paper's contribution but also provide a more complete understanding of the current state of the art in integer addition.

Finally, the paper could benefit from a more detailed analysis of the types of errors made by LLMs, particularly the close carry errors. While the authors categorize these errors, they do not provide a detailed explanation of why these errors occur. For example, the authors could investigate whether these errors are due to limitations in the model's ability to handle carries, or whether they are related to the tokenization process. A deeper understanding of the underlying causes of these errors would be valuable for developing more effective strategies for improving the performance of LLMs on integer addition. This could involve analyzing the internal representations of the model, or conducting experiments with different tokenization schemes. By providing a more detailed analysis of the error patterns, the paper could offer more concrete guidance for future research in this area.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer has identified two main weaknesses: the lack of insights into improving LLM performance on integer addition and the absence of comparisons with other model types. I need to go through the paper and see if these criticisms are valid based on the content.

**Weakness 1: No insights into improving LLM performance.**
- I need to check if the paper focuses solely on analysis and if it explicitly states that it doesn't offer solutions for improvement.

**Weakness 2: No comparison with other model types.**
- I need to verify if the paper's experiments are limited to LLMs and if it lacks comparisons with neural networks or symbolic solvers.

**Plan:**
1. Analyze the introduction and conclusion to see if the focus is on analysis.
2. Examine the experiments section to see the types of models used.
3. Check the discussion section for any mention of future directions or improvements.
**Review 1 Weakness Analysis**

1. Weakness Statement:
"The paper does not provide any insights into how to improve the performance of LLMs on integer addition."

2. Evidence Collection:
a) Method-related Evidence (if applicable):
   - The paper focuses on analyzing the performance of existing LLMs. The "Method" section describes the experimental setup and error categorization techniques but does not propose new methods or training strategies.
b) Experiment-related Evidence (if applicable):
   - The "Experiments" section details the setup for evaluating LLMs on integer addition. The "Results" section presents the findings of these evaluations, which are the performance metrics and error types observed. There is no mention of experiments designed to improve performance or alternative training methods.
c) Literature Gap Analysis:
   - The "Related Work" section discusses existing research on LLM performance and error analysis in arithmetic but does not delve into methods for improving performance on specific tasks like integer addition.

3. Literature Gap Analysis:
   - The paper cites works that analyze LLM performance on arithmetic tasks, indicating an awareness of the field. However, it doesn't cite or discuss literature focused on improving LLM performance on specific numerical tasks.

4. Validation Analysis:
   - The paper's primary focus is on identifying and characterizing the errors made by LLMs on integer addition. The "Discussion" section concludes by stating, "Recent work has studied the representational power of neural networks (and transformer architectures in particular) ( Weiss et al., 2021 ; Schnabel et al., 2025 ; Sanford et al., 2024 ) . While the specific modeling choices vary, basic arithmetic generally falls in the class of tasks that can be solved exactly using modern architectures. In fact, addition is one of the examples used to explain how to “think like a transformer” ( Weiss et al., 2021 ). However, our evidence suggests that modern LLMs are not finding reliable implementations for addition, instead resorting to error-prone strategies that give poor results and exhibit design-dependent idiosyncrasies." This explicitly states the paper's focus on the negative result (performance issues) rather than positive results like improvements.
   - The paper concludes with "Future work could focus on developing more robust and reliable AI systems capable of handling basic arithmetic." This acknowledges the limitation of not providing solutions but frames it as an area for future research.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper's focus is on analyzing errors and limitations of current LLMs, with the conclusion acknowledging the lack of proposed solutions for improvement.

1. Weakness Statement:
"The paper does not compare the performance of LLMs with other types of models, such as neural networks or symbolic solvers."

2. Evidence Collection:
a) Experiment-related Evidence (if applicable):
   - The "Experiments" section explicitly states, "We use prompts of the form: What is A + B? Write just the answer." This indicates a focus on evaluating the final output of the LLMs.
   - The "baselines" listed in the "setup" of the "Model Performance on Integer Addition" experiment are "None". There is no mention of comparing LLMs to other model types like neural networks or symbolic solvers.
b) Results Validation:
   - The "results" sections for each experiment only present data on the accuracy of the LLMs. There is no data or comparison provided for neural networks or symbolic solvers.

3. Literature Gap Analysis:
   - While the "Related Work" section discusses the capabilities of LLMs in general, it doesn't include a comparative analysis of different model architectures for arithmetic tasks.

4. Validation Analysis:
   - The paper's methodology is centered around evaluating the performance of LLMs on the given task. The experimental design and metrics are solely focused on the accuracy of the LLMs' responses. There is no mention of implementing or evaluating other model types like neural networks or symbolic solvers on the same task.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The experimental setup and results sections exclusively focus on LLM performance, with no mention or comparison to other model types.

**Synthesis and Reflection**

Both weaknesses identified by Reviewer 1 are valid and well-supported by the content of the paper. The paper's explicit focus on analyzing the shortcomings of LLMs in integer addition and the design of its experiments around evaluating these models alone confirm the reviewer's assessment. There are no indications of the paper exploring methods for improving LLM performance on this task or comparing their performance to other model architectures.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a systematic investigation into the performance of frontier large language models (LLMs) on the task of integer addition, a fundamental arithmetic operation. The authors' primary goal is to understand the limitations of these models when dealing with even basic mathematical reasoning. They conduct a comprehensive empirical study, evaluating several state-of-the-art LLMs on addition problems with varying digit lengths. The core methodological approach involves generating random addition problems and prompting the LLMs to compute the sum. The responses are then automatically corrected to align with the correct answer, and the presence of errors is flagged. Through careful error analysis, the authors identify two primary categories of errors: misalignment errors, where the digits of the operands or the result are incorrectly positioned, and close carry errors, where the addition process itself is flawed due to incorrect handling of carries. The main empirical findings reveal a significant degradation in LLM accuracy as the number of digits in the addends increases. Furthermore, the study demonstrates that a substantial portion of the errors can be attributed to these two error categories. The authors also explore the influence of tokenization on misalignment errors, revealing that LLMs using tokenizers with different granularity exhibit varying error patterns. Specifically, they observe that tokenization can impact the likelihood of misalignment errors, suggesting a potential link between tokenization strategy and the models' ability to perform accurate arithmetic. Overall, this paper provides a valuable contribution by highlighting the limitations of current LLMs in performing even basic arithmetic tasks and by offering a detailed error analysis that can inform future research in this area. The findings suggest that while LLMs possess impressive capabilities in many domains, they still struggle with fundamental numerical reasoning, which is a critical component of many real-world applications. This work underscores the need for further research into methods that can enhance the numerical reasoning abilities of LLMs and develop more robust and reliable AI systems.


## Soundness:

2.5


## Presentation:

3.0


## Contribution:

2.0


## Strengths:

This paper's primary strength lies in its clear and systematic approach to investigating the performance of LLMs on integer addition. The authors have successfully executed a large-scale empirical study, evaluating multiple frontier LLMs on a well-defined task. The methodology is well-described, and the experimental setup is robust, allowing for a thorough analysis of the models' performance. The identification of misalignment and close carry errors as the primary sources of error is a significant contribution, providing valuable insights into the specific types of mistakes LLMs make when performing arithmetic. This categorization of errors allows for a more nuanced understanding of the models' weaknesses and can guide future research in targeted areas. Furthermore, the investigation into the influence of tokenization on misalignment errors is a novel and insightful aspect of the paper. The authors demonstrate that different tokenization strategies can impact the likelihood of misalignment errors, suggesting that this is not merely a random occurrence but rather a systematic effect related to how the models process the input. This finding highlights the importance of considering tokenization as a potential factor influencing the performance of LLMs on numerical tasks. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors present their findings clearly and provide a detailed analysis of the results, which is crucial for the reader to understand the significance of their work. The comprehensive nature of the experiments, including the evaluation of multiple models and the analysis of various error types, adds to the credibility of the findings. The paper's focus on a fundamental task like integer addition makes it highly relevant to the broader field of AI, as it highlights the limitations of LLMs in a domain that is often considered a strength. This work serves as a valuable cautionary tale, reminding us that even the most advanced LLMs are not without their limitations and that further research is needed to improve their numerical reasoning abilities. The detailed error analysis and the investigation of tokenization effects are particularly valuable contributions that can inform future research directions.


## Weaknesses:

While this paper provides valuable insights into the limitations of LLMs on integer addition, it suffers from two primary weaknesses that significantly impact its overall contribution. Firstly, and most notably, the paper does not offer any insights into how to improve the performance of LLMs on this task. As I've verified, the paper's focus is primarily on analyzing the errors made by existing models, as stated in the introduction: "We conduct systematic experiments on a collection of frontier large language models, finding that: • When adding two numbers, all frontier models perform poorly as the number of digits increases (Figure 1 ). We also find that performance is not necessarily monotone in length." and "Future work could focus on developing more robust and reliable AI systems capable of handling basic arithmetic." The paper does not propose or explore any methods for training or fine-tuning LLMs to address the identified error types. This lack of a forward-looking perspective limits the paper's practical impact, as it does not provide a clear path towards enhancing the numerical reasoning abilities of these models. The paper's conclusion, while acknowledging the limitations, does not offer any concrete steps for improvement, which is a significant drawback for a paper that aims to contribute to the field. Secondly, the paper lacks a comparative analysis of LLMs with other types of models for integer addition. As I've confirmed, the paper's methodology is exclusively focused on evaluating LLMs, with no mention of comparing their performance to neural networks or symbolic solvers. The experimental setup, as described in the 'Model Performance on Integer Addition' section, uses the same prompts for all models, and the 'baselines' listed are 'None'. The results sections only present data on the accuracy of the LLMs, without any comparison to other model types. This absence of a comparative analysis is a significant limitation, as it does not provide a clear understanding of how LLMs perform relative to other approaches for numerical reasoning. For instance, the paper does not compare the performance of LLMs with that of neural networks trained on the same task, nor does it explore the use of symbolic solvers as a benchmark. This lack of context makes it difficult to assess the strengths and weaknesses of LLMs in this domain and limits the paper's ability to draw meaningful conclusions about the capabilities of different model architectures. The paper's focus on LLMs alone leaves open the question of whether other types of models might be better suited for this task, and this is a crucial point that the paper fails to address. The lack of a comparative analysis also prevents the paper from contextualizing its findings within the broader landscape of numerical reasoning, which is essential for a comprehensive understanding of the current state of the art. These two weaknesses, the lack of insights into improvement and the absence of comparative analysis, significantly limit the paper's contribution and impact.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. Firstly, the paper should explore potential avenues for improving the performance of LLMs on integer addition. This could involve investigating different training techniques, such as fine-tuning on a dataset of integer addition problems, or exploring the use of specialized architectures designed for numerical reasoning. Furthermore, the paper could examine the effect of different prompting strategies, such as chain-of-thought prompting, on the accuracy of LLMs. Without exploring these aspects, the paper remains primarily an observational study, lacking practical implications for the field. The authors could also investigate the impact of different tokenization schemes on the performance of LLMs, as this might reveal insights into how the models process numerical information. By delving into these areas, the paper could provide more concrete guidance for future research in this area. Secondly, the paper should include a more comprehensive comparison of LLMs with other types of models for integer addition. This would involve comparing the performance of LLMs with that of neural networks trained on the same task, as well as exploring the use of symbolic solvers as a benchmark. This comparison would help to determine whether LLMs are capable of achieving similar levels of accuracy and reliability as more traditional approaches. The authors could also explore the use of hybrid models that combine the strengths of different architectures. By providing a more comprehensive comparison, the paper could offer a more complete understanding of the current state of the art in integer addition and provide a more complete picture of the strengths and weaknesses of each approach. This would also enhance the paper's contribution by placing the findings of LLMs in the context of the broader landscape of numerical reasoning. Finally, the paper could benefit from a more detailed analysis of the types of errors made by LLMs, particularly the close carry errors. While the authors categorize these errors, they do not provide a detailed explanation of why these errors occur. For example, the authors could investigate whether these errors are due to limitations in the model's ability to handle carries, or whether they are related to the tokenization process. A deeper understanding of the underlying causes of these errors would be valuable for developing more effective strategies for improving the performance of LLMs on integer addition. This could involve analyzing the internal representations of the model, or conducting experiments with different tokenization schemes. By providing a more detailed analysis of the error patterns, the paper could offer more concrete guidance for future research in this area. These suggestions, if implemented, would significantly enhance the paper's contribution and impact, making it a more valuable resource for the research community.


## Questions:

Several key questions arise from my analysis of this paper, focusing on the core methodological choices and the interpretation of the results. Firstly, given the observed degradation in LLM performance with increasing digit length, what specific architectural or training characteristics of these models contribute to this decline in accuracy? The paper identifies misalignment and close carry errors, but it does not delve into the underlying mechanisms that cause these errors. Understanding the specific vulnerabilities of LLMs in this context is crucial for developing targeted solutions. For instance, are the models struggling with the positional encoding of digits, or are they having difficulty with the carry operations themselves? A deeper analysis of these mechanisms would be valuable. Secondly, why do certain tokenization strategies lead to a higher likelihood of misalignment errors, as observed in the paper? The authors note that tokenization can influence the occurrence of misalignment errors, but they do not provide a detailed explanation of the underlying reasons. Is it simply a matter of token size, or are there other factors at play? A more detailed analysis of the relationship between tokenization and error types would be beneficial. For example, do models using multi-digit tokens consistently make misalignment errors, or are there other patterns? What are the implications of these findings for the design of more robust tokenization strategies? Thirdly, how do the observed error patterns in LLMs compare to those observed in other types of models, such as neural networks or symbolic solvers? The paper focuses solely on LLMs, but it would be valuable to understand how these models compare to others in terms of their error profiles. Are the types of errors observed in LLMs similar to those observed in other models, or are they unique to these architectures? A comparative analysis of error patterns would provide a more complete understanding of the current state of the art in integer addition. Finally, what are the practical implications of the findings for the development of more robust and reliable AI systems? The paper highlights the limitations of current LLMs in performing even basic arithmetic tasks, but it does not offer concrete guidance on how to address these limitations. What are the most promising research directions for improving the numerical reasoning abilities of LLMs? Are there specific techniques or architectures that are most likely to lead to significant improvements in performance? A more detailed discussion of the practical implications of the findings would be valuable for guiding future research in this area. These questions, if addressed, would significantly enhance the paper's contribution and provide a more complete understanding of the challenges and opportunities in the field of numerical reasoning with LLMs.


## Rating:

5.0


## Confidence:

3.0


## Decision:

Reject
}