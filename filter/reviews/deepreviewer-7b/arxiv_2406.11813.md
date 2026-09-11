I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates how LLMs acquire factual knowledge during pretraining. The authors introduce a Fictional Knowledge dataset to study the dynamics of factual knowledge acquisition by injecting synthetic knowledge into the LLMs during pretraining. They analyze the impact of various factors, such as knowledge injection scenarios (duplication, paraphrase, once), pretraining stages, model sizes, and training batch sizes, on the acquisition and retention of factual knowledge. The authors find that factual knowledge acquisition occurs by accumulating small increases in the log probability of the injected knowledge at each training step. They also find that effectivity, the improvement in log probability after being trained with the injected knowledge, does not improve with model scale or pretraining stage. However, the effectivity does improve with model size and pretraining stage when the model is trained with a larger batch size. The authors also find that the acquisition of compositional generalization accumulates most slowly but is more robust to forgetting. Finally, the authors discuss how their findings explain recently observed behaviors of LLMs, such as the improved performance of LLMs through data scaling and the benefits of deduplicating the pretraining corpus.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The authors introduce a Fictional Knowledge dataset to study the dynamics of factual knowledge acquisition during pretraining. This dataset allows for a fine-grained analysis of how LLMs acquire and retain factual knowledge. The dataset is also designed to study the impact of various factors, such as knowledge injection scenarios (duplication, paraphrase, once), pretraining stages, model sizes, and training batch sizes, on the acquisition and retention of factual knowledge.
2. The authors provide a comprehensive analysis of the dynamics of factual knowledge acquisition during pretraining. They investigate various factors, such as knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes, and their impact on the acquisition and retention of factual knowledge. They also provide a detailed analysis of the effectivity of the injected knowledge and the forgetting of acquired knowledge.
3. The authors discuss how their findings explain recently observed behaviors of LLMs, such as the improved performance of LLMs through data scaling and the benefits of deduplicating the pretraining corpus. This provides a valuable contribution to the understanding of how LLMs learn and retain factual knowledge.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's analysis is primarily based on a single dataset, the Fictional Knowledge dataset, which may limit the generalizability of the findings. The dataset's synthetic nature and controlled structure might not fully capture the complexities of real-world factual knowledge acquisition in LLMs. The limited diversity in the types of factual knowledge presented could also lead to biased conclusions about the general mechanisms of knowledge acquisition.
2. While the paper provides a comprehensive analysis of the dynamics of factual knowledge acquisition during pretraining, it does not offer any new methods or techniques for improving the acquisition of factual knowledge. The focus is on understanding the dynamics rather than proposing new methods to enhance it. The lack of practical implications for improving factual knowledge acquisition limits the impact of the study.
3. The paper's analysis is primarily based on log probability, which may not be a reliable metric for evaluating the quality of factual knowledge acquisition. The use of log probability as a proxy for factual correctness might not capture the nuances of how LLMs represent and utilize factual knowledge. The paper does not explore other metrics that might provide a more comprehensive understanding of factual knowledge acquisition.

### Suggestions

The study would benefit from a more rigorous exploration of the Fictional Knowledge dataset's limitations. The synthetic nature of the dataset, while allowing for controlled experiments, raises questions about the ecological validity of the findings. Future work should consider expanding the dataset to include more diverse and complex factual knowledge, potentially incorporating real-world data sources. This would help to assess whether the observed dynamics of factual knowledge acquisition generalize to more realistic scenarios. Furthermore, the controlled structure of the dataset might oversimplify the interactions between different factual pieces, which could be explored by introducing more complex relationships between the injected facts. This would provide a more nuanced understanding of how LLMs integrate and retain factual knowledge.

To enhance the practical impact of the study, future research should focus on developing methods to improve factual knowledge acquisition. While the paper provides valuable insights into the dynamics of this process, it does not offer any concrete solutions for enhancing it. Future work could explore techniques such as curriculum learning, where the model is gradually exposed to more complex factual knowledge, or active learning, where the model selects the most informative examples to learn from. Additionally, the study could investigate the use of external knowledge sources, such as knowledge graphs, to augment the model's factual knowledge. These approaches could lead to more effective methods for improving the acquisition and retention of factual knowledge in LLMs.

Finally, the paper should explore alternative metrics for evaluating the quality of factual knowledge acquisition beyond log probability. While log probability is a useful metric for measuring the model's confidence in its predictions, it may not fully capture the nuances of factual correctness. Future work could explore metrics such as accuracy, precision, and recall, which provide a more comprehensive understanding of the model's performance. Additionally, the study could investigate the use of human evaluation to assess the quality of the model's generated text. This would provide a more reliable measure of the model's factual knowledge acquisition and its ability to generate coherent and accurate text.

### Questions

1. How does the choice of log probability as the primary metric for evaluating factual knowledge acquisition impact the conclusions of the study?
2. How do the findings of this study generalize to real-world factual knowledge, where the knowledge is not synthetic and the relationships between facts are more complex?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper investigates how LLMs acquire factual knowledge during pretraining. The authors introduce a Fictional Knowledge dataset and analyze the dynamics of factual knowledge acquisition by varying training conditions such as knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes. They find that factual knowledge acquisition occurs through accumulating micro-acquisitions, and that effectivity does not improve with model scale or pretraining stage. The authors also discuss how their findings explain recently observed behaviors of LLMs, such as the improved performance of LLMs through data scaling and the benefits of deduplicating the pretraining corpus.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper provides a comprehensive analysis of factual knowledge acquisition in LLMs by varying training conditions such as knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes. This systematic approach allows for a deeper understanding of the dynamics of factual knowledge acquisition.
- The authors introduce a Fictional Knowledge dataset, which is a valuable contribution to the field. The dataset allows for a fine-grained analysis of how LLMs acquire and retain factual knowledge.
- The paper discusses how the findings explain recently observed behaviors of LLMs, such as the improved performance of LLMs through data scaling and the benefits of deduplicating the pretraining corpus. This connection to real-world phenomena adds to the significance of the study.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's analysis is primarily based on a single dataset, the Fictional Knowledge dataset, which may limit the generalizability of the findings. The dataset's synthetic nature and controlled structure might not fully capture the complexities of real-world factual knowledge acquisition in LLMs. The limited diversity in the types of factual knowledge presented could also lead to biased conclusions about the general mechanisms of knowledge acquisition.
- While the paper provides a comprehensive analysis of the dynamics of factual knowledge acquisition during pretraining, it does not offer any new methods or techniques for improving the acquisition of factual knowledge. The focus is on understanding the dynamics rather than proposing new methods to enhance it. The lack of practical implications for improving factual knowledge acquisition limits the impact of the study.
- The paper's analysis is primarily based on log probability, which may not be a reliable metric for evaluating the quality of factual knowledge acquisition. The use of log probability as a proxy for factual correctness might not capture the nuances of how LLMs represent and utilize factual knowledge. The paper does not explore other metrics that might provide a more comprehensive understanding of factual knowledge acquisition.

