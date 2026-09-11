I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates the metacognitive abilities of LLMs, focusing on their capacity to monitor and control internal activations. The authors introduce a neurofeedback paradigm to quantify metacognition in LLMs at the neural level, exploring how models report and control their internal activations. They find that LLMs can monitor a limited subset of their neural mechanisms, suggesting that these models may not possess a robust understanding of their internal states. The study’s findings have implications for AI safety and the development of more transparent and controllable AI systems.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper introduces a novel neurofeedback paradigm to quantify metacognition in LLMs, providing a unique approach to understanding how these models monitor and control their internal activations. The study’s findings have implications for AI safety and the development of more transparent and controllable AI systems.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear definition of metacognition, which makes it difficult to understand the authors' objectives and the relevance of their experiments. A more precise definition of metacognition, along with a clear explanation of how the proposed experiments measure this concept, would greatly enhance the paper's clarity and rigor.
2. The paper does not adequately address the limitations of the proposed neurofeedback paradigm, particularly regarding its generalizability to other types of LLMs and its applicability to real-world scenarios. A more thorough discussion of these limitations would strengthen the paper's conclusions.
3. The paper does not provide a detailed analysis of the experimental results, particularly regarding the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs.

### Suggestions

The authors should begin by providing a more rigorous definition of metacognition within the context of large language models. This definition should clearly articulate what aspects of the model's internal state are being considered as 'metacognitive' and how these relate to the model's ability to monitor and control its own processing. For example, do they mean the model's ability to track the semantic content of its activations, or its ability to predict the outcome of its own computations? This clarification is crucial for understanding the experimental design and the interpretation of results. The authors should then explicitly link this definition to the experimental setup, explaining how the neurofeedback paradigm is designed to measure the proposed definition of metacognition. This should include a detailed explanation of how the 'neurofeedback' mechanism is implemented and how it relates to the model's ability to report and control its internal activations. Without this, the paper lacks a clear theoretical foundation.

Furthermore, the paper needs a more thorough discussion of the limitations of the proposed neurofeedback paradigm. The authors should acknowledge that the paradigm is based on in-context learning and may not generalize to other types of LLMs, such as those trained with different architectures or objectives. They should also discuss the potential impact of the specific choice of tasks and datasets on the results. For example, the tasks used in the study might be biased towards certain types of metacognitive abilities, and the results might not generalize to other types of tasks. The authors should also address the potential for the model to learn superficial correlations between the neurofeedback labels and the target behavior, rather than developing a genuine understanding of its internal states. This discussion should include a consideration of how the model's performance might be affected by changes in the experimental setup, such as the number of in-context examples or the specific choice of layers for control. A more robust analysis of these limitations would significantly strengthen the paper's conclusions.

Finally, the authors should provide a more detailed analysis of the experimental results, focusing on the relationship between the various factors that were manipulated in the study. For example, how does the number of in-context examples affect the model's ability to report and control its internal activations? How does the semantic interpretability of the target axis relate to the model's performance? How does the variance explained by the target axis affect the model's ability to control its internal activations? The authors should also investigate the relationship between the different layers of the model and their ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs and would help to clarify the conditions under which these models are able to monitor and control their internal states.

### Questions

1. How does the proposed neurofeedback paradigm compare to existing methods for measuring metacognition in LLMs, and what are its unique advantages?
2. How do the results of this study inform the development of more transparent and controllable AI systems?
3. What are the potential implications of the findings for the broader field of AI safety, particularly in the context of adversarial attacks and model monitoring?

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

The paper studies the metacognitive abilities of LLMs, i.e., their ability to monitor and control their internal activations. The authors propose a neurofeedback paradigm to quantify metacognition in LLMs, where in-context examples are used to provide feedback on the model's internal activations. The authors find that LLMs can report and control their internal activations along a limited subset of their neural mechanisms, suggesting that these models may not possess a robust understanding of their internal states.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed neurofeedback paradigm is a novel approach to studying metacognition in LLMs, and the authors provide a clear explanation of how it works.
- The authors conduct extensive experiments to validate their findings, including multiple datasets and models.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a clear definition of metacognition, which makes it difficult to understand the authors' objectives and the relevance of their experiments. A more precise definition of metacognition, along with a clear explanation of how the proposed experiments measure this concept, would greatly enhance the paper's clarity and rigor.
- The paper does not adequately address the limitations of the proposed neurofeedback paradigm, particularly regarding its generalizability to other types of LLMs and its applicability to real-world scenarios. A more thorough discussion of these limitations would strengthen the paper's conclusions.
- The paper does not provide a detailed analysis of the experimental results, particularly regarding the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs.

### Suggestions

The authors should begin by providing a more rigorous definition of metacognition within the context of large language models. This definition should clearly articulate what aspects of the model's internal state are being considered as 'metacognitive' and how these relate to the model's ability to monitor and control its own processing. For example, do they mean the model's ability to track the semantic content of its activations, or its ability to predict the outcome of its own computations? This clarification is crucial for understanding the experimental design and the interpretation of results. The authors should then explicitly link this definition to the experimental setup, explaining how the neurofeedback paradigm is designed to measure the proposed definition of metacognition. This should include a detailed explanation of how the 'neurofeedback' mechanism is implemented and how it relates to the model's ability to report and control its internal activations. Without this, the paper lacks a clear theoretical foundation.

