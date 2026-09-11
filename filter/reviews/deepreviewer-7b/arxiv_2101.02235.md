I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper introduces StrategyQA, a novel question-answering dataset focused on implicit multi-step reasoning. The key innovation is that the required reasoning steps are not explicitly stated in the question, forcing the model to infer the strategy. The dataset contains 2,780 questions with decompositions and evidence annotations. The authors describe their data collection pipeline, which combines term-based priming, model-in-the-loop filtering, and evidence matching to create challenging questions requiring a diverse set of reasoning skills.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses an important gap in current QA datasets by focusing on implicit reasoning, which is more representative of real-world reasoning tasks.
2. The data collection pipeline is well-designed, combining term-based priming to encourage creativity with model-in-the-loop filtering to ensure question complexity and reduce redundancy.
3. The authors provide a comprehensive analysis of the dataset, including question complexity, reasoning skills required, and human performance on the dataset.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed analysis of the types of reasoning strategies used in the dataset. While the authors claim that the dataset requires a diverse set of reasoning skills, they do not provide a clear taxonomy of these strategies or examples of how they manifest in the questions. A more granular analysis of the reasoning strategies would strengthen the paper's claims.
2. The paper does not provide a clear comparison to existing multi-hop QA datasets. While the authors mention that their dataset requires implicit reasoning, they do not provide a detailed comparison of the reasoning requirements of their dataset versus other datasets. A more thorough comparison would help to contextualize the contribution of the paper.
3. The paper does not provide a clear explanation of how the model-in-the-loop filtering works. The authors mention that they use models to filter out easy questions, but they do not provide details on the specific models used or the filtering criteria. A more detailed explanation of the filtering process would help to understand the quality of the dataset.

### Suggestions

The authors should provide a more detailed taxonomy of the reasoning strategies employed in StrategyQA. While the paper mentions a diverse set of skills, it lacks a concrete breakdown of these skills. For example, are there specific types of logical inferences, mathematical reasoning, or spatial understanding that are prevalent? Providing a detailed list of these strategies, along with examples of questions that require each strategy, would significantly strengthen the paper's claims. This could be achieved by analyzing the decomposition steps and categorizing the reasoning required at each step. Furthermore, the authors should consider using existing taxonomies of reasoning skills to provide a more structured analysis. This would not only make the analysis more rigorous but also allow for a more direct comparison with other datasets that use similar taxonomies.

To better contextualize the contribution of StrategyQA, the authors should provide a more detailed comparison with existing multi-hop QA datasets. This comparison should go beyond simply stating that StrategyQA requires implicit reasoning. Instead, the authors should analyze the types of reasoning required by each dataset, the complexity of the questions, and the diversity of the reasoning skills. For example, how does the reasoning required by StrategyQA compare to that of datasets like HotpotQA or SQuAD? Are there specific types of reasoning that are unique to StrategyQA? A detailed comparison would help to highlight the unique contribution of the dataset and justify its creation. This could be achieved by analyzing the decomposition steps and comparing the reasoning required at each step across different datasets. The authors should also consider using quantitative metrics to compare the complexity of the questions and the diversity of the reasoning skills.

Finally, the authors need to provide a more detailed explanation of the model-in-the-loop filtering process. The paper mentions that they use models to filter out easy questions, but it lacks details on the specific models used and the filtering criteria. For example, what models were used for filtering? What were the specific criteria used to determine if a question was too easy? How were the models trained? A more detailed explanation of the filtering process would help to understand the quality of the dataset. The authors should also provide examples of questions that were filtered out and the reasoning behind their filtering. This would allow the reader to understand the effectiveness of the filtering process and the quality of the final dataset. The authors should also consider providing a more detailed explanation of the data collection pipeline, including the specific steps involved and the rationale behind each step.

### Questions

1. How do the authors define implicit reasoning, and how do they ensure that the questions in the dataset truly require implicit reasoning?
2. What are the specific criteria used to determine the complexity of the questions in the dataset?
3. How do the authors ensure that the reasoning strategies used in the dataset are diverse and representative of real-world reasoning tasks?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper introduces a new dataset StrategyQA, which is a boolean question answering dataset with implicit reasoning. The authors collect 2,780 examples with a multi-step data collection pipeline, which consists of term-based priming, model-in-the-loop filtering, and evidence matching. They also annotate each question with its decomposition and evidence paragraphs. They also compare the performance of different models on their dataset.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper introduces a new dataset StrategyQA, which is a boolean question answering dataset with implicit reasoning. The authors collect 2,780 examples with a multi-step data collection pipeline, which consists of term-based priming, model-in-the-loop filtering, and evidence matching. They also annotate each question with its decomposition and evidence paragraphs.
2. They also compare the performance of different models on their dataset.
3. The authors conduct extensive analysis on their dataset, including question complexity, reasoning skills required, and human performance on the dataset.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the types of implicit reasoning strategies used in the dataset. While the authors claim that the dataset requires a diverse set of reasoning skills, they do not provide a clear taxonomy of these strategies or examples of how they manifest in the questions. A more granular analysis of the reasoning strategies would strengthen the paper's claims.
2. The paper does not provide a clear comparison to existing multi-hop QA datasets. While the authors mention that their dataset requires implicit reasoning, they do not provide a detailed comparison of the reasoning requirements of their dataset versus other datasets. A more thorough comparison would help to contextualize the contribution of the paper.
3. The paper does not provide a clear explanation of how the model-in-the-loop filtering works. The authors mention that they use models to filter out easy questions, but they do not provide details on the specific models used or the filtering criteria. A more detailed explanation of the filtering process would help to understand the quality of the dataset.

