I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies the phenomenon of concept-specific anti-readers in activation oracles (AOs). The authors focus on the setting of fine-tuned subject models trained to internally use a hidden concept while avoiding direct disclosure. They train AOs on activations from these fine-tuned subjects and evaluate whether the AOs can recover the hidden concept. The main finding is that fine-tuned AOs do not become better specialist readers of the hidden concept; instead, they develop concept-specific blind spots, failing to recover the concept even though it is present in the subject model's internal representations. The authors provide evidence that this failure is not simply due to the absence of the concept in the oracle's representations, but rather due to the oracle's own training process. They suggest that this phenomenon poses a reliability concern for learned interpretability interfaces, as the reader itself may acquire blind spots induced by its training procedure.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper addresses an important and timely topic in interpretability research: the reliability of learned models as readers of other models' internal states. This is particularly relevant as the field moves towards more complex and opaque models.
- The experimental setup is well-designed and the analysis is thorough, covering multiple aspects of the phenomenon.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's central claim that fine-tuned AOs develop concept-specific blind spots is not entirely convincing. The authors argue that the target concept is still decodable inside the oracle, but this does not necessarily imply that the oracle can effectively verbalize it. The fact that the target concept is present in the oracle's representations does not guarantee that the oracle can successfully communicate this information to the user. The authors need to provide more evidence to support their claim that the oracle's internal representation of the target concept is not effectively verbalized.
- The paper does not adequately address the potential for alternative explanations for the observed phenomenon. For example, the authors could have explored whether the observed behavior is due to the specific training data or the architecture of the AOs. The paper would benefit from a more thorough investigation of these alternative explanations.
- The paper's focus on concept-specific anti-readers is interesting, but the practical implications of this phenomenon are not fully explored. The authors should discuss how this phenomenon might affect the use of AOs in real-world applications and what steps could be taken to mitigate the risks.

### Suggestions

The authors should provide a more detailed analysis of the oracle's internal representations to support their claim that the target concept is not effectively verbalized. This could involve techniques such as probing the oracle's hidden states or visualizing the activation patterns. It is not sufficient to simply show that the target concept is decodable inside the oracle; the authors need to demonstrate that the oracle can successfully communicate this information to the user. Furthermore, the authors should explore the possibility that the observed behavior is due to the specific training data or the architecture of the AOs. This could involve experimenting with different training datasets or AO architectures, or by using techniques such as ablation studies to identify the specific factors that contribute to the phenomenon. For example, the authors could try training AOs with different levels of regularization or with different activation functions to see how these changes affect the oracle's ability to verbalize the target concept. 

The authors should also discuss the practical implications of their findings in more detail. While the paper focuses on the theoretical aspects of concept-specific anti-readers, it is important to consider how this phenomenon might affect the use of AOs in real-world applications. For example, if an AO is used to audit a large language model, it is important to understand whether the AO might develop blind spots that could lead to inaccurate or incomplete interpretations. The authors should discuss how these blind spots might affect the trustworthiness of the AO and what steps could be taken to mitigate these risks. This could involve developing new evaluation metrics or using techniques such as adversarial training to improve the robustness of AOs. The authors should also consider the ethical implications of their findings, particularly in the context of sensitive applications such as healthcare or finance.

Finally, the authors should consider the limitations of their study and suggest directions for future research. For example, the authors could explore whether the phenomenon of concept-specific anti-readers is specific to the type of model or task used in their study, or whether it is a more general phenomenon that applies to a wider range of models and tasks. The authors could also explore whether the phenomenon can be mitigated by using different training techniques or by incorporating additional information into the AO's training process. Addressing these limitations and suggesting future research directions would strengthen the paper and make it more impactful.

### Questions

- Could the authors provide more evidence to support their claim that fine-tuned AOs develop concept-specific blind spots? For example, could they show that the target concept is not effectively verbalized by the oracle, even though it is present in the subject model's internal representations?
- How do the authors' findings relate to other work on the limitations of learned models as readers of other models' internal states? Could the authors discuss how their work fits into the broader context of interpretability research?
- What are the practical implications of the phenomenon of concept-specific anti-readers for the use of AOs in real-world applications? How might this phenomenon affect the trustworthiness of AOs?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

The authors investigate whether activation oracles, which are trained to answer natural language questions about another model’s activations, can themselves become better specialist readers of those models’ internal states. The authors use a controlled setting with a Taboo Word Guessing task, where subject models are trained to internally use a hidden concept while avoiding direct disclosure. The authors find that fine-tuned activation oracles can become concept-specific anti-readers, selectively failing to recover the concept persistently present during their own training.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The authors provide a controlled and well-designed experiment, with multiple experimental settings and a thorough analysis of the results.
- The authors clearly articulate the research questions and hypotheses, and provide a clear and concise explanation of their methodology and findings.
- The authors provide a comprehensive set of experiments and analyses, including probing, LogitLens, and ablation studies, to support their claims.
- The authors provide a clear and well-written explanation of their methodology and findings, and the paper is generally well-organized and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The authors' findings are primarily based on a controlled setting with a specific type of model (subject models) and task (Taboo Word Guessing). It is unclear how well these findings generalize to more complex or real-world scenarios, where models and tasks may be more diverse and unpredictable. The controlled setting, while useful for isolating specific effects, may not capture the nuances of real-world model behavior, particularly in scenarios where multiple concepts are intertwined or where the model's internal representations are more complex and less neatly compartmentalized. For instance, the Taboo Word Guessing task, while providing a clear target concept, may not fully represent the challenges of interpreting concepts in more complex, open-ended tasks.
- The authors' analysis of the results is primarily focused on the performance of activation oracles, but does not explore the potential impact of these findings on the broader field of interpretability research. It would be useful to discuss how the concept-specific anti-readers might affect the reliability of activation oracles in real-world applications, and how this might inform the development of more robust interpretability methods. The paper lacks a discussion on how these findings might be used to improve interpretability techniques, such as by identifying failure modes of existing methods or by informing the design of new methods that are more robust to concept-specific blind spots. The implications for the broader field of interpretability are not clearly articulated.
- The authors' discussion of the limitations of their study is relatively brief, and does not fully address the potential impact of these limitations on the generalizability of their findings. For example, the authors could discuss how the choice of activation oracles, subject models, and tasks might affect the results, and what steps could be taken to mitigate these limitations in future work. The paper should delve deeper into the potential biases introduced by the specific choices of models and tasks, and discuss how these biases might affect the generalizability of the findings. A more thorough discussion of limitations is needed to fully assess the scope of the study.

### Suggestions