### Suggestions

The study would benefit from a more thorough investigation into the limitations of the Fictional Knowledge dataset. While controlled experiments are valuable, the synthetic nature of the data raises concerns about the ecological validity of the findings. Future work should explore methods to generate more realistic and diverse factual knowledge, potentially by incorporating data from real-world sources or by using more sophisticated data generation techniques. This would help to ensure that the conclusions drawn from the study are applicable to real-world scenarios. Furthermore, the study should investigate the impact of different types of factual knowledge on the acquisition process. For example, it would be interesting to examine whether the model learns factual knowledge about common entities and events differently than it learns about rare or obscure information. This could be achieved by categorizing the factual knowledge in the dataset based on its frequency and importance, and then analyzing the acquisition dynamics for each category.

To enhance the practical impact of the study, future research should focus on developing methods to improve the factual knowledge acquisition of LLMs. This could involve exploring techniques such as curriculum learning, where the model is gradually exposed to more complex factual knowledge, or active learning, where the model selects the most informative examples to learn from. Additionally, the study could investigate the use of external knowledge sources, such as knowledge graphs, to augment the model's factual knowledge. These approaches could lead to more effective methods for improving the acquisition and retention of factual knowledge in LLMs. The paper should also explore the use of alternative metrics for evaluating the quality of factual knowledge acquisition. While log probability is a useful metric for measuring the model's confidence in its predictions, it may not fully capture the nuances of factual correctness. Future work could explore metrics such as accuracy, precision, and recall, which provide a more comprehensive understanding of the model's performance. Furthermore, human evaluation could be used to assess the quality of the model's generated text and its ability to generate coherent and accurate factual information.

Finally, the paper should provide a more detailed analysis of the relationship between the model's performance on the Fictional Knowledge dataset and its performance on real-world tasks. While the dataset is useful for studying the dynamics of factual knowledge acquisition, it is important to ensure that the findings are relevant to practical applications. This could involve evaluating the model on a range of real-world benchmarks and comparing its performance to that of other state-of-the-art models. This would help to establish the generalizability of the findings and to identify any potential limitations of the approach. The paper should also discuss the ethical implications of the study, particularly in relation to the potential for bias in the model's factual knowledge. This is an important consideration that should be addressed in any research involving LLMs.

### Questions

- How does the choice of log probability as the primary metric for evaluating factual knowledge acquisition impact the conclusions of the study?
- How do the findings of this study generalize to real-world factual knowledge, where the knowledge is not synthetic and the relationships between facts are more complex?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates how LLMs acquire factual knowledge during pretraining. The authors propose a method to study the dynamics of factual knowledge acquisition by varying training conditions such as knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes. The authors find that factual knowledge acquisition occurs by accumulating micro-acquisitions, each of which occurs whenever the model is updated after seeing the factual knowledge. They also find that effectivity, the improvement in log probability after being trained with the injected knowledge, does not improve with model scale or pretraining stage. However, the effectivity does improve with model size and pretraining stage when the model is trained with a larger batch size. The authors also find that the acquisition of compositional generalization accumulates most slowly but is more robust to forgetting. Finally, the authors discuss how their findings explain recently observed behaviors of LLMs, such as the improved performance of LLMs through data scaling and the benefits of deduplicating the pretraining corpus.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The paper introduces a Fictional Knowledge dataset to study the dynamics of factual knowledge acquisition during pretraining. This dataset allows for a fine-grained analysis of how LLMs acquire and retain factual knowledge.
3. The paper provides a comprehensive analysis of the dynamics of factual knowledge acquisition during pretraining. They investigate various factors, such as knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes, and their impact on the acquisition and retention of factual knowledge.
4. The paper discusses how their findings explain recently observed behaviors of LLMs, such as the improved performance of LLMs through data scaling and the benefits of deduplicating the pretraining corpus.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's analysis is primarily based on a single dataset, the Fictional Knowledge dataset, which may limit the generalizability of the findings. The dataset's synthetic nature and controlled structure might not fully capture the complexities of real-world factual knowledge acquisition in LLMs. The limited diversity in the types of factual knowledge presented could also lead to biased conclusions about the general mechanisms of knowledge acquisition.
2. While the paper provides a comprehensive analysis of the dynamics of factual knowledge acquisition during pretraining, it does not offer any new methods or techniques for improving the acquisition of factual knowledge. The focus is on understanding the dynamics rather than proposing new methods to enhance it. The lack of practical implications for improving factual knowledge acquisition limits the impact of the study.
3. The paper's analysis is primarily based on log probability, which may not be a reliable metric for evaluating the quality of factual knowledge acquisition. The use of log probability as a proxy for factual correctness might not capture the nuances of how LLMs represent and utilize factual knowledge. The paper does not explore other metrics that might provide a more comprehensive understanding of factual knowledge acquisition.

### Suggestions

The study would benefit from a more rigorous exploration of the Fictional Knowledge dataset's limitations. The synthetic nature of the dataset, while allowing for controlled experiments, raises questions about the ecological validity of the findings. Future work should consider expanding the dataset to include more diverse and complex factual knowledge, potentially incorporating real-world data sources. This would help to assess whether the observed dynamics of factual knowledge acquisition generalize to more realistic scenarios. Furthermore, the controlled structure of the dataset might oversimplify the interactions between different factual pieces, which could be explored by introducing more complex relationships between the injected facts. This would provide a more nuanced understanding of how LLMs integrate and retain factual knowledge.

To enhance the practical impact of the study, future research should focus on developing methods to improve factual knowledge acquisition. While the paper provides valuable insights into the dynamics of this process, it does not offer any concrete solutions for enhancing it. Future work could explore techniques such as curriculum learning, where the model is gradually exposed to more complex factual knowledge, or active learning, where the model selects the most informative examples to learn from. Additionally, the study could investigate the use of external knowledge sources, such as knowledge graphs, to augment the model's factual knowledge. These approaches could lead to more effective methods for improving the acquisition and retention of factual knowledge in LLMs. The paper should also explore the use of alternative metrics for evaluating the quality of factual knowledge acquisition beyond log probability. While log probability is a useful metric for measuring the model's confidence in its predictions, it may not fully capture the nuances of factual correctness. Future work could explore metrics such as accuracy, precision, and recall, which provide a more comprehensive understanding of the model's performance. Furthermore, human evaluation could be used to assess the quality of the model's generated text and its ability to generate coherent and accurate factual information.

