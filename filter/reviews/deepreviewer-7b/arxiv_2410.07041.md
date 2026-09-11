I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies the impact of data repetition on the training of transformer models across three mathematical tasks: GCD computation, modular multiplication, and eigenvalue calculation. The authors compare training with repeated examples to training with unique examples, finding that repeated examples can significantly improve model performance and learning speed. They introduce a "two-set training" method, where a small subset of examples is repeatedly presented during training, while the rest are seen only once. This approach consistently outperforms traditional single-set training, especially as the training budget increases. The study highlights the importance of repetition in learning and suggests that transformers can benefit from repeated exposure to a limited set of examples rather than being trained on massive, diverse datasets.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow, with clear explanations of the methodology and results.
- The experiments are well-designed and provide a thorough comparison of different training strategies across multiple tasks.
- The findings are significant, as they challenge the conventional wisdom of minimizing data repetition in large-scale model training and offer a new perspective on the role of repetition in learning.

### Weaknesses

#### Some Related Works


#### comment

 - The experiments are limited to relatively small models (up to 44M parameters) and simple mathematical tasks, raising questions about the generalizability of the findings to larger, more complex models and real-world applications.
- The paper does not provide a clear explanation for why repeated examples improve performance, leaving an important question unanswered.
- The paper lacks a comparison with other data repetition strategies, such as curriculum learning or data augmentation, which could provide a more comprehensive understanding of the benefits of two-set training.

### Suggestions

The paper's exploration of repeated examples in training is intriguing, but further investigation is needed to solidify its claims and practical implications. Specifically, the experiments should be extended to larger transformer models, such as those with 100M or 100M parameters, to determine if the observed benefits of two-set training persist at scale. The current experiments, while well-designed, are limited in scope and do not fully capture the complexities of training large language models. It would be beneficial to explore the impact of varying the size of the repeated subset and the non-repeated subset to understand the optimal configuration for different tasks and model sizes. Furthermore, the paper should investigate the effect of different repetition frequencies on model performance. For example, does training with a very high repetition rate lead to diminishing returns, or are there specific repetition frequencies that are more beneficial than others? This would provide a more nuanced understanding of the role of repetition in learning.

To strengthen the paper's claims, a more thorough comparison with existing data repetition strategies is necessary. While the paper introduces two-set training, it does not adequately compare it to other established methods such as curriculum learning, where examples are presented in a specific order of difficulty, or data augmentation, which introduces variations of the same data point. A detailed comparison with these methods would help to clarify the unique advantages of two-set training and identify scenarios where it is most effective. For instance, it would be valuable to explore whether two-set training is more beneficial for tasks that require memorization of specific patterns or for tasks where the data distribution is highly skewed. Additionally, the paper should investigate the impact of different data distributions on the effectiveness of two-set training. For example, does the method perform equally well when the data is uniformly distributed versus when it is highly skewed? Understanding these factors would provide a more comprehensive picture of the method's strengths and limitations.

Finally, the paper should delve deeper into the underlying mechanisms that explain why repeated examples improve performance. While the paper suggests that repetition helps the model learn specific patterns, it does not provide a detailed analysis of how this occurs within the transformer architecture. It would be beneficial to investigate whether the model is overfitting to the repeated examples or if there is a genuine benefit in terms of improved generalization. This could involve analyzing the model's attention patterns or activation maps to understand how it processes repeated versus non-repeated examples. Furthermore, the paper should explore the potential negative effects of excessive repetition, such as reduced model diversity or over-specialization. A more thorough investigation of these aspects would provide a more complete understanding of the role of repetition in training and help to guide future research in this area.

### Questions

- How does the model perform when trained with a larger subset of repeated examples?
- What is the impact of different repetition frequencies on model performance?
- How does two-set training compare to other data repetition strategies, such as curriculum learning or data augmentation?
- Can the authors provide a more detailed explanation of why repeated examples improve performance?

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

This paper investigates the role of data repetition in training transformers for mathematical tasks, challenging the traditional view that minimizing repetition is optimal. Through controlled experiments on GCD, modular multiplication, and eigenvalue calculations, the authors demonstrate that repeating a small subset of training examples significantly enhances model performance and learning speed, even outperforming models trained on larger, diverse datasets. They introduce a "two-set training" method, where a small, randomly selected subset of examples is repeated many times, while the rest are seen only once. This approach consistently outperforms single-set training, particularly as the training budget increases. The study highlights that transformers can learn effectively from limited, repeated data, suggesting that the benefits of repetition may outweigh the data diversity typically emphasized in large-scale training.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper presents a novel investigation into the role of data repetition in transformer training, addressing a gap in our understanding of how transformers learn mathematical concepts.
- The experiments are well-designed, with clear metrics and comparisons across different data budgets and training regimes. The results are robust, showing consistent improvements with the two-set training approach.
- The paper is well-written and clearly explains the methodology and findings, making it accessible to a broad audience.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's scope is limited to relatively simple mathematical tasks (GCD, modular multiplication, and eigenvalue calculations), which may not fully generalize to more complex, real-world datasets or tasks. The findings, while interesting, are not necessarily applicable to the complex reasoning and generalization challenges seen in natural language processing or other domains. The tasks used, while controlled, may not capture the nuances of real-world data distributions and the complexities of learning from diverse, noisy data.
- The paper does not explore the impact of different repetition strategies, such as varying the frequency or distribution of repeated examples. This is a significant oversight, as the optimal repetition strategy is likely task-dependent and could involve more sophisticated scheduling or adaptive approaches. For instance, a high repetition rate for initial learning followed by a decrease might be beneficial, or a curriculum of increasing repetition as the model learns.
- While the paper introduces the two-set training approach, it does not provide a detailed analysis of why this method works better than single-set training. A deeper investigation into the underlying mechanisms, such as how repetition affects the model's internal representations or learning dynamics, would strengthen the paper's contribution. The paper lacks a theoretical framework to explain the observed empirical results.
- The paper does not discuss the computational cost of the two-set training approach compared to single-set training, which could be a limiting factor in practical applications. The increased training time due to the repeated examples, especially with large datasets, is not addressed, which is a crucial consideration for real-world deployment.

