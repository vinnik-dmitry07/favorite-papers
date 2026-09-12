##### Report GitHub Issue

Content selection saved. Describe the issue below:

# AlphaGo Moment for Model Architecture Discovery

###### Abstract

While AI systems demonstrate exponentially improving capabilities, the pace of AI research itself remains linearly bounded by human cognitive capacity, creating an increasingly severe development bottleneck. We present ASI-Arch , the first demonstration of Artificial Superintelligence for AI research (ASI4AI) in the critical domain of neural architecture discovery—a fully autonomous system that shatters this fundamental constraint by enabling AI to conduct its own architectural innovation. Moving beyond traditional Neural Architecture Search (NAS), which is fundamentally limited to exploring human-defined spaces, we introduce a paradigm shift from automated optimization to automated innovation . ASI-Arch can conduct end-to-end scientific research in the challenging domain of architecture discovery, autonomously hypothesizing novel architectural concepts, implementing them as executable code, training and empirically validating their performance through rigorous experimentation and past human and AI experience. ASI-Arch conducted 1,773 autonomous experiments over 20,000 GPU hours, culminating in the discovery of 106 innovative, state-of-the-art (SOTA) linear attention architectures. Like AlphaGo’s Move 37 that revealed unexpected strategic insights invisible to human players, our AI-discovered architectures demonstrate emergent design principles that systematically surpass human-designed baselines and illuminate previously unknown pathways for architectural innovation (Fig. 2 ). Crucially, we establish the first empirical scaling law for scientific discovery itself—demonstrating that architectural breakthroughs can be scaled computationally, transforming research progress from a human-limited to a computation-scalable process . We provide comprehensive analysis of the emergent design patterns and autonomous research capabilities that enabled these breakthroughs, establishing a blueprint for self-accelerating AI systems. To democratize AI-driven research, we open-source the complete framework, discovered architectures, and cognitive traces.

## 1 Introduction

Artificial Intelligence (AI) is impacting human society with unprecedented depth and breadth, and is widely regarded as a key driver of civilization’s progress Russell and Norvig (2010) ; Agrawal et al. (2018) ; Brynjolfsson and Mitchell (2017) . However, a fundamental paradox emerges: while AI systems demonstrate exponentially improving capabilities, the pace of AI research itself remains linearly bounded by human cognitive capacity The White House (2023) ; Ahmed et al. (2022) ; Sevilla et al. (2022) . This human-centric development model creates an increasingly severe bottleneck for AI advancement, where the velocity of innovation is constrained not by computational power, but by human research bandwidth . This motivates a transformative vision: Artificial Superintelligence for AI research (ASI4AI) —AI systems capable of autonomously conducting their own scientific research and designing more powerful next-generation models.

Neural architecture discovery stands as the most challenging and impactful frontier for realizing ASI4AI. Model architecture serves as the cornerstone of the AI technology stack, with each major leap in AI capabilities—from image recognition to natural language understanding—accompanied by corresponding architectural breakthroughs. The evolution from CNNs LeCun et al. (1995) to Transformers Vaswani et al. (2017) exemplifies how architectural innovation drives fundamental progress in AI. At the forefront of current research, a pivotal challenge involves enhancing computational efficiency while maintaining expressive power DeepSeek-AI et al. (2024) ; MiniMax et al. (2025) ; Yuan et al. (2025) . To ground our exploration in a domain of both fundamental importance and active research, we focus on attention-based architectures as our testbed, leveraging their extensive knowledge base to explore AI’s true architectural design potential Katharopoulos et al. (2020) ; Choromanski et al. (2020) ; Tay et al. (2022) ; Wang et al. (2020) .

Moving beyond traditional Neural Architecture Search (NAS), which is fundamentally limited to exploring human-defined spaces, our work represents a paradigm shift from automated optimization to automated innovation. While previous NAS methods Zoph and Le (2016) ; Real et al. (2017) ; Elsken et al. (2019) ; Cheng et al. (2025) could only optimize over predetermined building blocks at prohibitive computational costs, acting as sophisticated selection algorithms rather than creative agents, we present ASI-Arch —the first demonstration of ASI4AI in neural architecture discovery. Leveraging the advanced reasoning and coding capabilities of modern LLMs Brown et al. (2020) ; OpenAI (2023) ; Li et al. (2022) , ASI-Arch transcends human-designed search spaces by autonomously hypothesizing novel architectural concepts, implementing them as executable code, and empirically validating their performance through rigorous experimentation Chen et al. (2023) ; Zhang et al. (2024) .

This represents AI’s first demonstration of genuine scientific superintelligence in neural architecture design. Like AlphaGo’s Move 37 that revealed strategic insights invisible to human players, ASI-Arch discovers architectural principles that systematically surpass human intuition. After conducting 1,773 autonomous experiments over 20,000 GPU hours, ASI-Arch successfully discovered 106 novel, state-of-the-art linear attention architectures. Crucially, we establish the first empirical scaling law for scientific discovery itself—demonstrating that architectural breakthroughs can be scaled computationally, transforming research progress from a human-limited to a computation-scalable process and providing a concrete pathway toward ASI4AI.

Our primary contributions establish a blueprint for self-accelerating AI systems and advance this paradigm: • ASI4AI Framework: We design and build the first demonstration of Artificial Superintelligence for AI research through a highly autonomous, tool-centric multi-agent system that enables AI to independently conduct the entire scientific research process—from hypothesis generation to empirical validation—in neural architecture discovery.

• Emergent Design Intelligence: Through comprehensive analysis, we identify novel design patterns that emerge from AI-driven discovery, demonstrating qualitatively different architectural intelligence that expands beyond human design paradigms and establishes new principles for attention mechanism innovation.

• Computational Scaling of Discovery: We discover 106 novel, state-of-the-art linear attention architectures and establish the first scaling law for automated scientific breakthroughs, proving that research progress can be scaled with computational resources rather than human expertise. We open-source the complete framework, discovered architectures, and cognitive traces to democratize AI-driven research.

## 2 Related Work

#### AI For AI Research

