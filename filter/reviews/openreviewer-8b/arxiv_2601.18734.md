# Review

## Summary
This paper proposes a new post-training algorithm for reasoning tasks. The algorithm, OPSD, uses the same model as both teacher and student. The student generates a response, which the teacher evaluates by conditioning on the ground truth answer. The student is then trained to match the teacher’s distribution using a KL divergence loss. The authors demonstrate that this method outperforms both SFT and RL approaches on three math reasoning benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. 
- The proposed method is simple and intuitive. 
- The experiments are well-executed and the results are presented clearly. 
- The authors conduct thorough ablations to justify their design choices.

## Weaknesses
- The proposed method is only evaluated on Qwen models. It would be interesting to see if the results hold for other model families. 
- The authors only use a single dataset (OpenThoughts) to train the models. It would be interesting to see if the results hold for other datasets as well. 
- The authors do not provide error bars in their results.

## Questions
- Do you have any hypotheses as to why the performance of SFT degrades in Table 2? 
- Have you tried using the teacher model from the middle of training as the fixed teacher? Do you think this would improve performance? 
- Have you tried using a weaker model as the teacher (e.g., the initial student policy)?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4