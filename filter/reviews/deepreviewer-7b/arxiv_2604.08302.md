I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new paradigm for training diffusion language models, called DMax. It introduces two key components: On-Policy Uniform Training (OPUT) and Soft Parallel Decoding (SPD). OPUT addresses the issue of error accumulation in masked decoding by training the model to recover clean tokens from both masked inputs and its own predicted tokens. SPD represents each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding, allowing iterative self-revising in embedding space. The authors demonstrate the effectiveness of DMax through extensive experiments, showing improvements in decoding efficiency and accuracy on various benchmarks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and addresses a significant issue in diffusion language models.
3. The experimental results are comprehensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed method. While the authors mention that the method improves decoding efficiency, they do not provide a clear comparison of the computational resources required by DMax and the baseline models. This makes it difficult to assess the practical benefits of the proposed method in terms of computational efficiency.
2. The paper does not provide a clear explanation of the hyperparameter settings used in the experiments. The authors mention that they use a fixed mask ratio of 0.75, but they do not explain how this value was chosen or whether it is optimal for different datasets or model architectures. A sensitivity analysis of the mask ratio would be beneficial to understand the impact of this hyperparameter on the performance of the model.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. While the authors demonstrate the effectiveness of DMax on several benchmarks, they do not discuss the potential challenges or limitations of the method in real-world applications. For example, it would be useful to understand how the method performs on datasets with different characteristics or under different decoding conditions.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with the proposed DMax method. While the authors claim improved decoding efficiency, a detailed breakdown of the computational resources required, including GPU memory usage and training time, is necessary to fully evaluate the practical implications of the method. Specifically, a comparison of the FLOPs (Floating Point Operations) required by DMax and the baseline models would provide a more concrete understanding of the computational overhead. Furthermore, it would be helpful to analyze the scaling behavior of the method with respect to model size and dataset size. This analysis should include a discussion of the trade-offs between decoding speed and accuracy, and how these trade-offs are affected by different model configurations. Such an analysis would allow readers to better assess the practical applicability of the method in resource-constrained environments.

To address the lack of clarity regarding hyperparameter settings, the authors should provide a more detailed explanation of the mask ratio selection process. While a fixed ratio of 0.75 is used, the paper should justify this choice with empirical evidence or theoretical arguments. A sensitivity analysis of the mask ratio, showing how the model's performance varies with different values, would be crucial. This analysis should include a discussion of the optimal mask ratio for different datasets and model architectures. Furthermore, the authors should explore the impact of other hyperparameters, such as the learning rate, batch size, and number of training epochs, on the performance of the model. This would provide a more comprehensive understanding of the method's robustness and generalizability. The authors should also discuss the potential for adaptive hyperparameter tuning during training.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. While the authors demonstrate strong performance on several benchmarks, it is important to acknowledge the potential challenges and limitations of DMax in real-world applications. For example, the authors should discuss how the method performs on datasets with different characteristics, such as those with longer sequences or more complex syntactic structures. It would also be useful to analyze the method's robustness to noisy or corrupted inputs. Furthermore, the authors should discuss the potential for error accumulation in the iterative self-revising process and how this can be mitigated. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the method's practical value.

### Questions

1. How does the proposed method handle the trade-off between decoding speed and accuracy? Is there a way to control this trade-off to achieve a desired balance between speed and accuracy?
2. How does the proposed method perform on datasets with different characteristics or under different decoding conditions? Are there any limitations or challenges in applying the method to real-world applications?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a new decoding strategy for diffusion language models, called Soft Parallel Decoding (SPD). The key idea is to represent each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding. This allows for iterative self-revising in embedding space. The authors also introduce On-Policy Uniform Training (OPUT), a training method that enables the model to recover clean tokens from both masked inputs and its own predicted tokens. The authors demonstrate the effectiveness of their method through extensive experiments on various benchmarks, showing improvements in decoding efficiency and accuracy.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is well-motivated and addresses a significant challenge in diffusion language models: error accumulation during parallel decoding.
2. The authors provide a thorough analysis of their method, including ablation studies and comparisons with baseline models. The experimental results are comprehensive and demonstrate the effectiveness of the proposed approach.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that their method improves decoding efficiency, but they do not provide a detailed analysis of the computational cost of their approach. It would be helpful to see a breakdown of the time and memory requirements of the proposed method, especially in comparison to existing decoding strategies. Specifically, the paper lacks a detailed analysis of the computational overhead introduced by the iterative self-revising process. The authors should provide a more granular breakdown of the time spent on each step of the decoding process, including the embedding interpolation and the iterative refinement, to allow for a more thorough comparison with existing methods.
2. The authors only evaluate their method on a limited set of benchmarks. It would be beneficial to see results on a wider range of datasets, including those with different characteristics (e.g., length, complexity, domain). The current evaluation does not fully demonstrate the generalizability of the proposed method. The paper should include a more diverse set of benchmarks, including datasets with varying sequence lengths, complexities, and domains, to provide a more comprehensive evaluation of the method's performance.
3. The authors do not discuss the limitations of their method or potential areas for future research. It would be valuable to see a discussion of the potential challenges and open questions related to the proposed approach. The paper should include a more detailed discussion of the limitations of the proposed method, such as its sensitivity to hyperparameter settings or its performance on specific types of inputs. Furthermore, the authors should discuss potential avenues for future research, such as exploring alternative interpolation techniques or applying the method to other types of diffusion models.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their proposed Soft Parallel Decoding (SPD) method. This should include a breakdown of the time and memory requirements for each step of the decoding process, including the embedding interpolation and the iterative refinement. A comparison with existing decoding strategies, such as standard parallel decoding and other iterative refinement methods, would be beneficial. This analysis should also consider the impact of different parameters, such as the number of iterations and the size of the interpolation, on the computational cost. Furthermore, the authors should investigate the scalability of their method to larger models and datasets, as the computational cost may increase significantly with larger models and longer sequences.

To strengthen the evaluation of their method, the authors should include a more diverse set of benchmarks, covering a wider range of datasets with different characteristics. This should include datasets with varying sequence lengths, complexities, and domains. For example, the authors could include datasets from natural language processing, code generation, or other relevant areas. The evaluation should also include a comparison with other state-of-the-art decoding methods, such as those based on reinforcement learning or adversarial training. This would provide a more comprehensive assessment of the performance of the proposed method and its potential advantages over existing approaches. The authors should also analyze the performance of their method on different types of inputs, such as those with high levels of noise or those that require complex reasoning.

