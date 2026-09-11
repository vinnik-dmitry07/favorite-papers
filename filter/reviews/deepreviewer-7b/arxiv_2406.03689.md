I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper proposes a new evaluation metric for assessing the quality of world models learned from data. The authors focus on the case where the underlying world can be represented as a deterministic finite automaton (DFA). They introduce two metrics inspired by the Myhill-Nerode theorem to evaluate whether a generative model captures the underlying structure of the DFA, going beyond simple next-token prediction accuracy. The paper evaluates these metrics on tasks like navigation, games, and logic puzzles, revealing that models achieving high next-token prediction accuracy may still have a poor understanding of the underlying world model.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a novel theoretical framework for evaluating world models, particularly for systems with a DFA structure.
2. The proposed metrics (sequence compression and distinction) offer a deeper understanding of model capabilities compared to traditional next-token prediction metrics.
3. The evaluation across multiple domains (navigation, games, logic puzzles) demonstrates the versatility of the proposed metrics.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on DFAs, which may not fully capture the complexity of real-world environments. The evaluation metrics and findings may not directly translate to more complex, stochastic, or partially observable environments. Specifically, the assumption of a deterministic transition function in DFAs simplifies the problem significantly, and it is unclear how the proposed metrics would perform in scenarios with probabilistic transitions or partial observability, which are common in real-world settings. This limitation restricts the applicability of the findings to a narrow class of problems.
2. The computational cost of calculating the proposed metrics, especially for large datasets or complex models, is not thoroughly discussed. The paper lacks a detailed analysis of the time and space complexity of the proposed metrics, making it difficult to assess their scalability. For instance, the process of identifying Myhill-Nerode equivalence classes could be computationally expensive for large state spaces, and the paper does not provide sufficient information on how this cost scales with the size of the model or the dataset. This omission raises concerns about the practicality of the proposed metrics in real-world applications.
3. The paper does not provide a clear methodology for applying the proposed metrics to models trained on non-DFA environments. The reliance on the Myhill-Nerode theorem, which is specific to DFAs, makes it unclear how these metrics could be adapted for models trained on data that does not conform to a DFA structure. The paper does not address how the proposed metrics could be used to evaluate models trained on data with stochastic transitions or partial observability, which are common in real-world settings. This lack of guidance limits the practical applicability of the proposed metrics.

### Suggestions

The paper should include a more thorough discussion of the limitations of using DFAs to model real-world environments. It would be beneficial to acknowledge that DFAs are a simplification and that the proposed metrics may not directly translate to more complex scenarios. The authors could discuss how the Myhill-Nerode equivalence classes might be adapted or approximated in the presence of stochasticity or partial observability. For example, they could explore the use of probabilistic automata or partially observable Markov decision processes (POMDPs) as alternative models and discuss how the proposed metrics could be extended to these settings. Furthermore, the paper should provide a more detailed analysis of the computational cost of the proposed metrics. This should include a breakdown of the time and space complexity of each step in the calculation, as well as an empirical evaluation of the metrics on datasets of varying sizes. The authors should also discuss potential optimizations to improve the scalability of the metrics. For example, they could explore the use of approximation algorithms or sampling techniques to reduce the computational burden. This analysis is crucial for assessing the practicality of the proposed metrics in real-world applications.

To address the lack of clarity on applying the metrics to non-DFA environments, the authors should provide a more detailed discussion of how the proposed metrics could be adapted. This could involve exploring alternative definitions of Myhill-Nerode equivalence classes that are suitable for stochastic or partially observable environments. For example, they could discuss how the notion of distinguishability could be relaxed to allow for probabilistic transitions. The authors should also provide concrete examples of how the metrics could be applied to models trained on real-world data. This could involve describing how the metrics could be used to evaluate the performance of a language model trained on a dataset with noisy or ambiguous data. The paper should also discuss the limitations of the proposed metrics in these settings and suggest potential directions for future research. This would help to clarify the scope and applicability of the proposed metrics and provide guidance for future work.

Finally, the paper should include a more comprehensive evaluation of the proposed metrics. This should include experiments on a wider range of datasets and models, including those trained on non-DFA environments. The authors should also compare the performance of the proposed metrics with other existing evaluation metrics, such as those based on next-token prediction accuracy or reward-based metrics. This would help to demonstrate the advantages and limitations of the proposed metrics and provide a more complete picture of their performance. The evaluation should also include an analysis of the sensitivity of the metrics to different parameters and hyperparameters. This would help to ensure that the metrics are robust and reliable in different settings.

### Questions

1. How do the proposed metrics perform when applied to models trained on environments that do not conform to a DFA structure?
2. What is the computational complexity of calculating the proposed metrics, and how does it scale with the size of the dataset or model?
3. Could the proposed metrics be adapted or extended to evaluate models trained on partially observable environments?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a new evaluation metric for assessing the world models learned by generative models. The authors focus on the case where the underlying world can be represented as a deterministic finite automaton (DFA). They introduce two metrics inspired by the Myhill-Nerode theorem to evaluate whether a generative model captures the underlying structure of the DFA, going beyond simple next-token prediction accuracy. The paper evaluates these metrics on tasks like navigation, games, and logic puzzles, revealing that models achieving high next-token prediction accuracy may still have a poor understanding of the underlying world model.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel theoretical framework for evaluating world models, particularly for systems with a DFA structure.
2. The proposed metrics (sequence compression and distinction) offer a deeper understanding of model capabilities compared to traditional next-token prediction metrics.
3. The evaluation across multiple domains (navigation, games, logic puzzles) demonstrates the versatility of the proposed metrics.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on DFAs, which may not fully capture the complexity of real-world environments. The evaluation metrics and findings may not directly translate to more complex, stochastic, or partially observable environments. Specifically, the assumption of a deterministic transition function in DFAs simplifies the problem significantly, and it is unclear how the proposed metrics would perform in scenarios with probabilistic transitions or partial observability, which are common in real-world settings. This limitation restricts the applicability of the findings to a narrow class of problems.
2. The computational cost of calculating the proposed metrics, especially for large datasets or complex models, is not thoroughly discussed. The paper lacks a detailed analysis of the time and space complexity of the proposed metrics, making it difficult to assess their scalability. For instance, the process of identifying Myhill-Nerode equivalence classes could be computationally expensive for large state spaces, and the paper does not provide sufficient information on how this cost scales with the size of the model or the dataset. This omission raises concerns about the practicality of the proposed metrics in real-world applications.
3. The paper does not provide a clear methodology for applying the proposed metrics to models trained on non-DFA environments. The reliance on the Myhill-Nerode theorem, which is specific to DFAs, makes it unclear how these metrics could be adapted for models trained on data that does not conform to a DFA structure. The paper does not address how the proposed metrics could be used to evaluate models trained on data with stochastic transitions or partial observability, which are common in real-world settings. This lack of guidance limits the practical applicability of the proposed metrics.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of using DFAs to model real-world environments. While DFAs provide a useful abstraction for certain types of problems, they are a simplification of the complexities found in many real-world scenarios. The authors should acknowledge that the Myhill-Nerode equivalence classes, which are central to their evaluation metrics, may not be directly applicable to environments with stochastic transitions or partial observability. For example, in a partially observable environment, the notion of distinguishability between states based on sequences of observations is different from that in a fully observable DFA. The authors should discuss how their metrics could be adapted or extended to handle such scenarios, perhaps by considering probabilistic versions of the Myhill-Nerode theorem or by exploring alternative metrics that are more suitable for partially observable settings. This would significantly broaden the applicability of their work and make it more relevant to real-world problems.