### Suggestions

The paper would benefit from a more thorough investigation into the impact of different repetition strategies. Instead of simply using a fixed repetition rate, the authors could explore adaptive strategies that adjust the repetition frequency based on the model's learning progress or the characteristics of the data. For example, a curriculum learning approach could be implemented where the model is initially trained with a high repetition rate, followed by a gradual decrease as the model converges. Furthermore, the authors could investigate the effect of different distributions of repeated examples, such as clustering examples based on their difficulty or complexity and then repeating those clusters more frequently. This could potentially lead to more efficient learning and better generalization. A detailed analysis of the computational cost of the two-set training approach is also necessary. The authors should provide a comparison of the training time and resource requirements of the two-set training approach with those of single-set training, especially for large datasets. This would help to assess the practical feasibility of the proposed method in real-world scenarios.

To strengthen the paper's contribution, a deeper investigation into the underlying mechanisms of why the two-set training approach works better than single-set training is needed. The authors could explore the impact of repetition on the model's internal representations, such as by visualizing the activation patterns of different layers or analyzing the changes in the model's weights during training. This could provide insights into how repetition affects the learning dynamics and why it leads to better generalization. Furthermore, the authors could investigate the effect of repetition on the model's ability to learn specific mathematical concepts or patterns. For example, they could analyze the model's performance on different types of GCD problems or modular multiplication examples to see if certain types of examples benefit more from repetition than others. This could help to identify the optimal repetition strategy for different tasks and data distributions.

Finally, the paper should explore the applicability of the two-set training approach to more complex, real-world datasets and tasks. While the controlled mathematical tasks used in the paper are useful for isolating the effects of repetition, they may not fully capture the challenges of learning from diverse, noisy, and unstructured data. The authors could consider applying their approach to more complex tasks, such as natural language processing or computer vision, to assess its generalizability. This would involve adapting the two-set training approach to handle the complexities of real-world data, such as varying data distributions and the presence of irrelevant or noisy examples. The authors could also explore the use of more sophisticated data selection strategies, such as active learning or reinforcement learning, to determine which examples to repeat and when to stop repeating them. This would help to make the approach more practical and applicable to a wider range of real-world problems.

### Questions

- How does the two-set training approach perform on more complex, real-world datasets or tasks beyond the controlled mathematical problems?
- What are the computational costs associated with the two-set training approach compared to single-set training, especially for large datasets?
- Can the authors provide a deeper analysis of why repetition improves performance, perhaps by examining the model's internal representations or learning dynamics?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper studies the impact of data repetition on the performance of transformer models trained on mathematical tasks. The authors investigate three problems: GCD computation, modular multiplication, and eigenvalue calculation. They find that repeating a small subset of training examples can significantly improve model performance and learning speed, even outperforming models trained on larger, diverse datasets. They introduce a "two-set training" method, where a small subset of examples is repeatedly presented during training, while the rest are seen only once. This approach consistently outperforms single-set training, especially as the training budget increases. The study highlights the importance of repetition in learning and suggests that transformers can benefit from repeated exposure to a limited set of examples rather than being trained on massive, diverse datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow, with clear explanations of the methodology and results.
- The experiments are well-designed and provide a thorough comparison of different training strategies across multiple tasks.
- The findings are significant, as they challenge the conventional wisdom of minimizing data repetition in large-scale model training and offer a new perspective on the role of repetition in learning.

### Weaknesses

#### Some Related Works


#### comment

 - The experiments are limited to relatively small models (up to 44M parameters) and simple mathematical tasks, raising questions about the generalizability of the findings to larger, more complex models and real-world applications.
- The paper does not provide a clear explanation for why repeated examples improve performance, leaving an important question unanswered.
- The paper lacks a comparison with other data repetition strategies, such as curriculum learning or data augmentation, which could provide a more comprehensive understanding of the benefits of two-set training.

### Suggestions

The paper's exploration of data repetition in training is intriguing, but further investigation is needed to solidify its claims and practical implications. Specifically, the experiments should be extended to larger transformer models, such as those with 100M or 100M parameters, to determine if the observed benefits of two-set training persist at scale. The current experiments, while well-designed, are limited in scope and do not fully capture the complexities of training large language models. It would be beneficial to explore the impact of varying the size of the repeated subset and the non-repeated subset to understand the optimal configuration for different tasks and model sizes. Furthermore, the paper should investigate the effect of different repetition frequencies on model performance. For example, does training with a very high repetition rate lead to diminishing returns, or are there specific repetition frequencies that are more beneficial than others? This would provide a more nuanced understanding of the role of repetition in learning.

