I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper presents an analysis of how LLMs compute addition. The authors find that the tokens representing integers are mapped to a helical representation in the final hidden state of the transformer. The authors then show that the final hidden state corresponding to the sum token is a function of the hidden states corresponding to the addends and that the final token corresponding to the answer can be traced back to this helical representation.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper presents a novel analysis of how LLMs represent and compute with integers. The authors show that the hidden states corresponding to integers are mapped to a helical representation. This is a novel finding that could be relevant for understanding how LLMs compute with numbers.
- The paper presents a novel analysis of how LLMs compute addition. The authors show that the final hidden state corresponding to the sum token is a function of the hidden states corresponding to the addends. This is a novel finding that could be relevant for understanding how LLMs compute with numbers.
- The paper is well written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper presents an analysis of how LLMs compute addition. However, it is unclear how this analysis could be extended to other operations such as multiplication or division. The authors acknowledge this limitation in the paper, but it would be helpful to have a more detailed discussion of the challenges involved in extending the analysis to other operations.
- The paper presents an analysis of how LLMs compute addition. However, it is unclear how this analysis could be extended to larger numbers. The authors acknowledge this limitation in the paper, but it would be helpful to have a more detailed discussion of the challenges involved in extending the analysis to larger numbers.
- The paper presents an analysis of how LLMs compute addition. However, it is unclear how this analysis could be extended to other LLMs. The authors acknowledge this limitation in the paper, but it would be helpful to have a more detailed discussion of the challenges involved in extending the analysis to other LLMs.

### Suggestions

The authors should provide a more detailed discussion of the limitations of their analysis, particularly regarding the scope of operations, number size, and model architectures. For instance, while the helical representation of integers is an interesting finding, it's not clear how this representation would generalize to operations like multiplication, which likely involve more complex relationships between the digits of the operands and the digits of the product. A more thorough exploration of the challenges in extending the analysis to multiplication would strengthen the paper. Specifically, the authors could discuss how the carry-over mechanism in multiplication might interact with the helical representation, and whether the same helical mapping would be sufficient to explain the computation of the product. Furthermore, the authors should elaborate on the limitations of their analysis regarding the size of the numbers. The current analysis is limited to single-digit addition, and it is unclear how the helical representation would scale to multi-digit numbers. The authors could discuss how the carry-over mechanism in addition might interact with the helical representation, and whether the same helical mapping would be sufficient to explain the computation of the sum. It would be beneficial to include a discussion of the potential challenges in extending the analysis to larger numbers, such as the increased complexity of the hidden state representations and the potential for carry-over errors to propagate through the digits.

Additionally, the authors should provide a more detailed discussion of the challenges involved in extending their analysis to other LLMs. The current analysis is limited to a few specific models, and it is unclear whether the same helical representation would be present in other LLMs. The authors could discuss the differences in architecture and training data that might affect the representation of numbers in the hidden space. For example, the authors could discuss how the different attention mechanisms in different LLMs might affect the way numbers are processed, and whether the helical representation is specific to the models used in the analysis. It would be helpful to include a discussion of the potential challenges in extending the analysis to other LLMs, such as the need for new experimental setups and the potential for different representations of numbers in the hidden space. The authors could also discuss the potential for their findings to be model-agnostic, and whether the helical representation is a general property of LLMs or a specific artifact of the models used in the analysis.

Finally, the authors should consider including a more detailed discussion of the implications of their findings for the broader field of AI safety and interpretability. The authors could discuss how their findings could be used to develop more robust and reliable LLMs, and how their findings could be used to identify and mitigate potential risks associated with LLMs. For example, the authors could discuss how their findings could be used to develop more transparent and explainable LLMs, and how their findings could be used to detect and prevent adversarial attacks on LLMs. It would be beneficial to include a discussion of the potential societal impact of their findings, and how their work could contribute to the development of more responsible and ethical AI systems.

### Questions

- How could the analysis presented in the paper be extended to other operations such as multiplication or division?
- How could the analysis presented in the paper be extended to larger numbers?
- How could the analysis presented in the paper be extended to other LLMs?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

The authors investigate how LLMs compute addition. They find that the representations of numbers are mapped to helices in the LLM's hidden space. They also find that the helices for the sum are a function of the helices for the addends. They perform interventions to show that the model is indeed using the helices to compute the sum.

### Soundness

3

### Presentation

4

### Contribution

3

### Strengths

- The paper is very well written and easy to follow.
- The paper tackles an important problem: understanding how LLMs compute. This is a very important area of research.
- The authors perform a variety of analyses to support their claims. The interventions are particularly convincing.

