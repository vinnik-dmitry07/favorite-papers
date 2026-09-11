# Review

## Summary
This paper proposes a method to detect deception from LLMs by training a probe on a dataset of honest and deceptive responses and then evaluating it on more realistic scenarios. The authors find that probes trained on simpler datasets like Zou et al. (2023) and role-playing scenarios can generalize to more complex scenarios like the insider trading scenario from Scheurer et al. (2023) and the sandbagging scenario from Benton et al. (2024). The authors find that their probes have AUROC between 0.96 and 0.999 on their evaluation datasets, and can catch 95-99% of deceptive responses at a 1% false positive rate on neutral chat data.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. 
- The paper tackles an important problem of detecting deception from LLMs.
- The authors perform a thorough evaluation of their method on multiple datasets and compare it to multiple baselines.

## Weaknesses
- The paper does not provide much technical novelty. The authors simply train a probe on a dataset of honest and deceptive responses. 
- The paper does not provide much insight into why the probe works or doesn't work in different settings. The authors do provide some intuition in Section 4.1.1 on why the probe may be activating on responses that are not actually deceptive. However, this section could be significantly expanded on. For example, it would be helpful to see some examples of responses that the probe gets wrong and some analysis on why the probe gets these wrong. 
- The paper does not evaluate on the most realistic setting, which is deception that occurs in the context of normal conversations. The authors acknowledge this limitation in the paper.

## Questions
- Have you tried training a probe on the Roleplaying dataset and evaluating it on the other evaluation datasets? This would help to determine if training on more complex datasets like the Roleplaying dataset leads to better generalization. 
- Have you tried evaluating the probes on other LLMs besides Llama 3.3 70B Instruct?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4