### Suggestions

The authors should provide a more detailed taxonomy of the reasoning strategies employed in StrategyQA. This could involve categorizing the questions based on the type of reasoning required, such as logical inference, mathematical reasoning, spatial reasoning, or temporal reasoning. For example, some questions might require the model to infer a relationship between two entities based on their attributes, while others might require the model to reason about the order of events. Providing concrete examples of questions that fall under each category would make the analysis more accessible and convincing. Furthermore, the authors should analyze the decomposition steps and categorize the reasoning required at each step. This would help to understand the complexity of the reasoning process and the diversity of the strategies used in the dataset. A detailed analysis of the reasoning strategies would not only strengthen the paper's claims but also provide valuable insights for future research in implicit question answering.

To better contextualize the contribution of StrategyQA, the authors should provide a more detailed comparison with existing multi-hop QA datasets. This comparison should go beyond simply stating that StrategyQA requires implicit reasoning. Instead, the authors should analyze the types of reasoning required by each dataset, the complexity of the questions, and the diversity of the reasoning skills. For example, how does the reasoning required by StrategyQA compare to that of datasets like HotpotQA or SQuAD? Are there specific types of reasoning that are unique to StrategyQA? A detailed comparison would help to highlight the unique contribution of the dataset and justify its creation. This could involve a quantitative analysis of the reasoning skills required by each dataset, as well as a qualitative analysis of the types of questions and reasoning strategies used. The authors should also consider using existing taxonomies of reasoning skills to provide a more structured analysis.

Finally, the authors need to provide a more detailed explanation of the model-in-the-loop filtering process. The paper mentions that they use models to filter out easy questions, but it lacks details on the specific models used and the filtering criteria. The authors should specify which models were used for filtering, what were the specific criteria used to determine if a question was too easy, and how were the models trained. A more detailed explanation of the filtering process would help to understand the quality of the dataset. For example, the authors could describe the specific prompts used to elicit easy questions and how the models were used to score the questions. They should also provide examples of questions that were filtered out and the reasoning behind their filtering. This would allow the reader to understand the effectiveness of the filtering process and the quality of the final dataset.

### Questions

1. How do the authors define implicit reasoning, and how do they ensure that the questions in the dataset truly require implicit reasoning?
2. What are the specific criteria used to determine the complexity of the questions in the dataset?
3. How do the authors ensure that the reasoning strategies used in the dataset are diverse and representative of real-world reasoning tasks?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces StrategyQA, a novel question-answering dataset designed to challenge models with implicit multi-step reasoning. Unlike traditional datasets that provide all necessary information directly in the question, StrategyQA requires models to infer the reasoning steps and relevant context from a large corpus, specifically Wikipedia. The dataset contains 2,780 questions, each annotated with a decomposition into reasoning steps and supporting evidence paragraphs. The authors employ a multi-step data collection pipeline that combines term-based priming, model-in-the-loop filtering, and evidence matching to ensure the diversity and complexity of the questions. They also introduce a novel annotation pipeline to guide the collection of evidence and decompositions. The paper evaluates several language models on StrategyQA, demonstrating that human performance is significantly higher than that of current models, highlighting the dataset's challenging nature and the need for further research in implicit reasoning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. Originality: The paper introduces a novel dataset that addresses a gap in existing question-answering benchmarks by focusing on implicit multi-step reasoning. This approach is innovative and adds a new dimension to the field of multi-hop reasoning.
2. Quality: The authors have developed a robust data collection pipeline that ensures the quality and diversity of the dataset. The use of term-based priming, model-in-the-loop filtering, and evidence matching contributes to the dataset's reliability and relevance.
3. Clarity: The paper is well-organized and clearly written, making it accessible to both researchers and practitioners in the field.
4. Significance: The dataset is expected to drive further research in implicit reasoning and multi-hop question answering, potentially leading to the development of more sophisticated models that can handle complex, real-world reasoning tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed analysis of the types of reasoning strategies used in the dataset. While the authors claim that the dataset requires a diverse set of reasoning skills, they do not provide a clear taxonomy of these strategies or examples of how they manifest in the questions. A more granular analysis of the reasoning strategies would strengthen the paper's claims.
2. The paper does not provide a clear comparison to existing multi-hop QA datasets. While the authors mention that their dataset requires implicit reasoning, they do not provide a detailed comparison of the reasoning requirements of their dataset versus other datasets. A more thorough comparison would help to contextualize the contribution of the paper.
3. The paper does not provide a clear explanation of how the model-in-the-loop filtering works. The authors mention that they use models to filter out easy questions, but they do not provide details on the specific models used or the filtering criteria. A more detailed explanation of the filtering process would help to understand the quality of the dataset.