### Weaknesses

#### Some Related Works


#### comment

 - The authors only investigate three models (GPT-J, Pythia-6.9B, and Llama3.1-8B). I would have liked to see more models, especially the more recent ones. I am not sure if this is a limitation of the current work or if it is because there are not enough recent open-weight models that the authors could use.
- The authors only investigate addition. I would have liked to see if the authors could extend their analysis to other operations (e.g. subtraction and multiplication). It would also be interesting to see if the authors could extend their analysis to more complex operations (e.g. addition of more than two numbers).

### Suggestions

The authors should consider expanding their investigation to include a wider range of models, particularly those that have been trained on more diverse datasets or with different architectural choices. This would help to determine if the observed helical representation of numbers is a general phenomenon or if it is specific to the models used in the study. For example, models with different attention mechanisms or layer normalization techniques could reveal whether the helical structure is a robust feature of LLMs or an artifact of specific architectures. Furthermore, it would be beneficial to explore models with varying sizes to understand how the dimensionality of the hidden space impacts the emergence of this representation. This could involve analyzing models with both smaller and larger parameter counts to see if the helical structure is present across different scales. Such an analysis would provide a more comprehensive understanding of the phenomenon and its potential universality.

Additionally, the authors should investigate other arithmetic operations beyond addition. While addition is a fundamental operation, exploring subtraction and multiplication would provide a more complete picture of how LLMs perform mathematical computations. For subtraction, the authors could examine how the model represents negative numbers and whether the helical structure extends to negative representations. For multiplication, it would be interesting to see if the model represents the product of two numbers as a function of the helices of the individual numbers. This could involve analyzing the hidden states of the product and comparing them to the helices of the multiplicands. Furthermore, the authors could explore more complex operations, such as the addition of more than two numbers, to see if the helical representation and the Clock algorithm generalize to more complex scenarios. This would require analyzing the hidden states of the intermediate sums and the final result to determine if the same helical structure is present throughout the computation.

Finally, the authors should consider a more detailed analysis of the Clock algorithm. While they demonstrate that the helices for the sum are a function of the helices for the addends, they could provide more insights into the specific mathematical operations that are performed on the helices. For example, they could analyze the transformations that occur in the hidden space when adding two numbers and determine if these transformations are consistent across different pairs of numbers. This could involve analyzing the weights of the linear layers that operate on the hidden states and determining if there are any patterns or regularities in these weights. Furthermore, the authors could investigate the role of non-linearities in the hidden space and determine if they play a crucial role in the computation. A more detailed analysis of the Clock algorithm would provide a deeper understanding of how LLMs perform addition and could potentially lead to new insights into the internal workings of these models.

### Questions

- The authors mention that the helices are a generalized helix. Could the authors elaborate on this point? I did not understand this point.

### Rating

8

### Confidence

3

**********

## Reviewer 3

### Summary

The authors investigate how LLMs represent numbers and compute addition. They find that numbers are represented as helices in the LLM's hidden space, and that the Clock algorithm is used to compute the sum of two numbers. The authors perform causal interventions to show that the LLMs use the helices to compute the sum.

### Soundness

3

### Presentation

4

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a detailed analysis of how LLMs represent numbers and compute addition.
- The authors perform causal interventions to show that the LLMs use the helices to compute the sum.
- The authors provide a detailed analysis of how LLMs represent numbers and compute addition.

### Weaknesses

#### Some Related Works


#### comment

 - The authors only investigate three models (GPT-J, Pythia-6.9B, and Llama3.1-8B). I would have liked to see more models, especially the more recent ones. I am not sure if this is a limitation of the current work or if it is because there are not enough recent open-weight models that the authors could use.
- The authors only investigate addition. I would have liked to see if the authors could extend their analysis to other operations (e.g. subtraction and multiplication). It would also be interesting to see if the authors could extend their analysis to more complex operations (e.g. addition of more than two numbers).

### Suggestions

The authors should consider expanding their investigation to include a wider range of models, particularly those that have been trained on more diverse datasets or with different architectural choices. This would help to determine if the observed helical representation of numbers is a general phenomenon or if it is specific to the models used in the study. For example, models with different attention mechanisms or layer normalization techniques could reveal whether the helical structure is a robust feature of LLMs or an artifact of specific architectures. Furthermore, it would be beneficial to explore models with varying sizes to understand how the dimensionality of the hidden space impacts the emergence of this representation. This could involve analyzing models with both smaller and larger parameter counts to see if the helical structure is present across different scales. Such an analysis would provide a more comprehensive understanding of the phenomenon and its potential universality.