### Questions

1. How does the choice of log probability as the primary metric for evaluating factual knowledge acquisition impact the conclusions of the study?
2. How do the findings of this study generalize to real-world factual knowledge, where the knowledge is not synthetic and the relationships between facts are more complex?

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper studies the dynamics of factual knowledge acquisition in LLMs during pretraining. The authors introduce a Fictional Knowledge dataset to analyze how LLMs acquire and retain factual knowledge. They investigate various factors such as knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes. The key findings include that factual knowledge acquisition occurs through accumulating micro-acquisitions, effectivity does not improve with model scale or pretraining stage, and deduplicating the pretraining corpus is beneficial. The authors also discuss how their findings explain recent observations in LLMs, such as improved performance through data scaling and benefits of deduplication.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a fine-grained analysis of factual knowledge acquisition during pretraining, which is a novel contribution to the field.
- The use of a Fictional Knowledge dataset allows for controlled experiments and provides insights into the dynamics of knowledge acquisition.
- The paper offers a comprehensive analysis of various factors affecting factual knowledge acquisition, including knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes.
- The findings have practical implications for improving LLMs' factual knowledge and performance.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on synthetic factual knowledge, which may not fully capture the complexities of real-world knowledge acquisition in LLMs. The use of a fictional dataset, while allowing for controlled experiments, raises questions about the generalizability of the findings to real-world scenarios where knowledge is more complex and nuanced. The synthetic nature of the knowledge may not reflect the diverse and interconnected nature of factual information in real-world contexts.
- The paper does not explore the impact of different types of factual knowledge (e.g., common vs. rare) on the acquisition process. It is plausible that the model learns common factual knowledge more easily than rare or obscure information, and this could significantly impact the overall knowledge retention and generalization capabilities. The lack of analysis on the impact of different types of factual knowledge limits the scope of the study.
- The paper does not provide a detailed analysis of the forgetting dynamics of acquired factual knowledge. While the paper mentions that knowledge is forgotten after a certain period, it does not delve into the specific mechanisms or patterns of forgetting. Understanding the forgetting dynamics is crucial for developing strategies to mitigate the loss of acquired knowledge during pretraining. The paper should explore the factors that influence the rate and extent of forgetting.

### Suggestions

To enhance the study, the authors should consider incorporating more realistic knowledge sources beyond synthetic datasets. This could involve using existing knowledge graphs or knowledge bases to evaluate the model's ability to acquire and retain factual knowledge that is more representative of real-world scenarios. Furthermore, the authors should explore the impact of different types of factual knowledge, such as common, rare, and complex knowledge, on the acquisition process. This could involve designing experiments that specifically target these different types of knowledge and analyzing the resulting differences in acquisition rates and retention. For example, the authors could investigate whether the model learns common factual knowledge faster than rare or obscure information, and how this impacts the overall knowledge retention and generalization capabilities. This would provide a more nuanced understanding of the factors that influence factual knowledge acquisition in LLMs.

Additionally, the authors should conduct a more detailed analysis of the forgetting dynamics of acquired factual knowledge. This could involve tracking the model's performance on specific facts over time and identifying the factors that influence the rate and extent of forgetting. For instance, the authors could investigate whether the forgetting rate is influenced by the frequency of exposure to a particular fact, the type of knowledge being learned, or the overall training schedule. This analysis should also consider the potential for catastrophic forgetting, where the model forgets previously learned knowledge when learning new information. Understanding these dynamics is crucial for developing strategies to mitigate the loss of acquired knowledge during pretraining. The authors could also explore techniques such as knowledge distillation or replay methods to improve the retention of acquired knowledge.

Finally, the authors should consider exploring the impact of different pretraining strategies on factual knowledge acquisition. This could involve experimenting with different batch sizes, learning rates, or data augmentation techniques. The authors should also investigate the impact of different pretraining objectives on the model's ability to acquire and retain factual knowledge. For example, they could explore the use of contrastive learning or knowledge distillation to improve the model's factual knowledge. By exploring these different pretraining strategies, the authors can gain a deeper understanding of the factors that influence factual knowledge acquisition and develop more effective methods for improving it.

### Questions

- How does the choice of log probability as the primary metric for evaluating factual knowledge acquisition impact the conclusions of the study?
- How do the findings of this study generalize to real-world factual knowledge, where the knowledge is not synthetic and the relationships between facts are more complex?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find corresponding evidence in the paper.
3. If the weakness is about the method, look for issues in the description of the method, mathematical formulations, missing citations, etc.
4. If the weakness is about the experiments, look for issues in the dataset description, experimental setup, results, missing details, etc.
5. If the weakness is about the overall paper, consider the novelty, clarity, and impact.
6. If a weakness is not supported by evidence, mark it as invalid.
7. If there are conflicting opinions between reviewers, highlight them.
**Review 1**

1. Weakness Statement:
"The paper's analysis is primarily based on a single dataset, the Fictional Knowledge dataset, which may limit the generalizability of the findings. The dataset's synthetic nature and controlled structure might not fully capture the complexities of real-world factual knowledge acquisition in LLMs. The limited diversity in the types of factual knowledge presented could also lead to biased conclusions about the general mechanisms of knowledge acquisition."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: "To answer the research questions, we analyze how LLMs acquire and retain factual knowledge in terms of memorization and generalization by varying the following factors: (i) varying knowledge injection scenarios ( duplication , paraphrase , once ), (ii) varying pretraining stages ( early , mid , and late , pretrained with approximately 170B, 500B, and 1.5T tokens, respectively), (iii) varying model sizes (1B and 7B), and (iv) varying training batch sizes (2048 and 128)." (Section 3)
   - Dataset/setup descriptions: "To this end, we construct Fictional Knowledge dataset: passages that contain the description of fictional yet realistic entities. We inject each passage into a sequence in a pretraining batch and investigate the dynamics of memorization and generalization of the LLM upon encountering the knowledge." (Section 3)
   - Dataset/setup descriptions: "All instances for the injected knowledge and probes are generated by prompting GPT-4 [ 2 ] using the definitions from the ECBD dataset [ 35 ] as a template, and filtering out invalid cases." (Section 3)
   - Dataset/setup descriptions: "Each probe is structured as a cloze task, consisting of an input and a target span, where the target span is a short phrase designed to test the acquisition of the factual knowledge we evaluate." (Section 3)
   - Dataset/setup descriptions: "An example of injected knowledge and corresponding probes is illustrated in Table 1 ." (Section 3)
   - Dataset/setup descriptions: "Table 1 : An example of injected knowledge and corresponding probes is illustrated in Table 1 ." (Section 3) - This table shows examples of the synthetic factual knowledge.

