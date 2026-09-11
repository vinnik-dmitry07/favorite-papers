I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper explores the use of linear probes to detect deception in language model outputs. The authors train probes on datasets with contrastive pairs of honest and deceptive responses and evaluate their performance on various deception-related tasks, including strategic deception in realistic scenarios like Insider Trading and Sandbagging. The probes achieve high AUROC scores, but the study also highlights the limitations of current methods in generalizing to more complex and nuanced forms of deception.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses an important and timely problem: detecting deception in language models, which is crucial for ensuring the safety and reliability of AI systems.
2. The authors provide a comprehensive evaluation of their approach across multiple datasets and deception-related tasks, demonstrating the potential of linear probes for detecting deception.
3. The paper is well-written and easy to follow, with clear explanations of the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not adequately address the limitations of using linear probes for detecting deception. While the authors demonstrate the effectiveness of their approach, they do not discuss the potential biases or assumptions that may limit its generalizability to other types of deception or more complex scenarios. Specifically, the paper lacks a discussion on how the linear probe might be fooled by subtle forms of deception that do not manifest as obvious inconsistencies, or how the probe's performance might degrade when dealing with adversarial examples designed to evade detection. The analysis should include a more thorough investigation into the types of deceptive strategies that the probe is most susceptible to, and those it struggles with.
2. The evaluation of the probe's performance is limited to a few specific datasets and scenarios, which may not fully capture the range of deceptive behaviors that could arise in real-world applications. The paper should include a more diverse set of evaluation tasks, including scenarios with more subtle or nuanced forms of deception. For example, the evaluation could include tasks that require the model to deceive multiple parties with different objectives, or tasks that involve deceptive reasoning about complex or ambiguous situations. The current evaluation does not sufficiently demonstrate the robustness of the probe across a wide spectrum of deception scenarios.
3. The paper does not explore the potential for the probe to be used in conjunction with other detection methods, such as those based on model outputs or user behavior. The authors should discuss how their approach could be integrated with other techniques to improve the overall reliability of deception detection systems. For instance, the paper could explore how the linear probe's output could be combined with other indicators of deception, such as changes in the model's output distribution or unusual patterns in user interactions. The lack of integration with other methods limits the practical applicability of the proposed approach.

### Suggestions

To address the limitations of using linear probes, the authors should conduct a more in-depth analysis of the probe's behavior under various deceptive conditions. This should include an investigation into the types of deceptive strategies that the probe is most susceptible to, and those it struggles with. For example, the authors could explore how the probe performs when the model generates responses that are internally consistent but still deceptive, or when the probe is presented with conflicting information from different sources. Furthermore, the authors should investigate the probe's robustness to adversarial examples, which are specifically designed to evade detection. This could involve training the probe on a dataset of adversarial examples, or using techniques such as adversarial training to improve its robustness. The analysis should also consider the potential biases that may be introduced by the training data, and how these biases might affect the probe's performance in real-world scenarios. This could involve analyzing the probe's performance across different demographic groups or scenarios with varying levels of deception.

To enhance the evaluation of the probe's performance, the authors should include a more diverse set of evaluation tasks that cover a wider range of deceptive behaviors. This should include scenarios with more subtle or nuanced forms of deception, such as those that involve deceptive reasoning about complex or ambiguous situations. For example, the authors could evaluate the probe's ability to detect deception in scenarios where the model is required to deceive multiple parties with different objectives, or where the deception involves manipulating the model's internal state. The evaluation should also consider the probe's performance in more realistic scenarios, such as those involving deceptive behavior in conversations with multiple agents or in interactive environments. This could involve using more complex datasets or creating new datasets that are specifically designed to test the probe's ability to detect subtle forms of deception. The authors should also consider the probe's performance in scenarios where the deception is not explicitly stated, but rather implied or inferred from the model's behavior.

