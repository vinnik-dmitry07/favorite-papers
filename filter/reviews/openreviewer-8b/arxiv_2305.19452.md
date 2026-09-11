# Review

## Summary
This paper introduces a model-free RL agent called BBF that achieves super-human performance on the Atari 100K benchmark. The authors conduct extensive analyses of the design choices and provide insights for future work. They also discuss updating the goalposts for sample-efficient RL research on the ALE.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments and provide insights for future work.

## Weaknesses
1. The authors should include more baseline algorithms in their comparisons. For example, the authors claim that "it has remained elusive for model-free RL agents" and "Achieving this level of performance required a larger network than the decade-old 3-layer CNN architecture". However, to the best of my knowledge, [1] achieves even better performance with a 3-layer CNN architecture. The authors should also compare with other strong baselines like [1] and [2].
2. The authors should provide more details about the network architecture. For example, what is the exact structure of the network? How many layers does it have? How many parameters are there?
3. The authors should provide more details about the experimental setup. For example, what is the value of $n$ in $R^{(n)}$? What is the value of $\gamma$? What is the target network used in the experiments?
4. The authors should provide more details about the results. For example, what are the scores of the middle 50% runs? What are the best and worst scores? How many seeds are used in the experiments?
5. The authors should provide the results of BBF on all 55 games with sticky actions in the main text instead of the appendix. It would be better to provide the results of BBF on all 55 games with sticky actions and the results of other baseline algorithms like EfficientZero and SR-SPR.
6. The authors should provide the results of BBF on the 26 games in the standard Atari setting in the main text instead of the appendix. It would be better to provide the results of BBF on the 26 games in the standard Atari setting and the results of other baseline algorithms like EfficientZero and SR-SPR.

[1] Hafner, Danijar, et al. "Mastering atari with discrete world models and prioritized experience replay." arXiv preprint arXiv:2010.02193 (2020).

[2] Kaiser, Erik, et al. "Efficient zero: A generalized decision transformer for games, markov decision processes, and partial monitoring." Advances in Neural Information Processing Systems 34 (2021): 20567-20579.

## Questions
1. What is the exact structure of the network used in BBF?
2. What are the scores of the middle 50% runs of BBF on all 55 games with sticky actions?
3. What are the best and worst scores of BBF on all 55 games with sticky actions?
4. How many seeds are used in the experiments?
5. What is the value of $n$ in $R^{(n)}$?
6. What is the value of $\gamma$?
7. What is the target network used in the experiments?
8. What are the results of BBF on all 55 games with sticky actions in the standard Atari setting?
9. What are the results of other baseline algorithms like EfficientZero and SR-SPR on all 55 games with sticky actions in the standard Atari setting?
10. What are the results of BBF on the 26 games in the standard Atari setting?
11. What are the results of other baseline algorithms like EfficientZero and SR-SPR on the 26 games in the standard Atari setting?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4