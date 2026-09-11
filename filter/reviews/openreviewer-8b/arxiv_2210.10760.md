# Review

## Summary
This paper studies the phenomenon of reward model overoptimization, where optimizing a proxy reward model leads to suboptimal performance on the actual reward. The authors conduct a series of experiments on a synthetic setup with a fixed "gold-standard" reward model and a variable proxy reward model. They find that the relationship between the gold reward and the proxy reward follows different functional forms depending on the optimization method used (reinforcement learning or best-of-n sampling). The authors also study how the relationship between the gold reward and the proxy reward changes as the number of reward model parameters, the size of the reward model dataset, and the number of policy parameters vary. The authors discuss the implications of their findings for theoretical considerations in AI alignment.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper addresses an important and timely topic in the field of reinforcement learning from human feedback, namely the overoptimization of reward models. The authors provide empirical evidence of the phenomenon of overoptimization and propose functional forms that describe the relationship between the gold reward and the proxy reward. The authors also discuss the implications of their findings for theoretical considerations in AI alignment, which is a valuable contribution to the field.

## Weaknesses
The paper has several limitations that should be addressed. First, the experiments are conducted on a synthetic setup with a fixed gold reward model, which may not fully capture the complexities of real-world scenarios. Second, the authors do not provide a comparison of their proposed functional forms with existing theoretical models of Goodhart's law or reward hacking. It would be valuable to see how well the proposed forms align with existing theoretical frameworks. Third, the authors do not provide any recommendations or guidelines for practitioners on how to avoid or mitigate overoptimization in reward models. Providing practical advice would enhance the usefulness of the paper for the community.

## Questions
1. How do the proposed functional forms compare to existing theoretical models of Goodhart's law or reward hacking?
2. What are the practical implications of the findings in terms of how to avoid or mitigate overoptimization in reward models?
3. How do the findings generalize to real-world scenarios, where the reward model may be imperfect and the feedback may be noisy?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4