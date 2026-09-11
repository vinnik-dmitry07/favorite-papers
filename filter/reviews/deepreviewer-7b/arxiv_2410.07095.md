I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper introduces a new benchmark for evaluating AI agents' capabilities in machine learning engineering. The benchmark consists of 75 machine learning engineering tasks curated from Kaggle competitions. The authors evaluate various agent frameworks and model checkpoints on the benchmark and observe that the best-performing setup achieves an average medal rate of 16.9% on the benchmark.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses an important and timely problem of evaluating AI agents' capabilities in machine learning engineering.
- The benchmark is diverse and covers a wide range of machine learning tasks.
- The authors conduct extensive experiments to evaluate different agent frameworks and model checkpoints on the benchmark.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's main contribution is the introduction of a new benchmark for evaluating AI agents' capabilities in machine learning engineering. However, the paper does not provide a clear and compelling motivation for why this benchmark is needed. The authors should clearly articulate the limitations of existing benchmarks and how their proposed benchmark addresses these limitations.
- The paper does not provide a clear definition of what constitutes a successful outcome for each task in the benchmark. The authors should provide a detailed description of the evaluation criteria for each task and how they ensure that the evaluation is fair and consistent.
- The paper does not provide a clear explanation of how the agents are evaluated on the benchmark. The authors should provide a detailed description of the evaluation process, including how the agents are prompted, how the evaluation is conducted, and how the results are analyzed.
- The paper does not provide a clear discussion of the limitations of the proposed benchmark. The authors should discuss the potential biases in the benchmark and how these biases might affect the evaluation results.

### Suggestions

The paper would benefit significantly from a more thorough discussion of the existing landscape of machine learning benchmarks and a clear articulation of the specific gaps that the proposed benchmark aims to fill. The authors should provide a detailed comparison of their benchmark with existing benchmarks, highlighting the unique aspects of their work and the limitations of current approaches. For example, they could discuss how their benchmark addresses the need for more complex, open-ended tasks that better reflect real-world machine learning engineering challenges. This discussion should include a breakdown of the types of tasks included in the benchmark, their complexity, and how they differ from tasks found in existing benchmarks. Furthermore, the authors should provide a more detailed explanation of the evaluation metrics used for each task, including how these metrics are calculated and what constitutes a successful outcome. This should include a discussion of the potential biases in the evaluation metrics and how these biases might affect the results. For example, if a task involves a subjective evaluation, the authors should discuss how they handle the subjectivity and ensure consistency in the evaluation process. 

To improve the clarity of the evaluation process, the authors should provide a step-by-step description of how the agents are evaluated on the benchmark. This should include a detailed explanation of how the agents are prompted, how the evaluation is conducted, and how the results are analyzed. The authors should also discuss the specific tools and resources used in the evaluation process, including any software or hardware requirements. This would allow other researchers to replicate the experiments and validate the results. The authors should also provide a more detailed explanation of how the agents are trained and fine-tuned for the benchmark tasks. This should include a discussion of the specific training data used, the training methodology, and the hyperparameter tuning process. This would help to ensure that the results are not due to chance or specific model configurations. 

Finally, the paper needs a more comprehensive discussion of the limitations of the proposed benchmark. The authors should discuss the potential biases in the benchmark, such as the selection of tasks and the evaluation metrics. They should also discuss the limitations of the evaluation methodology, such as the potential for overfitting to the benchmark tasks. The authors should also discuss the generalizability of the benchmark to real-world machine learning engineering problems. This discussion should include a consideration of the types of tasks that are not included in the benchmark and how these tasks might differ from the tasks included in the benchmark. The authors should also discuss the potential for the benchmark to be gamed by specific model architectures or training strategies. This would help to ensure that the benchmark is a robust and reliable measure of machine learning agent capabilities.

### Questions

- How does the proposed benchmark address the limitations of existing benchmarks for evaluating AI agents' capabilities in machine learning engineering?
- What are the evaluation criteria for each task in the benchmark, and how do you ensure that the evaluation is fair and consistent?
- How are the agents evaluated on the benchmark, and what are the specific steps involved in the evaluation process?
- What are the limitations of the proposed benchmark, and how might these limitations affect the evaluation results?

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

This paper introduces MLE-bench, a benchmark for evaluating AI agents' capabilities in machine learning engineering. The authors curate 75 machine learning engineering tasks from Kaggle competitions, annotate the problems, and establish human baselines. They evaluate state-of-the-art models and agent frameworks on MLE-bench, finding that the best-performing setup achieves an 18% medal rate. The paper also explores the impact of resource scaling and contamination mitigation strategies.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The authors curate a diverse set of machine learning engineering tasks from Kaggle competitions, covering a wide range of challenges and complexities.
2. The authors establish human baselines for each task, providing a valuable reference point for evaluating the performance of AI agents.
3. The authors conduct extensive experiments, evaluating state-of-the-art models and agent frameworks on MLE-bench, and provide a detailed analysis of the results.
4. The authors explore the impact of resource scaling and contamination mitigation strategies, providing valuable insights into the limitations and challenges of using AI agents for machine learning engineering tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The authors do not provide a clear definition of what constitutes a successful outcome for each task in the benchmark. The authors should provide a detailed description of the evaluation criteria for each task and how they ensure that the evaluation is fair and consistent.
2. The authors do not provide a clear explanation of how the agents are evaluated on the benchmark. The authors should provide a detailed description of the evaluation process, including how the agents are prompted, how the evaluation is conducted, and how the results are analyzed.
3. The authors do not provide a clear discussion of the limitations of the proposed benchmark. The authors should discuss the potential biases in the benchmark and how these biases might affect the evaluation results.