The application of artificial intelligence to advance AI research itself represents a compelling frontier Kokotajlo et al. (2025) , best understood as a spectrum of increasing AI autonomy within the scientific process. Initially, AI’s role resembled that of a sophisticated assistant, handling specific tasks like code generation in a “copilot” model where human researchers retained full control of the research direction. The collaboration has since evolved toward AI as an “AI scientist” capable of independently generating novel hypotheses and proposing promising research ideas for human consideration Tshitoyan et al. (2019) ; Boiko et al. (2023) . More recently, several examples have demonstrated AI’s ability to navigate the entire research cycle with minimal human intervention. Frameworks such as AlphaEvolve Novikov et al. (2025) ; Cheng et al. (2025) , for instance, employ LLMs to iteratively mutate and select improved program variants, completing a full loop of discovery and refinement. Similarly, AlphaGeometry’s success in autonomously discovering mathematical proofs showcases a high degree of research autonomy from problem statement to solution Trinh et al. (2024) ; Chervonyi et al. (2025) . As the proportion of human involvement in this collaborative loop decreases, the potential for AI’s self-optimization becomes increasingly central. This concept is epitomized by self-referential systems like Darwin-Gödel machines Zhang et al. (2025) , which are designed to iteratively modify their own code and empirically validate these changes, marking a clear trajectory toward fully self-improving systems Schmidhuber (1997) ; Baum (2004) .

Building upon this path, ASI-Arch applies the principles of AI self-evolution to the highly complex domain of neural architecture design. This presents a greater challenge than prior self-improving systems, as architectural exploration involves a significantly more complex experimental environment and a vast search space where success is not guaranteed. Our work therefore represents a significant attempt to advance AI self-evolution in this more demanding and impactful frontier.

#### Efficient Architecture

The Transformer architecture has dominated sequence modeling since its introduction, but its quadratic attention complexity has catalyzed extensive research into sub-quadratic alternatives, creating an increasingly complex design space Vaswani et al. (2017) . Among these alternatives, sparse attention approaches like Native Sparse Attention (NSA) Yuan et al. (2025) employ hierarchical sparse strategies to achieve substantial speedups while maintaining model capabilities. Beyond sparse attention, three principal families have emerged with linear time complexity: Linear Attention, which uses linearizing feature maps Katharopoulos et al. (2020) ; Choromanski et al. (2020) ; Qin et al. (2022) ; State-Space Models (SSMs) like Mamba, employing structured state transition matrices Gu and Dao (2023) ; Dao and Gu (2024) ; and Linear RNNs such as RWKV, with matrix-valued recurrent states Peng et al. (2023) ; Qin et al. (2023) ; Qin et al. (2024b) . The current trajectory points toward synthesis and hybridization, with architectures like Jamba interleaving different model families to leverage their respective strengths Lieber et al. (2024) ; Qin et al. (2024a) . This evolution has transformed the landscape from a single dominant design to a vast combinatorial space where optimal architectures are highly dependent on specific tasks and constraints. While existing work focuses on manually designing individual architectural components or families, this process is often protracted, requiring months of iterative effort from human experts to yield a single state-of-the-art architecture. In contrast, ASI-Arch uniquely addresses the systematic exploration of this complex design landscape through automated multi-agent collaboration, enabling the discovery of novel architectures that transcend traditional family boundaries.

## 3 Methodology

ASI-Arch framework operates as a closed-loop system for autonomous architecture discovery, structured around a modular framework with three core roles. The Researcher module proposes novel architectures, the Engineer module conducts empirical evaluations by executing them in a real-world environment, and the Analyst module performs analytical summaries of the results to acquire new insights. All experimental data and derived insights are systematically archived in a central database, creating a persistent memory that drives the entire process.

To ensure the system progressively generates superior designs, we implement an evolutionary improvement strategy that enables the model to continuously learn from experience. This is realized through two key mechanisms: first, a comprehensive fitness score that holistically evaluates each new architecture, providing a clear optimization target; and second, the ability to leverage both distilled knowledge from human expert literature (cognition) and analytical summaries of its own past experiments (analysis) to inform subsequent design proposals. Given the resource-intensive nature of this evolutionary process, we adopt a two-stage exploration-then-verification strategy. The initial stage involves broad exploration on small-scale models to efficiently identify a large pool of promising candidates. In the final stage, these candidates are scaled up to larger models for rigorous validation, confirming their state-of-the-art performance.

### 3.1 The Fitness Function

ASI-Arch ’s model architecture evolution mirrors biological evolution, drawing insights from the principles of natural selection. In nature, fitness determines an organism’s survival and reproduction, and similarly, we define a fitness function that governs which architectures survive and propagate through our evolutionary process. A critical flaw in past approaches is their sole reliance on quantitative metrics like loss and benchmark scores. This narrow focus inevitably leads to reward hacking Amodei et al. (2016) , where the system learns to maximize scores without producing genuinely superior architectures. We expand this definition by incorporating a qualitative assessment of the architecture itself. Our composite fitness combines both quantitative and qualitative dimensions, holistically evaluating performance and design quality:

Fitness = Objective Performance ⏟ Quantitative + Architectural Quality ⏟ Qualitative \text{Fitness}=\underbrace{\text{Objective Performance}}_{\text{Quantitative}}+\underbrace{\text{Architectural Quality}}_{\text{Qualitative}} (1)

In our framework, the objective performance assessment evaluates both benchmark scores and loss performance relative to baseline architectures. Recognizing that scientific breakthroughs often emerge from incremental advances, we apply a sigmoid transformation to performance differences: σ ⁡ ( Δ performance ) \sigma(\Delta_{\text{performance}}) . This transformation serves a dual purpose—amplifying small but potentially significant improvements while capping extreme values that could otherwise dominate the optimization process. For the architectural quality assessment, we introduce a separate LLM that acts as an expert evaluator, mimicking how a human specialist would judge architectural merit. This judge examines multiple dimensions: architectural innovation, structural complexity, implementation correctness, and convergence characteristics. By incorporating these qualitative assessments alongside quantitative metrics, we capture architectural qualities that resist simple numerical measurement. Our final composite fitness function thus takes the form:

Fitness = 1 3 ​ [ σ ⁡ ( Δ loss ) + σ ⁡ ( Δ benchmark ) + LLM judge ] \text{Fitness}=\frac{1}{3}\left[\sigma(\Delta_{\text{loss}})+\sigma(\Delta_{\text{benchmark}})+\text{LLM}_{\text{judge}}\right] (2)

where σ ⁡ ( Δ loss ) \sigma(\Delta_{\text{loss}}) and σ ⁡ ( Δ benchmark ) \sigma(\Delta_{\text{benchmark}}) represent sigmoid-transformed performance improvements over baseline, and LLM j ​ u ​ d ​ g ​ e \text{LLM}_{judge} provides the subjective quality assessment normalized to [0,1].

