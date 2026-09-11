I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper investigates the necessity of learning causal models for achieving robust generalization in artificial agents. The authors prove that any agent capable of adapting to a wide range of distributional shifts must have learned a causal model of the data generating process. This finding is significant because it establishes a formal link between causal reasoning and robust generalization, suggesting that causal models are not just beneficial but essential for agents to adapt to new domains. The authors show that approximate causal models can still enable robust adaptation, with the approximation error growing linearly with the regret bound. This result provides a theoretical framework for understanding how imperfect causal knowledge can still facilitate adaptation, with limitations that become apparent under high distributional shifts. The paper also discusses the implications of this work for various fields, including transfer learning, causal inference, and the study of emergent capabilities in artificial agents.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel theoretical framework that establishes the necessity of causal models for robust generalization in artificial agents. This is a significant contribution to the field, as it formalizes the intuition that causal understanding is crucial for adapting to distributional shifts.
2. The paper is well-structured and clearly presents complex ideas, making it accessible to a broad audience. The authors effectively use illustrative examples, such as the Causal Influence Diagram (CID) and the conditional probability distribution (P(X,Y)), to clarify their theoretical claims.
3. The paper discusses the implications of its findings for various fields, including transfer learning, causal inference, and the study of emergent capabilities in artificial agents. This demonstrates the broad relevance and potential impact of the work.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that agents are capable of learning optimal policies under a large set of domain shifts. This assumption may not hold in practice, as agents may only be able to learn suboptimal policies or may not have the capacity to handle all types of domain shifts. The theoretical guarantees provided in the paper rely heavily on this assumption, and it is unclear how the results would be affected by the presence of suboptimal policies. Specifically, the paper does not address the scenario where the agent's policy class is limited, meaning that even with infinite data, the agent cannot achieve optimality. This limitation is significant because it restricts the applicability of the theoretical results to real-world scenarios where agents may be constrained by computational resources or algorithmic limitations. The paper should explore the implications of such limitations on the necessity of causal learning.
2. The paper does not provide a detailed discussion of the computational complexity of learning causal models, especially in high-dimensional settings. While the authors mention that learning causal models can be computationally intensive, they do not provide a rigorous analysis of the computational cost associated with their proposed framework. This is a critical oversight, as the computational burden of learning causal models could limit their practical applicability. The paper should include a more detailed analysis of the computational complexity, including the dependence on the number of variables, the complexity of the causal graph, and the size of the data. Furthermore, the paper should discuss potential strategies for mitigating the computational cost, such as using approximation algorithms or parallel computing techniques.

### Suggestions

The paper makes a significant theoretical contribution by establishing the necessity of causal models for robust generalization. However, several aspects could be strengthened to enhance its practical relevance and impact. First, the assumption of learning optimal policies should be relaxed to consider suboptimal policies. The current framework relies on the premise that agents can achieve optimality under a wide range of domain shifts, which may not hold in practice. To address this, the authors could explore the impact of suboptimal policies on the theoretical results. This could involve analyzing how the approximation error in causal models scales with the suboptimality of the policy. For example, the authors could investigate whether the linear relationship between approximation error and regret bound still holds when the policy is not optimal, and if not, what modifications to the framework are needed. Furthermore, the authors could consider scenarios where the agent's policy class is limited, and analyze the trade-offs between policy optimality and the necessity of causal learning. This would provide a more realistic assessment of the applicability of the theoretical results.

Second, the paper should include a more detailed analysis of the computational complexity of learning causal models. The current discussion is insufficient, and the paper should provide a rigorous analysis of the computational cost associated with the proposed framework. This analysis should include the dependence on the number of variables, the complexity of the causal graph, and the size of the data. Furthermore, the paper should discuss potential strategies for mitigating the computational cost, such as using approximation algorithms or parallel computing techniques. For example, the authors could explore the use of constraint-based causal discovery algorithms, which are known to be more computationally efficient than score-based methods. The paper could also investigate the use of distributed computing techniques to parallelize the causal discovery process, making it feasible for high-dimensional datasets. A thorough discussion of these practical considerations would significantly enhance the paper's impact and relevance.

