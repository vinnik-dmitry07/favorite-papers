I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates the impact of the learning rate decay schedule on large language model (LLM) training. The authors challenge the conventional use of cosine learning rate schedules, which require training from scratch for each model size and dataset combination. They propose a constant learning rate with a cooldown period as an alternative, demonstrating that it achieves comparable performance to cosine schedules across various model sizes and datasets. The authors also explore the use of stochastic weight averaging (SWA) and a schedule-free optimizer (SFO) to improve model performance and reduce training costs. Their findings suggest that these methods can significantly reduce the computational resources needed for LLM training, making it more accessible and efficient.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is well-written and easy to follow, with clear explanations of the proposed methods and their benefits. The authors provide a thorough analysis of the impact of different learning rate schedules on LLM training, and their experiments are well-designed and executed. The use of SWA and SFO to improve model performance and reduce training costs is a valuable contribution to the field, as it can help make LLM training more accessible and efficient. The paper also addresses an important issue in LLM training, which is the need for more efficient and flexible training methods that can adapt to different model sizes and datasets.

### Weaknesses

#### Some Related Works


#### comment

The paper's experimental results are promising, but they are limited in scope and do not fully address the challenges of large-scale LLM training. The experiments are conducted on relatively small models and datasets, and it is unclear how the proposed methods would perform on larger models with more complex architectures. The authors should provide more evidence to support their claims, such as experiments on larger models and datasets, and comparisons with other state-of-the-art methods. Additionally, the paper does not discuss the potential limitations of the proposed methods, such as the impact of different hyperparameters on model performance. A more thorough analysis of these issues would help to strengthen the paper's claims and make it more valuable to the research community.

### Suggestions

The authors should conduct more extensive experiments on larger models and datasets to validate the generalizability of their findings. Specifically, they should explore the performance of their proposed constant learning rate with cooldown (CLR) schedule on models with billions of parameters and datasets that are representative of real-world LLM training scenarios. This would involve not only scaling up the model size but also considering the impact of different data distributions and complexities. For example, experiments could be performed on datasets with varying levels of noise, different domain shifts, and different data modalities. Furthermore, the authors should compare their method against a wider range of state-of-the-art optimizers and learning rate schedules, including those that incorporate adaptive learning rates and momentum. This would provide a more comprehensive understanding of the strengths and weaknesses of their approach relative to existing techniques. The comparison should not only focus on final performance metrics but also on training speed, memory consumption, and convergence behavior.

In addition to scaling up the experiments, the authors should also investigate the sensitivity of their method to different hyperparameters. This includes not only the learning rate and cooldown duration but also other parameters such as batch size, optimizer momentum, and weight decay. A thorough hyperparameter study would help to identify the optimal settings for different model sizes and datasets and provide practical guidance for practitioners. The authors should also explore the impact of different initialization strategies and regularization techniques on the performance of their method. This would help to ensure that the observed results are not specific to a particular initialization or regularization approach. Furthermore, the authors should provide a more detailed analysis of the computational cost of their method, including the time and memory requirements for training and inference. This would help to assess the practical feasibility of their approach for large-scale LLM training.

Finally, the authors should discuss the potential limitations of their proposed method and suggest directions for future research. This includes addressing the challenges of applying their method to very large models and datasets, as well as exploring the possibility of combining their method with other techniques such as knowledge distillation and model pruning. The authors should also discuss the potential impact of their work on the broader machine learning community and identify open problems that need to be addressed in future research. For example, they could explore the use of their method for training models in low-resource settings or for applications where rapid prototyping is important. A more thorough discussion of these issues would help to position their work within the broader context of LLM research and highlight its potential impact.

### Questions

See above.

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a new learning rate schedule for LLM training, which is a constant learning rate followed by a decay to zero. The authors show that this schedule performs comparably to cosine decay and can be used to save compute for scaling experiments.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed learning rate schedule is simple and easy to implement.
- The paper provides a comprehensive comparison of the proposed learning rate schedule with cosine decay and stochastic weight averaging (SWA).

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a strong motivation for using a constant learning rate followed by a decay to zero. The authors should provide a more detailed explanation of why this particular schedule is expected to be effective for LLM training. Specifically, it is unclear why a constant learning rate is beneficial, and why the decay to zero is necessary, rather than a more gradual decrease. The paper lacks a theoretical justification or empirical evidence to support this choice, making it difficult to assess the validity of the approach.
- The paper does not provide a detailed analysis of the impact of different decay schedules on the final model performance. The authors should explore different decay schedules and provide a comparison of their performance. It is not clear if a linear decay is the optimal choice, or if other schedules, such as exponential or step-wise decay, would lead to better results. The lack of this analysis makes it difficult to determine the robustness of the proposed method.
- The paper does not provide a detailed analysis of the impact of different learning rates on the final model performance. The authors should explore different learning rates and provide a comparison of their performance. It is not clear if the proposed method is robust to different learning rates, or if it is sensitive to the choice of learning rate. The absence of this analysis makes it difficult to assess the practical applicability of the method.

