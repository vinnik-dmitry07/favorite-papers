# Review

## Summary
The paper proposes Promptbreeder, a system that uses LLMs to evolve prompts for solving tasks. The authors evaluate Promptbreeder on a wide range of reasoning tasks, and show that it outperforms previous methods like Chain-of-Thought and Plan-and-Solve.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The authors conducted extensive experiments on a wide range of tasks.

## Weaknesses
1. The novelty of the proposed method is limited. The idea of using LLMs to generate prompts for solving tasks has been explored in several previous works, such as [1, 2, 3]. The proposed method is similar to the Automatic Prompt Engineer (APE) [1]. The authors mentioned that "In contrast to APE, our work performs compositional task-specific initialization of mutation-prompts, subsequent online mutation of mutation-prompts, uses special mutation operators that take into account the whole population and elite history, and uses diversity-maintenance methods—all of which help avoid the problem of diminishing returns and diversity loss suffered by APE." However, these differences seem to be incremental, and the authors did not provide ablation studies to demonstrate the importance of these design choices.

2. The proposed method is not efficient. The authors mentioned that "we sample a batch of 100 Q&A pairs from the entire training set of the domain at hand" and "a generation involves forming random pairs of all individuals in the population and competing them against each other". This requires a lot of API calls to the LLM, making the method computationally expensive. The authors did not report the time and token cost of their method.

3. The proposed method is not generalizable. The authors mentioned that "Promptbreeder is general purpose in that the same system is able to adapt to many different domains". However, the method requires a set of domain-specific "thinking-styles" and a set of domain-specific initial mutation-prompts. It is unclear how to design these resources for a new domain.

4. The evaluation is not fair. The authors compared their method to Chain-of-Thought and Plan-and-Solve, but these baselines are not designed to evolve prompts. It is unclear how these baselines were implemented in the experiments. The authors should compare their method to other prompt evolution methods, such as APE [1] and EvoPrompt [4].

[1] Zhou, Denny, et al. "Automatic prompt engineer." arXiv preprint arXiv:2305.06161 (2023).

[2] Shinn, Noah, et al. "Reflexion: Language agents with verbal reinforcement learning." Advances in Neural Information Processing Systems 36 (2024).

[3] Guo, Shangmin, et al. "Large language models as optimizers." arXiv preprint arXiv:2310.02920 (2023).

[4] Guo, Shangmin, et al. "EvoPrompt: Evolutionary Prompt Optimization for Large Language Models." arXiv preprint arXiv:2405.12406 (2024).

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4