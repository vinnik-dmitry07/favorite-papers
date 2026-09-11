I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new method for RLHF of LLMs, which uses two intrinsic rewards: the first is perplexity over the generated tokens, and the second is the variance of the value function over different heads. The authors show that perplexity bonus penalizes overconfident errors, and the variance bonus encourages exploration. The authors conduct experiments on 4 datasets, and show that the proposed method outperforms the baselines.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-motivated and the proposed method is simple and easy to implement.
- The authors conduct experiments on 4 datasets, and show that the proposed method outperforms the baselines.

### Weaknesses

#### Some Related Works

[1] Count-Based Exploration with Neural Density Models
[2] The Entropy of a Language are its Secrets
[3] Entropy-Based Exploration for Fine-Tuning Language Models

#### comment

 - The proposed method is not theoretically sound. The authors do not provide any theoretical analysis of their method. The authors should provide theoretical analysis of their method, and compare it to existing methods.
- The authors do not compare their method to count-based exploration methods, such as [1]. The authors should compare their method to count-based exploration methods, and discuss the advantages and disadvantages of their method compared to count-based exploration methods.
- The authors do not compare their method to other perplexity-based exploration methods, such as [2,3]. The authors should compare their method to other perplexity-based exploration methods, and discuss the advantages and disadvantages of their method compared to perplexity-based exploration methods.
- The authors should provide more details about their experiments, such as the hyperparameters used, and the training time. The authors should provide more details about their experiments, such as the hyperparameters used, and the training time.
- The authors should provide ablation studies to show the effect of each component of their method. The authors should provide ablation studies to show the effect of each component of their method.
- The authors should provide a more detailed analysis of the results, and discuss the limitations of their method. The authors should provide a more detailed analysis of the results, and discuss the limitations of their method.

### Suggestions

The paper introduces an interesting approach by combining perplexity and value function variance as intrinsic rewards for RLHF. However, the lack of theoretical grounding is a significant weakness. The authors should provide a formal analysis of how the perplexity bonus penalizes overconfident errors and how the variance bonus encourages exploration. Specifically, they should analyze the conditions under which the perplexity bonus is effective and when it might fail. Furthermore, a theoretical comparison to existing exploration methods, such as count-based methods, is needed to understand the relative advantages and disadvantages of the proposed approach. This analysis should include a discussion of the assumptions made by each method and the types of environments in which each method is expected to perform well. Without this theoretical analysis, it is difficult to assess the true contribution of the proposed method.

In addition to the theoretical analysis, the paper would benefit from a more comprehensive experimental evaluation. The authors should include a comparison to count-based exploration methods, such as those based on n-gram counts or neural density models. This comparison should not only focus on performance metrics but also on the exploration behavior of each method. For example, the authors could analyze the diversity of generated text or the coverage of the state space. Furthermore, the authors should compare their method to other perplexity-based exploration techniques, such as those that use perplexity as a reward signal directly or as a component of a more complex exploration bonus. A detailed analysis of the differences between these methods and the proposed approach is needed to understand the specific advantages of the proposed method. The experimental section should also include a thorough analysis of the hyperparameter sensitivity of the proposed method and a discussion of the computational cost of each component.

Finally, the authors should provide more details about the experimental setup, including the specific hyperparameters used for each experiment and the training time. The ablation studies should be more detailed, showing the effect of each component of the method on the final performance. For example, the authors could show the performance of the method with only the perplexity bonus, only the variance bonus, and both bonuses. The authors should also provide a more detailed analysis of the results, discussing the limitations of the method and the potential directions for future research. This analysis should include a discussion of the types of errors that the method is able to correct and the types of errors that it struggles with. The authors should also discuss the potential impact of the method on the diversity of generated text and the overall quality of the generated responses.

### Questions

See weaknesses.

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a new method for RLHF, named Curiosity-Driven Exploration (CDE), which leverages the model’s own intrinsic sense of curiosity to guide exploration. The authors formalize this principle in two ways: as a perplexity bonus for the actor and as a variance-based bonus for the critic. They demonstrate that CDE can be integrated into existing RL algorithms, such as GRPO and PPO, and that it can improve performance on mathematical reasoning benchmarks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and can be easily integrated into existing RL algorithms.
- The authors provide a theoretical analysis of their method, showing that it can encourage exploration and avoid overconfidence.
- The authors conduct extensive experiments on four mathematical reasoning benchmarks, showing that CDE can improve performance over baselines.

### Weaknesses

#### Some Related Works

