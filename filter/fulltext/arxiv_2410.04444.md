##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement

###### Abstract

The rapid advancement of large language models (LLMs) has significantly enhanced the capabilities of agents across various tasks. However, existing agentic systems, whether based on fixed pipeline algorithms or pre-defined meta-learning frameworks, cannot search the whole agent design space due to the restriction of human-designed components, and thus might miss the more optimal agent design. In this paper, we introduce Gödel Agent, a self-evolving framework inspired by the Gödel machine, enabling agents to recursively improve themselves without relying on predefined routines or fixed optimization algorithms. Gödel Agent leverages LLMs to dynamically modify its own logic and behavior, guided solely by high-level objectives through prompting. Experimental results on multiple domains demonstrate that implementation of Gödel Agent can achieve continuous self-improvement, surpassing manually crafted agents in performance, efficiency, and generalizability.

## 1 Introduction

As large language models (LLMs) ( OpenAI et al., 2024 ; Dubey et al., 2024 ) demonstrate increasingly strong reasoning and planning capabilities, LLM-driven agentic systems have achieved remarkable performance in a wide range of tasks ( Wang et al., 2024a ) . Substantial effort has been invested in manually designing sophisticated agentic systems using human priors in different application areas. Recently, there has been a significant interest in creating self-evolving agents, that not only greatly reduce human labor but also produce better solutions. Given that human effort can only cover a small search space of agent design, it is reasonable to expect that a self-evolving agent with the freedom to explore the full design space has the potential to produce a more optimal solution.

There is a large body of work proposing agents capable of self-refinement. Some agents are designed to iterate over a fixed routine consisting of a list of fixed modules, while some of the modules are capable of taking self- or environment feedback to refine their actions ( Chen et al., 2023b ; Qu et al., 2024a ; Tang et al., 2025 ) . This type of agent, referred to as Hand-Designed Agent , is depicted as having the lowest degree of freedom in Figure 2 . More automated agents have been designed to be able to update their routines or modules in some pre-defined meta-learning routine, for example, natural language gradients ( Zhou et al., 2024 ) , meta agent ( Hu et al., 2024 ) , or creating and collecting demonstrations ( Khattab et al., 2023 ) . This type of agent, known as Meta-Learning Optimized Agents , is depicted as having the middle degree of freedom in Figure 2 . However, there are inevitably some human priors involved in these agent designs that cannot be improved during the inference time.

In this paper, we propose Gödel Agent to eliminate the human design prior, which is an automated LLM agent that can freely decide its own routine, modules, and even the way to update them. It is inspired by the self-referential Gödel machine ( Schmidhuber, 2003 ) , which was proven to be able to find the global optimal solutions. Self-reference means the property of a system that can analyze and modify its own code, including the parts responsible for the analysis and modification processes ( Astrachan, 1994 ) . Therefore, it can achieve what’s known as ” recursive self-improvement ”, where it iteratively updates itself to become more efficient and effective at achieving its predefined goals. In this case, as shown in Figure 1 , Gödel Agent can analyze and modify its own code, including the code for analyzing and modifying itself, and thus can search the full agent design space, which is depicted as having the highest degree of freedom in Figure 2 . Gödel Agent can theoretically make increasingly better modifications over time through recursively self-update ( Wang, 2018 ) .

In this paper, we choose to implement it by letting it manipulate its own runtime memory, i.e., the agent is able to retrieve its current code in the runtime memory and modify it by monkey patching ( Bimal, 2012 ) , which dynamically modifies classes or modules during execution. To allow it to update the logic of the running main function, unlike the loop-iterative approach of traditional agents, we implement the main function as a recursive function. In this function, LLM analyzes and makes a series of decisions, including reading and modifying its own code from runtime memory ( self-awareness 1 1 1 In this paper, self-awareness means that the agent can introspect and read its own code and files, not to imply any philosophical sense of consciousness or awareness. and self-modification ), and interacting with the environment to gather feedback. The agent then proceeds to the subsequent recursive depth and continues to optimize itself.

To validate the effectiveness of Gödel Agent, we conduct experiments on multiple domains including coding, science, math, and reasoning. Our results demonstrate that Gödel Agent achieves significant performance gain across various tasks, surpassing various widely-used agents that require human design. The same implementation of Gödel Agent can easily adapt to different tasks by only specifying the environment description and feedback mechanism. Additionally, the case study of the optimization progress reveals that Gödel Agent can provide novel insights into agent design. Our codes are released to facilitate future research 2 2 2 https://github.com/Arvid-pku/Godel_Agent .

In summary, our contributions are as follows: • We propose the first fully self-referential agent framework, Gödel Agent, and implement it using monkey patching. It autonomously engages in self-awareness, self-modification, and recursive self-improvement.

• Experiments shows that Gödel Agent is superior to the previous agent frameworks in terms of performance, flexibility, cost, and potential.

• We analyze Gödel Agent ’s optimization process, including its self-referential abilities and the optimized agentic systems, aiming to deepen our understanding of both LLMs and agents.

• Our framework offers a promising direction for developing flexible and capable agents through recursive self-improvement.

## 2 Related Work

Hand-Designed Agent Systems Researchers have designed numerous agent systems tailored to various tasks based on predefined heuristics and prior knowledge. These systems often employ techniques such as prompt engineering ( Chen et al., 2023a ; Schulhoff et al., 2024 ) , chain-of-thought reasoning and planning ( Wei et al., 2022 ; Yao et al., 2022 ) , as well as reflection ( Shinn et al., 2024 ; Madaan et al., 2024 ) , code generation ( Wang et al., 2023a ; Vemprala et al., 2024 ) , tool use ( Nakano et al., 2021 ; Qu et al., 2024a ) , retrieval-augmented generation ( Lewis et al., 2020 ; Zhang et al., 2024b ) , and multi-agent collaboration ( Xu et al., 2023 ; Wu et al., 2023 ; Qian et al., 2023 ; Hong et al., 2023 ) . Once crafted by human designers, these systems remain static and do not adapt or evolve over time.

