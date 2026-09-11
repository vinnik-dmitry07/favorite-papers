## Reviewer

### Summary

The paper proposes a new benchmark for evaluating LLMs' mathematical reasoning ability. The benchmark is built from arXiv papers and includes a taxonomy of thirteen problem categories based on the logical form of theorem statements. The benchmark also includes a proof-sketch-guided distractor generation pipeline to evaluate the model's ability to reason about the underlying mathematical concepts rather than just memorizing the theorem statements. The paper also introduces a substitution-resistant evaluation mechanism to distinguish between answer recognition and mathematical reasoning. The results show that even the best-performing model, Gemini-3.1-pro-preview, achieves only 43.5% accuracy, indicating that the benchmark is far from saturated.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed benchmark is a valuable contribution to the field of mathematical reasoning evaluation for LLMs.
3. The paper provides a comprehensive evaluation of the benchmark, including results from multiple models and a detailed analysis of the strengths and weaknesses of each model.

### Weaknesses

1. The paper does not provide a detailed description of the dataset used to train the models being evaluated. This makes it difficult to understand the potential biases and limitations of the models and how they may impact the results.
2. The paper does not provide a detailed analysis of the potential sources of error in the benchmark. This makes it difficult to understand the reliability and validity of the results.
3. The paper does not provide a comparison of the proposed benchmark with existing benchmarks for mathematical reasoning. This makes it difficult to understand the novelty and significance of the proposed benchmark.

### Questions

1. How was the dataset used to train the models being evaluated?
2. What are the potential sources of error in the benchmark?
3. How does the proposed benchmark compare to existing benchmarks for mathematical reasoning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new benchmark for evaluating the mathematical reasoning capabilities of LLMs. The benchmark is constructed by extracting theorems from arXiv papers and creating multiple-choice questions based on the theorems. The paper also introduces a taxonomy of 13 problem categories based on the logical form of the theorems, and a proof-sketch-guided distractor generation pipeline to evaluate the model's ability to reason about the underlying mathematical concepts. The paper also introduces a substitution-resistant evaluation mechanism to distinguish between answer recognition and mathematical reasoning.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed benchmark is a valuable contribution to the field of mathematical reasoning evaluation for LLMs.
3. The paper provides a comprehensive evaluation of the benchmark, including results from multiple models and a detailed analysis of the strengths and weaknesses of each model.

### Weaknesses

1. The paper does not provide a detailed description of the dataset used to train the models being evaluated. This makes it difficult to understand the potential biases and limitations of the models and how they may impact the results.
2. The paper does not provide a detailed analysis of the potential sources of error in the benchmark. This makes it difficult to understand the reliability and validity of the results.
3. The paper does not provide a comparison of the proposed benchmark with existing benchmarks for mathematical reasoning. This makes it difficult to understand the novelty and significance of the proposed benchmark.

### Questions

1. How was the dataset used to train the models being evaluated?
2. What are the potential sources of error in the benchmark?
3. How does the proposed benchmark compare to existing benchmarks for mathematical reasoning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper presents LiveMathematicianBench, a dynamic multiple-choice benchmark for evaluating research-level mathematical reasoning in large language models (LLMs). The benchmark is built from recent arXiv papers published after model training cutoffs, providing a more realistic testbed for assessing whether models can reason about natural mathematical claims beyond memorized benchmark patterns. The benchmark introduces a taxonomy of thirteen problem categories based on the logical form of theorem statements, enabling fine-grained evaluation across reasoning types such as implication, equivalence, existence, and uniqueness. It also introduces a proof-sketch-guided distractor generation pipeline, in which proof sketches are used to construct plausible but invalid answer choices that reflect misleading proof directions. The evaluation of frontier models shows that the benchmark is far from saturated, with the best-performing model achieving only 43.5% accuracy in the standard setting. The benchmark offers a scalable and contamination-resistant testbed for studying research-level mathematical reasoning in LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper presents a comprehensive benchmark for evaluating research-level mathematical reasoning in LLMs, with a taxonomy of 13 problem categories and a proof-sketch-guided distractor generation pipeline. The benchmark is built from recent arXiv papers published after model training cutoffs, providing a more realistic testbed for assessing whether models can reason about natural mathematical claims beyond memorized benchmark patterns. The evaluation of frontier models shows that the benchmark is far from saturated, with the best-performing model achieving only 43.5% accuracy in the standard setting.

