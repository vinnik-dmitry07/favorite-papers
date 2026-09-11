## Reviewer

### Summary

This paper proposes a novel communication protocol for heterogeneous LLMs. The proposed method is based on the observation that the current communication methods either discard the sender’s internal representations or require architectural homogeneity for latent-level transfer. The authors propose a decode-free communication protocol that addresses this through two mechanisms: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps the sender’s original context tokens to the receiver’s vocabulary, providing discrete entity anchors. LEB lets the receiver query the sender’s hidden states for contextual enrichment. The proposed method is evaluated on three model families (Llama, Qwen, and Mistral) and seven benchmarks, and it outperforms text-based communication on all seven tasks for each model pair while achieving 11x lower latency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and the idea is simple and effective.
3. The proposed method achieves state-of-the-art performance on the evaluated benchmarks.

### Weaknesses

1. The proposed method is only evaluated on a limited set of benchmarks, and it is unclear how the method will perform on other tasks.
2. The method requires training a separate bridge for each sender-receiver pair, which may be computationally expensive.
3. The method assumes that the sender and receiver have the same vocabulary, which may not always be the case in real-world applications.

### Questions

1. How does the proposed method perform on other tasks, such as question-answering and text summarization?
2. How computationally expensive is it to train a separate bridge for each sender-receiver pair?
3. How does the method perform when the sender and receiver have different vocabularies?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper presents a novel communication protocol for heterogeneous LLMs that addresses the entity grounding problem in cross-architecture communication. The proposed method, XBridge, consists of two mechanisms: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps the sender's original context tokens to the receiver's vocabulary, providing discrete entity anchors, while LEB lets the receiver query the sender's hidden states for contextual enrichment. The proposed method is evaluated on three model families (Llama, Qwen, and Mistral) and seven benchmarks, and it outperforms text-based communication on all seven tasks for each model pair while achieving 11x lower latency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and the idea is simple and effective.
3. The proposed method achieves state-of-the-art performance on the evaluated benchmarks.

### Weaknesses

1. The proposed method is only evaluated on a limited set of benchmarks, and it is unclear how the method will perform on other tasks.
2. The method requires training a separate bridge for each sender-receiver pair, which may be computationally expensive.
3. The method assumes that the sender and receiver have the same vocabulary, which may not always be the case in real-world applications.

### Questions

1. How does the proposed method perform on other tasks, such as question-answering and text summarization?
2. How computationally expensive is it to train a separate bridge for each sender-receiver pair?
3. How does the method perform when the sender and receiver have different vocabularies?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces a new communication protocol for heterogeneous LLMs, which is called XBridge. XBridge consists of two modules: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps the sender's original context tokens to the receiver's vocabulary, providing discrete entity anchors. LEB lets the receiver query the sender's hidden states for contextual enrichment. The proposed method is evaluated on three model families (Llama, Qwen, and Mistral) and seven benchmarks, and it outperforms text-based communication on all seven tasks for each model pair while achieving 11x lower latency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and the idea is simple and effective.
3. The proposed method achieves state-of-the-art performance on the evaluated benchmarks.

### Weaknesses

1. The proposed method is only evaluated on a limited set of benchmarks, and it is unclear how the method will perform on other tasks.
2. The method requires training a separate bridge for each sender-receiver pair, which may be computationally expensive.
3. The method assumes that the sender and receiver have the same vocabulary, which may not always be the case in real-world applications.

### Questions

1. How does the proposed method perform on other tasks, such as question-answering and text summarization?
2. How computationally expensive is it to train a separate bridge for each sender-receiver pair?
3. How does the method perform when the sender and receiver have different vocabularies?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a novel communication protocol for heterogeneous LLMs. The proposed method is based on the observation that the current communication methods either discard the sender’s internal representations or require architectural homogeneity for latent-level transfer. The authors propose a decode-free communication protocol that addresses this through two mechanisms: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps the sender’s original context tokens to the receiver’s vocabulary, providing discrete entity anchors. LEB lets the receiver query the sender’s hidden states for contextual enrichment. The proposed method is evaluated on three model families (Llama, Qwen, and Mistral) and seven benchmarks, and it outperforms text-based communication on all seven tasks for each model pair while achieving 11x lower latency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and the idea is simple and effective.
3. The proposed method achieves state-of-the-art performance on the evaluated benchmarks.