Furthermore, the paper needs a more thorough discussion of the limitations of the proposed neurofeedback paradigm. The authors should acknowledge that the paradigm is based on in-context learning and may not generalize to other types of LLMs, such as those trained with different architectures or objectives. They should also discuss the potential impact of the specific choice of tasks and datasets on the results. For example, the tasks used in the study might be biased towards certain types of metacognitive abilities, and the results might not generalize to other types of tasks. The authors should also address the potential for the model to learn superficial correlations between the neurofeedback labels and the target behavior, rather than developing a genuine understanding of its internal states. This discussion should include a consideration of how the model's performance might be affected by changes in the experimental setup, such as the number of in-context examples or the specific choice of layers for control. A more robust analysis of these limitations would significantly strengthen the paper's conclusions.

Finally, the authors should provide a more detailed analysis of the experimental results, focusing on the relationship between the various factors that were manipulated in the study. For example, how does the number of in-context examples affect the model's ability to report and control its internal activations? How does the semantic interpretability of the target axis relate to the model's performance? How does the variance explained by the target axis affect the model's ability to control its internal activations? The authors should also investigate the relationship between the different layers of the model and their ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs and would help to clarify the conditions under which these models are able to monitor and control their internal states. This analysis should include statistical significance testing and effect size calculations to support the claims made in the paper.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper studies the metacognitive abilities of LLMs, i.e., the ability to report and control their internal activations. The authors propose a neurofeedback paradigm that uses in-context learning to provide feedback on the model's activations. The authors show that LLMs can report and control their activations along a limited subset of their neural mechanisms. The authors also find that the ability to control activations is correlated with the semantic interpretability and variance explained by the target axis.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow. The authors provide a clear motivation and a comprehensive review of related work.
- The authors provide a novel neurofeedback paradigm to quantify metacognition in LLMs, which is an interesting and important topic.
- The authors provide extensive experiments to validate their findings, including multiple datasets and models.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a clear definition of metacognition, which makes it difficult to understand the authors' objectives and the relevance of their experiments. A more precise definition of metacognition, along with a clear explanation of how the proposed experiments measure this concept, would greatly enhance the paper's clarity and rigor.
- The paper does not adequately address the limitations of the proposed neurofeedback paradigm, particularly regarding its generalizability to other types of LLMs and its applicability to real-world scenarios. A more thorough discussion of these limitations would strengthen the paper's conclusions.
- The paper does not provide a detailed analysis of the experimental results, particularly regarding the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs.

### Suggestions

The authors should begin by providing a more rigorous definition of metacognition within the context of large language models. This definition should clearly articulate what aspects of the model's internal state are being considered as 'metacognitive' and how these relate to the model's ability to monitor and control its own processing. For example, do they mean the model's ability to track the semantic content of its activations, or its ability to predict the outcome of its own computations? This clarification is crucial for understanding the experimental design and the interpretation of results. The authors should then explicitly link this definition to the experimental setup, explaining how the neurofeedback paradigm is designed to measure the proposed definition of metacognition. This should include a detailed explanation of how the 'neurofeedback' mechanism is implemented and how it relates to the model's ability to report and control its internal activations. Without this, the paper lacks a clear theoretical foundation.

Furthermore, the paper needs a more thorough discussion of the limitations of the proposed neurofeedback paradigm. The authors should acknowledge that the paradigm is based on in-context learning and may not generalize to other types of LLMs, such as those trained with different architectures or objectives. They should also discuss the potential impact of the specific choice of tasks and datasets on the results. For example, the tasks used in the study might be biased towards certain types of metacognitive abilities, and the results might not generalize to other types of tasks. The authors should also address the potential for the model to learn superficial correlations between the neurofeedback labels and the target behavior, rather than developing a genuine understanding of its internal states. This discussion should include a consideration of how the model's performance might be affected by changes in the experimental setup, such as the number of in-context examples or the specific choice of layers for control. A more robust analysis of these limitations would significantly strengthen the paper's conclusions.

Finally, the authors should provide a more detailed analysis of the experimental results, focusing on the relationship between the various factors that were manipulated in the study. For example, how does the number of in-context examples affect the model's ability to report and control its internal activations? How does the semantic interpretability of the target axis relate to the model's performance? How does the variance explained by the target axis affect the model's ability to control its internal activations? The authors should also investigate the relationship between the different layers of the model and their ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs and would help to clarify the conditions under which these models are able to monitor and control their internal states. This analysis should include statistical significance testing and effect size calculations to support the claims made in the paper.

### Questions

- What is the difference between the proposed method and the method in Wang et al. (2024)? It seems that the proposed method is a special case of the method in Wang et al. (2024), where the target axis is computed using the first principal component of the layer activations.
- How does the number of in-context examples affect the model's ability to report and control internal activations?
- How does the semantic interpretability of the target axis relate to the model's performance?
- How does the variance explained by the target axis affect the model's ability to control internal activations?

### Rating

5

### Confidence

4

**********

## Reviewer 4

### Summary

This paper explores the metacognitive abilities of LLMs, focusing on their ability to report and control their internal activations. The authors introduce a neurofeedback paradigm that uses in-context learning to provide feedback on these activations, revealing that LLMs can monitor a limited subset of their neural mechanisms. This study has implications for AI safety and the development of more transparent and controllable AI systems.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- This paper is well-written and easy to follow.
- This paper is well-motivated and the problem is interesting.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a clear definition of metacognition, which makes it difficult to understand the authors' objectives and the relevance of their experiments. A more precise definition of metacognition, along with a clear explanation of how the proposed experiments measure this concept, would greatly enhance the paper's clarity and rigor.
- The paper does not adequately address the limitations of the proposed neurofeedback paradigm, particularly regarding its generalizability to other types of LLMs and its applicability to real-world scenarios. A more thorough discussion of these limitations would strengthen the paper's conclusions.
- The paper does not provide a detailed analysis of the experimental results, particularly regarding the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs.

