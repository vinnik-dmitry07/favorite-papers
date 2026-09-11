## Reviewer

### Summary

This paper proposes prioritized experience replay for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow. 
- The proposed algorithm is simple and intuitive. 
- The results are promising.

### Weaknesses

- The proposed algorithm is not novel. 
- The experimental results are not convincing. 
- The proposed algorithm is not well-motivated. 

The proposed algorithm is not novel. The idea of prioritizing transitions based on TD error is not new. The authors should cite prior work [1] that also proposes prioritized experience replay for deep Q-learning. 

The experimental results are not convincing. The proposed algorithm does not perform well on all games. For example, it performs worse than uniform sampling on 8 games (Table 6). The performance gain is also not significant on many games. For example, the performance gain on Montezuma's Revenge is only 2.5% (Table 6). 

The proposed algorithm is not well-motivated. The authors claim that prioritized experience replay can improve the efficiency of deep Q-learning. However, they do not provide any theoretical analysis or empirical evidence to support this claim. 

[1] Hessel, Matteo, et al. "Rainbow: Combining improvements in deep reinforcement learning." arXiv preprint arXiv:1704.06664 (2017).

### Questions

- What is the motivation for prioritizing transitions based on TD error? 
- How does the proposed algorithm compare to other prioritized experience replay algorithms, such as PER [1] and C51 [2]? 
- What is the theoretical guarantee of the proposed algorithm? 
- How does the proposed algorithm perform on other benchmark tasks, such as MuJoCo? 

[1] Hessel, Matteo, et al. "Rainbow: Combining improvements in deep reinforcement learning." arXiv preprint arXiv:1704.06664 (2017). 
[2] Wang, Ziyu, et al. "Distributed prioritized experience replay." arXiv preprint arXiv:1803.00933 (2018).

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a prioritized experience replay algorithm for reinforcement learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed algorithm is simple and intuitive.
- The results are promising.

### Weaknesses

- The proposed algorithm is not novel. The idea of prioritizing transitions based on TD error is not new. The authors should cite prior work [1] that also proposes prioritized experience replay for deep Q-learning.
- The experimental results are not convincing. The proposed algorithm does not perform well on all games. For example, it performs worse than uniform sampling on 8 games (Table 6). The performance gain is also not significant on many games. For example, the performance gain on Montezuma's Revenge is only 2.5% (Table 6).
- The proposed algorithm is not well-motivated. The authors claim that prioritized experience replay can improve the efficiency of deep Q-learning. However, they do not provide any theoretical analysis or empirical evidence to support this claim.

[1] Hessel, Matteo, et al. "Rainbow: Combining improvements in deep reinforcement learning." arXiv preprint arXiv:1704.06664 (2017).

### Questions

- What is the motivation for prioritizing transitions based on TD error? 
- How does the proposed algorithm compare to other prioritized experience replay algorithms, such as PER [1] and C51 [2]? 
- What is the theoretical guarantee of the proposed algorithm? 
- How does the proposed algorithm perform on other benchmark tasks, such as MuJoCo? 

[1] Hessel, Matteo, et al. "Rainbow: Combining improvements in deep reinforcement learning." arXiv preprint arXiv:1704.06664 (2017). 
[2] Wang, Ziyu, et al. "Distributed prioritized experience replay." arXiv preprint arXiv:1803.00933 (2018).

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a prioritized experience replay method for DQN. The key idea is to prioritize the replay of transitions with large TD error. The authors also propose to use stochastic prioritization and importance sampling to address the issue of diversity and bias. The authors show that the proposed method can achieve better performance on Atari games compared to the baseline DQN.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and intuitive.

### Weaknesses

The main weakness of this paper is the limited novelty of the proposed method. The idea of prioritizing transitions with large TD error is not new. The authors should cite prior work [1] that also proposes prioritized experience replay for deep Q-learning. 

[1] Hessel, Matteo, et al. "Rainbow: Combining improvements in deep reinforcement learning." arXiv preprint arXiv:1704.06664 (2017).

### Questions

None

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a prioritized experience replay method for DQN. The key idea is to prioritize the replay of transitions with large TD error. The authors also propose to use stochastic prioritization and importance sampling to address the issue of diversity and bias. The authors show that the proposed method can achieve better performance on Atari games compared to the baseline DQN.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and intuitive. The authors also provide a good motivation for the proposed method.

### Weaknesses

The main weakness of this paper is the limited novelty of the proposed method. The idea of prioritizing transitions with large TD error is not new. The authors should cite prior work [1] that also proposes prioritized experience replay for deep Q-learning. 

[1] Hessel, Matteo, et al. "Rainbow: Combining improvements in deep reinforcement learning." arXiv preprint arXiv:1704.06664 (2017).

### Questions

None

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

### justification_for_why_not_higher_score

The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject

**********

## Paper Decision Overview

Reject

**********

## Paper Decision Comments

Thanks for your submission to ICLR.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about the novelty of the proposed algorithm, the experimental results, and the motivation. The authors did not provide a response to the reviewers' comments.

**********

**********

## Paper Decision Policy

Unacceptable

**********

## Paper Decision Type

Reject (Reject, not good enough)

**********

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision Justification

Unacceptable

**********

## Paper Decision Category

Reject (not good enough)

**********

## Paper Decision Comment

This paper proposes a prioritized experience replay algorithm for deep Q-learning, which samples transitions from the replay buffer based on their TD error. The proposed algorithm is tested on the Atari 2600 benchmark suite and shows improved performance compared to uniform sampling. The reviewers raised concerns about