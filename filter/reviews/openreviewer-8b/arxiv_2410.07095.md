# Review

## Summary
This paper introduces MLE-bench, a benchmark for evaluating AI agents' capabilities in machine learning engineering tasks by curating 75 challenging competitions from Kaggle. The benchmark assesses agents' skills in training models, preparing datasets, and running experiments, establishing human baselines from Kaggle leaderboards. The authors evaluate several frontier language models using open-source agent scaffolds, finding that OpenAI’s o1-preview with AIDE achieves a medal (bronze, silver, or gold) in 16.9% of competitions. The paper also explores the impact of resource-scaling and pre-training contamination on agent performance.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. MLE-bench provides a novel and comprehensive evaluation framework for assessing AI agents' ML engineering capabilities, addressing a significant gap in current benchmarks.
2. The benchmark is carefully designed with challenging tasks and clear comparisons to human performance, ensuring its relevance and rigor.
3. The paper includes extensive experiments with state-of-the-art models and explores the impact of resource-scaling and contamination, offering valuable insights into agent capabilities and limitations.
4. The authors provide open-source code and detailed documentation, facilitating reproducibility and further research in this area.

## Weaknesses
1. The benchmark's reliance on Kaggle competitions may introduce limitations, such as potential contamination and the representativeness of the tasks.
2. The paper could benefit from a more detailed discussion on the implications of the results, particularly what they mean for the development of AI agents and their potential impact on scientific progress and safety.
3. The paper could provide more insights into the specific failures of agents, including examples and potential strategies for improvement.
4. The paper could include a more detailed analysis of the agent's behavior and decision-making process, including examples of successful and unsuccessful strategies employed.

## Questions
1. How do the authors plan to update the benchmark to address potential contamination issues, and what strategies will be implemented to ensure the benchmark's relevance and difficulty as AI agent capabilities advance?
2. Can the authors provide more insights into the specific failures of the agents, including examples and potential strategies for improvement?
3. How do the authors plan to enhance the benchmark to include a wider range of tasks that cover the full spectrum of capabilities required for AI R&D, including tasks that involve figuring out the dataset and metrics?
4. What are the implications of the results for the development of AI agents, and how do the authors suggest researchers address the challenges posed by agents that can autonomously perform ML engineering tasks at a high level?
5. How do the authors plan to address the limitations of the benchmark, such as the reliance on Kaggle competitions and the potential for differences between the benchmark and real-world competitions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4