Additionally, the authors should investigate other arithmetic operations beyond addition. While addition is a fundamental operation, exploring subtraction and multiplication would provide a more complete picture of how LLMs perform mathematical computations. For subtraction, the authors could examine how the model represents negative numbers and whether the helical structure extends to negative representations. For multiplication, it would be interesting to see if the model represents the product of two numbers as a function of the helices of the individual numbers. This could involve analyzing the hidden states of the product and comparing them to the helices of the multiplicands. Furthermore, the authors could explore more complex operations, such as the addition of more than two numbers, to see if the helical representation and the Clock algorithm generalize to more complex scenarios. This would require analyzing the hidden states of the intermediate sums and the final result to determine if the same helical structure is present throughout the computation.

Finally, the authors should consider a more detailed analysis of the Clock algorithm. While they demonstrate that the helices for the sum are a function of the helices for the addends, they could provide more insights into the specific mathematical operations that are performed on the helices. For example, they could analyze the transformations that occur in the hidden space when adding two numbers and determine if these transformations are consistent across different pairs of numbers. This could involve analyzing the weights of the linear layers that operate on the hidden states and determining if there are any patterns or regularities in these weights. Furthermore, the authors could investigate the role of non-linearities in the hidden space and determine if they play a crucial role in the computation. A more detailed analysis of the Clock algorithm would provide a deeper understanding of how LLMs perform addition and could potentially lead to new insights into the internal workings of these models.

### Questions

- How do you expect the helical representation of numbers to change if the model is trained on a different dataset or with a different architecture?
- How do you expect the Clock algorithm to change if the model is trained on a different dataset or with a different architecture?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper presents an investigation into how LLMs compute addition. The authors demonstrate that LLMs represent numbers as helices and use the Clock algorithm to perform addition. They conduct a series of experiments to validate their findings, including causal interventions and patching of model components. The results suggest that LLMs have an internal representation of numbers that is distinct from their tokenized form and that they use a specific algorithm to perform addition.

### Soundness

4

### Presentation

4

### Contribution

4

### Strengths

- The paper presents a novel approach to understanding how LLMs compute addition. The use of helices to represent numbers and the Clock algorithm to perform addition is a novel contribution to the field.
- The authors conduct a thorough investigation of how LLMs compute addition, including causal interventions and patching of model components. This provides strong evidence for their claims.
- The paper is well-written and easy to follow. The authors clearly explain their methodology and findings, making it accessible to a wide audience.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses on a specific set of LLMs (GPT-J, Pythia-6.9B, and Llama3.1-8B). It would be beneficial to see if these findings generalize to other LLMs, particularly those with different architectures or training data.
- The paper does not explore the limitations of the Clock algorithm. It would be interesting to see if the algorithm is robust to different inputs or if it has any limitations.

### Suggestions

The authors should consider expanding their analysis to include a more diverse set of LLMs. This would help to determine the generalizability of their findings and whether the helical representation and Clock algorithm are specific to the models they tested or a more universal phenomenon. For example, it would be valuable to see if models trained on different datasets or with different architectures exhibit similar helical representations and use a similar Clock algorithm for addition. This could involve testing models with different numbers of parameters, different attention mechanisms, or different pre-training objectives. Furthermore, the authors could investigate the performance of the Clock algorithm on different types of numbers, such as very large numbers or numbers with different digit patterns. This would help to determine the robustness of the algorithm and identify any potential limitations.

It would also be beneficial to explore the limitations of the Clock algorithm in more detail. The authors should investigate whether the algorithm is sensitive to the specific inputs used for addition. For example, does the algorithm perform equally well for all pairs of numbers, or are there certain pairs that are more difficult to compute? Additionally, the authors should explore whether the algorithm has any limitations in terms of the size of the numbers it can handle. It would be interesting to see if the algorithm can be extended to perform addition with larger numbers or if it is limited to the range of numbers that can be represented in the LLM's hidden state. The authors could also investigate whether the algorithm is robust to noise or errors in the input numbers. This could involve adding random noise to the input numbers and seeing how it affects the performance of the algorithm. Such an analysis would provide a more complete picture of the algorithm's capabilities and limitations.