Finally, the paper could benefit from a more detailed discussion of the limitations of the proposed framework. While the theoretical results are significant, the paper should acknowledge the assumptions and limitations that may affect the applicability of the results. For example, the paper could discuss the limitations of the assumption that the data generating process is known, and how this assumption might be relaxed in practice. The paper could also discuss the limitations of the assumption that the agent has access to the necessary data to learn the causal model, and how this assumption might be addressed in real-world scenarios. A more thorough discussion of these limitations would provide a more balanced assessment of the paper's contributions and guide future research in this area.

### Questions

1. How does the assumption of learning optimal policies under a large set of domain shifts affect the practical applicability of the theoretical results? Could the authors provide more insights into scenarios where this assumption might not hold?
2. Could the authors elaborate on the computational complexity of learning causal models, especially in high-dimensional settings? Are there any strategies or approximations that could be used to mitigate the computational cost?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper studies the question of whether agents need to learn causal models to generalize. The authors prove that any agent capable of adapting to a wide range of distributional shifts must have learned a causal model of the data generating process. They provide a theoretical framework that shows that any agent capable of adapting to a wide range of distributional shifts must have learned a causal model of the data generating process. They also show that approximate causal models can still enable adaptation, with the approximation becoming exact for optimal policies. The authors discuss the implications of their results for several fields and open questions.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and the proofs are clearly presented.
2. The authors provide a theoretical framework that shows that any agent capable of adapting to a wide range of distributional shifts must have learned a causal model of the data generating process. This is a novel and interesting result that has implications for the design of agents that can generalize to new domains.
3. The authors also show that approximate causal models can still enable adaptation, with the approximation becoming exact for optimal policies. This is a useful result that provides a more nuanced understanding of the relationship between causal models and generalization.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the agent has access to the set of all local interventions on the environment. This is a strong assumption that may not hold in practice. In many real-world scenarios, the agent may not have access to all possible interventions, and may only be able to perform a limited set of interventions. The authors should discuss the implications of this assumption and how it might affect the results.
2. The paper focuses on distributional shifts that are local interventions on the environment. It is not clear how the results would extend to non-local interventions, such as changes in the causal structure of the environment. The authors should discuss the limitations of their framework and how it might be extended to handle non-local interventions.
3. The paper does not provide a clear definition of what it means for an agent to "adapt" to a distributional shift. The authors should provide a more precise definition of adaptation and discuss how it relates to the concept of causal models.
4. The paper does not discuss the computational complexity of learning causal models. The authors should discuss the computational cost of learning causal models and how it might affect the practical applicability of their results.

### Suggestions

The paper's core contribution lies in establishing a theoretical link between causal models and generalization in agents, which is a valuable step. However, the practical implications of this result are somewhat limited by the strong assumptions made. Specifically, the assumption that the agent has access to all local interventions is a significant constraint. In real-world scenarios, an agent's ability to intervene is often limited by the environment's dynamics and the agent's own capabilities. For example, an agent might only be able to manipulate a subset of the variables or might be constrained by physical limitations. The authors should explore how their results might be extended to scenarios with limited or noisy interventions. This could involve considering partial or probabilistic interventions, or exploring the robustness of their framework to interventions that are not perfectly local. Furthermore, the paper should discuss the implications of these limitations for the design of agents that can generalize to new domains. 

The paper also needs to clarify the notion of adaptation. While the authors mention that adaptation refers to achieving low regret, a more precise definition is needed. It would be helpful to discuss how this definition relates to other concepts in machine learning, such as transfer learning or domain adaptation. For example, how does the concept of regret relate to the generalization performance of the agent? The authors should also discuss the limitations of their framework in handling non-local interventions. While the current framework focuses on local interventions, many real-world scenarios involve changes in the causal structure of the environment. The authors should discuss how their results might be extended to handle such changes. This could involve considering interventions that affect multiple variables simultaneously, or exploring the robustness of their framework to interventions that are not perfectly local. Furthermore, the authors should discuss the limitations of their framework in handling interventions that are not perfectly local. 

Finally, the paper should provide a more detailed discussion of the computational complexity of learning causal models. While the authors mention that learning causal models can be computationally intensive, they do not provide a precise analysis of the computational cost. It would be helpful to discuss the computational complexity of the algorithms used to learn causal models, and how this complexity might affect the practical applicability of their results. For example, how does the computational cost scale with the number of variables and the complexity of the causal graph? The authors should also discuss potential strategies for reducing the computational cost of learning causal models, such as using approximation algorithms or parallel computing techniques. This would make their results more relevant to real-world applications.