Furthermore, the paper needs to provide a more detailed analysis of the computational cost of the proposed metrics. The authors should include a formal analysis of the time and space complexity of calculating the Myhill-Nerode equivalence classes, as well as the sequence compression and distinction metrics. This analysis should consider the size of the state space, the length of the sequences, and the number of states in the DFA. It would also be beneficial to provide empirical results on the runtime of the proposed metrics on different datasets and model sizes. This would help readers understand the practical limitations of the proposed approach and assess its scalability. The authors could also explore potential optimizations or approximations to reduce the computational cost, such as using sampling techniques or incremental updates to the equivalence classes. A more thorough discussion of these practical aspects would greatly enhance the value of the paper.

Finally, the paper should provide a more concrete methodology for applying the proposed metrics to models trained on non-DFA environments. While the authors acknowledge that the Myhill-Nerode theorem is specific to DFAs, they do not offer any alternative approaches for evaluating models trained on data that does not conform to a DFA structure. The authors should explore potential extensions of their metrics to handle stochastic or partially observable environments. For example, they could consider using probabilistic versions of the Myhill-Nerode theorem or explore alternative metrics that are more suitable for partially observable settings. They could also discuss how their metrics could be used to evaluate the performance of reinforcement learning algorithms in environments with stochastic transitions or partial observability. Providing concrete examples of how the metrics could be applied in these settings would greatly enhance the practical relevance of the paper.

### Questions

1. How do the proposed metrics perform when applied to models trained on environments that do not conform to a DFA structure?
2. What is the computational complexity of calculating the proposed metrics, and how does it scale with the size of the dataset or model?
3. Could the proposed metrics be adapted or extended to evaluate models trained on partially observable environments?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a new evaluation metric for assessing the quality of world models learned by generative models. The authors focus on the case where the underlying world can be represented as a deterministic finite automaton (DFA). They introduce two metrics inspired by the Myhill-Nerode theorem to evaluate whether a generative model captures the underlying structure of the DFA, going beyond simple next-token prediction accuracy. The paper evaluates these metrics on tasks like navigation, games, and logic puzzles, revealing that models achieving high next-token prediction accuracy may still have a poor understanding of the underlying world model.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel theoretical framework for evaluating world models, particularly for systems with a DFA structure.
2. The proposed metrics (sequence compression and distinction) offer a deeper understanding of model capabilities compared to traditional next-token prediction metrics.
3. The evaluation across multiple domains (navigation, games, logic puzzles) demonstrates the versatility of the proposed metrics.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on DFAs, which may not fully capture the complexity of real-world environments. The evaluation metrics and findings may not directly translate to more complex, stochastic, or partially observable environments. Specifically, the assumption of a deterministic transition function in DFAs simplifies the problem significantly, and it is unclear how the proposed metrics would perform in scenarios with probabilistic transitions or partial observability, which are common in real-world settings. This limitation restricts the applicability of the findings to a narrow class of problems.
2. The computational cost of calculating the proposed metrics, especially for large datasets or complex models, is not thoroughly discussed. The paper lacks a detailed analysis of the time and space complexity of the proposed metrics, making it difficult to assess their scalability. For instance, the process of identifying Myhill-Nerode equivalence classes could be computationally expensive for large state spaces, and the paper does not provide sufficient information on how this cost scales with the size of the model or the dataset. This omission raises concerns about the practicality of the proposed metrics in real-world applications.
3. The paper does not provide a clear methodology for applying the proposed metrics to models trained on non-DFA environments. The reliance on the Myhill-Nerode theorem, which is specific to DFAs, makes it unclear how these metrics could be adapted for models trained on data that does not conform to a DFA structure. The paper does not address how the proposed metrics could be used to evaluate models trained on data with stochastic transitions or partial observability, which are common in real-world settings. This lack of guidance limits the practical applicability of the proposed metrics.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of using DFAs to model real-world environments. While DFAs provide a useful abstraction for certain types of problems, they are a simplification of the complexities found in many real-world scenarios. The authors should acknowledge that the Myhill-Nerode equivalence classes, which are central to their evaluation metrics, may not be directly applicable to environments with stochastic transitions or partial observability. For example, in a partially observable environment, the notion of distinguishability between states based on sequences of observations is different from that in a fully observable DFA. The authors should discuss how their metrics could be adapted or extended to handle such scenarios, perhaps by considering probabilistic versions of the Myhill-Nerode theorem or by exploring alternative metrics that are more suitable for partially observable settings. This would significantly broaden the applicability of their work and make it more relevant to real-world problems.