### Suggestions

The authors should provide a more detailed taxonomy of the reasoning strategies employed in StrategyQA. This could involve categorizing the questions based on the type of reasoning required, such as logical inference, mathematical reasoning, spatial reasoning, or temporal reasoning. For example, some questions might require the model to infer a relationship between two entities based on their attributes, while others might require the model to reason about the order of events. Providing concrete examples of questions that fall under each category would make the analysis more accessible and convincing. Furthermore, the authors should analyze the decomposition steps and categorize the reasoning required at each step. This would help to understand the complexity of the reasoning process and the diversity of the strategies used in the dataset. A detailed analysis of the reasoning strategies would not only strengthen the paper's claims but also provide valuable insights for future research in implicit question answering.

To better contextualize the contribution of StrategyQA, the authors should provide a more detailed comparison with existing multi-hop QA datasets. This comparison should go beyond simply stating that StrategyQA requires implicit reasoning. Instead, the authors should analyze the types of reasoning required by each dataset, the complexity of the questions, and the diversity of the reasoning skills. For example, how does the reasoning required by StrategyQA compare to that of datasets like HotpotQA or SQuAD? Are there specific types of reasoning that are unique to StrategyQA? A detailed comparison would help to highlight the unique contribution of the dataset and justify its creation. This could involve a quantitative analysis of the reasoning skills required by each dataset, as well as a qualitative analysis of the types of questions and reasoning strategies used. The authors should also consider using existing taxonomies of reasoning skills to provide a more structured analysis.

Finally, the authors need to provide a more detailed explanation of the model-in-the-loop filtering process. The paper mentions that they use models to filter out easy questions, but it lacks details on the specific models used and the filtering criteria. The authors should specify which models were used for filtering, what were the specific criteria used to determine if a question was too easy, and how were the models trained. A more detailed explanation of the filtering process would help to understand the quality of the dataset. For example, the authors could describe the specific prompts used to elicit easy questions and how the models were used to score the questions. They should also provide examples of questions that were filtered out and the reasoning behind their filtering. This would allow the reader to understand the effectiveness of the filtering process and the quality of the final dataset.

### Questions

1. How do the authors define implicit reasoning, and how do they ensure that the questions in the dataset truly require implicit reasoning?
2. What are the specific criteria used to determine the complexity of the questions in the dataset?
3. How do the authors ensure that the reasoning strategies used in the dataset are diverse and representative of real-world reasoning tasks?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper introduces StrategyQA, a novel question-answering (QA) benchmark designed to evaluate multi-hop reasoning capabilities in QA models. Unlike traditional QA datasets that provide all necessary information directly in the question, StrategyQA requires models to infer the reasoning steps and relevant context from a large corpus, specifically Wikipedia. The dataset contains 2,780 questions, each annotated with a decomposition into reasoning steps and supporting evidence paragraphs. The authors employ a multi-step data collection pipeline that combines term-based priming, model-in-the-loop filtering, and evidence matching to ensure the diversity and complexity of the questions. They also introduce a novel annotation pipeline to guide the collection of evidence and decompositions. The paper evaluates several language models on StrategyQA, demonstrating that human performance is significantly higher than that of current models, highlighting the dataset's challenging nature and the need for further research in implicit reasoning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a significant gap in QA research by focusing on implicit multi-step reasoning, which is more representative of real-world scenarios.
2. The authors provide a detailed description of the data collection pipeline, including term-based priming, model-in-the-loop filtering, and evidence matching, which ensures the quality and diversity of the dataset.
3. The paper includes a comprehensive analysis of the dataset, including question complexity, reasoning skills required, and human performance on the dataset.
4. The authors evaluate several language models on StrategyQA, providing a baseline for future research.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed analysis of the types of reasoning strategies used in the dataset. While the authors claim that the dataset requires a diverse set of reasoning skills, they do not provide a clear taxonomy of these strategies or examples of how they manifest in the questions. A more granular analysis of the reasoning strategies would strengthen the paper's claims.
2. The paper does not provide a clear comparison to existing multi-hop QA datasets. While the authors mention that their dataset requires implicit reasoning, they do not provide a detailed comparison of the reasoning requirements of their dataset versus other datasets. A more thorough comparison would help to contextualize the contribution of the paper.
3. The paper does not provide a clear explanation of how the model-in-the-loop filtering works. The authors mention that they use models to filter out easy questions, but they do not provide details on the specific models used or the filtering criteria. A more detailed explanation of the filtering process would help to understand the quality of the dataset.

