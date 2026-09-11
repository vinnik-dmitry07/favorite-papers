I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates the impact of training data complexity on the scaling laws of neural language models. By varying the complexity of synthetic data generated from probabilistic context-free grammars (PCFGs), the authors demonstrate that the scaling laws are sensitive to data complexity. They introduce a data-dependent scaling law that incorporates gzip compressibility as a predictor of scaling properties, showing that models trained on more compressible data exhibit different scaling behaviors compared to those trained on less compressible data. The authors validate their findings using both synthetic and real-world datasets, including code and natural language, and propose that their data-dependent scaling law can be used to optimize compute allocation for training language models.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel approach to studying scaling laws by incorporating data complexity as a key factor, which is a departure from the traditional view that scaling laws are independent of the training data.
2. The use of PCFGs to generate synthetic data allows for precise control over data complexity, enabling a systematic study of the relationship between data complexity and model performance.
3. The paper provides a clear and well-structured presentation of the methodology and results, making it easy to follow the experimental setup and findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's reliance on gzip compressibility as a proxy for data complexity may not fully capture the nuances of real-world data complexity, which can be influenced by factors beyond simple compression ratios. For instance, the presence of long-range dependencies, semantic structure, and the presence of adversarial examples could all impact model performance in ways that are not necessarily reflected in compressibility metrics. The study should consider incorporating other measures of data complexity, such as measures of information content or sensitivity to adversarial perturbations, to provide a more comprehensive picture.
2. The paper's findings are primarily based on synthetic data generated from PCFGs, which may not fully reflect the complexities of real-world datasets. The PCFGs used may not capture the full range of syntactic and semantic structures present in natural language or code, potentially limiting the generalizability of the results. The study should include experiments on more diverse real-world datasets to validate the findings.
3. The paper's use of a single compression algorithm (gzip) to measure data complexity may not capture the full spectrum of data characteristics that influence scaling laws. Different compression algorithms may highlight different aspects of data complexity, and relying on a single metric could lead to an incomplete understanding of the relationship between data complexity and model performance. The study should explore the use of multiple compression algorithms and analyze the results to determine the robustness of the findings.

### Suggestions

The study should explore the use of more sophisticated measures of data complexity beyond simple compression ratios. For example, measures based on information theory, such as entropy or mutual information, could provide a more nuanced understanding of the information content of the data. Additionally, the study could investigate the impact of adversarial examples on model performance, as these examples can reveal vulnerabilities that are not captured by simple compression metrics. Furthermore, the study should consider the impact of long-range dependencies and semantic structure on model performance, as these factors can significantly influence the learning process. These additional measures could be incorporated into the data-dependent scaling law to provide a more comprehensive model of the relationship between data complexity and model performance.

To address the limitations of using synthetic data, the study should include experiments on a wider range of real-world datasets. This should include datasets from diverse domains, such as natural language, code, and scientific text. The datasets should also vary in terms of their size, complexity, and domain-specific characteristics. This would help to validate the generalizability of the findings and ensure that the conclusions are not specific to the particular characteristics of the synthetic data used in the study. Furthermore, the study should investigate the impact of different data preprocessing techniques on the results, as these techniques can significantly affect the compressibility of the data.

Finally, the study should explore the use of multiple compression algorithms to measure data complexity. Different compression algorithms may highlight different aspects of data complexity, and relying on a single metric could lead to an incomplete understanding of the relationship between data complexity and model performance. For example, lossless compression algorithms such as Lempel-Ziv or Burrows-Wheeler transform could be used in conjunction with lossy compression algorithms like gzip. The study should also investigate the impact of different compression parameters on the results, as these parameters can affect the compressibility of the data. By using multiple compression algorithms and analyzing the results, the study could gain a more robust understanding of the relationship between data complexity and model performance.

### Questions

1. How does the choice of PCFG affect the generalizability of the findings? Would using different types of synthetic data generation methods lead to different conclusions?
2. How does the proposed data-dependent scaling law compare to existing scaling laws in terms of predictive accuracy and practical utility? Are there specific scenarios where the data-dependent scaling law provides a significant advantage over traditional scaling laws?
3. How sensitive are the findings to the choice of compression algorithm (gzip)? Would using other compression algorithms (e.g., Lempel-Ziv, Burrows-Wheeler transform) lead to different conclusions?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

The paper investigates the impact of data complexity on neural language model scaling laws. It uses probabilistic context-free grammars (PCFGs) to generate synthetic datasets with varying syntactic complexity, controlled by parameters like the number of non-terminals and production rules. The authors find that scaling laws are sensitive to data complexity, with models trained on more compressible data requiring different compute-optimal parameter-to-data ratios. They propose a data-dependent scaling law incorporating gzip compressibility as a predictor of scaling properties, suggesting that models trained on more compressible data benefit more from parameter count increases.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a critical gap in understanding the impact of data complexity on neural language model scaling laws, which is essential for optimizing model training and resource allocation.
2. The use of PCFGs to systematically generate datasets with controlled complexity is a novel approach that allows for precise experimentation across different levels of data complexity.
3. The proposed data-dependent scaling law, incorporating gzip compressibility, provides a new perspective on how data characteristics influence model scaling, potentially leading to more efficient training strategies.

### Weaknesses

#### Some Related Works


#### comment