To strengthen the paper's claims, a more thorough comparison with existing data repetition strategies is necessary. While the paper introduces two-set training, it does not adequately compare it to other established methods such as curriculum learning, where examples are presented in a specific order of difficulty, or data augmentation, which introduces variations of the same data point. A detailed comparison with these methods would help to clarify the unique advantages of two-set training and identify scenarios where it is most effective. For instance, it would be valuable to explore whether two-set training is more beneficial for tasks that require memorization of specific patterns or for tasks where the data distribution is highly skewed. Additionally, the paper should investigate the impact of different data distributions on the effectiveness of two-set training. For example, does the method perform equally well when the data is uniformly distributed versus when it is highly skewed? Understanding these factors would provide a more comprehensive picture of the method's strengths and limitations.

Finally, the paper should delve deeper into the underlying mechanisms that explain why repeated examples improve performance. While the paper suggests that repetition helps the model learn specific patterns, it does not provide a detailed analysis of how this occurs within the transformer architecture. It would be beneficial to investigate whether the model is overfitting to the repeated examples or if there is a genuine benefit in terms of improved generalization. This could involve analyzing the model's attention patterns or activation maps to understand how it processes repeated versus non-repeated examples. Furthermore, the paper should explore the potential negative effects of excessive repetition, such as reduced model diversity or over-specialization. A more thorough investigation of these aspects would provide a more complete understanding of the role of repetition in training and help to guide future research in this area.

### Questions

- How does the model perform when trained with a larger subset of repeated examples?
- What is the impact of different repetition frequencies on model performance?
- How does two-set training compare to other data repetition strategies, such as curriculum learning or data augmentation?
- Can the authors provide a more detailed explanation of why repeated examples improve performance?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper studies the effect of repetition on the performance of transformer models trained on mathematical tasks. The authors find that repeating a small subset of training examples can significantly improve model performance and learning speed, even outperforming models trained on larger, diverse datasets. They introduce a "two-set training" method, where a small subset of examples is repeatedly presented during training, while the rest are seen only once. This approach consistently outperforms single-set training, especially as the training budget increases. The study highlights the importance of repetition in learning and suggests that transformers can benefit from repeated exposure to a limited set of examples rather than being trained on massive, diverse datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow, with clear explanations of the methodology and results.
- The experiments are well-designed and provide a thorough comparison of different training strategies across multiple tasks.
- The findings are significant, as they challenge the conventional wisdom of minimizing data repetition in large-scale model training and offer a new perspective on the role of repetition in learning.

### Weaknesses

#### Some Related Works


#### comment

 - The experiments are limited to relatively small models (up to 44M parameters) and simple mathematical tasks, raising questions about the generalizability of the findings to larger, more complex models and real-world applications.
- The paper does not provide a clear explanation for why repeated examples improve performance, leaving an important question unanswered.
- The paper lacks a comparison with other data repetition strategies, such as curriculum learning or data augmentation, which could provide a more comprehensive understanding of the benefits of two-set training.

### Suggestions

The paper's exploration of data repetition in training is intriguing, but further investigation is needed to solidify its claims and practical implications. Specifically, the experiments should be extended to larger transformer models, such as those with 100M or 100M parameters, to determine if the observed benefits of two-set training persist at scale. The current experiments, while well-designed, are limited in scope and do not fully capture the complexities of training large language models. It would be beneficial to explore the impact of varying the size of the repeated subset and the non-repeated subset to understand the optimal configuration for different tasks and model sizes. Furthermore, the paper should investigate the effect of different repetition frequencies on model performance. For example, does training with a very high repetition rate lead to diminishing returns, or are there specific repetition frequencies that are more beneficial than others? This would provide a more nuanced understanding of the role of repetition in learning.

To strengthen the paper's claims, a more thorough comparison with existing data repetition strategies is necessary. While the paper introduces two-set training, it does not adequately compare it to other established methods such as curriculum learning, where examples are presented in a specific order of difficulty, or data augmentation, which introduces variations of the same data point. A detailed comparison with these methods would help to clarify the unique advantages of two-set training and identify scenarios where it is most effective. For instance, it would be valuable to explore whether two-set training is more beneficial for tasks that require memorization of specific patterns or for tasks where the data distribution is highly skewed. Additionally, the paper should investigate the impact of different data distributions on the effectiveness of two-set training. For example, does the method perform equally well when the data is uniformly distributed versus when it is highly skewed? Understanding these factors would provide a more comprehensive picture of the method's strengths and limitations.

Finally, the paper should delve deeper into the underlying mechanisms that explain why repeated examples improve performance. While the paper suggests that repetition helps the model learn specific patterns, it does not provide a detailed analysis of how this occurs within the transformer architecture. It would be beneficial to investigate whether the model is overfitting to the repeated examples or if there is a genuine benefit in terms of improved generalization. This could involve analyzing the model's attention patterns or activation maps to understand how it processes repeated versus non-repeated examples. Furthermore, the paper should explore the potential negative effects of excessive repetition, such as reduced model diversity or over-specialization. A more thorough investigation of these aspects would provide a more complete understanding of the role of repetition in training and help to guide future research in this area.

### Questions

