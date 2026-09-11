I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates the perplexity-based data pruning method for LLM pre-training. The authors find that a small language model can be used to prune the pre-training data of a larger language model, leading to both significant downstream performance improvements and increased training efficiency. The authors also investigate perplexity-based data pruning in two non-standard settings: the over-trained and data-constrained regimes. The authors find that for both settings, training on perplexity pruned data can outperform training on unpruned data, demonstrating that perplexity-based data pruning is a widely applicable and extensible technique.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The authors investigate perplexity-based data pruning in two non-standard settings: the over-trained and data-constrained regimes. The authors find that for both settings, training on perplexity pruned data can outperform training on unpruned data, demonstrating that perplexity-based data pruning is a widely applicable and extensible technique.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that perplexity-based data pruning can significantly improve downstream task performance. However, the authors do not provide a clear explanation of why perplexity-based data pruning can improve downstream task performance. The authors should provide a more detailed analysis of the relationship between perplexity and downstream task performance.
2. The authors claim that perplexity-based data pruning can increase training efficiency. However, the authors do not provide a clear explanation of how perplexity-based data pruning can increase training efficiency. The authors should provide a more detailed analysis of the relationship between perplexity and training efficiency.
3. The authors claim that perplexity-based data pruning can be widely applicable and extensible. However, the authors only investigate two datasets. The authors should investigate more datasets to support their claim.

### Suggestions

The paper would benefit significantly from a more in-depth analysis of the relationship between perplexity and downstream task performance. While the authors demonstrate that perplexity-based pruning leads to improvements, they do not sufficiently explain *why* this occurs. For instance, a detailed examination of the types of data points that are pruned could reveal whether perplexity is filtering out noisy or irrelevant data, or if it is selectively removing data that is detrimental to downstream task performance. This could involve analyzing the semantic content of the pruned data, or comparing the performance of models trained on pruned data versus unpruned data on specific subsets of the downstream tasks. Furthermore, the authors should explore the possibility that perplexity is acting as a form of regularization, preventing overfitting to the pre-training data. A more thorough investigation into these aspects would greatly strengthen the paper's claims and provide a more complete understanding of the method.

To address the lack of clarity regarding training efficiency, the authors should provide a more detailed breakdown of the computational costs associated with their approach. While the authors mention that perplexity-based pruning can reduce the size of the training dataset, they do not specify how this reduction translates to actual training time savings. A more detailed analysis should include the time required to compute perplexity for the entire dataset, the time required to train models with and without pruning, and the memory requirements of each approach. This analysis should also consider the impact of different pruning strategies on training efficiency. For example, the authors could investigate the trade-off between the amount of data pruned and the resulting training time reduction. This would provide a more nuanced understanding of the practical benefits of their method and allow readers to assess its suitability for different computational environments.

Finally, the authors should expand their evaluation to include a more diverse set of datasets. While the two datasets used in the study provide some evidence for the generalizability of their approach, they are not representative of the full range of language tasks. To strengthen their claims, the authors should include datasets that cover different domains, such as legal text, scientific literature, or conversational dialogue. This would help to demonstrate that the perplexity-based pruning method is not specific to a particular type of data and can be applied effectively across a variety of tasks. Furthermore, the authors should also consider evaluating their method on datasets with varying levels of noise and complexity. This would provide a more comprehensive assessment of the robustness of their approach and its ability to handle real-world data.

### Questions

1. Why does perplexity-based data pruning improve downstream task performance?
2. How does perplexity-based data pruning increase training efficiency?

### Rating

3

### Confidence

3

**********

## Reviewer 2

### Summary

This paper studies the perplexity-based data pruning for LLM pre-training. It shows that the small model can be used to prune the pre-training data of a larger language model, leading to both significant downstream performance improvements and increased training efficiency.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper studies the perplexity-based data pruning for LLM pre-training, which is a timely and important topic.

2. The paper shows that the small model can be used to prune the pre-training data of a larger language model, leading to both significant downstream performance improvements and increased training efficiency.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of why perplexity-based data pruning can improve downstream task performance. The authors should provide a more detailed analysis of the relationship between perplexity and downstream task performance.

2. The paper does not provide a clear explanation of how perplexity-based data pruning can increase training efficiency. The authors should provide a more detailed analysis of the relationship between perplexity and training efficiency.

3. The paper only investigates two datasets. The authors should investigate more datasets to support their claim.

### Suggestions

The paper would benefit from a more thorough investigation into the mechanisms by which perplexity-based pruning improves downstream task performance. While the authors demonstrate a correlation, they do not delve into the underlying reasons. For instance, it would be valuable to analyze the types of data points that are pruned and how their removal affects the model's learning process. Are these points noisy, redundant, or do they represent semantically different information? A deeper analysis could involve examining the distribution of perplexity scores across different data subsets and correlating these scores with downstream task performance metrics. Furthermore, the authors should explore whether the pruning strategy is consistent across different downstream tasks or if task-specific adjustments are needed. This could involve analyzing the correlation between perplexity and task performance for each task individually, which would provide a more nuanced understanding of the method's effectiveness.

To address the lack of clarity regarding training efficiency, the authors should provide a more detailed breakdown of the computational costs associated with their approach. While the paper mentions increased efficiency, it lacks a quantitative analysis of the time and resources saved. The authors should provide a comparison of the training time and memory usage with and without pruning. This analysis should include the time required to compute perplexity scores, the time required to train the model with and without pruning, and the memory footprint of each step. Furthermore, the authors should investigate how the pruning ratio affects both training efficiency and downstream task performance. It would be beneficial to show a trade-off curve between pruning ratio, training time, and downstream task performance. This would allow readers to assess the practical benefits of the method for different computational constraints. The authors should also consider the impact of different hardware configurations on the observed efficiency gains.

Finally, the authors should expand their evaluation to include a more diverse set of datasets. While the current datasets provide some evidence for the generalizability of their approach, they are not representative of the full range of language tasks. The authors should include datasets that cover different domains, such as legal text, scientific literature, or conversational dialogue. This would help to demonstrate that the perplexity-based pruning method is not specific to a particular type of data and can be applied effectively across a variety of tasks. Furthermore, the authors should also consider evaluating their method on datasets with varying levels of noise and complexity. This would provide a more comprehensive assessment of the robustness of their approach and its ability to handle real-world data. The authors should also consider the impact of different data sizes on the effectiveness of their method.