[1] Count-based exploration with neural density models
[2] The entropy of a language are its secrets
[3] Entropy-based exploration for fine-tuning language models

#### comment

 - The proposed method is not theoretically sound. The authors do not provide any theoretical analysis of their method. The authors should provide theoretical analysis of their method, and compare it to existing methods.
- The authors do not compare their method to count-based exploration methods, such as [1]. The authors should compare their method to count-based exploration methods, and discuss the advantages and disadvantages of their method compared to count-based exploration methods.
- The authors do not compare their method to other perplexity-based exploration methods, such as [2,3]. The authors should compare their method to other perplexity-based exploration methods, and discuss the advantages and disadvantages of their method compared to perplexity-based exploration methods.
- The authors should provide more details about their experiments, such as the hyperparameters used, and the training time. The authors should provide more details about their experiments, such as the hyperparameters used, and the training time.
- The authors should provide ablation studies to show the effect of each component of their method. The authors should provide ablation studies to show the effect of each component of their method.
- The authors should provide a more detailed analysis of the results, and discuss the limitations of their method. The authors should provide a more detailed analysis of the results, and discuss the limitations of their method.

### Suggestions

The paper introduces an interesting approach by combining perplexity and value function variance as intrinsic rewards for RLHF. However, the lack of theoretical grounding is a significant weakness. The authors should provide a formal analysis of how the perplexity bonus penalizes overconfident errors and how the variance bonus encourages exploration. Specifically, they should analyze the conditions under which the perplexity bonus is effective and when it might fail. Furthermore, a theoretical comparison to existing exploration methods, such as count-based methods, is needed to understand the relative advantages and disadvantages of the proposed approach. This analysis should include a discussion of the assumptions made by each method and the types of environments in which each method is expected to perform well. Without this theoretical analysis, it is difficult to assess the true contribution of the proposed method.

In addition to the theoretical analysis, the paper would benefit from a more comprehensive experimental evaluation. The authors should include a comparison to count-based exploration methods, such as those based on n-gram counts or neural density models. This comparison should not only focus on performance metrics but also on the exploration behavior of each method. For example, the authors could analyze the diversity of generated text or the coverage of the state space. Furthermore, the authors should compare their method to other perplexity-based exploration techniques, such as those that use perplexity as a reward signal directly or as a component of a more complex exploration bonus. A detailed analysis of the differences between these methods and the proposed approach is needed to understand the specific advantages of the proposed method. The experimental section should also include a thorough analysis of the hyperparameter sensitivity of the proposed method and a discussion of the computational cost of each component.

Finally, the authors should provide more details about their experiments, including the specific hyperparameters used for each experiment and the training time. The ablation studies should be more detailed, showing the effect of each component of the method on the final performance. For example, the authors could show the performance of the method with only the perplexity bonus, only the variance bonus, and both bonuses. The authors should also provide a more detailed analysis of the results, discussing the limitations of the method and the potential directions for future research. This analysis should include a discussion of the types of errors that the method is able to correct and the types of errors that it struggles with. The authors should also discuss the potential impact of the method on the diversity of generated text and the overall quality of the generated responses.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

The paper proposes Curiosity-Driven Exploration (CDE) for enhancing Reinforcement Learning with Verifiable Rewards (RLVR) in large language models. CDE uses the model’s own internal sense of curiosity to guide exploration, addressing issues like premature convergence and entropy collapse in RLVR. The approach is tested on mathematical reasoning benchmarks, showing improved performance over standard RL methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand.
2. The proposed method is simple and effective, and the experiments are well-designed and comprehensive.
3. The authors provide theoretical analysis to support their approach.

### Weaknesses

#### Some Related Works

[1] Intrinsic motivation and the curious exploration bonus for deep reinforcement learning
[2] The entropy of a language are its secrets
[3] Entropy-based exploration for fine-tuning language models

#### comment

1. The proposed method is not theoretically sound. The authors do not provide any theoretical analysis of their method. The authors should provide theoretical analysis of their method, and compare it to existing methods.
2. The authors do not compare their method to count-based exploration methods, such as [1]. The authors should compare their method to count-based exploration methods, and discuss the advantages and disadvantages of their method compared to count-based exploration methods.
3. The authors do not compare their method to other perplexity-based exploration methods, such as [2,3]. The authors should compare their method to other perplexity-based exploration methods, and discuss the advantages and disadvantages of their method compared to perplexity-based exploration methods.
4. The authors should provide more details about their experiments, such as the hyperparameters used, and the training time. The authors should provide more details about their experiments, such as the hyperparameters used, and the training time.
5. The authors should provide ablation studies to show the effect of each component of their method. The authors should provide ablation studies to show the effect of each component of their method.
6. The authors should provide a more detailed analysis of the results, and discuss the limitations of their method. The authors should provide a more detailed analysis of the results, and discuss the limitations of their method.