### Suggestions

The authors should provide a more thorough justification for the proposed learning rate schedule. This should include a theoretical analysis of why a constant learning rate followed by a decay to zero is expected to be effective for LLM training. For example, they could explore the connection between this schedule and the optimization landscape of LLMs, or provide empirical evidence that supports their choice. Furthermore, they should compare their approach with other learning rate schedules, such as step-wise decay or exponential decay, to demonstrate the superiority of their method. This would help to establish the novelty and effectiveness of their approach. The authors should also provide a more detailed analysis of the impact of different learning rates on the final model performance. They should explore a range of learning rates and provide a comparison of their performance. This would help to determine the robustness of the proposed method and provide practical guidance for practitioners. The authors should also investigate the impact of different decay schedules on the final model performance. They should explore different decay schedules and provide a comparison of their performance. This would help to determine the optimal decay schedule for LLM training and provide a more complete understanding of the proposed method.

To further strengthen the paper, the authors should provide a more detailed analysis of the computational cost of their method. They should compare the computational cost of their method with other learning rate schedules, such as cosine decay. This would help to determine the practical benefits of their method. The authors should also provide a more detailed analysis of the memory usage of their method. They should compare the memory usage of their method with other learning rate schedules. This would help to determine the practical feasibility of their method. The authors should also investigate the impact of their method on the generalization performance of the model. They should evaluate their method on a variety of downstream tasks and provide a comparison of their performance with other learning rate schedules. This would help to determine the effectiveness of their method for real-world applications.

Finally, the authors should provide a more detailed discussion of the limitations of their method. They should discuss the potential drawbacks of their method and provide guidance for practitioners on when to use their method and when to avoid it. This would help to provide a more balanced and comprehensive assessment of their work. The authors should also discuss the potential future directions of their research. They should discuss the potential for further improvements of their method and provide a roadmap for future research. This would help to inspire other researchers to build upon their work and contribute to the field of LLM training.

### Questions

- How does the proposed learning rate schedule compare to other learning rate schedules, such as step-wise decay or exponential decay?
- How does the proposed learning rate schedule affect the generalization performance of the model?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

The paper investigates the impact of learning rate schedules on large language model (LLM) training. The authors challenge the current use of cosine learning rate schedules, which require training from scratch for different model sizes and datasets. They propose a constant learning rate with a cooldown phase, finding that it achieves comparable performance to cosine schedules. The paper also explores the use of stochastic weight averaging (SWA) and a schedule-free optimizer (SFO) to improve model performance and reduce training costs. The authors demonstrate that these methods can significantly reduce the computational resources needed for LLM training, making it more accessible and efficient.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses a critical issue in LLM training, which is the need for more efficient and flexible training methods that can adapt to different model sizes and datasets. This is important for making LLM training more accessible and efficient.
2. The paper provides a comprehensive analysis of different learning rate schedules, including cosine, constant, and cooldown schedules. The authors also explore the use of SWA and SFO to improve model performance and reduce training costs.
3. The paper is well-written and easy to follow, with clear explanations of the proposed methods and their benefits. The authors also provide a thorough analysis of the results, including comparisons with existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a strong motivation for using a constant learning rate followed by a decay to zero. The authors should provide a more detailed explanation of why this particular schedule is expected to be effective for LLM training. Specifically, the paper lacks a theoretical justification or empirical evidence to support the claim that a constant learning rate followed by a decay is superior to other schedules, such as a gradual decay or a cyclical schedule. The absence of a clear rationale makes it difficult to assess the novelty and practical value of the proposed approach.
2. The paper does not provide a detailed analysis of the impact of different decay schedules on the final model performance. The authors should explore different decay schedules and provide a comparison of their performance. It is not clear if a linear decay is the optimal choice, or if other schedules, such as exponential or step-wise decay, would lead to better results. The lack of this analysis makes it difficult to determine the robustness of the proposed method.
3. The paper does not provide a detailed analysis of the impact of different learning rates on the final model performance. The authors should explore different learning rates and provide a comparison of their performance. It is not clear if the proposed method is robust to different learning rates, or if it is sensitive to the choice of learning rate. The absence of this analysis makes it difficult to assess the practical applicability of the method.

### Suggestions

The authors should provide a more thorough justification for the proposed constant learning rate with cooldown schedule. This should include a theoretical analysis of why this particular schedule is expected to be effective for LLM training, or at least a more extensive empirical study comparing it to other common learning rate schedules. For example, the authors could explore the loss landscape and show how the constant learning rate followed by a decay helps to navigate it. They could also investigate the effect of different decay rates and compare them to the proposed linear decay. Furthermore, the authors should provide a more detailed analysis of the impact of different learning rates on the final model performance. This should include a systematic exploration of a range of learning rates and a comparison of their performance. The authors should also investigate the sensitivity of the proposed method to the choice of learning rate and provide practical guidance for selecting an appropriate learning rate. This analysis should be done across different model sizes and datasets to ensure the robustness of the findings.

