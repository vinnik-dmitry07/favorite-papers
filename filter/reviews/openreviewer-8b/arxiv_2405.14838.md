# Review

## Summary
The paper proposes a method to internalize the CoT steps in LLMs. The method starts with a model trained with explicit CoT, and then gradually removes the intermediate steps and finetunes the model. The method is simple and effective, and achieves good performance on N-digit multiplication and GSM8K.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The method is simple and effective: start with a model trained with explicit CoT, and then gradually removes the intermediate steps and finetunes the model. The method is effective on N-digit multiplication and GSM8K.

2. The paper conducts thorough ablation studies on the design choices.

## Weaknesses
1. The paper only evaluates on two tasks: N-digit multiplication and GSM8K. The paper could be strengthened by evaluating on more tasks.

2. The paper only evaluates on a relatively small set of models: GPT-2 (124M), Phi-3 3.8B, and Mistral-7B. The paper could be strengthened by evaluating on larger models (e.g., GPT-3.5, GPT-4, Llama-70B, etc.)

## Questions
1. The paper mentions that the method is effective on 9x9 multiplication with GPT-2 Small, but what about 12x12 or higher? Does the method still work?

2. The paper mentions that the method is effective on GSM8K with Mistral-7B, but what about other math datasets (e.g., MATH)? Does the method still work?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4