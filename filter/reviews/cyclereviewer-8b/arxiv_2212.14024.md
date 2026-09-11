## Reviewer

### Summary

This paper introduces the Demonstrate – Search – Predict (DSP) framework for retrieval-augmented in-context learning. DSP is a composable framework that consists of three stages: Demonstrate, Search, and Predict. It uses natural language text and scores to communicate between a frozen retrieval model (RM) and a language model (LM). The authors demonstrate the effectiveness of DSP on three knowledge-intensive tasks: open-domain question answering, multi-hop question answering, and conversational question answering. The results show that DSP outperforms previous in-context learning approaches by a significant margin.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the DSP framework and its components. The evaluation is comprehensive, covering three knowledge-intensive tasks. The results are promising, with significant improvements over previous in-context learning approaches.

### Weaknesses

The paper lacks a clear motivation for the DSP framework. The authors should provide a more detailed explanation of the limitations of existing retrieval-augmented in-context learning approaches and how DSP addresses these limitations.

The paper does not provide a clear comparison with existing retrieval-augmented in-context learning approaches. The authors should compare DSP with other state-of-the-art approaches in the field and discuss the advantages and disadvantages of DSP compared to these approaches.

The paper does not provide a clear evaluation of the robustness and generalizability of DSP. The authors should evaluate DSP on a wider range of tasks and datasets to demonstrate its robustness and generalizability.

### Questions

How does DSP compare to other retrieval-augmented in-context learning approaches in terms of performance and efficiency?

How does DSP perform on other knowledge-intensive tasks beyond open-domain question answering, multi-hop question answering, and conversational question answering?

How does DSP handle out-of-domain or out-of-vocabulary queries?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper proposes a framework for retrieval-augmented in-context learning, called Demonstrate – Search – Predict (DSP), which is a framework that relies on passing natural language texts in sophisticated pipelines between an LM and an RM. DSP can express high-level programs that bootstrap pipeline-aware demonstrations, search for relevant passages, and generate grounded predictions, systematically breaking down problems into small transformations that the LM and RM can handle more reliably. The authors have written novel DSP programs for answering questions in open-domain, multi-hop, and conversational settings, establishing in early evaluations new state-of-the-art in-context learning results and delivering 37–120%, 8–39%, and 80–290% relative gains against the vanilla LM (GPT-3.5), a standard retrieve-then-read pipeline, and a contemporaneous self-ask pipeline, respectively. They release DSP at https://github.com/stanfordnlp/dsp.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the DSP framework and its components. The evaluation is comprehensive, covering three knowledge-intensive tasks. The results are promising, with significant improvements over previous in-context learning approaches.

2. The paper introduces a novel framework for retrieval-augmented in-context learning, called Demonstrate – Search – Predict (DSP), which is a framework that relies on passing natural language texts in sophisticated pipelines between an LM and an RM. DSP can express high-level programs that bootstrap pipeline-aware demonstrations, search for relevant passages, and generate grounded predictions, systematically breaking down problems into small transformations that the LM and RM can handle more reliably.

3. The paper demonstrates the effectiveness of DSP on three knowledge-intensive tasks: open-domain question answering, multi-hop question answering, and conversational question answering. The results show that DSP outperforms previous in-context learning approaches by a significant margin.

### Weaknesses

1. The paper lacks a clear motivation for the DSP framework. The authors should provide a more detailed explanation of the limitations of existing retrieval-augmented in-context learning approaches and how DSP addresses these limitations.

2. The paper does not provide a clear comparison with existing retrieval-augmented in-context learning approaches. The authors should compare DSP with other state-of-the-art approaches in the field and discuss the advantages and disadvantages of DSP compared to these approaches.

3. The paper does not provide a clear evaluation of the robustness and generalizability of DSP. The authors should evaluate DSP on a wider range of tasks and datasets to demonstrate its robustness and generalizability.

### Questions

1. How does DSP compare to other retrieval-augmented in-context learning approaches in terms of performance and efficiency?

2. How does DSP perform on other knowledge-intensive tasks beyond open-domain question answering, multi-hop question answering, and conversational question answering?

3. How does DSP handle out-of-domain or out-of-vocabulary queries?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces the Demonstrate – Search – Predict (DSP) framework for retrieval-augmented in-context learning. DSP is a composable framework that consists of three stages: Demonstrate, Search, and Predict. It uses natural language text and scores to communicate between a frozen retrieval model (RM) and a language model (LM). The authors demonstrate the effectiveness of DSP on three knowledge-intensive tasks: open-domain question answering, multi-hop question answering, and conversational question answering. The results show that DSP outperforms previous in-context learning approaches by a significant margin.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the DSP framework and its components. The evaluation is comprehensive, covering three knowledge-intensive tasks. The results are promising, with significant improvements over previous in-context learning approaches.