### 3.2 Researcher: Propose New Architecture

The Researcher module serves as the creative engine of our system, where AI independently proposes novel model architectures based on historical experience and human expertise. Our design targets two critical objectives: ensuring high-quality architectural innovations while preventing repeated explorations that squander computational resources. To achieve these goals, we implement four key mechanisms that work together:

#### Seed Selection

ASI-Arch maintains a candidate pool containing the top-50 highest-scoring architectures from all previous experiments. For each evolution step, we use a two-level sampling approach: one parent architecture is randomly selected from the top-10 performers to serve as the base for modifications, while 4 reference architectures are sampled from positions 11-50 to provide diverse design examples. This two-tier selection ensures that evolution builds on proven success while maintaining enough randomness to explore new directions. The parent architecture gets modified directly, while the reference architectures serve as examples of successful design patterns without being changed themselves.

#### Model Design

Before providing historical data to the Researcher for the next evolution cycle, we perform a crucial data summarization step. Each architecture in our database contains extensive information, including its motivation, implementation code, experimental results, and detailed analysis. To manage context size, we use a low-temperature LLM to generate brief, factual summaries of the natural language portions for each historical architecture. Critically, these summaries are generated on-the-fly for each evolutionary cycle and are not stored in the database. This dynamic summarization process inherently introduces subtle variations in how the same historical data is presented over time. This not only prevents the Researcher from receiving a static, repetitive context, which could limit the diversity of its outputs, but also actively encourages more varied design explorations. The final combined summaries provide the evolution model with both a manageable context and a constantly refreshed set of diverse insights to inform the next design attempt.

#### Program Implementation

Traditional approaches often separate architectural design from code implementation, using specialized models for each task. However, this separation creates a critical information gap—the implementation model, seeing only the high-level motivation, lacks the rich context that informed the original design. This often leads to implementation drift where the final code differs from the intended architecture. ASI-Arch addresses this by using a single agent for both tasks: first proposing the architectural motivation with full access to all context, then immediately implementing the corresponding code while maintaining complete awareness of the design reasoning.

#### Novelty and Sanity Check

To ensure that each proposed architecture is both novel and will be correctly implemented, we implement a two-stage validation process before it is accepted for training. The first stage is a similarity check to prevent redundancy. When a new architecture is proposed, we first extract its motivation and use embedding-based search to find the top-5 most similar historical motivations. A specialized LLM then evaluates whether the new proposal represents a genuine innovation or merely a variation of existing work. The second stage consists of code-level sanity checks to prevent fundamental implementation flaws, including verifying that the code does not exceed O ⁡ ( n 2 ) O(n^{2}) complexity and ensuring that masking is implemented correctly to prevent information leakage. If a proposal fails either the novelty or the correctness check, it is rejected, and the relevant feedback is returned to the agent to prompt a rewrite.

### 3.3 Engineer: Train and Evaluate Models

The evaluation process, which provides the data for the final fitness score, is composed of two parts: quantitative evaluation in a real code environment and qualitative scoring by an LLM-as-judge.

#### Real Code Environment

The quantitative evaluation takes place within an interactive coding environment where the agent must utilize a defined set of tools to initiate training, modify code, and inspect error logs. A key differentiator of ASI-Arch is its robust self-revision mechanism. In stark contrast to previous work Cheng et al. (2025) that often uses static analysis like Abstract Syntax Tree (AST) parsing and simply discards any architecture that fails these checks, ASI-Arch requires the agent to fix its own mistakes. When a training run fails due to an implementation error, the system automatically captures the full error log and delivers it back to the agent, which is then tasked with analyzing this feedback and revising its previously generated code. This iterative debugging loop continues until training is successful, ensuring promising ideas are not prematurely discarded due to simple coding mistakes. Furthermore, to maintain high efficiency, an automated quality assurance system monitors training logs in real-time. This is critical because some functional designs can be prohibitively inefficient, such as a model consuming two to three times the training duration of its peers. ASI-Arch detects such anomalies, as well as fundamental bugs indicated by abnormally low loss, and immediately terminates the run, reporting the issue back to the agent for revision. This proactive termination prevents wasting resources on flawed architectures and significantly accelerates the overall search process.

#### LLM-as-Judge Scoring

Following the quantitative evaluation, we initiate an LLM-based scoring module to provide a qualitative assessment. This scoring process considers not only the objective performance metrics but also the architectural complexity, computational efficiency, and the novelty of the proposed ideas, all benchmarked against baseline models. To ensure consistency and reproducibility, we provide a detailed syllabus in the prompt and slightly increase the model’s temperature, encouraging it to generate more detailed and nuanced justifications for its scores.

### 3.4 Analyzer: Mine Experimental Insights

To drive the evolutionary process, ASI-Arch provides the agent with two distinct sources of knowledge for each subsequent design step: cognition, derived from accumulated human expertise, and analysis, generated dynamically from the system’s own experimental history.

#### Cognition Base

To ensure ASI-Arch can leverage existing domain knowledge, we construct a cognition-centered knowledge base. We selected nearly 100 seminal papers from the field of linear attention and used a dedicated LLM to extract 1-3 distinct cognitions from each. Each cognition is a structured entry composed of three key elements: the applicable scenario, which describes the specific problem the original paper aimed to solve; the proposed algorithm, which summarizes the core technical solution; and the historical context, which situates the paper within the research trends of its time.

To guarantee the utility of this knowledge base, we carefully engineered the prompt for the extraction LLM. The prompt’s structure is specifically designed to ensure that the extracted “experiment trigger” align semantically with the “problem analyses” generated by our Analyst module. This alignment is crucial for effective retrieval. In the final stage of analysis, the Analyst summarizes the specific shortcomings observed in the current experiment, and this summary is used as a query for embedding-based retrieval against the scenarios in our knowledge base. The retrieved cognition content is then stored in our database for future reference, providing a highly relevant, information-dense, and targeted way for the Researcher module to find solutions.

#### Contextual Analysis

ASI-Arch generates its own insights through a dedicated Analysis Module driven by a large language model. This agent is provided with the complete set of information from the current experiment, including all performance metrics, training logs, and the performance of baseline models. Furthermore, to achieve an effect analogous to an ablation study, we also supply the data from the parent and sibling nodes of the current architecture in the phylogenetic tree. Based on the assumption that these nodes share significant structural similarities, we expect the agent to infer the specific contributions of individual modules by comparing the performance differences among these closely related architectures. The resulting analysis is then archived to inform subsequent design cycles.