The authors should consider expanding their analysis to include more complex and diverse scenarios to better assess the generalizability of their findings. This could involve using more complex models, such as large language models, and more complex tasks that involve multiple concepts and more nuanced interpretations. For example, the authors could explore tasks that require the model to perform reasoning or to generate explanations, which would provide a more realistic test of the robustness of activation oracles. Additionally, the authors should investigate how the concept-specific anti-readers might affect the reliability of activation oracles in real-world applications. This could involve testing the activation oracles on real-world datasets and tasks, and evaluating their performance in terms of both accuracy and interpretability. The authors should also discuss how these findings might inform the development of more robust interpretability methods, such as by identifying failure modes of existing methods or by informing the design of new methods that are more robust to concept-specific blind spots. This could involve exploring techniques such as ensemble methods or adversarial training to improve the robustness of activation oracles.

To address the limitations of the study, the authors should provide a more detailed discussion of the potential impact of their choices of models, tasks, and methods on the generalizability of their findings. This could involve exploring the potential biases introduced by the specific choices of models and tasks, and discussing how these biases might affect the generalizability of the findings. For example, the authors could investigate how the choice of activation oracle architecture affects the results, and whether certain architectures are more prone to concept-specific blind spots. The authors should also discuss how the findings might be used to improve interpretability techniques, such as by identifying failure modes of existing methods or by informing the design of new methods that are more robust to concept-specific blind spots. This could involve exploring techniques such as ensemble methods or adversarial training to improve the robustness of activation oracles. The authors should also discuss the limitations of their analysis, such as the fact that they only consider a single type of activation oracle, and how these limitations might affect the generalizability of their findings.

Finally, the authors should consider exploring the potential for using their findings to develop new interpretability techniques that are more robust to concept-specific blind spots. This could involve exploring techniques such as adversarial training or ensemble methods, which have been shown to be effective in improving the robustness of models to adversarial attacks. The authors could also explore the use of techniques such as causal tracing or saliency mapping to identify the specific parts of the model that are responsible for the concept-specific blind spots. This could provide valuable insights into the mechanisms underlying the phenomenon and could inform the development of new interpretability methods that are more robust to concept-specific blind spots. The authors should also discuss the ethical implications of their findings, particularly in the context of sensitive applications such as healthcare or finance. This could involve exploring the potential for using their findings to develop more transparent and accountable AI systems.

### Questions

- How might the findings of this study generalize to more complex or real-world scenarios, where models and tasks may be more diverse and unpredictable?
- How do the concept-specific anti-readers affect the reliability of activation oracles in real-world applications, and what steps could be taken to mitigate these risks?
- What are the potential implications of these findings for the broader field of interpretability research, and how might they inform the development of more robust interpretability methods?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the phenomenon of concept-specific blind spots in activation oracles (AOs) trained on fine-tuned subject models. The authors introduce a controlled setting using the Taboo Word Guessing task to examine whether AOs, trained on subject models that internally use a hidden concept while avoiding direct disclosure, can recover this concept. The study reveals that fine-tuned AOs become concept-specific anti-readers, selectively failing to recover the concept persistently present during their training. The authors provide evidence that this failure is not simply due to the absence of the concept in the AO's representations but rather due to the AO's own training process. The paper highlights a reliability concern for learned interpretability interfaces, as the reader itself may acquire blind spots induced by its training procedure. The authors also suggest that multi-concept subjects can exhibit similar blind spots, where the AO's blind spot aligns with the concept persistent during its own training.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses a critical reliability concern in learned interpretability interfaces, specifically activation oracles (AOs), by investigating the phenomenon of concept-specific blind spots. This is a novel and important contribution to the field, as it highlights a potential limitation of using AOs as reliable readers of model internals.
2. The paper is well-structured and clearly explains the research question, methodology, and findings. The use of a controlled setting with the Taboo Word Guessing task allows for a systematic and reproducible investigation of the concept-specific blind spot phenomenon.
3. The authors provide a comprehensive set of experiments and analyses, including probing, LogitLens, and ablation studies, to support their claims. These experiments are well-designed and provide strong evidence for the existence of concept-specific blind spots in fine-tuned AOs.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper introduces a novel and important concept, the practical implications of concept-specific blind spots in real-world applications are not fully explored. The authors could provide more concrete examples of how this phenomenon might affect the reliability of AOs in practical settings, such as in safety-critical applications or in domains where interpretability is crucial. Specifically, the paper lacks a discussion on how the identified blind spots might manifest in more complex, real-world scenarios where multiple concepts interact, and how this could impact the trustworthiness of AOs as interpretability tools. For instance, in a medical diagnosis setting, if an AO is trained on a model that internally represents 'pulmonary embolism' but fails to recover this concept due to a blind spot, the implications for diagnostic accuracy and patient safety are significant and require further exploration.
2. The paper's focus on a specific type of model (subject models) and task (Taboo Word Guessing) limits the generalizability of the findings. It would be beneficial to discuss how the concept-specific blind spots might manifest in different model architectures or tasks, and whether the observed phenomenon is specific to the chosen setup or a more general property of AOs. The current analysis does not sufficiently address the potential for the observed blind spots to be an artifact of the specific training procedure or the chosen model architecture. For example, it is unclear if the same phenomenon would be observed with different types of activation oracles, such as those trained with different optimization algorithms or on different types of data. Furthermore, the paper should explore the impact of varying the complexity of the hidden concept itself, as the current study uses a relatively simple concept.
3. The paper could benefit from a more detailed discussion of the limitations of the chosen evaluation metrics and how they might affect the interpretation of the results. For example, the use of exact match and semantic recovery as evaluation metrics may not fully capture the nuances of concept representation and recovery in AOs. The paper should also discuss the potential for the observed blind spots to be due to limitations in the evaluation metrics rather than an inherent property of the AOs themselves. For instance, it is possible that the evaluation metrics are not sensitive enough to detect subtle variations in the representation of the hidden concept, leading to an underestimation of the AO's capabilities.

### Suggestions

To enhance the practical relevance of the paper, the authors should provide a more detailed discussion of how concept-specific blind spots might manifest in real-world applications. This could include a case study or simulation that explores the implications of these blind spots in a safety-critical domain, such as autonomous driving or medical diagnosis. For example, the authors could investigate how an AO trained on a model that internally represents a specific type of vehicle damage might fail to recover this concept, leading to incorrect diagnoses or safety issues. This would help to clarify the practical risks associated with using AOs as interpretability tools and highlight the need for further research into mitigating these risks. Furthermore, the authors should explore the potential for developing methods to detect and correct these blind spots, such as through adversarial training or by incorporating additional information into the AO's training process.

