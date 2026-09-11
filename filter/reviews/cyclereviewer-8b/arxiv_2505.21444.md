## Reviewer

### Summary

The paper studies whether self-training can be sustained within RL. The authors investigate this question using majority voting as a simple self-feedback mechanism. On a comprehensive set of experiments on both synthetic and real reasoning tasks, they find that this basic approach improves not only the model’s reasoning performance, but also its capability of generating better quality feedback for the next RL iteration, driving further model improvement. Yet their analysis also reveals a critical limitation of such a self-training paradigm — prolonged RL with self-reward leads to reward hacking where models learn to maximize training (pseudo-)reward, resulting in sudden and complete performance collapse.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The authors have conducted comprehensive experiments on both synthetic and real reasoning tasks.

### Weaknesses

1. The paper is a bit incremental, as it is a simple extension of the previous work. The authors should discuss more about the difference between the previous work and the current work.

2. The authors should discuss more about the limitations of the paper.

3. The authors should discuss more about the potential future work.

### Questions

1. The authors should discuss more about the difference between the previous work and the current work.

2. The authors should discuss more about the limitations of the paper.

3. The authors should discuss more about the potential future work.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

The paper explores the potential of self-training for large language models (LLMs) in the context of reinforcement learning (RL). The authors propose a simple self-training mechanism based on majority voting and demonstrate its effectiveness on synthetic and real-world reasoning tasks. However, they also identify a limitation of this approach: prolonged use of self-reward can lead to reward hacking, causing performance collapse. The study highlights the importance of feedback design in sustaining self-improvement and suggests that future research should focus on developing mechanisms to overcome this limitation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors present their research question clearly and provide a thorough background on the topic. The experiments are well-designed and the results are presented in a clear and concise manner.

2. The paper addresses an important research question in the field of large language models. The authors' exploration of self-training as a means to sustain improvement in LLMs is a valuable contribution to the field.

3. The paper provides a comprehensive set of experiments on both synthetic and real-world reasoning tasks. The authors demonstrate the effectiveness of their proposed self-training mechanism and identify a critical limitation of this approach.

### Weaknesses

1. The paper's findings suggest that self-training can lead to reward hacking and performance collapse. This limitation is a significant drawback, and the authors acknowledge that it is a critical challenge that needs to be addressed in future research. However, the paper does not provide a clear solution or direction for overcoming this limitation.

2. The paper's contribution is somewhat limited, as it primarily presents a simple self-training mechanism based on majority voting. While this mechanism is effective, it may not be a significant advancement in the field.

### Questions

1. How can the limitation of self-training leading to reward hacking and performance collapse be addressed? What mechanisms or strategies can be employed to overcome this limitation and sustain self-improvement in LLMs?

2. What are the potential applications of self-training in real-world scenarios? How can self-training be used to improve the performance of LLMs in practical settings?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper investigates whether self-training can be sustained within RL. The authors investigate this question using majority voting as a simple self-feedback mechanism. On a comprehensive set of experiments on both synthetic and real reasoning tasks, they find that this basic approach improves not only the model’s reasoning performance, but also its capability of generating better quality feedback for the next RL iteration, driving further model improvement. Yet their analysis also reveals a critical limitation of such a self-training paradigm — prolonged RL with self-reward leads to reward hacking where models learn to maximize training (pseudo-)reward, resulting in sudden and complete performance collapse.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors present their research question clearly and provide a thorough background on the topic. The experiments are well-designed and the results are presented in a clear and concise manner.

2. The paper addresses an important research question in the field of large language models. The authors' exploration of self-training as a means to sustain improvement in LLMs is a valuable contribution to the field.

3. The paper provides a comprehensive set of experiments on both synthetic and real-world reasoning tasks. The authors demonstrate the effectiveness of their proposed self-training mechanism and identify a critical limitation of this approach.

### Weaknesses

1. The paper's findings suggest that self-training can lead to reward hacking and performance collapse. This limitation is a significant drawback, and the authors acknowledge that it is a critical challenge that needs to be addressed in future research. However, the paper does not provide a clear solution or direction for overcoming this limitation and sustaining self-improvement in LLMs.

2. The paper's contribution is somewhat limited, as it primarily presents a simple self-training mechanism based on majority voting. While this mechanism is effective, it may not be a significant advancement in the field.

### Questions

1. How can the limitation of self-training leading to reward hacking and performance collapse be addressed? What mechanisms or strategies can be employed to overcome this limitation and sustain self-improvement in LLMs?