To strengthen the paper, the authors should also investigate the impact of the cooldown period on the final model performance. They should explore different cooldown durations and compare their performance. It is possible that a very short cooldown is sufficient, while a longer cooldown might lead to better performance. The authors should also investigate the interaction between the constant learning rate and the cooldown period. For example, they could explore different combinations of constant learning rate and cooldown duration and compare their performance. This analysis should be done across different model sizes and datasets to ensure the robustness of the findings. The authors should also provide a more detailed analysis of the computational cost of their method, including the time and memory requirements for training and inference. This analysis should be compared to the computational cost of other learning rate schedules, such as cosine decay. This would help to assess the practical benefits of the proposed method.

Finally, the authors should provide a more detailed discussion of the limitations of their method. They should discuss the potential drawbacks of their method and provide guidance for practitioners on when to use their method and when to avoid it. For example, they could discuss the potential for overfitting or underfitting with their proposed method. They should also discuss the potential for the method to be less effective for certain types of models or datasets. This discussion should be based on the empirical results presented in the paper and should be supported by theoretical arguments. The authors should also discuss the potential for future research in this area, such as exploring different learning rate schedules or combining their method with other optimization techniques.

### Questions

1. How does the proposed learning rate schedule compare to other learning rate schedules, such as step-wise decay or exponential decay?
2. How does the proposed learning rate schedule affect the generalization performance of the model?

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper challenges the widely used cosine learning rate schedule for large language model (LLM) training. The authors propose a constant learning rate with a cooldown period, which is simpler and more flexible than cosine decay. They demonstrate that this alternative schedule achieves comparable performance to cosine decay across different model sizes and datasets. The paper also explores the use of stochastic weight averaging (SWA) and a schedule-free optimizer (SFO) to improve model performance and reduce training costs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed alternative learning rate schedule is simple and easy to implement, and it can significantly reduce the computational cost of scaling experiments.
3. The paper provides a comprehensive analysis of the proposed method, including comparisons with cosine decay and other learning rate schedules.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a strong motivation for using a constant learning rate followed by a decay to zero. The authors should provide a more detailed explanation of why this particular schedule is expected to be effective for LLM training. Specifically, the paper lacks a theoretical justification or empirical evidence to support the claim that a constant learning rate followed by a decay is superior to other schedules, such as a gradual decay or a cyclical schedule. The absence of a clear rationale makes it difficult to assess the novelty and practical value of the proposed approach.
2. The paper does not provide a detailed analysis of the impact of different decay schedules on the final model performance. The authors should explore different decay schedules and provide a comparison of their performance. It is not clear if a linear decay is the optimal choice, or if other schedules, such as exponential or step-wise decay, would lead to better results. The lack of this analysis makes it difficult to determine the robustness of the proposed method.
3. The paper does not provide a detailed analysis of the impact of different learning rates on the final model performance. The authors should explore different learning rates and provide a comparison of their performance. It is not clear if the proposed method is robust to different learning rates, or if it is sensitive to the choice of learning rate. The absence of this analysis makes it difficult to assess the practical applicability of the method.

### Suggestions

The authors should provide a more thorough justification for the proposed constant learning rate with cooldown schedule. This should include a theoretical analysis of why this particular schedule is expected to be effective for LLM training, or at least a more extensive empirical study comparing it to other common learning rate schedules. For example, the authors could explore the loss landscape and show how the constant learning rate followed by a decay helps to navigate it. They could also investigate the effect of different decay rates and compare them to the proposed linear decay. Furthermore, the authors should provide a more detailed analysis of the impact of different learning rates on the final model performance. This should include a systematic exploration of a range of learning rates and a comparison of their performance. The authors should also investigate the sensitivity of the proposed method to the choice of learning rate and provide practical guidance for selecting an appropriate learning rate. This analysis should be done across different model sizes and datasets to ensure the robustness of the findings.

To strengthen the paper, the authors should also investigate the impact of the cooldown period on the final model performance. They should explore different cooldown durations and compare their performance. It is possible that a very short cooldown is sufficient, while a longer cooldown might lead to better performance. The authors should also investigate the interaction between the constant learning rate and the cooldown period. For example, they could explore different combinations of constant learning rate and cooldown duration and compare their performance. This analysis should be done across different model sizes and datasets to ensure the robustness of the findings. Additionally, the authors should provide a more detailed analysis of the computational cost of their method, including the time and memory requirements for training and inference. This analysis should be compared to the computational cost of other learning rate schedules, such as cosine decay. This would help to assess the practical benefits of the proposed method.

Finally, the authors should provide a more detailed discussion of the limitations of their method. They should discuss the potential drawbacks of their method and provide guidance for practitioners on when to use their method and when to avoid it. For example, they could discuss the potential for overfitting or underfitting with their proposed method. They should also discuss the potential for the method to be less effective for certain types of models or datasets. This discussion should be based on the empirical results presented in the paper and should be supported by theoretical arguments. The authors should also discuss the potential for future research in this area, such as exploring different learning rate schedules or combining their method with other optimization techniques.

