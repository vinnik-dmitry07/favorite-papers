## Reviewer

### Summary

This paper studies the performance of LLMs on arithmetic tasks, specifically addition, and shows that LLMs have a high error rate on the task. The authors identify two main sources of error: misalignment and close carry errors. Misalignment errors occur when the model incorrectly shifts the digits of the two numbers being added. Close carry errors occur when the model incorrectly carries or fails to carry a 1 in a particular column. The authors also show that the error rate is periodic with respect to the length of the numbers being added, and that the error rate is higher for numbers whose length is not a multiple of 3.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well written and easy to follow. The figures are helpful in understanding the results.
- The authors identify two main sources of error and provide a good analysis of the sources of error.
- The paper shows that the error rate is periodic with respect to the length of the numbers being added.

### Weaknesses

- The paper does not provide a clear explanation of why the error rate is periodic with respect to the length of the numbers being added.
- The paper does not provide a clear explanation of why the error rate is higher for numbers whose length is not a multiple of 3.
- The paper does not provide a clear explanation of why the error rate is higher for numbers whose length is not a multiple of 3.

### Questions

- Can the authors explain why the error rate is periodic with respect to the length of the numbers being added?
- Can the authors explain why the error rate is higher for numbers whose length is not a multiple of 3?
- Can the authors explain why the error rate is higher for numbers whose length is not a multiple of 3?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the performance of frontier LLMs on addition problems. The authors find that all frontier LLMs perform poorly on addition as the number of digits increases. The authors also find that the errors made by the models are highly interpretable and can be attributed to either operand misalignment or a failure to correctly carry; these two error classes explain 87.9%, 62.9%, and 92.4% of Claude Opus 4.1, GPT-5, and Gemini 2.5 Pro errors, respectively.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct a systematic investigation of the performance of frontier LLMs on addition problems and identify two main sources of errors: misalignment and close carry errors.
3. The authors provide a detailed analysis of the errors made by the models and show that most errors can be attributed to either operand misalignment or a failure to correctly carry.

### Weaknesses

1. The authors only consider addition problems with two operands. It would be interesting to see the performance of the models on addition problems with more than two operands.
2. The authors only consider addition problems with single-digit numbers. It would be interesting to see the performance of the models on addition problems with multi-digit numbers.
3. The authors only consider addition problems with positive numbers. It would be interesting to see the performance of the models on addition problems with negative numbers.

### Questions

1. How do the models perform on addition problems with more than two operands?
2. How do the models perform on addition problems with multi-digit numbers?
3. How do the models perform on addition problems with negative numbers?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the performance of LLMs on simple addition problems. The authors find that LLMs perform poorly on addition as the number of digits increases. They attribute the errors to misalignment and close carry errors, and show that these two error classes explain a large proportion of the errors made by the models. The authors also show that misalignment errors are often periodic with respect to argument length, and that the occurrence of close carry errors is largely consistent with an independent error model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors do a good job of explaining the methodology and results.
- The authors identify two main sources of error and provide a good analysis of the sources of error.
- The paper shows that the error rate is periodic with respect to the length of the numbers being added.

### Weaknesses

- The paper only considers addition problems with two operands. It would be interesting to see the performance of the models on addition problems with more than two operands.
- The paper only considers addition problems with single-digit numbers. It would be interesting to see the performance of the models on addition problems with multi-digit numbers.
- The paper only considers addition problems with positive numbers. It would be interesting to see the performance of the models on addition problems with negative numbers.

### Questions

- How do the models perform on addition problems with more than two operands?
- How do the models perform on addition problems with multi-digit numbers?
- How do the models perform on addition problems with negative numbers?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper presents a systematic investigation of the performance of modern AI systems on basic arithmetic tasks, specifically integer addition. The authors demonstrate that these systems suffer from significant accuracy degradation as the number of digits increases. They also identify two primary sources of errors: operand misalignment and close carry errors, which account for a substantial proportion of mistakes. The study reveals that misalignment errors are often related to tokenization, while carrying errors appear as independent random failures. The findings suggest that current models struggle with basic arithmetic, and the authors propose that arithmetic serves as a probe to understand larger problems in AI systems.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors have conducted a systematic investigation of the performance of frontier LLMs on addition problems and identified two main sources of errors: misalignment and close carry errors. The paper provides a detailed analysis of the errors made by the models and shows that most errors can be attributed to either operand misalignment or a failure to correctly carry. The paper also shows that the error rate is periodic with respect to the length of the numbers being added.

### Weaknesses

The paper only considers addition problems with two operands. It would be interesting to see the performance of the models on addition problems with more than two operands. The paper only considers addition problems with single-digit numbers. It would be interesting to see the performance of the models on addition problems with multi-digit numbers. The paper only considers addition problems with positive numbers. It would be interesting to see the performance of the models on addition problems with negative numbers.

### Questions

How do the models perform on addition problems with more than two operands? How do the models perform on addition problems with multi-digit numbers? How do the models perform on addition problems with negative numbers?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies the performance of LLMs on simple addition problems. The authors find that LLMs perform poorly on addition as the number of digits increases. They attribute the errors to misalignment and close carry errors, and show that these two error classes explain a large proportion of the errors made by the models. The authors also show that misalignment errors are often periodic with respect to argument length, and that the occurrence of close carry errors is largely consistent with an independent error model.

The paper is well-written and easy to follow. The authors identify two main sources of error and provide a good analysis of the sources of error. The paper shows that the error rate is periodic with respect to the length of the numbers being added.

### justification_for_why_not_higher_score

The paper only considers addition problems with two operands. It would be interesting to see the performance of the models on addition problems with more than two operands. The paper only considers addition problems with single-digit numbers. It would be interesting to see the performance of the models on addition problems with multi-digit numbers. The paper only considers addition problems with positive numbers. It would be interesting to see the performance of the models on addition problems with negative numbers.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors identify two main sources of error and provide a good analysis of the sources of error. The paper shows that the error rate is periodic with respect to the length of the numbers being added.

**********

## Paper Decision

Reject (not selected for spotlight/oral)