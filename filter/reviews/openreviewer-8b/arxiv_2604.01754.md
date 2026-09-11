# Review

## Summary
This paper presents a novel benchmark for evaluating LLMs on research-level mathematical reasoning. The benchmark is constructed from arXiv papers published after the LLM's training cutoff date, and it includes a taxonomy of 13 problem categories based on logical form. The authors also introduce a proof-sketch-guided distractor generation pipeline to create plausible but incorrect answer choices that reflect misleading proof directions. The paper evaluates several LLMs on this benchmark, including Gemini-3.1-pro-preview and GPT-5.4, and shows that the benchmark is far from saturated. The authors also introduce a substitution-resistant evaluation mechanism to distinguish answer recognition from substantive mathematical reasoning.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper addresses an important problem in evaluating LLMs' mathematical reasoning abilities, namely the need for benchmarks that are both diverse and contamination-free.
- The benchmark is based on a taxonomy of 13 problem categories, which allows for fine-grained evaluation of LLMs' reasoning abilities.
- The paper introduces a novel proof-sketch-guided distractor generation pipeline, which helps to prevent LLMs from relying on surface-level pattern matching and encourages more substantive mathematical reasoning.
- The paper evaluates several state-of-the-art LLMs on the benchmark and shows that it is far from saturated, providing a challenge for future research.

## Weaknesses
- The paper does not provide a detailed analysis of the distribution of the benchmark, such as the difficulty distribution or the topics covered.
- The paper does not provide a detailed comparison with other mathematical reasoning benchmarks, such as RealMath or OlympiadBench.

## Questions
- How is the quality of the generated proof sketches ensured? Are they verified by humans or checked automatically?
- How is the difficulty of the questions in the benchmark measured? Is there a systematic way to determine the difficulty level of a theorem?
- How does the benchmark compare to other existing mathematical reasoning benchmarks in terms of its coverage of mathematical concepts and difficulty level?
- How does the benchmark address the issue of data contamination? How can it be ensured that the theorems in the benchmark have not been seen by the LLMs during training?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4