### Questions

1. How does the proposed learning rate schedule compare to other learning rate schedules, such as step-wise decay or exponential decay?
2. How does the proposed learning rate schedule affect the generalization performance of the model?

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
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find the corresponding section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) from the paper to support the reviewer's claim.
4. If the weakness is about missing information, confirm that the information is indeed absent.
5. If the weakness is about a lack of justification, check if the paper provides any reasoning for the proposed method.
6. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1**

1. Weakness Statement:
"The paper does not provide a strong motivation for using a constant learning rate followed by a decay to zero. The authors should provide a more detailed explanation of why this particular schedule is expected to be effective for LLM training. Specifically, it is unclear why a constant learning rate is beneficial, and why the decay to zero is necessary, rather than a more gradual decrease. The paper lacks a theoretical justification or empirical evidence to support this choice, making it difficult to assess the validity of the approach."

2. Evidence Collection:
a) Method-related Evidence:
   - The motivation is presented in the "Motivation" section: "Despite the widespread use of cosine learning rate schedules, which require training from scratch for different model sizes and datasets, the paper aims to explore the potential of simpler and more flexible alternatives. The paper identifies a gap in the literature where a comprehensive comparison of different learning rate schedules is lacking, particularly for large-scale LLM training. The authors propose a constant learning rate with a cooldown phase, which they argue can achieve comparable performance to cosine decay without the need for extensive training runs."
   - The "Method" section describes the constant learning rate with cooldown: "The constant learning rate phase ensures that the model continues to learn effectively even after the initial training phase. The cooldown phase allows the model to stabilize and converge to a better solution, potentially avoiding premature convergence."
   - There is no theoretical justification or empirical evidence provided for why a constant learning rate followed by a decay to zero is superior to other schedules.

3. Literature Gap Analysis:
   - The paper cites works that use cosine decay (Loshchilov & Hutter, 2016; Radford et al., 2018; Reimers et al., 2022) and mentions the work of Hoffmann et al. (2022) who found that the cosine schedule with a single cycle works well for LLM training. However, it doesn't provide a theoretical comparison or empirical evidence against other constant or decaying schedules.

4. Validation Analysis:
   - The paper motivates the alternative schedule by highlighting the limitations of cosine decay (need for scratch runs) and the lack of comparison with simpler alternatives. However, it lacks a deeper explanation of *why* the proposed constant + cooldown schedule is expected to work. The "Method" section describes *how* the schedule works, but not the underlying reasons for its effectiveness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of theoretical justification or empirical comparison against other schedules in the "Motivation" and "Method" sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the impact of different decay schedules on the final model performance. The authors should explore different decay schedules and provide a comparison of their performance. It is not clear if a linear decay is the optimal choice, or if other schedules, such as exponential or step-wise decay, would lead to better results. The lack of this analysis makes it difficult to determine the robustness of the proposed method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section focuses on comparing the constant cooldown schedule with cosine decay and SWA.
   - The "Method" section introduces the "warmup-stable-decay" schedule, which is a specific type of decay, but the experiments primarily focus on a constant learning rate with a cooldown.
   - There is no experiment comparing the proposed method with other decay schedules like exponential or step-wise decay.

3. Literature Gap Analysis:
   - The paper cites works using cosine decay but doesn't benchmark against other learning rate decay strategies.

4. Validation Analysis:
   - The paper's experimental design is centered around comparing the proposed method with cosine decay. While the "Method" section mentions "warmup-stable-decay," the experiments don't systematically explore different decay schedules.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section only compares the proposed method with cosine decay and SWA, lacking comparisons with other decay schedules.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the impact of different learning rates on the final model performance. The authors should explore different learning rates and provide a comparison of their performance. It is not clear if the proposed method is robust to different learning rates, or if it is sensitive to the choice of learning rate. The absence of this analysis makes it difficult to assess the practical applicability of the method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section mentions the learning rate for the constant cooldown schedule is set to half the maximum learning rate for cosine decay (Section 3.1).
   - The paper doesn't present experiments varying the learning rate for the proposed constant cooldown schedule or comparing its performance with different learning rates.

3. Literature Gap Analysis:
   - The paper doesn't cite works that specifically analyze the sensitivity of LLM training to different learning rates in the context of alternative schedules.

4. Validation Analysis:
   - The paper focuses on comparing the proposed method with cosine decay at a specific learning rate setting. There's no exploration of how varying the learning rate affects the performance of the proposed method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section doesn't include experiments varying the learning rate for the proposed method.

**Review 2**