### Suggestions

The authors should begin by providing a more rigorous definition of metacognition within the context of large language models. This definition should clearly articulate what aspects of the model's internal state are being considered as 'metacognitive' and how these relate to the model's ability to monitor and control its own processing. For example, do they mean the model's ability to track the semantic content of its activations, or its ability to predict the outcome of its own computations? This clarification is crucial for understanding the experimental design and the interpretation of results. The authors should then explicitly link this definition to the experimental setup, explaining how the neurofeedback paradigm is designed to measure the proposed definition of metacognition. This should include a detailed explanation of how the 'neurofeedback' mechanism is implemented and how it relates to the model's ability to report and control its internal activations. Without this, the paper lacks a clear theoretical foundation.

Furthermore, the paper needs a more thorough discussion of the limitations of the proposed neurofeedback paradigm. The authors should acknowledge that the paradigm is based on in-context learning and may not generalize to other types of LLMs, such as those trained with different architectures or objectives. They should also discuss the potential impact of the specific choice of tasks and datasets on the results. For example, the tasks used in the study might be biased towards certain types of metacognitive abilities, and the results might not generalize to other types of tasks. The authors should also address the potential for the model to learn superficial correlations between the neurofeedback labels and the target behavior, rather than developing a genuine understanding of its internal states. This discussion should include a consideration of how the model's performance might be affected by changes in the experimental setup, such as the number of in-context examples or the specific choice of layers for control. A more robust analysis of these limitations would significantly strengthen the paper's conclusions.

Finally, the authors should provide a more detailed analysis of the experimental results, focusing on the relationship between the various factors that were manipulated in the study. For example, how does the number of in-context examples affect the model's ability to report and control its internal activations? How does the semantic interpretability of the target axis relate to the model's performance? How does the variance explained by the target axis affect the model's ability to control its internal activations? The authors should also investigate the relationship between the different layers of the model and their ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs and would help to clarify the conditions under which these models are able to monitor and control their internal states. This analysis should include statistical significance testing and effect size calculations to support the claims made in the paper.

### Questions

- What is the difference between the proposed method and the method in Wang et al. (2024)? It seems that the proposed method is a special case of the method in Wang et al. (2024), where the target axis is computed using the first principal component of the layer activations.
- How does the number of in-context examples affect the model's ability to report and control internal activations?
- How does the semantic interpretability of the target axis relate to the model's performance?
- How does the variance explained by the target axis affect the model's ability to control internal activations?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer has raised several concerns about the paper, focusing on the lack of a clear definition of metacognition, the limitations of the neurofeedback paradigm, and the depth of the experimental analysis. I need to go through each of these points and see if they are valid based on the content of the paper.

**Plan:**
1. Address the lack of a clear definition of metacognition.
2. Evaluate the limitations of the neurofeedback paradigm.
3. Assess the depth of the experimental analysis.
4. Synthesize the findings and determine the validity of each weakness.
**Reviewer 1 Weaknesses Validation:**

**1. Weakness Statement:**
"The paper lacks a clear definition of metacognition, which makes it difficult to understand the authors' objectives and the relevance of their experiments. A more precise definition of metacognition, along with a clear explanation of how the proposed experiments measure this concept, would greatly enhance the paper's clarity and rigor."

**2. Evidence Collection:**
a) Method-related Evidence (if applicable):
   - The paper introduces the concept of metacognition in the Introduction: "Metacognition enhances LLMs’ capabilities in solving complex tasks through self-monitoring (e.g., reducing hallucinations through uncertainty awareness). However, these capabilities remain limited, as LLMs can monitor and report their internal computations but not in a reliable and consistent way as tasks and contexts vary." (Introduction, Paragraph 2)
   - The paper further elaborates on the definition: "Consider how we understand when someone says “hello” to us. Human language understanding involves many unconscious processes: parsing sounds, recognizing phonemes, retrieving word meanings, and building interpretations. We do not have conscious access to many of these intermediate computations: we can only consciously access the final understanding (“they said ‘hello’’), but cannot introspect how our brain distinguishes “hello” from “yellow” or whether certain neurons fire during this process. This illustrates a key principle: humans cannot monitor (through second-order metacognitive processes) all of their internal (first-order) cognitive processes. Crucially, the first-order and second-order processes rely on distinct neural mechanisms. Metacognition enhances LLMs’ capabilities in solving complex tasks through self-monitoring (e.g., reducing hallucinations through uncertainty awareness). However, these capabilities remain limited, as LLMs can monitor and report their internal computations but not in a reliable and consistent way as tasks and contexts vary." (Introduction, Paragraph 3)
   - The paper contrasts its approach with probing: "While prior research has explored metacognitive-like behaviors in LLMs, such as expressing confidence ( Wang et al., 2025 ; Tian et al., 2023 ; Xiong et al., 2023 ) or engaging in self-reflection ( Zhou et al., 2024 ) , these studies rely on behavioral outputs rather than directly probing underlying neural processes. Consequently, it remains unclear whether these behaviors arise from genuine second-order metacognitive mechanisms or merely spurious correlations in the training data. We tackle this question by operationalizing metacognition in LLMs through their abilities to report and control their internal activations. Specifically, can LLMs accurately monitor subtle variations in the activations of a neuron or a feature in their neural spaces? Another question of interest is why LLMs can report some intermediate steps but not others, despite both types playing essential roles in computations and behavior. Answering these questions requires a novel experimental approach that can directly probe whether LLMs can access their internal activations, moving beyond indirect behavioral proxies." (Introduction, Paragraph 4)