Finally, the authors should include a more detailed discussion of the limitations of their proposed method and potential avenues for future research. This should include a discussion of the sensitivity of the method to hyperparameter settings, its performance on specific types of inputs, and its potential limitations in certain scenarios. The authors should also discuss potential avenues for future research, such as exploring alternative interpolation techniques, applying the method to other types of diffusion models, or investigating the use of the method in other applications. This discussion should also include a consideration of the potential ethical implications of the proposed method, such as its potential for misuse or its impact on fairness and bias.

### Questions

1. How does the proposed method compare to other decoding strategies in terms of computational cost and memory usage?
2. What are the limitations of the proposed method, and how can they be addressed in future work?
3. How does the proposed method perform on datasets with different characteristics or under different decoding conditions?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes a new paradigm for decoding diffusion language models (dLLMs) with improved decoding efficiency and accuracy. The authors introduce On-Policy Uniform Training (OPUT) and Soft Parallel Decoding (SPD) to address the issue of error accumulation in parallel decoding. OPUT enables the model to recover clean tokens from both masked inputs and its own predicted tokens, while SPD represents each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding, allowing iterative self-revision in embedding space. The authors demonstrate the effectiveness of their method through extensive experiments on various benchmarks, showing improvements in decoding efficiency and accuracy compared to existing models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation behind their approach and the technical details of their method.
2. The authors provide a comprehensive set of experiments to validate their method, including comparisons with multiple baselines and ablation studies to analyze the impact of different components. The results show that the proposed method achieves significant improvements in decoding efficiency and accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that their method improves decoding efficiency, but they do not provide a detailed analysis of the computational cost of their approach. It would be helpful to see a breakdown of the time and memory requirements of the proposed method, especially in comparison to existing decoding strategies. Specifically, the paper lacks a detailed breakdown of the computational cost associated with the soft parallel decoding (SPD) component. The iterative refinement process, while potentially beneficial for accuracy, could introduce significant overhead in terms of both time and memory usage, especially when compared to standard parallel decoding methods. A more thorough analysis is needed to understand the trade-offs between accuracy gains and computational costs.
2. The authors only evaluate their method on a limited set of benchmarks. It would be beneficial to see results on a wider range of datasets, including those with different characteristics (e.g., length, complexity, domain). The current evaluation does not fully demonstrate the generalizability of the proposed method. The paper should include a more diverse set of benchmarks, including datasets with varying sequence lengths, complexities, and domains, to provide a more comprehensive evaluation of the method's performance. This is crucial to understand the method's applicability across different types of text generation tasks.
3. The authors do not discuss the limitations of their method or potential areas for future research. It would be valuable to see a discussion of the potential challenges and open questions related to the proposed approach. The paper should include a more detailed discussion of the limitations of the proposed method, such as its sensitivity to hyperparameter settings or its performance on specific types of inputs. Furthermore, the authors should discuss potential avenues for future research, such as exploring alternative interpolation techniques or applying the method to other types of diffusion models.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their proposed method, specifically focusing on the soft parallel decoding (SPD) component. This analysis should include a breakdown of the time and memory requirements for each step of the decoding process, including the embedding interpolation and the iterative refinement. It would be beneficial to compare the computational cost of their method with existing decoding strategies, such as standard parallel decoding and other iterative refinement methods, to provide a clear understanding of the trade-offs between accuracy and efficiency. Furthermore, the authors should investigate the scalability of their method to larger models and datasets, as the computational cost may increase significantly with larger models and longer sequences. This analysis should also consider the impact of different parameters, such as the number of iterations and the size of the interpolation, on the computational cost.

To address the limited evaluation on a narrow set of benchmarks, the authors should include a more diverse set of datasets in their experiments. This should include datasets with varying sequence lengths, complexities, and domains, such as code generation, mathematical reasoning, and natural language understanding tasks. This would provide a more comprehensive evaluation of the method's performance and its generalizability across different types of text generation tasks. The authors should also consider evaluating their method on datasets with different characteristics, such as those with longer sequences or more complex syntactic structures, to assess its robustness. This would help to identify potential limitations of the method and guide future research directions.

Finally, the authors should include a more detailed discussion of the limitations of their proposed method and potential avenues for future research. This discussion should include an analysis of the sensitivity of the method to hyperparameter settings, such as the interpolation parameter and the number of iterations. The authors should also discuss the potential challenges of applying their method to different types of diffusion models and tasks. Furthermore, the authors should explore alternative interpolation techniques, such as non-linear interpolation or adaptive interpolation, to improve the performance of their method. The authors should also consider applying their method to other types of diffusion models, such as those used for image generation or audio synthesis, to assess its broader applicability.

### Questions

1. How does the proposed method compare to other decoding strategies in terms of computational cost and memory usage?
2. What are the limitations of the proposed method, and how can they be addressed in future work?
3. How does the proposed method perform on datasets with different characteristics or under different decoding conditions?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a new paradigm for efficient diffusion language models (dLLMs) by addressing the issue of error accumulation in parallel decoding. The authors introduce On-Policy Uniform Training (OPUT) and Soft Parallel Decoding (SPD) to improve decoding efficiency while preserving generation quality. OPUT enables the model to recover clean tokens from both masked inputs and its own predicted tokens, while SPD represents each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding. The authors demonstrate the effectiveness of their method through extensive experiments on various benchmarks, showing improvements in decoding efficiency and accuracy compared to existing models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and addresses a significant challenge in diffusion language models.
3. The experimental results are comprehensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed method. While the authors claim that their method improves decoding efficiency, they do not provide a clear comparison of the computational resources required by DMax and the baseline models. This makes it difficult to assess the practical benefits of the proposed method in terms of computational efficiency.
2. The paper does not provide a thorough discussion of the limitations of the proposed method. While the authors demonstrate the effectiveness of their method on several benchmarks, they do not discuss the potential challenges or limitations of the method in real-world applications. For example, it would be useful to understand how the method performs on datasets with different characteristics or under different decoding conditions.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their proposed method. This should include a breakdown of the time and memory requirements for each step of the decoding process, including the embedding interpolation and the iterative refinement. A comparison with existing decoding strategies, such as standard parallel decoding and other iterative refinement methods, would be beneficial to understand the trade-offs between accuracy and efficiency. Furthermore, the authors should investigate the scalability of their method to larger models and datasets, as the computational cost may increase significantly with larger models and longer sequences. This analysis should also consider the impact of different parameters, such as the number of iterations and the size of the interpolation, on the computational cost.

