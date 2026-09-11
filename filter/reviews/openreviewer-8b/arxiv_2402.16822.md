# Review

## Summary
This paper introduces a new method for generating a diverse set of adversarial prompts for testing the robustness of LLMs. The method is based on quality-diversity search and uses LLMs for all key steps: mutation, evaluation, and preference model. The authors show that their method is able to find a large set of adversarial prompts for a variety of models and domains. They also show that fine-tuning on the generated prompts makes the models more robust.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
- The method is novel and interesting. It is also very general and can be applied to a variety of domains.
- The experiments are extensive and well-designed. The authors test their method on several models and compare it to reasonable baselines. They also show that the generated prompts are diverse and transfer to other models.
- The paper is well-written and easy to follow. The authors do a good job of explaining their method and the results.

## Weaknesses
- The authors do not compare to other methods for generating diverse adversarial prompts, such as [1].
- The authors do not evaluate the method on larger models (e.g. 70B+)
- The authors do not evaluate the method on models that are more difficult to attack (e.g. models with stronger safety measures)

[1] https://arxiv.org/abs/2402.16837

## Questions
- How does your method compare to other methods for generating diverse adversarial prompts?
- How well does your method work on larger models and on models that are more difficult to attack?
- Have you considered using a reward model instead of a preference model? What are the pros and cons?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4