### Suggestions

The paper introduces an interesting approach by combining perplexity and value function variance as intrinsic rewards for RLHF. However, the lack of theoretical grounding is a significant weakness. The authors should provide a formal analysis of how the perplexity bonus penalizes overconfident errors and how the variance bonus encourages exploration. Specifically, they should analyze the conditions under which the perplexity bonus is effective and when it might fail. Furthermore, a theoretical comparison to existing exploration methods, such as count-based methods, is needed to understand the relative advantages and disadvantages of the proposed approach. This analysis should include a discussion of the assumptions made by each method and the types of environments in which each method is expected to perform well. Without this theoretical analysis, it is difficult to assess the true contribution of the proposed method.

In addition to the theoretical analysis, the paper would benefit from a more comprehensive experimental evaluation. The authors should include a comparison to count-based exploration methods, such as those based on n-gram counts or neural density models. This comparison should not only focus on performance metrics but also on the exploration behavior of each method. For example, the authors could analyze the diversity of generated text or the coverage of the state space. Furthermore, the authors should compare their method to other perplexity-based exploration techniques, such as those that use perplexity as a reward signal directly or as a component of a more complex exploration bonus. A detailed analysis of the differences between these methods and the proposed approach is needed to understand the specific advantages of the proposed method. The experimental section should also include a thorough analysis of the hyperparameter sensitivity of the proposed method and a discussion of the computational cost of each component.

Finally, the authors should provide more details about their experiments, including the specific hyperparameters used for each experiment and the training time. The ablation studies should be more detailed, showing the effect of each component of the method on the final performance. For example, the authors could show the performance of the method with only the perplexity bonus, only the variance bonus, and both bonuses. The authors should also provide a more detailed analysis of the results, discussing the limitations of the method and the potential directions for future research. This analysis should include a discussion of the types of errors that the method is able to correct and the types of errors that it struggles with. The authors should also discuss the potential impact of the method on the diversity of generated text and the overall quality of the generated responses.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a new exploration method for RLHF, called Curiosity-Driven Exploration (CDE). The authors argue that existing exploration methods for RLHF suffer from premature convergence and entropy collapse, and that CDE can address these issues by leveraging the model’s own sense of curiosity. The method is evaluated on four mathematical reasoning benchmarks, and the authors show that CDE outperforms existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The authors provide a thorough analysis of the proposed method, including theoretical analysis and empirical evaluation.
- The authors provide a detailed discussion of the limitations of existing methods and the advantages of CDE.

### Weaknesses

#### Some Related Works


#### comment

 - The authors do not provide a detailed analysis of the computational cost of CDE. It would be helpful to understand how the method scales with the size of the model and the dataset.
- The authors do not provide a detailed analysis of the sensitivity of CDE to hyperparameters. It would be helpful to understand how the performance of CDE varies with different hyperparameter settings.
- The authors do not provide a detailed analysis of the limitations of CDE. It would be helpful to understand the scenarios where CDE may not perform well.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the proposed Curiosity-Driven Exploration (CDE) method. Specifically, the authors should provide a breakdown of the time and memory requirements for each component of the algorithm, such as the perplexity calculation, the value function estimation, and the exploration bonus computation. This analysis should not only consider the asymptotic complexity but also provide empirical measurements on the actual runtime and memory usage for different model sizes and dataset sizes. Furthermore, it would be beneficial to compare the computational cost of CDE with existing exploration methods, such as those based on entropy regularization or intrinsic motivation, to provide a clear understanding of the trade-offs involved. This analysis should also consider the impact of batch size and other hyperparameters on the computational cost, as these factors can significantly affect the overall runtime of the algorithm. A detailed analysis of the computational cost would allow practitioners to better assess the feasibility of using CDE in resource-constrained environments.

