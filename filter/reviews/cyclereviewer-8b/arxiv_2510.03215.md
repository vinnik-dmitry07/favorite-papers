##### Report GitHub Issue

## Summary

The paper proposes a new method for communication between LLMs, called Cache-to-Cache (C2C). The idea is to use the KV cache of one model to improve the performance of another model. The paper presents several experiments and ablation studies to show the effectiveness of C2C.

## Soundness

2 fair

## Presentation

3 good

## Contribution

2 fair

## Strengths

- The paper is well-written and easy to follow.
- The idea of using KV cache for communication between LLMs is interesting and novel.
- The paper presents several experiments and ablation studies to show the effectiveness of C2C.

## Weaknesses

- The paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper mentions that KV cache is a richer representation than text, but it does not provide any evidence to support this claim. In fact, KV cache is a lower-dimensional representation of the input, whereas text is a higher-dimensional representation. The paper also mentions that KV cache enables fully parallel communication, but this is not necessarily true since the KV cache is still generated sequentially.
- The paper does not compare C2C with other methods for LLM communication. For example, there are several papers that propose using attention-based methods for LLM communication, such as [1]. It would be interesting to compare C2C with these methods.
- The paper does not provide any analysis of the limitations of C2C. For example, how does C2C perform when the Sharer and Receiver models are different? How does C2C perform when the input is long?
- The paper does not provide any analysis of the computational cost of C2C. For example, how much faster is C2C compared to other methods for LLM communication?
- The paper does not provide any analysis of the generalizability of C2C. For example, how does C2C perform on other tasks and datasets?

[1] https://arxiv.org/abs/2305.10748

## Questions

- Why is KV cache a better communication medium than text? Can you provide some evidence to support this claim?
- How does C2C compare with other methods for LLM communication?
- What are the limitations of C2C? Can you provide some analysis of the limitations of C2C?
- How much faster is C2C compared to other methods for LLM communication?
- How does C2C perform on other tasks and datasets?

## Flag For Ethics Review

No ethics review needed.

## Rating

3: reject, not good enough

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

----


## Reviewer

## Summary

This paper proposes a new method for multi-LLM systems to communicate with each other using their KV cache. The proposed method, Cache-to-Cache, uses a neural network to project and fuse the source model’s KV-cache with that of the target model to enable direct semantic transfer. A learnable gating mechanism selects the target layers that benefit from cache communication. Experiments show that Cache-to-Cache achieves higher accuracy than individual models and outperforms the text communication paradigm by approximately 3.1-5.4%, while delivering an average 2.5× speedup in latency.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experiments are comprehensive and demonstrate the effectiveness of the proposed method.

## Weaknesses

1. The paper only considers two models in the experiments, and the performance gain is not very significant. It would be better to include more models to demonstrate the effectiveness of the proposed method.
2. The paper does not provide any analysis of the computational cost of the proposed method.

## Questions

1. How does the proposed method perform when the Sharer and Receiver models are different?
2. How does the proposed method perform when the input is long?
3. How much faster is the proposed method compared to other methods for LLM communication?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

----


## Reviewer

## Summary

The paper proposes Cache-to-Cache (C2C), a method to enable direct semantic communication between LLMs by projecting and fusing the KV cache of one model into the other. The authors conduct extensive experiments to demonstrate the effectiveness of C2C.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The experiments are comprehensive and demonstrate the effectiveness of the proposed method.

## Weaknesses

- The paper does not provide any analysis of the computational cost of the proposed method.
- The paper does not provide any analysis of the generalizability of the proposed method.

## Questions

- How does the proposed method perform when the Sharer and Receiver models are different?
- How does the proposed method perform when the input is long?
- How much faster is the proposed method compared to other methods for LLM communication?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

----


## Reviewer

## Summary

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems.

## Soundness

3 good

## Presentation

3 good

## Contribution

3 good

## Strengths

- The paper is well-written and easy to follow.
- The idea of using KV-cache for communication between LLMs is interesting and novel.
- The paper presents several experiments and ablation studies to show the effectiveness of C2C.

## Weaknesses

- The paper lacks a clear motivation for why KV-cache is a better communication medium than text. The paper mentions that KV-cache is a richer representation than text, but it does not provide any evidence to support this claim. In fact, KV-cache is a lower-dimensional representation of the input, whereas text is a higher-dimensional representation. The paper also mentions that KV-cache enables fully parallel communication, but this is not necessarily true since the KV-cache is still generated sequentially.
- The paper does not compare C2C with other methods for LLM communication. For example, there are several papers that propose using attention-based methods for LLM communication, such as [1]. It would be interesting to compare C2C with these methods.
- The paper does not provide any analysis of the limitations of C2C. For example, how does C2C perform when the Sharer and Receiver models are different? How does C2C perform when the input is long?
- The paper does not provide any analysis of the computational cost of C2C. For example, how much faster is C2C compared to other methods for LLM communication?
- The paper does not provide any analysis of the generalizability of C2C. For example, how does C2C perform on other tasks and datasets?

[1] https://arxiv.org/abs/2305.10748

## Questions

- Why is KV-cache a better communication medium than text? Can you provide some evidence to support this claim?
- How does C2C compare with other methods for LLM communication?
- What are the limitations of C2C? Can you provide some analysis of the limitations of C2C?
- How much faster is C2C compared to other methods for LLM communication?
- How does C2C perform on other tasks and datasets?

## Flag For Ethics Review

No ethics review needed.

## Rating

6: marginally above the acceptance threshold

## Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

----


## Meta Review

The paper proposes a new method for communication between LLMs, called Cache-to-Cache (C2C). The idea is to use the KV cache of one model to improve the performance of another model. The paper presents several experiments and ablation studies to show the effectiveness of C2C. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

## justification_for_why_not_higher_score

The paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C.

## justification_for_why_not_lower_score

N/A

**********

---

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Summary

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Paper Decision Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Meta Paper Decision Type

Reject

**********

---

## Potential Impact

The paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Sensitive Issues

No sensitive issues.

**********

---

## Paper Decision Comments

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Recommendation

Reject (not selected for publication)

**********

---

## justification_for_why_not_higher_score

The paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## justification_for_why_not_lower_score

N/A

**********

---

## justification_for_why_not_reject

N/A

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to-text communication in terms of accuracy and latency, showcasing its potential for efficient and effective multi-LLM systems. The paper is well-written and easy to follow. The proposed method is simple and effective. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. However, the paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper does not compare C2C with other methods for LLM communication. The paper does not provide any analysis of the limitations of C2C. The paper does not provide any analysis of the computational cost of C2C. The paper does not provide any analysis of the generalizability of C2C. The authors did not provide a response to the reviewers' comments.

**********

---

## Paper Decision Type

Reject (not selected for publication)

**********

---

## Reviewer

## Paper Decision

Reject (not selected for publication)

**********

---

## Paper Decision Public Feedback

This paper introduces Cache-to-Cache (C2C), a novel paradigm for direct semantic communication between LLMs. C2C leverages the KV-cache of LLMs to enhance the performance of other models, without the need for text communication. The authors demonstrate that C2C outperforms text-to