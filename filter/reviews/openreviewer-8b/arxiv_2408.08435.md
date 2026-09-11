# Review

## Summary
This paper introduces Automated Design of Agentic Systems (ADAS), a new research area focused on automatically creating powerful agentic systems by inventing novel building blocks and combining them in new ways. The authors propose Meta Agent Search, an algorithm where a meta agent iteratively programs new agents based on an archive of previous discoveries, using code as the search space. They demonstrate the effectiveness of this approach across various domains, showing that the discovered agents outperform hand-designed agents and exhibit strong transferability across models and domains. The work aims to automate the design of agentic systems, potentially saving human effort and accelerating the development of more effective solutions.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- Novel research direction: The paper introduces a new research area, Automated Design of Agentic Systems (ADAS), which aims to automate the creation of powerful agentic systems. This direction has the potential to significantly impact the field of AI by reducing the manual effort required in designing and developing agents.
- Meta Agent Search Algorithm: The paper proposes Meta Agent Search, a simple yet effective algorithm that defines and searches for agents in code space. The algorithm demonstrates the ability to discover agents that outperform state-of-the-art hand-designed agents across various domains.
- Extensive experiments: The authors conduct extensive experiments across multiple domains, including ARC logic puzzle task, reading comprehension, math, and science question-answering. The results consistently show that the discovered agents outperform hand-designed agents and exhibit strong transferability across models and domains.
- Open-sourced code: The authors provide open-sourced code, facilitating reproducibility and further research in this area.

## Weaknesses
- Limited complexity of tasks: The tasks evaluated in the paper are relatively simple, focusing on single-step QA. It would be interesting to see how the approach performs on more complex tasks that require multi-step reasoning and interaction with complex environments.
- Limited exploration of search algorithms: The search algorithm used in Meta Agent Search is relatively simple and focuses on exploring interesting new designs. A more thorough exploration of different search algorithms could potentially lead to better performance.
- Lack of human evaluation: The paper relies primarily on numerical performance metrics for evaluation. Incorporating human evaluation could provide a more nuanced understanding of the agents' performance and behavior.

## Questions
- How does the performance of the discovered agents compare to state-of-the-art methods in more complex tasks that require multi-step reasoning and interaction with complex environments?
- Have you explored other search algorithms besides the one used in Meta Agent Search? How do they compare in terms of performance and efficiency?
- How do the discovered agents compare to state-of-the-art methods in terms of explainability and interpretability? Can the authors provide more insights into the decision-making process of the meta agent?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4