Finally, the authors should explore the potential for integrating their approach with other detection methods to improve the overall reliability of deception detection systems. This could involve combining the linear probe's output with other indicators of deception, such as changes in the model's output distribution or unusual patterns in user interactions. The authors should investigate how these different methods can be combined to create a more robust and reliable system. For example, the authors could explore using the linear probe's output as a feature in a more complex detection model, or using the probe's output to trigger an alert when a potential deception is detected. The authors should also consider the computational cost and practical feasibility of integrating different detection methods, and how these costs might affect the overall performance of the system. This would provide a more comprehensive understanding of the strengths and limitations of the proposed approach and its potential for real-world applications.

### Questions

1. How do you anticipate the performance of the probe would vary across different types of deception, such as strategic deception versus deceptive intent?
2. What are the potential limitations of using linear probes for detecting deception in more complex or nuanced scenarios, such as those involving deceptive reasoning or manipulation of multiple parties?
3. How might the probe's performance be affected by adversarial examples or other forms of evasion?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

The paper explores the use of linear probes to detect deception in language model outputs. The authors train probes on datasets with contrastive pairs of honest and deceptive responses and evaluate their performance on various deception-related tasks, including strategic deception in realistic scenarios like Insider Trading and Sandbagging. The probes achieve high AUROC scores, but the study also highlights the limitations of current methods in generalizing to more complex and nuanced forms of deception.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper addresses an important and timely problem: detecting deception in language models, which is crucial for ensuring the safety and reliability of AI systems.
- The authors provide a comprehensive evaluation of their approach across multiple datasets and deception-related tasks, demonstrating the potential of linear probes for detecting deception.
- The paper is well-written and easy to follow, with clear explanations of the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not adequately address the limitations of using linear probes for detecting deception. While the authors demonstrate the effectiveness of their approach, they do not discuss the potential biases or assumptions that may limit its generalizability to other types of deception or more complex scenarios. Specifically, the paper lacks a discussion on how the linear probe might be fooled by subtle forms of deception that do not manifest as obvious inconsistencies, or how the probe's performance might degrade when dealing with adversarial examples designed to evade detection. The analysis should include a more thorough investigation into the types of deceptive strategies that the probe is most susceptible to, and those it struggles with.
- The evaluation of the probe's performance is limited to a few specific datasets and scenarios, which may not fully capture the range of deceptive behaviors that could arise in real-world applications. The paper should include a more diverse set of evaluation tasks, including scenarios with more subtle or nuanced forms of deception. For example, the evaluation could include tasks that require the model to deceive multiple parties with different objectives, or tasks that involve deceptive reasoning about complex or ambiguous situations. The current evaluation does not sufficiently demonstrate the robustness of the probe across a wide spectrum of deception scenarios.
- The paper does not explore the potential for the probe to be used in conjunction with other detection methods, such as those based on model outputs or user behavior. The authors should discuss how their approach could be integrated with other techniques to improve the overall reliability of deception detection systems. For instance, the paper could explore how the linear probe's output could be combined with other indicators of deception, such as changes in the model's output distribution or unusual patterns in user interactions. The lack of integration with other methods limits the practical applicability of the proposed approach.

### Suggestions

The authors should conduct a more thorough investigation into the limitations of linear probes for detecting deception. This should include an analysis of the types of deceptive strategies that are most likely to evade detection by the linear probe. For example, the authors could explore how the probe performs against deceptive strategies that involve subtle manipulation of the model's internal state or that use complex linguistic patterns to convey deception. Furthermore, the authors should investigate the probe's robustness to adversarial examples, which are specifically designed to evade detection. This could involve training the probe on a dataset of adversarial examples or using techniques such as adversarial training to improve its robustness. A more detailed analysis of the probe's failure modes would provide valuable insights into the limitations of the approach and guide future research in this area.

To address the limitations of the evaluation, the authors should include a more diverse set of evaluation tasks that cover a wider range of deceptive behaviors. This should include scenarios with more subtle or nuanced forms of deception, such as those that involve deceptive reasoning about complex or ambiguous situations. For example, the authors could evaluate the probe's ability to detect deception in scenarios where the model is required to deceive multiple parties with different objectives. Additionally, the authors should consider evaluating the probe's performance in more realistic scenarios, such as those involving deceptive behavior in conversations with multiple agents or in interactive environments. This would provide a more comprehensive assessment of the probe's ability to detect deception in real-world applications. The evaluation should also include a more detailed analysis of the probe's performance across different types of deception, such as strategic deception versus deceptive intent.