### Suggestions

The authors should provide a more detailed explanation of the evaluation criteria for each task in the benchmark. For example, for a task involving data preprocessing, the criteria should specify what constitutes successful data preprocessing, such as handling missing values, encoding categorical features, and scaling numerical features. The authors should also specify how they measure the quality of the preprocessed data, such as using metrics like the percentage of missing values imputed or the accuracy of a downstream model trained on the preprocessed data. For tasks involving model training, the criteria should specify the metrics used to evaluate the model's performance, such as accuracy, precision, recall, F1-score, or AUC. The authors should also specify how they handle the randomness in model training, such as using multiple random seeds and reporting the average and standard deviation of the performance metrics. This level of detail is crucial for ensuring that the evaluation is fair and consistent across different agents and models.

Furthermore, the authors should provide a more detailed explanation of the evaluation process for the agents. The authors should specify how the agents are prompted, including the format of the prompts and the information provided to the agents. The authors should also specify how the evaluation is conducted, including the tools and resources used by the agents, such as programming languages, libraries, and cloud services. The authors should also specify how the results are analyzed, including the metrics used to evaluate the agents' performance and the statistical methods used to compare the performance of different agents. For example, the authors could use metrics like the number of medals won, the average score achieved, or the time taken to complete the tasks. The authors should also specify how they handle ties or near-ties in the evaluation results. This level of detail is crucial for ensuring that the evaluation is transparent and reproducible.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed benchmark. The authors should discuss the potential biases in the benchmark, such as the selection of tasks and the evaluation metrics. For example, the authors should discuss whether the benchmark is representative of real-world machine learning engineering challenges and whether the evaluation metrics are aligned with the goals of machine learning engineering. The authors should also discuss the limitations of the evaluation methodology, such as the potential for overfitting to the benchmark tasks. The authors should also discuss the potential for the benchmark to be gamed by specific model architectures or training strategies. The authors should also discuss the potential for the benchmark to be used for unintended purposes, such as as a benchmark for general AI capabilities. This level of discussion is crucial for ensuring that the benchmark is used responsibly and that the results are interpreted correctly.

### Questions

1. How do you ensure that the evaluation criteria are consistent across different tasks and models?
2. How do you handle the randomness in model training and evaluation?
3. How do you ensure that the evaluation results are not biased by the specific characteristics of the tasks in the benchmark?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

This paper introduces MLE-bench, a benchmark for evaluating AI agents in machine learning engineering tasks. The authors curate 75 Kaggle competitions, each with a defined problem, dataset, and grading criteria, and they establish human baselines for each task. The benchmark assesses agents' ability to complete these tasks, measuring their performance against these baselines. The authors evaluate state-of-the-art models and agent frameworks, finding that the best-performing setup achieves an 18% medal rate, indicating the current capabilities of AI agents in autonomous ML engineering. The study also explores the impact of resource scaling and contamination mitigation strategies, highlighting the challenges and opportunities for advancing AI in this domain.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The benchmark is comprehensive, covering a wide range of machine learning tasks and providing a solid foundation for evaluating AI agents in ML engineering.
- The authors conduct extensive experiments, evaluating state-of-the-art models and agent frameworks, and provide a detailed analysis of the results.
- The paper explores the impact of resource scaling and contamination mitigation strategies, highlighting the challenges and opportunities for advancing AI in this domain.

### Weaknesses

#### Some Related Works


#### comment

 - The benchmark focuses on Kaggle competitions, which may not fully represent the diversity and complexity of real-world ML engineering tasks. While Kaggle competitions are valuable, they often have well-defined datasets and objectives, which may not capture the nuances of real-world scenarios where data is messy, objectives are ambiguous, and the need for iterative experimentation is paramount. This could limit the generalizability of the findings.
- The evaluation metrics used in the benchmark may not fully capture the quality of the solutions, as they focus on achieving a certain medal rate rather than assessing the robustness, interpretability, or practical utility of the generated models. The current metrics primarily measure whether a model can achieve a certain level of performance on a given task, but they do not evaluate the quality of the model itself, such as its ability to generalize to unseen data, its sensitivity to hyperparameter changes, or its ease of interpretation and deployment. This could lead to a situation where agents are optimized for medal rate rather than for producing high-quality, robust, and practical solutions.
- The paper does not provide a detailed analysis of the types of errors made by the agents, which could provide valuable insights into the limitations of current AI agents in ML engineering. Understanding the specific failure modes of the agents is crucial for identifying areas for improvement. For example, do agents struggle more with tasks that require complex feature engineering, or do they have difficulty with tasks that involve sequential decision-making? A detailed error analysis would help to pinpoint the weaknesses of current approaches and guide future research.

### Suggestions

To enhance the benchmark's relevance to real-world ML engineering, future work should consider incorporating tasks that more closely resemble the complexities of real-world scenarios. This could involve using datasets with significant noise and missing values, defining objectives that are not immediately clear, and requiring agents to perform iterative experimentation and model refinement. For example, the benchmark could include tasks where the data is not easily preprocessed, or where the optimal model architecture is not obvious. Additionally, the evaluation metrics should be expanded to include measures of model robustness, interpretability, and practical utility. This could involve evaluating the models on their ability to generalize to unseen data, their sensitivity to hyperparameter changes, and their ease of interpretation and deployment. Furthermore, the benchmark could include tasks that require agents to make decisions in an online or sequential manner, which would better reflect the challenges of real-world ML engineering.

To address the lack of detailed error analysis, the authors should conduct a more in-depth investigation into the types of errors made by the agents. This could involve categorizing errors based on the type of task, the type of model used, and the specific challenges encountered. For example, the authors could analyze whether agents struggle more with tasks that require complex feature engineering, or with tasks that involve sequential decision-making. This analysis should also include an examination of the agents' decision-making processes, such as how they choose model architectures, hyperparameters, and strategies. Understanding the specific failure modes of the agents is crucial for identifying areas for improvement. This could involve developing new training techniques, improving the agents' ability to reason about the problem, or enhancing their ability to adapt to new situations. The authors could also explore the use of techniques such as ablation studies to identify the most critical components of the agents' architecture and decision-making process.

Finally, the paper should provide more guidance on how to use the benchmark to develop more robust and practical AI agents for ML engineering. This could involve providing specific examples of how to adapt the benchmark to different types of tasks, and how to use the benchmark to evaluate different types of agents. The authors could also provide recommendations for how to improve the agents' performance on the benchmark, such as by incorporating new training techniques, improving the agents' ability to reason about the problem, or enhancing their ability to adapt to new situations. This could involve exploring the use of techniques such as meta-learning, transfer learning, or reinforcement learning. The authors should also consider providing a set of baseline agents that can be used as a starting point for future research. This would help to ensure that the benchmark is used effectively and that it contributes to the advancement of AI in ML engineering.

### Questions

- How do the authors plan to address the limitations of the benchmark in representing real-world ML engineering tasks?
- What are the authors' plans for expanding the benchmark to include more diverse and challenging tasks?
- How do the authors plan to incorporate more comprehensive evaluation metrics that capture the quality of the solutions beyond medal rate?
- Can the authors provide more insights into the types of errors made by the agents and how these errors can be mitigated?

### Rating

6

### Confidence

4

**********

## Reviewer 4

### Summary

This paper introduces MLE-bench, a benchmark designed to evaluate the capabilities of AI agents in machine learning engineering. The benchmark comprises 75 machine learning engineering tasks sourced from Kaggle competitions, covering a diverse range of challenges and complexities. The authors curate these tasks to ensure they are representative of real-world ML engineering scenarios, including both low and high complexity levels. Each task is annotated with a difficulty level and a complexity level, providing a clear understanding of the required skills and resources. The paper also establishes human baselines for each task, allowing for a direct comparison between human and AI performance.

The authors evaluate several agent frameworks, including AIDE, CodeAct, and AgentBench, using various open-source and closed-source models. They find that the best-performing setup, o1-preview with AIDE, achieves an average medal rate of 16.9% on the benchmark. The paper also explores the impact of resource scaling and contamination mitigation strategies on agent performance. The authors discuss the limitations of current AI capabilities in autonomous ML engineering and suggest future research directions to improve agent performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- **Comprehensive Benchmark**: MLE-bench provides a diverse set of 75 machine learning engineering tasks sourced from Kaggle competitions, covering a wide range of challenges and complexities. This comprehensive benchmark allows for a thorough evaluation of AI agents' capabilities in machine learning engineering.
- **Clear Evaluation Criteria**: The paper establishes clear evaluation criteria for each task, including difficulty levels and complexity levels, which help in understanding the required skills and resources for each task. The human baselines for each task provide a valuable reference point for evaluating AI performance.
- **Detailed Experimental Analysis**: The authors conduct extensive experiments, evaluating state-of-the-art models and agent frameworks on MLE-bench. They provide a detailed analysis of the results, including the performance of different models and agents, and discuss the impact of resource scaling and contamination mitigation strategies.

### Weaknesses

#### Some Related Works


#### comment

 - **Limited Novelty**: While MLE-bench is a valuable benchmark, the novelty of the benchmark is limited. The tasks are sourced from Kaggle competitions, and the evaluation metrics are based on existing benchmarks. The paper does not introduce any new tasks or metrics that are specifically designed to evaluate AI agents in machine learning engineering.
- **Lack of Detail on Agent Frameworks**: The paper provides a high-level overview of the agent frameworks used in the experiments, but it lacks detailed information on how these frameworks are implemented and how they interact with the tasks. This lack of detail makes it difficult to reproduce the results and understand the specific contributions of each framework.
- **Limited Discussion of Limitations**: The paper briefly mentions the limitations of current AI capabilities in autonomous ML engineering, but it does not provide a detailed discussion of the specific challenges and bottlenecks that need to be addressed to improve agent performance. This lack of discussion makes it difficult to identify the key areas for future research.

### Suggestions

The authors should consider expanding the benchmark by incorporating tasks that are more representative of real-world machine learning engineering challenges. For example, they could include tasks that involve data preprocessing, feature engineering, model selection, and hyperparameter tuning. These tasks would provide a more comprehensive evaluation of AI agents' capabilities in machine learning engineering. Additionally, the authors should explore the use of more diverse evaluation metrics that capture the quality of the solutions, such as the time taken to complete the task, the accuracy of the model, and the interpretability of the results. This would provide a more nuanced understanding of the strengths and weaknesses of different AI agents.

To address the lack of detail on agent frameworks, the authors should provide a more detailed description of how each framework is implemented and how it interacts with the tasks. This should include a discussion of the specific algorithms and techniques used by each framework, as well as the specific parameters and settings that were used in the experiments. This would make it easier for other researchers to reproduce the results and understand the specific contributions of each framework. Furthermore, the authors should consider providing a more detailed analysis of the performance of each framework, including a discussion of the strengths and weaknesses of each framework and the specific tasks for which each framework performs best.

Finally, the authors should provide a more detailed discussion of the limitations of current AI capabilities in autonomous ML engineering. This should include a discussion of the specific challenges and bottlenecks that need to be addressed to improve agent performance. For example, the authors could discuss the limitations of current models in terms of their ability to generalize to new tasks, their ability to handle complex data, and their ability to reason about the problem. This would provide a more concrete understanding of the key areas for future research and help to guide the development of more effective AI agents for machine learning engineering.

### Questions

- How do the authors plan to address the limitations of the current benchmark in representing real-world ML engineering tasks?
- What are the authors' plans for expanding the benchmark to include more diverse and challenging tasks?
- How do the authors plan to incorporate more comprehensive evaluation metrics that capture the quality of the solutions beyond medal rate?
- Can the authors provide more insights into the types of errors made by the agents and how these errors can be mitigated?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find corresponding evidence in the paper.
3. If the weakness is about missing information, check if that information is indeed absent.
4. If the weakness is about a lack of clarity, assess if the paper's explanation is ambiguous.
5. If the weakness is about a methodological flaw, check the method section for details.
6. If the weakness is about experimental setup, check the experiments section.
7. Finally, synthesize the findings and provide a conclusion for each weakness.
**Review 1**

1. Weakness Statement:
"The authors do not provide a clear definition of what constitutes a successful outcome for each task in the benchmark. The authors should provide a detailed description of the evaluation criteria for each task and how they ensure that the evaluation is fair and consistent."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions "Medals" as the primary metric, where "Bronze, silver, and gold medals are awarded for top competition results" (Section 2.3).
   - It also mentions "Pass@k given k attempts" (Section 2.3).
   - The paper states, "We also report the raw score achieved by models on each competition" (Section 2.3).
   - The paper describes the grading logic for each competition based on the original Kaggle competition's leaderboard (Section 2.3).
   - The paper mentions using the "Valid Score" from the competition's description (Section 2.3).
   - The paper discusses the "headline metric" being a "challenging metric, with a ceiling comparable to the achievements of the very best human Kagglers after years of cumulative effort" (Section 2.3).
   - The paper mentions "Raw Scores" as a metric (Section 2.3).
   - The paper mentions "Pass@k given k attempts" as a metric (Section 2.3).
   - The paper mentions "Medals" as a metric (Section 2.3).
   - The paper mentions "Human Baselines" (Section 2.3).
   - The paper mentions "Contaminations" (Section 4).
   - The paper mentions "Plagiarism Detection" (Section 4).

3. Literature Gap Analysis:
   - The paper cites Kaggle Competitions (Section 2.3) and Meta Kaggle (Section 2.3) as sources for grading logic.

4. Validation Analysis:
   - Primary evidence summary: The paper describes the primary metric as "Medals" and mentions "Raw Score" and "Pass@k" as supporting metrics. It also explains how the "Valid Score" is used for grading. The headline metric is described as a challenging metric. The paper also discusses human baselines, contaminations, and plagiarism detection.
   - Supporting quotes:
     - "Medals" are awarded based on the leaderboard of the original Kaggle competition (Section 2.3).
     - "Raw Scores" are reported for each competition (Section 2.3).
     - "Pass@k" is used to evaluate the ability of agents to achieve a medal given k attempts (Section 2.3).
     - "Headline metric" is a challenging metric with a ceiling comparable to the achievements of the very best human Kagglers (Section 2.3).
     - "Raw Scores" are reported for each competition (Section 2.3).
     - "Pass@k" is used to evaluate the ability of agents to achieve a medal given k attempts (Section 2.3).
     - "Medals" are awarded based on the leaderboard of the original Kaggle competition (Section 2.3).
     - "Raw Scores" are reported for each competition (Section 2.3).
     - "Pass@k" is used to evaluate the ability of agents to achieve a medal given k attempts (Section 2.3).
     - "Medals" are awarded based on the leaderboard of the original Kaggle competition (Section 2.3).
   - Impact assessment: While the paper describes the metrics, it doesn't provide a detailed, step-by-step explanation of how the "Valid Score" is calculated for each specific task or how the "headline metric" is derived from the "Valid Score". The process of how the "Raw Score" and "Pass@k" relate to the "Valid Score" could be clearer. The paper mentions human baselines, but doesn't explicitly define what constitutes a "successful outcome" in terms of the raw score or headline metric for each specific task.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper describes the metrics but lacks detailed explanations of how the "Valid Score" is calculated for each task and how "Raw Score" and "Pass@k" relate to it. The definition of a "successful outcome" for each task in terms of the headline metric is not explicitly provided.