### 3.5 Exploration-then-Verification Strategy

Given the resource-intensive nature of architecture evaluation, we adopt a two-stage exploration-then-verification strategy to maintain feasibility and efficiency. The underlying principle is that a truly superior architecture should demonstrate its advantages across different settings. Therefore, in the initial exploration stage, we use smaller models and resource-efficient protocols to rapidly identify a large pool of promising candidates that outperform a baseline. In the subsequent verification stage, only these promising candidates are scaled up with increased parameter sizes for extensive training and rigorous validation against established, state-of-the-art baselines. This two-stage approach allows us to balance the need for broad exploration with the necessity of thorough, high-fidelity validation.

## 4 Experiments

### 4.1 Experimental Setup

#### Fitness Function

Throughout our experiments, we use DeltaNet Yang et al. (2024b) as our baseline. As described in Section 3.1, our scoring system consists of three components. For quantitative scoring, since architectural differences in linear attention typically produce small performance variations, we focus only on differences within 10% of baseline and map these through a sigmoid function to obtain scores. Additionally, architectures with losses more than 10% below baseline are considered to have information leakage and are immediately discarded. For qualitative scoring, we establish a calibrated scale with DeltaNet at 5 points as the midpoint and Gated DeltaNet Yang et al. (2024a) at 10 points as the upper reference. The LLM evaluator assesses each architecture on this 1-10 scale.

#### Parallel Search Architecture and Policy

To accelerate discovery, we run numerous search processes in parallel. This is supported by a cloud-based database that stores all historical experiment results, allowing different agents to add or request data through API services and share all accumulated knowledge. To manage this parallel exploration effectively while encouraging diversity, we implement a strategic candidate pool update policy:

• Cold Start : At the beginning of our experiments, ASI-Arch conducts 200 explorations without database updates. This initial phase encourages the model to explore diverse architectural frameworks broadly rather than immediately converging on variations of early discoveries.

• Batched Updates : After the cold start period, we update the candidate pool only after every 50 new entries, rather than dynamically selecting the top-50. This batched approach ensures all agents work with stable reference sets during each exploration phase, promoting consistency while the initial delay fosters creativity.

#### Efficiency-Oriented Framework Settings

As outlined in our methodology, our search process is divided into two distinct phases with different configurations:

• Exploration Stage : To enable large-scale exploration, we constrain model size to approximately 20M parameters trained on 1B tokens. For evaluation, we sample only 500 examples per benchmark to balance assessment quality with computational efficiency.

• Verification Stage : The most promising candidates from the exploration stage are advanced to a rigorous verification phase. Here, we scale the architectures to 400M parameters and train them on 1B tokens for an initial performance validation. The top-performing models from this group are then selected for a final, more extensive training run on a 15B token dataset to comprehensively evaluate their capabilities against strong baselines.

### 4.2 Main results

To balance exploration efficiency with validation accuracy, we adopt a two-stage strategy: initial exploration on small models followed by verification on larger models. In the first stage, we conducted 1,773 explorations using 20M parameter models, consuming approximately 10,000 GPU hours. A partial phylogenetic tree of this first stage is shown in Figure 5 . From these experiments, we filtered architectures that outperformed DeltaNet at equivalent parameter scales in both loss and benchmark metrics, yielding 1,350 promising candidates. In the second stage, we scaled these candidates to 340M parameters matching DeltaNet’s configuration and filtered out architectures with excessive complexity or parameter counts. We then trained approximately 400 model architectures on 1B tokens, using 10,000 GPU hours. Among these, 106 architectures achieved state-of-the-art results, all of which are publicly available on our Model Gallery website for community reference. For final validation, we selected 5 top-performing architectures and trained them at 340M parameters setting on 15B tokens. These models were compared against DeltaNet, Gated DeltaNet, and Mamba2 under identical experimental settings. As presented in Table 1 , our models outperform almost all baselines on various benchmarks. The five architectures selected for this final validation are detailed below, each representing a distinct strategy for improving upon the DeltaNet baseline:

• Hierarchical Path-Aware Gating (PathGateFusionNet): This architecture introduces a hierarchical, two-stage router to resolve the trade-off between local and global reasoning. The first stage allocates budget between a direct copy path and a contextual pool, while the second stage distributes that contextual budget across short-range, long-range, and Delta-rule paths. It ensures stable gradient flow with a small, always-on residual connection and adds head-specific output gates for fine-grained local control.

• Content-Aware Sharpness Gating (ContentSharpRouter): This model addresses the challenge of creating a gate that is both content-aware and capable of making decisive (sharp) routing decisions. It fuses two key ideas: a content-aware gate that uses token embeddings and path statistics to inform its decision, and a learnable, per-head temperature parameter that allows the model to dynamically control the sharpness of the routing softmax, preventing premature gate collapse.

• Parallel Sigmoid Fusion with Retention (FusionGatedFIRNet): This architecture fundamentally changes the gating mechanism to break the “zero-sum” trade-off imposed by softmax. It replaces the single softmax router with parallel, independent sigmoid gates for each path. This allows the model to activate local and global paths simultaneously. It also enhances the Delta-rule with a learnable, per-head retention parameter, giving it a controllable memory horizon.

• Hierarchical Gating with Dynamic Floors (HierGateNet): This model employs a two-stage hierarchical gate to separate macro (local vs. global) and fine-grained routing decisions. Its key innovation is the use of dynamic, learnable floors for each path and head. This mechanism guarantees that no critical pathway (especially the Delta-path for long-range reasoning) is ever fully collapsed, adapting its minimum allocation based on the context.

• Adaptive Multi-Path Gating (AdaMultiPathGateNet): This design focuses on providing maximum control at the finest granularity. It implements a unified BalancedSparseGate that combines global, per-head, and per-token logits, allowing every path to be controlled at the token level. To prevent gate collapse, it uses a combination of a small epsilon-floor and a persistent, always-on entropy penalty, ensuring path diversity without complex training schedules.

## 5 Analysis

The evolution of architectures in ASI-Arch is driven by a candidate pool that is updated after every 50 new architectures are generated. Since each architecture mutation step exclusively references data from this pool, we analyze the search process sequentially according to the generation order, using a batch of 50 architectures as our fundamental unit of analysis. To facilitate our investigation into what distinguishes high-performing models, we collectively refer to the top 106 architectures as the “model gallery” .