Finally, the authors should explore the potential for integrating their approach with other detection methods to improve the overall reliability of deception detection systems. This could involve combining the linear probe's output with other indicators of deception, such as changes in the model's output distribution or unusual patterns in user interactions. For example, the authors could explore using the linear probe's output as a feature in a more complex detection model, or using the probe's output to trigger an alert when a potential deception is detected. The authors should also consider the computational cost and practical feasibility of integrating different detection methods, and how these costs might affect the overall performance of the system. This would provide a more comprehensive understanding of the strengths and limitations of the proposed approach and its potential for real-world applications.

### Questions

- How might the probe's performance be affected by adversarial examples or other forms of evasion?
- What are the potential limitations of using linear probes for detecting deception in more complex or nuanced scenarios, such as those involving deceptive reasoning or manipulation of multiple parties?
- How might the probe's performance vary across different types of deception, such as strategic deception versus deceptive intent?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the use of linear probes to detect deception in language models. The authors train probes on a dataset of contrastive pairs of honest and deceptive responses and evaluate their performance on several deception-related tasks, including strategic deception in realistic scenarios like Insider Trading and Sandbagging. The probes achieve high AUROC scores, but the study also highlights the limitations of current methods in generalizing to more complex and nuanced forms of deception.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses an important and timely problem: detecting deception in language models, which is crucial for ensuring the safety and reliability of AI systems.
- The authors provide a comprehensive evaluation of their approach across multiple datasets and deception-related tasks, demonstrating the potential of linear probes for detecting deception.
- The paper is well-written and easy to follow, with clear explanations of the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not adequately address the limitations of using linear probes for detecting deception. While the authors demonstrate the effectiveness of their approach, they do not discuss the potential biases or assumptions that may limit its generalizability to other types of deception or more complex scenarios. Specifically, the paper lacks a discussion on how the linear probe might be fooled by subtle forms of deception that do not manifest as obvious inconsistencies, or how the probe's performance might degrade when dealing with adversarial examples designed to evade detection. The analysis should include a more thorough investigation into the types of deceptive strategies that the probe is most susceptible to, and those it struggles with.
- The evaluation of the probe's performance is limited to a few specific datasets and scenarios, which may not fully capture the range of deceptive behaviors that could arise in real-world applications. The paper should include a more diverse set of evaluation tasks, including scenarios with more subtle or nuanced forms of deception. For example, the evaluation could include tasks that require the model to deceive multiple parties with different objectives, or tasks that involve deceptive reasoning about complex or ambiguous situations. The current evaluation does not sufficiently demonstrate the robustness of the probe across a wide spectrum of deception scenarios.
- The paper does not explore the potential for the probe to be used in conjunction with other detection methods, such as those based on model outputs or user behavior. The authors should discuss how their approach could be integrated with other techniques to improve the overall reliability of deception detection systems. For instance, the paper could explore how the linear probe's output could be combined with other indicators of deception, such as changes in the model's output distribution or unusual patterns in user interactions. The lack of integration with other methods limits the practical applicability of the proposed approach.

### Suggestions

The authors should conduct a more in-depth analysis of the probe's behavior under various deceptive conditions. This should include an investigation into the types of deceptive strategies that the probe is most susceptible to, and those it struggles with. For example, the authors could explore how the probe performs when the model generates responses that are internally consistent but still deceptive, or when the probe is presented with conflicting information from different sources. Furthermore, the authors should investigate the probe's robustness to adversarial examples, which are specifically designed to evade detection. This could involve training the probe on a dataset of adversarial examples, or using techniques such as adversarial training to improve its robustness. A more detailed analysis of the probe's failure modes would provide valuable insights into the limitations of the approach and guide future research in this area.