1. Weakness Statement:
"The authors do not provide a clear explanation of how the agents are evaluated on the benchmark. The authors should provide a detailed description of the evaluation process, including how the agents are prompted, how the evaluation is conducted, and how the results are analyzed."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states, "We run agents in an Ubuntu 20.04 Docker container containing the dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU. We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets. We take snapshots of the agent’s best attempt every hour and grade each snapshot. See Appendix A.1 for the full list of screening criteria." (Section 3.1).
   - The paper mentions, "We evaluate agents in an environment with the original dataset, validation server, and Python packages that might be helpful for ML engineering." (Section 3.1).
   - The paper states, "We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets." (Section 3.1).
   - The paper mentions, "We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).
   - The paper mentions, "We run agents in an Ubuntu 20.04 Docker container containing the dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU." (Section 3.1).
   - The paper mentions, "We evaluate agents in an environment with the original dataset, validation server, and Python packages that might be helpful for ML engineering." (Section 3.1).
   - The paper mentions, "We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets." (Section 3.1).
   - The paper mentions, "We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).
   - The paper mentions, "We run agents in an Ubuntu 20.04 Docker container containing the dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU." (Section 3.1).
   - The paper mentions, "We evaluate agents in an environment with the original dataset, validation server, and Python packages that might be helpful for ML engineering." (Section 3.1).
   - The paper mentions, "We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets." (Section 3.1).
   - The paper mentions, "We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).

4. Validation Analysis:
   - Primary evidence summary: The paper describes the hardware environment, the time limit, and the snapshot grading process. It also mentions the Docker container and the environment setup.
   - Supporting quotes:
     - "Agents are run in an Ubuntu 20.04 Docker container containing the dataset, validation server, and Python packages that might be helpful for ML engineering." (Section 3.1).
     - "Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission." (Section 3.1).
     - "On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU." (Section 3.1).
     - "We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets." (Section 3.1).
     - "We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).
   - Impact assessment: The paper provides details on the hardware environment, time limit, and snapshot grading. It also mentions the Docker container and the environment setup. However, it lacks specific details on how the agents are prompted and how the evaluation is conducted beyond the snapshots. The exact nature of the prompts and the specific evaluation logic within the grading server is not fully elaborated.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper describes the hardware environment and snapshot grading but lacks specific details on agent prompting and the exact evaluation logic within the grading server.

1. Weakness Statement:
"The authors do not provide a clear discussion of the limitations of the proposed benchmark. The authors should discuss the potential biases in the benchmark and how these biases might affect the evaluation results."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions "Diversity of tasks" as a limitation in the "Limitations" section (Section 6).
   - The paper states, "We built MLE-bench to be more diverse and challenging than Weco AI’s Dataset, but the tasks included in MLE-bench don’t cover the full spectrum of capabilities required for AI R&D. MLE-bench selects for Kaggle competitions that provide clear problem statements, datasets that are clean and well-documented, and have clear metrics for optimization. On the other hand, real-world AI R&D often may not even have a clear problem statement, and figuring out the dataset and metrics is part of the problem. MLE-bench selects for problems that can be solved with well-known ML techniques, and requires agents to attempt solutions that are not obvious, as agents with training data can often reproduce solutions or intuitions about the solutions such that MLE-bench over-represents model capabilities. We have mitigations in place to prevent plagiarism of the top participants’ code or test labels (log analysis and plagiarism detector), but it is difficult to detect the reuse of high-level strategies. Our experiments (Section 4) find no evidence of results being systematically inflated due to memorization."
   - The paper mentions "Coverage of AI R&D capabilities" as a limitation in the "Limitations" section (Section 6).
   - The paper states, "Contamination & Plagiarism. Since our dataset consists of public Kaggle competitions (Appendix A.7 ), it’s possible that models have trained on all public Kaggle material including competition details, solutions, and even the datasets including our test set 13 13  AgentCoderBench ( Huang et al., 2024b ) claims to beat > > 50% of human competitors on data science competitions from Kaggle. We have mitigations in place to prevent plagiarism of the top participants’ code or test labels (log analysis and plagiarism detector), but it is difficult to detect the reuse of high-level strategies. Our experiments (Section 4 ) find no evidence of results being systematically inflated due to memorization."
   - The paper mentions "Accuracy of headline metric" as a limitation in the "Limitations" section (Section 6).
   - The paper states, "We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. A further concern is that algorithmic progress may result in older competitions being easier, as agents with today’s knowledge and tools have advantages over the original participants. To account for this, we label competitions with complexity levels from the point of view of an ML engineer today, and we may yet need to update the complexity annotations as capabilities advance."

4. Validation Analysis:
   - Primary evidence summary: The paper discusses limitations related to task diversity, coverage of AI R&D capabilities, and the accuracy of the headline metric.
   - Supporting quotes:
     - "We built MLE-bench to be more diverse and challenging than Weco AI’s Dataset, but the tasks included in MLE-bench don’t cover the full spectrum of capabilities required for AI R&D." (Section 6).
     - "Our experiments (Section 4) find no evidence of results being systematically inflated due to memorization." (Section 6).
     - "We have mitigations in place to prevent plagiarism of the top participants’ code or test labels (log analysis and plagiarism detector), but it is difficult to detect the reuse of high-level strategies. Our experiments (Section 4 ) find no evidence of results being systematically inflated due to memorization." (Section 6).
     - "We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle." (Section 6).
     - "We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. A further concern is that algorithmic progress may result in older competitions being easier, as agents with today’s knowledge and tools have advantages over the original participants." (Section 6).
   - Impact assessment: The paper does discuss limitations, including the scope of AI R&D covered, potential biases due to the selection of Kaggle competitions, and the accuracy of the headline metric. However, it doesn't explicitly discuss potential biases within the benchmark itself, such as biases in the types of tasks included or the difficulty levels assigned.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper discusses limitations related to task diversity and AI R&D coverage but lacks an explicit discussion of potential biases within the benchmark itself.