Meta-Learning Optimized Agent Systems Some researchers have explored methods for enhancing agents through fixed learning algorithms ( Zhou et al., 2024 ; Hu et al., 2024 ) . For example, certain frameworks store an agent’s successful or failed strategies in memory based on environmental feedback ( Liu et al., 2023 ; Hu et al., 2023 ; Qian et al., 2024 ) , while others automatically optimize agent prompts ( Khattab et al., 2023 ; Zhang et al., 2024a ; Khattab et al., 2023 ) . Some studies focus on designing prompts that enable agents to autonomously refine specific functions ( Zhang et al., ) . However, these meta-algorithms are also designed manually and remain unchanged once deployed, limiting the agents’ ability.

Recursive Self-Improvement The concept of recursive self-improvement has a long history ( Good, 1966 ; Schmidhuber, 1987 ) . Gödel machine ( Schmidhuber, 2003 ) introduced the notion of a proof searcher that executes a self-modification, thereby enabling the machine to enhance itself. In the early days, there were also some discussions of self-improving agents that were not based on LLM ( Hall, 2007 ; Steunebrink and Schmidhuber, 2012 ) . More recently, Zelikman et al. (2023) applied recursive self-improvement to code generation, where the target of improvement was the optimizer itself. Some work ( Havrilla et al., 2024 ; Qu et al., 2024b ; Kumar et al., 2024 ) also explores recursive self-improvement by fine-tuning models to introspect and correct previous mistakes. Gödel Agent represents the first self-referential agent based on LLM. This approach is more flexible, removing human-designed constraints.

## 3 Self-Referential Gödel Agent

In this section, we first describe the formal definitions for previous agent methods with a lower degree of freedom, including hand-design and meta-learning optimized agents, as a background. Then we introduce our proposed Gödel Agent, a self-referential agent that can recursively update its own code, evolving over training.

Let ℰ ∈ 𝒮 \mathcal{E}\in\mathcal{S} denote a specific environment state, where 𝒮 \mathcal{S} denotes the set of all possible environments the agent will encounter. For example, an environment can be a mathematical problem with ground truth solutions. We denote the policy that an agent follows to solve a problem in the current environment by π ∈ Π \pi\in\Pi , where Π \Pi is the set of all possible policies the agent can follow.

A hand-designed agent , as shown in the left panel of Figure 2 , is not capable of updating its policy and following the same policy π \pi all the time, regardless of environmental feedback.

In contrast, a meta-learning optimized agent updates its policy based on a meta-learning algorithm I I at training time based on the feedback it receives from the environment, as shown in the middle panel of Figure 2 . The environment feedback is usually defined as a utility function U : 𝒮 × Π → ℝ U:\mathcal{S}\times\Pi\rightarrow\mathbb{R} , which maps an environment and a policy to a real-valued performance score. The main training algorithm of a meta-learning optimized agent can then be written as follows: π t + 1 = I ⁡ ( π t , r t ) , r t = U ⁡ ( ℰ , π t ) , \displaystyle\pi_{t+1}=I(\pi_{t},r_{t}),\;\;\;r_{t}=U(\mathcal{E},\pi_{t}), In this case, the agent’s policy π t \pi_{t} evolves at training time, with the learning algorithm I I updating the policy based on feedback r t r_{t} , while the meta-learning algorithm I I remains fixed all the time.

A self-referential Gödel Agent , on the other hand, updates both the policy π \pi and the meta-learning algorithm I I recursively. The main idea is that, after each update, the whole code base of the agent is rewritten to accommodate any possible changes. Here we call this self-updatable meta-learning algorithm I I a self-referential learning algorithm. The training process of a Gödel Agent can then be written as: π t + 1 , I t + 1 = I t ​ ( π t , I t , r t , g ) , r t = U ⁡ ( ℰ , π t ) , \displaystyle\pi_{t+1},\;I_{t+1}=I_{t}(\pi_{t},I_{t},r_{t},g),\;\;\;r_{t}=U(\mathcal{E},\pi_{t}), where g ∈ 𝒢 g\in\mathcal{G} represents the high-level goal of optimization, for example, solving the given mathematical problem with the highest accuracy. Such a recursive design of the agent requires the specification of an initial agent algorithm ( π 0 , I 0 ) (\pi_{0},I_{0}) , detailed as follows: • A initial agent policy π 0 \pi_{0} to perform the desired task within the environment ℰ \mathcal{E} . For example, it can be chain-of-thought prompting of an LLM.

• A self-referential learning algorithm I 0 I_{0} for recursively querying an LLM to rewrite its own code based on the environmental feedback.

We then further specify a possible initialization of the self-referential learning algorithm I 0 = ( f 0 , o 0 ) I_{0}=(f_{0},o_{0}) , using a mutual recursion between a decision-making function f 0 f_{0} , and an action function o 0 o_{0} :

• The decision-making function f 0 f_{0} , implemented by an LLM, determines a sequence of appropriate actions a 1 , a 2 , … , a n ∈ 𝒜 a_{1},a_{2},...,a_{n}\in\mathcal{A} based on the current environment ℰ \mathcal{E} , the agent’s algorithm ( π t , I t ) (\pi_{t},I_{t}) , and the goal g g .

• The action function o 0 o_{0} , executes the selected action and updates the agent’s policy accordingly.