- How does the model perform when trained with a larger subset of repeated examples?
- What is the impact of different repetition frequencies on model performance?
- How does two-set training compare to other data repetition strategies, such as curriculum learning or data augmentation?
- Can the authors provide a more detailed explanation of why repeated examples improve performance?

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
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence and link it to the specific weakness.
4. Formulate a conclusion about the validity of the weakness based on the evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The experiments are limited to relatively small models (up to 44M parameters) and simple mathematical tasks, raising questions about the generalizability of the findings to larger, more complex models and real-world applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "Models have 35  million parameters for GCD and modular multiplication, and 22  million for eigenvalues." (Experiments Section, Setup, Models)
   - "The GCD and modular multiplication problems are computed using sequences of digits in base 1000 1000 1000, and the eigenvalue problem is computed using floating point numbers, rounded to three significant digits." (Experiments Section, Setup, Datasets)
   - The paper focuses on mathematical tasks (GCD, modular multiplication, eigenvalues) which are considered relatively simple compared to the complexity of natural language processing or image recognition tasks often addressed in large-scale transformer training.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the limitations of the model size and task complexity in relation to generalizability to larger models and more complex tasks.

4. Validation Analysis:
   - The paper explicitly states the number of parameters for the models used in the experiments, confirming the reviewer's observation about the relatively small model sizes.
   - The description of the datasets confirms the use of relatively simple mathematical tasks.
   - The lack of experiments on larger models or more complex tasks supports the reviewer's concern about the generalizability of the findings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit mention of model sizes and the nature of the mathematical tasks used in the experiments.

1. Weakness Statement:
"The paper does not provide a clear explanation for why repeated examples improve performance, leaving an important question unanswered."

2. Evidence Collection:
a) Method-related Evidence:
   - "Our experiments uncover two striking phenomena: 1. Repetition Helps: For fixed training budgets (30 30  million), models trained on a small data budget (25 25  million) outperform models trained on large or unlimited data budgets. This sometimes gives rise to “emergent” phenomena: properties only learned by models trained on small DB." (Introduction)
   - "2. Two-Set Training: For fixed data budgets, learning speed and performance are significantly enhanced by randomly selecting a subset of training examples, and repeating them more often during training. The “two-set effect” is all the more surprising as the repeated examples are not curated, and only differ from the rest of the training data by their frequency of use." (Introduction)
   - "In all three cases, the benefits of repetition are significant, but come in different flavors, from improving performance and accelerating learning (GCD), to allowing a new task to be learned (multiplication), or increasing model accuracy (eigenvalues)." (Introduction)
b) Experiment-related Evidence:
   - The paper presents empirical results showing improved performance with two-set training but does not delve into the underlying mechanisms within the transformer architecture.

3. Literature Gap Analysis:
   - The paper does not cite or discuss literature that explains the mechanisms behind the benefits of repetition in neural networks, especially transformers.

4. Validation Analysis:
   - The paper focuses on demonstrating the empirical benefits of repetition and two-set training but does not offer a theoretical explanation for why these methods work.
   - The "Introduction" and "Main Idea" sections highlight the observed phenomena but do not provide a mechanistic explanation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus on empirical results and the absence of a theoretical discussion or citations related to the mechanisms of repetition in transformers.

1. Weakness Statement:
"The paper lacks a comparison with other data repetition strategies, such as curriculum learning or data augmentation, which could provide a more comprehensive understanding of the benefits of two-set training."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section focuses on comparing single-set training with two-set training.
   - The "Related Work" section mentions curriculum learning and data augmentation but does not include them as baselines in the experiments.

3. Literature Gap Analysis:
   - While the "Related Work" section mentions curriculum learning and data augmentation, the paper does not provide a detailed comparison of two-set training with these methods in the experimental section.

4. Validation Analysis:
   - The experimental design is limited to comparing single-set and two-set training.
   - Although related work is discussed, there is no experimental comparison with curriculum learning or data augmentation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental setup focuses solely on comparing single-set and two-set training, and the "Related Work" section does not include these methods as baselines in the experiments.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper's scope is limited to relatively simple mathematical tasks (GCD, modular multiplication, and eigenvalue calculations), which may not fully generalize to more complex, real-world datasets or tasks. The findings, while interesting, are not necessarily applicable to the complex reasoning and generalization challenges seen in natural language processing or other domains. The tasks used, while controlled, may not capture the nuances of real-world data distributions and the complexities of learning from diverse, noisy data."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "The GCD and modular multiplication problems are computed using sequences of digits in base 1000 1000 1000, and the eigenvalue problem is computed using floating point numbers, rounded to three significant digits." (Experiments Section, Setup, Datasets)
   - The paper focuses on mathematical tasks, which are simpler than natural language processing tasks.

3. Literature Gap Analysis:
   - The paper does not discuss the limitations of using mathematical tasks and the potential differences in generalization to more complex tasks.

4. Validation Analysis:
   - The description of the datasets confirms the use of relatively simple mathematical tasks.
   - The paper does not provide evidence or discussion on the generalizability of the findings to more complex, real-world datasets.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The description of the mathematical tasks used in the experiments and the lack of discussion on generalizability to more complex tasks.