1. Weakness Statement:
"The paper does not provide a strong motivation for using a constant learning rate followed by a decay to zero. The authors should provide a more detailed explanation of why this particular schedule is expected to be effective for LLM training. Specifically, the paper lacks a theoretical justification or empirical evidence to support the claim that a constant learning rate followed by a decay is superior to other schedules, such as a gradual decay or a cyclical schedule. The absence of a clear rationale makes it difficult to assess the novelty and practical value of the proposed approach."

2. Evidence Collection:
   - This is the same weakness as the first point for Reviewer 1. Please see the analysis above.

3. Literature Gap Analysis:
   - Same as above.

4. Validation Analysis:
   - Same as above.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of theoretical justification or empirical comparison against other schedules in the "Motivation" and "Method" sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the impact of different decay schedules on the final model performance. The authors should explore different decay schedules and provide a comparison of their performance. It is not clear if a linear decay is the optimal choice, or if other schedules, such as exponential or step-wise decay, would lead to better results. The lack of this analysis makes it difficult to determine the robustness of the proposed method."

2. Evidence Collection:
   - This is the same weakness as the second point for Reviewer 1. Please see the analysis above.

3. Literature Gap Analysis:
   - Same as above.

4. Validation Analysis:
   - Same as above.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section only compares the proposed method with cosine decay and SWA, lacking comparisons with other decay schedules.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the impact of different learning rates on the final model performance. The authors should explore different learning rates and provide a comparison of their performance. It is not clear if the proposed method is robust to different learning rates, or if it is sensitive to the choice of learning rate. The absence of this analysis makes it difficult to assess the practical applicability of the method."

2. Evidence Collection:
   - This is the same weakness as the third point for Reviewer 1. Please see the analysis above.

3. Literature Gap Analysis:
   - Same as above.

4. Validation Analysis:
   - Same as above.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section doesn't include experiments varying the learning rate for the proposed method.

**Review 3**

1. Weakness Statement:
"The paper's experimental results are promising, but they are limited in scope and do not fully address the challenges of large-scale LLM training. The experiments are conducted on relatively small models and datasets, and it is unclear how the proposed methods would perform on larger models with more complex architectures. The authors should provide more evidence to support their claims, such as experiments on larger models and datasets, and comparisons with other state-of-the-art methods."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section mentions using SlimPajama (6B tokens) for the 210M parameter model and OpenWebText2 for the 8B parameter model.
   - The paper doesn't present experiments on models significantly larger than 8B parameters or datasets that are considered state-of-the-art for LLM training.

3. Literature Gap Analysis:
   - The paper compares against cosine decay and SWA, but not against a comprehensive set of state-of-the-art methods for large-scale LLM training.

4. Validation Analysis:
   - While the paper includes experiments on a 210M parameter model, the reviewer correctly points out that the experiments are not on the largest models currently used for LLM training. The comparison is also limited to cosine decay and SWA.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The experiments are conducted on models up to 8B parameters, which is not the largest scale for current LLMs. The comparison is limited to cosine decay and SWA.

1. Weakness Statement:
"Additionally, the paper does not discuss the potential limitations of the proposed methods, such as the impact of different hyperparameters on model performance. A more thorough analysis of these issues would help to strengthen the paper's claims and make it more valuable to the research community."

2. Evidence Collection:
   - The "Limitations" section briefly mentions the experiments are limited to a fraction of the compute used in the original cosine learning rate paper and provides some analysis of the impact of batch size and learning rate.
   - However, a more detailed discussion of the limitations and the impact of other hyperparameters is missing.

3. Literature Gap Analysis:
   -  A thorough discussion of limitations and hyperparameter sensitivity is common in machine learning papers.

4. Validation Analysis:
   - The paper acknowledges some limitations, but a more in-depth discussion of the potential drawbacks and the sensitivity to hyperparameters is lacking.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Limitations" section is brief and doesn't cover a comprehensive analysis of hyperparameter impact.

**Review 4**

1. Weakness Statement:
"The paper does not provide a strong motivation for using a constant learning rate followed by a decay to zero. The authors should provide a more detailed explanation of why this particular schedule is expected to be effective for LLM training. Specifically, the paper lacks a theoretical justification or empirical evidence to support the claim that a constant learning rate followed by a decay is superior to other schedules, such as a gradual decay or a cyclical schedule. The absence of a clear rationale makes it difficult to assess the novelty and practical value of the proposed approach."

2. Evidence Collection:
   - This is the same weakness as the first point for Reviewer 1 and Reviewer 2. Please see the analysis above.

3. Literature Gap Analysis:
   - Same as above.

4. Validation Analysis:
   - Same as above.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of theoretical justification or empirical comparison against other schedules in the "Motivation" and "Method" sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the impact of different decay schedules on the final model performance. The authors should explore different decay schedules and provide a comparison of their performance. It is not clear if a linear decay is the optimal choice, or if other schedules, such as exponential or step-wise decay, would lead to better results. The lack of this analysis makes it difficult to determine the robustness of the proposed method."

2. Evidence Collection:
   - This is the same weakness as the second point for Reviewer 1 and Reviewer 2. Please see the analysis above.