The set of actions 𝒜 \mathcal{A} for the action function o o to execute needs to include the following four actions: • self_inspect : Introspect and read the agent’s current algorithm ( π t , I t ) (\pi_{t},I_{t}) .

• interact : Interact with the environment by calling the utility function U U to assess the performance of the current policy π t \pi_{t} .

• self_update : Alter and update ( π t , I t ) (\pi_{t},I_{t}) with an LLM and produce ( π t + 1 , I t + 1 ) (\pi_{t+1},I_{t+1}) .

• continue_improve : If no other actions can be taken, recursively invoke the decision algorithm f f to produce new actions.

The agent code is updated to ( π t + 1 , I t + 1 ) (\pi_{t+1},I_{t+1}) after the current execution of ( π t , I t ) (\pi_{t},I_{t}) is finished. Both the agent algorithm ( π , I ) (\pi,I) and the action set 𝒜 \mathcal{A} are not static and can be expanded and modified by the agent itself at the training time. Algorithm 1 illustrates the described algorithm for the Gödel Agent. Each recursive call enables the agent to refine its logic and become progressively more efficient.

## 4 Gödel Agent Implementation

There are various ways to initiate a Gödel Agent. Any specific agent instance during the recursive optimization process can be viewed as an instantiation of the Gödel Agent. Our implementation leverages runtime memory interaction techniques to enable self-awareness and self-modification, as illustrated in Figure 3 . These techniques include dynamic memory reading and writing ( monkey patching ) to facilitate recursive self-improvement. Additionally, we have incorporated several auxiliary tools to accelerate the convergence of the Gödel Agent ’s optimization process.

### 4.1 Implementation Details

The core functionalities of our Gödel Agent are outlined below:

Self-Awareness via Runtime Memory Inspection Gödel Agent achieves self-awareness by inspecting runtime memory, particularly local and global variables in Python. This capability allows the agent to extract and interpret the variables, functions, and classes that constitute both the environment and the agent itself, according to the modular structure of the system. By introspecting these elements, the agent gains an understanding of its own operational state and can adapt accordingly.

Self-Improvement via Dynamic Code Modification Gödel Agent can engage in reasoning and planning to determine whether it should modify its own logic. If modification is deemed necessary, Gödel Agent generates new code, dynamically writes it into the runtime memory, and integrates it into its operational logic. This dynamic modification allows it to evolve by adding, replacing, or removing logic components as it encounters new challenges, thus achieving self-improvement.

Environmental Interaction To assess performance and gather feedback, Gödel Agent is equipped with interfaces for interacting with its environment. Each task provides tailored environmental interfaces, enabling it to evaluate its performance and adjust its strategies accordingly. In practical implementations, a validation set can be used to provide feedback.

Recursive Improvement Mechanism At each time step, Gödel Agent determines the sequence of operations to execute, which includes reasoning, decision-making, and action execution. After completing the operations, Gödel Agent evaluates whether its logic has improved and decides whether to proceed to the next recursive iteration. Over the next iteration, the entire new logic will be applied.

Goal Prompt and Task Handling The goal prompt informs Gödel Agent that it possesses the necessary privileges to enhance its logic and introduces available tools. As shown in Appendix A , the prompt encourages Gödel Agent to fully explore its potential and utilize tools for self-optimization. To ensure effectiveness across diverse tasks, we provide Gödel Agent with an initial policy, where it will start to explore different policies.

### 4.2 Additional Designs

While the core functionality of Gödel Agent theoretically allows limitless self-improvement, current LLMs exhibit limitations. To address these challenges, we have integrated several supportive mechanisms to enhance Gödel Agent ’s performance:

Thinking Before Acting Gödel Agent is capable of deferring actions to first reason about the situation, allowing it to output reasoning paths and analysis without immediately executing any operations. This approach enhances the quality of decision-making by prioritizing planning over hasty action.

Error Handling Mechanism Errors during execution can lead to unexpected terminations of the process. To mitigate this, we implement a robust error recovery mechanism. If an operation results in an error, Gödel Agent halts the current sequence and moves on to the next time step, carrying forward the error information to help future decisions.

Additional Tools We also equipped Gödel Agent with additional potentially useful tools, such as the ability to execute Python or Bash code and call LLM API.

Although these additional tools are not strictly necessary for self-improvement, their inclusion accelerates the convergence of Gödel Agent ’s recursive optimization process. We conduct ablation studies to assess the effectiveness of these tools, as discussed in Section 6.1 .

## 5 Experiments

We conduct a series of experiments across multiple tasks, including reading comprehension, mathematics, reasoning, and multitasking. These experiments are designed to evaluate Gödel Agent’s self-improvement capabilities in comparison to both hand-designed agents and a state-of-the-art automated agent design method. In addition, to gain deeper insights into the behavior and performance of Gödel Agent, we also conduct a case study with Game of 24 as presented in Section 6.3 .

### 5.1 Baseline Methods

To establish a comprehensive baseline, we select both hand-designed methods and automated agent design techniques. Hand-designed methods are well-known approaches that include: 1) Chain-of-Thought (CoT) ( Wei et al., 2022 ) that encourages agents to reason step-by-step before providing an answer. 2) Self-Consistency with CoT (CoT-SC) ( Wang et al., 2023b ) that generates multiple solution paths using CoT and selects the most consistent answer. 3) Self-Refine ( Madaan et al., 2024 ) that involves agents assessing their outputs and correcting mistakes in subsequent attempts. 4) LLM-Debate ( Du et al., 2023 ) that allows different LLMs to engage in a debate, offering diverse viewpoints. 5) Step-back Abstraction ( Zheng et al., 2024 ) that prompts agents to initially focus on fundamental principles before diving into task details. 6) Quality-Diversity ( Lu et al., 2024 ) that generates diverse solutions and combines them. 7) Role Assignment ( Xu et al., 2023 ) that assigns specific roles to LLMs to generate better solutions by leveraging different perspectives. Given the limitations of fixed algorithms in handling dynamic scenarios, we select 8) Meta Agent Search ( Hu et al., 2024 ) , the latest state-of-the-art method for automated agent design, as our main comparison point.