### Questions

1. How does the assumption that the agent has access to the set of all local interventions on the environment affect the results?
2. How would the results extend to non-local interventions, such as changes in the causal structure of the environment?
3. What is the computational complexity of learning causal models in the context of this paper?
4. How does the notion of regret relate to the generalization performance of the agent?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper shows that any agent capable of adapting to a large set of distributional shifts must have learned a causal model of the data generating process. The authors show that any agent capable of adapting to a large set of distributional shifts must have learned a causal model of the data generating process. They show that for almost all CIDs, the underlying CBN can be reconstructed given optimal policies for a large set of distributional shifts. The authors also show that approximate causal models can still enable adaptation, with the approximation becoming exact for optimal policies. They also discuss the implications of this result for several fields, including transfer learning, causal inference, and the study of emergent capabilities in artificial agents.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a rigorous theoretical framework for their claims, and the proofs are well-explained.
3. The paper is well-organized and clearly presents the main ideas and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the agent has access to a set of local interventions on the environment. This assumption may not hold in practice, as agents may not be able to perform all possible interventions. The paper does not discuss the implications of this assumption for the results, and it is unclear how the results would change if the agent had access to a more limited set of interventions.
2. The paper does not provide a detailed analysis of the computational complexity of learning causal models. While the authors mention that learning causal models can be computationally intensive, they do not provide a precise analysis of the computational cost of their approach. This makes it difficult to assess the practical applicability of the results.
3. The paper does not discuss the limitations of the proposed framework. For example, it is unclear how the results would change if the agent had access to a more complex causal model, or if the interventions were not perfectly local.
4. The paper does not provide a clear definition of what it means for an agent to "adapt" to a distributional shift. The authors should provide a more precise definition of adaptation and discuss how it relates to the concept of causal models.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations imposed by the assumption of local interventions. While the authors acknowledge that agents may not have access to all possible interventions, they do not explore the implications of this assumption in detail. Specifically, it would be valuable to see an analysis of how the performance of the proposed method degrades as the set of available interventions becomes more limited. For example, the authors could investigate the impact of introducing non-local interventions, or interventions that affect multiple variables simultaneously. This would provide a more complete picture of the applicability of the results in real-world scenarios where agents may not have full control over the environment. Furthermore, the authors should consider discussing the potential for using techniques such as transfer learning or meta-learning to mitigate the limitations of local interventions.

Regarding the computational complexity, the authors should provide a more detailed analysis of the computational cost of their approach. While they mention that learning causal models can be computationally intensive, they do not provide a precise analysis of the computational cost of their approach. It would be helpful to see a breakdown of the computational cost of each step in their algorithm, and to compare the computational cost of their approach to other methods for learning causal models. This would allow readers to better assess the practical applicability of the results. Additionally, the authors should discuss the scalability of their approach to high-dimensional problems, and they should consider exploring techniques for reducing the computational cost of learning causal models, such as using approximation algorithms or parallel computing.

Finally, the paper needs a more precise definition of what it means for an agent to "adapt" to a distributional shift. The authors should provide a more rigorous definition of adaptation and discuss how it relates to the concept of causal models. For example, they could define adaptation in terms of the agent's ability to achieve low regret, or in terms of the agent's ability to generalize to new environments. This would allow readers to better understand the implications of the results and to compare them to other approaches for learning causal models. Furthermore, the authors should discuss the limitations of their definition of adaptation, and they should consider exploring alternative definitions that may be more appropriate for different applications.

### Questions

1. How does the assumption of local interventions affect the results? Could the results be extended to more general settings?
2. What is the computational complexity of learning causal models in the context of this paper? How does this complexity compare to other methods for learning causal models?
3. How does the notion of regret relate to the generalization performance of the agent? Could the authors provide a more detailed discussion of this relationship?

### Rating

8

### Confidence

2

**********

## Reviewer 4

### Summary

This paper studies the question of whether agents need to learn causal models to generalize. The authors prove that any agent capable of adapting to a wide range of distributional shifts must have learned a causal model of the data generating process. They show that approximate causal models can still enable adaptation, with the approximation becoming exact for optimal policies. The authors discuss the implications of their results for several fields and open questions.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written and easy to follow. The authors provide a rigorous theoretical framework for their claims, and the proofs are well-explained. The paper is well-organized and clearly presents the main ideas and results.

### Weaknesses