3. Literature Gap Analysis:
   - Same as above.

4. Validation Analysis:
   - Same as above.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section only compares the proposed method with cosine decay and SWA, lacking comparisons with other decay schedules.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the impact of different learning rates on the final model performance. The authors should explore different learning rates and provide a comparison of their performance. It is not clear if the proposed method is robust to different learning rates, or if it is sensitive to the choice of learning rate. The absence of this analysis makes it difficult to assess the practical applicability of the method."

2. Evidence Collection:
   - This is the same weakness as the third point for Reviewer 1 and Reviewer 2. Please see the analysis above.

3. Literature Gap Analysis:
   - Same as above.

4. Validation Analysis:
   - Same as above.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section doesn't include experiments varying the learning rate for the proposed method.

1. Weakness Statement:
"How does the proposed learning rate schedule compare to other learning rate schedules, such as step-wise decay or exponential decay?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section compares the proposed method with cosine decay and SWA.
   - There are no experiments comparing the proposed method with step-wise or exponential decay schedules.

3. Literature Gap Analysis:
   - The paper cites works using cosine decay but doesn't benchmark against other learning rate decay strategies in the experimental section.

4. Validation Analysis:
   - The experimental design doesn't include a comparison with step-wise or exponential decay schedules.

5. Conclusion:
   - Validity status: Valid (as a question highlighting a missing experiment)
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section lacks comparisons with step-wise and exponential decay schedules.

1. Weakness Statement:
"How does the proposed learning rate schedule affect the generalization performance of the model?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section evaluates performance using validation loss and downstream benchmarks (MMLU, Winogrande, ARC).
   - The results show comparable performance to cosine decay on these metrics.

3. Literature Gap Analysis:
   - The paper uses standard evaluation metrics for LLMs.

4. Validation Analysis:
   - The paper *does* evaluate generalization performance using standard benchmarks. The reviewer's question is more about whether the paper *thoroughly* analyzes this, which leads to the next point.

5. Conclusion:
   - Validity status: Partially Valid (as a question highlighting a potential area for more in-depth analysis)
   - Confidence level: Medium
   - Key supporting evidence: The paper includes generalization metrics, but the depth of analysis could be greater.

**Synthesis and Reflection:**

Several reviewers independently identified similar weaknesses, primarily concerning the lack of strong motivation and justification for the proposed constant cooldown schedule, the absence of a detailed analysis of different decay schedules, and the limited exploration of the impact of varying learning rates. These criticisms are consistently supported by the paper's content, specifically in the "Motivation," "Method," and "Experiments" sections.

There is a consensus that while the paper demonstrates promising results, the underlying reasons for the effectiveness of the proposed method and its robustness across different scenarios are not thoroughly explored. The lack of comparison with other learning rate schedules beyond cosine decay is a recurring concern.

The reviewers also point out that the experimental scope is limited, primarily focusing on smaller models and a specific set of comparisons. This limits the generalizability of the findings to larger, state-of-the-art LLMs.

The question about generalization performance is slightly different from the other two. While the paper *does* include generalization metrics, the reviewers suggest a more in-depth analysis of how the proposed method affects generalization compared to other schedules.

Overall, the reviewers raise valid concerns about the depth of justification and analysis for the proposed method, the limited scope of the experiments, and the need for a more comprehensive comparison with existing techniques.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel approach to training large language models (LLMs) by proposing a constant learning rate with a cooldown phase as an alternative to the widely used cosine learning rate schedule. The authors challenge the conventional wisdom of needing to train models from scratch for each new model size or dataset, arguing that their method can achieve comparable performance with less computational overhead. The core idea is to maintain a constant learning rate throughout the initial training phase and then gradually decay it to zero, allowing the model to stabilize before entering the cooldown period. This approach, they claim, simplifies the training process and reduces the computational resources needed for scaling experiments. The authors also explore the use of stochastic weight averaging (SWA) and a schedule-free optimizer (SFO) to further improve model performance and reduce training costs. The empirical findings suggest that the proposed constant learning rate with cooldown schedule performs comparably to cosine decay across various model sizes and datasets, demonstrating the potential for significant computational savings. The paper's significance lies in its attempt to simplify and accelerate the training of LLMs, which is a critical challenge in the field. By proposing a more flexible learning rate schedule, the authors aim to make LLM training more accessible and efficient, potentially enabling researchers to explore a wider range of model sizes and datasets with limited computational resources. The paper also contributes to the understanding of learning rate schedules for LLMs, highlighting the importance of exploring alternatives to the traditional cosine decay approach. The authors' work could have a substantial impact on the research community by providing a more efficient and flexible training method, potentially accelerating the development of more powerful and versatile LLMs. However, the paper's limitations, particularly in the justification of the proposed method and the scope of the experiments, need to be addressed to fully realize its potential.


## Soundness:

2.75


## Presentation:

2.75


## Contribution:

2.25


## Strengths:

I found several aspects of this paper to be commendable. Firstly, the paper is well-written and easy to follow, which makes it accessible to a broad audience. The authors clearly articulate their motivation and the proposed method, allowing for a straightforward understanding of their approach. The introduction of a constant learning rate with a cooldown phase is a simple yet potentially effective method for training LLMs, and the paper provides a clear explanation of how this schedule works. The authors also demonstrate that this alternative schedule achieves comparable performance to cosine decay across various model sizes and datasets, which is a significant finding. The exploration of stochastic weight averaging (SWA) and a schedule-free optimizer (SFO) to improve model performance and reduce training costs is another strength of the paper. These techniques are well-integrated into the proposed method, and the authors show that they can further enhance the performance of the model. The paper also addresses an important issue in LLM training, which is the need for more efficient and flexible training methods. The authors' focus on reducing the computational resources needed for scaling experiments is particularly relevant, as it could potentially make LLM training more accessible to a wider range of researchers. The empirical results presented in the paper are promising, and the authors provide a comprehensive analysis of the proposed method, including comparisons with existing techniques. The paper's contribution to the understanding of learning rate schedules for LLMs is also noteworthy, as it highlights the importance of exploring alternatives to the traditional cosine decay approach. Overall, the paper presents a well-motivated and technically sound approach to LLM training, with the potential to significantly impact the field.


## Weaknesses:

Despite the strengths of this paper, I have identified several significant weaknesses that need to be addressed. The most prominent issue is the lack of a strong motivation and justification for the proposed constant learning rate with cooldown schedule. While the authors demonstrate that this schedule performs comparably to cosine decay, they fail to provide a theoretical explanation or empirical evidence to support the claim that it is superior to other schedules, such as a gradual decay or a cyclical schedule. The paper lacks a clear rationale for why a constant learning rate followed by a decay to zero is expected to be effective for LLM training. This absence of a strong theoretical foundation makes it difficult to assess the novelty and practical value of the proposed approach. The authors do not provide a detailed analysis of the loss landscape and how the constant learning rate followed by a decay helps to navigate it, nor do they explore the effect of different decay rates. This lack of justification is a major limitation, as it leaves the reader wondering why this particular schedule is expected to work and whether it is indeed the best choice. Furthermore, the paper does not provide a detailed analysis of the impact of different decay schedules on the final model performance. The authors primarily compare their method with cosine decay and stochastic weight averaging (SWA), but they do not explore other common learning rate decay strategies, such as exponential or step-wise decay. This limited comparison makes it difficult to determine the robustness of the proposed method and whether it is optimal for LLM training. The paper also lacks a detailed analysis of the impact of different learning rates on the final model performance. The authors set the constant learning rate to half the maximum learning rate for cosine decay, but they do not explore different learning rates for their proposed method. This lack of exploration makes it difficult to assess the practical applicability of the method, as it is unclear if the proposed method is robust to different learning rates or if it is sensitive to the choice of learning rate. The absence of this analysis makes it difficult to determine the optimal learning rate for the proposed method and how it compares to other schedules. The experimental results, while promising, are limited in scope and do not fully address the challenges of large-scale LLM training. The experiments are conducted on relatively small models and datasets, with the largest model being 8B parameters. It is unclear how the proposed methods would perform on larger models with more complex architectures. The authors do not provide evidence to support their claims, such as experiments on larger models and datasets, and comparisons with other state-of-the-art methods. This limitation makes it difficult to assess the generalizability of the proposed method to real-world LLM training scenarios. The paper also lacks a thorough discussion of the potential limitations of the proposed methods. While the authors briefly mention the experiments are limited to a fraction of the compute used in the original cosine learning rate paper, they do not provide a detailed analysis of the impact of different hyperparameters on model performance. The paper does not discuss the potential drawbacks of the proposed method or the sensitivity of the method to the choice of hyperparameters. This lack of discussion makes it difficult to assess the practical implications of the proposed method and its potential for real-world applications. Finally, the paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors claim that their method can significantly reduce the computational resources needed for LLM training, they do not provide a detailed comparison of the computational cost of their method with other learning rate schedules. This lack of analysis makes it difficult to assess the practical benefits of the proposed method for large-scale LLM training. In summary, the paper's weaknesses stem from a lack of strong justification for the proposed method, a limited experimental scope, and a lack of detailed analysis of the impact of different hyperparameters and learning rates. These limitations significantly impact the paper's conclusions and need to be addressed to fully realize the potential of the proposed method.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. Firstly, the authors should provide a more thorough justification for the proposed constant learning rate with cooldown schedule. This should include a theoretical analysis of why this particular schedule is expected to be effective for LLM training, or at least a more extensive empirical study comparing it to other common learning rate schedules. For example, the authors could explore the loss landscape and show how the constant learning rate followed by a decay helps to navigate it. They could also investigate the effect of different decay rates and compare them to the proposed linear decay. This would help to establish the novelty and practical value of the proposed approach. Secondly, the authors should conduct a more detailed analysis of the impact of different decay schedules on the final model performance. They should explore different decay schedules, such as exponential or step-wise decay, and provide a comparison of their performance. This would help to determine the robustness of the proposed method and whether it is optimal for LLM training. The authors should also investigate the interaction between the constant learning rate and the cooldown period. For example, they could explore different cooldown durations and compare their performance. It is possible that a very short cooldown is sufficient, while a longer cooldown might lead to better performance. The authors should also investigate the impact of the interaction between the constant learning rate and the cooldown period. For example, they could explore different combinations of constant learning rate and cooldown duration and compare their performance. This analysis should be done across different model sizes and datasets to ensure the robustness of the findings. Thirdly, the authors should provide a more detailed analysis of the impact of different learning rates on the final model performance. They should explore different learning rates and provide a comparison of their performance. This would help to determine the robustness of the proposed method and whether it is sensitive to the choice of learning rate. The authors should also investigate the sensitivity of the proposed method to the choice of learning rate and provide practical guidance for selecting an appropriate learning rate. This analysis should be done across different model sizes and datasets to ensure the robustness of the findings. Fourthly, the authors should conduct more extensive experiments on larger models and datasets to validate the generalizability of their findings. Specifically, they should explore the performance of their proposed constant learning rate with cooldown (CLR) schedule on models with billions of parameters and datasets that are representative of real-world LLM training scenarios. This would involve not only scaling up the model size but also considering the impact of different data distributions and complexities. For example, experiments could be performed on datasets with varying levels of noise, different domain shifts, and different data modalities. Furthermore, the authors should compare their method against a wider range of state-of-the-art optimizers and learning rate schedules, including those that incorporate adaptive learning rates and momentum. This would provide a more comprehensive understanding of the strengths and weaknesses of their approach relative to existing techniques. The comparison should not only focus on final performance metrics but also on training speed, memory consumption, and convergence behavior. Fifthly, the authors should provide a more detailed analysis of the computational cost of their method, including the time and memory requirements for training and inference. This would help to assess the practical benefits of their method for large-scale LLM training. The authors should also provide a more detailed discussion of the limitations of their method. They should discuss the potential drawbacks of their method and provide guidance for practitioners on when to use their method and when to avoid it. For example, they could discuss the potential for overfitting or underfitting with their proposed method. They should also discuss the potential for the method to be less effective for certain types of models or datasets. This discussion should be based on the empirical results presented in the paper and should be supported by theoretical arguments. Finally, the authors should provide a more detailed analysis of the impact of their method on the generalization performance of the model. They should evaluate their method on a variety of downstream tasks and provide a comparison of their performance with other learning rate schedules. This would help to determine the effectiveness of their method for real-world applications. By addressing these suggestions, the authors can significantly strengthen their paper and make a more substantial contribution to the field of LLM training.