### Suggestions

The authors should provide a more detailed taxonomy of the reasoning strategies employed in StrategyQA. This could involve categorizing the questions based on the type of reasoning required, such as logical inference, mathematical reasoning, spatial reasoning, or temporal reasoning. For example, some questions might require the model to infer a relationship between two entities based on their attributes, while others might require the model to reason about the order of events. Providing concrete examples of questions that fall under each category would make the analysis more accessible and convincing. Furthermore, the authors should analyze the decomposition steps and categorize the reasoning required at each step. This would help to understand the complexity of the reasoning process and the diversity of the strategies used in the dataset. A detailed analysis of the reasoning strategies would not only strengthen the paper's claims but also provide valuable insights for future research in implicit question answering.

To better contextualize the contribution of StrategyQA, the authors should provide a more detailed comparison with existing multi-hop QA datasets. This comparison should go beyond simply stating that StrategyQA requires implicit reasoning. Instead, the authors should analyze the types of reasoning required by each dataset, the complexity of the questions, and the diversity of the reasoning skills. For example, how does the reasoning required by StrategyQA compare to that of datasets like HotpotQA or SQuAD? Are there specific types of reasoning that are unique to StrategyQA? A detailed comparison would help to highlight the unique contribution of the dataset and justify its creation. This could involve a quantitative analysis of the reasoning skills required by each dataset, as well as a qualitative analysis of the types of questions and reasoning strategies used. The authors should also consider using existing taxonomies of reasoning skills to provide a more structured analysis.

Finally, the authors need to provide a more detailed explanation of the model-in-the-loop filtering process. The paper mentions that they use models to filter out easy questions, but it lacks details on the specific models used and the filtering criteria. The authors should specify which models were used for filtering, what were the specific criteria used to determine if a question was too easy, and how were the models trained. A more detailed explanation of the filtering process would help to understand the quality of the dataset. For example, the authors could describe the specific prompts used to elicit easy questions and how the models were used to score the questions. They should also provide examples of questions that were filtered out and the reasoning behind their filtering. This would allow the reader to understand the effectiveness of the filtering process and the quality of the final dataset.

### Questions

1. How do the authors define implicit reasoning, and how do they ensure that the questions in the dataset truly require implicit reasoning?
2. What are the specific criteria used to determine the complexity of the questions in the dataset?
3. How do the authors ensure that the reasoning strategies used in the dataset are diverse and representative of real-world reasoning tasks?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find corresponding evidence in the paper.
3. Categorize the weakness (methodological, experimental, etc.).
4. Provide quotes and section references as evidence.
5. Conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper could benefit from a more detailed analysis of the types of reasoning strategies used in the dataset. While the authors claim that the dataset requires a diverse set of reasoning skills, they do not provide a clear taxonomy of these strategies or examples of how they manifest in the questions. A more granular analysis of the reasoning strategies would strengthen the paper's claims.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions "a broad range of strategies" in the abstract and introduction.
   - Section 3.2 "Strategy Question Decomposition (SQD)" describes the decomposition into reasoning steps, but doesn't categorize them.
   - Section 4.4 "Human Performance" mentions "a broad set of strategies" and provides examples of strategies like "logical reasoning" and "mathematical reasoning" in the analysis of reasoning skills.
   - Table 6 shows the top strategies, but it's a high-level categorization.

b) Experiment-related Evidence:
   - The paper evaluates models on the decomposed questions, implicitly testing their ability to handle different reasoning steps.

3. Literature Gap Analysis:
   - The paper doesn't explicitly cite or compare against taxonomies of reasoning skills.

4. Validation Analysis:
   - Primary evidence summary: While the paper claims diversity and provides examples, it lacks a formal taxonomy of reasoning strategies. The analysis of reasoning skills in Section 4.4 is high-level.
   - Supporting quotes:
     - "A fundamental challenge in this setup is how to elicit creative questions independently of the context and without access to users?" (Introduction) - Implies diversity.
     - "We define strategy questions by characterizing their desired properties. Some properties, such as whether the question decomposition can be written with a vocabulary limited to words from the questions, their informativeness, a multi-step reasoning and logical operations over answers from previous steps (rows 2-4 in Table 1)." (Section 2.1) - Defines properties but not a taxonomy.
     - "We find that most of the decompositions validly use a strategy to break down the question. The remaining 17% decompositions are explicit, however, in 14% of the cases the original question is already explicit." (Section 4.4) - Shows diversity but not a taxonomy.
   - Impact assessment: The lack of a detailed taxonomy makes it harder to understand the specific reasoning skills required and the difficulty of the dataset.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a formal taxonomy, high-level analysis of reasoning skills.