Finally, the authors should consider exploring the relationship between the helical representation and the Clock algorithm in more detail. For example, they could investigate whether the helical representation is a necessary condition for the Clock algorithm to work or if it is simply a convenient way to represent numbers in the LLM's hidden state. It would also be interesting to see if the helical representation can be used to perform other arithmetic operations, such as subtraction or multiplication. This could involve investigating whether the same algorithm can be used to compute these operations or if different algorithms are needed. Such an analysis would provide a deeper understanding of the internal workings of LLMs and their ability to perform arithmetic computations.

### Questions

- How do you expect the helical representation of numbers to change if the model is trained on a different dataset or with a different architecture?
- How do you expect the Clock algorithm to change if the model is trained on a different dataset or with a different architecture?

### Rating

10

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find supporting evidence from the paper.
3. Categorize the weakness and provide specific quotes or references to the paper.
4. If a weakness is not supported by the paper, explain why.
5. Synthesize the findings and provide a conclusion for each weakness.
**Review 1 Weaknesses:**

1. Weakness Statement: The authors only investigate three models (GPT-J, Pythia-6.9B, and Llama3.1-8B). I would have liked to see more models, especially the more recent ones. I am not sure if this is a limitation of the current work or if it is because there are not enough recent open-weight models that the authors could use.

2. Evidence Collection:
    b) Experiment-related Evidence: The "Experiments" section explicitly lists the models used: "We evaluate all three models on these 10,000 addition problems, and find that all models can competently complete the task: GPT-J achieves 80.5% accuracy, Pythia-6.9B achieves 77.2% accuracy, and Llama3.1-8B achieves 98.0% accuracy." (Section 4).

3. Literature Gap Analysis: The paper does not explicitly justify the choice of these three models or discuss the availability of other recent open-weight models.

4. Validation Analysis: The reviewer's statement is directly supported by the paper's content. The paper clearly states the models used in the experiments. The reviewer's speculation about the reason for the limited number of models is not verifiable from the paper.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: Explicit listing of the three models in the "Experiments" section.

1. Weakness Statement: The authors only investigate addition. I would have liked to see if the authors could extend their analysis to other operations (e.g. subtraction and multiplication). It would also be interesting to see if the authors could extend their analysis to more complex operations (e.g. addition of more than two numbers).

2. Evidence Collection:
    b) Experiment-related Evidence: The "Problem Setup" section states: "To ensure that answers require only a single token for all models, we construct problems a + b a+b for integers a , b ∈ [ 0 , 99 ] . We evaluate all three models on these 10,000 addition problems..." (Section 4). The experiments section focuses solely on addition.

3. Literature Gap Analysis: The paper does not discuss the challenges or feasibility of extending the analysis to other operations.

4. Validation Analysis: The reviewer's statement is directly supported by the paper's description of the experimental setup and the focus of the experiments.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: Explicit focus on addition in the "Problem Setup" and "Experiments" sections.

**Review 2 Weaknesses:**

1. Weakness Statement: The authors only investigate three models (GPT-J, Pythia-6.9B, and Llama3.1-8B). I would have liked to see more models, especially the more recent ones. I am not sure if this is a limitation of the current work or if it is because there are not enough recent open-weight models that the authors could use.

2. Evidence Collection:
    b) Experiment-related Evidence: The "Experiments" section explicitly lists the models used: "We evaluate all three models on these 10,000 addition problems, and find that all models can competently complete the task: GPT-J achieves 80.5% accuracy, Pythia-6.9B achieves 77.2% accuracy, and Llama3.1-8B achieves 98.0% accuracy." (Section 4).

3. Literature Gap Analysis: The paper does not explicitly justify the choice of these three models or discuss the availability of other recent open-weight models.

4. Validation Analysis: The reviewer's statement is directly supported by the paper's content. The paper clearly states the models used in the experiments. The reviewer's speculation about the reason for the limited number of models is not verifiable from the paper.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: Explicit listing of the three models in the "Experiments" section.

1. Weakness Statement: The authors only investigate addition. I would have liked to see if the authors could extend their analysis to other operations (e.g. subtraction and multiplication). It would also be interesting to see if the authors could extend their analysis to more complex operations (e.g. addition of more than two numbers).

2. Evidence Collection:
    b) Experiment-related Evidence: The "Problem Setup" section states: "To ensure that answers require only a single token for all models, we construct problems a + b a+b for integers a , b ∈ [ 0 , 99 ] . We evaluate all three models on these 10,000 addition problems..." (Section 4). The experiments section focuses solely on addition.

3. Literature Gap Analysis: The paper does not discuss the challenges or feasibility of extending the analysis to other operations.

4. Validation Analysis: The reviewer's statement is directly supported by the paper's description of the experimental setup and the focus of the experiments.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: Explicit focus on addition in the "Problem Setup" and "Experiments" sections.