3. Literature Gap Analysis:
   - No specific missing citations are directly related to this point, but the reviewer suggests that the dataset's synthetic nature and controlled structure might limit generalizability, implying a need for discussion on the limitations of synthetic datasets in this context.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly states the use of the Fictional Knowledge dataset and describes its construction as synthetic factual knowledge. The examples provided in Table 1 further support the synthetic nature of the data.
   - Supporting quotes: "We construct Fictional Knowledge dataset: passages that contain the description of fictional yet realistic entities." "All instances for the injected knowledge and probes are generated by prompting GPT-4..."
   - Impact assessment: The reviewer's point about the limitations of a single synthetic dataset is valid. The paper does not explicitly discuss the potential limitations of using such a dataset for generalizing findings to real-world factual knowledge.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the Fictional Knowledge dataset and its construction process.

1. Weakness Statement:
"While the paper provides a comprehensive analysis of the dynamics of factual knowledge acquisition during pretraining, it does not offer any new methods or techniques for improving the acquisition of factual knowledge. The focus is on understanding the dynamics rather than proposing new methods to enhance it. The lack of practical implications for improving factual knowledge acquisition limits the impact of the study."

2. Evidence Collection:
- The paper focuses on analyzing the dynamics of knowledge acquisition. The "Main Idea" section states: "This paper investigates how Large Language Models (LLMs) acquire factual knowledge during pretraining by analyzing the dynamics of factual knowledge acquisition." The "Method" section describes the experimental setup and metrics used for analysis. The "Findings" section presents observations about these dynamics. The "Conclusion" section discusses the implications of these findings for understanding LLM behavior but does not propose new methods.

3. Literature Gap Analysis:
   - The paper does not cite or discuss methods for improving factual knowledge acquisition in LLMs.

4. Validation Analysis:
   - Primary evidence summary: The paper's focus is clearly on understanding the dynamics of knowledge acquisition, not on proposing new methods to improve it.
   - Supporting quotes: "This paper investigates how Large Language Models (LLMs) acquire factual knowledge during pretraining..."
   - Impact assessment: The reviewer's point is valid. The paper's contribution is primarily analytical, and it does not offer novel methods for improving factual knowledge acquisition.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The stated focus of the paper and the content of the "Method" and "Findings" sections.

1. Weakness Statement:
"The paper's analysis is primarily based on log probability, which may not be a reliable metric for evaluating the quality of factual knowledge acquisition. The use of log probability as a proxy for factual correctness might not capture the nuances of how LLMs represent and utilize factual knowledge. The paper does not explore other metrics that might provide a more comprehensive understanding of factual knowledge acquisition."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Definition 1: "Definition 1 (Definition 1) Given a language model, let θ t \theta_{t} represent the model’s parameters before the t t -th update. Given injected knowledge k k (used as a training instance) and the corresponding probe q q (used as an evaluation instance), let ℓ ⁡ ( q , θ t ) \ell(q;\theta_{t}) denote the log probability of the target span of q q between t = t i t i and t = t i + t w i t_{\text{tw}} ) , where ​ t i ∈ T k . t_{i}\in T_{k} . (1) Given a language model parameterized by θ \theta trained with an injected knowledge k k at t = t i t=t_{i} where t i ∈ T k t_{i}\in T_{k} , and a corresponding probe q q , the log probability measured on the target spans of the probes for each injection scenario, evaluated at each training step. This metric, effectivity , will be used to answer the second research question." (Section 3)
   - Definition 2: "Definition 2 (Definition 2) Given a language model parameterized by θ \theta and trained with injected knowledge k k for N N iterations, occurance of the log probability reaches a maximum value in a short interval after the model is trained on the injected knowledge, which we refer to as the local acquisition maxima ." (Section 3)
   - Definition 3: "Definition 3 (Definition 3) Consider a language model parameterized by θ \theta and trained with injected knowledge k k for N N iterations, occuring at t = t i t_i . Given a corresponding probe q q , retainability ( ℛ ⁡ ( q , t ) \mathcal{R}( q , t ) ) is defined for t ≥ 0 t\geq 0 as follows: ℛ ⁡ ( q , t ) \displaystyle\mathcal{R} ⁡ ( q , t ) = ℓ ⁡ ( q , θ t L A M B D A ) − ℓ ⁡ ( q , θ t pre ) ℓ ⁡ ( q , θ t pre ) . (2) Finally, to investigate the forgetting phenomenon of acquired factual knowledge (R3), we define a metric that quantifies the fraction of improvement in log probability retained by the model after t t steps, relative to the local acquisition maxima of the last knowledge update." (Section 3)
   - Definition 4: "Definition 4 (Definition 4) Finally, to investigate the forgetting phenomenon of acquired factual knowledge (R3), we define a metric that quantifies the fraction of improvement in log probability retained by the model after t t steps, relative to the local acquisition maxima of the last knowledge update. Table 2 shows the decay constants of retainability measured for three OLMo-7B intermediate checkpoints, for duplication and paraphrase injection scenarios." (Section 3)

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly defines and uses log probability and related metrics (effectivity and retainability) as the primary measures for evaluating factual knowledge acquisition and retention.
   - Supporting quotes: The definitions of the metrics in Section 3 clearly show their reliance on log probability.
   - Impact assessment: The reviewer's point is valid. The paper's reliance on log probability as the primary metric is a limitation, and it does not explore other metrics for evaluating factual knowledge.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The definitions of the evaluation metrics in the paper.

**Review 2**

