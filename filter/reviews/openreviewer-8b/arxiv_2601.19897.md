# Review

## Summary
This paper proposes a novel method for continual learning in LLMs by using self-distillation. The method uses the model itself as a teacher and a student, conditioned on the demonstration. The method is evaluated in two continual learning settings: skill learning and knowledge acquisition. The method is compared with baselines such as SFT and CPT. The method shows better performance in skill learning and knowledge acquisition settings.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The paper proposes a novel method for continual learning in LLMs using self-distillation.
3. The method is evaluated in two different continual learning settings and compared with multiple baselines.
4. The paper provides a theoretical analysis of the method.

## Weaknesses
1. The proposed method is only applicable to models that have in-context learning capabilities.
2. The method is not evaluated on the most recent LLMs such as o1 and GPT-4.
3. The method is not compared with the most recent baselines such as [1].
4. The method is not evaluated on the most recent benchmarks such as BigBench and MMLU-Pro.

[1] Learning to Prompt for Continual Learning in Large Language Models

## Questions
1. Can the method be applied to the most recent LLMs such as o1 and GPT-4?
2. Can the method be used for other tasks such as math and code generation?
3. How does the method compare with the most recent baselines such as [1]?
4. How does the method perform on the most recent benchmarks such as BigBench and MMLU-Pro?
5. Can the method be applied to vision-language models such as CLIP and BLIP?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4