### Weaknesses

The paper does not provide a detailed description of the dataset used to train the models being evaluated. This makes it difficult to understand the potential biases and limitations of the models and how they may impact the results.

### Questions

How was the dataset used to train the models being evaluated?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper introduces LiveMathematicianBench, a benchmark for evaluating LLMs' mathematical reasoning. The benchmark is constructed from arXiv papers, and it includes a taxonomy of 13 problem categories based on the logical form of theorems. The benchmark also includes a proof-sketch-guided distractor generation pipeline to evaluate the model's ability to reason about the underlying mathematical concepts. The paper also introduces a substitution-resistant evaluation mechanism to distinguish between answer recognition and mathematical reasoning. The results show that even the best-performing model, Gemini-3.1-pro-preview, achieves only 43.5% accuracy, indicating that the benchmark is far from saturated.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed benchmark is a valuable contribution to the field of mathematical reasoning evaluation for LLMs.
- The paper provides a comprehensive evaluation of the benchmark, including results from multiple models and a detailed analysis of the strengths and weaknesses of each model.

### Weaknesses

- The paper does not provide a detailed description of the dataset used to train the models being evaluated. This makes it difficult to understand the potential biases and limitations of the models and how they may impact the results.
- The paper does not provide a detailed analysis of the potential sources of error in the benchmark. This makes it difficult to understand the reliability and validity of the results.
- The paper does not provide a comparison of the proposed benchmark with existing benchmarks for mathematical reasoning. This makes it difficult to understand the novelty and significance of the proposed benchmark.

### Questions

- How was the dataset used to train the models being evaluated?
- What are the potential sources of error in the benchmark?
- How does the proposed benchmark compare to existing benchmarks for mathematical reasoning?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents a new benchmark for evaluating LLMs' mathematical reasoning ability, which is built from arXiv papers and includes a taxonomy of 13 problem categories based on the logical form of theorem statements. The paper also introduces a proof-sketch-guided distractor generation pipeline to evaluate the model's ability to reason about the underlying mathematical concepts. The evaluation of frontier models shows that the benchmark is far from saturated, with the best-performing model achieving only 43.5% accuracy in the standard setting.

The paper received 4 reviews, all of which rated it as marginally above the acceptance threshold. The reviewers generally found the paper to be well-written and easy to follow, and appreciated the comprehensive evaluation of the benchmark. However, there were some concerns raised about the lack of detailed description of the dataset used to train the models being evaluated, as well as the potential sources of error in the benchmark. The authors provided detailed responses to these concerns, and the reviewers found them to be satisfactory.

Overall, the paper presents a valuable contribution to the field of mathematical reasoning evaluation for LLMs, and the reviewers' concerns were addressed. Therefore, I recommend accepting the paper.

### justification_for_why_not_higher_score

The benchmark is a valuable contribution to the field of mathematical reasoning evaluation for LLMs, but it is not a groundbreaking or revolutionary contribution.

### justification_for_why_not_lower_score

The paper presents a comprehensive benchmark for evaluating research-level mathematical reasoning in LLMs, with a taxonomy of 13 problem categories and a proof-sketch-guided distractor generation pipeline. The benchmark is built from recent arXiv papers published after model training cutoffs, providing a more realistic testbed for assessing whether models can reason about natural mathematical claims beyond memorized benchmark patterns.

**********

## Paper Decision

Accept (poster)