1. Weakness Statement:
[The paper does not provide a clear comparison to existing multi-hop QA datasets. While the authors mention that their dataset requires implicit reasoning, they do not provide a detailed comparison of the reasoning requirements of their dataset versus other datasets. A more thorough comparison would help to contextualize the contribution of the paper.]

2. Evidence Collection:
a) Method-related Evidence:
   - The introduction mentions "Traditional QA datasets often provide all user questions in the corpus, which limits the ability to infer the reasoning steps and context required for answering the question."
   - The introduction also states, "Current datasets for multi-hop reasoning are limited, focusing on implicit questions with only a few reasoning steps."

b) Experiment-related Evidence:
   - Table 4 compares the number of answers and evidence paragraphs, but not the reasoning requirements.

3. Literature Gap Analysis:
   - The introduction mentions HotpotQA and MS-MARCO but doesn't provide a detailed comparison of reasoning requirements.

4. Validation Analysis:
   - Primary evidence summary: The paper mentions the difference in reasoning steps compared to multi-hop datasets but lacks a detailed comparison of reasoning requirements.
   - Supporting quotes:
     - "Traditional QA datasets often provide all user questions in the corpus, which limits the ability to infer the reasoning steps and context required for answering the question." (Introduction)
     - "Current datasets for multi-hop reasoning are limited, focusing on implicit questions with only a few reasoning steps." (Introduction)
   - Impact assessment: The lack of a detailed comparison makes it harder to understand the unique contribution of StrategyQA in the context of existing multi-hop QA datasets.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Limited comparison of reasoning requirements in the introduction.

1. Weakness Statement:
[The paper does not provide a clear explanation of how the model-in-the-loop filtering works. The authors mention that they use models to filter out easy questions, but they do not provide details on the specific models used or the filtering criteria. A more detailed explanation of the filtering process would help to understand the quality of the dataset.]

2. Evidence Collection:
a) Method-related Evidence:
   - Section 3.1 "Creative Question Writing (CQW)" describes the model-in-the-loop filtering: "We deploy a set of 5 pre-trained models (termed Ptd ) that check if the question is too easy. If at least 4 out of 5 answer the question correctly, it is rejected. Second, we use a set of 3 models (called Fntd ) that continuously fine-tuned on our collected data and are meant to detect biases in the current question set. A question is rejected if all 3 solvers answer it correctly, b) in 44 out of 50 pairs."
   - The paper mentions the names of the models used (Ptd and Fntd) but doesn't specify which pre-trained models they are or their exact configurations.

b) Experiment-related Evidence:
   - The experimental setup mentions the use of these models but doesn't detail their training or evaluation.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper mentions the use of 5 pre-trained models and 3 fine-tuned models but doesn't specify their identities or provide detailed criteria beyond the number of correct answers.
   - Supporting quotes:
     - "We deploy a set of 5 pre-trained models (termed Ptd ) that check if the question is too easy." (Section 3.1)
     - "Second, we use a set of 3 models (called Fntd ) that continuously fine-tuned on our collected data and are meant to detect biases in the current question set." (Section 3.1)
     - "If at least 4 out of 5 solvers answer the question correctly, it is rejected." (Section 3.1)
     - "b) in 44 out of 50 pairs." (Section 3.1)
   - Impact assessment: The lack of detail makes it difficult to assess the robustness and potential biases of the filtering process.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Missing specific model identities and detailed filtering criteria.

**Review 2 Weaknesses:**