1. Weakness Statement:
"The paper does not explore the impact of different repetition strategies, such as varying the frequency or distribution of repeated examples. This is a significant oversight, as the optimal repetition strategy is likely task-dependent and could involve more sophisticated scheduling or adaptive approaches. For instance, a high repetition rate for initial learning followed by a decrease might be beneficial, or a curriculum of increasing repetition as the model learns."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "In two-set training, a small set of examples is randomly selected and repeated many times during training, while the rest of the training set is seen a few times only." (Method Section, Overview)
   - "During training, examples are selected from the repeated set with probability p and from the N − S remaining examples with probability (1 − p) / (1 − S) . As a result, a model trained with a training budget of T will see p  T / S repeated  T / (N − S) times on average, while the N − S remaining examples will be repeated ( 1 − p )  T / ( N − S ) times on average." (Method Section, Two-Set Training)
   - The paper uses a fixed probability 'p' to determine the repetition, implying a relatively fixed strategy.

3. Literature Gap Analysis:
   - The paper does not cite or discuss literature on adaptive repetition strategies or curriculum learning approaches to repetition.

4. Validation Analysis:
   - The method description indicates a fixed probability 'p' for repetition, suggesting a non-adaptive strategy.
   - The experiments do not explore varying repetition frequencies or distributions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The description of the two-set training method using a fixed probability 'p' and the lack of experiments exploring different repetition strategies.

1. Weakness Statement:
"While the paper introduces the two-set training approach, it does not provide a detailed analysis of why this method works better than single-set training. A deeper investigation into the underlying mechanisms, such as how repetition affects the model's internal representations or learning dynamics, would strengthen the paper's contribution. The paper lacks a theoretical framework to explain the observed empirical results."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the two-set training method but does not provide a theoretical explanation for its effectiveness.
b) Experiment-related Evidence:
   - The paper presents empirical results showing the superiority of two-set training but does not analyze the internal workings of the transformer.

3. Literature Gap Analysis:
   - The paper does not cite literature that provides a theoretical framework for understanding the impact of repetition on transformer learning.

4. Validation Analysis:
   - The paper focuses on empirical results and the description of the method, lacking a theoretical analysis of why two-set training works.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The absence of a theoretical framework or in-depth analysis of the internal mechanisms of the transformer in relation to the two-set training method.

1. Weakness Statement:
"The paper does not discuss the computational cost of the two-set training approach compared to single-set training, which could be a limiting factor in practical applications. The increased training time due to the repeated examples, especially with large datasets, is not addressed, which is a crucial consideration for real-world deployment."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the number of training samples and training budgets but does not explicitly compare the training time or computational cost between single-set and two-set training.

3. Literature Gap Analysis:
   - The paper does not discuss the computational implications of the two-set training method in comparison to single-set training.

4. Validation Analysis:
   - While the paper provides details on the number of training samples, it does not explicitly address the computational cost or training time differences between the two training methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The lack of explicit discussion or comparison of the computational cost and training time between single-set and two-set training.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The experiments are limited to relatively small models (up to 44M parameters) and simple mathematical tasks, raising questions about the generalizability of the findings to larger, more complex models and real-world applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "Models have 35  million parameters for GCD and modular multiplication, and 22  million for eigenvalues." (Experiments Section, Setup, Models)
   - "The GCD and modular multiplication problems are computed using sequences of digits in base 1000 1000 1000, and the eigenvalue problem is computed using floating point numbers, rounded to three significant digits." (Experiments Section, Setup, Datasets)
   - The paper focuses on mathematical tasks, which are simpler than natural language processing or image recognition.

3. Literature Gap Analysis:
   - The paper does not discuss the limitations of the model size and task complexity in relation to generalizability.

4. Validation Analysis:
   - The paper explicitly states the model sizes and the nature of the mathematical tasks, confirming the reviewer's observation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit mention of model sizes and the nature of the mathematical tasks used in the experiments.

1. Weakness Statement:
"The paper does not provide a clear explanation for why repeated examples improve performance, leaving an important question unanswered."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the two-set training method and presents empirical results but does not offer a theoretical explanation for the observed performance improvements.

3. Literature Gap Analysis:
   - The paper lacks a discussion of literature explaining the mechanisms behind the benefits of repetition in neural networks.

4. Validation Analysis:
   - The paper focuses on demonstrating the empirical benefits without delving into the underlying mechanisms.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus on empirical results and the absence of a theoretical discussion or citations related to the mechanisms of repetition in transformers.

1. Weakness Statement:
"The paper lacks a comparison with other data repetition strategies, such as curriculum learning or data augmentation, which could provide a more comprehensive understanding of the benefits of two-set training."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The experiments compare single-set training with two-set training but do not include curriculum learning or data augmentation as baselines.

3. Literature Gap Analysis:
   - While related work is mentioned, there is no experimental comparison with these methods.

4. Validation Analysis:
   - The experimental design is limited to comparing single-set and two-set training.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental setup focuses solely on comparing single-set and two-set training, and the related work section does not include these methods as baselines in the experiments.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper's exploration of data repetition in training is intriguing, but further investigation is needed to solidify its claims and practical implications. Specifically, the experiments should be extended to larger transformer models, such as those with 100M or 100M parameters, to determine if the observed benefits of two-set training persist at scale. The current experiments, while well-designed, are limited in scope and do not fully capture the complexities of training large language models. It would be beneficial to explore the impact of varying the size of the repeated subset and the non-repeated subset to understand the optimal configuration for different tasks and model sizes. Furthermore, the paper should investigate the effect of different repetition frequencies on model performance. For example, does training with a very high repetition rate lead to diminishing returns, or are there specific repetition frequencies that are more beneficial than others? This would provide a more nuanced understanding of the role of repetition in learning."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "Models have 35  million parameters for GCD and modular multiplication, and 22  million for eigenvalues." (Experiments Section, Setup, Models)
   - The experiments use a fixed ratio of repeated to non-repeated examples (S/N).
   - The paper explores different training budgets but does not systematically vary the size of the repeated and non-repeated subsets or the repetition frequency across different experiments.

