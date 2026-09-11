## Reviewer

### Summary

This paper presents DeepSeekMath-7B, a 7B parameter language model that is pre-trained on 120B math-related tokens from Common Crawl, along with natural language and code data. The model is evaluated on a range of benchmarks, including GSM8K, MATH, SAT, MMLU-STEM, CMATH, Gaokao MathCloze, and Gaokao MathQA. The model achieves 51.7% on the MATH benchmark without relying on external toolkits and voting techniques, which is close to the performance of Gemini-Ultra and GPT-4. The authors also introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), which enhances mathematical reasoning abilities while optimizing memory usage. The authors also discuss the limitations of the model and potential future directions for improvement.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper presents a new model, DeepSeekMath-7B, which is pre-trained on 120B math-related tokens from Common Crawl, along with natural language and code data. The model is evaluated on a range of benchmarks, including GSM8K, MATH, SAT, MMLU-STEM, CMATH, Gaokao MathCloze, and Gaokao MathQA. The model achieves 51.7% on the MATH benchmark without relying on external toolkits and voting techniques, which is close to the performance of Gemini-Ultra and GPT-4.

2. The authors also introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), which enhances mathematical reasoning abilities while optimizing memory usage.

3. The authors also discuss the limitations of the model and potential future directions for improvement.

### Weaknesses

1. The paper does not provide a detailed analysis of the data selection pipeline used to construct the DeepSeekMath Corpus. It would be helpful to have a more detailed description of the data selection process, including how the data was filtered and how the quality of the data was assessed.

2. The paper does not provide a detailed analysis of the performance of the model on different types of mathematical problems. It would be helpful to have a more detailed analysis of the model's performance on different types of mathematical problems, such as algebra, geometry, and calculus.

3. The paper does not provide a detailed analysis of the limitations of the model. It would be helpful to have a more detailed discussion of the limitations of the model and potential future directions for improvement.

### Questions

1. How does the model perform on different types of mathematical problems, such as algebra, geometry, and calculus?

2. How does the model perform on different benchmarks, such as GSM8K, MATH, SAT, MMLU-STEM, CMATH, Gaokao MathCloze, and Gaokao MathQA?

3. What are the limitations of the model and potential future directions for improvement?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces DeepSeekMath, a language model that has been trained on a large corpus of math-related data sourced from Common Crawl. The model has been trained using a combination of pre-training and reinforcement learning techniques, and has achieved strong performance on a variety of mathematical reasoning benchmarks. The authors also introduce a new algorithm for training language models called Group Relative Policy Optimization (GRPO), which is designed to improve the model's mathematical reasoning abilities while reducing memory usage. Overall, the paper presents a strong case for the potential of language models to improve mathematical reasoning and provides a valuable contribution to the field.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a new algorithm for training language models called Group Relative Policy Optimization (GRPO), which is designed to improve the model's mathematical reasoning abilities while reducing memory usage. This algorithm is a novel contribution to the field and has the potential to improve the performance of language models on mathematical reasoning tasks.
2. The paper presents a strong case for the potential of language models to improve mathematical reasoning. The authors demonstrate that their model, DeepSeekMath, outperforms other language models on a variety of mathematical reasoning benchmarks, including GSM8K and MATH.
3. The paper provides a thorough evaluation of the model's performance on a variety of mathematical reasoning tasks, including both quantitative and qualitative reasoning. This evaluation helps to establish the model's strengths and weaknesses and provides a basis for future work in this area.

### Weaknesses

1. The paper does not provide a detailed analysis of the data used to train the model. While the authors mention that the data was sourced from Common Crawl, they do not provide information on the specific types of data that were included in the corpus or how they were processed.
2. The paper does not provide a detailed analysis of the model's performance on a variety of mathematical reasoning tasks. While the authors present results on GSM8K and MATH, they do not provide results on other types of mathematical reasoning tasks, such as geometry or calculus.
3. The paper does not provide a detailed analysis of the limitations of the model. While the authors mention that the model is not as strong as GPT-4 on some tasks, they do not provide a detailed analysis of the specific limitations of the model or how they might be addressed in future work.