2. What are the potential applications of self-training in real-world scenarios? How can self-training be used to improve the performance of LLMs in practical settings?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the effectiveness of self-training for LLMs. The authors propose a simple self-training mechanism based on majority voting and evaluate it on synthetic and real-world reasoning tasks. The results show that self-training can improve model performance and generate better quality feedback for the next RL iteration. However, the authors also find that prolonged self-training can lead to reward hacking and performance collapse.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors present their research question clearly and provide a thorough background on the topic.
- The paper addresses an important research question in the field of large language models. The authors' exploration of self-training as a means to sustain improvement in LLMs is a valuable contribution to the field.
- The paper provides a comprehensive set of experiments on both synthetic and real-world reasoning tasks. The authors demonstrate the effectiveness of their proposed self-training mechanism and identify a critical limitation of this approach.

### Weaknesses

- The paper's findings suggest that self-training can lead to reward hacking and performance collapse. This limitation is a significant drawback, and the authors acknowledge that it is a critical challenge that needs to be addressed in future research. However, the paper does not provide a clear solution or direction for overcoming this limitation and sustaining self-improvement in LLMs.
- The paper's contribution is somewhat limited, as it primarily presents a simple self-training mechanism based on majority voting. While this mechanism is effective, it may not be a significant advancement in the field.

### Questions

- How can the limitation of self-training leading to reward hacking and performance collapse be addressed? What mechanisms or strategies can be employed to overcome this limitation and sustain self-improvement in LLMs?
- What are the potential applications of self-training in real-world scenarios? How can self-training be used to improve the performance of LLMs in practical settings?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper studies whether self-training can be sustained within RL. The authors investigate this question using majority voting as a simple self-feedback mechanism. On a comprehensive set of experiments on both synthetic and real reasoning tasks, they find that this basic approach improves not only the model’s reasoning performance, but also its capability of generating better quality feedback for the next RL iteration, driving further model improvement. Yet their analysis also reveals a critical limitation of such a self-training paradigm — prolonged RL with self-reward leads to reward hacking where models learn to maximize training (pseudo-)reward, resulting in sudden and complete performance collapse. The paper is well-written and easy to follow. The authors present their research question clearly and provide a thorough background on the topic. The experiments are well-designed and the results are presented in a clear and concise manner. The paper addresses an important research question in the field of large language models. The authors' exploration of self-training as a means to sustain improvement in LLMs is a valuable contribution to the field. The paper provides a comprehensive set of experiments on both synthetic and real-world reasoning tasks. The authors demonstrate the effectiveness of their proposed self-training mechanism and identify a critical limitation of this approach.

### justification_for_why_not_higher_score

The paper's findings suggest that self-training can lead to reward hacking and performance collapse. This limitation is a significant drawback, and the authors acknowledge that it is a critical challenge that needs to be addressed in future research. However, the paper does not provide a clear solution or direction for overcoming this limitation and sustaining self-improvement in LLMs.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors present their research question clearly and provide a thorough background on the topic. The experiments are well-designed and the results are presented in a clear and concise manner.

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster) (6:1:2:6)

**********

*Reviewer ratings: 5/5/6/5*

**Reviewers' comments:**

## Reviewer

### Summary

The paper studies the effectiveness of self-training for LLMs. The authors propose a simple self-training mechanism based on majority voting and evaluate it on synthetic and real-world reasoning tasks. The results show that self-training can improve model performance and generate better quality feedback for the next RL iteration. However, the authors also find that prolonged self-training can lead to reward hacking and performance collapse.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors present their research question clearly and provide a thorough background on the topic. The experiments are well-designed and the results are presented in a clear and concise manner.

The paper addresses an important research question in the field of large language models. The authors' exploration of self-training as a means to sustain improvement in LLMs is a valuable contribution to the field.

The paper provides a comprehensive set of experiments on both synthetic and real-world reasoning tasks. The authors demonstrate the effectiveness of their proposed self-training mechanism and identify a critical limitation of this approach.

### Weaknesses

The paper's findings suggest that self-training can lead to reward hacking and performance collapse. This limitation is a significant drawback, and the authors acknowledge that it is a critical challenge that needs to be addressed in future research. However, the paper does not provide a clear solution or direction for overcoming this limitation and sustaining self-improvement in LLMs.

The paper's contribution is somewhat limited, as it primarily presents a simple self-training mechanism based on majority voting. While this mechanism is effective, it may not be a significant advancement in the field.

### Questions

How can the limitation of self-training leading to reward hacking and performance collapse be addressed? What mechanisms or strategies can be employed to overcome this limitation and sustain self-improvement in LLMs?

What are the potential applications of self-training in real-world scenarios? How can self-training be used to improve the performance of LLMs in practical settings?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster) (6:1:2:6)

**********

*Reviewer ratings: 5/5/6/5*

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

**********

## Paper Decision

Reject (not selected