# Review

## Summary
This paper presents a novel mechanistic interpretability analysis of how LLMs perform addition at the representation level. The authors find that LLMs represent numbers as a generalized helix and use the Clock algorithm to manipulate these helices to produce the sum. The paper provides a detailed analysis of how different components of the model, including MLPs and attention heads, contribute to this process. The findings are validated through causal interventions and comparisons with other fitting functions.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper provides a novel and detailed mechanistic explanation of how LLMs perform addition, which is a significant contribution to our understanding of LLMs' mathematical capabilities.
- The use of causal interventions and comparisons with different fitting functions (e.g., circular, polynomial) strengthens the validity of the findings.
- The paper is well-structured and clearly written, with effective use of visualizations to explain complex concepts.

## Weaknesses
- The analysis is limited to three specific LLMs, and it's unclear how generalizable the findings are to other LLMs or even to addition problems of larger numbers.
- The paper doesn't fully explain how the Clock algorithm is implemented within the model, only that it exists. This leaves some gaps in the mechanistic understanding.
- The paper doesn't explore how the helical representation and Clock algorithm might be related to other mathematical tasks beyond addition.

## Questions
- Have you considered the possibility that the helical representation and Clock algorithm might be used for other mathematical operations like subtraction, multiplication, or division?
- How do you think the use of the Clock algorithm compares to other potential methods the model could use for addition, such as a "linear" algorithm?
- Do you think the findings about the helical representation and Clock algorithm can be generalized to other LLMs, or are they specific to the models studied in this paper?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4