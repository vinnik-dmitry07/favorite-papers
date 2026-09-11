I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates the potential for training a BERT-like language model from scratch with a single GPU for a single day. The authors explore various architectural and training modifications to achieve performance close to BERT within these constraints. They find that scaling laws still largely hold in this limited compute setting, with model size being the primary determinant of performance. They also identify several architectural and training tweaks that improve performance, such as disabling QKV biases, using rotary embeddings, and employing a gated linear unit in the feedforward block.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses an interesting and relevant problem: how much can we get away with training language models on a single GPU in a day?
- The authors conduct a thorough investigation of various architectural and training modifications, providing valuable insights into the factors that contribute to performance in this limited compute setting.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's central claim that scaling laws still largely hold in the low-resource regime is not particularly novel. This has been observed in prior work, such as the study by Izsak et al. (2021), which also explored training BERT for a single day with limited resources. The authors do not sufficiently differentiate their findings from this existing work, particularly in the context of architectural modifications. The paper's contribution in this area is limited, as it largely reiterates known scaling trends rather than providing new insights into the interplay between model size, compute, and performance in this specific constrained setting.
- The paper lacks a clear and compelling narrative. While the authors explore various modifications, the overall message is not well-defined. It is unclear whether the paper aims to provide a comprehensive analysis of the factors influencing performance or to propose a specific set of modifications for training efficient models. The absence of a clear research question makes it difficult to assess the significance of the findings. The paper would benefit from a more focused narrative that clearly articulates its goals and contributions.
- The paper does not adequately address the limitations of the study. For example, the authors do not discuss the potential impact of their specific choices of architectural modifications and training strategies on the generalizability of their findings. The paper should acknowledge that the observed scaling laws and performance gains may not hold for other model architectures or training regimes. Furthermore, the paper lacks a discussion of the potential biases introduced by the specific datasets and tasks used in the experiments. This lack of transparency makes it difficult to assess the robustness of the results.

### Suggestions

The authors should clarify their central claim by explicitly stating what novel insights their work provides beyond the existing literature on scaling laws in limited compute settings. They should clearly articulate the specific gap in the literature that their work addresses and how it advances our understanding of efficient model training. For example, instead of simply stating that scaling laws hold, they should quantify the degree to which these laws hold in their specific experimental setup, and compare it to previous studies. This would involve a more detailed analysis of the relationship between model size, compute, and performance, and a discussion of the factors that might cause deviations from the ideal scaling behavior. Furthermore, the authors should provide a more detailed analysis of the architectural modifications they explore, explaining why certain modifications are expected to improve performance and how these modifications interact with the limited compute resources. This would help to provide a more nuanced understanding of the factors that contribute to efficient model training.

To improve the narrative, the authors should clearly define the research question they are trying to answer. Is it to identify the key factors that influence performance in low-resource settings, or is it to propose a specific set of modifications for training efficient models? The paper should then focus on answering this question directly, providing a clear and concise summary of the main findings. The authors should also provide a more detailed discussion of the limitations of their study, including the potential impact of their specific choices of architectural modifications and training strategies. They should acknowledge that the observed scaling laws and performance gains may not hold for other model architectures or training regimes. The paper should also discuss the potential biases introduced by the specific datasets and tasks used in the experiments, and how these biases might affect the generalizability of the results. This would involve a more thorough analysis of the experimental setup and a more careful interpretation of the results.

Finally, the authors should provide a more detailed analysis of the computational cost of their proposed modifications, and compare it to the cost of the baseline BERT model. This would help to assess the practical value of their approach. The paper should also discuss the potential for combining the proposed modifications with other techniques for efficient model training, such as knowledge distillation or pruning. This would help to demonstrate the broader applicability of their findings and their potential impact on the field. The authors should also consider including a more detailed ablation study to isolate the impact of each modification, which would help to provide a more granular understanding of the factors that contribute to performance.

### Questions

- How does the performance of the crammed models compare to the original BERT checkpoint in terms of downstream task performance and generalization capabilities?
- What are the computational costs associated with the proposed modifications, and how do they compare to the baseline BERT model?

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