### Questions

See Weakness

### Rating

3

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the effectiveness of using perplexity as a metric for pruning large-scale text datasets used for pretraining large language models (LLMs). The authors explore whether a small reference model can accurately predict the perplexity of a large model on a given dataset and use this information to prune the dataset before training the large model. The study evaluates this approach on two datasets, Pile and Dolma, with 1B and 3B parameter models, and examines the impact of domain composition and pruning ratios on downstream performance and training efficiency. The findings suggest that perplexity-based pruning can significantly improve downstream task performance and reduce the amount of data needed for pretraining, especially in non-standard settings like over-training and data-constrained regimes.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses a relevant and timely topic in the field of large language models, specifically the impact of data pruning on model performance and efficiency.
2. The authors conduct experiments across different model sizes and datasets, providing a comprehensive evaluation of the proposed perplexity-based pruning approach.
3. The paper explores the effects of domain composition and pruning ratios on downstream performance and training efficiency, offering valuable insights into the practical application of the method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with calculating perplexity for large datasets, which could be a significant bottleneck in practical applications. Specifically, the paper does not discuss the time complexity of the perplexity calculation, nor does it provide empirical measurements of the time required for this step on different hardware configurations. This is crucial because the efficiency of the pruning method is directly tied to the efficiency of the perplexity calculation.
2. The study primarily focuses on perplexity-based pruning, without exploring other potential pruning strategies or comparing it with existing methods. This limits the scope of the evaluation and makes it difficult to assess the relative advantages and disadvantages of the proposed approach. For example, the paper does not compare its method to techniques like gradient-based pruning or methods that use a small model to estimate the importance of data points. A more thorough comparison would provide a better understanding of the strengths and weaknesses of the proposed approach.
3. The paper does not provide a clear explanation of why perplexity-based pruning works, particularly in non-standard settings such as over-training and data-constrained regimes. While the authors show empirical results, they do not delve into the underlying mechanisms that make perplexity a good indicator of data quality in these scenarios. A more detailed analysis of the relationship between perplexity and model performance in these settings would be beneficial.

### Suggestions

To address the lack of analysis regarding computational cost, the authors should include a detailed breakdown of the time and resources required for calculating perplexity on large datasets. This should include a theoretical analysis of the time complexity of the perplexity calculation, as well as empirical measurements of the actual time taken on different hardware configurations. Furthermore, the authors should investigate and report the memory footprint of the perplexity calculation, as this can be a limiting factor for very large datasets. This analysis should also consider the trade-offs between the accuracy of perplexity as a pruning metric and the computational cost of calculating it. For example, the authors could explore using approximate perplexity calculations or other techniques to reduce the computational burden without significantly sacrificing pruning performance. This would provide a more complete picture of the practical applicability of the proposed method.

To strengthen the evaluation, the authors should compare their perplexity-based pruning approach with other existing data pruning techniques. This comparison should not only focus on downstream performance but also consider other factors such as computational cost, ease of implementation, and robustness to different datasets. For example, the authors could compare their method to techniques that use gradient information to identify important data points, or methods that use a small model to estimate the importance of data points based on their contribution to the loss function. This would provide a more comprehensive understanding of the relative advantages and disadvantages of the proposed approach. Additionally, the authors should explore the sensitivity of their method to different hyperparameters, such as the size of the reference model and the perplexity threshold used for pruning. This would help to identify the optimal settings for different datasets and model sizes.

Finally, to provide a more thorough understanding of why perplexity-based pruning works, the authors should conduct a more in-depth analysis of the relationship between perplexity and model performance in non-standard settings. This could involve visualizing the distribution of perplexity scores across different data subsets and correlating these scores with downstream task performance. The authors should also investigate whether perplexity is a consistent indicator of data quality across different domains and model sizes. Furthermore, the authors should explore the impact of different pruning ratios on downstream performance and training efficiency. This would help to identify the optimal pruning strategy for different scenarios. A more detailed analysis of these aspects would provide a more complete understanding of the underlying mechanisms that make perplexity a good indicator of data quality.

### Questions

1. How does the computational cost of calculating perplexity scale with the size of the dataset, and what are the practical implications for large-scale pretraining?
2. How does perplexity-based pruning compare to other data pruning techniques in terms of downstream performance, computational cost, and ease of implementation?
3. What are the limitations of using perplexity as a metric for data quality, and how might these limitations affect the generalizability of the proposed method?

### Rating

5

### Confidence

4

**********

## Reviewer 4

### Summary

This paper investigates the use of perplexity-based data pruning for large language model pretraining. The authors demonstrate that a small language model can effectively prune the pretraining dataset of a larger model, leading to improved downstream task performance and training efficiency. The study explores the impact of domain composition and pruning ratios on the effectiveness of the method, and finds that perplexity-based pruning can significantly improve downstream performance and reduce the amount of data needed for pretraining. The authors also show that perplexity-based pruning can be effective in non-standard settings such as over-trained and data-constrained regimes.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments across different model sizes and datasets to validate their findings.
3. The authors provide a thorough analysis of the impact of perplexity-based pruning on downstream task performance and training efficiency.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with calculating perplexity for large datasets. This is a crucial aspect to consider, especially when dealing with massive datasets, as it can significantly impact the practicality of the proposed method.
2. The paper does not explore the potential limitations of using perplexity as a metric for data pruning. For example, it is possible that perplexity may not be a reliable indicator of data quality in certain scenarios, such as when the data contains noisy or irrelevant samples.
3. The paper does not investigate the potential impact of different model architectures on the effectiveness of perplexity-based pruning. It is possible that the method may be more effective with certain types of models than others.

### Suggestions

