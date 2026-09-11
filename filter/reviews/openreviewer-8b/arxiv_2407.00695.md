# Review

## Summary
The paper presents a novel approach to training agents for formal mathematical reasoning, starting from only the axioms of a given domain. The proposed agent, named Minimo, learns to propose challenging conjectures and prove them. The authors demonstrate that Minimo improves its performance across training iterations. However, the paper also highlights two crucial limitations of the current approach: the inability to discover deep mathematical theories and the difficulty in scaling up to large theories due to the fixed library and the finite action space. The authors suggest that future work should focus on bootstrapping cumulative learning in agents and developing more efficient premise selection methods to overcome these limitations and create a fully functional, self-improving agent for formal mathematics.

## Soundness
3

## Presentation
2

## Contribution
3

## Strengths
The paper introduces a novel approach to training agents for formal mathematical reasoning, which is a significant contribution to the field. The authors provide evidence of the agent's ability to improve its performance across training iterations, which is a promising result. The paper also highlights the current limitations of the approach, which is crucial for future research in this area.

## Weaknesses
The paper has two main weaknesses: (a) the inability to discover deep mathematical theories, and (b) the difficulty in scaling up to large theories. These limitations are significant as they prevent the proposed method from achieving its full potential in the current form. The paper could benefit from a more detailed discussion on how these limitations could be addressed in future work.

## Questions
1. How do you plan to address the limitations mentioned in the paper, particularly the inability to discover deep mathematical theories and the difficulty in scaling up to large theories?
2. Can you provide more details on the bootstrapping approach for cumulative learning that you mentioned in the paper? How do you envision it working, and what benefits it could bring to the agent's performance?
3. Can you elaborate on the premise selection method that you suggested as a potential solution to the scalability issue? How do you see it being implemented, and what advantages it could offer in terms of scaling up to large theories?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4