2. The paper introduces a novel framework for retrieval-augmented in-context learning, called Demonstrate – Search – Predict (DSP), which is a framework that relies on passing natural language texts in sophisticated pipelines between an LM and an RM. DSP can express high-level programs that bootstrap pipeline-aware demonstrations, search for relevant passages, and generate grounded predictions, systematically breaking down problems into small transformations that the LM and RM can handle more reliably.

3. The paper demonstrates the effectiveness of DSP on three knowledge-intensive tasks: open-domain question answering, multi-hop question answering, and conversational question answering. The results show that DSP outperforms previous in-context learning approaches by a significant margin.

### Weaknesses

1. The paper lacks a clear motivation for the DSP framework. The authors should provide a more detailed explanation of the limitations of existing retrieval-augmented in-context learning approaches and how DSP addresses these limitations.

2. The paper does not provide a clear comparison with existing retrieval-augmented in-context learning approaches. The authors should compare DSP with other state-of-the-art approaches in the field and discuss the advantages and disadvantages of DSP compared to these approaches.

3. The paper does not provide a clear evaluation of the robustness and generalizability of DSP. The authors should evaluate DSP on a wider range of tasks and datasets to demonstrate its robustness and generalizability.

### Questions

1. How does DSP compare to other retrieval-augmented in-context learning approaches in terms of performance and efficiency?

2. How does DSP perform on other knowledge-intensive tasks beyond open-domain question answering, multi-hop question answering, and conversational question answering?

3. How does DSP handle out-of-domain or out-of-vocabulary queries?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer

### Summary

This paper introduces the Demonstrate – Search – Predict (DSP) framework for retrieval-augmented in-context learning. DSP is a composable framework that consists of three stages: Demonstrate, Search, and Predict. It uses natural language text and scores to communicate between a frozen retrieval model (RM) and a language model (LM). The authors demonstrate the effectiveness of DSP on three knowledge-intensive tasks: open-domain question answering, multi-hop question answering, and conversational question answering. The results show that DSP outperforms previous in-context learning approaches by a significant margin.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the DSP framework and its components. The evaluation is comprehensive, covering three knowledge-intensive tasks. The results are promising, with significant improvements over previous in-context learning approaches.

2. The paper introduces a novel framework for retrieval-augmented in-context learning, called Demonstrate – Search – Predict (DSP), which is a framework that relies on passing natural language texts in sophisticated pipelines between an LM and an RM. DSP can express high-level programs that bootstrap pipeline-aware demonstrations, search for relevant passages, and generate grounded predictions, systematically breaking down problems into small transformations that the LM and RM can handle more reliably.

3. The paper demonstrates the effectiveness of DSP on three knowledge-intensive tasks: open-domain question answering, multi-hop question answering, and conversational question answering. The results show that DSP outperforms previous in-context learning approaches by a significant margin.

### Weaknesses

1. The paper lacks a clear motivation for the DSP framework. The authors should provide a more detailed explanation of the limitations of existing retrieval-augmented in-context learning approaches and how DSP addresses these limitations.

2. The paper does not provide a clear comparison with existing retrieval-augmented in-context learning approaches. The authors should compare DSP with other state-of-the-art approaches in the field and discuss the advantages and disadvantages of DSP compared to these approaches.

3. The paper does not provide a clear evaluation of the robustness and generalizability of DSP. The authors should evaluate DSP on a wider range of tasks and datasets to demonstrate its robustness and generalizability.

### Questions

1. How does DSP compare to other retrieval-augmented in-context learning approaches in terms of performance and efficiency?

2. How does DSP perform on other knowledge-intensive tasks beyond open-domain question answering, multi-hop question answering, and conversational question answering?

3. How does DSP handle out-of-domain or out-of-vocabulary queries?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper presents a framework for retrieval-augmented in-context learning, called Demonstrate – Search – Predict (DSP). DSP is a composable framework that consists of three stages: Demonstrate, Search, and Predict. It uses natural language text and scores to communicate between a frozen retrieval model (RM) and a language model (LM). The authors demonstrate the effectiveness of DSP on three knowledge-intensive tasks: open-domain question answering, multi-hop question answering, and conversational question answering. The results show that DSP outperforms previous in-context learning approaches by a significant margin.

### justification_for_why_not_higher_score

The paper lacks a clear motivation for the DSP framework. The authors should provide a more detailed explanation of the limitations of existing retrieval-augmented in-context learning approaches and how DSP addresses these limitations.

### justification_for_why_not_lower_score

The paper introduces a novel framework for retrieval-augmented in-context learning, called Demonstrate – Search – Predict (DSP), which is a framework that relies on passing natural language texts in sophisticated pipelines between an LM and an RM. DSP can express high-level programs that bootstrap pipeline-aware demonstrations, search for relevant passages, and generate grounded predictions, systematically breaking down problems into small transformations that the LM and RM can handle more reliably.

**********

## Paper Decision

Accept (poster)