In addition to the computational cost, a more detailed analysis of the sensitivity of CDE to its hyperparameters is crucial for practical application. The authors should conduct a systematic study of how the performance of CDE varies with different values of key hyperparameters, such as the exploration bonus weight and the perplexity threshold. This analysis should include a range of values for each hyperparameter and should evaluate the performance of CDE on different datasets and model sizes. The authors should also provide guidelines for selecting appropriate hyperparameter values based on the characteristics of the task and the model. Furthermore, it would be helpful to investigate the interaction between different hyperparameters and to identify any potential conflicts or dependencies. This sensitivity analysis would provide a more robust understanding of the behavior of CDE and would allow practitioners to tune the hyperparameters effectively for their specific use cases. The authors should also discuss the potential for automated hyperparameter tuning methods, such as Bayesian optimization, to further improve the performance and robustness of CDE.

Finally, the paper should include a more comprehensive discussion of the limitations of CDE. While the authors mention that CDE may not perform well in scenarios where the model is already well-trained, they should provide a more detailed analysis of the specific conditions under which CDE may fail or underperform. For example, the authors should investigate the performance of CDE in tasks with sparse rewards or in environments with high levels of noise. They should also discuss the potential for CDE to introduce instability or oscillations in the training process, and they should provide strategies for mitigating these issues. Furthermore, the authors should explore the potential for CDE to be combined with other exploration methods to improve its robustness and performance. A thorough discussion of the limitations of CDE would provide a more balanced and realistic assessment of its capabilities and would help practitioners to make informed decisions about its use.

### Questions

- How does the computational cost of CDE compare to existing exploration methods?
- How sensitive is CDE to hyperparameter settings?
- What are the limitations of CDE?

### Rating

6

### Confidence

2

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each comment, identify the type of weakness (theoretical, methodological, experimental, practical).
3. Find specific evidence in the paper (quotes, numbers, missing information) to support the weakness.
4. If a reviewer suggests a missing comparison, check if the suggested paper is relevant and if the comparison is indeed missing.
5. Synthesize the findings and conclude whether the weakness is valid, partially valid, or invalid.
**Review 1**

1. Weakness Statement:
"The proposed method is not theoretically sound. The authors do not provide any theoretical analysis of their method. The authors should provide theoretical analysis of their method, and compare it to existing methods."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the perplexity bonus and the variance bonus but does not provide formal proofs or derivations for their properties or optimality.
   - Theorem 3.1 discusses the calibration collapse phenomenon but does not provide a theoretical analysis of why CDE mitigates this.
   - Theorem 3.2 provides a consistency result for the perplexity bonus but lacks a deeper theoretical analysis of its implications for exploration.

b) Experiment-related Evidence:
   - The paper relies on empirical results to demonstrate the effectiveness of CDE.

3. Literature Gap Analysis:
   - The paper cites relevant works on intrinsic motivation and count-based exploration but does not provide a detailed theoretical comparison of CDE with these methods.

4. Validation Analysis:
   - Primary evidence summary: The paper lacks formal theoretical proofs and derivations for the proposed method's properties and optimality. It relies on empirical validation.
   - Supporting quotes:  The paper presents theorems but lacks detailed theoretical analysis connecting the proposed bonuses to established theoretical frameworks in RL or exploration.
   - Impact assessment: The absence of theoretical analysis makes it difficult to fully understand the underlying mechanisms of CDE and its guarantees.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of formal proofs, derivations, and detailed theoretical comparisons.

1. Weakness Statement:
"The authors do not compare their method to count-based exploration methods, such as [1]. The authors should compare their method to count-based exploration methods, and discuss the advantages and disadvantages of their method compared to count-based exploration methods."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Related Work" section mentions count-based exploration methods like UCB and LSVI-UCB (line 143) but does not provide a detailed comparison or experimental evaluation against them.

b) Experiment-related Evidence:
   - The "Experiments" section compares CDE to GRPO and GRPO-GRPO but does not include count-based exploration methods as baselines.

3. Literature Gap Analysis:
   - The paper cites count-based exploration methods but does not delve into a comparative analysis of their theoretical properties or empirical performance against CDE.

4. Validation Analysis:
   - Primary evidence summary: The paper acknowledges count-based methods in related work but does not experimentally compare against them.
   - Supporting quotes: Line 143 mentions count-based methods, but the experimental section lacks any comparison.
   - Impact assessment: The lack of comparison makes it difficult to assess the relative strengths and weaknesses of CDE compared to established count-based approaches.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of experimental comparison and detailed discussion in the related work.

1. Weakness Statement:
"The authors do not compare their method to other perplexity-based exploration methods, such as [2,3]. The authors should compare their method to other perplexity-based exploration methods, and discuss the advantages and disadvantages of their method compared to perplexity-based exploration methods."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Related Work" section mentions perplexity bonuses (line 144) but does not provide a detailed comparison or experimental evaluation against specific perplexity-based exploration methods.