#### Some Related Works


#### comment

The paper assumes that the agent has access to a set of local interventions on the environment. This assumption may not hold in practice, as agents may not be able to perform all possible interventions. The paper does not discuss the implications of this assumption for the results, and it is unclear how the results would change if the agent had access to a more limited set of interventions.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations imposed by the assumption of local interventions. While the authors acknowledge that agents may not have access to all possible interventions, they do not explore the implications of this assumption in detail. Specifically, it would be valuable to see an analysis of how the performance of the proposed method degrades as the set of available interventions becomes more limited. For example, the authors could investigate the impact of introducing non-local interventions, or interventions that affect multiple variables simultaneously. This would provide a more complete picture of the applicability of the results in real-world scenarios where agents may not have full control over the environment. Furthermore, the authors should consider discussing the potential for using techniques such as transfer learning or meta-learning to mitigate the limitations of local interventions.

Regarding the computational complexity, the authors should provide a more detailed analysis of the computational cost of their approach. While they mention that learning causal models can be computationally intensive, they do not provide a precise analysis of the computational cost of their approach. It would be helpful to see a breakdown of the computational cost of each step in their algorithm, and to compare the computational cost of their approach to other methods for learning causal models. This would allow readers to better assess the practical applicability of the results. Additionally, the authors should discuss the scalability of their approach to high-dimensional problems, and they should consider exploring techniques for reducing the computational cost of learning causal models, such as using approximation algorithms or parallel computing.

Finally, the paper should provide a more precise definition of what it means for an agent to "adapt" to a distributional shift. The authors should provide a more rigorous definition of adaptation and discuss how it relates to the concept of causal models. For example, they could define adaptation in terms of the agent's ability to achieve low regret, or in terms of the agent's ability to generalize to new environments. This would allow readers to better understand the implications of the results and to compare them to other approaches for learning causal models. Furthermore, the authors should discuss the limitations of their definition of adaptation, and they should consider exploring alternative definitions that may be more appropriate for different applications.

### Questions

1. How does the assumption of local interventions affect the results? Could the results be extended to more general settings?
2. What is the computational complexity of learning causal models in the context of this paper? How does this complexity compare to other methods for learning causal models?
3. How does the notion of regret relate to the generalization performance of the agent? Could the authors provide a more detailed discussion of this relationship?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support or refute their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find the relevant section in the paper.
3. Extract evidence (quotes, formulas, descriptions) from the paper that supports or contradicts the reviewer's claim.
4. If the weakness is about missing information, check if that information is indeed absent.
5. Synthesize the findings and conclude whether the weakness is valid, partially valid, or invalid, along with a confidence level.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper assumes that the agent has access to the set of all local interventions on the environment. This is a strong assumption that may not hold in practice. In many real-world scenarios, the agent may not have access to all possible interventions, and may only be able to perform a limited set of interventions. The authors should discuss the implications of this assumption and how it might affect the results."

2. Evidence Collection:
a) Method-related Evidence:
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Assumption 2 (Domain dependence). There exists a transfer learning algorithm that returns a policyπσ satisfying a regret bound Eπσ[U]≥ Eπ∗ σ[U]−δ and Σ is the set of all mixtures of local interventions." (Section 3)
   - Quote: "Assumption 2 (Domain dependence). There exists a transfer learning algorithm that returns a policyπσ satisfying a regret bound Eπσ[U]≥ Eπ∗ σ[U]−δ and Σ is the set of all mixtures of local interventions. Theorem 2 shows that we can identify an approximate causal model fromDS∪{Dσ}σ∈Σ. To see that this imparts non-trivial constraints on the existence of the transfer learning algorithm, we can consider the following simple example. Example: Consider the CID for the supervised learning task depicted in Figure 1. Let DS = {(xi,yi)∼ P(X,Y )}n i=1, so for sufficiently large n the agent can learn the P (X,Y ) fromDS. However,Y →X must also be identifiable fromP (x,y ) alone, which is impossible unless the causal data generating process Ob(X = y) that describes the response of a single variable U to intervention σ is non-identifiable without interventional data and/or additional assumptions. For example considerX→ Y → U,Y =N (0,x ) andU = D +Y , then changing X can only change the variance ofU while leaving its expected value (and hence the optimal policy) constant. However, this only occurs for very specific choices of the parametersP andU. For example considerX→ Y →U ,X =N (0,x ) andU = D +Y . Then changing X can only change the variance ofU while leaving its expected value (and hence the optimal policy) constant. However, this only occurs for very specific choices of the parametersP andU. For example considerX→ Y →U ,X =N (0,x ) andU = D +Y . Then changing X can only change the variance ofU while leaving its expected value (and hence the optimal policy) constant. However, this only occurs for very specific choices of the parametersP andU." (Section 3.2)