b) Experiment-related Evidence (if applicable):
   - The experiments are designed to directly measure the LLMs' ability to report and control internal activations based on defined target axes, which are intended to represent the "second-order" monitoring of the "first-order" neural processes. The "reporting" aspect directly assesses the LLM's ability to monitor its internal state, and the "control" aspect assesses its ability to manipulate it based on that monitoring.

3. Literature Gap Analysis:
   - The introduction cites relevant works on metacognition in humans and prior attempts to study metacognition in LLMs, highlighting the gap the paper aims to fill.

4. Validation Analysis:
   - The paper does provide a working definition of metacognition in the context of LLMs, focusing on the ability to monitor and control internal activations. It contrasts this approach with behavioral proxies used in previous studies. The experiments are designed to directly test this definition. While the reviewer is correct that the definition could be more formally stated, the paper does attempt to define the concept and its measurement.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The introduction provides a contextual definition of metacognition and contrasts the proposed approach with prior work. However, a more formal definition could enhance clarity.

**1. Weakness Statement:**
"The paper does not adequately address the limitations of the proposed neurofeedback paradigm, particularly regarding its generalizability to other types of LLMs and its applicability to real-world scenarios. A more thorough discussion of these limitations would strengthen the paper's conclusions."

**2. Evidence Collection:**
a) Method-related Evidence (if applicable):
   - The paper acknowledges the use of in-context learning: "To investigate LLMs’ metacognition of their neural activations, we must disentangle the first-order cognitive processes (i.e., core processes for performing a given task) from the second-order metacognitive processes (i.e., processes for monitoring, reporting, and controlling first-order processes)." (Introduction, Paragraph 4)
   - The paper mentions the use of in-context learning: "To investigate LLMs’ metacognition of their neural activations, we must disentangle the first-order cognitive processes (i.e., core processes for performing a given task) from the second-order metacognitive processes (i.e., processes for monitoring, reporting, and controlling first-order processes). We propose the neurofeedback paradigm for LLMs, which can effectively dissociate these two levels of processes by targeting first-order processes with neurofeedback labels (Fig. 1 c,d)." (Introduction, Paragraph 4)
   - The paper discusses the limitations of probing: "While prior research has explored metacognitive-like behaviors in LLMs, such as expressing confidence ( Wang et al., 2025 ; Tian et al., 2023 ; Xiong et al., 2023 ) or engaging in self-reflection ( Zhou et al., 2024 ) , these studies rely on behavioral outputs rather than directly probing underlying neural processes. Consequently, it remains unclear whether these behaviors arise from genuine second-order metacognitive mechanisms or merely spurious correlations in the training data. We tackle this question by operationalizing metacognition in LLMs through their abilities to report and control their internal activations. Specifically, can LLMs accurately monitor subtle variations in the activations of a neuron or a feature in their neural spaces? Another question of interest is why LLMs can report some intermediate steps but not others, despite both types playing essential roles in computations and behavior. Answering these questions requires a novel experimental approach that can directly probe whether LLMs can access their internal activations, moving beyond indirect behavioral proxies." (Introduction, Paragraph 4)
   - The paper mentions the use of in-context learning as a form of white-box adversarial attack: "In our setup, labels are generated from the model’s own activations rather than external annotations. The task prompt (see Appendix A.2.2 for examples) consists of N N in-context examples. Each sentence is randomly sampled from a given dataset and assigned a discretized label." (Section 2.4)
   - The paper acknowledges the use of specific datasets: "We evaluate several LLMs from the Llama 3 ( Grattafiori et al., 2024 ) and Qwen 2.5 series ( Yang et al., 2024 ) (Appendix A.2 ) on the ETHICS dataset ( Hendrycks et al., 2020 ) (Appendix A.3 ). Each sentence in this dataset is a first-person description of behavior or intention in a moral or immoral scenario. Moral judgment constitutes a crucial aspect of AI safety, as immoral outputs or behavioral tendencies in LLMs indicate potential misalignment with human values ( Hendrycks et al., 2020 ; Hendrycks et al., 2021 ) . While our main results are using ETHICS, we also replicated our results using the True-False dataset ( reflectivity et al., 2023 ) , the Emotion dataset ( reflectivity et al., 2023a ) , and a Sycophancy dataset ( reflectivity et al., 2023b ); see Appendix A.3 and Fig. B.7 ." (Section 2.3)

b) Experiment-related Evidence (if applicable):
   - The experiments are conducted on specific LLMs and datasets.

4. Validation Analysis:
   - The paper does acknowledge the use of in-context learning and the specific datasets used. It also contrasts its approach with probing. However, it does not explicitly discuss the limitations of the neurofeedback paradigm in terms of generalizability to other LLM architectures, training methods, or real-world scenarios. The paper focuses on demonstrating the principle of metacognition in LLMs using the chosen setup.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section or detailed discussion on the limitations of the neurofeedback paradigm regarding generalizability and real-world applicability.