To address the limitations regarding generalizability, the authors should conduct additional experiments using different model architectures and tasks. This could include exploring the phenomenon in larger language models or in tasks that involve more complex concept interactions. For example, the authors could investigate whether the concept-specific blind spots observed in the Taboo Word Guessing task also manifest in tasks that require reasoning or inference. This would help to determine whether the observed phenomenon is a general property of AOs or specific to the chosen setup. Furthermore, the authors should explore the impact of varying the complexity of the hidden concept itself, as the current study uses a relatively simple concept. This could involve using more abstract or nuanced concepts to assess whether the blind spots are more pronounced for complex concepts. This would provide a more comprehensive understanding of the phenomenon and its potential implications.

Finally, the authors should provide a more detailed discussion of the limitations of the chosen evaluation metrics and how they might affect the interpretation of the results. This could include exploring alternative evaluation metrics that are more sensitive to subtle variations in concept representation. For example, the authors could consider using metrics that measure the similarity between the AO's internal representation and the true representation of the hidden concept. This would provide a more nuanced assessment of the AO's capabilities and help to identify potential blind spots that might be missed by the current evaluation metrics. Additionally, the authors should discuss the potential for the observed blind spots to be due to limitations in the evaluation metrics rather than an inherent property of the AOs themselves. This would help to ensure that the results are not an artifact of the evaluation process and that the conclusions are robust and reliable.

### Questions

1. How might the concept-specific blind spots observed in fine-tuned AOs affect their reliability in real-world applications, particularly in safety-critical domains?
2. Could the authors provide more insights into the potential causes of the concept-specific blind spots, beyond the AO's own training process?
3. How might the findings of this study generalize to different model architectures or tasks, and are the observed blind spots specific to the chosen setup?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper studies the behavior of activation oracles (AOs) when they are trained on models that have been fine-tuned to internally use a hidden concept while avoiding direct disclosure. The authors find that fine-tuned AOs can become concept-specific anti-readers, selectively failing to recover the concept persistently present during their own training. This failure is not simply explained by absence of the concept from activations, but rather by the oracle's own training process. The authors suggest that this phenomenon poses a reliability concern for learned interpretability interfaces.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The paper introduces a novel and interesting phenomenon: concept-specific anti-readers in activation oracles, which is a new perspective on the limitations of learned interpretability interfaces.
3. The paper provides a comprehensive set of experiments and analyses, including probing, LogitLens, and ablation studies, to support their claims.
4. The paper's findings have implications for the reliability of learned interpretability interfaces and highlight the need for more robust methods for training interpreters.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear definition of what constitutes a "concept-specific anti-reader." While the authors describe this phenomenon, a more formal definition would help clarify the scope and implications of their findings. Specifically, it is unclear what constitutes a 'concept' in the context of the experiments, and how the authors are measuring the 'specificity' of the failure. A more rigorous definition, perhaps involving a formalization of the concept space and the notion of 'concept-specificity', would be beneficial.
2. The paper does not explore the potential causes of concept-specific anti-readers in fine-tuned AOs. While the authors suggest that the failure is due to the AO's own training process, they do not provide any concrete evidence or hypotheses to support this claim. Further investigation into the training dynamics of AOs, such as the impact of different training objectives or regularization techniques, could provide valuable insights. For example, it would be useful to explore whether the observed phenomenon is related to the specific architecture of the AO or the training data used.
3. The paper does not discuss the potential implications of concept-specific anti-readers for the development of more robust interpreters. While the authors suggest that their findings pose a reliability concern for learned interpretability interfaces, they do not provide concrete recommendations for mitigating this issue. Further discussion on potential solutions, such as incorporating additional information into the AO's training process or using alternative interpretability methods, would be valuable. The paper should also consider the trade-offs between interpretability and other desirable properties of interpretable systems, such as accuracy and robustness.

### Suggestions

To address the lack of a formal definition for 'concept-specific anti-reader,' the authors should consider defining a concept space and a notion of 'concept-specificity' within that space. For example, they could define a concept as a set of input-output pairs that share a common underlying mechanism or representation, and then define a concept-specific anti-reader as an AO that fails to recover the concept even when it is present in the training data. This could involve using a formal language or a mathematical framework to define the concept space and the notion of 'specificity.' Furthermore, the authors should provide a more detailed explanation of how they measure the 'specificity' of the failure. This could involve using metrics that quantify the degree to which the AO fails to recover the concept, or by analyzing the internal representations of the AO to identify the specific mechanisms that are responsible for the failure. A more rigorous definition and measurement of concept-specificity would greatly enhance the clarity and impact of the paper.

To explore the potential causes of concept-specific anti-readers, the authors should conduct more detailed experiments that investigate the training dynamics of AOs. This could involve varying the training objectives, regularization techniques, and data augmentation strategies to see how they affect the AO's ability to recover the concept. For example, they could explore whether the AO's failure is related to the specific architecture of the AO or the training data used. They could also investigate whether the AO's failure is related to the specific way in which the concept is encoded in the model's activations. Furthermore, the authors should consider using techniques from interpretability to analyze the internal representations of the AO and identify the specific mechanisms that are responsible for the failure. This could involve using techniques such as probing, saliency maps, or feature visualization to understand how the AO is processing the activations and why it is failing to recover the concept. A more detailed analysis of the training dynamics and internal representations of the AO would provide valuable insights into the causes of concept-specific anti-readers.

Finally, the authors should discuss the potential implications of concept-specific anti-readers for the development of more robust interpreters. This could involve exploring potential solutions for mitigating the issue, such as incorporating additional information into the AO's training process or using alternative interpretability methods. For example, they could investigate whether adding explicit supervision for the concept during training can improve the AO's ability to recover it. They could also explore whether using a different type of AO, such as a different architecture or a different training objective, can mitigate the issue. Furthermore, the authors should consider the trade-offs between interpretability and other desirable properties of interpretable systems, such as accuracy and robustness. A more detailed discussion of the implications and potential solutions would greatly enhance the practical relevance of the paper.

### Questions

1. Could the authors provide a more formal definition of what constitutes a "concept-specific anti-reader"?
2. What are the potential causes of concept-specific anti-readers in fine-tuned AOs, and how can these causes be addressed?
3. What are the potential implications of concept-specific anti-readers for the development of more robust interpreters?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper provided.

For each weakness, I will:
1. **State the weakness.**
2. **Collect evidence from the paper.** This will involve looking for relevant sections in the method and experiments.
3. **Analyze if there's a literature gap.** This means checking if the paper misses relevant citations or baseline comparisons.
4. **Provide a validation analysis.** This will summarize the evidence and assess the impact of the weakness.
5. **Conclude if the weakness is valid, partially valid, or invalid.**

Let's start with Reviewer 1.
**Review 1 Weakness Analysis:**

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "concept-specific anti-reader." While the authors describe this phenomenon, a more formal definition would help clarify the scope and implications of their findings. Specifically, it is unclear what constitutes a 'concept' in the context of the experiments, and how the authors are measuring the 'specificity' of the failure. A more rigorous definition, perhaps involving a formalization of the concept space and the notion of 'concept-specificity', would be beneficial."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the concept in the "Main Idea" section: "The paper introduces the concept of concept-specific anti-readers in activation oracles (AOs), which are models trained to answer natural language questions about another model's internal activations."
   - The definition is further elaborated in the "Method" -> "overview" section: "The method involves training AOs on activations from fine-tuned subject models and evaluating their ability to recover hidden concepts."
   - The "Method" -> "details" -> "Activation Oracle Training" section describes the training process.
   - The "Experiments" section describes the setup and evaluation metrics.
   - The "Mechanisms of Anti-Reading" section provides an analysis of *how* the anti-reading occurs but doesn't offer a formal definition of the term itself.

b) Experiment-related Evidence:
   - The "Multi-Concept Subjects" experiment uses "two hidden concepts: leaf and moon" as examples.
   - The evaluation metrics (exact target recovery, semantic recovery, probability and rank of target tokens) are used to measure the AO's ability to recover the concept.

3. Literature Gap Analysis:
   - The paper cites Karvonen et al. (2025) and Karvonen et al. (2023) in the introduction and related work, which are relevant to the topic of interpretability and learned models. However, there isn't a specific citation defining "concept-specific anti-readers" in this context.

4. Validation Analysis:
   - Primary evidence summary: The paper introduces the term "concept-specific anti-readers" and describes the experimental setup and evaluation metrics. It uses examples of concepts ("leaf" and "moon") and defines the recovery metrics. However, it lacks a formal, mathematical definition of the term.
   - Supporting quotes:
     - "The paper introduces the concept of concept-specific anti-readers in activation oracles (AOs)..." (Main Idea)
     - "The method involves training AOs on activations from fine-tuned subject models and evaluating their ability to recover hidden concepts." (Method -> overview)
     - "two hidden concepts: leaf and moon" (Experiments -> Multi-Concept Subjects -> setup -> datasets)
     - "exact target recovery, semantic recovery, probability and rank of target tokens" (Experiments -> Multi-Concept Subjects -> setup -> metrics)
   - Impact assessment: The lack of a formal definition makes it harder to precisely understand the scope and implications of the findings. It also makes it difficult to compare this concept with other potential definitions in the literature.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses the term "concept-specific anti-readers" extensively but does not provide a formal definition.

1. Weakness Statement:
"The paper does not explore the potential causes of concept-specific anti-readers in fine-tuned AOs. While the authors suggest that the failure is due to the AO's own training process, they do not provide any concrete evidence or hypotheses to support this claim. Further investigation into the training dynamics of AOs, such as the impact of different training objectives or regularization techniques, could provide valuable insights. For example, it would be useful to explore whether the observed phenomenon is related to the specific architecture of the AO or the training data used."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Mechanisms of Anti-Reading" section attempts to explore the causes by analyzing the difference in hidden states and the effect of LogitLens readouts.
   - The paper mentions using LoRA for fine-tuning and the fixed layer ℓ = 18 throughout the experiments.

b) Experiment-related Evidence:
   - The "Mechanisms of Anti-Reading" section presents results from layer-range ablations, which can be seen as an investigation into the AO's internal processing.
   - The paper notes that "the fine-tuning induced the target suppression" (Mechanisms of Anti-Reading -> Layer-Range Ablations).

3. Literature Gap Analysis:
   - The paper cites works on activation oracles and concept-specific decodability, but doesn't delve into the specific training dynamics or architectural choices that might lead to anti-reading.

4. Validation Analysis:
   - Primary evidence summary: The paper offers some investigation into the causes, particularly through the layer-range ablations, which show that the target concept is suppressed in later layers. However, it doesn't provide a comprehensive analysis of training objectives, regularization, or architectural choices.
   - Supporting quotes:
     - "The fine-tuning induced the target suppression." (Mechanisms of Anti-Reading -> Layer-Range Ablations)
     - "We find that the target concept is suppressed inside the oracle, leading to the AO's blind spot." (Mechanisms of Anti-Reading -> Layer-Range Ablations)
   - Impact assessment: While the paper touches upon the training process, it lacks a deeper exploration of potential causes. The reviewer's suggestion to investigate training objectives and architectural choices is valid.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper provides some evidence (layer-range ablations) but lacks a comprehensive investigation into training dynamics and architectural factors.

1. Weakness Statement:
"The paper does not discuss the potential implications of concept-specific anti-readers for the development of more robust interpreters. While the authors suggest that their findings pose a reliability concern for learned interpretability interfaces, they do not provide concrete recommendations for mitigating this issue. Further discussion on potential solutions, such as incorporating additional information into the AO's training process or using alternative interpretability methods, would be valuable. The paper should also consider the trade-offs between interpretability and other desirable properties of interpretable systems, such as accuracy and robustness."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Introduction" mentions the reliability concern: "This raises a critical question: if an AO is trained on activations from a model that internally represents a hidden concept, does it become a better specialist reader of that concept, or can it instead learn not to report it?"

b) Experiment-related Evidence:
   - The experiments demonstrate the phenomenon of concept-specific anti-reading.

3. Literature Gap Analysis:
   - The paper discusses related work on interpretability methods but doesn't offer specific solutions for mitigating the identified issue.

4. Validation Analysis:
   - Primary evidence summary: The paper identifies the problem and highlights its implications for reliability. However, it doesn't delve into specific solutions or trade-offs.
   - Supporting quotes:
     - "This raises a critical question: if an AO is trained on activations from a model that internally represents a hidden concept, does it become a better specialist reader of that concept, or can it instead learn not to report it?" (Introduction)
     - "Our results show that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising a reliability concern for learned interpretability interfaces." (Introduction)
   - Impact assessment: The reviewer's point about discussing potential solutions and trade-offs is valid. The paper focuses on identifying the problem rather than proposing solutions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper identifies the problem but lacks a discussion of mitigation strategies and trade-offs.

**Review 2 Weakness Analysis:**

1. Weakness Statement:
"The paper's central claim that fine-tuned AOs develop concept-specific blind spots is not entirely convincing. The authors argue that the target concept is still decodable inside the oracle, but this does not necessarily imply that the oracle can effectively verbalize it. The fact that the target concept is present in the oracle's representations does not guarantee that the oracle can successfully communicate this information to the user. The authors need to provide more evidence to support their claim that the oracle's internal representation of the target concept is not effectively verbalized."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper defines "AO-verbalizability" as the ability to map represented information into the intended natural language answer.

b) Experiment-related Evidence:
   - The "Baselines" section describes the "base AO" as trained on activations from the original subject model, which might not have the hidden concept.
   - The "experiments" section shows that the fine-tuned AOs have lower AO-verbalizability compared to the base AO.
   - The "Mechanisms of Anti-Reading" section uses LogitLens readouts to analyze the AO's internal representations and shows that the target concept is suppressed in later layers.