1. Weakness Statement:
"The paper primarily focuses on synthetic factual knowledge, which may not fully capture the complexities of real-world knowledge acquisition in LLMs. The use of a fictional dataset, while allowing for controlled experiments, raises questions about the generalizability of the findings to real-world scenarios where knowledge is more complex and nuanced. The synthetic nature of the knowledge may not reflect the diverse and interconnected nature of factual information in real-world contexts."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: "To this end, we construct Fictional Knowledge dataset: passages that contain the description of fictional yet realistic entities. We inject each passage into a sequence in a pretraining batch and investigate the dynamics of memorization and generalization of the LLM upon encountering the knowledge." (Section 3)
   - Dataset/setup descriptions: "Each probe is structured as a cloze task, consisting of an input and a target span, where the target span is a short phrase designed to test the acquisition of the factual knowledge we evaluate." (Section 3)
   - Dataset/setup descriptions: "An example of injected knowledge and corresponding probes is illustrated in Table 1 ." (Section 3)
   - Dataset/setup descriptions: "Table 1 : An example of injected knowledge and corresponding probes is illustrated in Table 1 ." (Section 3) - This table shows examples of the synthetic factual knowledge.

3. Literature Gap Analysis:
   - No specific missing citations are directly related to this point, but the reviewer suggests that the dataset's synthetic nature and controlled structure might limit generalizability, implying a need for discussion on the limitations of synthetic datasets in this context.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly states the use of the Fictional Knowledge dataset and describes its construction as synthetic factual knowledge. The examples provided in Table 1 further support the synthetic nature of the data.
   - Supporting quotes: "We construct Fictional Knowledge dataset: passages that contain the description of fictional yet realistic entities."
   - Impact assessment: The reviewer's point is valid. The paper does not explicitly discuss the potential limitations of using such a dataset for generalizing findings to real-world factual knowledge.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the Fictional Knowledge dataset and its construction process.

1. Weakness Statement:
"The paper does not explore the impact of different types of factual knowledge (e.g., common vs. rare) on the acquisition process. It is plausible that the model learns common factual knowledge more easily than rare or obscure information, and this could significantly impact the overall knowledge retention and generalization capabilities. The lack of analysis on the impact of different types of factual knowledge limits the scope of the study."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper describes the "Fictional Knowledge dataset" in Section 3. While it mentions "factual knowledge," it doesn't specify whether the knowledge is categorized by frequency or commonness. The examples in Table 1 appear to be of a similar nature.
   - The experimental setup in Section 4 focuses on varying knowledge injection scenarios (duplication, paraphrase, once) and pretraining stages, model sizes, and batch sizes, but there's no mention of experiments that specifically target different types of factual knowledge (common vs. rare).

3. Literature Gap Analysis:
   - The paper does not cite literature that specifically investigates the impact of different types of factual knowledge on LLM acquisition.

4. Validation Analysis:
   - Primary evidence summary: The paper's methodology and experiments do not include a systematic analysis of the impact of different types of factual knowledge (e.g., common vs. rare).
   - Supporting quotes: The descriptions of the dataset and experiments in Section 3 and 4 do not mention any categorization or manipulation of factual knowledge based on its frequency or commonness.
   - Impact assessment: The reviewer's point is valid. The lack of analysis on different types of factual knowledge is a limitation of the study.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The description of the dataset and the experimental setup.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the forgetting dynamics of acquired factual knowledge. While the paper mentions that knowledge is forgotten after a certain period, it does not delve into the specific mechanisms or patterns of forgetting. Understanding the forgetting dynamics is crucial for developing strategies to mitigate the loss of acquired knowledge during pretraining. The paper should explore the factors that influence the rate and extent of forgetting."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Definition 3: "Definition 3 (Definition 3) Consider a language model parameterized by θ \theta and trained with injected knowledge k k for N N iterations, occuring at t = t i t_i . Given a corresponding probe q q , retainability ( ℛ ⁡ ( q , t ) \mathcal{R}( q , t ) ) is defined for t ≥ 0 t\geq 0 as follows: ℛ ⁡ ( q , t ) \displaystyle\mathcal{R} ⁡ ( q , t ) = ℓ ⁡ ( q , θ t L A M B D A ) − ℓ ⁡ ( q , θ t pre ) ℓ ⁡ ( q , θ t pre ) . (2) Finally, to investigate the forgetting phenomenon of acquired factual knowledge (R3), we define a metric that quantifies the fraction of improvement in log probability retained by the model after t t steps, relative to the local acquisition maxima of the last knowledge update." (Section 3)
   - The paper introduces the concept of "forgetting" and uses the "decay constant" to quantify it in the results (Section 4.3). However, it does not delve into the underlying mechanisms or factors influencing this decay.

3. Literature Gap Analysis:
   - The paper cites works related to memorization and forgetting in neural networks, but it doesn't deeply engage with literature specifically focused on the mechanisms of forgetting in LLMs or the factors that influence it.

4. Validation Analysis:
   - Primary evidence summary: The paper defines and measures forgetting using the decay constant but does not provide a detailed analysis of the underlying mechanisms or influencing factors.
   - Supporting quotes: The definition of retainability in Section 3 and the discussion of the decay constant in Section 4.3 support this.
   - Impact assessment: The reviewer's point is valid. The analysis of forgetting dynamics is limited to quantifying the decay constant without exploring the underlying causes.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The definition of retainability and the discussion of the decay constant.

**Review 3**

1. Weakness Statement:
"The paper's analysis is primarily based on a single dataset, the Fictional Knowledge dataset, which may limit the generalizability of the findings. The dataset's synthetic nature and controlled structure might not fully capture the complexities of real-world factual knowledge acquisition in LLMs. The limited diversity in the types of factual knowledge presented could also lead to biased conclusions about the general mechanisms of knowledge acquisition."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: "To this end, we construct Fictional Knowledge dataset: passages that contain the description of fictional yet realistic entities. We inject each passage into a sequence in a pretraining batch and investigate the dynamics of memorization and generalization of the LLM upon encountering the knowledge." (Section 3)
   - Dataset/setup descriptions: "Each probe is structured as a cloze task, consisting of an input and a target span, where the target span is a short phrase designed to test the acquisition of the factual knowledge we evaluate." (Section 3)
   - Dataset/setup descriptions: "An example of injected knowledge and corresponding probes is illustrated in Table 1 ." (Section 3)
   - Dataset/setup descriptions: "Table 1 : An example of injected knowledge and corresponding probes is illustrated in Table 1 ." (Section 3) - This table shows examples of the synthetic factual knowledge.

3. Literature Gap Analysis:
   - No specific missing citations are directly related to this point, but the reviewer suggests that the dataset's synthetic nature and controlled structure might limit generalizability, implying a need for discussion on the limitations of synthetic datasets in this context.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly states the use of the Fictional Knowledge dataset and describes its construction as synthetic factual knowledge. The examples provided in Table 1 further support the synthetic nature of the data.
   - Supporting quotes: "We construct Fictional Knowledge dataset: passages that contain the description of fictional yet realistic entities."
   - Impact assessment: The reviewer's point is valid. The paper does not explicitly discuss the potential limitations of using such a dataset for generalizing findings to real-world factual knowledge.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the Fictional Knowledge dataset and its construction process.