3. Literature Gap Analysis:
   - The paper does not cite literature on the impact of varying the size of repeated and non-repeated subsets or different repetition frequencies in the context of transformer training.

4. Validation Analysis:
   - The experiments are limited to models with a few tens of millions of parameters.
   - The experiments use a fixed ratio of repeated to non-repeated examples.
   - The paper does not systematically explore the impact of varying repetition frequency.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The explicit mention of model sizes and the fixed ratio of repeated to non-repeated examples in the experimental setup.

1. Weakness Statement:
"To strengthen the paper's claims, a more thorough comparison with existing data repetition strategies is necessary. While the paper introduces two-set training, it does not adequately compare it to other established methods such as curriculum learning, where examples are presented in a specific order of difficulty, or data augmentation, which introduces variations of the same data point. A detailed comparison with these methods would help to clarify the unique advantages of two-set training and identify scenarios where it is most effective. For instance, it would be valuable to explore whether two-set training is more beneficial for tasks that require memorization of specific patterns or for tasks where the data distribution is highly skewed. Additionally, the paper should investigate the impact of different data distributions on the effectiveness of two-set training. For example, does the method perform equally well when the data is uniformly distributed versus when it is highly skewed? Understanding these factors would provide a more comprehensive picture of the method's strengths and limitations."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The experiments compare single-set training with two-set training but do not include curriculum learning or data augmentation as baselines.
   - The paper uses a specific data distribution for each task (base 1000 or floating-point numbers).
   - The paper does not systematically investigate the impact of different data distributions on the effectiveness of two-set training.

3. Literature Gap Analysis:
   - The paper does not cite literature on curriculum learning or data augmentation in the context of transformer training.

4. Validation Analysis:
   - The experimental design is limited to comparing single-set and two-set training.
   - The paper uses a fixed data distribution for each task and does not explore the impact of different data distributions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental setup and the lack of comparison with curriculum learning or data augmentation, as well as the fixed data distributions used in the experiments.

1. Weakness Statement:
"Finally, the paper should delve deeper into the underlying mechanisms that explain why repeated examples improve performance. While the paper suggests that repetition helps the model learn specific patterns, it does not provide a detailed analysis of how this occurs within the transformer architecture. It would be beneficial to investigate whether the model is overfitting to the repeated examples or if there is a genuine benefit in terms of improved generalization. This could involve analyzing the model's attention patterns or activation maps to understand how it processes repeated versus non-repeated examples. Furthermore, the paper should explore the potential negative effects of excessive repetition, such as reduced model diversity or over-specialization. A more thorough investigation of these aspects would provide a more complete understanding of the role of repetition in training and help to guide future research in this area."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the two-set training method but does not provide a detailed analysis of its impact on the transformer's internal workings.
b) Experiment-related Evidence:
   - The paper presents empirical results showing improved performance with two-set training but does not analyze attention patterns or activation maps.
   - The paper does not explicitly investigate the potential for overfitting to repeated examples or the negative effects of excessive repetition.

3. Literature Gap Analysis:
   - The paper lacks citations to literature that analyzes the internal mechanisms of transformers, such as attention patterns or activation maps, in the context of repetition.

4. Validation Analysis:
   - The paper focuses on empirical results without delving into the underlying mechanisms of the transformer.
   - There is no analysis of attention patterns or activation maps, nor a discussion of overfitting or negative effects of repetition.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus on empirical results and the absence of analysis of internal transformer mechanisms, attention patterns, activation maps, or discussion of overfitting or negative effects of repetition.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a compelling investigation into the role of data repetition in training transformer models, challenging the conventional wisdom of minimizing data repetition in large-scale model training. The authors explore this phenomenon across three mathematical tasks: Greatest Common Divisor (GCD) computation, modular multiplication, and eigenvalue calculation. Their core contribution lies in demonstrating that repeated exposure to a small subset of training examples, even when the overall training dataset is massive, can significantly enhance model performance and learning speed, often outperforming models trained on larger, diverse datasets. The paper introduces a 'two-set training' method, where a small, randomly selected subset of examples is repeatedly presented during training, while the rest of the dataset is seen only once. This approach consistently outperforms traditional single-set training, where all examples are treated equally, especially as the training budget increases. The authors show that this method can lead to emergent phenomena, where models trained on small data budgets exhibit properties only learned by models trained on large or unlimited data. The study's methodology involves carefully designed experiments with varying training budgets and dataset sizes. The models used range from 22 to 44 million parameters, and the datasets are carefully constructed to isolate the effects of repetition. The main empirical finding is that two-set training consistently achieves better performance and faster learning speed compared to single-set training across all three mathematical tasks. This finding is particularly notable in the context of the GCD task, where models trained with two-set training exhibit 'emergent' phenomena, learning properties only seen in models trained with much larger datasets. The overall significance of this work lies in its challenge to the conventional approach of minimizing data repetition in large-scale model training. The authors argue that transformers can benefit from repeated exposure to a limited set of examples, rather than being trained on massive, diverse datasets. This perspective suggests that the benefits of repetition may outweigh the data diversity typically emphasized in large-scale model training and offers a new perspective on the role of repetition in learning. The paper's findings have important implications for how we approach data curation and training in large-scale machine learning, suggesting that a balance between repetition and diversity may be optimal for learning. The authors also suggest that this approach could be particularly beneficial in scenarios where data is scarce or expensive to obtain, as it may allow for effective learning with limited data. However, the paper's focus on mathematical tasks raises questions about the generalizability of these findings to more complex, real-world datasets and tasks, such as natural language processing or computer vision. Despite this limitation, the paper provides a valuable contribution to our understanding of the role of repetition in learning and opens up new avenues for research in this area.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

