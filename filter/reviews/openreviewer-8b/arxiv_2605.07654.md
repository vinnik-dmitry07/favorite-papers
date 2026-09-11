# Review

## Summary
This paper proposes a new self-consistency algorithm for LLMs. The authors observe that when the initial answer is correct, regenerating from its prefix tends to produce the same answer, but when the initial answer is incorrect, regeneration more often produces a different incorrect answer. Based on this observation, the authors propose to truncate each sample’s CoT at an intermediate point and regenerate its continuation, treating samples whose initial answer reappears as more reliable than those whose answer changes. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed method is simple but effective, and the idea is novel.
2. The experiments are well-designed and comprehensive, and the results are convincing.

## Weaknesses
1. The proposed method requires generating $K$ continuations for each of the $N$ samples, which can be time-consuming.
2. The proposed method requires more hyperparameters to tune, including the truncation fraction $\tau$ and the number of regenerations per group $K$.
3. The proposed method may not be suitable for tasks with a large answer space, such as open-question answering.

## Questions
1. How does the proposed method perform on open-ended tasks?
2. How does the proposed method compare to other self-consistency algorithms, such as [1]?

[1] Self-Consistency Improves Chain of Thought Reasoning in Language Models

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4