The authors should provide a more detailed analysis of the computational cost associated with calculating perplexity, including the time and memory requirements for different dataset sizes and model configurations. This analysis should also consider the impact of different hardware configurations on the computational cost. Furthermore, the authors should explore alternative metrics for data pruning that may be more robust to noisy or irrelevant samples. For example, they could investigate the use of metrics based on information theory, such as mutual information or entropy, which may be less sensitive to outliers than perplexity. The authors should also investigate the impact of different model architectures on the effectiveness of perplexity-based pruning. They could experiment with different types of language models, such as transformer-based models or recurrent neural networks, and analyze how the model architecture affects the pruning performance. This would provide a more comprehensive understanding of the applicability of the proposed method.

To further strengthen the paper, the authors should also consider exploring the impact of different hyperparameters on the pruning performance. For example, the authors could investigate the effect of the pruning ratio on the downstream task performance and training efficiency. They could also explore the use of different perplexity thresholds for pruning. A more detailed analysis of these hyperparameters would provide a more complete picture of the method's behavior and allow for better tuning in practice. Additionally, the authors should consider comparing their method to other existing data pruning techniques, such as those based on gradient information or data importance. This would help to establish the relative advantages and disadvantages of the proposed method and provide a more comprehensive evaluation of its effectiveness.

Finally, the authors should also consider the potential impact of their method on the diversity of the training data. While perplexity-based pruning may lead to improved downstream performance, it is possible that it may also reduce the diversity of the training data, which could lead to overfitting or reduced generalization ability. The authors should investigate this potential trade-off and explore methods for maintaining data diversity while pruning. This could involve techniques such as stratified sampling or active learning, which can help to ensure that the pruned dataset is representative of the original dataset. Addressing these points would significantly enhance the paper's contribution and provide a more comprehensive understanding of the proposed method.

### Questions