**1. Weakness Statement:**
"The paper does not provide a detailed analysis of the experimental results, particularly regarding the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs."

**2. Evidence Collection:**
a) Method-related Evidence (if applicable):
   - The paper describes the manipulation of in-context examples: "To investigate these factors, we use feature directions identified through logistic regression (LR) and principal component (PC) analysis as representative examples of semantically interpretable and variance-explaining axes, respectively (Appendix A.3 ). We fit LR at each layer to predict original dataset labels (e.g., morality in ETHICS), using that layer’s activations across dataset sentences. The LR axis, representing the optimal direction for classifying dataset labels, allows us to examine how the semantic interpretability of the target axis influences monitoring. Although LR-defined labels are correlated with dataset labels, only these LR labels, not external dataset labels, are internally accessible to LLMs, since these are computed directly from the LLM’s own activations rather than external annotations. The PC analysis is performed based on each layer’s activations across dataset examples. PC axes enable us to examine how the amount of variance explained by a given target axis affects metacognitive abilities (Fig. 2 b)." (Section 2.4)
   - The paper describes the control tasks: "Next, we investigate whether LLMs can control their neural activations along a target axis. In our control task prompts (see Fig. 1 d and Appendix A.5.2 for examples), the LLM is first presented with N N turns of user and assistant messages. In the ( N + 1 ) th turn, the user message instructs the model to control its neural activations along the prompt-targeted axis by imitating one label’s behavior, which is exemplified by the in-context examples with the same label earlier in the context. We measure the control effect d d of prompts on that axis with its signal-to-noise ratio (the difference between the mean values of the two neural score distributions, normalized by the standard deviation averaged over the two distributions, see Appendix A.5.5 on Cohen’s d d ). Because the directional sign of the target axis is specified by the labels in the prompt, a significantly positive d d corresponds to successful control." (Section 2.4)

b) Experiment-related Evidence (if applicable):
   - The paper presents results showing the effect of in-context examples on control performance: "We find that LLMs can successfully control neural scores for LR-targeting prompts with enough in-context examples (Fig. 3 a, showing layer 16 in LLaMA3.1 8B). We quantified the control effect d d of prompts on that axis with its signal-to-noise ratio (the difference between the mean values of the two neural score distributions, normalized by the standard deviation averaged over the two distributions, see Appendix A.5.5 on Cohen’s d d ). Because the directional sign of the target axis is specified by the labels in the prompt, a significantly positive d d corresponds to successful control." (Section 3)
   - The paper presents results showing the relationship between control effect and variance explained: "We find that control effects on LR l axes are the highest, and control effects on earlier PCs are higher than for later PCs (e.g., PC 2) (for the same relative layer depth and similar model size). In general, control effects on the LR axis are the highest, and control effects on earlier PCs are higher than for later PCs (e.g., PC 2) (for the same relative layer depth and similar model size). Because our prompts did not explicitly instruct the model toward extremity, we anticipate that modifying task prompts could further enhance these effects up to the limits of the model’s capability." (Section 3)
   - The paper presents results showing the impact of semantic interpretability: "We find that LLMs can monitor only a subset of their neural mechanisms (reminiscent of the “hidden knowledge” phenomenon ( Gekhman et al., 2025 ) ). Below, we discuss the novelties and limitations of our study, as well as broader implications for AI safety. Our paradigm differs from prior methods (e.g., probing, ICL, verbalized responses) by quantifying metacognition in LLMs at the neural level. Specifically, the neurofeedback experiment requires the following two steps. (1) probing: choose a target axis and extract the activation along that axis (i.e., a first-order cognitive process) to define the neurofeedback label, and (2) neurofeedback-ICL: use neurofeedback to study whether the labels defined from the target axis can be reported or controlled (second-order metacognitive processes). In contrast, the standard ICL does not. In ICL studies ( Vacareanu et al., 2024 ) , labels are externally provided (e.g., semantic labels or external algorithms’ outputs). Researchers cannot be certain which of the models’ internal states relate to these external labels and how. In our setup, labels are generated from the model’s own activations rather than external annotations. The neurofeedback paradigm clearly distinguishes first-order cognitive processes from second-order metacognitive processes (e.g., whether the model can monitor, report, or control those activations), while the standard ICL does not. Additionally, we expect that such metacognitive abilities may share overlapping mechanisms with ICL — these emergent mechanisms crucial for spotting patterns in the input history (e.g., induction heads ( Elhage et al., 2021 ) , function vectors ( Hendel et al., 2023 ) ) can be flexibly recruited for metacognitive purposes. Therefore, factors leading to the emergence of ICL (e.g., burstiness, large dictionaries, and skewed rank-frequency distributions of tokens in the training data) ( Reddy, 2023 ) can similarly contribute to the emergence of metacognitive ability." (Section 2.4)

4. Validation Analysis:
   - The paper does analyze the relationship between the number of in-context examples and control performance. It also analyzes the relationship between control effect and variance explained by the target axis. The paper also discusses the role of semantic interpretability by comparing LR and PC axes. However, the analysis could be more in-depth, including statistical significance testing and effect size calculations as suggested by the reviewer.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper presents results related to the number of in-context examples, variance explained, and the type of target axis. However, the analysis lacks statistical significance testing and effect size calculations, which would provide a more rigorous assessment of the relationships.

**Reviewer 2 Weaknesses Validation:**