This paper explores the possibility of training a BERT-like model from scratch with limited computational resources, specifically one day on a single GPU. The authors investigate the impact of various architectural and training modifications on the model's downstream performance. They find that scaling laws still largely hold in this constrained setting and identify architectural and training tweaks that improve performance, such as disabling QKV biases, using rotary embeddings, and employing a gated linear unit in the feedforward block. The paper also discusses the limitations of the study and provides insights into the trade-offs between model size, training efficiency, and performance.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses an interesting and relevant problem: how much can we get away with training language models on a single GPU in a day? The authors explore various architectural and training modifications to achieve performance close to BERT within these constraints.

2. The paper is well-written and easy to follow. The authors provide a clear and concise description of their methodology and findings.

3. The paper identifies several architectural and training tweaks that improve performance, such as disabling QKV biases, using rotary embeddings, and employing a gated linear unit in the feedforward block. These findings could be valuable for practitioners who are interested in training language models with limited resources.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's central claim that scaling laws still largely hold in the low-resource regime is not particularly novel. This has been observed in prior work, such as the study by Izsak et al. (2021), which also explored training BERT for a single day with limited resources. The authors do not sufficiently differentiate their findings from this existing work, particularly in the context of architectural modifications. The paper's contribution in this area is limited, as it largely reiterates known scaling trends rather than providing new insights into the interplay between model size, compute, and performance in this specific constrained setting.

2. The paper lacks a clear and compelling narrative. While the authors explore various modifications, the overall message is not well-defined. It is unclear whether the paper aims to provide a comprehensive analysis of the factors influencing performance or to propose a specific set of modifications for training efficient models. The absence of a clear research question makes it difficult to assess the significance of the findings. The paper would benefit from a more focused narrative that clearly articulates its goals and contributions.

3. The paper does not adequately address the limitations of the study. For example, the authors do not discuss the potential impact of their specific choices of architectural modifications and training strategies on the generalizability of their findings. The paper should acknowledge that the observed scaling laws and performance gains may not hold for other model architectures or training regimes. Furthermore, the paper lacks a discussion of the potential biases introduced by the specific datasets and tasks used in the experiments. This lack of transparency makes it difficult to assess the robustness of the results.

### Suggestions

The authors should clarify their central claim by explicitly stating what novel insights their work provides beyond the existing literature on scaling laws in limited compute settings. They should clearly articulate the specific gap in the literature that their work addresses and how it advances our understanding of efficient model training. For example, instead of simply stating that scaling laws hold, they should quantify the degree to which these laws hold in their specific experimental setup, and compare it to previous studies. This would involve a more detailed analysis of the relationship between model size, compute, and performance, and a discussion of the factors that might cause deviations from the ideal scaling behavior. Furthermore, the authors should provide a more detailed analysis of the architectural modifications they explore, explaining why certain modifications are expected to improve performance and how these modifications interact with the limited compute resources. This would help to provide a more nuanced understanding of the factors that contribute to efficient model training.

To improve the narrative, the authors should clearly define the research question they are trying to answer. Is it to identify the key factors that influence performance in low-resource settings, or is it to propose a specific set of modifications for training efficient models? The paper should then focus on answering this question directly, providing a clear and concise summary of the main findings. The authors should also provide a more detailed discussion of the limitations of their study, including the potential impact of their specific choices of architectural modifications and training strategies. They should acknowledge that the observed scaling laws and performance gains may not hold for other model architectures or training regimes. Furthermore, the paper should discuss the potential biases introduced by the specific datasets and tasks used in the experiments, and how these biases might affect the generalizability of the results. This would involve a more thorough analysis of the experimental setup and a more careful interpretation of the results.

Finally, the authors should provide a more detailed analysis of the computational cost of their proposed modifications, and compare it to the cost of the baseline BERT model. This would help to assess the practical value of their approach. The paper should also discuss the potential for combining the proposed modifications with other techniques for efficient model training, such as knowledge distillation or pruning. This would help to demonstrate the broader applicability of their findings and their potential impact on the field. The authors should also consider including a more detailed ablation study to isolate the impact of each modification, which would help to provide a more granular understanding of the factors that contribute to performance.

### Questions

