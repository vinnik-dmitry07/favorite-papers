# Review

## Summary
This paper proposes a novel framework called Chord, which harmonizes supervised fine-tuning (SFT) and reinforcement learning (RL) through a dynamically weighted auxiliary loss. The framework aims to address the challenges of disrupting established response patterns and overfitting to expert data when integrating SFT and RL. Chord employs a global coefficient to control the influence of expert data and a token-wise weighting function to promote on-policy exploration and mitigate disruption from off-policy data. The authors conduct extensive experiments on various practical tasks, providing empirical evidence of Chord's effectiveness.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. Chord reframes SFT as a dynamically weighted auxiliary objective within the on-policy RL process, providing a novel perspective on integrating SFT and RL.
2. Chord employs a dual-control mechanism, including a global coefficient and a token-wise weighting function, allowing for fine-grained control of the influence of off-policy expert data.
3. The authors provide extensive experimental results demonstrating Chord's superiority over traditional SFT-then-RL paradigm and other baseline methods.

## Weaknesses
1. The performance of Chord depends on the careful tuning of the global coefficient and the token-wise weighting function, which may require additional effort and expertise.
2. The experiments are conducted on specific tasks and datasets, and it is unclear how well Chord generalizes to other domains or tasks outside of the tested scope.

## Questions
1. How does Chord perform on tasks that are significantly different from the tested math reasoning and tool-use tasks?
2. How sensitive is Chord to the choice of hyperparameters, especially the global coefficient and the token-wise weighting function?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4