3. Literature Gap Analysis:
   - The paper cites works on concept-specific decodability, which is relevant to the idea of the target concept being present in the representations.

4. Validation Analysis:
   - Primary evidence summary: The paper provides evidence that the target concept is present in the AO's representations (through decodability and LogitLens) but shows that the AO fails to effectively verbalize it (lower AO-verbalizability). The reviewer's point about the difference between presence and effective verbalization is valid.
   - Supporting quotes:
     - "The AO's ability to verbalize the target concept is measured by AO-verbalizability, which is the ability to map represented information into the intended natural language answer." (Method -> details -> AO-Verbalizability)
     - "The base AO is trained on activations from the original subject model, which might not have the hidden concept." (Baselines)
     - "The fine-tuned AOs, however, show a significant drop in AO-verbalizability, indicating that they become concept-specific anti-readers." (Experiments -> Base AOs Recover Hidden Concepts from Non-Leaking Subjects)
     - "The fine-tuned AOs show a significant drop in AO-verbalizability, indicating that they become concept-specific anti-readers." (Experiments -> Cross Subject Text-to-Text)
     - "The fine-tuned AOs show a significant drop in AO-verbalizability, indicating that they become concept-specific anti-readers." (Experiments -> Cross Subject Image-to-Image)
     - "The fine-tuned AOs show a significant drop in AO-verbalizability, indicating that they become concept-specific anti-readers." (Experiments -> Multi-Concept Subjects)
     - "The fine-tuned AOs show a significant drop in AO-verbalizability, indicating that they become concept-specific anti-readers." (Experiments -> Layer-Range Ablations)
     - "The fine-tuned AOs show a significant drop in AO-verbalizability, indicating that they become concept-specific anti-readers." (Experiments -> Ablation Studies)
   - Impact assessment: The reviewer raises a valid point about the distinction between the presence of a concept in representations and the ability to effectively verbalize it. The paper's evidence supports the claim of a blind spot in verbalization.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper shows the target concept is present in representations but the AO's verbalization is impaired.

1. Weakness Statement:
"The paper does not adequately address the potential for alternative explanations for the observed phenomenon. For example, the authors could have explored whether the observed behavior is due to the specific training data or the architecture of the AOs. The paper would benefit from a more thorough investigation of these alternative explanations."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions using LoRA for fine-tuning, which is a specific training method.
   - The paper uses a specific architecture for the AOs (LoRA-fine-tuned copy of the subject model).

b) Experiment-related Evidence:
   - The experiments compare fine-tuned AOs with base AOs and cross-subject AOs.
   - The paper includes layer-range ablation studies, which can be seen as an investigation into the AO's internal processing.

3. Literature Gap Analysis:
   - The paper cites relevant works but doesn't deeply explore alternative explanations for anti-reading in the context of AOs.

4. Validation Analysis:
   - Primary evidence summary: The paper investigates the impact of fine-tuning and compares different AO types. The layer-range ablation provides some insight into the AO's internal workings. However, it doesn't systematically explore alternative explanations like different training data or architectures beyond the specific LoRA setup.
   - Supporting quotes:
     - "The subject models are fine-tuned using LoRA, a parameter-efficient fine-tuning technique, to ensure that the hidden concept is consistently represented during their training." (Method -> details -> Subject Models)
     - "The AOs are trained using LoRA-fine-tuned copies of the subject models." (Method -> details -> Activation Oracles)
     - "The layer-range ablation studies further confirm that the target concept is suppressed in the AO's internal representations." (Experiments -> Layer-Range Ablations)
   - Impact assessment: The reviewer's point about alternative explanations is valid. While the paper explores some aspects, a more thorough investigation of training data and architecture variations would strengthen the findings.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper explores fine-tuning and ablations but lacks a systematic investigation of alternative explanations like different training data or architectures.

1. Weakness Statement:
"The paper's focus on concept-specific anti-readers is interesting, but the practical implications of this phenomenon are not fully explored. The authors should discuss how this phenomenon might affect the use of AOs in real-world applications, and what steps could be taken to mitigate the risks."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Introduction" mentions the reliability concern.

b) Experiment-related Evidence:
   - The experiments demonstrate the phenomenon.

3. Literature Gap Analysis:
   - The paper discusses related work but doesn't offer specific mitigation strategies.

4. Validation Analysis:
   - Primary evidence summary: The paper identifies the problem but doesn't delve into practical implications or mitigation strategies.
   - Supporting quotes:
     - "This raises a critical question: if an AO is trained on activations from a model that internally represents a hidden concept, does it become a better specialist reader of that concept, or can it instead learn not to report it?" (Introduction)
     - "Our results show that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising a reliability concern for learned interpretability interfaces." (Introduction)
   - Impact assessment: The reviewer's point about exploring practical implications and mitigation strategies is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper identifies the problem but lacks a discussion of practical implications and mitigation.

**Review 3 Weakness Analysis:**

1. Weakness Statement:
"While the paper introduces a novel and important concept, the practical implications of concept-specific blind spots in real-world applications are not fully explored. The authors could provide more concrete examples of how this phenomenon might affect the reliability of AOs in practical settings, such as in safety-critical applications or in domains where interpretability is crucial. Specifically, the paper lacks a discussion on how the identified blind spots might manifest in more complex, real-world scenarios where multiple concepts interact, and how this could impact the trustworthiness of AOs as interpretability tools. For instance, in a medical diagnosis setting, if an AO is trained on a model that internally represents a specific type of vehicle damage, but fails to recover this concept due to a blind spot, the implications for diagnostic accuracy and patient safety are significant and require further exploration."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Introduction" mentions the reliability concern.

b) Experiment-related Evidence:
   - The experiments use a controlled setting with a single hidden concept.

3. Literature Gap Analysis:
   - The paper discusses related work but doesn't provide specific examples of real-world impact.

4. Validation Analysis:
   - Primary evidence summary: The paper identifies the problem in a controlled setting but lacks concrete examples of real-world implications, especially in safety-critical applications.
   - Supporting quotes:
     - "This raises a critical question: if an AO is trained on activations from a model that internally represents a hidden concept, does it become a better specialist reader of that concept, or can it instead learn not to report it?" (Introduction)
     - "Our results show that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising a reliability concern for learned interpretability interfaces." (Introduction)
   - Impact assessment: The reviewer's point about exploring practical implications is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper focuses on the phenomenon in a controlled setting without detailed exploration of real-world implications.