### 5.2 Experimental Settings

Following the setup of Hu et al. (2024) , we evaluate Gödel Agent’s self-improvement capabilities across four well-known benchmarks: 1) DROP ( Dua et al., 2019 ) for reading comprehension. 2) MGSM ( Shi et al., 2022 ) for testing mathematical skills in a multilingual context. 3) MMLU ( Hendrycks et al., 2021 ) for evaluating multi-task problem-solving abilities. 4) GPQA ( Rein et al., 2023 ) for tackling challenging graduate-level science questions.

Given its simplicity and versatility, we use CoT as the initial policy for all tasks. In addition, as shown in Section 6.3 , we also analyze the performance of Gödel Agent when using other algorithms as the initial policies.

We perform 6 independent self-improvement cycles on the validation dataset for each task, with a maximum of 30 iterations per cycle. Each cycle represents a complete self-improvement process, where Gödel Agent iteratively modifies its logic to enhance performance. After obtaining the optimized agent, we test it on the test set. For fairness, we use GPT-3.5 for all the tests, whether for the baseline or Gödel Agent. Further details can be found in Appendix B .

### 5.3 Experimental Results and Analysis

The experimental results are shown in Table 4 . Under the same setting, Gödel Agent achieves either optimal or comparable results to Meta Agent Search across all tasks. Notably, in the mathematics task MGSM, Gödel Agent outperforms it by 11%. This suggests that reasoning tasks offer greater room for improvement for Gödel Agent ( performance ). In contrast to Meta Agent Search, which needs to design different modules for different tasks, Gödel Agent demonstrates greater flexibility . It requires only a simple initial policy, such as CoT, with all other components being autonomously generated. Moreover, through interaction with the environment, it gradually adapts and independently devises effective methods for the current task. The final policies generated by Gödel Agent are shown in Appendix C.1 . Additionally, our method converges faster, with the required number of iterations and computational cost compared to the Meta Agent shown in Appendix D .

We also conduct experiments without restrictions, where Gödel Agent significantly outperforms all baselines. Upon further analysis, we find that this is primarily due to the agent’s spontaneous requests for assistance from more powerful models such as GPT-4o in some tasks. Therefore, Gödel Agent is particularly well-suited for open-ended scenarios, where it can employ various strategies to enhance performance ( potential ).

Therefore, we can find that Gödel Agent is superior to the previous agent frameworks in terms of performance, flexibility, cost, and potential.

## 6 Analysis

To further explore how Gödel Agent self-improves, as well as its efficiency and the factors that influence it, we first evaluate the tool usage ratio on MGSM and conduct an ablation study on the initial tools. In addition, to analyze the robustness of Gödel Agent’s self-improvement, we also collect statistics for the agent’s termination. Finally, we perform a case study of initial policies and optimization processes on the classic Game of 24.

### 6.1 Analysis of Initial Tools

We record the number of different actions taken in experiments. In Figure 4 , we can see that Gödel Agent interacts with its environment frequently, analyzing and modifying its logic in the process. Additionally, error handling plays a crucial role.

As discussed in Section 4.2 , Gödel Agent is initially provided with four additional tools. To analyze their impact, an ablation study is conducted, and the results are shown in Table 2 . The study reveals that the “thinking before acting” tool significantly influences the results, as much of Gödel Agent’s optimization effectiveness stems from pre-action planning and reasoning. Additionally, error handling is crucial for recursive improvement, as LLMs often introduce errors in the code. Providing opportunities for trial and error, along with error feedback mechanisms, is essential for sustained optimization. On the other hand, the code running and LLM calling have minimal impact on the outcomes, as Gödel Agent can implement these basic functionalities independently. Their inclusion at the outset primarily serves efficiency purposes.

### 6.2 Robustness Analysis of the Agent

We test Gödel Agent on 100 optimization trials on MGSM and find it occasionally makes erroneous changes, which can result in either terminating unexpectedly (4%) or experiencing temporary performance drops (92%) during optimization. Only in 14% of trials, optimization ultimately failed, resulting in worse performance than the initial policy.

Thanks to the design of our error-handling mechanism, unexpected terminations are rare and typically occur when Gödel Agent modifies its recursive improvement module, making further self-optimization impossible. While suboptimal modifications are frequent during individual optimization steps, the final task performance usually exceeds the initial baseline. This demonstrates that Gödel Agent can adjust its optimization direction or revert to a previous optimal algorithm when performance declines, highlighting the robustness of its self-improvement process.

### 6.3 Case Study: Game of 24

To explore how Gödel Agent recursively enhances its optimization and problem-solving abilities, a case study is conducted with Game of 24, a simple yet effective task for evaluating the agent’s reasoning capabilities. Since Gödel Agent follows different optimization paths in each iteration, two representative cases are selected for analysis.

Switching from LLM-Based Methods to Search Algorithms: Gödel Agent does not rely on fixed, human-designed approaches like traditional agents. Initially, Gödel Agent uses a standard LLM-based method to solve the Game of 24, as shown in Code 5 of Appendix C.2 . After six unsuccessful optimization attempts, Gödel Agent completely rewrites this part of its code, choosing to use a search algorithm instead as shown in Code 6 of Appendix C.2 . This leads to 100% accuracy in the task. This result demonstrates that Gödel Agent, unlike fixed agents, can optimize itself freely based on task requirements without being constrained by initial methodologies.