## Questions:

I have several questions that arise from my analysis of this paper. Firstly, how does the proposed learning rate schedule compare to other learning rate schedules, such as step-wise decay or exponential decay? The paper primarily compares the proposed method with cosine decay and SWA, but it does not explore other common learning rate decay strategies. A more detailed comparison would help to determine the robustness of the proposed method and whether it is optimal for LLM training. Secondly, how does the proposed learning rate schedule affect the generalization performance of the model? While the paper includes generalization metrics, a more in-depth analysis of how the proposed method affects generalization compared to other schedules would be beneficial. This would help to determine the practical applicability of the method for real-world applications. Thirdly, what is the optimal learning rate for the proposed constant cooldown schedule, and how does it compare to the optimal learning rate for cosine decay? The paper sets the constant learning rate to half the maximum learning rate for cosine decay, but it does not explore different learning rates for its proposed method. A more detailed analysis of the impact of different learning rates would help to determine the robustness of the proposed method and its practical applicability. Fourthly, what is the impact of different decay rates on the final model performance? The paper uses a linear decay, but it does not explore other decay schedules. A more detailed analysis of the impact of different decay rates would help to determine the robustness of the proposed method and whether it is optimal for LLM training. Fifthly, how does the proposed method scale to larger models and datasets? The experiments are conducted on relatively small models and datasets, with the largest model being 8B parameters. It is unclear how the proposed methods would perform on larger models with more complex architectures. A more detailed analysis of the scalability of the proposed method would help to determine its practical applicability for real-world LLM training scenarios. Finally, what are the potential limitations of the proposed method, and what are the potential drawbacks of using this method? The paper briefly mentions the experiments are limited to a fraction of the compute used in the original cosine learning rate paper, but it does not provide a detailed analysis of the potential drawbacks of the proposed method or the sensitivity of the method to the choice of hyperparameters. A more detailed discussion of the limitations of the method would help to guide practitioners on when to use the method and when to avoid it. These questions target core methodological choices and seek clarification of critical assumptions, aiming to provide a more comprehensive understanding of the proposed method and its implications.


## Rating:

4.75


## Confidence:

3.25


## Decision:

Reject
}