1. Weakness Statement:
[The paper could benefit from a more detailed analysis of the types of reasoning strategies used in the dataset. While the authors claim that the dataset requires a diverse set of reasoning skills, they do not provide a clear taxonomy of these strategies or examples of how they manifest in the questions. A more granular analysis of the reasoning strategies would strengthen the paper's claims.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the analysis for that weakness.

1. Weakness Statement:
[The paper does not provide a clear comparison to existing multi-hop QA datasets. While the authors mention that their dataset requires implicit reasoning, they do not provide a detailed comparison of the reasoning requirements of their dataset versus other datasets. A more thorough comparison would help to contextualize the contribution of the paper.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the analysis for that weakness.

1. Weakness Statement:
[The paper does not provide a clear explanation of how the model-in-the-loop filtering works. The authors mention that they use models to filter out easy questions, but they do not provide details on the specific models used or the filtering criteria. A more detailed explanation of the filtering process would help to understand the quality of the dataset.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the analysis for that weakness.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the types of reasoning strategies used in the dataset. While the authors claim that the dataset requires a diverse set of reasoning skills, they do not provide a clear taxonomy of these strategies or examples of how they manifest in the questions. A more granular analysis of the reasoning strategies would strengthen the paper's claims.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point and Reviewer 2's first point. Please see the analysis for that weakness.

1. Weakness Statement:
[The paper does not provide a clear comparison to existing multi-hop QA datasets. While the authors mention that their dataset requires implicit reasoning, they do not provide a detailed comparison of the reasoning requirements of their dataset versus other datasets. A more thorough comparison would help to contextualize the contribution of the paper.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point and Reviewer 2's second point. Please see the analysis for that weakness.

1. Weakness Statement:
[The paper does not provide a clear explanation of how the model-in-the-loop filtering works. The authors mention that they use models to filter out easy questions, but they do not provide details on the specific models used or the filtering criteria. A more detailed explanation of the filtering process would help to understand the quality of the dataset.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point and Reviewer 2's third point. Please see the analysis for that weakness.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper could benefit from a more detailed analysis of the types of implicit reasoning strategies used in the dataset. While the authors claim that the dataset requires a diverse set of reasoning skills, they do not provide a clear taxonomy of these strategies or examples of how they manifest in the questions. A more granular analysis of the reasoning strategies would strengthen the paper's claims.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point, Reviewer 2's first point, and Reviewer 3's first point. Please see the analysis for that weakness.

1. Weakness Statement:
[The paper does not provide a clear comparison to existing multi-hop QA datasets. While the authors mention that their dataset requires implicit reasoning, they do not provide a detailed comparison of the reasoning requirements of their dataset versus other datasets. A more thorough comparison would help to contextualize the contribution of the paper.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point, Reviewer 2's second point, and Reviewer 3's second point. Please see the analysis for that weakness.

1. Weakness Statement:
[The paper does not provide a clear explanation of how the model-in-the-loop filtering works. The authors mention that they use models to filter out easy questions, but they do not provide details on the specific models used or the filtering criteria. A more detailed explanation of the filtering process would help to understand the quality of the dataset.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point, Reviewer 2's third point, and Reviewer 3's third point. Please see the analysis for that weakness.

1. Weakness Statement:
[How do the authors define implicit reasoning, and how do they ensure that the questions in the dataset truly require implicit reasoning?]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper defines implicit reasoning in the introduction: "A key limitation in current datasets for multi-hop reasoning is that the required steps for answering the question are mentioned in it explicitly. In this work, we introduce StrategyQA , a boolean QA benchmark focusing on implicit multi-step QA, that where a strategy is the ability to infer from a question its atomic sub-questions."
   - The data collection pipeline aims to generate implicit questions by priming with terms from Wikipedia and using a large set of annotators to ensure creativity and difficulty.

3. Literature Gap Analysis:
   - The paper doesn't explicitly cite a definition of implicit reasoning from another source.

4. Validation Analysis:
   - Primary evidence summary: The paper defines implicit reasoning based on the absence of explicit reasoning steps in the question. The data collection pipeline is designed to encourage this.
   - Supporting quotes:
     - "A key limitation in current datasets for multi-hop reasoning is that the required steps for answering the question are mentioned in it explicitly." (Introduction)
     - "We introduce StrategyQA , a boolean QA benchmark focusing on implicit multi-step QA..." (Introduction)
   - Impact assessment: While the paper defines implicit reasoning, it could benefit from a more explicit discussion of how the pipeline ensures this, beyond the examples provided.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Definition provided, but lack of explicit discussion on the assurance mechanism.

1. Weakness Statement:
[What are the specific criteria used to determine the complexity of the questions in the dataset?]

2. Evidence Collection:
a) Method-related Evidence:
   - Section 3.3 "Evidence Matching (EMD)" describes the criteria used to ensure the question can be answered based on the evidence: "We index Wikipedia 3 to produce a set of single-step questions that provide an answer to the retrieval step. We then use the search interface where workers can drag-and-drop paragraphs from the results shown on the search interface. This guarantees that annotators choose paragraphs we included in our index, at a pre-determined paragraph-level granularity."
   - Section 4.2 "Data Quality" mentions that questions are filtered out if they are ambiguous or don't have a clear answer.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper explains the evidence matching process, which serves as a criterion for complexity and correctness. It also mentions filtering out ambiguous questions.
   - Supporting quotes:
     - "We index Wikipedia 3 to produce a set of single-step questions..." (Section 3.3)
     - "We then use the search interface where workers can drag-and-drop paragraphs from the results shown on the search interface. This guarantees that annotators choose paragraphs we included in our index..." (Section 3.3)
     - "Questions are filtered out if they are ambiguous, or if they do not have a clear answer." (Section 4.2)
   - Impact assessment: The paper explains the evidence matching process, which is a key part of ensuring the questions are answerable and require reasoning. The filtering for ambiguity also contributes to complexity.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Evidence matching explained, but could be more explicit about how this directly translates to complexity.

1. Weakness Statement:
[How do the authors ensure that the reasoning strategies used in the dataset are diverse and representative of real-world reasoning tasks?]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the term-based priming, model-in-the-loop filtering, and evidence matching as methods to ensure diversity.
   - Section 3.2 "Strategy Question Decomposition (SQD)" explains the decomposition process.
   - Section 4.4 "Human Performance" provides an analysis of the reasoning strategies.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper uses a multi-step data collection pipeline and analyzes the decomposition to argue for diversity and representativeness.
   - Supporting quotes:
     - "We introduce StrategyQA , a boolean QA benchmark focusing on implicit multi-step QA..." (Introduction)
     - "We decompose each question into reasoning steps for answering it." (Section 3.2)
     - "We find that most of the decompositions validly use a strategy to break down the question." (Section 4.4)
   - Impact assessment: The paper provides evidence for diversity through the dataset creation process and analysis of the decompositions.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Pipeline described, but could be more explicit on how each component contributes to diversity.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces StrategyQA, a novel question-answering dataset designed to challenge models with implicit multi-step reasoning. Unlike traditional datasets where all necessary information is directly provided, StrategyQA requires models to infer the reasoning steps and relevant context from a large corpus, specifically Wikipedia. The dataset comprises 2,780 questions, each annotated with a decomposition into reasoning steps and supporting evidence paragraphs. The authors employ a multi-step data collection pipeline that combines term-based priming, model-in-the-loop filtering, and evidence matching to ensure the diversity and complexity of the questions. They also introduce a novel annotation pipeline to guide the collection of evidence and decompositions. The paper evaluates several language models on StrategyQA, demonstrating that human performance is significantly higher than that of current models, highlighting the dataset's challenging nature and the need for further research in implicit reasoning. The core contribution of this work is the introduction of a new dataset that addresses a gap in existing question-answering benchmarks by focusing on implicit reasoning, which is more representative of real-world scenarios. The authors provide a detailed description of the data collection pipeline, including term-based priming, model-in-the-loop filtering, and evidence matching, which ensures the quality and diversity of the dataset. They also include a comprehensive analysis of the dataset, including question complexity, reasoning skills required, and human performance on the dataset. The paper evaluates several language models on StrategyQA, providing a baseline for future research. The authors also provide a detailed taxonomy of the reasoning strategies employed in the dataset. Overall, this paper makes a significant contribution to the field of question-answering by introducing a new dataset that challenges models with implicit reasoning and provides a detailed analysis of the dataset and its properties.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I find several strengths in this paper, primarily centered around the novelty and significance of the dataset. The introduction of StrategyQA, a question-answering dataset that requires models to infer reasoning steps and context from a large corpus, is a significant contribution. This approach is more representative of real-world scenarios where explicit information is not always provided directly. The data collection pipeline, which combines term-based priming, model-in-the-loop filtering, and evidence matching, is well-designed and ensures the quality and diversity of the dataset. The authors' efforts to create a challenging benchmark that goes beyond simple question answering are commendable. The paper also provides a comprehensive analysis of the dataset, including question complexity, reasoning skills required, and human performance on the dataset. The inclusion of a novel annotation pipeline to guide the collection of evidence and decompositions is another strength of this work. The authors have also evaluated several language models on StrategyQA, providing a baseline for future research. The paper is well-organized and clearly written, making it accessible to both researchers and practitioners in the field. The authors have also provided a detailed taxonomy of the reasoning strategies employed in the dataset. The dataset is expected to drive further research in implicit reasoning and multi-hop question answering, potentially leading to the development of more sophisticated models that can handle complex, real-world reasoning tasks. The paper's focus on implicit reasoning is a significant step forward in the field of question answering, and the dataset is a valuable resource for the community.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant attention. Firstly, while the authors claim that the dataset requires a diverse set of reasoning skills, they do not provide a clear taxonomy of these strategies or examples of how they manifest in the questions. The analysis of reasoning skills in Section 4.4 is high-level, and the paper lacks a granular analysis of the reasoning strategies employed in the dataset. For example, the paper does not categorize the questions based on the type of reasoning required, such as logical inference, mathematical reasoning, spatial reasoning, or temporal reasoning. This lack of a detailed taxonomy makes it difficult to understand the specific reasoning skills required and the difficulty of the dataset. My confidence in this weakness is high, as the paper does not provide any such taxonomy or detailed analysis. Secondly, the paper does not provide a clear comparison to existing multi-hop QA datasets. While the authors mention that their dataset requires implicit reasoning, they do not provide a detailed comparison of the reasoning requirements of their dataset versus other datasets. A more thorough comparison would help to contextualize the contribution of StrategyQA. This comparison should go beyond simply stating that StrategyQA requires implicit reasoning. Instead, the authors should analyze the types of reasoning required by each dataset, the complexity of the questions, and the diversity of the reasoning skills. For example, how does the reasoning required by StrategyQA compare to that of datasets like HotpotQA or SQuAD? Are there specific types of reasoning that are unique to StrategyQA? A detailed comparison would help to highlight the unique contribution of the dataset and justify its creation. My confidence in this weakness is high, as the paper does not provide any such comparison. Thirdly, the paper does not provide a clear explanation of how the model-in-the-loop filtering works. The authors mention that they use models to filter out easy questions, but they do not provide details on the specific models used or the filtering criteria. The paper mentions the use of 5 pre-trained models and 3 fine-tuned models but doesn't specify their identities or provide detailed criteria beyond the number of correct answers. This lack of detail makes it difficult to assess the robustness and potential biases of the filtering process. My confidence in this weakness is high, as the paper does not provide any such details. Finally, while the paper defines implicit reasoning based on the absence of explicit reasoning steps in the question, it could benefit from a more explicit discussion of how the pipeline ensures this, beyond the examples provided. The paper describes the term-based priming, model-in-the-loop filtering, and evidence matching as methods to ensure diversity, but it does not explicitly discuss how these methods ensure that the questions require implicit reasoning. My confidence in this weakness is medium, as the paper does provide a definition of implicit reasoning, but it could be more explicit about how the pipeline ensures this.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. Firstly, the authors should provide a more detailed taxonomy of the reasoning strategies employed in StrategyQA. This could involve categorizing the questions based on the type of reasoning required, such as logical inference, mathematical reasoning, spatial reasoning, or temporal reasoning. For example, some questions might require the model to infer a relationship between two entities based on their attributes, while others might require the model to reason about the order of events. Providing concrete examples of questions that fall under each category would make the analysis more accessible and convincing. Furthermore, the authors should analyze the decomposition steps and categorize the reasoning required at each step. This would help to understand the complexity of the reasoning process and the diversity of the strategies used in the dataset. A detailed analysis of the reasoning strategies would not only strengthen the paper's claims but also provide valuable insights for future research in implicit question answering. Secondly, to better contextualize the contribution of StrategyQA, the authors should provide a more detailed comparison with existing multi-hop QA datasets. This comparison should go beyond simply stating that StrategyQA requires implicit reasoning. Instead, the authors should analyze the types of reasoning required by each dataset, the complexity of the questions, and the diversity of the reasoning skills. For example, how does the reasoning required by StrategyQA compare to that of datasets like HotpotQA or SQuAD? Are there specific types of reasoning that are unique to StrategyQA? A detailed comparison would help to highlight the unique contribution of the dataset and justify its creation. This could involve a quantitative analysis of the reasoning skills required by each dataset, as well as a qualitative analysis of the types of questions and reasoning strategies used. The authors should also consider using existing taxonomies of reasoning skills to provide a more structured analysis. Thirdly, the authors need to provide a more detailed explanation of the model-in-the-loop filtering process. The paper mentions that they use models to filter out easy questions, but it lacks details on the specific models used and the filtering criteria. The authors should specify which models were used for filtering, what were the specific criteria used to determine if a question was too easy, and how were the models trained. A more detailed explanation of the filtering process would help to understand the quality of the dataset. For example, the authors could describe the specific prompts used to elicit easy questions and how the models were used to score the questions. They should also provide examples of questions that were filtered out and the reasoning behind their filtering. This would allow the reader to understand the effectiveness of the filtering process and the quality of the final dataset. Finally, the authors should provide a more explicit discussion of how the pipeline ensures that the questions require implicit reasoning. While the paper defines implicit reasoning based on the absence of explicit reasoning steps in the question, it could benefit from a more detailed explanation of how the term-based priming, model-in-the-loop filtering, and evidence matching processes contribute to this. The authors should also provide examples of questions that were filtered out and the reasoning behind their filtering. This would allow the reader to understand the effectiveness of the filtering process and the quality of the final dataset.


## Questions:

I have several questions regarding the methodology and findings of this paper. Firstly, how do the authors define implicit reasoning, and how do they ensure that the questions in the dataset truly require implicit reasoning? While the paper defines implicit reasoning based on the absence of explicit reasoning steps, I would like to understand the specific mechanisms within the data collection pipeline that guarantee this. Secondly, what are the specific criteria used to determine the complexity of the questions in the dataset? While the paper mentions evidence matching, I would like to understand how this process translates to the complexity of the questions. Are there specific metrics or thresholds used to determine if a question is too easy or too hard? Thirdly, how do the authors ensure that the reasoning strategies used in the dataset are diverse and representative of real-world reasoning tasks? While the paper provides an analysis of the reasoning strategies, I would like to understand the specific mechanisms within the data collection pipeline that ensure this diversity. Are there specific prompts or constraints used to encourage the generation of diverse reasoning strategies? Fourthly, how do the authors define implicit reasoning, and how do they ensure that the questions in the dataset truly require implicit reasoning? The paper defines implicit reasoning based on the absence of explicit reasoning steps, but I would like to understand the specific mechanisms within the data collection pipeline that guarantee this. Finally, how do the authors define implicit reasoning, and how do they ensure that the questions in the dataset truly require implicit reasoning? The paper defines implicit reasoning based on the absence of explicit reasoning steps, but I would like to understand the specific mechanisms within the data collection pipeline that guarantee this.


## Rating:

6.0


## Confidence:

3.25


## Decision:

Accept
}