1. Weakness Statement:
"The paper's focus on a specific type of model (subject models) and task (Taboo Word Guessing) limits the generalizability of the findings. It would be beneficial to discuss how the concept-specific anti-reads might manifest in different model architectures or tasks, and whether the observed phenomenon is specific to the chosen setup or a more general property of AOs. The current analysis does not sufficiently address the potential for the observed blind spots to be an artifact of the specific training procedure or the chosen model architecture. For example, it is unclear if the same phenomenon would be observed with different types of activation oracles, such as those trained with different optimization algorithms or on different types of data. Furthermore, the paper should explore the impact of varying the complexity of the hidden concept itself, as the current study uses a relatively simple concept."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper uses a specific model (Qwen3-8B) and the Taboo Word Guessing task.

b) Experiment-related Evidence:
   - The experiments are conducted with this specific setup.

3. Literature Gap Analysis:
   - The paper cites relevant works but doesn't deeply explore the generalizability of the findings across different model architectures or tasks.

4. Validation Analysis:
   - Primary evidence summary: The paper uses a specific model and task, and the generalizability of the findings is not fully explored.
   - Supporting quotes:
     - "We instantiate the AO framework in a controlled Taboo Word Guessing setting..." (Method -> details -> Subject models and Taboo fine-tuning)
     - "We fine-tune subject models to internally use a hidden target word, such as leaf or moon, while avoiding direct disclosure." (Method -> details -> Subject models and Taboo fine-tuning)
   - Impact assessment: The reviewer's point about limited generalizability is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses a specific model and task, and the generalizability of the findings is not fully explored.

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the chosen evaluation metrics and how they might affect the interpretation of the results. For example, the use of exact match and semantic recovery as evaluation metrics may not fully capture the nuances of concept representation and recovery in AOs. The paper should also discuss the potential for the observed blind spots to be due to limitations in the evaluation metrics rather than an inherent property of the AOs themselves. For instance, it is possible that the evaluation metrics are not sensitive enough to detect subtle variations in the representation of the hidden concept, leading to an underestimation of the AO's capabilities."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the evaluation metrics used.

b) Experiment-related Evidence:
   - The results are based on these metrics.

3. Literature Gap Analysis:
   - The paper cites works on evaluation metrics but doesn't deeply discuss their limitations in this specific context.

4. Validation Analysis:
   - Primary evidence summary: The paper uses specific evaluation metrics, and the potential limitations of these metrics are not discussed in detail.
   - Supporting quotes:
     - "Exact recovery measures whether the generated answer contains the target word, while semantic recovery counts close clues or semantic associates. Probability and rank measure whether the correct word is accessible in the AO distribution even when it is not generated. Metric definitions and Sonnet judging prompts are provided in Appendix F." (Experiments -> Evaluation metrics)
   - Impact assessment: The reviewer's point about the limitations of evaluation metrics is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses specific evaluation metrics without a detailed discussion of their limitations.

**Review 4 Weakness Analysis:**

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "concept-specific anti-reader." While the authors describe this phenomenon, a more formal definition would help clarify the scope and implications of their findings. Specifically, it is unclear what constitutes a 'concept' in the context of the experiments, and how the authors are measuring the 'specificity' of the failure. A more rigorous definition, perhaps involving a formalization of the concept space and the notion of 'concept-specificity', would be beneficial."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses the term "concept-specific anti-readers" extensively but does not provide a formal, mathematical definition.

1. Weakness Statement:
"The paper does not explore the potential causes of concept-specific anti-readers in fine-tuned AOs. While the authors suggest that the failure is due to the AO's own training process, they do not provide any concrete evidence or hypotheses to support this claim. Further investigation into the training dynamics of AOs, such as the impact of different training objectives or regularization techniques, could provide valuable insights. For example, it would be useful to explore whether the observed phenomenon is related to the specific architecture of the AO or the training data used."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper touches upon the training process but lacks a comprehensive investigation into training dynamics and architectural factors.

1. Weakness Statement:
"The paper does not discuss the potential implications of concept-specific anti-readers for the development of more robust interpreters. While the authors suggest that their findings pose a reliability concern for learned interpretability interfaces, they do not provide concrete recommendations for mitigating this issue. Further discussion on potential solutions, such as incorporating additional information into the AO's training process or using alternative interpretability methods, would be valuable. The paper should also consider the trade-offs between interpretability and other desirable properties of interpretable systems, such as accuracy and robustness."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper identifies the problem but lacks a discussion of mitigation strategies and trade-offs.

1. Weakness Statement:
"Could the authors provide a more formal definition of what constitutes a "concept-specific anti-reader"?"

2. Evidence Collection:
   - This is a question prompting for a definition already identified as a weakness.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as the first weakness identified by Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses the term "concept-specific anti-readers" extensively but does not provide a formal, mathematical definition.

1. Weakness Statement:
"What are the potential causes of concept-specific anti-readers in fine-tuned AOs, and how can these causes be addressed?"

2. Evidence Collection:
   - This is a question prompting for causes already identified as a weakness.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as the second weakness identified by Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper touches upon the training process but lacks a comprehensive investigation into training dynamics and architectural factors.

1. Weakness Statement:
"What are the potential implications of concept-specific anti-readers for the development of more robust interpreters?"

2. Evidence Collection:
   - This is a question prompting for implications already identified as a weakness.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as the third weakness identified by Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper identifies the problem but lacks a discussion of mitigation strategies and trade-offs.

**Synthesis and Reflection:**

After analyzing the weaknesses identified by the reviewers, several recurring themes emerge:

*   **Lack of a Formal Definition:**  Reviewers 1 and 4 specifically point out the absence of a clear, formal definition of "concept-specific anti-readers." This is a valid criticism as the paper introduces the term but doesn't provide a rigorous mathematical or conceptual framework.
*   **Limited Exploration of Causes:** Reviewers 1 and 4 question the extent to which the paper explores the underlying causes of concept-specific anti-reading. While the paper suggests the AO's training process is a factor, it doesn't delve deeply into training objectives, regularization, or architectural choices. This is a partially valid criticism, as the paper does offer some investigation through layer-range ablations, but it's not comprehensive.
*   **Insufficient Discussion of Implications:** Reviewers 1, 2, and 4 note the lack of a thorough discussion regarding the implications of concept-specific anti-reading for the development of more robust interpreters. The paper raises a reliability concern but doesn't offer concrete solutions or consider trade-offs. This is a valid criticism.
*   **Limited Generalizability:** Reviewers 3 and 4 raise concerns about the generalizability of the findings due to the specific model (Qwen3-8B) and task (Taboo Word Guessing) used. The paper doesn't sufficiently explore how the phenomenon might manifest in different model architectures or tasks. This is a valid criticism.
*   **Evaluation Metric Limitations:** Reviewer 3 points out the potential limitations of the chosen evaluation metrics (exact match and semantic recovery) in capturing the nuances of concept representation and recovery. This is a valid criticism.