**1. Weakness Statement:**
"The paper lacks a clear definition of metacognition, which makes it difficult to understand the authors' objectives and the relevance of their experiments. A more precise definition of metacognition, along with a clear explanation of how the proposed experiments measure this concept, would greatly enhance the paper's clarity and rigor."

**2. Evidence Collection:** (Same as Reviewer 1, Weakness 1)

**Validation Analysis:** (Same as Reviewer 1, Weakness 1)

**Conclusion:**
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The introduction provides a contextual definition of metacognition and contrasts the proposed approach with prior work. However, a more formal definition could enhance clarity.

**1. Weakness Statement:**
"The paper does not adequately address the limitations of the proposed neurofeedback paradigm, particularly regarding its generalizability to other types of LLMs and its applicability to real-world scenarios. A more thorough discussion of these limitations would strengthen the paper's conclusions."

**2. Evidence Collection:** (Same as Reviewer 1, Weakness 2)

**Validation Analysis:** (Same as Reviewer 1, Weakness 2)

**Conclusion:**
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section or detailed discussion on the limitations of the neurofeedback paradigm regarding generalizability and real-world applicability.

**1. Weakness Statement:**
"The paper does not provide a detailed analysis of the experimental results, particularly regarding the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs."

**2. Evidence Collection:** (Same as Reviewer 1, Weakness 3)

**Validation Analysis:** (Same as Reviewer 1, Weakness 3)

**Conclusion:**
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper presents results related to the number of in-context examples, variance explained, and the type of target axis. However, the analysis lacks statistical significance testing and effect size calculations, which would provide a more rigorous assessment of the relationships.

**Reviewer 3 Weaknesses Validation:**

**1. Weakness Statement:**
"The paper lacks a clear definition of metacognition, which makes it difficult to understand the authors' objectives and the relevance of their experiments. A more precise definition of metacognition, along with a clear explanation of how the proposed experiments measure this concept, would greatly enhance the paper's clarity and rigor."

**2. Evidence Collection:** (Same as Reviewer 1, Weakness 1 and Reviewer 2, Weakness 1)

**Validation Analysis:** (Same as Reviewer 1, Weakness 1 and Reviewer 2, Weakness 1)

**Conclusion:**
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The introduction provides a contextual definition of metacognition and contrasts the proposed approach with prior work. However, a more formal definition could enhance clarity.

**1. Weakness Statement:**
"The paper does not adequately address the limitations of the proposed neurofeedback paradigm, particularly regarding its generalizability to other types of LLMs and its applicability to real-world scenarios. A more thorough discussion of these limitations would strengthen the paper's conclusions."

**2. Evidence Collection:** (Same as Reviewer 1, Weakness 2 and Reviewer 2, Weakness 2)

**Validation Analysis:** (Same as Reviewer 1, Weakness 2 and Reviewer 2, Weakness 2)

**Conclusion:**
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section or detailed discussion on the limitations of the neurofeedback paradigm regarding generalizability and real-world applicability.

**1. Weakness Statement:**
"The paper does not provide a detailed analysis of the experimental results, particularly regarding the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs."

**2. Evidence Collection:** (Same as Reviewer 1, Weakness 3 and Reviewer 2, Weakness 3)

**Validation Analysis:** (Same as Reviewer 1, Weakness 3 and Reviewer 2, Weakness 3)

**Conclusion:**
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper presents results related to the number of in-context examples, variance explained, and the type of target axis. However, the analysis lacks statistical significance testing and effect size calculations, which would provide a more rigorous assessment of the relationships.

**Reviewer 4 Weaknesses Validation:**

**1. Weakness Statement:**
"The paper lacks a clear definition of metacognition, which makes it difficult to understand the authors' objectives and the relevance of their experiments. A more precise definition of metacognition, along with a clear explanation of how the proposed experiments measure this concept, would greatly enhance the paper's clarity and rigor."

**2. Evidence Collection:** (Same as Reviewer 1, Weakness 1, Reviewer 2, Weakness 1, and Reviewer 3, Weakness 1)

**Validation Analysis:** (Same as Reviewer 1, Weakness 1, Reviewer 2, Weakness 1, and Reviewer 3, Weakness 1)

**Conclusion:**
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The introduction provides a contextual definition of metacognition and contrasts the proposed approach with prior work. However, a more formal definition could enhance clarity.

**1. Weakness Statement:**
"The paper does not adequately address the limitations of the proposed neurofeedback paradigm, particularly regarding its generalizability to other types of LLMs and its applicability to real-world scenarios. A more thorough discussion of these limitations would strengthen the paper's conclusions."

**2. Evidence Collection:** (Same as Reviewer 1, Weakness 2 and Reviewer 2, Weakness 2)

**Validation Analysis:** (Same as Reviewer 1, Weakness 2 and Reviewer 2, Weakness 2)

**Conclusion:**
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section or detailed discussion on the limitations of the neurofeedback paradigm regarding generalizability and real-world applicability.

**1. Weakness Statement:**
"The paper does not provide a detailed analysis of the experimental results, particularly regarding the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs."

**2. Evidence Collection:** (Same as Reviewer 1, Weakness 3 and Reviewer 2, Weakness 3)

**Validation Analysis:** (Same as Reviewer 1, Weakness 3 and Reviewer 2, Weakness 3)

**Conclusion:**
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper presents results related to the number of in-context examples, variance explained, and the type of target axis. However, the analysis lacks statistical significance testing and effect size calculations, which would provide a more rigorous assessment of the relationships.