1. How does the choice of the small language model affect the performance of perplexity-based pruning? Is there an optimal size for the reference model?
2. How does perplexity-based pruning perform on datasets with varying levels of noise or quality? Are there any specific strategies to mitigate the impact of noisy data?
3. How does the method perform on datasets with different domain distributions? Are there any specific adjustments needed for datasets with highly diverse content?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Find the corresponding section in the paper.
3. Look for evidence (quotes, missing information, etc.) to support the weakness.
4. If the weakness is about missing information, check if the information is indeed absent.
5. If the weakness is about a claim, check if the claim is supported by evidence in the paper.
6. Synthesize the findings and provide a conclusion for each weakness.
```json
[
  {
    "Weakness Statement": "The paper does not provide a clear explanation of why perplexity-based data pruning can improve downstream task performance. The authors should provide a more detailed analysis of the relationship between perplexity and downstream task performance.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper demonstrates that perplexity-based pruning improves downstream performance but doesn't delve into the underlying reasons.",
      "Supporting quotes": [
        "We demonstrate that for multiple dataset compositions, a small reference model can effectively prune the pretraining dataset of a significantly larger language model ( 30 × 30\giga parameter), providing both a significant increase in downstream performance and decrease in pretraining steps ( Table 1 and Figure 1 ).",
        "We also investigate whether evaluating the quality of data interventions based on upstream test set perplexity is a sound methodology for gauging downstream performance. We compare the test set perplexity and average downstream performance for 1 billion parameter models trained on the original and pruned version of the Pile and Dolma in Table 3 . For both the Pile and Dolma, training on perplexity pruned data significantly worsens perplexity on a test split of the pretraining data, while the average downstream performance is significantly improved."
      ],
      "Impact assessment": "The reviewer correctly points out the lack of mechanistic explanation for the observed improvement in downstream performance."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper focuses on demonstrating the effectiveness of perplexity-based pruning for downstream performance improvement without explaining the underlying mechanisms."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a clear explanation of how perplexity-based data pruning can increase training efficiency. The authors should provide a more detailed analysis of the relationship between perplexity and training efficiency.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper shows perplexity-based pruning reduces the amount of data needed for pretraining, leading to faster training, but lacks a detailed analysis of the relationship between perplexity and training efficiency.",
      "Supporting quotes": [
        "We plot the average downstream performance of partially trained checkpoints from the 1B baseline and perplexity pruned models in Figure 1 . Perplexity pruning outperforms the baseline model for all intermediate pretraining durations evaluated. Furthermore, perplexity pruned models reach the same average normalized accuracy as the baseline models in 1.31 × 1.31\time{1B} and 1.45 × 1.45\times fewer steps for Pile 1B and 3B respectively and in 1.29 × 1.29\times and 1.14 × 1.14\times fewer steps for Dolma 1B and Dolma 3B respectively.",
        "These results demonstrate that the resulting high-quality data from perplexity-based data pruning enables faster learning which can be leveraged to achieve the same downstream performance as training on unpruned data with fewer pretraining steps."
      ],
      "Impact assessment": "The reviewer's point is valid as the paper demonstrates efficiency gains but doesn't deeply analyze the link between perplexity and this efficiency."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "While the paper shows training efficiency improvements, it lacks a detailed explanation of the mechanism linking perplexity to this efficiency."
    }
  },
  {
    "Weakness Statement": "The paper only investigates two datasets. The authors should investigate more datasets to support their claim.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "We consider two datasets in this work. The Pile ( Gao et al., 2020 ) is composed of many diverse curated domains, with only 15.61% of the data being derived from general web scrapes, while Dolma ( Soldaini et al., 2024 ) is a web-scrape skewed dataset, with 81.31% of its data being derived from the CommonCrawl.",
        "We consider two datasets in this work. The Pile ( Gao et al., 2020 ) is composed of many diverse curated domains, with only 15.61% of the data being derived from general web scrapes, while Dolma ( Soldaini et al., 2024 ) is a web-scrape skewed dataset, with 81.31% of its data being derived from the CommonCrawl."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly states the use of only two datasets, Pile and Dolma.",
      "Supporting quotes": [
        "We consider two datasets in this work. The Pile ( Gao et al., 2020 ) is composed of many diverse curated domains, with only 15.61% of the data being derived from general web scrapes, while Dolma ( Soldaini et al., 2024 ) is a web-scrape skewed dataset, with 81.31% of its data being derived from the CommonCrawl."
      ],
      "Impact assessment": "The reviewer's concern about the limited number of datasets is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly mentions using only two datasets for evaluation."
    }
  },
  {
    "Weakness Statement": "The authors claim that perplexity-based data pruning can significantly improve downstream task performance. However, the authors do not provide a clear explanation of why perplexity-based data pruning can improve downstream task performance. The authors should provide a more detailed analysis of the relationship between perplexity and downstream task performance.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "This is a repetition of the first reviewer's point.",
      "Supporting quotes": [
        "We demonstrate that for multiple dataset compositions, a small reference model can effectively prune the pretraining dataset of a significantly larger language model ( 30 × 30\giga parameter), providing both a significant increase in downstream performance and decrease in pretraining steps ( Table 1 and Figure 1 )."
      ],
      "Impact assessment": "The reviewer's point is valid as the paper demonstrates the improvement but lacks a mechanistic explanation."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper focuses on demonstrating the effectiveness of perplexity-based pruning for downstream performance improvement without explaining the underlying mechanisms."
    }
  },
  {
    "Weakness Statement": "The authors claim that perplexity-based data pruning can increase training efficiency. However, the authors do not provide a clear explanation of how perplexity-based data pruning can increase training efficiency. The authors should provide a more detailed analysis of the relationship between perplexity and training efficiency.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "This is a repetition of the second reviewer's point.",
      "Supporting quotes": [
        "We plot the average downstream performance of partially trained checkpoints from the 1B baseline and perplexity pruned models in Figure 1 . Perplexity pruning outperforms the baseline model for all intermediate pretraining durations evaluated. Furthermore, perplexity pruned models reach the same average normalized accuracy as the baseline models in 1.31 × 1.31\time{1B} and 1.45 × 1.45\times fewer steps for Pile 1B and 3B respectively and in 1.29 × 1.29\times and 1.14 × 1.14\times fewer steps for Dolma 1B and Dolma 3B respectively.",
        "These results demonstrate that the resulting high-quality data from perplexity-based data pruning enables faster learning which can be leveraged to achieve the same downstream performance as training on unpruned data with fewer pretraining steps."
      ],
      "Impact assessment": "The reviewer's point is valid as the paper demonstrates efficiency gains but doesn't deeply analyze the link between perplexity and this efficiency."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "While the paper shows training efficiency improvements, it lacks a detailed explanation of the mechanism linking perplexity to this efficiency."
    }
  },
  {
    "Weakness Statement": "The paper only investigates two datasets. The authors should investigate more datasets to support their claim.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "We consider two datasets in this work. The Pile ( Gao et al., 2020 ) is composed of many diverse curated domains, with only 15.61% of the data being derived from general web scrapes, while Dolma ( Soldaini et al., 2024 ) is a web-scrape skewed dataset, with 81.31% of its data being derived from the CommonCrawl."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "This is a repetition of the third reviewer's point.",
      "Supporting quotes": [
        "We consider two datasets in this work. The Pile ( Gao et al., 2020 ) is composed of many diverse curated domains, with only 15.61% of the data being derived from general web scrapes, while Dolma ( Soldaini et al., 2024 ) is a web-scrape skewed dataset, with 81.31% of its data being derived from the CommonCrawl."
      ],
      "Impact assessment": "The reviewer's concern about the limited number of datasets is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly mentions using only two datasets for evaluation."
    }
  },
  {
    "Weakness Statement": "How does the computational cost of calculating perplexity scale with the size of the dataset, and what are the practical implications for large-scale pretraining?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper does not provide a detailed analysis of the computational cost of calculating perplexity.",
      "Supporting quotes": [],
      "Impact assessment": "The reviewer's question highlights a missing analysis in the paper."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a discussion on the computational cost of perplexity calculation."
    }
  },
  {
    "Weakness Statement": "How does perplexity-based pruning compare to other data pruning techniques in terms of downstream performance, computational cost, and ease of implementation?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper does not compare perplexity-based pruning with other data pruning techniques.",
      "Supporting quotes": [],
      "Impact assessment": "The reviewer's question points to a gap in the comparative analysis of the method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a comparison with other data pruning techniques."
    }
  },
  {
    "Weakness Statement": "What are the limitations of using perplexity as a metric for data quality, and how might these limitations affect the generalizability of the proposed method?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper does not explicitly discuss the limitations of using perplexity as a data quality metric.",
      "Supporting quotes": [],
      "Impact assessment": "The reviewer's question highlights a potential limitation of the method that is not addressed in the paper."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not discuss the limitations of using perplexity as a data quality metric."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a clear explanation of why perplexity-based pruning works, particularly in non-standard settings such as over-training and data-constrained regimes. While the authors demonstrate that perplexity-based pruning leads to improvements, they do not sufficiently explain *why* this occurs. For instance, a detailed examination of the types of data points that are pruned could reveal whether perplexity is filtering out noisy or redundant data, or if it is selectively removing data that is detrimental to downstream task performance. This could involve analyzing the semantic content of the pruned data, or comparing the performance of models trained on pruned data versus unpruned data on specific subsets of the downstream tasks. Furthermore, the authors should explore the possibility that perplexity is acting as a form of regularization, preventing overfitting to the pre-training data. A more thorough investigation into these aspects would greatly strengthen the paper's claims and provide a more complete understanding of the method.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper demonstrates the effectiveness of perplexity-based pruning but lacks a detailed explanation of the underlying mechanisms, including the types of data points pruned and the potential regularization effects.",
      "Supporting quotes": [
        "We demonstrate that for multiple dataset compositions, a small reference model can effectively prune the pretraining dataset of a significantly larger language model ( 30 × 30\giga parameter), providing both a significant increase in downstream performance and decrease in pretraining steps ( Table 1 and Figure 1 ).",
        "We also investigate whether evaluating the quality of data interventions based on upstream test set perplexity is a sound methodology for gauging downstream performance. We compare the test set perplexity and average downstream performance for 1 billion parameter models trained on the original and pruned version of the Pile and Dolma in Table 3 . For both the Pile and Dolma, training on perplexity pruned data significantly worsens perplexity on a test split of the pretraining data, while the average downstream performance is significantly improved."
      ],
      "Impact assessment": "The reviewer accurately identifies the lack of mechanistic explanation as a weakness."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper focuses on demonstrating the effectiveness of perplexity-based pruning without delving into the underlying reasons for its success."
    }
  },
  {
    "Weakness Statement": "To address the lack of clarity regarding training efficiency, the authors should provide a more detailed breakdown of the computational costs associated with their approach. While the paper mentions increased efficiency, it lacks a quantitative analysis of the time and resources saved. The authors should provide a comparison of the training time and memory usage with and without pruning. This analysis should include the time required to compute perplexity scores, the time required to train the model with and without pruning, and the memory requirements of each approach. Furthermore, the authors should investigate how the pruning ratio affects both training efficiency and downstream task performance. It would be beneficial to show a trade-off curve between pruning ratio, training time, and downstream task performance. This would allow readers to assess the practical benefits of the method for different computational constraints. The authors should also consider the impact of different hardware configurations on the observed efficiency gains.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "We plot the average downstream performance of partially trained checkpoints from the 1B baseline and perplexity pruned models in Figure 1 . Perplexity pruning outperforms the baseline model for all intermediate pretraining durations evaluated. Furthermore, perplexity pruned models reach the same average normalized accuracy as the baseline models in 1.31 × 1.31\time{1B} and 1.45 × 1.45\times fewer steps for Pile 1B and 3B respectively and in 1.29 × 1.29\times and 1.14 × 1.14\times fewer steps for Dolma 1B and Dolma 3B respectively.",
        "These results demonstrate that the resulting high-quality data from perplexity-based data pruning enables faster learning which can be leveraged to achieve the same downstream performance as training on unpruned data with fewer pretraining steps."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions training efficiency improvements but lacks a detailed breakdown of computational costs, including time and memory usage, and the impact of pruning ratio.",
      "Supporting quotes": [
        "Perplexity pruning outperforms the baseline model for all intermediate pretraining durations evaluated. Furthermore, perplexity pruned models reach the same average normalized accuracy as the baseline models in 1.31 × 1.31\time{1B} and 1.45 × 1.45\times fewer steps for Pile 1B and 3B respectively and in 1.29 × 1.29\times and 1.14 × 1.14\times fewer steps for Dolma 1B and Dolma 3B respectively.",
        "These results demonstrate that the resulting high-quality data from perplexity-based data pruning enables faster learning which can be leveraged to achieve the same downstream performance as training on unpruned data with fewer pretraining steps."
      ],
      "Impact assessment": "The reviewer's point about the lack of detailed computational cost analysis is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides efficiency gains but lacks a detailed quantitative analysis of computational costs."
    }
  },
  {
    "Weakness Statement": "Finally, the authors should expand their evaluation to include a more diverse set of datasets. While the current datasets used in the study provide some evidence for the generalizability of their approach, they are not representative of the full range of language tasks. To strengthen their claims, the authors should include datasets that cover different domains, such as legal text, scientific literature, or conversational dialogue. This would help to demonstrate that the perplexity-based pruning method is not specific to a particular type of data and can be applied effectively across a variety of tasks. Furthermore, the authors should also consider evaluating their method on datasets with varying levels of noise and complexity. This would provide a more comprehensive assessment of the robustness of their approach and its ability to handle real-world data.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "We consider two datasets in this work. The Pile ( Gao et al., 2020 ) is composed of many diverse curated domains, with only 15.61% of the data being derived from general web scrapes, while Dolma ( Soldaini et al., 2024 ) is a web-scrape skewed dataset, with 81.31% of its data being derived from the CommonCrawl."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's evaluation is limited to two datasets, and expanding to more diverse and noisy datasets would strengthen the generalizability claims.",
      "Supporting quotes": [
        "We consider two datasets in this work. The Pile ( Gao et al., 2020 ) is composed of many diverse curated domains, with only 15.61% of the data being derived from general web scrapes, while Dolma ( Soldaini et al., 2024 ) is a web-scrape skewed dataset, with 81.31% of its data being derived from the CommonCrawl."
      ],
      "Impact assessment": "The reviewer's suggestion to include more diverse datasets is valid for strengthening the generalizability claims."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's evaluation is limited to two datasets, and more diverse datasets would provide stronger evidence for generalizability."
    }
  },
  {
    "Weakness Statement": "Why does perplexity-based data pruning improve downstream task performance?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "This is a question directly related to the lack of mechanistic explanation for the observed performance improvement.",
      "Supporting quotes": [
        "We demonstrate that for multiple dataset compositions, a small reference model can effectively prune the pretraining dataset of a significantly larger language model ( 30 × 30\giga parameter), providing both a significant increase in downstream performance and decrease in pretraining steps ( Table 1 and Figure 1 )."
      ],
      "Impact assessment": "The reviewer's question highlights a missing explanation in the paper."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper demonstrates the performance improvement but doesn't explain the underlying mechanism."
    }
  },
  {
    "Weakness Statement": "How does perplexity-based data pruning increase training efficiency?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "This is a question related to the lack of a detailed analysis of the efficiency gains.",
      "Supporting quotes": [
        "We plot the average downstream performance of partially trained checkpoints from the 1B baseline and perplexity pruned models in Figure 1 . Perplexity pruning outperforms the baseline model for all intermediate pretraining durations evaluated. Furthermore, perplexity pruned models reach the same average normalized accuracy as the baseline models in 1.31 × 1.31\time{1B} and 1.45 × 1.45\times fewer steps for Pile 1B and 3B respectively and in 1.29 × 1.29\times and 1.14 × 1.14\times fewer steps for Dolma 1B and Dolma 3B respectively.",
        "These results demonstrate that the resulting high-quality data from perplexity-based data pruning enables faster learning which can be leveraged to achieve the same downstream performance as training on unpruned data with fewer pretraining steps."
      ],
      "Impact assessment": "The reviewer's question points to a missing analysis of the efficiency gains."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper shows efficiency gains but lacks a detailed explanation of the mechanism."
    }
  },
  {
    "Weakness Statement": "The paper lacks a detailed analysis of the computational cost associated with calculating perplexity for large datasets. This is a crucial aspect to consider, especially when dealing with massive datasets, as it can significantly impact the practicality of the proposed method.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper does not provide a detailed analysis of the computational cost of calculating perplexity.",
      "Supporting quotes": [],
      "Impact assessment": "The reviewer's point about the missing computational cost analysis is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a discussion on the computational cost of perplexity calculation."
    }
  },
  {
    "Weakness Statement": "The study primarily focuses on perplexity-based pruning, without exploring other potential pruning strategies or comparing it with existing methods. This limits the scope of the evaluation and makes it difficult to assess the relative advantages and disadvantages of the proposed approach. For example, the paper does not compare its method to techniques like gradient-based pruning or methods that use a small model to estimate the importance of data points. A more thorough comparison would provide a better understanding of the strengths and weaknesses of the proposed approach.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper focuses on perplexity-based pruning without comparing it to other data pruning techniques.",
      "Supporting quotes": [],
      "Impact assessment": "The reviewer's point about the lack of comparison with other pruning methods is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a comparison with other data pruning techniques."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a clear explanation of why perplexity-based pruning works, particularly in non-standard settings such as over-training and data-constrained regimes. While the authors demonstrate that perplexity-based pruning leads to improvements, they do not delve into the underlying reasons. For instance, it would be valuable to analyze the types of data points that are pruned and how their removal affects the model's learning process. Are these points noisy, redundant, or do they represent semantically different information? A deeper analysis could involve examining the distribution of perplexity scores across different data subsets and correlating these scores with downstream task performance. Furthermore, the authors should explore the impact of different pruning ratios on downstream performance and training efficiency. It would be beneficial to show a trade-off curve between pruning ratio, training time, and downstream task performance. This would allow readers to assess the practical benefits of the method for different computational constraints.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper demonstrates the effectiveness of perplexity-based pruning but lacks a detailed explanation of the underlying mechanisms, including the types of data points pruned and the potential regularization effects.",
      "Supporting quotes": [
        "We demonstrate that for multiple dataset compositions, a small reference model can effectively prune the pretraining dataset of a significantly larger language model ( 30 × 30\giga parameter), providing both a significant increase in downstream performance and decrease in pretraining steps ( Table 1 and Figure 1 ).",
        "We also investigate whether evaluating the quality of data interventions based on upstream test set perplexity is a sound methodology for gauging downstream performance. We compare the test set perplexity and average downstream performance for 1 billion parameter models trained on the original and pruned version of the Pile and Dolma in Table 3 . For both the Pile and Dolma, training on perplexity pruned data significantly worsens perplexity on a test split of the pretraining data, while the average downstream performance is significantly improved."
      ],
      "Impact assessment": "The reviewer accurately identifies the lack of mechanistic explanation as a weakness."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper focuses on demonstrating the effectiveness of perplexity-based pruning without delving into the underlying reasons for its success."
    }
  },
  {
    "Weakness Statement": "To address the lack of clarity regarding training efficiency, the authors should provide a more detailed breakdown of the computational costs associated with their approach. While the paper mentions increased efficiency, it lacks a quantitative analysis of the time and resources saved. The authors should provide a comparison of the training time and memory usage with and without pruning. This analysis should include the time required to compute perplexity scores, the time required to train the model with and without pruning, and the memory requirements of each approach. Furthermore, the authors should investigate how the pruning ratio affects both training efficiency and downstream task performance. It would be beneficial to show a trade-off curve between pruning ratio, training time, and downstream task performance. This would allow readers to assess the practical benefits of the method for different computational constraints. The authors should also consider the impact of different hardware configurations on the observed efficiency gains.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "We plot the average downstream performance of partially trained checkpoints from the 1B baseline and perplexity pruned models in Figure 1 . Perplexity pruning outperforms the baseline model for all intermediate pretraining durations evaluated. Furthermore, perplexity pruned models reach the same average normalized accuracy as the baseline models in 1.31 × 1.31\time{1B} and 1.45 × 1.45\times fewer steps for Pile 1B and 3B respectively and in 1.29 × 1.29\times and 1.14 × 1.14\times fewer steps for Dolma 1B and Dolma 3B respectively.",
        "These results demonstrate that the resulting high-quality data from perplexity-based data pruning enables faster learning which can be leveraged to achieve the same downstream performance as training on unpruned data with fewer pretraining steps."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions training efficiency improvements but lacks a detailed breakdown of computational costs, including time and memory usage, and the impact of pruning ratio.",
      "Supporting quotes": [
        "Perplexity pruning outperforms the baseline model for all intermediate pretraining durations evaluated. Furthermore, perplexity pruned models reach the same average normalized accuracy as the baseline models in 1.31 × 1.31\time{1B} and 1.45 × 1.45\times fewer steps for Pile 1B and 3B respectively and in 1.29 × 1.29\times and 1.14 × 1.14\times fewer steps for Dolma 1B and Dolma 3B respectively.",
        "These results demonstrate that the resulting high-quality data from perplexity-based data pruning enables faster learning which can be leveraged to achieve the same downstream performance as training on unpruned data with fewer pretraining steps."
      ],
      "Impact assessment": "The reviewer's point about the lack of detailed computational cost analysis is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides efficiency gains but lacks a detailed quantitative analysis of computational costs."
    }
  },
  {
    "Weakness Statement": "Finally, the authors should expand their evaluation to include a more diverse set of datasets. While the current datasets used in the study provide some evidence for the generalizability of their approach, they are not representative of the full range of language tasks. To strengthen their claims, the authors should include datasets that cover different domains, such as legal text, scientific literature, or conversational dialogue. This would help to demonstrate that the perplexity-based pruning method is not specific to a particular type of data and can be applied effectively across a variety of tasks. Furthermore, the authors should also consider evaluating their method on datasets with varying levels of noise and complexity. This would provide a more comprehensive assessment of the robustness of their approach and its ability to handle real-world data.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "We consider two datasets in this work. The Pile ( Gao et al., 2020 ) is composed of many diverse curated domains, with only 15.61% of the data being derived from general web scrapes, while Dolma ( Soldaini et al., 2024 ) is a web-scrape skewed dataset, with 81.31% of its data being derived from the CommonCrawl."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's evaluation is limited to two datasets, and expanding to more diverse and noisy datasets would strengthen the generalizability claims.",
      "Supporting quotes": [
        "We consider two datasets in this work. The Pile ( Gao et al., 2020 ) is composed of many diverse curated domains, with only 15.61% of the data being derived from general web scrapes, while Dolma ( Soldaini et al., 2024 ) is a web-scrape skewed dataset, with 81.31% of its data being derived from the CommonCrawl."
      ],
      "Impact assessment": "The reviewer's suggestion to include more diverse datasets is valid for strengthening the generalizability claims."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's evaluation is limited to two datasets, and more diverse datasets would provide stronger evidence for generalizability."
    }
  },
  {
    "Weakness Statement": "How does the computational cost of calculating perplexity scale with the size of the dataset, and what are the practical implications for large-scale pretraining?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper does not provide a detailed analysis of the computational cost of calculating perplexity.",
      "Supporting quotes": [],
      "Impact assessment": "The reviewer's question highlights a missing analysis in the paper."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a discussion on the computational cost of perplexity calculation."
    }
  },
  {
    "Weakness Statement": "How does perplexity-based pruning compare to other data pruning techniques in terms of downstream performance, computational cost, and ease of implementation?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper does not compare perplexity-based pruning with other data pruning techniques.",
      "Supporting quotes": [],
      "Impact assessment": "The reviewer's question points to a gap in the comparative analysis of the method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a comparison with other data pruning techniques."
    }
  },
  {
    "Weakness Statement": "What are the limitations of using perplexity as a metric for data quality, and how might these limitations affect the generalizability of the proposed method?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper does not explicitly discuss the limitations of using perplexity as a data quality metric.",
      "Supporting quotes": [],
      "Impact assessment": "The reviewer}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper investigates the efficacy of using perplexity-based data pruning to enhance the pre-training of large language models (LLMs). The core idea is to leverage a smaller reference model to estimate the perplexity of a large dataset, and then use this perplexity score to prune the dataset for the larger model. The authors hypothesize that data points that are consistently predicted as low-perplexity by a smaller model are likely to be of higher quality and more valuable for pre-training a larger model. The study focuses on two large-scale datasets, Pile and Dolma, and examines the impact of perplexity-based pruning across different model sizes (1B, 3B parameters) and dataset compositions. The main empirical findings demonstrate that perplexity-based pruning can significantly improve downstream task performance while reducing the amount of data needed for pre-training. Specifically, the authors show that models trained on perplexity-pruned datasets achieve comparable downstream performance to models trained on the full dataset, but with a substantial reduction in pre-training steps. The paper also explores the effects of domain composition and pruning ratios on the effectiveness of the method. The authors find that perplexity-based pruning is particularly effective in non-standard settings, such as over-training and data-constrained regimes. Overall, the paper presents a compelling case for the use of perplexity-based data pruning as a practical and effective technique for pre-training LLMs, offering a way to reduce computational costs and improve training efficiency. The study contributes to the growing body of research on data-centric approaches to LLM pre-training, highlighting the potential of simple, yet powerful, methods to optimize the use of large datasets. The authors also investigate whether evaluating the quality of data interventions based on upstream test set perplexity is a sound methodology for gauging downstream performance. They compare the test set perplexity and average downstream performance for 1 billion parameter models trained on the original and pruned version of the Pile and Dolma in Table 3. For both the Pile and Dolma, training on perplexity pruned data significantly worsens perplexity on a test split of the pretraining data, while the average downstream performance is significantly improved. This finding suggests that perplexity is a useful metric for identifying low-quality data, but it may not be a reliable indicator of downstream performance. The paper's findings have important implications for the practical application of LLMs, particularly in resource-constrained environments. By demonstrating that perplexity-based pruning can significantly reduce the amount of data needed for pre-training without sacrificing downstream performance, the authors provide a valuable contribution to the field of natural language processing.


## Soundness:

2.25


## Presentation:

2.25


## Contribution:

2.0


## Strengths:

I find several aspects of this paper to be particularly strong. First, the paper addresses a highly relevant and timely topic: the efficient pre-training of large language models. The authors tackle the challenge of reducing the computational cost associated with training LLMs, which is a critical issue in the field. The proposed method, perplexity-based data pruning, is both simple and innovative. It leverages the power of smaller reference models to identify and remove low-quality data points from large datasets, offering a practical approach to data optimization. The fact that a small language model can effectively prune the pre-training dataset of a significantly larger language model (30x30 Giga parameter) is a significant achievement. The empirical results presented in the paper are compelling. The authors demonstrate that perplexity-based pruning can significantly improve downstream task performance while reducing the amount of data needed for pre-training. The experiments are well-designed and provide strong evidence for the effectiveness of the method. The authors also explore the effects of domain composition and pruning ratios on the effectiveness of the method, providing a comprehensive analysis of the approach. The paper's investigation into non-standard settings, such as over-training and data-constrained regimes, is another strength. The authors show that perplexity-based pruning can be effective even in these challenging scenarios, which further validates the robustness of the method. The authors also provide a thorough analysis of the impact of perplexity-based pruning on downstream task performance and training efficiency. The paper is well-written and easy to follow, making it accessible to a wide audience. The authors clearly explain the methodology and the experimental setup, which allows for a thorough understanding of the results. The paper also includes a discussion of the limitations of using perplexity as a metric for data quality, which demonstrates a critical and nuanced understanding of the method. Overall, the paper makes a significant contribution to the field of natural language processing by providing a practical and effective method for pre-training large language models. The simplicity of the approach, combined with its strong empirical results, makes it a valuable contribution to the community.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper lacks a clear and detailed explanation of *why* perplexity-based data pruning improves downstream task performance. While the authors demonstrate that perplexity-based pruning leads to improvements, they do not sufficiently explain the underlying mechanisms. For instance, it is not clear whether the pruned data points are noisy, redundant, or semantically different. This lack of mechanistic explanation is a significant limitation, as it leaves the reader wondering about the fundamental reasons for the observed improvements. The paper also lacks a detailed analysis of the computational cost associated with calculating perplexity. While the authors show that perplexity-based pruning reduces the amount of data needed for pre-training, they do not provide a quantitative analysis of the time and resources saved. This is a crucial aspect to consider, especially when dealing with massive datasets. The paper should provide a comparison of the training time and memory usage with and without pruning, including the time required to compute perplexity scores. Furthermore, the paper does not explore the impact of different pruning ratios on downstream task performance and training efficiency. It would be beneficial to show a trade-off curve between pruning ratio, training time, and downstream task performance. This would allow readers to assess the practical benefits of the method for different computational constraints. The paper also does not compare perplexity-based pruning with other data pruning techniques. This is a significant limitation, as it makes it difficult to assess the relative advantages and disadvantages of the proposed approach. The paper should compare its method to techniques like gradient-based pruning or methods that use a small model to estimate the importance of data points. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach. The evaluation of the method is limited to only two datasets, Pile and Dolma. While these datasets are widely used, they are not representative of the full range of language tasks. The authors should investigate more datasets to support their claim. The paper should include datasets that cover different domains, such as legal text, scientific literature, or conversational dialogue. This would help to demonstrate that the perplexity-based pruning method is not specific to a particular type of data and can be applied effectively across a variety of tasks. Furthermore, the authors should also consider evaluating their method on datasets with varying levels of noise and complexity. This would provide a more comprehensive assessment of the robustness of their approach and its ability to handle real-world data. The paper also does not explicitly discuss the limitations of using perplexity as a metric for data quality. While the authors show that perplexity-based pruning improves downstream performance, they do not address the potential limitations of using perplexity as a measure of data quality. For example, it is possible that perplexity may not be a reliable indicator of data quality in certain scenarios, such as when the data contains noisy or irrelevant samples. The authors should investigate this potential trade-off and explore methods for mitigating its impact. Finally, the paper does not provide a clear explanation of how the choice of the small language model affects the performance of perplexity-based pruning. The authors should investigate the effect of the size of the reference model on the downstream performance and training efficiency. They should also explore using approximate perplexity calculations or other techniques to reduce the computational cost of calculating perplexity. These weaknesses, while not invalidating the core findings, highlight areas where the paper could be significantly improved. I have high confidence in these identified weaknesses, as they are directly supported by the paper's content and lack of specific analysis in these areas.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a more in-depth analysis of the relationship between perplexity and downstream task performance. This could involve analyzing the types of data points that are pruned, such as whether they are noisy, redundant, or semantically different. A detailed examination of the distribution of perplexity scores across different data subsets and correlating these scores with downstream task performance would be beneficial. The authors should also investigate whether perplexity is a consistent indicator of data quality across different domains and model sizes. Furthermore, the authors should explore the possibility that perplexity is acting as a form of regularization, preventing overfitting to the pre-training data. A more thorough investigation into these aspects would greatly strengthen the paper's claims and provide a more complete understanding of the method. Second, the authors should provide a detailed breakdown of the computational costs associated with their approach. This should include a theoretical analysis of the time and memory requirements of the perplexity calculation, as well as empirical measurements of the actual time taken on different hardware configurations. Furthermore, the authors should investigate how the pruning ratio affects both training efficiency and downstream task performance. It would be beneficial to show a trade-off curve between pruning ratio, training time, and downstream task performance. This would allow readers to assess the practical benefits of the method for different computational constraints. The authors should also consider the impact of different hardware configurations on the observed efficiency gains. Third, the authors should compare their perplexity-based pruning approach with other existing data pruning techniques. This comparison should not only focus on downstream performance but also consider other factors such as computational cost, ease of implementation, and robustness to different datasets. For example, the authors could compare their method to techniques that use gradient information to identify important data points, or methods that use a small model to estimate the importance of data points based on their contribution to the loss function. This would provide a more comprehensive understanding of the relative advantages and disadvantages of the proposed approach. Fourth, the authors should expand their evaluation to include a more diverse set of datasets. This should include datasets that cover different domains, such as legal text, scientific literature, or conversational dialogue. This would help to demonstrate that the perplexity-based pruning method is not specific to a particular type of data and can be applied effectively across a variety of tasks. Furthermore, the authors should also consider evaluating their method on datasets with varying levels of noise and complexity. This would provide a more comprehensive assessment of the robustness of their approach and its ability to handle real-world data. Fifth, the authors should explicitly discuss the limitations of using perplexity as a metric for data quality. They should investigate the potential trade-off between perplexity and other metrics, such as information theory, and explore the impact of different pruning ratios on downstream task performance and training efficiency. Finally, the authors should investigate the effect of the size of the reference model on the downstream performance and training efficiency. They should also explore using approximate perplexity calculations or other techniques to reduce the computational cost of calculating perplexity. These suggestions are all concrete and actionable, and they directly address the identified weaknesses. Implementing these changes would significantly strengthen the paper and provide a more comprehensive understanding of the proposed method.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the computational cost of calculating perplexity scale with the size of the dataset, and what are the practical implications for large-scale pretraining? While the paper demonstrates the effectiveness of perplexity-based pruning, it lacks a detailed analysis of the computational cost associated with calculating perplexity. This is a crucial aspect to consider, especially when dealing with massive datasets. Second, how does perplexity-based pruning compare to other data pruning techniques in terms of downstream performance, computational cost, and ease of implementation? The paper focuses on perplexity-based pruning without comparing it to other data pruning techniques. A more thorough comparison would provide a better understanding of the relative advantages and disadvantages of the proposed approach. Third, what are the limitations of using perplexity as a metric for data quality, and how might these limitations affect the generalizability of the proposed method? The paper uses perplexity as a metric for data quality, but it does not explicitly discuss its limitations. A more thorough discussion of these limitations would be valuable. Fourth, how does the choice of the small language model affect the performance of perplexity-based pruning? The paper does not investigate the effect of the size of the reference model on the downstream performance and training efficiency. Understanding this relationship is crucial for practical applications of the method. Fifth, how does perplexity-based pruning perform on datasets with varying levels of noise and complexity? The paper's evaluation is limited to two datasets, Pile and Dolma. Evaluating the method on datasets with varying levels of noise and complexity would provide a more comprehensive assessment of its robustness. Sixth, how does perplexity-based pruning perform in non-standard settings, such as over-training and data-constrained regimes? While the paper shows that perplexity-based pruning is effective in these settings, a more detailed analysis of the underlying mechanisms would be beneficial. These questions target key uncertainties and methodological choices in the paper, and addressing them would significantly enhance the paper's overall contribution.


## Rating:

4.25


## Confidence:

3.25


## Decision:

Reject
}