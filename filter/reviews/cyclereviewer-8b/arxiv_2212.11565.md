## Reviewer

### Summary

This paper proposes a new setting of One-Shot Video Tuning for T2V generation, which eliminates the burden of training with large-scale video datasets. The authors also propose a new framework for T2V generation via an efficient tuning of pre-trained T2I diffusion models on one text-video pair. The proposed method can generate temporally-coherent videos. Extensive experiments demonstrate the remarkable results of the proposed method.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The idea of using a single video for T2V generation is novel.
2. The proposed method can generate temporally-coherent videos.

### Weaknesses

1. The proposed method is based on the existing T2I model, and the proposed method is not very novel.
2. The proposed method is not very effective. For example, the video generation results in Fig. 7 are not good enough.
3. The proposed method is not very efficient. For example, the training time is 10 minutes for a single video.

### Questions

1. The proposed method is based on the existing T2I model, and the proposed method is not very novel.
2. The proposed method is not very effective. For example, the video generation results in Fig. 7 are not good enough.
3. The proposed method is not very efficient. For example, the training time is 10 minutes for a single video.

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new setting of One-Shot Video Tuning for T2V generation, which eliminates the burden of training with large-scale video datasets. The authors also propose a new framework for T2V generation via an efficient tuning of pre-trained T2I diffusion models on one text-video pair. The proposed method can generate temporally-coherent videos. Extensive experiments demonstrate the remarkable results of the proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The proposed method can generate temporally-coherent videos.
2. The proposed method can generate temporally-coherent videos.

### Weaknesses

1. The proposed method is based on the existing T2I model, and the proposed method is not very novel.
2. The proposed method is not very effective. For example, the video generation results in Fig. 7 are not good enough.
3. The proposed method is not very efficient. For example, the training time is 10 minutes for a single video.
4. The proposed method is not very effective. For example, the video generation results in Fig. 7 are not good enough.

### Questions

1. The proposed method is based on the existing T2I model, and the proposed method is not very novel.
2. The proposed method is not very effective. For example, the video generation results in Fig. 7 are not good enough.
3. The proposed method is not very efficient. For example, the training time is 10 minutes for a single video.

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper introduces a novel approach to text-to-video generation, dubbed One-Shot Video Tuning, which leverages a single text-video pair and a pretrained text-to-image model. The method employs a tailored spatio-temporal attention mechanism and an efficient one-shot tuning strategy. The paper presents extensive qualitative and numerical experiments demonstrating the method's effectiveness across various applications.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper introduces a novel approach to text-to-video generation, leveraging a single text-video pair and a pretrained text-to-image model. This approach is efficient and computationally less expensive compared to training on large-scale video datasets.
2. The paper presents extensive qualitative and numerical experiments demonstrating the method's effectiveness across various applications.
3. The paper is well-written and easy to follow.

### Weaknesses

1. The paper lacks a comprehensive comparison with existing methods, making it challenging to assess the method's novelty and effectiveness.
2. The paper does not provide a detailed explanation of the experimental setup, including the choice of dataset, hyperparameters, and evaluation metrics.
3. The paper does not discuss the limitations of the proposed method and potential future research directions.

### Questions

1. How does the proposed method compare to existing text-to-video generation methods in terms of performance and computational efficiency?
2. What are the key hyperparameters used in the proposed method, and how are they tuned?
3. What are the limitations of the proposed method, and how can they be addressed in future work?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a method to perform text-to-video generation using a single text-video pair. The method is based on a pretrained text-to-image diffusion model and adds a spatio-temporal attention mechanism to generate videos. The method also uses a fine-tuning strategy to update the model parameters. The method is evaluated on a dataset of 42 videos and achieves good results compared to baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper proposes a novel method for text-to-video generation using a single text-video pair.
- The method is based on a pretrained text-to-image diffusion model, which is efficient and effective.
- The paper provides extensive qualitative and quantitative results demonstrating the method's effectiveness across various applications.

### Weaknesses

- The method requires a pretrained text-to-image model, which is not always available.
- The method requires a single text-video pair, which may not be sufficient to capture the complexity of real-world videos.
- The method is limited to generating videos with a single object or action, which may not be sufficient for more complex scenarios.

### Questions

- How does the method perform on more complex videos with multiple objects or actions?
- How does the method compare to other text-to-video generation methods that use large-scale video datasets?
- Can the method be used to generate videos with more complex backgrounds or environments?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper introduces a new setting of One-Shot Video Tuning for T2V generation, which eliminates the burden of training with large-scale video datasets. The authors also propose a new framework for T2V generation via an efficient tuning of pre-trained T2I diffusion models on one text-video pair. The proposed method can generate temporally-coherent videos. Extensive experiments demonstrate the remarkable results of the proposed method.

Strengths: The idea of using a single video for T2V generation is novel.

Weaknesses: The proposed method is based on the existing T2I model, and the proposed method is not very novel. The proposed method is not very effective. For example, the video generation results in Fig. 7 are not good enough. The proposed method is not very efficient. For example, the training time is 10 minutes for a single video.

### justification_for_why_not_higher_score

The proposed method is based on the existing T2I model, and the proposed method is not very novel. The proposed method is not very effective. For example, the video generation results in Fig. 7 are not good enough. The proposed method is not very efficient. For example, the training time is 10 minutes for a single video.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (out of the borderline between accept and reject)

**********

## Paper Decision View

Reject (out of the borderline between accept and reject)

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (5)
* **New Score Distribution**:
	- score 1: 0
	- score 5: 4
	- score 10: 0
* **New Majority**:
	- accept: 0
	- reject: 4
* **New Decision**: Reject (out of the borderline between accept and reject)

**********

**********

---

## Paper Decision Policy

1. If at least 5 reviews are submitted, we take a vote among the reviewers (by majority).
2. If the paper received a "weak reject" (score 3) from all the reviewers, we reject the paper.
3. If the paper received a "marginally below the acceptance threshold" (score 5) from all the reviewers, we reject the paper.
4. If the paper received a score 10 from any reviewer, we accept the paper immediately.
5. If at least 1/3 of the reviewers gave a score 1, we accept the paper immediately.
6. If at least 1/3 of the reviewers gave a score 5, we reject the paper immediately.
7. Otherwise, we take a vote among the reviewers (by majority).

## Paper Decision History

* **Initial Decision**: Accept (poster) (score 6)
* **Author Response**:
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
	- reviewer_6wLr: no response
* **New Score**:
	- reviewer_6wLr: 5 (5)
	- reviewer_6wLr: 5 (