1. Weakness Statement:
"While the paper provides a comprehensive analysis of the dynamics of factual knowledge acquisition during pretraining, it does not offer any new methods or techniques for improving the acquisition of factual knowledge. The focus is on understanding the dynamics rather than proposing new methods to enhance it. The lack of practical implications for improving factual knowledge acquisition limits the impact of the study."

2. Evidence Collection:
- The paper focuses on analyzing the dynamics of knowledge acquisition. The "Main Idea" section states: "This paper investigates how Large Language Models (LLMs) acquire factual knowledge during pretraining by analyzing the dynamics of factual knowledge acquisition." The "Method" section describes the experimental setup and metrics used for analysis. The "Findings" section presents observations about these dynamics. The "Conclusion" section discusses the implications of these findings for understanding LLM behavior but does not propose new methods.

3. Literature Gap Analysis:
   - The paper does not cite or discuss methods for improving factual knowledge acquisition in LLMs.

4. Validation Analysis:
   - Primary evidence summary: The paper's focus is clearly on understanding the dynamics of knowledge acquisition, not on proposing new methods to improve it.
   - Supporting quotes: "This paper investigates how Large Language Models (LLMs) acquire factual knowledge during pretraining..."
   - Impact assessment: The reviewer's point is valid. The paper's contribution is primarily analytical, and it does not offer novel methods for improving factual knowledge acquisition.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The stated focus of the paper and the content of the "Method" and "Findings" sections.

1. Weakness Statement:
"The paper's analysis is primarily based on log probability, which may not be a reliable metric for evaluating the quality of factual knowledge acquisition. The use of log probability as a proxy for factual correctness might not capture the nuances of how LLMs represent and utilize factual knowledge. The paper does not explore other metrics that might provide a more comprehensive understanding of factual knowledge acquisition."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Definition 1: "Definition 1 (Definition 1) Given a language model, let θ t \theta_{t} represent the model’s parameters before the t t -th update. Given injected knowledge k k (used as a training instance) and the corresponding probe q q (used as an evaluation instance), let ℓ ⁡ ( q , θ t ) \ell(q;\theta_{t}) denote the log probability of the target span of q q between t = t i t i and t = t i + t w i t_{\text{tw}} ) , where ​ t i ∈ T k . t_{i}\in T_{k} . (1) Given a language model parameterized by θ \theta trained with an injected knowledge k k at t = t i t=t_{i} where t i ∈ T k t_{i}\in T_{k} , and a corresponding probe q q , the log probability measured on the target spans of the probes for each injection scenario, evaluated at each training step. This metric, effectivity , will be used to answer the second research question." (Section 3)
   - Definition 2: "Definition 2 (Definition 2) Given a language model parameterized by θ \theta and trained with injected knowledge k k for N N iterations, occurance of the log probability reaches a maximum value in a short interval after the model is trained on the injected knowledge, which we refer to as the local acquisition maxima ." (Section 3)
   - Definition 3: "Definition 3 (Definition 3) Consider a language model parameterized by θ \theta and trained with injected knowledge k k for N N iterations, occuring at t = t i t_i . Given a corresponding probe q q , retainability ( ℛ ⁡ ( q , t ) \mathcal{R}( q , t ) ) is defined for t ≥ 0 t\geq 0 as follows: ℛ ⁡ ( q , t ) \displaystyle\mathcal{R} ⁡ ( q , t ) = ℓ ⁡ ( q , θ t L A M B D A ) − ℓ ⁡ ( q , θ t pre ) ℓ ⁡ ( q , θ t pre ) . (2) Finally, to investigate the forgetting phenomenon of acquired factual knowledge (R3), we define a metric that quantifies the fraction of improvement in log probability retained by the model after t t steps, relative to the local acquisition maxima of the last knowledge update." (Section 3)
   - Definition 4: "Definition 4 (Definition 4) Finally, to investigate the forgetting phenomenon of acquired factual knowledge (R3), we define a metric that quantifies the fraction of improvement in log probability retained by the model after t t steps, relative to the local acquisition maxima of the last knowledge update. Table 2 shows the decay constants of retainability measured for three OLMo-7B intermediate checkpoints, for duplication and paraphrase injection scenarios." (Section 3)

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly defines and uses log probability and related metrics (effectivity and retainability) as the primary measures for evaluating factual knowledge acquisition and retention.
   - Supporting quotes: The definitions of the metrics in Section 3 clearly show their reliance on log probability.
   - Impact assessment: The reviewer's point is valid. The paper's reliance on log probability as the primary metric is a limitation, and it does not explore other metrics for evaluating factual knowledge.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The definitions of the evaluation metrics in the paper.

**Review 4**

1. Weakness Statement:
"How does the choice of log probability as the primary metric for evaluating factual knowledge acquisition impact the conclusions of the study?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - Definition 1: "Definition 1 (Definition 1) Given a language model, let θ t \theta_{t} represent the model’s parameters before the t t -th update. Given injected knowledge k k (used as a training instance) and the corresponding probe q q (used as an evaluation instance), let ℓ ⁡ ( q , θ t ) \ell(q;\theta_{t}) denote the log probability of the target span of q q between t = t i t_i and t = t i + t w i t_{\text{tw}} ) , where ​ t i ∈ T k . t_{i}\in T_{k} . (1) Given a language model parameterized by θ \theta trained with an injected knowledge k k at t = t i t=t_{i} where t i ∈ T k t_{i}\in T_{k} , and a corresponding probe q q , the log probability measured on the target spans of the probes for each injection scenario, evaluated at each training step. This metric, effectivity , will be used to answer the second research question." (Section 3)
   - Definition 2: "Definition 2 (Definition 2) Given a language model parameterized by θ \theta and trained with injected knowledge k k for N N iterations, occurance of the log probability reaches a maximum value in a short interval after the model is trained on the injected knowledge, which we refer to as the local acquisition maxima ." (Section 3)
   - Definition 3: "Definition 3 (Definition 3) Consider a language model parameterized by θ \theta and trained with injected knowledge k k for N N iterations, occuring at t = t i t_i . Given a corresponding probe q q , retainability ( ℛ ⁡ ( q , t ) \mathcal{R}( q , t ) ) is defined for t ≥ 0 t\geq 0 as follows: ℛ ⁡ ( q , t ) \displaystyle\mathcal{R} ⁡ ( q , t ) = ℓ ⁡ ( q , θ t L A M B D A ) − ℓ ⁡ ( q , θ t pre ) ℓ ⁡ ( q , θ t pre ) . (2) Finally, to investigate the forgetting phenomenon of acquired factual knowledge (R3), we define a metric that quantifies the fraction of improvement in log probability retained by the model after t t steps, relative to the local acquisition maxima of the last knowledge update." (Section 3)
   - Definition 4: "Definition 4 (Definition 4) Finally, to investigate the forgetting phenomenon of acquired factual knowledge (R3), we define a metric that quantifies the fraction of improvement in log probability retained by the model after t t steps, relative to the local acquisition maxima of the last knowledge update. Table 2 shows the decay constants of retainability measured for three OLMo-7B intermediate checkpoints, for duplication and paraphrase injection scenarios." (Section 3)

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly defines and uses log probability and related metrics (effectivity and retainability) as the primary measures for evaluating factual knowledge acquisition and retention.
   - Supporting quotes: The definitions of the metrics in Section 3 clearly show their reliance on log probability.
   - Impact assessment: The reviewer's point is valid. The paper's reliance on log probability as the primary metric is a limitation, and it does not explore other metrics for evaluating factual knowledge.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The definitions of the evaluation metrics in the paper.

1. Weakness Statement:
"How do the findings of this study generalize to real-world factual knowledge, where the knowledge is not synthetic and the relationships between facts are more complex?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: "To this end, we construct Fictional Knowledge dataset: passages that contain the description of fictional yet realistic entities. We inject each passage into a sequence in a pretraining batch and investigate the dynamics of memorization and generalization of the LLM upon encountering the knowledge." (Section 3)
   - Dataset/setup descriptions: "Each probe is structured as a cloze task, consisting of an input and a target span, where the target span is a short phrase designed to test the acquisition of the factual knowledge we evaluate." (Section 3)
   - Dataset/setup descriptions: "An example of injected knowledge and corresponding probes is illustrated in Table 1 ." (Section 3)
   - Dataset/setup descriptions: "Table 1 : An example of injected knowledge and corresponding probes is illustrated in Table 1 ." (Section 3) - This table shows examples of the synthetic factual knowledge.

3. Literature Gap Analysis:
   - The paper does not cite literature that specifically investigates the impact of different types of factual knowledge on LLM acquisition.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly states the use of the Fictional Knowledge dataset and describes its construction as synthetic factual knowledge. The examples provided in Table 1 further support the synthetic nature of the data.
   - Supporting quotes: "We construct Fictional Knowledge dataset: passages that contain the description of fictional yet realistic entities."
   - Impact assessment: The reviewer's point is valid. The paper does not explicitly discuss the potential limitations of using such a dataset for generalizing findings to real-world factual knowledge.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the Fictional Knowledge dataset and its construction process.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper delves into the dynamics of factual knowledge acquisition in Large Language Models (LLMs) during the pretraining phase, employing a Fictional Knowledge dataset to facilitate a controlled experimental environment. The authors meticulously examine how LLMs acquire and retain factual information by varying several key factors, including knowledge injection scenarios (such as duplication, paraphrasing, and once), pretraining stages (early, mid, and late), model sizes, and training batch sizes. Their core methodology revolves around injecting synthetic factual knowledge into the pretraining data and then assessing the model's ability to memorize and generalize this information through carefully designed probing tasks. The primary metric used to evaluate the model's performance is the log probability of the target span in the cloze task, which serves as a proxy for the model's confidence and correctness in its knowledge. The study's findings reveal several interesting trends. Notably, the acquisition of factual knowledge occurs through a process of accumulating micro-acquisitions, where the model gradually improves its performance with each exposure to the knowledge. A significant finding is that the effectivity, or the improvement in log probability after being trained with the injected knowledge, does not improve with model scale or pretraining stage. This challenges the common assumption that larger models or more extensive pretraining leads to better factual knowledge acquisition. Furthermore, the authors observe that the acquisition of compositional generalization accumulates most slowly but is more robust to forgetting. Finally, the study demonstrates that increasing the training batch size can improve effectivity, suggesting that more data processed during training leads to better knowledge retention. Overall, this paper provides a comprehensive analysis of the dynamics of factual knowledge acquisition in LLMs, highlighting the complex interplay between various factors and challenging some of the conventional assumptions in the field. The authors' work is significant because it offers a fine-grained analysis of how LLMs learn factual knowledge, which can inform future research and development in this area. By using a controlled dataset and a well-defined methodology, the authors are able to provide a clear and detailed picture of the learning process, which is a valuable contribution to the field.


## Soundness:

2.25


## Presentation:

2.75


## Contribution:

2.25


## Strengths:

This paper presents several notable strengths that contribute to its overall value and impact. First and foremost, the introduction of the Fictional Knowledge dataset is a significant contribution. This dataset allows for a fine-grained analysis of how LLMs acquire and retain factual knowledge, which is a valuable tool for researchers in this field. The dataset's controlled nature, with its synthetic factual knowledge and structured probing tasks, enables a detailed examination of the learning process. The authors' meticulous approach to experimental design is another strength. By systematically varying knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes, they are able to provide a comprehensive analysis of the factors that influence factual knowledge acquisition. This rigorous approach allows for a clear understanding of the complex interplay between these factors. Furthermore, the paper's analysis of the dynamics of factual knowledge acquisition is a key strength. The authors' finding that factual knowledge acquisition occurs through accumulating micro-acquisitions is a novel and insightful observation. This finding challenges the notion that knowledge acquisition is a linear process and highlights the importance of understanding the dynamics of this process. The paper also provides a comprehensive analysis of the effectivity of the injected knowledge, which is a crucial metric for evaluating the quality of knowledge acquisition. The authors' finding that effectivity does not improve with model scale or pretraining stage is a significant contribution to our understanding of how LLMs learn. This finding challenges some of the conventional assumptions in the field and highlights the need for further research in this area. Finally, the paper's discussion of how the findings explain recently observed behaviors of LLMs, such as the improved performance of LLMs through data scaling and the benefits of deduplicating the pretraining corpus, is a valuable contribution. This discussion provides a clear connection between the paper's findings and real-world phenomena, which enhances the paper's overall impact. In summary, the paper's strengths lie in its novel dataset, rigorous experimental design, insightful analysis of the dynamics of factual knowledge acquisition, and clear connection to real-world phenomena. These strengths make the paper a valuable contribution to the field of LLM research.