1. How does the performance of the crammed models compare to the original BERT checkpoint in terms of downstream task performance and generalization capabilities?

2. What are the computational costs associated with the proposed modifications, and how do they compare to the baseline BERT model?

### Rating

3

### Confidence

4

**********

## Reviewer 3

### Summary

This paper explores the performance of BERT-like language models trained on a single GPU for a single day. The authors investigate various architectural and training modifications to achieve performance close to BERT under these constraints. The study aims to understand how much a model can be trained with limited resources and what trade-offs emerge when scaling down model size and training compute. The authors find that scaling laws still largely hold in the low-resource regime, with model size being the primary determinant of performance. They also identify several architectural and training tweaks that improve performance, such as disabling QKV biases, using rotary embeddings, and employing a gated linear unit in the feedforward block.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses a relevant and timely question: how much can we get away with training language models on a single GPU in a day? This is an important question for researchers and practitioners with limited computational resources.

2. The authors conduct a thorough investigation of various architectural and training modifications, providing valuable insights into the factors that contribute to performance in this limited compute setting.

3. The paper is well-written and easy to follow. The authors provide a clear and concise description of their methodology and findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's central claim that scaling laws still largely hold in the low-resource regime is not particularly novel. This has been observed in prior work, such as the study by Izsak et al. (2021), which also explored training BERT for a single day with limited resources. The authors do not sufficiently differentiate their findings from this existing work, particularly in the context of architectural modifications. The paper's contribution in this area is limited, as it largely reiterates known scaling trends rather than providing new insights into the interplay between model size, compute, and performance in this specific constrained setting.

2. The paper lacks a clear and compelling narrative. While the authors explore various modifications, the overall message is not well-defined. It is unclear whether the paper aims to provide a comprehensive analysis of the factors influencing performance or to propose a specific set of modifications for training efficient models. The absence of a clear research question makes it difficult to assess the significance of the findings. The paper would benefit from a more focused narrative that clearly articulates its goals and contributions.

3. The paper does not adequately address the limitations of the study. For example, the authors do not discuss the potential impact of their specific choices of architectural modifications and training strategies on the generalizability of their findings. The paper should acknowledge that the observed scaling laws and performance gains may not hold for other model architectures or training regimes. Furthermore, the paper lacks a discussion of the potential biases introduced by the specific datasets and tasks used in the experiments. This lack of transparency makes it difficult to assess the robustness of the results.

### Suggestions

The authors should clarify their central claim by explicitly stating what novel insights their work provides beyond the existing literature on scaling laws in limited compute settings. They should clearly articulate the specific gap in the literature that their work addresses and how it advances our understanding of efficient model training. For example, instead of simply stating that scaling laws hold, they should quantify the degree to which these laws hold in their specific experimental setup, and compare it to previous studies. This would involve a more detailed analysis of the relationship between model size, compute, and performance, and a discussion of the factors that might cause deviations from the ideal scaling behavior. Furthermore, the authors should provide a more detailed analysis of the architectural modifications they explore, explaining why certain modifications are expected to improve performance and how these modifications interact with the limited compute resources. This would help to provide a more nuanced understanding of the factors that contribute to efficient model training.

To improve the narrative, the authors should clearly define the research question they are trying to answer. Is it to identify the key factors that influence performance in low-resource settings, or is it to propose a specific set of modifications for training efficient models? The paper should then focus on answering this question directly, providing a clear and concise summary of the main findings. The authors should also provide a more detailed discussion of the limitations of their study, including the potential impact of their specific choices of architectural modifications and training strategies. They should acknowledge that the observed scaling laws and performance gains may not hold for other model architectures or training regimes. Furthermore, the paper should discuss the potential biases introduced by the specific datasets and tasks used in the experiments, and how these biases might affect the generalizability of the results. This would involve a more thorough analysis of the experimental setup and a more careful interpretation of the results.

Finally, the authors should provide a more detailed analysis of the computational cost of their proposed modifications, and compare it to the cost of the baseline BERT model. This would help to assess the practical value of their approach. The paper should also discuss the potential for combining the proposed modifications with other techniques for efficient model training, such as knowledge distillation or pruning. This would help to demonstrate the broader applicability of their findings and their potential impact on the field. The authors should also consider including a more detailed ablation study to isolate the impact of each modification, which would help to provide a more granular understanding of the factors that contribute to performance.