### 5.1 Effectiveness of LLM-Driven Architecture Search

To demonstrate the effectiveness of our LLM-driven neural architecture search system, we examine how the search process evolves over time. Since our system exclusively selects parent architectures from the top-50 candidate pool for modification, the characteristics of this pool directly determine the search trajectory and ultimate performance. Therefore, we analyze two key sets of metrics related to this candidate pool: (1) both the overall trend of the average fitness score for the top-50 candidates and the individual trends of its three components: loss improvement, benchmark improvement, and the LLM judge score; and (2) the average raw performance, specifically the benchmark scores and loss values, of these same candidates. These metrics collectively provide a comprehensive view of our system’s search dynamics and continuous optimization process.

Analysis of the search dynamics reveals several complementary patterns. First, the average fitness score of the top-50 candidates follows a characteristic learning curve, with rapid initial gains that gradually stabilize Figure 6 b. The early-stage score increase is primarily driven by the optimization of the loss component. The subsequent stabilization is a direct result of our fitness function’s design; due to the sigmoid transformation, even significant performance gains in later stages are mapped to smaller score increases. This prevents reward hacking by capping the score contribution from any single metric and thus discouraging over-optimization. Importantly, while the fitness score growth flattens by design, the system does not encounter a performance bottleneck, as evidenced by the continued, steady improvement in the raw benchmark and loss metrics. This convergent evidence confirms that our LLM-driven search effectively learns to generate superior architectures throughout the search process.

### 5.2 Architectural Design Patterns

To understand the architectural preferences of LLMs during the search process which can provide insights into how these models approach the design space, we analyze both the complexity trends and component preferences.

#### Model Complexity Stability

A fundamental concern in neural architecture search is whether performance improvements come from simply increasing model size. We use parameter count as a proxy for model complexity to examine this issue. Figure 8 shows the distribution of parameter counts across iterations. The data reveals that while early iterations predominantly generate models in the 400-600M parameter range, the system quickly diversifies to explore models between 600-800M parameters. Importantly, after this initial exploration phase, the parameter distribution remains stable without systematic growth. The majority of architectures consistently fall within the 400-600M range throughout the search process, with no trend toward increasingly complex models. This stability demonstrates that ASI-Arch does not exploit complex component stacking as a simple strategy for performance improvement, maintaining architectural discipline even without explicit parameter constraints.

#### Architectural Component Preferences

To understand the LLM’s underlying design strategy, we performed a fine-grained analysis of the architectural components it chose to modify. We employed a separate Large Language Model to parse every motivation generated by the system, identifying which specific model components were targeted for modification in each step. This process yielded approximately 5,000 component instances, which we then manually curated and grouped into 40 high-level categories. We then statistically compared the proportional usage of these categories within our high-performing model gallery against that of the remaining models. This comparative analysis, visualized in Figure 7 , reveals two key insights into our LLM-driven design process. First, ASI-Arch shows a clear preference for established architectural components like gating mechanisms and convolutions, while less common ones like physics-inspired mechanisms appear infrequently, likely reflecting biases in the training literature. Second, and more revealingly, the model gallery exhibits a significantly less pronounced long-tail distribution in its component usage. This indicates that while the system explores many novel components, the top-performing models converge on a core set of validated and effective techniques. This mirrors the typical methodology of human scientists: achieving state-of-the-art results by primarily iterating and innovating upon a foundation of proven technologies, rather than pursuing novelty for its own sake.

### 5.3 Where Do Good Designs Come From?

To guide the future development of more efficient and adaptive frameworks, it is crucial to understand which components of ASI-Arch exert the most significant influence on model architecture design. Our system’s design process is constrained by its inputs: for each new architecture, the model’s context is strictly limited to the motivation, program, experiment result, analysis, and cognition sections of five historical experiment records drawn from the candidate pool. Given this bounded context, we can posit that any new design inspiration must originate from one of only three channels: knowledge distilled from human expert literature (which we term cognition), patterns identified through the analysis and summary of its related historical experiments (analysis), or novel ideas generated by the model itself (original). To quantify the contributions of these three channels, we designed an experiment to trace the provenance of each design idea. We prompted a LLM, acting as an impartial evaluator, to classify each architectural component (as identified in our prior motivation analysis) by its most likely origin, classifying it as derived from cognition, analysis, or as an original idea.

The results, presented in Table 5.3 , reveal a compelling two-fold pattern. Across the entire population of generated architectures, a majority of design ideas originate from the cognition phase, indicating a baseline reliance on direct, prior examples. However, a significant shift is observed when we focus exclusively on the model gallery. For these top-performing architectures, the proportion of design components attributed to the analysis phase increases markedly. This finding suggests a crucial parallel to human scientific progress: while competency can be built upon direct experience, achieving true excellence requires a deeper, more abstract level of understanding. It proves that for an AI to produce breakthrough results, it cannot merely reuse past successes (a reliance on cognition). Instead, it must engage in a process of exploration, summary, and discovery (a reliance on analysis) to synthesize novel and superior solutions.

## Discussion and Future Work

Our work successfully demonstrates a framework for AI self-optimization, where an autonomous agent can iteratively discover and refine novel neural architectures. The primary focus of this study was to establish the viability of this methodology—proving that an AI can navigate a complex design space to achieve state-of-the-art performance. Our findings open up several promising directions for future research.

#### Multi-Architecture Initialization

Our current approach initializes the search from a single, strong baseline (DeltaNet). This was a deliberate methodological choice, providing a clear objective and a stable foundation to drive continuous improvement, which is crucial in the early stages of exploring such a framework. A natural and exciting extension would be to initialize the process with a diverse portfolio of architectures simultaneously. This would not only test the framework’s ability to manage a more complex, multi-modal search but could also lead to the discovery of entirely new families of architectures. Such an endeavor would, however, demand a significant increase in computational resources and time.

#### Component-wise Analysis

Our experiments validate the effectiveness of our pipeline as a cohesive whole. Due to the substantial resources required for each design iteration, we did not perform a fine-grained ablation study to isolate the contribution of each component within the framework. A crucial avenue for future work is to dissect the pipeline from multiple angles to better understand the interplay and individual importance of its parts, such as the “cognition” and “analysis” modules. This would enable a more targeted optimization of the framework, potentially leading to even greater efficiency and creativity.