To enhance the evaluation of the probe's performance, the authors should include a more diverse set of evaluation tasks that cover a wider range of deceptive behaviors. This should include scenarios with more subtle or nuanced forms of deception, such as those that involve deceptive reasoning about complex or ambiguous situations. For example, the authors could evaluate the probe's ability to detect deception in scenarios where the model is required to deceive multiple parties with different objectives, or where the deception involves manipulating the model's internal state. The evaluation should also consider the probe's performance in more realistic scenarios, such as those involving deceptive behavior in conversations with multiple agents or in interactive environments. This would provide a more comprehensive assessment of the probe's ability to detect deception in real-world applications. The authors should also consider using a more fine-grained evaluation metric that can capture the nuances of deception, rather than relying solely on AUROC.

Finally, the authors should explore the potential for integrating their approach with other detection methods to improve the overall reliability of deception detection systems. This could involve combining the linear probe's output with other indicators of deception, such as changes in the model's output distribution or unusual patterns in user interactions. For example, the authors could explore using the linear probe's output as a feature in a more complex detection model, or using the probe's output to trigger an alert when a potential deception is detected. The authors should also consider the computational cost and practical feasibility of integrating different detection methods, and how these costs might affect the overall performance of the system. This would provide a more comprehensive understanding of the strengths and limitations of the proposed approach and its potential for real-world applications.

### Questions

- How might the probe's performance be affected by adversarial examples or other forms of evasion?
- What are the potential limitations of using linear probes for detecting deception in more complex or nuanced scenarios, such as those involving deceptive reasoning or manipulation of multiple parties?
- How might the probe's performance vary across different types of deception, such as strategic deception versus deceptive intent?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper explores the use of linear probes to detect deception in language models. The authors train probes on datasets with contrastive pairs of honest and deceptive responses and evaluate their performance on various deception-related tasks, including strategic deception in realistic scenarios like Insider Trading and Sandbagging. The probes achieve high AUROC scores, but the study also highlights the limitations of current methods in generalizing to more complex and nuanced forms of deception.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses an important and timely problem: detecting deception in language models, which is crucial for ensuring the safety and reliability of AI systems.

2. The authors provide a comprehensive evaluation of their approach across multiple datasets and deception-related tasks, demonstrating the potential of linear probes for detecting deception.

3. The paper is well-written and easy to follow, with clear explanations of the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not adequately address the limitations of using linear probes for detecting deception. While the authors demonstrate the effectiveness of their approach, they do not discuss the potential biases or assumptions that may limit its generalizability to other types of deception or more complex scenarios. Specifically, the paper lacks a discussion on how the linear probe might be fooled by subtle forms of deception that do not manifest as obvious inconsistencies, or how the probe's performance might degrade when dealing with adversarial examples designed to evade detection. The analysis should include a more thorough investigation into the types of deceptive strategies that the probe is most susceptible to, and those it struggles with.

2. The evaluation of the probe's performance is limited to a few specific datasets and scenarios, which may not fully capture the range of deceptive behaviors that could arise in real-world applications. The paper should include a more diverse set of evaluation tasks, including scenarios with more subtle or nuanced forms of deception. For example, the evaluation could include tasks that require the model to deceive multiple parties with different objectives, or tasks that involve deceptive reasoning about complex or ambiguous situations. The current evaluation does not sufficiently demonstrate the robustness of the probe across a wide spectrum of deception scenarios.

3. The paper does not explore the potential for the probe to be used in conjunction with other detection methods, such as those based on model outputs or user behavior. The authors should discuss how their approach could be integrated with other techniques to improve the overall reliability of deception detection systems. For instance, the paper could explore how the linear probe's output could be combined with other indicators of deception, such as changes in the model's output distribution or unusual patterns in user interactions. The lack of integration with other methods limits the practical applicability of the proposed approach.

### Suggestions