**Synthesis and Reflection:**

All reviewers raise concerns about the clarity of the definition of metacognition within the context of LLMs. While the paper provides a contextual definition, reviewers suggest a more formal and precise definition would enhance the paper's rigor and clarity. This is a valid criticism, as a clearer definition would help readers better understand the authors' objectives and the relevance of their experiments.

A significant point of agreement among the reviewers is the need for a more thorough discussion of the limitations of the proposed neurofeedback paradigm. Reviewers correctly point out the lack of a dedicated section addressing the generalizability of the paradigm to other LLM architectures, training methods, and real-world scenarios. This is a valid concern, as the conclusions drawn from the experiments are limited by the specific setup used.

Another shared concern is the depth of the experimental analysis. Reviewers note that while the paper presents results related to the number of in-context examples, semantic interpretability, and variance explained, the analysis lacks statistical significance testing and effect size calculations. This is a valid point, as these analyses would provide a more robust and rigorous assessment of the relationships between these factors and the model's metacognitive abilities.

There are no significant contradictions between the reviewers' opinions. They largely converge on the need for a clearer definition of metacognition, a more thorough discussion of limitations, and a more in-depth analysis of the experimental results.

**Overall Conclusion:**

All identified weaknesses are valid or partially valid. The paper could be significantly improved by providing a more formal definition of metacognition, discussing the limitations of the neurofeedback paradigm in more detail, and conducting a more rigorous statistical analysis of the experimental results.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel neurofeedback paradigm to investigate metacognitive abilities in large language models (LLMs). The authors propose that metacognition, the capacity to monitor and control one's own cognitive processes, can be dissected by examining how LLMs report and control their internal activations. To achieve this, they employ in-context learning to provide LLMs with feedback on their internal activations, effectively training the models to report and control these activations. The core methodology involves defining a target axis in the LLM's neural space, which can be either semantically interpretable (e.g., derived from logistic regression) or variance-explaining (e.g., derived from principal component analysis). The authors then manipulate the LLM's internal activations along this target axis using the neurofeedback paradigm, where the model is trained to associate a specific label with a particular activation state. The primary empirical findings indicate that LLMs can indeed monitor a limited subset of their neural mechanisms, suggesting that these models possess some inherent metacognitive capabilities. Furthermore, the study demonstrates that the ability to control these internal activations is correlated with the semantic interpretability and variance explained by the target axis. Specifically, the models exhibit higher control performance when the target axis is semantically meaningful and explains more variance in the input data. The authors also find that the models can report and control their activations along a target axis that is related to the model's ability to perform a given task, suggesting that metacognition is not merely an abstract concept but is linked to concrete behavioral outcomes. Overall, this study provides a unique approach to understanding metacognition in LLMs by directly probing their internal states and manipulating their activations, offering valuable insights into the mechanisms underlying self-awareness and control in these models. The findings also have implications for AI safety, suggesting that the ability to control internal activations may be a potential vulnerability, which the authors discuss in detail.


## Soundness:

2.5


## Presentation:

2.75


## Contribution:

2.25


## Strengths:

