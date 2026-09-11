# Review

## Summary
The paper proposes a unified framework to define and measure continual learning in modern LLMs. The authors disentangle the change along two axes — space, where the model encounters new domains, and time, where the underlying data drifts under a fixed task. The paper evaluates eight methods under a common mechanism-agnostic protocol and finds that prompt-based methods alone are insufficient across most regimes, calling for actual learning. Different learning methods each have their own strengths depending on how the task and data shift over time.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper proposes a unified framework to define and measure continual learning in modern LLMs, which is a step forward in the field.
2. The paper evaluates eight methods under a common mechanism-agnostic protocol, providing a comprehensive analysis of their performance.

## Weaknesses
1. The paper evaluates the methods using only one model, Qwen3-8B, which may not be representative of other models. Larger models may have different behaviors and requirements.
2. The benchmark suite captures only a subset of realistic environmental change, which may not reflect the diversity and complexity of real-world scenarios.

## Questions
1. How do the relative behaviors of the tested methods change for larger models or models in reasoning mode?
2. What are the open-ended, changing, and uncertain environments and diverse use cases that the results can guide?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4