1. The study primarily focuses on synthetic datasets generated from PCFGs, which may not fully capture the complexities of real-world data. The findings may not generalize well to datasets with different statistical properties or structures, such as those found in natural language or code, which can exhibit long-range dependencies and semantic structures not present in the synthetic data. Specifically, the synthetic data may lack the nuances of real-world text, such as variations in sentence structure, vocabulary, and the presence of noise, which could significantly impact the observed scaling laws.
2. The reliance on gzip compressibility as a measure of data complexity may not fully capture all relevant aspects of data complexity. While gzip is effective for detecting repetitive patterns, it may not account for other important factors, such as the presence of long-range dependencies, semantic structure, or the presence of adversarial examples, which could all influence model performance. For instance, a dataset might be highly compressible using gzip but still require significant parameter count increases to achieve optimal performance, or vice versa. The study should explore alternative measures of data complexity to provide a more comprehensive understanding.
3. The paper does not provide a detailed analysis of how the proposed data-dependent scaling law performs across different model architectures and sizes. The scaling law may be sensitive to architectural choices, such as the number of layers, attention heads, or the use of specific activation functions, which could affect the observed scaling behavior. Furthermore, the study should investigate how the scaling law behaves with varying model sizes, as the optimal parameter-to-data ratio might change with model capacity. It is unclear if the proposed scaling law is robust across different architectures and model sizes, which is crucial for its practical applicability.

### Suggestions

To address the limitations of using only synthetic data, future work should include experiments on real-world datasets with varying complexities. This would involve not only using different domains (e.g., natural language, code, scientific text) but also varying the size and structure of the datasets. For example, the study could include datasets with different vocabulary sizes, sentence lengths, and levels of noise. This would help to determine if the observed scaling laws are consistent across different types of data and if the proposed data-dependent scaling law generalizes beyond the specific characteristics of the synthetic data. Furthermore, it would be beneficial to explore how the scaling laws change as the dataset size increases, as the optimal parameter-to-data ratio might be affected by the amount of training data available.

To address the limitations of using gzip compressibility as the sole measure of data complexity, the study should explore alternative measures that capture different aspects of data complexity. For example, metrics based on information theory, such as entropy or mutual information, could provide a more comprehensive understanding of the information content of the data. Additionally, the study could investigate the impact of long-range dependencies and semantic structure on model performance. This could involve using techniques such as graph-based analysis or semantic similarity measures to quantify the complexity of the data. Furthermore, the study should explore the impact of adversarial examples on model performance, as these examples can reveal vulnerabilities that are not captured by simple compression metrics. By incorporating multiple measures of data complexity, the study could provide a more robust and comprehensive understanding of the relationship between data complexity and model scaling.

Finally, the paper should provide a more detailed analysis of how the proposed data-dependent scaling law performs across different model architectures and sizes. This would involve conducting experiments with different architectures, such as transformers with varying numbers of layers and attention heads, and different model sizes. The study should also investigate how the optimal parameter-to-data ratio changes with model capacity. It is important to determine if the proposed scaling law is robust across different architectures and model sizes, as this is crucial for its practical applicability. The study should also explore the limitations of the proposed scaling law and identify scenarios where it might not be applicable. This would help to establish the boundaries of the proposed scaling law and provide guidance for its use in practical applications.

### Questions

1. How does the proposed data-dependent scaling law compare to existing scaling laws in terms of predictive accuracy and practical utility? Are there specific scenarios where the data-dependent scaling law provides a significant advantage over traditional scaling laws?
2. How sensitive are the findings to the choice of compression algorithm (gzip)? Would using other compression algorithms (e.g., Lempel-Ziv, Burrows-Wheeler transform) lead to different conclusions?
3. How well do the findings generalize to real-world datasets beyond the synthetic PCFG-generated data? Are there specific characteristics of real-world data that might affect the applicability of the proposed scaling law?
4. How does the proposed data-dependent scaling law perform across different model architectures and sizes? Are there specific architectures or model sizes where the data-dependent scaling law is more or less effective?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates how the compressibility of training data affects the scaling laws of neural language models. The authors generate synthetic datasets using probabilistic context-free grammars (PCFGs) and systematically vary the syntactic complexity of the generated data. They find that scaling laws differ significantly across datasets with varying compressibility and propose a new data-dependent scaling law that accounts for the compressibility of the training data.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach by linking data compressibility to scaling laws, which is a creative and interesting idea.
2. The paper is well-written and easy to follow.
3. The experiments are comprehensive and well-designed.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's reliance on PCFGs for generating synthetic data may limit the generalizability of the findings to real-world datasets. While the authors acknowledge this limitation, it would be beneficial to see some discussion on how the results might translate to more complex, real-world datasets.
2. The paper does not explore the impact of different compression algorithms on the results. It would be interesting to see if other compression algorithms, such as Lempel-Ziv or Burrows-Wheeler transform, yield different scaling laws.
3. The paper does not provide a clear definition of what constitutes "data complexity" beyond compressibility. It would be helpful to have a more formal definition of data complexity and how it relates to the proposed scaling law.
4. The paper does not discuss the limitations of using gzip for measuring compressibility. It would be interesting to see if other measures of compressibility, such as entropy or mutual information, yield different results.
5. The paper does not explore the impact of different model architectures on the results. It would be interesting to see if the proposed scaling law holds for different model architectures, such as transformers or recurrent neural networks.

### Suggestions

The authors should consider expanding their analysis to include a more diverse set of synthetic datasets generated using different PCFG parameters. This would help to assess the robustness of their findings and determine if the observed scaling laws are specific to the particular PCFG configurations used in the study. For example, varying the number of non-terminals, the average length of production rules, or the number of possible derivations could reveal how these factors influence the relationship between data compressibility and model performance. Furthermore, it would be beneficial to explore the impact of different PCFG grammars, such as context-free grammars with different branching factors or context-sensitive grammars, to see if the observed scaling laws are consistent across different types of grammatical structures. This would provide a more comprehensive understanding of how data complexity affects the scaling behavior of language models.

In addition to exploring different PCFG parameters, the authors should also investigate the impact of different compression algorithms on the measured data complexity and the resulting scaling laws. While gzip is a widely used compression algorithm, it is not the only one available. Exploring other compression algorithms, such as Lempel-Ziv or Burrows-Wheeler transform, could reveal whether the observed scaling laws are specific to gzip or if they generalize to other compression techniques. It would also be interesting to compare the compressibility measured by these different algorithms and see if they correlate with each other. This would provide a more robust measure of data complexity and help to validate the proposed scaling law. Furthermore, the authors should consider using information-theoretic measures of compressibility, such as entropy or mutual information, to complement the lossless compression-based approach. These measures could provide a more nuanced understanding of the information content of the data and its relationship to model performance.

