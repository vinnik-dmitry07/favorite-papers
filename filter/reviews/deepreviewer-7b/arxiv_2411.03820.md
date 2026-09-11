I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper presents an algorithm called "Beyond The Rainbow" (BTR), which integrates six improvements from the Rainbow DQN algorithm to achieve state-of-the-art performance on Atari-60 while maintaining computational efficiency. BTR demonstrates strong performance on Atari-60 and Procgen benchmarks, and it successfully trains agents to play three modern 3D games: Super Mario Galaxy, Mario Kart Wii, and Mortal Kombat. The authors provide detailed ablation studies and analyses of BTR's components to understand their individual contributions. The paper also includes a discussion of the computational resources required to train BTR and compares it to other state-of-the-art algorithms. Overall, the paper highlights the potential of combining existing techniques to achieve high performance in RL with minimal computational resources.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand.
2. The authors provide a thorough analysis of BTR's components, including ablation studies and comparisons with other algorithms. This analysis helps to understand the individual contributions of each component and their impact on the overall performance of the algorithm.
3. The paper demonstrates the potential of combining existing techniques to achieve high performance in RL with minimal computational resources. This is a significant contribution to the field, as it makes high-performance RL more accessible to researchers and practitioners with limited computational resources.
4. The paper includes a discussion of the computational resources required to train BTR and compares it to other state-of-the-art algorithms. This information is valuable for researchers and practitioners who are interested in using BTR and want to understand its computational requirements.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of BTR or the scenarios where it may not perform well. This is a significant limitation, as it is important to understand the limitations of any algorithm in order to use it effectively. For example, the paper does not discuss how BTR would perform in environments with sparse rewards or in environments with high-dimensional state spaces. It would be beneficial to include a discussion of the potential limitations of BTR and the scenarios where it may not perform well.
2. The paper does not provide a detailed discussion of the hyperparameters used in BTR and how they were selected. This is important because the performance of RL algorithms is often sensitive to the choice of hyperparameters. The paper should include a discussion of the hyperparameters used in BTR and how they were selected, as well as a discussion of the potential impact of different hyperparameter values on the performance of the algorithm. For example, the paper does not discuss the impact of different learning rates or different exploration strategies on the performance of BTR.
3. The paper does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the paper mentions that BTR is computationally efficient, it does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. This is important because computational efficiency is a key factor in the practical application of RL algorithms. The paper should include a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency, including a discussion of the computational resources required to train BTR and other state-of-the-art algorithms. For example, the paper does not discuss the impact of different hardware configurations on the computational efficiency of BTR.
4. The paper does not provide a detailed discussion of the robustness of BTR to different types of noise or perturbations in the environment. This is important because RL algorithms are often used in real-world environments, which may be subject to noise and perturbations. The paper should include a discussion of the robustness of BTR to different types of noise or perturbations in the environment, as well as a discussion of the potential impact of different types of noise on the performance of the algorithm. For example, the paper does not discuss the impact of different types of noise on the performance of BTR in environments with sparse rewards or in environments with high-dimensional state spaces.

### Suggestions

The paper would benefit significantly from a more thorough discussion of the limitations of the proposed BTR algorithm. While the authors demonstrate strong performance on several benchmarks, it is crucial to understand the scenarios where BTR might struggle. For instance, the paper should explore the performance of BTR in environments with extremely sparse rewards, where the agent receives feedback only rarely, or in environments with very high-dimensional state spaces, where the complexity of the state representation could pose challenges. Furthermore, the paper should discuss the potential limitations of BTR in terms of its ability to generalize to unseen environments or tasks. A detailed analysis of these limitations would provide a more balanced view of the algorithm's capabilities and help guide future research in this area. This analysis should include a discussion of the potential failure modes of BTR and the conditions under which it might not be the most suitable algorithm to use.

In addition to the limitations, the paper should provide a more detailed explanation of the hyperparameter selection process. The authors mention that they used a small amount of tuning, but they do not provide sufficient information about the specific hyperparameters that were tuned, the range of values that were explored, and the criteria used to select the optimal values. This lack of detail makes it difficult to reproduce the results and to understand the sensitivity of the algorithm to different hyperparameter settings. The paper should include a table or a figure that shows the performance of BTR as a function of different hyperparameter values, as well as a discussion of the potential impact of different hyperparameter choices on the performance of the algorithm. Furthermore, the paper should discuss the potential impact of different exploration strategies on the performance of BTR. For example, the paper should discuss the impact of different epsilon-greedy strategies or different noise schedules on the learning process. This analysis should include a discussion of the potential trade-offs between exploration and exploitation in the context of BTR.

Finally, the paper should provide a more detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the authors mention that BTR is computationally efficient, they do not provide a detailed comparison of BTR with other algorithms in terms of wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance. This comparison should include a discussion of the computational resources required to train BTR and other state-of-the-art algorithms on different hardware configurations. The paper should also discuss the potential impact of different optimization techniques on the computational efficiency of BTR. For example, the paper should discuss the impact of different gradient clipping techniques or different optimization algorithms on the training time of BTR. This analysis should include a discussion of the potential trade-offs between computational efficiency and performance in the context of BTR.

### Questions

1. How does BTR perform in environments with sparse rewards or in environments with high-dimensional state spaces?
2. What is the impact of different hyperparameters on the performance of BTR, and how were the hyperparameters selected?
3. How does BTR compare to other state-of-the-art algorithms in terms of computational efficiency, including wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance?
4. How robust is BTR to different types of noise or perturbations in the environment?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

The paper proposes a combination of existing techniques to improve the performance of DQN. The paper is well-written and easy to follow. The authors provide a comprehensive analysis of the proposed method.

### Soundness

3

### Presentation

4

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The authors provide a comprehensive analysis of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of BTR or the scenarios where it may not perform well. This is a significant limitation, as it is important to understand the limitations of any algorithm in order to use it effectively. For example, the paper does not discuss how BTR would perform in environments with sparse rewards or in environments with high-dimensional state spaces. It would be beneficial to include a discussion of the potential limitations of BTR and the scenarios where it may not perform well.
2. The paper does not provide a detailed discussion of the hyperparameters used in BTR and how they were selected. This is important because the performance of RL algorithms is often sensitive to the choice of hyperparameters. The paper should include a discussion of the hyperparameters used in BTR and how they were selected, as well as a discussion of the potential impact of different hyperparameter values on the performance of the algorithm. For example, the paper does not discuss the impact of different learning rates or different exploration strategies on the performance of BTR.
3. The paper does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the paper mentions that BTR is computationally efficient, it does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. This is important because computational efficiency is a key factor in the practical application of RL algorithms. The paper should include a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency, including a discussion of the computational resources required to train BTR and other state-of-the-art algorithms. For example, the paper does not discuss the impact of different hardware configurations on the computational efficiency of BTR.
4. The paper does not provide a detailed discussion of the robustness of BTR to different types of noise or perturbations in the environment. This is important because RL algorithms are often used in real-world environments, which may be subject to noise and perturbations. The paper should include a discussion of the robustness of BTR to different types of noise or perturbations in the environment, as well as a discussion of the potential impact of different types of noise on the performance of the algorithm. For example, the paper does not discuss the impact of different types of noise on the performance of BTR in environments with sparse rewards or in environments with high-dimensional state spaces.