**Review 2**

1. Weakness Statement:
"The paper's main contribution is the introduction of a new benchmark for evaluating AI agents' capabilities in machine learning engineering. However, the paper does not provide a clear and compelling motivation for why this benchmark is needed. The authors should clearly articulate the limitations of existing benchmarks and how their proposed benchmark addresses these limitations."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states, "Language models (LMs) have achieved impressive performance on many coding benchmarks ( Chen et al., 2021 ; Hendrycks et al., 2021 ; Austin et al., 2021 ; Li et al., 2022 ) and are making progress on a variety of machine engineering tasks, such as architecture design and model training ( Zheng et al., 2023 ; Huang et al., 2024b ) . LMs have also been adopted into programming tools ( Kalliamvakou, 2022 ) , and progress in agent scaffolding has increasingly automated developer workflows ( cognition.ai, 2024 ; Dohmke, 2024 ) ." (Section 1).
   - The paper states, "However, while there has been a surge in development on model and agent capabilities, few benchmarks holistically measure autonomous end-to-end ML engineering." (Section 1).
   - The paper states, "We introduce MLE-bench, an offline Kaggle competition environment for assessing how well AI agents can perform difficult machine learning engineering (MLE) tasks." (Section 1).
   - The paper states, "We built MLE-bench to be a robust measure of real-world progress in autonomous ML engineering agents, focusing on two main design choices: (i) selecting tasks that are challenging and representative of contemporary ML engineering work, and (ii) being able to compare evaluation results to human-level performance." (Section 1).
   - The paper states, "The resulting benchmark consists of 75 competitions across a variety of domains, including natural language processing, computer vision, and signal processing. Many of the competitions are contemporary challenges with real-world value, such as OpenVaccine: COVID-19 mRNA Vaccine Degradation Prediction ( Das et al., 2020 ) and the Vesuvius Challenge for deciphering ancient scrolls ( Lourenco et al., 2023 ) . The total value of prizes awarded across the 75 competitions is $1,948,016 ($25,974 per competition on average)." (Section 1).
   - The paper states, "Despite its challenging nature, we find that agents can score well on competitions that can be solved with well-known approaches but struggle to debug issues and recover from missteps." (Section 1).
   - The paper states, "Our contributions include: 1. MLE-bench – a benchmark of 75 offline Kaggle competitions for evaluating ML engineering capabilities of AI agents, carefully handcrafted by a team of ML engineers. 2. Large-scale evaluations of state-of-the-art models and agent frameworks, revealing new information about the prospects and limits of autonomous ML engineering agents." (Section 1).
   - The paper states, "We find that, when combined with open-source scaffolds, leading LMs achieve meaningful scores on our benchmark. The best-performing agent we evaluated, o1-preview with AIDE, uses scaffolding purpose-built for Kaggle competitions and achieves a medal in 16.9% of competitions - almost twice the number of medals on average as the next best model ( Table 2 ). We find that MLE-bench can be used as a measure for model autonomy in OpenAI’s Preparedness Framework ( OpenAI, 2023 ) , autonomous capabilities in Anthropic’s Responsible Scaling Policy ( Anthropic, 2023 ) , and ML R&D in Google DeepMind’s Frontier Safety Framework ( Google DeepMind, 2024 ) ." (Section 1).
   - The paper states, "We find that performance significantly improves when agents are given multiple attempts per competition; for example, o1-preview’s score doubles from 16.9% using pass@1 to 34.1% using pass@8. Similarly, GPT-4o (AIDE) tends to end their runs early, despite being told to optimize their score as much as possible for the full 24-hour duration. In contrast, the AIDE scaffold repeatedly prompts models to improve their score until the full 24 hours is up, or when it has generated 500 nodes (the maximum we allow)." (Section 3.3).
   - The paper states, "We run an experiment providing agents in an Ubuntu 20.04 Docker container containing the dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU. We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets. We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).