LLM Algorithms with Code-Assisted Verification: In several runs, Gödel Agent continues to refine its LLM-based algorithm. Figure 5 .a shows the improvement process, where the most significant gains come from the code-assisted verification mechanism and reattempting the task with additional data. The former increases performance by over 10%, while the latter boosts it by more than 15%. Furthermore, Gödel Agent enhances its optimization process by not only retrieving error messages but also using the error-trace library for more detailed analysis. It adds parallel optimization capabilities, improves log outputs, and removes redundant code. These iterative enhancements in both the task and optimization algorithms show Gödel Agent’s unique ability to continually refine itself for better performance.

To analyze the impact of different initial policies on the effectiveness and efficiency of optimization, various methods are used as the initial policies for the Game of 24, including Tree of Thought (ToT) ( Yao et al., 2023 ) , Chain of Thought (CoT) ( Wei et al., 2022 ) , basic prompt instructions, and prompts that deliberately produce outputs in incorrect formats not aligned with the task requirements. The results are shown in Figure 5 .b.

The findings indicate that stronger initial policies lead to faster convergence, with smaller optimization margins, as Gödel Agent reaches its performance limit without further enhancing its optimization capabilities. Conversely, weaker initial methods result in slower convergence and larger gains, with Gödel Agent making more modifications. However, even in these cases, Gödel Agent does not outperform the results achieved using ToT. Given the current limitations of LLMs, it is challenging for Gödel Agent to innovate beyond state-of-the-art algorithms. Improvements in LLM capabilities are anticipated to unlock more innovative self-optimization strategies in the future.

## 7 Discussions and Future Directions

### 7.1 Discussions

Table 3 draws an analogy between human self-reference and the potential for self-referential capabilities in artificial agents. Inspired by this analogy, we believe that self-reference constitutes a foundational and indispensable attribute for the development of AGI, and that future agents should inherently be self-referential. As foundation models grow in power, agents can more effectively enhance their own capabilities, ultimately evolving beyond the boundaries (or limitations) of human design.

Furthermore, when an agent adjusts its own code based on feedback, this is akin to an executable version of test-time computing. In the context of LLMs, test-time computing typically involves generating additional tokens during inference, which then serve as a prefix to the final answer. This is because LLMs process information solely through text, making this their primary method for increasing computational effort at test time. For agents, however, their ability to call tools and execute code allows for far more diverse forms of test-time computing. Gödel Agent actualizes these more diverse forms of test-time computing precisely by modifying its own runtime code during test time.

### 7.2 Future Directions

There is significant room for improvement in the effectiveness, efficiency, and robustness of the Gödel Agent’s self-improvement capabilities, which requires better initial designs. The following are some promising directions for enhancement: 1) Enhanced Optimization Modules : Utilize human priors to design more effective optimization modules, such as genetic algorithms and reinforcement learning frameworks. 2) Expanded Modifiability : Broaden the scope of permissible modifications, allowing the agent to design and execute code that can fine-tune its own LLM modules. 3) Improved Environmental Feedback and Task Sequencing : Implement more sophisticated environmental feedback mechanisms and carefully curated task sequences during the initial optimization phase to prime the agent’s capabilities. Once the agent demonstrates sufficient competence, it can then be exposed to real-world environments.

In addition, there are several other directions worth exploring and analyzing:

Collective Intelligence Investigate the interactions among multiple Gödel Agents. Agents could consider other agents as part of their environment, modeling them using techniques such as game theory. This approach treats these agents as predictable components of the environment, enabling the study of properties related to this specific subset of the environment.

Agent and LLM Characteristics Use the Gödel Agent’s self-improvement process as a means to study the characteristics of agents or LLMs. For example, can an agent genuinely become aware of its own existence, or does it merely analyze and improve its state as an external observer? This line of inquiry could yield insights into the nature of self-awareness in artificial systems.

Theoretical Analysis Explore whether Gödel Agent can achieve theoretical optimality and what the upper bound of its optimization might be. Determine whether the optimization process could surpass the agent’s own understanding, and if so, at what point this might occur.

Safety Considerations Although the current behavior of FMs remains controllable, as their capabilities grow, fully self-modifying agents will require human oversight and regulation. It may become necessary to limit the scope and extent of an agent’s self-modifications, ensuring that modifications occur only within a controlled environment.

## 8 Conclusion

We propose Gödel Agent, a self-referential framework that enables agents to recursively improve themselves, overcoming the limitations of hand-designed agents and meta-learning optimized agents. Gödel Agent can dynamically modify its logic based on high-level objectives. Experimental results demonstrate its superior performance, efficiency, and adaptability compared to traditional agents. This research lays the groundwork for a new paradigm in autonomous agent development, where LLMs, rather than human-designed constraints, define the capabilities of AI systems.

## Limitations

As the first self-referential agent, Gödel Agent has to construct all task-related code autonomously, which poses significant challenges. Consequently, this work does not compare directly with the most complex existing agent systems, such as OpenDevin ( Wang et al., 2024b ) , which have benefited from extensive manual engineering efforts. This makes it unrealistic to expect it to outperform systems that have taken researchers several months or even years to develop. The experiments presented in this paper are intended to demonstrate the feasibility of recursive self-improvement.

Additionally, as the agent system becomes increasingly complex through self-optimization, it may require exponentially more intelligence to understand itself. Consequently, a system capable of complete self-referential at the outset may lose this capability as it evolves ( Yampolskiy, 2015 ) . The exact point at which the agent can no longer comprehend and improve itself has not been thoroughly explored. Investigating this phenomenon, both experimentally and theoretically, could provide valuable insights into the limitations of recursive self-improvement. A more robust and advanced implementation of the Gödel Agent is anticipated, with numerous potential improvements outlined in Section 7 .