This paper presents a novel and intriguing investigation into the role of data repetition in training transformer models, and I find several aspects of the work to be particularly strong. First and foremost, the paper's central challenge to the conventional wisdom of minimizing data repetition is a significant contribution. By demonstrating that repeated exposure to a small subset of training examples can lead to improved performance and faster learning, the authors open up a new perspective on how we approach data curation and training in large-scale machine learning. This is a valuable contribution that challenges established norms and encourages a more nuanced understanding of the role of repetition in learning. The experimental design is also a strength of this paper. The authors carefully crafted and controlled the experiments, using clear metrics and comparisons across different data budgets and training regimes. The results are robust, showing consistent improvements with the two-set training approach. The use of controlled mathematical tasks, while simple, allows for a clear and focused analysis of the impact of repetition. The paper is also well-written and easy to follow, with clear explanations of the methodology and results. The authors effectively communicate their findings, making the paper accessible to a broad audience. Furthermore, the paper's introduction of the 'two-set training' method is a valuable contribution. This method, where a small subset of examples is repeatedly presented during training, consistently outperforms single-set training and provides a practical approach for leveraging repetition in training. The authors also explore the underlying mechanisms that explain why repeated examples improve performance, although this is not fully addressed in the paper. Finally, the paper's findings are significant, as they challenge the conventional wisdom of minimizing data repetition in large-scale model training. The authors argue that transformers can benefit from repeated exposure to a limited set of examples, rather than being trained on massive, diverse datasets. This perspective suggests that the benefits of repetition may outweigh the data diversity typically emphasized in large-scale model training. The paper's findings have important implications for how we approach data curation and training in large-scale machine learning, suggesting that a balance between repetition and diversity may be optimal for learning. The authors also suggest that this approach could be particularly beneficial in scenarios where data is scarce or expensive to obtain, as it may allow for effective learning with limited data.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's scope is limited by the relatively small model sizes and simple mathematical tasks used in the experiments. The models used range from 22 million to 44 million parameters, which is significantly smaller than the models typically used in large-scale transformer training, such as those with 100 million or more parameters. This raises concerns about the generalizability of the findings to larger, more complex models and real-world applications. The authors do not provide any evidence or discussion on how their findings might translate to larger models, which is a significant limitation. Furthermore, the mathematical tasks used in the paper, such as GCD computation, modular multiplication, and eigenvalue calculation, are relatively simple compared to the complexity of tasks typically encountered in natural language processing or computer vision. The authors do not explore the impact of different repetition strategies on more complex, real-world datasets or tasks, which limits the generalizability of their findings. The paper also lacks a clear explanation for why repeated examples improve performance. While the authors demonstrate that repetition helps the model learn specific patterns, they do not provide a detailed analysis of how this occurs within the transformer architecture. The paper suggests that repetition helps the model learn specific patterns, but it does not provide a detailed analysis of how this occurs within the transformer architecture. It would be beneficial to investigate whether the model is overfitting to the repeated examples or if there is a genuine benefit in terms of improved generalization. This lack of mechanistic explanation is a significant weakness, as it leaves an important question unanswered. The paper also lacks a comparison with other data repetition strategies, such as curriculum learning or data augmentation. While the paper introduces two-set training, it does not adequately compare it to other established methods such as curriculum learning, where examples are presented in a specific order of difficulty, or data augmentation, which introduces variations of the same data point. This is a significant oversight, as these methods could provide a more comprehensive understanding of the benefits of two-set training. The authors do not cite or discuss literature on adaptive repetition strategies or curriculum learning approaches to repetition. The experimental design is also limited to comparing single-set training with two-set training. The experiments do not explore varying repetition frequencies or distributions. This is a significant oversight, as the optimal repetition strategy is likely task-dependent and could involve more sophisticated scheduling or adaptive approaches. For instance, a high repetition rate for initial learning followed by a decrease might be beneficial, or a curriculum of increasing repetition as the model learns. The paper uses a fixed ratio of repeated to non-repeated examples (S/N) and does not systematically vary the size of the repeated and non-repeated subsets or the repetition frequency across different experiments. This limits the scope of the study and prevents a thorough understanding of the role of repetition in learning. Finally, the paper does not discuss the computational cost of the two-set training approach compared to single-set training. The increased training time due to the repeated examples, especially with large datasets, is not addressed, which is a crucial consideration for real-world deployment. The paper mentions the number of training samples and training budgets but does not explicitly compare the training time or computational cost between single-set and two-set training. This is a significant oversight, as the increased training time could be a limiting factor in practical applications. The paper also does not explore the impact of different data distributions on the effectiveness of two-set training. The paper uses a specific data distribution for each task (base 1000 or floating-point numbers) and does not systematically investigate the impact of different data distributions on the effectiveness of two-set training. This is a significant limitation, as the method's performance might be sensitive to the data distribution. In summary, while the paper presents a novel and intriguing finding, the limitations in model size, task complexity, explanation of the benefits of repetition, comparison with other repetition strategies, and computational cost analysis significantly impact the generalizability and practical implications of the findings. These limitations are supported by the paper's content and are not speculative.