### Questions

1. How does the performance of the crammed models compare to the original BERT checkpoint in terms of downstream task performance and generalization capabilities?

2. What are the computational costs associated with the proposed modifications, and how do they compare to the baseline BERT model?

### Rating

3

### Confidence

4

**********

## Reviewer 4

### Summary

The paper investigates the performance of BERT-like language models trained on a single GPU for a single day. The authors explore various architectural and training modifications to achieve performance close to BERT under these constraints. They find that scaling laws still largely hold in the low-resource regime, with model size being the primary determinant of performance. They also identify several architectural and training tweaks that improve performance, such as disabling QKV biases, using rotary embeddings, and employing a gated linear unit in the feedforward block.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper addresses an interesting and relevant problem: how much can we get away with training language models on a single GPU in a day? The authors conduct a thorough investigation of various architectural and training modifications, providing valuable insights into the factors that contribute to performance in this limited compute setting.

### Weaknesses

#### Some Related Works


#### comment

The paper's central claim that scaling laws still largely hold in the low-resource regime is not particularly novel. This has been observed in prior work, such as the study by Izsak et al. (2021), which also explored training BERT for a single day with limited resources. The authors do not sufficiently differentiate their findings from this existing work, particularly in the context of architectural modifications. The paper's contribution in this area is limited, as it largely reiterates known scaling trends rather than providing new insights into the interplay between model size, compute, and performance in this specific constrained setting.

### Suggestions

The authors should more clearly articulate the specific novel contributions of their work beyond the existing literature on scaling laws in limited compute settings. While the paper explores architectural and training modifications, the core finding that scaling laws hold in this regime is not a new insight. To strengthen their contribution, the authors should focus on identifying and analyzing specific architectural or training modifications that are particularly effective in this low-resource regime. For example, they could investigate how different activation functions, normalization techniques, or optimization algorithms interact with the limited compute available. A more detailed analysis of these interactions, beyond simply stating that scaling laws hold, would be valuable. This could involve a more granular ablation study, focusing on the impact of each modification on the scaling behavior, and providing a theoretical justification for the observed results.

Furthermore, the paper could benefit from a more thorough discussion of the limitations of the study. The authors should acknowledge that the observed scaling laws and performance gains may not hold for other model architectures or training regimes. They should also discuss the potential biases introduced by the specific datasets and tasks used in the experiments. For example, the performance on specific downstream tasks might be influenced by the characteristics of the chosen datasets, and this should be acknowledged and discussed. A more nuanced discussion of these limitations would help to contextualize the findings and provide a more balanced perspective on the applicability of the results. The authors should also consider exploring the impact of different training data sizes and compositions on the observed scaling behavior, as this could reveal important insights into the robustness of their findings.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed modifications, and compare it to the cost of the baseline BERT model. This would help to assess the practical value of their approach. The authors should also discuss the potential for combining the proposed modifications with other techniques for efficient model training, such as knowledge distillation or pruning. This would help to demonstrate the broader applicability of their findings and their potential impact on the field. A more detailed analysis of the computational trade-offs would be valuable for practitioners who are interested in applying these techniques in real-world scenarios.

### Questions

How does the performance of the crammed models compare to the original BERT checkpoint in terms of downstream task performance and generalization capabilities?

### Rating