#### Engineering Optimization

The core contribution of this paper lies in the design of the AI-for-AI framework itself, with an emphasis on architectural innovation and performance. Consequently, we did not extend our work to include the labor-intensive task of writing custom accelerated kernels (e.g., using Triton) for the newly discovered architectures. As a result, a direct comparison of their computational efficiency is not provided. A critical next step, particularly for transitioning these designs from research to practice, would be to focus on this engineering aspect. Benchmarking the efficiency and latency of these models would be an invaluable follow-up study and would complete the cycle from automated discovery to practical deployment.

## References

Agrawal et al. (2018) Ajay Agrawal, Joshua Gans, and Avi Goldfarb. 2018. Prediction Machines: The Simple Economics of Artificial Intelligence . Harvard Business Press.

Ahmed et al. (2022) N’Daye Ahmed, Maliha Wahed, and N. C. Thompson. 2022. Modeling the ai-research ecosystem: A study of the circulation of scientific knowledge and talent. Research Policy , 51(5):104505.

Amodei et al. (2016) Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. 2016. Concrete problems in ai safety. arXiv preprint arXiv:1606.06565 .

Baum (2004) Eric B. Baum. 2004. What is Thought? The MIT Press.

Boiko et al. (2023) Daniil A Boiko, Robert MacKnight, Gabe Gomes, and Adam Funke. 2023. Autonomous chemical research with large language models. Nature , 624(7992):570–576.

Brown et al. (2020) Tom B Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020. Language models are few-shot learners. arXiv preprint arXiv:2005.14165 .

Brynjolfsson and Mitchell (2017) Erik Brynjolfsson and Tom Mitchell. 2017. What can machine learning do? workforce implications. Science , 358(6370):1530–1534.

Chen et al. (2023) Shidong Chen, Zhaofei Li, Boyu Du, and Hu Li. 2023. Llmatic: A generative llm for neural architecture search. arXiv preprint arXiv:2312.01633 .

Cheng et al. (2025) Junyan Cheng, Peter Clark, and Kyle Richardson. 2025. Language modeling by language models. arXiv preprint arXiv:2506.20249 .

Chervonyi et al. (2025) Yuri Chervonyi, Trieu H. Trinh, Miroslav Olšák, Xiaomeng Yang, Hoang Nguyen, Marcelo Menegali, Junehyuk Jung, Vikas Verma, Quoc V. Le, and Thang Luong. 2025. Gold-medalist performance in solving olympiad geometry with alphageometry2 .

Choromanski et al. (2020) Krzysztof Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamas Sarlos, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, et al. 2020. Rethinking attention with performers. arXiv preprint arXiv:2009.14794 .

Dao and Gu (2024) Tri Dao and Albert Gu. 2024. Transformers are ssms: Generalized models and efficient algorithms through structured state space duality. arXiv preprint arXiv:2405.21060 .

DeepSeek-AI et al. (2024) DeepSeek-AI, Aixin Liu, Bei Feng, Bin Wang, Bingxuan Wang, Bo Liu, Chenggang Zhao, Chengqi Dengr, Chong Ruan, Damai Dai, Daya Guo, Dejian Yang, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Hanwei Xu, Hao Yang, Haowei Zhang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Li, Hui Qu, J. L. Cai, Jian Liang, Jianzhong Guo, Jiaqi Ni, Jiashi Li, Jin Chen, Jingyang Yuan, Junjie Qiu, Junxiao Song, Kai Dong, Kaige Gao, Kang Guan, Lean Wang, Lecong Zhang, Lei Xu, Leyi Xia, Liang Zhao, Liyue Zhang, Meng Li, Miaojun Wang, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Mingming Li, Ning Tian, Panpan Huang, Peiyi Wang, Peng Zhang, Qihao Zhu, Qinyu Chen, Qiushi Du, R. J. Chen, R. L. Jin, Ruiqi Ge, Ruizhe Pan, Runxin Xu, Ruyi Chen, S. S. Li, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shaoqing Wu, Shengfeng Ye, Shirong Ma, Shiyu Wang, Shuang Zhou, Shuiping Yu, Shunfeng Zhou, Size Zheng, T. Wang, Tian Pei, Tian Yuan, Tianyu Sun, W. L. Xiao, Wangding Zeng, Wei An, Wen Liu, Wenfeng Liang, Wenjun Gao, Wentao Zhang, X. Q. Li, Xiangyue Jin, Xianzu Wang, Xiao Bi, Xiaodong Liu, Xiaohan Wang, Xiaojin Shen, Xiaokang Chen, Xiaosha Chen, Xiaotao Nie, Xiaowen Sun, Xiaoxiang Wang, Xin Liu, Xin Xie, Xingkai Yu, Xinnan Song, Xinyi Zhou, Xinyu Yang, Xuan Lu, Xuecheng Su, Y. Wu, Y. K. Li, Y. X. Wei, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Li, Yaohui Wang, Yi Zheng, Yichao Zhang, Yiliang Xiong, Yilong Zhao, Ying He, Ying Tang, Yishi Piao, Yixin Dong, Yixuan Tan, Yiyuan Liu, Yongji Wang, Yongqiang Guo, Yuchen Zhu, Yuduan Wang, Yuheng Zou, Yukun Zha, Yunxian Ma, Yuting Yan, Yuxiang You, Yuxuan Liu, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhen Huang, Zhen Zhang, Zhenda Xie, Zhewen Hao, Zhihong Shao, Zhiniu Wen, Zhipeng Xu, Zhongyu Zhang, Zhuoshu Li, Zihan Wang, Zihui Gu, Zilin Li, and Ziwei Xie. 2024. Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model .

Elsken et al. (2019) Thomas Elsken, Jan Hendrik Metzen, and Frank Hutter. 2019. Neural architecture search: A survey. Journal of Machine Learning Research , 20(55):1–21.

Gu and Dao (2023) Albert Gu and Tri Dao. 2023. Mamba: Linear-time sequence modeling with selective state spaces. arXiv preprint arXiv:2312.00752 .

Katharopoulos et al. (2020) Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and François Fleuret. 2020. Transformers are rnns: Fast autoregressive transformers with linear attention. In International conference on machine learning , pages 5156–5165. PMLR.

Kokotajlo et al. (2025) D. Kokotajlo, S. Alexander, T. Larsen, E. Lifland, and R. Dean. 2025. Ai 2027.