To address the limitations of the proposed method, the authors should include a more thorough discussion of potential challenges and areas for future research. This should include an analysis of the sensitivity of the method to hyperparameter settings, such as the interpolation parameter and the number of iterations. The authors should also discuss the potential challenges of applying their method to different types of diffusion models and tasks. Furthermore, the authors should explore alternative interpolation techniques, such as non-linear interpolation or adaptive interpolation, to improve the performance of their method. The authors should also consider applying their method to other types of diffusion models, such as those used for image generation or audio synthesis, to assess its broader applicability. A more detailed discussion of these aspects would provide a more comprehensive understanding of the proposed method and its potential impact.

Finally, the authors should consider including a more detailed analysis of the error accumulation phenomenon in parallel decoding. While the paper mentions this issue, a more in-depth analysis of the underlying causes and the impact of different decoding strategies on error accumulation would be beneficial. This could include an analysis of the error propagation during the decoding process and the factors that contribute to the accumulation of errors. This analysis could also provide insights into how to design more robust decoding strategies that minimize error accumulation. A more thorough understanding of this issue would further strengthen the motivation for the proposed method and its contribution to the field.

### Questions

1. How does the proposed method compare to other decoding strategies in terms of computational cost and memory usage?
2. What are the limitations of the proposed method, and how can they be addressed in future work?
3. How does the proposed method perform on datasets with different characteristics or under different decoding conditions?

### Rating

6

### Confidence