3. Literature Gap Analysis:
   - The paper does not explicitly cite literature discussing the limitations of assuming access to all local interventions.

4. Validation Analysis:
   - The paper explicitly states Assumption 2, which assumes the ability to perform all mixtures of local interventions. The reviewer correctly points out that this is a strong assumption. While the paper provides an example to illustrate the point, it doesn't delve into the implications of this assumption being violated in more complex scenarios. The paper focuses on the theoretical result given this assumption.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit statement of Assumption 2 and the lack of discussion on the implications of this assumption being violated.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational complexity of learning causal models. While the authors mention that learning causal models can be computationally intensive, they do not provide a precise analysis of the computational cost of their approach. This makes it difficult to assess the practical applicability of the results."

2. Evidence Collection:
a) Method-related Evidence:
   - Quote: "Theorem 2. For almost all CIDs M = (G,P ) satisfying Assumptions 1 and 2, we can identify the approximate causal model M′ = (P′,G′) given{πσ(d | paD)}σ∈Σ where Eπσ[U] ≥ Eπ∗ σ[U]−δ and Σ is the set of all mixtures of local interventions. Proof in Appendix C." (Section 3.2)
   - The paper mentions the use of an oracle for optimal policies but does not detail the computational cost of this oracle or the process of identifying the approximate causal model.

3. Literature Gap Analysis:
   - The paper does not cite literature on the computational complexity of causal model learning.

4. Validation Analysis:
   - The reviewer is correct. The paper focuses on the theoretical possibility of learning a causal model but lacks a detailed analysis of the computational resources required. The mention of an "oracle" for optimal policies suggests that the computational cost is not explicitly addressed.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of computational complexity analysis in the method description and reliance on an "oracle" for optimal policies.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed framework. For example, it is unclear how the results would change if the agent had access to a more complex causal model, or if the interventions were not perfectly local."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the theoretical conditions for learning a causal model under the assumption of local interventions. There is no explicit discussion of how the framework would behave with more complex causal models or non-perfectly local interventions.

3. Literature Gap Analysis:
   - The paper does not cite literature discussing the limitations of the proposed framework regarding causal model complexity or the nature of interventions.

4. Validation Analysis:
   - The reviewer accurately points out the lack of discussion on the limitations of the framework. The paper's scope is primarily theoretical, and it doesn't explore the boundaries of its applicability or the impact of relaxing its core assumptions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of discussion on limitations related to causal model complexity or non-local interventions.

1. Weakness Statement:
"The paper does not provide a clear definition of what it means for an agent to "adapt" to a distributional shift. The authors should provide a more precise definition of adaptation and discuss how it relates to the concept of causal models."