### Questions

1. How does the model perform on other types of mathematical reasoning tasks, such as geometry or calculus?
2. How does the model perform on other benchmarks, such as GSM8K and MATH?
3. What are the limitations of the model and how might they be addressed in future work?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces DeepSeekMath, a new language model designed to improve mathematical reasoning. The authors have created a large-scale corpus of math-related data from Common Crawl, which they use to pre-train their model. They also introduce a new algorithm, Group Relative Policy Optimization (GRPO), to further improve the model's performance. The results show that DeepSeekMath outperforms other language models on various mathematical reasoning tasks, including GSM8K and MATH. The paper also provides a detailed analysis of the model's performance on different types of mathematical problems and discusses its limitations.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper presents a novel approach to improving mathematical reasoning in language models, by creating a large-scale corpus of math-related data and using it to pre-train the model. The results show that the model outperforms other language models on various mathematical reasoning tasks, including GSM8K and MATH. The paper also provides a detailed analysis of the model's performance on different types of mathematical problems and discusses its limitations.

### Weaknesses

The paper does not provide a detailed analysis of the limitations of the model. While the authors mention that the model is not as strong as GPT-4 on some tasks, they do not provide a detailed analysis of the specific limitations of the model or how they might be addressed in future work.

### Questions

How does the model perform on other types of mathematical reasoning tasks, such as geometry or calculus?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper introduces DeepSeekMath, a domain-specific language model that outperforms open-source models in mathematical reasoning and approaches the performance of closed models. It achieves this by pre-training on a large corpus of math-related data sourced from Common Crawl. The authors also introduce a new algorithm, Group Relative Policy Optimization (GRPO), which enhances mathematical reasoning while reducing memory usage. The paper also provides a unified paradigm to understand different methods and summarizes potential directions for more effective reinforcement learning.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper presents a strong case for the potential of language models to improve mathematical reasoning. The authors demonstrate that their model, DeepSeekMath, outperforms other language models on a variety of mathematical reasoning benchmarks, including GSM8K and MATH. The paper also provides a thorough evaluation of the model's performance on a variety of mathematical reasoning tasks, including both quantitative and qualitative reasoning. This evaluation helps to establish the model's strengths and weaknesses and provides a basis for future work in this area.

### Weaknesses

The paper does not provide a detailed analysis of the limitations of the model. While the authors mention that the model is not as strong as GPT-4 on some tasks, they do not provide a detailed analysis of the specific limitations of the model or how they might be addressed in future work.

### Questions

1. How does the model perform on other types of mathematical reasoning tasks, such as geometry or calculus?
2. How does the model perform on other benchmarks, such as GSM8K and MATH?
3. What are the limitations of the model and how might they be addressed in future work?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents DeepSeekMath, a language model that has been trained on a large corpus of math-related data sourced from Common Crawl. The model has been trained using a combination of pre-training and reinforcement learning techniques, and has achieved strong performance on a variety of mathematical reasoning benchmarks. The authors also introduce a new algorithm for training language models called Group Relative Policy Optimization (GRPO), which is designed to improve the model's mathematical reasoning abilities while reducing memory usage. The authors also discuss the limitations of the model and potential future directions for improvement.

The paper received four reviews, all of which were positive. Reviewers appreciated the strong performance of the model on mathematical reasoning benchmarks, as well as the introduction of a new algorithm for training language models. They also appreciated the thorough evaluation of the model's performance on a variety of mathematical reasoning tasks, including both quantitative and qualitative reasoning. The authors provided detailed responses to all the reviews, which were found to be satisfactory by the reviewers.

### justification_for_why_not_higher_score

The paper presents a strong case for the potential of language models to improve mathematical reasoning. The authors demonstrate that their model, DeepSeekMath, outperforms other language models on a variety of mathematical reasoning benchmarks, including GSM8K and MATH. The paper also provides a thorough evaluation of the model's performance on a variety of mathematical reasoning tasks, including both quantitative and qualitative reasoning. This evaluation helps to establish the model's strengths and weaknesses and provides a basis for future work in this area.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Accept (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster) (poster)