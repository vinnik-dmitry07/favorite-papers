# Review

## Summary
The paper investigates how language models (LMs) compare quantities with measurement units, such as determining which is larger between 110 cm and 1.2 m. The authors find that LM accuracy decreases near the comparison boundary, with errors being systematic. They propose that LM behavior is better explained by a "bag of heuristics" based on numerical differences and unit-scale differences rather than by exact unit conversion. The study uses behavioral analysis, surrogate models, and causal interventions to support this claim.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-structured, with a clear methodology and rigorous experimental design.
2. The use of surrogate models and causal interventions provides strong evidence for the proposed heuristic-based explanation.
3. The findings contribute to our understanding of how LMs process quantitative information with measurement units, which has practical implications for various applications.

## Weaknesses
1. The study focuses on single-step comparisons in a controlled setting, which may not reflect how LMs handle more complex, real-world quantitative reasoning tasks.
2. The use of linear surrogate models may oversimplify the actual heuristic mechanisms used by LMs.
3. The analysis is limited to short answer generation, and it is unclear how these findings would extend to reasoning-oriented LMs or tasks requiring multi-token reasoning.

## Questions
1. How do the proposed heuristics perform in more complex, real-world scenarios involving multi-step quantitative reasoning?
2. Could the methods used in this study be adapted to analyze reasoning-oriented LMs or models generating multi-token outputs?
3. How do the findings about the "bag of heuristics" compare with existing work on LMs using pattern-matching heuristics for arithmetic operations? (e.g., Nikankin et al., 2025)

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4