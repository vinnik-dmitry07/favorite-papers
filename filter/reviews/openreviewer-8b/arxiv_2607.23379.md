# Review

## Summary
This paper investigates Activation Oracles (AOs), which are language models trained to interpret hidden states of another model and respond to natural language queries about them. The authors examine whether an AO trained on a model that is secretly using a specific concept (e.g., "leaf") will become better at interpreting that concept. Surprisingly, they find that the AO actually becomes worse at interpreting this concept, even though the concept is still present in the hidden states and can be recovered by other methods. This suggests that the AO has learned to "not read" this concept, which the authors term a "concept-specific blind spot." The authors investigate the mechanisms behind this phenomenon and show that the concept remains decodable from the activations, but the AO's output head learns to suppress it. They conclude that interpretability tools must be carefully evaluated not just for what information they recover, but also for what they fail to recover due to their training.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The experiments are well-designed and the results are clearly presented.
- The findings are interesting and relevant to the interpretability community.
- The authors provide a detailed analysis of the mechanisms behind the phenomenon.

## Weaknesses
- The experiments are conducted on a relatively small set of hidden concepts (5 single-concept models + 1 two-concept model). It would be interesting to see if the results hold for a larger set of concepts and models.
- The authors focus on a specific implementation of activation oracles, where the oracle is a LoRA-fine-tuned copy of the subject model. It would be interesting to see if the results hold for other implementations of activation oracles.

## Questions
- Do the authors expect these results to hold for other architectures and larger scales?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4