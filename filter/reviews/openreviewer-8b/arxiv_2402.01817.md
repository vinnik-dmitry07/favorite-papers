# Review

## Summary
This paper argues that LLMs cannot plan or self-verify on their own, but can be useful in planning tasks when integrated with external verifiers in an LLM-Modulo Framework. It reviews the literature showing LLMs cannot reliably generate executable plans or verify plans, and discusses reasons for contrary claims. The paper proposes an LLM-Modulo Framework that uses LLMs to generate candidate plans, translate plans, help users specify problems, and help experts acquire domain models, while external verifiers check plan correctness. The framework aims to leverage LLMs' knowledge without ascribing planning abilities. Two case studies illustrate the framework's application to classical planning and travel planning, showing improved performance with LLM-Modulo Framework.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well-written and easy to follow. The authors have done a good job in explaining the key ideas and the motivation behind them. The paper is well-positioned in the literature, and the authors have done a good job in explaining the limitations of LLMs in planning and reasoning. The proposed LLM-Modulo Framework is a novel approach to integrating LLMs with external verifiers for planning tasks. The framework leverages LLMs' strengths in generating ideas and translating between representations while relying on external verifiers for correctness. The case studies demonstrate the practical applicability of the framework to different planning domains. The framework is more representative of real-world planning scenarios where plans are vetted by multiple critics before execution. The paper provides a principled approach to using LLMs in planning that avoids the pitfalls of relying on LLMs alone and provides a path forward for robust planning systems.

## Weaknesses
The paper could benefit from more detailed descriptions of the specific roles and responsibilities of LLMs and external verifiers in the framework. For instance, it would be helpful to have more examples of how LLMs can help acquire domain models and how the external verifiers integrate with the LLM to validate the plans. The paper could also provide more details on the implementation of the framework, including the specific techniques used for backprompting and the design of the Meta Controller. The evaluation of the framework is limited to two case studies. While these provide some evidence of the framework's effectiveness, a more comprehensive evaluation across a wider range of planning tasks and domains would strengthen the paper's claims. The paper could benefit from a more detailed discussion of the limitations of the LLM-Modulo Framework. For example, it would be helpful to address potential challenges in scaling the framework to more complex planning problems, integrating multiple external verifiers, and handling ambiguous or uncertain input from LLMs. The paper could also provide more analysis of the computational costs and resource requirements of the framework.

## Questions
1. Can you provide more details on how LLMs can help acquire domain models and how the external verifiers integrate with the LLM to validate the plans? 2. Can you provide more details on the implementation of the framework, including the specific techniques used for backprompting and the design of the Meta Controller? 3. How does the LLM-Modulo Framework scale to more complex planning problems? What are the computational costs and resource requirements of the framework? 4. How does the framework handle ambiguous or uncertain input from LLMs? Can you provide more details on how the framework integrates multiple external verifiers? 5. Can you provide more examples of how the framework can be applied to different types of planning tasks and domains? How does the framework perform in real-world planning scenarios?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4