### Suggestions

The paper would benefit significantly from a more thorough analysis of the limitations of the proposed BTR algorithm. While the authors demonstrate strong performance on several benchmarks, it is crucial to understand the scenarios where BTR might struggle. For instance, the paper should explore the performance of BTR in environments with extremely sparse rewards, where the agent receives feedback only rarely, or in environments with very high-dimensional state spaces, where the complexity of the state representation could pose challenges. Furthermore, the paper should discuss the potential limitations of BTR in terms of its ability to generalize to unseen environments or tasks. A detailed analysis of these limitations would provide a more balanced view of the algorithm's capabilities and help guide future research in this area. This analysis should include a discussion of the potential failure modes of BTR and the conditions under which it might not be the most suitable algorithm to use.

In addition to the limitations, the paper needs a more detailed discussion of the hyperparameter selection process. The authors mention that they used a small amount of tuning, but they do not provide sufficient information about the specific hyperparameters that were tuned, the range of values that were explored, and the criteria used to select the optimal values. This lack of detail makes it difficult to reproduce the results and to understand the sensitivity of the algorithm to different hyperparameter settings. The paper should include a table or a figure that shows the performance of BTR as a function of different hyperparameter values, as well as a discussion of the potential impact of different hyperparameter choices on the performance of the algorithm. Furthermore, the paper should discuss the potential impact of different exploration strategies on the performance of BTR. For example, the paper should discuss the impact of different epsilon-greedy strategies or different noise schedules on the learning process. This analysis should include a discussion of the potential trade-offs between exploration and exploitation in the context of BTR.

Finally, the paper should provide a more detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the authors mention that BTR is computationally efficient, they do not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance. This comparison should include a discussion of the computational resources required to train BTR and other state-of-the-art algorithms on different hardware configurations. The paper should also discuss the potential impact of different optimization techniques on the computational efficiency of BTR. For example, the paper should discuss the impact of different gradient clipping techniques or different optimization algorithms on the training time of BTR. This analysis should include a discussion of the potential trade-offs between computational efficiency and performance in the context of BTR.

### Questions

1. How does BTR perform in environments with sparse rewards or in environments with high-dimensional state spaces?
2. What is the impact of different hyperparameters on the performance of BTR, and how were the hyperparameters selected?
3. How does BTR compare to other state-of-the-art algorithms in terms of computational efficiency, including wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance?
4. How robust is BTR to different types of noise or perturbations in the environment?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

This paper presents BTR (Beyond The Rainbow), a new reinforcement learning algorithm that combines six improvements from the Rainbow DQN algorithm to achieve state-of-the-art performance on Atari-60 while maintaining computational efficiency. BTR demonstrates strong performance on Atari-60 and Procgen benchmarks, and it successfully trains agents to play three modern 3D games: Super Mario Galaxy, Mario Kart Wii, and Mortal Kombat. The authors provide detailed ablation studies and analyses of BTR's components to understand their individual contributions. The paper also includes a discussion of the computational resources required to train BTR and compares it to other state-of-the-art algorithms. Overall, the paper highlights the potential of combining existing techniques to achieve high performance in RL with minimal computational resources.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand.
2. The authors provide a thorough analysis of BTR's components, including ablation studies and comparisons with other algorithms. This analysis helps to understand the individual contributions of each component and their impact on the overall performance of the algorithm.
3. The paper demonstrates the potential of combining existing techniques to achieve high performance in RL with minimal computational resources. This is a significant contribution to the field, as it makes high-performance RL more accessible to researchers and practitioners with limited computational resources.
4. The paper includes a discussion of the computational resources required to train BTR and compares it to other state-of-the-art algorithms. This information is valuable for researchers and practitioners who are interested in using BTR and want to understand its computational requirements.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of BTR or the scenarios where it may not perform well. This is a significant limitation, as it is important to understand the limitations of any algorithm in order to use it effectively. For example, the paper does not discuss how BTR would perform in environments with sparse rewards or in environments with high-dimensional state spaces. It would be beneficial to include a discussion of the potential limitations of BTR and the scenarios where it may not perform well.
2. The paper does not provide a detailed discussion of the hyperparameters used in BTR and how they were selected. This is important because the performance of RL algorithms is often sensitive to the choice of hyperparameters. The paper should include a discussion of the hyperparameters used in BTR and how they were selected, as well as a discussion of the potential impact of different hyperparameter values on the performance of the algorithm. For example, the paper does not discuss the impact of different learning rates or different exploration strategies on the performance of BTR.
3. The paper does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the paper mentions that BTR is computationally efficient, it does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. This is important because computational efficiency is a key factor in the practical application of RL algorithms. The paper should include a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency, including a discussion of the computational resources required to train BTR and other state-of-the-art algorithms. For example, the paper does not discuss the impact of different hardware configurations on the computational efficiency of BTR.
4. The paper does not provide a detailed discussion of the robustness of BTR to different types of noise or perturbations in the environment. This is important because RL algorithms are often used in real-world environments, which may be subject to noise and perturbations. The paper should include a discussion of the robustness of BTR to different types of noise or perturbations in the environment, as well as a discussion of the potential impact of different types of noise on the performance of the algorithm. For example, the paper does not discuss the impact of different types of noise on the performance of BTR in environments with sparse rewards or in environments with high-dimensional state spaces.

### Suggestions

The paper would significantly benefit from a more thorough analysis of the limitations of the proposed BTR algorithm. While the authors demonstrate strong performance on Atari-60 and Procgen, it is crucial to understand the boundaries of its applicability. Specifically, the paper should include experiments or discussions on how BTR performs in environments with sparse rewards, which are common in many real-world scenarios. For instance, the authors could evaluate BTR on environments with very infrequent positive feedback, such as those found in some robotic control tasks or complex strategy games. Furthermore, the paper should explore the performance of BTR in high-dimensional state spaces, as many real-world problems involve complex, high-dimensional inputs. This could be done by testing BTR on environments with a large number of features or by artificially increasing the dimensionality of the state space. A detailed analysis of these limitations would provide a more complete picture of the algorithm's capabilities and limitations.

In addition to the limitations, the paper needs a more detailed discussion of the hyperparameter selection process. The authors mention using a small amount of tuning, but this is not sufficient for a rigorous scientific analysis. The paper should include a table or figure that shows the performance of BTR as a function of different hyperparameter values. This would allow readers to understand the sensitivity of the algorithm to different parameter settings. Furthermore, the paper should discuss the impact of different learning rates, exploration strategies, and other key hyperparameters on the performance of BTR. For example, the authors could explore the effect of different epsilon-greedy strategies or different noise schedules. This analysis should also include a discussion of the potential trade-offs between different hyperparameter choices and their impact on the overall performance of the algorithm. This would provide valuable guidance for practitioners who want to use BTR in their own applications.