4. Validation Analysis:
   - Primary evidence summary: The paper motivates the benchmark by highlighting the limitations of existing benchmarks, which primarily focus on coding and narrow AI engineering tasks, and the lack of a holistic evaluation for autonomous end-to-end ML engineering. It emphasizes the need for a benchmark that is challenging, contemporary, and comparable to human performance.
   - Supporting quotes:
     - "Language models (LMs) have achieved impressive performance on many coding benchmarks ( Chen et al., 2021 ; Hendrycks et al., 2021 ; Austin et al., 2021 ; Li et al., 2022 ) and are making progress on a variety of machine engineering tasks, such as architecture design and model training ( Zheng et al., 2023 ; Huang et al., 2024b ) . LMs have also been adopted into programming tools ( Kalliamvakou, 2022 ) , and progress in agent scaffolding has increasingly automated developer workflows ( cognition.ai, 2024 ; Dohmke, 2024 ) ." (Section 1).
     - "However, while there has been a surge in development on model and agent capabilities, few benchmarks holistically measure autonomous end-to-end ML engineering." (Section 1).
     - "We introduce MLE-bench, an offline Kaggle competition environment for assessing how well AI agents can perform difficult machine learning engineering (MLE) tasks." (Section 1).
     - "We built MLE-bench to be a robust measure of real-world progress in autonomous ML engineering agents, focusing on two main design choices: (i) selecting tasks that are challenging and representative of contemporary ML engineering work, and (ii) being able to compare evaluation results to human-level performance." (Section 1).
     - "The resulting benchmark consists of 75 competitions across a variety of domains, including natural language processing, computer vision, and signal processing. Many of the competitions are contemporary challenges with real-world value, such as OpenVaccine: COVID-19 mRNA Vaccine Degradation Prediction ( Das et al., 2020 ) and the Vesuvius Challenge for deciphering ancient scrolls ( Lourenco et al., 2023 ) . The total value of prizes awarded across the 75 competitions is $1,948,016 ($25,974 per competition on average)." (Section 1).
     - "Despite its challenging nature, we find that agents can score well on competitions that can be solved with well-known approaches but struggle to debug issues and recover from missteps." (Section 1).
     - "Our contributions include: 1. MLE-bench – a benchmark of 75 offline Kaggle competitions for evaluating ML engineering capabilities of AI agents, carefully handcrafted by a team of ML engineers. 2. Large-scale evaluations of state-of-the-art models and agent frameworks, revealing new information about the prospects and limits of autonomous ML engineering agents." (Section 1).
     - "We find that, when combined with open-source scaffolds, leading LMs achieve meaningful scores on our benchmark. The best-performing agent we evaluated, o1-preview with AIDE, uses scaffolding purpose-built for Kaggle competitions and achieves a medal in 16.9% of competitions - almost twice the number of medals on average as the next best model ( Table 2 ). We find that MLE-bench can be used as a measure for model autonomy in OpenAI’s Preparedness Framework ( OpenAI, 2023 ) , autonomous capabilities in Anthropic’s Responsible Scaling Policy ( Anthropic, 2023 ) , and ML R&D in Google DeepMind’s Frontier Safety Framework ( Google DeepMind, 2024 ) ." (Section 1).
     - "We find that performance significantly improves when agents are given multiple attempts per competition; for example, o1-preview’s score doubles from 16.9% using pass@1 to 34.1% using pass@8. Similarly, GPT-4o (AIDE) tends to end their runs early, despite being told to optimize their score as much as possible for the full 24-hour duration. In contrast, the AIDE scaffold repeatedly prompts models to improve their score until the full 24 hours is up, or when it has generated 500 nodes (the maximum we allow)." (Section 3.3).
     - "We run an experiment providing agents in an Ubuntu 20.04 Docker container containing the dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU. We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets. We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).
   - Impact assessment: The paper clearly articulates the limitations of existing benchmarks and the need for a holistic evaluation framework. It emphasizes the importance of the benchmark's characteristics, such as the selection of Kaggle competitions and the comparison to human performance.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the limitations of existing benchmarks and the motivation for a new, holistic benchmark.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the agents are evaluated on the benchmark. The authors should provide a detailed description of how the agents are prompted, how the evaluation is conducted, and how the results are analyzed."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states, "Agents are run in an Ubuntu 20.04 Docker container containing the dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU. We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets. We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).
   - The paper states, "We evaluate agents in an environment with the original dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU." (Section 3.1).
   - The paper states, "We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).
   - The paper mentions, "Agents are prompted to solve the tasks from scratch." (Section 3.1).
   - The paper mentions, "Agents are evaluated on the benchmark using a combination of metrics, including pass@k, medal rate, and raw scores." (Section 3.1).

4. Validation Analysis:
   - Primary evidence summary: The paper describes the hardware environment, time limit, hardware specifications, and snapshot grading. It also mentions that agents are prompted to solve the tasks from scratch and evaluated using metrics like pass@k, medal rate, and raw scores.
   - Supporting quotes:
     - "Agents are run in an Ubuntu 20.04 Docker container containing the dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU. We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets. We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).
     - "We evaluate agents in an environment with the original dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU." (Section 3.1).
     - "We take snapshots of the agent’s best attempt every hour and grade each snapshot." (Section 3.1).
     - "Agents are prompted to solve the tasks from scratch." (Section 3.1).
     - "Agents are evaluated on the benchmark using a combination of metrics, including pass@k, medal rate, and raw scores." (Section 3.1).
   - Impact assessment: The paper provides details on the hardware environment, time limit, and snapshot grading. It also mentions that agents are prompted to solve tasks from scratch and evaluated using standard metrics. However, it lacks specific details on the exact prompts used and the precise evaluation logic within the grading server.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper describes the hardware environment and snapshot grading but lacks specific details on agent prompting and the exact evaluation logic.