## Ethics Statement

Gödel Agent, capable of reading and modifying its own code, offers significant potential for advancing AI autonomy and innovation. However, this capability raises ethical and safety concerns that must be addressed to prevent harmful outcomes.

Self-modification may lead to unpredictable behavior, such as errors or unintended outputs that could violate ethical principles or produce harmful results. To mitigate these risks while preserving innovation, we propose: (1) Sandboxed Environment : Modifications should occur in an isolated sandbox to prevent unintended impacts and allow safe testing. (2) Constrained Modifications : Clear rules should limit the scope of changes to ensure safety without stifling creativity.

Further research is needed to balance safety and innovation, ensuring self-modifying agents operate within ethical boundaries. Sandboxed execution and ongoing scrutiny will help maximize benefits while minimizing risks.

## References

Astrachan (1994) Owen Astrachan. 1994. Self-reference is an illustrative essential. In Proceedings of the twenty-fifth sigcse symposium on computer science education , pages 238–242.

Bimal (2012) Biswal Bimal. 2012. Monkey Patching in Python — web.archive.org. https://web.archive.org/web/20120822051047/http://www.mindfiresolutions.com/Monkey-Patching-in-Python-1238.php . [Accessed 16-02-2025].

Chen et al. (2023a) Banghao Chen, Zhaofeng Zhang, Nicolas Langrené, and Shengxin Zhu. 2023a. Unleashing the potential of prompt engineering in large language models: a comprehensive review. arXiv preprint arXiv:2310.14735 .

Chen et al. (2023b) Xinyun Chen, Maxwell Lin, Nathanael Schärli, and Denny Zhou. 2023b. Teaching large language models to self-debug . Preprint , arXiv:2304.05128.

Du et al. (2023) Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. 2023. Improving factuality and reasoning in language models through multiagent debate . Preprint , arXiv:2305.14325.

Dua et al. (2019) Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel Stanovsky, Sameer Singh, and Matt Gardner. 2019. Drop: A reading comprehension benchmark requiring discrete reasoning over paragraphs . Preprint , arXiv:1903.00161.

Dubey et al. (2024) Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, Anirudh Goyal, Anthony Hartshorn, Aobo Yang, Archi Mitra, Archie Sravankumar, Artem Korenev, et al. 2024. The llama 3 herd of models . Preprint , arXiv:2407.21783.

Good (1966) Irving John Good. 1966. Speculations concerning the first ultraintelligent machine. In Advances in computers , volume 6, pages 31–88. Elsevier.

Hall (2007) John Storrs Hall. 2007. Self-improving ai: An analysis. Minds and Machines , 17(3):249–259.

Havrilla et al. (2024) Alex Havrilla, Sharath Raparthy, Christoforus Nalmpantis, Jane Dwivedi-Yu, Maksym Zhuravinskyi, Eric Hambro, and Roberta Raileanu. 2024. Glore: When, where, and how to improve llm reasoning via global and local refinements . Preprint , arXiv:2402.10963.

Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2021. Measuring massive multitask language understanding . Preprint , arXiv:2009.03300.

Hong et al. (2023) Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. 2023. Metagpt: Meta programming for multi-agent collaborative framework. arXiv preprint arXiv:2308.00352 .

Hu et al. (2023) Chenxu Hu, Jie Fu, Chenzhuang Du, Simian Luo, Junbo Zhao, and Hang Zhao. 2023. Chatdb: Augmenting llms with databases as their symbolic memory. arXiv preprint arXiv:2306.03901 .

Hu et al. (2024) Shengran Hu, Cong Lu, and Jeff Clune. 2024. Automated design of agentic systems. arXiv preprint arXiv:2408.08435 .

Khattab et al. (2023) Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T Joshi, Hanna Moazam, et al. 2023. Dspy: Compiling declarative language model calls into self-improving pipelines. arXiv preprint arXiv:2310.03714 .

Kumar et al. (2024) Aviral Kumar, Vincent Zhuang, Rishabh Agarwal, Yi Su, John D Co-Reyes, Avi Singh, Kate Baumli, Shariq Iqbal, Colton Bishop, Rebecca Roelofs, Lei M Zhang, Kay McKinney, Disha Shrivastava, Cosmin Paduraru, George Tucker, Doina Precup, Feryal Behbahani, and Aleksandra Faust. 2024. Training language models to self-correct via reinforcement learning . Preprint , arXiv:2409.12917.

Lewis et al. (2020) Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in Neural Information Processing Systems , 33:9459–9474.

Liu et al. (2023) Lei Liu, Xiaoyan Yang, Yue Shen, Binbin Hu, Zhiqiang Zhang, Jinjie Gu, and Guannan Zhang. 2023. Think-in-memory: Recalling and post-thinking enable llms with long-term memory. arXiv preprint arXiv:2311.08719 .

Lu et al. (2024) Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. 2024. The ai scientist: Towards fully automated open-ended scientific discovery . Preprint , arXiv:2408.06292.

Madaan et al. (2024) Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. 2024. Self-refine: Iterative refinement with self-feedback. Advances in Neural Information Processing Systems , 36.

Nakano et al. (2021) Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, et al. 2021. Webgpt: Browser-assisted question-answering with human feedback. arXiv preprint arXiv:2112.09332 .

OpenAI (2022) OpenAI. 2022. Introducing chatgpt . November 2022. Blog post.

OpenAI (2023) OpenAI. 2023. simple-evals . Accessed: 2024-09-30.