LeCun et al. (1995) Yann LeCun, Yoshua Bengio, et al. 1995. Convolutional networks for images, speech, and time series. The handbook of brain theory and neural networks , 3361(10):1995.

Li et al. (2022) Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Pogodin, Oriol Vinyals, et al. 2022. Competition-level code generation with alphacode. Science , 378(6624):1092–1097.

Lieber et al. (2024) Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Jhonathan Osin, Itay Dalmedigos, Erez Safahi, Shaked Meirom, Yonatan Belinkov, Shai Shalev-Shwartz, et al. 2024. Jamba: A hybrid transformer-mamba language model. arXiv preprint arXiv:2403.19887 .

MiniMax et al. (2025) MiniMax, :, Aili Chen, Aonian Li, Bangwei Gong, Binyang Jiang, Bo Fei, Bo Yang, Boji Shan, Changqing Yu, Chao Wang, Cheng Zhu, Chengjun Xiao, Chengyu Du, Chi Zhang, Chu Qiao, Chunhao Zhang, Chunhui Du, Congchao Guo, Da Chen, Deming Ding, Dianjun Sun, Dong Li, Enwei Jiao, Haigang Zhou, Haimo Zhang, Han Ding, Haohai Sun, Haoyu Feng, Huaiguang Cai, Haichao Zhu, Jian Sun, Jiaqi Zhuang, Jiaren Cai, Jiayuan Song, Jin Zhu, Jingyang Li, Jinhao Tian, Jinli Liu, Junhao Xu, Junjie Yan, Junteng Liu, Junxian He, Kaiyi Feng, Ke Yang, Kecheng Xiao, Le Han, Leyang Wang, Lianfei Yu, Liheng Feng, Lin Li, Lin Zheng, Linge Du, Lingyu Yang, Lunbin Zeng, Minghui Yu, Mingliang Tao, Mingyuan Chi, Mozhi Zhang, Mujie Lin, Nan Hu, Nongyu Di, Peng Gao, Pengfei Li, Pengyu Zhao, Qibing Ren, Qidi Xu, Qile Li, Qin Wang, Rong Tian, Ruitao Leng, Shaoxiang Chen, Shaoyu Chen, Shengmin Shi, Shitong Weng, Shuchang Guan, Shuqi Yu, Sichen Li, Songquan Zhu, Tengfei Li, Tianchi Cai, Tianrun Liang, Weiyu Cheng, Weize Kong, Wenkai Li, Xiancai Chen, Xiangjun Song, Xiao Luo, Xiao Su, Xiaobo Li, Xiaodong Han, Xinzhu Hou, Xuan Lu, Xun Zou, Xuyang Shen, Yan Gong, Yan Ma, Yang Wang, Yiqi Shi, Yiran Zhong, Yonghong Duan, Yongxiang Fu, Yongyi Hu, Yu Gao, Yuanxiang Fan, Yufeng Yang, Yuhao Li, Yulin Hu, Yunan Huang, Yunji Li, Yunzhi Xu, Yuxin Mao, Yuxuan Shi, Yuze Wenren, Zehan Li, Zelin Li, Zhanxu Tian, Zhengmao Zhu, Zhenhua Fan, Zhenzhen Wu, Zhichao Xu, Zhihang Yu, Zhiheng Lyu, Zhuo Jiang, Zibo Gao, Zijia Wu, Zijian Song, and Zijun Sun. 2025. Minimax-m1: Scaling test-time compute efficiently with lightning attention .

Novikov et al. (2025) Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco JR Ruiz, Abbas Mehrabian, et al. 2025. Alphaevolve: A coding agent for scientific and algorithmic discovery. arXiv preprint arXiv:2506.13131 .

OpenAI (2023) OpenAI. 2023. Gpt-4 technical report. techreport arXiv:2303.08774, OpenAI.

Peng et al. (2023) Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Stella Biderman, Huanqi Cao, Xin Cheng, Michael Chung, Matteo Grella, et al. 2023. Rwkv: Reinventing rnns for the transformer era. arXiv preprint arXiv:2305.13048 .

Qin et al. (2024a) Zhen Qin, Weigao Sun, Dong Li, Xuyang Shen, Weixuan Sun, and Yiran Zhong. 2024a. Lightning attention-2: A free lunch for handling unlimited sequence lengths in large language models. arXiv preprint arXiv:2401.04658 .

Qin et al. (2022) Zhen Qin, Weixuan Sun, Hui Deng, Dongxu Li, Yunshen Wei, Baohong Lv, Junjie Yan, Lingpeng Kong, and Yiran Zhong. 2022. cosformer: Rethinking softmax in attention. arXiv preprint arXiv:2202.08791 .

Qin et al. (2024b) Zhen Qin, Songlin Yang, Weixuan Sun, Xuyang Shen, Dong Li, Weigao Sun, and Yiran Zhong. 2024b. Hgrn2: Gated linear rnns with state expansion. arXiv preprint arXiv:2404.07904 .

Qin et al. (2023) Zhen Qin, Songlin Yang, and Yiran Zhong. 2023. Hierarchically gated recurrent neural network for sequence modeling. Advances in Neural Information Processing Systems , 36:33202–33221.

Real et al. (2017) Esteban Real, Sherry Moore, Andrew Selle, Saurabh Saxena, Yutaka L Suematsu, Jie Tan, Quoc V Le, and Alex Kurakin. 2017. Large-scale evolution of image classifiers. In International conference on machine learning , pages 2902–2911. PMLR.

Russell and Norvig (2010) Stuart J. Russell and Peter Norvig. 2010. Artificial intelligence: a modern approach . Prentice Hall.

Schmidhuber (1997) Jürgen Schmidhuber. 1997. A computer scientist’s view of life, the universe, and everything. Lecture Notes in Computer Science , 1337:201–208.

Sevilla et al. (2022) Jaime Sevilla, Lennart Heim, Anson Ho, Tamay Besiroglu, Marius Hobbhahn, and Pablo Villalobos. 2022. Compute trends across three eras of machine learning. arXiv preprint arXiv:2202.05924 .

Tay et al. (2022) Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Metzler. 2022. Efficient transformers: A survey. ACM Computing Surveys (CSUR) , 55(6):1–28.

The White House (2023) The White House. 2023. Ai talent: A report on the workforce needs for a booming artificial intelligence industry . Technical report, The White House Office of Science and Technology Policy.