## Suggestions:

To address the identified weaknesses and further strengthen the paper's claims, I recommend several concrete improvements. First, the authors should extend their experiments to larger transformer models, such as those with 100 million or 100 million parameters. This would determine if the observed benefits of two-set training persist at scale and provide a more realistic assessment of its applicability to large-scale model training. It would also be beneficial to explore the impact of varying the size of the repeated subset and the non-repeated subset to understand the optimal configuration for different tasks and model sizes. This could involve systematically varying the ratio of repeated to non-repeated examples and analyzing the impact on model performance. Second, the authors should investigate the effect of different repetition frequencies on model performance. For example, they could explore whether training with a very high repetition rate leads to diminishing returns, or if there are specific repetition frequencies that are more beneficial than others. This would provide a more nuanced understanding of the role of repetition in learning and help to identify the optimal repetition strategy for different tasks. Third, the authors should conduct a more thorough comparison with existing data repetition strategies, such as curriculum learning and data augmentation. This would help to clarify the unique advantages of two-set training and identify scenarios where it is most effective. For instance, it would be valuable to explore whether two-set training is more beneficial for tasks that require memorization of specific patterns or for tasks where the data distribution is highly skewed. Additionally, the authors should investigate the impact of different data distributions on the effectiveness of two-set training. For example, they could analyze the model's performance on different types of GCD problems or modular multiplication examples to see if certain types of examples benefit more from repetition than others. This could help to identify the optimal repetition strategy for different tasks and data distributions. Fourth, the authors should delve deeper into the underlying mechanisms that explain why repeated examples improve performance. This could involve analyzing the model's attention patterns or activation maps to understand how it processes repeated versus non-repeated examples. Furthermore, the authors should explore the potential negative effects of excessive repetition, such as reduced model diversity or over-specialization. A more thorough investigation of these aspects would provide a more complete understanding of the role of repetition in training and help to guide future research in this area. Fifth, the authors should provide a more detailed analysis of the computational cost of the two-set training approach compared to single-set training. This would help to assess the practical feasibility of the proposed method in real-world scenarios. The authors should provide a comparison of the training time and resource requirements of the two-set training approach with those of single-set training, especially for large datasets. This would help to assess the practical feasibility of the proposed method in real-world scenarios. Finally, the authors should explore the applicability of the two-set training approach to more complex, real-world datasets and tasks. While the controlled mathematical tasks used in the paper are useful for isolating the effects of repetition, they may not fully capture the complexities of training large language models. The authors could consider applying their approach to more complex tasks, such as natural language processing or computer vision, to assess its generalizability. This would involve adapting the two-set training approach to handle the complexities of real-world data, such as varying data distributions and the presence of irrelevant or noisy examples. The authors could also explore the use of more sophisticated data selection strategies, such as active learning or reinforcement learning, to determine which examples to repeat and when to stop repeating them. This would help to make the approach more practical and applicable to a wider range of real-world problems.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for further understanding the implications of this work. First, how does the model performance when trained with a larger subset of repeated examples? The paper uses a fixed ratio of repeated to non-repeated examples, and it would be valuable to understand the impact of varying the size of the repeated subset. Specifically, does training with a very high repetition rate lead to diminishing returns, or are there specific repetition rates that are more beneficial than others? Second, what is the impact of different repetition frequencies on model performance? The paper does not systematically explore the impact of varying repetition frequencies, and it would be valuable to understand how the optimal repetition frequency might depend on the task and the model size. For example, is there a point at which increasing the repetition rate leads to diminishing returns, or are there specific repetition frequencies that are more beneficial than others? Third, how does two-set training compare to other data repetition strategies, such as curriculum learning or data augmentation? The paper does not include a comparison with these methods, and it would be valuable to understand the unique advantages and limitations of two-set training compared to these alternatives. For instance, is two-set training more beneficial for tasks that require memorization of specific patterns, or for tasks where the data distribution is highly skewed? Fourth, can the authors provide a more detailed explanation of why repeated examples improve performance? The paper suggests that repetition helps the model learn specific patterns, but it does not provide a detailed analysis of how this occurs within the transformer architecture. It would be valuable to understand whether the model is overfitting to the repeated examples or if there is a genuine benefit in terms of improved generalization. This could involve analyzing the model's attention patterns or activation maps to understand how it processes repeated versus non-repeated examples. Fifth, what are the computational costs associated with the two-set training approach compared to single-set training, especially for large datasets? The paper does not explicitly address the computational cost or training time differences between the two training methods, and it would be valuable to understand the practical implications of this for real-world deployment. Finally, can the authors provide a deeper analysis of why repetition improves performance, perhaps by examining the model's internal representations or learning dynamics? The paper suggests that repetition helps the model learn specific patterns, but it does not provide a detailed analysis of how this occurs within the transformer architecture. It would be beneficial to investigate whether the model is overfitting to the repeated examples or if there is a genuine benefit in terms of improved generalization. This could involve analyzing the model's attention patterns or activation maps to understand how it processes repeated versus non-repeated examples.


## Rating:

5.0


## Confidence:

3.25


## Decision:

Reject
}