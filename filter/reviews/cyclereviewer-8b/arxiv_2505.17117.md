## Reviewer

### Summary

The paper investigates how LLMs and humans navigate the compression-meaning trade-off in conceptual representation. The authors apply an Information Bottleneck framework to compare human conceptual structure with embeddings from 40+ LLMs using classic categorization benchmarks. They find that LLMs broadly agree with human category boundaries, yet fall short on fine-grained semantic distinctions. The authors also analyze encoder models and decoder models, revealing that encoder models outperform decoder models in human alignment, suggesting that understanding and generation rely on distinct representational mechanisms. The paper also explores the training dynamics of LLMs, revealing a two-phase trajectory: rapid initial concept formation followed by architectural reorganization, during which semantic processing migrates from deep to mid-network layers as the model discovers increasingly efficient, sparser encodings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a comprehensive analysis of the compression-meaning trade-off in conceptual representation, comparing human and LLMs.
3. The paper offers a novel framework for evaluating the trade-off between compression and meaning in LLMs.
4. The paper provides a detailed analysis of the training dynamics of LLMs, revealing a two-phase trajectory.

### Weaknesses

1. The paper could benefit from a more detailed discussion of the limitations of the Information Bottleneck framework and how it may not fully capture the complexity of human cognition.
2. The paper could benefit from a more detailed discussion of the implications of the findings for the development of LLMs and their applications.
3. The paper could benefit from a more detailed discussion of the potential risks and challenges associated with the use of LLMs in various domains.
4. The paper could benefit from a more detailed discussion of the potential ethical implications of the findings and how they may impact the development of AI systems that are more human-like.

### Questions

1. How do the authors plan to address the limitations of the Information Bottleneck framework in future work?
2. How do the authors plan to incorporate the findings of the paper into the development of LLMs and their applications?
3. What are the potential risks and challenges associated with the use of LLMs in various domains?
4. How do the authors plan to address the potential ethical implications of the findings and how they may impact the development of AI systems that are more human-like?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper compares the LLMs and humans on the compression vs meaning trade-off, using the information bottleneck framework. The authors digitize and release three classic datasets from cognitive psychology, which are then used to compare the LLMs and humans. The authors find that LLMs are better at compression, but worse at meaning. The authors also find that encoder models are better at compression and meaning than decoder models, and that the compression and meaning trade-off is different for LLMs and humans.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well written and easy to follow.
2. The authors digitize and release classic datasets from cognitive psychology, which will be useful for future research.
3. The paper is the first to compare LLMs and humans on the compression vs meaning trade-off, which is an important question for understanding LLMs.
4. The authors provide a thorough analysis of the results and discuss the implications for future research.

### Weaknesses

1. The paper only compares LLMs to humans on a limited set of tasks, which may not be representative of all tasks that LLMs are used for.
2. The paper does not provide a clear explanation for why LLMs are better at compression than meaning, or why encoder models are better at compression and meaning than decoder models.
3. The paper does not provide a clear explanation for why the compression and meaning trade-off is different for LLMs and humans.

### Questions

1. Why are LLMs better at compression than meaning? Is this because they are trained on a large corpus of text that contains many examples of compression?
2. Why are encoder models better at compression and meaning than decoder models? Is this because encoder models are trained on a smaller corpus of text that contains fewer examples of compression?
3. Why is the compression and meaning trade-off different for LLMs and humans? Is this because LLMs are trained on a large corpus of text that contains many examples of compression, while humans are not?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper investigates the conceptual representations in LLMs by comparing them with human conceptual structures. The authors digitize and release classic datasets from cognitive psychology, which are used to compare the LLMs and humans. They find that LLMs are better at compression but worse at meaning. They also find that encoder models are better at compression and meaning than decoder models. Finally, they find that the compression and meaning trade-off is different for LLMs and humans.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors digitize and release classic datasets from cognitive psychology, which will be useful for future research.
3. The paper is the first to compare LLMs and humans on the compression vs meaning trade-off, which is an important question for understanding LLMs.
4. The authors provide a thorough analysis of the results and discuss the implications for future research.