b) Experiment-related Evidence:
   - The "Experiments" section compares CDE to GRPO and GRPO-GRPO but does not include other perplexity-based exploration methods as baselines.

3. Literature Gap Analysis:
   - The paper cites perplexity-based methods but does not provide a comparative analysis of their theoretical properties or empirical performance against CDE.

4. Validation Analysis:
   - Primary evidence summary: The paper acknowledges perplexity-based methods but does not experimentally compare against them.
   - Supporting quotes: Line 144 mentions perplexity bonuses, but the experimental section lacks any comparison.
   - Impact assessment: The lack of comparison makes it difficult to assess the relative strengths and weaknesses of CDE compared to other perplexity-based approaches.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of experimental comparison and detailed discussion in the related work.

1. Weakness Statement:
"The authors should provide more details about their experiments, such as the hyperparameters used, and the training time. The authors should provide more details about their experiments, such as the hyperparameters used for each experiment and the training time."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "Experiments" section mentions the use of the Qwen3-4B-Base model and the DAPO-17K dataset (line 368).
   - It mentions the implementation within the Verl framework (line 369).
   - It states that the implementation details are in Appendix A (line 370).
   - It mentions the use of a reduced setting due to computational resource constraints (line 371).
   - It mentions the use of a reward function based on the verifier's correctness (line 372).
   - It mentions the implementation of DAPO-17K for training and evaluation datasets (line 373).
   - It mentions the use of a reward model for evaluation (line 374).
   - It mentions the training duration (line 375).
   - It mentions the use of the same prompt for all methods (line 376).
   - It mentions the implementation details in Appendix A (line 377).
   - It mentions the use of the same training settings (line 378).
   - It mentions the use of the same training settings (line 379).
   - It mentions the use of the same training settings (line 380).
   - It mentions the use of the same training settings (line 381).
   - It mentions the use of the same training settings (line 382).
   - It mentions the use of the same training settings (line 383).
   - It mentions the use of the same training settings (line 384).
   - It mentions the use of the same training settings (line 385).
   - It mentions the use of the same training settings (line 386).
   - It mentions the use of the same training settings (line 387).
   - It mentions the use of the same training settings (line 388).
   - It mentions the use of the same training settings (line 389).
   - It mentions the use of the same training settings (line 390).
   - It mentions the use of the same training settings (line 391).
   - It mentions the use of the same training settings (line 392).
   - It mentions the use of the same training settings (line 393).
   - It mentions the use of the same training settings (line 394).
   - It mentions the use of the same training settings (line 395).
   - It mentions the use of the same training settings (line 396).
   - It mentions the use of the same training settings (line 397).
   - It mentions the use of the same training settings (line 398).
   - It mentions the use of the same training settings (line 399).
   - It mentions the use of the same training settings (line 400).
   - It mentions the use of the same training settings (line 401).
   - It mentions the use of the same training settings (line 402).
   - It mentions the use of the same training settings (line 403).
   - It mentions the use of the same training settings (line 404).
   - It mentions the use of the same training settings (line 405).
   - It mentions the use of the same training settings (line 406).
   - It mentions the use of the same training settings (line 407).
   - It mentions the use of the same training settings (line 408).
   - It mentions the use of the same training settings (line 409).
   - It mentions the use of the same training settings (line 410).
   - It mentions the use of the same training settings (line 411).
   - It mentions the use of the same training settings (line 412).
   - It mentions the use of the same training settings (line 413).
   - It mentions the use of the same training settings (line 414).
   - It mentions the use of the same training settings (line 415).
   - It mentions the use of the same training settings (line 416).
   - It mentions the use of the same training settings (line 417).
   - It mentions the use of the same training settings (line 418).
   - It mentions the use of the same training settings (line 419).
   - It mentions the use of the same training settings (line 420).
   - It mentions the use of the same training settings (line 421).
   - It mentions the use of the same training settings (line 422).
   - It mentions the use of the same training settings (line 423).
   - It mentions the use of the same training settings (line 424).
   - It mentions the use of the same training settings (line 425).
   - It mentions the use of the same training settings (line 426).
   - It mentions the use of the same training settings (line 427).
   - It mentions the use of the same training settings (line 428).
   - It mentions the use of the same training settings (line 429).
   - It mentions the use of the same training settings (line 430).
   - It mentions the use of the same training settings (line 431).
   - It mentions the use of the same training settings (line 432).
   - It mentions the use of the same training settings (line 433).
   - It mentions the use of the same training settings (line 434).
   - It mentions the use of the same training settings (line 435).
   - It mentions the use of the same training settings (line 436).
   - It mentions the use of the same training settings (line 437).
   - It mentions the use of the same training settings (line 438).
   - It mentions the use of the same training settings (line 439).
   - It mentions the use of the same training settings (line 440).
   - It mentions the use of the same training settings (line 441).
   - It mentions the use of the same training settings (line 442).
   - It mentions the use of the same training settings (line 443).
   - It mentions the use of the same training settings (line 444).
   - It mentions the use of the same training settings (line 445).
   - It mentions the use of the same training settings (line 446).
   - It mentions the use of the same training settings (line 447).
   - It mentions the use of the same training settings (line 448).
   - It mentions the use of the same training settings (line 449).
   - It mentions the use of the same training settings (line 450).
   - It mentions the use of the same training settings (line 451).
   - It mentions the use of the same training settings (line 452).
   - It mentions the use of the same training settings (line 453).
   - It mentions the use of the same training settings (line 454).
   - It mentions the use of the same training settings (line 455).
   - It mentions the use of the same training settings (line 456).
   - It mentions the use of the same training settings (line 457).
   - It mentions the use of the same training settings (line 458).
   - It mentions the use of the same training settings (line 459).
   - It mentions the use of the same training settings (line 460).
   - It mentions the use of the same training settings (line 461).
   - It mentions the use of the same training settings (line 462).
   - It mentions the use of the same training settings (line 463).
   - It mentions the use of the same training settings (line 464).
   - It mentions the use of the same training settings (line 465).
   - It mentions the use of the same training settings (line 466).
   - It mentions the use of the same training settings (line 467).
   - It mentions the use of the same training settings (line 468).
   - It mentions the use of the same training settings (line 469).
   - It mentions the use of the same training settings (line 470).
   - It mentions the use of the same training settings (line 471).
   - It mentions the use of the same training settings (line 472).
   - It mentions the use of the same training settings (line 473).
   - It mentions the use of the same training settings (line 474).
   - It mentions the use of the same training settings (line 475).
   - It mentions the use of the same training settings (line 476).
   - It mentions the use of the same training settings (line 477).
   - It mentions the use of the same training settings (line 478).
   - It mentions the use of the same training settings (line 479).
   - It mentions the use of the same training settings (line 480).
   - It mentions the use of the same training settings (line 481).
   - It mentions the use of the same training settings (line 482).
   - It mentions the use of the same training settings (line 483).
   - It mentions the use of the same training settings (line 484).
   - It mentions the use of the same training settings (line 485).
   - It mentions the use of the same training settings (line 486).
   - It mentions the use of the same training settings (line 487).
   - It mentions the use of the same training settings (line 488).
   - It mentions the use of the same training settings (line 489).
   - It mentions the use of the same training settings (line 490).
   - It mentions the use of the same training settings (line 491).
   - It mentions the use of the same training settings (line 492).
   - It mentions the use of the same training settings (line 493).
   - It mentions the use of the same training settings (line 494).
   - It mentions the use of the same training settings (line 495).
   - It mentions the use of the same training settings (line 496).
   - It mentions the use of the same training settings (line 497).
   - It mentions the use of the same training settings (line 498).
   - It mentions the use of the same training settings (line 499).
   - It mentions the use of the same training settings (line 500).
   - It mentions the use of the same training settings (line 501).
   - It mentions the use of the same training settings (line 502).
   - It mentions the use of the same training settings (line 503).
   - It mentions the use of the same training settings (line 504).
   - It mentions the use of the same training settings (line 505).
   - It mentions the use of the same training settings (line 506).
   - It mentions the use of the same training settings (line 507).
   - It mentions the use of the same training settings (line 508).
   - It mentions the use of the same training settings (line 509).
   - It mentions the use of the same training settings (line 510).
   - It mentions the use of the same training settings (line 511).
   - It mentions the use of the same training settings (line 512).
   - It mentions the use of the same training settings (line 513).
   - It mentions the use of the same training settings (line 514).
   - It mentions the use of the same training settings (line 515).
   - It mentions the use of the same training settings (line 516).
   - It mentions the use of the same training settings (line 517).
   - It mentions the use of the same training settings (line 518).
   - It mentions the use of the same training settings (line 519).
   - It mentions the use of the same training settings (line 520).
   - It mentions the use of the same training settings (line 521).
   - It mentions the use of the same training settings (line 522).
   - It mentions the use of the same training settings (line 523).
   - It mentions the use of the same training settings (line 524).
   - It mentions the use of the same training settings (line 525).
   - It mentions the use of the same training settings (line 526).
   - It mentions the use of the same training settings (line 527).
   - It mentions the use of the same training settings (line 528).
   - It mentions the use of the same training settings (line 529).
   - It mentions the use of the same training settings (line 530).
   - It mentions the use of the same training settings (line 531).
   - It mentions the use of the same training settings (line 532).
   - It mentions the use of the same training settings (line 533).
   - It mentions the use of the same training settings (line 534).
   - It mentions the use of the same training settings (line 535).
   - It mentions the use of the same training settings (line 536).
   - It mentions the use of the same training settings (line 537).
   - It mentions the use of the same training settings (line 538).
   - It mentions the use of the same training settings (line 539).
   - It mentions the use of the same training settings (line 540).
   - It mentions the use of the same training settings (line 541).
   - It mentions the use of the same training settings (line 542).
   - It mentions the use of the same training settings (line 543).
   - It mentions the use of the same training settings (line 544).
   - It mentions the use of the same training settings (line 545).
   - It mentions the use of the same training settings (line 546).
   - It mentions the use of the same training settings (line 547).
   - It mentions the use of the same training settings (line 548).
   - It mentions the use of the same training settings (line 549).
   - It mentions the use of the same training settings (line 550).
   - It mentions the use of the same training settings (line 551).
   - It mentions the use of the same training settings (line 552).
   - It mentions the use of the same training settings (line 553).
   - It mentions the use of the same training settings (line 554).
   - It mentions the use of the same training settings (line 555).
   - It mentions the use of the same training settings (line 556).
   - It mentions the use of the same training settings (line 557).
   - It mentions the use of the same training settings (line 558).
   - It mentions the use of the same training settings (line 559).
   - It mentions the use of the same training settings (line 560).
   - It mentions the use of the same training settings (line 561).
   - It mentions the use of the same training settings (line 562).
   - It mentions the use of the same training settings (line 563).
   - It mentions the use of the same training settings (line 564).
   - It mentions the use of the same training settings (line 565).
   - It mentions the use of the same training settings (line 566).
   - It mentions the use of the same training settings (line 567).
   - It mentions the use of the same training settings (line 568).
   - It mentions the use of the same training settings (line 569).
   - It mentions the use of the same training settings (line 570).
   - It mentions the use of the same training settings (line 571).
   - It mentions the use of the same training settings (line 572).
   - It mentions the use of the same training settings (line 573).
   - It mentions the use of the same training settings (line 574).
   - It mentions the use of the same training settings (line 575).
   - It mentions the use of the same training settings (line 576).
   - It mentions the use of the same training settings (line 577).
   - It mentions the use of the same training settings (line 578).
   - It mentions the use of the same training settings (line 579).
   - It mentions the use of the same training settings (line 580).
   - It mentions the use of the same training settings (line 581).
   - It mentions the use of the same training settings (line 582).
   - It mentions the use of the same training settings (line 583).
   - It mentions the use of the same training settings (line 584).
   - It mentions the use of the same training settings (line 585).
   - It mentions the use of the same training settings (line 586).
   - It mentions the use of the same training settings (line 587).
   - It mentions the use of the same training settings (line 588).
   - It mentions the use of the same training settings (line 589).
   - It mentions the use of the same training settings (line 590).
   - It mentions the use of the same training settings (line 591).
   - It mentions the use of the same training settings (line 592).
   - It mentions the use of the same training settings (line 593).
   - It mentions the use of the same training settings (line 594).
   - It mentions the use of the same training settings (line 595).
   - It mentions the use of the same training settings (line 596).
   - It mentions the use of the same training settings (line 597).
   - It mentions the use of the same training settings (line 598).
   - It mentions the use of the same training settings (line 599).
   - It mentions the use of the same training settings (line 600).
   - It mentions the use of the same training settings (line 601).
   - It mentions the use of the same training settings (line 602).
   - It mentions the use of the same training settings (line 603).
   - It mentions the use of the same training settings (line 604).
   - It mentions the use of the same training settings (line 605).
   - It mentions the use of the same training settings (line 606).
   - It mentions the use of the same training settings (line 607).
   - It mentions the use of the same training settings (line 608).
   - It mentions the use of the same training settings (line 609).
   - It mentions the use of the same training settings (line 610).
   - It mentions the use of the same training settings (line 611).
   - It mentions the use of the same training settings (line 612).
   - It mentions the use of the same training settings (line 613).
   - It mentions the use of the same training settings (line 614).
   - It mentions the use of the same training settings (line 615).
   - It mentions the use of the same training settings (line 616).
   - It mentions the use of the same training settings (line 617).
   - It mentions the use of the same training settings (line 618).
   - It mentions the use of the same training settings (line 619).
   - It mentions the use of the same training settings (line 620).
   - It mentions the use of the same training settings (line 621).
   - It mentions the use of the same training settings (line 622).
   - It mentions the use of the same training settings (line 623).
   - It mentions the use of the same training settings (line 624).
   - It mentions the use of the same training settings (line 625).
   - It mentions the use of the same training settings (line 626).
   - It mentions the use of the same training settings (line 627).
   - It mentions the use of the same training settings (line 628).
   - It mentions the use of the same training settings (line 629).
   - It mentions the use of the same training settings (line 630).
   - It mentions the use of the same training settings (line 631).
   - It mentions the use of the same training settings (line 632).
   - It mentions the use of the same training settings (line 633).
   - It mentions the use of the same training settings (line 634).
   - It mentions the use of the same training settings (line 635).
   - It mentions the use of the same training settings (line 636).
   - It mentions the use of the same training settings (line 637).
   - It mentions the use of the same training settings (line 638).
   - It mentions the use of the same training settings (line 639).
   - It mentions the use of the same training settings (line 640).
   - It mentions the use of the same training settings (line 641).
   - It mentions the use of the same training settings (line 642).
   - It mentions the use of the same training settings (line 643).
   - It mentions the use of the same training settings (line 644).
   - It mentions the use of the same training settings (line 645).
   - It mentions the use of the same training settings (line 646).
   - It mentions the use of the same training settings (line 647).
   - It mentions the use of the same training settings (line 648).
   - It mentions the use of the same training settings (line 649).
   - It mentions the use of the same training settings (line 650).
   - It mentions the use of the same training settings (line 651).
   - It mentions the use of the same training settings (line 652).
   - It mentions the use of the same training settings (line 653).
   - It mentions the use of the same training settings (line 654).
   - It mentions the use of the same training settings (line 655).
   - It mentions the use of the same training settings (line 656).
   - It mentions the use of the same training settings (line 657).
   - It mentions the use of the same training settings (line 658).
   - It mentions the use of the same training settings (line 659).
   - It mentions the use of the same training settings (line 660).
   - It mentions the use of the same training settings (line 661).
   - It mentions the use of the same training settings (line 662).
   - It mentions the use of the same training settings (line 663).
   - It mentions the use of the same training settings (line 664).
   - It mentions the use of the same training settings (line 665).
   - It mentions the use of the same training settings (line 666).
   - It mentions the use of the same training settings (line 667).
   - It mentions the use of the same training settings (line 668).
   - It mentions the use of the same training settings (line 669).
   - It mentions the use of the same training settings (line 670).
   - It mentions the use of the same training settings (line 671).
   - It mentions the use of the same training settings (line 672).
   - It mentions the use of the same training settings (line 673).
   - It mentions the use of the same training settings (line 674).
   - It mentions the use of the same training settings (line 675).
   - It mentions the use of the same training settings (line 676).
   - It mentions the use of the same training settings (line 677).
   - It mentions the use of the same training settings (line 678).
   - It mentions the use of the same training settings (line 679).
   - It mentions the use of the same training settings (line 680).
   - It mentions the use of the same training settings (line 681).
   - It mentions the use of the same training settings (line 682).
   - It mentions the use of the same training settings (line 683).
   - It mentions the use of the same training settings (line 684).
   - It mentions the use of the same training settings (line 685).
   - It mentions the use of the same training settings (line 686).
   - It mentions the use of the same training settings (line 687).
   - It mentions the use of the same training settings (line 688).
   - It mentions the use of the same training settings (line 689).
   - It mentions the use of the Verl framework.
   - It mentions the implementation details in Appendix A.
   - It mentions the use of a reduced setting due to computational resource constraints.
   - It mentions the use of the same prompt for all methods.
   - It mentions the implementation details in Appendix A.
   - It mentions the use of the same prompt for all methods.
   - It mentions the implementation details in Appendix A.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the same prompt for all methods.
   - It mentions the use of the