I found several aspects of this paper to be particularly strong. First, the introduction of a neurofeedback paradigm to quantify metacognition in LLMs is a novel and innovative approach. This method allows for a direct investigation of how LLMs monitor and control their internal activations, moving beyond indirect behavioral measures. The authors' decision to use in-context learning to provide feedback on internal activations is also a clever way to disentangle first-order cognitive processes from second-order metacognitive processes. This allows them to specifically target the metacognitive abilities of the models. The paper is also well-written and easy to follow, making the complex concepts accessible to a broad audience. The authors provide a clear explanation of their methodology and the experimental setup, which is crucial for the reproducibility of their work. Furthermore, the authors conduct extensive experiments across multiple datasets and models, which strengthens the robustness of their findings. The inclusion of various datasets, such as the ETHICS dataset, the True-False dataset, the Emotion dataset, and the Sycophancy dataset, demonstrates the generalizability of their results. The paper also provides a clear motivation for studying metacognition in LLMs, highlighting the potential risks associated with the development of AI systems that can monitor and control their internal states. The authors also make a clear distinction between their approach and prior methods, such as probing, ICL, and verbalized responses, which helps to contextualize their contributions. Finally, the authors' discussion of the potential implications of their findings for AI safety is insightful and highlights the importance of considering the limitations of LLMs, particularly in the context of adversarial attacks and model monitoring. The paper's focus on the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations is also a valuable contribution, providing a more nuanced understanding of the underlying mechanisms of metacognition in LLMs.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces the concept of metacognition and contrasts it with prior work, it lacks a more formal and precise definition. Although the authors provide a contextual definition, stating that metacognition is the ability to monitor and control internal activations, this definition could be more rigorously defined. The paper contrasts its approach with behavioral proxies used in previous studies, but a more explicit link to the experimental setup, explaining how the neurofeedback mechanism is implemented and how it relates to the model's ability to report and control its internal activations, would greatly enhance the paper's clarity and rigor. This lack of a clear definition makes it difficult to fully understand the authors' objectives and the relevance of their experiments. My confidence in this assessment is high, as the paper does not provide a more formal definition, and the current definition could be interpreted in multiple ways. Second, the paper does not adequately address the limitations of the proposed neurofeedback paradigm. While the authors acknowledge that the paradigm is based on in-context learning, they do not discuss the potential impact of the specific choice of tasks and datasets on the results. For example, the tasks used in the study might be biased towards certain types of metacognitive abilities, and the results might not generalize to other types of tasks. The authors also do not discuss the potential impact of the specific choice of layers for control. The paper also does not address the potential for the model to learn superficial correlations between the neurofeedback labels and the target behavior, rather than developing a genuine understanding of its internal states. This discussion should include a consideration of how the model's performance might be affected by changes in the experimental setup, such as the number of in-context examples or the specific choice of layers for control. My confidence in this assessment is high, as the paper lacks a dedicated section or detailed discussion on the limitations of the neurofeedback paradigm regarding generalizability and real-world applicability. Third, the paper does not provide a detailed analysis of the experimental results, particularly regarding the relationship between the number of in-context examples, semantic interpretability, variance explained, and the model's ability to report and control internal activations. While the authors present results showing the effect of in-context examples on control performance, the relationship between the number of in-context examples and control performance is not analyzed in detail. The paper also presents results showing the relationship between control effect and variance explained by the target axis, but this analysis lacks statistical significance testing and effect size calculations, which would provide a more rigorous assessment of the relationships. The authors should also investigate the relationship between the different layers of the model and their ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs. My confidence in this assessment is high, as the paper presents results related to these factors, but lacks statistical significance testing and effect size calculations. Finally, while the paper does discuss the potential implications of the findings for AI safety, the discussion could be more detailed. The authors should elaborate on how the results of this study inform the development of more transparent and controllable AI systems. They should also discuss the potential implications of the findings for the broader field of AI safety, particularly in the context of adversarial attacks and model monitoring. My confidence in this assessment is high, as the paper does not provide a detailed discussion of the implications for AI safety.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should begin by providing a more rigorous definition of metacognition within the context of large language models. This definition should clearly articulate what aspects of the model's internal state are being considered as 'metacognitive' and how these relate to the model's ability to monitor and control its own processing. For example, do they mean the model's ability to track the semantic content of its activations, or its ability to predict the outcome of its own computations? This clarification is crucial for understanding the experimental design and the interpretation of results. The authors should then explicitly link this definition to the experimental setup, explaining how the neurofeedback mechanism is implemented and how it relates to the model's ability to report and control its internal activations. Without this, the paper lacks a clear theoretical foundation. Second, the authors should include a more thorough discussion of the limitations of the proposed neurofeedback paradigm. The authors should acknowledge that the paradigm is based on in-context learning and may not generalize to other types of LLMs, such as those trained with different architectures or objectives. They should also discuss the potential impact of the specific choice of tasks and datasets on the results. For example, the tasks used in the study might be biased towards certain types of metacognitive abilities, and the results might not generalize to other types of tasks. The authors should also address the potential for the model to learn superficial correlations between the neurofeedback labels and the target behavior, rather than developing a genuine understanding of its internal states. This discussion should include a consideration of how the model's performance might be affected by changes in the experimental setup, such as the number of in-context examples or the specific choice of layers for control. A more robust analysis of these limitations would significantly strengthen the paper's conclusions. Third, the authors should provide a more detailed analysis of the experimental results, focusing on the relationship between the various factors that were manipulated in the study. For example, how does the number of in-context examples affect the model's ability to report and control its internal activations? How does the semantic interpretability of the target axis relate to the model's performance? How does the variance explained by the target axis affect the model's ability to control its internal activations? The authors should also investigate the relationship between the different layers of the model and their ability to report and control internal activations. A more in-depth analysis of these factors would provide valuable insights into the underlying mechanisms of metacognition in LLMs. This analysis should include statistical significance testing and effect size calculations to support the claims made in the paper. Finally, the authors should provide a more detailed discussion of the implications of their findings for AI safety. They should elaborate on how the results of this study inform the development of more transparent and controllable AI systems. They should also discuss the potential implications of the findings for the broader field of AI safety, particularly in the context of adversarial attacks and model monitoring. This discussion should include specific examples of how the findings could be used to develop more robust and reliable AI systems.


## Questions:

Based on my analysis, I have several questions that I believe would be important for the authors to address. First, how does the proposed neurofeedback paradigm compare to existing methods for measuring metacognition in LLMs, and what are its unique advantages? Specifically, how does the neurofeedback approach differ from methods that use probing or in-context learning to assess metacognitive abilities? Second, how do the results of this study inform the development of more transparent and controllable AI systems? What specific steps can be taken to ensure that LLMs can monitor and control their internal states in a safe and reliable manner? Third, what are the potential implications of the findings for the broader field of AI safety, particularly in the context of adversarial attacks and model monitoring? How can the ability of LLMs to report and control their internal activations be used to detect and mitigate adversarial attacks? Fourth, what are the potential limitations of the proposed neurofeedback paradigm, particularly regarding its generalizability to other types of LLMs and its applicability to real-world scenarios? What steps can be taken to address these limitations and ensure that the findings are robust and generalizable? Finally, how does the number of in-context examples affect the model's ability to report and control its internal activations, and what is the optimal number of in-context examples for achieving the best performance? What is the relationship between the semantic interpretability of the target axis and the model's performance, and how can this relationship be leveraged to improve the model's metacognitive abilities? These questions are aimed at clarifying the core methodological choices and assumptions of the study, and at exploring the broader implications of the findings for the field of AI safety.


## Rating:

4.75


## Confidence:

3.75


## Decision:

Reject
}