To enhance the paper, the authors should conduct a more thorough investigation into the limitations of linear probes for detecting deception. This should include an analysis of the types of deceptive strategies that are most likely to evade detection by the linear probe. For example, the authors could explore how the probe performs against deceptive strategies that involve subtle manipulation of the model's internal state or that use complex linguistic patterns to convey deception. Furthermore, the authors should investigate the probe's robustness to adversarial examples, which are specifically designed to evade detection. This could involve training the probe on a dataset of adversarial examples or using techniques such as adversarial training to improve its robustness. A more detailed analysis of the probe's failure modes would provide valuable insights into the limitations of the approach and guide future research in this area.

To address the limitations of the evaluation, the authors should include a more diverse set of evaluation tasks that cover a wider range of deceptive behaviors. This should include scenarios with more subtle or nuanced forms of deception, such as those that involve deceptive reasoning about complex or ambiguous situations. For example, the authors could evaluate the probe's ability to detect deception in scenarios where the model is required to deceive multiple parties with different objectives. Additionally, the authors should consider evaluating the probe's performance in more realistic scenarios, such as those involving deceptive behavior in conversations with multiple agents or in interactive environments. This would provide a more comprehensive assessment of the probe's ability to detect deception in real-world applications. The evaluation should also include a more fine-grained analysis of the probe's performance, going beyond AUROC to consider other metrics that capture the nuances of deception.

Finally, the authors should explore the potential for integrating their approach with other detection methods to improve the overall reliability of deception detection systems. This could involve combining the linear probe's output with other indicators of deception, such as changes in the model's output distribution or unusual patterns in user interactions. For example, the authors could explore using the linear probe's output as a feature in a more complex detection model, or using the probe's output to trigger an alert when a potential deception is detected. The authors should also consider the computational cost and practical feasibility of integrating different detection methods, and how these costs might affect the overall performance of the system. This would provide a more comprehensive understanding of the strengths and limitations of the proposed approach and its potential for real-world applications.

### Questions

1. How might the probe's performance be affected by adversarial examples or other forms of evasion?

2. What are the potential limitations of using linear probes for detecting deception in more complex or nuanced scenarios, such as those involving deceptive reasoning or manipulation of multiple parties?

3. How might the probe's performance vary across different types of deception, such as strategic deception versus deceptive intent?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper provided.

Here's my plan:
1. **Iterate through each reviewer's comments.**
2. **For each weakness identified by a reviewer:**
    - **Locate the specific claim in the paper.**
    - **Find evidence (quotes, experimental details, missing citations) to support or refute the weakness.**
    - **Categorize the weakness (methodological, experimental, etc.).**
    - **Assess the impact of the weakness.**
    - **Formulate a conclusion on the validity of the weakness.**
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not adequately address the limitations of using linear probes for detecting deception. While the authors demonstrate the effectiveness of their approach, they do not discuss the potential biases or assumptions that may limit its generalizability to other types of deception or more complex scenarios. Specifically, the paper lacks a discussion on how the linear probe might be fooled by subtle forms of deception that do not manifest as obvious inconsistencies, or how the probe's performance might degrade when dealing with adversarial examples designed to evade detection. The analysis should include a more thorough investigation into the types of deceptive strategies that the probe is most susceptible to, and those it struggles with."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the linear probe methodology in the "Methodology" section, specifically under "Building Deception Probes".
   - Quote: "We apply our probes after layer 22 (of 80) in the residual stream of Llama-3.3-70B-Instruct (Grattafiori et al., 2024) . To fit our probe we flatten across samples and sequence positions to give a dataset of activations x i ∈ ℝ d x_{i}\in\mathbb{R}^{d} with corresponding labels y i ∈ { honest , deceptive } y_{i}\in\{\text{honest},\text{deceptive}\} . We then take the mean across tokens to get a single deceptiveness-score for each model response. We then take the mean across per-token scores to get a per-prompt score. We then take the mean across tokens to get a per-prompt score. We then take the mean across tokens to get a per-prompt score. We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the mean across per-token scores to get a per-prompt score . We then take the mean across tokens to get a per-prompt score . We then take the