Trinh et al. (2024) Trieu H. Trinh, Yuhuai Wu, Quoc V. Le, He He, and Thang Luong. 2024. Solving olympiad geometry without human demonstrations . Nature , 625(7995):476–482.

Tshitoyan et al. (2019) Vahe Tshitoyan, John Dagdelen, Leigh Weston, Alexander Dunn, Ziqin Rong, Olga Kononova, Kristin A Persson, Gerbrand Ceder, and Anubhav Jain. 2019. Unsupervised word embeddings capture latent knowledge from materials science literature. Nature , 571(7763):95–98.

Vaswani et al. (2017) Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. Advances in neural information processing systems , 30.

Wang et al. (2020) Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. 2020. Linformer: Self-attention with linear complexity. arXiv preprint arXiv:2006.04768 .

Yang et al. (2024a) Songlin Yang, Jan Kautz, and Ali Hatamizadeh. 2024a. Gated delta networks: Improving mamba2 with delta rule. arXiv preprint arXiv:2412.06464 .

Yang et al. (2024b) Songlin Yang, Bailin Wang, Yu Zhang, Yikang Shen, and Yoon Kim. 2024b. Parallelizing linear transformers with the delta rule over sequence length. Advances in neural information processing systems , 37:115491–115522.

Yuan et al. (2025) Jingyang Yuan, Huazuo Gao, Damai Dai, Junyu Luo, Liang Zhao, Zhengyan Zhang, Zhenda Xie, Y. X. Wei, Lean Wang, Zhiping Xiao, Yuqing Wang, Chong Ruan, Ming Zhang, Wenfeng Liang, and Wangding Zeng. 2025. Native sparse attention: Hardware-aligned and natively trainable sparse attention .

Zhang et al. (2025) Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune. 2025. Darwin godel machine: Open-ended evolution of self-improving agents . ArXiv , abs/2505.22954.

Zhang et al. (2024) Ruocheng Zhang, Jiaxin Li, Zhaoning Liu, James A. Evans, Jeff Clune, and Diyi Ho. 2024. Large language models for science: A study on the state of the art. arXiv preprint arXiv:2402.16912 .

Zoph and Le (2016) Barret Zoph and Quoc V Le. 2016. Neural architecture search with reinforcement learning. arXiv preprint arXiv:1611.01578 .

## Appendix A Experimental Setup

### A.1 Pipeline Configuration

#### Framework Overview

Our experimental framework implements an automated AI self-iterative system for exploring novel neural network architectures through three core phases: Evolve, Training, and Analysis. The system operates cyclically, extracting nodes from a MongoDB database, generating new motivations and implementations, conducting training and evaluation, and performing comprehensive analysis with knowledge integration.

#### Multi-Model Integration

We employ a hybrid multi-model approach to optimize both quality and efficiency. In the Evolve phase, we combine O3 and GPT-4.1 models for the planner component to balance motivation quality and generation speed while enhancing architectural diversity. The checker component utilizes O3 to ensure code validity and prevent resource waste, while motivation deduplication employs GPT-4.1 for rapid processing. During the Training phase, GPT-4.1 handles training initiation, testing, and debugging operations, focusing on detail-level modifications without structural changes for rapid iteration capabilities. The Analysis phase utilizes O3 to conduct comprehensive experimental analysis, providing high-quality insights to enhance subsequent exploration efficiency.

#### Data Management and Retrieval

For data management and retrieval, MongoDB serves as our primary storage solution, supporting name-based and sequential storage along with deletion functionality for experimental nodes. FAISS enables efficient similarity matching during motivation deduplication, identifying similar concepts in the database before agent-based verification to improve exploration efficiency. We extract cognitive insights from relevant literature and employ OpenSearch for RAG-based retrieval. For each experimental result, we extract the three most similar cognitive entries, integrating them into the experimental node for enhanced future exploration.

### A.2 Experimental Configuration

#### Progressive Evaluation Strategy

To balance exploration efficiency with computational constraints, we implement a three-tiered progressive evaluation approach with rapid architecture exploration using 20M parameter models, followed by validation phases at larger scales.

#### Model Architecture

The base 20M configuration employs 8 attention heads across 8 hidden layers with a hidden dimension of 256, maintaining computational tractability while preserving architectural expressiveness. The model uses SiLU activation for query-key transformations with L2 normalization and incorporates short convolutions with a kernel size of 4. For comparison, 340M parameter models employ 1024 hidden size, 8 attention heads, and 24 hidden layers with tied word embeddings disabled.

#### Training Protocol

We utilize the FLAME framework with AdamW optimization, employing a peak learning rate of 3 ​ × ​ 10 − 4 3×10^{-4} , epsilon value of 1 ​ × ​ 10 − 8 1×10^{-8} , and a warmup-stabilize-decay (WSD) learning rate schedule. Training proceeds for 2000 steps with 1000 warmup steps for 20M models, using mixed precision training with bfloat16 parameters and float32 gradient reduction. All models maintain a consistent batch size of 256 and employ GPT-2 tokenizer throughout training and evaluation phases.

#### Data Configuration

Training utilizes FinewWeb-edu sample-10BT and sample-100BT datasets with a context length of 2048 tokens. For comprehensive evaluation of discovered architectures, we scale to 340M parameter models that provide more reliable performance assessment. The 340M models are trained using 15 billion tokens, employing the same cosine learning rate schedule with a warm-up phase of 0.5 billion tokens, maintaining identical training hyperparameters to ensure consistent evaluation.

#### Evaluation Protocol

Model evaluation employs the LM-Evaluation-Harness framework, a standardized open-source tool developed by EleutherAI that provides unified benchmarking protocols for language models. The evaluation suite encompasses diverse cognitive capabilities including reading comprehension (LAMBADA, SQuAD), commonsense reasoning (HellaSwag, PIQA), knowledge-intensive tasks (ARC-Challenge, ARC-Easy, OpenBookQA), boolean question answering (BoolQ), and additional benchmarks (FDA, Social-IQA, SWDE, WinoGrande). During rapid exploration phase, we limit samples to 500 per dataset for 20M parameter models to accelerate architectural search, while validation phases utilize full datasets. All evaluations are conducted using consistent hyperparameters and random seeds to ensure reproducible comparisons across architectural variants. Final ranking incorporates LLM subjective evaluation, training loss metrics, and benchmark performance for comprehensive model assessment.

## Appendix B Prompts

### B.1 Planner

### B.2 Checker

### B.3 Debugger

### B.4 Analyser

### B.5 Cognition

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