### Weaknesses

1. The proposed method is only evaluated on a limited set of benchmarks, and it is unclear how the method will perform on other tasks.
2. The method requires training a separate bridge for each sender-receiver pair, which may be computationally expensive.
3. The method assumes that the sender and receiver have the same vocabulary, which may not always be the case in real-world applications.

### Questions

1. How does the proposed method perform on other tasks, such as question-answering and text summarization?
2. How computationally expensive is it to train a separate bridge for each sender-receiver pair?
3. How does the method perform when the sender and receiver have different vocabularies?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents a novel communication protocol for heterogeneous LLMs. The proposed method, XBridge, consists of two mechanisms: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps the sender's original context tokens to the receiver's vocabulary, providing discrete entity anchors, while LEB lets the receiver query the sender's hidden states for contextual enrichment. The proposed method is evaluated on three model families (Llama, Qwen, and Mistral) and seven benchmarks, and it outperforms text-based communication on all seven tasks for each model pair while achieving 11x lower latency.

The paper is well-written and easy to follow. The proposed method is well-motivated and the idea is simple and effective. The proposed method achieves state-of-the-art performance on the evaluated benchmarks.

### justification_for_why_not_higher_score

The proposed method is only evaluated on a limited set of benchmarks, and it is unclear how the method will perform on other tasks. The method requires training a separate bridge for each sender-receiver pair, which may be computationally expensive. The method assumes that the sender and receiver have the same vocabulary, which may not always be the case in real-world applications.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The proposed method is well-motivated and the idea is simple and effective. The proposed method achieves state-of-the-art performance on the evaluated benchmarks.

**********

## Paper Decision

Reject (not selected for spotlight/oral/poster)

**********

## Paper Decision Summary

This paper was reviewed by 4 members of the program committee. The final score was -0.5. The paper received 4 borderline accept ratings. The reviewers raised some concerns regarding the evaluation and the generalizability of the proposed method. The authors provided a detailed response to the reviewers. After considering the reviews, author response, and discussion, the paper was not selected for publication at ICLR 2024.

**********

## Paper Decision Comments

Dear Authors,

Thank you for your submission and for your hard work on this paper. We appreciate the effort you put into preparing your submission and the time you took to respond to the reviewers’ comments and questions. 

While the paper received borderline accept ratings, the reviewers raised some concerns regarding the evaluation and the generalizability of the proposed method. Unfortunately, the authors did not provide a response to these concerns in their author response. We understand that the authors might not have had the time to address all the comments, but we hope that they will consider the reviewers’ comments and suggestions in future work.

We encourage you to take the reviewers’ comments into consideration and submit an improved version of your paper to a future venue.

Best regards,

ICLR 2024 Paper Decision Committee

**********

## Paper Decision Type

Reject (not selected for spotlight/oral/poster)

**********

## Paper Decision Category

Other (please specify in the remark)

**********

## Remark

The paper was not selected for publication at ICLR 2024.

**********

## Paper Decision Comments

Dear Authors,

Thank you for your submission and for your hard work on this paper. We appreciate the effort you put into preparing your submission and the time you took to respond to the reviewers’ comments and questions. 

While the paper received borderline accept ratings, the reviewers raised some concerns regarding the evaluation and the generalizability of the proposed method. Unfortunately, the authors did not provide a response to these concerns in their author response. We understand that the authors might not have had the time to address all the comments, but we hope that they will consider the reviewers’ comments and suggestions in future work.

We encourage you to take the reviewers’ comments into consideration and submit an improved version of your paper to a future venue.

Best regards,

ICLR 2024 Paper Decision Committee

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

**********

********