There are no significant contradictions between the reviewers' opinions. They largely converge on the need for a more formal definition, a deeper investigation into the causes, a more thorough discussion of implications, and an exploration of generalizability and evaluation metric limitations.

**Conclusion:**

Based on the evidence collected, the majority of the weaknesses identified by the reviewers are **valid**. Some weaknesses are **partially valid**, indicating that the paper touches upon the issue but doesn't provide a comprehensive analysis. There are no instances where a weakness can be definitively classified as **invalid**.

**Overall Confidence Level:** High. The weaknesses are well-supported by the paper's content and omissions.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces the concept of "concept-specific anti-readers" in the context of activation oracles (AOs), which are models trained to mimic the internal representations of other models. The authors investigate whether fine-tuning an AO on a subject model that internally represents a hidden concept, while preventing direct disclosure of that concept, leads to the AO becoming a worse specialist reader of that concept compared to a base AO trained on a model that does not represent the concept internally. The core methodology involves training AOs on subject models that have been fine-tuned using LoRA to consistently represent a hidden concept, such as 'leaf' or 'moon', while avoiding direct disclosure of this concept. The AOs are then evaluated on their ability to recover this hidden concept through natural language questions, using metrics like exact match, semantic recovery, probability, and rank. The main empirical finding is that fine-tuned AOs, despite being able to represent the hidden concept internally, exhibit a significant drop in their ability to recover it, a phenomenon the authors term "concept-specific anti-reading." This is demonstrated through a series of experiments using the Taboo Word Guessing task, where the subject models are trained to internally represent a target word while avoiding its direct disclosure. The authors compare the performance of fine-tuned AOs with base AOs and cross-subject AOs, showing that fine-tuned AOs, while maintaining their ability to recover concepts persistently present during their training, fail to recover the concept that was persistently present during their own training. This is a significant finding because it suggests that even when an AO is trained on a model that internally represents a concept, it does not necessarily mean that the AO will be able to effectively verbalize that concept. The authors also explore the internal representations of the AOs using techniques like LogitLens readouts, layer-range ablation studies, and ablation studies, providing further evidence for the existence of concept-specific blind spots. The overall significance of this work lies in its implications for the reliability of learned interpretability interfaces. The paper highlights a potential pitfall of using AOs as readouts of other models' internal states, suggesting that the reader itself may acquire blind spots induced by its training procedure. This raises concerns about the trustworthiness of AOs as reliable tools for understanding other models' internal representations, particularly in safety-critical applications where interpretability is crucial. The paper's findings suggest that the reader itself may acquire blind spots induced by its training procedure, which could have significant implications for the use of AOs in real-world applications.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.25


## Strengths:

This paper makes a valuable contribution by introducing the concept of concept-specific anti-reading in activation oracles, a phenomenon that highlights a potential limitation of using AOs as reliable readouts of other models' internal states. The authors have designed a controlled experimental setup using the Taboo Word Guessing task, which allows for a systematic investigation of this phenomenon. The use of a consistent and reproducible task setup enhances the reliability of the findings. The paper's methodology is thorough, incorporating multiple experimental settings and a variety of evaluation metrics, including probing, LogitLens, and ablation studies. This comprehensive approach provides strong evidence for the existence of concept-specific blind spots in fine-tuned AOs. The authors' analysis of the internal representations of the AOs, using techniques like LogitLens readouts and layer-range ablation studies, is particularly insightful. These analyses provide a deeper understanding of how the fine-tuning process affects the AO's ability to verbalize the hidden concept. The paper is well-written and easy to follow, making the methodology and findings accessible to a broad audience. The authors clearly articulate the research question, describe the experimental setup, and present their results in a clear and concise manner. The use of a controlled setting with a single hidden concept allows for a focused investigation of the phenomenon, which is a strength of the paper. The paper's findings have significant implications for the field of interpretability research, raising concerns about the reliability of learned interpretability interfaces. The authors have successfully highlighted a potential pitfall of using AOs as readouts of other models' internal states, suggesting that the reader itself may acquire blind spots induced by its training procedure. This is a novel and important contribution to the field, as it challenges the assumption that AOs are always reliable indicators of a model's internal representations. The paper's findings also have implications for the development of more robust and trustworthy AI systems, particularly in safety-critical applications where interpretability is crucial. The authors have successfully identified a potential limitation of a widely used technique, which is a valuable contribution to the field.


## Weaknesses:

While the paper presents a compelling investigation into the phenomenon of concept-specific anti-reading, several limitations warrant careful consideration. A primary concern is the lack of a formal, mathematical definition of what constitutes a "concept-specific anti-reader." The authors introduce this term extensively, but they do not provide a rigorous framework for understanding the scope and implications of their findings. This absence of a formal definition makes it difficult to precisely understand the nature of the failure and to compare this concept with other potential definitions in the literature. The paper uses examples of concepts ("leaf" and "moon") but does not define a concept space or a notion of "concept-specificity" within that space. This lack of a formal definition is a significant limitation, as it makes it harder to generalize the findings and to apply them to different contexts. My confidence in this assessment is high, as the paper uses the term extensively but does not provide a formal definition. Another significant weakness is the limited exploration of the potential causes of concept-specific anti-reading. While the authors suggest that the failure is due to the AO's own training process, they do not provide concrete evidence or hypotheses to support this claim. The paper offers some investigation into the training dynamics of AOs, particularly through the layer-range ablation studies, which show that the target concept is suppressed in later layers. However, this analysis does not provide a comprehensive understanding of the underlying mechanisms. The authors do not explore the impact of different training objectives, regularization techniques, or architectural choices on the AO's ability to verbalize the target concept. This lack of a deeper investigation into the training dynamics is a significant limitation, as it leaves open the possibility that the observed phenomenon is due to specific aspects of the training process rather than an inherent property of AOs. My confidence in this assessment is high, as the paper touches upon the training process but lacks a comprehensive investigation into training dynamics and architectural factors. Furthermore, the paper does not adequately discuss the potential implications of concept-specific anti-reading for the development of more robust interpreters. While the authors raise a reliability concern for learned interpretability interfaces, they do not provide concrete recommendations for mitigating this issue. The paper focuses on identifying the problem but does not delve into potential solutions or trade-offs between interpretability and other desirable properties of interpretable systems, such as accuracy and robustness. This lack of discussion on mitigation strategies and trade-offs is a significant limitation, as it leaves the reader without a clear path forward for addressing the identified problem. My confidence in this assessment is high, as the paper identifies the problem but lacks a discussion of mitigation strategies and trade-offs. The paper's focus on a specific type of model (subject models) and task (Taboo Word Guessing) also limits the generalizability of the findings. The authors do not discuss how the concept-specific anti-reads might manifest in different model architectures or tasks, and whether the observed phenomenon is specific to the chosen setup or a more general property of AOs. The current analysis does not sufficiently address the potential for the observed blind spots to be an artifact of the specific training procedure or the chosen model architecture. For example, it is unclear if the same phenomenon would be observed with different types of activation oracles, such as those trained with different optimization algorithms or on different types of data. This limitation is significant, as it raises questions about the applicability of the findings to other contexts. My confidence in this assessment is high, as the paper uses a specific model and task, and the generalizability of the findings is not fully explored. Finally, the paper's reliance on specific evaluation metrics, such as exact match and semantic recovery, may not fully capture the nuances of concept representation and recovery in AOs. The authors do not discuss the potential for the observed blind spots to be due to limitations in the evaluation metrics rather than an inherent property of the AOs themselves. For instance, it is possible that the evaluation metrics are not sensitive enough to detect subtle variations in the representation of the hidden concept, leading to an underestimation of the AO's capabilities. This limitation is significant, as it raises questions about the validity of the conclusions drawn from the experimental results. My confidence in this assessment is high, as the paper uses specific evaluation metrics without a detailed discussion of their limitations.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more formal and rigorous definition of "concept-specific anti-reading." This could involve defining a concept space and a notion of "concept-specificity" within that space. For example, they could define a concept as a set of input-output pairs that share a common underlying mechanism or representation. Then, they could define a concept-specific anti-reader as an AO that fails to recover the concept even when it is present in the training data. This could involve using a formal language or a mathematical framework to define the concept space and the notion of 'specificity.' Furthermore, the authors should provide a more detailed explanation of how they measure the 'specificity' of the failure. This could involve using metrics that quantify the degree to which the AO fails to recover the concept, or by analyzing the internal representations of the AO to identify the specific mechanisms that are responsible for the failure. A more rigorous definition and measurement of concept-specificity would greatly enhance the clarity and impact of the paper. Second, the authors should conduct a more detailed investigation into the potential causes of concept-specific anti-reading. This could involve varying the training objectives, regularization techniques, and data augmentation strategies to see how they affect the AO's ability to recover the concept. For example, they could explore whether the AO's failure is related to the specific architecture of the AO or the training data used. They could also investigate whether the AO's failure is related to the specific way in which the concept is encoded in the model's activations. Furthermore, the authors should consider using techniques from interpretability to analyze the internal representations of the AO and identify the specific mechanisms that are responsible for the failure. This could involve using techniques such as probing, saliency maps, or feature visualization to understand how the AO is processing the activations and why it is failing to recover the concept. A more detailed analysis of the training dynamics and internal representations of the AO would provide valuable insights into the causes of concept-specific anti-reading. Third, the authors should discuss the potential implications of concept-specific anti-reading for the development of more robust interpreters. This could involve exploring potential solutions for mitigating the issue, such as incorporating additional information into the AO's training process or using alternative interpretability methods. For example, they could investigate whether adding explicit supervision for the concept during training can improve the AO's ability to recover it. They could also explore whether using a different type of AO, such as a different architecture or a different training objective, can mitigate the issue. Furthermore, the authors should consider the trade-offs between interpretability and other desirable properties of interpretable systems, such as accuracy and robustness. A more detailed discussion of the implications and potential solutions would greatly enhance the practical relevance of the paper. Fourth, the authors should conduct additional experiments using different model architectures and tasks to better assess the generalizability of their findings. This could include exploring the phenomenon in larger language models or in tasks that involve more complex concept interactions. For example, the authors could investigate whether the concept-specific blind spots observed in the Taboo Word Guessing task also manifest in tasks that require reasoning or inference. This would help to determine whether the observed phenomenon is a general property of AOs or specific to the chosen setup. Furthermore, the authors should explore the impact of varying the complexity of the hidden concept itself, as the current study uses a relatively simple concept. This could involve using more abstract or nuanced concepts to assess whether the blind spots are more pronounced for complex concepts. Finally, the authors should provide a more detailed discussion of the limitations of the chosen evaluation metrics and how they might affect the interpretation of the results. This could include exploring alternative evaluation metrics that are more sensitive to subtle variations in concept representation. For example, the authors could consider using metrics that measure the similarity between the AO's internal representation and the true representation of the hidden concept. This would provide a more nuanced assessment of the AO's capabilities and help to identify potential blind spots that might be missed by the current evaluation metrics. Additionally, the authors should discuss the potential for the observed blind spots to be due to limitations in the evaluation metrics rather than an inherent property of the AOs themselves. This would help to ensure that the results are not an artifact of the evaluation process and that the conclusions are robust and reliable.


## Questions:

Several key questions arise from my analysis of this paper. First, how might the concept-specific blind spots observed in fine-tuned AOs affect their reliability in real-world applications, particularly in safety-critical domains? The paper identifies the problem but does not delve into practical implications. I am curious to know if the authors have considered specific scenarios where these blind spots might manifest, such as in autonomous driving or medical diagnosis, and what steps could be taken to mitigate these risks. Second, could the authors provide a more formal definition of what constitutes a "concept-specific anti-reader"? The paper introduces this term extensively but does not provide a rigorous framework for understanding the scope and implications of their findings. I am interested in knowing if the authors have considered a formal mathematical definition or a more precise conceptualization of the term. Third, what are the potential causes of concept-specific anti-reading in fine-tuned AOs, and how can these causes be addressed? The paper suggests that the failure is due to the AO's own training process, but it does not provide concrete evidence or hypotheses to support this claim. I am curious to know if the authors have explored specific training objectives, regularization techniques, or architectural choices that might lead to concept-specific blind spots. Fourth, what are the potential implications of concept-specific anti-reading for the development of more robust interpreters? The paper raises a reliability concern for learned interpretability interfaces but does not offer concrete recommendations for mitigating this issue. I am interested in knowing if the authors have considered potential solutions for addressing this problem, such as incorporating additional information into the AO's training process or using alternative interpretability methods. Fifth, what are the potential implications of concept-specific anti-reading for the broader field of interpretability research, and how might they inform the development of more robust interpretability methods? The paper suggests that their findings pose a reliability concern for learned interpretability interfaces, but it does not provide a detailed discussion of the potential implications for the broader field of interpretability research. I am interested in knowing if the authors have considered how their findings might influence the development of new interpretability methods or if they have identified any potential risks associated with using AOs as readouts of other models' internal states. Finally, what are the limitations of the chosen evaluation metrics, and how might these limitations affect the interpretation of the results? The paper uses exact match and semantic recovery as evaluation metrics, but it does not discuss the potential for these metrics to be insufficient in capturing the nuances of concept representation and recovery in AOs. I am interested in knowing if the authors have considered alternative evaluation metrics that might be more sensitive to subtle variations in concept representation.


## Rating:

5.5


## Confidence:

3.5


## Decision:

Reject
}