**Review 3 Weaknesses:**

1. Weakness Statement: The authors only investigate three models (GPT-J, Pythia-6.9B, and Llama3.1-8B). I would have liked to see more models, especially the more recent ones. I am not sure if this is a limitation of the current work or if it is because there are not enough recent open-weight models that the authors could use.

2. Evidence Collection:
    b) Experiment-related Evidence: The "Experiments" section explicitly lists the models used: "We evaluate all three models on these 10,000 addition problems, and find that all models can competently complete the task: GPT-J achieves 80.5% accuracy, Pythia-6.9B achieves 77.2% accuracy, and Llama3.1-8B achieves 98.0% accuracy." (Section 4).

3. Literature Gap Analysis: The paper does not explicitly justify the choice of these three models or discuss the availability of other recent open-weight models.

4. Validation Analysis: The reviewer's statement is directly supported by the paper's content. The paper clearly states the models used in the experiments. The reviewer's speculation about the reason for the limited number of models is not verifiable from the paper.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: Explicit listing of the three models in the "Experiments" section.

1. Weakness Statement: The authors only investigate addition. I would have liked to see if the authors could extend their analysis to other operations (e.g. subtraction and multiplication). It would also be interesting to see if the authors could extend their analysis to more complex operations (e.g. addition of more than two numbers).

2. Evidence Collection:
    b) Experiment-related Evidence: The "Problem Setup" section states: "To ensure that answers require only a single token for all models, we construct problems a + b a+b for integers a , b ∈ [ 0 , 99 ] . We evaluate all three models on these 10,000 addition problems..." (Section 4). The experiments section focuses solely on addition.

3. Literature Gap Analysis: The paper does not discuss the challenges or feasibility of extending the analysis to other operations.

4. Validation Analysis: The reviewer's statement is directly supported by the paper's description of the experimental setup and the focus of the experiments.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: Explicit focus on addition in the "Problem Setup" and "Experiments" sections.

**Review 4 Weaknesses:**

1. Weakness Statement: The paper focuses on a specific set of LLMs (GPT-J, Pythia-6.9B, and Llama3.1-8B). It would be beneficial to see if these findings generalize to other LLMs, particularly those with different architectures or training data.

2. Evidence Collection:
    b) Experiment-related Evidence: The "Experiments" section explicitly lists the models used: "We evaluate all three models on these 10,000 addition problems, and find that all models can competently complete the task: GPT-J achieves 80.5% accuracy, Pythia-6.9B achieves 77.2% accuracy, and Llama3.1-8B achieves 98.0% accuracy." (Section 4).

3. Literature Gap Analysis: The paper does not explicitly discuss the limitations of generalizing the findings to other LLMs or the potential impact of different architectures or training data.

4. Validation Analysis: The reviewer's statement is directly supported by the paper's content. The paper clearly states the models used in the experiments, and the reviewer's point about the limitations of generalization is a valid concern that the paper does not address.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: Explicit listing of the three models in the "Experiments" section and the absence of discussion on generalization.

1. Weakness Statement: The paper does not explore the limitations of the Clock algorithm. It would be interesting to see if the algorithm is robust to different inputs or if it has any limitations.

2. Evidence Collection:
    b) Experiment-related Evidence: The paper presents experiments validating the Clock algorithm's effectiveness in specific tasks (e.g., single-token answers, specific addition problems). However, there is no systematic exploration of its limitations with different inputs or scenarios.

3. Literature Gap Analysis: The paper does not cite or discuss literature on the limitations of similar algorithms used in other contexts.

4. Validation Analysis: The reviewer's statement is valid. While the paper demonstrates the algorithm's effectiveness in the tested scenarios, it lacks a broader exploration of its limitations.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: The experimental design focuses on validating the algorithm's core functionality rather than exploring its boundaries.

1. Weakness Statement: How do you expect the helical representation of numbers to change if the model is trained on a different dataset or with a different architecture?

2. Evidence Collection: The paper does not explicitly address the potential changes in the helical representation with different training data or architectures.

3. Literature Gap Analysis: The paper does not cite or discuss literature on how training data and architecture influence internal representations in LLMs.

4. Validation Analysis: The reviewer's question points to a limitation in the paper's scope. The paper focuses on a specific set of models and training data, and its findings might not generalize to other scenarios.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: The paper's focus on a specific set of models and training data without discussing the potential impact of alternatives.

1. Weakness Statement: How do you expect the Clock algorithm to change if the model is trained on a different dataset or with a different architecture?