### Weaknesses

1. The paper only compares LLMs to humans on a limited set of tasks, which may not be representative of all tasks that LLMs are used for.
2. The paper does not provide a clear explanation for why LLMs are better at compression than meaning, or why encoder models are better at compression and meaning than decoder models.
3. The paper does not provide a clear explanation for why the compression and meaning trade-off is different for LLMs and humans.

### Questions

1. Why are LLMs better at compression than meaning? Is this because they are trained on a large corpus of text that contains many examples of compression?
2. Why are encoder models better at compression and meaning than decoder models? Is this because encoder models are trained on a smaller corpus of text that contains fewer examples of compression?
3. Why is the compression and meaning trade-off different for LLMs and humans? Is this because LLMs are trained on a large corpus of text that contains many examples of compression, while humans are not?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper studies the concept formation in LLMs by comparing them with human concept formation. The authors digitize and release classic datasets from cognitive psychology, which are used to compare the LLMs and humans. The authors find that LLMs are better at compression but worse at meaning. They also find that encoder models are better at compression and meaning than decoder models. Finally, they find that the compression and meaning trade-off is different for LLMs and humans.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. This paper is the first to compare LLMs and humans on the compression vs meaning trade-off, which is an important question for understanding LLMs.
3. The authors digitize and release classic datasets from cognitive psychology, which will be useful for future research.
4. The authors provide a thorough analysis of the results and discuss the implications for future research.

### Weaknesses

1. The authors use the mutual information to measure the compression, which is not very convincing. I think the authors should use the entropy to measure the compression.
2. The authors use the distortion to measure the meaning, which is not very convincing. I think the authors should use the semantic similarity to measure the meaning.
3. The authors only use the classic datasets from cognitive psychology to compare the LLMs and humans, which is not enough. I think the authors should use more datasets to compare the LLMs and humans.

### Questions

1. Why do the authors use the mutual information to measure the compression? Why not use the entropy?
2. Why do the authors use the distortion to measure the meaning? Why not use the semantic similarity?
3. Why do the authors only use the classic datasets from cognitive psychology to compare the LLMs and humans? Why not use more datasets?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

This paper presents a thorough analysis of the compression-meaning trade-off in conceptual representation, comparing human and LLMs. The authors digitize and release classic datasets from cognitive psychology, which are used to compare the LLMs and humans. They find that LLMs are better at compression but worse at meaning. They also find that encoder models are better at compression and meaning than decoder models. Finally, they find that the compression and meaning trade-off is different for LLMs and humans.

Strengths: The paper is well-written and easy to follow. The authors digitize and release classic datasets from cognitive psychology, which will be useful for future research. The paper is the first to compare LLMs and humans on the compression vs meaning trade-off, which is an important question for understanding LLMs. The authors provide a thorough analysis of the results and discuss the implications for future research.

Weaknesses: The paper only compares LLMs to humans on a limited set of tasks, which may not be representative of all tasks that LLMs are used for. The paper does not provide a clear explanation for why LLMs are better at compression than meaning, or why encoder models are better at compression and meaning than decoder models. The paper does not provide a clear explanation for why the compression and meaning trade-off is different for LLMs and humans.

### justification_for_why_not_higher_score

The paper only compares LLMs to humans on a limited set of tasks, which may not be representative of all tasks that LLMs are used for. The paper does not provide a clear explanation for why LLMs are better at compression than meaning, or why encoder models are better at compression and meaning than decoder models. The paper does not provide a clear explanation for why the compression and meaning trade-off is different for LLMs and humans.

### justification_for_why_not_lower_score

The paper is well-written and easy to follow. The authors digitize and release classic datasets from cognitive psychology, which will be useful for future research. The paper is the first to compare LLMs and humans on the compression vs meaning trade-off, which is an important question for understanding LLMs. The authors provide a thorough analysis of the results and discuss the implications for future research.

**********

## Paper Decision

Accept (poster) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral) (poster) (spotlight) (oral)