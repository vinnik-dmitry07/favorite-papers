# Review

## Summary
The paper investigates whether probe-based methods can reliably detect evaluation awareness in LLMs. It demonstrates that these methods often fail to distinguish between evaluation and deployment contexts when prompt formats are partially controlled, as probes tend to track benchmark-canonical structures rather than genuine evaluation contexts. The study employs a 2x2 design to examine the interaction between context (evaluation vs. deployment) and format (benchmark vs. casual) and shows that probes primarily respond to format, especially under standard training conditions. The authors conclude that probe-based diagnostics are format-sensitive and may not provide a robust measure of evaluation awareness.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow. 
- The paper introduces a novel 2x2 design that systematically examines the interaction between context and format, isolating the effects of each variable. This methodological rigor allows for a more precise understanding of probe behavior under controlled conditions.
- The paper provides a nuanced contribution to the understanding of evaluation awareness in LLMs. Rather than questioning the existence of evaluation awareness, it critically examines the reliability of probe-based methods, highlighting the distinction between format and context. This is valuable for future research aiming to improve the robustness of evaluation methods for LLMs.

## Weaknesses
- The paper only evaluates linear probes and a single LLM (Llama-3.1-8B-Instruct). This limited scope raises questions about the generalizability of the findings. It would be valuable to see whether the observed format sensitivity persists across different models and more complex probe architectures.
- The study relies on a few datasets, some of which are constructed for this paper. While the 2x2 design is useful, the findings may not be representative of the diverse range of prompts encountered in real-world LLM applications. The reliance on synthetic or proxy datasets for some conditions (e.g., Casual-Eval) could limit the external validity of the results.
- The paper identifies the issue of format sensitivity but does not propose concrete solutions. Providing guidelines for designing probes that are less sensitive to format or suggesting alternative evaluation methods would enhance the practical impact of the findings.

## Questions
- Have you considered using non-linear probe methods, such as MLPs or more sophisticated neural network architectures? Would these methods show different results in terms of format sensitivity?
- How do you think your findings might generalize to other LLMs? Would larger models or different architectures show similar sensitivity to prompt format?
- Can you elaborate on the potential applications of your findings? For instance, how might this impact the design of future benchmarks or the development of more robust evaluation methods for LLMs?
- How do you think the format sensitivity observed in linear probes relates to the broader question of evaluation awareness in LLMs? Do you believe this is an inherent limitation of probe-based methods, or do you see a way to overcome this through more advanced probe designs or alternative evaluation techniques?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4