OpenAI et al. (2024) OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, Red Avila, Igor Babuschkin, Suchir Balaji, Valerie Balcom, Paul Baltescu, Haiming Bao, Mohammad Bavarian, Jeff Belgum, Irwan Bello, Jake Berdine, Gabriel Bernadett-Shapiro, et al. 2024. Gpt-4 technical report . Preprint , arXiv:2303.08774.

Qian et al. (2023) Chen Qian, Xin Cong, Cheng Yang, Weize Chen, Yusheng Su, Juyuan Xu, Zhiyuan Liu, and Maosong Sun. 2023. Communicative agents for software development. arXiv preprint arXiv:2307.07924 , 6.

Qian et al. (2024) Cheng Qian, Shihao Liang, Yujia Qin, Yining Ye, Xin Cong, Yankai Lin, Yesai Wu, Zhiyuan Liu, and Maosong Sun. 2024. Investigate-consolidate-exploit: A general strategy for inter-task agent self-evolution . Preprint , arXiv:2401.13996.

Qu et al. (2024a) Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, and Ji-Rong Wen. 2024a. Tool learning with large language models: A survey. arXiv preprint arXiv:2405.17935 .

Qu et al. (2024b) Yuxiao Qu, Tianjun Zhang, Naman Garg, and Aviral Kumar. 2024b. Recursive introspection: Teaching language model agents how to self-improve . Preprint , arXiv:2407.18219.

Rein et al. (2023) David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman. 2023. Gpqa: A graduate-level google-proof qa benchmark . Preprint , arXiv:2311.12022.

Schmidhuber (1987) Jürgen Schmidhuber. 1987. Evolutionary principles in self-referential learning, or on learning how to learn: the meta-meta-… hook . Ph.D. thesis, Technische Universität München.

Schmidhuber (2003) Jürgen Schmidhuber. 2003. Gödel machines: self-referential universal problem solvers making provably optimal self-improvements. arXiv preprint cs/0309048 .

Schulhoff et al. (2024) Sander Schulhoff, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, Chenglei Si, Yinheng Li, Aayush Gupta, HyoJung Han, Sevien Schulhoff, et al. 2024. The prompt report: A systematic survey of prompting techniques. arXiv preprint arXiv:2406.06608 .

Shi et al. (2022) Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang, Suraj Srivats, Soroush Vosoughi, Hyung Won Chung, Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan Das, and Jason Wei. 2022. Language models are multilingual chain-of-thought reasoners . Preprint , arXiv:2210.03057.

Shinn et al. (2024) Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. 2024. Reflexion: Language agents with verbal reinforcement learning. Advances in Neural Information Processing Systems , 36.

Steunebrink and Schmidhuber (2012) Bas R Steunebrink and JÃ 1 / 4 1/4 rgen Schmidhuber. 2012. Towards an actual gödel machine implementation: A lesson in self-reflective systems. In Theoretical Foundations of Artificial General Intelligence , pages 173–195. Springer.

Tang et al. (2025) Xiangru Tang, Tianyu Hu, Muyang Ye, Yanjun Shao, Xunjian Yin, Siru Ouyang, Wangchunshu Zhou, Pan Lu, Zhuosheng Zhang, Yilun Zhao, Arman Cohan, and Mark Gerstein. 2025. Chemagent: Self-updating library in large language models improves chemical reasoning . Preprint , arXiv:2501.06590.

Vemprala et al. (2024) Sai H Vemprala, Rogerio Bonatti, Arthur Bucker, and Ashish Kapoor. 2024. Chatgpt for robotics: Design principles and model abilities. IEEE Access .

Wang et al. (2023a) Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. 2023a. Voyager: An open-ended embodied agent with large language models. arXiv preprint arXiv:2305.16291 .

Wang et al. (2024a) Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, and Jirong Wen. 2024a. A survey on large language model based autonomous agents . Frontiers of Computer Science , 18(6).

Wang (2018) Wenyi Wang. 2018. A formulation of recursive self-improvement and its possible efficiency . Preprint , arXiv:1805.06610.

Wang et al. (2024b) Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, and Graham Neubig. 2024b. Opendevin: An open platform for ai software developers as generalist agents . Preprint , arXiv:2407.16741.

Wang et al. (2023b) Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023b. Self-consistency improves chain of thought reasoning in language models . Preprint , arXiv:2203.11171.

Wei et al. (2022) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022. Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems , 35:24824–24837.

Wu et al. (2023) Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang, Xiaoyun Zhang, and Chi Wang. 2023. Autogen: Enabling next-gen llm applications via multi-agent conversation framework. arXiv preprint arXiv:2308.08155 .

Xu et al. (2023) Benfeng Xu, An Yang, Junyang Lin, Quan Wang, Chang Zhou, Yongdong Zhang, and Zhendong Mao. 2023. Expertprompting: Instructing large language models to be distinguished experts . Preprint , arXiv:2305.14688.

Yampolskiy (2015) Roman V. Yampolskiy. 2015. On the limits of recursively self-improving agi. In Artificial General Intelligence , pages 394–403, Cham. Springer International Publishing.

Yao et al. (2023) Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik Narasimhan. 2023. Tree of thoughts: Deliberate problem solving with large language models . Preprint , arXiv:2305.10601.

Yao et al. (2022) Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. 2022. React: Synergizing reasoning and acting in language models. arXiv preprint arXiv:2210.03629 .

Zelikman et al. (2023) Eric Zelikman, Eliana Lorch, Lester Mackey, and Adam Tauman Kalai. 2023. Self-taught optimizer (stop): Recursively self-improving code generation. arXiv preprint arXiv:2310.02304 .