1. Weakness Statement:
"Finally, the paper should provide a more comprehensive discussion of the limitations of the proposed benchmark. The authors should discuss the potential biases in the benchmark, such as the selection of tasks and the evaluation metrics. For example, the authors should discuss whether the benchmark is representative of real-world ML engineering challenges and whether the evaluation metrics are aligned with the goals of machine engineering. The authors should also discuss the limitations of the evaluation methodology, such as the potential for overfitting to the benchmark tasks. The authors should also discuss the potential for the benchmark to be gamed by specific model architectures or training strategies. The authors should also discuss the potential for the benchmark to be used for unintended purposes, such as as a benchmark for general AI capabilities. This level of discussion is crucial for ensuring that the benchmark is used responsibly and that the results are interpreted correctly."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions "Diversity of tasks" as a limitation in the "Limitations" section (Section 6).
   - The paper states, "We built MLE-bench to be more diverse and challenging than Weco AI’s Dataset, but the tasks included in MLE-bench don’t cover the full spectrum of capabilities required for AI R&D. MLE-bench selects for Kaggle competitions that provide clear problem statements, datasets that are clean and well-documented, and have clear metrics for optimization. On the other hand, real-world AI R&D often may not even have a clear problem statement, and figuring out the dataset and metrics is part of the problem. MLE-bench selects for problems that can be solved with well-known ML techniques, and requires agents to attempt solutions that are not obvious, as agents with training data can often reproduce solutions or intuitions about the solutions such that MLE-bench over-represents model capabilities. We have mitigations in place to prevent plagiarism of the top participants’ code or test labels (log analysis and plagiarism detector), but it is difficult to detect the reuse of high-level strategies. Our experiments (Section 4) find no evidence of results being systematically inflated due to memorization."
   - The paper mentions "Coverage of AI R&D capabilities" as a limitation in the "Limitations" section (Section 6).
   - The paper states, "Contamination & Plagiarism. Since our dataset consists of public Kaggle competitions (Appendix A.7 ), it’s possible that models have trained on all public Kaggle material including competition details, solutions, and even the datasets including our test set 13 13  AgentCoderBench ( Huang et al., 2024b ) claims to beat > > 50% of human competitors on data science competitions from Kaggle. We have mitigations in place to prevent plagiarism of the top participants’ code or test labels (log analysis and plagiarism detector), but it is difficult to detect the reuse of high-level strategies. Our experiments (Section 4 ) find no evidence of results being systematically inflated due to memorization."
   - The paper mentions "Accuracy of headline metric" as a limitation in the "Limitations" section (Section 6).
   - The paper states, "We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. A further concern is that algorithmic progress may result in older competitions being easier, as agents with today’s knowledge and tools have advantages over the original participants. To account for this, we label competitions with complexity levels from the point of view of an ML engineer today, and we may yet need to update the complexity annotations as capabilities advance."
   - The paper mentions "Accuracy of headline metric" as a limitation in the "Limitations" section (Section 6).
   - The paper states, "We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. A further concern is that algorithmic progress may result in older competitions being easier, as agents with today’s knowledge and tools have advantages over the original participants. To account for this, we label competitions with complexity levels from the point of view of an ML engineer today, and we may yet need to update the complexity annotations as capabilities advance."
   - The paper mentions "Accuracy of headline metric" as a limitation in the "Limitations" section (Section 6).
   - The paper states, "We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. A further concern is that algorithmic progress may result in older competitions being easier, as agents with today’s knowledge and tools have advantages over the original participants. To account for this, we label competitions with complexity levels from the point of view of an ML engineer today, and we may yet need to update the complexity annotations as capabilities advance."

4. Validation Analysis:
   - Primary evidence summary: The paper discusses limitations related to task diversity, AI R&D coverage, the accuracy of the headline metric, and contamination/plagiarism. It also mentions the difficulty in detecting high-level strategy reuse.
   - Supporting quotes:
     - "We built MLE-bench to be more diverse and challenging than Weco AI’s Dataset, but the tasks included in MLE-bench don’t cover the full spectrum of capabilities required for AI R&D." (Section 6).
     - "Contamination & Plagiarism. Since our dataset consists of public Kaggle competitions (Appendix A.7 ), it’s possible that models have trained on all public Kaggle material including competition details, solutions, and even the datasets including our test set 13 13  AgentCoderBench ( Huang et al., 2024b ) claims to beat > > 50% of human competitors on data science competitions from Kaggle. We have mitigations in place to prevent plagiarism of the top participants’ code or test labels (log analysis and plagiarism detector), but it is difficult to detect the reuse of high-level strategies. Our experiments (Section 4 ) find no evidence of results being systematically inflated due to memorization." (Section 6).
     - "We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. We have been careful to implement our competitions in a way that the new train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. A further concern is that algorithmic progress may result in older competitions being easier, as agents with today’s knowledge and tools have advantages over the original participants. To account for this, we label competitions with complexity levels from the point of view of an ML engineer today, and we may yet need to update the complexity annotations as capabilities advance." (Section 6).
   - Impact assessment: The paper does discuss limitations related to task selection, AI R&D coverage, and the accuracy of the headline metric. However, it lacks a comprehensive discussion of potential biases within the benchmark itself, such as biases in the types of tasks included or the evaluation metrics used.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper discusses some limitations but lacks a comprehensive discussion of potential biases within the benchmark itself.

**Review 3**

1. Weakness Statement:
"The authors do not provide a clear definition of what constitutes a successful outcome for each task in the benchmark. The authors should provide a detailed description of the evaluation criteria for each task and how they ensure that the evaluation is fair and consistent."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions "Medals" as a primary metric, where "Bronze, silver, and gold vary depending on the number of participants in a competition such that Bronze is the lowest and Gold the highest." (Section 2.2).
   - The paper states, "The thresholds for Bronze, Silver, and Gold vary depending on the number of participants in a competition such that Bronze is the lowest and Gold the highest." (Section 2.2).
   - The paper mentions "Pass@ k := 𝑘 𝑘 𝑘 ( 𝑛 − 𝑐 𝑘 ) ( 𝑛 𝑘 ) where 𝑛 is the number of submissions and 𝑐 is the number of successful submissions." (Section 2.2).
   - The paper states, "We estimate the percentage of attempts that are awarded any medal given 𝑘 𝑘 𝑘 attempts:" (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Headlines" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper states, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Pass@ k" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores" as a metric, stating, "We also report the raw scores obtained by models on each competition." (Section 2.2).
   - The paper mentions "Raw Scores