2. Evidence Collection: The paper does not explicitly address the potential changes in the Clock algorithm with different training data or architectures.

3. Literature Gap Analysis: The paper does not cite or discuss literature on how training data and architecture influence the algorithms used in LLMs.

4. Validation Analysis: Similar to the previous question, this points to a limitation in the paper's scope regarding the generalizability of its findings.

5. Conclusion: Valid. Confidence level: High. Key supporting evidence: The paper's focus on a specific set of models and training data without discussing the potential impact of alternatives.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a compelling investigation into how Large Language Models (LLMs) represent and compute integer addition, revealing a fascinating underlying mechanism that the authors term the 'Clock algorithm.' The authors' core contribution lies in their discovery that numerical representations within LLMs are not simply token-level mappings, but rather, are mapped onto a helical structure within the model's hidden state space. This helical representation, they argue, is a fundamental aspect of how LLMs encode numerical information. The authors then demonstrate that the Clock algorithm, a specific computational procedure, is used by LLMs to perform addition. This algorithm operates on the helical representations of the input numbers, effectively combining them to produce the helical representation of the sum. The authors meticulously validate their claims through a series of causal interventions and patching experiments, providing strong evidence that the LLMs are indeed utilizing these helical representations and the Clock algorithm for addition. The experiments, conducted on three different LLMs (GPT-J, Pythia-6.9B, and Llama3.1-8B), show that these models can perform addition with varying degrees of accuracy, and the authors demonstrate that the helical representation and the Clock algorithm are present in all three models. The paper's findings are significant because they offer a deeper understanding of the internal workings of LLMs, moving beyond surface-level token-level analysis to explore the more abstract and potentially interpretable representations and algorithms that underlie their capabilities. This work contributes to the growing body of research aimed at demystifying LLMs and making them more transparent and trustworthy, which is a critical step towards their wider and more responsible application. The authors' approach of combining mathematical analysis with empirical validation is a key strength of the paper, providing a robust and convincing argument for their claims. The paper is well-written and easy to follow, making it accessible to a broad audience of researchers interested in the intersection of machine learning and cognitive science. Overall, this paper represents a significant advancement in our understanding of how LLMs perform arithmetic computations, and it provides a valuable framework for future research in this area.


## Soundness:

3.25


## Presentation:

3.75


## Contribution:

3.0


## Strengths:

This paper exhibits several notable strengths that contribute to its overall impact and significance. First and foremost, the authors' identification of the helical representation of numbers within LLMs is a novel and insightful finding. This representation, which maps numerical values onto a helix within the model's hidden state space, is a departure from the more commonly understood token-level representations. This discovery suggests a more abstract and potentially more fundamental way in which LLMs encode numerical information. The authors' ability to validate this representation through causal interventions and patching experiments is particularly compelling. These experiments provide strong evidence that the LLMs are not simply relying on superficial token-level correlations but are instead engaging with the underlying helical structure. The authors' demonstration that the Clock algorithm is used to compute the sum of two numbers is another significant contribution. This algorithm, which operates on the helical representations of the input numbers, provides a concrete mechanism for how LLMs perform addition. The authors' ability to validate this algorithm through a series of experiments is a testament to the robustness of their findings. The paper's experimental design is also a strength. The authors' use of three different LLMs (GPT-J, Pythia-6.9B, and Llama3.1-8B) provides a degree of robustness to their findings, showing that the helical representation and the Clock algorithm are not specific to a single model. Furthermore, the authors' focus on a single, well-defined task (integer addition) allows for a clear and focused analysis, which is a strength in itself. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors' clear articulation of their methodology and findings is a significant strength, allowing for easy comprehension and replication of their work. The combination of mathematical analysis with empirical validation is another key strength of the paper. The authors' ability to translate their mathematical understanding of the helical representation and the Clock algorithm into concrete experimental designs is a testament to their analytical skills. Finally, the paper's contribution to the broader field of AI safety and interpretability is significant. By demystifying the internal workings of LLMs, this paper provides a valuable framework for future research aimed at developing more transparent and trustworthy AI systems. The authors' work is a crucial step towards a better understanding of how LLMs perform computations and how we can ensure that they are used responsibly.


## Weaknesses:

While this paper presents a compelling and well-supported analysis of how LLMs perform addition, there are several limitations that warrant careful consideration. One significant weakness is the limited scope of the models used in the experiments. The authors focus on three specific models: GPT-J, Pythia-6.9B, and Llama3.1-8B. As the reviewers correctly point out, this selection is not exhaustive, and it is unclear whether the observed helical representation and Clock algorithm are specific to these models or if they are a more general phenomenon. The paper does not provide a strong justification for choosing these particular models, nor does it discuss the potential impact of using other models with different architectures, training data, or sizes. This limitation is particularly concerning because it raises questions about the generalizability of the findings. For example, the authors do not explore models with different attention mechanisms or layer normalization techniques, which could potentially affect the helical representation. Furthermore, the paper does not investigate the performance of the Clock algorithm on models with varying sizes, which could reveal whether the algorithm's effectiveness is dependent on model scale. This lack of exploration limits the confidence I have in the generalizability of the findings. Another significant limitation is the paper's exclusive focus on the addition operation. While the authors demonstrate that LLMs can perform addition, they do not extend their analysis to other fundamental arithmetic operations, such as subtraction or multiplication. This narrow focus limits the scope of the paper's conclusions. It is unclear whether the helical representation and the Clock algorithm are applicable to other operations, or if other algorithms would be required. For instance, the authors do not explore how the model represents negative numbers, which is crucial for understanding the representation of subtraction. Similarly, they do not investigate how the model might represent the product of two numbers as a function of the helices of the individual numbers. This limitation is significant because it restricts the paper's contribution to a specific type of computation and leaves open the question of whether the observed phenomena are unique to addition or are a more general feature of LLMs. The paper also lacks a detailed discussion of the limitations of the Clock algorithm. While the authors demonstrate that the algorithm is effective for the specific tasks they investigate, they do not explore its robustness to different inputs or scenarios. For example, the paper does not investigate whether the algorithm is sensitive to the specific inputs used for addition. It is unclear whether the algorithm performs equally well for all pairs of numbers, or if there are certain pairs that are more difficult to compute. Additionally, the paper does not explore whether the algorithm has any limitations in terms of the size of the numbers it can handle. It would be interesting to see if the algorithm can be extended to perform addition with larger numbers, or if it is limited to the range of numbers that can be represented in the LLM's hidden state. This lack of exploration of the algorithm's limitations is a significant weakness, as it leaves open the question of the algorithm's practical applicability. Finally, the paper does not adequately address the potential impact of different training data or architectures on the helical representation and the Clock algorithm. The authors focus on a specific set of models and training data, and their findings might not generalize to other scenarios. The paper does not discuss how the training data or architecture might affect the internal representations in the hidden space. It is unclear whether the helical structure is a robust feature of LLMs or an artifact of specific architectures. This limitation is significant because it raises questions about the generalizability of the findings and the extent to which they can be applied to other LLMs. The paper's focus on a specific set of models and training data without discussing the potential impact of alternatives is a significant weakness that limits the scope of the conclusions. These limitations, while not invalidating the paper's findings, highlight areas where further research is needed to fully understand the internal workings of LLMs and the generalizability of the observed phenomena. My confidence in these limitations is high, as they are directly supported by the paper's content and the absence of specific discussions on these issues.


## Suggestions:

To address the identified weaknesses and further strengthen this research, I recommend several concrete and actionable improvements. First, the authors should significantly expand their investigation to include a more diverse set of LLMs. This would involve testing models with different architectures, training data, and sizes. Specifically, I suggest including models with different attention mechanisms, layer normalization techniques, and parameter counts. This would help to determine if the observed helical representation and Clock algorithm are a general phenomenon or specific to the models used in the study. Furthermore, the authors should investigate models with varying sizes to understand how the dimensionality of the hidden space impacts the emergence of this representation. This would provide a more comprehensive understanding of the phenomenon and its potential universality. Second, the authors should extend their analysis beyond addition to other fundamental arithmetic operations, such as subtraction and multiplication. This would involve examining how the model represents negative numbers and whether the helical structure extends to negative representations. For subtraction, the authors could investigate how the model represents the difference between two numbers as a function of the helices of the individual numbers. For multiplication, it would be interesting to see if the model represents the product of two numbers as a function of the helices of the individual numbers. This would require analyzing the hidden states of the product and comparing them to the helices of the multiplicands. Furthermore, the authors could explore more complex operations, such as the addition of more than two numbers, to see if the helical representation and the Clock algorithm generalize to more complex scenarios. This would require analyzing the hidden states of the intermediate sums and the final result to determine if the same helical structure is present throughout the computation. Third, the authors should conduct a more detailed analysis of the Clock algorithm's limitations. This would involve investigating whether the algorithm is sensitive to the specific inputs used for addition. For example, does the algorithm perform equally well for all pairs of numbers, or are there certain pairs that are more difficult to compute? Additionally, the authors should explore whether the algorithm has any limitations in terms of the size of the numbers it can handle. It would be interesting to see if the algorithm can be extended to perform addition with larger numbers, or if it is limited to the range of numbers that can be represented in the LLM's hidden state. This could involve analyzing the weights of the linear layers that operate on the hidden states and determining if there are any patterns or regularities in these weights that are related to the Clock algorithm. Furthermore, the authors could investigate the role of non-linearities in the hidden space and determine if they play a crucial role in the computation. A more detailed analysis of the Clock algorithm would provide a deeper understanding of how LLMs perform addition and could potentially lead to new insights into the internal workings of these models. Fourth, the authors should consider a more detailed analysis of the Clock algorithm. While they demonstrate that the helices for the sum are a function of the helices for the addends, they could provide more insights into the specific mathematical operations that are performed on the helices. For example, they could analyze the transformations that occur in the hidden space when adding two numbers and determine if these transformations are consistent across different pairs of numbers. This could involve analyzing the weights of the linear layers that operate on the hidden states and determining if there are any patterns or regularities in these weights. Furthermore, the authors could investigate the role of non-linearities in the hidden space and determine if they play a crucial role in the computation. A more detailed analysis of the Clock algorithm would provide a deeper understanding of how LLMs perform addition and could potentially lead to new insights into the internal workings of these models. Finally, the authors should consider exploring the relationship between the helical representation and the Clock algorithm in more detail. For example, they could investigate whether the helical representation is a necessary condition for the Clock algorithm to work or if it is simply a convenient way to represent numbers in the LLM's hidden state. It would also be interesting to see if the helical representation can be used to perform other arithmetic operations, such as subtraction or multiplication. This could involve investigating whether the same algorithm can be used to compute these operations or if different algorithms are needed. Such an analysis would provide a deeper understanding of the internal workings of LLMs and their ability to perform arithmetic computations. These suggestions, while requiring additional effort, would significantly enhance the paper's contribution and provide a more comprehensive understanding of the internal mechanisms of LLMs.


## Questions:

Several key questions arise from this research that warrant further investigation. First, how would the helical representation of numbers and the Clock algorithm change if the model were trained on a different dataset or with a different architecture? The current study focuses on a specific set of models and training data, and it is unclear whether the observed phenomena are specific to these models or a more general feature of LLMs. Understanding how the helical representation and the Clock algorithm might be affected by different training regimes or architectural choices is crucial for determining the robustness and generalizability of the findings. For example, would models trained on a dataset with more explicit numerical information exhibit a more pronounced helical representation? Or would models with different attention mechanisms or layer normalization techniques produce a different helical structure? Second, how would the Clock algorithm change if the model were trained on a different dataset or with a different architecture? The paper demonstrates the effectiveness of the Clock algorithm for addition, but it does not explore its limitations or robustness. It is unclear whether the algorithm is sensitive to the specific inputs used for addition or if it has any limitations in terms of the size of the numbers it can handle. Furthermore, it would be interesting to know if the algorithm's performance is affected by different training regimes or architectural choices. For example, would models trained on a dataset with more complex arithmetic problems exhibit a more robust Clock algorithm? Or would models with different activation functions or regularization techniques produce a different algorithm? Third, the authors mention that the helices are a generalized helix. Could the authors elaborate on this point? I did not understand this point. A more detailed explanation of what constitutes a generalized helix in this context would be beneficial. What are the specific mathematical properties that define a generalized helix, and how do these properties relate to the representation of numbers within the LLM's hidden space? Fourth, how could the analysis presented in the paper be extended to other operations such as multiplication or division? The paper focuses on addition, but it is unclear whether the helical representation and the Clock algorithm are applicable to other arithmetic operations. For multiplication, it would be interesting to see if the model represents the product of two numbers as a function of the helices of the individual numbers. For division, it would be interesting to see if the model represents the quotient of two numbers as a function of the helices of the individual numbers. Finally, how could the analysis presented in the paper be extended to larger numbers? The current study focuses on relatively small numbers, and it is unclear whether the helical representation and the Clock algorithm would still be effective for larger numbers. It would be interesting to see if the algorithm can be extended to perform addition with larger numbers, or if it is limited to the range of numbers that can be represented in the LLM's hidden state. These questions highlight key uncertainties in the current research and point to areas where further investigation is needed to fully understand the internal workings of LLMs.


## Rating:

8.0


## Confidence:

3.25


## Decision:

Accept
}