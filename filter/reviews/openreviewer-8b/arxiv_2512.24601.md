# Review

## Summary
This paper proposes a new inference paradigm for LLMs, namely recursive LMs (RLMs), which treats the input prompt as an external environment and allows the LLM to examine, decompose, and recursively call itself over snippets of the prompt. The authors conduct extensive experiments, and the results show that RLMs can significantly outperform vanilla LMs and other baselines on long-context tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The idea of treating the input prompt as an external environment is novel and interesting.
2. The authors conduct extensive experiments to demonstrate the effectiveness of RLMs.
3. The paper is well-written and easy to follow.

## Weaknesses
1. The idea of treating the input prompt as an external environment is interesting, but it also introduces additional inference overhead. Although the authors claim that the inference cost of RLMs is comparable to other methods, I think they should provide more details about the computation cost, e.g., the number of tokens and the number of API calls.
2. The authors mainly evaluate RLMs on long-context tasks. How about their performance on general benchmarks, e.g., the ones included in the DeepSeek-RULER (https://github.com/deepseekai/DeepSeek-RULER)? Will RLMs also bring performance improvements on general benchmarks?
3. The authors mainly use GPT-5 and Qwen3-Coder-480B-A35B in their experiments. Can RLMs also work well on smaller open-source models, e.g., Llama 3 8B?

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4