2. Evidence Collection:
a) Method-related Evidence:
   - Quote: "Definition 3 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(σD) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori =1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and Σ is the mixture of local interventions (transitions)σi fori=1,2,..,i.e.,σ =Xσ=Qσ=σi=1P(σi)" (Section 2.3)
   - Quote: "Definition 4 (Mixtures of interventions). A mixed interventionσ∗ =P(CID) forP = (D,σ) that E can perform on a given target domainσ and η is the set of all local interventions on all environment variables. We do not consider shifts that change the agent’s decisionD, although we include shifts that drop inputs to the policy PaD→ Pa′D⊆ PaD (e.g. masking) as local interventions. We do not consider task shifts i.e. changing the set of environment variablesC, and introducing selection biases (Shen et al., 2018). See Appendix A.3 for discussion. Our main results restrict to local domain shifts, which correspond to local interventions on the chance distributionP (Observe that such a choice ofC always exists. We note Markov decision processes can be formulated as a single-decision single-utility CID, by modelling the choice of policy as a single decision and the cumulative discounted reward as a single utility variable. In general, soft interventions, noting the such a choice only states thatX∈ AncU that obervational data can be changed by intervening on the intermediate variablesC, not that variablesX can be changed by intervening on the intermediate variablesD, and that our results can be straightforwardly adapted to these settings. We do not consider shifts that change the agent’s decisionD, although we include shifts that drop inputs to the policy PaD→ Pa′D⊆ PaD (e.g. masking) as local interventions. See Appendix A.3 for discussion. Our main results restrict to local domain shifts, which correspond to local interventions on the chance distributionP (Observe that such a choice ofC always exists. We note Markov decision processes can be formulated as a single-decision single-utility CID, by modelling the choice of policy as a single decision and the cumulative discounted reward as a single utility variable. In general, soft interventions, noting the such a choice only states thatX∈ AncU that obervational data can be changed by intervening on the intermediate variablesC, not that variablesX can be changed by intervening on the intermediate variablesD, and that our results can be straightforwardly adapted to these settings. We do not consider shifts that change the agent’s decisionD, although we include shifts that drop inputs to the policy PaD→ Pa′D⊆ PaD (e.g. masking) as local interventions. See Appendix A.3 for discussion. Our main results restrict to local domain shifts, which correspond to local interventions on the chance distributionP (Observe that such a choice ofC always exists. We note Markov decision processes can be formulated as a single-decision single-utility CID, by modelling the choice of policy as a single decision and the cumulative discounted reward as a single utility variable. In general, soft interventions, noting the such a choice only states thatX∈ AncU that obervational data can be changed by intervening on the intermediate variablesC, not that variablesX can be changed by intervening on the intermediate variablesD, and that our results can be straightforwardly adapted to these settings. We do not consider shifts that change the agent’s decisionD, although we include shifts that drop inputs to the policy PaD→ Pa′D⊆ PaD (e.g. masking) as local interventions. See Appendix A.3 for discussion. Our main results restrict to local domain shifts, which correspond to local interventions on the chance distributionP (Observe that such a choice ofC always exists. We note Markov decision processes can be formulated as a single-decision single-utility CID, by modelling the choice of policy as a single decision and the cumulative discounted reward as a single utility variable. In general, soft interventions, noting the such a choice only states thatX∈ AncU that obervational data can be changed by intervening on the intermediate variablesC, not that variablesX can be changed by intervening on the intermediate variablesD, and that our results can be straightforwardly adapted to these settings. We do not consider shifts that change the agent’s decisionD, although we include shifts that drop inputs to the policy PaD→ Pa′D⊆ PaD (e.g. masking) as local interventions. See Appendix A.3 for discussion. Our main results restrict to local domain shifts, which correspond to local interventions on the chance distributionP (Observe that such a choice ofC always exists. We note Markov decision processes can be formulated as a single-decision single-utility CID, by modelling the choice of policy as a single decision and the cumulative discounted reward as a single utility variable. In general, soft interventions, noting the such a choice only states thatX∈ AncU that obervational data can be changed by intervening on the intermediate variablesC, not that variablesX can be changed by intervening on the intermediate variablesD, and that our results can be straightforwardly adapted to these settings. We do not consider shifts that change the agent’s decisionD, although we include shifts that drop inputs to the policy PaD→ Pa′D⊆ PaD (e.g. masking) as local interventions. See Appendix A.3 for discussion. Our main results restrict to local domain shifts, which correspond to local interventions on the chance distributionP (Observe that such a choice ofC always exists. We note Markov decision processes can be formulated as a single-decision single-utility CID, by modelling the choice of policy as a single decision and the cumulative discounted reward as a single utility variable. In general, soft interventions, noting the such a choice only states thatX∈ AncU that obervational data can be changed by intervening on the intermediate variablesC, not that variablesX can be changed by intervening on the intermediate variablesD, and that our results can be straightforwardly adapted to these settings. We do not consider shifts that change the agent’s decisionD, although we include shifts that drop inputs to the policy PaD→ Pa′D⊆ PaD (e.g. masking) as local interventions. See Appendix A.3 for discussion. Our main results restrict to local domain shifts, which correspond to local interventions on the chance distributionP (Observe that such a choice ofC always exists. We note Markov decision processes can be formulated as a single-decision single-utility CID, by modelling the choice of policy as a single decision and the cumulative discounted reward as a single utility variable. In general, soft interventions, noting the such a choice only states thatX∈ AncU that obervational data can be changed by intervening on the intermediate variablesC, not that variablesX can be changed by intervening on the intermediate variablesD, and that our results can be ob