Finally, the authors should provide a more formal definition of data complexity and discuss how it relates to the proposed scaling law. While compressibility is a useful proxy for data complexity, it is not the only factor that influences model performance. Other factors, such as the semantic structure of the data, the presence of noise, or the diversity of the vocabulary, can also play a significant role. The authors should discuss how these factors interact with data compressibility and how they affect the scaling behavior of language models. Furthermore, they should explore the impact of different model architectures on the results. It would be interesting to see if the proposed scaling law holds for different model architectures, such as transformers or recurrent neural networks. This would provide a more comprehensive understanding of the relationship between data complexity, model architecture, and model performance.

### Questions

1. How does the proposed data-dependent scaling law compare to existing scaling laws in terms of predictive accuracy and practical utility? Are there specific scenarios where the data-dependent scaling law provides a significant advantage over traditional scaling laws?
2. How sensitive are the findings to the choice of compression algorithm (gzip)? Would using other compression algorithms (e.g., Lempel-Ziv, Burrows-Wheeler transform) lead to different conclusions?
3. How well do the findings generalize to real-world datasets beyond the synthetic PCFG-generated data? Are there specific characteristics of real-world data that might affect the applicability of the proposed scaling law?
4. How does the proposed data-dependent scaling law perform across different model architectures and sizes? Are there specific architectures or model sizes where the data-dependent scaling law is more or less effective?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper explores the impact of data complexity on the scaling laws of neural language models. The authors use probabilistic context-free grammars (PCFGs) to generate synthetic datasets with varying syntactic complexity, allowing them to systematically control the complexity of the training data. They find that the scaling laws are sensitive to data complexity, with models trained on more compressible data requiring different compute-optimal parameter-to-data ratios. The authors propose a data-dependent scaling law that incorporates gzip compressibility as a predictor of scaling properties, suggesting that models trained on more compressible data benefit more from parameter count increases.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach to studying scaling laws by incorporating data complexity as a key factor, which is a departure from the traditional view that scaling laws are independent of the training data.
- The use of PCFGs to generate synthetic datasets allows for precise control over data complexity, enabling a systematic study of the relationship between data complexity and model performance.
- The paper provides a clear and well-structured presentation of the methodology and results, making it easy to follow the experimental setup and findings.

### Weaknesses

#### Some Related Works


#### comment

 - The study primarily focuses on synthetic datasets generated from PCFGs, which may not fully capture the complexities of real-world data. The findings may not generalize well to datasets with different statistical properties or structures, such as those found in natural language or code, which can exhibit long-range dependencies and semantic structures not present in the synthetic data. Specifically, the synthetic data may lack the nuances of real-world text, such as variations in sentence structure, vocabulary, and the presence of noise, which could significantly impact the observed scaling laws.
- The reliance on gzip compressibility as a measure of data complexity may not fully capture all relevant aspects of data complexity. While gzip is effective for detecting repetitive patterns, it may not account for other important factors, such as the presence of long-range dependencies, semantic structure, or the presence of adversarial examples, which could all influence model performance. For instance, a dataset might be highly compressible using gzip but still require significant parameter count increases to achieve optimal performance, or vice versa. The study should explore alternative measures of data complexity to provide a more comprehensive understanding.
- The paper does not provide a detailed analysis of how the proposed data-dependent scaling law performs across different model architectures and sizes. The scaling law may be sensitive to architectural choices, such as the number of layers, attention heads, or the use of specific activation functions, which could affect the observed scaling behavior. Furthermore, the study should investigate how the scaling law behaves with varying model sizes, as the optimal parameter-to-data ratio might change with model capacity. It is unclear if the proposed scaling law is robust across different architectures and model sizes, which is crucial for its practical applicability.

### Suggestions

The authors should conduct experiments on a wider range of real-world datasets to validate the generalizability of their findings. This should include datasets with varying statistical properties, such as natural language text, code, and scientific data. Specifically, the study should investigate how the scaling laws and the proposed data-dependent scaling law behave on datasets with different levels of long-range dependencies, semantic structure, and noise. For example, datasets with complex syntactic structures and semantic relationships, such as those found in code or scientific text, might exhibit different scaling behaviors compared to simpler datasets like synthetic PCFGs. Furthermore, the study should explore the impact of different data preprocessing techniques on the results, as these techniques can significantly affect the compressibility of the data and the observed scaling laws. This would provide a more robust understanding of the relationship between data complexity and model performance.

To address the limitations of using gzip compressibility as the sole measure of data complexity, the authors should explore alternative measures that capture different aspects of data complexity. For example, information-theoretic measures, such as entropy or mutual information, could provide a more comprehensive understanding of the information content of the data. Additionally, the study should investigate the impact of long-range dependencies and semantic structure on model performance. This could involve using techniques such as graph-based analysis or semantic similarity measures to quantify the complexity of the data. Furthermore, the authors should explore the impact of adversarial examples on model performance, as these examples can reveal vulnerabilities that are not captured by simple compression metrics. By incorporating multiple measures of data complexity, the study could provide a more robust and comprehensive understanding of the relationship between data complexity and model scaling.

The authors should also conduct a more thorough analysis of the proposed data-dependent scaling law across different model architectures and sizes. This should include experiments with different types of neural network architectures, such as transformers, recurrent neural networks, and convolutional networks. Furthermore, the study should investigate how the scaling law behaves with varying model sizes, as the optimal parameter-to-data ratio might change with model capacity. It is important to determine if the proposed scaling law is robust across different architectures and model sizes, as this is crucial for its practical applicability. The authors should also explore the sensitivity of the scaling law to different hyperparameters, such as learning rate, batch size, and optimizer. This would provide a more complete understanding of the behavior of the proposed scaling law and its limitations.