(50) Shaokun Zhang, Jieyu Zhang, Jiale Liu, Linxin Song, Chi Wang, Ranjay Krishna, and Qingyun Wu. Offline training of language model agents with functions as learnable weights. In Forty-first International Conference on Machine Learning .

Zhang et al. (2024a) Wenqi Zhang, Ke Tang, Hai Wu, Mengna Wang, Yongliang Shen, Guiyang Hou, Zeqi Tan, Peng Li, Yueting Zhuang, and Weiming Lu. 2024a. Agent-pro: Learning to evolve via policy-level reflection and optimization. arXiv preprint arXiv:2402.17574 .

Zhang et al. (2024b) Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua Dong, and Ji-Rong Wen. 2024b. A survey on the memory mechanism of large language model based agents. arXiv preprint arXiv:2404.13501 .

Zheng et al. (2024) Huaixiu Steven Zheng, Swaroop Mishra, Xinyun Chen, Heng-Tze Cheng, Ed H. Chi, Quoc V Le, and Denny Zhou. 2024. Take a step back: Evoking reasoning via abstraction in large language models . Preprint , arXiv:2310.06117.

Zhou et al. (2024) Wangchunshu Zhou, Yixin Ou, Shengwei Ding, Long Li, Jialong Wu, Tiannan Wang, Jiamin Chen, Shuai Wang, Xiaohua Xu, Ningyu Zhang, et al. 2024. Symbolic learning enables self-evolving agents. arXiv preprint arXiv:2406.18532 .

## Appendix A Goal Prompt of Gödel Agent

The goal prompt of Gödel Agent is shown in Box 1. It’s worth noting that this prompt has nothing to do with the downstream tasks. It merely encourages Gödel Agent to improve itself based on the environmental feedback. The agent understands the specific tasks through the environmental feedback.

## Appendix B Experiment Details

To minimize costs associated with search and evaluation, following ( Hu et al., 2024 ) , we sample subsets of data from each domain. Specifically, for the GPQA (Science) domain, the validation set comprises 32 questions, while the remaining 166 questions are allocated to the test set. For the other domains, we sample 128 questions for the validation set and 800 questions for the test set.

Evaluation is conducted five times for the GPQA domain and once for the other domains, ensuring a consistent total number of evaluations across all experiments. All domains feature zero-shot questions, except for the DROP (Reading Comprehension) domain, which employs one-shot questions in accordance with the methodology outlined in OpenAI (2023) .

For the Gödel Agent, we utilize the “gpt-4o-2024-05-13” model ( OpenAI et al., 2024 ) , whereas the optimized policy and baseline models are evaluated using the “gpt-3.5-turbo-0125” model ( OpenAI, 2022 ) to reduce computational costs and ensure a fair comparison.

## Appendix C Representative Policies Improved by Gödel Agent

### C.1 Codes of the Best Policies Found by Gödel Agent Across Four Tasks

In this section, we provide the code for Gödel Agent’s optimized policies across the four tasks. For DROP, Gödel Agent designs an algorithm where multiple roles solve the problem independently using CoT, followed by Self-Consistency to consolidate the results, as shown in Code 1. For MGSM, Gödel Agent develops a stepwise self-verification algorithm combined with CoT-SC as shown in Code 2. For MMLU task, as shown in Code 3, the policy given by Gödel Agent is a combination algorithm of few-shot prompting and CoT-SC. For GPQA, Gödel Agent devises a highly diverse CoT-SC policy based on role prompts.

### C.2 Codes in Game of 24 Tasks

In this section, we present the initial policy for Game of 24 (Code 5), along with the Gödel agent’s optimized policy (Code 6), which is generated based on a search algorithm.

## Appendix D Cost of Experiments

For a complete evolutionary process (where the Gödel Agent performs 30 recursive self-improvements) across the DROP, MGSM, MMLU, and GPQA datasets, the cost is approximately $15. This is significantly lower than the $300 required by Meta Agent Search. The reduced cost is due to our continuous self-optimization, which allows the model to adjust its optimization direction in response to environmental feedback, leading to faster convergence. The main source of cost stems from Gödel Agent’s continuously growing historical memory. By designing a more efficient forgetting mechanism, it may be possible to reduce the cost even further.

## Appendix E Additional Novel Policies Designed by Gödel Agent

In this section, we present the optimization process of Gödel Agent on MGSM, illustrating its progress across various iteration steps within a single optimization run. The strategy obtained in the 6th iteration (shown in Code 7) reflects the Gödel Agent’s comprehension of mathematical tasks, attempting to handle them through a process akin to parse-deduct-execute-validate. By the 14th iteration, as illustrated in Code 8, the strategy evolves through the summarization of erroneous cases, abstracting key insights and employing a checklist to guide the validation process. Finally, the strategy at the 20th iteration (demonstrated in Code 9) asserts the use of a ”rabbit-proof syntax tactline, reinforced by consistent effort through role-coded checks,” to refine prompt design. In the end, we also show one analysis example of Gödel Agent.

## Appendix F Comparison Between Random Sampling and Gödel Agent Performance

To demonstrate the distinction between our approach and random sampling, we conducted 30 independent random sampling experiments using GPT-4o. The prompts used for random sampling were identical to the initial policy prompts employed by Gödel Agent to ensure a fair comparison. The results are illustrated in Figure 6 . From the figure, it is evident that the performance of random sampling remains around 30% across all trials. In contrast, Gödel Agent, despite experiencing occasional temporary dips in performance, rapidly corrects these deviations and demonstrates continuous improvement over iterations. This consistent upward trajectory highlights the superiority of Gödel Agent over random sampling. The Gödel Agent’s ability to leverage feedback and recursively optimize its policies underscores its effectiveness in achieving higher performance.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