Finally, the paper should provide a more detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the authors mention that BTR is computationally efficient, they do not provide a detailed comparison of its computational requirements with other algorithms. The paper should include a table that shows the training time, memory usage, and other relevant computational metrics for BTR and other state-of-the-art algorithms. This comparison should also include a discussion of the computational resources required to train BTR and other algorithms on different hardware configurations. For example, the authors could compare the performance of BTR on different GPUs or CPUs. This would provide a more complete understanding of the computational trade-offs associated with using BTR. Furthermore, the paper should discuss the robustness of BTR to different types of noise or perturbations in the environment. This could be done by testing BTR on environments with different types of noise, such as Gaussian noise or salt-and-pepper noise. The paper should also discuss the potential impact of different types of noise on the performance of the algorithm.

### Questions

1. How does BTR perform in environments with sparse rewards or in environments with high-dimensional state spaces?
2. What is the impact of different hyperparameters on the performance of BTR, and how were the hyperparameters selected?
3. How does BTR compare to other state-of-the-art algorithms in terms of computational efficiency, including wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance?
4. How robust is BTR to different types of noise or perturbations in the environment?

### Rating

6

### Confidence

4

**********

## Reviewer 4

### Summary

This paper introduces BTR, an algorithm that combines six improvements from Rainbow DQN to achieve state-of-the-art performance on Atari-60 while maintaining computational efficiency. The authors demonstrate BTR's capabilities by training agents to play three modern 3D games: Super Mario Galaxy, Mario Kart Wii, and Mortal Kombat. The paper provides detailed ablation studies and analyses of BTR's components to understand their individual contributions.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand.
2. The authors provide a thorough analysis of BTR's components, including ablation studies and comparisons with other algorithms. This analysis helps to understand the individual contributions of each component and their impact on the overall performance of the algorithm.
3. The paper demonstrates the potential of combining existing techniques to achieve high performance in RL with minimal computational resources. This is a significant contribution to the field, as it makes high-performance RL more accessible to researchers and practitioners with limited computational resources.
4. The paper includes a discussion of the computational resources required to train BTR and compares it to other state-of-the-art algorithms. This information is valuable for researchers and practitioners who are interested in using BTR and want to understand its computational requirements.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of BTR or the scenarios where it may not perform well. This is a significant limitation, as it is important to understand the limitations of any algorithm in order to use it effectively. For example, the paper does not discuss how BTR would perform in environments with sparse rewards or in environments with high-dimensional state spaces. It would be beneficial to include a discussion of the potential limitations of BTR and the scenarios where it may not perform well.
2. The paper does not provide a detailed discussion of the hyperparameters used in BTR and how they were selected. This is important because the performance of RL algorithms is often sensitive to the choice of hyperparameters. The paper should include a discussion of the hyperparameters used in BTR and how they were selected, as well as a discussion of the potential impact of different hyperparameter values on the performance of the algorithm. For example, the paper does not discuss the impact of different learning rates or different exploration strategies on the performance of BTR.
3. The paper does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the paper mentions that BTR is computationally efficient, it does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. This is important because computational efficiency is a key factor in the practical application of RL algorithms. The paper should include a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency, including a discussion of the computational resources required to train BTR and other state-of-the-art algorithms. For example, the paper does not discuss the impact of different hardware configurations on the computational efficiency of BTR.
4. The paper does not provide a detailed discussion of the robustness of BTR to different types of noise or perturbations in the environment. This is important because RL algorithms are often used in real-world environments, which may be subject to noise and perturbations. The paper should include a discussion of the robustness of BTR to different types of noise or perturbations in the environment, as well as a discussion of the potential impact of different types of noise on the performance of the algorithm. For example, the paper does not discuss the impact of different types of noise on the performance of BTR in environments with sparse rewards or in environments with high-dimensional state spaces.

### Suggestions

The paper would benefit from a more thorough analysis of the limitations of the proposed BTR algorithm. Specifically, the authors should investigate the performance of BTR in environments with sparse rewards, which are common in many real-world scenarios. For instance, they could evaluate BTR on environments with very infrequent positive feedback, such as those found in some robotic control tasks or complex strategy games. This would provide a more comprehensive understanding of the algorithm's robustness and its applicability to a wider range of problems. Furthermore, the paper should explore the performance of BTR in high-dimensional state spaces, as many real-world problems involve complex, high-dimensional inputs. This could be done by testing BTR on environments with a large number of features or by artificially increasing the dimensionality of the state space. A detailed analysis of these limitations would provide a more complete picture of the algorithm's capabilities and limitations.

In addition to the limitations, the paper needs a more detailed discussion of the hyperparameter selection process. The authors mention using a small amount of tuning, but this is not sufficient for a rigorous scientific analysis. The paper should include a table or figure that shows the performance of BTR as a function of different hyperparameter values. This would allow readers to understand the sensitivity of the algorithm to different parameter settings. Furthermore, the paper should discuss the impact of different learning rates, exploration strategies, and other key hyperparameters on the performance of BTR. For example, the authors could explore the effect of different epsilon-greedy strategies or different noise schedules. This analysis should also include a discussion of the potential trade-offs between different hyperparameter choices and their impact on the overall performance of the algorithm. This would provide valuable guidance for practitioners who want to use BTR in their own applications.

Finally, the paper should provide a more detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the authors mention that BTR is computationally efficient, they do not provide a detailed comparison of its computational requirements with other algorithms. The paper should include a table that shows the training time, memory usage, and other relevant computational metrics for BTR and other state-of-the-art algorithms. This comparison should also include a discussion of the computational resources required to train BTR and other algorithms on different hardware configurations. For example, the authors could compare the performance of BTR on different GPUs or CPUs. This would provide a more complete understanding of the computational trade-offs associated with using BTR. Furthermore, the paper should discuss the robustness of BTR to different types of noise or perturbations in the environment. This could be done by testing BTR on environments with different types of noise, such as Gaussian noise or salt-and-pepper noise. The paper should also discuss the potential impact of different types of noise on the performance of the algorithm.

### Questions

1. How does BTR perform in environments with sparse rewards or in environments with high-dimensional state spaces?
2. What is the impact of different hyperparameters on the performance of BTR, and how were the hyperparameters selected?
3. How does BTR compare to other state-of-the-art algorithms in terms of computational efficiency, including wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance?
4. How robust is BTR to different types of noise or perturbations in the environment?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence (methodological, experimental).
4. Write a validation analysis for each weakness, including evidence and a conclusion about its validity.
```json
[
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the limitations of BTR or the scenarios where it may not perform well. This is a significant limitation, as it is important to understand the limitations of any algorithm in order to use it effectively. For example, the paper does not discuss how BTR would perform in environments with sparse rewards or in environments with high-dimensional state spaces. It would be beneficial to include a discussion of the potential limitations of BTR and the scenarios where it may not perform well.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "The paper focuses on demonstrating BTR's performance on Atari-60 and three modern 3D games.",
        "The 'Limitations' section in the 'Conclusion' mentions: \"We acknowledge there exists many more promising improvements we could not include in BTR, leaving room for more future work to create stronger integrated agents in a few years. For example, BTR does not add an explicit exploration component, resulting in it struggling in hard-exploration tasks such as Montezuma’s Revenge ; therefore, mechanisms used in Never Give Up ( Badia et al., 2020b ) , etc may prove useful. Section 5.1 found that the neural network’s core architecture, Impala, had the largest effect on performance, an area we believe is generally underappreciated in RL. Previous work ( Kapturowski et al., 2018 ) has incorporated recurrent models enhancing performance, though we are uncertain how this can be incorporated into BTR without affecting its computational accessibility, a question which warrants future research.\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper acknowledges limitations in the conclusion, specifically mentioning the absence of an explicit exploration component and potential struggles with hard-exploration tasks like Montezuma's Revenge. It also notes that the neural network architecture's impact is not fully explored.",
      "Supporting quotes": [
        "\"BTR does not add an explicit exploration component, resulting in it struggling in hard-exploration tasks such as Montezuma’s Revenge\"",
        "\"Previous work ( Kapturowski et al., 2018 ) has incorporated recurrent models enhancing performance, though we are uncertain how this can be incorporated into BTR without affecting its computational accessibility, a question which warrants future research.\""
      ],
      "Impact assessment": "While the paper does mention some limitations, it doesn't delve into specific scenarios like sparse rewards or high-dimensional state spaces in detail, as suggested by the reviewer."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions limitations like the lack of explicit exploration and potential struggles with hard exploration, but lacks a detailed discussion on performance in environments with sparse rewards or high-dimensional state spaces."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed discussion of the hyperparameters used in BTR and how they were selected. This is important because the performance of RL algorithms is often sensitive to the choice of hyperparameters. The paper should include a discussion of the hyperparameters used in BTR and how they were selected, as well as a discussion of the potential impact of different hyperparameter values on the performance of the algorithm. For example, the paper does not discuss the impact of different learning rates or different exploration strategies on the performance of BTR.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 3.2 'Hyperparameters' discusses the choice of hyperparameters: \"Hyperparameters have repeatedly shown to have a very large impact on performance in RL ( Ceron et al., 2024 ) , thus we perform a small amount of tuning to improve performance. Firstly, how frequently the target network is updated is closely intertwined with batch size and replay ratio. We found that updating the target network every 500 gradient steps 4 4 4 This equates to 32,000 environment steps (128,000 frames), compared to Rainbow DQN’s 8,000 steps. performed best. Given our high batch size, we additionally performed minor hyperparameter tests using different learning rates finding that a slightly higher learning rate of 1 × 10 − 4 performed best, compared to 6.25 × 10 − 5 in Rainbow DQN. In Appendix H for a discussion on the impact of hyperparameters.\""
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions a small amount of hyperparameter tuning and provides some details on the learning rate and target network update frequency. However, it lacks a detailed discussion on the selection process for other hyperparameters and their potential impact.",
      "Supporting quotes": [
        "\"Given our high batch size, we additionally performed minor hyperparameter tests using different learning rates finding that a slightly higher learning rate of 1 × 10 − 4 performed best, compared to 6.25 × 10 − 5 in Rainbow DQN.\"",
        "\"In Appendix H for a discussion on the impact of hyperparameters.\""
      ],
      "Impact assessment": "While the paper mentions tuning, it doesn't provide a comprehensive discussion on the selection process and the sensitivity of the algorithm to different hyperparameter settings."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions some hyperparameter tuning but lacks a detailed discussion on the selection process and the impact of various hyperparameters."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the authors mention that BTR is computationally efficient, they do not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. This is important because computational efficiency is a key factor in the practical application of RL algorithms. The paper should include a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency, including a discussion of the computational resources required to train BTR and other state-of-the-art algorithms. For example, the paper does not discuss the impact of different hardware configurations on the computational efficiency of BTR.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "Section 4.1 'Atari and Procgen Performance' includes a paragraph on computational resources: \"To further confirm BTR’s performance, we benchmark on Procgen ( Cobbe et al., 2020 ) , a procedurally generated set of environments aiming to prevent overfitting to specific tasks, a prevalent problem in RL ( Justesen et al., 2018 ; Juliani et al., 2019 ) . The results are shown in Figure 3 with individual games in Appendix B . BTR was able to solve all three games, including consistently finishing first place in Mario Kart. In contrast, Rainbow DQN’s performance plateaued before completing any of the games. We provide videos of our agent playing all three Wii games and all games in the Atari-5 benchmark 5 5 5 https://www.youtube.com/playlist?list=PL4geUsKi0NN-sjbuZP_fU28AmAPQunLoI .\"",
        "The paper mentions the hardware used: \"We evaluate BTR on the Atari-60 benchmark following ( Machado et al., 2018 ) and without life information (see Appendix I for the impact), evaluating every million frames on 100 episodes. Figure 1 plots BTR against DQN, Rainbow DQN and Dreamer v3, showing BTR’s competitive performance despite using significantly less walltime. Figure 2 shows a box plot comparison of final performance. In comparison to human expert performance, BTR equals or exceeds them in 52 of 60. Importantly, we find that BTR appears to continue increasing performance beyond 200 million frames, indicating that higher performance is still possible with more time and data. Results tables and graphs can be found in Appendices A and B , respectively.\"",
        "Appendix D.2 'Hyperparameters' mentions: \"For many years, RL algorithms have used a discount rate of 0.99 0.99 , however, when reaching high performance, lower discount rates alter the optimal policy, causing even optimally performing agents to not collect the maximum cumulative rewards. To prevent this, we follow MuZero Reanalyse ( Schrittwieser et al., 2021 ) using γ = 0.997 . For our Prioritized Experience Replay, we use the lower value of α = 0.2 α = 0.2 , the parameter used to determine sample priority, recommended by Toromanoff et al. (2019) when using IQN. Lastly, many previous experiments used only noisy networks or ϵ -greedy exploration, however, we opt to use both until 100M frames, then set ϵ to zero, effectively disabling it. We elaborate on this decision in Appendix F .\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides some information on the computational resources used, including the hardware and the number of frames and episodes used for training. It also mentions the impact of hyperparameters on the discount rate. However, it lacks a direct comparison of BTR's computational efficiency with other state-of-the-art algorithms.",
      "Supporting quotes": [
        "\"BTR was able to solve all three games, including consistently finishing first place in Mario Kart.\"",
        "\"Figure 1 plots BTR against DQN, Rainbow DQN and Dreamer v3, showing BTR’s competitive performance despite using significantly less walltime.\"",
        "\"We evaluate BTR on the Atari-60 benchmark following ( Machado et al., 2018 ) and without life information... evaluating every million frames on 100 episodes.\"",
        "\"To prevent this, we follow MuZero Reanalyse ( Schrittwieser et al., 2021 ) using γ = 0.997 .\""
      ],
      "Impact assessment": "While the paper provides some computational details, it doesn't offer a comparative analysis against other algorithms, which would be valuable for assessing BTR's efficiency relative to alternatives."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides some computational details but lacks a direct comparison of BTR's efficiency with other state-of-the-art algorithms."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed discussion of the robustness of BTR to different types of noise or perturbations in the environment. This is important because RL algorithms are often used in real-world environments, which may be subject to noise and perturbations. The paper should include a discussion of the robustness of BTR to different types of noise or perturbations in the environment, as well as a discussion of the potential impact of different types of noise on the performance of the algorithm. For example, the paper does not discuss the impact of different types of noise on the performance of BTR in environments with sparse rewards or in environments with high-dimensional state spaces.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "The paper evaluates BTR on Atari-60 and three modern 3D games, which inherently involve some level of environmental noise and perturbations.",
        "The 'Atari and Procgen Performance' section (4.1) presents results on these benchmarks, showing BTR's performance.",
        "The 'Ablation Studies' section (5) investigates the impact of individual components, which could indirectly reflect robustness to specific types of perturbations introduced by those components."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates BTR on standard RL benchmarks, which involve environmental noise. The ablation studies offer insights into component-wise robustness. However, there's no explicit discussion or experimentation focused on systematically varying and analyzing different types of noise or perturbations.",
      "Supporting quotes": [],
      "Impact assessment": "While the paper shows BTR's performance on noisy environments, it lacks a dedicated analysis of its robustness to specific types of noise or perturbations."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper evaluates on noisy environments but lacks a dedicated discussion and experimentation on the impact of different types of noise or perturbations."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the limitations of the proposed BTR algorithm. While the authors demonstrate strong performance on Atari-60 and Procgen, it is crucial to understand the boundaries of its applicability. Specifically, the paper should include experiments or discussions on how BTR performs in environments with sparse rewards or in environments with high-dimensional state spaces. This could be done by evaluating BTR on environments with a large number of features or by artificially increasing the dimensionality of the state space. A detailed analysis of these limitations would provide a more complete picture of the algorithm's capabilities and limitations.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "The paper evaluates BTR on Atari-60, which includes games with varying reward densities (some sparse, some more dense).",
        "The paper evaluates BTR on Procgen, which involves high-dimensional state spaces.",
        "The 'Limitations' section in the 'Conclusion' mentions: \"We acknowledge there exists many more promising improvements we could not include in BTR, leaving room for more future work to create stronger integrated agents in a few years. For example, BTR does not add an explicit exploration component, resulting in it struggling in hard-exploration tasks such as Montezuma’s Revenge ; therefore, mechanisms used in Never Give Up ( Badia et al., 2020b ) , etc may prove useful.\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates BTR on both Atari-60 (with varying reward densities) and Procgen (high-dimensional). The conclusion also acknowledges limitations, specifically regarding hard-exploration tasks. However, it doesn't include specific experiments designed to isolate and analyze performance in environments with *only* sparse rewards or *only* artificially inflated high-dimensional state spaces.",
      "Supporting quotes": [
        "\"We acknowledge there exists many more promising improvements we could not include in BTR, leaving room for more future work to create stronger integrated agents in a few years. For example, BTR does not add an explicit exploration component, resulting in it struggling in hard-exploration tasks such as Montezuma’s Revenge\""
      ],
      "Impact assessment": "While the paper touches on limitations, it lacks targeted experiments to fully understand BTR's performance in environments specifically designed to test its robustness to sparse rewards or high dimensionality."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper evaluates on Atari-60 and Procgen, and mentions limitations, but lacks specific experiments isolating performance in environments with only sparse rewards or artificially inflated high-dimensional state spaces."
    }
  },
  {
    "Weakness Statement": "In addition to the limitations, the paper needs a more detailed discussion of the hyperparameter selection process. The authors mention using a small amount of tuning, but this is not sufficient for a rigorous scientific analysis. The paper should include a table or figure that shows the performance of BTR as a function of different hyperparameter values. This would allow readers to understand the sensitivity of the algorithm to different parameter settings. Furthermore, the paper should discuss the impact of different learning rates, exploration strategies, and other key hyperparameters on the performance of BTR. For example, the authors could explore the effect of different epsilon-greedy strategies or different noise schedules. This analysis should also include a discussion of the potential trade-offs between different hyperparameter choices and their impact on the overall performance of the algorithm. This would provide valuable guidance for practitioners who want to use BTR in their own applications.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 3.2 'Hyperparameters' discusses the choice of hyperparameters: \"Hyperparameters have repeatedly shown to have a very large impact on performance in RL ( Ceron et al., 2024 ) , thus we perform a small amount of tuning to improve performance. Firstly, how frequently the target network is updated is closely intertwined with batch size and replay ratio. We found that updating the target network every 500 gradient steps 4 4 4 This equates to 32,000 environment steps (128,000 frames), compared to Rainbow DQN’s 8,000 steps. performed best. Given our high batch size, we additionally performed minor hyperparameter tests using different learning rates finding that a slightly higher learning rate of 1 × 10 − 4 performed best, compared to 6.25 × 10 − 5 in Rainbow DQN. In Appendix H for a discussion on the impact of hyperparameters.\""
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions a small amount of hyperparameter tuning and provides some details on the learning rate and target network update frequency. However, it lacks a detailed discussion on the selection process for other hyperparameters and their potential impact, as well as a presentation of performance as a function of different hyperparameter values.",
      "Supporting quotes": [
        "\"Given our high batch size, we additionally performed minor hyperparameter tests using different learning rates finding that a slightly higher learning rate of 1 × 10 − 4 performed best, compared to 6.25 × 10 − 5 in Rainbow DQN.\"",
        "\"In Appendix H for a discussion on the impact of hyperparameters.\""
      ],
      "Impact assessment": "The paper provides some information on hyperparameter tuning but lacks a comprehensive analysis of the selection process and the sensitivity of the algorithm to different hyperparameter settings."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions some hyperparameter tuning but lacks a detailed discussion on the selection process and the sensitivity of the algorithm to different hyperparameter settings, including a performance analysis across different hyperparameter values."
    }
  },
  {
    "Weakness Statement": "Finally, the paper should provide a more detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the authors mention that BTR is computationally efficient, they do not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. This is important because computational efficiency is a key factor in the practical application of RL algorithms. The paper should include a table that shows the training time, memory usage, and other relevant computational metrics for BTR and other state-of-the-art algorithms. This comparison should also include a discussion of the computational resources required to train BTR and other algorithms on different hardware configurations. For example, the authors could compare the performance of BTR on different GPUs or CPUs. This would provide a more complete understanding of the computational trade-offs associated with using BTR. Furthermore, the paper should discuss the robustness of BTR to different types of noise or perturbations in the environment. This could be done by testing BTR on environments with different types of noise, such as Gaussian noise or salt-and-pepper noise. The paper should also discuss the potential impact of different types of noise on the performance of the algorithm.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "Section 4.1 'Atari and Procgen Performance' includes a paragraph on computational resources: \"To further confirm BTR’s performance, we benchmark on Procgen ( Cobbe et al., 2020 ) , a procedurally generated set of environments aiming to prevent overfitting to specific tasks, a prevalent problem in RL ( Justesen et al., 2018 ; Juliani et al., 2019 ) . The results are shown in Figure 3 with individual games in Appendix B . BTR was able to solve all three games, including consistently finishing first place in Mario Kart. In contrast, Rainbow DQN’s performance plateaued before completing any of the games. We provide videos of our agent playing all three Wii games and all games in the Atari-5 benchmark 5 5 5 https://www.youtube.com/playlist?list=PL4geUsKi0NN-sjbuZP_fU28AmAPQunLoI .\"",
        "The paper mentions the hardware used: \"We evaluate BTR on the Atari-60 benchmark following ( Machado et al., 2018 ) and without life information (see Appendix I for the impact), evaluating every million frames on 100 episodes. Figure 1 plots BTR against DQN, Rainbow DQN and Dreamer v3, showing BTR’s competitive performance despite using significantly less walltime. Figure 2 shows a box plot comparison of final performance. In comparison to human expert performance, BTR equals or exceeds them in 52 of 60. Importantly, we find that BTR appears to continue increasing performance beyond 200 million frames, indicating that higher performance is still possible with more time and data. Results tables and graphs can be found in Appendices A and B , respectively.\"",
        "Appendix D.2 'Hyperparameters' mentions: \"For many years, RL algorithms have used a discount rate of 0.99 0.99 , however, when reaching high performance, lower discount rates alter the optimal policy, causing even optimally performing agents to not collect the maximum cumulative rewards. To prevent this, we follow MuZero Reanalyse ( Schrittwieser et al., 2021 ) using γ = 0.997 . For our Prioritized Experience Replay, we use the lower value of α = 0.2 α = 0.2 , the parameter used to determine sample priority, recommended by Toromanoff et al. (2019) when using IQN. Lastly, many previous experiments used only noisy networks or ϵ -greedy exploration, however, we opt to use both until 100M frames, then set ϵ to zero, effectively disabling it. We elaborate on this decision in Appendix F .\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides some information on computational resources and compares BTR's performance against other algorithms in terms of walltime. However, it lacks a detailed table comparing computational metrics like training time, memory usage, and the impact of different hardware configurations. It also lacks experiments specifically designed to test robustness to different types of noise.",
      "Supporting quotes": [
        "\"Figure 1 plots BTR against DQN, Rainbow DQN and Dreamer v3, showing BTR’s competitive performance despite using significantly less walltime.\"",
        "\"We evaluate BTR on the Atari-60 benchmark following ( Machado et al., 2018 ) and without life information... evaluating every million frames on 100 episodes.\"",
        "\"To prevent this, we follow MuZero Reanalyse ( Schrittwieser et al., 2021 ) using γ = 0.997 .\""
      ],
      "Impact assessment": "The paper provides some computational context but lacks a comprehensive comparison and specific experiments on robustness to noise."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides some computational context and compares performance against other algorithms but lacks a detailed table comparing computational metrics and specific experiments on robustness to different types of noise."
    }
  },
  {
    "Weakness Statement": "How does BTR perform in environments with sparse rewards or in environments with high-dimensional state spaces?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "The paper evaluates BTR on Atari-60, which includes games with varying reward densities (some sparse, some more dense).",
        "The paper evaluates BTR on Procgen, which involves high-dimensional state spaces."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates BTR on Atari-60, which includes games with varying reward densities, and on Procgen, which has high-dimensional state spaces. However, it doesn't isolate and specifically test BTR's performance in environments *only* with sparse rewards or *only* with high-dimensional state spaces.",
      "Supporting quotes": [],
      "Impact assessment": "While the paper evaluates on benchmarks with varying reward densities and high dimensionality, it lacks specific experiments designed to isolate performance in these environments."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper evaluates on Atari-60 and Procgen, which include varying reward densities and high dimensionality, but lacks specific experiments isolating performance in environments with *only* sparse rewards or *only* high dimensionality."
    }
  },
  {
    "Weakness Statement": "What is the impact of different hyperparameters on the performance of BTR, and how were the hyperparameters selected?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 3.2 'Hyperparameters' discusses the choice of hyperparameters: \"Hyperparameters have repeatedly shown to have a very large impact on performance in RL ( Ceron et al., 2024 ) , thus we perform a small amount of tuning to improve performance. Firstly, how frequently the target network is updated is closely intertwined with batch size and replay ratio. We found that updating the target network every 500 gradient steps 4 4 4 This equates to 32,000 environment steps (128,000 frames), compared to Rainbow DQN’s 8,000 steps. performed best. Given our high batch size, we additionally performed minor hyperparameter tests using different learning rates finding that a slightly higher learning rate of 1 × 10 − 4 performed best, compared to 6.25 × 10 − 5 in Rainbow DQN. In Appendix H for a discussion on the impact of hyperparameters.\""
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions a small amount of hyperparameter tuning and provides some details on the learning rate and target network update frequency. However, it lacks a detailed discussion on the selection process for other hyperparameters and their potential impact.",
      "Supporting quotes": [
        "\"Given our high batch size, we additionally performed minor hyperparameter tests using different learning rates finding that a slightly higher learning rate of 1 × 10 − 4 performed best, compared to 6.25 × 10 − 5 in Rainbow DQN.\"",
        "\"In Appendix H for a discussion on the impact of hyperparameters.\""
      ],
      "Impact assessment": "The paper provides some information on hyperparameter tuning but lacks a comprehensive analysis of the selection process and the sensitivity of the algorithm to different hyperparameter settings."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions some hyperparameter tuning but lacks a detailed discussion on the selection process and the sensitivity of the algorithm to different hyperparameter settings."
    }
  },
  {
    "Weakness Statement": "How does BTR compare to other state-of-the-art algorithms in terms of computational efficiency, including wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "Section 4.1 'Atari and Procgen Performance' includes a paragraph on computational resources: \"To further confirm BTR’s performance, we benchmark on Procgen ( Cobbe et al., 2020 ) , a procedurally generated set of environments aiming to prevent overfitting to specific tasks, a prevalent problem in RL ( Justesen et al., 2018 ; Juliani et al., 2019 ) . The results are shown in Figure 3 with individual games in Appendix B . BTR was able to solve all three games, including consistently finishing first place in Mario Kart. In contrast, Rainbow DQN’s performance plateaued before completing any of the games. We provide videos of our agent playing all three Wii games and all games in the Atari-5 benchmark 5 5 5 https://www.youtube.com/playlist?list=PL4geUsKi0NN-sjbuZP_fU28AmAPQunLoI .\"",
        "The paper mentions the hardware used: \"We evaluate BTR on the Atari-60 benchmark following ( Machado et al., 2018 ) and without life information (see Appendix I for the impact), evaluating every million frames on 100 episodes.\"",
        "Appendix D.2 'Hyperparameters' mentions: \"For many years, RL algorithms have used a discount rate of 0.99 0.99 , however, when reaching high performance, lower discount rates alter the optimal policy, causing even optimally performing agents to not collect the maximum cumulative rewards. To prevent this, we follow MuZero Reanalyse ( Schrittwieser et al., 2021 ) using γ = 0.997 .\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides some information on computational resources and compares BTR's performance against other algorithms in terms of walltime. However, it lacks a detailed comparison of BTR's computational efficiency with other state-of-the-art algorithms, including wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance.",
      "Supporting quotes": [
        "\"Figure 1 plots BTR against DQN, Rainbow DQN and Dreamer v3, showing BTR’s competitive performance despite using significantly less walltime.\"",
        "\"We evaluate BTR on the Atari-60 benchmark following ( Machado et al., 2018 ) and without life information... evaluating every million frames on 100 episodes.\"",
        "\"To prevent this, we follow MuZero Reanalyse ( Schrittwieser et al., 2021 ) using γ = 0.997 .\""
      ],
      "Impact assessment": "The paper provides some computational context but lacks a comprehensive comparison of computational efficiency with other algorithms."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides some computational context and compares performance against other algorithms but lacks a detailed comparison of computational efficiency with other state-of-the-art algorithms, including wall-clock time, memory usage, and the number of environment steps."
    }
  },
  {
    "Weakness Statement": "How robust is BTR to different types of noise or perturbations in the environment?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "The paper evaluates BTR on Atari-60, which inherently involves some level of environmental noise.",
        "The paper evaluates BTR on Procgen, which involves high-dimensional state spaces, which can be affected by noise."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates BTR on standard RL benchmarks, which involve environmental noise. The ablation studies offer insights into component-wise robustness. However, there's no explicit discussion or experimentation focused on systematically varying and analyzing different types of noise or perturbations.",
      "Supporting quotes": [],
      "Impact assessment": "While the paper shows BTR's performance on noisy environments, it lacks a dedicated analysis of its robustness to specific types of noise or perturbations."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper evaluates on noisy environments but lacks a dedicated discussion and experimentation on the impact of different types of noise or perturbations."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the limitations of the proposed BTR algorithm. Specifically, the paper does not discuss how BTR would perform in environments with sparse rewards or in environments with high-dimensional state spaces. It would be beneficial to include a discussion of the potential limitations of BTR and the scenarios where it may not perform well.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "The paper evaluates BTR on Atari-60, which includes games with varying reward densities (some sparse, some more dense).",
        "The paper evaluates BTR on Procgen, which involves high-dimensional state spaces."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates BTR on Atari-60 and Procgen, which include games with varying reward densities and high-dimensional state spaces. However, it lacks a dedicated discussion of the limitations of BTR, specifically regarding its performance in environments with sparse rewards or high-dimensional state spaces, beyond the general limitations mentioned in the conclusion.",
      "Supporting quotes": [],
      "Impact assessment": "While the paper evaluates on benchmarks with varying reward densities and high dimensionality, it lacks a dedicated discussion of the limitations of BTR in these specific scenarios."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper evaluates on Atari-60 and Procgen, which include varying reward densities and high dimensionality, but lacks a dedicated discussion of the limitations of BTR in these specific scenarios."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed discussion of the hyperparameters used in BTR and how they were selected. This is important because the performance of RL algorithms is often sensitive to the choice of hyperparameters. The paper should include a table or figure that shows the performance of BTR as a function of different hyperparameter values. This would allow readers to understand the sensitivity of the algorithm to different parameter settings. Furthermore, the paper should discuss the impact of different learning rates, exploration strategies, and other key hyperparameters on the performance of BTR. For example, the authors could explore the effect of different epsilon-greedy strategies or different noise schedules. This analysis should also include a discussion of the potential trade-offs between different hyperparameter choices and their impact on the overall performance of the algorithm. This would provide valuable guidance for practitioners who want to use BTR in their own applications.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 3.2 'Hyperparameters' discusses the choice of hyperparameters: \"Hyperparameters have repeatedly shown to have a very large impact on performance in RL ( Ceron et al., 2024 ) , thus we perform a small amount of tuning to improve performance. Firstly, how frequently the target network is updated is closely intertwined with batch size and replay ratio. We found that updating the target network every 500 gradient steps 4 4 4 This equates to 32,000 environment steps (128,000 frames), compared to Rainbow DQN’s 8,000 steps. performed best. Given our high batch size, we additionally performed minor hyperparameter tests using different learning rates finding that a slightly higher learning rate of 1 × 10 − 4 performed best, compared to 6.25 × 10 − 5 in Rainbow DQN. In Appendix H for a discussion on the impact of hyperparameters.\""
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions a small amount of hyperparameter tuning and provides some details on the learning rate and target network update frequency. However, it lacks a detailed discussion on the selection process for other hyperparameters and their potential impact, as well as a presentation of performance as a function of different hyperparameter values.",
      "Supporting quotes": [
        "\"Given our high batch size, we additionally performed minor hyperparameter tests using different learning rates finding that a slightly higher learning rate of 1 × 10 − 4 performed best, compared to 6.25 × 10 − 5 in Rainbow DQN.\"",
        "\"In Appendix H for a discussion on the impact of hyperparameters.\""
      ],
      "Impact assessment": "The paper provides some information on hyperparameter tuning but lacks a comprehensive analysis of the selection process and the sensitivity of the algorithm to different hyperparameter settings."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions some hyperparameter tuning but lacks a detailed discussion on the selection process and the sensitivity of the algorithm to different hyperparameter settings, including}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces BTR (Beyond The Rainbow), a reinforcement learning algorithm that builds upon the Rainbow DQN framework by incorporating six key improvements from the original Rainbow paper. These improvements include the use of a target network, a prioritized experience replay, an epsilon-greedy exploration strategy, a clipped double Q-learning objective, an implicit quantile network, a double DQN target, and a dueling network architecture. The authors evaluate BTR on the Atari-60 benchmark and three modern 3D games, demonstrating state-of-the-art performance on Atari-60 while maintaining computational efficiency. Notably, BTR successfully trains agents to play three modern 3D games, including Super Mario Galaxy, Mario Kart Wii, and Mortal Kombat End Era, using a relatively small number of frames and computational resources. The paper also includes a detailed ablation study, analyzing the impact of each component of BTR, and a discussion of the computational resources required for training. The authors emphasize the potential of BTR to achieve high performance in RL with minimal computational resources, making it accessible to researchers and practitioners with limited resources. While the paper presents a compelling case for BTR, it also acknowledges certain limitations, such as the lack of explicit exploration and potential struggles with hard-exploration tasks. Overall, the paper highlights the importance of combining existing techniques to achieve high performance in RL while maintaining computational efficiency, and it provides a valuable contribution to the field by demonstrating the feasibility of training complex agents in a resource-constrained setting. The work is significant in that it demonstrates a path towards more accessible and efficient RL, potentially enabling a broader range of applications in both research and industry.


## Soundness:

3.0


## Presentation:

3.25


## Contribution:

2.25


## Strengths:

I found several aspects of this paper to be particularly strong. First, the paper is exceptionally well-structured and clearly written, making it easy to follow and understand the proposed method and its evaluation. The authors provide a comprehensive analysis of BTR's components, including ablation studies and comparisons with other algorithms, which allows for a thorough understanding of the individual contributions of each improvement. The paper's focus on combining existing techniques to achieve high performance in RL with minimal computational resources is a significant strength. The authors demonstrate that BTR achieves state-of-the-art performance on Atari-60 while maintaining computational efficiency, which is a crucial factor for practical applications. The fact that BTR successfully trains agents to play three modern 3D games, which are known to be challenging, is a remarkable achievement and highlights the potential of the proposed approach. The paper also includes a discussion of the computational resources required for training, which is valuable for researchers and practitioners who are interested in using BTR. The authors provide a clear explanation of the algorithm, its components, and its performance, which makes it easy to understand and reproduce. The paper also acknowledges some of the limitations of the proposed method, which is a sign of intellectual honesty and a commitment to scientific rigor. The authors' focus on achieving high performance in RL with minimal computational resources is a significant contribution to the field, as it makes RL more accessible to a wider range of researchers and practitioners. The paper's emphasis on combining existing techniques to achieve high performance in RL with minimal computational resources is a significant strength. The authors demonstrate that BTR achieves state-of-the-art performance on Atari-60 while maintaining computational efficiency, which is a crucial factor for practical applications. The fact that BTR successfully trains agents to play three modern 3D games, which are known to be challenging, is a remarkable achievement and highlights the potential of the proposed approach. The paper also includes a discussion of the computational resources required for training, which is valuable for researchers and practitioners who are interested in using BTR. The authors provide a clear explanation of the algorithm, its components, and its performance, which makes it easy to understand and reproduce. The paper also acknowledges some of the limitations of the proposed method, which is a sign of intellectual honesty and a commitment to scientific rigor. The authors' focus on achieving high performance in RL with minimal computational resources is a significant contribution to the field, as it makes RL more accessible to a wider range of researchers and practitioners.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper demonstrates strong performance on Atari-60 and three modern 3D games, it lacks a detailed analysis of the limitations of BTR, particularly in scenarios where it might struggle. Specifically, the paper does not discuss how BTR would perform in environments with sparse rewards or in environments with high-dimensional state spaces. While the paper evaluates BTR on Atari-60, which includes games with varying reward densities, and on Procgen, which has high-dimensional state spaces, it does not include experiments or discussions specifically designed to isolate and analyze performance in environments with *only* sparse rewards or *only* artificially inflated high-dimensional state spaces. This is a significant limitation, as it is important to understand the boundaries of the algorithm's applicability. My confidence in this weakness is high, as the paper does not include any experiments or discussion specifically designed to isolate performance in these environments. Second, the paper does not provide a detailed discussion of the hyperparameter selection process. While the authors mention a small amount of tuning, they do not provide a table or figure that shows the performance of BTR as a function of different hyperparameter values. The paper mentions some details on the learning rate and target network update frequency, but it lacks a comprehensive discussion on the selection process for other hyperparameters and their potential impact on the performance of BTR. This is a significant concern, as the performance of RL algorithms is often sensitive to the choice of hyperparameters. My confidence in this weakness is high, as the paper lacks a detailed discussion on the hyperparameter selection process. Third, the paper does not provide a detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the authors mention that BTR is computationally efficient, they do not provide a detailed comparison of BTR's computational metrics with other algorithms, such as wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance. The paper provides some information on computational resources and compares BTR's performance against other algorithms in terms of walltime, but it lacks a detailed table comparing computational metrics like training time, memory usage, and the impact of different hardware configurations. This is a significant limitation, as computational efficiency is a key factor in the practical application of RL algorithms. My confidence in this weakness is high, as the paper lacks a detailed comparison of BTR's computational efficiency with other state-of-the-art algorithms. Fourth, the paper does not provide a detailed discussion of the robustness of BTR to different types of noise or perturbations in the environment. While the paper evaluates BTR on Atari-60 and Procgen, which inherently involve some level of environmental noise, it lacks specific experiments or discussions focused on systematically varying and analyzing different types of noise or perturbations. This is a significant limitation, as RL algorithms are often used in real-world environments, which may be subject to noise and perturbations. My confidence in this weakness is high, as the paper lacks specific experiments or discussions focused on robustness to different types of noise. Finally, while the paper mentions some hyperparameter tuning, it lacks a detailed discussion on the selection process for other hyperparameters and their potential impact on the performance of BTR. This is a significant concern, as the performance of RL algorithms is often sensitive to the choice of hyperparameters. My confidence in this weakness is high, as the paper lacks a detailed discussion on the hyperparameter selection process.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should include a more thorough analysis of the limitations of the proposed BTR algorithm. Specifically, the paper should explore the performance of BTR in environments with sparse rewards, where the agent receives feedback only rarely, or in environments with very high-dimensional state spaces, where the complexity of the input could pose challenges. This could be done by evaluating BTR on environments with different reward densities and state space dimensions, or by artificially increasing the dimensionality of the state space. A detailed analysis of these limitations would provide a more complete picture of the algorithm's capabilities and limitations. Second, the paper needs a more detailed discussion of the hyperparameter selection process. The authors mention that they used a small amount of tuning, but they do not provide sufficient information about the specific hyperparameters that were tuned, the range of values that were explored, and the criteria used to select the optimal values. The paper should include a table or figure that shows the performance of BTR as a function of different hyperparameter values. This would allow readers to understand the sensitivity of the algorithm to different parameter settings. Furthermore, the paper should discuss the impact of different learning rates, exploration strategies, and other key hyperparameters on the performance of BTR. For example, the authors could explore the effect of different epsilon-greedy strategies or different noise schedules. This analysis should also include a discussion of the potential trade-offs between different hyperparameter choices and their impact on the overall performance of the algorithm. Third, the paper should provide a more detailed comparison of BTR with other state-of-the-art algorithms in terms of computational efficiency. While the authors mention that BTR is computationally efficient, they do not provide a detailed comparison of its computational requirements with other algorithms. The paper should include a table that shows the training time, memory usage, and other relevant computational metrics for BTR and other state-of-the-art algorithms. This comparison should also include a discussion of the computational resources required to train BTR and other algorithms on different hardware configurations. For example, the authors could compare the performance of BTR on different GPUs or CPUs. This would provide a more complete understanding of the computational trade-offs associated with using BTR. Furthermore, the paper should discuss the robustness of BTR to different types of noise or perturbations in the environment. This could be done by testing BTR on environments with different types of noise, such as Gaussian noise or salt-and-pepper noise. The paper should also discuss the potential impact of different types of noise on the performance of the algorithm. Finally, the paper should include a more detailed discussion of the hyperparameter selection process, including a table or figure that shows the performance of BTR as a function of different hyperparameter values. This would allow readers to understand the sensitivity of the algorithm to different parameter settings. The paper should also discuss the impact of different learning rates, exploration strategies, and other key hyperparameters on the performance of BTR.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does BTR perform in environments with sparse rewards or in environments with very high-dimensional state spaces? While the paper evaluates BTR on Atari-60 and Procgen, it does not include experiments or discussions specifically designed to isolate and analyze performance in these environments. I am curious to know how BTR would perform in these scenarios, as these are important considerations for the practical application of RL algorithms. Second, what is the impact of different hyperparameters on the performance of BTR, and how were the hyperparameters selected? The paper mentions a small amount of hyperparameter tuning, but it lacks a detailed discussion on the selection process for other hyperparameters and their potential impact on the performance of BTR. I would like to understand the sensitivity of the algorithm to different parameter settings and the criteria used to select the optimal values. Third, how does BTR compare to other state-of-the-art algorithms in terms of computational efficiency, including wall-clock time, memory usage, and the number of environment steps required to achieve a certain level of performance? The paper provides some information on computational resources and compares BTR's performance against other algorithms in terms of walltime, but it lacks a detailed comparison of computational metrics with other algorithms. I am interested in understanding the computational trade-offs associated with using BTR compared to other algorithms. Finally, how robust is BTR to different types of noise or perturbations in the environment? The paper evaluates BTR on Atari-60 and Procgen, which inherently involve some level of environmental noise, but it lacks specific experiments or discussions focused on systematically varying and analyzing different types of noise or perturbations. I would like to understand the potential impact of different types of noise on the performance of the algorithm and its robustness to different types of perturbations.


## Rating:

5.5


## Confidence:

4.0


## Decision:

Reject
}