## Weaknesses:

Despite its strengths, this paper exhibits several weaknesses that warrant careful consideration. A primary concern is the paper's reliance on a single dataset, the Fictional Knowledge dataset. As the authors themselves acknowledge, this dataset, while allowing for controlled experiments, may not fully capture the complexities of real-world factual knowledge acquisition in LLMs. The synthetic nature of the factual knowledge presented in the dataset, as evidenced by the examples in Table 1, raises questions about the generalizability of the findings. The limited diversity in the types of factual knowledge presented could also lead to biased conclusions about the general mechanisms of knowledge acquisition. The paper does not explore the impact of different types of factual knowledge, such as common versus rare knowledge, on the acquisition process. This is a significant limitation, as the model's ability to learn common factual knowledge may differ from its ability to learn rare or obscure information. Furthermore, the paper's analysis is primarily based on log probability, which may not be a reliable metric for evaluating the quality of factual knowledge acquisition. The use of log probability as a proxy for factual correctness might not capture the nuances of how LLMs represent and utilize factual knowledge. The paper does not explore other metrics that might provide a more comprehensive understanding of factual knowledge acquisition. This reliance on log probability as the primary metric is a limitation, and it does not explore other metrics for evaluating factual knowledge. The paper's analysis of forgetting dynamics is also limited. While the paper mentions that knowledge is forgotten after a certain period, it does not delve into the specific mechanisms or patterns of forgetting. The paper introduces the concept of 'forgetting' and uses the 'decay constant' to quantify it in the results, but it does not provide a detailed analysis of the underlying mechanisms or influencing factors. Understanding the forgetting dynamics is crucial for developing strategies to mitigate the loss of acquired knowledge during pretraining. The paper should explore the factors that influence the rate and extent of forgetting. Finally, the paper does not offer any new methods or techniques for improving the acquisition of factual knowledge. The focus is on understanding the dynamics rather than proposing new methods to enhance it. The lack of practical implications for improving factual knowledge acquisition limits the impact of the study. The paper's contribution is primarily analytical, and it does not offer novel methods for improving factual knowledge acquisition. These limitations, all of which are supported by the paper's content, highlight the need for further research to address these concerns. The confidence level in these identified issues is high, as they are clearly demonstrated by the paper's methodology and results.


## Suggestions:

To enhance the practical impact of this study, several concrete improvements can be made. First, the authors should consider expanding the dataset to include more diverse and complex factual knowledge. This could involve incorporating real-world data sources and using existing knowledge graphs to evaluate the model's ability to acquire and retain factual knowledge that is not synthetic and the relationships between facts are more complex. This would help to assess whether the observed dynamics of factual knowledge acquisition generalize to more realistic scenarios. Furthermore, the controlled structure of the dataset might oversimplify the interactions between different factual pieces, which could be explored by introducing more complex relationships between the injected facts. This would provide a more nuanced understanding of how LLMs integrate and retain factual knowledge. To enhance the practical impact of the study, future research should focus on developing methods to improve factual knowledge acquisition. While the paper provides valuable insights into the dynamics of this process, it does not offer any concrete solutions for enhancing it. Future work could explore techniques such as curriculum learning, where the model is gradually exposed to more complex factual knowledge, or active learning, where the model selects the most informative examples to learn from. Additionally, the study could investigate the use of external knowledge sources, such as knowledge graphs, to augment the model's factual knowledge. These approaches could lead to more effective methods for improving the acquisition and retention of factual knowledge in LLMs. The paper should also explore the use of alternative metrics for evaluating the quality of factual knowledge acquisition beyond log probability. While log probability is a useful metric for measuring the model's confidence in its predictions, it may not fully capture the nuances of how LLMs represent and utilize factual knowledge. Future work could explore metrics such as accuracy, precision, and recall, which provide a more comprehensive understanding of the model's performance. Additionally, the study could investigate the use of human evaluation to assess the quality of the model's generated text and its ability to generate coherent and accurate factual information. This would provide a more reliable measure of the model's factual knowledge acquisition and its ability to generate coherent and accurate text. Finally, the paper should provide a more detailed analysis of the forgetting dynamics of acquired factual knowledge. This could involve tracking the model's performance on specific facts over time and identifying the factors that influence the rate and extent of forgetting. For instance, the authors could investigate whether the forgetting rate is influenced by the frequency of exposure to a particular fact, the type of knowledge being learned, or the overall training schedule. This analysis should also consider the potential for catastrophic forgetting, where the model forgets previously learned knowledge when learning new information. Understanding these dynamics is crucial for developing strategies to mitigate the loss of acquired knowledge during pretraining. The authors could also explore techniques such as knowledge distillation or replay methods to improve the retention of acquired knowledge. By addressing these limitations, the study can provide a more comprehensive understanding of factual knowledge acquisition in LLMs and contribute to the development of more effective methods for improving it.


## Questions:

Several key questions arise from my analysis of this paper, primarily concerning the generalizability of the findings and the choice of evaluation metrics. First, how does the choice of log probability as the primary metric for evaluating factual knowledge acquisition impact the conclusions of the study? The paper relies heavily on log probability, which, as I've verified, may not be a reliable metric for evaluating the quality of factual knowledge acquisition. I am curious about the authors' rationale for choosing this metric and whether they considered alternative metrics that might provide a more comprehensive understanding of factual knowledge. Second, how do the findings of this study generalize to real-world factual knowledge, where the knowledge is not synthetic and the relationships between facts are more complex? The paper's use of the Fictional Knowledge dataset, while allowing for controlled experiments, raises questions about the generalizability of the findings to real-world scenarios. I am interested in understanding the authors' perspective on the limitations of their dataset and the potential for bias in their conclusions. Third, what are the specific mechanisms or patterns of forgetting that influence the rate and extent of knowledge loss? The paper introduces the concept of 'forgetting' and uses the 'decay constant' to quantify it, but it does not provide a detailed analysis of the underlying mechanisms or influencing factors. I am curious about the authors' insights into the factors that contribute to forgetting and how these factors might be mitigated. Finally, how do the findings of this study generalize to real-world factual knowledge, where the knowledge is not synthetic and the relationships between facts are more complex? This question is closely related to the second question, but I am particularly interested in understanding the authors' perspective on the challenges of applying their findings to real-world scenarios. These questions highlight key uncertainties in the paper and point to areas where further research is needed to fully understand the dynamics of factual knowledge acquisition in LLMs.


## Rating:

5.25


## Confidence:

3.25


## Decision:

Reject
}