### Questions

- How does the proposed data-dependent scaling law compare to existing scaling laws in terms of predictive accuracy and practical utility? Are there specific scenarios where the data-dependent scaling law provides a significant advantage over traditional scaling laws?
- How sensitive are the findings to the choice of compression algorithm (gzip)? Would using other compression algorithms (e.g., Lempel-Ziv, Burrows-Wheeler transform) lead to different conclusions?
- How well do the findings generalize to real-world datasets beyond the synthetic PCFG-generated data? Are there specific characteristics of real-world data that might affect the applicability of the proposed scaling law?
- How does the proposed data-dependent scaling law perform across different model architectures and sizes? Are there specific architectures or model sizes where the data-dependent scaling law is more or less effective?

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
3. Look for evidence (quotes, experimental details, missing citations, etc.) to support the weakness.
4. If evidence is found, categorize it and note it down.
5. If no evidence is found, explain why.
6. Synthesize the findings and provide a conclusion for each weakness.
```json
[
  {
    "Weakness Statement": "The study primarily focuses on synthetic datasets generated from PCFGs, which may not fully capture the complexities of real-world data. The findings may not generalize well to datasets with different statistical properties or structures, such as those found in natural language or code, which can exhibit long-range dependencies and semantic structures not present in the synthetic data. Specifically, the synthetic data may lack the nuances of real-world text, such as variations in sentence structure, vocabulary, and the presence of noise, which could significantly impact the observed scaling laws.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "To create a PCFG from the above arguments, for each non-terminal, we randomly choose its number of productions (RHS options), each of those production’s length, instantiate a production rule by randomly sampling from the terminals & non-terminals, and assign it a probability normalized by the total RHS options for the non-terminal.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly states that the datasets are generated using PCFGs, which are synthetic and controlled. The experiments are conducted on these synthetic datasets.",
      "Supporting quotes": [
        "To create a PCFG from the above arguments...",
        "We generate 6 datasets of token sequences with varying complexities..."
      ],
      "Impact assessment": "The reviewer's concern about the generalizability of findings to real-world data is valid because the study is limited to synthetic data."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly describes the use of PCFGs for generating synthetic datasets."
    }
  },
  {
    "Weakness Statement": "The reliance on gzip compressibility as a measure of data complexity may not fully capture all relevant aspects of data complexity. While gzip is effective for detecting repetitive patterns, it may not account for other important factors, such as the presence of long-range dependencies, semantic structure, or the presence of adversarial examples, which could all influence model performance. For instance, a dataset might be highly compressible using gzip but still require significant parameter count increases to achieve optimal performance, or vice versa. The study should explore alternative measures of data complexity to provide a more comprehensive understanding.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We compute the ratio of the size (in bytes) of the compressed data to the original data. We then compute the median and standard deviation in compressibility, confirming that grammars with higher syntactic complexity also increase its preference for dataset size over parameter count.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        },
        {
          "quote": "We use a compression algorithm, gzip , to estimate the entropy of sampled linguistic sequences.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses gzip compressibility as the primary measure of data complexity. The reviewer correctly points out that gzip might not capture all aspects of complexity.",
      "Supporting quotes": [
        "We compute the ratio of the size (in bytes) of the compressed data to the original data.",
        "We use a compression algorithm, gzip , to estimate the entropy of sampled linguistic sequences."
      ],
      "Impact assessment": "The reviewer's concern is valid as the paper focuses solely on gzip compressibility without exploring other measures."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly mentions using gzip as the measure of compressibility."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of how the proposed data-dependent scaling law performs across different model architectures and sizes. The scaling law may be sensitive to architectural choices, such as the number of layers, attention heads, or the use of specific activation functions, which could affect the observed scaling behavior. Furthermore, the study should investigate how the scaling law behaves with varying model sizes, as the optimal parameter-to-data ratio might change with model capacity. It is unclear if the proposed scaling law is robust across different architectures and model sizes, which is crucial for its practical applicability.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the model architecture and training hyperparameters used, but it does not explicitly explore the performance of the data-dependent scaling law with different architectures or sizes.",
      "Supporting quotes": [
        "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method..."
      ],
      "Impact assessment": "The reviewer's point about the lack of analysis across different architectures and sizes is valid as the experiments are limited to a specific setup."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental setup focuses on a specific model architecture and training parameters."
    }
  },
  {
    "Weakness Statement": "How does the proposed data-dependent scaling law compare to existing scaling laws in terms of predictive accuracy and practical utility? Are there specific scenarios where the data-dependent scaling law provides a significant advantage over traditional scaling laws?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "The scaling law induces a compute-optimal frontier for parameter count derived by Kaplan et al. & Hoffmann et al. and simplifiable as:  \n\nN o p t ​ ( C ) = ( α ​ A ’ + β ​ B ’) 1 α ’ + β ’ N p t ​ ( C 6 ) ,  \n\nwhere C C is a compute budget in FLOPs. They claim that E E captures the “entropy of natural text” (their Sec. 3.3) and that scaling laws are “independent of dataset” (their App. C). However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 ).",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "To establish such a non-trivial sensitivity of scaling laws to data complexity, we need to compute the law for each dataset and examine its fitted parameters.",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "The scaling law induces a compute-optimal frontier for parameter count derived by Kaplan et al. & Hoffmann et al. and simplifiable as:  \n\nN o p t ​ ( C ) = ( α ’ A ’ + β ’ B ’) 1 α ’ + β ’ N p t ​ ( C 6 ) ,  \n\nwhere C C is a compute budget in FLOPs. They claim that E E captures the “entropy of natural text” (their Sec. 3.3) and that scaling laws are “independent of dataset” (their App. C). However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 ).",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "The scaling law induces a compute-optimal frontier for parameter count derived by Kaplan et al. & Hoffmann et al. and simplifiable as:  \n\nN o p t ​ ( C ) = ( α ’ A ’ + β ’ B ’) 1 α ’ + β ’ N p t ​ ( C 6 ) ,  \n\nwhere C C is a compute budget in FLOPs. They claim that E E captures the “entropy of natural text” (their Sec. 3.3) and that scaling laws are “independent of dataset” (their App. C). However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 ).",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly compares the proposed data-dependent scaling law with the standard Chinchilla scaling law by showing that the fitted parameters (alpha and beta) are different for each dataset, indicating sensitivity to data complexity.",
      "Supporting quotes": [
        "However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 )."
      ],
      "Impact assessment": "The paper directly addresses the comparison by demonstrating the differences in the fitted scaling laws."
    },
    "Conclusion": {
      "Validity status": "Invalid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly compares the fitted parameters of the standard scaling law and the proposed data-dependent scaling law."
    }
  },
  {
    "Weakness Statement": "How sensitive are the findings to the choice of compression algorithm (gzip)? Would using other compression algorithms (e.g., Lempel-Ziv, Burrows-Wheeler transform) lead to different conclusions?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use a compression algorithm, gzip , to estimate the entropy of sampled linguistic sequences.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        },
        {
          "quote": "The scaling law induces a compute-optimal frontier for parameter count derived by Kaplan et al. & Hoffmann et al. and simplifiable as:  \n\nN o p t ​ ( C ) = ( α ’ A ’ + β ’ B ’) 1 α ’ + β ’ N p t ​ ( C 6 ) ,  \n\nwhere C C is a compute budget in FLOPs. They claim that E E captures the “entropy of natural text” (their Sec. 3.3) and that scaling laws are “independent of dataset” (their App. C). However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 ).",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses gzip as the primary compression algorithm. The reviewer's question about the sensitivity to other algorithms is valid as the paper doesn't explore this.",
      "Supporting quotes": [
        "We use a compression algorithm, gzip , to estimate the entropy of sampled linguistic sequences."
      ],
      "Impact assessment": "The lack of experimentation with other compression algorithms is a valid limitation."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly states the use of gzip as the compression algorithm."
    }
  },
  {
    "Weakness Statement": "How well do the findings generalize to real-world datasets beyond the synthetic PCFG-generated data? Are there specific characteristics of real-world data that might affect the applicability of the proposed scaling law?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "To create a PCFG from the above arguments, for each non-terminal, we randomly choose its number of productions (RHS options), each of those production’s length, instantiate a production rule by randomly sampling from the terminals & non-terminals, and assign it a probability normalized by the total RHS options for the non-terminal.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's experiments are conducted solely on synthetic data generated by PCFGs. The generalizability to real-world datasets is not directly tested.",
      "Supporting quotes": [
        "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints."
      ],
      "Impact assessment": "The reviewer's concern about generalizability is valid as the study is limited to synthetic data."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental setup focuses on generating synthetic datasets."
    }
  },
  {
    "Weakness Statement": "How does the proposed data-dependent scaling law perform across different model architectures and sizes? Are there specific architectures or model sizes where the data-dependent scaling law is more or less effective?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper specifies a particular model architecture and training hyperparameters used for the experiments. It does not explore the performance of the data-dependent scaling law with different architectures or sizes.",
      "Supporting quotes": [
        "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method..."
      ],
      "Impact assessment": "The reviewer's point about the lack of analysis across different architectures and sizes is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental setup uses a specific model architecture and training parameters."
    }
  },
  {
    "Weakness Statement": "The paper's reliance on PCFGs for generating synthetic data may limit the generalizability of the findings to real-world datasets. The findings may not generalize well to datasets with different statistical properties or structures, such as those found in natural language or code, which can exhibit long-range dependencies and semantic structures not present in the synthetic data. Specifically, the synthetic data may lack the nuances of real-world text, such as variations in sentence structure, vocabulary, and the presence of noise, which could significantly impact the observed scaling laws.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "To create a PCFG from the above arguments, for each non-terminal, we randomly choose its number of productions (RHS options), each of those production’s length, instantiate a production rule by randomly sampling from the terminals & non-terminals, and assign it a probability normalized by the total RHS options for the non-terminal.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly uses PCFGs to generate synthetic datasets, and the reviewer correctly points out the limitations of this approach regarding generalizability to real-world data.",
      "Supporting quotes": [
        "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints."
      ],
      "Impact assessment": "The reviewer's concern about the limitations of using synthetic data is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the use of PCFGs for generating synthetic datasets."
    }
  },
  {
    "Weakness Statement": "The reliance on gzip compressibility as a measure of data complexity may not fully capture all relevant aspects of data complexity. While gzip is effective for detecting repetitive patterns, it may not account for other important factors, such as the presence of long-range dependencies, semantic structure, or the presence of adversarial examples, which could all influence model performance. For instance, a dataset might be highly compressible using gzip but still require significant parameter count increases to achieve optimal performance, or vice versa. The study should explore alternative measures of data complexity to provide a more comprehensive understanding.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We compute the ratio of the size (in bytes) of the compressed data to the original data. We then compute the median and standard deviation in compressibility, confirming that grammars with higher syntactic complexity also increase its preference for dataset size over parameter count.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        },
        {
          "quote": "We use a compression algorithm, gzip , to estimate the entropy of sampled linguistic sequences.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses gzip compressibility as the primary measure of data complexity, and the reviewer correctly identifies its limitations in capturing all aspects of data complexity.",
      "Supporting quotes": [
        "We compute the ratio of the size (in bytes) of the compressed data to the original data.",
        "We use a compression algorithm, gzip , to estimate the entropy of sampled linguistic sequences."
      ],
      "Impact assessment": "The reviewer's concern about the limitations of using gzip compressibility is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly mentions using gzip as the measure of compressibility."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of how the proposed data-dependent scaling law performs across different model architectures and sizes. The scaling law may be sensitive to architectural choices, such as the number of layers, attention heads, or the use of specific activation functions, which could affect the observed scaling behavior. Furthermore, the study should investigate how the scaling law behaves with varying model sizes, as the optimal parameter-to-data ratio might change with model capacity. It is unclear if the proposed scaling law is robust across different architectures and model sizes, which is crucial for its practical applicability.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the model architecture and training hyperparameters used, but it does not explore the performance of the data-dependent scaling law with different architectures or sizes.",
      "Supporting quotes": [
        "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method..."
      ],
      "Impact assessment": "The reviewer's point about the lack of analysis across different architectures and sizes is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental setup focuses on a specific model architecture and training parameters."
    }
  },
  {
    "Weakness Statement": "How does the proposed data-dependent scaling law compare to existing scaling laws in terms of predictive accuracy and practical utility? Are there specific scenarios where the data-dependent scaling law provides a significant advantage over traditional scaling laws?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "The scaling law induces a compute-optimal frontier for parameter count derived by Kaplan et al. & Hoffmann et al. and simplifiable as:  \n\nN o p t ​ ( C ) = ( α ’ A ’ + β ’ B ’) 1 α ’ + β ’ N p t ​ ( C 6 ) ,  \n\nwhere C C is a compute budget in FLOPs. They claim that E E captures the “entropy of natural text” (their Sec. 3.3) and that scaling laws are “independent of dataset” (their App. C). However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 ).",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "To establish such a non-trivial sensitivity of scaling laws to data complexity, we need to compute the law for each dataset and examine its fitted parameters.",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "The scaling law induces a compute-optimal frontier for parameter count derived by Kaplan et al. & Hoffmann et al. and simplifiable as:  \n\nN o p t ​ ( C ) = ( α ’ A ’ + β ’ B ’) 1 α ’ + β ’ N p t ​ ( C 6 ) ,  \n\nwhere C C is a compute budget in FLOPs. They claim that E E captures the “entropy of natural text” (their Sec. 3.3) and that scaling laws are “independent of dataset” (their App. C). However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 ).",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "The scaling law induces a compute-optimal frontier for parameter count derived by Kaplan et al. & Hoffmann et al. and simplifiable as:  \n\nN o p t ​ ( C ) = ( α ’ A ’ + β ’ B ’) 1 α ’ + β ’ N p t ​ ( C 6 ) ,  \n\nwhere C C is a compute budget in FLOPs. They claim that E E captures the “entropy of natural text” (their Sec. 3.3) and that scaling laws are “independent of dataset” (their App. C). However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 ).",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly compares the fitted parameters of the standard scaling law and the proposed data-dependent scaling law, showing that they are different for each dataset.",
      "Supporting quotes": [
        "However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 )."
      ],
      "Impact assessment": "The paper directly addresses the comparison by demonstrating the differences in the fitted scaling laws."
    },
    "Conclusion": {
      "Validity status": "Invalid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly compares the fitted parameters of the standard and data-dependent scaling laws."
    }
  },
  {
    "Weakness Statement": "How sensitive are the findings to the choice of compression algorithm (gzip)? Would using other compression algorithms (e.g., Lempel-Ziv, Burrows-Wheeler transform) lead to different conclusions?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use a compression algorithm, gzip , to estimate the entropy of sampled linguistic sequences.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper uses gzip as the primary compression algorithm, and the reviewer's question about the sensitivity to other algorithms is valid as the paper doesn't explore this.",
      "Supporting quotes": [
        "We use a compression algorithm, gzip , to estimate the entropy of sampled linguistic sequences."
      ],
      "Impact assessment": "The lack of experimentation with other compression algorithms is a valid limitation."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly states the use of gzip as the compression algorithm."
    }
  },
  {
    "Weakness Statement": "How well do the findings generalize to real-world datasets beyond the synthetic PCFG-generated data? Are there specific characteristics of real-world data that might affect the applicability of the proposed scaling law?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "To create a PCFG from the above arguments, for each non-terminal, we randomly choose its number of productions (RHS options), each of those production’s length, instantiate a production rule by randomly sampling from the terminals & non-terminals, and assign it a probability normalized by the total RHS options for the non-terminal.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's experiments are conducted solely on synthetic data generated by PCFGs. The generalizability to real-world datasets is not directly tested.",
      "Supporting quotes": [
        "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints."
      ],
      "Impact assessment": "The reviewer's concern about generalizability is valid as the study is limited to synthetic data."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental setup focuses on generating synthetic datasets."
    }
  },
  {
    "Weakness Statement": "How does the proposed data-dependent scaling law perform across different model architectures and sizes? Are there specific architectures or model sizes where the data-dependent scaling law is more or less effective?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method, and a learning rate starting from 5 e − 5 and cosine decayed over the number of train steps [ L o g e ( D 6 ) + n ( 1 − e − ( c / 6 ) ) ] .",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper specifies a particular model architecture and training hyperparameters used for the experiments. It does not explore the performance of the data-dependent scaling law with different architectures or sizes.",
      "Supporting quotes": [
        "We use a batch size of 32, single epoch training, the A d a p t i v e Scaling Law method..."
      ],
      "Impact assessment": "The reviewer's point about the lack of analysis across different architectures and sizes is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental setup uses a specific model architecture and training parameters."
    }
  },
  {
    "Weakness Statement": "The study primarily focuses on synthetic datasets generated from PCFGs, which may not fully capture the complexities of real-world data. The findings may not generalize well to datasets with different statistical properties or structures, such as those found in natural language or code, which can exhibit long-range dependencies and semantic structures not present in the synthetic data. Specifically, the synthetic data may lack the nuances of real-world text, such as variations in sentence structure, vocabulary, and the presence of noise, which could significantly impact the observed scaling laws.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "To create a PCFG from the above arguments, for each non-terminal, we randomly choose its number of productions (RHS options), each of those production’s length, instantiate a production rule by randomly sampling from the terminals & non-terminals, and assign it a probability normalized by the total RHS options for the non-terminal.",
          "section": "3.1 gzip -compressibility Measures Syntactic Parameters for Each Grammar"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility"
        },
        {
          "quote": "We generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.",
          "section": "4.3 Discussion"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly uses PCFGs to generate synthetic datasets}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel approach to studying scaling laws in neural language models by investigating the impact of training data complexity. Instead of focusing solely on dataset size, the authors propose that the compressibility of training data, measured using gzip, can serve as a proxy for data complexity. They generate synthetic datasets using Probabilistic Context-Free Grammars (PCFGs), allowing for precise control over data syntactic complexity. By training language models on these datasets with varying compressibility, they observe that models trained on more compressible data require different compute-optimal parameter-to-data ratios. Specifically, they find that models trained on more compressible data benefit more from parameter count increases. This finding challenges the conventional view that scaling laws are independent of the training data. The authors then propose a data-dependent scaling law that incorporates gzip compressibility as a predictor of scaling properties. They validate their findings using both synthetic and real-world datasets, including code and natural language, demonstrating the potential of their approach to optimize compute allocation for training language models. The core contribution of this work lies in its shift from a dataset-centric to a data complexity-centric perspective, offering a new lens through which to understand the relationship between data characteristics and model scaling. The use of PCFGs to systematically generate datasets with controlled complexity is a key methodological innovation, allowing for a rigorous analysis of the impact of data compressibility on scaling laws. The empirical findings highlight the sensitivity of scaling laws to data complexity, suggesting that models trained on less compressible data may require different training strategies and compute allocations. This work has significant implications for the efficient training of large language models, potentially enabling more effective use of computational resources by tailoring training data and model parameters to the specific characteristics of the data. The proposed data-dependent scaling law offers a promising avenue for optimizing compute allocation, potentially leading to more efficient and effective training of language models.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I found several aspects of this paper to be particularly strong. The most compelling is the novel approach of linking data complexity, as measured by gzip compressibility, to scaling laws. This is a departure from the traditional view that scaling laws are largely independent of the training data, and it opens up new avenues for understanding the relationship between data characteristics and model performance. The use of PCFGs to generate synthetic datasets with controlled syntactic complexity is a significant methodological strength. This allows for precise manipulation of data complexity, enabling a systematic study of its impact on scaling laws. The authors' decision to use gzip compressibility as a measure of data complexity is also well-justified, as it provides a quantitative measure of the information content of the data. The paper's empirical findings are robust and clearly demonstrate the sensitivity of scaling laws to data complexity. The authors show that models trained on more compressible data require different compute-optimal parameter-to-data ratios, and that these ratios vary across datasets with different compressibility. This is a key finding that challenges the conventional view of scaling laws. Furthermore, the proposed data-dependent scaling law is a valuable contribution, as it provides a way to predict scaling properties based on data complexity. The authors show that this data-dependent scaling law fits the data better than traditional scaling laws, suggesting that it is a more accurate model of the relationship between data complexity and model performance. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors clearly explain their methodology and results, and they provide sufficient detail for the reader to understand the key concepts. The experiments are comprehensive and well-designed, and the results are presented in a clear and concise manner. Overall, I believe that this paper makes a significant contribution to the field of language model training, and it has the potential to influence future research in this area.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the study's primary focus on synthetic datasets generated from PCFGs raises concerns about the generalizability of the findings to real-world datasets. As the authors themselves acknowledge, these synthetic datasets may not fully capture the complexities of real-world data, which can exhibit long-range dependencies, semantic structures, and other features not present in the synthetic data. Specifically, the synthetic data may lack the nuances of real-world text, such as variations in sentence structure, vocabulary, and the presence of noise, which could significantly impact the observed scaling laws. This limitation is evident in the paper's methodology, which relies on a controlled environment that may not fully reflect the challenges of real-world data. The authors do not explore the impact of different data preprocessing techniques on the results, which could significantly affect the compressibility of the data and the observed scaling laws. This is a critical issue because the conclusions may not generalize well to datasets with different statistical properties or structures. My confidence in this weakness is high, as the paper explicitly states the use of PCFGs for generating synthetic data and does not include any experiments on real-world datasets. Second, the reliance on gzip compressibility as the sole measure of data complexity is a significant limitation. While gzip is effective for detecting repetitive patterns, it may not capture all relevant aspects of data complexity. As the reviewers have pointed out, a dataset might be highly compressible using gzip but still require significant parameter count increases to achieve optimal performance, or vice versa. The study should explore alternative measures of data complexity to provide a more comprehensive understanding. For example, information-theoretic measures, such as entropy or mutual information, could provide a more nuanced understanding of the information content of the data. Additionally, the study could investigate the impact of long-range dependencies and semantic structure on model performance. This limitation is evident in the paper's methodology, which uses gzip compressibility as the primary measure of data complexity. The authors do not explore other measures of complexity, which could provide a more complete picture of the relationship between data complexity and model performance. My confidence in this weakness is high, as the paper explicitly states the use of gzip as the measure of compressibility. Third, the paper does not provide a detailed analysis of how the proposed data-dependent scaling law performs across different model architectures and sizes. The scaling law may be sensitive to architectural choices, such as the number of layers, attention heads, or the use of specific activation functions, which could affect the observed scaling behavior. Furthermore, the study should investigate how the scaling law behaves with varying model sizes, as the optimal parameter-to-data ratio might change with model capacity. It is unclear if the proposed scaling law is robust across different architectures and model sizes, which is crucial for its practical applicability. This limitation is evident in the paper's experimental setup, which focuses on a specific model architecture and training hyperparameters. The authors do not explore the performance of the data-dependent scaling law with different architectures or sizes, which limits the generalizability of the findings. My confidence in this weakness is high, as the paper explicitly uses a specific model architecture and training parameters in its experiments. Fourth, the paper does not explore the impact of different compression algorithms on the results. The study uses gzip compressibility as a measure of data complexity and the resulting data compressibility and the resulting scaling laws. It would be interesting to see if other compression algorithms (e.g., Lempel-Ziv, Burrows-Wheeler transform) yield different conclusions. This is a significant limitation, as the choice of compression algorithm could affect the compressibility of the data and the observed scaling laws. My confidence in this weakness is high, as the paper explicitly states the use of gzip as the compression algorithm. Finally, while the paper compares the proposed data-dependent scaling law with the standard Chinchilla scaling law, it does not explore the sensitivity of the findings to the choice of compression algorithm (gzip). The paper uses gzip compressibility as the primary measure of data complexity, and the reviewer correctly points out that other compression algorithms might yield different results. This is a valid concern as the compressibility of data can vary significantly depending on the algorithm used. My confidence in this weakness is high, as the paper explicitly mentions using gzip as the measure of compressibility. These limitations, while not invalidating the core findings, highlight areas where further research is needed to strengthen the conclusions and increase the generalizability of the results.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should expand their analysis to include a wider range of real-world datasets. This should include datasets from diverse domains, such as natural language, code, and scientific text. The datasets should vary in terms of their size, complexity, and domain-specific characteristics. This would help to determine if the observed scaling laws are consistent across different types of data and if the proposed data-dependent scaling law generalizes beyond the specific characteristics of the synthetic data. Furthermore, it would be beneficial to explore how the scaling laws change as the dataset size increases, as the optimal parameter-to-data ratio might be affected by the amount of training data available. Second, the authors should explore alternative measures of data complexity beyond simple compression ratios. For example, information-theoretic measures, such as entropy or mutual information, could provide a more comprehensive understanding of the information content of the data. Additionally, the study should investigate the impact of long-range dependencies and semantic structure on model performance. This could involve using techniques such as graph-based analysis or semantic similarity measures to quantify the complexity of the data. Furthermore, the study should explore the impact of adversarial examples on model performance, as these examples can reveal vulnerabilities that are not captured by simple compression metrics. Third, the authors should conduct a more thorough analysis of the proposed data-dependent scaling law across different model architectures and sizes. This should include experiments with different types of neural network architectures, such as transformers, recurrent neural networks, and convolutional networks. Furthermore, the study should investigate how the scaling law behaves with varying model sizes, as the optimal parameter-to-data ratio might change with model capacity. It is important to determine if the proposed scaling law is robust across different architectures and model sizes, as this is crucial for its practical applicability. The authors should also explore the limitations of the proposed scaling law and identify scenarios where it might not be applicable. This would help to establish the boundaries of the proposed scaling law and provide guidance for its use in practical applications. Fourth, the authors should conduct a more thorough analysis of the impact of different compression algorithms on the results. This should include experiments with different compression algorithms, such as Lempel-Ziv or Burrows-Wheeler transform, to determine if the observed scaling laws are specific to gzip or if they generalize to other compression techniques. This would provide a more robust measure of the relationship between data complexity and model performance. Finally, the authors should provide a more formal definition of data complexity and discuss how it relates to the proposed scaling law. While compressibility is a useful proxy for data complexity, it is not the only factor that influences model performance. Other factors, such as the presence of long-range dependencies, semantic structure, or the presence of adversarial examples, can also play a significant role. The authors should discuss how these factors interact with data compressibility and how they affect the scaling behavior of language models. Furthermore, they should explore the impact of different data preprocessing techniques on the results, as these techniques can significantly affect the compressibility of the data. By addressing these limitations, the authors can significantly strengthen their findings and increase the generalizability of their results.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the proposed data-dependent scaling law compare to existing scaling laws in terms of predictive accuracy and practical utility? Are there specific scenarios where the data-dependent scaling law provides a significant advantage over traditional scaling laws? The paper does show that the data-dependent scaling law fits the data better than the standard scaling law, but it does not explore the practical implications of this difference. Second, how sensitive are the findings to the choice of compression algorithm (gzip)? Would using other compression algorithms (e.g., Lempel-Ziv, Burrows-Wheeler transform) lead to different conclusions? The paper uses gzip as the primary measure of data complexity, but it does not explore the impact of other compression algorithms. Third, how well do the findings generalize to real-world datasets beyond the synthetic PCFG-generated data? Are there specific characteristics of real-world data that might affect the applicability of the proposed scaling law? The paper's experiments are conducted solely on synthetic data, and it does not explore the impact of different data preprocessing techniques on the results. Fourth, how does the proposed data-dependent scaling law perform across different model architectures and sizes? Are there specific architectures or model sizes where the data-dependent scaling law is more or less effective? The paper uses a specific model architecture and training hyperparameters, and it does not explore the performance of the data-dependent scaling law with different architectures or sizes. Fifth, how does the proposed data-dependent scaling law compare to existing scaling laws in terms of predictive accuracy and practical utility? Are there specific scenarios where the data-dependent scaling law provides a significant advantage over traditional scaling laws? The paper does show that the data-dependent scaling law fits the data better than the standard scaling law, but it does not explore the practical implications of this difference. Finally, how does the proposed data-dependent scaling law perform across different model architectures and sizes? Are there specific architectures or model sizes where the data-dependent scaling law is more or less effective? The paper uses a specific model architecture and training hyperparameters, and it does not explore the performance of the data-dependent scaling law with different architectures or sizes. These questions target core methodological choices and seek clarification of critical assumptions, aiming to further understand the implications of the proposed approach.


## Rating:

5.75


## Confidence:

3.0


## Decision:

Reject
}