Furthermore, the paper needs to provide a more detailed analysis of the computational cost of the proposed metrics. The authors should include a formal analysis of the time and space complexity of calculating the Myhill-Nerode equivalence classes, as well as the sequence compression and distinction metrics. This analysis should consider the size of the state space, the length of the sequences, and the number of states in the DFA. It would also be beneficial to provide empirical results on the runtime of the proposed metrics on different datasets and model sizes. This would help readers understand the practical limitations of the proposed approach and assess its scalability. The authors could also explore potential optimizations or approximations to reduce the computational cost, such as using sampling techniques or incremental updates to the equivalence classes. A more thorough discussion of these practical aspects would greatly enhance the value of the paper.

Finally, the paper should provide a more concrete methodology for applying the proposed metrics to models trained on non-DFA environments. While the authors acknowledge that the Myhill-Nerode theorem is specific to DFAs, they do not offer any alternative approaches for evaluating models trained on data that does not conform to a DFA structure. The authors should explore potential extensions of their metrics to handle stochastic or partially observable environments. For example, they could consider using probabilistic versions of the Myhill-Nerode theorem or explore alternative metrics that are more suitable for partially observable settings. They could also discuss how their metrics could be used to evaluate the performance of reinforcement learning algorithms in environments with stochastic transitions or partial observability. Providing concrete examples of how the metrics could be applied in these settings would greatly enhance the practical relevance of the paper.

### Questions

1. How do the proposed metrics perform when applied to models trained on environments that do not conform to a DFA structure?
2. What is the computational complexity of calculating the proposed metrics, and how does it scale with the size of the dataset or model?
3. Could the proposed metrics be adapted or extended to evaluate models trained on partially observable environments?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper proposes a new way to evaluate the world model of a generative model. The idea is to use the Myhill-Nerode theorem to define two new metrics that measure how well the world model can distinguish between different states and compress sequences. The authors show that these metrics can reveal flaws in the world model that are not captured by traditional metrics like next-token prediction. They apply their metrics to several tasks, including navigation, logic puzzles, and games, and show that models that perform well on next-token prediction can still have a poor understanding of the underlying world model.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper introduces a novel way to evaluate world models by using the Myhill-Nerode theorem. This is a creative and original approach that has the potential to provide deeper insights into the inner workings of generative models.
- The paper is well-written and easy to follow. The authors clearly explain the theoretical background and the proposed metrics.
- The paper provides a comprehensive evaluation of the proposed metrics on several tasks, including navigation, logic puzzles, and games. This demonstrates the versatility of the metrics and their potential for real-world applications.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses on deterministic finite automata (DFAs) as a way to represent the underlying world model. While DFAs are a useful abstraction, they may not capture the complexity of real-world environments. The authors should acknowledge this limitation and discuss how their approach might be extended to more complex environments.
- The paper does not provide a clear explanation of how the Myhill-Nerode theorem can be used to evaluate world models. While the authors mention that the theorem can be used to define two new metrics, they do not provide a detailed explanation of how these metrics are calculated or how they relate to the world model. A more detailed explanation of the theoretical background would be helpful for readers who are not familiar with the Myhill-Nerode theorem.
- The paper does not provide a clear definition of what constitutes a "good" world model. While the authors show that their metrics can reveal flaws in the world model, they do not provide a clear criterion for determining whether a world model is good or bad. This makes it difficult to compare the performance of different world models.

### Suggestions

The paper introduces an interesting approach to evaluating world models using the Myhill-Nerode theorem, but it could be strengthened by addressing several key areas. First, the authors should more thoroughly discuss the limitations of using DFAs to represent real-world environments. While DFAs provide a useful abstraction, they are inherently limited in their ability to capture the complexities of stochasticity, partial observability, and continuous state spaces that are often present in real-world scenarios. The authors should acknowledge that their approach, while novel, may not be directly applicable to these more complex environments and should discuss potential avenues for extending their work to handle such cases. For example, they could explore how their metrics might be adapted to handle probabilistic transitions or partial observability, perhaps by considering Bayesian approaches or by defining a notion of approximate distinguishability. Furthermore, the authors should provide a more detailed explanation of how the Myhill-Nerode theorem is used to define the proposed metrics. While they mention that the theorem can be used to define two new metrics, they do not provide a clear explanation of how these metrics are calculated or how they relate to the world model. A more detailed explanation of the theoretical background would be helpful for readers who are not familiar with the Myhill-Nerode theorem. Specifically, they should provide a step-by-step explanation of how the Myhill-Nerode equivalence classes are computed and how these classes are used to define the sequence compression and distinction metrics. This explanation should include concrete examples to illustrate the concepts and make them more accessible to a wider audience. 

Second, the authors should provide a more rigorous definition of what constitutes a "good" world model. While they show that their metrics can reveal flaws in the world model, they do not provide a clear criterion for determining whether a world model is good or bad. This makes it difficult to compare the performance of different world models. A more precise definition of a good world model would help to establish a benchmark for evaluating the quality of world models and would make the paper more impactful. For example, they could define a good world model as one that is able to accurately predict the next state of the environment given the current state and the action taken, or as one that is able to generalize to unseen situations. They could also explore the relationship between the proposed metrics and other measures of world model quality, such as the ability to perform downstream tasks or the accuracy of predictions. This would help to establish a more comprehensive understanding of the strengths and weaknesses of their approach. 

Finally, the authors should consider evaluating their metrics on a wider range of tasks and environments. While they have shown that their metrics can reveal flaws in the world model on navigation, logic puzzle, and game tasks, it is not clear whether these results generalize to other types of tasks. It would be beneficial to evaluate their metrics on tasks that involve more complex dynamics, such as those found in robotics or autonomous driving. This would help to establish the generalizability of their approach and would make the paper more relevant to a wider range of applications. Additionally, the authors should consider comparing their metrics to other existing methods for evaluating world models, such as those based on reinforcement learning or imitation learning. This would help to establish the relative strengths and weaknesses of their approach and would make the paper more impactful.

### Questions