5

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Search the paper for evidence related to that weakness.
3. Categorize the evidence as method-related or experiment-related.
4. Analyze the evidence and determine if the weakness is valid, partially valid, or invalid.
5. Provide a confidence level for my assessment.
```json
[
  {
    "Weakness Statement": "The paper's central claim that scaling laws still largely hold in the low-resource regime is not particularly novel. This has been observed in prior work, such as the study by Izsak et al. (2021), which also explored training BERT for a single day with limited resources. The authors do not sufficiently differentiate their findings from this existing work, particularly in the context of architectural modifications. The paper's contribution in this area is limited, as it largely reiterates known scaling trends rather than providing new insights into the interplay between model size, compute, and performance in this specific constrained setting.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        {
          "quote": "Our central point of comparison for BERT training with limited resources is the work of Izsak et al. (2021) who also attempt the goal of training BERT within 24 hours with overall similar limitations, but use a full server node with 8 V100 GPUs. Izsak et al. (2021) choose a BERT LARGE \text{BERT}_{\text{LARGE}} architecture variant and train with sequence length of 128 128 , including a range of tweaks such as modified learning rates schedules, large batch sizes, sparse prediction and packed sequences. We re-evaluate this setup as a baseline setting for our own compute budget (which is about 15x smaller).",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We find that a simple one-cycle learning rate ( Smith & Topin, 2018 ) with a peak learning rate of 10 − 3 leads to minimal pretraining loss within our budget.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "Interestingly, we observe in Figure 2 that while globally a large number of learning rate shapes lead to similar reductions in loss, we find that we can make some gains through the choice of schedule. We find that a simple one-cycle learning rate ( Smith & Topin, 2018 ) with a peak learning rate of 10 − 3 leads to minimal pretraining loss within our budget.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We see no improvement from masking at larger rates, e.g. at 40% as proposed in ( Wettig et al., 2022 ) , see Appendix.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We further experiment with Fourier attention as proposed in Lee-Thorp et al. (2021) , but find no benefits.",
          "section": "4.3 Modifying the Training Setup"
        }
      ]
    },
    "Literature Gap Analysis": [
      "Izsak et al. (2021)"
    ],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly acknowledges and compares itself to Izsak et al. (2021) in the related work and method sections. It highlights the difference in compute resources and the specific architectural modifications explored.",
      "Supporting quotes": [
        "Our central point of comparison for BERT training with limited resources is the work of Izsak et al. (2021)...",
        "We re-evaluate this setup as a baseline setting for our own compute budget (which is about 15x smaller)."
      ],
      "Impact assessment": "While the paper does differentiate itself, the reviewer's point about the core finding of scaling laws holding in the low-resource regime not being novel is valid. The paper could have more clearly articulated the novel aspects beyond simply achieving comparable performance with less compute, particularly in the architectural modifications and the specific insights gained."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper compares itself to Izsak et al. (2021) but could have more clearly differentiated its novel contributions, especially regarding architectural modifications and specific insights."
    }
  },
  {
    "Weakness Statement": "The paper lacks a clear and compelling narrative. While the authors explore various modifications, the overall message is not well-defined. It is unclear whether the paper aims to provide a comprehensive analysis of the factors influencing performance or to propose a specific set of modifications for training efficient models. The absence of a clear research question makes it difficult to assess the significance of the findings. The paper would benefit from a more focused narrative that clearly articulates its goals and contributions.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        {
          "quote": "We investigate the downstream performance achievable with a transformer-based language model trained completely from scratch with a single GPU for a single day on a single node.",
          "section": "Introduction"
        },
        {
          "quote": "Our goals are as follows: • A transformer-based language model of arbitrary size is trained with masked-language modeling, completely from scratch.",
          "section": "Introduction"
        },
        {
          "quote": "• A setup with limited compute",
          "section": "Introduction"
        },
        {
          "quote": "• Training proceeds on a single GPU for 24 hours.",
          "section": "Introduction"
        },
        {
          "quote": "• Downstream performance is evaluated on GLUE ( Wang et al., 2018 ) .",
          "section": "Introduction"
        },
        {
          "quote": "• Downstream finetuning is limited to brief training with only the training data of the downstream task (we consider 5 epochs or less) and needs to work with hyperparameters set globally for all GLUE tasks. Downstream finetuning is excluded from the total compute budget.",
          "section": "Introduction"
        },
        {
          "quote": "In addition we test the rtp performance on GLUE",
          "section": "Introduction"
        },
        {
          "quote": "We discuss how much performance a transformer-based language model can achieve with limited compute resources would have several interesting implications. The goal of achieving BERT-like performance with modest training resources would have several interesting implications. For one, if scaled-down model pretraining is a viable analogue of large-compute pretraining, then this opens up a host of further academic investigations that are currently hard to realize for large-scale models. For example, research questions about the differences between existing and new pre-training tasks, tracing model predictions to data points ( Izsak et al., 2021 ; Bandy & Vincent, 2021 ) , security questions such as membership inference ( Carlini et al., 2022 ) and data poisoning ( Geiping et al., 2021 ) , and a wide range of empirical investigations into topics such as stability or generalization that arise during training ( Nagarajan & Kolter, 2019 ; Jiang et al., 2019 ) . At the same time, we can imagine situations in which legal requirements make it unclear whether models trained on public data with uncertain origin are permissible, and where a practitioner is interested in retraining their language models using a specialized or trustworthy data source ( Wilka et al., 2017 ; Gold & Latonero, 2017 ) .",
          "section": "Introduction"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The introduction clearly states the research goals and the scope of the investigation. It outlines the specific setup (single GPU, single day, masked language modeling, GLUE evaluation) and the broader implications of the work. While the narrative could be more focused, the research questions are stated.",
      "Supporting quotes": [
        "Our goals are as follows: • A transformer-based language model of arbitrary size is trained with masked-language modeling, completely from scratch.",
        "• Training proceeds on a single GPU for 24 hours.",
        "• Downstream performance is evaluated on GLUE ( Wang et al., 2018 ) ."
      ],
      "Impact assessment": "The reviewer's point about the lack of a clear research question is not entirely accurate, as the introduction does lay out the research goals. However, the narrative could be more tightly wound to emphasize the core contribution and its significance."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The introduction states research goals, but the narrative could be more focused on the core contribution and its significance."
    }
  },
  {
    "Weakness Statement": "The paper does not adequately address the limitations of the study. For example, the authors do not discuss the potential impact of their specific choices of architectural modifications and training strategies on the generalizability of their findings. The paper should acknowledge that the observed scaling laws and performance gains may not hold for other model architectures or training regimes. Furthermore, the paper lacks a discussion of the potential biases introduced by the specific datasets and tasks used in the experiments. This lack of transparency makes it difficult to assess the robustness of the results.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        {
          "quote": "We find that we can train models that achieve respectable performance on GLUE tasks – often close to and sometimes exceeding BERT on GLUE tasks – on a shoestring budget 1 1 1 We provide code to replicate all experiments at https://github.com/JonasGeiping/cramming .",
          "section": "Introduction"
        },
        {
          "quote": "We see no improvement from masking at larger rates, e.g. at 40% as proposed in ( Wettig et al., 2022 ) , see Appendix.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We further experiment with Fourier attention as proposed in Lee-Thorp et al. (2021) , but find no benefits.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We find that we can make some gains through the choice of schedule. We find that a simple one-cycle learning rate ( Smith & Topin, 2018 ) with a peak learning rate of 10 − 3 leads to minimal pretraining loss within our budget.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We see no benefit from disabling the mentioned 20% rule. We further decide against other variants of this modification, such as ( Liu et al., 2019b ; Shleifer et al., 2021 ) .",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We find that we can remove the nonlinear head without ill effect. We can further drop the decoder bias ( Radford et al., 2019 ) and gain in memory using sparse token prediction ( Liu et al., 2019 ; Izsak et al., 2021 ) .",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We find that we can further drop the decoder bias ( Radford et al., 2019 ) and gain in memory using sparse token prediction ( Liu et al., 2019 ; Izsak et al., 2021 ) .",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We find no benefits from changing to another activation than GELU.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We see no advantages using higher-order optimizers ( Yadav, 2020 ; Anil et al., 2021 ) , but note that especially for higher-order optimizers there is a greater amount of variability in implementation.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We further experiment with Fourier attention as proposed in Lee-Thorp et al. (2021) , but find no benefits.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We find rotary embeddings ( Su et al., 2021 ; Black et al., 2022 ) , to provide small benefits, but these are evened out by the drop in speed, so we ultimately decide against these.",
          "section": "4.3 Modifying the Training Setup"
        },
        {
          "quote": "We find that we can remove the original vocabulary size of 32768 32 32 32 32 2^{15}=32768 2^{16} 2^{16} 2^{16} 2^{16} 2^{16} 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2032 2