4

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
```json
[
  {
    "Weakness Statement": "The authors claim that their method improves decoding efficiency, but they do not provide a detailed analysis of the computational cost of their approach. It would be helpful to see a breakdown of the time and memory requirements of the proposed method, especially in comparison to existing decoding strategies. Specifically, the paper lacks a detailed analysis of the computational overhead introduced by the iterative self-revising process. The authors should provide a more granular breakdown of the time spent on each step of the decoding process, including the embedding interpolation and the iterative refinement, to allow for a more thorough comparison with existing methods.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "Table 1 also compares our method with conventional uniform diffusion training. The latter neither improves decoding speed nor preserves model quality, instead causing a noticeable performance drop. We find that this failure stems from the large mismatch between the randomly sampled noisy sequences used in training and the model’s actual decoding trajectories at inference time. Consequently, the model struggles to revise erroneous predictions while unnecessarily perturbing correct ones, resulting in unstable oscillations within each block. By contrast, our on-policy training samples noisy sequences from the model’s own outputs, effectively bridging this train–inference gap and substantially improving self-revision under parallel decoding.",
          "section": "4.1 Experimental Setup"
        },
        {
          "quote": "On LLaDA-2.0-mini, our method improves GSM8K accuracy from 78 % 78\% to 90 % 90\% under confidence-threshold decoding with a threshold of 0 0 , while also delivering faster decoding.",
          "section": "4.1 Experimental Setup"
        },
        {
          "quote": "On LLaDA-2.0-mini, our method improves GSM8K accuracy from 78 % 78\% to 90 % 90\% under confidence-threshold decoding with a threshold of 0 0 , while also delivering faster decoding.",
          "section": "4.1 Experimental Setup"
        },
        {
          "quote": "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy. The key ingredient of SPD is to use soft embeddings, rather than discrete tokens, as intermediate decoding states. Maintaining the non-masked region as a contiguous prefix further improves performance. Another important result is that OPUT is a prerequisite for SPD. As shown in Table 3 , directly applying SPD to the original model causes generation to collapse. This is because OPUT trains the model to recover the correct target not only from masked inputs, but also from its own sampled predictions. As a result, the model learns a consistent mapping from both mask embeddings and self-predicted token embeddings toward the correct output, which makes interpolation between their embeddings a meaningful and effective input for denoising.",
          "section": "4.2 Experimental Results"
        },
        {
          "quote": "Table 1 also compares our method with conventional uniform diffusion training. The latter neither improves decoding speed nor preserves model quality, instead causing a noticeable performance drop. We find that this failure stems from the large mismatch between the randomly sampled noisy sequences used in training and the model’s actual decoding trajectories at inference time. Consequently, the model struggles to revise erroneous predictions while unnecessarily perturbing correct ones, resulting in unstable oscillations within each block. By contrast, our on-policy training samples noisy sequences from the model’s own outputs, effectively bridging this train–inference gap and substantially improving self-revision under parallel decoding.",
          "section": "4.1 Experimental Setup"
        },
        {
          "quote": "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy. The key ingredient of SPD is to use soft embeddings, rather than discrete tokens, as intermediate decoding states. Maintaining the non-masked region as a contiguous prefix further improves performance. Another important result is that OPUT is a prerequisite for SPD. As shown in Table 3 , directly applying SPD to the original model causes generation to collapse. This is because OPUT trains the model to recover the correct target not only from masked inputs, but also from its own sampled predictions. As a result, the model learns a consistent mapping from both mask embeddings and self-predicted token embeddings toward the correct output, which makes interpolation between their embeddings a meaningful and effective input for denoising.",
          "section": "4.2 Experimental Results"
        },
        {
          "quote": "Table 3 presents a comprehensive ablation study of both our training and inference strategies. We compare different combinations of training and decoding strategies on GSM8K under three decoding thresholds, τ dec ∈ { 0.95 , 0.5 , 0.0 } \tau_{\mathrm{dec}}\in\{0.95,0.5,0.0\} . On-policy rollout is the core of our training method. Even with OPUT alone, the model acquires the ability to revise its own errors, yielding substantial accuracy gains over the original model at τ dec = 0.5 \tau_{\mathrm{dec}}=0.5 and 0.0 0.0 . Our proposed SPD further improves robustness when many erroneous predictions emerge simultaneously, allowing the accuracy on GSM8K to reach only 68 % 68\% while achieving a higher speedup.",
          "section": "4.2 Experimental Results"
        }
      ],
      "Missing specifications": [
        "The paper does not provide a detailed breakdown of the time and memory requirements of the proposed method compared to existing decoding strategies."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The reviewer correctly points out the lack of a detailed computational cost analysis. While the paper mentions improvements in decoding speed and provides some comparisons in Table 1, it doesn't offer a granular breakdown of time and memory usage compared to baselines.",
      "Supporting quotes": [
        "Table 1 also compares our method with conventional uniform diffusion training.",
        "On LLaDA-2.0-mini, our method improves GSM8K accuracy from 78 % 78\% to 90 % 90\% under confidence-threshold decoding with a threshold of 0 0 , while also delivering faster decoding.",
        "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy."
      ],
      "Impact assessment": "The absence of a detailed computational cost analysis makes it difficult to fully assess the practical benefits of the proposed method in terms of efficiency."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a detailed breakdown of time and memory requirements compared to baselines."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a clear explanation of the hyperparameter settings used in the experiments. The authors mention that they use a fixed mask ratio of 0.75, but they do not explain how this value was chosen or whether it is optimal for different datasets or model architectures. A sensitivity analysis of the mask ratio would be beneficial to understand the impact of this hyperparameter on the performance of the model.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We build our method on LLaDA-2.0-mini [ 10 ] , a state-of-the-art open-source diffusion language model. During training, we use OPUT with a fixed mask ratio of 0.75.",
          "section": "4.1 Experimental Setup"
        }
      ],
      "Missing specifications": [
        "The paper does not provide a justification for the choice of the mask ratio of 0.75.",
        "There is no sensitivity analysis of the mask ratio."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The reviewer is correct. The paper mentions using a fixed mask ratio of 0.75 but doesn't explain the reasoning behind this choice or provide any analysis of its impact on performance.",
      "Supporting quotes": [
        "During training, we use OPUT with a fixed mask ratio of 0.75."
      ],
      "Impact assessment": "Without a justification or sensitivity analysis, it's unclear if the chosen mask ratio is optimal and how the method's performance might vary with different values."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper states the use of a fixed mask ratio of 0.75 without providing justification or sensitivity analysis."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the limitations of the proposed method. While the authors demonstrate the effectiveness of DMax on several benchmarks, they do not discuss the potential challenges or limitations of the method in real-world applications. For example, it would be useful to understand how the method performs on datasets with different characteristics or under different decoding conditions.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "Table 2 presents a comprehensive ablation study of both our training and inference strategies. We compare different combinations of training and decoding strategies on GSM8K under three decoding thresholds, τ dec ∈ { 0.95 , 0.5 , 0.0 } \tau_{\mathrm{dec}}\in\{0.95,0.5,0.0\} . On-policy rollout is the core of our training method. Even with OPUT alone, the model acquires the ability to revise its own errors, yielding substantial accuracy gains over the original model at τ dec = 0.5 \tau_{\mathrm{dec}}=0.5 and 0.0 0.0 . Our proposed SPD further improves robustness when many erroneous predictions emerge simultaneously, allowing the accuracy on GSM8K to reach only 68 % 68\% while achieving a higher speedup.",
          "section": "4.2 Experimental Results"
        },
        {
          "quote": "Ablation Study on Training and Inference Strategies. Table 3 presents a comprehensive ablation study of both our training and decoding strategies on GSM8K under three decoding thresholds, τ dec ∈ { 0.95 , 0.5 , 0.0 } \tau_{\mathrm{dec}}\in\{0.95,0.5,0.0\} . On-policy rollout is the core of our training method. Even with OPUT alone, the model acquires the ability to revise its own errors, yielding substantial accuracy gains over the original model at τ dec = 0.5 \tau_{\mathrm{dec}}=0.5 and 0.0 0.0 . Our proposed SPD further improves robustness when many erroneous predictions emerge simultaneously, allowing the accuracy on GSM8K to reach only 68 % 68\% while achieving a higher speedup. Another important result is that OPUT is a prerequisite for SPD. As shown in Table 3 , directly applying SPD to the original model causes generation to collapse. This is because OPUT trains the model to recover the correct target not only from masked inputs, but also from its own sampled predictions. As a result, the model learns a consistent mapping from both mask embeddings and self-predicted token embeddings toward the correct output, which makes interpolation between their embeddings a meaningful and effective input for denoising.",
          "section": "4.2 Experimental Results"
        },
        {
          "quote": "Superior Efficiency–Performance Trade-off. Figure 4 compares the accuracy–TPF trade-off curves of our method and the original model on GSM8K, MATH500, HumanEval, and MBPP. As TPF increases, the original model suffers a sharp accuracy drop, whereas our method maintains stable performance. For instance, on MATH500, at around 6.5 TPF, our method still retains over 71.6% accuracy, while the original model falls to 15.2%. The gap is even larger on code benchmarks: on MBPP, at a similar TPF, our method achieves 79.2%, whereas the original model drops to only 2.3%. This superior trade-off stems from the self-revision capability of our paradigm, which effectively mitigates error accumulation under aggressive parallel decoding.",
          "section": "4.2 Experimental Results"
        }
      ],
      "Missing specifications": [
        "The paper does not explicitly discuss the limitations of the proposed method in terms of real-world applications or performance on datasets with different characteristics.",
        "While the paper shows results on several benchmarks, a deeper discussion on potential failure cases or limitations in specific scenarios is missing."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The reviewer is correct. While the paper demonstrates effectiveness on several benchmarks, it lacks a dedicated discussion on the limitations and potential challenges in real-world applications.",
      "Supporting quotes": [],
      "Impact assessment": "The absence of a limitations section makes it harder to understand the scope and potential drawbacks of the proposed method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper focuses on demonstrating effectiveness but lacks a dedicated discussion on limitations and real-world applicability."
    }
  },
  {
    "Weakness Statement": "How does the proposed method compare to other decoding strategies in terms of computational cost and memory usage?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy. The key ingredient of SPD is to use soft embeddings, rather than discrete tokens, as intermediate decoding states. Maintaining the non-masked region as a contiguous prefix further improves performance. Another important result is that OPUT is a prerequisite for SPD. As shown in Table 3 , directly applying SPD to the original model causes generation to collapse. This is because OPUT trains the model to recover the correct target not only from masked inputs, but also from its own sampled predictions. As a result, the model learns a consistent mapping from both mask embeddings and self-predicted token embeddings toward the correct output, which makes interpolation between their embeddings a meaningful and effective input for denoising.",
          "section": "4.2 Experimental Results"
        },
        {
          "quote": "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy.",
          "section": "4.2 Experimental Results"
        },
        {
          "quote": "On LLaDA-2.0-mini, our method improves GSM8K accuracy from 78 % 78\% to 90 % 90\% under confidence-threshold decoding with a threshold of 0 0 , while also delivering faster decoding.",
          "section": "4.1 Experimental Setup"
        }
      ],
      "Missing specifications": [
        "The paper does not provide a direct comparison of computational cost and memory usage with other decoding strategies."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The reviewer's question highlights a gap in the paper. While the paper shows improved accuracy and speed, it doesn't provide a direct comparison of computational cost and memory usage with other decoding methods.",
      "Supporting quotes": [
        "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy.",
        "On LLaDA-2.0-mini, our method improves GSM8K accuracy from 78 % 78\% to 90 % 90\% under confidence-threshold decoding with a threshold of 0 0 , while also delivering faster decoding."
      ],
      "Impact assessment": "Without this comparison, it's difficult to fully assess the practical trade-offs of the proposed method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a direct comparison of computational cost and memory usage with other decoding strategies."
    }
  },
  {
    "Weakness Statement": "What are the limitations of the proposed method, and how can they be addressed in future work?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "Superior Efficiency–Performance Trade-off. Figure 4 compares the accuracy–TPF trade-off curves of our method and the original model on GSM8K, MATH500, HumanEval, and MBPP. As TPF increases, the original model suffers a sharp accuracy drop, whereas our method maintains stable performance. For instance, on MATH500, at around 6.5 TPF, our method still retains over 71.6% accuracy, while the original model falls to 15.2%. The gap is even larger on code benchmarks: on MBPP, at a similar TPF, our method achieves 79.2%, whereas the original model drops to only 2.3%. This superior trade-off stems from the self-revision capability of our paradigm, which effectively mitigates error accumulation under aggressive parallel decoding.",
          "section": "4.2 Experimental Results"
        },
        {
          "quote": "Ablation Study on Training and Inference Strategies. Table 3 presents a comprehensive ablation study of both our training and decoding strategies on GSM8K under three decoding thresholds, τ dec ∈ { 0.95 , 0.5 , 0.0 } \tau_{\mathrm{dec}}\in\{0.95,0.5,0.0\} . On-policy rollout is the core of our training method. Even with OPUT alone, the model acquires the ability to revise its own errors, yielding substantial accuracy gains over the original model at τ dec = 0.5 \tau_{\mathrm{dec}}=0.5 and 0.0 0.0 . Our proposed SPD further improves robustness when many erroneous predictions emerge simultaneously, allowing the accuracy on GSM8K to reach only 68 % 68\% while achieving a higher speedup. Another important result is that OPUT is a prerequisite for SPD. As shown in Table 3 , directly applying SPD to the original model causes generation to collapse. This is because OPUT trains the model to recover the correct target not only from masked inputs, but also from its own sampled predictions. As a result, the model learns a consistent mapping from both mask embeddings and self-predicted token embeddings toward the correct output, which makes interpolation between their embeddings a meaningful and effective input for denoising.",
          "section": "4.2 Experimental Results"
        }
      ],
      "Missing specifications": [
        "The paper does not explicitly discuss the limitations of the proposed method or potential avenues for future research to address these limitations."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The reviewer is correct. The paper focuses on the strengths of the proposed method but doesn't delve into its limitations or suggest future research directions to overcome them.",
      "Supporting quotes": [
        "Superior Efficiency–Performance Trade-off.",
        "Ablation Study on Training and Inference Strategies."
      ],
      "Impact assessment": "The lack of a discussion on limitations makes it harder to understand the scope and potential drawbacks of the method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a dedicated section discussing the limitations of the proposed method and potential future work."
    }
  },
  {
    "Weakness Statement": "How does the proposed method perform on datasets with different characteristics or under different decoding conditions?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "Table 1 also compares our method with conventional uniform diffusion training. The latter neither improves decoding speed nor preserves model quality, instead causing a noticeable performance drop. We find that this failure stems from the large mismatch between the randomly sampled noisy sequences used in training and the model’s actual decoding trajectories at inference time. Consequently, the model struggles to revise erroneous predictions while unnecessarily perturbing correct ones, resulting in unstable oscillations within each block. By contrast, our on-policy training samples noisy sequences from the model’s own outputs, effectively bridging this train–inference gap and substantially improving self-revision under parallel decoding.",
          "section": "4.1 Experimental Setup"
        },
        {
          "quote": "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy. The key ingredient of SPD is to use soft embeddings, rather than discrete tokens, as intermediate decoding states. Maintaining the non-masked region as a contiguous prefix further improves performance. Another important result is that OPUT is a prerequisite for SPD. As shown in Table 3 , directly applying SPD to the original model causes generation to collapse. This is because OPUT trains the model to recover the correct target not only from masked inputs, but also from its own sampled predictions. As a result, the model learns a consistent mapping from both mask embeddings and self-predicted token embeddings toward the correct output, which makes interpolation between their embeddings a meaningful and effective input for denoising.",
          "section": "4.2 Experimental Results"
        },
        {
          "quote": "Table 1 also compares our method with conventional uniform diffusion training. The latter neither improves decoding speed nor preserves model quality, instead causing a noticeable performance drop. We find that this failure stems from the large mismatch between the randomly sampled noisy sequences used in training and the model’s actual decoding trajectories at inference time. Consequently, the model struggles to revise erroneous predictions while unnecessarily perturbing correct ones, resulting in unstable oscillations within each block. By contrast, our on-policy training samples noisy sequences from the model’s own outputs, effectively bridging this train–inference gap and substantially improving self-revision under parallel decoding.",
          "section": "4.1 Experimental Setup"
        }
      ],
      "Missing specifications": [
        "The paper evaluates the method on several datasets, but a systematic analysis of performance across datasets with different characteristics (e.g., length, complexity, domain) is not explicitly presented in a dedicated section.",
        "While the paper explores different decoding thresholds, a comprehensive analysis of performance under various decoding conditions beyond these explored thresholds is missing."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The reviewer's question points to an area where the paper could be strengthened. While the paper shows results on multiple datasets, a dedicated analysis of performance across datasets with varying characteristics and under different decoding conditions is not explicitly provided.",
      "Supporting quotes": [
        "Table 1 also compares our method with conventional uniform diffusion training.",
        "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy."
      ],
      "Impact assessment": "A more detailed analysis of performance across different dataset characteristics and decoding conditions would provide a more comprehensive understanding of the method's robustness and generalizability."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "Medium",
      "Key supporting evidence": "The paper presents results on multiple datasets, but a dedicated and systematic analysis of performance across datasets with different characteristics and under various decoding conditions is lacking."
    }
  },
  {
    "Weakness Statement": "The authors claim that their method improves decoding efficiency, but they do not provide a detailed analysis of the computational cost of their approach. It would be helpful to see a breakdown of the time and memory requirements of the proposed method, especially in comparison to existing decoding strategies. Specifically, the paper lacks a detailed analysis of the computational overhead introduced by the iterative self-revising process. The authors should provide a more granular breakdown of the time spent on each step of the decoding process, including the embedding interpolation and the iterative refinement, to allow for a more thorough comparison with existing methods.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "Table 1 also compares our method with conventional uniform diffusion training. The latter neither improves decoding speed nor preserves model quality, instead causing a noticeable performance drop. We find that this failure stems from the large mismatch between the randomly sampled noisy sequences used in training and the model’s actual decoding trajectories at inference time. Consequently, the model struggles to revise erroneous predictions while unnecessarily perturbing correct ones, resulting in unstable oscillations within each block. By contrast, our on-policy training samples noisy sequences from the model’s own outputs, effectively bridging this train–inference gap and substantially improving self-revision under parallel decoding.",
          "section": "4.1 Experimental Setup"
        },
        {
          "quote": "On LLaDA-2.0-mini, our method improves GSM8K accuracy from 78 % 78\% to 90 % 90\% under confidence-threshold decoding with a threshold of 0 0 , while also delivering faster decoding.",
          "section": "4.1 Experimental Setup"
        },
        {
          "quote": "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy. The key ingredient of SPD is to use soft embeddings, rather than discrete tokens, as intermediate decoding states. Maintaining the non-masked region as a contiguous prefix further improves performance. Another important result is that OPUT is a prerequisite for SPD. As shown in Table 3 , directly applying SPD to the original model causes generation to collapse. This is because OPUT trains the model to recover the correct target not only from masked inputs, but also from its own sampled predictions. As a result, the model learns a consistent mapping from both mask embeddings and self-predicted token embeddings toward the correct output, which makes interpolation between their embeddings a meaningful and effective input for denoising.",
          "section": "4.2 Experimental Results"
        }
      ],
      "Missing specifications": [
        "The paper lacks a detailed breakdown of the time and memory requirements of the proposed method compared to existing decoding strategies.",
        "There is no granular breakdown of the time spent on each step of the decoding process, such as embedding interpolation and iterative refinement."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The reviewer is correct. While the paper claims improved decoding efficiency and shows speedups in some experiments, it lacks a detailed analysis of the computational cost, including a breakdown of time and memory usage and a comparison with existing methods.",
      "Supporting quotes": [
        "On LLaDA-2.0-mini, our method improves GSM8K accuracy from 78 % 78\% to 90 % 90\% under confidence-threshold decoding with a threshold of 0 0 , while also delivering faster decoding.",
        "On OPUT-trained LLaDA-2.0-mini, under the highly aggressive setting of τ dec = 0 \tau_{\mathrm{dec}}=0 , soft parallel decoding improves TPF by 6.2 while maintaining accuracy."
      ],
      "Impact assessment": "The absence of a detailed computational cost analysis makes it difficult to fully assess the practical benefits of the proposed method in terms of efficiency."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a detailed breakdown of the time and memory requirements of the proposed method compared to existing decoding strategies."
    }
  },
  {
    "Weakness Statement": "The authors only evaluate their method on a limited set of benchmarks. It would be beneficial to see results on a wider range of datasets, including those with different characteristics (e.g., length, complexity, domain). The current evaluation does not fully demonstrate the generalizability of the proposed method. The paper should include a more diverse set of benchmarks, including datasets with varying sequence lengths, complexities, and domains, to provide a more comprehensive evaluation of the method's performance.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We evaluate our method on multiple benchmarks. For mathematical reasoning, we use GSM8K [ 20 ] , MATH500 [ 44 ] , a subset of Numina-Math [ 40 ] , and a subset of OpenThoughts [ 26 ] . For code generation, we use the instruction versions of HumanEval [ 54 ] and MBPP [ 5 ] . All evaluations are conducted with the dInFer [ 54 ] framework on 2 H200 GPUs using tensor parallelism.",
          "section": "4.1 Experimental Setup"
        },
        {
          "quote": "Table 1 also compares our method with conventional uniform diffusion training. The latter neither improves decoding speed nor preserves model quality, instead causing a noticeable performance drop. We find that this failure stems from the large mismatch between the randomly sampled noisy sequences used in training and the model’s actual decoding trajectories at inference time. Consequently, the model struggles to revise erroneous predictions while unnecessarily perturbing correct ones, resulting in unstable oscillations within each block. By contrast, our on-policy training samples noisy sequences from the model’s own outputs, effectively bridging this train–inference gap and substantially improving self-revision under parallel decoding.",
          "section": "4.1 Experimental Setup"
        }
      ],
      "Missing specifications": [
        "The paper evaluates the method on a reasonable number of benchmarks, covering different tasks (mathematical reasoning and code generation).",
        "While the paper includes benchmarks with varying complexities, it doesn't explicitly detail the range of sequence lengths or domains covered by the datasets used."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The reviewer's claim is partially valid. The paper does evaluate on a reasonable number of benchmarks covering different tasks, but the paper doesn't explicitly detail the range of sequence lengths or domains covered by the datasets used, which could be seen as a limitation in demonstrating generalizability across all possible dataset characteristics.",
      "Supporting quotes": [
        "We evaluate our method on multiple benchmarks. For mathematical reasoning, we use GSM8K [ 20 ] , MATH500 [ 44 ] , a subset of Numina-Math [ 40 ] , and a subset of OpenThoughts [ 26 ] . For code generation, we use the instruction versions of HumanEval [ 54 ] and MBPP [ 5 ] ."
      ],
      "Impact assessment": "While the evaluation is not on an *extremely* large number of datasets, the chosen benchmarks are relevant and cover different aspects of language understanding and generation."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "Medium",
      "Key supporting evidence": "The paper evaluates on a reasonable number of benchmarks, but lacks explicit details on the range of sequence lengths and domains covered."
    }
  },
  {
    "Weakness Statement": "The authors do not discuss the limitations of their method or potential areas for future research. It would be valuable to see a discussion of the potential challenges and open questions related to the proposed approach. The paper should include a more detailed discussion of the limitations of the proposed method, such as its sensitivity to hyperparameter settings or its performance on specific types of inputs. Furthermore, the authors should discuss potential avenues for future research, such as exploring alternative interpolation techniques, applying the method to other types of diffusion models, or investigating the use of the method in other applications. This discussion would also include a consideration of the potential ethical implications of the proposed method, such as its potential for misuse or its impact on fairness and bias.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "Table 3 presents a comprehensive ablation study of both our training and decoding strategies on GSM8K under three decoding thresholds, τ dec ∈ { 0.95 , 0.5 , 0.0 } \tau_{\mathrm{dec}}\in\{0.95,0.5,0.0\} . On-policy rollout is the core of our training method. Even with OPUT alone, the model acquires the ability to revise its own errors, yielding substantial accuracy gains over the original model at τ dec = 0.5 \tau_{\mathrm{dec}}=0.5 and 0.0 0.0 . Our proposed SPD further improves robustness when many erroneous predictions emerge simultaneously, allowing the accuracy on GSM8K to reach only 68 % 68\% while achieving a higher speedup. Another important result is that OPUT is a prerequisite for SPD. As shown in Table 3 , directly applying SPD to the original model causes generation to collapse. This is because OPUT trains the model to recover the correct target not only from masked inputs, but also from its own sampled predictions. As a result, the model learns a consistent mapping from both mask embeddings and self-predicted token embeddings toward the correct output, which makes interpolation between their embeddings a meaningful and effective input for denoising.",
          "section": "4.2 Experimental Results"
        },
        {
          "quote": "Superior Efficiency–Performance Trade-off. Figure 4 compares the accuracy–TPF trade-off curves of our method and the original model on GSM8K, MATH500, HumanEval, and MBPP. As TPF increases, the original model suffers a sharp accuracy drop, whereas our method maintains stable performance. For instance, on MATH500, at around 6.5 TPF, our method still retains over 71.6% accuracy, while the original model falls to 15.2%. The gap is even larger on code benchmarks: on MBPP, at a similar TPF, our method achieves 79.2%, whereas the original model drops to only 2.3%. This superior trade-off stems from the self-revision capability of our paradigm, which effectively mitigates error accumulation under aggressive parallel decoding.",
          "section": "4.2 Experimental Results"
        }
      ],
      "Missing specifications": [
        "The paper lacks a dedicated section discussing the limitations of the proposed method, including its sensitivity to hyperparameter settings or performance on specific types of inputs.",
        "There is no discussion of potential avenues for future research, such as exploring alternative interpolation techniques, applying the method to other types of diffusion models, or investigating the use of the method in other applications.",
        "The paper does not discuss potential ethical implications of the proposed method, such as its potential for misuse or its impact on fairness and bias."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The reviewer is correct. The paper lacks a dedicated discussion of the limitations of the proposed method, potential areas for future research, and ethical implications.",
      "Supporting quotes": [
        "Table 3 presents a comprehensive ablation study of both our training and decoding strategies on GSM8K under three decoding thresholds, τ dec ∈ { 0.95 , 0.5 , 0.0 } \tau_{\mathrm{dec}}\in\{0.95,0.5,0.0\} .",
        "Superior Efficiency–Performance Trade-off."
      ],
      "Impact assessment": "The absence of a limitations section and discussion of future work and ethical considerations makes the paper less complete and leaves open important questions for future research and practical applications."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a dedicated discussion of the limitations of the proposed method, potential areas for future research, and ethical implications."
    }
  },
  {
    "Weakness Statement": "How does the proposed method compare to other decoding strategies in terms of computational cost and memory usage?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "Table 1 also compares our method with conventional uniform diffusion training. The latter neither improves decoding speed nor preserves model quality, instead causing a noticeable performance drop. We find that this failure stems from the large mismatch between the randomly sampled noisy sequences used in training and the model’s actual decoding trajectories at inference time. Consequently, the model struggles to revise erroneous predictions while unnecessarily perturbing correct ones, resulting in unstable oscillations within each block. By contrast, our on-policy training samples noisy sequences from the model’s own outputs, effectively bridging this train–inference gap and substantially improving self-revision under parallel decoding.",
          "section": "4.1 Experimental Setup"
        },
        {
          "quote": "On LLa}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces DMax, a novel paradigm for efficient diffusion language models (dLLMs) that aims to address the issue of error accumulation during parallel decoding. The authors propose two key components: On-Policy Uniform Training (OPUT) and Soft Parallel Decoding (SPD). OPUT is designed to enable the model to recover clean tokens from both masked inputs and its own predicted tokens, effectively bridging the gap between training and inference. This is achieved by training the model to recover the correct target from both masked inputs and its own predicted tokens. SPD, on the other hand, represents each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding, allowing for iterative self-revising in embedding space. This approach enables the model to revise its predictions iteratively, leading to improved decoding efficiency and accuracy. The authors demonstrate the effectiveness of DMax through extensive experiments on various benchmarks, including mathematical reasoning (GSM8K, MATH500, Numina-Math, OpenThoughts) and code generation (HumanEval, MBPP). The results show significant improvements in decoding efficiency and accuracy compared to existing models. Specifically, the paper reports that DMax achieves a higher trade-off between accuracy and tokens per forward (TPF) compared to the original model, indicating a better balance between performance and speed. The authors also provide ablation studies to analyze the impact of different components of their method, such as the on-policy training strategy and the soft parallel decoding approach. Overall, the paper presents a well-motivated and empirically validated approach to improving the efficiency of dLLMs, with a focus on addressing the challenges of parallel decoding and error accumulation. The proposed method, DMax, offers a promising direction for future research in this area, with potential applications in various natural language processing tasks.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

I found several aspects of this paper to be particularly strong. The core idea of addressing error accumulation in parallel decoding is both timely and relevant, given the increasing interest in dLLMs and their limitations in terms of decoding efficiency. The proposed method, DMax, is well-motivated and addresses a significant challenge in the field. The authors' approach of using On-Policy Uniform Training (OPUT) to enable the model to recover clean tokens from both masked inputs and its own predicted tokens is a novel and effective way to bridge the gap between training and inference. This is a crucial step towards making dLLMs more robust and reliable. The introduction of Soft Parallel Decoding (SPD) is another significant contribution. By representing each intermediate decoding state as an interpolation between the predicted token embedding and the mask embedding, the authors enable the model to revise its predictions iteratively in embedding space. This approach is not only conceptually elegant but also empirically effective, as demonstrated by the experimental results. The experimental results presented in the paper are comprehensive and convincing. The authors have conducted experiments on a variety of benchmarks, including mathematical reasoning and code generation tasks, and have shown that DMax achieves significant improvements in both accuracy and decoding efficiency compared to existing models. The ablation studies are also well-designed and provide valuable insights into the impact of different components of the proposed method. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors clearly explain their motivation, methodology, and experimental results, which makes the paper a pleasure to read. Overall, I believe that this paper makes a valuable contribution to the field of dLLMs and provides a solid foundation for future research in this area.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the authors claim that their method improves decoding efficiency, they do not provide a detailed analysis of the computational cost of their approach. Specifically, the paper lacks a granular breakdown of the time and memory requirements of the proposed method, especially in comparison to existing decoding strategies. The authors mention that DMax achieves faster decoding, but they do not provide a detailed analysis of the time spent on each step of the decoding process, such as embedding interpolation and the iterative refinement. This lack of a detailed computational cost analysis makes it difficult to fully assess the practical trade-offs between accuracy and efficiency. For example, the paper does not provide a comparison of the FLOPs (Floating Point Operations) required by DMax and the baseline models, nor does it analyze the scaling behavior of the method with respect to model size and dataset size. This is a significant omission, as the computational cost is a crucial factor in determining the practical applicability of a method. My confidence in this weakness is high, as the paper explicitly lacks this analysis. Second, the paper does not provide a clear explanation of the hyperparameter settings used in the experiments. While the authors mention that they use a fixed mask ratio of 0.75, they do not explain how this value was chosen or whether it is optimal for different datasets or model architectures. A sensitivity analysis of the mask ratio would be beneficial to understand the impact of this hyperparameter on the performance of the model. The paper should justify this choice with empirical evidence or theoretical arguments. My confidence in this weakness is also high, as the paper explicitly states the use of a fixed mask ratio without further justification. Third, the paper does not include a dedicated discussion of the limitations of the proposed method. While the authors demonstrate the effectiveness of DMax on several benchmarks, they do not discuss the potential challenges or limitations of the method in real-world applications. For example, the paper does not analyze how the method performs on datasets with different characteristics or under different decoding conditions. The paper also does not discuss the potential impact of the method on fairness and bias. My confidence in this weakness is high, as the paper lacks a dedicated section on limitations. Fourth, the paper does not provide a direct comparison of computational cost and memory usage with other decoding strategies. While the paper shows improved accuracy and speed, it does not provide a direct comparison of computational cost and memory usage with other decoding methods. This makes it difficult to fully assess the practical trade-offs of the proposed method. My confidence in this weakness is high, as the paper lacks this comparison. Finally, while the paper evaluates the method on a reasonable number of benchmarks, it does not explicitly detail the range of sequence lengths or domains covered by the datasets used. While the paper includes benchmarks with varying complexities, it doesn't explicitly detail the range of sequence lengths or domains covered by the datasets used. This makes it difficult to assess the generalizability of the method across all possible dataset characteristics. My confidence in this weakness is medium, as the paper does evaluate on a reasonable number of benchmarks, but lacks explicit details on the range of sequence lengths and domains covered.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed analysis of the computational cost of their proposed method. This should include a breakdown of the time and memory requirements for each step of the decoding process, including the embedding interpolation and the iterative refinement. A comparison with existing decoding strategies, such as standard parallel decoding and other iterative refinement methods, would be beneficial. This analysis should also consider the impact of different parameters, such as the number of iterations and the size of the interpolation, on the computational cost. Furthermore, the authors should investigate the scalability of their method to larger models and datasets, as the computational cost may increase significantly with larger models and longer sequences. Second, the authors should provide a more detailed explanation of the hyperparameter settings used in the experiments. Specifically, they should justify the choice of the mask ratio of 0.75 with empirical evidence or theoretical arguments. A sensitivity analysis of the mask ratio, showing how the model's performance varies with different values, would be crucial. This analysis should include a discussion of the optimal mask ratio for different datasets and model architectures. Third, the authors should include a more detailed discussion of the limitations of their proposed method. This should include an analysis of the sensitivity of the method to hyperparameter settings, such as the interpolation parameter and the number of iterations. The authors should also discuss the potential challenges of applying their method to different types of diffusion models and tasks. Furthermore, the authors should discuss the potential ethical implications of their proposed method, such as its potential for misuse or its impact on fairness and bias. Fourth, the authors should include a direct comparison of computational cost and memory usage with other decoding strategies. This would provide a more comprehensive assessment of the practical trade-offs of the proposed method. Finally, the authors should include a more diverse set of benchmarks, covering a wider range of datasets with different characteristics, such as those with longer sequences, complexities, and domains. This would provide a more comprehensive evaluation of the method's performance and its generalizability across different types of text generation tasks. By addressing these points, the authors can significantly strengthen their paper and make it more impactful.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the proposed method compare to other decoding strategies in terms of computational cost and memory usage, specifically in terms of FLOPs and memory footprint? While the paper shows improved decoding speed, a direct comparison with existing methods would be beneficial. Second, what are the limitations of the proposed method, and how can they be addressed in future work? The paper does not explicitly discuss the limitations of the method, and a more detailed analysis of potential challenges and open questions would be valuable. Third, how does the proposed method perform on datasets with different characteristics, such as those with longer sequences or more complex syntactic structures? The paper evaluates the method on a reasonable number of benchmarks, but a more detailed analysis of performance across datasets with varying characteristics would be beneficial. Fourth, what is the impact of the number of iterations and the size of the interpolation on the computational cost and memory usage of the method? The paper does not provide a detailed analysis of the impact of these parameters, and a more thorough investigation would be valuable. Fifth, how does the proposed method compare to other decoding strategies in terms of robustness to noisy or corrupted inputs? The paper does not evaluate the method's performance under such conditions, and a more detailed analysis of robustness would be beneficial. Finally, what are the ethical implications of the proposed method, such as its potential for misuse or its impact on fairness and bias? The paper does not discuss these issues, and a more detailed analysis of the ethical implications would be valuable.


## Rating:

5.5


## Confidence:

3.75


## Decision:

Reject
}