- How can the proposed metrics be extended to evaluate world models in environments with stochastic transitions or partial observability?
- What are the limitations of using DFAs to represent real-world environments, and how can these limitations be addressed?
- How can the Myhill-Nerode theorem be used to evaluate world models in practice? Could you provide a more detailed explanation of how the proposed metrics are calculated and how they relate to the world model?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Find the corresponding section in the paper.
3. Look for evidence (quotes, formulas, missing information) to support the weakness.
4. If the weakness is about missing information, check if the information is indeed absent.
5. If there are conflicting opinions, note them.
6. Summarize the evidence and conclude if the weakness is valid.
```json
[
  {
    "Weakness Statement": "The paper focuses on DFAs, which may not fully capture the complexity of real-world environments. The evaluation metrics and findings may not directly translate to more complex, stochastic, or partially observable environments. Specifically, the assumption of a deterministic transition function in DFAs simplifies the problem significantly, and it is unclear how the proposed metrics would perform in scenarios with probabilistic transitions or partial observability, which are common in real-world settings. This limitation restricts the applicability of the findings to a narrow class of problems.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states). An extended transition function δ ^ \hat{\delta} takes a state and a sequence, and it inductively applies δ \delta to each token of the sequence.",
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} . Since a DFA provides multiple ways to arrive at the same state, this test assesses whether a generative model recognizes that two sequences correspond to the same state. For example, in cumulative Connect-4, there may be multiple sequences that arrive at the same board position. Recall is undefined for equal states because there is no true boundary, so our compression metric only reports precision, averaged over states sampled uniformly at random (we say a generative model’s precision is 1 if its boundary is correctly empty)."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly defines the problem using DFAs with deterministic transitions. The evaluation metrics are designed based on the properties of DFAs.",
      "Supporting quotes": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "Impact assessment": "The reviewer correctly points out that the focus on DFAs limits the generalizability of the findings to more complex real-world environments with stochasticity and partial observability."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's definition and evaluation are based on the properties of DFAs with deterministic transitions."
    }
  },
  {
    "Weakness Statement": "The computational cost of calculating the proposed metrics, especially for large datasets or complex models, is not thoroughly discussed. The paper lacks a detailed analysis of the time and space complexity of the proposed metrics, making it difficult to assess their scalability. For instance, the process of identifying Myhill-Nerode equivalence classes could be computationally expensive for large state spaces, and the paper does not provide sufficient information on how this cost scales with the size of the model or the dataset. This omission raises concerns about the practicality of the proposed metrics in real-world applications.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} . Since a DFA provides multiple ways to arrive at the same state, this test assesses whether a generative model recognizes that two sequences correspond to the same state. For example, in cumulative Connect-4, there may be multiple sequences that arrive at the same board position. Recall is undefined for equal states because there is no true boundary, so our compression metric only reports precision, averaged over states sampled uniformly at random (we say a generative model’s precision is 1 if its boundary is correctly empty)."
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the metrics but does not provide any analysis of their computational complexity.",
      "Supporting quotes": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} ."
      ],
      "Impact assessment": "The reviewer's concern about the computational cost is valid as the paper lacks any discussion or analysis of the time and space complexity of the proposed metrics."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include any analysis of the computational complexity of the proposed metrics."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a clear methodology for applying the proposed metrics to models trained on non-DFA environments. The reliance on the Myhill-Nerode theorem, which is specific to DFAs, makes it unclear how these metrics could be adapted for models trained on data that does not conform to a DFA structure. The paper does not address how the proposed metrics could be used to evaluate models trained on data with stochastic transitions or partial observability, which are common in real-world settings. This lack of guidance limits the practical applicability of the proposed metrics.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "b) Experiment-related Evidence": [
        "We then examine the underlying world model of the trained models. Despite the route planning capabilities of these models, we find that their underlying world models are incoherent; they recovers streets whose orientations are physically impossible (e.g. labeled NW but facing east) and require flyovers above other streets (see Figure 3 )."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's methodology is explicitly tied to DFAs. The experiments focus on scenarios where the underlying world can be represented as a DFA. There is no discussion on applying the metrics to non-DFA environments.",
      "Supporting quotes": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) .",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition)."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper does not provide a methodology for applying the proposed metrics to models trained on non-DFA environments, limiting the general applicability of the evaluation framework."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's methodology and experiments are centered around DFAs, and there is no discussion on extending the metrics to other types of environments."
    }
  },
  {
    "Weakness Statement": "How do the proposed metrics perform when applied to models trained on environments that do not conform to a DFA structure?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "b) Experiment-related Evidence": [
        "We then examine the underlying world model of the trained models. Despite the route planning capabilities of these models, we find that their underlying world models are incoherent; they recovers streets whose orientations are physically impossible (e.g. labeled NW but facing east) and require flyovers above other streets (see Figure 3 )."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's methodology and experiments are based on the assumption that the underlying world can be represented as a DFA. There is no empirical evaluation of the metrics on models trained on non-DFA environments.",
      "Supporting quotes": [
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition)."
      ],
      "Impact assessment": "The reviewer's question highlights a gap in the paper. The paper does not provide empirical evidence on the performance of the metrics when applied to models trained on non-DFA environments."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's experimental setup and analysis are based on the DFA assumption, and there is no empirical evaluation on non-DFA environments."
    }
  },
  {
    "Weakness Statement": "What is the computational complexity of calculating the proposed metrics, and how does it scale with the size of the dataset or model?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} . Since a DFA provides multiple ways to arrive at the same state, this test assesses whether a generative model recognizes that two sequences correspond to the same state. For example, in cumulative Connect-4, there may be multiple sequences that arrive at the same board position. Recall is undefined for equal states because there is no true boundary, so our compression metric only reports precision, averaged over states sampled uniformly at random (we say a generative model’s precision is 1 if its boundary is correctly empty)."
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the metrics but does not provide any analysis of their computational complexity.",
      "Supporting quotes": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} ."
      ],
      "Impact assessment": "The reviewer's question is valid. The paper lacks any discussion or analysis of the computational complexity of the proposed metrics."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include any analysis of the computational complexity of the proposed metrics."
    }
  },
  {
    "Weakness Statement": "Could the proposed metrics be adapted or extended to evaluate models trained on partially observable environments?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "b) Experiment-related Evidence": [
        "We then examine the underlying world model of the trained models. Despite the route planning capabilities of these models, we find that their underlying world models are incoherent; they recovers streets whose orientations are physically impossible (e.g. labeled NW but facing east) and require flyovers above other streets (see Figure 3 )."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's methodology is based on DFAs, which assume full observability. The metrics are defined based on distinguishing states based on sequences of actions. Extending this to partially observable environments is not directly addressed.",
      "Supporting quotes": [
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition)."
      ],
      "Impact assessment": "The reviewer's question is valid. The paper does not discuss how the proposed metrics could be adapted for partially observable environments."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's formulation and experiments are based on the assumption of full observability inherent in the DFA framework."
    }
  },
  {
    "Weakness Statement": "The paper focuses on DFAs, which may not fully capture the complexity of real-world environments. The evaluation metrics and findings may not directly translate to more complex, stochastic, or partially observable environments. Specifically, the assumption of a deterministic transition function in DFAs simplifies the problem significantly, and it is unclear how the proposed metrics would perform in scenarios with probabilistic transitions or partial observability, which are common in real-world settings. This limitation restricts the applicability of the findings to a narrow class of problems.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "b) Experiment-related Evidence": [
        "We then examine the underlying world model of the trained models. Despite the route planning capabilities of these models, we find that their underlying world models are incoherent; they recovers streets whose orientations are physically impossible (e.g. labeled NW but facing east) and require flyovers above other streets (see Figure 3 )."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly defines the problem using DFAs with deterministic transitions. The evaluation metrics are designed based on the properties of DFAs.",
      "Supporting quotes": [
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "Impact assessment": "The reviewer correctly identifies the limitation of focusing on DFAs and the potential issues with generalizing the findings to more complex environments."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's methodology and experiments are based on the assumption that the underlying world can be represented as a DFA with deterministic transitions."
    }
  },
  {
    "Weakness Statement": "The computational cost of calculating the proposed metrics, especially for large datasets or complex models, is not thoroughly discussed. The paper lacks a detailed analysis of the time and space complexity of the proposed metrics, making it difficult to assess their scalability. For instance, the process of identifying Myhill-Nerode equivalence classes could be computationally expensive for large state spaces, and the paper does not provide sufficient information on how this cost scales with the size of the model or the dataset. This omission raises concerns about the practicality of the proposed metrics in real-world applications.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} . Since a DFA provides multiple ways to arrive at the same state, this test assesses whether a generative model recognizes that two sequences correspond to the same state. For example, in cumulative Connect-4, there may be multiple sequences that arrive at the same board position. Recall is undefined for equal states because there is no true boundary, so our compression metric only reports precision, averaged over states sampled uniformly at random (we say a generative model’s precision is 1 if its boundary is correctly empty)."
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the metrics but does not provide any analysis of their computational complexity.",
      "Supporting quotes": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} ."
      ],
      "Impact assessment": "The reviewer's concern about the computational cost is valid as the paper lacks any discussion or analysis of the time and space complexity of the proposed metrics."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include any analysis of the computational complexity of the proposed metrics."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a clear methodology for applying the proposed metrics to models trained on non-DFA environments. The reliance on the Myhill-Nerode theorem, which is specific to DFAs, makes it unclear how these metrics could be adapted for models trained on data that does not conform to a DFA structure. The paper does not address how the proposed metrics could be used to evaluate models trained on data with stochastic transitions or partial observability, which are common in real-world settings. This lack of guidance limits the practical applicability of the proposed metrics.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "b) Experiment-related Evidence": [
        "We then examine the underlying world model of the trained models. Despite the route planning capabilities of these models, we find that their underlying world models are incoherent; they recovers streets whose orientations are physically impossible (e.g. labeled NW but facing east) and require flyovers above other streets (see Figure 3 )."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's methodology is explicitly tied to DFAs. The experiments focus on scenarios where the underlying world can be represented as a DFA. There is no discussion on applying the metrics to non-DFA environments.",
      "Supporting quotes": [
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition)."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper does not provide a methodology for applying the proposed metrics to models trained on non-DFA environments, limiting the general applicability of the evaluation framework."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's methodology and experiments are centered around DFAs, and there is no discussion on extending the metrics to other types of environments."
    }
  },
  {
    "Weakness Statement": "The paper would benefit from a more thorough discussion of the limitations of using DFAs to model real-world environments. While DFAs provide a useful abstraction for certain types of problems, they are a simplification of the complexities found in many real-world scenarios. The authors should acknowledge that the Myhill-Nerode equivalence classes, which are central to their evaluation metrics, may not be directly applicable to environments with stochastic transitions or partial observability. For example, in a partially observable environment, the notion of distinguishability between states based on sequences of observations is different from that in a fully observable DFA. The authors should discuss how their metrics could be adapted or extended to handle such scenarios, perhaps by considering probabilistic versions of the Myhill-Nerode theorem or by exploring alternative metrics that are more suitable for partially observable settings. This would significantly broaden the applicability of their work and make it more relevant to real-world problems.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "b) Experiment-related Evidence": [
        "We then examine the underlying world model of the trained models. Despite the route planning capabilities of these models, we find that their underlying world models are incoherent; they recovers streets whose orientations are physically impossible (e.g. labeled NW but facing east) and require flyovers above other streets (see Figure 3 )."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's methodology is explicitly based on DFAs, which inherently assume full observability and deterministic transitions. The paper does not discuss the limitations of this assumption or how the metrics would apply to more complex environments.",
      "Supporting quotes": [
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper lacks a discussion on the limitations of using DFAs for real-world modeling and potential adaptations for more complex scenarios."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's formulation and experiments are based on the assumption of full observability inherent in the DFA framework, and it lacks a discussion on the limitations of this assumption."
    }
  },
  {
    "Weakness Statement": "Furthermore, the paper needs to provide a more detailed analysis of the computational cost of the proposed metrics. The authors should include a formal analysis of the time and space complexity of calculating the Myhill-Nerode equivalence classes, as well as the sequence compression and distinction metrics. This analysis should consider the size of the state space, the length of the sequences, and the number of states in the DFA. It would also be beneficial to provide empirical results on the runtime of the proposed metrics on different datasets and model sizes. This would help readers understand the practical limitations of the proposed approach and assess its scalability. The authors could also explore potential optimizations or approximations to improve the scalability of the metrics. For example, they could explore the use of sampling techniques or incremental updates to the equivalence classes. A more thorough discussion of these practical aspects would greatly enhance the value of the paper.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} . Since a DFA provides multiple ways to arrive at the same state, this test assesses whether a generative model recognizes that two sequences correspond to the same state. For example, in cumulative Connect-4, there may be multiple sequences that arrive at the same board position. Recall is undefined for equal states because there is no true boundary, so our compression metric only reports precision, averaged over states sampled uniformly at random (we say a generative model’s precision is 1 if its boundary is correctly empty)."
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the metrics but does not provide any analysis of their computational complexity.",
      "Supporting quotes": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} ."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper lacks a detailed analysis of the computational cost of the proposed metrics."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include any analysis of the computational complexity of the proposed metrics."
    }
  },
  {
    "Weakness Statement": "Finally, the paper should provide a more concrete methodology for applying the proposed metrics to models trained on non-DFA environments. While the authors acknowledge that the Myhill-Nerode theorem is specific to DFAs, they do not offer any alternative approaches for evaluating models trained on data that does not conform to a DFA structure. The authors should explore potential extensions of their metrics to handle stochastic or partially observable environments. For example, they could consider using probabilistic versions of the Myhill-Nerode theorem or explore alternative metrics that are more suitable for partially observable settings. They could also discuss how their metrics could be used to evaluate the performance of reinforcement learning algorithms in environments with stochastic transitions or partial observability. Providing concrete examples of how the metrics could be applied in these settings would greatly enhance the practical relevance of the paper.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "b) Experiment-related Evidence": [
        "We then examine the underlying world model of the trained models. Despite the route planning capabilities of these models, we find that their underlying world models are incoherent; they recovers streets whose orientations are physically impossible (e.g. labeled NW but facing east) and require flyovers above other streets (see Figure 3 )."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's methodology is explicitly tied to DFAs. The experiments focus on scenarios where the underlying world can be represented as a DFA. There is no discussion on applying the metrics to non-DFA environments.",
      "Supporting quotes": [
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper lacks a concrete methodology for applying the proposed metrics to non-DFA environments."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's methodology and experiments are centered around DFAs, and there is no discussion on extending the metrics to other types of environments."
    }
  },
  {
    "Weakness Statement": "How do the proposed metrics perform when applied to models trained on environments that do not conform to a DFA structure?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We consider a finite alphabet Σ with tokens a ∈ Σ a∈Σ , and sequences s = ( a 1 , a 2 , … ) s=( a 1 , a 2 , \u22ef ) . Let Σ ∗ Σ ∗ denote the collection of sequences on the alphabet.",
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "b) Experiment-related Evidence": [
        "We then examine the underlying world model of the trained models. Despite the route planning capabilities of these models, we find that their underlying world models are incoherent; they recovers streets whose orientations are physically impossible (e.g. labeled NW but facing east) and require flyovers above other streets (see Figure 3 )."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's methodology is explicitly tied to DFAs. The experiments focus on scenarios where the underlying world can be represented as a DFA. There is no empirical evaluation of the metrics on models trained on non-DFA environments.",
      "Supporting quotes": [
        "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition). As a simplifying assumption, we consider the case where there is a special state q reject q_{\text{reject}} with no outgoing transitions and F = Q ∖ { q reject } F=Q\setminus\{q_{\text{reject}}\} (i.e., the DFA accepts all valid states)."
      ],
      "Impact assessment": "The reviewer's question highlights a gap in the paper. The paper does not provide empirical evidence on the performance of the metrics when applied to models trained on non-DFA environments."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's experimental setup and analysis are based on the DFA assumption, and there is no empirical evaluation on non-DFA environments."
    }
  },
  {
    "Weakness Statement": "What is the computational complexity of calculating the proposed metrics, and how does it scale with the size of the dataset or model?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} . Since a DFA provides multiple ways to arrive at the same state, this test assesses whether a generative model recognizes that two sequences correspond to the same state. For example, in cumulative Connect-4, there may be multiple sequences that arrive at the same board position. Recall is undefined for equal states because there is no true boundary, so our compression metric only reports precision, averaged over states sampled uniformly at random (we say a generative model’s precision is 1 if its boundary is correctly empty)."
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the metrics but does not provide any analysis of their computational complexity.",
      "Supporting quotes": [
        "Our evaluation metrics summarize how well a generative model identifies sequences that distinguish a given pair of states. Given a pair of states q 1 q_{1} and q 2 q_{2} , the metric is formed by first sampling equal state pairs q 1 = q 2 q_{1}=q_{2} ."
      ],
      "Impact assessment": "The reviewer's question is valid. The paper lacks any discussion or analysis of the computational complexity of the proposed metrics."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not include}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel framework for evaluating the quality of world models learned by generative models, particularly focusing on scenarios where the underlying environment can be represented as a deterministic finite automaton (DFA). The core contribution lies in the development of two new metrics, sequence compression and distinction, which are derived from the Myhill-Nerode theorem. These metrics aim to assess the model's ability to capture the underlying structure of the DFA, going beyond simple next-token prediction accuracy. The authors argue that while next-token prediction metrics may indicate high next-token probability accuracy, they fail to capture a model's understanding of the underlying world model. The proposed metrics, on the other hand, are designed to evaluate the model's ability to distinguish between different states and compress sequences based on the DFA's structure. The paper evaluates these metrics across multiple domains, including navigation, games, and logic puzzles, demonstrating that models achieving high next-token prediction accuracy can still exhibit a poor understanding of the underlying world model. Specifically, the experiments involve training generative models on sequences of actions and states within these environments and then assessing the quality of the learned world model using the proposed metrics. The empirical findings reveal that models capable of achieving high next-token prediction accuracy may still struggle to differentiate between states that lead to the same outcome or compress sequences effectively, indicating a discrepancy between token-level prediction and world-model understanding. The authors use a finite alphabet to represent actions, and the DFA provides a structured way to define transitions between states. The evaluation metrics focus on how well a generative model can identify sequences that distinguish a given pair of states, and how well it can compress sequences based on the DFA's structure. The paper's overall significance lies in its attempt to provide a more nuanced evaluation of generative models, moving beyond simple next-token prediction metrics and towards a more comprehensive assessment of their understanding of the underlying world model. By introducing the sequence compression and distinction metrics, the paper offers a new perspective on evaluating generative models, particularly in scenarios where the underlying environment can be represented as a DFA. The findings highlight the limitations of relying solely on next-token prediction metrics and emphasize the need for more sophisticated evaluation methods that can capture the true understanding of the world model.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

The paper's primary strength lies in its novel approach to evaluating world models using the Myhill-Nerode theorem. This is a significant contribution, as it moves beyond traditional next-token prediction metrics, which often fail to capture the underlying structure of the environment. The proposed metrics, sequence compression and distinction, are technically sound and offer a deeper understanding of model capabilities compared to standard next-token prediction metrics. This is a creative and original approach that has the potential to provide a more comprehensive evaluation of generative models. The paper is also well-written and easy to follow, making the technical concepts accessible to a wider audience. The authors clearly explain the theoretical background and the proposed metrics, which is crucial for the paper's overall clarity and impact. The evaluation across multiple domains, including navigation, games, and logic puzzles, demonstrates the versatility of the proposed metrics. This is a strength because it shows that the metrics are not limited to a specific type of environment and can be applied to a variety of scenarios. The experiments are well-designed and provide compelling evidence that models achieving high next-token prediction accuracy may still exhibit a poor understanding of the underlying world model. This is a key finding of the paper and highlights the limitations of relying solely on next-token prediction metrics. The paper also provides a clear and concise explanation of the DFA framework, which is essential for understanding the proposed metrics. The authors use a finite alphabet to represent actions and define transitions between states using the DFA, which is a standard and well-understood framework. This makes the paper accessible to a wider audience and allows for a more rigorous analysis of the proposed metrics. The paper's focus on evaluating the underlying world model is also a strength. By moving beyond next-token prediction metrics, the paper provides a more comprehensive assessment of the model's understanding of the environment. This is a crucial step towards developing more robust and reliable generative models. The paper's overall contribution is significant, as it provides a new perspective on evaluating generative models and highlights the limitations of relying solely on next-token prediction metrics. The proposed metrics are technically sound and offer a deeper understanding of model capabilities, which is a valuable contribution to the field.


## Weaknesses:

Despite the paper's strengths, several weaknesses limit its overall impact and generalizability. A primary concern is the paper's focus on deterministic finite automata (DFAs) as a model for the underlying environment. While DFAs provide a useful abstraction for certain types of problems, they are inherently limited in their ability to capture the complexities of real-world environments. Specifically, the assumption of a deterministic transition function, which is central to DFAs, simplifies the problem significantly. As the paper states, "We use standard notation for a deterministic finite automaton W = ( Q , Σ , δ , q 0 , F ) (see Appendix C for a complete definition)." This simplification means that the proposed metrics may not directly translate to more complex, stochastic, or partially observable environments, which are common in real-world settings. The paper does not adequately address how the proposed metrics could be adapted or extended to handle such scenarios. This limitation restricts the applicability of the findings to a narrow class of problems. Furthermore, the paper lacks a detailed analysis of the computational complexity of the proposed metrics. The authors introduce the Myhill-Nerode theorem, which is specific to DFAs, but do not provide any analysis of the time and space complexity of calculating the Myhill-Nerode equivalence classes, sequence compression, and distinction metrics. As one reviewer noted, "The paper does not include any analysis of the computational complexity of the proposed metrics." This omission raises concerns about the scalability of the proposed metrics, particularly for large datasets or complex models. The process of identifying Myhill-Nerode equivalence classes could be computationally expensive for large state spaces, and the paper does not provide sufficient information on how this cost scales with the size of the model or the dataset. This lack of analysis makes it difficult to assess the practicality of the proposed metrics in real-world applications. The paper also lacks a clear methodology for applying the proposed metrics to models trained on non-DFA environments. The reliance on the Myhill-Nerode theorem, which is specific to DFAs, makes it unclear how these metrics could be adapted for models trained on data that does not conform to a DFA structure. As another reviewer pointed out, "The paper does not provide a methodology for applying the proposed metrics to models trained on data that does not conform to a DFA structure." This lack of guidance limits the practical applicability of the proposed metrics. The paper does not address how the metrics could be used to evaluate models trained on data with stochastic transitions or partial observability, which are common in real-world settings. This omission significantly restricts the generalizability of the proposed metrics. The paper's experiments are primarily focused on scenarios where the underlying world can be represented as a DFA. There is no empirical evaluation of the metrics on models trained on non-DFA environments. This lack of empirical evidence limits the confidence in the generalizability of the proposed metrics. The paper also does not provide a concrete methodology for applying the proposed metrics to models trained on non-DFA environments. While the authors acknowledge that the Myhill-Nerode theorem is specific to DFAs, they do not offer any alternative approaches for evaluating models trained on data that does not conform to a DFA structure. This lack of guidance limits the practical applicability of the proposed metrics. Finally, the paper does not provide a clear definition of what constitutes a "good" world model. While the authors show that their metrics can reveal flaws in the underlying world model, they do not provide a clear criterion for determining whether a world model is good or bad. This makes it difficult to compare the performance of different world models and to assess the overall quality of the learned environment model. This lack of a clear definition limits the practical applicability of the proposed metrics. In summary, the paper's limitations stem from its focus on DFAs, the lack of computational complexity analysis, the absence of a methodology for non-DFA environments, the lack of empirical evaluation on non-DFA environments, and the absence of a clear definition of a "good" world model. These weaknesses significantly limit the generalizability and practical applicability of the proposed metrics.


## Suggestions:

To address the identified weaknesses, several concrete improvements can be made. First, the paper should include a more thorough discussion of the limitations of using DFAs to model real-world environments. While DFAs provide a useful abstraction, they are inherently limited in their ability to capture the complexities of real-world scenarios. The authors should acknowledge that the Myhill-Nerode equivalence classes, which are central to their evaluation metrics, may not be directly applicable to environments with stochastic transitions or partial observability. For example, in a partially observable environment, the notion of distinguishability between states based on sequences of observations is different from that in a fully observable DFA. The authors should discuss how their metrics could be adapted or extended to handle such scenarios, perhaps by considering probabilistic versions of the Myhill-Nerode theorem or by exploring alternative metrics that are more suitable for partially observable settings. This would significantly broaden the applicability of their work and make it more relevant to real-world problems. Second, the paper needs to provide a formal analysis of the time and space complexity of calculating the Myhill-Nerode equivalence classes, as well as the sequence compression and distinction metrics. This analysis should consider the size of the state space, the length of the sequences, and the number of states in the DFA. It would also be beneficial to provide empirical results on the runtime of the proposed metrics on different datasets and model sizes. This would help readers understand the practical limitations of the proposed approach and assess its scalability. The authors could also explore potential optimizations or approximations to improve the scalability of the metrics. For example, they could explore the use of sampling techniques or incremental updates to the equivalence classes. A more thorough discussion of these practical aspects would greatly enhance the value of the paper. Third, the paper should provide a more concrete methodology for applying the proposed metrics to models trained on non-DFA environments. While the authors acknowledge that the Myhill-Nerode theorem is specific to DFAs, they do not offer any alternative approaches for evaluating models trained on data that does not conform to a DFA structure. The authors should explore potential extensions of their metrics to handle stochastic or partially observable environments. For example, they could consider using probabilistic versions of the Myhill-Nerode theorem or explore alternative metrics that are more suitable for partially observable settings. They could also discuss how their metrics could be used to evaluate the performance of reinforcement learning algorithms in environments with stochastic transitions or partial observability. Providing concrete examples of how the metrics could be applied in these settings would greatly enhance the practical relevance of the paper. Fourth, the paper should include a more comprehensive evaluation of the proposed metrics. This should include experiments on a wider range of datasets and models, including those trained on non-DFA environments. The authors should also compare the performance of the proposed metrics with other existing evaluation metrics, such as those based on next-token prediction accuracy or reward-based metrics. This would help to demonstrate the advantages and limitations of the proposed metrics and provide a more complete picture of their performance. The evaluation should also include an analysis of the sensitivity of the metrics to different parameters and hyperparameters. This would help to ensure that the metrics are robust and reliable in different settings. Fifth, the paper should provide a more rigorous definition of what constitutes a "good" world model. While the authors show that their metrics can reveal flaws in the underlying world model, they do not provide a clear criterion for determining whether a world model is good or bad. This makes it difficult to compare the performance of different world models and to assess the overall quality of the learned environment model. A more precise definition of a good world model would help to establish a benchmark for evaluating the quality of world models and would make the paper more impactful. For example, they could define a good world model as one that is able to accurately predict the next state of the environment given the current state and the action taken, or as one that is able to generalize to unseen situations. Finally, the paper should include a more detailed analysis of the computational cost of the proposed metrics. This should include a formal analysis of the time and space complexity of calculating the Myhill-Nerode equivalence classes, as well as the sequence compression and distinction metrics. This analysis should consider the size of the state space, the length of the sequences, and the number of states in the DFA. It would also be beneficial to provide empirical results on the runtime of the proposed metrics on different datasets and model sizes. This would help readers understand the practical limitations of the proposed approach and assess its scalability. The authors could also explore potential optimizations or approximations to improve the scalability of the metrics. For example, they could explore the use of sampling techniques or incremental updates to the equivalence classes. A more thorough discussion of these practical aspects would greatly enhance the value of the paper.


## Questions:

Several key uncertainties and methodological choices warrant further clarification. First, how do the proposed metrics perform when applied to models trained on environments that do not conform to a DFA structure? The paper's methodology is explicitly tied to DFAs, and there is no empirical evaluation of the metrics on models trained on non-DFA environments. This is a crucial question, as it directly impacts the generalizability of the proposed metrics. Second, what is the computational complexity of calculating the proposed metrics, and how does it scale with the size of the dataset or model? The paper does not include a formal analysis of the time and space complexity of the proposed metrics, which is a significant omission. This makes it difficult to assess the practical limitations of the proposed approach and evaluate its scalability. Third, could the proposed metrics be adapted or extended to handle stochastic or partially observable environments? The paper acknowledges that the Myhill-Nerode theorem is specific to DFAs, but it does not offer any alternative approaches for evaluating models trained on data that does not conform to a DFA structure. This is a critical question, as it directly impacts the applicability of the proposed metrics to real-world scenarios. Fourth, what are the limitations of using DFAs to model real-world environments, and how can these limitations be addressed? The paper does not provide a thorough discussion of the limitations of using DFAs to model real-world environments. This is a crucial question, as it directly impacts the validity of the proposed metrics. Fifth, what is a "good" world model? The paper does not provide a clear definition of what constitutes a "good" world model. This makes it difficult to compare the performance of different world models and to assess the overall quality of the learned environment model. Sixth, how sensitive are the proposed metrics to different parameters and hyperparameters? The paper does not include an analysis of the sensitivity of the metrics to different parameters and hyperparameters. This makes it difficult to ensure that the metrics are robust and reliable in different settings. Finally, how do the proposed metrics compare to other existing evaluation metrics, such as those based on next-token prediction accuracy or reward-based metrics? The paper does not include a comprehensive evaluation of the proposed metrics, including comparisons with other existing evaluation metrics. This makes it difficult to assess the advantages and limitations of the proposed metrics and to determine their relative strengths and weaknesses. These questions are crucial for understanding the limitations of the proposed metrics and for guiding future research in this area.


## Rating:

6.0


## Confidence:

3.0


## Decision:

Reject
}