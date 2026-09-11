## Reviewer

### Summary

This paper proposes a new method for improving the inference efficiency of LLMs by predicting the execution program of layers. The authors first conduct an empirical study on the MCTS-searched programs to find that the best programs are mostly composed of contiguous layer segments, and then propose a lightweight PoLar prediction network to predict the execution program for each input. The proposed method is evaluated on a range of mathematical reasoning benchmarks and shows improvements over standard inference and prior dynamic-depth methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.

### Weaknesses

1. The authors claim that their method can reduce the inference latency. However, the authors only report the number of layers executed, but not the actual inference latency. I think it is more important to report the actual inference latency, as the number of layers executed may not be a good indicator of the actual inference latency. 
2. The authors only evaluate the proposed method on a limited range of mathematical reasoning benchmarks. It would be better if the authors can evaluate the proposed method on a wider range of tasks, such as language translation, question answering, and text summarization.
3. The authors only evaluate the proposed method on a single dataset (DART-Math) for out-of-distribution evaluation. It would be better if the authors can evaluate the proposed method on a wider range of datasets for out-of-distribution evaluation.

### Questions

1. How does the proposed method perform on the tasks other than mathematical reasoning?
2. How does the proposed method perform on the out-of-distribution datasets other than DART-Math?
3. How does the actual inference latency compare to the standard inference?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a new method to dynamically control the execution of LLMs by learning a program-of-layers (PoLar) that can skip or repeat some layers. The authors conduct a search-based study to show that better programs exist for every input task and propose a lightweight PoLar prediction network to predict the execution program for each input. Experiments on mathematical reasoning benchmarks show that PoLar improves accuracy over standard inference and prior dynamic-depth methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The idea of using a program-of-layers to dynamically control the execution of LLMs is interesting and novel.
- The paper is well-written and easy to follow.
- The proposed method is simple and effective.

### Weaknesses

- The experiments are limited to mathematical reasoning benchmarks. It would be better if the authors can evaluate the proposed method on a wider range of tasks, such as language translation, question answering, and text summarization.
- The authors only evaluate the proposed method on a single dataset (DART-Math) for out-of-distribution evaluation. It would be better if the authors can evaluate the proposed method on a wider range of datasets for out-of-distribution evaluation.

### Questions

- How does the proposed method perform on the tasks other than mathematical reasoning?
- How does the proposed method perform on the out-of-distribution datasets other than DART-Math?
- How does the actual inference latency compare to the standard inference?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a lightweight program-of-layers (PoLar) prediction network for dynamically skipping or repeating layers in pretrained LLMs. The authors first conduct an empirical study to show that better programs exist for every input task, and then propose a lightweight PoLar prediction network to predict the execution program for each input. The proposed method is evaluated on mathematical reasoning benchmarks and shows improvements over standard inference and prior dynamic-depth methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experiments are well-designed and the results are promising.

### Weaknesses

1. The proposed method is only evaluated on mathematical reasoning benchmarks. It would be better if the authors can evaluate the proposed method on a wider range of tasks, such as language translation, question answering, and text summarization.
2. The authors only evaluate the proposed method on a single dataset (DART-Math) for out-of-distribution evaluation. It would be better if the authors can evaluate the proposed method on a wider range of datasets for out-of-distribution evaluation.

### Questions

1. How does the proposed method perform on the tasks other than mathematical reasoning?
2. How does the proposed method perform on the out-of-distribution datasets other than DART-Math?
3. How does the actual inference latency compare to the standard inference?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to dynamically control the execution of LLMs by learning a program-of-layers (PoLar) that can skip or repeat some layers. The authors conduct a search-based study to show that better programs exist for every input task and propose a lightweight PoLar prediction network to predict the execution program for each input. Experiments on mathematical reasoning benchmarks show that PoLar improves accuracy over standard inference and prior dynamic-depth methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The idea of using a program-of-layers to dynamically control the execution of LLMs is interesting and novel.
2. The paper is well-written and easy to follow.
3. The proposed method is simple and effective.

### Weaknesses

1. The experiments are limited to mathematical reasoning benchmarks. It would be better if the authors can evaluate the proposed method on a wider range of tasks, such as language translation, question answering, and text summarization.
2. The authors only evaluate the proposed method on a single dataset (DART-Math) for out-of-distribution evaluation. It would be better if the authors can evaluate the proposed method on a wider range of datasets for out-of-distribution evaluation.

### Questions

1. How does the proposed method perform on the tasks other than mathematical reasoning?
2. How does the proposed method perform on the out-of-distribution datasets other than DART-Math?
3. How does the actual inference latency compare to the standard inference?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper proposes a lightweight PoLar prediction network to predict the execution program for each input. The proposed method is evaluated on mathematical reasoning benchmarks and shows improvements over standard inference and prior dynamic-depth methods. All reviewers gave a rating of 5 and the authors did not provide a rebuttal. Therefore, I recommend rejection.

### justification_for_why_not_higher_score

The paper received 4x 5 ratings and no rebuttal was provided.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication)